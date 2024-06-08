import './assets/main.css'
import { createApp } from 'vue'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
import router from './router'
import App from './App.vue'
// import D3test from './D3test.vue'
// import Menu from './components/Menu.vue'


// const testapp = createApp(D3test)
// testapp.use(ElementPlus)
// testapp.mount('#D3test')

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')

