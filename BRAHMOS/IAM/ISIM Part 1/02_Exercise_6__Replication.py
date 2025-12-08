"""
Interactive Guide for: Exercise 6 – Replication
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
    print("=== STARTING EXERCISE: Exercise 6 – Replication ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1. Open")
    web_bot.try_action("1. Open")
    print_step("2. Login to LDAPServer")
    web_bot.try_action("2. Login to LDAPServer")
    print_step("3. Select")
    web_bot.try_action("3. Select")
    print_step("4. Click the")
    web_bot.try_action("4. Click the")
    print_step("5. Click the")
    web_bot.try_action("5. Click the")
    print_step("6. In")
    web_bot.try_action("6. In")
    print_step("7. Click the")
    web_bot.try_action("7. Click the")
    print_step("8. Add the credential information")
    web_bot.try_action("8. Add the credential information")
    print_step("9. Click the")
    web_bot.try_action("9. Click the")
    print_step("10. Enter the Simple Bind information")
    web_bot.try_action("10. Enter the Simple Bind information")
    print_step("11. Click the")
    web_bot.try_action("11. Click the")
    print_step("12. On next screen click the")
    web_bot.try_action("12. On next screen click the")
    print_step("13. Now that the credentials are configured for the")
    web_bot.try_action("13. Now that the credentials are configured for the")
    print_step("14. Under")
    web_bot.try_action("14. Under")
    print_step("15. With the")
    web_bot.try_action("15. With the")
    print_step("16. From the “Topology for the selected subtree” section, click on")
    web_bot.try_action("16. From the “Topology for the selected subtree” section, click on")
    print_step("17. Click the")
    web_bot.try_action("17. Click the")
    print_step("18. On the Add master screen enter the following information:")
    web_bot.try_action("18. On the Add master screen enter the following information:")
    print_step("19. Credential Object")
    web_bot.try_action("19. Credential Object")
    print_step("20. In the Select Credential screen, select the")
    web_bot.try_action("20. In the Select Credential screen, select the")
    print_step("21. Click the")
    web_bot.try_action("21. Click the")
    print_step("22. The Add Replica – Additional screen allows the administrator to add further details about the replica")
    web_bot.try_action("22. The Add Replica – Additional screen allows the administrator to add further details about the replica")
    print_step("23. Select the")
    web_bot.try_action("23. Select the")
    print_step("24. Click the")
    web_bot.try_action("24. Click the")
    print_step("25. Select O=JKE")
    web_bot.try_action("25. Select O=JKE")
    print_step("26. Select the")
    web_bot.try_action("26. Select the")
    print_step("27. Following image shows the operation :")
    web_bot.try_action("27. Following image shows the operation :")
    print_step("28. Click")
    web_bot.try_action("28. Click")
    print_step("29. You will get the following message")
    web_bot.try_action("29. You will get the following message")
    print_step("30. Click")
    web_bot.try_action("30. Click")
    print_step("31. In Replication Management go to")
    web_bot.try_action("31. In Replication Management go to")
    print_step("32. Click")
    web_bot.try_action("32. Click")
    print_step("33. The replication is now started from")
    web_bot.try_action("33. The replication is now started from")
    print_step("34. Click")
    web_bot.try_action("34. Click")
    print_step("35. Login to")
    web_bot.try_action("35. Login to")
    print_step("36. In Replication Management go to")
    web_bot.try_action("36. In Replication Management go to")
    print_step("37. The queue is in supended state, select the")
    web_bot.try_action("37. The queue is in supended state, select the")
    print_step("38. Click")
    web_bot.try_action("38. Click")
    print_step("39. Replication from IDSLDAP2 to IDSLDAP1 is")
    web_bot.try_action("39. Replication from IDSLDAP2 to IDSLDAP1 is")
    print_step("40. Logout")
    web_bot.try_action("40. Logout")
    print_step("41. In this we will check if replication works fine for modifications. n the SDS Web Administration Tool,")
    web_bot.try_action("41. In this we will check if replication works fine for modifications. n the SDS Web Administration Tool,")
    print_step("42. Select")
    web_bot.try_action("42. Select")
    print_step("43. Select user")
    web_bot.try_action("43. Select user")
    print_step("44. Modify the sn attribute to some new value , say “walter” to “")
    web_bot.try_action("44. Modify the sn attribute to some new value , say “walter” to “")
    print_step("45. Logout")
    web_bot.try_action("45. Logout")
    print_step("46. Login using")
    web_bot.try_action("46. Login using")
    print_step("47. Select")
    web_bot.try_action("47. Select")
    print_step("48. Select user")
    web_bot.try_action("48. Select user")
    print_step("49. Now you can see sn as")
    web_bot.try_action("49. Now you can see sn as")
    print_step("50. Press")
    web_bot.try_action("50. Press")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Note", ":")
    val = get_input("open. In that case, clear the browser cache.", "(Ctr+Shift+Del) Clear Data")
    val = get_input("a. Select", "o=jke")
    val = get_input("b. Check to ensure", "ldap://localhost:1389")
    val = get_input("a.", "Select")
    val = get_input("b. Click the", "Show Credentials")
    val = get_input("Credential Name –", "cn=replicamanager")
    val = get_input("Authentication method –", "Simple bind")
    val = get_input("Bind DN –", "cn=replicamanager,o=jke")
    val = get_input("Bind password –", "P@ssw0rd")
    val = get_input("Confirm password –", "P@ssw0rd")
    val = get_input("topology", ".")
    val = get_input("Server Hostname:port – Select", "localhost:2389")
    val = get_input("Enable SSL –", "leave unchecked")
    val = get_input("Peer Master –", "leave blank")
    val = get_input("Server ID –", "click the Get server ID button")
    val = get_input("Description –", "leave blank")
    val = get_input("Credentials", "button,")
    val = get_input("replicamanager", "credential displayed, click the")
    val = get_input("performance.", "On this screen, the only change that will be made for this lab is to add the")
    val = get_input("Consumer admin DN –", "cn=root")
    val = get_input("Consumer admin password –", "P@ssw0rd")
    val = get_input("Consumer admin DN –", "cn=root")
    val = get_input("Consumer admin password –", "P@ssw0rd")
    val = get_input("Note", ":")
    val = get_input("Radio", "button")
    val = get_input("Note", ":")
    val = get_input("IDSLDAP2 server. We just need to", "start the queue")
    val = get_input("Login to", "idsldap1")
    val = get_input("Note", ":")
    val = get_input("that we created previously. Also try to create the replication between the subtree", "CN=IBMPOLICIES")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
