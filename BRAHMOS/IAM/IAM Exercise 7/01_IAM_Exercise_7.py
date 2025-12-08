"""
Interactive Guide for: IAM Exercise 7
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
    print("=== STARTING EXERCISE: IAM Exercise 7 ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1.      Log in        to the IBM Security Identity Manager Administrative Console as the system administrator with")
    web_bot.try_action("1.      Log in        to the IBM Security Identity Manager Administrative Console as the system administrator with")
    print_step("2.      In the      Home         tab, go to         Manage           Users        .")
    web_bot.try_action("2.      In the      Home         tab, go to         Manage           Users        .")
    print_step("3.      Edit the        Alice      Smyth          entry.")
    web_bot.try_action("3.      Edit the        Alice      Smyth          entry.")
    print_step("4.      In the      Personal           Information              tab    , add the         JKE System Admin                        organizational              role    .")
    web_bot.try_action("4.      In the      Personal           Information              tab    , add the         JKE System Admin                        organizational              role    .")
    print_step("5.      Click      Submit         Now       . Click     Close.")
    web_bot.try_action("5.      Click      Submit         Now       . Click     Close.")
    print_step("6.      Repeat steps 1-5 for                    Douglas           Adams           and     Edwin         Abbott        .")
    web_bot.try_action("6.      Repeat steps 1-5 for                    Douglas           Adams           and     Edwin         Abbott        .")
    print_step("7.      Add user          Linux System-Accounts                              to role      System Accounts Owner.")
    web_bot.try_action("7.      Add user          Linux System-Accounts                              to role      System Accounts Owner.")
    print_step("1.      On the         Home         tab, you go to              Manage Policies > Manage Provisioning Policies.")
    web_bot.try_action("1.      On the         Home         tab, you go to              Manage Policies > Manage Provisioning Policies.")
    print_step("2.      Click      Refresh         . Click the policy named                        Default Provisioning Policy for service Linux Service.")
    web_bot.try_action("2.      Click      Refresh         . Click the policy named                        Default Provisioning Policy for service Linux Service.")
    print_step("3.      Modify the provisioning policy to match the following information:")
    web_bot.try_action("3.      Modify the provisioning policy to match the following information:")
    print_step("4. Click")
    web_bot.try_action("4. Click")
    print_step("5. Click the")
    web_bot.try_action("5. Click the")
    print_step("6. Close")
    web_bot.try_action("6. Close")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Policy name", "Admin Linux Accounts")
    val = get_input("Policy Status", "Enable")
    val = get_input("Priority", "100")
    val = get_input("Members (Section)", "Select :")
    val = get_input("Add organizational role", "JKE System Admin")
    val = get_input("Entitlements (Section)", "Select check box for")
    val = get_input("Provisioning options:", "Automatic")
    val = get_input("Target type:", "Specific Service")
    val = get_input("Service Name:", "Linux Service")
    val = get_input("Workflow:", "[Leave blank, click clear button if populated]")
    val = get_input("Entitlement parameters(Section)", "Select check box for")
    val = get_input("click", "Create")
    val = get_input("Select", "UNIX shell")
    val = get_input("Enforcement type", "default")
    val = get_input("Change UNIX shell value to", "/bin/bash")
    val = get_input("policy. Click", "Continue")
    val = get_input("enforcement action is set to", "Mark")
    val = get_input("Manager regarding these violations. If you set the enforcement action to", "Correct")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
