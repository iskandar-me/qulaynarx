<template>
   <div class="product-card" :class="marketClass">
      <h3 class="market-name">{{ product.market_name }}</h3>
      <div class="product-tags">
         <div class="product-tag">
            <span
               v-if="
                  product.discount_period &&
                  product.discount_period.trim() !== ''
               "
               class="discount-period"
               >{{ product.discount_period }}</span
            >
            <span
               v-if="
                  product.promotion_info && product.promotion_info.trim() !== ''
               "
               class="promotion-info"
               >{{ product.promotion_info }}</span
            >
         </div>
         <img class="img" :src="product.image_url" alt="product image" />

         <p class="old-price">{{ product.old_price }}</p>
         <p class="current-price">{{ product.current_price }}</p>
         <p v-if="product.discount" class="discount">
            <span>{{ product.discount }}</span>
         </p>
      </div>

      <h3 class="name">{{ product.product_name }}</h3>
      <h3 class="weight">{{ product.weight }}</h3>
   </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({ product: Object });

const marketClass = computed(() => {
   switch (props.product.market_name.toLowerCase()) {
      case "korzinka":
         return "market-korzinka";
      case "makro":
         return "market-makro";
      case "baraka":
         return "market-baraka";
      default:
         return "market-default";
   }
});
</script>

<style scoped>
.product-card {
   border-radius: 12px;
   box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
   transition: transform 0.2s ease, box-shadow 0.2s ease;
   margin: 0.5rem;
}

.product-card:hover {
   transform: translateY(-1px);
   box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}
.market-name {
   text-transform: uppercase;
   font-weight: bold;
   font-size: 1.25rem;
}
.img {
   object-fit: cover;
   border-radius: 0.5rem;
}
.market-korzinka {
   display: flex;
   flex-direction: column;
   background-color: #f7f7f9;
   border-radius: 8px;
   height: auto !important;
   padding: 16px 8px 12px;
   position: relative;
}
.market-korzinka:hover {
   cursor: pointer;
}
.market-korzinka .product-tags {
   font-weight: 700;
   left: 2px;
   line-height: 12px;
   position: relative;
   font-weight: 400;
   line-height: 1.1875;
}
.market-korzinka .product-tag {
   display: flex;
   flex-direction: column;
   position: absolute;
   top: 8px;
   z-index: 2;
}
.market-korzinka .discount-period {
   display: inline;
   border-radius: 22px;
   background-color: #95cde8;
   color: #e4002b;
   font-size: 10px;
   font-style: italic;
   font-weight: 700;
   padding: 1px 4px;
   transform: skew(-15deg);
   z-index: -1;
}

.market-korzinka .promotion-info {
   font-size: 10px;
   font-style: italic;
   font-weight: 700;
   left: 2px;
   line-height: 12px;
   padding: 6px 14px;
   position: relative;
   top: 12px;
   z-index: 2;
   border-radius: 22px;
   background-color: #e4002b;
   color: #fff;
   transform: skew(-15deg);
}
.market-korzinka .img {
   margin-bottom: 1rem;
   width: 100%;
}
.market-korzinka .old-price,
.market-korzinka .current-price {
   display: inline;
   width: min-content;
   font-style: italic;
   padding: 8px;
   text-align: end;
   background-color: #f6e81f;
   color: #e4002b;
   border-radius: 50px;
}
.market-korzinka .old-price {
   text-decoration: line-through;
   font-size: 14px;
   margin-right: 8px;
}
.market-korzinka .current-price {
   font-size: 18px;
}
.market-korzinka .discount {
   border-radius: 50px;
   width: min-content;
   font-style: italic;
   padding: 8px;
   text-align: end;
   background-color: #e4002b;
   color: #fff;
   font-size: 16px;
}
.market-korzinka .name {
   color: #222025;
   font-size: 16px;
   font-weight: 400;
   line-height: 1.1875;
   word-wrap: break-word;
   letter-spacing: -0.3px;
   margin-bottom: 8px;
}
.market-korzinka .weight {
   font-size: 16px;
   font-weight: 400;
   line-height: 1.1875;
   color: #9c9b9f;
   letter-spacing: -0.3px;
   margin: 0 0 0 15px;
}

/* ======MAKRO ======*/
.market-makro {
   background: hsla(34, 67%, 92%, 0.6);
   border-radius: 10px;
   font-family: sans-serif;
   color: #005809;
   padding: 4px;
}

.market-makro .promotion-info {
   display: none;
}
.market-makro .img {
   background-color: #fff;
   width: 100%;
   color: #005809;
   font-size: 18px;
   font-style: normal;
   font-weight: 700;
   line-height: 120%;
   margin-bottom: 1rem;
}
.market-makro .name {
   font-size: 18px;
   font-weight: 700;
}
.market-makro .old-price {
   text-decoration: line-through;
   margin: 0;
   font-size: 14px;
}
.market-makro .current-price {
   margin: 0;
   font-size: 18px;
   font-weight: 700;
   line-height: 100%;
   text-wrap: nowrap;
}
.market-makro .discount {
   background-color: #e4002b;
   color: #fff;
   transform: rotate(-20deg);
   width: min-content;
   font-weight: 900;
   padding: 5px 15px;
   font-size: 18px;
   border-radius: 1rem;
}
.market-makro .weight {
   display: none;
}

/* ==== BARAKA ==== */

.market-baraka {
   padding: 0.75rem;
}
.market-baraka .market-name {
   color: #fe5000;
}
.market-baraka:hover {
   cursor: pointer;
}
.market-baraka .promotion-info,
.market-baraka .discount-period {
   display: none;
}
.market-baraka .img {
   width: 100%;
   margin-bottom: 1rem;
}
.market-baraka .old-price {
   background-color: #fe5000;
   padding: 8px;
   color: #fff;
   width: min-content;
   margin: 0;
   border-radius: 50px;
   display: inline;
   margin-right: 0.5rem;
   font-size: 16px;
   text-decoration: line-through;
}
.market-baraka .current-price {
   display: inline;
   margin: 0;
   padding: 8px;
   width: min-content;
   background-color: #fe5000;
   color: #fff;
   font-size: 18px;
   border-radius: 50px;
}
.market-baraka .discount {
   background-color: #e4002b;
   color: #fff;
   width: min-content;
   padding: 8px;
   border-radius: 50px;
   font-size: 16px;
}
.market-baraka .name {
   font-size: medium;
   font-weight: 700;
}
.market-baraka:hover .name {
   color: #fe5000;
   cursor: pointer;
}
.market-baraka .weight {
   display: none;
}

/* ===== MOBILE STYLES ===== */
@media (max-width: 600px) {
   .product-card {
      width: 100%;
      margin: 0.5rem 0;
      padding: 0.75rem;
   }

   /* ===== KORZINKA ===== */
   .market-korzinka {
      padding: 12px 8px;
      height: auto !important;
   }

   .market-korzinka .img {
      margin-bottom: 0.5rem;
      width: 100%;
   }

   .market-korzinka .discount-period,
   .market-korzinka .promotion-info {
      font-size: 8px;
      padding: 2px 4px;
   }

   .market-korzinka .old-price,
   .market-korzinka .current-price {
      font-size: 14px;
      padding: 6px;
   }

   .market-korzinka .discount {
      font-size: 14px;
      padding: 6px;
   }

   .market-korzinka .name {
      font-size: 14px;
   }

   .market-korzinka .weight {
      font-size: 14px;
      margin-left: 8px;
   }

   /* ===== MAKRO ===== */
   .market-makro {
      padding: 4px;
      font-size: 14px;
   }

   .market-makro .img {
      margin-bottom: 0.5rem;
   }

   .market-makro .name {
      font-size: 16px;
   }

   .market-makro .old-price {
      font-size: 12px;
   }

   .market-makro .current-price {
      font-size: 16px;
   }

   .market-makro .discount {
      font-size: 14px;
      padding: 4px 10px;
   }

   /* ===== BARAKA ===== */
   .market-baraka {
      padding: 0.5rem;
   }

   .market-baraka .old-price,
   .market-baraka .current-price {
      font-size: 14px;
      padding: 6px;
   }

   .market-baraka .discount {
      font-size: 14px;
      padding: 6px;
   }

   .market-baraka .name {
      font-size: 14px;
   }
}
</style>
