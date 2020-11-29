<template>
  <v-card class="max-height rounded-lg" color="primary">
    <slot name="header"></slot>
    <v-divider color="white"></v-divider>
    <div class="card-content pa-2">
      <slot></slot>
    </div>
  </v-card>
</template>
<script>
export default {};
</script>
<style>
.card-header {
  height: 73px;
}
.max-height {
  height: 100%;
  max-height: 100%;
  min-height: 100%;
}
</style>
