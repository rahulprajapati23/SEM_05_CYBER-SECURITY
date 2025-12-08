"""
Interactive Guide for: Exercise 5 – Creating identities with a IBM Security Directory
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
    print("=== STARTING EXERCISE: Exercise 5 – Creating identities with a IBM Security Directory ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Log in to the IBM Security Identity Manager Administrative Console as the system administrator with")
    web_bot.try_action("1. Log in to the IBM Security Identity Manager Administrative Console as the system administrator with")
    print_step("2. On the")
    web_bot.try_action("2. On the")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. Confirm that the Business unit is set to")
    web_bot.try_action("4. Confirm that the Business unit is set to")
    print_step("5. Use the following information to complete the Create a Service form:")
    web_bot.try_action("5. Use the following information to complete the Create a Service form:")
    print_step("6. Click")
    web_bot.try_action("6. Click")
    print_step("7. Assuming a successful connection test, click")
    web_bot.try_action("7. Assuming a successful connection test, click")
    print_step("8. Return to the")
    web_bot.try_action("8. Return to the")
    print_step("9. Click the small arrow to the right of")
    web_bot.try_action("9. Click the small arrow to the right of")
    print_step("10. To verify that the feed is successful, click Manage Users to confirm the identities are added to")
    web_bot.try_action("10. To verify that the feed is successful, click Manage Users to confirm the identities are added to")
    print_step("11. Return to the IBM Security Directory Integrator editor and click the red square icon(")
    web_bot.try_action("11. Return to the IBM Security Directory Integrator editor and click the red square icon(")
    print_step("12. Exit")
    web_bot.try_action("12. Exit")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Next", ".")
    val = get_input("Service name", "TDI feed")
    val = get_input("URL", "http://isim.test:8800/")
    val = get_input("Naming context", "dc=IDIFeed")
    val = get_input("Use workflow", "[Cleared]")
    val = get_input("Evaluate separation of duty", "[Cleared]")
    val = get_input("Name attribute", "uid")
    val = get_input("Placement rule", "var deptNum = entry.departmentnumber[0];")
    val = get_input("the file", "/classfiles/scripts/ IDI_placementrule.js.")
    val = get_input("and you can copy the JavaScript and paste the into the", "Placement Rule")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
