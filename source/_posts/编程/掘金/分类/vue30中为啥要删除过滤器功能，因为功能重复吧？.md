
---
title: 'vue3.0中为啥要删除过滤器功能，因为功能重复吧？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6132e973caee431a9cf58e1f94c72da4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 19:38:01 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6132e973caee431a9cf58e1f94c72da4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">问题描述</h2>
<p>去年，也就是2020年9月份，vue3出来了。增加了很多新功能，但是也删掉了一些功能。比如删掉了vue2中的过滤器filter功能。与此同时，官方建议：<code>用方法调用或计算属性替换过滤器。</code></p>
<h3 data-id="heading-1">什么是vue的过滤器</h3>
<p>过滤器可以通俗理解成是一个特殊的方法，用来加工数据的</p>
<ul>
<li>比如枚举值可以使用过滤器：如 1 2 3 4 对应 成功 失败 进行中 已退回</li>
<li>比如价格后面跟个过滤器，将价格格式化成小数点两位</li>
<li>比如时间格式化等</li>
</ul>
<blockquote>
<p>详细请看官方文档</p>
</blockquote>
<h3 data-id="heading-2">why？</h3>
<p>笔者认为：原因就是vue3要精简代码，并且filter功能重复，filter能实现的功能，methods和计算属性基本上也可以实现。所以就干脆把filter这方面的vue源码给删掉，这样的话，更加方便维护。</p>
<h2 data-id="heading-3">举例分析</h2>
<h3 data-id="heading-4">需求描述</h3>
<p>假设我们有一个快递信息，后端返回给我们的并不是具体的状态值，而是对应的字符串1 2 3 4 5 6等，不同的状态有着一套对应规则，比如状态为1是待发货等，具体效果图和状态对应关系如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6132e973caee431a9cf58e1f94c72da4~tplv-k3u1fbpfcp-watermark.image" alt="snipaste_20210509_110239.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">HTML结构和data数据如下</h3>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in arr"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>快递公司:&#123;&#123; item.deliverCompany &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>运输状态:&#123;&#123; item.expressState &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">arr</span>: [
        &#123;
          <span class="hljs-attr">deliverCompany</span>: <span class="hljs-string">"京东快递"</span>,
          <span class="hljs-attr">expressState</span>: <span class="hljs-string">"1"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">deliverCompany</span>: <span class="hljs-string">"顺丰快递"</span>,
          <span class="hljs-attr">expressState</span>: <span class="hljs-string">"2"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">deliverCompany</span>: <span class="hljs-string">"中通快递"</span>,
          <span class="hljs-attr">expressState</span>: <span class="hljs-string">"3"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">deliverCompany</span>: <span class="hljs-string">"邮政快递"</span>,
          <span class="hljs-attr">expressState</span>: <span class="hljs-string">"4"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">deliverCompany</span>: <span class="hljs-string">"极兔快递"</span>,
          <span class="hljs-attr">expressState</span>: <span class="hljs-string">"5"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">deliverCompany</span>: <span class="hljs-string">"某某快递"</span>,
          <span class="hljs-attr">expressState</span>: <span class="hljs-literal">null</span>,
        &#125;,
      ],
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">使用filter实现</h3>
<blockquote>
<p>这里我们就不用全局filter了，使用组件内部的filter</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in arr"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>快递公司:&#123;&#123; item.deliverCompany &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-comment"><!-- 使用过滤器语法 --></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>运输状态:&#123;&#123; item.expressState | showState &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// data ...... 篇幅有限直接省略掉</span>
  <span class="hljs-comment">// 在组件内定义，然后根据不同的状态返回不同的值内容</span>
  <span class="hljs-attr">filters</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">showState</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">switch</span> (state) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"1"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"待发货"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"2"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"已发货"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"3"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"运输中"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"4"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"派件中"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"5"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"已收货"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"快递信息丢失"</span>;
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">使用computed实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in arr"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>快递公司:&#123;&#123; item.deliverCompany &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-comment"><!-- 使用计算属性 --></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>运输状态:&#123;&#123; computedText(item.expressState) &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// data ...... 篇幅有限直接省略掉</span>
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">computedText</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 计算属性要return一个函数接收参数</span>
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">state</span>) </span>&#123;
        <span class="hljs-keyword">switch</span> (state) &#123;
          <span class="hljs-keyword">case</span> <span class="hljs-string">"1"</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">"待发货"</span>;
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">case</span> <span class="hljs-string">"2"</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">"已发货"</span>;
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">case</span> <span class="hljs-string">"3"</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">"运输中"</span>;
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">case</span> <span class="hljs-string">"4"</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">"派件中"</span>;
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">case</span> <span class="hljs-string">"5"</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">"已收货"</span>;
            <span class="hljs-keyword">break</span>;
          <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">"快递信息丢失"</span>;
            <span class="hljs-keyword">break</span>;
        &#125;
      &#125;;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用methods实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in arr"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>快递公司:&#123;&#123; item.deliverCompany &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-comment"><!-- 使用方法 --></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span>运输状态:&#123;&#123; methodsText(item.expressState) &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// data ...... 篇幅有限直接省略掉</span>
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">methodsText</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">switch</span> (state) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"1"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"待发货"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"2"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"已发货"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"3"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"运输中"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"4"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"派件中"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"5"</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"已收货"</span>;
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>:
          <span class="hljs-keyword">return</span> <span class="hljs-string">"快递信息丢失"</span>;
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>看到了叭，filter过滤器能加工数据，computed计算属性和methods方法也都可以加工数据，这样的话，就重复了...</p>
</blockquote>
<h2 data-id="heading-9">总结</h2>
<p><strong>vue3删除了filter就好比：</strong></p>
<p>员工filter会干的活，员工computed和员工methods也会干，而且比员工filter干得多，干的好。这样的话，老板vue就把filter开除了，filter就被fired了。毕竟多一个员工，多一些用工成本（员工filter哇的一声哭了出来）</p></div>  
</div>
            