<script setup>
import { onMounted, ref } from "vue";
import { useOperadoras } from "../composables/useOperadoras";
import OperadorTable from "../components/OperadoraTable.vue";
import GraficoUF from "../components/GraficoUF.vue";

const search = ref("");

const { operadoras, loading, error, pagination, fetchOperadoras } =
  useOperadoras();

onMounted(() => {
  fetchOperadoras();
});
</script>

<template>
  <div>
    <h1>Operadoras</h1>
    <input
      v-model="search"
      placeholder="Buscar por CNPJ ou Razão Social"
      @keyup.enter="fetchOperadoras(1, search)"
    />
    <button @click="fetchOperadoras(1, search)">Buscar</button>
    <p v-if="loading">Carregando...</p>
    <p v-if="error">{{ error }}</p>
    <OperadorTable v-if="!loading" :operadoras="operadoras" />
    <div>
      <button
        :disabled="pagination.page === 1"
        @click="fetchOperadoras(pagination.page - 1, search)"
      >
        Anterior
      </button>
      <span>Página {{ pagination.page }}</span>
      <button @click="fetchOperadoras(pagination.page + 1, search)">
        Próxima
      </button>
    </div>
    <h2>Distribuição de Despesas por UF</h2>
    <GraficoUF />
  </div>
</template>
