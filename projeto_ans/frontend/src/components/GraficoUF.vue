<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import Chart from "chart.js/auto";
import api from "../api/api";

const canvasRef = ref(null);
let chartInstance = null;

onMounted(async () => {
  const res = await api.get("estatisticas/api/estatisticas");

  chartInstance = new Chart(canvasRef.value, {
    type: "bar",
    data: {
      labels: res.data.top_5_operadoras.map((o) => o.cnpj),
      datasets: [
        {
          label: "Total de Despesas (R$)",
          data: res.data.top_5_operadoras.map((o) => o.total),
        },
      ],
    },
    options: {
      responsive: true,
    },
  });
});

onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.destroy();
  }
});
</script>

<template>
  <canvas ref="canvasRef"></canvas>
</template>
