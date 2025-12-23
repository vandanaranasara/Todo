import streamlit as st
import requests
from typing import Optional
import os

# Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Initialize session state
if "access_token" not in st.session_state:
    st.session_state.access_token = None
if "username" not in st.session_state:
    st.session_state.username = None
if "user_id" not in st.session_state:
    st.session_state.user_id = None

def get_auth_headers() -> dict:
    """Get authorization headers with token if available"""
    if st.session_state.access_token:
        return {"Authorization": f"Bearer {st.session_state.access_token}"}
    return {}

def register_user(username: str, email: str, password: str) -> dict:
    """Register a new user"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/",
            json={"username": username, "email": email, "password": password}
        )
        return {"success": response.status_code == 200, "data": response.json(), "status": response.status_code}
    except Exception as e:
        return {"success": False, "error": str(e), "status": 500}

def login_user(username: str, password: str) -> dict:
    """Login user and get access token"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/auth/login",
            data={"username": username, "password": password}
        )
        if response.status_code == 200:
            return {"success": True, "data": response.json()}
        return {"success": False, "error": response.json().get("detail", "Login failed"), "status": response.status_code}
    except Exception as e:
        return {"success": False, "error": str(e), "status": 500}

def get_todos() -> list:
    """Get all todos for current user"""
    try:
        response = requests.get(
            f"{API_BASE_URL}/todos/",
            headers=get_auth_headers()
        )
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        st.error(f"Error fetching todos: {str(e)}")
        return []

def create_todo(title: str) -> dict:
    """Create a new todo"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/todos/",
            json={"title": title},
            headers=get_auth_headers()
        )
        return {"success": response.status_code == 200, "data": response.json() if response.status_code == 200 else None}
    except Exception as e:
        return {"success": False, "error": str(e)}

def update_todo(todo_id: int) -> dict:
    """Toggle todo completion status"""
    try:
        response = requests.put(
            f"{API_BASE_URL}/todos/{todo_id}",
            headers=get_auth_headers()
        )
        return {"success": response.status_code == 200, "data": response.json() if response.status_code == 200 else None}
    except Exception as e:
        return {"success": False, "error": str(e)}

def delete_todo(todo_id: int) -> dict:
    """Delete a todo"""
    try:
        response = requests.delete(
            f"{API_BASE_URL}/todos/{todo_id}",
            headers=get_auth_headers()
        )
        return {"success": response.status_code == 200}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    st.set_page_config(
        page_title="Todo App",
        page_icon="✅",
        layout="centered"
    )
    
    st.title("✅ Todo Application")
    
    # Check if user is logged in
    if st.session_state.access_token is None:
        # Login/Register section
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            st.header("Login")
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")
                
                if submit:
                    if username and password:
                        result = login_user(username, password)
                        if result["success"]:
                            st.session_state.access_token = result["data"]["access_token"]
                            st.session_state.username = username
                            st.success("Logged in successfully!")
                            st.rerun()
                        else:
                            st.error(f"Login failed: {result.get('error', 'Unknown error')}")
                    else:
                        st.warning("Please enter both username and password")
        
        with tab2:
            st.header("Register")
            with st.form("register_form"):
                username = st.text_input("Username")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Register")
                
                if submit:
                    if username and email and password:
                        result = register_user(username, email, password)
                        if result["success"]:
                            st.success("Registration successful! Please login.")
                        else:
                            error_msg = result.get("data", {}).get("detail", result.get("error", "Registration failed"))
                            st.error(f"Registration failed: {error_msg}")
                    else:
                        st.warning("Please fill in all fields")
    else:
        # Main Todo App
        st.sidebar.title(f"Welcome, {st.session_state.username}!")
        if st.sidebar.button("Logout"):
            st.session_state.access_token = None
            st.session_state.username = None
            st.session_state.user_id = None
            st.rerun()
        
        st.header("My Todos")
        
        # Add new todo
        with st.form("add_todo_form"):
            col1, col2 = st.columns([4, 1])
            with col1:
                new_todo_title = st.text_input("New Todo", placeholder="Enter a new task...", label_visibility="collapsed")
            with col2:
                add_todo = st.form_submit_button("Add", use_container_width=True)
            
            if add_todo and new_todo_title:
                result = create_todo(new_todo_title)
                if result["success"]:
                    st.success("Todo added successfully!")
                    st.rerun()
                else:
                    st.error(f"Failed to add todo: {result.get('error', 'Unknown error')}")
        
        # Display todos
        todos = get_todos()
        
        if todos:
            st.subheader(f"Total: {len(todos)} todos")
            
            # Filter options
            filter_option = st.radio(
                "Filter:",
                ["All", "Active", "Completed"],
                horizontal=True
            )
            
            # Filter todos based on selection
            if filter_option == "Active":
                filtered_todos = [t for t in todos if not t["completed"]]
            elif filter_option == "Completed":
                filtered_todos = [t for t in todos if t["completed"]]
            else:
                filtered_todos = todos
            
            # Display todos
            for todo in filtered_todos:
                with st.container():
                    col1, col2, col3 = st.columns([1, 8, 1])
                    
                    with col1:
                        status_icon = "✅" if todo["completed"] else "⭕"
                        if st.button(status_icon, key=f"toggle_{todo['id']}", use_container_width=True):
                            result = update_todo(todo["id"])
                            if result["success"]:
                                st.rerun()
                            else:
                                st.error("Failed to update todo")
                    
                    with col2:
                        if todo["completed"]:
                            st.markdown(f"~~{todo['title']}~~")
                        else:
                            st.markdown(f"**{todo['title']}**")
                    
                    with col3:
                        if st.button("🗑️", key=f"delete_{todo['id']}", use_container_width=True):
                            result = delete_todo(todo["id"])
                            if result["success"]:
                                st.success("Todo deleted!")
                                st.rerun()
                            else:
                                st.error("Failed to delete todo")
                    
                    st.divider()
        else:
            st.info("No todos yet. Add one above to get started!")

if __name__ == "__main__":
    main()
