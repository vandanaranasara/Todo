## ✅ FastAPI + Streamlit Todo App

> A clean, full‑stack Todo application with authentication, built using **FastAPI** (backend) and **Streamlit** (frontend).

[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

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

## 🚀 Quick Start

### 1️⃣ Setup (once)

From the project root (`Fast API`):

```bash
cd "Fast API"

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DB_URL=sqlite:///./todo.db
SECRET_KEY=your-secret-key-here-change-in-production
```

> 💡 **Tip:** Use a long, random `SECRET_KEY` value in real deployments.

### 2️⃣ Run the backend (Terminal 1)

```bash
uvicorn app.main:app --reload
```

- API base URL: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 3️⃣ Run the frontend (Terminal 2)

```bash
streamlit run frontend.py
```

- Frontend URL: `http://localhost:8501`

> ✅ **Make sure** the FastAPI backend is running **before** starting Streamlit.

---

## 🧩 API Endpoints

### 🔐 Authentication
- `POST /auth/login` – user login  
  - Body: `username`, `password` (form data)  
  - Returns: `access_token`

### 👤 Users
- `POST /users/` – register a new user  
  - Body: `username`, `email`, `password` (JSON)  
  - Returns: created user info

### 📝 Todos  (requires Bearer token)
- `GET /todos/` – list todos for the authenticated user
- `POST /todos/` – create a new todo  
  - Body: `title` (JSON)
- `PUT /todos/{todo_id}` – toggle completion status
- `DELETE /todos/{todo_id}` – delete a todo

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

### Backend API URL

If the backend is not at `http://localhost:8000`, you can:

- Set an environment variable:

```bash
export API_BASE_URL=http://your-host:your-port
```

or on Windows PowerShell:

```powershell
$env:API_BASE_URL="http://your-host:your-port"
```

- Or update `API_BASE_URL` directly in `frontend.py`.

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

