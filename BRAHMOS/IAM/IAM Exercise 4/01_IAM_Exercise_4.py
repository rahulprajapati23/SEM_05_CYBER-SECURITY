"""
Interactive Guide for: IAM Exercise 4
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
    print("=== STARTING EXERCISE: IAM Exercise 4 ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1.      On the        Home         tab, go to         Manage Users.")
    web_bot.try_action("1.      On the        Home         tab, go to         Manage Users.")
    print_step("2.      Click     Refresh         . Locate         Alice Smith.              Click the arrow to the right of the name and click                                           Change         .")
    web_bot.try_action("2.      Click     Refresh         . Locate         Alice Smith.              Click the arrow to the right of the name and click                                           Change         .")
    print_step("3.      Change the              Last name, Full name, Preferred user ID, and email address                                                                   attributes to reflect her")
    web_bot.try_action("3.      Change the              Last name, Full name, Preferred user ID, and email address                                                                   attributes to reflect her")
    print_step("4.      Refresh          the user list to confirm the name change.")
    web_bot.try_action("4.      Refresh          the user list to confirm the name change.")
    print_step("5.      Click the          arrow       to the right of Alice Smyth and click                                    Accounts            . Click      Refresh          . For the account on")
    web_bot.try_action("5.      Click the          arrow       to the right of Alice Smyth and click                                    Accounts            . Click      Refresh          . For the account on")
    print_step("1.      On the        Home         tab, you go to             Manage Users.")
    web_bot.try_action("1.      On the        Home         tab, you go to             Manage Users.")
    print_step("2.      Locate        Alice Smyth              . Click the arrow to the right of the name and click                                           Change          .")
    web_bot.try_action("2.      Locate        Alice Smyth              . Click the arrow to the right of the name and click                                           Change          .")
    print_step("3.      Click the         Business Information tab.")
    web_bot.try_action("3.      Click the         Business Information tab.")
    print_step("4.      In the       Manager            field, click         Search         and locate             Sue Thomas                . Select Sue as the manager and Click")
    web_bot.try_action("4.      In the       Manager            field, click         Search         and locate             Sue Thomas                . Select Sue as the manager and Click")
    print_step("5.      Click      Submit Now                to update the entry. Click                       Close       .")
    web_bot.try_action("5.      Click      Submit Now                to update the entry. Click                       Close       .")
    print_step("1.      On the        Home          tab, go to         Manage Users.")
    web_bot.try_action("1.      On the        Home          tab, go to         Manage Users.")
    print_step("2.      Search          the user list and locate the entry for                               Sue Thomas.")
    web_bot.try_action("2.      Search          the user list and locate the entry for                               Sue Thomas.")
    print_step("3.      Select        the Sue Thomas entry and click                                Transfer         .")
    web_bot.try_action("3.      Select        the Sue Thomas entry and click                                Transfer         .")
    print_step("4.      Search for the               Finance          organizational unit. Select                        Finance           and click         OK     .")
    web_bot.try_action("4.      Search for the               Finance          organizational unit. Select                        Finance           and click         OK     .")
    print_step("5.      Click      Transfer         . Click      Close       .")
    web_bot.try_action("5.      Click      Transfer         . Click      Close       .")
    print_step("6.      Return to the              Manage           Users        tab.     Refresh          the user list to verify that                    Sue      Thomas            is transferred.")
    web_bot.try_action("6.      Return to the              Manage           Users        tab.     Refresh          the user list to verify that                    Sue      Thomas            is transferred.")
    print_step("7.      Repeat steps 1 through 6 to transfer                                      Bob       Smith        to the        WW       location           in   Sales       . Also, transfer              John")
    web_bot.try_action("7.      Repeat steps 1 through 6 to transfer                                      Bob       Smith        to the        WW       location           in   Sales       . Also, transfer              John")
    print_step("8.      When you are done, the user list should look like this:")
    web_bot.try_action("8.      When you are done, the user list should look like this:")
    print_step("1.      On the        Home          tab, click        Manage           Roles       .")
    web_bot.try_action("1.      On the        Home          tab, click        Manage           Roles       .")
    print_step("2.      Click      Create         to add a new role.")
    web_bot.try_action("2.      Click      Create         to add a new role.")
    print_step("3.      Complete the                Create         Role       form with the following information:")
    web_bot.try_action("3.      Complete the                Create         Role       form with the following information:")
    print_step("4. Click")
    web_bot.try_action("4. Click")
    print_step("5. Repeat steps 2 through 4 to create 5 more static roles")
    web_bot.try_action("5. Repeat steps 2 through 4 to create 5 more static roles")
    print_step("1. Create another role, this time choose the")
    web_bot.try_action("1. Create another role, this time choose the")
    print_step("2. Complete the")
    web_bot.try_action("2. Complete the")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. On the")
    web_bot.try_action("4. On the")
    print_step("5. Click the arrow to the right of the")
    web_bot.try_action("5. Click the arrow to the right of the")
    print_step("6. Verify that the users in this dynamic role have")
    web_bot.try_action("6. Verify that the users in this dynamic role have")
    print_step("7. Create another Dynamic role")
    web_bot.try_action("7. Create another Dynamic role")
    print_step("8. Complete the form with the following information:")
    web_bot.try_action("8. Complete the form with the following information:")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Role Type", "Static")
    val = get_input("Role Classification", "[Leave blank]")
    val = get_input("Business unit", "JK Enterprises")
    val = get_input("Role Name", "JKE System Admin")
    val = get_input("Description", "Organizational Role for System Administrators")
    val = get_input("Access Information", "[Leave as is]")
    val = get_input("Assignment Attributes", "[none]")
    val = get_input("Role Membership", "Erica Carr")
    val = get_input("initially)", ":")
    val = get_input("a)", "System Account Owner")
    val = get_input("b)", "Finance Employees")
    val = get_input("c)", "Asset Handling")
    val = get_input("Check the", "Enable access for this role")
    val = get_input("access", "check box. These settings allow users to request membership in the roles as an access.")
    val = get_input("d)", "Booking and Ledgers")
    val = get_input("Check the", "Enable access for this role")
    val = get_input("access", "check box.")
    val = get_input("e)", "Comparison and Review")
    val = get_input("Check the", "Enable access for this role")
    val = get_input("access", "check box.")
    val = get_input("Role Type", "Dynamic")
    val = get_input("Role Classification", "[Leave blank]")
    val = get_input("Business unit", "JK Enterprises")
    val = get_input("Make role applicable to", "This business unit and its subunits")
    val = get_input("Role Name", "JKE Managers")
    val = get_input("Description", "Organizational Role for JKE Managers")
    val = get_input("Access Information", "[Leave as is]")
    val = get_input("Definition (Rule)", "(title=*Manager*)")
    val = get_input("Role Type", "Dynamic")
    val = get_input("Role Classification", "[Leave blank]")
    val = get_input("Business unit", "TechSupport")
    val = get_input("Make role applicable to", "This business unit and its subunits")
    val = get_input("Role Name", "Help Desk")
    val = get_input("Description", "TechSupport help desk")
    val = get_input("Access Information", "[Leave as is]")
    val = get_input("Definition (Rule)", "(cn=*)")
    val = get_input("Note", ":  The role scope is relative to the position of the role in the organization tree. A dynamic role")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
