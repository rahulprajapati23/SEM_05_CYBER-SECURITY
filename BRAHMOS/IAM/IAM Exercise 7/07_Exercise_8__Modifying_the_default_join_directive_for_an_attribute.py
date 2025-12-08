"""
Interactive Guide for: Exercise 8 – Modifying the default join directive for an attribute
"""
import time
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def print_step(msg):
    print(f"\n[STEP] {msg}")

def get_input(field, suggested):
    print(f"\n[INPUT] Field: {field}")
    val = input(f"Enter value (Suggested: {suggested}): ")
    return val if val.strip() else suggested

def run_command(desc, auto_cmd=None):
    print(f"\n[ACTION] Command required for: {desc}")
    if auto_cmd:
        print(f"Auto-executing known command: {auto_cmd}")
        try:
             os.system(auto_cmd)
             print("Execution finished.")
        except Exception as e:
             print(f"Error executing: {e}")
    else:
        # User requested NO PROMPTS. Just display the instruction.
        print("(No automated command matched. Please execute manually if required.)")

class WebBot:
    def __init__(self):
        print("Initializing Browser for Web Automation (Firefox)...")
        try:
            self.driver = webdriver.Firefox() # Assumes geckodriver is in PATH
        except Exception as e:
            print(f"Warning: Firefox driver (geckodriver) not found. Web automation skipped. Error: {e}")
            self.driver = None

    def try_action(self, step_text):
        if not self.driver: return
        step_lower = step_text.lower()
        try:
            if "log in" in step_lower or "login" in step_lower:
                 print("Attempting to find Login fields...")
                 # Generic login attempt
                 try:
                     self.driver.find_element(By.NAME, "j_username").send_keys("system")
                     self.driver.find_element(By.NAME, "j_password").send_keys("secret")
                 except: pass
            elif "click" in step_lower:
                 # Extract quoted text or prominent words
                 match = re.search(r"Click\s+([A-Za-z0-9\s]+)", step_text, re.IGNORECASE)
                 target = match.group(1).strip() if match else None
                 if target:
                     print(f"Attempting to Click: {target}")
                     # Try generic xpath by text
                     el = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{target}')]")
                     el.click()
            elif "enter" in step_lower or "type" in step_lower:
                 # Input attempt
                 pass
        except Exception as e:
            print(f"Web Action Failed (Expected, as this is heuristic): {e}")

def main():
    print("=== STARTING EXERCISE: Exercise 8 – Modifying the default join directive for an attribute ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Click the")
    web_bot.try_action("2. Click the")
    print_step("3. Select")
    web_bot.try_action("3. Select")
    print_step("4. Create")
    web_bot.try_action("4. Create")
    print_step("5. Create")
    web_bot.try_action("5. Create")
    print_step("6. Submit")
    web_bot.try_action("6. Submit")
    print_step("7. Repeat steps 1 through 6 for the")
    web_bot.try_action("7. Repeat steps 1 through 6 for the")
    print_step("8. Submit")
    web_bot.try_action("8. Submit")
    print_step("9. On the")
    web_bot.try_action("9. On the")
    print_step("10. On the")
    web_bot.try_action("10. On the")
    print_step("11. Click")
    web_bot.try_action("11. Click")
    print_step("12. Submit")
    web_bot.try_action("12. Submit")
    print_step("13. As")
    web_bot.try_action("13. As")
    print_step("14. On the Home tab, go to")
    web_bot.try_action("14. On the Home tab, go to")
    print_step("15. Select the")
    web_bot.try_action("15. Select the")
    print_step("16. Select Intersection as the join type")
    web_bot.try_action("16. Select Intersection as the join type")
    print_step("17. Click")
    web_bot.try_action("17. Click")
    print_step("18. Restart")
    web_bot.try_action("18. Restart")
    print_step("19. On the")
    web_bot.try_action("19. On the")
    print_step("20. Click")
    web_bot.try_action("20. Click")
    print_step("21. Submit")
    web_bot.try_action("21. Submit")
    print_step("22. As")
    web_bot.try_action("22. As")
    print_step("23. On the Home tab, you go to")
    web_bot.try_action("23. On the Home tab, you go to")
    print_step("24. Select the")
    web_bot.try_action("24. Select the")
    print_step("25. Select")
    web_bot.try_action("25. Select")
    print_step("26. Click")
    web_bot.try_action("26. Click")
    print_step("27. Click")
    web_bot.try_action("27. Click")
    print_step("28. Restart")
    web_bot.try_action("28. Restart")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("the", "adm")
    val = get_input("and add the", "dialout")
    val = get_input("Note", ":  You add the dialout and video groups because those groups are assigned to new users by default")
    val = get_input("printadmin", "as a")
    val = get_input("secondary groups.", "Do not add games.")
    val = get_input("User", "Data")
    val = get_input("Uma Join", "Last Name:")
    val = get_input("Full Name:", "Uma Join")
    val = get_input("Preferred user ID:", "ujoin")
    val = get_input("First Name:", "Uma")
    val = get_input("Organizational Role:", "JKE System Admin")
    val = get_input("Title:", "Manager")
    val = get_input("E-mail address:", "ujoin@")
    val = get_input("Password", ": P@ssw0rd")
    val = get_input("Note", ":  Be sure to specify Uma’s first name, even though the information is optional. You create")
    val = get_input("", "printadmin")
    val = get_input("", "adm")
    val = get_input("using Java Webstart(default). Click", "OK")
    val = get_input("Click", "Run")
    val = get_input("attribute", "erposixsecondgroup")
    val = get_input("command", ":")
    val = get_input("Note", ":  There is an option in")
    val = get_input("provisioning.policy.join.overridingCacheTimeout", "that controls how often the join directives are refreshed")
    val = get_input("User", "Data")
    val = get_input("Ima Join", "Last Name:")
    val = get_input("Full Name:", "Ima Join")
    val = get_input("Preferred user ID:", "ijoin")
    val = get_input("First Name:", "Ima")
    val = get_input("Organizational Role:", "JKE System Admin")
    val = get_input("Title:", "Manager")
    val = get_input("E-mail address:", "ijoin@jke.test")
    val = get_input("Password", ": P@ssw0rd")
    val = get_input("groups", "Ima")
    val = get_input("", "printadmin")
    val = get_input("to  union", ".")
    val = get_input("using Java Webstart(default). Click", "OK")
    val = get_input("Click", "Run")
    val = get_input("attribute", "erposixsecondgroup")
    val = get_input("command", ":")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
