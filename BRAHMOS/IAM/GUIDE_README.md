
# BRAHMOS Automation Scripts - User Guide

This folder contains automated Python scripts generated from your ISIM/IAM PDF lab exercises.

## 🚀 Features
1.  **Automated CLI Commands**: 
    -   Commands like `idsicrt`, `ibmslapd`, and `ldapsearch` are automatically executed when the script runs on the ISIM server.
    -   No manual typing required.
2.  **Automated Web Actions (Selenium)**:
    -   The scripts attempt to launch **Google Chrome** to perform web steps (Login, Click, Create).
    -   It uses "Smart Text Matching" to find buttons. 
    -   *Fallback*: If it can't find a button (e.g., complex UI), it prints a warning and lets you click it manually. **The script will NOT crash.**
3.  **Interactive Data Entry**:
    -   For form fields (names, passwords), the script asks you to verify or enter the value.

## 📋 Prerequisites
To run these scripts successfully "without verification errors", you need:
1.  **Environment**: The IBM ISIM Virtual Machine (Linux/Windows) where the software is installed.
2.  **Python 3**: Installed on that machine.
3.  **Firefox Browser**: The standard browser in the ISIM environment.
4.  **GeckoDriver**: 
    -   Must match your Firefox version.
    -   Must be in your system `PATH` (e.g., `/usr/bin/` or same folder as script).
    -   *If missing*: The script will default to text-only mode.

## 🛠️ How to Run
1.  Open your terminal on the ISIM machine.
2.  Navigate to the specific exercise folder (e.g., `cd "IAM Exercise 3"`).
3.  Run the script:
    ```bash
    python 02_Exercise_2__Creating_users.py
    ```
4.  Follow the on-screen prompts.

## ❓ FAQ
**Q: The script says "Web Action Failed: Unable to locate element..."**  
A: This is normal for complex pages. Since we don't have the exact source code of the ISIM webpage, the "smart guess" might fail. **Just perform that single click manually** in the browser, and the script will continue automating the next steps!

**Q: 'idsicrt' command not found?**  
A: Ensure you are logged in as the correct user (e.g., `root` or `idsldap`) and that the IBM SDS bin directory is in your `PATH`.
