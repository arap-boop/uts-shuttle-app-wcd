<template>
  <div>
    <!-- STATE 1: LOADING -->
    <div v-if="loading" style="text-align: center; padding: 40px; color: #64748b;">
      Memuat data sesi shuttle dari server...
    </div>

    <!-- STATE 2: ERROR + TOMBOL RETRY -->
    <div v-else-if="errorMsg" class="error-box">
      <span>Gagal memuat data: {{ errorMsg }}</span>
      <button @click="$emit('retry')" style="background: #991b1b;">Coba Lagi (Retry)</button>
    </div>

    <!-- STATE 3 & 4: EMPTY ATAU SUCCESS -->
    <div v-else>
      <div v-if="sessions.length === 0" class="empty-box">
        Tidak ada data sesi shuttle yang ditemukan.
      </div>
      <table v-else>
        <thead>
          <tr>
            <th>ID</th>
            <th>Rute</th>
            <th>Driver</th>
            <th>Waktu</th>
            <th>Okupansi Kursi</th>
            <th>Status</th>
            <th>Aksi</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in sessions" :key="item.id">
            <td>#{{ item.id }}</td>
            <td><strong>{{ item.route }}</strong></td>
            <td>{{ item.driver_name }}</td>
            <td>{{ item.departure_time }}</td>
            <td>{{ item.booked }} / {{ item.capacity }} Kursi</td>
            <td>
              <span :class="['badge', item.status.toLowerCase() === 'full' ? 'full' : 'scheduled']">
                {{ item.status }}
              </span>
            </td>
            <td>
              <button class="danger" @click="$emit('delete-session', item.id)">Hapus</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    sessions: { type: Array, required: true },
    loading: { type: Boolean, required: true },
    errorMsg: { type: String, default: null }
  },
  emits: ['retry', 'delete-session']
}
</script>