<template>
  <div class="main_page">
    <PageTitle msg="Word" />
    <el-row :gutter="20" style="margin-left: 0">
      <el-col :span="20">
        <el-card class="box-card black-bg white-text">
          <div slot="header" class="clearfix">
            <span>词云</span>
          </div>

          <div>
            <img :src="wordcloudImage" width="100%" @click="openLightbox('wordcloud')" v-if="wordcloudImage" />
            <p v-else>Loading...</p>
          </div>
          <div>
            <img :src="wordbarImage" width="100%" @click="openLightbox('wordbar')" v-if="wordbarImage" />
            <p v-else>Loading...</p>
          </div>

        </el-card>
      </el-col>
      <el-col :span="4">
        <el-card class="box-card black-bg white-text" >
          <div slot="header" class="clearfix">
            <span>词频统计</span>
          </div>
          <div>
            <ul>
              <li v-for="(value, key, index) in wordFreq" :key="key" class="word-freq-item" >
                <span class="word-key">{{ key }}</span>: 
                <span class="word-value">{{ value }}</span>
              </li>
            </ul>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <svg id="mainsvg" class="svgs"></svg>
    <vue-easy-lightbox
      :visible="lightboxVisible"
      :imgs="lightboxImages"
      @hide="lightboxVisible = false"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick,watch } from 'vue';
import { useRoute } from 'vue-router';
import PageTitle from '../src/components/PageTitle.vue';
import axios from 'axios';
import VueEasyLightbox from 'vue-easy-lightbox';
const wordcloudImage = ref('');
const wordbarImage = ref('');
const wordFreq = ref({});
const lightboxVisible = ref(false);
const lightboxImages = ref([]);
const route = useRoute();


const fetchurl = async () => {
 
  const data = route.query.data ? JSON.parse(route.query.data) : null;
  console.log('Received_push_data:', data);
  if (data) {
    wordcloudImage.value = `${window.location.origin}/${data.wordcloud_image}`;
    wordbarImage.value = `${window.location.origin}/${data.wordbar_image_path}`;
    // Fetch the word frequency data from the provided path
    try {
      const wordFreqResponse = await axios.get(`${window.location.origin}/${data.word_freq_path}`);
      wordFreq.value = wordFreqResponse.data;
      // limit the wordfreq length to 100
      wordFreq.value = Object.fromEntries(Object.entries(wordFreq.value).slice(0, 100));
    } catch (error) {
      console.error('Error fetching word frequency data:', error);
    }
  }
};





onMounted(() => {
  fetchurl();
});

watch(
  () => route.query.data,
  async () => {
    await fetchurl();
  }
);
const openLightbox = (type) => {
  if (type === 'wordcloud') {
    lightboxImages.value = [wordcloudImage.value];
  } else if (type === 'wordbar') {
    lightboxImages.value = [wordbarImage.value];
  }
  lightboxVisible.value = true;
};



</script>

<style scoped>
.main_page {
  padding: 20px;
}
.box-card {
  display: flex;
  width: 100%;
}
.white-text {
  color: #fff; 
}
.text {
  font-size: 14px;
}
.wordcloud-image {
  margin: 0;
  padding: 0;
  display: block;
  cursor: pointer;
  width: 100%;
}


.black-bg {
  background-color: #282828;
}
ul {
  list-style-type: none;
  padding: 0;
}

.word-freq-item {
  margin-bottom: 10px;
  color: #fff; 
  font-size: 16px; 
}

.word-key {
  font-weight: bold; 
  margin-right: 5px;
}

.word-value {
  font-style: italic; 
}
</style>