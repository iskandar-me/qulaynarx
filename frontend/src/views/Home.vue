<template>
   <div>

      <FilterPanel @search="onSearch" class="filter-panel" />

      <!-- Loading  -->
      <div v-if="loading" class="loading">
         <img
            src="@/assets/img/loading.gif"
            alt="Loading..."
            height="240"
            width="260" />
         <p class="loading__text">Yuklanmoqda...</p>
      </div>

      <!-- Error message -->
      <!-- <div v-if="error" class="error">{{ error }}</div> -->

      <!-- No products message -->
      <div v-if="noProduct" class="no-products">
         <img
            src="../assets/img/no-products-found.gif"
            alt="No products found ("
            height="320" />
         <h2>Hech qanday mahsulot topilmadi.</h2>
      </div>

      <!-- Products list -->
      <div class="products" v-if="!loading && products.length">
         <ProductCard
            v-for="product in products"
            :key="product._id"
            :product="product" />
      </div>

      <!-- Pagination -->
      <Pagination
         v-if="products.length && !loading"
         :page="page"
         :totalPages="totalPages"
         :limit="limit"
         :totalCount="totalProducts"
         @change="setPage" />
   </div>
</template>

<script setup>
import FilterPanel from "../components/FilterPanel.vue";
import ProductCard from "../components/ProductCard.vue";
import Pagination from "../components/Pagination.vue";
import useProducts from "../composables/useProducts.js";

const {
   products,
   page,
   limit,
   totalPages,
   totalProducts,
   fetchProducts,
   setPage,
   loading,
   error,
   noProduct,
} = useProducts();

// Filter paneldan kelgan search
const onSearch = (filters) => {
   page.value = 1;

   // agar name bo'sh bo'lsa, filters dan o'chirib yubor
   if (!filters.name) delete filters.name;

   fetchProducts(filters);
};

// Initial load
fetchProducts({ name: "" });
</script>

<style scoped>
.loading {
   text-align: center;
   padding: 40px;
}
.loading__text {
   text-align: center;
   margin-top: 15px;
   font-size: 1rem;
   color: #555;
}
.products {
   display: grid;
   grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
   gap: 0.75rem;
}

.no-products {
   text-align: center;
   font-size: 0.95rem;
   color: #777;
   padding: 1rem 0;
}

.error {
   color: #e33;
   font-size: 0.9rem;
}

@media (max-width: 600px) {
   .products {
      margin: auto 1rem;
   }
}
</style>
