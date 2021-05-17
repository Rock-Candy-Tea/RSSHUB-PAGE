
---
title: '_建议收藏_ Webpack 4+ 优秀学习资料合集'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b570d97c66994db19791387fff445fa4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 01:49:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b570d97c66994db19791387fff445fa4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>最近在学习 Webpack 源码，前前后后输出了 6 篇原理分析、工具分享类型的文章，过程中找到一些质量很高，值得一看的学习资料，所以熬夜整理了一波，希望对大家有帮助。</p>
<p>收录的规则很简单：</p>
<ul>
<li>内容适用于 Webpack 4 以上</li>
<li>不看点赞、阅读数，篇幅也可以很短，但内容必须详实，不能有明显偏误</li>
<li>不求量不求全，但求涵盖应用、原理、工具等维度，能够给各个层级的同学带来新的知识</li>
</ul>
<p>未来我会持续维护这份列表，非常欢迎社区小伙伴们评论或到我个人公众号 tecvan 投稿。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b570d97c66994db19791387fff445fa4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>关注公众号【Tecvan】，回复【2】，博主手把手带你进字节</strong></p>
<h1 data-id="heading-1">Webpack 基础</h1>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-2">使用 Webpack 开发 Web 应用</h2>
<ul>
<li><a href="https://zhaoda.net/webpack-handbook/index.html" target="_blank" rel="nofollow noopener noreferrer">介绍 | Webpack 中文指南</a>: 比较基础比较细的入门教程，很适合初学者</li>
<li><a href="https://juejin.cn/post/6844904031240863758#heading-0" target="_blank">2020年了,再不会webpack敲得代码就不香了(近万字实战)</a>: 掘金 3000 赞，非常详尽的应用指南，特别是最后性能优化那一块有很强的实践指导意义</li>
<li><a href="https://juejin.cn/post/6844903862898262024#heading-0" target="_blank">webpack4 的30个步骤打造优化到极致的 react 开发环境，如约而至</a>: 介绍 Webpack + React 开发环境搭建的方方面面，建议读者按图索骥</li>
<li><a href="https://www.freecodecamp.org/news/learn-webpack-for-react-a36d4cac5060/" target="_blank" rel="nofollow noopener noreferrer">How to use Webpack with React: an in-depth tutorial</a></li>
<li><a href="https://github.com/webpack-contrib/awesome-webpack" target="_blank" rel="nofollow noopener noreferrer">webpack-contrib/awesome-webpack</a></li>
<li><a href="https://github.com/petehunt/webpack-howto/blob/master/README-zh.md" target="_blank" rel="nofollow noopener noreferrer">petehunt/webpack-howto</a></li>
<li><a href="https://github.com/AriaFallah/WebpackTutorial/tree/master/zh-cn/part1" target="_blank" rel="nofollow noopener noreferrer">Webpack 初学者教学课程 Part 1 - Webpack 简介</a></li>
<li><a href="https://www.valentinog.com/blog/webpack/" target="_blank" rel="nofollow noopener noreferrer">A mostly complete guide to webpack 5 (2020)</a></li>
</ul>
<h2 data-id="heading-3">使用 Webpack 编写 npm 包</h2>
<ul>
<li><a href="https://www.loginradius.com/blog/async/write-a-javascript-library-using-webpack-and-babel/" target="_blank" rel="nofollow noopener noreferrer">Let's Write a JavaScript Library in ES6 using Webpack and Babel</a></li>
<li><a href="https://juejin.cn/post/6844904021291958286" target="_blank">现代前端库开发指南系列(二):使用 webpack 构建一个库</a></li>
<li><a href="https://github.com/cssmagic/blog/issues/56" target="_blank" rel="nofollow noopener noreferrer">[译] 基于 Webpack 和 ES6 打造 JavaScript 类库</a></li>
</ul>
<h2 data-id="heading-4">使用脚手架</h2>
<ul>
<li><a href="https://github.com/facebook/create-react-app" target="_blank" rel="nofollow noopener noreferrer">facebook/create-react-app</a>: 快速创建 React 应用脚手架工具</li>
<li><a href="https://github.com/vuejs/vue-cli" target="_blank" rel="nofollow noopener noreferrer">vuejs/vue-cli</a>: 快速创建 Vue 应用脚手架工具</li>
<li><a href="https://github.com/tjx666/awesome-chrome-extension-boilerplate" target="_blank" rel="nofollow noopener noreferrer">tjx666/awesome-chrome-extension-boilerplate</a> : 基于 React & TypeScript & Webpack 的 Chrome 扩展开发模板</li>
</ul>
<h2 data-id="heading-5">Hello World</h2>
<ul>
<li><a href="https://github.com/webpack/webpack/tree/master/examples" target="_blank" rel="nofollow noopener noreferrer">Webpack Examples</a>： Webpack 官方提供的示例，涵盖大多数特性的用法</li>
<li><a href="https://github.com/ruanyf/webpack-demos" target="_blank" rel="nofollow noopener noreferrer">ruanyf/webpack-demos</a>: 阮一峰老师的 Webpack 入门示例</li>
</ul>
<h1 data-id="heading-6">Webpack 进阶</h1>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-7">高级特性</h2>
<ul>
<li>Tree Shaking
<ul>
<li><a href="https://juejin.cn/post/6844903998634328072" target="_blank">Webpack 4 Tree Shaking 终极优化指南</a></li>
<li><a href="https://juejin.cn/post/6844903544756109319" target="_blank">Tree-Shaking性能优化实践 - 原理篇</a></li>
<li><a href="https://juejin.cn/post/6844903544760336398" target="_blank">Tree-Shaking性能优化实践 - 实践篇</a></li>
</ul>
</li>
<li>缓存
<ul>
<li><a href="https://juejin.cn/post/6847902218570432520" target="_blank">Webpack5 内置缓存方案探索</a></li>
</ul>
</li>
<li>Module Federation
<ul>
<li><a href="https://juejin.cn/post/6883408771322740743" target="_blank">webpack 5 ModuleFederationPlugin vue 项目初体验</a></li>
</ul>
</li>
</ul>
<h2 data-id="heading-8">如何编写 Loader</h2>
<ul>
<li><a href="https://juejin.cn/post/6950092728919130126" target="_blank">✏️ loader知识分享</a>: 展开讲解了 loader 的应用、种类、原理、执行方式等内容，质量很高</li>
<li><a href="https://zhuanlan.zhihu.com/p/360421184" target="_blank" rel="nofollow noopener noreferrer">【Webpack进阶】Loader深入解析</a>: 虽然阅读量跟赞都不多，但内容详尽，值得看一看</li>
<li><a href="https://juejin.cn/post/6844903555673882632" target="_blank">手把手教你撸一个 Webpack Loader</a></li>
<li><a href="https://github.com/joeyguo/blog/issues/4" target="_blank" rel="nofollow noopener noreferrer">如何开发一个 Webpack Loader ( 一 )</a></li>
</ul>
<h2 data-id="heading-9">如何编写 Plugin</h2>
<ul>
<li><a href="https://juejin.cn/post/6937125495439900685" target="_blank">Webpack 案例 -- vue-loader 原理分析</a>: 结合 vue-loader ，实例分析如何编写 Webpack 插件，特别分析了 vue-loader 如何解析一份 SFC 中的三种内容；如何复用 Webpack 配置中的其它 Loader</li>
</ul>
<ul>
<li><a href="https://github.com/lcxfs1991/blog/issues/1" target="_blank" rel="nofollow noopener noreferrer">如何写一个webpack插件（一）</a></li>
</ul>
<h2 data-id="heading-10">实现原理</h2>
<ul>
<li><a href="https://mp.weixin.qq.com/s/SbJNbSVzSPSKBe2YStn2Zw" target="_blank" rel="nofollow noopener noreferrer">[万字总结] 一文吃透 Webpack 核心原理</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/58151131" target="_blank" rel="nofollow noopener noreferrer">理解webpack原理，手写一个100行的webpack</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/30669007" target="_blank" rel="nofollow noopener noreferrer">Webpack HMR 原理解析</a> : 知乎高赞，非常详细的 Hot Module Replace 原理分析文档</li>
<li><a href="https://mp.weixin.qq.com/s/2ACQ0KwdB0ph3sqj2iK-uA" target="_blank" rel="nofollow noopener noreferrer">AST 与前端工程化实战</a></li>
</ul>
<h2 data-id="heading-11">面试</h2>
<ul>
<li><a href="https://juejin.cn/post/6844904094281236487#heading-0" target="_blank">「吐血整理」再来一打Webpack面试题</a>: 掘金高赞，以面试题视角概要解释 Webpack 中的各个知识点</li>
<li><a href="https://github.com/styopdev/webpack-interview-questions" target="_blank" rel="nofollow noopener noreferrer">Webpack interview questions</a></li>
<li><a href="https://juejin.cn/post/6844904007362674701" target="_blank">webpack 中那些最易混淆的 5 个知识点</a>: 讲解 Webpack 一些常用但容易被忽视的配置项，对面试和日常应用都很有启发</li>
</ul>
<h2 data-id="heading-12">系列连载</h2>
<ul>
<li><a href="https://www.zhihu.com/people/tec-van/posts" target="_blank" rel="nofollow noopener noreferrer">范文杰</a> - 源码解析 Webpack(私货)
<ul>
<li><a href="https://mp.weixin.qq.com/s/SbJNbSVzSPSKBe2YStn2Zw" target="_blank" rel="nofollow noopener noreferrer">[万字总结] 一文吃透 Webpack 核心原理</a></li>
<li><a href="https://mp.weixin.qq.com/s/tXkGx6Ckt9ucT2o8tNM-8w" target="_blank" rel="nofollow noopener noreferrer">[源码解读] Webpack 插件架构深度讲解</a></li>
<li><a href="https://mp.weixin.qq.com/s/QkXFOHNpL0PRQtCcWIaX-g" target="_blank" rel="nofollow noopener noreferrer">十分钟精进 Webpack：module.issuer 属性详解</a></li>
<li><a href="https://mp.weixin.qq.com/s/kr73Epnn6wAx9DH7KRVUaA" target="_blank" rel="nofollow noopener noreferrer">有点难的 webpack 知识点：Dependency Graph 深度解析</a></li>
<li><a href="https://mp.weixin.qq.com/s/dFrRY_ntUwmIOXzs8TYcFQ" target="_blank" rel="nofollow noopener noreferrer">有点难的知识点： Webpack Chunk 分包规则详解</a></li>
<li><a href="https://mp.weixin.qq.com/s/A0udBhvNoA0o-kX1B0rt9A" target="_blank" rel="nofollow noopener noreferrer">分享几个 Webpack 实用分析工具</a></li>
</ul>
</li>
</ul>
<ul>
<li><a href="https://webpack.wuhaolin.cn/" target="_blank" rel="nofollow noopener noreferrer">深入浅出 Webpack</a>: 应该是国内最详尽的 Webpack 书籍，从入门到应用，再到原理、工具都有介绍，非常值得入手</li>
<li><a href="https://gitmind.cn/app/doc/fac1c196e29b8f9052239f16cff7d4c7" target="_blank" rel="nofollow noopener noreferrer">Webpack 5 知识体系</a>: 一份拆解 Webpack 核心原理、架构、编译流程、loader、插件的在线知识图谱</li>
<li><a href="https://www.cnblogs.com/QH-Jimmy/default.html?page=6" target="_blank" rel="nofollow noopener noreferrer">随笔列表第6页 - 书生小龙 - 博客园</a>: 一系列 Webpack 源码分析文章，每篇文章都针对源码某一个特别小的点展开来讲</li>
<li><a href="https://survivejs.com/webpack/foreword/" target="_blank" rel="nofollow noopener noreferrer">Webpack Book from SurviveJS</a> : 一本深入浅出 Webpack 应用、原理、工具等主题的在线书籍</li>
<li><a href="https://www.cnblogs.com/dashnowords/p/9572755.html" target="_blank" rel="nofollow noopener noreferrer">史上最走心webpack4.0中级教程--配置之外你应该知道的事</a></li>
<li><a href="https://juejin.cn/user/3368559358523944" target="_blank">刘小夕</a> - 带你深度解锁 Webpack 系列
<ul>
<li><a href="https://juejin.cn/post/6844904079219490830" target="_blank">带你深度解锁Webpack系列(基础篇)</a></li>
<li><a href="https://juejin.cn/post/6844904084927938567" target="_blank">带你深度解锁Webpack系列(进阶篇)</a></li>
<li><a href="https://juejin.cn/post/6844904093463347208" target="_blank">带你深度解锁Webpack系列(优化篇)</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/team/6943816493473726472/posts" target="_blank">滴滴前端技术团队</a> - 比较硬核的 Webpack 原理分析系列文章，得静下心来慢慢看
<ul>
<li><a href="https://juejin.cn/post/6959449526197288996" target="_blank">你不知道的webpack静态文件生成过程</a></li>
<li><a href="https://juejin.cn/post/6844903925179482119" target="_blank">webpack系列之七-文件生成</a></li>
<li><a href="https://juejin.cn/post/6844903925171093518" target="_blank">webpack系列之七-附dependencyTemplates依赖模板</a></li>
<li><a href="https://juejin.cn/post/6844903864592777229" target="_blank">webpack系列之六chunk图生成</a></li>
<li><a href="https://juejin.cn/post/6844903830266576909" target="_blank">webpack系列之五module生成1</a></li>
<li><a href="https://juejin.cn/post/6844903780769595405" target="_blank">webpack系列之四loader详解1</a></li>
<li><a href="https://juejin.cn/post/6844903779712630797" target="_blank">webpack系列之三resolve</a></li>
<li><a href="https://juejin.cn/post/6844903750729990152" target="_blank">webpack系列之二Tapable</a></li>
<li><a href="https://juejin.cn/post/6844903726981840904" target="_blank">webpack系列之一总览</a></li>
</ul>
</li>
</ul>
<h1 data-id="heading-13">性能优化</h1>
<ul>
<li><a href="https://developers.google.com/web/fundamentals/performance/webpack/" target="_blank" rel="nofollow noopener noreferrer">Web Performance Optimization with Webpack</a></li>
<li><a href="https://medium.com/webpack/webpack-4-mode-and-optimization-5423a6bc597a" target="_blank" rel="nofollow noopener noreferrer">Webpack 4: mode and optimization</a></li>
<li><a href="https://medium.com/hackernoon/the-100-correct-way-to-split-your-chunks-with-webpack-f8a9df5b7758" target="_blank" rel="nofollow noopener noreferrer">The 100% correct way to split your chunks with Webpack</a></li>
<li><a href="https://github.com/iamakulov/awesome-webpack-perf" target="_blank" rel="nofollow noopener noreferrer">iamakulov/awesome-webpack-perf</a></li>
<li><a href="https://github.com/pigcan/blog/issues/1" target="_blank" rel="nofollow noopener noreferrer">Webpack 构建性能优化探索</a></li>
<li><a href="https://segmentfault.com/a/1190000005770042" target="_blank" rel="nofollow noopener noreferrer">开发工具心得：如何 10 倍提高你的 Webpack 构建效率</a></li>
<li><a href="https://github.com/lcxfs1991/blog/issues/15" target="_blank" rel="nofollow noopener noreferrer">webpack Performance: The Comprehensive Guide</a></li>
<li><a href="https://segmentfault.com/a/1190000006087638" target="_blank" rel="nofollow noopener noreferrer">彻底解决Webpack打包慢的问题</a></li>
<li><a href="https://segmentfault.com/a/1190000007891318" target="_blank" rel="nofollow noopener noreferrer">webpack 构建性能优化策略小结</a></li>
<li><a href="https://www.jianshu.com/p/a64735eb0e2b" target="_blank" rel="nofollow noopener noreferrer">彻底解决 webpack 打包文件体积过大</a>: 文章介绍 5 种常见的包体积优化方法，行文特别清晰</li>
<li><a href="https://juejin.cn/post/6844904071736852487" target="_blank">玩转 webpack，使你的打包速度提升 90%</a></li>
<li><a href="https://juejin.cn/post/6947890290896142350" target="_blank">ESM vs Webpack 面向高性能构建的探索</a></li>
</ul></div>  
</div>
            