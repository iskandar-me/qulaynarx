<template>
   <div class="pagination">
      <button @click="prev" :disabled="page === 1">Prev</button>

      <span>
         Jami {{ totalCount }} ta product, ko‘rsatilyapti {{ startIndex }}–{{
            endIndex
         }}
      </span>

      <button @click="next" :disabled="page === totalPages">Next</button>
   </div>
</template>

<script setup>
import { defineProps, computed } from "vue";

const props = defineProps({
   page: Number,
   totalPages: Number,
   limit: Number,
   totalCount: Number,
});

const startIndex = computed(() => {
   return (props.page - 1) * props.limit + 1;
});

const endIndex = computed(() => {
   return Math.min(props.page * props.limit, props.totalCount);
});

const emit = defineEmits(["change"]);

const prev = () => emit("change", props.page - 1);
const next = () => emit("change", props.page + 1);
</script>

<style scoped>
.pagination {
   display: flex;
   align-items: center;
   justify-content: center;
   gap: 1rem;
   margin: 1rem 0;
}

button {
   padding: 0.3rem 0.7rem;
   border: 1px solid #ccc;
   border-radius: 4px;
   background: white;
   cursor: pointer;
}

button:disabled {
   opacity: 0.5;
   cursor: not-allowed;
}
</style>
