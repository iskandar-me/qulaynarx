<template>
   <div class="filter-panel">
      <!-- Product name input -->
      <input
         v-model="searchName"
         placeholder="Product nomi"
         :class="{ 'input-error': nameError }"
         @input="nameError = false"
         class="input"
         value="ol" />

      <!-- Min price va Max price -->
      <input
         v-model="minPrice"
         type="text"
         placeholder="Min Price"
         @input="sanitizePrice('min')"
         class="input" />
      <input
         v-model="maxPrice"
         type="text"
         placeholder="Max Price"
         @input="sanitizePrice('max')"
         class="input" />

      <!-- Market name -->
      <input
         v-model="marketName"
         placeholder="Market"
         class="input"
         value="korzinka" />

      <!-- Sort options -->
      <select v-model="sortBy" class="select">
         <option value="current_price">Narx</option>
         <option value="product_name">Nom</option>
      </select>
      <select v-model="sortOrder" class="select">
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
.filter-panel {
   width: 100%;
   box-sizing: border-box;
   display: flex;
   flex-wrap: wrap;
   gap: 0.75rem;
   padding: 1rem;
   background: #fafafa;
   border-radius: 12px;
   border: 1px solid #eee;
   margin-bottom: 1rem;
}
.input,
.select {
   padding: 0.55rem 0.75rem;
   border: 1px solid #ddd;
   border-radius: 8px;
   font-size: 0.9rem;
   outline: none;
   transition: all 0.2s ease;
   min-width: 120px;
   background: #fff;
}
.select:hover {
   cursor: pointer;
   box-shadow: 0 0 4px rgba(64, 158, 255, 0.3);
}
.filter-panel input:focus,
.filter-panel select:focus {
   border-color: #409eff;
   box-shadow: 0 0 4px rgba(64, 158, 255, 0.3);
}

.input-error {
   border: 2px solid #ff4d4d !important;
}

/* Button */
.filter-panel button {
   padding: 0.6rem 1rem;
   background: #409eff;
   border: none;
   color: white;
   border-radius: 8px;
   font-size: 0.9rem;
   cursor: pointer;
   transition: all 0.2s ease;
}

.filter-panel button:hover {
   background: #318ae5;
}

.filter-panel button:active {
   transform: scale(0.97);
}

/* Mobile */
@media (max-width: 600px) {
   .filter-panel {
      gap: 0.5rem;
      padding: 0.75rem;
   }

   .input,
   .filter-panel button {
      width: 100%;
      min-width: 0;
   }
   .select {
      width: calc((100% - 0.5rem) / 2);
   }
}
</style>
