<template>
  <v-app>
    <v-navigation-drawer
      app
      expand-on-hover
      class="ma-3 rounded-lg"
      floating
      elevation="4"
    >
      <v-card color="primary" class="max-height rounded-lg dense" elevation="4">
        <v-list>
          <v-list-item class="px-2">
            <v-list-item-avatar>
              <v-img
                src="https://randomuser.me/api/portraits/women/85.jpg"
              ></v-img>
            </v-list-item-avatar>
            <v-list-item-content
              class="py-0"
              style="letter-spacing: 0.05px;line-height: 0;"
            >
              <v-list-item-title>
                <span style="font-size: 9px; font-weight: 600;">{{
                  currentUser.name
                }}</span>
              </v-list-item-title>
              <v-list-item-subtitle>
                <span style="font-size: 8px; font-weight: 500;">{{
                  currentUser.email
                }}</span>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-divider color="white"></v-divider>

        <v-list nav dense rounded>
          <v-list-item
            v-for="user in users"
            :key="user.id"
            link
            color="secondary"
          >
            <v-list-item-icon>
              <v-btn
                depressed
                rounded
                elevation="4"
                class="mx-n2 pa-1 my-n2"
                block
                color="secondary"
              >
                <span>{{ formatName(user.name) }}</span>
              </v-btn>
            </v-list-item-icon>
            <v-list-item-content class="py-0">
              <v-list-item-title>
                {{ user.name }}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ user.email }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link color="secondary">
            <v-list-item-icon>
              <v-btn
                depressed
                rounded
                elevation="4"
                class="mx-n2 pa-1 my-n2"
                block
                icon
                color="secondary"
              >
                <v-icon lg>mdi-account-plus-outline</v-icon>
              </v-btn>
            </v-list-item-icon>
            <v-list-item-content
              class="py-0"
              style="letter-spacing: 0.05px;line-height: 0;"
            >
              <v-list-item-title>
                <span>Добавить контакт</span>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
    </v-navigation-drawer>
    <v-main class="main-container mx-auto my-auto">
      <v-container fluid class="max-height px-4">
        <v-row no-gutters class="max-height">
          <v-col cols="3" class="max-height">
            <column-card>
              <template #header>
                <v-list color="primary">
                  <v-list-item class="pa-1">
                    <v-list-item-content class="py-0">
                      <v-list-item-title>
                        {{ currentUser.name }}
                      </v-list-item-title>
                      <v-list-item-subtitle
                        >{{ currentUser.email }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </template>
              <v-card
                class="mx-auto d-flex justify-start flex-column"
                color="primary"
                flat
              >
                <v-btn icon class="text-right align-self-end pa-0">
                  <v-icon>mdi-cog-outline</v-icon>
                </v-btn>
                <v-list color="primary" class="text-left align-self-start pa-0">
                  <v-list-item v-for="folder in folders" :key="folder.id">
                    <v-list-item-content>
                      <v-btn
                        block
                        left
                        color="primary"
                        depressed
                        large
                        class="ml-n2"
                      >
                        {{ folder.name }}
                        <v-icon v-if="folder.type == 1" right color="orange">
                          mdi-fire
                        </v-icon>
                      </v-btn>
                      <v-list-item-subtitle
                        v-for="child in folder.children"
                        :key="child.id"
                      >
                        <v-btn text small class="ml-2">
                          {{ child.name }}
                          <v-icon v-if="child.type == 1" right color="orange">
                            mdi-fire
                          </v-icon></v-btn
                        >
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card>
            </column-card>
          </v-col>
          <v-col cols="9" color="green lighten-2">
            <column-card class="ml-4">
              <template #header>
                <v-list color="primary">
                  <v-list-item class="px-6">
                    <v-list-item-title>
                      <v-text-field
                        color="white"
                        hide-details="auto"
                        placeholder="Поиск"
                        clearable
                        dense
                        rounded
                        filled
                      >
                        <template #append>
                          <v-btn icon small class="mb-2">
                            <v-icon xs>mdi-microphone</v-icon>
                          </v-btn>
                        </template>
                      </v-text-field>
                    </v-list-item-title>
                    <v-list-item-avatar>
                      <v-img
                        src="https://randomuser.me/api/portraits/women/85.jpg"
                      ></v-img>
                    </v-list-item-avatar>
                  </v-list-item>
                </v-list>
              </template>
              <v-row no-gutters>
                <v-col>
                  <chat-box></chat-box>
                </v-col>
                <v-col>
                  <chat-box></chat-box>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <chat-box></chat-box>
                </v-col>
                <v-col>
                  <chat-box></chat-box>
                </v-col>
              </v-row>
            </column-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import ColumnCard from "@/components/ColumnCard.vue";
import ChatBox from "@/components/ChatBox.vue";
export default {
  name: "main-page",
  components: { ColumnCard, ChatBox },
  data() {
    return {
      folders: [
        {
          id: 1,
          name: "Договоры",
          children: [
            { id: 2, name: "Договор ЦИП 270" },
            { id: 3, name: "Договор ИТ 202" },
            { id: 4, name: "Продление договора" }
          ]
        },
        {
          id: 5,
          name: "Бизнес-процессы",
          children: [
            {
              id: 6,
              name: "Помощь с ресурсами Wonder",
              type: 1
            },
            {
              id: 10,
              name: "Тестирование моделей"
            },
            {
              id: 11,
              name: "Итоги обсуждения онтологии"
            },
            {
              id: 12,
              name: "Внедрение ПО"
            }
          ]
        },
        {
          id: 15,
          name: "Разное",
          children: [
            { id: 16, name: "Кремлевская елка" },
            { id: 17, name: "Странные дела" },
            { id: 18, name: "Спасибо" }
          ]
        }
      ],
      currentUser: {
        name: "Смирнова Анна Сергеевна",
        id: 1,
        email: "smirnovaanna@gmail.com"
      },
      users: [
        {
          name: "Акмурзин Наиль Рамильевич",
          id: 1,
          email: "nailakmurzin@gmail.com"
        },
        {
          name: "Музафаров Ильгам Ильшатович",
          id: 2,
          email: "ilgammuz@gmail.com"
        }
      ]
    };
  },
  methods: {
    formatName(name) {
      return name
        .split(" ", 2)
        .filter(s => s)
        .map(str => str[0].toLocaleUpperCase())
        .join("");
    }
  }
};
</script>
<style>
.main-container {
  max-width: 1920px;
  min-height: 1080px;
  width: 100%;
}
.max-height {
  height: 100%;
  max-height: 100%;
  min-height: 100%;
}
.main {
  height: 100%;
  width: 100%;
}
.left-nav-bars {
  height: 100%;
}
</style>
