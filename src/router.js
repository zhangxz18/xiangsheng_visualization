import { createRouter, createWebHistory ,createWebHashHistory} from 'vue-router'
import Word from './Word.vue';
import Sentence from './Sentence.vue';
import Paragraph from './Paragraph.vue';
import D3test from './D3test.vue';

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
    { path: '/', redirect: '/word' },
    { path: '/word', name:'word' ,component: Word },
    { path: '/sentence', name:'sentence', component: Sentence },
    { path: '/paragraph', name:'paragraph', component: Paragraph },
    { path: '/d3test', name:'d3test', component: D3test },]
})

export default router;