<template>
  <div class="container">
    <h1>🚌 Dashboard Pemesanan Shuttle Kampus</h1>

    <!-- Search Bar -->
    <div class="search-bar">
      <input 
        v-model="searchQuery" 
        placeholder="Cari berdasarkan rute atau nama driver..." 
        @keyup.enter="loadSessions"
      />
      <button @click="loadSessions">Cari</button>
    </div>

    <!-- Form Create -->
    <ShuttleForm @session-created="handleCreateSession" />

    <!-- List & 4 States -->
    <ShuttleList 
      :sessions="sessions" 
      :loading="loading" 
      :errorMsg="errorMsg" 
      @retry="loadSessions"
      @delete-session="handleDeleteSession"
    />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { getSessions, createSession, deleteSession } from './api/shuttle'
import ShuttleForm from './components/ShuttleForm.vue'
import ShuttleList from './components/ShuttleList.vue'

export default {
  components: { ShuttleForm, ShuttleList },
  setup() {
    const sessions = ref([])
    const loading = ref(false)
    const errorMsg = ref(null)
    const searchQuery = ref('')

    const loadSessions = async () => {
      loading.value = true
      errorMsg.value = null
      try {
        sessions.value = await getSessions(searchQuery.value)
      } catch (err) {
        errorMsg.value = err.message
      } finally {
        loading.value = false
      }
    }

    const handleCreateSession = async (payload) => {
      try {
        await createSession(payload)
        loadSessions()
      } catch (err) {
        alert(err.message)
      }
    }

    const handleDeleteSession = async (id) => {
      if (!confirm('Apakah Anda yakin ingin menghapus sesi shuttle ini?')) return
      try {
        await deleteSession(id)
        loadSessions()
      } catch (err) {
        alert(err.message)
      }
    }

    onMounted(loadSessions)

    return {
      sessions,
      loading,
      errorMsg,
      searchQuery,
      loadSessions,
      handleCreateSession,
      handleDeleteSession
    }
  }
}
</script>