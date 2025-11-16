<template>
   <footer class="site-footer">
      <div class="footer-content">
         <p>© {{ year }} QulayNarx. All rights reserved.</p>
         <!-- <p>
            Sayt ma'lumotlari ochiq manbalardan, ya'ni do'konlarning rasmiy
            veb-saytlaridan web scraping orqali olingan. Narxlar do'konlardagi
            narxlar bilan farq qilishi mumkin va biz ushbu farqlar uchun
            javobgar emasmiz.
         </p> -->
         <div class="footer-links">
            <router-link to="/about">Biz haqimizda</router-link>
            <router-link to="/disclaimer">Disclaimer</router-link>
         </div>
      </div>
   </footer>
</template>

<script setup>
import { ref } from "vue";
const currentYear = ref(new Date().getFullYear());
const originYear = 2025;
let year = 2025;
if (originYear == currentYear.value) {
   year = 2025;
} else {
   year = `${originYear}-${currentYear.value}`;
}
</script>

<style scoped>
.site-footer {
   background-color: #222025;
   color: #fff;
   padding: 2rem 1rem;
   text-align: center;
   font-size: 0.9rem;
}
.site-footer .footer-content p {
   margin: 0.5rem 0;
}
.site-footer .footer-links {
   margin-top: 1rem;
}
.site-footer .footer-links a {
   color: #fff;
   margin: 0 10px;
   text-decoration: none;
}
.site-footer .footer-links a:hover {
   text-decoration: underline;
}
</style>
