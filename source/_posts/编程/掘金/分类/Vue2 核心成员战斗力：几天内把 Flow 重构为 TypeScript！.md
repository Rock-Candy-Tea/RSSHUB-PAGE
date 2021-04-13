
---
title: 'Vue2 核心成员战斗力：几天内把 Flow 重构为 TypeScript！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a7e267097ba448992cdaeb8a950ed87~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 22:15:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a7e267097ba448992cdaeb8a950ed87~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>事情起源于 4 月 7 号晚上，尤雨溪在推特说，Vue2 收到了一个将整个代码库迁移到 TypeScript 的 PR。</p>
<p><img alt="Evan's twitter" title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a7e267097ba448992cdaeb8a950ed87~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>去 Github 围观了一下<a href="https://github.com/vuejs/vue/pull/12001/commits" title="chore: move to typescript 这个 PR" target="_blank" rel="nofollow noopener noreferrer">chore: move to typescript 这个 PR</a>，基本上是 10w 行级别代码量的改动，把整个 Vue2 的代码库从原先的 flow 类型系统全部迁移到了 TypeScript，包括代码、构建系统、各种 lint 工具等等，恐怖的战斗力！</p>
<p><img alt="Github PR" title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b714be0a48104178b0caf8182bd539ef~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个 PR 的贡献者是 <a href="https://twitter.com/pikax_dev" title="Carlos Rodrigues" target="_blank" rel="nofollow noopener noreferrer">Carlos Rodrigues</a>，以下是他的自我介绍：</p>
<blockquote>
<p>Fullstack developer, interested in @vuejs, @dotnet and @nodejs.</p>
<p>Typescript 🧙‍♂️</p>
<p>Consultant 🕵️‍♂️</p>
</blockquote>
<p>全栈开发工程师，Vue.js、dotnet、Node.js 的爱好者。</p>
<p>TypeScript 魔法师 🧙‍♂️</p>
<p>顾问 🕵️‍♂️。</p>
<h2 data-id="heading-0">起源</h2>
<p>Vue2 为什么最开始选择 Flow 作为类型系统？其实在一个 2016 年的知乎问题<a href="https://www.zhihu.com/question/46397274/answer/101193678" title="Vue 2.0 为什么选用 Flow 进行静态代码检查而不是直接使用 TypeScript？" target="_blank" rel="nofollow noopener noreferrer">Vue 2.0 为什么选用 Flow 进行静态代码检查而不是直接使用 TypeScript？</a>里，尤雨溪已经详细说明了这个问题，以下是当时他的回答：</p>
<p>这个选择最根本的还是在于<strong>工程上成本和收益的考量</strong>。</p>
<p>Vue 2.0 本身在初期的快速迭代阶段是用 ES2015 写的，整个构建工具链也沿用了 Vue 1.x 的基于 ES 生态的一套（Babel, ESLint, Webpack, Rollup...)，全部换 TS 成本过高，短期内并不现实。</p>
<p>相比之下 Flow 对于已有的 ES2015 代码的迁入/迁出成本都非常低：</p>
<ol>
<li>可以一个文件一个文件地迁移，不需要一竿子全弄了。</li>
<li>Babel 和 ESLint 都有对应的 Flow 插件以支持语法，可以完全沿用现有的构建配置；</li>
<li>更贴近 ES 规范。除了 Flow 的类型声明之外，其他都是标准的 ES。万一哪天不想用 Flow 了，用 babel-plugin-transform-flow-strip-types 转一下，就得到符合规范的 ES。</li>
<li>在需要的地方保留 ES 的灵活性，并且对于生成的代码尺寸有更好的控制力 (rollup / 自定义 babel 插件）</li>
</ol>
<p>不过在 2018 年的时候，尤大更新了回答，<strong>真香定律</strong>再现：</p>
<p><img alt="真香" title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ffa8c371e104b0d93dc02a9ec7104ce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>也正因如此，Vue3 从一开始就选择了 TypeScript 作为类型系统。</p>
<h2 data-id="heading-1">困扰</h2>
<p>那么也许有人要问，Vue2 不是已经稳定了吗，何必再大费周章的把这么多代码迁移到 TypeScript 中呢？其实在之前 <a href="https://mp.weixin.qq.com/s?__biz=MzI3NTM5NDgzOA==&mid=2247495151&idx=1&sn=981920c2345fb3a70097b2a8dfa5ba66&chksm=eb07d596dc705c80b9db1bf62b0cc614b4f4012087e994ad178d5d91cfc3b9ad16f5c5ae72f0&token=349155749&lang=zh_CN#rd" target="_blank" rel="nofollow noopener noreferrer">Vue3 放弃 IE11 的 RFC</a> 中就有提及，之后还是会为 Vue 2.7 去加入一些和 Vue3 语法更类似的功能：</p>
<ul>
<li>把 <a href="https://github.com/vuejs/composition-api" title="@vue/composition-api plugin" target="_blank" rel="nofollow noopener noreferrer">@vue/composition-api plugin</a>合并进 Vue2。这会让使用 Composition API 开发的库同时支持 Vue2 和 Vue3。</li>
<li>单文件组件（SFC）中的<a href="https://github.com/vuejs/rfcs/pull/227" title="script setup" target="_blank" rel="nofollow noopener noreferrer">script setup</a>语法。</li>
<li><code>emits</code> 选项。</li>
<li>提升 TypeScript 类型支持。</li>
<li>在 Vite 中正式支持 Vue 2(目前通过<a href="https://github.com/underfin/vite-plugin-vue2" title="非官方插件" target="_blank" rel="nofollow noopener noreferrer">非官方插件</a>)</li>
</ul>
<p>而这些功能的开发和适配，如果继续用 flow 的话，势必会带来一些割裂的开发体验。一些已经用 TS 开发好的库，也没办法做代码的合并。事实上 Twitter 也有网友提出了这个问题，PR 作者进行了回答：</p>
<p><img alt="Why" title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95c0bd96e7f3463ebe00111571b2716e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>简单来说，就是为 Vue 2.7 的开发做准备，尤其是 composition-api 的代码合并。</p>
<h2 data-id="heading-2">具体内容</h2>
<p>先看作者对这次更新的简单描述：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e59a505132448cc8bfe73a2975830c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>代码格式化风格更新。</li>
<li>重构。</li>
<li>构建相关的改动。</li>
<li>代码库更新为 TypeScript 编写。</li>
</ol>
<p>值得一提的是，更换成 TS 之后，生成的代码体积都有少量的增加，作者猜测是 TS 加入了一些 runtime 的代码导致的：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25080ecb7371460698bea174b130d05c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>第一个 Commit 中，作者把代码的类型全部改成 .ts，移除文件开头 flow 的标记，并且把类型的语法全部替换成 TypeScript：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d990ce79836462f8b5500162b8cc456~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作者用 TS 的 <code>import type</code> 语法重构了类型导入，我个人也比较喜欢这样导入类型，更有助于区分导入的内容：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a414896e52c4262955234a377c9d085~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>单测工具的更新，以及 TS 的支持，利用 ts-loader 做编译：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45dc6a49e3094883b7f94ef4ee3f23a8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>RollUp 版本的一次大升级：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8223683a694a48339eba9318dd509e62~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>ESLint 也需要一些改动，使用 <code>@typescript-eslint/parser</code>，继承的一些推荐预设也改为 <code>@typescript-eslint/eslint-recommended</code>。</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13471feb51784fa1aba8ff07f186761d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>CI 中原本 flow 的类型检测，也改成使用 <code>tsc --noEmit</code> 做 TS 的类型检查。</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d90157deefd64f318a6f574904af347b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">评价</h2>
<p>可怕的是，这个如此庞大的 PR 是作者在几天内完成的，这战斗力简直是惊人。</p>
<p>Twitter 的评论中有人提问：“把如此巨大的代码库迁移到 TypeScript 需要多长时间？”</p>
<p>作者回答：在几小时内重命名文件，把 flow types 重写成 TS 类型并修复错误，之后的几天主要是忙构建、测试相关的工作。</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88209bcf4e80464c9b11640cb64b008e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对此，外国推友也表示很震惊：</p>
<blockquote>
<p>“你简直是个<strong>机器</strong>”：
<img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f4251807664c718de5f997b843f306~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>“他生活的宇宙中，1 小时可以顶我们 24 小时，或者也可能他是用<strong>光速</strong>在敲代码”
<img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dbec9dc55f94939a102f3157daf1396~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>CamiloR：“太棒了，很高兴核心团队之外，也有人付出如此多的努力”</p>
<p>Carlos：“我就是核心团队的成员 😆”
<img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2927cee6f5e44944ba2185247dd4ff34~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-4">总结</h2>
<p>不得不感叹，十倍工程师是真实存在的……这样一次巨型代码库迁移只花了短短几天时间，其实也体现出作者在 TS 生态、构建以及测试相关方面的熟悉程度。</p>
<p>感谢 Vue 核心团队成员们夸张的战斗力，给前端界带来这么优秀的框架而且持续迭代和优化。</p>
<p>Vue 3 虽然是未来，但是 Vue 2 也不会被放弃，迁移到 TS 以后的 Vue 2 具有更强的代码可移植性，一定会绽放出更多精彩。</p>
<h2 data-id="heading-5">感谢大家</h2>
<p>我是 ssh，目前就职于<a href="https://webinfra.org/bytedance/web-infra" target="_blank" rel="nofollow noopener noreferrer">字节跳动的 Web Infra 团队</a>，目前团队在北上广深杭都还缺人（尤其是北京）。</p>
<p>我组建了一个<a href="https://github.com/sl1673495/bytedance-apm-group/blob/main/README.md" target="_blank" rel="nofollow noopener noreferrer">氛围特别好的招聘社群</a>，大家在里面尽情的讨论面试相关的想法和问题，也欢迎你加入，随时投递简历给我。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            