
---
title: 'vue中的v-model 与 .sync'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8441'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 23:15:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=8441'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>.sync与v-model的相同点和区别是</p>
<p>相同点：都是语法糖，都可以实现父子组件中的数据的双向通信。</p>
<p>区别点：
格式不同。</p>
<p>v-model="num",
:num.sync="num"
v-model： @input + value
:num.sync: @update:num
v-model只能用一次；.sync可以有多个。
.sync  相当于绑定了自定义属性a，和一个自定义事件@upadte:a</p>
<pre><code class="hljs language-js copyable" lang="js">
父组件
 
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">MyCom</span> <span class="hljs-attr">:a.sync</span>=<span class="hljs-string">'num'</span>/></span>
    // <span class="hljs-tag"><<span class="hljs-name">MyCom</span> <span class="hljs-attr">:a</span>=<span class="hljs-string">'num'</span> @<span class="hljs-attr">upadte:a</span>=<span class="hljs-string">'val=>num=val'</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> MyCom <span class="hljs-keyword">from</span> <span class="hljs-string">'./MyCom.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">compontents</span>:&#123;MyCom&#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">num</span>:<span class="hljs-number">100</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(<span class="hljs-string">'f'</span>)
    &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
 
子组件 <MyCom>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  自定义组件
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'$emit('</span><span class="hljs-attr">update:a</span>',<span class="hljs-attr">a</span>=<span class="hljs-string">1)</span>'></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">a</span>:&#123;<span class="hljs-attr">type</span>:<span class="hljs-built_in">Number</span>,<span class="hljs-attr">required</span>:<span class="hljs-literal">true</span>&#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
v-model 相当于绑定了自定义属性value和input事件

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">
父组件
 
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">MyCom</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">'num'</span>/></span>
    // <span class="hljs-tag"><<span class="hljs-name">MyCom</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">'num'</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">'val=>num=val'</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> MyCom <span class="hljs-keyword">from</span> <span class="hljs-string">'./MyCom.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">compontents</span>:&#123;MyCom&#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">num</span>:<span class="hljs-number">100</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(<span class="hljs-string">'f'</span>)
    &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
 
子组件 <MyCom>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  自定义组件
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'$emit('</span><span class="hljs-attr">input</span>',<span class="hljs-attr">value</span>=<span class="hljs-string">1)</span>'></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">value</span>:&#123;<span class="hljs-attr">type</span>:<span class="hljs-built_in">Number</span>,<span class="hljs-attr">required</span>:<span class="hljs-literal">true</span>&#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            