import streamlit as st
import os
import base64

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["root_password"]:
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = "root"
            del st.session_state["password"]  # don't store password
        elif st.session_state["password"] == st.secrets["guest_password"]:
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = "guest"
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

def inject_guest_css():
    """Injects CSS to restrict copy/paste and right-click for guest users."""
    st.markdown(
        """
        <style>
        /* Disable text selection */
        body {
            -webkit-user-select: none; /* Safari */
            -ms-user-select: none; /* IE 10 and IE 11 */
            user-select: none; /* Standard syntax */
        }
        /* Attempt to disable right-click context menu (not foolproof in all browsers via CSS, but helps) */
        /* Note: JS is better for this, but Streamlit allows limited JS injection via components. 
           We will use a simple overlay or just rely on the user-select for now as a deterrent. */
        </style>
        <script>
        document.addEventListener('contextmenu', event => event.preventDefault());
        </script>
        """,
        unsafe_allow_html=True
    )
    # Note: Streamlit's st.markdown with unsafe_allow_html=True allows <script> tags but they might not execute 
    # as expected in all contexts due to iframe sandboxing or re-renders. 
    # A better approach for right-click disable in Streamlit is often just CSS overlays or accepting it's "best effort".
    # We will try to inject a script tag that disables context menu.
    
    st.components.v1.html(
        """
        <script>
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
        });
        document.addEventListener('keydown', function(e) {
            // Disable F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U
            if (e.keyCode == 123) { // F12
                e.preventDefault();
            }
            if (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) { // Ctrl+Shift+I/J
                e.preventDefault();
            }
            if (e.ctrlKey && e.keyCode == 85) { // Ctrl+U
                e.preventDefault();
            }
        });
        </script>
        """,
        height=0,
        width=0,
    )

def get_file_content_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(page_title="SEM_05 File Explorer", layout="wide")
    
    if not check_password():
        st.stop()

    # Inject Guest CSS if applicable
    if st.session_state.get("user_role") == "guest":
        inject_guest_css()

    st.title("📂 SEM_05 File Explorer")

    # Base directory is the current directory where the app is running
    base_dir = os.getcwd()

    # Initialize session state for current path
    if "current_path" not in st.session_state:
        st.session_state.current_path = base_dir

    # Calculate relative path for display
    rel_path = os.path.relpath(st.session_state.current_path, base_dir)
    if rel_path == ".":
        display_path = "Root"
    else:
        display_path = rel_path
    
    st.markdown(f"### 📍 Current Path: `{display_path}`")

    # Navigation controls
    col1, col2, col3 = st.columns([1, 1, 4])
    
    with col1:
        if st.button("🏠 Home"):
            st.session_state.current_path = base_dir
            st.rerun()
            
    with col2:
        if st.session_state.current_path != base_dir:
            if st.button("⬅️ Back"):
                st.session_state.current_path = os.path.dirname(st.session_state.current_path)
                st.rerun()

    # Get contents of current path
    try:
        items = os.listdir(st.session_state.current_path)
    except Exception as e:
        st.error(f"Error accessing directory: {e}")
        return

    # Separate directories and files
    dirs = []
    files = []
    for item in items:
        # Skip hidden files/dirs
        if item.startswith(".") or item == "__pycache__" or item == "streamlit_app.py":
            continue
            
        full_path = os.path.join(st.session_state.current_path, item)
        if os.path.isdir(full_path):
            dirs.append(item)
        else:
            files.append(item)
            
    dirs.sort()
    files.sort()

    if not dirs and not files:
        st.info("This folder is empty.")

    # Display Directories
    if dirs:
        st.subheader("📁 Folders")
        cols = st.columns(4)
        for i, d in enumerate(dirs):
            with cols[i % 4]:
                # Use full path hash for unique key to prevent collisions
                full_dir_path = os.path.join(st.session_state.current_path, d)
                if st.button(f"📂 {d}", key=f"dir_{abs(hash(full_dir_path))}"):
                    st.session_state.current_path = full_dir_path
                    st.rerun()

    # Display Files
    if files:
        st.subheader("📄 Files")
        
        # File selection with unique key based on path
        # Use a hash of the path to ensure the key is valid and unique
        files_key = f"files_{abs(hash(st.session_state.current_path))}"
        selected_file = st.radio("Select a file to view:", files, key=files_key)
        
        if selected_file:
            file_path = os.path.join(st.session_state.current_path, selected_file)
            st.markdown("---")
            st.header(f"📄 {selected_file}")
            
            # Download button (Only for Root)
            if st.session_state.get("user_role") == "root":
                try:
                    with open(file_path, "rb") as f:
                        file_bytes = f.read()
                    st.download_button(
                        label=f"⬇️ Download {selected_file}",
                        data=file_bytes,
                        file_name=selected_file,
                        mime="application/octet-stream"
                    )
                except Exception as e:
                    st.error(f"Error preparing download: {e}")
            elif st.session_state.get("user_role") == "guest":
                st.info("🔒 Download disabled for guest users.")

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
                    # Embed PDF using base64
                    base64_pdf = get_file_content_as_base64(file_path)
                    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
                    st.markdown(pdf_display, unsafe_allow_html=True)
                    
                else:
                    st.info("Preview not available for this file type. Please use the download button above.")
            
            except Exception as e:
                st.error(f"Error reading file preview: {e}")

if __name__ == "__main__":
    main()
