
---
title: 'vue3.0使用ant-design-vue进行按需加载原来这么简单'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e6874532364f16a9324e2e66c9248a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 23:32:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e6874532364f16a9324e2e66c9248a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h4 data-id="heading-0">下载 ui库</h4>
<pre><code class="copyable">yarn add ant-design-vue
默认是全局引入，打包后体积很大，
非常影响首屏加载速度，
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">按需加载</h4>
<pre><code class="copyable">下载按需加载的插件;推荐使用cnpm
cnpm install babel-plugin-import --save-dev 下载在开发环境中
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">在项目的根目录下创建 babel.config.js</h4>
<pre><code class="copyable">module.exports = &#123;
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  plugins: [
    ["import", 
      &#123; 
        libraryName: "ant-design-vue",
        libraryDirectory: "es",
        style: true,   // `style: true` 会加载 less 文件
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">在项目跟目录下创建vue.config.js配置项目信息</h4>
<pre><code class="copyable">const Timestamp = new Date().getTime()
module.exports = &#123;
    chainWebpack: config => &#123;
        config.plugin('html').tap(args => &#123;
            args[0].title = '我的vue3.0' //这个是网站标题
            return args
        &#125;)
    &#125;,
    css: &#123;
        loaderOptions: &#123;
            // 你的基础样式 因为没有我就注释了
            // sass: &#123;
            //     data: `
            // @import "@/assets/style/base.scss";
            // `,
            // &#125;,

            //这只主题样式，修改此文件后需要重新启动，
            less: &#123;
                lessOptions: &#123;
                    modifyVars: &#123;
                      //这是配置css主题色
                      'primary-color': '#007AFF', 
                    &#125;,
                    javascriptEnabled: true,
                &#125;,
            &#125;,
        &#125;,
        // 每次打包后生成的css携带时间戳
        extract: &#123;
            filename: `css/[name].$&#123;Timestamp&#125;.css`,
            chunkFilename: `css/[name].$&#123;Timestamp&#125;.css`,
        &#125;,
    &#125;,
    productionSourceMap: false,
    //打包后相对目录
    publicPath: process.env.NODE_ENV === 'production' ? '././' : './',
    configureWebpack: &#123;
        //每次打包后生成的js携带时间戳
        output: &#123;
            filename: `[name].$&#123;Timestamp&#125;.js`,
            chunkFilename: `[name].$&#123;Timestamp&#125;.js`,
        &#125;,
    &#125;,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">安装less与less-loader</h4>
<pre><code class="copyable">我们需要确认自己是否安装了 less与less-loader
【自己看一下】
cnpm install less less-loader --save-dev  【进行安装】
可能你安装后会出现ess less-loader的版本过高。
这个时候你需要将你的版本下降一下

我们为什么需要安装less与less-loader
因为我们ant-design-vue是用less编写的
配置babel.config.js后，

下面是我的版本库

dependencies用户发布环境
"dependencies": &#123;
  "@ant-design/icons-vue": "^6.0.1",
  "ant-design-vue": "^2.2.1",
  "core-js": "^3.6.5",
  "vue": "^3.0.0",
  "vue-class-component": "^8.0.0-0",
  "vue-router": "^4.0.0-0"
&#125;,


devDependencies用于本地环境开发时候
"devDependencies": &#123;
    "@typescript-eslint/eslint-plugin": "^4.18.0",
    "@typescript-eslint/parser": "^4.18.0",
    "@vue/cli-plugin-babel": "~4.5.0",
    "@vue/cli-plugin-eslint": "~4.5.0",
    "@vue/cli-plugin-router": "~4.5.0",
    "@vue/cli-plugin-typescript": "~4.5.0",
    "@vue/cli-service": "~4.5.0",
    "@vue/compiler-sfc": "^3.0.0",
    "@vue/eslint-config-typescript": "^7.0.0",
    "babel-plugin-import": "^1.13.3",
    "eslint": "^6.7.2",
    "eslint-plugin-vue": "^7.0.0",
    "less": "^3.13.1",
    "less-loader": "^7.1.0",
    "node-sass": "^4.12.0",
    "sass-loader": "^8.0.2",
    "typescript": "~4.1.5"
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">devDependencies和dependencies区别?</h4>
<pre><code class="copyable">devDependencies是只会在开发环境下依赖的模块，
生产环境不会被打入包内。
通过NODE_ENV=developement或
NODE_ENV=production指定开发还是生产环境。

而dependencies依赖的包不仅开发环境能使用，
生产环境也能使用。
其实这句话是重点，
按照这个观念很容易决定安装模块时是使用--save还是--save-dev

所以像css预处理语言我们肯定是--save-dev
像ui库请求axios我们肯定是--save
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">main.ts 组件进行按需引入</h4>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
// 引入App.vue这个入口文件
import App from './App.vue'
// 引入路由
import router from './router'
const app = createApp(App)
import &#123;
    Button,
    ConfigProvider,
    Layout,
    Menu,
    message,
    Input,
    Space,
    Dropdown,
    Divider,
    Form,
    AutoComplete,
    Modal,
    Tree,
    Drawer,
    Row,
    Col,
    Select,
    DatePicker,
    Tooltip,
    Breadcrumb,
    Popconfirm,
    InputNumber,
    Table,
    Pagination,
&#125; from 'ant-design-vue'
app.use(Button)
    .use(Layout)
    .use(ConfigProvider)
    .use(Menu)
    .use(Input)
    .use(Space)
    .use(Dropdown)
    .use(Divider)
    .use(Form)
    .use(AutoComplete)
    .use(Modal)
    .use(Tree)
    .use(Drawer)
    .use(Row)
    .use(Col)
    .use(Select)
    .use(DatePicker)
    .use(Tooltip)
    .use(Breadcrumb)
    .use(Popconfirm)
    .use(InputNumber)
    .use(Table)
    .use(Pagination)
    .use(router).
    mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">按需加载说明和优势</h4>
<pre><code class="copyable">后只需从 ant-design-vue 引入模块即可，无需单独引入样式.
babel-plugin-import 会帮助你加载 JS 和 CSS
import &#123; Button &#125; from "ant-design-vue";
也就是说你不需要引入
import 'ant-design-vue/dist/antd.css'
这个样式文件了
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">Vue3.0出现Cannot read property ‘use‘ of undefined</h4>
<pre><code class="copyable">其实很简单 哈哈哈 就是因为版本的问题
执行  cnpm i --save ant-design-vue@next
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">Vue3.0出现Cannot find module 'vue-loader-v16/package.json</h4>
<pre><code class="copyable">当你第一次删除后node-module可能会报错:
Cannot find module 'vue-loader-v16/package.json'.
你在yarn.lock 可以看见这个文件的描述
先卸载vue-loader-v16依赖
npm uninstall vue-loader-v16

之后使用cnpm安装vue-loader-v16依赖
cnpm i vue-loader-v16
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">vue3.0 ant-design-vue Failed to resolve component: a-layout-header</h4>
<pre><code class="copyable">如果是这样的警告提示
这就说明了 你使用的a-layout-header没有进行加载
需要你在main.ts中添加该组件哈
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e6874532364f16a9324e2e66c9248a~tplv-k3u1fbpfcp-watermark.image" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            