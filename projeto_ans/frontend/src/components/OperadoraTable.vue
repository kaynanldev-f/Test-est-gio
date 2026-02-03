<script setup>
defineProps({
  operadoras: Array,
});
</script>

<template>
  <table>
    <thead>
      <tr>
        <th>CNPJ</th>
        <th>Razão Social</th>
        <th>UF</th>
        <th>Modalidade</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="op in operadoras" :key="op.cnpj">
        <td>{{ op.cnpj }}</td>
        <td>{{ op.razao_social }}</td>
        <td>{{ op.uf }}</td>
        <td>{{ op.modalidade }}</td>
      </tr>
    </tbody>
  </table>
</template>
