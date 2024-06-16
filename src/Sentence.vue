<template>
    <div class="main_page">
        <PageTitle msg="Sentence" />
        <svg  id="mainsvg" class="svgs"></svg>
    </div>
</template>

<script setup>
import * as d3 from "d3";
import PageTitle from './components/PageTitle.vue';
</script>

<script>
import * as d3 from "d3";
export default {
    mounted(){
        // d3.select("#mainsvg")
        //     .append("text")
        //     .attr("x", 800)
        //     .attr("y", 400)
        //     .text("hello, sentence");
    },
};

</script> 