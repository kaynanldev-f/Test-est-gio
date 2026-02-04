import { ref, reactive } from "vue";
import api from "../api/api";

export function useOperadoras() {
  const operadoras = ref([]);
  const loading = ref(false);
  const error = ref(null);

  const pagination = reactive({
    page: 1,
    limit: 10,
    total: 0,
  });

  async function fetchOperadoras(page = 1) {
    loading.value = true;
    error.value = null;

    try {
      const response = await api.get("api/operadoras/", {
        params: { page, limit: pagination.limit },
      });

      operadoras.value = response.data.data;

      pagination.page = response.data.page;
      pagination.limit = response.data.limit;
      pagination.total = response.data.total;
    } catch (err) {
      console.error(err);
      error.value = "Erro ao carregar operadoras";
    } finally {
      loading.value = false;
    }
  }

  return {
    operadoras,
    loading,
    error,
    pagination,
    fetchOperadoras,
  };
}
