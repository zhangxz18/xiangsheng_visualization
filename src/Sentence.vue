<template>
  <div class="main_page">
    <PageTitle msg="Sentence" />
    <select v-model="selectedFile" @change="loadMdFile" class="custom-select">
      <option v-for="file in mdFiles" :key="file" :value="file">{{ file }}</option>
    </select>
    <div class="display-container">
      <div class="text-container">
        <p v-for="(line, index) in lines" 
           :key="index" 
           @mouseover="handleMouseOver(line, index)" 
           @mouseleave="hideEmoji"
           :class="{ highlighted: currentLine === index }">
          {{ line.split(' ').slice(0, -1).join(' ') }}
        </p>
      </div>
      <div class="emoji-container">
        <p v-if="currentEmoji">{{ currentEmoji }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PageTitle from './components/PageTitle.vue';

const mdFiles = ref(['百戏名.md', '不宜动土.md', '当行论.md', '画扇面.md', '开殃榜.md', '练气功.md', '刘伶醉酒.md', '扭嘴儿.md', '聘秘书.md', '山西家信.md', '邵康节测字.md', '双音字.md', '说大话.md', '阳平关.md', '战马超.md', '主客问答.md']);
const selectedFile = ref(mdFiles.value[0]);
const lines = ref([]);
const currentEmoji = ref('');
const currentLine = ref(null);

// Function to load md file content
const loadMdFile = () => {
  fetch(`/response-4o/${selectedFile.value}`)
    .then(response => response.text())
    .then(data => {
      lines.value = data.split('\n');
    });
};

// Combined function to handle mouse over
const handleMouseOver = (line, index) => {
  currentEmoji.value = line.split(' ').pop();
  currentLine.value = index;
};

// Function to hide emoji
const hideEmoji = () => {
  currentEmoji.value = '';
  currentLine.value = null;
};

// Load initial file
onMounted(() => {
  loadMdFile();
});
</script>

<style scoped>
.main_page {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.custom-select {
  width: 200px;
  height: 40px;
  font-size: 1.2em;
  margin-bottom: 20px;
  padding: 5px;
}

.display-container {
  display: flex;
  align-items: flex-start;
}

.text-container {
  width: 70%;
  height: 600px;
  padding: 10px;
  border-right: 1px solid #ccc;
  overflow-y: scroll;
}

.text-container p {
  margin: 5px 0;
  cursor: pointer;
  border: 2px solid transparent; /* 原本无色边框 */
}

.text-container p.highlighted {
  border-color: yellow; /* 修改颜色为黄色 */
}

.emoji-container {
  width: 30%;
  padding: 10px;
  font-size: 20em;
  text-align: center;
}
</style>
