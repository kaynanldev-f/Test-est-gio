import { createRouter, createWebHistory } from "vue-router";
import Operadoras from "../views/Operadoras.vue";
import OperadoraDetalhe from "../views/OperadorasDetalhe.vue";

const routes = [
  {
    path: "/",
    name: "operadoras",
    component: Operadoras,
  },
  {
    path: "/operadoras/:cnpj",
    name: "operadora-detalhe",
    component: OperadoraDetalhe,
    props: true,
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
