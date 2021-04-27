
---
title: '微信小程序app.onLaunch与page.onLoad异步问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6818'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 23:41:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=6818'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">微信小程序app.onLaunch与page.onLoad异步问题</h2>
<h3 data-id="heading-1">问题：</h3>
<p>相信很多人都遇到过这个问题，通常我们会在应用启动app.onLaunch() 去发起静默登录，同时我们需要在加载页面的时候，去调用一个需要登录态的后端 API 。由于两者都是异步，往往page.onload()调用API的时候，app.onLaunch() 内调用的静态登录过程还没有完成，从而导致请求失败。</p>
<h3 data-id="heading-2">解决方案：</h3>
<h4 data-id="heading-3">1. 通过回调函数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// on app.js</span>
App(&#123;
    <span class="hljs-function"><span class="hljs-title">onLaunch</span>(<span class="hljs-params"></span>)</span> &#123;
      login()
      <span class="hljs-comment">// 把hasLogin设置为 true</span>
        .then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.globalData.hasLogin = <span class="hljs-literal">true</span>;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.checkLoginReadyCallback) &#123;
            <span class="hljs-built_in">this</span>.checkLoginReadyCallback();
          &#125;
      &#125;)
      <span class="hljs-comment">// 把hasLogin设置为 false</span>
        .catch(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.globalData.hasLogin = <span class="hljs-literal">false</span>;
      &#125;);
    &#125;,
&#125;);

<span class="hljs-comment">// on page.js</span>
Page(&#123;
    <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (getApp().globalData.hasLogin) &#123; <span class="hljs-comment">// 登录已完成</span>
            fn() <span class="hljs-comment">// do something</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
            getApp().checkLoginReadyCallback = <span class="hljs-function">() =></span> &#123;
              fn()
            &#125;
      &#125;
    &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>⚠️注意：这个方法有一定的缺陷（如果启动页中有多个组件需要判断登录情况，就会产生多个异步回调，过程冗余），不建议采用。</p>
<hr>
<h4 data-id="heading-4">2. 通过Object.defineProperty监听globalData中的hasLogin值</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// on app.js</span>
App(&#123;
    <span class="hljs-function"><span class="hljs-title">onLaunch</span>(<span class="hljs-params"></span>)</span> &#123;
      login()
      <span class="hljs-comment">// 把hasLogin设置为 true</span>
        .then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.globalData.hasLogin = <span class="hljs-literal">true</span>;
      &#125;)
      <span class="hljs-comment">// 把hasLogin设置为 false</span>
        .catch(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.globalData.hasLogin = <span class="hljs-literal">false</span>;
      &#125;);
    &#125;,
  <span class="hljs-comment">// 监听hasLogin属性</span>
    <span class="hljs-attr">watch</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn</span>) </span>&#123;
        <span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">this</span>.globalData
        <span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">'hasLogin'</span>, &#123;
          <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
            <span class="hljs-built_in">this</span>._hasLogin = value;
            fn(value);
          &#125;,
          <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._hasLogin
          &#125;
        &#125;)
    &#125;,
&#125;);

<span class="hljs-comment">// on page.js</span>
Page(&#123;
    <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (getApp().globalData.hasLogin) &#123; <span class="hljs-comment">// 登录已完成</span>
            fn() <span class="hljs-comment">// do something</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
            getApp().watch(<span class="hljs-function">() =></span> fn())
      &#125;
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3. 通过<a href="http://beautywejs.com/#/" target="_blank" rel="nofollow noopener noreferrer">beautywe</a>的状态机插件（项目中使用该方法）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// on app.js</span>
<span class="hljs-keyword">import</span> &#123; BtApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@beautywe/core/index.js'</span>;
<span class="hljs-keyword">import</span> status <span class="hljs-keyword">from</span> <span class="hljs-string">'@beautywe/plugin-status/index.js'</span>;
<span class="hljs-keyword">import</span> event <span class="hljs-keyword">from</span> <span class="hljs-string">'@beautywe/plugin-event/index.js'</span>;

<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> BtApp(&#123;
    <span class="hljs-function"><span class="hljs-title">onLaunch</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 发起静默登录调用</span>
      login()

      <span class="hljs-comment">// 把状态机设置为 success</span>
        .then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.status.get(<span class="hljs-string">'login'</span>).success())

      <span class="hljs-comment">// 把状态机设置为 fail</span>
        .catch(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.status.get(<span class="hljs-string">'login'</span>).fail());
    &#125;,
&#125;);
<span class="hljs-comment">// status 插件依赖于 beautywe-plugin-event</span>
app.use(event());
 
<span class="hljs-comment">// 使用 status 插件</span>
app.use(status(&#123;
  <span class="hljs-attr">statuses</span>: [
    <span class="hljs-string">'login'</span>
  ],
&#125;));

<span class="hljs-comment">// 使用原生的 App 方法</span>
App(app);


<span class="hljs-comment">// on page.js</span>
Page(&#123;
    <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// must 里面会进行状态的判断，例如登录中就等待，登录成功就直接返回，登录失败抛出等。</span>
      getApp().status.get(<span class="hljs-string">'login'</span>).must().then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 进行一些需要登录态的操作...</span>
      &#125;)
    &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">具体实现</h3>
<p>具体实现可以参考我的商城小程序项目
项目体验地址：<a href="https://wxop-pic.0-1-byte.com/byte01/web_link/index.html#/?link_id=6087bd6f5f9cac78bd74a177&account_id=1&target_link=https%3A%2F%2Fbytemall.0-1-byte.com%2Fadmin%2Findex.html" target="_blank" rel="nofollow noopener noreferrer">体验</a>
代码：<a href="https://gitee.com/frank-say/bytemall/blob/master/bytemall-app/app.js" target="_blank" rel="nofollow noopener noreferrer">代码</a></p></div>  
</div>
            