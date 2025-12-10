import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import platform
import subprocess

# --- 1. DETECT OS ---
current_os = platform.system() # Returns "Linux", "Windows", or "Darwin"

# --- 2. SIMULATION ENGINE (For Windows) ---
def get_simulated_output(command):
    if "useradd" in command: return f"User '{command.split()[-1]}' added to system.\n[root@rhel9 ~]#"
    elif "passwd" in command: return "passwd: all authentication tokens updated successfully."
    elif "userdel" in command: return "User deleted successfully."
    elif "touch" in command: return "" 
    elif "mkdir" in command: return ""
    elif "chmod" in command: return ""
    elif "ip addr" in command: 
        return """2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 state UP
    inet 192.168.1.10/24 brd 192.168.1.255 scope global dynamic"""
    elif "df -h" in command: 
        return """Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3        50G   5.2G   45G  11% /"""
    elif "systemctl" in command: return f"Redirecting to /bin/systemctl {command.split()[2]}..."
    else: return "Command executed."

# --- 3. RUN FUNCTION (Smart Mode) ---
def run_command(command_text):
    output_box.config(state="normal")
    output_box.insert(tk.END, f"[root@server ~]# {command_text}\n")
    
    result = ""
    
    if current_os == "Linux":
        # REAL MODE: Run actual command on Linux
        try:
            # subprocess.getoutput returns the shell output as a string
            result = subprocess.getoutput(command_text)
        except Exception as e:
            result = f"Error executing command: {e}"
    else:
        # SIMULATION MODE: Run fake output on Windows
        result = get_simulated_output(command_text)
    
    output_box.insert(tk.END, result + "\n\n")
    output_box.see(tk.END)
    output_box.config(state="disabled")

# --- 4. USER FUNCTIONS ---
def add_user():
    username = simpledialog.askstring("Input", "Enter Username:")
    if username: run_command(f"useradd {username}")

def set_password():
    username = simpledialog.askstring("Input", "Enter Username:")
    if username: run_command(f"passwd {username}")

def delete_user():
    username = simpledialog.askstring("Input", "Enter Username:")
    if username: run_command(f"userdel {username}")

# --- 5. FILE FUNCTIONS ---
def create_file():
    filename = simpledialog.askstring("Input", "Enter Filename:")
    if filename: run_command(f"touch {filename}")

def make_directory():
    dirname = simpledialog.askstring("Input", "Enter Directory Name:")
    if dirname: run_command(f"mkdir -p {dirname}")

def change_permission():
    path = simpledialog.askstring("Input", "File Path:")
    if path: run_command(f"chmod 755 {path}")

# --- 6. SYSTEM FUNCTIONS ---
def check_ip(): run_command("ip addr show")
def check_disk(): run_command("df -h")
def restart_service():
    service = simpledialog.askstring("Input", "Service Name:")
    if service: run_command(f"systemctl restart {service}")

# --- 7. GUI SETUP ---
root = tk.Tk()
title_text = f"RHCSA Tool - {current_os} Mode"
root.title(title_text)
root.geometry("700x550")

# Header
tk.Label(root, text="RHCSA Automation Hub", font=("Arial", 18, "bold"), bg="#222", fg="#0f0", pady=10).pack(fill="x")

# Tabs
tabs = ttk.Notebook(root)
tabs.pack(pady=10, expand=True, fill="both")

# Tab Frames
tab1 = tk.Frame(tabs); tabs.add(tab1, text="User Mgmt")
tab2 = tk.Frame(tabs); tabs.add(tab2, text="File Ops")
tab3 = tk.Frame(tabs); tabs.add(tab3, text="System Info")

# Buttons (Tab 1)
tk.Button(tab1, text="Add User", width=20, command=add_user).pack(pady=5)
tk.Button(tab1, text="Set Password", width=20, command=set_password).pack(pady=5)
tk.Button(tab1, text="Delete User", width=20, command=delete_user).pack(pady=5)

# Buttons (Tab 2)
tk.Button(tab2, text="Create File", width=20, command=create_file).pack(pady=5)
tk.Button(tab2, text="Make Directory", width=20, command=make_directory).pack(pady=5)
tk.Button(tab2, text="Change Perms", width=20, command=change_permission).pack(pady=5)

# Buttons (Tab 3)
tk.Button(tab3, text="Check IP", width=20, command=check_ip).pack(pady=5)
tk.Button(tab3, text="Check Storage", width=20, command=check_disk).pack(pady=5)
tk.Button(tab3, text="Restart Service", width=20, command=restart_service).pack(pady=5)

# Output
tk.Label(root, text="Terminal Output:", font=("Arial", 10, "bold")).pack(anchor="w", padx=10)
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.pack(fill="both", expand=True)

output_box = tk.Text(output_frame, height=10, bg="black", fg="#0f0", font=("Consolas", 10))
output_box.pack(fill="both", expand=True)

root.mainloop()
