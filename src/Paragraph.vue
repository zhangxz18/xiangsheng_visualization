<template>
    <div class="main_page">
        <PageTitle msg="不同时期相声主题分布" />
        <el-card class="box-card">
            <div>
                <svg width="800" height="600" id="mainsvg" class="svgs"></svg>
            </div>
        </el-card>
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
        const svg = d3.select('#mainsvg');
        const width = svg.attr('width');
        const height = svg.attr('height');
        const margin = {top: 60, right: 30, bottom: 60, left: 150};
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;
        const g = svg.append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`)
        // const color = d3.scaleOrdinal(d3.schemeSet1.concat(d3.schemeSet2).concat(d3.schemeSet3));
        const naiveKeys = [
            "经济", "教育", "科学", "社会", "政治", "体育", "娱乐", "历史"
        ]
        // const stackData = [];
        // const stack = d3.stack().keys(KEYS);
        const naiveData = [{time: '1949前', '经济': 22, '娱乐': 354, '社会': 79, '教育': 27, '历史': 56, '政治': 5, '科学': 1, '体育': 0}, {time: '1949-1978', '体育': 1, '教育': 1, '娱乐': 24, '社会': 7, '历史': 2, '政治': 1, '经济': 0, '科学': 0}, {time: '1978-2024', '娱乐': 21, '社会': 6, '历史': 1, '政治': 3, '科学': 1, '经济': 0, '教育': 0, '体育': 0}]

        // d3.csv('theme_and_time.csv').then(data =>{
        //     data.forEach(d => {
        //         d.theme = d.theme;
        //         d.time = d.time;
        //     });
        // })
        var naiveStack = d3.stack()
        .keys(naiveKeys)
        .order(d3.stackOrderNone)(naiveData);

        const xValue = d => d.time;

        const yScale = d3.scaleLinear()
        .domain([0, d3.max(naiveStack, d => d3.max(d, subd => subd[1]))])
        .range([innerHeight, 0]).nice();

        const xScale = d3.scaleBand()
        .domain(naiveData.map(d => xValue(d)))
        .range([0, innerWidth])
        .padding(0.5);

        const color = d3.scaleOrdinal()
        .domain(naiveKeys)
        .range(d3.schemeSet3)

        // start to do data-join; 
        g.selectAll('.datagroup').data(naiveStack).join('g')
        .attr('class', 'datagroup')
        .attr('fill', d => color(d.key))
        .selectAll('.datarect').data(d => d).join('rect')
        .attr('class', 'datarect')
        .attr('y', d => yScale(d[1]))
        .attr('x', d => xScale(xValue(d.data)))
        .attr('height', d => yScale(d[0]) - yScale(d[1]))
        .attr('width', xScale.bandwidth());
        // Add legend
        const legend = g.append('g')
            .attr('class', 'legend')
            .attr('transform', `translate(${innerWidth-60}, 0)`);

        const legendRects = legend.selectAll('.legend-rect')
            .data(naiveKeys)
            .enter()
            .append('rect')
            .attr('class', 'legend-rect')
            .attr('y', (d, i) => i * 30)
            .attr('width', 20)
            .attr('height', 20)
            .attr('fill', d => color(d));

        const legendTexts = legend.selectAll('.legend-text')
            .data(naiveKeys)
            .enter()
            .append('text')
            .attr('class', 'legend-text')
            .attr('x', 40)
            .attr('y', (d, i) => i * 30 + 15)
            .text(d => d);

        // drawing axes;
        let yAxis = d3.axisLeft(yScale);
        let xAxis = d3.axisBottom(xScale);
        g.append('g').attr('id', 'yaxis').call(yAxis);
        g.append('g').attr('id', 'xaxis').call(xAxis).attr('transform', `translate(0, ${innerHeight})`);
        d3.selectAll('.tick text').attr('font-size', '2em');
        d3.selectAll('#xaxis text').attr('y', '10')
    },
};

</script> 