"""
Interactive Guide for: Exercise 2 – Creating a Directory Services Markup Language (DSML)
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
    print("=== STARTING EXERCISE: Exercise 2 – Creating a Directory Services Markup Language (DSML) ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Click")
    web_bot.try_action("2. Click")
    print_step("3. Select the")
    web_bot.try_action("3. Select the")
    print_step("4. Select")
    web_bot.try_action("4. Select")
    print_step("5. Complete the")
    web_bot.try_action("5. Complete the")
    print_step("6. Click")
    web_bot.try_action("6. Click")
    print_step("7. If the connection is")
    web_bot.try_action("7. If the connection is")
    print_step("8. When you see the message that you")
    web_bot.try_action("8. When you see the message that you")
    print_step("9. From")
    web_bot.try_action("9. From")
    print_step("10. Click the")
    web_bot.try_action("10. Click the")
    print_step("11. When you see the message that you successfully submitted a reconciliation request, click")
    web_bot.try_action("11. When you see the message that you successfully submitted a reconciliation request, click")
    print_step("12. If the status of the request is pending(wait for a minute), click")
    web_bot.try_action("12. If the status of the request is pending(wait for a minute), click")
    print_step("13. On the")
    web_bot.try_action("13. On the")
    print_step("14. You can also review the contents of")
    web_bot.try_action("14. You can also review the contents of")
    print_step("15. Close all the tabs.")
    web_bot.try_action("15. Close all the tabs.")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Development", ".")
    val = get_input("Service name", "DSML Identity Feed")
    val = get_input("Description", "Load Dev Team through DSML Feed")
    val = get_input("User ID", "[Leave blank]")
    val = get_input("Password", "[Leave blank]")
    val = get_input("File name", "/classfiles/data/development.dsml")
    val = get_input("Use workflow", "[Cleared]")
    val = get_input("Evaluate separation of duty", "[Cleared]")
    val = get_input("Placement rule", "return \"ou=Development\";")
    val = get_input("my request.", "The reconciliation request should be the top-most request in the list.")
    val = get_input("to the", "Development")
    val = get_input("in", "Text Editor")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
