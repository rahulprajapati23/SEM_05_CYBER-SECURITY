# How to Deploy a Directory to the Web (Step-by-Step Guide)

This guide explains how to take any folder on your computer and turn it into a live website using **Streamlit Cloud** and **GitHub**.

## Prerequisites
1.  **GitHub Account**: [Sign up here](https://github.com/join).
2.  **Streamlit Cloud Account**: [Sign up here](https://share.streamlit.io/) (Connect with GitHub).
3.  **Git Installed**: Ensure Git is installed on your computer.

---

## Step 1: Prepare Your Folder

1.  Open your folder in VS Code.
2.  Create a file named `requirements.txt` and add the following line:
    ```text
    streamlit
    ```
3.  Create a file named `streamlit_app.py`. This is the "brain" of your website. Copy the code below into it.

### `streamlit_app.py` Template
This code creates a file explorer with password protection.

```python
import streamlit as st
import os
import base64

def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True

def get_file_content_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(page_title="File Explorer", layout="wide")
    
    # UNCOMMENT THE LINE BELOW TO ENABLE PASSWORD PROTECTION
    # if not check_password(): st.stop()

    st.title("📂 File Explorer")
    base_dir = os.getcwd()

    if "current_path" not in st.session_state:
        st.session_state.current_path = base_dir

    # Navigation
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("🏠 Home"):
            st.session_state.current_path = base_dir
            st.rerun()
    with col2:
        if st.session_state.current_path != base_dir:
            if st.button("⬅️ Back"):
                st.session_state.current_path = os.path.dirname(st.session_state.current_path)
                st.rerun()

    # List files
    try:
        items = os.listdir(st.session_state.current_path)
    except:
        st.error("Error accessing directory")
        return

    dirs = [d for d in items if os.path.isdir(os.path.join(st.session_state.current_path, d)) and not d.startswith(".")]
    files = [f for f in items if os.path.isfile(os.path.join(st.session_state.current_path, f)) and not f.startswith(".") and f != "streamlit_app.py"]
    
    dirs.sort()
    files.sort()

    # Display Folders
    if dirs:
        st.subheader("📁 Folders")
        cols = st.columns(4)
        for i, d in enumerate(dirs):
            with cols[i % 4]:
                path = os.path.join(st.session_state.current_path, d)
                if st.button(f"📂 {d}", key=f"dir_{abs(hash(path))}"):
                    st.session_state.current_path = path
                    st.rerun()

    # Display Files
    if files:
        st.subheader("📄 Files")
        key = f"files_{abs(hash(st.session_state.current_path))}"
        selected = st.radio("Select file:", files, key=key)
        
        if selected:
            path = os.path.join(st.session_state.current_path, selected)
            st.markdown("---")
            st.header(f"📄 {selected}")
            
            # Download Button
            with open(path, "rb") as f:
                st.download_button(f"⬇️ Download {selected}", f, file_name=selected)

            # Preview
            _, ext = os.path.splitext(path)
            ext = ext.lower()
            if ext == ".pdf":
                b64 = get_file_content_as_base64(path)
                st.markdown(f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="800"></iframe>', unsafe_allow_html=True)
            elif ext in ['.png', '.jpg']:
                st.image(path)
            else:
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        st.code(f.read())
                except:
                    st.warning("Cannot preview this file.")

if __name__ == "__main__":
    main()
```

---

## Step 2: Push to GitHub

1.  **Create a Repository**: Go to [GitHub New Repo](https://github.com/new) and create a new repository (e.g., `my-folder-online`).
2.  **Initialize Git**: Open your terminal in the folder and run:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```
3.  **Connect and Push**:
    *(Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual details)*
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
    git branch -M main
    git push -u origin main
    ```

---

## Step 3: Deploy on Streamlit Cloud

1.  Go to [Streamlit Cloud](https://share.streamlit.io/).
2.  Click **"New app"**.
3.  Select your repository (`my-folder-online`).
4.  Set **Main file path** to `streamlit_app.py`.
5.  Click **"Deploy"**.

---

## Step 4: Add Password Protection (Optional)

If you enabled the password code in `streamlit_app.py`:

1.  On your deployed app, click **Settings** (three dots) -> **Settings** -> **Secrets**.
2.  Add your password like this:
    ```toml
    password = "your_secret_password"
    ```
3.  Click **Save**.

---

## Common Issues

*   **PDFs/Files Missing?**
    Check your `.gitignore` file. Make sure it doesn't contain `*.pdf` or the file extensions you are missing. If it does, remove that line and run:
    ```bash
    git add .
    git commit -m "Fix missing files"
    git push
    ```

---

## Step 5: Updating Your Website

Whenever you make changes to your files (add new files, edit code, etc.) on your computer, follow these 3 commands to update your live website:

1.  **Add changes**:
    ```bash
    git add .
    ```
2.  **Save changes (Commit)**:
    ```bash
    git commit -m "Description of what you changed"
    ```
3.  **Upload (Push)**:
    ```bash
    git push
    ```

Streamlit Cloud will detect the new code and automatically update your website in about 1-2 minutes.

> **Note:** This same process applies if you **move**, **rename**, or **delete** files. Git will detect the changes when you run `git add .`.
