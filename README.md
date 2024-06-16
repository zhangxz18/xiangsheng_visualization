# xiangsheng_vis

An xiangsheng visualization network developed with Vue 3 and element plus.

## Project Setup
Download node.js from https://nodejs.org/en.


```sh
git clone https://github.com/zhangxz18/xiangsheng_visualization.git
cd xiangsheng_visualization
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

## todo
- [ ] 子标签起名字
- [ ] logo改成透明背景
### 词
+ 对每篇相声做分词
+ 加一个多选框，可以选择需要的相声（默认全选）
+ 根据选择的相声，显示词云/词频统计
### 句
+ 加一个单选框，可以选择需要的相声
+ 根据选择的相声，允许每一句交互式地加emoji
### 主题
+ 找个model对相声主题做分类
+ 根据分类结果，画主题河流
### 如果觉得工作量不够
+ 相声长度的分布
+ 逗哏捧哏的时长分布对比

node:
    注意在vscode配置python的虚拟环境，然后安装所需要的包，配置完虚拟环境，激活虚拟环境，然后pip install -r requirements.txt
    注意要修改yuntu.py中base_path
    注意把所有的相声txt文件放在D盘下的xiangsheng文件夹下，不然你自己在代码中找地方改路径
    生成的图和数据都在项目里的public文件夹里面
    