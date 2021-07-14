
---
title: 'Vue3 + TypeScript 系列一 - Vue3 初体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a630a854ac34b048a3d59af4bc26345~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 03:55:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a630a854ac34b048a3d59af4bc26345~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a630a854ac34b048a3d59af4bc26345~tplv-k3u1fbpfcp-watermark.image" alt="一、Vue3 初体验.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">1. 认识 <code>Vue.js</code></h2>
<h3 data-id="heading-1">1.1 为什么要学习 <code>Vue</code></h3>
<p>如果从现实（找工作）的角度出发，学好 <code>Vue</code> 你可以找到一份满意的前端工作，而没有掌握 <code>Vue</code> 则很难找到一份满意的前端工作（需要补充的是，除了 <code>Vue</code>，现在不少岗位对“小程序”也有要求）。</p>
<h3 data-id="heading-2">1.2 <code>Vue</code> 的特点</h3>
<p><code>Vue</code>（读音 <code>/vjuː/</code>，类似于 <code>view</code>）是一套用于构建用户界面的渐进式 <code>JavaScript</code> 框架：</p>
<ul>
<li>全称是 <code>Vue.js</code> 或 <code>Vuejs</code>；</li>
<li>什么是渐进式框架呢？
<ul>
<li>渐进式框架意味着我们可以在项目中一点点地引入和使用 <code>Vue</code>，而不一定需要全部使用 <code>Vue</code> 来开发整个项目。你可以选择使用（或不使用） <code>Vue</code> 的某部分功能，你也可以只在项目的某个模块中使用 <code>Vue</code>。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-3">1.3 <code>Vue</code> 和 <code>React</code> 等框架的对比</h3>
<p>目前前端最流行的三大框架：<code>Vue</code>、<code>React</code>、<code>Angular</code>。</p>
<ul>
<li><code>Angular</code>：入门门槛较高，并且国内市场占有率较低。但不否认其本身是非常优秀的框架，它的很多设计思想与 <code>Node</code> 框架 <code>nest.js</code> 相似，而且它们基本上都要用 <code>TypeScript</code> 开发。</li>
<li><code>React</code>：国内外的市场占有率都较高。作为前端工程师也是必须学习的一个框架。大公司大项目在以前也更倾向于使用 <code>React</code> 开发，因为相对来说 <code>React</code> 可能更加的灵活，一些 <code>Vue2</code> 可能没法做的场景 <code>React</code>则可以做（当然，现在 <code>Vue</code> 从 <code>2</code> 版本升级到 <code>3</code> 版本后，有了 <code>Composition API</code>，也非常灵活了）。</li>
<li><code>Vue</code>：在国内市场占有率最高，几乎所有的前端岗位都会对 <code>Vue</code> 有要求。</li>
</ul>
<h4 data-id="heading-4">1.3.1 框架数据对比</h4>
<h5 data-id="heading-5">1.3.1.1 <code>Google</code> 指数</h5>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83806bed3622430fa90bf00a19fcde53~tplv-k3u1fbpfcp-watermark.image" alt="框架数据对比-Google 指数" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">1.3.1.2 百度指数</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed409acaeac94c27902d0a48e95d4b6d~tplv-k3u1fbpfcp-watermark.image" alt="框架数据对比-百度指数" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">1.3.1.3 <code>npm</code> 下载量</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b6c27a11b7b460b9a8234254475ae8b~tplv-k3u1fbpfcp-watermark.image" alt="框架数据对比-npm 下载量" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-8">1.3.1.4 <code>GitHub</code></h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa3a13dda28f44808cbcfa8ab3d5c59a~tplv-k3u1fbpfcp-watermark.image" alt="框架数据对比-GitHub" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">1.3.2 谁是最好的前端框架</h4>
<p>这里不给出结论，因为就像人们争论谁是世界上最好的语言一样，争论这个问题没有意义。</p>
<p>但我们不妨从现实的角度先分析一下，学习哪门语言更容易找工作（哪门语言市场占有率更高）？</p>
<ul>
<li>找后端的工作：优先推荐 <code>Java</code>，其次是 <code>Go</code>，再次是 <code>Node</code>（<code>JavaScript</code>），可能不推荐 <code>PHP</code>、<code>C#</code>；</li>
<li>找前端的工作：优先推荐 <code>JavaScript</code>（<code>TypeScript</code>），其次是 <code>Flutter</code>，再次是 <code>Android</code>（<code>Java</code>、<code>Kotlin</code>）、<code>iOS</code>（<code>OC</code>、<code>Swift</code>）；</li>
<li>其它方向：算法工程师、游戏开发、人工智能等等。</li>
</ul>
<p>那么，就前端来说，学习了 <code>HTML</code>、<code>CSS</code>、<code>JavaScript</code> 之后，哪一个框架更容易找到工作？</p>
<ul>
<li>如果去国外找工作，优先推荐 <code>React</code>，其次是 <code>Vue</code> 和 <code>Angular</code>，不推荐 <code>jQuery</code> 了；</li>
<li>如果在国内找工作，优先推荐、必须学习 <code>Vue</code>，其次是 <code>React</code>，再次是 <code>Angular</code>，不推荐 <code>jQuery</code> 了。</li>
</ul>
<h3 data-id="heading-10">1.4 学习 <code>Vue2</code> 还是 <code>Vue3</code></h3>
<ul>
<li>对于已经掌握 <code>Vue2</code> 的同学来说，直接学习 <code>Vue3</code> 中相关的内容即可；</li>
<li>对于没有学过 <code>Vue2</code> 的同学，直接学习 <code>Vue3</code> 就行了。</li>
</ul>
<p>《程序员》：<code>Vue 3</code> 版本兼容 <code>2.x</code>，对于想要学习 <code>Vue</code> 的开发者而言，时常在纠结是从 <code>Vue2</code> 开始学基础还是直接学 <code>Vue3</code>，对此，你有着什么样的建议？</p>
<p>尤雨溪（<code>Vue</code> 作者）：直接学 <code>Vue 3</code>就行了，基础概念是一模一样的。</p>
<h3 data-id="heading-11">1.5 目前需要学习 <code>Vue3</code> 吗</h3>
<p><code>2020</code> 年 <code>9</code> 月 <code>18</code> 日，万众期待的 <code>Vue3</code> 终于发布了正式版，命名为 “<code>One Piece</code>”。</p>
<ul>
<li>它带来了很多新的特性：<strong>更小的体积</strong>、<strong>更好的性能</strong>、<strong>更优秀的 <code>API</code> 设计</strong>、<strong>更好的 <code>TypeScript</code> 集成</strong>；</li>
<li>在 <code>Vue3</code> 刚刚发布时，很多人跃跃欲试，想要尝试 <code>Vue3</code> 的各种新特性，这时我们用 <code>Vue3</code> 写写 <code>demo</code> 练习是没有问题的，但真正在实际业务项目中使用 <code>Vue3</code> 还需要一个相对过程；</li>
<li>包括 <code>Vue3</code> 的进一步稳定、社区更多 <code>Vue3</code> 相关的插件、组件库的支持和完善（因为生态需要时间，生态里的工具、周边以及库都需要时间去兼容，<code>Vue3</code> 的一些新用法也需要时间去沉淀）。</li>
</ul>
<p><strong>那么现在是否是学习 <code>Vue3</code> 的时间呢？</strong></p>
<ul>
<li><strong>答案是肯定的</strong>；</li>
<li>首先 <code>Vue3</code> 在经过一系列的更新和维护后，已经趋于稳定，并且尤雨溪之前在 <code>VueConf China 2021</code> 上也宣布会在<strong>今年（2021）第二季度</strong>将 <code>Vue3</code> 作为默认版本（现在的时间是 <code>7</code> 月 <code>10</code> 号，<code>npm</code> 还没有默认安装 <code>Vue3</code>，文档也还没有默认指向 <code>v3</code> 文档）。</li>
<li>社区经过一段时间的沉淀后，也更加完善了，包括 <code>Ant Design Vue</code>、<code>Element Plus</code> 都提供了对 <code>Vue3</code> 的支持，所以很多公司目前新的项目都已经在使用 <code>Vue3</code> 来进行开发了。</li>
<li>并且在面试中，也会问到 <code>Vue3</code>、<code>Vite2</code> 工具相关的问题。</li>
</ul>
<h3 data-id="heading-12">1.6 <code>Vue3</code> 带来的变化</h3>
<h4 data-id="heading-13">1.6.1 源码</h4>
<ul>
<li>源码通过 <code>monorepo</code> 的形式来管理
<ul>
<li><code>mono</code>：单个；</li>
<li><code>repo</code>：<code>repository</code>（仓库）；</li>
<li>就是将许多项目的代码存储在同一个仓库中；</li>
<li>这样做可以使得多个包本身相互独立，可以有自己的功能逻辑、单元测试等，同时又在同一个仓库下，方便管理；</li>
<li>而且模块划分得更加清晰，可维护性、可扩展性更强。</li>
</ul>
</li>
<li>源码使用 <code>TypeScript</code> 进行了重写
<ul>
<li>在 <code>Vue2.x</code> 时，<code>Vue</code> 使用 <code>Flow</code> 进行类型检测；</li>
<li>现在到了 <code>Vue3.x</code> ，<code>Vue</code> 的源码全部使用 <code>TypeScript</code> 进行重构，并且 <code>Vue</code> 本身对 <code>TypeScript</code> 的支持也更好了。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-14">1.6.2 性能</h4>
<ul>
<li>使用 <code>Proxy</code> 进行数据劫持
<ul>
<li>在 <code>Vue2.x</code> 的时候，<code>Vue2</code> 是使用 <code>Object.defineProperty</code> 来劫持数据的 <code>getter</code> 和 <code>setter</code> 方法的；</li>
<li>这种方式一直存在一个缺陷：当给对象添加或删除属性时，无法劫持和监听；</li>
<li>所以在 <code>Vue2.x</code> 的时候，不得不提供一些特殊的 <code>API</code>，比如 <code>$set</code>、<code>$delete</code>，事实上都是一些 <code>hack</code> 方法，增加了开发者学习新的 <code>API</code> 的成本；</li>
<li>而在 <code>Vue3.x</code> 开始，<code>Vue</code> 使用 <code>Proxy</code> 来实现数据的劫持，该 <code>API</code> 的用法和相关原理后续会讲到；</li>
</ul>
</li>
<li>删除了一些不必要的 <code>API</code>
<ul>
<li>移除了实例上的 <code>$on</code>、<code>$off</code> 和 <code>$once</code>；</li>
<li>移除了一些特性：<code>filters</code>（过滤器）、<code>inline template attribute</code>（内联模板属性）等；</li>
</ul>
</li>
<li>编译方面的优化
<ul>
<li>生成 <code>Block Tree</code>；</li>
<li><code>Slot</code> 编译优化；</li>
<li><code>diff</code> 算法优化；</li>
</ul>
</li>
</ul>
<h4 data-id="heading-15">1.6.3 新的 <code>API</code></h4>
<ul>
<li>由 <code>Options API</code> 到 <code>Composition API</code>
<ul>
<li>在 <code>Vue2.x</code> 的时候，我们会通过 <code>Options API</code> 来描述组件对象；</li>
<li><code>Options API</code> 包括 <code>props</code>、<code>data</code>、<code>computed</code>、<code>watch</code>、生命周期事件、<code>methods</code> 等等选项；</li>
<li><code>Options API</code> 存在比较大的问题是多个逻辑可能是在不同的地方：
<ul>
<li>比如 <code>created</code> 中会使用 <code>methods</code> 中的某个方法来修改 <code>data</code> 中的数据，代码的内聚性非常差；</li>
</ul>
</li>
<li>而 <code>Composition API</code> 可以将相关联的代码放到同一处进行处理，而不需要分散在多个 <code>Options</code> 中，也就不用再在多个 <code>Options</code> 之间寻找了；</li>
</ul>
</li>
<li><code>Hooks</code> 函数增加代码的复用性
<ul>
<li>在 <code>Vue2.x</code> 的时候，我们通常通过 <code>mixins</code> 在多个组件之间共享逻辑；</li>
<li>但是有一个很大的缺陷就是 <code>mixins</code> 也是由一大堆的 <code>Options</code> 组成的，多个 <code>mixins</code> 间会存在命名冲突的问题；</li>
<li>到了 <code>Vue3.x</code>，我们可以通过 <code>Hook</code> 函数将一部分独立的逻辑抽取出去，并且它们还可以做到是响应式的；</li>
<li>具体的好处，会在后续演练和讲解（包括原理）；</li>
</ul>
</li>
</ul>
<h2 data-id="heading-16">2. <code>Vue</code> 的安装</h2>
<p>简单认识了 <code>Vue</code> 之后，如何使用它呢？</p>
<p>首先，我们要知道，<code>Vue</code> 的本质就是一个 <code>JavaScript</code> 库。刚开始我们不需要把它想象的非常复杂，只需把它理解成一个已经帮助我们封装好的库，在项目中我们可以引入并使用它。</p>
<p>使用 <code>Vue</code> 之前，我们需要先安装 <code>Vue</code>，安装 <code>Vue</code> 这个 <code>JavaScript</code> 库的方式有以下 <code>4</code> 种：</p>
<ul>
<li>在页面中通过 <code>CDN</code> 的方式引入；</li>
<li>下载 <code>Vue</code> 的 <code>JavaScript</code> 文件后在页面中手动引入；</li>
<li>通过 <code>npm</code> 包管理工具安装（讲 <code>Webapck</code> 时再讲）；</li>
<li>直接安装 <code>Vue CLI</code>，安装 <code>Vue CLI</code> 时会安装 <code>Vue</code>（讲完 <code>Webpack</code> 后讲脚手架时再讲，后续我们通过 <code>Vue CLI</code> 创建项目并使用 <code>Vue</code>）；</li>
</ul>
<h3 data-id="heading-17">2.1 方式一、<code>CDN</code> 引入</h3>
<ul>
<li>什么是 <code>CDN</code> 呢？<code>CDN</code> 即内容分发网络（<code>Content Delivery Network</code> 或 <code>Content Distribution Network</code>，缩写：<code>CDN</code>）
<ul>
<li>它是指通过<strong>相互连接的网络系统</strong>，利用<strong>最靠近</strong>每位用户的服务器；</li>
<li>更快、更可靠地将<strong>音乐、图片、视频、应用程序及其它文件</strong>发送给用户；</li>
<li>来提供<strong>高性能、可扩展性及低成本</strong>的网络内容传递给用户。</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6359771822d14bbcb1512c3b97532e3e~tplv-k3u1fbpfcp-watermark.image" alt="未使用 CDN 服务器" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4f7d7bedf2e41a798a937f11ee08ac1~tplv-k3u1fbpfcp-watermark.image" alt="使用 CDN 服务器" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>常用的 <code>CDN</code> 服务器可以分为两种：
<ul>
<li>自己的 <code>CDN</code> 服务器：需要购买自己的 <code>CDN</code> 服务器，目前华为、阿里、腾讯、亚马逊、谷歌等平台上都可以购买 <code>CDN</code> 服务器；</li>
<li>开源的 <code>CDN</code> 服务器：国际上使用比较多的是 <code>unpkg</code>、<code>JSDelivr</code>、<code>cdnjs</code>；</li>
</ul>
</li>
<li>通过 <code>CDN</code> 引入 <code>Vue</code> 的最新版本：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中访问 <code>https://unpkg.com/vue@next</code> 这一 <code>CDN</code> 地址也可以看到 <code>Vue</code> 打包后没有经过压缩的源代码（在开发阶段建议用没有经过压缩的代码，这样可以看到更多细节）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24c9219fb45b44ad99b321e7d346e5ce~tplv-k3u1fbpfcp-watermark.image" alt="通过 CDN 引入的 Vue 源码" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，该文件的最上面定义了一个全局变量 <code>Vue</code>（其实是一个对象），因此，我们接下来就是通过这个全局变量 <code>Vue</code> 来使用 <code>Vue</code> 了。</p>
<ul>
<li><code>Hello Vue</code> 案例的实现：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 4. 用来给 app 对象挂载的元素（通常为 div，并且设置 id 为 app，但也可以使用其它元素和其它
选择器） --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!-- 1. CDN 引入 Vue --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-comment">// 3. 在 template 属性中声明后续 createApp 函数返回的 app 对象中要显示的内容</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">'<h2>Hello Vue</h2>'</span>
  &#125;;
  <span class="hljs-comment">// 2. 调用全局变量 Vue 中的 createApp 函数，</span>
  <span class="hljs-comment">// 该函数要求传入一个对象，而其返回值也是一个对象</span>
  <span class="hljs-keyword">const</span> app = Vue.createApp(obj);
  <span class="hljs-comment">// 5. 将 app 对象挂载到 id 为 app 的 HTML 元素上（即告诉 app 对象要在哪里显示）</span>
  <span class="hljs-comment">// 这里我们不需要通过 document.querySelector 方法手动去拿目标元素，只需要传入要匹配的选择器的 </span>
  <span class="hljs-comment">// DOM 字符串即可，因为 Vue 内部会根据这里传入的字符串帮助我们用 document.querySelector 去找到</span>
  <span class="hljs-comment">// 目标元素（源码中对应的代码：packages/runtime-dom/src/index.ts -> createApp -> app.mount -> </span>
  <span class="hljs-comment">// normalizeContainer(containerOrSelector) -> if (isString(container)) -> </span>
  <span class="hljs-comment">// document.querySelector(container)）</span>
  app.mount(<span class="hljs-string">'#app'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8ead681217b424983db0a43246ee3c7~tplv-k3u1fbpfcp-watermark.image" alt="CDN 引入并使用 Vue" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结一下上述案例使用 <code>Vue</code> 的 <code>5</code> 个步骤：</p>
<ol>
<li>引入 <code>Vue</code>；</li>
<li>创建一个包含模板的对象；</li>
<li>通过全局变量 <code>Vue</code> 调用 <code>createApp</code> 方法（对象中的函数称之为方法）并传入该对象；</li>
<li>返回的对象调用 <code>mount</code> 方法把自己挂载到某个元素上；</li>
<li>页面上显示出模板内容；</li>
</ol>
<h3 data-id="heading-18">2.2 方式二、下载后引入</h3>
<p>下载 <code>Vue</code> 的源码，可以直接打开 <code>CDN</code> 的链接：</p>
<ul>
<li>打开链接（<a href="https://link.juejin.cn/?target=https%3A%2F%2Funpkg.com%2Fvue%40next" target="_blank" rel="nofollow noopener noreferrer" title="https://unpkg.com/vue@next" ref="nofollow noopener noreferrer">unpkg.com/vue@next</a> ），复制其中所有的代码；</li>
<li>创建一个新的文件，如 <code>vue.js</code>，将复制的代码粘贴进该文件中。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c49b4778264940f0b5d4c7d4268cd42a~tplv-k3u1fbpfcp-watermark.image" alt="通过 CDN 链接获取 Vue 源码" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，就可以（比如在“<code>本地引入.html</code>”中）通过 <code>script</code> 标签引入刚才创建的新文件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>你好啊，Vue3</code> 案例的实现：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  Vue.createApp(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'<h2>你好啊，Vue3</h2>'</span>
  &#125;).mount(<span class="hljs-string">'#app'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94debef87ac34fc4affd27b8e2bffdb1~tplv-k3u1fbpfcp-watermark.image" alt="下载后引入并使用 Vue" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">3. 计数器案例</h2>
<p>下面我们来实现一个计数器的案例：</p>
<ul>
<li>点击 <code>+1</code> 按钮，页面内容会显示数字 <code>+1</code>；</li>
<li>点击 <code>-1</code> 按钮，页面内容会显示数字 <code>-1</code>；</li>
</ul>
<p>可以选择很多种方式来实现，我们这里选择用<strong>原生的方式</strong>和 <strong><code>Vue</code> 的方式</strong>分别实现，并比较两者的不同。</p>
<h3 data-id="heading-20">3.1 原生实现</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"counter"</span>></span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 1. 获取展示当前计数的元素和两个按钮元素</span>
  <span class="hljs-keyword">const</span> counterEl = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.counter'</span>);
  <span class="hljs-keyword">const</span> incrementBtnEl = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.increment'</span>);
  <span class="hljs-keyword">const</span> decrementBtnEl = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.decrement'</span>);

  <span class="hljs-comment">// 2. 定义一个变量，用来记录当前计数</span>
  <span class="hljs-keyword">let</span> counter = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 3. 为展示当前计数的元素内容赋初值</span>
  counterEl.innerHTML = counter;

  <span class="hljs-comment">// 4. 为按钮添加点击事件的监听</span>
  incrementBtnEl.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
    counter++;
    counterEl.innerHTML = counter;
  &#125;);
  decrementBtnEl.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
    counter--;
    counterEl.innerHTML = counter;
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3bce1c6d68a4de299891ceffdd85555~tplv-k3u1fbpfcp-watermark.image" alt="计数器-原生实现" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">3.2 <code>Vue</code> 实现</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!-- 引入 Vue --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  Vue.createApp(&#123;
    <span class="hljs-comment">// 模板内容有点多，写在一行不好写，可以采用 ES6 新增的模板字面量定义字符串，这样就能保留换行字符，</span>
    <span class="hljs-comment">// 可以跨行定义字符串了。</span>
    <span class="hljs-comment">// 下面模板内容的最外层包了个 div，这是 Vue2 的要求，而到了 Vue3 中，可以去掉这个 div。</span>
    <span class="hljs-comment">// Vue3 的 template 最外层根元素（如下面的 div）可以不加（Vue2 必须要加一层根元素进行包裹，</span>
    <span class="hljs-comment">// 否则会报错：Component template should contain exactly one root element. If you are</span>
    <span class="hljs-comment">// using v-if on multiple elements, use v-else-if to chain them instead.）。</span>
    <span class="hljs-comment">// 模板中可以通过“Mustache”语法（双大括号）使用下面 data 函数属性返回对象中的属性；</span>
    <span class="hljs-comment">// 模板中可以通过“@click”绑定点击事件，与下面 methods 对象中的属性进行绑定。</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
      <div>
        <h2>&#123;&#123; message &#125;&#125;</h2>
        <h2>&#123;&#123; counter &#125;&#125;</h2>
        <button @click="increment">+1</button>
        <button @click="decrement">-1</button>
      </div>
    `</span>,
    <span class="hljs-comment">// createApp 函数需要传入的是一个对象，对象是可以有多个属性的，</span>
    <span class="hljs-comment">// 而 Vue 中规定了，这里还可以有 data 属性。</span>
    <span class="hljs-comment">// Vue3 中 data 属性对应的值需要是一个函数并返回一个对象，而不允许直接传对象，</span>
    <span class="hljs-comment">// 否则会报错：Uncaught TypeError: dataFn.call is not a function（Vue2 中 data 可以直接传一个对象）</span>
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-comment">// data 函数返回的对象中可以定义任意属性；</span>
        <span class="hljs-comment">// 它们都会被加入到 Vue 的响应式系统中，所以都是响应式的；</span>
        <span class="hljs-comment">// 它们都可以在模板中使用</span>
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello World'</span>,
        <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
      &#125;;
    &#125;,
    <span class="hljs-comment">// 还可以有 methods 属性</span>
    <span class="hljs-comment">// methods 属性对应一个对象，里面可以定义各种各样的方法</span>
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-comment">// 定义“加一”操作的方法（ES6 之前对象中定义方法的语法）</span>
      <span class="hljs-attr">increment</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击了 +1'</span>);
        <span class="hljs-comment">// methods 中可以通过 this 拿到 data 中的数据(本质上拿到的是 Proxy)</span>
        <span class="hljs-built_in">this</span>.counter++;
      &#125;,
      <span class="hljs-comment">// 定义“减一”操作的方法（ES6 对象中定义方法的语法糖，即简写形式）</span>
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击了 -1'</span>);
        <span class="hljs-built_in">this</span>.counter--;
      &#125;
    &#125;
  &#125;).mount(<span class="hljs-string">'#app'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe767a92f797469997debed7afb791b9~tplv-k3u1fbpfcp-watermark.image" alt="计数器-Vue 实现" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还可以对上述代码做一点抽取（<code>template</code> 的抽取 <code>4.1.1</code> 节会详细讲），修改如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> App = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#my-app'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello World'</span>,
        <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
      &#125;;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-attr">increment</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击了 +1'</span>);
        <span class="hljs-built_in">this</span>.counter++;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击了 -1'</span>);
        <span class="hljs-built_in">this</span>.counter--;
      &#125;
    &#125;
  &#125;;

  Vue.createApp(App).mount(<span class="hljs-string">'#app'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">3.3 命令式和声明式</h3>
<p>我们会发现，原生开发和 <code>Vue</code> 开发的模式和特点是完全不同的，这里其实涉及到<strong>两种不同的编程范式</strong>：</p>
<ul>
<li><strong>命令式编程</strong>和<strong>声明式编程</strong>；</li>
<li><strong>命令式编程</strong>关注的是 <strong>“怎么做”（<code>how to do</code>）</strong>；<strong>声明式编程</strong>关注的是 <strong>“做什么”（<code>what to do</code>）</strong>，<strong>”怎么做“（<code>how to do</code>）的过程交给框架（机器）完成</strong>。</li>
</ul>
<p>在原生的实现过程中，我们是如何操作的呢？</p>
<ul>
<li>我们每完成一个操作，都需要通过 <strong><code>JavaScript</code> 编写一条代码</strong>，来给<strong>浏览器一个指令</strong>；</li>
<li>这样的编写代码的过程，我们称之为<strong>命令式编程</strong>；</li>
<li>在早期的原生 <code>JavaScript</code> 和 <code>jQuery</code> 开发中，我们都是通过这种命令式的方式编写代码的；</li>
</ul>
<p>在 <code>Vue</code> 的实现过程中，我们是如何操作的呢？</p>
<ul>
<li>我们会在 <code>createApp</code> 传入的对象中声明需要的内容：模板（<code>template</code>）、数据（<code>data</code>）、方法（<code>methods</code>），剩下的具体操作则由 <code>Vue</code> 帮助我们完成；</li>
<li>这样编写代码的过程，我们称之为<strong>声明式编程</strong>；</li>
<li>目前 <code>Vue</code>、<code>React</code>、<code>Angular</code> 的编程模式，都是这种声明式。</li>
</ul>
<h3 data-id="heading-23">3.4 <code>MVVM</code> 模型</h3>
<ul>
<li>
<p><code>MVC</code> 和 <code>MVVM</code> 都是一种<strong>软件的体系结构</strong>：</p>
<ul>
<li><code>MVC</code> 是 <code>Model-View-Controller</code> 的简称，是前期使用非常广泛的框架的架构模式，比如 <code>iOS</code>、前端；</li>
<li><code>MVVM</code> 是 <code>Model-View-ViewModel</code> 的简称，是目前非常流行的架构模式；</li>
</ul>
</li>
<li>
<p>通常情况下，我们也称 <code>Vue</code> 是一个 <code>MVVM</code> 的框架</p>
<ul>
<li><code>Vue</code> 官网其实有说明：“虽然没有完全遵循 <code>MVVM</code> 模型，但是 <code>Vue</code> 的设计也受到了它的启发”。</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59ebec6bf8a849b1933de04acf2aa5a7~tplv-k3u1fbpfcp-watermark.image" alt="MVVM 软件架构模式" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前面原生实现计数器的代码就可以按照 <code>MVC</code> 的软件体系结构进行划分（虽然划分得不是很清晰）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec18a0b98a70460292ae5015bf9ccdab~tplv-k3u1fbpfcp-watermark.image" alt="MVC 架构模式" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而前面 <code>Vue</code> 实现计数器的代码则是按照 <code>MVVM</code> 的软件架构模式编写的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4554afdb14d341d4b07e01a6230873b6~tplv-k3u1fbpfcp-watermark.image" alt="MVVM 架构模式" loading="lazy" referrerpolicy="no-referrer"></p>
<p>综上，计数器的原生实现可以看成是一个 <code>MVC</code> 架构模式的命令式编程，计数器的 <code>Vue</code> 实现可以看成是一个 <code>MVVM</code> 架构模式的声明式编程。</p>
<h2 data-id="heading-24">4. <code>template</code>、<code>data</code>、<code>methods</code> 属性详解</h2>
<p>在使用 <code>createApp</code> 的时候，我们传入了<strong>一个对象</strong>，下面我们详细解析一下之前传入的属性分别代表什么含义。</p>
<h3 data-id="heading-25">4.1 <code>template</code> 属性</h3>
<p><code>template</code> 属性表示的是 <code>Vue</code> 需要帮助我们渲染的模板信息。</p>
<ul>
<li>目前我们看到它里面有<strong>很多的 <code>HTML</code> 标签</strong>，这些标签会<strong>替换掉</strong>我们挂载到的元素（我们这里是 <code>id</code> 为 <code>app</code> 的 <code>div</code>）的 <code>innerHTML</code>；
<ul>
<li>源码中对应的代码：<code>packages/runtime-dom/src/index.ts</code> -> <code>createApp</code> -> <code>app.mount</code> -> <code>container.innerHTML = ''</code>，<code>Vue</code> 会在挂载前清空里面的内容；</li>
</ul>
</li>
<li>模板中有一些<strong>奇怪的语法</strong>，比如 <code>&#123;&#123;&#125;&#125;</code>、<code>@click</code>，这些都是<strong>模板特有的语法</strong>，我们会在后面讲到；</li>
</ul>
<p>但是这个模板的写法<strong>有点别扭</strong>，并且 <code>IDE</code> 很有可能<strong>没有任何提示</strong>，有碍我们编程的效率。</p>
<h4 data-id="heading-26">4.1.1 <code>template</code> 写法</h4>
<p>好消息是，<code>Vue</code> 为我们提供了另外两种方式来编写 <code>template</code>：</p>
<ul>
<li>方式一：使用 <code>script</code> 标签，同时标记它的类型为 <code>x-template</code>，设置 <code>id</code>；</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"x-template"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-app"</span>></span><span class="handlebars"><span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span></span><span class="hljs-template-variable">&#123;&#123; <span class="hljs-name">message</span> &#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span></span><span class="hljs-template-variable">&#123;&#123; <span class="hljs-name">counter</span> &#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方式二：使用任意标签（<strong>通常是 <code>template</code> 标签，因为它不会被浏览器渲染</strong>），设置 <code>id</code>；
<ul>
<li><code>HTML</code> 内容模板（<code><template></code>）元素是一种用于保存 <code>HTML</code> 的机制，它不会在页面加载完后立即被渲染（呈现），但随后在运行时使用 <code>JavaScript</code> 期间可能会被实例化。<sup id="user-content-fnref-1"><a href="https://juejin.cn/post/6984378114902065182#fn-1" class="footnote-ref" target="_blank" title="#fn-1">1</a></sup></li>
</ul>
</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这个时候，在给 <code>createApp</code> 函数传入的对象中，我们需要传入的 <code>template</code> 以 <code>#</code> 开头
<ul>
<li>如果字符串是以 <code>#</code> 开始，那么它将被用作 <code>querySelector</code>，并且使用匹配元素的 <code>innerHTML</code> 作为模板字符串。</li>
</ul>
</li>
</ul>
<p>方式一完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"x-template"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-app"</span>></span><span class="handlebars"><span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span></span><span class="hljs-template-variable">&#123;&#123; <span class="hljs-name">message</span> &#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span></span><span class="hljs-template-variable">&#123;&#123; <span class="hljs-name">counter</span> &#125;&#125;</span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  Vue.createApp(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#my-app'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello World'</span>,
        <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
      &#125;;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-attr">increment</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.counter++;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.counter--;
      &#125;
    &#125;
  &#125;).mount(<span class="hljs-string">'#app'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式二完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"my-app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  Vue.createApp(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#my-app'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello World'</span>,
        <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
      &#125;;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-attr">increment</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.counter++;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.counter--;
      &#125;
    &#125;
  &#125;).mount(<span class="hljs-string">'#app'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开发中，推荐使用 <code><template></code> 的方式编写模板，因为有代码提示和代码高亮。</p>
<h3 data-id="heading-27">4.2 <code>data</code> 属性</h3>
<ul>
<li><code>data</code> 属性需要传入一个函数，并且该函数需要返回一个对象：
<ul>
<li>在 <code>Vue2.x</code> 的时候，也可以传入一个对象（仅就 <code>Vue</code> 实例而言，如果是组件的 <code>data</code>，则只接受 <code>function</code>）；</li>
<li>在 <code>Vue3.x</code> 的时候，必须传入一个函数，否则会直接在浏览器中报错；</li>
</ul>
</li>
<li><code>data</code> 中返回的对象会被 <strong><code>Vue</code> 的响应式系统劫持</strong>，之后<strong>对该对象的访问或修改</strong>都会在劫持中被处理；
<ul>
<li>所以我们在 <code>template</code> 中通过 <code>&#123;&#123; counter &#125;&#125;</code> 访问 <code>counter</code>，可以从对象中获取到数据；</li>
<li>所以我们修改 <code>counter</code> 的值时，<code>template</code> 中的 <code>&#123;&#123; counter &#125;&#125;</code> 也会发生改变；</li>
</ul>
</li>
<li>这种响应式的具体原理，我们后面会有专门的篇幅来讲解。</li>
</ul>
<h3 data-id="heading-28">4.3 <code>methods</code> 属性</h3>
<ul>
<li>
<p><code>methods</code> 属性是一个对象，我们通常会在这个对象中定义很多的方法：</p>
<ul>
<li>这些方法可以<strong>被绑定到 <code>template</code> 模板</strong>中；</li>
<li>在这些方法中，我们可以<strong>使用 <code>this</code> 关键字</strong>来直接访问到 <code>data</code> 中返回的对象的属性；</li>
</ul>
</li>
<li>
<p>对于有经验的同志，这里可以就官方文档中的以下这段描述<sup id="user-content-fnref-2"><a href="https://juejin.cn/post/6984378114902065182#fn-2" class="footnote-ref" target="_blank" title="#fn-2">2</a></sup>思考两个问题：</p>
<ol>
<li>为什么不能使用<strong>箭头函数</strong>？（官方文档给出的解释真的理解了吗？）</li>
<li>不使用箭头函数的情况下，<strong><code>this</code> 到底指向什么</strong>？（可以作为一道面试题）</li>
</ol>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c287b13b28b7421aa11e8087523b2de0~tplv-k3u1fbpfcp-watermark.image" alt="不应该使用箭头函数来定义 method 函数" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-29">4.4 其它属性</h3>
<p>当然，<code>createApp()</code> 函数传入的对象中还有很多其它的属性，我们会在后续进行讲解：</p>
<ul>
<li>比如 <code>props</code>、<code>emits</code>、<code>setup</code>、<code>computed</code>、<code>watch</code> 等等；</li>
<li>也包括很多的生命周期函数；</li>
</ul>
<p>不用着急，我们会一个个学习它们的。</p>
<h2 data-id="heading-30">5. <code>Vue</code> 源码的下载、调试、阅读</h2>
<ul>
<li>有同志可能会疑惑，前面第 <code>2</code> 节不是已经下载了 <code>Vue</code> 的源码了吗？怎么又要下载？
<ul>
<li>因为前面下载的 <code>Vue</code> 源码是已经打包过的，所有代码都放到一个文件中了，看起来非常不方便。</li>
</ul>
</li>
<li>也有同志可能会问，第 <code>2</code> 节中通过 <code>CDN</code> 下载的 <code>Vue</code> 的源码中不仅有 <code>ES5</code> 的代码，怎么还有 <code>ES6</code> 的代码呢？
<ul>
<li>这是因为事实上最终在项目打包时，通过 <code>babel</code> 工具进行设置之后，这个代码还会进行一次打包（二次打包，而且还会做压缩等其它处理），所以暂时还存在 <code>ES6</code> 的代码不会有问题。</li>
</ul>
</li>
</ul>
<p>对于第 <code>2</code> 节中通过 <code>CDN</code> 下载的 <code>Vue</code> 的源码，我们可能会阅读里面的某个函数，但不会按照这份打包后的源码一点点地去读。那我们该怎么办呢？我们会这样做：</p>
<ol>
<li>
<p>打开 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/" ref="nofollow noopener noreferrer"><code>GitHub</code></a> 网站，左上方搜索框里输入 <code>vue-next</code>（即 <code>Vue3</code> 版本）进行搜索；</p>
</li>
<li>
<p>点击搜索结果中的 <code>vuejs/vue-next</code>（我们可以看到，它是用 <code>TypeScript</code> 写的）；</p>
</li>
<li>
<p>进入 <code>vuejs/vue-next</code> 仓库后，点击 <code>master</code> 下拉按钮，点击 <code>Tags</code> 标签，选择最新的稳定的版本进行下载（我们一般不会下载 <code>Branches</code> 下的 <code>master</code> 主分支或其它 <code>dev</code> 分支（最终会合并到 <code>master</code> 主分支中），因为它们很可能是正在进行开发中的代码，存在不稳定性；而 <code>Tags</code> 下的 <code>xxx-beta.x</code> 则是测试版，也不够稳定），我们这里就选择 <code>v3.1.4</code> 版本进行下载：</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d646e99e848e454faa1e594b2fe65a3d~tplv-k3u1fbpfcp-watermark.image" alt="Vue3 源码选择版本下载" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>
<p>进入该版本的页面后，点击 <code>Code</code> 按钮，直接点击下面 <code>URL</code> 链接后面的复制按钮复制 <code>URL</code>，然后我们以 <code>git clone</code> 的方式下载源码（为什么选择这种方式？因为 <code>git</code> 在运行它的 <code>dev</code> 时，会依赖 <code>git</code> 的一些东西，有用 <code>git</code> 做一些校验。如果直接选择 <code>Download ZIP</code>，里面没有 <code>git</code>（缺少一个 <code>.git</code> 文件夹），到时候代码可能会运行不起来）：</p>
<ul>
<li>打开终端（<code>Windows</code> 上是 <code>cmd</code> 或者使用 <code>Git Bash</code>）；</li>
<li>通过 <code>cd</code> 命令进入待会下载的源码你想要存储的目录；</li>
<li>执行 <code>git clone 刚才复制的URL</code> 命令，下载源码；</li>
</ul>
</li>
</ol>
<p>如果你选择了 <code>Download ZIP</code> 的方式下载了源码，又想让源码运行起来，可以这么做：</p>
<ol>
<li>先解压下载下来的源码压缩包，用 <code>Visual Studio Code</code> 打开解压后的文件夹（<code>vue-next-3.1.4</code>）；</li>
<li>在 <code>Visual Studio Code</code> 中打开终端，输入 <code>yarn install</code> 命令并执行；
<ul>
<li>这里需要你电脑上之前已经安装过 <code>node</code> 了，并且用 <code>node</code> 安装过 <code>yarn</code> 了，如果没有，需要先下载 <code>node</code>（建议去 <code>node</code> 官网下载“长期支持版”（<code>LTS</code>）的，因为相对于“当前发布版”（<code>Current</code>）的，“长期支持版”的会更稳定一点）；</li>
<li>下载安装完 <code>node</code> 之后，就会有 <code>npm</code> 这个工具了，就可以在命令行终端执行 <code>npm install yarn -g</code> 命令，然后你的电脑上就有 <code>yarn</code> 这个工具了；</li>
<li>因为 <code>Vue</code> 的源码是用 <code>yarn</code> 来管理的（源码目录下可以看到 <code>yarn.lock</code> 文件），所以我们需要执行 <code>yarn install</code> 命令安装 <code>Vue</code> 源码所需的依赖。</li>
</ul>
</li>
<li>执行 <code>git init</code> 命令将当前文件夹（<code>vue-next-3.1.4</code>）初始化为一个空的 <code>Git</code> 仓库；</li>
<li>执行 <code>git add .</code> 命令将当前目录下的所有文件添加到暂存区；</li>
<li>执行 <code>git commit -m "fix(install): install dependences"</code> 命令将暂存区内容提交到本地仓库中；</li>
<li>执行 <code>yarn dev</code>（本质上会去执行当前文件夹下 <code>package.json</code> 文件中的 <code>scripts</code> 中的 <code>dev</code> 脚本对应的命令）命令，它会把当前文件夹下的 <code>packages</code> 文件夹下的所有文件（都是 <code>Vue</code> 的源代码）进行打包，打包后的代码会放到 <code>packages\vue\dist\vue.global.js</code> 文件（该文件其实就是上传到 <code>CDN</code> 上面的那个文件）中；</li>
<li>有了这份打包后的源代码文件，我们就可以来到 <code>packages\vue\examples</code> 目录下，新建一个目录（如 <code>coderzhj</code>），再在该目录中新建一个 <code>html</code> 文件（如 <code>demo.html</code>），接着在该文件中引入这个打包后的源码文件后，就可以用 <code>Vue</code> 编写一些代码并在 <code>Vue</code> 的项目里跑起来了：</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01bcba9c90ca40ce90f7149146f903ad~tplv-k3u1fbpfcp-watermark.image" alt="Vue 源码打包后使用" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而如果是通过 <code>git clone</code> 方式下载的源码，则无需解压，用 <code>Visual Studio Code</code> 直接打开源码存放位置下的 <code>vue-next</code> 文件夹，然后在终端执行 <code>yarn install</code> 后直接执行 <code>yarn dev</code> 即可。</p>
<p>那跑起来后有什么用呢？用处就是我们可以在 <code>script</code> 标签中打上 <code>debugger</code> 进行调试啦：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed72fcf66b82444491c5e2448a591ea9~tplv-k3u1fbpfcp-watermark.image" alt="在 Vue 源码项目中进行调试 1" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如，我们想看下 <code>createApp</code> 究竟做了些什么，就可以 <code>F10</code> 到 <code>Vue.createApp</code> 这行，再 <code>F11</code> 跳转进 <code>createApp</code> 函数：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9fdbefb9074b3f9f0e079d7d1e9068~tplv-k3u1fbpfcp-watermark.image" alt="在 Vue 源码项目中进行调试 2" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是，我们会发现这样做是在 <code>vue.global.js</code> 这个大文件中进行的调试，这意味着所有源代码都是放到了一起的，看起来非常不方便。那有没有办法让调试的时候跳转到某个具体的源代码文件中呢？有，我们可以修改项目目录下 <code>package.json</code> 文件中的 <code>scripts</code> 中的 <code>dev</code> 脚本对应的命令，在该命令最后添加上 <code> --sourcemap</code>（<code>webpack</code> 相关的内容）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0a1ec3a9136448db5b40e89d95260d8~tplv-k3u1fbpfcp-watermark.image" alt="设置代码映射" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后重新执行 <code>yarn dev</code> 把项目重新打包后跑起来（这时 <code>dist</code> 目录下会多出来一个 <code>vue.global.js.map</code> 文件，这个就是 <code>sourcemap</code> 文件，用来方便我们调试），这样一来，调试过程中的每一行代码都可以映射到它所在的具体文件中了，那么我们就能通过映射的文件和项目中的 <code>packages</code> 文件夹下的文件对应起来了：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ce992be10cd4bb28ebbe55715ef7084~tplv-k3u1fbpfcp-watermark.image" alt="设置 sourcemap 代码映射" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/506bb56de5f54008a8ea23bd110cc1e5~tplv-k3u1fbpfcp-watermark.image" alt="在 Vue 项目中的对应文件中查看" loading="lazy" referrerpolicy="no-referrer"></p>
<div class="footnotes">
<hr>
<ol>
<li id="user-content-fn-1">The <strong><code><template></code></strong> HTML element is a mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript. -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FElement%2Ftemplate" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template" ref="nofollow noopener noreferrer">MDN</a><a href="https://juejin.cn/post/6984378114902065182#fnref-1" class="footnote-backref" target="_blank" title="#fnref-1">↩</a></li>
<li id="user-content-fn-2">详见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fapi%2Foptions-data.html%23methods" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/api/options-data.html#methods" ref="nofollow noopener noreferrer">v3.cn.vuejs.org/api/options…</a><a href="https://juejin.cn/post/6984378114902065182#fnref-2" class="footnote-backref" target="_blank" title="#fnref-2">↩</a></li>
</ol>
</div></div>  
</div>
            