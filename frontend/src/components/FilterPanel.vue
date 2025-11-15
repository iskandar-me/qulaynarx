<template>
   <div class="filter-panel">
      <!-- Product name input -->
      <input
         v-model="searchName"
         placeholder="Product nomi"
         :class="{ 'input-error': nameError }"
         @input="nameError = false" />

      <!-- Min price va Max price -->
      <input
         v-model="minPrice"
         type="text"
         placeholder="Min Price"
         @input="sanitizePrice('min')" />
      <input
         v-model="maxPrice"
         type="text"
         placeholder="Max Price"
         @input="sanitizePrice('max')" />

      <!-- Market name -->
      <input v-model="marketName" placeholder="Market" />

      <!-- Sort options -->
      <select v-model="sortBy">
         <option value="current_price">Narx</option>
         <option value="product_name">Nom</option>
      </select>
      <select v-model="sortOrder">
         <option value="asc">O‘sish</option>
         <option value="desc">Kamayish</option>
      </select>

      <!-- Search button -->
      <button @click="search">Qidirish</button>
   </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";

const emit = defineEmits(["search"]);

const searchName = ref("");
const minPrice = ref("");
const maxPrice = ref("");
const marketName = ref("");
const sortBy = ref("current_price");
const sortOrder = ref("asc");

// Validation flag
const nameError = ref(false);

// Raqam va nuqta qabul qiladigan sanitizer
const sanitizePrice = (type) => {
   if (type === "min") minPrice.value = minPrice.value.replace(/[^0-9.]/g, "");
   if (type === "max") maxPrice.value = maxPrice.value.replace(/[^0-9.]/g, "");
};

const search = () => {
   const trimmedName = searchName.value.trim();

   // Agar name bo'sh bo'lsa, border qizarsin va hech narsa yuborilmasin
   if (!trimmedName) {
      nameError.value = true;
      return;
   }

   const min_price_num = minPrice.value
      ? parseFloat(minPrice.value)
      : undefined;
   const max_price_num = maxPrice.value
      ? parseFloat(maxPrice.value)
      : undefined;

   emit("search", {
      name: trimmedName,
      min_price: min_price_num,
      max_price: max_price_num,
      market_name: marketName.value.trim(),
      sort_by: sortBy.value,
      sort_order: sortOrder.value,
   });
};
</script>

<style scoped>
.input-error {
   border: 2px solid red;
}
</style>
