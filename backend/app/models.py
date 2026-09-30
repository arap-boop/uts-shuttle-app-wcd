from pydantic import BaseModel, Field, ConfigDict

class ShuttleBase(BaseModel):
    route: str = Field(..., min_length=3, description="Nama atau rute shuttle")
    driver_name: str = Field(..., min_length=2, description="Nama pengemudi")
    departure_time: str = Field(..., description="Format: YYYY-MM-DD HH:MM")
    capacity: int = Field(..., gt=0, description="Kapasitas harus lebih dari 0")
    booked: int = Field(0, ge=0, description="Jumlah kursi terpesan")
    status: str = Field("Scheduled", description="Status jadwal")

class ShuttleCreate(ShuttleBase):
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "route": "Rute F: Kampus - Bandara",
            "driver_name": "Pak Asep",
            "departure_time": "2026-10-02 07:00",
            "capacity": 30,
            "booked": 0,
            "status": "Scheduled"
        }
    })

class ShuttleResponse(ShuttleBase):
    id: int
    model_config = ConfigDict(from_attributes=True)