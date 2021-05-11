
---
title: '写给 React 开发的 Vue 上手指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8012'
author: 掘金
comments: false
date: Mon, 10 May 2021 18:31:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=8012'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">写给 React 开发的 Vue 上手指南</h1>
<h2 data-id="heading-1">前言</h2>
<p>Vue 和 React 是前端三大流行框架之二，它们在国内有多流行，不必解释。本人呆过不少团队，选择 Vue 的团队对 Vue 的第一印象是：简单、易上手。那么 Vue 是否真的如众多开发者所说的那么简单？能否让一个 React 前端程序猿快速上手？本文会从 React 开发的视角入手，介绍 Vue 的简单使用、特性和对比。</p>
<p>本文适合以下类型的读者：</p>
<ul>
<li>被上司逼着换 Vue 框架的 React 程序猿</li>
<li>精力旺盛想尝试 Vue 的 React 程序猿</li>
<li>Vue 、 React 浅度使用，想深入了解其中一项的程序猿</li>
</ul>
<p>阅读本文需要掌握以下知识：</p>
<ul>
<li>理解 this 指向</li>
<li>理解 ES6 的 class 、 解构赋值和箭头函数等语法</li>
</ul>
<p>另外，如果觉得看文档更加方便，这里提供传送门： <a href="https://cn.vuejs.org/index.html" target="_blank" rel="nofollow noopener noreferrer">cn.vuejs.org/index.html</a></p>
<h2 data-id="heading-2">Vue 简介</h2>
<p>来看看官网如何定义 Vue：</p>
<blockquote>
<p>渐进式 JavaScript 框架</p>
</blockquote>
<p>何为渐进式：与开箱即用相反，框架的规模根据你期望的项目规模灵活配置。Vue 本体只提供最基本的数据 - 视图渲染功能，如果想使用模块化开发，可以借助 <code>@vue/cli</code> ，如果想引入路由，可以添加 <code>vue-router</code>，如果想引入全局状态管理，可以添加 <code>vuex</code> ...如果这些还不能满足，还可以引入第三方或者自己编写的插件。<strong>Talk is cheap, show you the code</strong>，下面开始讲解代码：</p>
<h2 data-id="heading-3">极简体验</h2>
<p>把下面这段代码保存成 <code>.html</code> 文件，在浏览器打开就能看到效果（得联网）:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Simple Vue<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">

    <span class="hljs-keyword">const</span> template = <span class="hljs-string">`<h3>&#123;&#123; message &#125;&#125;</h3>`</span>;

    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">message</span>:; <span class="hljs-string">'Hello Vue!'</span>
          &#125;
        &#125;
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果大概就是：</p>
<blockquote>
<h3 data-id="heading-4">Hello Vue!</h3>
</blockquote>
<p>这种使用方式，类似于 <code>jQuery</code>，只要引入 <code>vue</code> 脚本，就能立马开发。</p>
<h2 data-id="heading-5">直观对比</h2>
<p>如果需要模块化开发，单单在 html 里写 vue 代码是很吃力的。让我们看看借助脚手架工具创建的单文件组件的写法：
这次简单点，实现一个只有标题和名称的表单：
使用 React 可以这么写：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cart</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// 属性类型检查</span>
  <span class="hljs-keyword">static</span> propTypes = &#123;
    <span class="hljs-attr">title</span>: PropTypes.string;
  &#125;
  <span class="hljs-comment">// 组件的状态</span>
  state = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'John Smith'</span>
  &#125;

  onChange = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">name</span>: e.target.value
    &#125;)
  &#125;

  submit = <span class="hljs-function">() =></span> &#123;
    alert(<span class="hljs-string">`你的名字是: <span class="hljs-subst">$&#123;state.name&#125;</span>`</span>)
  &#125;

  <span class="hljs-comment">// 渲染视图</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">props</span>: &#123; title &#125;,
      <span class="hljs-attr">state</span>: &#123; name &#125;,
      onChange,
      submit
    &#125; = <span class="hljs-built_in">this</span>;

    <span class="hljs-comment">// JSX 模板</span>
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;name&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;onChange&#125;</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;submit&#125;</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以，这很 OOP ，接下来看看 Vue 怎么写：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123;title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"name"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"submit"</span>></span>提交<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// 声明属性</span>
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-comment">// 声明状态</span>
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"John Smith"</span>
    &#125;
  &#125;,
  <span class="hljs-comment">// 回调</span>
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">settle</span>(<span class="hljs-params"></span>)</span> &#123;
      alert(<span class="hljs-string">`下单成功，总价: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.total&#125;</span>`</span>)
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一板一眼的，看起来非常规律，看起来很像在写 <code>html</code>。这里简单介绍一下 Vue 组件的特点：</p>
<ol>
<li>Vue 的组件以单文件形式存在，文件后缀为 <code>.vue</code> ，JavaScript 逻辑部分变成了配置式的写法。</li>
<li><code>template</code> 以双花括号<code>&#123;&#123;&#125;&#125;</code> 作占位符，用以插入表达式</li>
<li>标签属性比 <code>JSX</code> 复杂，但实现的功能也比较多。</li>
<li>代表状态的 <code>data</code> 属性居然要写成一个函数，原因参考下文。</li>
</ol>
<h2 data-id="heading-6">概念梳理</h2>
<h3 data-id="heading-7">介绍 Template</h3>
<p><code>template</code> 是 Vue 用来组成 UI 视图的模板语法。有两种使用方式：</p>
<ul>
<li>如果使用脚手架创建的工程化 Vue 项目，可以新建 .vue 文件编写：</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"my-div"</span>></span>
    这是一个 .vue 文件，代表一个组件
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// JavaScript 逻辑</span>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-comment">/* 此处可以编写 CSS */</span>
    <span class="hljs-selector-class">.my-div</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">300</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 会通过编译工具，把上述代码编译成 JavaScript 代码。</p>
<ul>
<li>如果在纯 JavaScript 中使用，那么 template 要写成字符串形式：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MyComp = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div class="my-div">这也是一个 vue 组件</div>`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得一提的是： <code>template</code> 不会直接变成 <code>html</code> ，而是会变成一个 <code>render</code> 函数，拿上文的 MyComp 的 template 举例，编译以后会变成（伪代码）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">render</span>: (createElement) &#123;
    <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'div'</span>, &#123; <span class="hljs-attr">staticClass</span>: <span class="hljs-string">'my-div'</span>&#125;, <span class="hljs-string">'这也是一个 vue 组件'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下文会对 <code>render</code> 函数进行进一步介绍</p>
<h4 data-id="heading-8">Template 指令</h4>
<p>指令是 Vue 特殊的属性，借助 Vue 丰富的指令，可以完成很多数据与视图交互功能：</p>
<h5 data-id="heading-9">v-bind —— 表达式绑定指令</h5>
<p>普通的属性会当作字符串处理，而 <code>v-bind</code> 则会解析其中的 JavaScript 表达式</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><my-comp v-bind:value=<span class="hljs-string">"myValue * 2"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>myValue</code> 是你定义的变量可以来自于组件上的 <code>data</code> 、 <code>props</code> 、<code>methods</code> 等。
不过 <code>v-bind</code> 太长了，一般会省略掉，可以简写成：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><my-comp :value=<span class="hljs-string">"myValue * 2"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">v-on —— 回调绑定指令</h5>
<p>跟 <code>v-bind</code> 差不多， <code>v-on</code> 用来绑定回调：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><my-comp v-on:change=<span class="hljs-string">"handleChange"</span> />
<!-- 可以传入参数，并且不会立即执行 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">my-comp</span> <span class="hljs-attr">v-on:change</span>=<span class="hljs-string">"handleChange(1, 2, 3)"</span> /></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简写：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><my-comp @change=<span class="hljs-string">"handleChange"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">v-model —— 双向绑定指令</h5>
<p>这是一条复合指令，用来对表单元素或者自定义组件的双向绑定，一般在 <code>input</code>、 <code>textarea</code> 等表单元素中使用：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><input v-model=<span class="hljs-string">"inputValue"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等价于</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><input :value=<span class="hljs-string">"inputValue"</span> @input=<span class="hljs-string">"e => inputValue = e.target.value"</span> type=<span class="hljs-string">"text"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">v-for —— 循环指令</h5>
<p>常用于列表渲染，记得带上 key</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><li v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"(item, index) in list"</span>>&#123;&#123;index&#125;&#125; - &#123;&#123;item.name&#125;&#125; </li>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了数组，对字符串、对象同样可以使用，甚至还可以直接写个数字表示循环次数。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span v-<span class="hljs-keyword">for</span>=<span class="hljs-string">"num in 6"</span>>&#123;&#123;num&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">v-if/v-else —— 条件渲染指令</h5>
<p>顾名思义，通过条件决定元素渲染与否</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"scrore >= 100"</span>>你是满分</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"scrore >= 60"</span>></span>你及格了<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else</span>></span>你挂了<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">子节点渲染</h4>
<p>如同 JSX 中的 <code>children</code> , <code>template</code> 中的字节的需要使用 <code>slot</code> （插槽）作为占位：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div> <span class="hljs-built_in">this</span> is <span class="hljs-keyword">default</span> <slot><<span class="hljs-regexp">/slot> </</span>div>
<!-- 还可以绑定带有命名空间的插槽 -->
<div> <span class="hljs-built_in">this</span> is named <slot name=<span class="hljs-string">"bar"</span>></slot><div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父节点传入：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><!-- <span class="hljs-built_in">this</span> is <span class="hljs-keyword">default</span> child node -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Foo</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span> child node <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Foo</span>></span></span>

<!-- <span class="hljs-built_in">this</span> is named bar node -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Foo</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"bar"</span>></span> bar node <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Foo</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">如果不用 Template</h3>
<p>尽管 <code>template</code> 能覆盖绝大部分视图场景，但 <code>template</code> 并不是唯一的选择。 Vue 组件 API 中提供了一个 <code>render</code> 函数选项，用 JavaScript 的方法直接创建虚拟 DOM：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    render (createElement) &#123;
        <span class="hljs-keyword">return</span> createElement(<span class="hljs-string">'h3'</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">'Hello Vue!'</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>emmmm... 标签 属性 子节点...有没有似曾相识的感觉？没错，如果 React 不借助 JSX ，也是在 <code>render</code> 方法中调用 <code>createElement</code> 创建虚拟 DOM ，那么问题来了：能不能使用 JSX 来编写 Vue 组件？
答案是<strong>能</strong>，借助 <code>@vue/babel-preset-jsx</code> 这个 babel 插件，就能实现 JSX 编写 Vue 组件视图，详情参考：<a href="https://cn.vuejs.org/v2/guide/render-function.html#JSX" target="_blank" rel="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/re…</a></p>
<h3 data-id="heading-16">一言难尽的 this —— Vue 篇</h3>
<p><code>this</code> 真是一个令人又爱又恨的东西，好在 Vue 组件中，绝大部分方法都会把 this 指向当前组件，并且不需要区分 <code>props</code> 、<code>data</code> （直接 <code>this.xxx</code> 一把梭）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">propA</span>: <span class="hljs-built_in">Number</span>,
        <span class="hljs-attr">propB</span>: <span class="hljs-built_in">String</span>,
    &#125;,
    data () &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.propA); <span class="hljs-comment">// propA 传入的值</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.propB); <span class="hljs-comment">// propB 传入的值</span>
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">dataA</span>: <span class="hljs-string">'a'</span>,
            <span class="hljs-attr">dataB</span>: <span class="hljs-string">'b'</span>,
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">getDataA</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">getPropA</span>(<span class="hljs-params"></span>)</span> &#123;
            retun <span class="hljs-built_in">this</span>.propA;
        &#125;,
        getMethodA () &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.getDataA); <span class="hljs-comment">// function</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.getPropA); <span class="hljs-comment">// function</span>
        &#125;
    &#125;,
    <span class="hljs-comment">// ....</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：<strong>箭头函数不会帮你绑定 this</strong>，除了 <code>data</code> 第一个参数可以访问当前组件，其他的箭头函数使用 this 是没用的：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-built_in">Number</span>,
    &#125;,
    <span class="hljs-attr">data</span>: <span class="hljs-function"><span class="hljs-params">context</span> =></span> (&#123;
        <span class="hljs-attr">doubleCount</span>: context.count * <span class="hljs-number">2</span> <span class="hljs-comment">// work , context 指向当前组件</span>
    &#125;),
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">// bad， this 不对</span>
        <span class="hljs-attr">badTripleCount</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.count * <span class="hljs-number">3</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了 <code>data</code> 、 <code>methods</code> 以外， <code>watch</code> 、 <code>computed</code> 或者部分声明周期钩子回调， this 同样指向当前组件。
如果你不喜欢 <code>this</code>， 可以尝试下文的 <strong>Composition API</strong></p>
<h3 data-id="heading-17">组件的状态 —— data</h3>
<p>在 React 中，组件的状态放在 state 中，修改状态需要调用 <code>setState</code> ，且最好使用新的对象代替：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">list</span>: [
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'foo'</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'bar'</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'baz'</span> &#125;,
    ]
  &#125;

  removeItem (id) &#123;
    <span class="hljs-keyword">const</span> &#123; list &#125; = <span class="hljs-built_in">this</span>.state;
    <span class="hljs-built_in">this</span>.setState(list.filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i.id !== id))
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Vue 中，组件的状态叫做 <code>data</code> ，但是绝大部分更新都可以由直接对属性赋值完成：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">list</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">setA</span>(<span class="hljs-params">num</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.a = num;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">appendToList</span>(<span class="hljs-params">num</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.list.push(num);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于实现原理，可以移步下文 <strong>响应式数据</strong>。</p>
<h3 data-id="heading-18">单向数据流</h3>
<p>同 React 一样，来自父组件的状态称为 <code>Props</code> ，且子组件不要直接修改父组件传入的状态：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">badSetTitle</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-comment">// BAD, 不要直接修改</span>
            <span class="hljs-built_in">this</span>.title = <span class="hljs-string">'????'</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果硬要修改，请使用 <code>Props</code> 回调：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">onChange</span>: <span class="hljs-built_in">Function</span>
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    setValue (value) &#123;
      <span class="hljs-built_in">this</span>.onChange(value);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件通过传入 <code>onChange</code> 回调实现修改：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyComp</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"myValue"</span> <span class="hljs-attr">:onChange</span>=<span class="hljs-string">"handleChange"</span> /></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-attr">myValue</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myValue = value
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者使用 Vue 约定的事件更新语法糖：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">setTitle</span>(<span class="hljs-params"></span>)</span> &#123;
           <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:title'</span>, <span class="hljs-string">'???'</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后父组件传入的 <code>prop</code> 也要做一次处理：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><!-- title 属性追加 .sync 修饰保证 update 事件生效 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyComponent</span> <span class="hljs-attr">title.sync</span>=<span class="hljs-string">"title"</span> /></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：<strong>这种方法将在 Vue3.0 废弃</strong> 。<br>
还有一种办法是：把 value 和 onChange 封装成 v-model （抱歉，template 编译就是可以为所欲为），但原理是一样的：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"type something"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"e => onChange(e.target.value)"</span> /></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">model</span>: &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'value'</span>,
      <span class="hljs-attr">event</span>: <span class="hljs-string">'change'</span>
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件中就可以一条 v-model 搞定：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><my-input v-model=<span class="hljs-string">"myValue"</span> />
<!-- 等价于 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">my-input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"myValue"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"e => myValue = e.target.value"</span> /></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">生命周期钩子</h3>
<p>组件不是一个持久化的东西，从创建、更新到销毁，每一个 timing 都可以处理一些逻辑，下面列举几个常用的生命周期钩子：</p>
<ul>
<li><code>beforeCreate</code> Vue 向组件实例组件挂载 <code>data</code> 、 <code>props</code> 等状态之前调用</li>
<li><code>created</code> 组件挂载 <code>data</code> 、 <code>props</code> 等状态之后调用，可以在此处发起网络请求获取数据</li>
<li><code>mounted</code> 对应 <code>componentDidMount</code> 组件第一次完成 DOM 渲染后的回调，可以在此处发起网络请求获取数据</li>
<li><code>updated</code> 对应 <code>componentDidUpdate</code> 组件更新完毕后调用，由于 Vue 响应式机制，这个方法大部分的场景会被 <code>watch</code> 替代。</li>
<li><code>beforeDestroy</code> 对应 <code>componentWillUnmount</code> 组件销毁之前的回调，通常用来清除计时器、某些原生监听事件等操作。</li>
</ul>
<p>其他诸如 <code>beforeMount</code> 、 <code>actived</code> 、 <code>destoryed</code> 等钩子的用法可以参考 <a href="https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90" target="_blank" rel="nofollow noopener noreferrer">cn.vuejs.org/v2/api/#%E9…</a></p>
<h2 data-id="heading-20">特性</h2>
<p>讲完了对比，接下来讲 Vue 的一些特性：</p>
<h3 data-id="heading-21">响应式数据</h3>
<p>如果你对响应式属性不熟悉，看到赋值也能触发更新，可能会觉得不可思议。事实上 Vue2.x 版本借助了 <code>Object.defineProperty</code> 方法，对响应式数据的 <code>get</code> 和 <code>set</code> 做了一层拦截处理，使得状态在赋值的时候触发了更新回调，从而进行更新操作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> valueA = <span class="hljs-number">1</span>;

<span class="hljs-keyword">let</span> data = &#123;&#125;;

<span class="hljs-built_in">Object</span>.defineProperty(data, <span class="hljs-string">'a'</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取 data.a'</span>)
    <span class="hljs-keyword">return</span> valueA 
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'更新 data.a'</span>)
    valueA = newVal;
  &#125;

&#125;) <span class="hljs-comment">// data 此时为 &#123; a: 1 &#125;</span>

data.a <span class="hljs-comment">// 输出 "获取 data.a"</span>
data.a = <span class="hljs-number">100</span> <span class="hljs-comment">// 输出 "更新 data.a"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管 <code>Object.defineProperty</code> 能让更新更符合直觉，但是这个 API 也有它的局限性：</p>
<ul>
<li>只能检测对象属性的更新，无法检测对象属性的添加和删除，上文如果直接进行 <code>data.b = 1</code> 赋值或者 <code>delete data.a</code> 删除， set 回调是不会触发的。需要借助 <code>Vue.set(data, 'b', 1)</code> 和 <code>Vue.delete(data, 'a')</code> 进行显式的添加和删除。</li>
<li>对于数组的 <code>push</code> 、 <code>pop</code> 、 <code>splice</code> 等改变原数组的方法，Vue 会隐式重写他们，使得我们直接对数组调用这些方法能够正常被监听。</li>
</ul>
<p>在 Vue3.x 中，使用了 <code>Proxy</code> API 替代了 <code>Object.defineProperty</code> ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> data = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;

<span class="hljs-keyword">const</span> proxyData = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(data, &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取 data.a'</span>)
    <span class="hljs-keyword">return</span> obj[key];
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'更新 data.a'</span>)
    obj[key] = value;
  &#125;
&#125;)

<span class="hljs-keyword">const</span> proxyArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">obj, key</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取 array[key]'</span>)
    <span class="hljs-keyword">return</span> obj[key];
  &#125;,
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">obj, key, value</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'更新 array[key]'</span>)
    obj[key] = value;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Proxy</code> 能更加优雅地拦截对象的变更，解决了无法对属性增删和拦截数组的问题，而且不需要对每一条属性进行拦截，在一定程度上减少了监听数据的开销。<br>
相比于 React ， Vue 能更细致地追踪数据的变化，尽可能减少组件更新的粒度。</p>
<h4 data-id="heading-22">data 应该是一个函数</h4>
<p>看了之前的几段代码你也许注意到一个问题： data 为什么是一个函数？
这是为了避免在创建多个组件时，引用相同的 data 导致多个组件的 data 相互影响：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> MyComponent = &#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
  &#125;
&#125;

<span class="hljs-comment">// 实例化组件的伪代码</span>
<span class="hljs-keyword">const</span> <span class="hljs-function"><span class="hljs-title">initComponent</span>(<span class="hljs-params">comp</span>)</span> &#123;
  <span class="hljs-keyword">const</span> compInstance = &#123;&#125;;

  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> comp.data) &#123;
    compInstance[key] = data[key];
  &#125;

  <span class="hljs-keyword">return</span> compInstance;
&#125;

<span class="hljs-keyword">const</span> comp1 = initComponent(MyComponent)
<span class="hljs-keyword">const</span> comp2 = initComponent(comp1)

comp1.a = <span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(comp1.a); <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(comp2.a); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何避免上述问题？你可能会想到对组件深拷贝，但是这样会造成不必要的性能浪费，为了优雅地解决这个问题，我们约定： data 应该做成一个返回对象的函数：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> MyComponent = &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 实例化组件的伪代码</span>
<span class="hljs-keyword">const</span> <span class="hljs-function"><span class="hljs-title">initComponent</span>(<span class="hljs-params">comp</span>)</span> &#123;
  <span class="hljs-keyword">const</span> compInstance = &#123;&#125;;

  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> comp.data()) &#123;
    compInstance[key] = data[key];
  &#125;

  <span class="hljs-keyword">return</span> compInstance;
&#125;

<span class="hljs-comment">// ...</span>

<span class="hljs-built_in">console</span>.log(comp1.a); <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(comp2.a); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">DOM 的异步更新</h3>
<p>同 React 一样， Vue 也会创建虚拟 DOM ，并且通过一系列的 Diff 算法和 Patch，把虚拟 DOM 转变成真实 DOM ，那么 Vue 中真实 DOM 什么时候更新呢？答案是状态变更后，借助 JavaScript 事件循环机制，在下一个微任务进行异步更新：</p>
<pre><code class="copyable"><template>
  <div id="msg">&#123;&#123; message &#125;&#125;</div>
</template>
<script>
export default &#123;
  data() &#123;
    message: 'hello world'
  &#125;,
  setData() &#123;
    document.getElementById('msg').innerHTML // 'hello world';

    this.message = 'goodbye world';
    // 此时 DOM 尚未更新
    document.getElementById('msg').innerHTML // 'hello world';

    // 下一轮微任务的回调， DOM 已然更新
    this.$nextTick(() => &#123;
      document.getElementById('msg').innerHTML // 'goodbye world';
    &#125;)

    // 噢，是个宏任务，已经更新很久了
    setTimeout(() => &#123;
      document.getElementById('msg').innerHTML // 'goodbye world';
    &#125;, 0)
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">小结</h2>
<p>本文是 <a href="https://juejin.cn/post/6952545904087793678" target="_blank">写给 Vue 开发的 React 上手指南</a> 的镜像文章，以React 开发者的视角介绍了 Vue 的特性和用法，旨在引导部分 React 转 Vue 的程序猿快速上手 Vue ，避免一些</p>
<h2 data-id="heading-25">问答环节</h2>
<h3 data-id="heading-26">感觉讲不完啊，还有什么能介绍的？</h3>
<p>要想把 Vue 的全貌压缩成一篇几百行的文章是不现实的，本文主要还是以 React 对照为主。如果想深入了解，这里推荐一些常见的用法和配置，带着这些问题翻文档吧：</p>
<ul>
<li>Vue 全局配置</li>
<li>插件的用法</li>
<li>自定义指令</li>
<li>computed 和 watch</li>
<li>Provide/Inject 依赖注入</li>
<li>组件实例方法(组件 this 上挂载了很多东西)</li>
<li>内置组件</li>
</ul>
<h3 data-id="heading-27">Vue 有好多相似的 API ，我应该用哪个？</h3>
<p><a href="https://juejin.cn/post/6868262202697056269" target="_blank">【Vue.js】 那些相似的 API，我该用哪个？ Vue API 用法大比拼</a></p></div>  
</div>
            