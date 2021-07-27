
---
title: 'vue2.0  笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46fd880fcb524b09baa37ae4138b26f2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 01:53:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46fd880fcb524b09baa37ae4138b26f2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue传入的对象option</h1>
<h5 data-id="heading-1">1. el：</h5>
<ul>
<li>①类型：string | HTMLElement</li>
<li>②作用：决定管理哪个DOM对象</li>
</ul>
<h5 data-id="heading-2">2. data:</h5>
<ul>
<li>①类型：Object | Function（<strong>组件当中data必须是一个函数</strong>）</li>
<li>②作用：Vue实例对应的数据对象</li>
</ul>
<h5 data-id="heading-3">3. methods：</h5>
<ul>
<li>①类型：&#123;[key:string]:Function&#125;</li>
<li>②作用：定义属于Vue的方法，可以在其他地方调用，也可以在指令中调用</li>
</ul>
<h5 data-id="heading-4">4. watch：</h5>
<ul>
<li>①类型：&#123;[key:string]: Function | Object&#125;</li>
<li>②作用：监听器作用，监听某个数据或者方法等的变化而执行的副作用</li>
</ul>
<h1 data-id="heading-5">一、Vue基本语法</h1>
<h2 data-id="heading-6">1、插值操作</h2>
<h3 data-id="heading-7">1-1、Mustache语法（双大括号）</h3>
<p>不仅可以直接写变量，还可以写简单表达式</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- Mustache的语法不仅可以直接写变量，还可以写简单表达式 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;firstName + " " + lastName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span> // kevin durant
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;firstName&#125;&#125; &#123;&#123;lastName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>     // kevin durant
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;count * 2&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>     // 200
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">firstName</span>:<span class="hljs-string">"kevin"</span>,
        <span class="hljs-attr">lastName</span>:<span class="hljs-string">"durant"</span>,
        <span class="hljs-attr">count</span>:<span class="hljs-number">100</span>
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1-2、v-once</h3>
<p>只渲染一次，不随着数据改变而改变。
后面不跟表达式。</p>
<h3 data-id="heading-9">1-3、v-html</h3>
<p>识别 html 标签</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"url"</span>></span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">url</span>:<span class="hljs-string">"<a href='http://www.baidu.com'>百度一下</a>"</span>
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">1-4、v-text</h3>
<p>v-text作用和Mustache比较相似：都是用于将数据显示在界面中
v-text通常情况下，接受一个string类型</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">"你好啊"</span>
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但一般不用，不够灵活。</p>
<h3 data-id="heading-11">1-5、v-pre</h3>
<p>不跟表达式
直接将文本原封不动显示出来</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>        // 你好啊
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">v-pre</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  // &#123;&#123;message&#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">"你好啊"</span>
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">1-6、v-cloak</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span> <span class="hljs-attr">v-cloak</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
// 在vue解析之前，该div有v-cloak属性
// 在vue解析之后，自动删掉v-cloak属性
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">2、绑定属性</h2>
<h3 data-id="heading-14">2-1、v-bind</h3>
<p>v-bind用于绑定一个或多个属性值，或者向另一个组件传递props值
对一些属性进行动态绑定，比如图片的链接src、网站的链接href、动态绑定一些类、样式等等。</p>

























<table><thead><tr><th>v-bind</th><th>Value</th></tr></thead><tbody><tr><td>作用</td><td>动态绑定属性</td></tr><tr><td>缩写</td><td>: （语法糖）</td></tr><tr><td>预期</td><td>any (with argument)</td></tr><tr><td>参数</td><td>attrOrProp (optional)</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">v-bind:src</span>=<span class="hljs-string">"imgURL"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-bind:href</span>=<span class="hljs-string">"aHerf"</span>></span>百度一下<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-comment"><!-- 语法糖写法 --></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"imgURL"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">:href</span>=<span class="hljs-string">"aHerf"</span>></span>百度一下<span class="hljs-tag"></<span class="hljs-name">a</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">imgURL</span>: <span class="hljs-string">"https://cn.bing.com/th?id=OIP.NaSKiHPRcquisK2EehUI3gHaE8&pid=Api&rs=1"</span>,
                <span class="hljs-attr">aHerf</span>: <span class="hljs-string">"http://www.baidu.com"</span>
            &#125;
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">2-2、绑定class</h3>
<h4 data-id="heading-16">（1）对象语法：</h4>
<p>:class="&#123;类名1:boolean,类名2:boolean&#125;"</p>
<p>一般不直接赋值布尔值，而是用变量来赋值。</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 动态绑定class对象用法  --></span>
    <span class="hljs-comment"><!-- <h2 :class="&#123;类名1:boolean,类名2:boolean&#125;">&#123;&#123;message&#125;&#125;</h2> --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;active:isActive&#125;"</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"change"</span>></span>点击变色<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">"你好啊"</span>,
        <span class="hljs-attr">active</span>:<span class="hljs-string">"active"</span>,
        <span class="hljs-attr">isActive</span>:<span class="hljs-literal">true</span>
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-built_in">this</span>.isActive = !<span class="hljs-built_in">this</span>.isActive
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">（2）数组语法</h4>
<p>:class="[类名1,类名2]"
数组中加引号，则表示的是字符串；不加引号则是变量。
一般不太使用。</p>
<h3 data-id="heading-18">2-3、绑定style</h3>
<p>利用v-bind:style来绑定一些CSS内联样式。</p>
<p>在写CSS属性名的时候，比如font-size
①我们可以使用驼峰式 (camelCase)  fontSize
②字符串形式：短横线分隔 (kebab-case，记得用单引号括起来) ‘font-size’</p>
<h4 data-id="heading-19">（1）对象语法</h4>
<p>:style="&#123;key(属性名):value(属性值)&#125;"</p>
<p>对象的key是CSS属性名称
对象的value是具体赋的值，值可以来自于data中的属性</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 加单引号，当成字符串解析 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;fontSize:'50px'&#125;"</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-comment"><!-- 不加单引号，变量解析 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;fontSize:fontSize&#125;"</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;fontSize:fontSize1 + 'px'&#125;"</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">"你好啊"</span>,
        <span class="hljs-attr">fontSize</span>:<span class="hljs-string">'100px'</span>,
        <span class="hljs-attr">fontSize1</span>:<span class="hljs-number">100</span>
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">（2）数组对象</h4>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"[baseStyle1,baseStyle2]"</span>></span>&#123;&#123;message&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">message</span>:<span class="hljs-string">"你好啊"</span>,
        <span class="hljs-attr">baseStyle1</span>:&#123;<span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">'red'</span>,<span class="hljs-attr">fontSize</span>:<span class="hljs-string">'100px'</span>&#125;,
        <span class="hljs-attr">baseStyle2</span>:&#123;<span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">'black'</span>,<span class="hljs-attr">fontSize</span>:<span class="hljs-string">'50px'</span>&#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">3、计算属性 computed</h2>
<h3 data-id="heading-22">3-1、基础</h3>
<p>本质上还是属性，但是写法上类似于函数。命名的时候尽量以属性的形式命名，调用时是调用名字，不需要加小括号()</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- Mastache语法 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;firstName+ " " + lastName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  // Kevin Durant
    <span class="hljs-comment"><!-- 方法 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;getFullName()&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>              // Kevin Durant
    <span class="hljs-comment"><!-- 计算属性 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;fullName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>                   // Kevin Durant
<span class="hljs-comment"><!-- 不需要加() --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">firstName</span>:<span class="hljs-string">"Kevin"</span>,
        <span class="hljs-attr">lastName</span>:<span class="hljs-string">"Durant"</span>
      &#125;,
      <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-attr">fullName</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">" "</span> + <span class="hljs-built_in">this</span>.lastName
        &#125;
      &#125;,
      <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">getFullName</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">" "</span> + <span class="hljs-built_in">this</span>.lastName
        &#125;
      &#125;,
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">3-2、复杂操作</h3>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>总价格：&#123;&#123;totalPrice&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">books</span>:[
          &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">110</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">"JavaScript从入门到入土"</span>,<span class="hljs-attr">price</span>:<span class="hljs-number">1</span>&#125;,
          &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">111</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">"Java从入门到放弃"</span>,<span class="hljs-attr">price</span>:<span class="hljs-number">2</span>&#125;,
          &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">112</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">"编码艺术"</span>,<span class="hljs-attr">price</span>:<span class="hljs-number">3</span>&#125;,
          &#123;<span class="hljs-attr">id</span>:<span class="hljs-number">113</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">"代码大全"</span>,<span class="hljs-attr">price</span>:<span class="hljs-number">4</span>&#125;,
        ]
      &#125;,
      <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">totalPrice</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-keyword">let</span> result= <span class="hljs-number">0</span>;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.books.length; i++) &#123;
            result += <span class="hljs-built_in">this</span>.books[i].price;
          &#125;
          <span class="hljs-keyword">return</span> result
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">3-3、缓存</h3>
<p>methods和computed看起来都可以实现我们的功能，
那么为什么还要多一个计算属性这个东西呢？
原因：计算属性会进行缓存，如果多次使用时，计算属性只会调用一次；而方法会使用一次则调用一次，因此计算属性相对而言性能更好。</p>
<h3 data-id="heading-25">3-4、计算属性的setter</h3>
<p>计算属性默认只有getter，但是如果需要也可以提供setter</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123; 
  <span class="hljs-attr">fullName</span>: &#123; 
    <span class="hljs-comment">// getter </span>
   <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; 
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">' '</span> + <span class="hljs-built_in">this</span>.lastName 
   &#125;,
   <span class="hljs-comment">// setter </span>
   <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newValue</span>) </span>&#123; 
     <span class="hljs-keyword">var</span> names = newValue.split(<span class="hljs-string">' '</span>) 
     <span class="hljs-built_in">this</span>.firstName = names[<span class="hljs-number">0</span>] 
     <span class="hljs-built_in">this</span>.lastName = names[names.length - <span class="hljs-number">1</span>] 
    &#125; 
  &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">4、事件监听</h2>
<h3 data-id="heading-27">4-1、v-on介绍</h3>

























<table><thead><tr><th>项目</th><th>Value</th></tr></thead><tbody><tr><td>作用</td><td>绑定事件监听器</td></tr><tr><td>缩写</td><td>@</td></tr><tr><td>预期</td><td>Function 、 Inline Statement 、 Object</td></tr><tr><td>参数</td><td>event</td></tr></tbody></table>
<h3 data-id="heading-28">4-2、v-on参数</h3>
<p>当通过methods中定义方法，以供@click调用时，需要注意参数问题：</p>
<ul>
<li>① 如果该方法不需要额外参数，那么方法后的()可以不添加。
但是注意：如果方法本身中有一个参数，那么会默认将原生事件event参数传递进去</li>
<li>② 如果需要同时传入某个参数，同时需要event时，可以通过 $event 传入事件。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!-- 事件没传参 --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span>></span>按钮1<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- 事件没传参数 --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick()"</span>></span>按钮2<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- 事件没传参数 --></span>
    
    <span class="hljs-comment"><!-- 事件调用方法传参，写函数时候省略小括号，但是函数本身需要传递一个参数 --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick2(123)"</span>></span>按钮3<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- 123 --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick2()"</span>></span>按钮4<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- undefined --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick2"</span>></span>按钮5<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- [object MouseEvent] --></span>
    
    <span class="hljs-comment"><!-- 事件调用时候需要传入event还需要传入其他参数 --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick3($event,123)"</span>></span>按钮6<span class="hljs-tag"></<span class="hljs-name">button</span>></span>  <span class="hljs-comment"><!-- [object MouseEvent]123 --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
      <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
      <span class="hljs-attr">methods</span>:&#123;
        <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"事件没传参数"</span>);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">btnClick2</span>(<span class="hljs-params">value</span>)</span>&#123;
          <span class="hljs-built_in">console</span>.log(value);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">btnClick3</span>(<span class="hljs-params">event,value</span>)</span>&#123;
          <span class="hljs-built_in">console</span>.log(event+value);
        &#125;
      &#125;
    &#125;)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">4-3、v-on修饰符</h3>





























<table><thead><tr><th>修饰符</th><th>作用</th></tr></thead><tbody><tr><td>.stop</td><td>调用 event.stopPropagation()。阻止冒泡</td></tr><tr><td>.prevent</td><td>调用 event.preventDefault()。 阻止默认行为</td></tr><tr><td>.keyCode 或 .keyAlias</td><td>只当事件是从特定键触发时才触发回调。</td></tr><tr><td>.native</td><td>监听组件根元素的原生事件。</td></tr><tr><td>.once</td><td>只触发一次</td></tr></tbody></table>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--1. .stop修饰符的使用--></span>
  <span class="hljs-comment"><!-- 未使用.stop --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"divClick"</span>></span>
    aaaaaaa  <span class="hljs-comment"><!-- 点击aaa时显示div --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"btnClick"</span>></span>按钮1<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- 点击按钮时显示btn div 冒泡了 --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-comment"><!-- 使用.stop --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"divClick"</span>></span>
    aaaaaaa  <span class="hljs-comment"><!-- 点击aaa时显示div --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"btnClick"</span>></span>按钮2<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- 点击按钮时显示btn --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-comment"><!--2. .prevent修饰符的使用--></span>
  <span class="hljs-comment"><!-- 未使用.prevent --></span>
  <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"http://www.baidu.com"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submitClick"</span>></span> <span class="hljs-comment"><!-- 点击提交时显示submit,但是却快速跳转到另一页面 --></span>
  <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
  <span class="hljs-comment"><!-- 使用.prevent --></span>
  <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"http://www.baidu.com"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"submitClick"</span>></span> <span class="hljs-comment"><!-- 点击提交时显示submit,没有跳转到另一页面 --></span>
  <span class="hljs-tag"></<span class="hljs-name">form</span>></span>

  <span class="hljs-comment"><!--3. .监听某个键盘的键帽--></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">keyup.enter</span>=<span class="hljs-string">"keyUp"</span>></span> <span class="hljs-comment"><!-- 监听回车键 --></span>

  <span class="hljs-comment"><!--4. .once修饰符的使用--></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.once</span>=<span class="hljs-string">"btn2Click"</span>></span>按钮3<span class="hljs-tag"></<span class="hljs-name">button</span>></span> <span class="hljs-comment"><!-- 调用一次 --></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"btn"</span>);
      &#125;,
      <span class="hljs-function"><span class="hljs-title">divClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"div"</span>);
      &#125;,
      <span class="hljs-function"><span class="hljs-title">submitClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'submit'</span>);
      &#125;,
      <span class="hljs-function"><span class="hljs-title">keyUp</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'keyUp'</span>);
      &#125;,
      <span class="hljs-function"><span class="hljs-title">btn2Click</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'调用一次'</span>);
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">5、条件和循环</h2>
<h3 data-id="heading-31">5-1、条件渲染</h3>
<p>v-if、v-else-if、v-else
这三个指令与JavaScript的条件语句if、else、else if类似。
Vue的条件指令可以根据表达式的值在DOM中渲染或销毁元素或组件</p>
<p>v-if的原理：
v-if后面的条件为false时，对应的元素以及其子元素不会渲染，也就是根本没有不会有对应的标签出现在DOM中。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"score>=90"</span>></span>优秀<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"score>=80"</span>></span>良好<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"score>=60"</span>></span>及格<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else</span>></span>不及格<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">score</span>: <span class="hljs-number">99</span>
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">5-2、v-if和v-show对比</h3>
<p>v-if当条件为false时，压根不会有对应的元素在DOM中。
v-show当条件为false时，仅仅是将元素的display属性设置为none而已。</p>
<p>当需要在显示与隐藏之间切片很频繁时，使用v-show
当只有一次切换时，使用v-if</p>
<h3 data-id="heading-33">5-3、v-for指令</h3>
<h4 data-id="heading-34">（1）遍历数组</h4>
<p>（1）直接遍历 item in Arry
（2）包含索引号 (item,index) in Arry</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--1.在遍历的过程中,没有使用索引值(下标值)--></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in names"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

  <span class="hljs-comment"><!--2.在遍历的过程中, 获取索引值--></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in names"</span>></span>&#123;&#123;index+1&#125;&#125;.&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">names</span>: [<span class="hljs-string">'Durant'</span>, <span class="hljs-string">'Kobe'</span>, <span class="hljs-string">'Irving'</span>, <span class="hljs-string">'Curry'</span>]
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46fd880fcb524b09baa37ae4138b26f2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-35">（2）vue.js的遍历数组</h4>
<p>一般我们在js代码中，遍历数组的写法是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> books = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < books.length; i++) &#123;
  <span class="hljs-built_in">console</span>.log(books[i]); <span class="hljs-comment">// 1 2 3</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现有两种简单的写法：for(let i in/of books)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. in</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> books)&#123;
  <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// 0 1 2</span>
  conlose.log(books[i]); <span class="hljs-comment">// 1 2 3</span>
  <span class="hljs-comment">// 此时的i为索引值</span>
&#125;
<span class="hljs-comment">// 2. of</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> books)&#123;
  <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// 1 2 3</span>
  <span class="hljs-comment">// 此时的i为数组元素</span>
  <span class="hljs-comment">// 这里还是把i写出item，好认一点</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">（3）遍历对象</h4>
<p>获得值的个数：</p>
<ul>
<li>在遍历对象的过程中, 如果只是获取一个值, 那么获取到的是value</li>
<li>获取两个值, 那么获取到的是value，key 格式: (value, key)</li>
<li>获取三个值, 那么获取到的是value，key ，index 格式: (value, key, index)</li>
<li><strong>注意：</strong> value、key、index只是一个代号而已，就算是（key,index,value）这种写法，得到信息是（属性值，属性名，索引号），即此时key是属性值，index是属性名，value是索引号。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--1.在遍历对象的过程中, 如果只是获取一个值, 那么获取到的是value--></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in info"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>


  <span class="hljs-comment"><!--2.获取两个值, 那么获取到的是value，key 格式: (value, key) --></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(value, key) in info"</span>></span>&#123;&#123;value&#125;&#125;-&#123;&#123;key&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>


  <span class="hljs-comment"><!--3.获取三个值, 那么获取到的是value，key ，index 格式: (value, key, index) --></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(value, key, index) in info"</span>></span>&#123;&#123;value&#125;&#125;-&#123;&#123;key&#125;&#125;-&#123;&#123;index&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">info</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'why'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
        <span class="hljs-attr">height</span>: <span class="hljs-number">1.88</span>
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a181ce5567ef420c853f2c2dcc093b01~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>官方推荐我们在使用v-for时，给对应的元素或组件添加上一个:key属性。</strong></p>
<p><strong>后面会出文章详细讲到key的作用</strong></p>
<h3 data-id="heading-37">5-4、检测数组更新</h3>
<p>因为Vue是响应式的，所以当数据发生变化时，Vue会自动检测数据变化，视图会发生对应的更新。
Vue中包含了一组观察数组编译的方法，使用它们改变数组也会触发视图的更新。
以下方法可以做到响应式</p>





































<table><thead><tr><th>方法</th><th>作用</th></tr></thead><tbody><tr><td>push()</td><td>在数组最后追加数据</td></tr><tr><td>pop()</td><td>删除数组最后一个数据</td></tr><tr><td>shift()</td><td>删除数组第一个元素</td></tr><tr><td>unshift()</td><td>在数组最前面添加元素</td></tr><tr><td>splice()</td><td>删除元素、插入元素、替换元素</td></tr><tr><td>sort()</td><td>排序</td></tr><tr><td>reverse()</td><td>翻转数组</td></tr></tbody></table>
<h4 data-id="heading-38">（1）splice()的用法：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// splice作用: 删除元素/插入元素/替换元素</span>
<span class="hljs-comment">// 第一个参数是索引号，代表起始位置</span>
<span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>];
<span class="hljs-comment">// 删除元素: 第二个参数传入你要删除几个元素(如果没有传,就删除后面所有的元素)</span>
arr.splice(<span class="hljs-number">1</span>,<span class="hljs-number">1</span>); <span class="hljs-comment">// ['a','c']</span>
<span class="hljs-comment">// 插入元素: 第二个参数, 传入0, 并且后面跟上要插入的元素</span>
arr.splice(<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-string">'d'</span>); <span class="hljs-comment">// ['a','b','d','c']</span>
<span class="hljs-comment">// 替换元素: 第二个参数, 表示我们要替换几个元素, 后面是用于替换前面的元素</span>
arr.splice(<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-string">'d'</span>); <span class="hljs-comment">// ['a','d','c']</span>
arr.splice(<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-string">'d'</span>,<span class="hljs-string">'f'</span>); <span class="hljs-comment">// ['a','d','f','c']</span>
<span class="hljs-comment">// 替换这个功能可以理解为删除再插入，比如第二个，先把[1]的b删除，再把后面的'd','f'插入</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">（2）sort()</h4>
<p>单独使用.sort()时，即没有参数。
判断个位数的大小，可以从小到大排序；
但是数值是多位数的时候，它的判断方式却变了，它先比较第一位数，再比较第二位...
所以下面案例中的排序是 1，13，4，7，77。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr1 = [<span class="hljs-number">1</span>,<span class="hljs-number">4</span>,<span class="hljs-number">7</span>,<span class="hljs-number">3</span>];
arr1.sort();
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// [1,3,4,7]</span>
<span class="hljs-keyword">var</span> arr2 = [<span class="hljs-number">13</span>,<span class="hljs-number">1</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>,<span class="hljs-number">77</span>];
arr2.sort();
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">//[1,13,4,7,77]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要想按照从小到大的排序，有以下模板：</p>
<p>从大到小：arr.sort(function(a,b)&#123;
return a-b;//升序
&#125;);</p>
<p>从小到大：
arr.sort(function(a,b)&#123;
return b-a;//降序
&#125;);</p>
<p>注意：sort的括号是 括 整个函数的，最后记得加分号</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr1 = [<span class="hljs-number">13</span>,<span class="hljs-number">1</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>,<span class="hljs-number">77</span>];
arr1.sort(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a,b</span>)</span>&#123;
<span class="hljs-keyword">return</span> a-b；<span class="hljs-comment">//升序</span>
&#125;);
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">//[1,4,7,13,77]</span>
<span class="hljs-keyword">var</span> arr2 = [<span class="hljs-number">13</span>,<span class="hljs-number">1</span>,<span class="hljs-number">7</span>,<span class="hljs-number">4</span>,<span class="hljs-number">77</span>];
arr2.sort(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a,b</span>)</span>&#123;
<span class="hljs-keyword">return</span> b-a；<span class="hljs-comment">//降序</span>
&#125;);
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">//[77,13,7,4,1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">6、表单绑定</h2>
<h3 data-id="heading-41">6-1、v-model基本使用</h3>
<p>Vue中使用v-model指令来实现表单元素和数据的<strong>双向绑定</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"message"</span>></span>
  &#123;&#123;message&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们在输入框输入内容时，因为input中的v-model绑定了message，所以会实时将输入的内容传递给message，message发生改变。当message发生改变时，因为上面我们使用Mustache语法，将message的值插入到DOM中，所以DOM会发生响应的改变。</p>
<p>所以，通过v-model实现了双向的绑定。</p>
<p>当然，我们也可以将v-model用于textarea元素</p>
<h3 data-id="heading-42">6-2、v-model原理</h3>
<p>v-model其实是一个语法糖，它的背后本质上是包含两个操作：</p>
<ol>
<li>v-bind绑定一个value属性</li>
<li>v-on指令给当前元素绑定input事件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"message"</span>></span> &#123;&#123;message&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"message"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"message = $event.target.value"</span>></span>>&#123;&#123;message&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">6-3、其他类型</h3>
<h4 data-id="heading-44">（1）radio</h4>
<p>单选，把选择的东西存入信息。</p>
<p>这个案例就是把选择的性别存进数据里面去</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"male"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"male"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"男"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sex"</span>></span>男
  <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"female"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"female"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"女"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sex"</span>></span>女
  <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>您选择的性别是: &#123;&#123;sex&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">sex</span>: <span class="hljs-string">''</span>
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>v-model 绑定同一个变量sex，所以可以互斥。（这个功能等同于两个radio都设置name="sex"）</p>
<h4 data-id="heading-45">（2）checkbox</h4>
<p>复选框分为两种情况：单个勾选框和多个勾选框
（1）单个勾选框：</p>
<ul>
<li>v-model即为布尔值。</li>
<li>此时input的value并不影响v-model的值。</li>
</ul>
<p>（2）多个复选框：</p>
<ul>
<li>当是多个复选框时，因为可以选中多个，所以对应的data中属性是一个数组。</li>
<li>当选中某一个时，就会将input的value添加到数组中。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--1.checkbox单选框--></span>
  <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"agree"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"agree"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"isAgree"</span>></span>同意协议
  <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>您选择的是: &#123;&#123;isAgree&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"!isAgree"</span>></span>下一步<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

  <span class="hljs-comment"><!--2.checkbox多选框--></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"篮球"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobbies"</span>></span>篮球
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"足球"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobbies"</span>></span>足球
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"乒乓球"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobbies"</span>></span>乒乓球
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"羽毛球"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobbies"</span>></span>羽毛球
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>您的爱好是: &#123;&#123;hobbies&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">isAgree</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 单选框</span>
      <span class="hljs-attr">hobbies</span>: []     <span class="hljs-comment">// 多选框,</span>
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f45a9f65bab49c0bc42e18e2f7ff68e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-46">（3）select</h4>
<p>不常用
（1）单选：只能选中一个值。</p>
<ul>
<li>v-model绑定的是一个值。</li>
<li>当我们选中option中的一个时，会将它对应的value赋值到mySelect中</li>
</ul>
<p>（2）多选：可以选中多个值。 multiple</p>
<ul>
<li>v-model绑定的是一个数组。</li>
<li>当选中多个值时，就会将选中的option对应的value添加到数组mySelects中</li>
<li>多选时要用crtl + 鼠标点击</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--1.选择一个--></span>
  <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"abc"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"fruit"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"苹果"</span>></span>苹果<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"香蕉"</span>></span>香蕉<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"榴莲"</span>></span>榴莲<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"葡萄"</span>></span>葡萄<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>您选择的水果是: &#123;&#123;fruit&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>

  <span class="hljs-comment"><!--2.选择多个--></span>
  <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"abc"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"fruits"</span> <span class="hljs-attr">multiple</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"苹果"</span>></span>苹果<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"香蕉"</span>></span>香蕉<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"榴莲"</span>></span>榴莲<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"葡萄"</span>></span>葡萄<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>您选择的水果是: &#123;&#123;fruits&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">fruit</span>: <span class="hljs-string">'香蕉'</span>,
      <span class="hljs-attr">fruits</span>: []
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbb5a561ddc548f4aaea0f59505fcc95~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-47">6-4、值绑定</h3>
<p>就是动态的给value赋值而已。
v-bind:value=""</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">num1</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">num2</span>: <span class="hljs-number">0</span>
    &#125;,
    <span class="hljs-comment">// 当num1和num2改变时，会调用对应的函数</span>
    <span class="hljs-attr">watch</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">num1</span>(<span class="hljs-params">newvalue</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(num1改变了);
        <span class="hljs-built_in">this</span>.num2 = newvalue * <span class="hljs-number">10</span>; <span class="hljs-comment">// num2改变，会调用num2()&#123;&#125;</span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">num2</span>(<span class="hljs-params">newvalue</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(num2改变了);
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">6-5、修饰符</h3>
<ul>
<li><strong>lazy</strong>修饰符：</li>
</ul>
<p>默认情况下，v-model默认是在input事件中同步输入框的数据的。也就是说，一旦有数据发生改变对应的data中的数据就会自动发生改变。
lazy修饰符可以让数据在<strong>失去焦点</strong>或者<strong>按回车时</strong>才会更新</p>
<ul>
<li><strong>number</strong>修饰符：</li>
</ul>
<p>默认情况下，在输入框中无论我们输入的是字母还是数字，都会被当做字符串类型进行处理。但是如果我们希望处理的是数字类型，那么最好直接将内容当做数字处理。
number修饰符可以让在输入框中输入的内容<strong>自动转成数字类型</strong></p>
<ul>
<li><strong>trim</strong>修饰符：</li>
</ul>
<p>如果输入的内容首尾有很多空格，通常我们希望将其去除，trim修饰符可以过滤内容左右两边的空格</p>
<h2 data-id="heading-49">7、过滤器 filters</h2>
<p>可被用于一些常见的文本格式化。
过滤器可以用在两个地方：双花括号插值和 v-bind 表达式</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span>
&#123;&#123;123 | show&#125;&#125;  // ￥123.00
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>;
  filters:&#123;
    <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params">price</span>)</span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'￥'</span>+price.toFixed(<span class="hljs-number">2</span>)
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">8、监视器 watch</h2>
<p>监听某个变量属性的变化，函数名为该属性名，传入的参数：一个，则为newvalue；两个则为newvalue,oldvalue</p>
<h3 data-id="heading-51">8-1 watch的多种写法</h3>
<pre><code class="hljs language-js copyable" lang="js">watch:&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-keyword">new</span>，old</span>)</span>&#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
     &#125;,
    <span class="hljs-function"><span class="hljs-title">el</span>(<span class="hljs-params"><span class="hljs-keyword">new</span>，old</span>)</span>&#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
     &#125;,    <span class="hljs-comment">//直接观测el值的变化执行副作用</span>
    <span class="hljs-attr">el</span>: &#123;
         <span class="hljs-attr">immediate</span>: <span class="hljs-literal">true</span>，
         <span class="hljs-function"><span class="hljs-title">handle</span>(<span class="hljs-params"><span class="hljs-keyword">new</span>, old</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
        &#125;,
         <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>,
     &#125;,   <span class="hljs-comment">//写成对象的形式，可以方便配置多个参数</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>watch可配置的参数除了immediate和deep外还有一个flush，具体可参照这篇文章<a href="https://juejin.cn/post/6988014110877810724#heading-39" target="_blank" title="https://juejin.cn/post/6988014110877810724#heading-39">vue composition API 一个迷人的新特性</a>中的watchEffect</p>
<h3 data-id="heading-52">停止监听</h3>
<p>vue中有个专门的API    $watch与vue option中watch功能一样，可以注册watch监听器作用，当然<strong>其执行函数默认返回一个停止函数</strong>可以利用这一点注销监听器</p>
<h1 data-id="heading-53">二、组件化开发</h1>
<h2 data-id="heading-54">1、认识组件</h2>
<h3 data-id="heading-55">vue组件化思想</h3>
<p>尽可能的将页面拆分成一个个小的、可复用的组件。
这样让我们的代码更加方便组织和管理，并且扩展性也更强。</p>
<h2 data-id="heading-56">2、组件化基础</h2>
<h3 data-id="heading-57">2-1.注册组件</h3>
<h4 data-id="heading-58">（1）注册的基本步骤</h4>
<p>组件的使用分成三个步骤：
①创建组件构造器： Vue.extend()
②注册组件： Vue.component()
③使用组件。在Vue实例范围内使用</p>
<h4 data-id="heading-59">（2）组件化初体验</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!--3.使用组件--></span>
  <span class="hljs-tag"><<span class="hljs-name">my-cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">my-cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">my-cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">my-cpn</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 1.创建组件构造器对象</span>
  <span class="hljs-keyword">const</span> cpnC = Vue.extend(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
      <div>
        <h2>我是标题</h2>
        <p>我是内容, 哈哈哈哈</p>
        <p>我是内容, 呵呵呵呵</p>
      </div>`</span>
  &#125;)

  <span class="hljs-comment">// 2.注册组件</span>
  Vue.component(<span class="hljs-string">'my-cpn'</span>, cpnC)

  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-60">（3）全局和局部组件</h4>
<p>①全局组件, 意味着可以在多个Vue的实例下面使用
在new Vue 外部注册
②局部组件，在new Vue内部注册，components</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app2"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span> // 全局时可以使用，局部时，由于没有注册，不能使用
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 1.创建组件构造器</span>
  <span class="hljs-keyword">const</span> cpnC = Vue.extend(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
      <div>
        <h2>我是标题</h2>
        <p>我是内容,哈哈哈哈啊</p>
      </div>
    `</span>
  &#125;)
  <span class="hljs-comment">// 2.注册组件</span>
  <span class="hljs-comment">// ①全局组件, 意味着可以在多个Vue的实例下面使用</span>
  <span class="hljs-comment">// Vue.component('cpn', cpnC)</span>
  
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-comment">// ②局部组件</span>
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">cpn</span>: cpnC   <span class="hljs-comment">// cpn使用组件时的标签名，cpnC组件名</span>
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> app2 = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app2'</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-61">（4）父组件和子组件</h4>
<p>A组件在B组件内注册，则A组件是B组件的子组件。
子组件只能在父组件内使用，子组件不能在实例或其他地方使用，除非子组件在实例或者全局注册。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn2</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn2</span>></span>
  <span class="hljs-comment"><!-- 当cpn1只在cpn2中注册时，只能在cpn2调用，除非在vue实例注册或者全局注册，才能在这里使用 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn1</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
  // 1.创建第一个组件构造器(子组件)
  const cpnC1 = Vue.extend(&#123;
    template: `
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是标题1<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是内容, 哈哈哈哈<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    `
  &#125;)
  // 2.创建第二个组件构造器(父组件)
  const cpnC2 = Vue.extend(&#123;
    template: `
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是标题2<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是内容, 呵呵呵呵<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn1</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn1</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    `,
    // 注册子组件
    components: &#123;
      cpn1: cpnC1
    &#125;
  &#125;)

  // root组件，实例相当于一个组件
  const app = new Vue(&#123;
    el: '#app',
    components: &#123;
      cpn2: cpnC2
    &#125;
  &#125;)
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-62">（5）注册组件语法糖</h4>
<p>主要是省去了调用Vue.extend()的步骤，而是可以直接使用一个对象来代替。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn1</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn2</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 1.全局组件注册的语法糖</span>
  <span class="hljs-comment">// 1.创建组件构造器</span>
  <span class="hljs-comment">// const cpn1 = Vue.extend()</span>
  <span class="hljs-comment">// 2.注册组件</span>
  Vue.component(<span class="hljs-string">'cpn1'</span>, &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`
      <div>
        <h2>我是标题1</h2>
        <p>我是内容, 哈哈哈哈</p>
      </div>
    `</span>
  &#125;)
  <span class="hljs-comment">// 2.注册局部组件的语法糖</span>
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-string">'cpn2'</span>: &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div>
            <h2>我是标题2</h2>
            <p>我是内容, 呵呵呵</p>
          </div>
    `</span>
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-63">（6）模板的分离写法</h4>
<p>①使用 script 标签，text/x-template
②使用 template 标签 （较常用）
记得给模板定个id
<strong>script标签：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!--1.script标签, 注意:类型必须是text/x-template--></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/x-template"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span><span class="handlebars"><span class="xml">
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是标题<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是内容,哈哈哈<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 1.注册一个全局组件</span>
  Vue.component(<span class="hljs-string">'cpn'</span>, &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>
  &#125;)
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>template标签:</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--2.template标签--></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是标题<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是内容,呵呵呵<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-64">（7）组件不能访问Vue实例中data的数据</h4>
<p>组件是一个单独功能模块的封装，它有属于自己的HTML模板，也应该有属性自己的数据data。</p>
<p>①组件对象也有一个data属性(也可以有methods等属性)
②data属性必须是一个函数，而且这个函数返回一个对象，对象内部保存着数据</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 1.注册一个全局组件</span>
  Vue.component(<span class="hljs-string">'cpn'</span>, &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-comment">// data是一个函数，返回一个对象，这个对象存放数据</span>
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'abc'</span>
      &#125;
    &#125;
  &#125;)
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>,
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-65">（8）组件data返回对象的两种方式</h4>
<p>组件中data返回对象有两种写法：
（1）返回的对象在data里面定义。（信息不会共享）
（2）返回的对象在外部定义。（信息共享）</p>
<p><strong>第一种写法：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前计数: &#123;&#123;counter&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
Vue.component(<span class="hljs-string">'cpn'</span>, &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.counter++
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.counter--
      &#125;
    &#125;
  &#125;)
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2cf7f4f948b49869cc5e5f6d9e68bd3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当点击任意一个模块时，只会改变当前组件的count的值。因为这种写法是调用组件的data时才定义一个对象，则每个对象都有自己的一个内存地址，当调用三次组件的data时，返回的是三个不同内存地址的对象(虽说内容相同，但地址不同)。所以信息不会共享共享。</p>
<p><strong>第二种写法：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
  &#125;
  Vue.component(<span class="hljs-string">'cpn'</span>, &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> obj
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.counter++
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.counter--
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0158860e9c44a548352493f9dcf4495~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当点击任意一个模块均会改变count的值。因为这种写法是先将obj定义，则obj有一个内存地址，当调用三次组件的data时，返回的都是同一个内存地址的obj。所以导致信息共享。</p>
<h3 data-id="heading-66">2-2.数据传递</h3>
<p>父组件通过props向子组件传递数据
子组件通过事件向父组件发送消息
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65b2e294cbd0426093e150cb961159f9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
真实的开发中，Vue实例和子组件的通信和父组件和子组件的通信过程是一样的。</p>
<h4 data-id="heading-67">（1）父级向子级传递 props</h4>
<p>在子组件中使用选项 props 来声明需要从父级接收到的数据。</p>
<p>props的值有两种方式：</p>
<p>方式一：字符串数组，数组中的字符串就是传递时的名称。</p>
<p>方式二：对象，对象可以设置传递时的类型，也可以设置默认值等。</p>
<h5 data-id="heading-68">①数组形式</h5>
<p><strong>字符串数组形式：</strong>（不常用）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 调用子组件且子组件需要父组件的数据时，必须v-bind绑定属性 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">:cmessage</span>=<span class="hljs-string">"message"</span> <span class="hljs-attr">:cmovies</span>=<span class="hljs-string">"movies"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;cmovies&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;cmessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 父传子: props</span>
  <span class="hljs-keyword">const</span> cpn = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-attr">props</span>: [<span class="hljs-string">'cmovies'</span>, <span class="hljs-string">'cmessage'</span>]
  &#125;

  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>,
      <span class="hljs-attr">movies</span>: [<span class="hljs-string">'海王'</span>, <span class="hljs-string">'海贼王'</span>, <span class="hljs-string">'海尔兄弟'</span>]
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      cpn
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-69">②对象形式</h5>
<p><strong>对象形式：</strong>（当需要对props进行类型等验证时，就需要对象写法了）
验证支持的数据类型：String、Number、Boolean、Array、Object、Date、Function、Symbol</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 调用子组件且子组件需要父组件的数据时，必须v-bind绑定属性 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">:cmessage</span>=<span class="hljs-string">"message"</span> <span class="hljs-attr">:cmovies</span>=<span class="hljs-string">"movies"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;cmovies&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;cmessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 父传子: props</span>
  <span class="hljs-keyword">const</span> cpn = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-comment">// 1.类型限制</span>
      <span class="hljs-comment">// cmovies: Array,</span>
      <span class="hljs-comment">// cmessage: String,</span>
      <span class="hljs-comment">// 2.提供一些默认值, 以及必传值</span>
      <span class="hljs-attr">cmessage</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,         <span class="hljs-comment">// 数据类型</span>
        <span class="hljs-attr">default</span>: <span class="hljs-string">'aaaaaaaa'</span>,  <span class="hljs-comment">// 默认值</span>
        <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>        <span class="hljs-comment">// true表示调用这个组件时，必须调用cmessage这个属性</span>
      &#125;,
      <span class="hljs-comment">// 类型是对象或者数组时, 默认值必须是一个函数</span>
      <span class="hljs-attr">cmovies</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
        <span class="hljs-function"><span class="hljs-title">default</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> []
        &#125;
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>,
      <span class="hljs-attr">movies</span>: [<span class="hljs-string">'海王'</span>, <span class="hljs-string">'海贼王'</span>, <span class="hljs-string">'海尔兄弟'</span>]
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      cpn
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-70">③驼峰标识的注意点：</h5>
<p>当我们在props中声明变量时，采用的驼峰命名法的话，即cMessage，在调用子组件且传递父组件数据时，v-bind绑定属性名不能驼峰标识，需要变换。cMessage 转换成 c-message</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 错误写法 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">:cMessage</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-comment"><!-- 正确写法 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">:c-message</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;cMessage&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> cpn = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-attr">cMessage</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
        <span class="hljs-attr">default</span>: <span class="hljs-string">'很好'</span>
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      cpn
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-71">（2）子级向父级传递</h4>
<p>子组件传递数据或事件到父组件中需要使用自定义事件来完成。</p>
<p>自定义事件的流程：
在子组件中，通过$emit('事件名'，参数)来触发事件。（emit是发射的意思）
在父组件中，通过v-on来监听子组件事件。 @事件名='父组件的事件'</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--父组件模板--></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span> @<span class="hljs-attr">item-click</span>=<span class="hljs-string">"cpnClick"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!--子组件模板--></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in categories"</span>
            @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick(item)"</span>></span>
      &#123;&#123;item.name&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

  <span class="hljs-comment">// 1.子组件</span>
  <span class="hljs-keyword">const</span> cpn = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-comment">// 类别</span>
        <span class="hljs-attr">categories</span>: [
          &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'aaa'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'热门推荐'</span>&#125;,
          &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'bbb'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'手机数码'</span>&#125;,
          &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'ccc'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'家用家电'</span>&#125;,
          &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'ddd'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'电脑办公'</span>&#125;,
        ]
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-comment">// 发射事件: 自定义事件</span>
        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'item-click'</span>, item); 
        <span class="hljs-comment">// item-click为父组件的绑定事件名 @item-click='' ，可以传参数</span>
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">// 2.父组件</span>
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">components</span>: &#123;
      cpn
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">cpnClick</span>(<span class="hljs-params">item</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'cpnClick'</span>, item);
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-72">（3）父子组件的访问</h4>
<p>父组件访问子组件：使用 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>c</mi><mi>h</mi><mi>i</mi><mi>l</mi><mi>d</mi><mi>r</mi><mi>e</mi><mi>n</mi><mtext>或</mtext></mrow><annotation encoding="application/x-tex">children或 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord cjk_fallback">或</span></span></span></span></span>refs (reference 引用)
子组件访问父组件：使用 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mtext>访问根组件：使用</mtext></mrow><annotation encoding="application/x-tex">parent 访问根组件：使用 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">访</span><span class="mord cjk_fallback">问</span><span class="mord cjk_fallback">根</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">：</span><span class="mord cjk_fallback">使</span><span class="mord cjk_fallback">用</span></span></span></span></span>root</p>
<p>最常用的是 <strong>refs</strong></p>
<p>children 获取到的是子组件的集合，是一个<strong>数组</strong>，访问其中的子组件必须通过索引值。
children的缺陷：
当子组件过多，我们需要拿到其中一个时，往往不能确定它的索引值，甚至还可能会发生变化。</p>
<p>refs 相当于key，先给每个子组件定义ref属性，再使用refs调用，就可以访问特定的子组件，不会随着位置数目得变化而出错。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"aaa"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是子组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 1.$children</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children);
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> c <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.$children) &#123;
           <span class="hljs-built_in">console</span>.log(c.name);
        &#125;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children[<span class="hljs-number">1</span>].name);

        <span class="hljs-comment">// 2.$refs => 对象类型, 默认是一个空的对象</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs.aaa.name);
      &#125;
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">cpn</span>: &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'我是子组件的name'</span>
          &#125;
        &#125;
      &#125;,
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>parent：</p>
<ul>
<li>尽管在Vue开发中，允许我们通过 parent来访问父组件，但是在真实开发中尽量不要这样做。</li>
<li>子组件应该尽量避免直接访问父组件的数据，因为这样耦合度太高了。</li>
<li>如果我们将子组件放在另外一个组件之内，很可能该父组件没有对应的属性，往往会引起问题。</li>
<li>另外，更不好做的是通过$parent直接修改父组件的状态，那么父组件中的状态将变得飘忽不定，很不利于我的调试和维护。</li>
<li></li>
</ul>
<h4 data-id="heading-73">（4）非父子组件通信</h4>
<h2 data-id="heading-74">3、组件化高级</h2>
<h3 data-id="heading-75">3-1、插槽slot</h3>
<p>组件的插槽也是为了让我们封装的组件更加具有扩展性。让使用者可以决定组件内部的一些内容到底展示什么。</p>
<h4 data-id="heading-76">（1）编译作用域</h4>
<p>父组件模板的所有东西都会在父级作用域内编译；子组件模板的所有东西都会在子级作用域内编译。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8441fd8dafb846dbbfb500e78a17f893~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-77">（2）slot的基本使用</h4>
<p>在子组件中使用标签 slot
在父组件中直接使用子组件，并在内部使用想要的标签即可。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--
1.插槽的基本使用 <slot></slot>
2.插槽的默认值 <slot>button</slot>
3.如果有多个值, 同时放入到组件进行替换时, 一起作为替换元素
--></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span> <span class="hljs-comment"><!-- 按钮 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"><<span class="hljs-name">i</span>></span>呵呵呵<span class="hljs-tag"></<span class="hljs-name">i</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span> <span class="hljs-comment"><!-- 呵呵呵 --></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">i</span>></span>呵呵呵<span class="hljs-tag"></<span class="hljs-name">i</span>></span>           <span class="hljs-comment"><!--呵呵呵 div p--></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是div元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是p元素<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是组件, 哈哈哈<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"><<span class="hljs-name">button</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span> <span class="hljs-comment"><!-- 默认为按钮 --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">cpn</span>: &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-78">（3）slot的具名插槽</h4>
<p>当有多个slot插槽时，想替换某个插槽的内容，只需给slot元素一个name属性，再在替换时，可以在一个template标签上使用v-slot指令，并以v-slot的参数提供name(也可以是动态参数)即可。缩写 #name</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"center"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>标题<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"><<span class="hljs-name">button</span>></span>返回<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"left"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>左边<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"center"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>中间<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"right"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>右边<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你好啊'</span>
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">cpn</span>: &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-79">（4）slot作用域插槽</h4>
<p>父组件替换插槽的标签，但是内容由子组件来提供。
最核心就是从子组件获得数据，并可以在父组件中使用。
我们可以将user作为元素的一个属性绑定</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">span</span>></span> 
   <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">v-bind:user</span>=<span class="hljs-string">"user"</span>></span> &#123;&#123; user.lastName &#125;&#125; 
   <span class="hljs-tag"></<span class="hljs-name">slot</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绑定在 <code><slot></code> 元素上的 attribute 被称为<strong>插槽 prop</strong>。现在在父级作用域中，我们可以使用带值的 <code>v-slot</code> 来定义我们提供的插槽 prop 的名字：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">current-user</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:default</span>=<span class="hljs-string">"slotProps"</span>></span>
    &#123;&#123; slotProps.user.firstName &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">current-user</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，我们选择将包含所有插槽 prop 的对象命名为 <code>slotProps</code>，但你也可以使用任意你喜欢的名字。</p>
<h2 data-id="heading-80">4、组件生命周期</h2>
<p>这里简单介绍一下父子组件生命周期创建顺序，后面我会出文章对vue源码分析详细介绍</p>
<p>当一个父组件中包含一个子组件，其生命周期创建顺序如下：</p>
<blockquote>
<p><strong>父beforeCreate->父created->父beforeMount->子beforeCreate->子created->子beforeMount->子mounted->父mounted</strong></p>
</blockquote>
<h2 data-id="heading-81">5、模块化开发</h2>
<p>CommonJS、AMD、CMD，也有ES6的Modules</p>
<h3 data-id="heading-82">5-1、CommonJS</h3>
<p>Node用的多，Node会学到，<a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">后面学node写文章会介绍并在这补充链接</a></p>
<p>导入module.exports = &#123; &#125;
导出 let &#123; &#125; = require('./...js')</p>
<h3 data-id="heading-83">5-2、ES6的Modules</h3>
<p>先在导入js文件处写入 type="module"</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"aaa.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"mmm.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>export(导出)</strong>、<strong>inport(导入)</strong></p>
<p>导出方式一：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> flag= <span class="hljs-literal">true</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">num1,num2</span>)</span>&#123;
  <span class="hljs-keyword">return</span> num1 + num2
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在奔跑'</span>);
  &#125;
&#125;
<span class="hljs-keyword">export</span> &#123;
  flag,
  sum,
  Person
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导出方式二：（定义时就先导出）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> num1 = <span class="hljs-number">1000</span>;
<span class="hljs-comment">// 导出函数/类：</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mul</span>(<span class="hljs-params">num1, num2</span>) </span>&#123;
    <span class="hljs-keyword">return</span> num1 * num2
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'在奔跑'</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>某些情况下，一个模块中包含某个的功能，我们并不希望给这个功能命名，而且让导入者可以自己来命名，使用export default</p>
<p><strong>注：export default在同一个模块中，不允许同时存在多个。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// export default</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">const</span> address = <span class="hljs-string">'北京市'</span>
<span class="hljs-comment">// 导出函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">argument</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(argument);
&#125;

<span class="hljs-comment">// 导入的写法与平常不一样</span>
<span class="hljs-keyword">import</span> addr <span class="hljs-keyword">from</span> <span class="hljs-string">"./aaa.js"</span>; <span class="hljs-comment">// addr为自己命名的，不再需要加&#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 部分导入</span>
<span class="hljs-keyword">import</span> &#123;flag,sum&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./aaa.js"</span>;
<span class="hljs-comment">// 统一全部导入</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> bbb <span class="hljs-keyword">from</span> <span class="hljs-string">'./aaa.js'</span>  <span class="hljs-comment">// bbb为自己命名的名字</span>
<span class="hljs-built_in">console</span>.log(bbb.flag);           <span class="hljs-comment">// 调用导入的flag</span>
<span class="hljs-built_in">console</span>.log(bbb.sum(<span class="hljs-number">10</span>,<span class="hljs-number">20</span>));     <span class="hljs-comment">// 调用导入的sum()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-84">三、vue-router</h1>
<h2 data-id="heading-85">1、认识路由</h2>
<p>路由就是通过互联的网络把信息从源地址传输到目的地址的活动——维基百科。
路由就是决定数据包从来源到目的地的路径.</p>
<p>路由中有一个非常重要的概念叫路由表，本质上就是一个映射表, 决定了数据包的指向.</p>
<h2 data-id="heading-86">2、vue-router基本使用</h2>
<h3 data-id="heading-87">2-1、路由跳转规则</h3>
<h4 data-id="heading-88">（1）url的hash</h4>
<p>URL的hash也就是锚点(#)，我们可以通过直接赋值location.hash来改变href, 但是页面不发生刷新。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddc21b48e6734d1680b43da16cf5f4d4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-89">（2）ES5的history</h4>
<h5 data-id="heading-90">pushState</h5>
<p>可跳转回来。
跳转指令是：history.back()
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c53b6e24f79145d6b83ca471387c5961~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-91">replaceState</h5>
<p>替换掉，不可跳转。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6e7b698bd034a6c88c7ee28e6396e24~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-92">go</h5>
<p>history.back() 等价于 history.go(-1)
history.forward() 则等价于 history.go(1)
这三个接口等同于浏览器界面的前进后退。</p>
<h3 data-id="heading-93">2-2、安装路由</h3>
<p>webpack安装：npm install vue-router --save
CLI安装：选择vue-router yes即可
CLI安装会自动帮我们配置好，如果是webpack安装，就需要我们自己配置。可按以下进行配置：</p>
<p>src/router/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置路由相关的信息</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-comment">// 1.通过Vue.use(插件), 安装插件</span>
Vue.use(VueRouter)
<span class="hljs-comment">// 配置路由和组件之间的映射关系（映射表）</span>
<span class="hljs-keyword">const</span> routes = [
]
<span class="hljs-comment">// 2.创建VueRouter对象</span>
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes
&#125;)
<span class="hljs-comment">// 3.将router对象传入到Vue实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>  <span class="hljs-comment">// 导入路由 导入的是文件夹的话，会默认导入index文件</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  router,  <span class="hljs-comment">//导入路由</span>
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-94">2-3、使用路由</h3>
<p>src/router/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置路由相关的信息</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/Home'</span>  <span class="hljs-comment">// 导入组件</span>
<span class="hljs-keyword">import</span> About <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/About'</span> <span class="hljs-comment">// 导入组件</span>

<span class="hljs-comment">// 1.通过Vue.use(插件), 安装插件</span>
Vue.use(VueRouter)
<span class="hljs-comment">// 配置路由和组件之间的映射关系</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-comment">// 路由的默认路径</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>  <span class="hljs-comment">// redirect重定向</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">component</span>: About
  &#125;
]
<span class="hljs-comment">// 2.创建VueRouter对象</span>
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes,
  <span class="hljs-attr">mode</span>:<span class="hljs-string">'history'</span>  <span class="hljs-comment">// mode：模式，默认情况是hash值，也就是‘#/home’,改用ES5的history就没有#</span>
&#125;)
<span class="hljs-comment">// 3.将router对象传入到Vue实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>  <span class="hljs-comment">// 导入路由 导入的是文件夹的话，会默认导入index文件</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  router,  <span class="hljs-comment">//导入路由</span>
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span> <span class="hljs-comment"><!-- 组件将替换掉router-view --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>router-link：该标签是一个vue-router中已经内置的组件, 它会被默认渲染成一个 a 标签.
router-view：该标签会根据当前的路径, 动态渲染出不同的组件.
网页的其他内容, 比如顶部的标题/导航, 或者底部的一些版权信息等会和router-view处于同一个等级.
在路由切换时, 切换的是router-view挂载的组件, 其他内容不会发生改变</p>
<h4 data-id="heading-95">（1）router-link</h4>
<p>router-link：该标签是一个vue-router中已经内置的组件, 它会被默认渲染成一个 a 标签.
<strong>属性：</strong></p>
<ul>
<li>to：用于指定跳转的路径.</li>
<li>tag：可以指定router-link之后渲染成什么标签，比如渲染成一个button标签，tag="button"</li>
<li>replace：默认跳转方式是pushState，想要设置成replaceState，可以直接加上replace属性。</li>
<li>④ctive-class: 当router-link对应的路由匹配成功时，会自动给当前元素设置一个router-link-active的class，设置active-class可以修改默认的名称。</li>
</ul>
<p>当我们在对进行高亮显示的导航菜单或者底部tabbar时, 会使用到该类。</p>
<p>但是呢，如果有多个router-link就需要修改多次，所以有一种简便写法：
src/router/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes,
  <span class="hljs-attr">mode</span>:<span class="hljs-string">'history'</span>,
  <span class="hljs-attr">linkActiveClass</span>:<span class="hljs-string">'active'</span> <span class="hljs-comment">// 路由匹配成功时，默认添加的类名为active</span>
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-96">（2）另一种跳转方式</h4>
<p>之前的跳转是依赖router-link，现在不用router-link来跳转的话，可以这样：
App.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"homeClick"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"aboutClick"</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">homeClick</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 通过代码的方式修改路由 vue-router</span>
      <span class="hljs-comment">// this.$router.push('/home')</span>
      <span class="hljs-built_in">this</span>.$router.replace(<span class="hljs-string">'/home'</span>) <span class="hljs-comment">// router其实是index.js中定义的router（Vuerouter对象）</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">aboutClick</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// this.$router.push('/about') // push=>pushState</span>
      <span class="hljs-built_in">this</span>.$router.replace(<span class="hljs-string">'/about'</span>) <span class="hljs-comment">// replace=>replaceState</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-97">2-4、动态路由</h3>
<p>在某些情况下，一个页面的path路径可能是不确定的，比如我们进入用户界面时，希望是如下的路径：
/user/aaaa或/user/bbbb（除了有前面的/user之外，后面还跟上了用户的ID），也可以通过路由获取到信息。
index.js中的路径写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>, <span class="hljs-comment">// id是从App.vue获取到的useId</span>
    <span class="hljs-attr">component</span>: User
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"'/user/'+userId"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">userId</span>: <span class="hljs-string">'zhangsan'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以在打开组件User.vue时路径显示的是 /user/zhangsan
<strong>获取路径里的zhangsan：</strong>
User.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;userId&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  <span class="hljs-comment"><!-- 通过computer获取到信息 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$route.params.id&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  <span class="hljs-comment"><!-- 直接获取 --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"User"</span>,
    <span class="hljs-attr">computed</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">userId</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$route.params.id 
        <span class="hljs-comment">// 这里的route与“另一种跳转方式”的router是不一样的</span>
        <span class="hljs-comment">// route是router里面的routes中活跃的路由</span>
        <span class="hljs-comment">// id是活跃路由中path: '/user/:id'的id</span>
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-98">2-5、路由懒加载</h3>
<p>当打包构建应用时，Javascript 包会变得非常大，影响页面加载。
如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样就更加高效了。</p>
<p>路由懒加载的主要作用就是将路由对应的组件打包成一个个的js代码块，只有在这个路由被访问到的时候, 才加载对应的组件。
<strong>之前的写法：</strong>
index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/Home'</span>  <span class="hljs-comment">// 导入组件</span>
<span class="hljs-keyword">import</span> About <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/About'</span> <span class="hljs-comment">// 导入组件</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-comment">// 路由的默认路径</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">component</span>: About
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>路由懒加载写法：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">const</span> Home = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Home'</span>)  <span class="hljs-comment">// 动态导入组件</span>
<span class="hljs-keyword">const</span> About = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/About'</span>) <span class="hljs-comment">// 动态导入组件</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-comment">// 路由的默认路径</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">component</span>: About
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-99">3、vue-router嵌套路由</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/983ab86f17c64aeeadf6b42a020b158a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在组件home中再有两个路径对应两个子组件。</p>
<p>1、创建对应的子组件(News.vue，Message.vue)，并且在路由映射中配置对应的子路由：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">const</span> Home = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Home'</span>) 
<span class="hljs-keyword">const</span> News = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/News'</span>) <span class="hljs-comment">// 动态导入子组件News</span>
<span class="hljs-keyword">const</span> Message = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Message'</span>) <span class="hljs-comment">// 动态导入子组件Message</span>
<span class="hljs-keyword">const</span> About = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/About'</span>)

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-comment">// 路由的默认路径</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>: Home,
    <span class="hljs-attr">children</span>:[
    &#123;
       <span class="hljs-attr">path</span>:<span class="hljs-string">''</span>,
       <span class="hljs-attr">redirect</span>: News
    &#125;,
    &#123;
       <span class="hljs-attr">path</span>:<span class="hljs-string">'news'</span>,  <span class="hljs-comment">// 不用加/</span>
       <span class="hljs-attr">component</span>: News
     &#125;,
     &#123;
       <span class="hljs-attr">path</span>:<span class="hljs-string">'message'</span>, <span class="hljs-comment">// 不用加/</span>
       <span class="hljs-attr">component</span>: Message
     &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">component</span>: About
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、在两个子组件的父组件内部使用router-link和router-view标签.
Home.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/news"</span>></span>新闻<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/message"</span>></span>消息<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-100">4、vue-router参数传递</h2>
<p>URL：
协议://主机:端口/路径?查询#片段
scheme://host:port/path?query#fragment</p>
<p>传递参数主要有两种类型: params和query</p>
<h3 data-id="heading-101">4-1、params的类型:</h3>
<p>配置路由格式：/router/:id</p>
<p>传递的方式：在path后面跟上对应的值</p>
<p>传递后形成的路径：/router/123, /router/abc</p>
<p>见2-4、动态路由</p>
<p>另一种跳转方式，不用router-link跳转（参考2-3(2)）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"userClick"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">userId</span>: <span class="hljs-string">'zhangsan'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">userClick</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.$route.push(<span class="hljs-string">'/user'</span>+<span class="hljs-built_in">this</span>.userId)
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-102">4-2、query的类型:</h3>
<p>配置路由格式：/router, 也就是普通配置</p>
<p>传递的方式：对象中使用query的key作为传递方式</p>
<p>传递后形成的路径：/router?id=123, /router?id=abc</p>
<p>index.js(不用跟params一样设置，正常设置就行)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/profile'</span>,
    <span class="hljs-attr">component</span>: Profile
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123;path:'/profile',query:&#123;name:'wu',age:20&#125;&#125;"</span>></span>我的<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Profile.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$route.query&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>      <span class="hljs-comment"><!-- &#123;name:wu,age:20&#125; --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$route.query.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span> <span class="hljs-comment"><!-- wu --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$route.query.age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>  <span class="hljs-comment"><!-- 20 --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时的url为 .../profile?name=wu&&age=20</p>
<p>另一种跳转方式，不用router-link跳转</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"profileClick"</span>></span>我的<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">profileClick</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.$route.push(&#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/profile'</span>,
        <span class="hljs-attr">qurey</span>:&#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'wu'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
        &#125;
      &#125;)
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-103">5、route和router是有区别的</h2>
<p>router为VueRouter实例，可以导航到不同URL，使用$router.push/replace方法</p>
<p>$route为当前router跳转的对象（route是router里面的routes中活跃的路由），可以获取name、path、query、params等</p>
<h2 data-id="heading-104">6、vue-router导航守卫</h2>
<p>在一个SPA应用中, 如何改变网页的标题呢?
网页标题是通过 title 标签来显示的, 但是SPA只有一个固定的HTML, 切换不同的页面时, 标题并不会改变。利用导航守卫可解决这一问题。</p>
<p><strong>什么是导航守卫?</strong></p>
<ol>
<li>vue-router提供的导航守卫主要用来监听监听路由的进入和离开的.</li>
<li>vue-router提供了beforeEach和afterEach的钩子函数, 它们会在路由即将改变前和改变后触发。</li>
<li>前置守卫和后置钩子都是全局守卫</li>
<li>路由独享守卫 beforeEnter，参数与beforeEach一致。</li>
<li>组件内的守卫 beforeRouteEnter（在渲染该组件的对应路由前被调用）、beforeRouteUpdate（在当前路由改变，但是该组件被复用时调用）、beforeRouteLeave（导航离开该组件的对应路由前调用）</li>
</ol>
<p>改变网页标题：
index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>: Home,
    <span class="hljs-attr">meta</span>: &#123;         <span class="hljs-comment">// meta元数据（描述数据的数据）</span>
      <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span>
    &#125;
  &#125;,
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,<span class="hljs-attr">component</span>: About,<span class="hljs-attr">meta</span>: &#123;<span class="hljs-attr">title</span>: <span class="hljs-string">'关于'</span>&#125;&#125;,
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,<span class="hljs-attr">component</span>: User,<span class="hljs-attr">meta</span>: &#123;<span class="hljs-attr">title</span>: <span class="hljs-string">'用户'</span>&#125;&#125;,
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/profile'</span>, <span class="hljs-attr">component</span>: Profile,<span class="hljs-attr">meta</span>: &#123;<span class="hljs-attr">title</span>: <span class="hljs-string">'档案'</span>&#125;&#125;
]

<span class="hljs-comment">// 前置守卫(guard)</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-comment">// 从from跳转到to</span>
  <span class="hljs-built_in">document</span>.title = to.matched[<span class="hljs-number">0</span>].meta.title  
  <span class="hljs-comment">// 路由存在嵌套的话，必须调用matched才能调用到meta，所以干脆都使用</span>
  <span class="hljs-comment">// console.log(to);  // 活跃的路由</span>
  next()  <span class="hljs-comment">// beforeEach必写，跳转页面</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导航钩子的三个参数解析：</p>
<ul>
<li>①to：即将要进入的目标的路由对象.</li>
<li>②from：当前导航即将要离开的路由对象.</li>
<li>③next：调用该方法后, 才能进入下一个钩子.
next('/路径') 指定某个路径</li>
</ul>
<p>后置钩子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 后置钩子(hook)</span>
router.afterEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  <span class="hljs-comment">// console.log('----');</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由独享守卫：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">component</span>: Home,
    <span class="hljs-attr">meta</span>: &#123;         <span class="hljs-comment">// meta元数据（描述数据的数据）</span>
      <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span>
    &#125;,
    <span class="hljs-attr">beforeEnter</span>:<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>) =></span> &#123;
      <span class="hljs-comment">// ...</span>
      next()
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-105">7、keep-alive</h2>
<p>keep-alive 是 Vue 内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染。
router-view 也是一个组件，如果直接被包在 keep-alive 里面，所有路径匹配到的视图组件都会被缓存。</p>
<p>其中activated函数和deactivated函数均在keep-alive存在时才能使用。
activated（活跃）、deactivated（不活跃）
App.vue</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Home.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
    <span class="hljs-function"><span class="hljs-title">activated</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Home activated'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">deactivated</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Home deactivated'</span>)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们的页面在Home时，会打印Home activated，当页面离开Home时，会打印Home deactivated。（当然，这是在存在keep-alive的情况下）</p>
<p>调用keep-alive后，组件不会被频繁的创建销毁。它会使其保留状态，或避免重新渲染。
没有使用keep-alive时，组件被调用时就创建，切换时又被销毁。</p>
<p><strong>测试：</strong>
App.vue</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Home.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Home created'</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Home destroyed'</span>)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-106">keep-alive的属性</h3>
<p>①include（包括） 值为字符串或正则表达，只有匹配的组件会被缓存
②exclude（不包括） 值为字符串或正则表达式，任何匹配的组件都不会被缓存</p>
<p>App.vue</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">keep-alive</span> <span class="hljs-attr">exclude</span>=<span class="hljs-string">"Home,About"</span>></span> <span class="hljs-comment"><!--Home和About会被频繁创建销毁--></span>
  <span class="hljs-comment"><!-- Home、About其实是组件的name --></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-107">8、起别名</h2>
<p>当需要到多个外层文件夹取文件时，../../ 就需要很多个了，这在开发中很忌讳，而且如果移动文件所在地，就可能需要改动调用路径代码了。所以起个别名就非常方便。</p>
<p>webpack.base.conf.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'src'</span>),  <span class="hljs-comment">// 当前项目的src文件夹(第一层)</span>
      <span class="hljs-string">'assets'</span>: resolve(<span class="hljs-string">'src/assets'</span>), 
      <span class="hljs-string">'components'</span>: resolve(<span class="hljs-string">'src/components'</span>),
      <span class="hljs-string">'views'</span>: resolve(<span class="hljs-string">'src/views'</span>),
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用：有两种情况：①在html标签内调用（图片的引用）②在import调用
①html标签（加~）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"item-icon"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"~assets/img/tabbar/home.svg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
<span class="hljs-comment"><!-- assets是src/assets  但是在html标签内使用别名就需要加~ --></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>②在import调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> TabBar <span class="hljs-keyword">from</span> <span class="hljs-string">'components/tabbar/TabBar'</span>
<span class="hljs-comment">// component是src/component 直接调用就行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-108">9、Promise（ES6）</h2>
<p>Promise是异步编程的一种解决方案。</p>
<p>什么时候我们会来处理异步事件呢？
一种很常见的场景应该就是网络请求了。我们封装一个网络请求的函数，因为不能立即拿到结果，所以往往我们会传入另外一个函数，在数据请求成功时，将数据通过传入的函数回调出去。但是，当网络请求非常复杂时，就会出现回调地狱（多个回调函数）。</p>
<p>回调地狱的一般写法，在正常情况下，不会有什么问题，可以正常运行并且获取我们想要的结果。但是，这样的代码难看而且不容易维护。</p>
<h3 data-id="heading-109">9-1、Promise的结构</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Promise的参数是一个函数(resolve,reject)=>&#123;&#125;</span>
<span class="hljs-comment">// 这个函数的参数有两个：resolve, reject它们本身又是函数(可以传递参数也可以不传)</span>
<span class="hljs-comment">// reject用不到时可以不传</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
  <span class="hljs-comment">// 异步事件</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 请求成功的时候调用resolve</span>
    resolve()
    <span class="hljs-comment">// 请求失败的时候调用reject</span>
    reject()
  &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 请求成功时的100行处理代码</span>
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 另一个异步事件，再来一个Promise</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span>&#123;&#125;) <span class="hljs-comment">// 用不到reject时可以不传</span>
&#125;).catch(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 请求失败时的处理代码</span>
  <span class="hljs-comment">// ...</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例：setTimeout里面有setTimeout
回调地狱的一般写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World'</span>);
  
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Vuejs'</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Vuejs'</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Vuejs'</span>);
    
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Python'</span>);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Python'</span>);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Python'</span>);
    &#125;, <span class="hljs-number">1000</span>)
  &#125;, <span class="hljs-number">1000</span>)
&#125;, <span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Promise的写法：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 链式编程</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;  <span class="hljs-comment">// 用不到reject时可以不传</span>
  <span class="hljs-comment">// 第一个异步事件</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve()
    &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 第一个异步事件的处理代码</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello World'</span>);
  <span class="hljs-comment">// 第二个异步事件</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;  <span class="hljs-comment">// 用不到reject时可以不传</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve()
    &#125;, <span class="hljs-number">1000</span>)
  &#125;)
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 第二个异步事件处理的代码</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Vuejs'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Vuejs'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Vuejs'</span>);
  <span class="hljs-comment">// 第三个异步事件</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;  <span class="hljs-comment">// 用不到reject时可以不传</span>
     <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
       resolve()
    &#125;,<span class="hljs-number">1000</span>)
  &#125;)
&#125;).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 第三个异步事件处理的代码</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Python'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Python'</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Python'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注：</strong> 其实第二个then()是跟在第一个then()后面的，第三个then()是跟在第二个then()后面的。而不是跟在Promise()后面</p>
<h3 data-id="heading-110">9-2、Promise的三种状态</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d785a1259dc64e79ab54825533ac5cc3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-111">9-3、Promise的链式编程</h3>
<p>网络请求到aaa -> 处理成aaa111 -> 再处理成aaa111222 -> 再拒绝处理成aaa111222error->再处理成aaa111222error444 。所以整个过程只有一个异步操作。</p>
<p>常规链式编程：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'aaa'</span>)
    &#125;, <span class="hljs-number">1000</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa</span>
    <span class="hljs-comment">// 2.对结果进行第一次处理</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      resovle(data + <span class="hljs-string">'111'</span>)
    &#125;)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      resovle(data + <span class="hljs-string">'222'</span>)
    &#125;)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">reject</span> =></span> &#123;
      reject(data + <span class="hljs-string">'error'</span>)
    &#125;)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// 这里没有输出，不会被执行的</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      resovle(data + <span class="hljs-string">'333'</span>)
    &#125;)
  &#125;).catch(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222error</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      resovle(data + <span class="hljs-string">'444'</span>)
    &#125;)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222error444</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>new Promise(resolve => resolve(结果))简写：</p>
<ul>
<li>①Promise.resovle()：将数据包装成Promise对象，并且在内部回调resolve()函数</li>
<li>②Promise.reject()：将数据包装成Promise对象，并且在内部回调reject()函数</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'aaa'</span>)
    &#125;, <span class="hljs-number">1000</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa</span>
    <span class="hljs-comment">// 2.对结果进行第一次处理</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resovle(data + <span class="hljs-string">'111'</span>)   <span class="hljs-comment">// Promise.resolve的简写</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resovle(data + <span class="hljs-string">'222'</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(data + <span class="hljs-string">'error'</span>)  <span class="hljs-comment">// Promise.reject的简写</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// 这里没有输出，不会被执行的</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resovle(data + <span class="hljs-string">'333'</span>)
  &#125;).catch(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222error</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resovle(data + <span class="hljs-string">'444'</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222error444</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>省略掉Promise.resolve
如果我们希望数据直接包装成Promise.resolve，那么在then中可以直接返回数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'aaa'</span>)
    &#125;, <span class="hljs-number">1000</span>)
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa</span>
    <span class="hljs-comment">// 2.对结果进行第一次处理</span>
    <span class="hljs-keyword">return</span> data + <span class="hljs-string">'111'</span>   <span class="hljs-comment">// Promise.resolve的简写</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111</span>
    <span class="hljs-keyword">return</span> data + <span class="hljs-string">'222'</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222</span>
    <span class="hljs-keyword">throw</span> data + <span class="hljs-string">'error'</span>  <span class="hljs-comment">// Promise.reject的简写</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// 这里没有输出，不会被执行的</span>
    <span class="hljs-keyword">return</span> data + <span class="hljs-string">'333'</span>
  &#125;).catch(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222error</span>
    <span class="hljs-keyword">return</span> data + <span class="hljs-string">'444'</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);  <span class="hljs-comment">// => aaa111222error444</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-112">9-4、Promise的all</h3>
<p>某个请求需要两个请求都完成才能继续进行：</p>
<p>Promise.all([ ])  // 数组类型，因为要放多个请求</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">Promise</span>.all([
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'why'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;)
      &#125;, <span class="hljs-number">2000</span>)
    &#125;),
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'kobe'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">19</span>&#125;)
      &#125;, <span class="hljs-number">1000</span>)
    &#125;)
  ]).then(<span class="hljs-function"><span class="hljs-params">results</span> =></span> &#123;  <span class="hljs-comment">// 两个请求都完成时才调用</span>
    <span class="hljs-built_in">console</span>.log(results);
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两秒后显示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/086751eea6d84992b7c0f4245cee4ef3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-113">五、Vuex详解</h1>
<h3 data-id="heading-114">1、认识Vuex</h3>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。
可以简单的将其看成把需要多个组件共享的变量全部存储在一个对象里面。然后，将这个对象放在顶层的Vue实例中，让其他组件可以使用。
Vuex是响应式的。</p>
<p>在多个界面间的共享的可以放在Vuex，比如用户的登录状态、用户名称、头像、地理位置信息等等。比如商品的收藏、购物车中的物品等等。
这些状态信息，我们都可以放在统一的地方，对它进行保存和管理，而且它们还是响应式的</p>
<h2 data-id="heading-115">2、Vuex的基本使用</h2>
<p>安装Vuex插件：npm install vuex --save</p>
<p>在src下建文件夹：store（仓库）</p>
<p>再建index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-comment">// 安装插件</span>
Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  state&#123;&#125;,
  mutations&#123;&#125;,
  actions&#123;&#125;,
  getters&#123;&#125;,
  <span class="hljs-attr">modules</span>: &#123;&#125;
&#125;)

<span class="hljs-comment">// 导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js引用（挂载到vue实例中）</p>
<p>这样，在其他Vue组件中，我们就可以通过this.$store的方式，获取到这个store对象了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>  <span class="hljs-comment">// 导入store</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  store,  <span class="hljs-comment">// 导入store</span>
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-116">2-1、Vuex状态管理图例</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57fcf8576cc54059a153c96a4b3927e0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-117">2-2、小案例</h3>
<p>index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  state&#123;
    count = <span class="hljs-number">1000</span>
  &#125;,
  mutations&#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">state</span>)</span>&#123;  <span class="hljs-comment">// 调用state</span>
      state.count++
    &#125;,
    <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params">state</span>)</span>&#123;
      state.count--
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挂载到Vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>  <span class="hljs-comment">// 导入store</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  store,  <span class="hljs-comment">// 导入store</span>
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用vuex</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$store.state.count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"sub"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>)  <span class="hljs-comment">// 通过commit(提交)mutation的方式引用increment方法</span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">sub</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'decrement'</span>)
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-118">3、Vuex的核心</h2>
<h3 data-id="heading-119">3-1、State</h3>
<h3 data-id="heading-120">3-2、Getters</h3>
<p>类似于computed（计算属性）</p>
<p><strong>基本使用：</strong>
需要从store中获取一些state变异后的状态，就使用getters。</p>
<p><strong>作为参数：</strong>
<strong>需要传递参数：</strong>
getters默认是不能传递参数的, 如果希望传递参数, 那么只能让getters本身返回另一个函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  state:&#123;
    <span class="hljs-attr">student</span>:[&#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">'durant'</span>,
      <span class="hljs-attr">age</span>:<span class="hljs-number">35</span>
    &#125;,&#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">'curry'</span>,
      <span class="hljs-attr">age</span>:<span class="hljs-number">30</span>
    &#125;]
  &#125;,
  <span class="hljs-attr">getters</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">more20stu</span>(<span class="hljs-params">state</span>)</span>&#123;    <span class="hljs-comment">// 基本使用</span>
      <span class="hljs-keyword">return</span> state.students.filter(<span class="hljs-function"><span class="hljs-params">s</span> =></span> s.age > <span class="hljs-number">20</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">more20stuNumber</span>(<span class="hljs-params">state,getters</span>)</span>&#123;   <span class="hljs-comment">// getters作为参数</span>
      <span class="hljs-keyword">return</span> getters.more20stu.length
    &#125;,
    <span class="hljs-function"><span class="hljs-title">moreAgeStu</span>(<span class="hljs-params">state</span>)</span> &#123;  <span class="hljs-comment">// 传递参数的方式：返回一个函数</span>
      <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">age</span> =></span> &#123;
        <span class="hljs-keyword">return</span> state.students.filter(<span class="hljs-function"><span class="hljs-params">s</span> =></span> s.age > age)
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$store.getters.more20stu&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$store.getters.more20stuNumber&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$store.getters.moreAgeStu(32)&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-121">3-3、Mutation（状态更新）</h3>
<h4 data-id="heading-122">（1）基本使用</h4>
<p>Vuex的store状态的更新唯一方式：提交Mutation</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  mutations&#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">state</span>)</span>&#123;  <span class="hljs-comment">// 第一个参数必须为state</span>
      state.count++
    &#125;,
    <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params">state</span>)</span>&#123;
      state.count--
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>必须用commit调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    methods:&#123;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>)  <span class="hljs-comment">// 通过commit(提交)mutation的方式引用increment方法</span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">sub</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'decrement'</span>)
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-123">（2）传递参数</h4>
<p>事件名(state，payload)
payload（负载），可以是一个参数，也可以是一个对象（需要传递多个参数时，可以包装在对象里传递）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  mutations&#123;
    <span class="hljs-function"><span class="hljs-title">incrementCount</span>(<span class="hljs-params">state,counter</span>)</span>&#123;  <span class="hljs-comment">// 第一个参数必须为state</span>
      state.count += counter
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    methods:&#123;
      <span class="hljs-function"><span class="hljs-title">addCounter</span>(<span class="hljs-params">counter</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>,counter)
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-124">（3）提交风格</h4>
<ul>
<li>①普通：commit('事件名'，参数)</li>
<li>②commit(&#123;type:'事件名',参数&#125;)  对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  methods:&#123;
      <span class="hljs-function"><span class="hljs-title">addCounter</span>(<span class="hljs-params">counter</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(&#123;
          <span class="hljs-attr">type</span>:<span class="hljs-string">'increment'</span>,
          counter
        &#125;)
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">  mutations&#123;
    <span class="hljs-function"><span class="hljs-title">incrementCount</span>(<span class="hljs-params">state,payload</span>)</span>&#123;  <span class="hljs-comment">// 此时的payload是一个对象，而之前的提交风格payload是counter</span>
      state.count += payload.counter
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-125">（4）响应式</h4>
<p>Vuex的store中的state是响应式的, 当state中的数据发生改变时, Vue组件会自动更新.
Vuex对应的响应式规则：提前在store中初始化好所需的属性.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  state:&#123;
    <span class="hljs-attr">info</span>:&#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">'durant'</span>,
      <span class="hljs-attr">number</span>:<span class="hljs-number">7</span>,
      <span class="hljs-attr">height</span>:<span class="hljs-number">2.11</span>
    &#125;
  &#125;,
  mutations&#123;
    <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params">state</span>)</span>&#123;
      state.info.name = <span class="hljs-string">'curry'</span> <span class="hljs-comment">// 响应式</span>
      state.info[<span class="hljs-string">'address'</span>] = <span class="hljs-string">'布鲁克林'</span>  <span class="hljs-comment">// 非响应式，但是info会添加 address:'布鲁克林'</span>
      Vue.set(state.info,<span class="hljs-string">'address'</span>,<span class="hljs-string">'华盛顿'</span>) <span class="hljs-comment">// 响应式</span>
      <span class="hljs-keyword">delete</span> state.info.number  <span class="hljs-comment">// 非响应式,但是info会删除 number:7</span>
      Vue.delete(state.info,<span class="hljs-string">'number'</span>) <span class="hljs-comment">// 响应式</span>
      <span class="hljs-comment">// Vue.set和Vue.delete 的第二个参数只能是string或者number</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$store.state.info&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'change'</span>></span>改变<span class="hljs-tag"><<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">change</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'change'</span>)
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-126">（5）常量类型</h4>
<p>在mutation中, 我们定义了很多事件类型(也就是其中的方法名称).</p>
<p>当我们的项目增大时，Vuex管理的Mutation中的方法越来越多，方法过多，使用者需要花费大量的经历去记住这些方法, 甚至是多个文件间来回切换, 查看方法名称, 甚至如果不是复制的时候, 可能还会出现写错的情况.</p>
<p><strong>官方推荐：</strong> 使用常量替代Mutation事件的类型，我们可以将这些常量放在一个单独的文件中，方便管理以及让整个app所有的事件类型一目了然。</p>
<p>新建mutations-type.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> INCREMENT = <span class="hljs-string">'increment'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> DECREMENT = <span class="hljs-string">'decrement'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">import</span> &#123;INCREMENT,DECREMENT&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./mutations-types"</span>  <span class="hljs-comment">// 导入常量类型</span>

Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  state&#123;
    count = <span class="hljs-number">1000</span>
  &#125;,
  mutations&#123;
    [INCREMENT](state)&#123;  <span class="hljs-comment">// [常量]()&#123;&#125;</span>
      state.count++
    &#125;,
    [DECREMENT](state)&#123;
      state.count--
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用vuex</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123;$store.state.count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"sub"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123;INCREMENT,DECREMENT&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./mutations-types"</span>  <span class="hljs-comment">// 导入常量类型</span>
  
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
    <span class="hljs-attr">methods</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(INCREMENT)  <span class="hljs-comment">// 不再是字符串形式</span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">sub</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.$store.commit(DECREMENT)
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-127">（6）只能同步操作</h4>
<p>Vuex要求我们Mutation中的方法必须是同步方法.</p>
<p>主要的原因是当我们使用devtools时, 可以devtools可以帮助我们捕捉mutation的快照.
但是如果是异步操作, 那么devtools将不能很好的追踪这个操作什么时候会被完成.</p>
<h3 data-id="heading-128">3-4、Action</h3>
<p>Action类似于Mutation, 但是是用来代替Mutation进行异步操作的。</p>
<p>第一个参数context（上下文），它是和store对象具有相同方法和属性的对象。
也可以传递payload。</p>
<p>调用：是dispatch。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4f8c325c68a4fa6a7b86ae6a25472da~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
当我们的异步操作或者说网络请求成功或者失败的时候执行一些代码时，我们可以利用Promise。
将异步操作或者网络请求放在Promise里，但是<strong>then()和catch()是跟在dispatch后面的</strong>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d233f3f13854496b396e43b058c171c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-129">3-5、Module</h3>
<p>Vuex允许我们将store分割成模块(Module), 而每个模块拥有自己的state、mutations、actions、getters等。但是模块最好最多两个。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2f8928d39d54a849a6a2ee06d00e29e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-130">4、store的项目结构组织图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c6accf583b8464aba116a8c74bb38ad~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            