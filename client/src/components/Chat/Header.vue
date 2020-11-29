<template>
  <div class="header-container">
    <div class="header-title" color="red">
      <p class="header-title-text">
        {{ chatTitle }}
      </p>
    </div>

    <div>
      <v-btn icon small fab @click="onAdd"
        ><v-icon small>mdi-plus</v-icon></v-btn
      >
      <v-btn icon small fab @click="onSound"
        ><v-icon small>mdi-volume-high</v-icon></v-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    participants() {
      return this.$store.state.participants;
    },
    myself() {
      return this.$store.state.myself;
    },
    chatTitle() {
      return this.$store.state.chatTitle;
    },
    hasHeaderSlot: function() {
      return !!this.$slots["header"];
    }
  },
  methods: {
    onAdd() {
      this.$emit("add");
    },
    onSound() {
      this.$emit("sound");
    }
  }
};
</script>

<style lang="less">
.quick-chat-container .header-container {
  height: 30px;
  background-color: #ff8500;
  display: flex;
  padding: 0 20px 0 10px;
  align-items: center;

  .header-title {
    padding: 10px;
    flex: 1;
    text-align: left;
  }

  .header-title-text {
    margin-bottom: 0;
  }

  .header-paticipants-text {
    color: #e4e4e4;
    font-size: 12px;
    overflow: hidden;
  }

  .header-exit-button {
    text-decoration: none;
    color: #fff;
    font-size: 20px;
  }
}
</style>
