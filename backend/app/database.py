from typing import List, Dict, Any, Optional

class InMemoryDatabase:
    def __init__(self):
        self._sessions: List[Dict[str, Any]] = [
            {
                "id": 1,
                "route": "Rute A: Kampus Pusat - Asrama Mahasiswa",
                "driver_name": "Pak Budi",
                "departure_time": "2026-10-01 08:00",
                "capacity": 20,
                "booked": 14,
                "status": "Scheduled",
            },
            {
                "id": 2,
                "route": "Rute B: Asrama Mahasiswa - Fakultas Teknik",
                "driver_name": "Pak Joko",
                "departure_time": "2026-10-01 08:30",
                "capacity": 15,
                "booked": 15,
                "status": "Full",
            },
            {
                "id": 3,
                "route": "Rute C: Kampus Pusat - Stasiun MRT",
                "driver_name": "Pak Slamet",
                "departure_time": "2026-10-01 09:00",
                "capacity": 25,
                "booked": 10,
                "status": "Scheduled",
            },
            {
                "id": 4,
                "route": "Rute A: Asrama Mahasiswa - Kampus Pusat",
                "driver_name": "Pak Budi",
                "departure_time": "2026-10-01 10:00",
                "capacity": 20,
                "booked": 5,
                "status": "Scheduled",
            },
            {
                "id": 5,
                "route": "Rute D: Fakultas Teknik - Gedung Rektorat",
                "driver_name": "Bu Siti",
                "departure_time": "2026-10-01 10:30",
                "capacity": 15,
                "booked": 8,
                "status": "Scheduled",
            },
            {
                "id": 6,
                "route": "Rute B: Fakultas Teknik - Asrama Mahasiswa",
                "driver_name": "Pak Joko",
                "departure_time": "2026-10-01 11:00",
                "capacity": 15,
                "booked": 12,
                "status": "Scheduled",
            },
            {
                "id": 7,
                "route": "Rute C: Stasiun MRT - Kampus Pusat",
                "driver_name": "Pak Slamet",
                "departure_time": "2026-10-01 13:00",
                "capacity": 25,
                "booked": 22,
                "status": "Scheduled",
            },
            {
                "id": 8,
                "route": "Rute E: Parkiran Timur - Lab Terpadu",
                "driver_name": "Pak Udin",
                "departure_time": "2026-10-01 13:30",
                "capacity": 10,
                "booked": 10,
                "status": "Full",
            },
            {
                "id": 9,
                "route": "Rute A: Kampus Pusat - Asrama Mahasiswa",
                "driver_name": "Pak Budi",
                "departure_time": "2026-10-01 14:00",
                "capacity": 20,
                "booked": 18,
                "status": "Scheduled",
            },
            {
                "id": 10,
                "route": "Rute D: Gedung Rektorat - Fakultas Teknik",
                "driver_name": "Bu Siti",
                "departure_time": "2026-10-01 15:00",
                "capacity": 15,
                "booked": 3,
                "status": "Scheduled",
            },
            {
                "id": 11,
                "route": "Rute C: Kampus Pusat - Stasiun MRT",
                "driver_name": "Pak Slamet",
                "departure_time": "2026-10-01 16:00",
                "capacity": 25,
                "booked": 25,
                "status": "Full",
            },
            {
                "id": 12,
                "route": "Rute E: Lab Terpadu - Parkiran Timur",
                "driver_name": "Pak Udin",
                "departure_time": "2026-10-01 16:30",
                "capacity": 10,
                "booked": 4,
                "status": "Scheduled",
            },
        ]

    def get_all(self, search: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        data = self._sessions
        if search:
            search_lower = search.lower()
            data = [
                item for item in data 
                if search_lower in item["route"].lower() or search_lower in item["driver_name"].lower()
            ]
        return data[skip : skip + limit]

    def get_by_id(self, session_id: int) -> Optional[Dict[str, Any]]:
        for item in self._sessions:
            if item["id"] == session_id:
                return item
        return None

    def create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        new_id = max([item["id"] for item in self._sessions], default=0) + 1
        payload["id"] = new_id
        self._sessions.append(payload)
        return payload

    def delete(self, session_id: int) -> bool:
        for idx, item in enumerate(self._sessions):
            if item["id"] == session_id:
                self._sessions.pop(idx)
                return True
        return False

db = InMemoryDatabase()