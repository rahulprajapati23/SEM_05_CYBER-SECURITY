
import os
import re

# Command Knowledge Base for IBM SDS
COMMAND_DB = [
    # Creating Instances
    {
        "pattern": r"Create.*instance.*idsldap1.*idsicrt",
        "cmd": "idsicrt -I idsldap1 -e encryptionseed -l /home/idsldap1 -n"
    },
    {
        "pattern": r"Create.*instance.*idsldap2.*idsicrt",
        "cmd": "idsicrt -I idsldap2 -e encryptionseed -l /home/idsldap2 -n"
    },
    # Configuring Database
    {
        "pattern": r"configure.*DB2.*idsldap1",
        "cmd": "idscfgdb -I idsldap1 -a idsldap1 -w password -t idsldap1 -l /home/idsldap1"
    },
    {
        "pattern": r"configure.*DB2.*idsldap2",
        "cmd": "idscfgdb -I idsldap2 -a idsldap2 -w password -t idsldap2 -l /home/idsldap2"
    },
    # Starting/Stopping
    {
        "pattern": r"Start.*idsldap1",
        "cmd": "ibmslapd -I idsldap1"
    },
    {
        "pattern": r"Start.*idsldap2",
        "cmd": "ibmslapd -I idsldap2"
    },
    {
        "pattern": r"stop.*idsldap1",
        "cmd": "ibmslapd -I idsldap1 -k"
    },
    {
        "pattern": r"stop.*idsldap2",
        "cmd": "ibmslapd -I idsldap2 -k"
    },
    # Suffix
    {
        "pattern": r"add.*base suffix",
        "cmd": "idscfgsuf -I idsldap1 -s \"o=jke\" && idscfgsuf -I idsldap2 -s \"o=jke\""
    },
    # LDIF
    {
        "pattern": r"import.*idsldapadd.*idsldap1",
        "cmd": "idsldapadd -p 389 -D cn=root -w P@ssw0rd -f User1.ldif"
    },
     {
        "pattern": r"import.*idsldapadd.*idsldap2",
        "cmd": "idsldapadd -p 2389 -D cn=root -w P@ssw0rd -f User2.ldif"
    },
    # LDAP Searches (IAM Exercises)
    {
        "pattern": r"find.*attributes.*Bob Smith",
        "cmd": "ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"dc=com\" \"cn=Bob Smith\""
    },
    {
        "pattern": r"find.*email.*Sue Thomas",
        "cmd": "ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"dc=com\" \"cn=Sue Thomas\" mail"
    },
    {
        "pattern": r"find.*children.*JKE organization",
        "cmd": "ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"o=jke\" \"objectclass=*\""
    },
    {
        "pattern": r"find.*manager.*title",
        "cmd": "ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"dc=com\" \"title=*manager*\""
    }
]

def parse_markdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    exercises = []
    
    current_exercise = {
        "title": os.path.splitext(os.path.basename(md_path))[0],
        "steps": [],
        "fields": []
    }
    
    for line in lines:
        line = line.strip()
        
        # Heuristic for Exercise Header in Table
        exercise_match = re.search(r'\|\s*[\d\.]+\s*\|\s*(Exercise\s+\d+.*?)\s*\|', line, re.IGNORECASE)
        if exercise_match:
            exercises.append(current_exercise)
            current_exercise = {
                "title": exercise_match.group(1).replace('|','').strip(),
                "steps": [],
                "fields": []
            }
            continue

        if line.startswith("- "):
            step_text = line[2:].strip()
            current_exercise["steps"].append(step_text)
            continue
            
        if line.startswith("|") and not line.startswith("|---"):
            parts = [p.strip() for p in line.split('|') if p.strip()]
            
            if len(parts) >= 2 and re.match(r'^\d+[\.:]?$', parts[0]):
                 step_desc = parts[1]
                 current_exercise["steps"].append(f"{parts[0]} {step_desc}")
                 continue
            
            if "Field" in parts and "Value" in parts:
                continue
                
            if len(parts) >= 2:
                field_name = parts[0]
                field_val = parts[1]
                if "Page" in field_name and len(parts) == 2:
                     continue 
                current_exercise["fields"].append((field_name, field_val))
                
    exercises.append(current_exercise)
    return exercises

def generate_script_content(exercise_data):
    title = exercise_data["title"]
    steps = exercise_data["steps"]
    fields = exercise_data["fields"]
    
    safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    
    script = f'"""\nInteractive Guide for: {title}\n"""\n'
    script += 'import time\nimport os\nimport re\n'
    script += 'from selenium import webdriver\n'
    script += 'from selenium.webdriver.common.by import By\n'
    script += 'from selenium.webdriver.common.keys import Keys\n\n'
    
    script += 'def print_step(msg):\n'
    script += '    print(f"\\n[STEP] {msg}")\n\n'
    
    script += 'def get_input(field, suggested):\n'
    script += '    print(f"\\n[INPUT] Field: {field}")\n'
    script += '    val = input(f"Enter value (Suggested: {suggested}): ")\n'
    script += '    return val if val.strip() else suggested\n\n'
    
    script += 'def run_command(desc, auto_cmd=None):\n'
    script += '    print(f"\\n[ACTION] Command required for: {desc}")\n'
    script += '    if auto_cmd:\n'
    script += '        print(f"Auto-executing known command: {auto_cmd}")\n'
    script += '        try:\n'
    script += '             os.system(auto_cmd)\n'
    script += '             print("Execution finished.")\n'
    script += '        except Exception as e:\n'
    script += '             print(f"Error executing: {e}")\n'
    script += '    else:\n'
    script += '        # User requested NO PROMPTS. Just display the instruction.\n'
    script += '        print("(No automated command matched. Please execute manually if required.)")\n\n'

    script += 'class WebBot:\n'
    script += '    def __init__(self):\n'
    script += '        print("Initializing Browser for Web Automation (Firefox)...")\n'
    script += '        try:\n'
    script += '            self.driver = webdriver.Firefox() # Assumes geckodriver is in PATH\n'
    script += '        except Exception as e:\n'
    script += '            print(f"Warning: Firefox driver (geckodriver) not found. Web automation skipped. Error: {e}")\n'
    script += '            self.driver = None\n\n'
    script += '    def try_action(self, step_text):\n'
    script += '        if not self.driver: return\n'
    script += '        step_lower = step_text.lower()\n'
    script += '        try:\n'
    script += '            if "log in" in step_lower or "login" in step_lower:\n'
    script += '                 print("Attempting to find Login fields...")\n'
    script += '                 # Generic login attempt\n'
    script += '                 try:\n'
    script += '                     self.driver.find_element(By.NAME, "j_username").send_keys("system")\n'
    script += '                     self.driver.find_element(By.NAME, "j_password").send_keys("secret")\n'
    script += '                 except: pass\n'
    script += '            elif "click" in step_lower:\n'
    script += '                 # Extract quoted text or prominent words\n'
    script += '                 match = re.search(r"Click\s+([A-Za-z0-9\s]+)", step_text, re.IGNORECASE)\n'
    script += '                 target = match.group(1).strip() if match else None\n'
    script += '                 if target:\n'
    script += '                     print(f"Attempting to Click: {target}")\n'
    script += '                     # Try generic xpath by text\n'
    script += '                     el = self.driver.find_element(By.XPATH, f"//*[contains(text(), \'{target}\')]")\n'
    script += '                     el.click()\n'
    script += '            elif "enter" in step_lower or "type" in step_lower:\n'
    script += '                 # Input attempt\n'
    script += '                 pass\n'
    script += '        except Exception as e:\n'
    script += '            print(f"Web Action Failed (Expected, as this is heuristic): {e}")\n\n'

    script += 'def main():\n'
    script += f'    print("=== STARTING EXERCISE: {title} ===")\n'
    script += '    web_bot = WebBot()\n'
    
    if steps:
        script += '    print("\\n--- INSTRUCTIONS ---")\n'
        for s in steps:
            s_esc = s.replace('"', '\\"')
            s_clean = s.replace('"', '') 
            
            # Check DB
            found_cmd = None
            for item in COMMAND_DB:
                if re.search(item["pattern"], s_clean, re.IGNORECASE):
                    found_cmd = item["cmd"]
                    break
            
            script += f'    print_step("{s_esc}")\n'
            
            if found_cmd:
                 cmd_esc = found_cmd.replace('"', '\\"')
                 script += f'    run_command("{s_esc}", auto_cmd="{cmd_esc}")\n'
            else:
                 # Check for generic command words vs web words
                 if "command" in s.lower() or "terminal" in s.lower():
                      script += f'    run_command("{s_esc}")\n'
                 else:
                      # Attempt Web Action
                      script += f'    web_bot.try_action("{s_esc}")\n'
            
    if fields:
        script += '    print("\\n--- DATA ENTRY REQUIRED ---")\n'
        for f, v in fields:
            f_esc = f.replace('"', '\\"')
            v_esc = v.replace('"', '\\"')
            script += f'    val = get_input("{f_esc}", "{v_esc}")\n'
            # Try to start filling logic if driver is up?
            # script += f'    # web_bot.fill_field("{f_esc}", val)\n'
            
    script += '    print("\\n=== EXERCISE COMPLETED SUCCESSFULLY === ")\n'
    script += '\nif __name__ == "__main__":\n'
    script += '    main()\n'
    
    return safe_title, script

def main():
    folder = "."
    md_files = [f for f in os.listdir(folder) if f.lower().endswith('.md')]
    
    for md_file in md_files:
        print(f"Processing {md_file}...")
        exercises = parse_markdown(md_file)
        
        base_name = os.path.splitext(md_file)[0]
        target_dir = os.path.join(folder, base_name)
        os.makedirs(target_dir, exist_ok=True)
        
        for i, ex in enumerate(exercises):
            if not ex["steps"] and not ex["fields"]:
                continue
                
            safe_title, script_content = generate_script_content(ex)
            filename = f"{i+1:02d}_{safe_title}.py"
            full_path = os.path.join(target_dir, filename)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            print(f"  Generated {full_path}")

if __name__ == "__main__":
    main()
