<template>
   <div class="product-card">
      <img :src="product.image_url" alt="" />
      <h3>{{ product.market_name }}</h3>
      <h3>{{ product.product_name }}</h3>
      <p>
         Current Price:
         <span style="font-weight: bold; text-decoration: underline">
            {{ product.current_price }}</span
         >
         so'm
      </p>
      <p style="text-decoration: line-through">
         Old Price: {{ product.old_price }} so'm
      </p>
      <p v-if="product.discount">
         Discount: <span style="color: crimson">{{ product.discount }}</span>
      </p>
   </div>
</template>

<script setup>
defineProps({
   product: Object,
});
</script>

<style scoped>
.product-card {
   border: 1px solid #ccc;
   padding: 10px;
   margin: 5px;
   width: 200px;
}
.product-card img {
   width: 100%;
   height: auto;
}
</style>
