<template>
    <div class="main_page">
        <PageTitle msg="Vue.js and D3 Line Chart" />
        <svg width="800" height="800" id="mainsvg" class="svgs"></svg>
    </div>
</template>

<script setup>
import * as d3 from "d3";
import PageTitle from './components/PageTitle.vue';
</script>

<script>
export default {
    mounted(){
        // The following code is the typical routine of my d3.js code. 
        const svg = d3.select('#mainsvg');
        const width = svg.attr('width');
        const height = svg.attr('height');
        const margin = {top: 60, right: 30, bottom: 60, left: 150};
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;
        const mainGroup = svg.append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`)
        const xValue = d => d.globalsale;
        const yValue = d => d.platform;
        const xScale = d3.scaleLinear();
        const yScale = d3.scaleBand();

        /* 
            Loading mydata and preprocessing mydata. 
            Note that you can also preprocessing mydata in your own way using your prefered language, e.g., Python. 
        */

        d3.csv('platform_globalsale.csv').then(mydata => {
            console.log(mydata);
            // calculationg scales: 
            yScale.domain(mydata.map(yValue)).range([0, innerHeight]).padding(0.1);
            xScale.domain([0, d3.max(mydata, xValue)]).range([0, innerWidth]);   
            // mydata-join for rectangles: 
            mainGroup.selectAll('rect').data(mydata).join('rect')
            .attr('height', yScale.bandwidth()).attr('width', d => xScale(xValue(d)))
            .attr('x', 0).attr('y', d => yScale(yValue(d)));
            // adding axes: 
            const xAxisMethod = d3.axisBottom(xScale);
            const yAxisMethod = d3.axisLeft(yScale);
            const xAxisGroup = mainGroup.append('g').call(xAxisMethod);
            const yAxisGroup = mainGroup.append('g').call(yAxisMethod);
            xAxisGroup.attr('transform', `translate(${0}, ${innerHeight})`);
        });
    },
};

</script> 