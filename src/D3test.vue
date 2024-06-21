<template>
    <div class="main_page">
        <PageTitle msg="Vue.js and D3 Line Chart" />
        <el-card class="box-card">
            <div>
                <svg width="1100" height="1300" id="mainsvg" class="svgs"></svg>
            </div>
        </el-card>
        
    </div>
</template>

<script setup>
import * as d3 from "d3";
import { sankey as d3Sankey, sankeyLinkHorizontal } from 'd3-sankey';
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
        var json = {
          'nodes': [
            {'name': '传统节目'},
            {'name': '新编节目'},
            {'name': '当代节目'},
            {'name': '经济'},
            {'name': '教育'},
            {'name': '科学'},
            {'name': '社会'},
            {'name': '政治'},
            {'name': '体育'},
            {'name': '娱乐'},
            {'name': '历史'}
          ],
          'links': [
            {'source': 0, 'target': 3, 'value': 22},
            {'source': 0, 'target': 4, 'value': 27},
            {'source': 0, 'target': 5, 'value': 1},
            {'source': 0, 'target': 6, 'value': 79},
            {'source': 0, 'target': 7, 'value': 5},
            {'source': 0, 'target': 9, 'value': 354},
            {'source': 0, 'target': 10, 'value': 56},
            {'source': 1, 'target': 4, 'value': 1},
            {'source': 1, 'target': 6, 'value': 7},
            {'source': 1, 'target': 7, 'value': 1},
            {'source': 1, 'target': 8, 'value': 1},
            {'source': 1, 'target': 9, 'value': 24},
            {'source': 1, 'target': 10, 'value': 2},
            {'source': 2, 'target': 5, 'value': 1},
            {'source': 2, 'target': 6, 'value': 6},
            {'source': 2, 'target': 7, 'value': 3},
            {'source': 2, 'target': 9, 'value': 21},
            {'source': 2, 'target': 10, 'value': 1}
          ]
        };
        
        // const width = 700, height = 400;
        let color = d3.scale
        // Create a new Sankey generator
        const sankey = d3Sankey()
        .nodeWidth(80)
        .nodePadding(5)
        .size([innerWidth, innerHeight]);

        // Apply the data
        const graph = sankey({
        nodes: json.nodes.map(d => Object.assign({}, d)),
        links: json.links.map(d => Object.assign({}, d))
        });

        svg.append("g")
            .selectAll("rect")
            .data(graph.nodes)
            .enter().append("rect")
            .attr("x", d => d.x0)
            .attr("y", d => d.y0)
            .attr("height", d => d.y1 - d.y0)
            .attr("width", d => d.x1 - d.x0)
            .style("fill", d => getColor(d.name)) // Change the fill color based on node name
            .style("stroke", "black")
            .style("stroke-width", 1)
            .append("title")
            .text(d => `${d.name}\n${d.value}`);

        function getColor(name) {
            // Define your color mapping logic here
            // For example, you can use a switch statement to assign different colors based on node name
            switch (name) {
            case '传统节目':
                return '#de7d72';
            case '新编节目':
                return '#7b8dd4';
            case '当代节目':
                return '#7b7579';
            // Add more cases for other node names
            case '经济':
                return '#f9d057';
            case '教育':
                return '#f29e2e';
            case '科学':
                return '#e76818';
            case '社会':
                return '#d7191c';
            case '政治':
                return '#b83b5e';
            case '体育':
                return '#6a4c93';
            case '娱乐':
                return '#3e4a89';
            case '历史':
                return '#2a5674';
            default:
                return 'gray';
            }
        }
        // svg.append("g")
        //   .selectAll("rect")
        //   .data(graph.nodes)
        //   .enter().append("rect")
        //   .attr("x", d => d.x0)
        //   .attr("y", d => d.y0)
        //   .attr("height", d => d.y1 - d.y0)
        //   .attr("width", d => d.x1 - d.x0)
        //   .style("fill", "blue")
        //   .style("stroke", "black")
        //   .style("stroke-width", 1)
        //   .append("title")
        //   .text(d => `${d.name}\n${d.value}`);
        // Draw the links
        // svg.append("g")
        //   .selectAll("path")
        //   .data(graph.links)
        //   .enter().append("path")
        //   .attr("d", sankeyLinkHorizontal())
        //   .style("stroke-width", d => Math.max(1, d.width));
        // add style to draw colorful link

        svg.append("g")
          .selectAll("path")
          .data(graph.links)
          .enter().append("path")
          .attr("d", sankeyLinkHorizontal())
          .style("stroke", d => getColor(d.target.name))
        //   .style("fill", d => getColor(d.target.name))
          .style("fill", "none")
          .style("stroke-width", d => Math.max(1, d.width));
        
        // draw the nodes

        // Add node names
        svg.append("g")
            .selectAll("text")
            .data(graph.nodes)
            .enter().append("text")
            .attr("x", d => (d.x0 + d.x1) / 2)
            .attr("y", d => (d.y0 + d.y1) / 2)
            .attr("dy", "0.35em")
            .attr("text-anchor", "middle")
            .text(d => {
                const nodeHeight = d.y1 - d.y0;
                const nodeName = d.name;
                const fontSize = 12;
                const maxTextWidth = d.x1 - d.x0;
                const maxTextHeight = nodeHeight - fontSize;
                const words = nodeName.split(' ');
                let line = '';
                let lines = [];
                words.forEach(word => {
                    const testLine = line + word + ' ';
                    const testWidth = svg.select('text').text(testLine).node().getComputedTextLength();
                    if (testWidth > maxTextWidth && line !== '') {
                        lines.push(line);
                        line = word + ' ';
                    } else {
                        line = testLine;
                    }
                });
                lines.push(line);
                if (lines.length * fontSize > maxTextHeight) {
                    return '';
                } else {
                    return lines.join('\n');
                }
            })
            .style("font-size", "12px")
            .style("fill", "black");
        // svg.append("g")
        //     .selectAll("text")
        //     .data(graph.nodes)
        //     .enter().append("text")
        //     .attr("x", d => (d.x0 + d.x1) / 2)
        //     .attr("y", d => (d.y0 + d.y1) / 2)
        //     .attr("dy", "0.35em")
        //     .attr("text-anchor", "middle")
        //     .text(d => d.name)
        //     .style("font-size", "12px")
        //     .style("fill", "white");

    },
};

</script> 