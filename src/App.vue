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
  <div class="layout-container-demo">
  <el-container class="page_container">
    <el-header class="header-flex"> 
    <img alt="logo" class="logo" src="/logo.jpg" width="50" height="50"/>
    <h1>相声可视化</h1>      
      <!-- <div class="logo">
        <img src="/logo.jpg" alt="xiangsheng logo" />
      </div> -->
          
    </el-header>
    <el-container >
      <el-aside width="250px">
        <el-row class="tac">
          <el-col :span="24">
            <!-- <h5 class="mb-2">Custom colors</h5> -->
            <el-menu
              class="el-menu-vertical-demo"
              :default-active="activeIndex"
              @open="handleOpen"
              @close="handleClose"
            >
              <el-menu-item index="/word" @click="handleSelect('word')">
                <template #title>
                  <el-icon><location /></el-icon>
                  <span>Word</span>
                </template>
              </el-menu-item>
              <el-menu-item index="/sentence" @click="handleSelect('sentence')">
                <el-icon><icon-menu /></el-icon>
                <span>Sentence</span>
              </el-menu-item>
              <el-menu-item index="/paragraph" @click="handleSelect('paragraph')">
                <el-icon><document /></el-icon>
                <span>Paragraph</span>
              </el-menu-item>
              <el-menu-item index="/d3test" @click="handleSelect('d3test')">
                <el-icon><setting /></el-icon>
                <span>D3 Example</span>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-main><RouterView /></el-main>
    </el-container>
  </el-container>
  </div>
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
div.layout-container-demo {
  height: 100%;
  width: 100%;
}
.page_container {
  height: 100%;
}
.el-row.tac {
  height: 100%;
}
.el-menu{
  height: 100%;

}

.layout-container-demo .el-header h1 {
  margin-left: 20px; /* Adjust the value as needed */
}


.layout-container-demo .el-header {
  background-color: #fff;
  color: var(--el-text-color-primary);
  padding: 8px;
  display: flex;
  align-items: center;
}
.layout-container-demo .el-aside {
  position: relative;

  color: var(--el-text-color-primary);
  /* background: var(--el-color-primary-light-8); */
}
.layout-container-demo .el-menu {
  border-right: none;
}
.layout-container-demo .el-main {
  padding: 0;
}
</style>
