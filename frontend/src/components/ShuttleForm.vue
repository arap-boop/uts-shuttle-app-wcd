<template>
  <div class="card">
    <h3 style="margin-top: 0; margin-bottom: 16px; color: #334155;">➕ Tambah Jadwal Shuttle Baru</h3>
    <form @submit.prevent="handleSubmit">
      <div class="form-grid">
        <div class="form-group">
          <label>Rute Perjalanan</label>
          <input v-model="form.route" required placeholder="Contoh: Rute A: Kampus Pusat" />
        </div>
        <div class="form-group">
          <label>Nama Driver</label>
          <input v-model="form.driver_name" required placeholder="Nama pengemudi" />
        </div>
        <div class="form-group">
          <label>Waktu Keberangkatan</label>
          <input v-model="form.departure_time" required placeholder="YYYY-MM-DD HH:MM" />
        </div>
        <div class="form-group">
          <label>Kapasitas Kursi</label>
          <input type="number" v-model.number="form.capacity" required min="1" />
        </div>
      </div>
      <button type="submit">Simpan Sesi Shuttle</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  emits: ['session-created'],
  setup(props, { emit }) {
    const form = ref({
      route: '',
      driver_name: '',
      departure_time: '2026-10-02 08:00',
      capacity: 20,
      booked: 0,
      status: 'Scheduled'
    })

    const handleSubmit = () => {
      emit('session-created', { ...form.value })
      form.value.route = ''
      form.value.driver_name = ''
    }

    return { form, handleSubmit }
  }
}
</script>