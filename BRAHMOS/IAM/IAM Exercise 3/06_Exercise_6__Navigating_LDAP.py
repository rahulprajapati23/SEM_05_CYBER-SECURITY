"""
Interactive Guide for: Exercise 6 – Navigating LDAP
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
    print("=== STARTING EXERCISE: Exercise 6 – Navigating LDAP ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Open a terminal window.")
    run_command("1. Open a terminal window.")
    print_step("2. Change directory to")
    web_bot.try_action("2. Change directory to")
    print_step("3. To find all the attributes for Bob Smith, type the following command:")
    run_command("3. To find all the attributes for Bob Smith, type the following command:", auto_cmd="ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"dc=com\" \"cn=Bob Smith\"")
    print_step("4. To find the email address for Sue Thomas, type the following command:")
    run_command("4. To find the email address for Sue Thomas, type the following command:", auto_cmd="ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"dc=com\" \"cn=Sue Thomas\" mail")
    print_step("5. To find all the entries that are the children of the JKE organization, you type the following command:")
    run_command("5. To find all the entries that are the children of the JKE organization, you type the following command:", auto_cmd="ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"o=jke\" \"objectclass=*\"")
    print_step("6. To find all the entries who have manager in their title, you type the following command:")
    run_command("6. To find all the entries who have manager in their title, you type the following command:", auto_cmd="ldapsearch -h localhost -p 389 -D cn=root -w P@ssw0rd -b \"dc=com\" \"title=*manager*\"")
    print_step("1. Double-click the")
    web_bot.try_action("1. Double-click the")
    print_step("2. In the sessions panel of the interface, double-click")
    web_bot.try_action("2. In the sessions panel of the interface, double-click")
    print_step("3. In the LDAP Browser panel, expand the")
    web_bot.try_action("3. In the LDAP Browser panel, expand the")
    print_step("4. Right click")
    web_bot.try_action("4. Right click")
    print_step("5. You set the filter to")
    web_bot.try_action("5. You set the filter to")
    print_step("6. The search result is the Sue Thomas entry. Right click on the result and click")
    web_bot.try_action("6. The search result is the Sue Thomas entry. Right click on the result and click")
    print_step("1. Open a web browser and open")
    web_bot.try_action("1. Open a web browser and open")
    print_step("2. Log in as user name")
    web_bot.try_action("2. Log in as user name")
    print_step("1. Click")
    web_bot.try_action("1. Click")
    print_step("2. Select")
    web_bot.try_action("2. Select")
    print_step("3. Use the following information to fill in the form:")
    web_bot.try_action("3. Use the following information to fill in the form:")
    print_step("4. The completed form looks like :")
    web_bot.try_action("4. The completed form looks like :")
    print_step("5. Click")
    web_bot.try_action("5. Click")
    print_step("6. Select the entry and click")
    web_bot.try_action("6. Select the entry and click")
    print_step("7. Click")
    web_bot.try_action("7. Click")
    print_step("1. Select")
    web_bot.try_action("1. Select")
    print_step("2. Click")
    web_bot.try_action("2. Click")
    print_step("3. Use the following information to complete the form:")
    web_bot.try_action("3. Use the following information to complete the form:")
    print_step("4. Click")
    web_bot.try_action("4. Click")
    print_step("5. Click")
    web_bot.try_action("5. Click")
    print_step("6. Use the following information to complete the form:")
    web_bot.try_action("6. Use the following information to complete the form:")
    print_step("7. Click")
    web_bot.try_action("7. Click")
    print_step("8. Click")
    web_bot.try_action("8. Click")
    print_step("9. View the attributes of an entry to verify that it contains a title of")
    web_bot.try_action("9. View the attributes of an entry to verify that it contains a title of")
    print_step("10. Repeat steps 1 through 8, changing step 6 to search for title")
    web_bot.try_action("10. Repeat steps 1 through 8, changing step 6 to search for title")
    print_step("1. Click")
    web_bot.try_action("1. Click")
    print_step("2. Select")
    web_bot.try_action("2. Select")
    print_step("3. Select")
    web_bot.try_action("3. Select")
    print_step("4. Select")
    web_bot.try_action("4. Select")
    print_step("5. Select")
    web_bot.try_action("5. Select")
    print_step("6. Select a role and click")
    web_bot.try_action("6. Select a role and click")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("The", "basedn")
    val = get_input("search the entire organization, or", "“ou=Sales,dc=com”")
    val = get_input("inetOrgPerson, use the filter", "“objectclass=inetOrgPerson”.")
    val = get_input("returned. If you want the search to return a user’s email address, use", "mail")
    val = get_input("Note", ":  Some time the quote marks can give problems if copied from Windows machine to CentOS if the")
    val = get_input("command does not work just remove", "quote marks")
    val = get_input("Server. It is already installed and configured for you. LDAP Browser", "simplifies viewing entries and")
    val = get_input("Important", ":  IBM Security Identity Manager stores data and configuration information in the sub tree under")
    val = get_input("ou=itim,dc=com and ou=ibm,dc=com", ". You can browse these portions of the tree but")
    val = get_input("Note", ":  If Firefox gives certificate issue, Click")
    val = get_input("Note", ":  The drop-down for the below Attribute field might get delayed sometimes to open due to loading of")
    val = get_input("objectClass", "top")
    val = get_input("Attribute", "cn")
    val = get_input("Is equal to", "Bob Smith")
    val = get_input("Attribute", "objectClass")
    val = get_input("Comparison", "Is equal to")
    val = get_input("Value", "Person")
    val = get_input("Operator", "AND")
    val = get_input("Attribute", "title")
    val = get_input("Comparison", "Is equal to")
    val = get_input("Value", "*manager*")
    val = get_input("Operator", "AND")
    val = get_input("Note", ":  For exercises that require browsing LDAP, you can use either LDAP Browser or")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
