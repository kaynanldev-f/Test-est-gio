import { createRouter, createWebHistory } from "vue-router";
import Operadoras from "../views/operadoras.vue";
import operadorasDetalhe from "../views/operadorasDetalhe.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Operadoras },
    { path: "/operadoras/:cnpj", component: operadorasDetalhe },
  ],
});
