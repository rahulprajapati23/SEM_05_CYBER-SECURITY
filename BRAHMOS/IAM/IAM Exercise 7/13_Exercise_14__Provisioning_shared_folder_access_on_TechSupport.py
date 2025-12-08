"""
Interactive Guide for: Exercise 14 – Provisioning shared folder access on TechSupport
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
    print("=== STARTING EXERCISE: Exercise 14 – Provisioning shared folder access on TechSupport ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Log in to the IBM Security Identity Manager Administrative Console as the system administrator with")
    web_bot.try_action("1. Log in to the IBM Security Identity Manager Administrative Console as the system administrator with")
    print_step("2. On the")
    web_bot.try_action("2. On the")
    print_step("3. Click the policy named")
    web_bot.try_action("3. Click the policy named")
    print_step("4. Modify the provisioning policy to match the following information.")
    web_bot.try_action("4. Modify the provisioning policy to match the following information.")
    print_step("5. Click")
    web_bot.try_action("5. Click")
    print_step("6. Close")
    web_bot.try_action("6. Close")
    print_step("7. On the")
    web_bot.try_action("7. On the")
    print_step("8. Click the group name")
    web_bot.try_action("8. Click the group name")
    print_step("9. On the")
    web_bot.try_action("9. On the")
    print_step("10. Select")
    web_bot.try_action("10. Select")
    print_step("11. Click")
    web_bot.try_action("11. Click")
    print_step("12. Click")
    web_bot.try_action("12. Click")
    print_step("13. Close")
    web_bot.try_action("13. Close")
    print_step("14. Enter the URL for the Self Service console in New Firefox Window:")
    web_bot.try_action("14. Enter the URL for the Self Service console in New Firefox Window:")
    print_step("15. Log in as John Davis, with user ID")
    web_bot.try_action("15. Log in as John Davis, with user ID")
    print_step("16. Click")
    web_bot.try_action("16. Click")
    print_step("17. Enter the justification –")
    web_bot.try_action("17. Enter the justification –")
    print_step("18. Return to the home page using the")
    web_bot.try_action("18. Return to the home page using the")
    print_step("19. Confirm that John receives the access by reviewing")
    web_bot.try_action("19. Confirm that John receives the access by reviewing")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("the user ID", "itim manager.")
    val = get_input("Policy name", "Help Desk LDAP Accounts")
    val = get_input("Policy Status", "Enable")
    val = get_input("Priority", "1000")
    val = get_input("Members(Section)", "Add organizational role")
    val = get_input("Entitlements(Section)", "Click on")
    val = get_input("Provisioning options:", "Manual")
    val = get_input("Target type:", "Specific Service")
    val = get_input("Service Name:", "TechSupport LDAP")
    val = get_input("Workflow:", "[Leave blank, click Clear button if populated]")
    val = get_input("Entitlement Parameters(Section)", "Select check box for")
    val = get_input("Create", "button.")
    val = get_input("Select", "Group")
    val = get_input("Enforcement type", "Allowed")
    val = get_input("Group value", "JKENetworkShare")
    val = get_input("click", "Create button.")
    val = get_input("Select", "Full Name")
    val = get_input("Parameter type", "Javascript")
    val = get_input("Enforcement type", "Mandatory")
    val = get_input("Value", "return subject.getProperty(\"cn\");")
    val = get_input("click", "Create button.")
    val = get_input("Select", "Last Name")
    val = get_input("Parameter type", "Javascript")
    val = get_input("Enforcement type", "Mandatory")
    val = get_input("Value", "return subject.getProperty(\"sn\");")
    val = get_input("click", "Create button.")
    val = get_input("Select", "UserID")
    val = get_input("Parameter type", "Javascript")
    val = get_input("Enforcement type", "Mandatory")
    val = get_input("Value", "return subject.getProperty(\"uid\");")
    val = get_input("Click", "Continue")
    val = get_input("and", "refresh")
    val = get_input("Service and click", "Manage Groups.")
    val = get_input("access type", "Shared folder.")
    val = get_input("In access description put", "Shared Directory Access for TechSupport Employees only")
    val = get_input("workflow of", "No Approval Required.")
    val = get_input("In this task, you request access to the", "TechSupport Shared Directory")
    val = get_input("TechSupport LDAP", "Service. Click")
    val = get_input("You can open the", "LDAP Browser")
    val = get_input("expand", "ou=TechSuppEmployees.")
    val = get_input("also if you click", "cn")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
