
---
title: '关于写vue时候发现的那些坑（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f02daefae1ab431b8eea2ecf7cc29946~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 02:29:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f02daefae1ab431b8eea2ecf7cc29946~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇来讲一下修饰符，也算是比较细节的一些地方，用得恰当能省下不少函数封装代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f02daefae1ab431b8eea2ecf7cc29946~tplv-k3u1fbpfcp-watermark.image" alt="pexels-tima-miroshnichenko-5380664.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">v-model的三个修饰符</h1>
<h2 data-id="heading-1">1. v-model.number</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num"</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>数字&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
   data () &#123;
     <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-attr">num</span>: <span class="hljs-number">0</span>,
     &#125;
   &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如图所示，众所周知，这是很基础很常见的输入框，现在他的初始值是0，旁边的span也会是0。那现在我们去掉0，改成任意的字符或者在0后面加上1，“01”，那么我们会发现span和input都变成了输入的字符或者"01"。我们的需求是限制用户输入只能为数字，方法多种，但多数都需要函数，如果我们改成下面这种，那就省事很多。话不多说，贴图，往你脸上贴那种。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.number</span>=<span class="hljs-string">"num"</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>数字&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
   data () &#123;
     <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-attr">num</span>: <span class="hljs-number">0</span>,
     &#125;
   &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>呐，在v-model后面加上.number就可以限制输入的类型必须为数字了。本系列第一篇文章当中，也有类似的需求，咱使用el-input-number组件做了些小花招。那个和这里区别就是，这里输入内容就会去判断类型，el-input-number组件则是在blur事件后判断，也就是input失去焦点的时候。但这不是说，el-input-number那种方式就不好，但就小数点精确后两位这种场景，还是用el-input-number更香。
顺便附上前面两章地址。
<a href="https://juejin.cn/post/6977736244570783751" target="_blank" title="https://juejin.cn/post/6977736244570783751">关于写vue时候发现的那些坑（一）</a>，
<a href="https://juejin.cn/post/6988148874770645022" target="_blank" title="https://juejin.cn/post/6988148874770645022">关于写vue时候发现的那些坑（二）</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/104506cda1df46ccb272d3773937068c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2. v-mdel.trim</h2>
<p>同样是input输入框，现在有个用户需求，就是用户在输入框输入查询条件的时候要去除前后空格。比方说在商品列表，用户输入了商品名称，但是不巧，人家是在和好基友聊天的时候，好基友给推荐的某款耳机，把名字发给他就是不发地址。他也懒的敲，然后直接复制了名字，在商品列表查询。也不知道微信改了啥，好家伙，复制出来的名称前面后面都有空格，虽然商品也查出来了，但是输入框里面这名字没贴边，好家伙，强迫症难受。那么，作为前端的在座各位，该怎么做？哎，贴图！呸，贴代码！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.trim</span>=<span class="hljs-string">"name"</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>商品名称&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
   data () &#123;
     <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
     &#125;
   &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加了.trim修饰符，就可以实现去除前后空格的效果，那么有人会说了，那我中间加个空格咧，那不行。只针对前后空格，中间空格其实相当于内容了。</p>
<h2 data-id="heading-3">3. v-model.lazy</h2>
<p>哎，这是用来干啥的，我们发现每次在input输入内容，vue都会实时更新，这点可以用vue-devtools工具看到实时的数据变化，一改就更新。就是这工具。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d089784f2c542d4af139046363cf379~tplv-k3u1fbpfcp-watermark.image" alt="devtools.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么假如团队来个需求，要你做像百度那样，输入就马上发送请求获取数据那种，但是服务器负载能力又有限，又或者团队希望，用户输完在发生请求，且如果第二次输入的内容和第一次一致，则不发生请求。用户场景，举个例子，用户想买衣服，比如碎花裙，输入框只会在碎花裙输完再去获取请求，然后用户又输入了一次碎花裙，此时不发生请求。只会在内容变化完成之后才会发送请求。那么此时就是.lazy出场了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.lazy</span>=<span class="hljs-string">"name"</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>商品名称&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
   data () &#123;
     <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
     &#125;
   &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码如上所示，.lazy不会马上更新数据，它只会在change事件之后在更新。第一次name的初始值是空串，所以当你输入碎花裙，则发送请求，然后第二次在输入碎花裙，则不发生请求。</p>
<p>以上，是v-model的修饰符，希望对你有用！</p></div>  
</div>
            