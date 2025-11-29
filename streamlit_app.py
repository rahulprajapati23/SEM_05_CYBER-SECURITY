import streamlit as st
import os
import base64

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

def get_file_content_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(page_title="SEM_05 File Explorer", layout="wide")
    
    if not check_password():
        st.stop()  # Do not continue if check_password is not True.

    st.title("📂 SEM_05 File Explorer")

    # Base directory is the current directory where the app is running
    base_dir = os.getcwd()
    
    # Sidebar for navigation
    st.sidebar.header("Navigation")
    
    # Get all subdirectories and files
    items = []
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories and the app file itself
        if ".git" in root or "__pycache__" in root:
            continue
            
        for name in files:
            if name == "streamlit_app.py" or name.startswith("."):
                continue
            path = os.path.join(root, name)
            rel_path = os.path.relpath(path, base_dir)
            items.append(rel_path)
            
    # Filter items
    search_query = st.sidebar.text_input("Search files", "")
    if search_query:
        items = [item for item in items if search_query.lower() in item.lower()]
    
    if not items:
        st.info("No files found.")
        return

    selected_file = st.sidebar.radio("Select a file", items)

    if selected_file:
        file_path = os.path.join(base_dir, selected_file)
        st.header(f"📄 {selected_file}")
        
        # Determine file extension
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        
        # Display content based on file type
        try:
            if ext in ['.py', '.c', '.cpp', '.java', '.js', '.html', '.css', '.txt', '.md', '.json', '.xml']:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                st.code(content, language=ext[1:] if ext.startswith('.') else ext)
                
            elif ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
                st.image(file_path)
                
            elif ext in ['.pdf']:
                # Embedding PDF might be tricky, providing download link is safer
                st.info("PDF preview not supported directly. Please download to view.")
                
            else:
                st.warning("File type not supported for direct preview.")

            # Download button
            with open(file_path, "rb") as f:
                file_bytes = f.read()
            st.download_button(
                label="Download File",
                data=file_bytes,
                file_name=os.path.basename(file_path),
                mime="application/octet-stream"
            )
            
        except Exception as e:
            st.error(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
