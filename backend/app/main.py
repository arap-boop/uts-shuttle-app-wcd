from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router as shuttle_router

app = FastAPI(
    title="Campus Shuttle API",
    description="Backend Service Ujian Praktik Web Application Development (Clean Architecture)",
    version="2.0.0"
)

# Konfigurasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Daftarkan Router
app.include_router(shuttle_router)

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Campus Shuttle API is running smoothly!"}