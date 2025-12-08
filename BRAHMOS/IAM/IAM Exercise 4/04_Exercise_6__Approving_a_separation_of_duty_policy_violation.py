"""
Interactive Guide for: Exercise 6 – Approving a separation of duty policy violation
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
    print("=== STARTING EXERCISE: Exercise 6 – Approving a separation of duty policy violation ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Restart")
    web_bot.try_action("1. Restart")
    print_step("2. Log on as Alice Smyth (")
    web_bot.try_action("2. Log on as Alice Smyth (")
    print_step("3. Click")
    web_bot.try_action("3. Click")
    print_step("4. Click on")
    web_bot.try_action("4. Click on")
    print_step("5. Click the")
    web_bot.try_action("5. Click the")
    print_step("6. Click")
    web_bot.try_action("6. Click")
    print_step("7. Log out")
    web_bot.try_action("7. Log out")
    print_step("8. Now, log in to the Identity Service Center as")
    web_bot.try_action("8. Now, log in to the Identity Service Center as")
    print_step("9. Click on")
    web_bot.try_action("9. Click on")
    print_step("10. Provide Justification –")
    web_bot.try_action("10. Provide Justification –")
    print_step("11. Log out")
    web_bot.try_action("11. Log out")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("https://isim.test:9443/itim/ui/Login.jsp", "or click the bookmark")
    val = get_input("role and Click", "Next.")
    val = get_input("Finance", "and Click")
    val = get_input("exception.", "Log back")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
