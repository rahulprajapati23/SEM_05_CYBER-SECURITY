# Deployment Guide: SEM_05 File Explorer

This guide explains how to deploy the **SEM_05 File Explorer** with Role-Based Access Control (RBAC).

## 1. Prerequisites
- **Python 3.11** (Recommended)
- **Streamlit** installed (`pip install streamlit`)
- A GitHub account (for Streamlit Cloud deployment)

## 2. Local Setup

### Installation
1.  Clone or download this repository.
2.  Open a terminal in the project folder.
3.  Install dependencies:
    ```powershell
    pip install streamlit
    ```

### Configuration (Secrets)
The app uses a **secrets file** to store passwords for the Root and Guest users. This file is **NOT** committed to GitHub for security.

1.  Create a folder named `.streamlit` in the project root.
2.  Inside it, create a file named `secrets.toml`.
3.  Add your passwords:
    ```toml
    # .streamlit/secrets.toml
    root_password = "your_secure_root_password"
    guest_password = "your_guest_password"
    ```

### Running Locally
Run the app with:
```powershell
streamlit run streamlit_app.py
```

## 3. Deployment to Streamlit Cloud

### Step 1: Push to GitHub
1.  Initialize Git (if not done): `git init`
2.  Add files: `git add .`
3.  **Important**: Ensure `.streamlit/secrets.toml` is in your `.gitignore` (it should be by default).
4.  Commit and push to a new GitHub repository.

### Step 2: Deploy
1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click **New app**.
3.  Select your repository, branch, and main file (`streamlit_app.py`).
4.  Click **Deploy**.

### Step 3: Configure Secrets on Cloud
The app will likely fail to start initially because it's missing the passwords.

1.  On your app's dashboard, click the **Settings** (three dots) menu.
2.  Select **Settings** -> **Secrets**.
3.  Paste the contents of your local `secrets.toml` into the text area:
    ```toml
    root_password = "your_secure_root_password"
    guest_password = "your_guest_password"
    ```
4.  Click **Save**. The app will restart automatically.

## 4. Usage
- **Root User**: Full access (View + Download).
- **Guest User**: View only (No Download, Copy Protection enabled).
