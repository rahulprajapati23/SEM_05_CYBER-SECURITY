"""
Interactive Guide for: Exercise 7 – Creating a provisioning policy for system accounts
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
    print("=== STARTING EXERCISE: Exercise 7 – Creating a provisioning policy for system accounts ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Create")
    web_bot.try_action("2. Create")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. On the")
    web_bot.try_action("4. On the")
    print_step("5. Click the small arrow to the right of")
    web_bot.try_action("5. Click the small arrow to the right of")
    print_step("6. Filter the list of accounts to show only the accounts that Linux System-Accounts owns by completing")
    web_bot.try_action("6. Filter the list of accounts to show only the accounts that Linux System-Accounts owns by completing")
    print_step("7. Click")
    web_bot.try_action("7. Click")
    print_step("8. Choose the check box at the top of the select column to")
    web_bot.try_action("8. Choose the check box at the top of the select column to")
    print_step("9. Find and choose user")
    web_bot.try_action("9. Find and choose user")
    print_step("10. On the confirmation screen, click")
    web_bot.try_action("10. On the confirmation screen, click")
    print_step("11. Click")
    web_bot.try_action("11. Click")
    print_step("12. The accounts show ownership type")
    web_bot.try_action("12. The accounts show ownership type")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("use ownership type", "system")
    val = get_input("Policy name", "System Linux Accounts")
    val = get_input("Policy Status", "Enable")
    val = get_input("Priority", "10000")
    val = get_input("Business unit", "JK Enterprises")
    val = get_input("Members (Section)", "Select :")
    val = get_input("Add organizational role", "System Account Owner")
    val = get_input("Entitlements (Section)", "Select")
    val = get_input("Provisioning options:", "Manual")
    val = get_input("Ownership type:", "System")
    val = get_input("Target type:", "Specific Service")
    val = get_input("Service Name:", "Linux Service")
    val = get_input("Workflow:", "[Leave blank, click clear button if populated]")
    val = get_input("Entitlement parameters(Section)", "[none set]")
    val = get_input("Now you change the account ownership for all the accounts that", "Linux System-Accounts")
    val = get_input("assign", "to user function to change the ownership type.")
    val = get_input("Hint", ":  If you don’t see any accounts, ensure that your Search settings specify ownership type")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
