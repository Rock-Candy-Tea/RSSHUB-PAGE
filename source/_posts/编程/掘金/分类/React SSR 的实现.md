
---
title: 'React SSR 的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f8bdeee53e04252b8ee96da96eb8099~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 07:59:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f8bdeee53e04252b8ee96da96eb8099~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f8bdeee53e04252b8ee96da96eb8099~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再看react ssr 之前，我们先来看一个使用react ssr 实现的应用，感受一下它飞一般的渲染速度 <a href="https://m.xin.com/" target="_blank" rel="nofollow noopener noreferrer">m.xin.com/</a> 看过之后我们再来看文章。</p>
<h2 data-id="heading-0">📚导读</h2>
<p>关于服务端渲染（SSR）、客户端渲染（CSR）和 同构渲染，我在<a href="https://juejin.cn/post/6854573217365884941" target="_blank">next.js从入门到实战</a>这篇文章中开头有详细的介绍，还不了解这三种渲染方式的可以简单了解一下。</p>
<p>但只实现 SSR 没什么意义，技术上没有任何改进，否则 SPA 技术就不会出现😀。
但是单纯的 SPA 又不够完美，所以最好的方案就是这两种技术和体验的结合。但是要实现两种技术的结合，同时可以最大限度的重用代码（同构），减少开发维护成本，那就需要采用 react 或者 vue 等前端框架和node(ssr)相结合的方式来实现。</p>
<p>如果我们使用react ssr 来实际开发项目，我们就需要一个完整的开发框架，next.js其实就是这种框架，类似的还有nuxt.js。那这种框架的实现原理是什么呢？</p>
<h2 data-id="heading-1">📚react ssr 实现原理</h2>
<p>在了解react ssr 我们先来看两个概念。</p>
<h3 data-id="heading-2">📒虚拟dom</h3>
<p><code>react ssr </code>其中的<code>SSR</code>指的是在服务端渲染组件。而组件可以在服务端渲染的根本原因就是<code>虚拟 DOM</code>，我们一般使用jsx来编写react组件，但其实jsx是一个语法糖，其实我们编写的组件都可以解析为一个个对象。这个对象包含</p>
<ul>
<li>🎈tag：节点标签名</li>
<li>🎈props：DOM的属性，用一个对象存储键值对</li>
<li>🎈children： 该节点的子节点</li>
</ul>
<p>我们有了这个对象，我们就可以轻松的将其转换为我们需要的格式，比如<code>html</code>格式，当然这个转换不需要我们来完成，这个转换<code>react</code>已经帮我们完成了，其本身提供内置方法支持服务端渲染；我们先来具体了解一下同构的概念；</p>
<h3 data-id="heading-3">📒同构</h3>
<p>同构是将传统的纯服务端直出的首屏优势和SPA的站内体验优势结合起来，以取得最优解的解决方案。</p>
<p>就是服务端把首屏的内容直出，让用户更快的看到页面，然后后面的数据采用js来异步请求和加载。貌似不用<code>react</code>一样可以做到的呀，那为什么还一定要使用<code>react</code>或者<code>vue</code>这种框架来结合<code>ssr</code>呢？</p>
<p>我们知道同构就是指前后端公用一套代码，比如我们的组件可以在服务端渲染也可以在客户端渲染，但都是同一个组件。这也是react本身的优势。我们使用react来写，可以减少我们的代码量，基于react来实现更加方便，高效，因为我们可以使用react + node 来构造</p>
<h3 data-id="heading-4">📒结语</h3>
<p>其实到这里我们也明白了什么是react ssr , react ssr 就是react 利用自身虚拟dom的优势，然后通过同构渲染来实现的。react ssr 的核心就是同构，没有同构的 ssr 是没有意义的。</p>
<h2 data-id="heading-5">📚react ssr 是如何实现的</h2>
<p>我们了解了什么是react ssr ，那么react ssr 是怎么实现的呢，是怎么实现的服务端渲染，html的转换？</p>
<p>为了实现服务端渲染，打造同构应用，react内部实现了相关的API，可以将组件转换为html，可以一起来看一下这ReactDOMServer 这个 api</p>
<h3 data-id="heading-6">📒ReactDOMServer</h3>
<p>ReactDOMServer 类可以帮我们在服务端渲染组件 - 得到组件的 html 字符串。</p>
<p>该模块有两个方法renderToString 和 renderToStaticMarkup，两个方法都是将组件转换为html格式的，它们的使用方式也是相同的，不同的是renderToStaticMarkup不需要计算，所以性能能高，速度更快。</p>
<h2 data-id="heading-7">📚react ssr 如何解决seo tdk支持</h2>
<p>对于这个问题，其实有现成的轮子可以使用。它就是[react-helmet](ReactDOMServer.renderToString();
const helmet = Helmet.renderStatic();)。</p>
<h3 data-id="heading-8">📒简介</h3>
<p>React Helmet是一个HTML文档head管理工具，管理对文档头的所有更改。</p>
<h3 data-id="heading-9">📒特点</h3>
<ul>
<li>支持所有有效的head标签: title、 base、 meta、 link、 script、 noscript、 和style。</li>
<li>支持body、 html 和 title 的属性</li>
<li>支持服务端渲染</li>
<li>嵌套组件覆盖重复的head标签更改。</li>
<li>在同一组件中定义时，将保留重复的head标签更改。(支持如"apple-touch-icon"的标签).</li>
<li>支持跟踪DOM更改的回调</li>
</ul>
<h3 data-id="heading-10">📒安装</h3>
<p>Npm</p>
<pre><code class="copyable">npm i react-helmet
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Yarn</p>
<pre><code class="copyable">yarn add react-helmet
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">📒💁‍♀️🌰简单示例</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123;Helmet&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-helmet"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Application</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  render () &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"application"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Helmet</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charSet</span>=<span class="hljs-string">"utf-8"</span> /></span>
                <span class="hljs-tag"><<span class="hljs-name">title</span>></span>My Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"canonical"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://mysite.com/example"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">Helmet</span>></span>
            ...
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            