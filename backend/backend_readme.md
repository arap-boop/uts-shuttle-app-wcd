# Campus Shuttle API (Backend Service)

Backend service for the Individual Practical Coding Exam (UTS Web Application Development), built with **FastAPI** and **Pydantic v2**, featuring an encapsulated in-memory data store, clean architecture, and complete CRUD operations.

---

## 🛠️ Tech Stack
- **Python** (v3.10+)
- **FastAPI** (Modern, fast web framework for building APIs)
- **Uvicorn** (ASGI server implementation)
- **Pydantic v2** (Data validation and settings management)

---

## 📁 Project Structure (`backend/`)
```text
backend/
├── app/
│   ├── __init__.py
│   ├── database.py   # Encapsulated in-memory database singleton (12 synthetic rows)
│   ├── models.py     # Pydantic v2 schemas for validation & serialization
│   ├── routers.py    # APIRouter containing all endpoint logic
│   └── main.py       # FastAPI application entry point & CORS configuration
├── requirements.txt  # Project dependencies
└── README.md         # Backend documentation
```

---

## 🚀 Getting Started & Running Locally

1. **Open your terminal** and navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   venv\Scripts\Activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server using Uvicorn**:
   ```bash
   uvicorn app.main:app --reload
   ```

- The API server will run at: `http://127.0.0.1:8000`
- Interactive API Documentation (Swagger UI): `http://127.0.0.1:8000/docs`
- Alternative Documentation (ReDoc): `http://127.0.0.1:8000/redoc`

---

## 🔌 API Endpoints & Verification

| Method | Endpoint | Description | Parameters / Payload | Status Code |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/sessions` | Retrieve all shuttle sessions with search & pagination | `search` (query), `skip` (query), `limit` (query) | `200 OK` |
| **GET** | `/sessions/{session_id}` | Retrieve specific session details by ID | `session_id` (path) | `200 OK` or `404 Not Found` |
| **POST** | `/sessions` | Create a new shuttle session | JSON body (`ShuttleCreate` schema) | `201 Created` |
| **DELETE** | `/sessions/{session_id}` | Delete a shuttle session by ID | `session_id` (path) | `204 No Content` or `404 Not Found` |

---

## 🧪 Requirements Compliance
- **In-Memory Dataset**: Contains at least 12 baseline synthetic rows initialized in `app/database.py`.
- **CORS Enabled**: Configured via `CORSMiddleware` to allow seamless communication with the frontend client.
- **Validation**: Strict schema validation handled by Pydantic v2.