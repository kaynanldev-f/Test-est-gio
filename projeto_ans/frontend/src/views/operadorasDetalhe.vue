<script setup>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import api from "../api/api";

const route = useRoute();
const operadora = ref(null);
const despesas = ref([]);

onMounted(async () => {
  const cnpj = route.params.cnpj;

  const opRes = await api.get(`operadoras/${cnpj}`);
  operadora.value = opRes.data;

  const despRes = await api.get(`operadoras/${cnpj}/despesas`);
  despesas.value = despRes.data;
});
</script>

<template>
  <div v-if="operadora">
    <h1>{{ operadora.razao_social }}</h1>
    <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
    <p><strong>UF:</strong> {{ operadora.uf }}</p>

    <h2>Histórico de Despesas</h2>
    <ul>
      <li v-for="d in despesas" :key="d.id">
        {{ d.ano }} - {{ d.trimestre }} → R$ {{ d.total }}
      </li>
    </ul>
  </div>
</template>
