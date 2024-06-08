<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Menu from './components/Menu.vue'
import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
} from '@element-plus/icons-vue'
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<template>
  <p>
  <el-row class="tac">
    <el-col :span="24">
      <h5 class="mb-2">Custom colors</h5>
      <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        :default-active="activeIndex"
        text-color="#fff"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-menu-item index="/word" @click="handleSelect('word')">
          <template #title>
            <el-icon><location /></el-icon>
            <span>Navigator One</span>
          </template>
        </el-menu-item>
        <el-menu-item index="/sentence" @click="handleSelect('sentence')">
          <el-icon><icon-menu /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>
        <el-menu-item index="/paragraph" @click="handleSelect('paragraph')">
          <el-icon><document /></el-icon>
          <span>Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="/d3test" @click="handleSelect('d3test')">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</p>
  <main>
    <RouterView />
  </main>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: 'word', // Set to the default route name or path
    };
  },
  watch: {
    $route () {
      this.setCurrentRoute()
    }
  },
  mounted () {
  },
  created () {
    this.setCurrentRoute()
  },
  methods: {
    handleSelect (key) {
      // Update the route based on the selected menu item
      this.$router.push({ name: key });
    },
    setCurrentRoute () {
      this.activeIndex = this.$route.name;
    }
  }
}
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
