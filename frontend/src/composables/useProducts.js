import { ref } from "vue";
import axios from "axios";

export default function useProducts() {
   const products = ref([]);
   const page = ref(1);
   const limit = ref(10);
   const totalPages = ref(1);
   const totalProducts = ref(0); // <-- jami productlar soni

   const loading = ref(false);
   const error = ref("");
   const noProduct = ref(false);

   const lastFilters = ref({ name: "" });

   const fetchProducts = async (filters = {}) => {
      loading.value = true;
      error.value = "";
      noProduct.value = false;

      lastFilters.value = { ...filters };
      filters.page = page.value;
      filters.limit = limit.value;

      // Agar name bo'sh bo'lsa, "" yuboramiz
      if (!filters.name) filters.name = "";

      try {
         const res = await axios.get("http://127.0.0.1:8000/products/search", {
            params: filters,
         });

         products.value = res.data.products;
         totalProducts.value = res.data.total;
         totalPages.value = Math.ceil(res.data.total / limit.value);

         if (!products.value.length) {
            noProduct.value = true;
            error.value = "Hech qanday product topilmadi";
         }
      } catch (err) {
         if (err.response) {
            error.value = `Server xatoligi: ${err.response.status} ${err.response.statusText}`;
         } else if (err.request) {
            error.value =
               "Server bilan bog‘lanib bo‘lmadi. Iltimos, internetni tekshiring.";
         } else {
            error.value = `Xatolik yuz berdi: ${err.message}`;
         }
      } finally {
         loading.value = false;
      }
   };

   const setPage = (newPage) => {
      page.value = newPage;
      fetchProducts(lastFilters.value);
   };

   return {
      products,
      page,
      limit,
      totalPages,
      totalProducts,
      loading,
      error,
      noProduct,
      fetchProducts,
      setPage,
   };
}
