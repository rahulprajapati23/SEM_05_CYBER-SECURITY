"""
Interactive Guide for: IAM Exercise 3
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
    print("=== STARTING EXERCISE: IAM Exercise 3 ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1.       Log in to the IBM Security Identity Manager Administrative Console as the system administrator")
    web_bot.try_action("1.       Log in to the IBM Security Identity Manager Administrative Console as the system administrator")
    print_step("2.      On the        Home         tab, you go to              Manage Organization Structure.")
    web_bot.try_action("2.      On the        Home         tab, you go to              Manage Organization Structure.")
    print_step("3.      Click the plus (+) sign to the left of the house icon to expand the selection. Click the small")
    web_bot.try_action("3.      Click the plus (+) sign to the left of the house icon to expand the selection. Click the small")
    print_step("4.      Complete the               Organizational Unit                      form with the following information:")
    web_bot.try_action("4.      Complete the               Organizational Unit                      form with the following information:")
    print_step("6. Repeat steps 3 through 5 to create the")
    web_bot.try_action("6. Repeat steps 3 through 5 to create the")
    print_step("1. Click the triangle to the right of")
    web_bot.try_action("1. Click the triangle to the right of")
    print_step("2. You complete the Location Details form with the following information.")
    web_bot.try_action("2. You complete the Location Details form with the following information.")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. You repeat steps 1 through 3 for the remaining locations:")
    web_bot.try_action("4. You repeat steps 1 through 3 for the remaining locations:")
    print_step("1. Click the arrow to the right of")
    web_bot.try_action("1. Click the arrow to the right of")
    print_step("2. Complete the Business Partner Unit form with the following information:")
    web_bot.try_action("2. Complete the Business Partner Unit form with the following information:")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Organizational unit name", "Sales")
    val = get_input("Description", "Sales Organizational Unit")
    val = get_input("Supervisor", "System Administrator")
    val = get_input("Note5.", ":  Click It is good practice to specify an organization supervisor. The system can notify the supervisor ofOK. You might have to refresh the Manage Organization Structure tab to see your new entry.")
    val = get_input("Adding the locations unitsNote :  Be sure to add these entries under the", "JK Enterprises entry,")
    val = get_input("The sales organization for JKE is divided into four regions:", "WW, Americas, EMEA, and AP")
    val = get_input("Location Name", "WW")
    val = get_input("Description", "Worldwide Sales")
    val = get_input("Supervisor", "System Administrator")
    val = get_input("", "Americas")
    val = get_input("", "EMEA")
    val = get_input("", "AP")
    val = get_input("Business partner name", "TechSupport")
    val = get_input("Sponsor", "System Administrator")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
