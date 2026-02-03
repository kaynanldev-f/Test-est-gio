<script setup>
import { onMounted } from "vue";
import Chart from "chart.js/auto";
import api from "../api/api";

onMounted(async () => {
  const res = await api.get("/estatisticas");

  new Chart(document.getElementById("graficoUF"), {
    type: "bar",
    data: {
      labels: res.data.top_5_operadoras.map((o) => o.cnpj),
      datasets: [
        {
          label: "Total de Despesas",
          data: res.data.top_5_operadoras.map((o) => o.total),
        },
      ],
    },
  });
});
</script>

<template>
  <canvas id="graficoUF"></canvas>
</template>
