
---
title: '推荐 7 个 Vue2、Vue3 源码解密分析的重磅开源项目 👍'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 06:56:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79811af9d85a4c6c8a40eb9371253bd9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是你们的 猫哥，那个不喜欢吃鱼、又不喜欢喵 的超级猫 ~</p>
<h2 data-id="heading-0">1. 为什么要学习源码 ?</h2>
<ol>
<li>
<p>阅读优秀的代码的目的是让我们能够写出优秀的代码。</p>
</li>
<li>
<p>不给自己设限，不要让你周围人的技术上限成为你的上限。</p>
</li>
</ol>
<p>其实就跟我们写作文一样，你看的高分作文越多，写出高分作文的概率就越大。</p>
<p>基于现在的程序员工作模式(模块化开发，只需要拿到需求做自己的部分)，别说看源码，甚至就连项目里的代码都懒的去看，我认识的很多程序员就是这样的，一个项目摸了两三年，你要问他项目中 webpack 都干了哪些事情，他的回答是不知道，反而趾高气扬的告诉你，那些他从来都用不上，看了也没什么用，也看不懂，这里省略内心千字脏文。</p>
<p>阅读主要目的 是为了帮助我们 积累素材，不要书到用时方恨少，看到美女我们应该能有一万种词语去形容，如气若幽兰，美艳不可方物，一笑倾城，再笑倾国，世间尤物，而不是简短的几个字，我艹，美女!</p>
<p><strong>功利性的阅读源码</strong></p>
<p>功利性即指有目的性的，明确知道自己干完某一件事后能得到什么样的回报，所以首先你要知道你想得到什么？</p>
<p>看每一本书都有明确的目的，想学会理财，就得看理财相关的书，想学点技术，就得看点技术相关的书</p>
<p>看源码也是一样，你对 Vue.use 之后发生了什么比较好奇，或者是你觉得现在面试都需要会看点源码，这都很好，至少你有明确的诉求</p>
<p>凡事只要有了功利属性，才更容易走的下去，否则就是真香警告。</p>
<h2 data-id="heading-1">2. Vue2</h2>
<p>Vue 虽然出到 Vue3 了，也出了不少 Vue3 的源码教程，但是 Vue2 还是很棒的框架，它的源码还是值得细读的，所以先推荐几个 Vue2 的源码项目。</p>
<h3 data-id="heading-2">2.1 vue-analysis</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79811af9d85a4c6c8a40eb9371253bd9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>👍 Vue.js 源码分析</p>
<p>目前社区有很多 Vue.js 的源码解析文章，但是质量层次不齐，不够系统和全面，这本电子书的目标是全方位细致深度解析 Vue.js 的实现原理，让同学们可以彻底掌握 Vue.js。目前分析的版本是 Vue.js 的最新版本 Vue.js 2.5.17-beta.0，并且之后会随着版本升级而做相应的更新，充分发挥电子书的优势。</p>
<p>这本电子书是作为《Vue.js 源码揭秘》视频课程的辅助教材。电子书是开源的，同学们可以免费阅读，视频是收费的，25+小时纯干货课程，如果有需要的同学可以购买来学习，<strong>但请务必支持正版，请尊重作者的劳动成果</strong>。</p>
<blockquote>
<p><a href="https://github.com/ustbhuangyi/vue-analysis" target="_blank" rel="nofollow noopener noreferrer">github.com/ustbhuangyi…</a></p>
</blockquote>
<h3 data-id="heading-3">2.2 vue-design</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a94caf4d834b04ab18f97aa363d389~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>超级详细 - 逐行级别的分析</strong></p>
<p>所谓逐行并非一行接着一行，逐行指的是讲解的详细程度，这套文章将致力于覆盖所有核心代码，毕竟每一句代码都有他存在的意思，假如我们不讲明白任何一句代码的意义，那又怎么敢说是源码分析呢？</p>
<p><strong>深度分析 - 讲解 issue</strong></p>
<p>我们知道 Vue 这个项目自诞生以来一直都在不断的更新完善，比如添加新的特性，修复已知bug等等。而在这个过程中源码也将越来越完善，这也意味着代码曾经并不完善，本套文章在分析源码时除了告诉你这段代码为什么这么写之外，还会根据相关 issue 分析这段代码之前是怎么写的以及存在的问题。</p>
<blockquote>
<p><a href="http://hcysun.me/vue-design/zh/" target="_blank" rel="nofollow noopener noreferrer">hcysun.me/vue-design/…</a></p>
</blockquote>
<h3 data-id="heading-4">2.3 vue-family-mindmap</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95496781c94943a1b44d8b947d32a2fa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>用一张思维导图总结了 Vue | Vue-Router | Vuex 源码与架构要点。</p>
<p>以上内容是笔者最近学习 Vue 源码时的收获与所做的笔记，本文内容大多是开源项目 <strong>Vue.js 技术揭秘</strong> 的内容，只不过是以思维导图的形式来展现，内容有省略，还加入了笔者的一点理解。</p>
<p>笔者之所以采用思维导图的形式来记录所学内容，是因为思维导图更能反映知识体系与结构，更能使人形成完整的知识架构，知识一旦形成一个体系，就会容易理解和不易忘记。</p>
<blockquote>
<p><strong>注意</strong>：文章的图片可能上传时会经过压缩，可能有点模糊，不过本文用到的 所有 <strong>超清图片</strong> 都已经放在 <a href="https://github.com/biaochenxuying/vue-family-mindmap" target="_blank" rel="nofollow noopener noreferrer">github</a> 上，而且还有 <strong>pdf 格式、markdown 语法、思维导图 的原文件</strong>，自己可以根据 <strong>思维导图原文件</strong> 导出相应的超清图片。</p>
</blockquote>
<blockquote>
<p><a href="https://github.com/biaochenxuying/vue-family-mindmap" target="_blank" rel="nofollow noopener noreferrer">github.com/biaochenxuy…</a></p>
</blockquote>
<h3 data-id="heading-5">2.4 learnVue</h3>
<p>Vue.js 源码分析，记录了个人学习 Vue.js 源码的过程中的一些心得以及收获。以及对于 Vue 框架，周边库的一些个人见解。</p>
<p>在学习的过程中我为Vue.js（2.3.0）、Vuex（2.4.0）、Vue-router（3.0.1）加上了注释，分别在文件夹 vue-src、vuex-src 以及 vue-router-src 中，希望可以帮助有需要的同学更好地学习理解 Vue.js 及周边库的源码。</p>
<blockquote>
<p><a href="https://github.com/answershuto/learnVue" target="_blank" rel="nofollow noopener noreferrer">github.com/answershuto…</a></p>
</blockquote>
<h3 data-id="heading-6">2.5 vue</h3>
<p>Vue 源码逐行注释分析 +40 多 M 的 Vue 源码程序流程图思维导图 （diff 部分待后续更新）</p>
<p>Vue 源码业余时间差不多看了一年，以前在网上找帖子，发现很多帖子很零散，都是一部分一部分说，断章的很多，所以自己下定决定一行行看，经过自己坚持与努力，现在基本看完了 。</p>
<p>这个 Vue 源码逐行分析，我基本每一行都打上注释，加上整个框架的流程思维导图，基本上是小白也能看懂的 Vue 源码了。</p>
<blockquote>
<p><a href="https://github.com/qq281113270/vue" target="_blank" rel="nofollow noopener noreferrer">github.com/qq281113270…</a></p>
</blockquote>
<h2 data-id="heading-7">2.6 vue2.0-source</h2>
<p>Vue 源码分析 -- 基于 2.2.6 版本</p>
<p>该源码分析，会带着大家一起学习 Vue 的大部分代码，而不是简单的讲一下它的原理，我会尽可能的多解释每一行主要的代码含义，另外一些辅助方法什么的，大家可以在学习的过程中，自己看一眼就知道了。</p>
<blockquote>
<p><a href="https://github.com/liutao/vue2.0-source" target="_blank" rel="nofollow noopener noreferrer">github.com/liutao/vue2…</a></p>
</blockquote>
<h2 data-id="heading-8">3. Vue3</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ae8497a706c448aa253b562761867be~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">3.1 中文学习网址</h3>
<p>先给大家提供 2 个 Vue3 的中文学习网址。</p>
<p>Vue3 中文文档，国内 CDN 加速版</p>
<blockquote>
<p><a href="https://vue3js.cn/docs/zh/" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/docs/zh/</a></p>
</blockquote>
<p>Vue3 相关项目聚合网站</p>
<blockquote>
<p><a href="https://vue3js.cn/" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/</a></p>
</blockquote>
<h3 data-id="heading-10">3.2 Vue3 源码</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/261ab56682da4d9b9e4a55356e54fe4f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://vue3js.cn/start/" target="_blank" rel="nofollow noopener noreferrer">vue3js.cn/start/</a></p>
</blockquote>
<h2 data-id="heading-11">最后</h2>
<p>更多关于 Vue3 的优质项目，请看往期精文： <a href="https://mp.weixin.qq.com/s/TbilFowgrMrUigZcHUWB7g" target="_blank" rel="nofollow noopener noreferrer">Vue3 的学习教程汇总、源码解释项目、支持的 UI 组件库、优质实战项目</a></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba5fe9f57d3c4bb2a87e9b4c048424ba~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>公众号：<a href="https://github.com/FrontEndGitHub/FrontEndGitHub" target="_blank" rel="nofollow noopener noreferrer"><strong>前端GitHub</strong></a>，专注于挖掘优秀的前端开源项目，抹平你的前端信息不对称。</p>
</blockquote>
<p>平时如何发现好的开源项目，可以看看这篇文章：<a href="https://github.com/biaochenxuying/blog/issues/45" target="_blank" rel="nofollow noopener noreferrer">GitHub 上能挖矿的神仙技巧 - 如何发现优秀开源项目</a></p>
<p>关于猫哥，大家可以看看我的年终总结 <a href="https://github.com/biaochenxuying/blog/issues/79" target="_blank" rel="nofollow noopener noreferrer">前端工程师的 2020 年终总结 - 乾坤未定，你我皆黑马</a></p>
<p>不知不觉，已经写到第 <strong>31</strong> 期了呢，往期精文请看下方宝藏仓库，请慎入！</p>
<blockquote>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub" target="_blank" rel="nofollow noopener noreferrer">github.com/FrontEndGit…</a></p>
</blockquote>
<p>微信搜 “<strong>前端GitHub</strong>”，回复 “<strong>电子书</strong>” 即可以获得 <strong>160</strong> 本前端精华书籍哦，猫哥 WX：<strong>CB834301747</strong> 。</p>
<p><strong>往期精文</strong></p>
<ul>
<li><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/18" target="_blank" rel="nofollow noopener noreferrer">Vue3 的学习教程汇总、源码解释项目、支持的 UI 组件库、优质实战项目</a></li>
</ul>
<ul>
<li>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/6" target="_blank" rel="nofollow noopener noreferrer">10 个 GitHub 上超火的前端面试项目，打造自己的加薪宝库！</a></p>
</li>
<li>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/7" target="_blank" rel="nofollow noopener noreferrer">10 个 GitHub 上超火的 CSS 技巧项目，找到写 CSS 的灵感！</a></p>
</li>
<li>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/9" target="_blank" rel="nofollow noopener noreferrer">11 个超火的前端必备在线工具，终于有时间上班摸鱼了</a></p>
</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec291e9db3924dffb86b6ce668a9d019~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            