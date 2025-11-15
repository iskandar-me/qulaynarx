<template>
   <div>
      <FilterPanel @search="onSearch" />

      <!-- Loading spinner -->
      <div v-if="loading">Loading...</div>

      <!-- Error message -->
      <!-- <div v-if="error" class="error">{{ error }}</div> -->

      <!-- No products message -->
      <div v-if="noProduct" class="no-products">
         Hech qanday mahsulot topilmadi.
      </div>

      <!-- Products list -->
      <div class="products" v-if="products.length">
         <ProductCard
            v-for="product in products"
            :key="product._id"
            :product="product" />
      </div>

      <!-- Pagination -->
      <Pagination
         v-if="products.length"
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
   fetchProducts(filters);
};

// Initial load
fetchProducts({ name: "" });
</script>

<style scoped>
.products {
   display: flex;
   flex-wrap: wrap;
   gap: 1rem;
}
.error {
   color: red;
}
.no-products {
   color: gray;
   font-style: italic;
}
</style>
