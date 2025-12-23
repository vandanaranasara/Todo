## ✅ FastAPI + Streamlit Todo App

> A clean, full‑stack Todo application with authentication, built using **FastAPI** (backend) and **Streamlit** (frontend).

[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org)

---

### 📚 Table of Contents
- **✨ Features**
- **🧱 Tech Stack**
- **📁 Project Structure**
- **🚀 Quick Start (Run in 2 terminals)**
- **🧩 API Endpoints**
- **🖥️ App Usage**
- **⚙️ Configuration**
- **🗄️ Database & Migrations**
- **🔒 Security Notes**
- **🧪 Development**
- **🆘 Troubleshooting**

---

## ✨ Features

- ✅ **User authentication** (registration & login)
- 🔐 **JWT-based secure auth**
- 📝 **Create, read, update, delete** todos
- ✅ **Mark todos as complete / incomplete**
- 🎯 **Filter todos** by status (All, Active, Completed)
- 👤 **User-specific todo lists**
- 💅 **Modern and intuitive Streamlit UI**

---

## 🧱 Tech Stack

- **Backend**
  - ⚡ **FastAPI** – high‑performance Python API framework
  - 🧱 **SQLAlchemy** – ORM & DB toolkit
  - 🔁 **Alembic** – database migrations
  - 🛡️ **Argon2** – secure password hashing
  - 🎫 **JWT** – token‑based authentication
  - 🗄️ **SQLite** (easily swappable with PostgreSQL/MySQL)

- **Frontend**
  - 📊 **Streamlit** – fast UI for data/web apps
  - 🌐 **Requests** – HTTP client for API calls

---

## 📁 Project Structure

```text
Fast API/
├── app/
│   ├── auth.py              # JWT token generation/verification
│   ├── config.py            # Application configuration
│   ├── database.py          # Database setup and session management
│   ├── main.py              # FastAPI application entry point
│   ├── models.py            # SQLAlchemy database models
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── utils.py             # Utility functions (password hashing, etc.)
│   ├── middleware/
│   │   └── cors.py          # CORS middleware configuration
│   └── routers/
│       ├── auth.py          # Authentication routes
│       ├── todos.py         # Todo CRUD routes
│       └── users.py         # User registration routes
├── alembic/                 # Database migration files
├── scripts/
│   └── create_admin.py      # Admin user creation script
├── frontend.py              # Streamlit frontend application
├── requirements.txt         # Python dependencies
├── alembic.ini              # Alembic configuration
├── todo.db                  # SQLite database file (generated)
└── README.md
```

---

# 🚀 How to Run the Project

Follow these steps to set up and run the project on your local system:

### 1️⃣ Clone the Repository
- Clone the project from GitHub using:
 ```bash
git clone https://github.com/vandanaranasara/Todo.git
cd Todo
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
- Activate the Virtual Environment
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Development Server
```bash
uvicorn uvicorn app.main:app --reload  
streamlit run frontend.py
```
---

## 🧩 API Endpoints

### 🔐 Authentication
- `POST /auth/login` – User login  

### 👤 Users
- `POST /users/` – Register a new user  

### 📝 Todos  (requires Bearer token)
- `GET /todos/` – List todos for the authenticated user
- `POST /todos/` – Create a new todo  
- `PUT /todos/{todo_id}` – Toggle completion status
- `DELETE /todos/{todo_id}` – Delete a todo

---

## 🖥️ Using the App

1. 🔌 **Start both servers** (backend & frontend).
2. 🌐 Open `http://localhost:8501` in your browser.
3. 📝 On the **Register** tab, create a new account.
4. 🔑 Log in with your credentials.
5. ✅ Manage your todos:
   - ➕ Add todos using the input field.
   - ✅ Click the circle/checkmark to toggle completion.
   - 🗑️ Click the trash icon to delete.
   - 🎯 Use filters to view **All / Active / Completed** todos.

---

## ⚙️ Configuration

### Set an environment variable:

```bash
DB_URL=YOUR_DB_URL
```

---

## 🗄️ Database & Migrations

Run migrations to sync the database schema:

```bash
alembic upgrade head
```

Create a new migration:

```bash
alembic revision --autogenerate -m "describe your change"
```

---

## 🔒 Security Notes

- 🛡️ Passwords are hashed with **Argon2**.
- 🎫 **JWT tokens** are used for authentication.
- 🌍 **CORS** is configured for cross‑origin requests.
- 👤 Users can only access **their own** todos.

---

## 🆘 Troubleshooting

1. ❌ **Connection error**  
   - Confirm the FastAPI backend is running on the correct port.
   - Check that `API_BASE_URL` matches the backend URL.

2. 🔑 **Authentication issues**  
   - Clear browser cache or stop & restart the Streamlit app.

3. 🗄️ **Database errors**  
   - Ensure `todo.db` is writable and migrations are up‑to‑date (`alembic upgrade head`).

## 📸 Screenshots

| Login | Register |
|-----------|------------|
| ![Login](screenshots/login.png) | ![Register](screenshots/register.png) |

| Todo | Query |
|-----------|------------|
| ![Todo](screenshots/todo.png) |

## 👥 Contributor

- [Vandana Ranasara](https://github.com/vandanaranasara)

