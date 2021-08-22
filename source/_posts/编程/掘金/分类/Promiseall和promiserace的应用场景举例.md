
---
title: 'Promise.all和promise.race的应用场景举例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f2c8b83fe3486a8728695a947d7383~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:33:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f2c8b83fe3486a8728695a947d7383~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">问题描述</h2>
<p>为了解决前端异步函数多层嵌套会产生回调地狱问题，以及回调地狱错误不方便捕捉的问题。所以，那些制造规则的大佬们，就在ES6中加入了一个新功能~Promise。本文主要记录一下Promise.all和promise.race的应用场景并举例说明。</p>
<blockquote>
<p>关于Promise的基本概念什么的，这里就不赘述了。</p>
</blockquote>
<h2 data-id="heading-1">Promise.all方法</h2>
<p>简而言之：<code>Promise.all( ).then( )适用于处理多个异步任务，且所有的异步任务都得到结果时的情况。</code></p>
<p>比如：用户点击按钮，会弹出一个弹出对话框，对话框中有两部分数据呈现，这两部分数据分别是不同的后端接口获取的数据。</p>
<p>弹框弹出后的初始情况下，就让这个弹出框处于<code>数据加载中</code>的状态，当这两部分数据都从接口获取到的时候，才让这个<code>数据加载中</code>状态消失。让用户看到这两部分的数据。</p>
<p>那么此时，我们就需求这两个异步接口请求任务都完成的时候做处理，所以此时，使用Promise.all方法，就可以轻松的实现，我们来看一下代码写法</p>
<h3 data-id="heading-2">代码附上</h3>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">plain</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"clickFn"</span>></span>点开弹出框<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">clickFn</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.alertMask = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 打开弹出框</span>
      <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 暂时还没数据，所以就呈现loading加载中效果</span>

      <span class="hljs-comment">// 第一个异步任务</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncOne</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> async1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-keyword">async</span> (resolve, reject) => &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 这里我们用定时器模拟后端发请求的返回的结果，毕竟都是异步的</span>
            <span class="hljs-keyword">let</span> apiData1 = <span class="hljs-string">"第一个接口返回数据啦"</span>;
            resolve(apiData1);
          &#125;, <span class="hljs-number">800</span>);
        &#125;);
        <span class="hljs-keyword">return</span> async1;
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"异步任务一"</span>, asyncOne());  <span class="hljs-comment">// 返回的是一个Promise对象</span>

      <span class="hljs-comment">// 第二个异步任务</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncTwo</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> async2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-keyword">async</span> (resolve, reject) => &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">let</span> apiData2 = <span class="hljs-string">"第二个接口返回数据啦"</span>;
            resolve(apiData2);
          &#125;, <span class="hljs-number">700</span>);
        &#125;);
        <span class="hljs-keyword">return</span> async2;
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"异步任务二"</span>, asyncTwo()); <span class="hljs-comment">// 返回的是一个Promise对象</span>

      <span class="hljs-keyword">let</span> paramsArr = [asyncOne(), asyncTwo()]

      <span class="hljs-comment">// Promise.all方法接收的参数是一个数组，数组中的每一项是一个个的Promise对象</span>
      <span class="hljs-comment">// 我们在 .then方法里面可以取到 .all的结果。这个结果是一个数组，数组中的每一项</span>
      <span class="hljs-comment">// 对应的就是 .all数组中的每一项的请求结果返回的值</span>
      <span class="hljs-built_in">Promise</span>
      .all(paramsArr)
      .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Promise.all方法的结果"</span>, value);
        <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 现在有数据了，所以就关闭loading加载中效果</span>
      &#125;);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">打印的结果图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f2c8b83fe3486a8728695a947d7383~tplv-k3u1fbpfcp-watermark.image" alt="111.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Promise.race方法</h2>
<p><code>Promise.race赛跑机制，只认第一名</code></p>
<p>Promise.race其实使用的并不多，如果真要使用。我们可以提出这样一个需求：</p>
<p><strong>比如：点击按钮发请求，当后端的接口超过一定时间，假设超过三秒，没有返回结果，我们就提示用户请求超时</strong></p>
<h3 data-id="heading-5">代码附上</h3>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">plain</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"clickFn"</span>></span>点击测试<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">clickFn</span>(<span class="hljs-params"></span>)</span> &#123;

      <span class="hljs-comment">// 第一个异步任务</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncOne</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> async1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-keyword">async</span> (resolve, reject) => &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 这里我们用定时器模拟后端发请求的返回的结果，毕竟都是异步的</span>
            <span class="hljs-keyword">let</span> apiData1 = <span class="hljs-string">"某个请求"</span>;
            resolve(apiData1);
          &#125;, <span class="hljs-number">4000</span>);
        &#125;);
        <span class="hljs-keyword">return</span> async1;
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"异步任务一"</span>, asyncOne());  <span class="hljs-comment">// 返回的是pending状态的Promise对象</span>

      <span class="hljs-comment">// 第二个异步任务</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncTwo</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> async2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-keyword">async</span> (resolve, reject) => &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">let</span> apiData2 = <span class="hljs-string">"超时提示"</span>;
            resolve(apiData2);
          &#125;, <span class="hljs-number">3000</span>);
        &#125;);
        <span class="hljs-keyword">return</span> async2;
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"异步任务二"</span>, asyncTwo()); <span class="hljs-comment">// 返回的是pending状态的Promise对象</span>

      <span class="hljs-comment">// Promise.race接收的参数也是数组，和Promise.all类似。只不过race方法得到的结果只有一个</span>
      <span class="hljs-comment">// 就是谁跑的快，结果就使用谁的值</span>
      <span class="hljs-keyword">let</span> paramsArr = [asyncOne(), asyncTwo()]

      <span class="hljs-built_in">Promise</span>
      .race(paramsArr)
      .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Promise.race方法的结果"</span>, value);
        <span class="hljs-keyword">if</span> (value == <span class="hljs-string">"超时提示"</span>) &#123;
          <span class="hljs-built_in">this</span>.$message(&#123;
            <span class="hljs-attr">type</span>:<span class="hljs-string">"warning"</span>,
            <span class="hljs-attr">message</span>:<span class="hljs-string">"接口请求超时了"</span>
          &#125;)  
        &#125;<span class="hljs-keyword">else</span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'正常操作即可'</span>);
        &#125;
      &#125;)
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里就不打印了，结果和上图打印的类似</p>
</blockquote>
<h2 data-id="heading-6">总结</h2>
<ul>
<li>Promise.all接收的是数组，得到的结果也是数组，并且一一对应，也可以理解为Promise.all照顾跑的最慢的，最慢的跑完才结束。</li>
<li>Promise.race接收的也是数组，不过，得到的却是数组中跑的最快的那个，当最快的一跑完就立马结束。</li>
</ul></div>  
</div>
            