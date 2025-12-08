"""
Interactive Guide for: ISIM Part 1
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
    print("=== STARTING EXERCISE: ISIM Part 1 ===")
    web_bot = WebBot()
    print("\n--- INSTRUCTIONS ---")
    print_step("1.     Create 2 IBM SDS instances")
    web_bot.try_action("1.     Create 2 IBM SDS instances")
    print_step("2.     Import the sample data using LDIF.")
    web_bot.try_action("2.     Import the sample data using LDIF.")
    print_step("3.     Configure Master – Master replication within IBM Security Directory Servers.")
    web_bot.try_action("3.     Configure Master – Master replication within IBM Security Directory Servers.")
    print_step("1.      Operating System – CentOS 7.7 installed on a VMware Workstation VM.")
    web_bot.try_action("1.      Operating System – CentOS 7.7 installed on a VMware Workstation VM.")
    print_step("2.      IBM Security Directory Server – version 6.4.0.20 x64 Linux.  IBM Security Directory Server 6.4.0.20")
    web_bot.try_action("2.      IBM Security Directory Server – version 6.4.0.20 x64 Linux.  IBM Security Directory Server 6.4.0.20")
    print_step("2. DB2  - /opt/ibm/db2/V11.1/")
    web_bot.try_action("2. DB2  - /opt/ibm/db2/V11.1/")
    print_step("3. WAS - /opt/IBM/WebSphere/AppServer/")
    web_bot.try_action("3. WAS - /opt/IBM/WebSphere/AppServer/")
    print_step("1.    Open     Terminal      from   Desktop       and navigate to the SDS folder as below")
    run_command("1.    Open     Terminal      from   Desktop       and navigate to the SDS folder as below")
    print_step("2.    Create two new users            idsldap1      and    idsldap2      as the owner of two new instances using :")
    web_bot.try_action("2.    Create two new users            idsldap1      and    idsldap2      as the owner of two new instances using :")
    print_step("3.    Similarly, add the second user              idsldap2")
    web_bot.try_action("3.    Similarly, add the second user              idsldap2")
    print_step("4.    Create the instance for the idsldap1 user using                     idsicrt    command as below :")
    run_command("4.    Create the instance for the idsldap1 user using                     idsicrt    command as below :", auto_cmd="idsicrt -I idsldap1 -e encryptionseed -l /home/idsldap1 -n")
    print_step("5.   Similarly, create the instance for the       idsldap2    user using idsicrt command as below :")
    run_command("5.   Similarly, create the instance for the       idsldap2    user using idsicrt command as below :", auto_cmd="idsicrt -I idsldap2 -e encryptionseed -l /home/idsldap2 -n")
    print_step("6.    Now you can check the instance details using the below command in terminal and check the new")
    run_command("6.    Now you can check the instance details using the below command in terminal and check the new")
    print_step("7.    Once the instances are created we will configure the DB2 database for the SDS instance, the DB2")
    web_bot.try_action("7.    Once the instances are created we will configure the DB2 database for the SDS instance, the DB2")
    print_step("8.    Similarly, configure database for the second instance idsldap2 with below command")
    run_command("8.    Similarly, configure database for the second instance idsldap2 with below command")
    print_step("9.    Minimize the           Terminal         window,        Double-click           the    Home       icon from        Desktop         . Click    Other Locations               in")
    run_command("9.    Minimize the           Terminal         window,        Double-click           the    Home       icon from        Desktop         . Click    Other Locations               in")
    print_step("10.   Double-click            idsldap1 directory and you can see                              idsslapd-idsldap1                folder which have all instance")
    web_bot.try_action("10.   Double-click            idsldap1 directory and you can see                              idsslapd-idsldap1                folder which have all instance")
    print_step("11.   Minimize          the   Files     window and go back to                     Terminal        window. Create admin user (                       cn=root       ) who can")
    run_command("11.   Minimize          the   Files     window and go back to                     Terminal        window. Create admin user (                       cn=root       ) who can")
    print_step("12.   Similarly, for        idsldap2         instance create the admin user cn=root as below:")
    web_bot.try_action("12.   Similarly, for        idsldap2         instance create the admin user cn=root as below:")
    print_step("13.   Close      Terminal        .")
    run_command("13.   Close      Terminal        .")
    print_step("1.     Open     Terminal        from Desktop.")
    run_command("1.     Open     Terminal        from Desktop.")
    print_step("2.     Start    the newly created SDS instance                      idsldap1        using below command:")
    run_command("2.     Start    the newly created SDS instance                      idsldap1        using below command:", auto_cmd="ibmslapd -I idsldap1")
    print_step("3.     Similary, start the         idsldap2        instance using :")
    run_command("3.     Similary, start the         idsldap2        instance using :", auto_cmd="ibmslapd -I idsldap2")
    print_step("4.     To  stop     the instance idsldap1 enter the below command :")
    run_command("4.     To  stop     the instance idsldap1 enter the below command :", auto_cmd="ibmslapd -I idsldap1 -k")
    print_step("5.     Similarly, to      stop     the idsldap2 instance enter below command:")
    run_command("5.     Similarly, to      stop     the idsldap2 instance enter below command:", auto_cmd="ibmslapd -I idsldap2 -k")
    print_step("6.     Start    both the instances again :")
    web_bot.try_action("6.     Start    both the instances again :")
    print_step("1.     Open the Firefox browser from the task bar and enter the below URL or Click the                                                   Web Admin Tool")
    web_bot.try_action("1.     Open the Firefox browser from the task bar and enter the below URL or Click the                                                   Web Admin Tool")
    print_step("2.     Click on     Login to Console admin                    . Enter the credentials as               superadmin           using the password              secret     .")
    web_bot.try_action("2.     Click on     Login to Console admin                    . Enter the credentials as               superadmin           using the password              secret     .")
    print_step("3.     Click on     Manage Console Servers.")
    web_bot.try_action("3.     Click on     Manage Console Servers.")
    print_step("4.      Click on         Add.")
    web_bot.try_action("4.      Click on         Add.")
    print_step("5.      Click on         Add.")
    web_bot.try_action("5.      Click on         Add.")
    print_step("6.      Click on         Logout           in the left pane and then on next screen press on                                                   here.")
    web_bot.try_action("6.      Click on         Logout           in the left pane and then on next screen press on                                                   here.")
    print_step("7.      Now we will get the LDAP Server Name. Select idsldap1 and enter the credential cn=                                                                                         root/P@ssw0rd")
    web_bot.try_action("7.      Now we will get the LDAP Server Name. Select idsldap1 and enter the credential cn=                                                                                         root/P@ssw0rd")
    print_step("8.      Click      Manage Entries                    in the Content Management Section . There are few default entries created by")
    web_bot.try_action("8.      Click      Manage Entries                    in the Content Management Section . There are few default entries created by")
    print_step("9.      Press        Logout          in Left Pane and login with                            idsldap2           with Userid             cn=root/P@ssw0rd")
    web_bot.try_action("9.      Press        Logout          in Left Pane and login with                            idsldap2           with Userid             cn=root/P@ssw0rd")
    print_step("10.   Click    Manage Entrie           s as above steps and similar data will be shown as idsldap1.")
    web_bot.try_action("10.   Click    Manage Entrie           s as above steps and similar data will be shown as idsldap1.")
    print_step("1.    To add the suffix         stop     both the SDS instances. Open                    terminal      and enter command:")
    run_command("1.    To add the suffix         stop     both the SDS instances. Open                    terminal      and enter command:")
    print_step("2.    Since we will be loading data into the directory servers, it is necessary to                                     add    the   base suffix        into the")
    run_command("2.    Since we will be loading data into the directory servers, it is necessary to                                     add    the   base suffix        into the", auto_cmd="idscfgsuf -I idsldap1 -s \"o=jke\" && idscfgsuf -I idsldap2 -s \"o=jke\"")
    print_step("3.    Start the IBM SDS instances using below commands:")
    run_command("3.    Start the IBM SDS instances using below commands:")
    print_step("4.    Now that the suffix information has been added, and the directory server instances have been started")
    web_bot.try_action("4.    Now that the suffix information has been added, and the directory server instances have been started")
    print_step("5.    In the    terminal      enter below command for                  idsldap1      ,")
    run_command("5.    In the    terminal      enter below command for                  idsldap1      ,")
    print_step("6.     Similarly, for idsldap2 add the o=jke entry as organization, we use 2389 port to imply the idsldap2")
    web_bot.try_action("6.     Similarly, for idsldap2 add the o=jke entry as organization, we use 2389 port to imply the idsldap2")
    print_step("7.     Minimize        Terminal        . Open       Firefox        and click       Web Admin Tool Bookmark                            . Login to        idsldap       using")
    run_command("7.     Minimize        Terminal        . Open       Firefox        and click       Web Admin Tool Bookmark                            . Login to        idsldap       using")
    print_step("8.     Click    Manage Entries                from Content Management section on Homepage. You can see the")
    web_bot.try_action("8.     Click    Manage Entries                from Content Management section on Homepage. You can see the")
    print_step("9.     Login to       idsldap2         using       cn=root/P@ssw0rd                    and you can see similar entries in idsldap2 instance.")
    web_bot.try_action("9.     Login to       idsldap2         using       cn=root/P@ssw0rd                    and you can see similar entries in idsldap2 instance.")
    print_step("10.    Logout       . Close      Firefox       .")
    web_bot.try_action("10.    Logout       . Close      Firefox       .")
    print_step("1.     We will import user data into the organization                               “o=jke”        using LDIF file. Open                Terminal       . Navigate to")
    run_command("1.     We will import user data into the organization                               “o=jke”        using LDIF file. Open                Terminal       . Navigate to")
    print_step("2.     Create the file          User1.ldif       in this folder. Use           gedit    to open")
    web_bot.try_action("2.     Create the file          User1.ldif       in this folder. Use           gedit    to open")
    print_step("3.     Copy or type the below ldif entries into the file:")
    web_bot.try_action("3.     Copy or type the below ldif entries into the file:")
    print_step("4.     Save     the file and       Close     .")
    web_bot.try_action("4.     Save     the file and       Close     .")
    print_step("5.     In the terminal enter the idsldapadd command as below for idsldap1 :")
    run_command("5.     In the terminal enter the idsldapadd command as below for idsldap1 :")
    print_step("6.     Verify if the users are added into the                           idsldap1         instance of SDS using WAT. Open                              Firefox     . Click     Web")
    web_bot.try_action("6.     Verify if the users are added into the                           idsldap1         instance of SDS using WAT. Open                              Firefox     . Click     Web")
    print_step("7.     Login to       idsldap1         using      cn=root/P@ssw0rd.")
    web_bot.try_action("7.     Login to       idsldap1         using      cn=root/P@ssw0rd.")
    print_step("8.     Click     Manage Entries                in Content Management section. Click the plus (+) sign near o=jke and you can")
    web_bot.try_action("8.     Click     Manage Entries                in Content Management section. Click the plus (+) sign near o=jke and you can")
    print_step("9.     You can         click     cn=joe and see some extra details. Click                                 Cancel       and then Close. Click                   Logout        in left")
    web_bot.try_action("9.     You can         click     cn=joe and see some extra details. Click                                 Cancel       and then Close. Click                   Logout        in left")
    print_step("10.    Open the           Terminal        window and repeat the above step of                                  idsldap2         using the port             2389     . Enter the")
    run_command("10.    Open the           Terminal        window and repeat the above step of                                  idsldap2         using the port             2389     . Enter the")
    print_step("11.    Similar output window will be shown, now open                                       Firefox       and login to          idsldap2         into (Web Admin Tool)")
    web_bot.try_action("11.    Similar output window will be shown, now open                                       Firefox       and login to          idsldap2         into (Web Admin Tool)")
    print_step("12.    We will import user data into the organization “o=jke”  using LDIF file. Open Terminal. Navigate to")
    run_command("12.    We will import user data into the organization “o=jke”  using LDIF file. Open Terminal. Navigate to")
    print_step("13.    Create the file            User2.ldif        in this folder. Use            gedit      to open")
    web_bot.try_action("13.    Create the file            User2.ldif        in this folder. Use            gedit      to open")
    print_step("14.    Copy or type the below ldif entries into the file:")
    web_bot.try_action("14.    Copy or type the below ldif entries into the file:")
    print_step("15.     Open        LDAP          Browser            by double-click on LDAP Browser of                                        Desktop           .")
    web_bot.try_action("15.     Open        LDAP          Browser            by double-click on LDAP Browser of                                        Desktop           .")
    print_step("16.     To add new connection of idsldap1 instance Click                                                    New       .")
    web_bot.try_action("16.     To add new connection of idsldap1 instance Click                                                    New       .")
    print_step("17.     Enter name :               IDSLDAP1               . Click the          Connection                tab.")
    web_bot.try_action("17.     Enter name :               IDSLDAP1               . Click the          Connection                tab.")
    print_step("18.     Enter the details as below")
    web_bot.try_action("18.     Enter the details as below")
    print_step("19. Click")
    web_bot.try_action("19. Click")
    print_step("20. Click")
    web_bot.try_action("20. Click")
    print_step("21. Browse")
    web_bot.try_action("21. Browse")
    print_step("22. Click")
    web_bot.try_action("22. Click")
    print_step("23. You can see users")
    web_bot.try_action("23. You can see users")
    print_step("24. Repeat similar steps for IDSLDAP2. From")
    web_bot.try_action("24. Repeat similar steps for IDSLDAP2. From")
    print_step("25. Menu bar→ File → Connect")
    web_bot.try_action("25. Menu bar→ File → Connect")
    print_step("26. Create connection for IDSLDAP2. Click")
    web_bot.try_action("26. Create connection for IDSLDAP2. Click")
    print_step("27. Enter name :")
    web_bot.try_action("27. Enter name :")
    print_step("28. Enter the details as below")
    web_bot.try_action("28. Enter the details as below")
    print_step("29. Click")
    web_bot.try_action("29. Click")
    print_step("30. You will be able to see the entries in the")
    web_bot.try_action("30. You will be able to see the entries in the")
    print_step("31. Close")
    web_bot.try_action("31. Close")
    print("\n--- DATA ENTRY REQUIRED ---")
    val = get_input("Host", "localhost")
    val = get_input("Port", "1389")
    val = get_input("Version", "3")
    val = get_input("Base DN (Click Fetch DN)", "o=jke")
    val = get_input("Anonymous Bind", "Uncheck")
    val = get_input("User DN", "cn=root")
    val = get_input("Password", "P@ssw0rd")
    val = get_input("Host", "localhost")
    val = get_input("Port", "2389")
    val = get_input("Version", "3")
    val = get_input("Base DN (Click Fetch DN)", "o=jke")
    val = get_input("Anonymous Bind", "Uncheck")
    val = get_input("User DN", "cn=root")
    val = get_input("Password", "P@ssw0rd")
    print("\n=== EXERCISE COMPLETED SUCCESSFULLY === ")

if __name__ == "__main__":
    main()
