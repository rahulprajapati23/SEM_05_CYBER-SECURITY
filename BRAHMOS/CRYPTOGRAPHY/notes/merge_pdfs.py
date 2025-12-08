import os
import re
from pypdf import PdfWriter

SOURCE_DIR = r"c:\Users\Hp\OneDrive\Desktop\SEM_05\BRAHMOS\CRYPTOGRAPHY\notes"
OUTPUT_FILE = os.path.join(SOURCE_DIR, "All_Lectures_Merged.pdf")

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def merge_pdfs():
    print("Scanning for PDFs...")
    files = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith('.pdf')]
    
    # Exclude the output file itself to avoid loop
    if "All_Lectures_Merged.pdf" in files:
        files.remove("All_Lectures_Merged.pdf")
        
    # Ask about Stallings? We'll exclude it if it's huge, or just merge everything.
    # Usually users want the notes merged. Stallings is 15MB.
    # Let's include everything but put Stallings *last* or *first*?
    # Actually, natural sort might put "Cryptography...Stallings" somewhere in the middle (starts with C).
    # Lecture_1 starts with L.
    
    # Let's separates "Lectures" from "Textbooks"
    lectures = []
    others = []
    
    for f in files:
        if "stallings" in f.lower():
            print(f"Skipping textbook: {f}")
            continue
        else:
            lectures.append(f)
            
    lectures.sort(key=natural_sort_key)
    
    # Merge Sequence: Only Lectures
    sorted_files = lectures
    
    print(f"Merging {len(sorted_files)} files in this order:")
    for f in sorted_files:
        print(f" - {f}")

    merger = PdfWriter()

    for filename in sorted_files:
        path = os.path.join(SOURCE_DIR, filename)
        try:
            merger.append(path)
        except Exception as e:
            print(f"Error appending {filename}: {e}")

    print(f"Writing to {OUTPUT_FILE}...")
    merger.write(OUTPUT_FILE)
    merger.close()
    print("Success!")

if __name__ == "__main__":
    merge_pdfs()
