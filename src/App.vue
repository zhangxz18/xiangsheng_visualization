<template>
  <div class="layout-container-demo">
    <el-container class="page_container">
      <el-header class="header-flex">
        <img alt="logo" class="logo" src="/logo.jpg" width="50" height="50" />
        <h1>相声可视化</h1>
      </el-header>
      <el-container>
        <el-aside width="250px">
          <el-row class="tac">
            <el-col :span="24">
              <el-menu
                class="el-menu-vertical-demo"
                :default-active="activeIndex"
                @open="handleOpen"
                @close="handleClose"
              >
                <el-menu-item index="/word" @click="handleSelect('word')">
                  <template #title>
                    <el-icon><location /></el-icon>
                    <span>词云和词频</span>
                  </template>
                </el-menu-item>
                <el-menu-item index="/sentence" @click="handleSelect('sentence')">
                  <el-icon><icon-menu /></el-icon>
                  <span>情绪演绎</span>
                </el-menu-item>
                <el-menu-item index="/paragraph" @click="handleSelect('paragraph')">
                  <el-icon><document /></el-icon>
                  <span>主题分析：堆叠柱状图</span>
                </el-menu-item>
                <el-menu-item index="/d3test" @click="handleSelect('d3test')">
                  <el-icon><setting /></el-icon>
                  <span>主题分析：桑基图</span>
                </el-menu-item>
                <div class="menu-checkbox-container">
                  <h3>XiangSheng Directory
                    <el-button size="mini" @click="selectAll">全选</el-button>
                    <el-button size="mini" @click="deselectAll">取消</el-button>
                  </h3>
                  <el-checkbox-group v-model="selectedFiles">
                    <div class="checkbox-scroll">
                      <el-checkbox
                        v-for="file in files"
                        :key="file"
                        :label="file"
                      >{{ file }}</el-checkbox>
                    </div>
                  </el-checkbox-group>
                  <el-button type="primary" @click="processFiles">确认</el-button>
                </div>
              </el-menu>
            </el-col>
          </el-row>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue';

const files = ref([]);
const selectedFiles = ref([]);
const activeIndex = ref('word');
const router = useRouter()


const handleOpen = (key, keyPath) => {
  console.log(key, keyPath);
};

const handleClose = (key, keyPath) => {
  console.log(key, keyPath);
};

const handleSelect = (key) => {
  // Update the route based on the selected menu item
  router.push({ name: key });
  console.log('Selected:', key);
};

const fetchFiles = async () => {
  try {
    const response = await axios.get('http://localhost:3001/api/files');
    files.value = response.data;
  } catch (error) {
    console.error('Error fetching files:', error);
  }
};

const processFiles = async () => {
  try {
    const response = await axios.post('http://localhost:3001/api/process-files', {
      files: selectedFiles.value,
    });

    console.log('Processing response:', response.data);
    
    router.push({ name: 'word', query: { data: JSON.stringify(response.data) } });
    
  } catch (error) {
    console.error('Error processing files:', error);
  }
};


const selectAll = () => {
  selectedFiles.value = files.value.slice();
};

const deselectAll = () => {
  selectedFiles.value = [];
};

onMounted(() => {
  fetchFiles();
});
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
.el-menu {
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

.menu-checkbox-container {
  margin-top: 10px;
  padding: 10px;
  border-top: 1px solid #ebeef5;
}

.menu-checkbox-container h3 {
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  font-weight: bold;
}

.menu-checkbox-container .el-button {
  margin-left: 5px;
  font-size: 12px;
  padding: 3px 5px;
}

.checkbox-scroll {
  max-height: 300px; /* Adjust as needed */
  overflow-y: auto;
  border: 1px solid #ebeef5;
  padding: 10px;
  margin-bottom: 10px;
}
</style>