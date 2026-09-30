from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Optional
from app.models import ShuttleCreate, ShuttleResponse
from app.database import db

router = APIRouter(prefix="/sessions", tags=["Shuttle Sessions"])

@router.get("", response_model=List[ShuttleResponse], summary="Ambil daftar sesi dengan pencarian & pagination")
def get_sessions(
    search: Optional[str] = Query(None, description="Cari berdasarkan rute atau nama driver"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return db.get_all(search=search, skip=skip, limit=limit)

@router.get("/{session_id}", response_model=ShuttleResponse, summary="Ambil detail sesi berdasarkan ID")
def get_session_by_id(session_id: int):
    item = db.get_by_id(session_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Sesi shuttle dengan ID {session_id} tidak ditemukan"
        )
    return item

@router.post("", response_model=ShuttleResponse, status_code=status.HTTP_201_CREATED, summary="Tambah sesi shuttle baru")
def create_session(payload: ShuttleCreate):
    # Menggunakan model_dump() standar Pydantic v2
    new_item = db.create(payload.model_dump())
    return new_item

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Hapus sesi shuttle")
def delete_session(session_id: int):
    success = db.delete(session_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Sesi shuttle dengan ID {session_id} tidak ditemukan"
        )
    return None