# UTS — Practical Coding Exam (Individu): Pemesanan Shuttle Kampus

Aplikasi pencatat sesi transportasi kampus berbasis **FastAPI** (Backend) dan **Vue 3 + Vite** (Frontend) yang dibangun secara mandiri untuk Ujian Praktik Web Application Development.

---

## 📁 Struktur Repository
```text
uts-shuttle-app-wcd/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py   # Encapsulated In-Memory Database
│   │   ├── models.py     # Pydantic v2 Schemas & Validations
│   │   ├── routers.py    # FastAPI Endpoints
│   │   └── main.py       # FastAPI Entrypoint & CORS Middleware
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── shuttle.js     # API Service Layer (Fetch Wrapper)
│   │   ├── components/
│   │   │   ├── ShuttleForm.vue  # Form input dengan validasi
│   │   │   └── ShuttleList.vue  # Tabel data & penanganan 4 State (Loading, Error+Retry, Empty, Success)
│   │   ├── App.vue              # Root Component
│   │   ├── main.js
│   │   └── style.css
│   ├── package.json
│   └── vite.config.js
└── README.md