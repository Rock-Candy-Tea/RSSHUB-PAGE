
---
title: '2021年了，还在vue中用this获取data中的变量？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57fdb2b047c8467aadf9ad4506ccfb70~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 18:54:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57fdb2b047c8467aadf9ad4506ccfb70~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先来上图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57fdb2b047c8467aadf9ad4506ccfb70~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01316ff5918a4344b754ab25c31cbb22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是两个测试vue渲染速度的页面，源码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; mm &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; nn &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; time &#125;&#125; s<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"sum"</span>></span>点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">mm</span>: <span class="hljs-number">321</span>,
      <span class="hljs-attr">nn</span>: <span class="hljs-number">123</span>,
      <span class="hljs-attr">time</span>: <span class="hljs-number">0</span>,
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// sum() &#123;</span>
    <span class="hljs-comment">//   let start, end</span>
    <span class="hljs-comment">//   start = window.performance.now()</span>
    <span class="hljs-comment">//   var a = new Array(10000000)</span>
    <span class="hljs-comment">//   a.fill(1)</span>
    <span class="hljs-comment">//   a.forEach(item => &#123;</span>
    <span class="hljs-comment">//     this.mm += 1</span>
    <span class="hljs-comment">//     this.nn += 1</span>
    <span class="hljs-comment">//   &#125;)</span>
    <span class="hljs-comment">//   this.$nextTick(() => &#123;</span>
    <span class="hljs-comment">//     end = window.performance.now()</span>
    <span class="hljs-comment">//     this.time = (end - start) / 1000</span>
    <span class="hljs-comment">//   &#125;)</span>
    <span class="hljs-comment">// &#125;,</span>
    <span class="hljs-function"><span class="hljs-title">sum</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> start, end;
      start = <span class="hljs-built_in">window</span>.performance.now();
      <span class="hljs-keyword">let</span> &#123; mm, nn &#125; = <span class="hljs-built_in">this</span>;
      <span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">10000000</span>);
      a.fill(<span class="hljs-number">1</span>);
      a.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        mm += <span class="hljs-number">1</span>;
        nn += <span class="hljs-number">1</span>;
      &#125;);
      <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>, &#123; mm, nn &#125;);
      <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
        end = <span class="hljs-built_in">window</span>.performance.now();
        <span class="hljs-built_in">this</span>.time = (end - start) / <span class="hljs-number">1000</span>;
      &#125;);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以知道，第二次的渲染时间只要0.1s，相比第一次提升巨大，推荐大家采用第二种写法哦！</p></div>  
</div>
            