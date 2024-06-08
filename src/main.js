import './assets/main.css'
import { createApp } from 'vue'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
import App from './App.vue'
import d3test from './d3test.vue'
import menu from './menu.vue'


const testapp = createApp(d3test)
testapp.use(ElementPlus)
testapp.mount('#app')

const menuapp = createApp(menu)
menuapp.use(ElementPlus)
menuapp.mount('#menu')


// createApp(App).mount('#app2')
