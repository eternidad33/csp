# 本站搭建过程

### 1.安装

推荐全局安装 docsify-cli 工具，可以方便地创建及在本地预览生成的文档。

```bash
npm i docsify-cli -g
```

### 2.初始化项目

如果想在项目的 ./docs 目录里写文档，直接通过 init 初始化项目。

```bash
docsify init ./docs
```

### 3.写文档

初始化成功后，可以看到 ./docs 目录下创建的几个文件

- `index.html` 入口文件
- `README.md` 会做为主页内容渲染
- `.nojekyll` 用于阻止 GitHub Pages 忽略掉下划线开头的文件


直接编辑 `docs/README.md` 就能更新文档内容，当然也可以添加更多页面。

### 4.本地预览

通过运行`docsify serve`启动一个本地服务器，可以方便地实时预览效果。默认访问地址 http://localhost:3000 。

```bash
docsify serve docs
```

更多命令行工具用法，参考 [docsify-cli](https://github.com/docsifyjs/docsify-cli) 文档。