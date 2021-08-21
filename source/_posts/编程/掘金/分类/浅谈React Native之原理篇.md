
---
title: '浅谈React Native之原理篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7527'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 02:27:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=7527'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 20 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>要说React Native的原理，我们就不得不先聊聊React了。</p>
<p>React 框架是一个非常优雅、现代的前端开发框架，通过数据驱动的模式，可以让我们可以更专注于开发业务逻辑。</p>
<h2 data-id="heading-1">React介绍</h2>
<p>React 的组件是用户界面的最小元素，与外界的所有交互都通过 state 和 props 进行传递。通过这样的组件封装设计，使用声明式的编程方式，使得 React 的逻辑足够简化，并可以通过模块化开发逐步构建出项目的整体 UI。</p>
<p>React 框架中还有一个重要的概念是单向数据流，所有的数据流从父节点传递到子节点。假设父节点数据通过 props 传递到子节点，如果相对父节点（或者说相对顶层）传递的 props 值改变了，那么其所有的子节点（默认在没有使用 shouldComponentUpdate 进行优化的情况下）都会进行重新渲染，这样的设计使得组件足够扁平并且也便于维护。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorldApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Hello world!<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Virtual DOM</h2>
<p>React 框架底层的核心为 Virtual DOM，也就是虚拟 DOM。那么，我们为什么需要虚拟DOM呢？</p>
<ul>
<li>Virtual DOM是一种描述，而不是具体实现，这可以让我们可以通过Virtual DOM实现一码多用</li>
<li>频繁操作DOM是低效的，通过Virtual DOM的diff机制，可以合并和缩减操作次数</li>
</ul>
<h2 data-id="heading-3">React Native介绍</h2>
<p>在了解了React的关键机制后，会对我们学习React Native更有帮助。</p>
<p>Facebook 曾致力于使用 HTML 5 进行移动端的开发，最终发现与原生的 App 相比，体验上还是有非常大的差距，并且这种差距越来越大，特别是性能方面的差距。</p>
<p>最终，Facebook 放弃了 HTML 5 的技术方向，结合之前章节介绍的 React 框架的发展历史，2015 年 3 月，Facebook 正式发布了 React Native 框架，此框架专注于移动端 App 的开发。</p>
<p>在最初发布的版本中，我们只可以使用 React Native 框架开发 iOS 平台的 App，在 2015 年 9 月，Facebook 发布了支持 Android 平台的 React Native 框架。至此，React Native 框架真正实现了跨平台的移动 App 开发，此消息简直就是移动开发人员的福音。</p>
<p>React Native 框架在 React 框架的基础上，底层通过对 iOS 平台与 Android 平台原生代码的封装与调用，结合前台的 JavaScript 代码，这样我们就可以通过 JavaScript 代码编写出调用 iOS 平台与 Android 平台原生代码的 App，调用原生代码编写的 App 的性能远远优于使用 HTML 5 开发的 App 性能，因为 HTML 5 开发的 App 只是在 HTML 5 外部包裹上一个程序外壳后在移动平台上运行，在性能与可以实现的功能上都不能达到 React Native 框架的水准。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; Text, View &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorldApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Text</span>></span>Hello world!<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，和传统的React开发相比，只是把DOM的描述替换成了react-native模块，react-native模块通过平台判断，继续渲染为对应的平台原生组件。</p></div>  
</div>
            