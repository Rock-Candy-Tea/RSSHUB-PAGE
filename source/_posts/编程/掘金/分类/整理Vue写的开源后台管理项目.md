
---
title: '整理Vue写的开源后台管理项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f57684f2b5054b29880bad99fb143285~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 09 May 2021 01:44:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f57684f2b5054b29880bad99fb143285~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>国人开发的前端框架Vue.js现在在国内的前端市场还是很多的，所以推荐几个开源很热的项目，不需要各位来重复造轮子，</p>
<h2 data-id="heading-0">美观的后台模板</h2>
<h3 data-id="heading-1">Vue-element-admin</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f57684f2b5054b29880bad99fb143285~tplv-k3u1fbpfcp-zoom-1.image" alt="68747470733a2f2f7770696d672e77616c6c7374636e2e636f6d2f61353839346331622d663661662d343536652d383264662d3131353164613038333962662e706e67.png" loading="lazy" referrerpolicy="no-referrer">
<a href="https://panjiachen.github.io/vue-element-admin" target="_blank" rel="nofollow noopener noreferrer">vue-element-admin</a> 是一个后台前端解决方案，它基于 <a href="https://github.com/vuejs/vue" target="_blank" rel="nofollow noopener noreferrer">vue</a> 和 <a href="https://github.com/ElemeFE/element" target="_blank" rel="nofollow noopener noreferrer">element-ui</a>实现。它使用了最新的前端技术栈，内置了 i18n 国际化解决方案，动态路由，权限验证，提炼了典型的业务模型，提供了丰富的功能组件，它可以帮助你快速搭建企业级中后台产品原型。相信不管你的需求是什么，
想接私活？这就是你的选择之一。
地址：<a href="https://github.com/PanJiaChen/vue-element-admin" target="_blank" rel="nofollow noopener noreferrer">github.com/PanJiaChen/…</a></p>
<h3 data-id="heading-2">vue-manage-system</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85ac2828fdf4f379bd6cff7af2b4e45~tplv-k3u1fbpfcp-zoom-1.image" alt="20190411152731598.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>该后台模板在Github的星标虽然没有vue-element-admin的start多，但是也是一个不错的vue后台模板，而且也升级到vue3了</p>
<p>地址：<a href="https://github.com/lin-xin/vue-manage-system" target="_blank" rel="nofollow noopener noreferrer">github.com/lin-xin/vue…</a></p>
<h3 data-id="heading-3">NX-Admin</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67d6bb13dc1546269208c6cb9fe751d3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/mgbq/nx-admin" target="_blank" rel="nofollow noopener noreferrer">nx-admin</a> 是基于 Vue2.0，配合使用 Element UI 组件库的一个前端管理后台集成解决方案
该开源项目好像没有维护了
地址：<a href="https://github.com/taylorchen709/vue-admin" target="_blank" rel="nofollow noopener noreferrer">github.com/taylorchen7…</a></p>
<h3 data-id="heading-4">vue-admin</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b70f05b2c3a04281be20e792d04e2032~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一个Vue2+elementUI搭建的清爽后台，这个框架东西不多，可以当作vue写的第一个练手项目
该开源项目好像没有维护了
地址：<a href="https://github.com/taylorchen709/vue-admin" target="_blank" rel="nofollow noopener noreferrer">github.com/taylorchen7…</a></p>
<h3 data-id="heading-5">D2admin</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/093f60294783456d87dcc9ad07fbbdcc~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/d2-projects/d2-admin" target="_blank" rel="nofollow noopener noreferrer">D2Admin (opens new window)</a>是一个完全 <strong>开源免费</strong> 的企业中后台产品前端集成方案，使用最新的前端技术栈，小于 60kb 的本地首屏 js 加载，已经做好大部分项目前期准备工作，并且带有大量示例代码，助力管理系统快速开发。
开源地址：<a href="https://github.com/d2-projects/d2-admin" target="_blank" rel="nofollow noopener noreferrer">github.com/d2-projects…</a>
文档地址：<a href="https://d2.pub/zh/doc/d2-admin/" target="_blank" rel="nofollow noopener noreferrer">d2.pub/zh/doc/d2-a…</a>
效果预览：<a href="https://d2.pub/d2-admin/preview/#/index" target="_blank" rel="nofollow noopener noreferrer">d2.pub/d2-admin/pr…</a></p>
<h3 data-id="heading-6">vue-admin-beautiful</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1bdad8cd37548b7967bb62b9ec038c6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一个开箱即用的Vue后台页面项目
开源地址：<a href="https://github.com/chuzhixin/vue-admin-beautiful" target="_blank" rel="nofollow noopener noreferrer">github.com/chuzhixin/v…</a>
文档地址：<a href="https://www.gin-vue-admin.com/" target="_blank" rel="nofollow noopener noreferrer">www.gin-vue-admin.com/</a>
效果预览：<a href="http://beautiful.panm.cn/" target="_blank" rel="nofollow noopener noreferrer">beautiful.panm.cn/</a></p>
<h2 data-id="heading-7">Api请求构建工具：Hoppscotch</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29b627fdf11640e79ff549adc06b3ba3~tplv-k3u1fbpfcp-zoom-1.image" alt="微信图片_20210509120730.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>hoppscotch是一种可以通过Web服务的方式构建API访问的工具。可以帮助你更快地创建请求，节省开发时间，早下班。Hoppscotch 除了支持 REST API 外，它还支持 GraphQL。它还可以为你的 API 生成文档。</p>
<p>地址：<a href="https://github.com/hoppscotch/hoppscotch" target="_blank" rel="nofollow noopener noreferrer">github.com/hoppscotch/…</a></p>
<h2 data-id="heading-8">best-resume-ever个人简历开源项目</h2>
<p>                                                                                <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4035bd5d600c48fd931735f09dd5f400~tplv-k3u1fbpfcp-zoom-1.image" alt="102712621-5b0df9c6e9326_fix732.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>简历项目，用代码快速构建简历项目，它支持使用 Vue 和 LESS 构建的各种模板。你可以在本地预览自己的简历，还可以在模板之间随意切换，方便选择合适自己的简历。</p>
<h2 data-id="heading-9">一个<strong>优雅的 Markdown 编辑器</strong></h2>
<p>                                                        <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f5ece9f3f114caca36a6552e4344ba2~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
地址：
一款美观的 Markdown 编辑器，我用了一下，感觉没有 Typora 好用。</p>
<p>下期推荐React的开源项目</p></div>  
</div>
            