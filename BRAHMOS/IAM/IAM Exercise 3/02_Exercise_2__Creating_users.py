"""
Interactive Guide for: Exercise 2 – Creating users
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
    print("=== STARTING EXERCISE: Exercise 2 – Creating users ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. On the")
    web_bot.try_action("1. On the")
    print_step("2. Click")
    web_bot.try_action("2. Click")
    print_step("3. Add")
    web_bot.try_action("3. Add")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Type", "Person")
    val = get_input("Note", ":  Title")
    val = get_input("section. On the password page Select", "Allow me to type a password.")
    val = get_input("for a password, enter", "P@ssw0rd.")
    val = get_input("User", "Data")
    val = get_input("Sue Thomas", "Last Name:")
    val = get_input("Full Name:", "Sue")
    val = get_input("Preferred user ID:", "sthomas")
    val = get_input("First Name:", "Sue")
    val = get_input("Title:", "Manager")
    val = get_input("E-mail address:", "sthomas@jke.test")
    val = get_input("Password:", "P@ssw0rd")
    val = get_input("Bob Smith", "Last Name:")
    val = get_input("Full Name:", "Bob Smith")
    val = get_input("Preferred user ID:", "bsmith")
    val = get_input("First Name:", "Bob")
    val = get_input("Title:", "[Leave blank]")
    val = get_input("E-mail address:", "bsmith@jke.test")
    val = get_input("Erica Carr", "Last Name:")
    val = get_input("Full Name:", "Erica")
    val = get_input("Preferred user ID:", "ecarr")
    val = get_input("First Name:", "Erica")
    val = get_input("Title:", "[Leave blank]")
    val = get_input("E-mail address:", "ecarr@jke.test")
    val = get_input("John Davis", "Last Name:")
    val = get_input("Full Name:", "John")
    val = get_input("Preferred user ID:", "jdavis")
    val = get_input("First Name:", "John")
    val = get_input("Title:", "[Leave blank]")
    val = get_input("E-mail address:", "jdavis@jke.test")
    val = get_input("On the", "Home")
    val = get_input("Click", "Create")
    val = get_input("Person", "and Click")
    val = get_input("UserNote", ":  Your previous users are added to the top of the organization chart. Make sure that you select theData")
    val = get_input("Finance", "business unit when adding Alice.")
    val = get_input("Alice Smith", "Last Name:")
    val = get_input("Full Name:", "Alice Smith")
    val = get_input("Preferred user ID:", "asmith")
    val = get_input("First Name:", "Alice")
    val = get_input("Title:", "[Leave blank]")
    val = get_input("E-mail address:", "asmith@jke.test")
    val = get_input("When you are done, return to the", "Manage Users")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
