"""
Interactive Guide for: Exercise 7 – Adopting accounts automatically
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
    print("=== STARTING EXERCISE: Exercise 7 – Adopting accounts automatically ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Create")
    web_bot.try_action("2. Create")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. Return to the")
    web_bot.try_action("4. Return to the")
    print_step("5. Verify that the status of the reconciliation is")
    web_bot.try_action("5. Verify that the status of the reconciliation is")
    print_step("6. Return to the")
    web_bot.try_action("6. Return to the")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Name", "Linux Service Adoption Policy")
    val = get_input("Description", "Adoption policy for Linux Service")
    val = get_input("Services (Section)", "Linux Service (Change Service type to :")
    val = get_input("service type,", "Click")
    val = get_input("Rule (Section)", "Providing a script")
    val = get_input("Note:", "There are system-defined JavaScript objects that you use in adoption rules. For more information,")
    val = get_input("refer to the on-line help. In this example, you are using the", "searchByFilter")
    val = get_input("object.", "The syntax is:")
    val = get_input("where", "scope=1")
    val = get_input("click", "Reconcile")
    val = get_input("click", "Accounts")
    val = get_input("and", "ntp")
    val = get_input("Note:", "If you click one of these accounts to view the attributes, you might see the following warning")
    val = get_input("This error is occurring because", "/sbin/nologin")
    val = get_input("form. You can safely", "ignore")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
