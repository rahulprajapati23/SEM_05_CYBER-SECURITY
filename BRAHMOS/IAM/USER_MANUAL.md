# 📘 ISIM Automation Scripts - User Manual

## 🎯 What These Scripts Do
These Python scripts are your **"Robot Assistant"** for the ISIM PDF labs. 
Instead of manually typing every command and clicking every button, the script does it for you.

1.  **Auto-Types Commands**: It runs complex CLI commands (like `idsicrt`, `ldapsearch`) automatically in the terminal.
2.  **Auto-Clicks Webpages**: It opens Firefox and clicks buttons (like "Create", "Submit") for you.
3.  **Guides You**: It shows you exactly which step you are on, so you don't get lost in the PDF.

---

## 👷 Your Role (The Supervisor)
You are the supervisor. The robot does the work, but you must approve it.

### 1. Press "Enter" to Verify Data
The script will ask for confirmation before entering data.
**Example:**
> `[INPUT] Field: Password`  
> `Enter value (Suggested: P@ssw0rd):`

*   **What you do**: Just press **ENTER**.
*   (The script fills in the suggested value for you).

### 2. "Rescue" the Web Bot
Sometimes, the ISIM webpage might load slowly or have a tricky button that the bot can't find.
**Example:**
> `Web Action Failed: Unable to locate element "Click Submit"`

*   **What you do**: Don't panic! Just click the "Submit" button **manually** in the Firefox window.
*   The script will verify the step is done and continue to the next one.

---

## 🚀 How to Run (Step-by-Step)

### Prerequisites
1.  **IBM ISIM Lab Environment** (VM).
2.  **Firefox Browser** installed.
3.  **GeckoDriver** (Firefox Driver) placed in this folder or your system PATH.
4.  **Python** installed.

### Setup
1.  Open Terminal in this folder (`BRAHMOS/IAM`).
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running an Exercise
1.  Navigate to the exercise folder, for example `ISIM Part 1`.
    ```bash
    cd "ISIM Part 1"
    ```
2.  Run the script for the first part:
    ```bash
    python 01_ISIM_Part_1.py
    ```
3.  **Follow the on-screen prompts.**
4.  If the PDF has a second part (like Replication), run that next:
    ```bash
    python 02_Exercise_6__Replication.py
    ```

---

## 🧹 Troubleshooting
*   **Netscape/Firefox Error**: If the browser doesn't open, ensure `geckodriver` is installed. If not, you can just read the text instructions in the terminal and click manually.
*   **Command Not Found**: Ensure you are running as `root` (or the correct user) on the ISIM machine.
