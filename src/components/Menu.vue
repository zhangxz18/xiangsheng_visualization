<template>
    <el-row class="tac">
      <el-col :span="24">
        <h5 class="mb-2">Custom colors</h5>
        <el-menu
          active-text-color="#ffd04b"
          background-color="#545c64"
          class="el-menu-vertical-demo"
          default-active="Word"
          text-color="#fff"
          @open="handleOpen"
          @close="handleClose"
        >
          <el-menu-item index="Word">
            <template #title>
              <el-icon><location /></el-icon>
              <span>Navigator One</span>
            </template>
          </el-menu-item>
          <el-menu-item index="Sentence">
            <el-icon><icon-menu /></el-icon>
            <span>Navigator Two</span>
          </el-menu-item>
          <el-menu-item index="Paragraph">
            <el-icon><document /></el-icon>
            <span>Navigator Three</span>
          </el-menu-item>
          <el-menu-item index="D3test">
            <el-icon><setting /></el-icon>
            <span>Navigator Four</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </template>
  
  <script setup>
  import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
  } from '@element-plus/icons-vue'
  const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
    // this.activeIndex = key
  }
  const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
  }
  </script>