import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import "@mdi/font/css/materialdesignicons.css"; // Ensure you are using css-loader

Vue.use(Vuetify);

const opts = {
  theme: {
    icons: { iconfont: "mdi" },
    dark: false,
    themes: {
      light: {
        primary: "#9EEBCF",
        secondary: "#19A974",
        tertiary: "FF8500",
        accent: "#145C43",
        error: "#F44336",
        info: "#2196F3",
        success: "#30DB9F",
        warning: "#FFC107"
      }
    }
  }
};

export default new Vuetify(opts);
