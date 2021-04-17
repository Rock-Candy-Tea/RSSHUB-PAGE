
---
title: '使用vue写项目的准备工作【学生必看】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a48b45875f84c6f8b012f950bec13f7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 17:36:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a48b45875f84c6f8b012f950bec13f7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>Hello大家好，学习vue的小伙伴，在学习<code>vue-cli</code>脚手架之前，总会遇到一些困惑，我在真正使用vue开发项目的时候，我该怎么去做？走哪些流程？</p>
<p>我先说一下我的学习心得：学脚手架之前，那些Vue模板语法，常用特性，组件化开发，前后端交互从<code>Promise</code>异步处理到接口调用<code>fetch</code>，然后<code>axios</code>到<code>async/aweit</code>用法，随着知识点的循序渐进的灌输，就感觉很混乱。后来Vue前端路由<code>vue-router</code>的引入，<code>webpack</code>等等。以至于我刚开始接触用<code>vue-cli</code>脚手架所搭建的项目，进行一些相关配置就感觉很模糊。随着后来vue项目的练习，做了两个项目才慢慢熟练掌握。</p>
<p>那么，今天我分享一下使用vue写项目的准备工作！</p>
<h2 data-id="heading-1">正片</h2>
<h4 data-id="heading-2">搭建VUE项目的准备（利用vue-cli来构建项目）</h4>
<p>1.安装node.js,检测版本<code>node -v</code>,还要检测包管理工具<code>npm -v</code></p>
<p>这里需要说明下，因为在官网下载安装node.js后，就已经自带npm（包管理工具）了，另需要注意的是npm的版本最好是最新版本，以免对后续产生影响。</p>
<p><img alt="JLYLUOSPK03MUTHL1YW3%13.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a48b45875f84c6f8b012f950bec13f7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2.脚手架环境的安装</p>
<ul>
<li>
<p>在全局环境中安装 vue-cli 脚手架</p>
<pre><code class="copyable"> npm install -g @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>3.工程的创建</p>
<ul>
<li>
<p>使用命令行执行</p>
<pre><code class="copyable"> vue create vision
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img alt="2.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e67499bda9214cf990e4227d23811683~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>具体的配置项如下:</li>
</ul>
<ol>
<li>手动选择特性(集成Router , Vuex , CSS Pre-processors)</li>
</ol>
<p><img alt="3.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f8fb9c4696e4eedad8eafb119c0ab42~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
2. vue版本选择
<img alt="4.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e47e91c3b5943c699630b6b79fb6ac0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
3. 是否选用历史模式的路由</p>
<p><img alt="5.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a73b4ceddca146a0a38be9141de14050~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
4. 选择 Less 作为 CSS 的预处理器</p>
<p><img alt="6.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a69f5f8357d414b98273f7f8f4d9d67~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
5. 选择 ESLint 的配置</p>
<p><img alt="7.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48a03bdb6805489998173f2f5c83acae~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
6. 什么时候进行 Lint 提示</p>
<p><img alt="8.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3851488a051d4a8ea5becaba4876b504~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
7. 如何存放 Babel , ESLint 等配置文件</p>
<p><img alt="9.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c0401c151184c89992dbc07410c03b2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
8. 是否保存以上配置以便下次创建项目时使用</p>
<p><img alt="10.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fee8d5d420fb4330ab119988b915efe5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>配置选择完之后, 就开始创建项目了, 这个过程需要一些时间:</li>
</ul>
<p><img alt="12.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/702b845fca5f42c0877da4a48afeb595~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>当项目就创建完成了, 会看到这个提示</li>
</ul>
<p><img alt="13.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd901b2dcfc44c4cb3eeeec6fbb5f7bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>运行默认的项目</p>
<p>ad vision
npm run serve</p>
</li>
<li>
<p>将目录使用 vscode 打开</p>
</li>
</ul>
<ol start="4">
<li>删除无关代码</li>
</ol>
<ul>
<li>
<p>修改 App.vue 中的代码,将布局和样式删除, 变成如下代码:</p>
<pre><code class="copyable"> <template>
     <div id="app">
         <router-view/>
     </div>
 </template> 
 <style lang="less"> 
 </style>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>删除 components/HelloWorld.vue 这个文件</p>
</li>
<li>
<p>删除 views/About.vue 和 views/Home.vue 这两个文件</p>
</li>
<li>
<p>修改 router/index.js 中的代码,去除路由配置和 Home 组件导入的代码</p>
<pre><code class="copyable">import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter) 
const routes = []
const router = new VueRouter(&#123; 
    routes
&#125;)
export default router
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-3">项目的基本配置</h4>
<ul>
<li>
<p>在项目根目录下创建 vue.config.js 文件</p>
</li>
<li>
<p>在文件中增加代码:</p>
<pre><code class="copyable"> // 使用vue-cli创建出来的vue工程, Webpack的配置是被隐藏起来了的 
 // 如果想覆盖Webpack中的默认配置,需要在项目的根路径下增加vue.config.js文件 
 module.exports = &#123; 
     devServer: &#123; 
         port: 8888, // 端口号的配置 
         open: true // 自动打开浏览器 
     &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-4">axios 的处理</h4>
<p>1.安装 axios 包</p>
<pre><code class="copyable">npm install axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.封装 axios 对象</p>
<ul>
<li>
<p>在 src/main.js 文件中配置 axios 并且挂载到Vue的原型对象上</p>
<pre><code class="copyable"> ...... 
 import axios from 'axios' 
 // 请求基准路径的配置
 axios.defaults.baseURL = 'http://127.0.0.1:8888/×××' 
 // 将axios挂载到Vue的原型对象上 
 Vue.prototype.$http = axios 
 ......
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>3.使用 axios 对象
在其他组件中使用： <code>this.$http</code></p>
<h4 data-id="heading-5">router 配置</h4>
<p>简单介绍一下routers中的结构，这里主要用来配置路由的，上面说过所有子路由都在App.vue下，所有App.vue是最外层的父路由，这里的routes中存的就是路由的数组，path就是你要访问你所创建的页面的路径，这里写的是根路径序所以你直接访问localhost:8080就会出现一个App.vue中插入一个ScreenPage.vue的页面（这个相当于路由嵌套），name想到与给它命名这个比较无关紧要，component相当于你要引用的页面，这里引用的是ScreenPage.vue这个页面，主要上面的import，这里的ScreenPage是一个变量，对应上面的路径文件。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d105dab1a4ee48b1abf851d7d19b738c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c985465026c64a118518dfd8d58cf650~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>1.<code>router-link</code>组件是用来跳转路由的，to属性是将要跳转的路由页地址。</p>
<p>2.<code>router-view</code>组件是用来展示组件页的。</p>
<p>3.<code>$route.query</code>来获取URL 查询参数，例如你有一个路由地址：/page?id=1，则有 let id= $route.query.id || -1，如果没有查询参数，则默认给了个-1的数值。</p>
<p>接下来就可以正式根据项目需求来写项目了！</p>
<p><strong>今天就到这里啦，vue东西还是比较多的，项目的准备工作大概就这么多吧！get到的小伙伴点赞支持支持，有哪些不足和欠缺的地方，欢迎评论区纠正！</strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            