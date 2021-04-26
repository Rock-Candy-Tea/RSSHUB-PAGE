
---
title: 'Vue3发布半年我不学，摸鱼爽歪歪，哎~就是玩儿'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 08:22:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image" alt="quote" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是从 Vue 2 开始学基础还是直接学 Vue 3 ？<strong>尤雨溪给出的答案是：</strong>“直接学 Vue 3 就行了，基础概念是一模一样的。”</p>
<p>以上内容源引自最新一期的《程序员》期刊，原文链接为<a href="https://mp.weixin.qq.com/s/K9Fb5lMxD2WbxQrk6y6sZA" target="_blank" rel="nofollow noopener noreferrer">《直接学 Vue 3 吧 —— 对话 Vue.js 作者尤雨溪》</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p><code>Vue 3.0</code> 出来之后，我一直在不断的尝试学习和接受新的概念。没办法，作为一个前端开发，并且也不是毕业于名校或就职于大厂，不断地学习，培养学习能力，才是我们这些普通前端开发的核心竞争力。</p>
<p>当然，有些同学抬杠，我专精一门技术，也能开发出自己的核心竞争力。好！！！有志气。但是多数同学，很难有这种意志力。如 <code>CSS</code> 大佬<a href="https://www.zhangxinxu.com/" target="_blank" rel="nofollow noopener noreferrer">张鑫旭</a>、 <code>Canva</code> 大佬<a href="https://juejin.cn/user/78820536232855" target="_blank">老姚</a>、可视化大佬<a href="https://juejin.cn/user/712139263189303" target="_blank">月影大大</a>、面试题大佬<a href="https://juejin.cn/user/4406498333825357" target="_blank">敖丙</a>等等等等。这些大佬在一件事情上花费的精力，是需要极高的意志力和执行力才能做到的。我反正做不到（逃）。</p>
<p>学无止境！</p>
<p>一定要动手敲代码。仅仅学习而不实践，这种做法也不可取。</p>
<p>本文主要是介绍一些我学习 <code>Vue 3.0</code> 期间，看过的一些比较有用的资源，和大家分享一下，不喜勿喷，喷了我也学着 @尼克陈 顺着网线找到你家。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86b6d7fe1b4f409b9155576e12adcd21~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">我与 Vue 3.0</h2>
<p>其实一直都有在关注 Vue 3.0 相关的进度和新闻，不过真正学习是在它正式 release 后，2020 年 9 月我也发布了一篇文章<a href="https://juejin.cn/post/6874604408030789640" target="_blank">《Vue 3.0 来了，我们该做些什么？》</a>阐述了自己的看法，也制定了自己的学习计划。</p>
<p>其实，学习任何一门新技术的步骤都一样：</p>
<p>看文档 → 学习新语法 → 做小 demo → 做几个实战项目 → 看源码 → 整理心得并分享。</p>
<p>学习 Vue 3.0 亦是如此，虽然我这个人比较爱开玩笑，也爱写段子，标题取的也吊儿郎当，但是学习和行动起来我可不比别人差。</p>
<p>学习过程中看文档、做 demo，然后也一直在学习和分享 Vue3 的知识点，比如发布一些 Vue3 的教程：</p>
<ul>
<li><a href="https://juejin.cn/post/6874604408030789640" target="_blank">《Vue 3.0 来了，我们该做些什么？》</a></li>
<li><a href="https://juejin.cn/post/6882393804310052871" target="_blank">《Vue3实战系列：结合 Ant-Design-of-Vue 实践 Composition API》</a></li>
<li><a href="https://juejin.cn/post/6884991023811215374" target="_blank">《Vue3 来了，Vue3 开源商城项目重构计划正式启动！》</a></li>
<li><a href="https://juejin.cn/post/6887590229692121096" target="_blank">《Vue3实战系列：Vue3.0 + Vant3.0 搭建种子项目》</a></li>
<li><a href="https://juejin.cn/post/6892783570016796679" target="_blank">《🎉🎉一个基于 Vue 3 + Vant 3 的开源商城项目🎉🎉》</a></li>
<li><a href="https://juejin.cn/post/6895360073460416525" target="_blank">《Vue3教程：用 Vue3 开发小程序，这里有一份实践代码！》</a></li>
<li><a href="https://juejin.cn/post/6903171037211557895" target="_blank">《Vue3教程：Vue 3.x 快在哪里？》</a></li>
<li><a href="https://juejin.cn/post/6942251234191654949" target="_blank">《Vue3教程：开发一个 Vue 3 + element-plus 的后台管理系统》</a></li>
<li><a href="https://juejin.cn/post/6945072070132760590" target="_blank">《🎉🎉Vue 3 + Element Plus + Vite 2 的后台管理系统开源啦🎉🎉》</a></li>
<li><a href="https://juejin.cn/post/6947703226128924702" target="_blank">程序员的副业：写了一个专栏《Vue 3企业级项目实战》</a></li>
</ul>
<p>也做了几个  Vue 3.0 实战的项目练手，之后发布到也开源了 GitHub 中，访问地址如下：</p>
<blockquote>
<p>in GitHub : <a href="https://github.com/newbee-ltd" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd</a></p>
<p>in Gitee : <a href="https://gitee.com/newbee-ltd" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd</a></p>
</blockquote>
<p>一个是 Vue3 版本的商城项目：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3382607a2a46a2944d59d4ad7cf3be~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个是 Vue3 版本的后台管理项目：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1482ea27549d4462bfc97ca14765fd2a~tplv-k3u1fbpfcp-zoom-1.image" alt="panban1 (1)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>源码全部开放，后台 API 也有，都是很实用的项目。目前的反响还不错，得到了很多的正向反馈，这些免费的开源项目让大家有了一个不错的 Vue3 练手项目，顺利的完成了课程作业或者在简历里多了一份项目经验，因此也收到了很多感谢的话。</p>
<p>接下来就是学习过程中，我觉得非常有用的资源了，大家在学习 Vue 3 时可以参考和使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcd33c72e2c644e7b860fd885b316e21~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210228175425067" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Vue 3.0 相关技术栈</h2>

















































<table><thead><tr><th>相关库名称</th><th>在线地址 🔗</th></tr></thead><tbody><tr><td>Vue 3.0 官方文档(英文)</td><td><a href="https://v3.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 中文文档</td><td><a href="https://v3.cn.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">在线地址</a> <a href="https://vue3js.cn/docs/zh/" target="_blank" rel="nofollow noopener noreferrer">国内加速版</a></td></tr><tr><td>Composition-API手册</td><td><a href="https://vue3js.cn/vue-composition-api/" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 源码学习</td><td><a href="https://vue3js.cn/start/" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue-Router 官方文档</td><td><a href="https://next.router.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vuex 4.0</td><td><a href="https://github.com/vuejs/vuex/tree/4.0" target="_blank" rel="nofollow noopener noreferrer">Github</a></td></tr><tr><td>vue-devtools</td><td><a href="https://github.com/vuejs/vue-devtools/releases" target="_blank" rel="nofollow noopener noreferrer">Github</a>(Vue3.0 需要使用最新版本)</td></tr><tr><td>Vite 源码学习</td><td><a href="https://vite-design.surge.sh/guide/" target="_blank" rel="nofollow noopener noreferrer">线上地址</a></td></tr><tr><td>Vite 2.0 中文文档</td><td><a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">线上地址</a></td></tr><tr><td>Vue3 新动态</td><td><a href="https://github.com/vue3/vue3-News" target="_blank" rel="nofollow noopener noreferrer">线上地址</a></td></tr></tbody></table>
<p><a href="https://github.com/vue3/vue3-News" target="_blank" rel="nofollow noopener noreferrer">Vue3 新动态</a> 这个仓库我经常看，里面有最新的 Vue 3 文章、仓库等等，都是中文的，作者应该是咱们的大兄弟，大家也可以关注一下。</p>
<h2 data-id="heading-3">更新 Vue 3.0 的开源 UI 组件库</h2>
<p><code>Vue 2.0</code> 时期，产生了不少好的开源组件库，这些组件库伴随着我们的成长，我们看看哪些组件库更新了 <code>Vue 3.0</code> 版本。</p>
<h4 data-id="heading-4">Element-plus</h4>
<p><strong>简介</strong>：大家想必也不陌生，它的 <code>Vue 2.0</code> 版本是 <code>Element-UI</code>，后经<a href="https://juejin.cn/user/3315782798806430" target="_blank">坤哥</a>和他的小伙伴开发出了 <code>Vue 3.0</code> 版本的  <code>Element-plus</code>，确实很优秀，目前点赞数快破万了，持续关注。</p>
<p><strong>仓库地址</strong> 🏠 ：<a href="https://github.com/element-plus/element-plus" target="_blank" rel="nofollow noopener noreferrer">github.com/element-plu…</a> ⭐ ： <strong>9.8k</strong></p>
<p><strong>文档地址</strong> 📖 ：<a href="https://element-plus.gitee.io/#/zh-CN" target="_blank" rel="nofollow noopener noreferrer">element-plus.gitee.io/#/zh-CN</a></p>
<p><strong>开源项目</strong> 🔗 ：</p>
<ul>
<li><a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">Vue 3.0 + Vite 2.0 + Vue-Router 4.0 + Element-Plus + Echarts 5.0 + Axios 开发的后台管理系统</a> ⭐ ： <strong>419</strong></li>
<li><a href="https://github.com/xiaoxian521/CURD-TS" target="_blank" rel="nofollow noopener noreferrer">Vue3.0+TypeScript+NodeJS+MySql编写的一套后台管理系统</a> ⭐ ： <strong>262</strong></li>
</ul>
<p>目前 <code>Element-plus</code> 的开源项目还不多，之前 <code>Element-UI</code> 相关开源项目，大大小小都在做 <code>Element-plus</code> 的适配。在此也感谢<a href="https://juejin.cn/user/3315782798806430" target="_blank">坤哥</a>和他的小伙伴们，持续 <code>Element</code> 系列的维护，这对 <code>Vue</code> 生态是非常强大的贡献。</p>
<h4 data-id="heading-5">Ant Design of Vue</h4>
<p><strong>简介</strong>：它是最早一批做 <code>Vue 3.0</code> 适配的组件库， <code>Antd</code> 官方推荐的组件库。</p>
<p><strong>仓库地址</strong> 🏠 ：<a href="https://github.com/vueComponent/ant-design-vue/" target="_blank" rel="nofollow noopener noreferrer">github.com/vueComponen…</a> ⭐ ： <strong>14.8k</strong></p>
<p><strong>文档地址</strong> 📖 ：<a href="https://antdv.com/docs/vue/introduce-cn/" target="_blank" rel="nofollow noopener noreferrer">antdv.com/docs/vue/in…</a></p>
<p><strong>开源项目</strong> 🔗 ：</p>
<ul>
<li><a href="https://github.com/iczer/vue-antd-admin" target="_blank" rel="nofollow noopener noreferrer">AntdV后台管理系统</a> ⭐ ： <strong>2.8k</strong></li>
<li><a href="https://github.com/chuzhixin/vue-admin-better" target="_blank" rel="nofollow noopener noreferrer">vue3.x + ant-design-vue（beta 版本，免费商用，支持 PC、平板、手机）</a> ⭐ ： <strong>8.2k</strong></li>
<li><a href="https://github.com/lirongtong/miitvip-vue-admin-manager" target="_blank" rel="nofollow noopener noreferrer">基于 Vue3.0 + Vite + Ant Design Vue</a> ⭐ ： <strong>74</strong></li>
</ul>
<p>他们的更新维护还是很积极的，最近一次更新实在 2021 年 2 月 27 号，可见这个组件库还是值得信赖的，有问题可以去 issue 提。</p>
<h4 data-id="heading-6">Vant</h4>
<p><strong>简介</strong>：国内移动端首屈一指的组件库，用过的都说好，个人已经在两个项目中使用过该组件库，也算是比较早支持 <code>Vue 3.0</code> 的框架，该有的都有。</p>
<p><strong>仓库地址</strong> 🏠 ：<a href="https://github.com/youzan/vant" target="_blank" rel="nofollow noopener noreferrer">github.com/youzan/vant</a> ⭐ ： <strong>16.9k</strong></p>
<p><strong>文档地址</strong> 📖 ：<a href="https://vant-contrib.gitee.io/vant/v3/#/zh-CN" target="_blank" rel="nofollow noopener noreferrer">vant-contrib.gitee.io/vant/v3/#/z…</a></p>
<p><strong>开源项目</strong> 🔗 ：</p>
<ul>
<li><a href="https://github.com/newbee-ltd/newbee-mall-vue3-app" target="_blank" rel="nofollow noopener noreferrer">newbee-mall Vue3 版本</a>⭐ ： <strong>1.7k</strong></li>
<li><a href="https://github.com/Nick930826/daily-cost" target="_blank" rel="nofollow noopener noreferrer">高仿微信记账本</a> ⭐ ： <strong>48</strong></li>
<li><a href="https://github.com/GitHubGanKai/vue3-jd-h5" target="_blank" rel="nofollow noopener noreferrer">仿京东淘宝电商</a>  ⭐ ： <strong>319</strong></li>
</ul>
<h4 data-id="heading-7">NutUI 3</h4>
<p><strong>简介</strong>：京东团队开发的移动端组件库，近期才升级到 <code>Vue 3.0</code> 版本，<a href="https://juejin.cn/post/6935231099102560293" target="_blank">文章在此</a>。虽然我没有使用过这个组件库，但是从他们的更新速度来看，比其他很多组件库要快，说明对待最近技术，还是有态度的。</p>
<p><strong>仓库地址</strong> 🏠 ：<a href="https://github.com/jdf2e/nutui" target="_blank" rel="nofollow noopener noreferrer">github.com/jdf2e/nutui</a> ⭐ ： <strong>3.1k</strong></p>
<p><strong>文档地址</strong> 📖 ：<a href="https://nutui.jd.com/#/index" target="_blank" rel="nofollow noopener noreferrer">nutui.jd.com</a> （看看这简短的域名，透露出壕的气息）</p>
<p><strong>开源项目</strong> 🔗 ：基本上还没有见到有公开的开源项目，如果有还望大家积极评论。</p>
<h2 data-id="heading-8">Vue 3.0 实战视频学习</h2>





































<table><thead><tr><th>相关库名称</th><th>在线地址 🔗</th></tr></thead><tbody><tr><td>Vue 3.0 实战星座物语 H5 项目</td><td><a href="https://www.bilibili.com/video/BV1Q64y1F7mm?from=search&seid=15048255084253288459" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 UI 组件库开发</td><td><a href="https://www.bilibili.com/video/BV1ny4y1i7Sh?from=search&seid=15048255084253288459" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 + Vite 手册阅读</td><td><a href="https://www.bilibili.com/video/BV1Q54y1k7At?from=search&seid=15048255084253288459" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 入门之项目搭建（杨村长）</td><td><a href="https://www.bilibili.com/video/BV1vX4y1K7bQ?from=search&seid=17184556019333060655" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 入门（技术胖）</td><td><a href="https://www.bilibili.com/video/BV1L5411j7vj?from=search&seid=17184556019333060655" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vite 2.0 插件开发指南</td><td><a href="https://www.bilibili.com/video/BV1jb4y1R7UV?from=search&seid=384387825939775015" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr><tr><td>Vue 3.0 + Vite 2.0 快速搭建 Electron 应用</td><td><a href="https://www.bilibili.com/video/BV1XV411e7Hq?from=search&seid=384387825939775015" target="_blank" rel="nofollow noopener noreferrer">在线地址</a></td></tr></tbody></table>
<blockquote>
<p>上述视频，本人都学习过，质量可控，希望对大家入门 Vue 3.0 有帮助。</p>
</blockquote>
<h2 data-id="heading-9">总结</h2>
<p>学习是一辈子的事，不光指学习计算机技术，生活的方方面面都需要保持一个学习的心，祝大家学习愉快。</p>
<blockquote>
<p>除注明转载/出处外，皆为作者原创，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文链接，否则保留追究法律责任的权利。</p>
</blockquote></div>  
</div>
            