
---
title: 'Fes.js for Vue3，简洁却不简单'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 18:12:23 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98cf5c167ac243b089138ba9402f37b7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Fes.js 是一套优秀的中后台前端解决方案。提供初始项目，开发调试，模拟接口，编译打包的命令行工具。内置布局，权限，数据字典，状态管理，存储，API 等多个模块。以约定，配置化，组件化的设计思想，让用户只需关心使用组件构造页面内容。基于 Vue.js，上手简单。经过多个项目中打磨，趋于稳定。</p>
<p>1.0 上线后收到了社区小伙伴们的良好建议，在此谢谢支持 Fes.js 的你们，希望本次升级给大家带来更多的帮助，期待未来共同创造更多功能。</p>
<p>我们需要开发的大部分前端应用的业务比较类似，比如中后台应用大多都是工作台、增删改查、权限、图表等。所以在开发一个前端应用之前，除了环境准备工作，还需要处理这些基础的业务逻辑。</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98cf5c167ac243b089138ba9402f37b7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果没有统一的规范或者框架，技术选型也要看开发人员的喜好，每个项目的准备工作都手动处理一遍，非常耗费时间。久而久之，当团队会出现多种技术栈，历史项目将越来越难维护。所以我们需要一套完整的解决方案，管理开发到部署整个流程，在问题发生前将其解决。</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a295c2cca6694170b443b0b8b8cd73fb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>Fes.js 2.0 做了哪些改进</strong></p>
<p>对于 1.0 本只支持 PC 应用、不易扩展等不足，我们在 2.0 版本重新设计了以插件机制为基础的可扩展架构。</p>
<p>重写了 90% 代码，Fes.js 2.0 以 <strong>Vue 3.0</strong> 和路由为基础，同时支持配置式路由和约定式路由，并以此进行功能扩展。匹配了覆盖编译时和运行时生命周期完善的插件体系，支持各种功能扩展和业务需求。</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5da05a0b9d420cad31f2731d683f68~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Fes.js 架构</p>
<p>Fes.js 把大家常用的技术栈封装成一个个插件进行整理，收敛到一起，让大家只用 Fes.js 就可以完成 80% 的日常工作。</p>
<p>支持插件和插件集，通过这张图应该很好理解到他们的关系，通过插件集我们把插件收敛依赖然后支持不同的业务类型。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1464237627634afaa43a07ed4e69f8d2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>插件和插件集</p>
<p><strong>Fes.js 2.0 的特点</strong></p>
<ul>
<li><strong>快速 Fast</strong></li>
</ul>
<p>内置了路由、开发、构建等，并且提供测试、布局、权限、国际化、状态管理、API 请求、数据字典、SvgIcon 等插件，可以满足大部分日常开发需求。</p>
<ul>
<li><strong>简单 Easy</strong></li>
</ul>
<p>基于 Vue.js 3.0，上手简单。贯彻“约定优于配置”思想，设计插件上尽可能用约定替代配置，同时提供统一的插件配置入口，简单简洁又不失灵活。提供一致性的 API 入口，一致化的体验，学习起来更轻松。</p>
<ul>
<li><strong>健壮 Strong</strong></li>
</ul>
<p>只需要关心页面内容，减少写 BUG 的机会！提供单元测试、覆盖测试能力保障项目质量。</p>
<ul>
<li><strong>可扩展</strong></li>
</ul>
<p>借鉴 Umi 实现了完整的生命周期和插件化机制，插件可以管理项目的编译时和运行时，能力均可以通过插件封装进来，在 Fes.js 中协调有序的运行。</p>
<ul>
<li><strong>面向未来</strong></li>
</ul>
<p>在满足需求的同时，我们也不会停止对新技术的探索。已使用 Vue3.0 来提升应用性能，已使用 webpack 5 提升构建性能和实现微服务，未来会探索vite等新技术。</p>
<ul>
<li><strong>令人愉悦</strong></li>
</ul>
<p>我们的主要重点是开发人员体验。我们喜欢 Fes.js，并且会不断改进框架，所以您也喜欢它！期待有吸引力的解决方案，描述性的错误消息，强大的默认值和详细的文档。如果有问题或疑问，我们有用的社区将为您提供帮助。</p>
<ul>
<li><strong>快速上手</strong></li>
</ul>
<p>基础配置：要有 10.13 或以上版本的 Node.js， 管理 npm 依赖推荐使用 yarn。</p>
<p>使用 yarn：</p>
<pre><code class="copyable"># 创建模板
yarn create 
# @fesjs/fes-app myapp``
# 安装依赖
yarn 
# 运行
yarn de 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 npm：</p>
<pre><code class="copyable">#创建模板
npx @fesjs/create-fes-app myapp
# 安装依赖
npm install 
# 运行
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://mp.weixin.qq.com/s?__biz=MjM5NDk2OTEzOA==&mid=2247484215&idx=1&sn=80afe48939a0a7812fc8a25beba7da24&chksm=a6fee06a9189697c0f42edaf612fb3a98ee7f773224fb704020407d9eba4f8f6762bb151e3c5&mpshare=1&scene=1&srcid=03225dF8jbkQVOX0gwFUSFIa&sharer_sharetime=1616388830932&sharer_shareid=967fd85e1954a2fdc667dd2f3ac3fe9c&version=3.1.2.2211&platform=win#rd" target="_blank" rel="nofollow noopener noreferrer">演示操作文章视频</a></p>
<p><strong>写在最后</strong></p>
<p>使用过程中，如果遇到困难，可到文档下查看解决方案；同时社区鼓励所有同学通过 Github 交流反馈，第一时间提交 issue。Fes.js 正在迅速发展中， 期待大家来一起玩耍！</p>
<ul>
<li>
<p>Github Issue</p>
<p><a href="https://github.com/WeBankFinTech/fes.js/issues" target="_blank" rel="nofollow noopener noreferrer">github.com/WeBankFinT.…</a></p>
</li>
<li>
<p>Github repo</p>
<p><a href="https://github.com/WeBankFinTech/fes.js/tree/vue3" target="_blank" rel="nofollow noopener noreferrer">github.com/WeBankFinT.…</a></p>
</li>
<li>
<p>使用文档</p>
<p><a href="https://winixt.gitee.io/fesjs/zh/" target="_blank" rel="nofollow noopener noreferrer">winixt.gitee.io/fesjs...</a></p>
</li>
<li>
<p>共建指南</p>
<p><a href="https://winixt.gitee.io/fesjs/zh/guide/contributing.html" target="_blank" rel="nofollow noopener noreferrer">winixt.gitee.io/fesjs...</a></p>
</li>
<li>
<p>项目联络</p>
<p>geniusWanc</p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            