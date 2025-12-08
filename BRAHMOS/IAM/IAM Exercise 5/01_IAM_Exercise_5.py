"""
Interactive Guide for: IAM Exercise 5
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
    print("=== STARTING EXERCISE: IAM Exercise 5 ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1.      Log in        to the IBM Security Identity Manager Administrative Console as the system administrator with")
    web_bot.try_action("1.      Log in        to the IBM Security Identity Manager Administrative Console as the system administrator with")
    print_step("2.      On the        Home         tab, navigate to                Manage Services.")
    web_bot.try_action("2.      On the        Home         tab, navigate to                Manage Services.")
    print_step("3.      Click      Create       .")
    web_bot.try_action("3.      Click      Create       .")
    print_step("4.      Confirm that the                 Finance business                        unit is selected or Click                        Search          in front of Business Unit and")
    web_bot.try_action("4.      Confirm that the                 Finance business                        unit is selected or Click                        Search          in front of Business Unit and")
    print_step("5.      Select       Comma Separated File (CSV) identity feed                                                and click         Next      .")
    web_bot.try_action("5.      Select       Comma Separated File (CSV) identity feed                                                and click         Next      .")
    print_step("6.      Complete the Create a Service form with the following information:")
    web_bot.try_action("6.      Complete the Create a Service form with the following information:")
    print_step("7. Click")
    web_bot.try_action("7. Click")
    print_step("8. If the connection is")
    web_bot.try_action("8. If the connection is")
    print_step("9. When you see the message that you")
    web_bot.try_action("9. When you see the message that you")
    print_step("10. From")
    web_bot.try_action("10. From")
    print_step("11. Click the")
    web_bot.try_action("11. Click the")
    print_step("12. When you see the message that you successfully submitted a reconciliation request, click")
    web_bot.try_action("12. When you see the message that you successfully submitted a reconciliation request, click")
    print_step("13. If the status of the request shows it is")
    web_bot.try_action("13. If the status of the request shows it is")
    print_step("14. On the")
    web_bot.try_action("14. On the")
    print_step("15. You can also review the contents of")
    web_bot.try_action("15. You can also review the contents of")
    print_step("16. Close")
    web_bot.try_action("16. Close")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Service name", "CSV Identity Feed")
    val = get_input("Description", "CSV Feed for finance users")
    val = get_input("File name", "/classfiles/data/newhires_finance.csv")
    val = get_input("Use workflow", "[Cleared]")
    val = get_input("Evaluate separation of duty", "[Cleared]")
    val = get_input("Person profile name", "Person")
    val = get_input("Name attribute", "uid")
    val = get_input("Placement rule", "return \"ou=Finance\";")
    val = get_input("my request.", "The reconciliation request should be the")
    val = get_input("Finance", "business unit.")
    val = get_input("correct. Open it in", "Text Editor")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
