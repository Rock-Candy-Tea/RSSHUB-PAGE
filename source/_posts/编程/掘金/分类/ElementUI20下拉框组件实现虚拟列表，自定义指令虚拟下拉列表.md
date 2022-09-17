
---
title: 'ElementUI2.0下拉框组件实现虚拟列表，自定义指令虚拟下拉列表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36ea83c232474a16bca7bcd48d15cd58~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 22:00:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36ea83c232474a16bca7bcd48d15cd58~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<p>由于业务对页面性能要求很高，如果下拉框数据很大，如果一个页面有多个下拉框，那么就导致页面很卡顿。由于elementPlus已经支持了下拉组件虚拟列表，但是所在项目仍然使用elementUI2.0，所以需要自己扩展支持下拉组件虚拟列表，以下是笔者总结的一篇关于elementUI2.0支持下拉框虚拟列表的实践方案，希望看完在项目中有所帮助。</p>
<p>正文开始...</p>
<p>在开始本文之前，笔者主要会从以下方向上去实现该业务需求</p>
<p>1、尝试在原有<code>elementUI</code>组件上，写一个自定义指令，支持下拉虚拟列表</p>
<p>2、尝试使用社区成熟的<code>虚拟列表</code>插件方案实现虚拟列表</p>
<h3 data-id="heading-0">前置</h3>
<p>我们知道<code>虚拟列表</code>本质上就是在可视区域内显示对应的数据，由于数据是按需加载，所以我们首先就要明白如何实现虚拟列表，具体可以参考以前写的一篇文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzk0ODMxODIzNw%3D%3D%26mid%3D2247487858%26idx%3D1%26sn%3D7f7e5d6e3430438bcad17ca85c8d6c6f%26chksm%3Dc3682800f41fa1167e57552bb701483b760deeaa1cb3b2597e59064c4c02c80b78bf893a1e14%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=Mzk0ODMxODIzNw==&mid=2247487858&idx=1&sn=7f7e5d6e3430438bcad17ca85c8d6c6f&chksm=c3682800f41fa1167e57552bb701483b760deeaa1cb3b2597e59064c4c02c80b78bf893a1e14#rd" ref="nofollow noopener noreferrer">了解虚拟列表背后原理，轻松实现虚拟列表</a></p>
<h3 data-id="heading-1">快速实现页面</h3>
<p>我们是使用<code>vue-cli2</code>快速搭建了一个基本项目</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36ea83c232474a16bca7bcd48d15cd58~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer">
我们可以非常清晰的看到右侧下拉测试<code>100</code>条数据直接渲染出来的</p>
<p>我们看下实际代码</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"非虚拟列表-活动名称2"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-select</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"form.value"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请选择"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-option</span>
          <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in sourceData"</span>
          <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.value"</span>
          <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.label"</span>
          <span class="hljs-attr">:value</span>=<span class="hljs-string">"item.value"</span>
        ></span>
        <span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应数据就是在<code>created</code>中直接生成了一组<code>100</code>条数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'hello-word'</span>,
  <span class="hljs-title function_">data</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">sourceData</span>: []
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Array</span>(<span class="hljs-number">100</span>).<span class="hljs-title function_">fill</span>(<span class="hljs-number">1</span>);
    arr.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">v, index</span>) =></span> &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">sourceData</span>.<span class="hljs-title function_">push</span>(&#123;
        <span class="hljs-attr">value</span>: index,
        <span class="hljs-attr">label</span>: <span class="hljs-string">`test_<span class="hljs-subst">$&#123;index&#125;</span>`</span>
      &#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先看下左侧虚拟列表
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc9903763cff48a88290c2827323fb0b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下拉框并不是一次性渲染所有数据，而是按需获取可视区域的数据，这是如何实现的？</p>
<h3 data-id="heading-2">虚拟列表指令</h3>
<p>主要思路就是控制下拉数据显示条数，本质就是要控制<code>optionsData</code></p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"虚拟列表-活动名称"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-select</span>
        <span class="hljs-attr">v-model</span>=<span class="hljs-string">"form.value1"</span>
        <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请选择"</span>
        @<span class="hljs-attr">visible-change</span>=<span class="hljs-string">"handleVisibleChange"</span>
        <span class="hljs-attr">v-select</span>=<span class="hljs-string">"&#123; ...selectAttrs, data: sourceData &#125;"</span>
      ></span>
        <span class="hljs-tag"><<span class="hljs-name">el-option</span>
          <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in optionsData"</span>
          <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.value"</span>
          <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.label"</span>
          <span class="hljs-attr">:value</span>=<span class="hljs-string">"item.value"</span>
        ></span>
        <span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到<code>v-select</code>指令上主要有<code>data</code>,<code>selectAttrs</code>,<code>data</code>是原数据，<code>selectAttrs</code>主要是虚拟列表需要的参数</p>
<ul>
<li><code>selectAttrs</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'hello-world'</span>,
  <span class="hljs-title function_">data</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">sourceData</span>: [], <span class="hljs-comment">// 原始数据</span>
      <span class="hljs-attr">selectAttrs</span>: &#123;
        <span class="hljs-attr">viewHeight</span>: <span class="hljs-number">220</span>, <span class="hljs-comment">// 可视区域的高度</span>
        <span class="hljs-attr">rowHeight</span>: <span class="hljs-number">30</span>, <span class="hljs-comment">// 当前行的默认高度</span>
        <span class="hljs-attr">startIndex</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">endIndex</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">callback</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">updateOptions</span>,
        <span class="hljs-attr">scrollView</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 滚动容器</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从指令配置所需要的参数来看，主要是以下几个关键字段：</p>
<p><code>viewHeight</code>可视区域的高度</p>
<p><code>rowHeight</code>当前行的默认高度</p>
<p><code>startIndex</code>数据起始位置</p>
<p><code>endIndex</code>数据默认位置</p>
<p><code>callback</code>执行回调，主要是控制下拉数据</p>
<p><code>scrollView</code>监听滚动容器</p>
<p>然后我们看下指令是如何编写的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> selectDirectives = &#123;
  <span class="hljs-attr">wrap</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">fn</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">select</span>: &#123;
    inserted (el, binding, vnode) &#123;
      <span class="hljs-keyword">let</span> &#123; data, rowHeight, startIndex, callback, filterable &#125; = binding.<span class="hljs-property">value</span>;
      <span class="hljs-keyword">const</span> &#123;
        <span class="hljs-attr">componentInstance</span>: &#123; <span class="hljs-attr">$children</span>: children &#125;
      &#125; = vnode;
      <span class="hljs-keyword">const</span> selectDown = children[children.<span class="hljs-property">length</span> - <span class="hljs-number">1</span>];
      <span class="hljs-keyword">const</span> [elScrollBar] = selectDown.<span class="hljs-property">$children</span>;
      <span class="hljs-keyword">const</span> [wrap] = elScrollBar.<span class="hljs-property">$el</span>.<span class="hljs-property">childNodes</span>;
      <span class="hljs-keyword">const</span> scrollView = wrap.<span class="hljs-title function_">getElementsByClassName</span>(<span class="hljs-string">'el-scrollbar__view'</span>)[<span class="hljs-number">0</span>];
      <span class="hljs-keyword">const</span> total = data.<span class="hljs-property">length</span>; <span class="hljs-comment">// 所有数据的总条数</span>
      <span class="hljs-comment">// 设置el-scrollbar__view的高度</span>
      <span class="hljs-keyword">if</span> (filterable) &#123;
        scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">'auto'</span>;
      &#125; <span class="hljs-keyword">else</span> &#123;
        scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">`<span class="hljs-subst">$&#123;total * rowHeight&#125;</span>px`</span>;
      &#125;
      <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">const</span> <span class="hljs-title function_">fn</span> = (<span class="hljs-params"></span>) => &#123;
        <span class="hljs-keyword">if</span> (timer) &#123;
          <span class="hljs-keyword">return</span>;
        &#125;
        timer = <span class="hljs-literal">true</span>;
        <span class="hljs-keyword">const</span> requestId = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          timer = <span class="hljs-literal">false</span>;
          <span class="hljs-keyword">const</span> scrollTop = wrap.<span class="hljs-property">scrollTop</span>;
          <span class="hljs-comment">// 计算当前滚动位置，获取当前开始的起始位置</span>
          <span class="hljs-keyword">const</span> currentIndex = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(scrollTop / rowHeight);
          <span class="hljs-comment">// console.log(startIndex, 'startIndex222', currentIndex);</span>
          <span class="hljs-comment">// 根据滚动条获取当前索引与起始索引不相等时，将滚动的当前位置设置为起始位置</span>
          <span class="hljs-keyword">if</span> (currentIndex !== startIndex) &#123;
            startIndex = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">max</span>(currentIndex, <span class="hljs-number">0</span>);
          &#125;
          <span class="hljs-keyword">const</span> paddingTop = <span class="hljs-string">`<span class="hljs-subst">$&#123;startIndex * rowHeight&#125;</span>px`</span>;
          scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">paddingTop</span> = paddingTop;
          <span class="hljs-comment">// eslint-disable-next-line standard/no-callback-literal</span>
          <span class="hljs-title function_">callback</span>(&#123; startIndex, scrollView &#125;);
        &#125;, <span class="hljs-number">100</span>);
        <span class="hljs-keyword">if</span> (!requestId) &#123;
          <span class="hljs-built_in">clearTimeout</span>(requestId);
        &#125;
      &#125;;
      selectDirectives.<span class="hljs-property">fn</span> = fn;
      selectDirectives.<span class="hljs-property">wrap</span> = wrap;
      wrap.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'scroll'</span>, fn, <span class="hljs-literal">false</span>);
    &#125;,
    unbind () &#123;
      selectDirectives.<span class="hljs-property">wrap</span>.<span class="hljs-title function_">removeEventListener</span>(<span class="hljs-string">'scroll'</span>, selectDirectives.<span class="hljs-property">fn</span>);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关键的几点</p>
<p>1、找到内容滚动容器<code>wrap</code>，主要是通过<code>componentInstance</code>找到下拉滚动父容器</p>
<p>2、设置滚动容器内部高度<code>scrollView</code>【必须要设置】,不设置的话，内容数据将无法滚动显示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> &#123; data, rowHeight, startIndex, callback &#125; = binding.<span class="hljs-property">value</span>;
<span class="hljs-keyword">const</span> &#123;
  <span class="hljs-attr">componentInstance</span>: &#123; <span class="hljs-attr">$children</span>: children &#125;
&#125; = vnode;
<span class="hljs-keyword">const</span> selectDown = children[children.<span class="hljs-property">length</span> - <span class="hljs-number">1</span>];
<span class="hljs-keyword">const</span> [elScrollBar] = selectDown.<span class="hljs-property">$children</span>;
<span class="hljs-keyword">const</span> [wrap] = elScrollBar.<span class="hljs-property">$el</span>.<span class="hljs-property">childNodes</span>;
<span class="hljs-keyword">const</span> scrollView = wrap.<span class="hljs-title function_">getElementsByClassName</span>(<span class="hljs-string">'el-scrollbar__view'</span>)[<span class="hljs-number">0</span>];
<span class="hljs-keyword">const</span> total = data.<span class="hljs-property">length</span>; <span class="hljs-comment">// 所有数据的总条数</span>
<span class="hljs-comment">// 设置el-scrollbar__view的高度</span>
scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">`<span class="hljs-subst">$&#123;total * rowHeight&#125;</span>px`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用一张图还原一下，为什么需要设置<code>scrollView</code>的高度，以及当内部容器滚动时，我们需要给内部设置一个<code>paddingTop</code>,不然显示就会有空白块
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/549b80bd92c94292993537278b596f32~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、确定当前滚动的起始位</p>
<p>主要是当我们滚动容器时，根据滚动的位置确定起始位,核心代码如下</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> scrollTop = wrap.<span class="hljs-property">scrollTop</span>;
   <span class="hljs-comment">// 计算当前滚动位置，获取当前开始的起始位置</span>
  <span class="hljs-keyword">const</span> currentIndex = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(scrollTop / rowHeight);
  <span class="hljs-comment">// console.log(startIndex, 'startIndex222', currentIndex);</span>
  <span class="hljs-comment">// 根据滚动条获取当前索引与起始索引不相等时，将滚动的当前位置设置为起始位置</span>
  <span class="hljs-keyword">if</span> (currentIndex !== startIndex) &#123;
    startIndex = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">max</span>(currentIndex, <span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-keyword">const</span> paddingTop = <span class="hljs-string">`<span class="hljs-subst">$&#123;startIndex * rowHeight&#125;</span>px`</span>;
  scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">paddingTop</span> = paddingTop;
  <span class="hljs-comment">// eslint-disable-next-line standard/no-callback-literal</span>
  <span class="hljs-title function_">callback</span>(&#123; startIndex, scrollView &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、我们看到有<code>callback</code>执行回调返回出去了<code>startIndex</code>,<code>scrollView</code></p>
<p>所以从最初设计指令时，我们看到了指令的<code>selectAttrs</code>上有一个<code>callback</code></p>
<pre><code class="hljs language-js copyable" lang="js"> ...
 <span class="hljs-attr">selectAttrs</span>: &#123;
    <span class="hljs-attr">viewHeight</span>: <span class="hljs-number">250</span>, <span class="hljs-comment">// 可视区域的高度</span>
    <span class="hljs-attr">rowHeight</span>: <span class="hljs-number">30</span>, <span class="hljs-comment">// 当前行的默认高度</span>
    <span class="hljs-attr">startIndex</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">endIndex</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">callback</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">updateOptions</span>,
    <span class="hljs-attr">scrollView</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 滚动容器</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">指令执行回调</h3>
<p>主要看<code>updateOptions</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-attr">methods</span>: &#123;
  updateOptions (&#123; startIndex, scrollView &#125;) &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">selectAttrs</span>.<span class="hljs-property">startIndex</span> = startIndex;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">selectAttrs</span>.<span class="hljs-property">scrollView</span> = scrollView;
      <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">renderOptions</span>();
   &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看下<code>renderOptions</code>这个方法，主要是更新下拉框数据</p>
<pre><code class="hljs language-js copyable" lang="js">...
 renderOptions () &#123;
      <span class="hljs-keyword">let</span> &#123;
        <span class="hljs-attr">selectAttrs</span>: &#123; viewHeight, rowHeight, startIndex, endIndex &#125;,
        sourceData
      &#125; = <span class="hljs-variable language_">this</span>;
      <span class="hljs-keyword">const</span> total = sourceData.<span class="hljs-property">length</span>;
      <span class="hljs-comment">// 可视区域的条数</span>
      <span class="hljs-keyword">const</span> limit = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">ceil</span>(viewHeight / rowHeight);
      <span class="hljs-comment">// 设置末位索引</span>
      endIndex = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">min</span>(startIndex + limit, total);
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">selectAttrs</span>.<span class="hljs-property">endIndex</span> = endIndex;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">optionsData</span> = sourceData.<span class="hljs-title function_">slice</span>(startIndex, endIndex);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上比较关键的一行代码就是根据回调函数中的<code>startIndex</code>以及<code>limit</code>确认最后的<code>endIndex</code>,
以下是核心关键代码</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> limit = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">ceil</span>(viewHeight / rowHeight);
      <span class="hljs-comment">// 设置末位索引</span>
 endIndex = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">min</span>(startIndex + limit, total);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们就是根据起始位对愿数数据进行<code>slice</code>操作，确认真正需要显示的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">this</span>.<span class="hljs-property">optionsData</span> = sourceData.<span class="hljs-title function_">slice</span>(startIndex, endIndex);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应的页面显示</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">el-select</span>
    <span class="hljs-attr">v-model</span>=<span class="hljs-string">"form.value1"</span>
    <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请选择"</span>
    @<span class="hljs-attr">visible-change</span>=<span class="hljs-string">"handleVisibleChange"</span>
    <span class="hljs-attr">v-select</span>=<span class="hljs-string">"&#123; ...selectAttrs, data: sourceData &#125;"</span>
 ></span>
    <span class="hljs-tag"><<span class="hljs-name">el-option</span>
      <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in optionsData"</span>
      <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.value"</span>
      <span class="hljs-attr">:label</span>=<span class="hljs-string">"item.label"</span>
      <span class="hljs-attr">:value</span>=<span class="hljs-string">"item.value"</span>
    ></span>
    <span class="hljs-tag"></<span class="hljs-name">el-option</span>></span>
<span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们注意到，我们在下拉框下绑定了一个<code>@visible-change="handleVisibleChange"</code>方法，实际上只有我们在打开下拉框时才会需要触发更新下拉，所以我们需要调用<code>renderOptions</code></p>
<pre><code class="hljs language-js copyable" lang="js">...
 handleVisibleChange () &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">selectAttrs</span>: &#123; scrollView &#125;
    &#125; = <span class="hljs-variable language_">this</span>;
    <span class="hljs-comment">// 当打开下拉框时，重置scrollView的paadingTop,避免白屏</span>
    <span class="hljs-keyword">if</span> (scrollView) &#123;
      scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">paddingTop</span> = <span class="hljs-string">'0px'</span>;
    &#125;
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">renderOptions</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是我们注意到，这里我们重置了<code>scrollView</code>的<code>paddingTop</code>,因为我们在滚动时设置了<code>paddingTop</code>,所以此时我们需要重置<code>paddingTop</code>就是为了回显我们上次选择的内容区域</p>
<p>由于我们设置了内容器的高度，所以如果有设置过滤搜索，就会显示有问题，于是我们在过滤搜索时，就将高度置<code>auto</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> &#123; data, rowHeight, startIndex, callback, filterable &#125; = binding.<span class="hljs-property">value</span>;
<span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">componentInstance</span>: &#123; <span class="hljs-attr">$children</span>: children &#125;
 &#125; = vnode;
  <span class="hljs-keyword">const</span> selectDown = children[children.<span class="hljs-property">length</span> - <span class="hljs-number">1</span>];
  <span class="hljs-keyword">const</span> [elScrollBar] = selectDown.<span class="hljs-property">$children</span>;
  <span class="hljs-keyword">const</span> [wrap] = elScrollBar.<span class="hljs-property">$el</span>.<span class="hljs-property">childNodes</span>;
  <span class="hljs-keyword">const</span> scrollView = wrap.<span class="hljs-title function_">getElementsByClassName</span>(<span class="hljs-string">'el-scrollbar__view'</span>)[<span class="hljs-number">0</span>];
  <span class="hljs-keyword">const</span> total = data.<span class="hljs-property">length</span>; <span class="hljs-comment">// 所有数据的总条数</span>
  <span class="hljs-comment">// 设置el-scrollbar__view的高度</span>
<span class="hljs-keyword">if</span> (filterable) &#123;
    scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">'auto'</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    scrollView.<span class="hljs-property">style</span>.<span class="hljs-property">height</span> = <span class="hljs-string">`<span class="hljs-subst">$&#123;total * rowHeight&#125;</span>px`</span>;
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">挂载指令</h3>
<p>主要是局部注册就行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 指令</span>
<span class="hljs-keyword">const</span> selectDirectives = &#123;
  <span class="hljs-attr">wrap</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">fn</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">select</span>: &#123;
    inserted (el, binding, vnode) &#123;
    ...
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们需要挂在在当前单文件中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWorld'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Your Vue.js App'</span>,
      <span class="hljs-attr">form</span>: &#123;
        <span class="hljs-attr">value1</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">value2</span>: <span class="hljs-string">''</span>
      &#125;,
      <span class="hljs-attr">sourceData</span>: [],
      <span class="hljs-attr">optionsData</span>: [],
      <span class="hljs-attr">selectAttrs</span>: &#123;
        <span class="hljs-attr">viewHeight</span>: <span class="hljs-number">220</span>, <span class="hljs-comment">// 可视区域的高度</span>
        <span class="hljs-attr">rowHeight</span>: <span class="hljs-number">30</span>, <span class="hljs-comment">// 当前行的默认高度</span>
        <span class="hljs-attr">startIndex</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">endIndex</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">callback</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">updateOptions</span>,
        <span class="hljs-attr">scrollView</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 滚动容器</span>
        <span class="hljs-attr">filterable</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;;
  &#125;,
  <span class="hljs-attr">directives</span>: selectDirectives,
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终结果就是下面这样了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/168a68ad2e8a47e8af3a2bea37e1e88f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">vue-virtual-scroll-list插件实现虚拟列表</h3>
<p>在以上例子中我们尝试用自己写的指令已经满足虚拟列表，那如果不用自己写的指令，使用社区的方案，会不会更快，更简单呢？我们考虑主要是用这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftangbc%2Fvue-virtual-scroll-list" title="https://github.com/tangbc/vue-virtual-scroll-list" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">社区插件</a>，实现起来就更简单</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hello"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-form</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"form"</span> <span class="hljs-attr">:model</span>=<span class="hljs-string">"form"</span> <span class="hljs-attr">inline</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-form-item</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"活动名称"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-select</span>
          <span class="hljs-attr">v-model</span>=<span class="hljs-string">"form.value"</span>
          <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请选择"</span>
          @<span class="hljs-attr">visible-change</span>=<span class="hljs-string">"handleVisibleChange"</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">"select"</span>
        ></span>
          <span class="hljs-tag"><<span class="hljs-name">virtual-list</span>
            <span class="hljs-attr">:data-key</span>=<span class="hljs-string">"'id'"</span>
            <span class="hljs-attr">:data-sources</span>=<span class="hljs-string">"sourceData"</span>
            <span class="hljs-attr">:data-component</span>=<span class="hljs-string">"optionComponent"</span>
            <span class="hljs-attr">:keeps</span>=<span class="hljs-string">"10"</span>
            <span class="hljs-attr">:extra-props</span>=<span class="hljs-string">"extraProps"</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">"max-height: 245px; overflow-y: auto;"</span>
          ></span>
          <span class="hljs-tag"></<span class="hljs-name">virtual-list</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">el-select</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-form-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-form</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入<code>vue-virtual-scroll-list</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> virtualList <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-virtual-scroll-list'</span>;
<span class="hljs-keyword">const</span> optionComponent = &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">source</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-title class_">Object</span>,
      <span class="hljs-keyword">default</span> () &#123;
        <span class="hljs-keyword">return</span> &#123;&#125;;
      &#125;
    &#125;,
    <span class="hljs-attr">label</span>: <span class="hljs-title class_">String</span>,
    <span class="hljs-attr">value</span>: <span class="hljs-title class_">String</span>
  &#125;,
  <span class="hljs-attr">template</span>:
    <span class="hljs-string">'<el-option :label="source[label]" :value="source[value]"></el-option>'</span>
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWorld'</span>,
  <span class="hljs-attr">components</span>: &#123;
    virtualList
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Your Vue.js App'</span>,
      <span class="hljs-attr">form</span>: &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>
      &#125;,
      optionComponent,
      <span class="hljs-attr">sourceData</span>: [],
      <span class="hljs-attr">extraProps</span>: &#123;
        <span class="hljs-attr">label</span>: <span class="hljs-string">'label'</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-string">'value'</span>
      &#125;
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    handleVisibleChange () &#123;
      <span class="hljs-keyword">const</span> select = <span class="hljs-variable language_">this</span>.<span class="hljs-property">$refs</span>.<span class="hljs-property">select</span>;
      <span class="hljs-keyword">const</span> child = select.<span class="hljs-property">$children</span>;
      <span class="hljs-keyword">const</span> [, selectDrop] = child;
      <span class="hljs-keyword">const</span> [cchild] = selectDrop.<span class="hljs-property">$children</span>;
      <span class="hljs-keyword">const</span> [a] = cchild.<span class="hljs-property">$children</span>;
      <span class="hljs-keyword">const</span> [group] = a.<span class="hljs-property">$el</span>.<span class="hljs-property">children</span>;
      group.<span class="hljs-property">style</span>.<span class="hljs-property">paddingTop</span> = <span class="hljs-string">'0px'</span>;
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(group);
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Array</span>(<span class="hljs-number">100</span>).<span class="hljs-title function_">fill</span>(<span class="hljs-number">1</span>);
    arr.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">v, index</span>) =></span> &#123;
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">sourceData</span>.<span class="hljs-title function_">push</span>(&#123;
        <span class="hljs-attr">value</span>: index,
        <span class="hljs-attr">label</span>: <span class="hljs-string">`test_<span class="hljs-subst">$&#123;index&#125;</span>`</span>,
        <span class="hljs-attr">id</span>: <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>()
      &#125;);
    &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们注意到<code>handleVisibleChange</code>同样是将滚动容器的<code>paddingTop</code>置零了，这样保证，打开下拉框时不会白屏。</p>
<p>并且如果是用插件，就必须要有<code>id</code>,<code>virtual-list</code>上指定<code>data-key</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e26a63097bee420680ad73c151ef004a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">总结</h3>
<ul>
<li>
<p>主要是写了一个指令，在<code>elementUI</code>的<code>select</code>组件上支持虚拟列表展示，我们在项目使用自定义指令支持下拉框的虚拟列表</p>
</li>
<li>
<p>使用第三方插件<code>vue-virtual-scroll-list</code>实现虚拟列表</p>
</li>
<li>
<p>本文实例源码<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FmaicFir%2FlessonNote%2Ftree%2Fmaster%2Fvue%2F04-select%25E4%25B8%258B%25E6%258B%2589%25E6%25A1%2586%25E8%2599%259A%25E6%258B%259F%25E5%2588%2597%25E8%25A1%25A8%26%25E6%258B%2596%25E6%258B%25BD%2Felem-select" title="https://github.com/maicFir/lessonNote/tree/master/vue/04-select%E4%B8%8B%E6%8B%89%E6%A1%86%E8%99%9A%E6%8B%9F%E5%88%97%E8%A1%A8&%E6%8B%96%E6%8B%BD/elem-select" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">code example</a></p>
</li>
<li>
<p>个人比较推荐社区优秀成熟的第三方库去满足我们的业务，自己虽然手写了一个指令支持虚拟列表，但是在业务时间紧凑的情况下，肯定优先使用插件，除非插件不满足我们自己的业务需求，那么只能自己造轮子了。</p>
</li>
</ul></div>  
</div>
            