"""
Interactive Guide for: Exercise 4 – Creating a IBM Security Directory Integrator identity feed
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
    print("=== STARTING EXERCISE: Exercise 4 – Creating a IBM Security Directory Integrator identity feed ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Launch the IBM Security Directory Integrator editor with the following command: Open the")
    run_command("1. Launch the IBM Security Directory Integrator editor with the following command: Open the")
    print_step("2. If you are prompted to select a workspace, accept the default location and click")
    web_bot.try_action("2. If you are prompted to select a workspace, accept the default location and click")
    print_step("3. Import the pre-built configuration file by clicking")
    web_bot.try_action("3. Import the pre-built configuration file by clicking")
    print_step("4. Select")
    web_bot.try_action("4. Select")
    print_step("5. When prompted for the")
    web_bot.try_action("5. When prompted for the")
    print_step("6. In the Navigator panel, expand")
    web_bot.try_action("6. In the Navigator panel, expand")
    print_step("7. Double-click")
    web_bot.try_action("7. Double-click")
    print_step("8. Click")
    web_bot.try_action("8. Click")
    print_step("9. The mapping table has three columns. The")
    web_bot.try_action("9. The mapping table has three columns. The")
    print_step("10. Close")
    web_bot.try_action("10. Close")
    print_step("11. Double-Click")
    web_bot.try_action("11. Double-Click")
    print_step("12. The")
    web_bot.try_action("12. The")
    print_step("13. Click")
    web_bot.try_action("13. Click")
    print_step("14. The Assembly Line is running successfully when you see a message similar to the following:")
    web_bot.try_action("14. The Assembly Line is running successfully when you see a message similar to the following:")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Integrator > Configuration", "and click")
    val = get_input("source CSV file.", "The")
    val = get_input("Security Identity Manager. The", "middle")
    val = get_input("IBM Security Identity Manager. If the request is for a", "reconciliation")
    val = get_input("line calls the", "CSVtoISIM")
    val = get_input("assembly line are collected and then", "passed back")
    val = get_input("on port", "8800")
    val = get_input("Note", ": Don’t close")
    val = get_input("exercise", "5.5")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
