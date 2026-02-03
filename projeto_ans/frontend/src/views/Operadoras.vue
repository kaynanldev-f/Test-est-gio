<script setup>
import { onMounted } from "vue";
import { useOperadoras } from "../composables/useOperadoras";
import OperadorasTable from "../components/OperadoraTable.vue";

const { operadoras, loading, error, pagination, fetchOperadoras } =
  useOperadoras();

onMounted(() => {
  fetchOperadoras();
});
</script>

<template>
  <main>
    <h1>Operadoras</h1>
    <div v-if="loading">Carregando...</div>
    <div v-if="error">{{ error }}</div>
    <OperadorasTable v-if="!loading" :operadoras="operadoras" />
    <button
      :disabled="pagination.page === 1"
      @click="fetchOperadoras(pagination.page - 1)"
    >
      Anterior
    </button>
    <button
      :disabled="pagination.page * pagination.limit >= pagination.total"
      @click="fetchOperadoras(pagination.page + 1)"
    >
      Próxima
    </button>
  </main>
</template>
