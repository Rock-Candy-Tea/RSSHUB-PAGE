
---
title: 'postMessage解决Vue页面到React页面的跨域问题实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/503118e1d9c449cdb4d334914a3decc4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 03:07:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/503118e1d9c449cdb4d334914a3decc4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>背景：有两个项目，一个基于<code>Vue</code>开发，一个基于<code>React</code>开发。<code>Vue</code>项目中某个页面（称为<code>父页面</code>）通过<code>iframe</code>标签嵌入了<code>React</code>项目的某个页面（称为<code>子页面</code>）。现在子页面要和父页面要进行通信，传递数据。</p>
</blockquote>
<h1 data-id="heading-0">关键技术</h1>
<p>跨域方式还挺多的，本次主要通过<code>H5</code>提供的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow%2FpostMessage" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage" ref="nofollow noopener noreferrer">postMessage()</a>方法解决上面提到的问题。</p>
<h1 data-id="heading-1">最佳实践</h1>
<h2 data-id="heading-2">初步方案</h2>
<ul>
<li>Vue 父页面核心代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// PostMessageVueSide.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container border-2 border-gray-400 border-solid"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>这是基于Vue的页面（父页面）<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text-red-500"</span>></span>传递的数据：<span class="hljs-tag"></<span class="hljs-name">span</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"w-full h-full"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"w-full h-full"</span>  <span class="hljs-attr">ref</span>=<span class="hljs-string">"parentPage"</span> <span class="hljs-attr">scrolling</span>=<span class="hljs-string">"no"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"http://localhost:3001"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'vue page data'</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$refs.parentPage.contentWindow.postMessage(<span class="hljs-built_in">this</span>.message, <span class="hljs-string">'*'</span>);
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.container</span> &#123;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100vh</span> - <span class="hljs-number">100px</span>);
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于Vue的项目启动服务后的地址在<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080/" ref="nofollow noopener noreferrer">http://localhost:8080/</a>。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3001" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3001" ref="nofollow noopener noreferrer">http://localhost:3001</a>是基于React的项目启动服务后的地址。</p>
<p>当页面挂载完成，我们通过<code>$fefs</code>获取<code>iframe</code>实例，并通过<code>contentWindow.postMessage</code>向子页面发送数据。</p>
<ul>
<li>React 子页面核心代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// PostMessageReactSide.jsx</span>
<span class="hljs-keyword">import</span> React, &#123;useEffect, useState&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">'./Home.scss'</span>

<span class="hljs-keyword">const</span> Home = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [message, setMessage] = useState(<span class="hljs-string">''</span>);

  useEffect(<span class="hljs-function">() =></span>&#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span>&#123;
      <span class="hljs-built_in">console</span>.log(e.data);
      setMessage(e.data);
    &#125;)
   &#125;
  );
  
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是基于React的页面（子页面）<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"received-data"</span>></span>收到的数据：<span class="hljs-tag"></<span class="hljs-name">span</span>></span>&#123;message&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Home;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>React</code>界面基于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Fhooks-intro.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/hooks-intro.html" ref="nofollow noopener noreferrer">React  Hook</a>实现。</p>
<p>在<code>useEffect</code>函数中我们监听<code>message</code>事件，并试图获取从父页面发来的数据。</p>
<ul>
<li>界面效果</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/503118e1d9c449cdb4d334914a3decc4~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从网上看到的大多数基于<code>postMessage</code>跨域的教程基本上都是这个流程。</p>
<p>但是，从页面效果可看到，我们的子页面并没有拿到从父页面拿到数据。</p>
<p>为什么呢？请往下看：</p>
<p>我们进行<code>debug</code>，可以看到当我们准备要向子页面发送数据时，此时子页面还没加载出来。</p>
<p>因此，如果我们想要在子页面拿到父页面的数据，必须等子页面加载完成后，父页面再向子页面发送数据。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab33239d0cf54c19ab7f27289543b217~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">改善方案</h2>
<p>通过<code>load</code>事件，在页面加载完成时，再发送数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// PostMessageVueSide.vue</span>
 <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>);
    <span class="hljs-keyword">const</span> parentPage = <span class="hljs-built_in">this</span>.$refs.parentPage;
    parentPage.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function">()=></span> &#123;
      parentPage.contentWindow.postMessage(<span class="hljs-built_in">this</span>.message, <span class="hljs-string">'*'</span>);
    &#125;)
    <span class="hljs-comment">// this.$refs.parentPage.contentWindow.postMessage(this.message, '*');</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>debug</code>可以看到当我们准备从父页面发送数据时，子页面已经渲染出来。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59b49ba6494f40e4ac47abe3ee1a30f3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
因此，接下来我们就拿到了父页面的数据：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58e0b214eb9b44edb90c1d8606a3c38d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在实际工作的项目中，<code>React</code>界面往往没有这么简单，页面需要加载的东西很多。</p>
<p>在实际工作中用上面的方案可能是下面的结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/804e9bccd7e54ac8990d4200cfeb32f9~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
所以，用这种方案，我们在子页面还是不能拿到数据。</p>
<h2 data-id="heading-4">寻求其他方案</h2>
<p>我们还可以用定时器来延时发送数据。这里我们延时设置为<code>3000ms</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// PostMessageVueSide.vue</span>
<span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">this</span>.$refs.parentPage.contentWindow.postMessage(<span class="hljs-built_in">this</span>.message, <span class="hljs-string">'*'</span>);
    &#125;, <span class="hljs-number">3000</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99596d0582604e3d81d7fe13812824c0~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
这种方案是可行的，数据是能拿到。</p>
<p>但因为子页面加载较快，过了一会儿数据才显示。</p>
<p>这种方案的缺陷很明显，我们不确定子页面究竟要多少<code>ms</code>才能加载完成。</p>
<h2 data-id="heading-5">终极方案</h2>
<p>既然上面我们不确定子页面究竟要多少<code>ms</code>才能加载完成。那我们可以等子页面加载完成时向父页面发送一个信号，告诉父页面“我已经加载完成，你可以向我发送数据了”。</p>
<p>那这里我们就需要从子页面通过<code>postMessage</code>向父页面发送数据了。</p>
<p>在子页面中我们在<code>useEffect</code>中发送数据通知父页面，子页面已加载完成。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// PostMessageReactSide.jsx</span>
<span class="hljs-keyword">const</span> Home = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [message, setMessage] = useState(<span class="hljs-string">''</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 页面加载已完成，通知父页面</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child page mounted'</span>);
    <span class="hljs-built_in">window</span>.parent.postMessage(&#123;<span class="hljs-attr">retcode</span>: <span class="hljs-number">200</span>&#125;, <span class="hljs-string">'*'</span>);   
  &#125;);

  useEffect(<span class="hljs-function">() =></span>&#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span>&#123;
      <span class="hljs-built_in">console</span>.log(e.data);
      setMessage(e.data);
    &#125;)
   &#125;
  );
  
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是基于React的页面（子页面）<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"received-data"</span>></span>收到的数据：<span class="hljs-tag"></<span class="hljs-name">span</span>></span>&#123;message&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父页面中监听<code>message</code>，当拿到子页面的数据时（说明子页面已加载完成），我们就向子页面发送数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// PostMessageVueSide.vue</span>
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'parent page mounted'</span>);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (e.data.retcode === <span class="hljs-number">200</span>) &#123;
        <span class="hljs-built_in">this</span>.$refs.parentPage.contentWindow.postMessage(<span class="hljs-built_in">this</span>.message, <span class="hljs-string">'*'</span>);
      &#125;
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新页面：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7781ef024b814f7baaf970fecafd086e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
完美解决了问题。</p>
<h2 data-id="heading-6">展望方案</h2>
<p>父子页面来回传递数据容易造成数据混乱，难以管理，数据流不明确。</p>
<p>我们可以设计一个<code>顶层数据点</code>，让父页面和子页面都从这个<code>顶层数据点</code>拿数据及修改数据等。这样可以保证父子界面拿到的数据是同步的。</p>
<p>例如，父子页面都可以从后台调统一接口拿数据，而不用让数据在父子页面间来回传递。</p>
<h1 data-id="heading-7">总结</h1>
<p>用<code>postMessage</code>解决跨域问题最关键的点就是，<strong>父页面要在子页面加载完成时再发送数据</strong>，否则子页面可能收不到数据。</p>
<h1 data-id="heading-8">源码</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FLynnHg%2Fbest-practice-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/LynnHg/best-practice-demo" ref="nofollow noopener noreferrer">gitee.com/LynnHg/best…</a></li>
</ul></div>  
</div>
            