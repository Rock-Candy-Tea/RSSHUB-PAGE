
---
title: '前端是不是又要回去操作真实dom年代？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83070a8b69964908984547ca82a8ba5c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 04:29:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83070a8b69964908984547ca82a8ba5c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">写在开头</h2>
<ul>
<li>近期我有写两篇文章，一篇是:<code>petite-vue</code>源码解析和掘金编辑器的源码解析，发现里面用到了<code>Svelte</code>这个框架</li>
<li>加上最近React17，vite大家也在逐步的用在生产环境中，我于是有了今天的思考</li>
</ul>
<h2 data-id="heading-1">看前端的技术演进</h2>
<ul>
<li>原生<code>Javascript - Jquery</code>为代表的时代，例如，引入<code>Jquery</code>只要</li>
</ul>
<pre><code class="copyable"><script src="cdn/jquery.min,js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接着便又有了<code>gulp</code> <code>webpack</code>等构建工具出现，React和Vue也在这个时候开始火了起来，随即而来的是一大堆工程化的辅助工具，例如<code>babel</code>,还有提供整套服务的<code>create-react-app</code>等脚手架</li>
<li>这也带来了问题，当然这个是<code>npm</code>的问题，每次启动项目前，都要安装大量的依赖，即便出现了yarn pnpm`等优化的依赖管理工具，但是这个问题根源不应该使用工具解决，而是问题本质是依赖本地化，代码和依赖需要工具帮助才能运行在浏览器中</li>
</ul>
<blockquote>
<p>总结就是：现有的开发模式，让项目太重，例如我要使用某个脚手架，我只想写一个<code>helloworld</code>演示下,结果它让我装<code>500mb</code>的依赖，不同的脚手架产物，配置不同，产物也不同</p>
</blockquote>
<h2 data-id="heading-2">理想的开发模式</h2>
<ul>
<li>
<p>1.不需要辅助的工具配置，我不需要webpack这类帮我打包的工具，模块化浏览器本身就支持，而且是一个规范。例如<code>vite</code>号称不打包，用的是浏览器本身支持的<code>esm</code>模块化，但是它没有解决依赖的问题，因为依赖问题本身是依赖的问题，而不是工具的问题</p>
</li>
<li>
<p>2.不需要安装依赖，一切都可以<code>import from remote</code>,我觉得<code>webpack5</code>的<code>Module Federation</code>设计，就考虑到了这一点，下面是官方的解释：</p>
<ul>
<li>
<p>多个独立的构建可以组成一个应用程序，这些独立的构建之间不应该存在依赖关系，因此可以单独开发和部署它们。</p>
</li>
<li>
<p>这通常被称作微前端，但并不仅限于此。</p>
</li>
</ul>
</li>
</ul>
<blockquote>
<p>但是这可能并不是最佳实践，目前是有<code>import from http</code>，例如</p>
</blockquote>
<pre><code class="copyable">import lodash from 'https://unpackage/lodash/es'
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这里又会有人问，那你不都是要发请求吗，都是要每次启动的时候去远程拉取，还不如在本地呢。<code>import from http</code>我想只是解决了一个点的问题，就是不用手动安装依赖到本地磁盘</li>
<li>前段时间我写过，在浏览器中本地运行Node.js</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83070a8b69964908984547ca82a8ba5c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这个技术叫<code>WebContainers</code>技术，感兴趣的可以去翻翻我公众号之前的文章</p>
</blockquote>
<ul>
<li>等等，别急。这些仅仅开了个头，新的技术往往要探索才能实现价值最大化，我想此处应该可以彻底颠覆现有的开发模式，而且应该就在3-5年内。</li>
</ul>
<h2 data-id="heading-3">将几个新的前端技术理念融合？</h2>
<ul>
<li><code>vite</code>的不打包理念：直接使用浏览器支持的<code>esm</code>模块化</li>
<li><code>WebContainers</code>技术：让浏览器直接运行<code>node.js</code></li>
<li><code>import from remote</code>,从一个个远程地址直接引入可以使用的依赖</li>
<li>现在很火的<code>webIDE</code>:类似<code>remix</code>编辑器，直接全部可以在云端搞定</li>
<li>浏览器的优化，天然有缓存支持</li>
</ul>
<h2 data-id="heading-4">会发生什么变化？</h2>
<ul>
<li>我们所有的一切开始，都直接启动一个浏览器即可</li>
<li>浏览器中的<code>webIDE</code>,可以直接引入远程依赖，浏览器可以运行<code>Node.js</code>，使用的都是<code>esm</code>模块化，不需要打包工具，项目启动的时间和热更新时间都非常短，构建也是直接可以在浏览器中构建</li>
</ul>
<blockquote>
<p>这些看似解决了我们之前提出的大部分问题，回到今天的主题</p>
</blockquote>
<hr>
<h2 data-id="heading-5">回到主题</h2>
<ul>
<li>前端会不会回到操作原生<code>dom</code>的时代？</li>
<li>我觉得，有这个趋势，例如<code>petite-vue</code>,还有<code>Svelte</code>。</li>
</ul>
<blockquote>
<p>因为之前写过<code>petite-vue</code>源码解析了，我们今天就讲讲<code>Svelte</code></p>
</blockquote>
<h2 data-id="heading-6">Svelte</h2>
<blockquote>
<p><code>Svelte</code> 是一种全新的构建用户界面的方法。传统框架如 React 和 Vue 在浏览器中需要做大量的工作，而 Svelte 将这些工作放到构建应用程序的编译阶段来处理。</p>
</blockquote>
<ul>
<li>与使用虚拟（virtual）DOM 差异对比不同。Svelte 编写的代码在应用程序的状态更改时就能像做外科手术一样更新 DOM</li>
</ul>
<hr>
<ul>
<li>
<p>上面是官方的介绍，我们看看知乎这篇文章<code>https://zhuanlan.zhihu.com/p/97825481</code>,感觉他写得很好，这里照搬一些过来吧直接</p>
</li>
<li>
<p>React和Vue都是基于runtime的框架。所谓基于runtime的框架就是框架本身的代码也会被打包到最终的bundle.js并被发送到用户浏览器。</p>
</li>
<li>
<p>当用户在你的页面进行各种操作改变组件的状态时，框架的runtime会根据新的组件状态（state）计算（diff）出哪些DOM节点需要被更新</p>
</li>
</ul>
<blockquote>
<p>可是，这些被打包进去的框架，实在太大了。</p>
</blockquote>
<p>(今天还在跟同事说，前年写的登录站点，纯原生手工打造，性能无敌)
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17fe57b4aa604135b2890701faea42b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>100kb</code>对于一个弱网环境来说，很要命，我们看看<code>svelte</code>减少了多少体积:</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4034c9d7af1454588774dda4cc19f16~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">科普</h2>
<ul>
<li>虚拟<code>dom</code>并没有加快用户操作浏览器响应的速度，只是说，方便用于数据驱动视图，更便于管理而已，并且在一定程度上，更慢。真正最快的永远是：</li>
</ul>
<pre><code class="copyable">currentDom.innerHtml = '前端巅峰';
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>所以<code>Svelte</code>并不是说多好，而是它的这种理念，可能未来会越来越成为主流</p>
</blockquote>
<h2 data-id="heading-8">React17的改变</h2>
<ul>
<li>大家应该都知道，现有的浏览器都是无法直接解译JSX的，所以大多数React用户都需要使用Babel或者TypeScript之类的编译器来将JSX转换为浏览器能够理解的JavaScript语言。许多预配置的工具箱（如：Create React App 或者Next.js）内部也有JSX的转换。</li>
<li>React 17.0，尽管React团队想对JSX的转换进行改进，但React团队不想打破现有的配置。这就是为什么React团队与Babel合作，为想要升级的开发者提供了一个全新的JSX转换的重写版本。</li>
<li>通过全新的转换，你可以单独使用JSX而无需引入React.</li>
</ul>
<blockquote>
<p>我猜想，或许React团队有意将jsx语法推动到成为es标准语法中去，剥离开来希望会大大提升。</p>
</blockquote>
<h2 data-id="heading-9">重点</h2>
<ul>
<li>说了这么多，大家可能没理解到重点，那就是：大家都在想着减轻自身的负重，把丢下来的东西标准化，交给浏览器处理，这也是在为未来的只需要打开一个浏览器，就可以完成所有的事情做铺垫</li>
<li>而我，相信这一天应该不远了，据我所知已经有不少顶尖的团队在研发这种产品</li>
</ul>
<h2 data-id="heading-10">写在最后</h2>
<ul>
<li>如果你感觉有什么疑问，在下方给我留言吧</li>
<li>如果你感觉写得不错，帮我的公众号：<code>前端巅峰</code>点个<code>在看/赞/关注</code>三连吧，原创不易</li>
</ul></div>  
</div>
            