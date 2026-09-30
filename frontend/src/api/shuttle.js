const API_BASE_URL = 'http://127.0.0.1:8000';

export async function getSessions(search = '') {
  let url = `${API_BASE_URL}/sessions`;
  if (search) {
    url += `?search=${encodeURIComponent(search)}`;
  }
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error('Gagal terhubung ke server backend FastAPI');
  }
  return response.json();
}

export async function createSession(payload) {
  const response = await fetch(`${API_BASE_URL}/sessions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (!response.ok) {
    throw new Error('Gagal menambah sesi shuttle baru');
  }
  return response.json();
}

export async function deleteSession(id) {
  const response = await fetch(`${API_BASE_URL}/sessions/${id}`, {
    method: 'DELETE'
  });
  if (!response.ok) {
    throw new Error('Gagal menghapus sesi shuttle');
  }
  return true;
}