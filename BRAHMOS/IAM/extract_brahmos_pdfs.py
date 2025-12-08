
import os
import re
from pypdf import PdfReader

def extract_content(pdf_path):
    reader = PdfReader(pdf_path)
    content = {
        "exercise_name": os.path.splitext(os.path.basename(pdf_path))[0],
        "steps": [],
        "fields": []
    }

    full_text = ""
    for page in reader.pages:
        try:
            full_text += page.extract_text(extraction_mode="layout") + "\n"
        except:
            full_text += page.extract_text() + "\n"

    lines = full_text.split('\n')
    
    current_section = None # 'steps', 'fields'
    
    # Heuristic: We'll parse line by line
    # If we see numbers like "1. ", "2. ", we assume Steps.
    # If we see "Field" and "Value" broadly on a line, we assume Fields section starts.
    
    field_section_active = False

    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue

        # Check for Field header
        if re.search(r'Field\s+Value', line, re.IGNORECASE) or re.search(r'Attribute\s+Value', line, re.IGNORECASE):
            field_section_active = True
            continue 

        # Check for Step (1. or a) )
        step_match = re.match(r'^(\d+\.|[a-z]\))\s+(.*)', line_clean)
        
        if field_section_active:
            # If it looks like a step, maybe field section ended?
            # But sometimes steps have fields inside. 
            # Let's see if it looks like a field-value pair (two chunks text separated by spaces)
            parts = re.split(r'\s{3,}', line_clean)
            if len(parts) >= 2:
                content["fields"].append((parts[0], parts[1]))
            elif step_match:
                 # Back to steps? Or step inside field instructions? 
                 # Let's count it as a step if we found one
                 content["steps"].append(line_clean)
                 # Don't disable field_section_active immediately unless it's clearly a high level step?
                 # For safety, let's just also add it as step.
            else:
                # Text in field section?
                pass
        else:
            if step_match:
                content["steps"].append(line_clean)
            elif re.search(r'\s{3,}', line_clean) and len(re.split(r'\s{3,}', line_clean)) >= 2:
                 # Might be a field even without header detected earlier?
                 # No, explicit instruction was "IF THERE IS ANY FIELDS". Safer to risk missing than hallucinating.
                 # But the provided PDF was messy.
                 pass

    return content

def save_to_markdown(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {content['exercise_name']}\n\n")
        
        if content['steps']:
            f.write("## Steps\n")
            for step in content['steps']:
                f.write(f"- {step}\n")
            f.write("\n")
            
        if content['fields']:
            f.write("## Fields and Values\n")
            f.write("| Field | Value |\n")
            f.write("|---|---|\n")
            for field, value in content['fields']:
                f.write(f"| {field} | {value} |\n")
            f.write("\n")
        elif not content['fields']:
             # If no fields were found by strict logic, let's try a fallback or just leave empty?
             # User said: "IF THERE IS ANY FIELDS THEN I WANT BOTH FIELDS AND VALUES"
             pass

def main():
    folder = "."
    files = [f for f in os.listdir(folder) if f.lower().endswith('.pdf')]
    
    print(f"Found {len(files)} PDF files.")

    for filename in files:
        print(f"Processing {filename}...")
        try:
            content = extract_content(filename)
            md_filename = os.path.splitext(filename)[0] + ".md"
            save_to_markdown(content, md_filename)
            print(f"Saved {md_filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    main()
