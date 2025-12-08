"""
Interactive Guide for: GUIDE_README
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
    print("=== STARTING EXERCISE: GUIDE_README ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("Commands like `idsicrt`, `ibmslapd`, and `ldapsearch` are automatically executed when the script runs on the ISIM server.")
    run_command("Commands like `idsicrt`, `ibmslapd`, and `ldapsearch` are automatically executed when the script runs on the ISIM server.")
    print_step("No manual typing required.")
    web_bot.try_action("No manual typing required.")
    print_step("The scripts attempt to launch **Google Chrome** to perform web steps (Login, Click, Create).")
    web_bot.try_action("The scripts attempt to launch **Google Chrome** to perform web steps (Login, Click, Create).")
    print_step("It uses \"Smart Text Matching\" to find buttons.")
    web_bot.try_action("It uses \"Smart Text Matching\" to find buttons.")
    print_step("*Fallback*: If it can't find a button (e.g., complex UI), it prints a warning and lets you click it manually. **The script will NOT crash.**")
    web_bot.try_action("*Fallback*: If it can't find a button (e.g., complex UI), it prints a warning and lets you click it manually. **The script will NOT crash.**")
    print_step("For form fields (names, passwords), the script asks you to verify or enter the value.")
    web_bot.try_action("For form fields (names, passwords), the script asks you to verify or enter the value.")
    print_step("Must match your Firefox version.")
    web_bot.try_action("Must match your Firefox version.")
    print_step("Must be in your system `PATH` (e.g., `/usr/bin/` or same folder as script).")
    web_bot.try_action("Must be in your system `PATH` (e.g., `/usr/bin/` or same folder as script).")
    print_step("*If missing*: The script will default to text-only mode.")
    web_bot.try_action("*If missing*: The script will default to text-only mode.")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
