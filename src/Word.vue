<template>
    <div class="main_page">
        <PageTitle msg="Word" />
        <svg  id="mainsvg" class="svgs"></svg>
    </div>
</template>

<script setup>
import * as d3 from "d3";
import PageTitle from './components/PageTitle.vue';
</script>

<script>
export default {
    mounted(){
        // d3.select("#mainsvg")
        //     .append("text")
        //     .attr("x", 800)
        //     .attr("y", 400)
        //     .text("hello, words");
    },
};

</script> 