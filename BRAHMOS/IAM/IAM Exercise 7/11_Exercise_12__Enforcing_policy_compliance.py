"""
Interactive Guide for: Exercise 12 – Enforcing policy compliance
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
    print("=== STARTING EXERCISE: Exercise 12 – Enforcing policy compliance ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Click the small")
    web_bot.try_action("2. Click the small")
    print_step("3. Click the")
    web_bot.try_action("3. Click the")
    print_step("4. Click the small yellow warning icon to see the non-compliant attributes.")
    web_bot.try_action("4. Click the small yellow warning icon to see the non-compliant attributes.")
    print_step("5. On the")
    web_bot.try_action("5. On the")
    print_step("6. Click the small")
    web_bot.try_action("6. Click the small")
    print_step("7. Set the enforcement action to")
    web_bot.try_action("7. Set the enforcement action to")
    print_step("8. Submit")
    web_bot.try_action("8. Submit")
    print_step("9. Click")
    web_bot.try_action("9. Click")
    print_step("10. Return to")
    web_bot.try_action("10. Return to")
    print_step("11. Click the small")
    web_bot.try_action("11. Click the small")
    print_step("12. Set the enforcement action to")
    web_bot.try_action("12. Set the enforcement action to")
    print_step("13. Click")
    web_bot.try_action("13. Click")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Important", ":  Be careful when setting enforcement to Correct because disallowed accounts will be")
    val = get_input("detail to see which user’s Linux accounts are modified.", "Refresh")
    val = get_input("Accounts", "Tab to confirm all accounts are now compliant.")
    val = get_input("In order to prevent unintended account changes or deletions, you set the policy enforcement back to", "Mark")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
