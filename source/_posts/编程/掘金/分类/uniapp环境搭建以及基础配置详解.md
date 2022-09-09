
---
title: 'uniapp环境搭建以及基础配置详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d59a6bd5fe1b44f98e9f6726e61ab4b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 19:11:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d59a6bd5fe1b44f98e9f6726e61ab4b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与「新人创作礼」活动， 一起开启掘金创作之路。</p>
<h2 data-id="heading-0">环境搭建</h2>
<ul>
<li>安装编辑器 HbuilderX(HbuilderX 是通用的前端开发工具，但为 uni-app 做了特别强化)。</li>
<li>下载 APP 开发板，可开箱即用。</li>
<li>安装微信开发者工具。</li>
</ul>
<h2 data-id="heading-1">利用 HbuilderX 初始化项目</h2>
<h3 data-id="heading-2">创建 uni-app 项目</h3>
<blockquote>
<p>选择 uni-app 类型，输入工程名，选择模板，点击创建，即可成功创建。</p>
<p>un-app 自带的模板有 Hello uni-app，是官方的组件和 API 示例。</p>
<p>还有一个重要的模板是 uni ui 项目模板，日常开发推荐使用该模板，已内置大量常用组件。</p>
</blockquote>
<h3 data-id="heading-3">运行 uni-app</h3>
<blockquote>
<p>主要包括：浏览器运行、真机运行、小程序运行等。</p>
</blockquote>
<h3 data-id="heading-4">发布 uni-app</h3>
<blockquote>
<p>主要包括：云端原生 APP、离线原生 APP、H5、各种小程序。</p>
</blockquote>
<h2 data-id="heading-5">uni-app 初始化相关配置</h2>
<h3 data-id="heading-6">工程目录结构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d59a6bd5fe1b44f98e9f6726e61ab4b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提示：</p>
<ul>
<li><code>static</code>下目录的 js 文件不会被 webpack 编译，里面如果有 es6 的代码，不经过转换直接运行，在手机设备上会报错。</li>
<li>所以 less、scss 等资源同样不要放在 static 目录下，建议这些公共的资源放在 common 目录下。</li>
</ul>
</blockquote>
<h3 data-id="heading-7">应用配置 manifest.json</h3>
<blockquote>
<p><code>manifest.json</code>文件是应用的配置文件，用于指定应用的名称、图标、权限等，也可以为 Vue 为 H5 设置跨域拦截处理器。</p>
</blockquote>
<h3 data-id="heading-8">编译配置 vue.config.js</h3>
<blockquote>
<p><code>vue.config.js</code>是一个可选的配置文件，如果项目的根目录中存在这个文件，那么它会被自动加载，一般用于配置 webpack 等编译选项。</p>
</blockquote>
<h3 data-id="heading-9">全局配置 page.json</h3>
<blockquote>
<p><code>page.json</code>文件用来对 uni-app 进行全局配置，决定页面文件的路径、窗口样式、原生的导航栏、底部的原生 tabbar 等。类似于微信小程序中<code>app.json</code>的页面管理部分。</p>
</blockquote>





















































<table><thead><tr><th>属性</th><th>类型</th><th>必填</th><th>描述</th></tr></thead><tbody><tr><td>globalStyle</td><td>Object</td><td>否</td><td>设置默认页面的窗口表现</td></tr><tr><td>pages</td><td>Object Array</td><td>是</td><td>设置页面路径及窗口表现</td></tr><tr><td>easycom</td><td>Object</td><td>否</td><td>组件自动引入规则</td></tr><tr><td>tabBar</td><td>Object</td><td>否</td><td>设置底部 tab 的表现</td></tr><tr><td>condition</td><td>Object</td><td>否</td><td>启动模式配置</td></tr><tr><td>subPackages</td><td>Object Array</td><td>否</td><td>分包加载配置</td></tr><tr><td>preloadRule</td><td>Object</td><td>否</td><td>分包预下载规则</td></tr></tbody></table>
<h3 data-id="heading-10">全局样式 uni.scss</h3>
<blockquote>
<p><code>uni.scss</code>文件的用途是为了方便整体控制应用的风格。比如按钮颜色、边框风格，<code>uni.scss</code>文件里预置了一批 scss 变量预置。</p>
<p>uni-app 官方扩展插件（uni ui）及插件市场上很多第三方插件均使用了这些样式变量，如果是样式开发，建议使用 scss 预处理，并在代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的 APP 。</p>
<p><code>uni.scss</code>是一个特殊文件，在代码中无需 import 这个文件即可在 scss 代码中使用这样的样式变量。uni-app 的编译器载 webpack 配置中特殊处理了这个 uni.scss，使得每个 scss 文件都被注入这个 uni.scss，达到全局可用效果。如果想要 less、stylus 的全局使用，需要在 vue.config.js 中自行配置 webpack 策略。</p>
</blockquote>
<h3 data-id="heading-11">主组件 App.vue</h3>
<blockquote>
<p><code>App.vue</code>是 uni-app 的主组件，所有页面都是在 <code>App.vue</code> 下进行切换的，是页面入口文件。但 <code>App.vue</code> 本身不是页面，这里不能编写视图元素。</p>
<p>这个文件的作用包括：调用应用生命周期函数、配置全局样式、配置全局的存储 globalData 。</p>
<p>应用生命周期仅可在 <code>App.vue</code> 中监听，在页面监听无效。</p>
</blockquote>
<h3 data-id="heading-12">入口文件 main.js</h3>
<blockquote>
<p><code>main.js</code> 是 uni-app 的入口文件，主要作用是初始化 vue 实例、定义全局组件、使用需要的插件如 vuex 。</p>
</blockquote></div>  
</div>
            