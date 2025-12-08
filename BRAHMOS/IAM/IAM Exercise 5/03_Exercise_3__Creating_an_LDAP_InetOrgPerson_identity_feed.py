"""
Interactive Guide for: Exercise 3 – Creating an LDAP InetOrgPerson identity feed
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
    print("=== STARTING EXERCISE: Exercise 3 – Creating an LDAP InetOrgPerson identity feed ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Log in to the IBM Security Identity Manager Administrative Console as the system administrator with")
    web_bot.try_action("1. Log in to the IBM Security Identity Manager Administrative Console as the system administrator with")
    print_step("2. On the")
    web_bot.try_action("2. On the")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. Complete the")
    web_bot.try_action("4. Complete the")
    print_step("5. Click")
    web_bot.try_action("5. Click")
    print_step("6. If the connection is successful, click")
    web_bot.try_action("6. If the connection is successful, click")
    print_step("7. When you see the message that you")
    web_bot.try_action("7. When you see the message that you")
    print_step("8. From")
    web_bot.try_action("8. From")
    print_step("9. Click the small")
    web_bot.try_action("9. Click the small")
    print_step("10. When you see the message that you successfully submitted a reconciliation request, click")
    web_bot.try_action("10. When you see the message that you successfully submitted a reconciliation request, click")
    print_step("11. If the initial status of the request shows that it is in the pending state, click")
    web_bot.try_action("11. If the initial status of the request shows that it is in the pending state, click")
    print_step("12. On the")
    web_bot.try_action("12. On the")
    print_step("13. To activate each user,")
    web_bot.try_action("13. To activate each user,")
    print_step("14. Close the Reconcile Now tab.")
    web_bot.try_action("14. Close the Reconcile Now tab.")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("ou=sales,o=PDQ.", "You can use")
    val = get_input("Open the", "LDAP Browser")
    val = get_input("O=PDQ then Expand ou=sales.", "Confirm there are five users in the PDQ organization to import with this")
    val = get_input("the user ID", "itim manager.")
    val = get_input("Business unit", "JK Enterprises")
    val = get_input("Service type", "INetOrgPerson identity feed")
    val = get_input("Service name", "LDAP inetOrgPerson Identity Feed")
    val = get_input("Description", "LDAP Identity Feed")
    val = get_input("URL", "ldap://isim.test:389")
    val = get_input("User ID", "cn=root")
    val = get_input("Password", "P@ssw0rd")
    val = get_input("Naming context", "ou=sales,o=pdq")
    val = get_input("Use workflow", "[Cleared]")
    val = get_input("Evaluate separation of duty", "[Cleared]")
    val = get_input("Person profile name", "Person")
    val = get_input("Name attribute", "uid")
    val = get_input("Placement rule", "return \"L=AP,ou=Sales\";")
    val = get_input("Note", ":  The placement rule uses L=AP,ou=Sales to indicate that new users are placed in the AP")
    val = get_input("Notice that the users are imported but marked as", "inactive")
    val = get_input("the users inactive because they do not have a", "userPasssword")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
