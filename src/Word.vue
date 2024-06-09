<template>
    <div class="main_page">
        <PageTitle msg="Word" />
        <el-row :gutter="20" style="margin-left: 0">
            <el-col :span="12">
                <el-card class="box-card">
                    <div slot="header" class="clearfix">
                        <span>词云</span>
                    </div>
                    <div>
                        <img src="/logo.jpg" width="100%">
                    </div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card class="box-card">
                    <div slot="header" class="clearfix">
                        <span>词频统计</span>
                    </div>
                    <div>
                        <img src="/logo.jpg" width="100%">
                    </div>
                </el-card>
            </el-col>
        </el-row>


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

<style scoped>
  .box-card {
    display: flex;
    width: 480px;
  }
  .text {
    font-size: 14px;
  }
</style>