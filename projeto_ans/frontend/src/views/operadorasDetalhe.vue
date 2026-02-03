<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../api/api";

const route = useRoute();
const cnpj = route.params.cnpj;

const operadora = ref(null);
const despesas = ref([]);
const loading = ref(true);
const error = ref(null);

const formatarValor = (valor) =>
  Number(valor).toLocaleString("pt-BR", {
    minimumFractionDigits: 2,
  });

const carregarDados = async () => {
  try {
    const [op, desp] = await Promise.all([
      api.get(`api/operadoras/${cnpj}/`),
      api.get(`api/operadoras/${cnpj}/despesas/`),
    ]);

    operadora.value = op.data;
    despesas.value = desp.data;
  } catch (err) {
    error.value = "Erro ao carregar dados da operadora.";
  } finally {
    loading.value = false;
  }
};

onMounted(carregarDados);
</script>

<template>
  <div class="container">
    <button @click="$router.back()">← Voltar</button>

    <!-- Loading -->
    <p v-if="loading">Carregando dados da operadora...</p>

    <!-- Erro -->
    <p v-if="error" class="error">{{ error }}</p>

    <!-- Conteúdo -->
    <div v-if="operadora">
      <h1>{{ operadora.razao_social }}</h1>

      <ul class="info">
        <li><strong>CNPJ:</strong> {{ operadora.cnpj }}</li>
        <li><strong>Registro ANS:</strong> {{ operadora.registro_ans }}</li>
        <li><strong>Modalidade:</strong> {{ operadora.modalidade }}</li>
        <li><strong>UF:</strong> {{ operadora.uf }}</li>
      </ul>

      <h2>Histórico de Despesas</h2>

      <table v-if="despesas.length">
        <thead>
          <tr>
            <th>Ano</th>
            <th>Trimestre</th>
            <th>Valor</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="d in despesas" :key="d.ano + d.trimestre">
            <td>{{ d.ano }}</td>
            <td>{{ d.trimestre }}</td>
            <td>R$ {{ formatarValor(d.total_despesas) }}</td>
          </tr>
        </tbody>
      </table>

      <p v-else>Nenhum dado de despesa disponível.</p>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 900px;
  margin: auto;
}

.error {
  color: red;
}

.info {
  list-style: none;
  padding: 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
}
</style>
