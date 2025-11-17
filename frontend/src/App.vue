<template>
   <div id="app">
      <!-- Header -->
      <header class="site-header">
         <div class="container header-container">
            <router-link to="/" class="logo">Qulay Narx</router-link>
            <nav class="site-nav">
               <router-link to="/">Mahsulotlar</router-link>
               <router-link to="/about">Biz haqimizda</router-link>
               <router-link to="/disclaimer">Disclaimer</router-link>
            </nav>
         </div>
      </header>

      <!-- Main content -->
      <main class="site-main">
         <router-view />
      </main>

      <!-- Footer -->
      <Footer />
   </div>
</template>

<script setup>
import Footer from "./components/Footer.vue";
</script>

<style>
/* Global style */
body,
html,
#app {
   margin: 0;
   padding: 0;
   height: 100%;
   font-family: "JetBrains Mono", monospace;
}

#app {
   display: flex;
   flex-direction: column;
   min-height: 100vh;
}

/* Header */
.site-header {
   background-color: #222025;
   color: #fff;
}

.header-container {
   display: flex;
   justify-content: space-between;
   align-items: center;
   max-width: 1200px;
   margin: 0 auto;
   padding: 15px 20px;
}
.logo {
   color: #fff;
}
.site-nav a {
   color: #fff;
   margin-left: 15px;
   text-decoration: none;
   font-weight: 500;
}

.site-nav a:hover {
   text-decoration: underline;
}

/* Main content */
.site-main {
   flex: 1; /* footer pastga tushsin */
   max-width: 1200px;
   margin: 0 auto;
   width: 100%;
   padding: 20px;
}

/* Footer */
footer {
   width: calc(100%-2rem);
}
</style>
