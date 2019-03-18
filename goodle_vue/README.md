# Goodle Vue
软件实训课程作业，goodle搜索引擎前端工程

| date | version | operator | remark |
| - | - | - | - |
| 20190318 | V0.1 | Jeanrry | 1 新增目录 |
| | | | 2 新增章节《如何运行项目》 |
| | | | 3 新增章节《项目目录介绍》 |
| | | | 4 新增章节《项目方法顺序》 |
| | | | 5 新增章节《vue项目打包》 |

## 目录
+ 如何运行项目
+ 项目目录介绍
+ 项目方法顺序
+ vue项目打包

## 如何运行项目
| date | version | operator | remark |
| - | - | - | - |
| 20190318 | V0.1 | Jeanrry | 创建 |

### 首次运行说明
vue 项目基于 node.js 所以需要先安装 node.js 等相关工具

#### npm工具
node.js官网上下载msi安装包点击安装

#### 查看版本
``` bash
$ npm -v
6.4.1
```
#### 全局升级npm
``` bash
$ npm install npm -g
```

执行完以上之后，应该还会有一些需要安装的插件啥的，控制台说装啥就装啥，不再赘述

### 命令行方法
推荐值 3☆
``` bash
# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

### JetBrain 全家桶
推荐值 5☆
界面右上角选择 dev 为开发环境运行，build为打包

### 扩展介绍
重磅推荐命令行工具 cmder，用了都说好

## 项目目录介绍
| date | version | operator | remark |
| - | - | - | - |
| 20190318 | V0.1 | Jeanrry | 创建 |
```
├── build/                      # 项目构建(webpack)相关代码
│   └── ...
├── config/                     # 配置目录，包括端口号、跨域代理等。
│   ├── index.js                # 主要项目配置
│   └── ...
├── node_modules                # node 依赖文件夹，不用管
│   └── ...
├── src/
│   ├── assets/                 # 模块资源（由webpack处理）
│   │   ├── icon/               # 原项目图标文件夹，系统首页侧边栏使用
│   │   └── ...                 # 其他的一些图标啥的，用处不详
│   ├── components/             # ui组件
│   ├── router/                 # vue 路由
│   │   └── index.js            # 路由文件
│   ├── App.vue                 # 主应用程序组件
│   ├── main.js                 # 应用入口文件
├── static/                     # 纯静态资源（直接复制）
├── .babelrc                    # babel 配置
├── .postcssrc.js               # postcss 配置
├── .eslintrc.js                # eslint 配置
├── .editorconfig               # editor 配置
├── index.html                  # index.html模板
└── package.json                # 构建脚本和依赖关系
```

## 项目方法顺序
| date | version | operator | remark |
| - | - | - | - |
| 20190318 | V0.1 | Jeanrry | 创建 |
[vue风格指南官网][vue风格指南官网]

### 组件/实例顺序
就是每个vue文件内部的 `<script>` 中的部分
##### 1.副作用
+ `el`

##### 2.全局感知
+ `name`
+ `parent`

##### 3.组件类型
+ `functional`

##### 4.模板修改器
+ `delimiters`
+ `comments`

##### 5.模板依赖
+ `components`
+ `directives`
+ `filters`

##### 6.组合
+ `extends`
+ `mixins`

##### 7.接口
+ `inheritAttrs`
+ `model`
+ `props` / `propsData`

##### 8.本地状态
+ `data`
+ `computed`

##### 9.事件
+ `watch`
+ 生命周期钩子
  + `beforeCreate`
  + `created`
  + `beforeMount`
  + `mounted`
  + `beforeUpdate`
  + `updated`
  + `activated`
  + `deactivated`
  + `beforeDestroy`
  + `destroyed`

##### 10.非响应式的属性
+ `methods`

##### 11.渲染
+ `template` / `render`
+ `renderError`

### 元素特性的顺序
##### 1.定义
+ `is`

##### 2.列表渲染
+ `v-for`

##### 3.条件渲染
+ `v-if`
+ `v-else-if`
+ `v-else`
+ `v-show`
+ `v-cloak`

##### 4.渲染方式
+ `v-pre`
+ `v-once`

##### 5.全局感知
+ `id`

##### 6.唯一的特性
+ `ref`
+ `key`
+ `slot`

##### 7.双向绑定
+ `v-model`

##### 8.其他特性
所有的普通的绑定或未绑定的特性

##### 9.事件
+ `v-on`

##### 10.内容
+ `v-html`
+ `v-text`

## vue项目打包
| date | version | operator | remark |
| - | - | - | - |
| 20190318 | V0.1 | Jeanrry | 创建 |

### 相关配置项介绍

![avatar][vue打包-配置文件修改]

如图文件位置

+ `index` 段描述的是生成包的 `index` 模板路径
+ `assetsRoot` 段指的是生成文件夹路径
+ `assetsSubDirectory` 段指的是打包之后的 `static` 文件夹路径
+ `assetsPublicPath` 公共资源路径
+ `productionSourceMap` 是否是生产环境

照图片改就可以

需要注意的是上文的 `index`，`assetsRoot`，`assetsSubDirectory`，`assetsPublicPath` 这四个段修改需要相互配合

### 打包命令
``` bash
npm run build
```

如上配置，生成文件夹路径如下：

![avatar][生成文件夹路径]




[^_^]: # (下面是变量区，不要乱动)
[Vue Devtools @ github]: https://github.com/vuejs/vue-devtools#vue-devtools
[vue风格指南官网]: https://cn.vuejs.org/v2/style-guide/
[vue打包-配置文件修改]: https://jeanrry-test-1251663958.cos.ap-beijing.myqcloud.com/vue%E5%9B%BE%E5%BA%8A/vue%E6%89%93%E5%8C%85-build%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.png
[生成文件夹路径]: https://jeanrry-test-1251663958.cos.ap-beijing.myqcloud.com/vue%E5%9B%BE%E5%BA%8A/%E7%94%9F%E6%88%90%E5%8C%85%E8%B7%AF%E5%BE%84.png
