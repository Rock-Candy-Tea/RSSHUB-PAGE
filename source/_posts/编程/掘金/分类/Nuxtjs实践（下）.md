
---
title: 'Nuxt.js实践（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e11883fc0b5e4ef3a84acc99f70ee8fe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 18:40:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e11883fc0b5e4ef3a84acc99f70ee8fe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>前两篇我们依次从Web的发展了解到了SSR的特点，同时也知道了SSR真正实现的原理以及整个过程，并且我们以Vue为例，完成了基于Vue的同构开发应用，今天就是SSR的最后一部分，我们将进行Nuxt.js框架的实践</p>
<p>PS：Vue-SSR将会分为三部分完成：理解SSR以及实践于Vue（上）、Vue中同构开发SSR应用（中）、Nuxt.js实践（下）</p>
<h2 data-id="heading-1">Nuxt.js是什么</h2>
<p>Nuxt.js 是⼀个基于 Vue.js 的<strong>通⽤应⽤</strong>框架。
通过对客户端/服务端基础架构的抽象组织，Nuxt.js主要关注的是应⽤的UI渲染。</p>
<p>结论：</p>
<ul>
<li>nuxt不仅仅⽤于服务端渲染也可⽤于spa应⽤开发；</li>
<li>利⽤nuxt提供的基础项⽬结构、路由⽣成、中间件、插件等特性可⼤幅提⾼开发效率</li>
<li>nuxt可⽤于⽹站静态化</li>
</ul>
<p>PS：<a href="https://www.nuxtjs.cn/guide%EF%BC%88%E5%AE%98%E6%96%B9%E6%96%87%E6%A1%A3%E4%B8%AD%E6%96%87%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">www.nuxtjs.cn/guide（官方文档中…</a></p>
<h2 data-id="heading-2">Nuxt.js的特性</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e11883fc0b5e4ef3a84acc99f70ee8fe~tplv-k3u1fbpfcp-watermark.image" alt="nuxt.js特性.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Nuxt.js的渲染流程</h2>
<p>Nuxt.js 应用一个完整的服务器请求到渲染（或用户通过  切换路由渲染页面）的流程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b62bf38f620a42c3bb71761c65469b99~tplv-k3u1fbpfcp-watermark.image" alt="nuxt渲染流程图.png" loading="lazy" referrerpolicy="no-referrer">
接下来我们就针对Nuxt.js的特性模块分别进行实践</p>
<h3 data-id="heading-4">1、nuxt的安装</h3>
<p>安装我们使用官方提供cli</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npx create-nuxt-app <项⽬名>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是安装之中的选择配置项，可以按照自己项目的需要来进行适当的选择：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d8361cee5e4c15b750f600ed147377~tplv-k3u1fbpfcp-watermark.image" alt="安装nuxt.png" loading="lazy" referrerpolicy="no-referrer">
运行项目：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就能在浏览器中看到这样的效果，说明我们就已经安装成功了：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5576be4fcfcf49b7be9b5e0dea5cf1e0~tplv-k3u1fbpfcp-watermark.image" alt="启动服务.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">2、项目结构</h3>
<p>我们先来看下官方生成的项目结构，简单看下各个文件夹的作用：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9218734308ba46bf985dcee929ea3c0d~tplv-k3u1fbpfcp-watermark.image" alt="目录结构.png" loading="lazy" referrerpolicy="no-referrer">
目录结构：</p>
<ul>
<li><strong>assets</strong>：<strong>资源⽬录</strong> assets ⽤于组织未编译的静态资源如 LESS 、 SASS 或 JavaScript</li>
<li><strong>components</strong>：<strong>组件⽬录</strong> components ⽤于组织应⽤的 Vue.js 组件。Nuxt.js 不会扩展增强该⽬录下 Vue.js 组件，即这些组件不会像⻚⾯组件那样有 asyncData ⽅法的特性。</li>
<li><strong>layouts</strong>：<strong>布局⽬录</strong> layouts ⽤于组织应⽤的布局组件。</li>
<li><strong>middleware</strong>：<strong>中间件</strong>⽬录⽤于存放应⽤的中间件</li>
<li><strong>pages</strong>：<strong>⻚⾯⽬录</strong> pages ⽤于组织应⽤的路由及视图。Nuxt.js 框架读取该⽬录下所有的 .vue⽂件并⾃动⽣成对应的路由配置。（PS：新建文件后路由是自动生成的，后面具体看例子）</li>
<li><strong>plugins</strong>：<strong>插件⽬录</strong> plugins ⽤于组织那些需要在 根vue.js应⽤ 实例化之前需要运⾏的Javascript 插件。</li>
<li><strong>static</strong>：<strong>静态⽂件⽬录</strong> static ⽤于存放应⽤的静态⽂件，此类⽂件不会被 Nuxt.js 调⽤ Webpack进⾏构建编译处理。 服务器启动的时候，该⽬录下的⽂件会映射⾄应⽤的根路径 / 下。</li>
<li><strong>store</strong>：⽤于组织应⽤的 <strong>Vuex</strong> 状态树⽂件。 Nuxt.js 框架集成了 Vuex 状态树 的相关功能配置，在 store ⽬录下创建⼀个 index.js ⽂件可激活这些配置。</li>
<li><strong>nuxt.config.js</strong>：该⽂件⽤于<strong>个性化配置</strong>Nuxt应⽤。</li>
</ul>
<p>好啦，项目结构大概就说这么多了，接下来主要针对Nuxt.js的特点特性来进行一些简单的实践～</p>
<h2 data-id="heading-6">路由</h2>
<p><strong>1、自动路由配置</strong></p>
<ul>
<li><strong>基础路由</strong></li>
</ul>
<p>我们先来看一个非常方便的特性，这是常规vue项目结构没有的，我们都知道我们平时使用vue-cli开发我们在pages里面新建完文件之后还要自己去配置路由，项目大了多少有点麻烦，但是我们的Nuxt.js就推出了<strong>自动路由配置</strong></p>
<p>简单点说，就是只要我们在pages里面新建文件之后，路由结构就能自动配置好，没错，你没听错，就是自动配置好！（是不是感觉体验感贼好）那我们就来试试</p>
<p>我们在pages里面新建两个.vue文件：</p>
<ul>
<li>pages/admin.vue 商品管理⻚</li>
<li>pages/login.vue 登录⻚</li>
</ul>
<p>然后我们什么都不做，直接在浏览器当中输入URL：<a href="http://localhost:3000/admin" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/admin</a>
我们看图：神奇吧，什么都没配置，路由就自动已经配置好了，是不是感觉很香！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7963569c2b64af383fd3a7a452edbdc~tplv-k3u1fbpfcp-watermark.image" alt="自动生成路由admin.png" loading="lazy" referrerpolicy="no-referrer">
那这个路由是在哪里自己配置的呢？哎，我们来到文件结构当中，所有的路由都是在这里进行了自动配置：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e87622e2e8f48e0922d3049bc3cc99e~tplv-k3u1fbpfcp-watermark.image" alt="自动配置路由文件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>动态路由</strong></li>
</ul>
<p>那我们可能会想，简单的路由是可以自动生成，那假如说我们是动态路由呢？路由后面携带参数怎么做呢？</p>
<p>很显然，Nuxt是考虑到的，在我们需要使用动态路由的时候，Nuxt规定：在 Nuxt.js 里面定义带参数的动态路由，需要创建对应的以下划线（_）作为前缀的 Vue 文件 或 目录</p>
<p>举个例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67bc207040d845b7a93fae34fd18e305~tplv-k3u1fbpfcp-watermark.image" alt="动态路由.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b894cb1ad7ca431883972fce41f10aeb~tplv-k3u1fbpfcp-watermark.image" alt="动态路由添加结果.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6570e80f47ea4431908f3cbbe4d55ea1~tplv-k3u1fbpfcp-watermark.image" alt="动态路由结果.png" loading="lazy" referrerpolicy="no-referrer">
我们来看这三张图，我们按照规则添加了文件夹，结果在路由表当中也是自动添加了我们想要的动态路由，是不是同样很方便呢？</p>
<ul>
<li><strong>嵌套路由</strong></li>
</ul>
<p>那我们又会说，如果我们项目中是嵌套路由呢？那又该怎么做呢？</p>
<p>同样Nuxt.js也有考虑到，规则是：创建内嵌子路由，你需要添加一个 Vue 文件，同时添加一个与该文件同名的目录用来存放子视图组件</p>
<p>我们同样也来举一个🌰：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87f8de9d7fd241ffa381f24ab10de713~tplv-k3u1fbpfcp-watermark.image" alt="嵌套路由.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20f3d6b201ec43a18b9e8ed1babdf75b~tplv-k3u1fbpfcp-watermark.image" alt="嵌套路由表.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/592e763caa6c4f2a8c4e3a6b48adc278~tplv-k3u1fbpfcp-watermark.image" alt="嵌套路由结果显示.png" loading="lazy" referrerpolicy="no-referrer">
我们看这个，同样也会比较方便的自动生成嵌套路由的问题，不得不说，这种开发体验感真的是挺好的，而且按照一定的规则来命名文件名称也有利于我们来管理文件结构</p>
<p><strong>2、导航</strong>
我们来添加路由导航，我们在layouts/default.vue文件里面添加代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">nav</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">nuxt-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">nuxt-link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">nuxt-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/admin"</span>></span>管理<span class="hljs-tag"></<span class="hljs-name">nuxt-link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">nuxt-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/cart"</span>></span>购物车<span class="hljs-tag"></<span class="hljs-name">nuxt-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Nuxt</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是感觉很眼熟？没错就是和传统vue开发的router-link差不多，但是这里我们由于是使用SSR的模式，所以我们还是选择nuxt-link做导航</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f61f9dfb21ef4e1cbb97613f1677d599~tplv-k3u1fbpfcp-watermark.image" alt="导航.png" loading="lazy" referrerpolicy="no-referrer">
PS：layout里面的default.vue就是默认的全局使用的布局组件，我们看上图就可以看到其实就是对全局的一个包裹容器</p>
<p><strong>3、自定义路由</strong>
我们学习了在Nuxt中怎么实现动态路由，那我们想一想那我们怎么来实现自定义路由呢？换句话说就是假如我现在有个页面我想用我自定义的路由名称怎么做呢？（这还用想嘛，改文件名字，ennnn,没错的确可以，但是我们需要用较为高端的方式）</p>
<p>我们找到nuxt.config.js，我们在里面加入代码：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6116482b2593427d9eb33899a5952555~tplv-k3u1fbpfcp-watermark.image" alt="自定义路由配置.png" loading="lazy" referrerpolicy="no-referrer">
然后这时候我们就可以使用我们自定义的路由配置了（虽然好像并没有什么太大的用）</p>
<h2 data-id="heading-7">视图</h2>
<p>我们来看下Nuxt中关于布局部分的内容，我们先来看一张图，这张图展示了Nuxt.js 如何为指定的路由配置数据和视图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceaf5b8eac6f4b4f92e210e786770e56~tplv-k3u1fbpfcp-watermark.image" alt="视图.png" loading="lazy" referrerpolicy="no-referrer">
<strong>1、默认布局</strong>
默认布局其实上面我们已经提到过了，就是刚开始创建项目的时候layouts/default.vue</p>
<p><strong>2、自定义布局</strong>
同样我们也能自定义布局，比如我们现在想创建空⽩布局⻚⾯ layouts/blank.vue ，⽤于login.vue</p>
<p>那首先我们先在layouts里面新建一个blank.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>hello, welcome to login<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Nuxt</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在pages/login.vue里面使用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    登录页面
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">layout</span>: <span class="hljs-string">'blank'</span>
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa9b93370fb4becbad9abd887c4321d~tplv-k3u1fbpfcp-watermark.image" alt="自定义布局.png" loading="lazy" referrerpolicy="no-referrer">
<strong>3、自定义错误页面</strong>
我们日常开发的过程中经常有着自定义错误页面的需求，那在Nuxt里面这个就很方便来做，新建layouts/error.vue：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"error.statusCode === 404"</span>></span>⻚⾯不存在<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">v-else</span>></span>应⽤发⽣错误异常<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; error &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">nuxt-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>⾸ ⻚<span class="hljs-tag"></<span class="hljs-name">nuxt-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">"error"</span>],
  <span class="hljs-attr">layout</span>: <span class="hljs-string">"empty"</span>
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看下结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f5343d11c04db1a82bac8c88a90075~tplv-k3u1fbpfcp-watermark.image" alt="自定义错误页面.png" loading="lazy" referrerpolicy="no-referrer">
<strong>4、页面</strong>
⻚⾯组件就是 Vue 组件，只不过 Nuxt.js 为这些组件添加了⼀些特殊的配置项，比如给⾸⻚添加标题和meta等，index.vue：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">head</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">"课程列表"</span>,
      <span class="hljs-comment">// vue-meta利⽤hid确定要更新meta</span>
      <span class="hljs-attr">meta</span>: [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"description"</span>, <span class="hljs-attr">hid</span>: <span class="hljs-string">"description"</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">"set pagemeta"</span> &#125;],
      <span class="hljs-attr">link</span>: [&#123; <span class="hljs-attr">rel</span>: <span class="hljs-string">"favicon"</span>, <span class="hljs-attr">href</span>: <span class="hljs-string">"favicon.ico"</span> &#125;],
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来看下结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64ffbc02c1b64afd886cbc531447d022~tplv-k3u1fbpfcp-watermark.image" alt="自定义页面配置.png" loading="lazy" referrerpolicy="no-referrer">
Nuxt.js为页面提供的自定义特殊配置，具体可以查看官网：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6119f19ff649419208da7a4d4afb1f~tplv-k3u1fbpfcp-watermark.image" alt="为页面提供的特殊配置.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">异步数据获取</h2>
<p>asyncData ⽅法使得我们可以在设置组件数据之前异步获取或处理数据。
PS：看了上一篇的会对这个方法熟悉</p>
<p>接下来我们就通过一个例子来实践一下：</p>
<p>1、安装依赖，我们以koa为例编写服务端接口：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i koa-router koa-bodyparser -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、编写服务端脚本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>);
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();
<span class="hljs-keyword">const</span> bodyparser = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-bodyparser"</span>);
<span class="hljs-keyword">const</span> router = <span class="hljs-built_in">require</span>(<span class="hljs-string">"koa-router"</span>)(&#123; <span class="hljs-attr">prefix</span>: <span class="hljs-string">"/api"</span> &#125;);

<span class="hljs-keyword">const</span> goods = [
  &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">text</span>: <span class="hljs-string">"iphone12"</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">1000</span> &#125;,
  &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">text</span>: <span class="hljs-string">"guangying"</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">1000</span> &#125;
];

<span class="hljs-comment">// 配置路由</span>
<span class="hljs-comment">// 获取产品列表</span>
router.get(<span class="hljs-string">"/goods"</span>, <span class="hljs-function"><span class="hljs-params">ctx</span> =></span> &#123;
  ctx.body = &#123;
    <span class="hljs-attr">ok</span>: <span class="hljs-number">1</span>,
    goods
  &#125;;
&#125;);

<span class="hljs-comment">// 解析post数据并注册路由</span>
app.use(bodyparser());
<span class="hljs-comment">// 注册路由</span>
app.use(router.routes());
app.listen(<span class="hljs-number">3030</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'api服务已启动'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、整合Axios模块
先安装依赖：</p>
<pre><code class="hljs language-js copyable" lang="js">npm install @nuxtjs/axios -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在nuxt.config.js里面配置：</p>
<pre><code class="hljs language-js copyable" lang="js">modules: [
  <span class="hljs-string">'@nuxtjs/axios'</span>,
],
<span class="hljs-attr">axios</span>: &#123;
  <span class="hljs-attr">proxy</span>: <span class="hljs-literal">true</span>
&#125;,
<span class="hljs-attr">proxy</span>: &#123;
  <span class="hljs-string">"/api"</span>: <span class="hljs-string">"http://localhost:3030"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、测试代码，index.vue：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">asyncData</span>(<span class="hljs-params">&#123; $axios, error &#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; ok, goods &#125; = <span class="hljs-keyword">await</span> $axios.$get(<span class="hljs-string">"/api/goods"</span>);
    <span class="hljs-keyword">if</span> (ok) &#123;
      <span class="hljs-keyword">return</span> &#123; goods &#125;;
    &#125;
    <span class="hljs-comment">// 错误处理</span>
    error(&#123; <span class="hljs-attr">statusCode</span>: <span class="hljs-number">400</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">"数据查询失败"</span> &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们启动server服务器，然后看下我们测试的结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5625685f39941388d0f4248e9ad9be4~tplv-k3u1fbpfcp-watermark.image" alt="asyncData异步数据.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">状态管理Vuex</h2>
<p>应⽤根⽬录下如果存在 store ⽬录，Nuxt.js将启⽤vuex状态树。定义各状态树时具名导出state, mutations, getters, actions即可</p>
<p>我们以用户登陆为例，先新建store/user.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> state = <span class="hljs-function">() =></span> (&#123;
  <span class="hljs-attr">token</span>: <span class="hljs-string">""</span>
&#125;);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> mutations = &#123;
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">state, token</span>)</span> &#123;
    state.token = token;
  &#125;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getters = &#123;
  <span class="hljs-function"><span class="hljs-title">isLogin</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-keyword">return</span> !!state.token;
  &#125;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> actions = &#123;
  <span class="hljs-function"><span class="hljs-title">login</span>(<span class="hljs-params">&#123; commit, getters &#125;, u</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$axios.$post(<span class="hljs-string">"/api/login"</span>, u).then(<span class="hljs-function">(<span class="hljs-params">&#123; token &#125;</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (token) &#123;
        commit(<span class="hljs-string">"init"</span>, token);
      &#125;
      <span class="hljs-keyword">return</span> getters.isLogin;
    &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在pages/login.vue中写入登录逻辑：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>⽤户登录<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"user.username"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"user.password"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"onLogin"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">user</span>: &#123;
        <span class="hljs-attr">username</span>: <span class="hljs-string">""</span>,
        <span class="hljs-attr">password</span>: <span class="hljs-string">""</span>
      &#125;
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onLogin</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.dispatch(<span class="hljs-string">"user/login"</span>, <span class="hljs-built_in">this</span>.user).then(<span class="hljs-function"><span class="hljs-params">ok</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (ok) &#123;
          <span class="hljs-keyword">const</span> redirect = <span class="hljs-built_in">this</span>.$route.query.redirect || <span class="hljs-string">"/"</span>;
          <span class="hljs-built_in">this</span>.$router.push(redirect);
        &#125;
      &#125;);
    &#125;
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后这时候我们的登录逻辑就完成了！</p>
<h2 data-id="heading-10">中间件</h2>
<p>中间件会在⼀个⻚⾯或⼀组⻚⾯渲染之前运⾏我们定义的函数，常⽤于权限控制、校验等任务。</p>
<p>比如我们在进入admin管理页面的时候就可以使用中间件，判断此时是否登录，如果没有则重定向到登录页面，我们先来编写中间件，创建middleware/auth.js：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">&#123; route, redirect, store &#125;</span>) </span>&#123;
  <span class="hljs-comment">// 上下⽂中通过store访问vuex中的全局状态</span>
  <span class="hljs-comment">// 通过vuex中令牌存在与否判断是否登录</span>
  <span class="hljs-keyword">if</span> (!store.state.user.token) &#123;
    redirect(<span class="hljs-string">"/login?redirect="</span> + route.path);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写完之后我们剩下来要做的就是注册中间件，这里有两方式：</p>
<ul>
<li>全局注册中间件，这种方式就是会直接作用在全局范围内，对每一个页面的访问都会有用，这种方式就直接在nuxt.config.js里面配置：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">router: &#123;
    <span class="hljs-attr">middleware</span>: [<span class="hljs-string">'auth'</span>],
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>局部注册中间件，这种方式就是按需注册，哪个页面需要就在哪个页面里面注册使用就行，注册方式就是如在admin.vue中：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">middleware</span>: [<span class="hljs-string">'auth'</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">插件</h2>
<p>Nuxt.js会在运⾏应⽤之前执⾏插件函数，需要引⼊或设置Vue插件、⾃定义模块和第三⽅模块时特别有⽤</p>
<p>我们可以来写一个简单的插件，添加请求拦截器附加token，创建plugins/interceptor.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">&#123; $axios, store &#125;</span>) </span>&#123;
  <span class="hljs-comment">//onRequest是@nuxtjs/axios模块提供的帮助方法</span>
  $axios.onRequest(<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">// 附加令牌</span>
    <span class="hljs-keyword">if</span> (store.state.user.token) &#123;
      config.headers.Authorization = <span class="hljs-string">"Bearer "</span> + store.state.user.token;
    &#125;
    <span class="hljs-keyword">return</span> config;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样我们也需要注册插件，在nuxt.config.js中：</p>
<pre><code class="hljs language-js copyable" lang="js">plugins: [<span class="hljs-string">"@/plugins/interceptor"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们每次在会有用到网络请求的时候都会使用到这个插件</p>
<h2 data-id="heading-12">nuxtServerInit</h2>
<p>通过在store的<strong>根模块</strong>中定义 nuxtServerInit ⽅法，Nuxt.js 调⽤它的时候会将⻚⾯的上下⽂对象作为第2个参数传给它。当我们想将服务端的⼀些数据传到客户端时，这个⽅法⾮常好⽤。</p>
<ul>
<li>nuxtServerInit只能写在store/index.js</li>
<li>nuxtServerInit仅在服务端执⾏</li>
</ul>
<p>比如在这个例子里面我们要做到登录状态初始化，我们就可以在store/index.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> actions = &#123;
  <span class="hljs-function"><span class="hljs-title">nuxtServerInit</span>(<span class="hljs-params">&#123; commit &#125;, &#123; app &#125;</span>)</span> &#123;
    <span class="hljs-comment">// 注意这个app是服务端实例，在我们这个例子中就是koa实例</span>
    <span class="hljs-keyword">const</span> token = app.$cookies.get(<span class="hljs-string">"token"</span>);
    <span class="hljs-keyword">if</span> (token) &#123;
      commit(<span class="hljs-string">"user/init"</span>, token);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在运行之前我们需要先安装一个依赖：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i -S cookie-universal-nuxt
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在nuxt.config.js中注册：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">modules: [<span class="hljs-string">'@nuxtjs/axios'</span>, <span class="hljs-string">'@nuxtjs/proxy'</span>, <span class="hljs-string">"cookie-universal-nuxt"</span>],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开发过程中会涉及的几大特性基本完结！现在你再回过头去看那个nuxt的渲染流程图，是不是会明白许多了呢？</p>
<h2 data-id="heading-13">发布部署</h2>
<p>1、<strong>服务端渲染应用部署</strong>：先进⾏编译构建，然后再启动 Nuxt 服务</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm run build
npm start
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包生成的内容位置见图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6441efa9187649a6b5fac2b37c9c53a9~tplv-k3u1fbpfcp-watermark.image" alt="服务端渲染应用部署.png" loading="lazy" referrerpolicy="no-referrer">
2、<strong>静态应用部署</strong>：Nuxt.js 可依据路由配置将应⽤静态化，使得我们可以将应⽤部署⾄任何⼀个静态站点主机服务商。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm run generate
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行命令之前注意渲染和接⼝服务器都需要处于启动状态</li>
<li>⽣成内容在dist中（根目录的，和上一种方式的不一样）</li>
</ul>
<p>这种方式的好处就是他会在打包过程中将所有的页面都会打包处理成静态html页面，这样其实在我们打开URL的时候我们其实访问就是静态页面，我们可以想到那这样不用每次都要渲染了，那我们访问时候的效率将会是一个巨大的提升！</p>
<p>OK，Vue SSR最后一篇文章也就结束啦～</p>
<p>这一篇我们主要学习了Vue SSR开箱即用的方案Nuxt.js，我们分析了Nuxt的基本核心内容，其余具体还有更多的点还需要我们以后慢慢去挖掘，好啦，Vue SSR系列基本上就已经结束了，经过三篇文章下来，相信我们应该对SSR的相关的东西都有了一些了解了吧～</p>
<h2 data-id="heading-14">文末</h2>
<p>欢迎关注「前端光影」公众号，公众号都是以系统专题模块的形式来展示的，这样看起来就会比较方便，系统，让我们一起持续学习各种前端知识，加油！</p></div>  
</div>
            