import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import NotFound from "@/views/NotFound.vue";
import About from "../views/About.vue";
import Disclaimer from "../views/Disclaimer.vue";

const routes = [
   { path: "/", name: "Home", component: Home },
   { path: "/about", name: "About", component: About },
   { path: "/disclaimer", name: "Disclaimer", component: Disclaimer },
   { path: "/:pathMatch(.*)*", name: "notfound", component: NotFound },
];

const router = createRouter({
   history: createWebHistory(),
   routes,
});

export default router;
