
---
title: '【Vue3 从入门到实战 进阶式掌握完整知识体系】024-Vue中的高级语法：Mixin混入的基础语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a4951049c3494ab69be9da7b4428a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 05:51:21 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a4951049c3494ab69be9da7b4428a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">五、Vue中的高级语法</h1>
<h2 data-id="heading-1">1、Mixin混入的基础语法</h2>
<blockquote>
<p>不推荐使用全局 mixin，vue3之后就不推荐使用 mixin 了，组合式 api 取代 mixin ， mixin 的可维护性不高！</p>
</blockquote>
<h3 data-id="heading-2">混入data</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Minxin 混入</span>
  <span class="hljs-keyword">const</span> mymixin = &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">100</span>
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// mixins：我们知道 vue实例自身数据里面有个 num 这里又混入一个 num</span>
    <span class="hljs-comment">// 当混入的内容与组件原有内容有冲突时，优先使用原有的内容</span>
    <span class="hljs-comment">// 当组件原有内容不存在混入的内容时，使用混入的内容</span>
    <span class="hljs-comment">// 优先级：组件 data > mixin data</span>
    <span class="hljs-attr">mixins</span>: [mymixin],
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"handleClick"</span>);
      &#125;
    &#125;,
    <span class="hljs-comment">// num 组件数据里面有，使用组件里面的 1</span>
    <span class="hljs-comment">// count 组件数据里面没有，就是用混入里面的 100</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;num&#125;&#125;</div>
          <div>&#123;&#123;count&#125;&#125;</div>
          <button @click="handleClick">点击</button>
        </div>
    `</span>
  &#125;);

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">运行结果</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42a4951049c3494ab69be9da7b4428a1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614095009285.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">混入生命周期函数</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Minxin 混入</span>
  <span class="hljs-keyword">const</span> mymixin = &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">100</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// 混入生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入生命周期函数：created"</span>);
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// mixins：我们知道 vue实例自身数据里面有个 num 这里又混入一个 num</span>
    <span class="hljs-comment">// 当混入的内容与组件原有内容有冲突时，优先使用原有的内容</span>
    <span class="hljs-comment">// 当组件原有内容不存在混入的内容时，使用混入的内容</span>
    <span class="hljs-comment">// 优先级：组件 data > mixin data</span>
    <span class="hljs-attr">mixins</span>: [mymixin],
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"handleClick"</span>);
      &#125;
    &#125;,
    <span class="hljs-comment">// num 组件数据里面有，使用组件里面的 1</span>
    <span class="hljs-comment">// count 组件数据里面没有，就是用混入里面的 100</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;num&#125;&#125;</div>
          <div>&#123;&#123;count&#125;&#125;</div>
          <button @click="handleClick">点击</button>
        </div>
    `</span>
  &#125;);

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">运行结果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b26aeeecf84f0f8072a32e15a8ecab~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614095204466.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">组件和混入同时存在同一生命周期函数</h3>
<blockquote>
<p>都会执行：先执行混入的生命周期函数，后执行组件的生命周期函数</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Minxin 混入</span>
  <span class="hljs-keyword">const</span> mymixin = &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">100</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// 混入生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入生命周期函数：created"</span>);
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// mixins：我们知道 vue实例自身数据里面有个 num 这里又混入一个 num</span>
    <span class="hljs-comment">// 当混入的内容与组件原有内容有冲突时，优先使用原有的内容</span>
    <span class="hljs-comment">// 当组件原有内容不存在混入的内容时，使用混入的内容</span>
    <span class="hljs-comment">// 优先级：组件 data > mixin data</span>
    <span class="hljs-attr">mixins</span>: [mymixin],
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"handleClick"</span>);
      &#125;
    &#125;,
    <span class="hljs-comment">// 组件生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"组件生命周期函数：created"</span>);
    &#125;,
    <span class="hljs-comment">// num 组件数据里面有，使用组件里面的 1</span>
    <span class="hljs-comment">// count 组件数据里面没有，就是用混入里面的 100</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;num&#125;&#125;</div>
          <div>&#123;&#123;count&#125;&#125;</div>
          <button @click="handleClick">点击</button>
        </div>
    `</span>
  &#125;);

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">运行结果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8926606c12da4b3b9a340cfd0e269c02~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614095440099.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">混入方法</h3>
<blockquote>
<p>类似混入data，优先级：组件内的方法 > 混入的方法；</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Minxin 混入</span>
  <span class="hljs-keyword">const</span> mymixin = &#123;
    <span class="hljs-comment">// 混入数据</span>
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">100</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// 混入生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入生命周期函数：created"</span>);
    &#125;,
    <span class="hljs-comment">// 混入方法</span>
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-comment">// 组件内存在的方法</span>
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入的handleClick"</span>);
      &#125;,
      <span class="hljs-comment">// 组件内不存在的方法</span>
      <span class="hljs-function"><span class="hljs-title">handleClick2</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入的handleClick2"</span>);
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// mixins：我们知道 vue实例自身数据里面有个 num 这里又混入一个 num</span>
    <span class="hljs-comment">// 当混入的内容与组件原有内容有冲突时，优先使用原有的内容</span>
    <span class="hljs-comment">// 当组件原有内容不存在混入的内容时，使用混入的内容</span>
    <span class="hljs-comment">// 优先级：组件 data > mixin data</span>
    <span class="hljs-attr">mixins</span>: [mymixin],
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"handleClick"</span>);
      &#125;
    &#125;,
    <span class="hljs-comment">// 组件生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"组件生命周期函数：created"</span>);
    &#125;,
    <span class="hljs-comment">// num 组件数据里面有，使用组件里面的 1</span>
    <span class="hljs-comment">// count 组件数据里面没有，就是用混入里面的 100</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;num&#125;&#125;</div>
          <div>&#123;&#123;count&#125;&#125;</div>
          <button @click="handleClick(), handleClick2()">点击</button>
        </div>
    `</span>
  &#125;);

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">运行结果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d3514bd32484928bbd93143d4e28337~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614100029044.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">使用全局Mixin</h3>
<blockquote>
<p>全局的Maixin不推荐使用！</p>
</blockquote>
<blockquote>
<p>默认再父组件引入的 mixin 无法在子组件里面使用，需要子组件也引入，当前我们定义的 mixin 是局部的 mixin ，让我们来定义全局的 mixin ， 全局的 mixin 和全局组件非常类似！</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// 不需要引入了</span>
    <span class="hljs-comment">// mixins: [mymixin],</span>
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"handleClick"</span>);
      &#125;
    &#125;,
    <span class="hljs-comment">// 组件生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"组件生命周期函数：created"</span>);
    &#125;,
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;num&#125;&#125;</div>
          <div>&#123;&#123;count&#125;&#125;</div>
          <child />
          <button @click="handleClick(), handleClick2()">点击</button>
        </div>
    `</span>
  &#125;);

  <span class="hljs-comment">// 定义全局 mixin</span>
  app.mixin(&#123;
    <span class="hljs-comment">// 混入数据</span>
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>&#123;
        <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">100</span>
      &#125;
    &#125;,
    <span class="hljs-comment">// 混入生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入生命周期函数：created"</span>);
    &#125;,
    <span class="hljs-comment">// 混入方法</span>
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-comment">// 组件内存在的方法</span>
      <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入的handleClick"</span>);
      &#125;,
      <span class="hljs-comment">// 组件内不存在的方法</span>
      <span class="hljs-function"><span class="hljs-title">handleClick2</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"混入的handleClick2"</span>);
      &#125;
    &#125;
  &#125;);

  <span class="hljs-comment">// 定义子组件</span>
  app.component(<span class="hljs-string">"child"</span>, &#123;
    <span class="hljs-comment">// 不需要引入了</span>
    <span class="hljs-comment">// mixins: [mymixin],</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
      <div> 子组件里混入的count：&#123;&#123;count&#125;&#125;</div>
    `</span>
  &#125;);

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">运行结果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/998f649b67944c0c9a4e41d303454f98~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614102001166.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">自定义属性</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Minxin 混入</span>
  <span class="hljs-keyword">const</span> mymixin = &#123;
    <span class="hljs-comment">// 自定义一个 num 属性，注意这个 num 不在 data 里面</span>
    <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
  &#125;
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-comment">// 自定义一个 num 属性，注意这个 num 不在 data 里面</span>
    <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">mixins</span>: [mymixin],
    <span class="hljs-comment">// 自定义的属性，在插值语法中要使用 this.@options.num 使用</span>
    <span class="hljs-comment">// 所有的属性都会挂载在 this.$options 上</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;this.$options.num&#125;&#125;</div>
        </div>
    `</span>
  &#125;);

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">运行结果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a901f3da1ab486f91eb034a4054238c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614102817081.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">修改自定义属性的优先级</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-comment"><!-- 引入Vue库 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// Minxin 混入</span>
  <span class="hljs-keyword">const</span> mymixin = &#123;
    <span class="hljs-comment">// 自定义一个 num 属性，注意这个 num 不在 data 里面</span>
    <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,
  &#125;
  <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;
    <span class="hljs-comment">// 自定义一个 num 属性，注意这个 num 不在 data 里面</span>
    <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">mixins</span>: [mymixin],
    <span class="hljs-comment">// 自定义的属性，在插值语法中要使用 this.@options.num 使用</span>
    <span class="hljs-comment">// 所有的属性都会挂载在 this.$options 上</span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
        <div>
          <div>&#123;&#123;this.$options.num&#125;&#125;</div>
        </div>
    `</span>
  &#125;);

  app.config.optionMergeStrategies.num = <span class="hljs-function">(<span class="hljs-params">mixinValue, appValue</span>) =></span> &#123;
    <span class="hljs-comment">// 优先返回 mixinValue</span>
    <span class="hljs-keyword">return</span> mixinValue || appValue;
  &#125;

  <span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">'#root'</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">运行结果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a074c7dbc41049edacead88cadd66093~tplv-k3u1fbpfcp-watermark.image" alt="image-20210614103328008.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            