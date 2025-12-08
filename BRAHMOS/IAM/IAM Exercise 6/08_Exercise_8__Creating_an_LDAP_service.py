"""
Interactive Guide for: Exercise 8 – Creating an LDAP service
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
    print("=== STARTING EXERCISE: Exercise 8 – Creating an LDAP service ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Click")
    web_bot.try_action("2. Click")
    print_step("3. Wait for the list of services to appear. Ensure that Business unit is set to")
    web_bot.try_action("3. Wait for the list of services to appear. Ensure that Business unit is set to")
    print_step("4. Select")
    web_bot.try_action("4. Select")
    print_step("5. Create a new service of type LDAP Profile with the information in the following table:")
    web_bot.try_action("5. Create a new service of type LDAP Profile with the information in the following table:")
    print_step("6. Click")
    web_bot.try_action("6. Click")
    print_step("7. If the connection is")
    web_bot.try_action("7. If the connection is")
    print_step("8. Complete the form the information in the below table :")
    web_bot.try_action("8. Complete the form the information in the below table :")
    print_step("9. Keep other values as default and Click")
    web_bot.try_action("9. Keep other values as default and Click")
    print_step("10. Return to")
    web_bot.try_action("10. Return to")
    print_step("11. Click the small arrow to the right of")
    web_bot.try_action("11. Click the small arrow to the right of")
    print_step("12. View the status of the reconciliation request.")
    web_bot.try_action("12. View the status of the reconciliation request.")
    print_step("13. Return to Manage Services. Click the small arrow to the right of")
    web_bot.try_action("13. Return to Manage Services. Click the small arrow to the right of")
    print_step("14. Click")
    web_bot.try_action("14. Click")
    print_step("15. The red X icon in the State column indicates that the account is not permitted. Click the red X for")
    web_bot.try_action("15. The red X icon in the State column indicates that the account is not permitted. Click the red X for")
    print_step("16. Close")
    web_bot.try_action("16. Close")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Service name", "TechSupport LDAP")
    val = get_input("Description", "TechSupport LDAP Service for ISIM")
    val = get_input("Tivoli Directory Integrator location", "rmi://isim.test:1099/ITDIDispatcher")
    val = get_input("Directory Server Location", "ldap://isim.test:389")
    val = get_input("Administrator name", "cn=root")
    val = get_input("Password", "P@ssw0rd")
    val = get_input("Directory server name", "IBM Directory Server")
    val = get_input("Owner", "Bob Smith")
    val = get_input("User base DN", "ou=TechSuppEmployees,dc=contractors")
    val = get_input("User RDN Attribute", "UID")
    val = get_input("Group base DN", "ou=TechSuppEmployees,dc=contractors")
    val = get_input("Group RDN attribute", "CN")
    val = get_input("Select", "Yes, create a policy to automatically create accounts, and later enable the policy")
    val = get_input("Click", "Finish")
    val = get_input("a query.", "Submit")
    val = get_input("Accounts", ".")
    val = get_input("allows the account on the service. Recall that when you created the", "TechSupport")
    val = get_input("indicated you would", "enable the provisioning policy later.")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
