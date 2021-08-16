
---
title: 'Vuex状态管理的那些事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b2af0f12cbe4e8faba8f3312797f9f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 20:35:53 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b2af0f12cbe4e8faba8f3312797f9f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">组件内的状态管理流程</h2>
<p>Vue 最核心的两个功能：数据驱动和组件化。</p>
<p>组件化开发给我们带来了：</p>
<ul>
<li>更快的开发效率</li>
<li>更好的可维护性</li>
</ul>
<p>每个组件都有自己的状态、视图和行为等组成部分。</p>
<p>状态管理包含以下几部分：</p>
<ul>
<li>state，驱动应用的数据源；</li>
<li>view，以声明方式将 state 映射到视图；</li>
<li>actions，响应在 view 上的用户输入导致的状态变化。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b2af0f12cbe4e8faba8f3312797f9f0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中的箭头是数据的流向，此时数据的流向是单向的。state（状态）就是我们说的数据，数据绑定到视图，展示给用户，当用户和视图交互，通过actions更改数据后，再把更改后的数据重新绑定到视图。单向的数据流程特别清晰，但是多个组件共享数据的时候会破坏这种简单的结构。</p>
<h2 data-id="heading-1">组件间通信方式</h2>
<p>大多数场景下的组件都并不是独立存在的，而是相互协作共同构成了一个复杂的业务功能。在 Vue 中为 不同的组件关系提供了不同的通信规则。</p>
<h3 data-id="heading-2">父组件给子组件传值</h3>
<ul>
<li>子组件中通过props接收数据</li>
<li>父组件中给子组件通过相应属性传值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Props Down Child<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// props: ['title'],</span>
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Props Down Parent<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"My journey with Vue"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">'./Child'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    child
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">子组件给父组件传值</h3>
<p>在子组件中使用 $emit 发布一个自定义事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; fontSize: fontSize + 'em' &#125;"</span>></span>Props Down Child<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handler"</span>></span>文字增大<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">fontSize</span>: <span class="hljs-built_in">Number</span>
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    handler () &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'enlargeText'</span>, <span class="hljs-number">0.1</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用这个组件的时候，使用 v-on 监听这个自定义事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; fontSize: hFontSize + 'em'&#125;"</span>></span>Event Up Parent<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

    这里的文字不需要变化

    <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:fontSize</span>=<span class="hljs-string">"hFontSize"</span> <span class="hljs-attr">v-on:enlargeText</span>=<span class="hljs-string">"enlargeText"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:fontSize</span>=<span class="hljs-string">"hFontSize"</span> <span class="hljs-attr">v-on:enlargeText</span>=<span class="hljs-string">"enlargeText"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">:fontSize</span>=<span class="hljs-string">"hFontSize"</span> <span class="hljs-attr">v-on:enlargeText</span>=<span class="hljs-string">"hFontSize += $event"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">'./Child'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    child
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">hFontSize</span>: <span class="hljs-number">1</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    enlargeText (size) &#123;
      <span class="hljs-built_in">this</span>.hFontSize += size
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">不相关组件之间传值</h3>
<p>不相关组件之间传值也是使用自定义事件传值，但是与子组件给父组件传值不同的是，因为没有父子关系，所以不能在子组件触发事件传值，这里需要通过 Event Bus 来传值，就是创建一个公共的vue实例，这个vue实例的作用是作为事件组件或者事件中心。
<strong>方法：</strong>
eventbus.js :</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vue()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在需要通信的两端：</p>
<p>使用 $on 订阅：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 没有参数</span>
bus.$on(<span class="hljs-string">'自定义事件名称'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 执行操作</span>
&#125;)

<span class="hljs-comment">// 有参数</span>
bus.$on(<span class="hljs-string">'自定义事件名称'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-comment">// 执行操作</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 $emit 发布：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 没有自定义传参</span>
bus.$emit(<span class="hljs-string">'自定义事件名称'</span>);

<span class="hljs-comment">// 有自定义传参</span>
bus.$emit(<span class="hljs-string">'自定义事件名称'</span>, 数据);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>例子：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// eventbus.js</span>
<span class="hljs-comment">// 这个文件仅仅导出一个vue实例</span>
<span class="hljs-comment">// 这个实例并不用来展示内容，使用的目的是调用它的$emit和$on，用来触发和注册事件</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vue()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Event Bus Sibling01<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"sub"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 30px; text-align: center"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"value"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> bus <span class="hljs-keyword">from</span> <span class="hljs-string">'./eventbus'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-built_in">Number</span>
  &#125;,
  created () &#123;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">this</span>.num
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: -<span class="hljs-number">1</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    sub () &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.value > <span class="hljs-number">1</span>) &#123;
        <span class="hljs-built_in">this</span>.value--
        bus.$emit(<span class="hljs-string">'numchange'</span>, <span class="hljs-built_in">this</span>.value) <span class="hljs-comment">// 触发事件</span>
      &#125;
    &#125;,
    add () &#123;
      <span class="hljs-built_in">this</span>.value++
      bus.$emit(<span class="hljs-string">'numchange'</span>, <span class="hljs-built_in">this</span>.value)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.number</span> &#123;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">cursor</span>: pointer;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">text-align</span>: center;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Event Bus Sibling02<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> bus <span class="hljs-keyword">from</span> <span class="hljs-string">'./eventbus'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">''</span>
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-comment">// 注册事件</span>
    bus.$on(<span class="hljs-string">'numchange'</span>, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.msg = <span class="hljs-string">`您选择了<span class="hljs-subst">$&#123;value&#125;</span>件商品`</span>
    &#125;)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">父直接访问子组件：通过 ref 获取子组件</h3>
<p>只有当项目比较小，或者开发自定义组件的时候，才会使用这种方式；大型项目的时候还是要使用vuex。</p>
<p>ref 有两个作用：</p>
<ul>
<li>如果你把它作用到普通 HTML 标签上，则获取到的是 DOM</li>
<li>如果你把它作用到组件标签上，则获取到的是组件实例</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>ref Child<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"input"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    focus () &#123;
      <span class="hljs-built_in">this</span>.$refs.input.focus()
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>ref Parent<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"c"</span>></span><span class="hljs-tag"></<span class="hljs-name">child</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> child <span class="hljs-keyword">from</span> <span class="hljs-string">'./04-Child'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    child
  &#125;,
  mounted () &#123;
    <span class="hljs-built_in">this</span>.$refs.c.focus()
    <span class="hljs-built_in">this</span>.$refs.c.value = <span class="hljs-string">'hello input'</span>
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>$refs</code> 只会在组件渲染完成之后生效，并且它们不是响应式的。这仅作为一个用于直接操作子组 件的“逃生舱”——你应该避免在模板或计算属性中访问 <code>$refs</code> 。</p>
</blockquote>
<h2 data-id="heading-6">简易的状态管理方案</h2>
<p>如果多个组件之间要共享状态(数据)，使用上面的方式虽然可以实现，但是比较麻烦，而且多个组件之间互相传值很难跟踪数据的变化，如果出现问题很难定位问题。</p>
<p>当遇到多个组件需要共享状态的时候，典型的场景：购物车。我们如果使用上述的方案都不合适，我们会遇到以下的问题：</p>
<ul>
<li>多个视图依赖于同一状态。</li>
<li>来自不同视图的行为需要变更同一状态。</li>
</ul>
<p>对于问题一，传参的方法对于多层嵌套的组件将会非常繁琐，并且对于兄弟组件间的状态传递无能为 力。</p>
<p>对于问题二，我们经常会采用父子组件直接引用或者通过事件来变更和同步状态的多份拷贝。以上的这些模式非常脆弱，通常会导致无法维护的代码</p>
<p>因此，我们为什么不把组件的共享状态抽取出来，以一个全局单例模式管理呢？在这种模式下，我们的 组件树构成了一个巨大的“视图”，不管在树的哪个位置，任何组件都能获取状态或者触发行为！
我们可以把多个组件的状态，或者整个程序的状态放到一个集中的位置存储，并且可以检测到数据的更改。你可能已经想到了 Vuex。</p>
<p>这里我们先以一种简单的方式来实现。</p>
<ul>
<li>首先创建一个共享的仓库 store 对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">user</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'xiaomao'</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
      <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>
    &#125;
  &#125;,
  setUserNameAction (name) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.debug) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setUserNameAction triggered：'</span>, name)
    &#125;
    <span class="hljs-built_in">this</span>.state.user.name = name
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>把共享的仓库 store 对象，存储到需要共享状态的组件的 data 中</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>componentA<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    user name: &#123;&#123; sharedState.user.name &#125;&#125;
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"change"</span>></span>Change Info<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">methods</span>: &#123;
    change () &#123;
      store.setUserNameAction(<span class="hljs-string">'componentA'</span>)
    &#125;
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">privateState</span>: &#123;&#125;,
      <span class="hljs-attr">sharedState</span>: store.state
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们继续延伸约定，组件不允许直接变更属于 store 对象的 state，而应执行 action 来分发 (dispatch) 事件通知 store 去改变，这样最终的样子跟 Vuex 的结构就类似了。这样约定的好处是，我们能够记录所有 store 中发生的 state 变更，同时实现能做到记录变更、保存状态快照、历史回滚/时光旅行的先进的调试工具。</p>
<h2 data-id="heading-7">Vuex 回顾</h2>
<h3 data-id="heading-8">什么是 Vuex</h3>
<blockquote>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件 的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 也集成到 Vue 的官方调试工具 devtools extension，提供了诸如零配置的 time-travel 调试、状态快照导入导出等高级调 试功能。</p>
</blockquote>
<ul>
<li>Vuex 是专门为 Vue.js 设计的状态管理库</li>
<li>它采用集中式的方式存储需要共享的数据</li>
<li>从使用角度，它就是一个 JavaScript 库</li>
<li>它的作用是进行状态管理，解决复杂组件通信，数据共享</li>
</ul>
<h3 data-id="heading-9">什么情况下使用 Vuex</h3>
<blockquote>
<p>官方文档：</p>
<p>Vuex 可以帮助我们管理共享状态，并附带了更多的概念和框架。这需要对短期和长期效益进行权衡。</p>
<p>如果您不打算开发大型单页应用，使用 Vuex 可能是繁琐冗余的。确实是如此——如果您的应用够简单，您最好不要使用 Vuex。一个简单的 store 模式就足够您所需了。但是，如果您需要构建一个中大型单页应用，您很可能会考虑如何更好地在组件外部管理状态，Vuex 将会成为自然而然的选择。引用 Redux 的作者 Dan Abramov 的话说就是：Flux 架构就像眼镜：您自会知道什么时候需要它。</p>
</blockquote>
<p>当你的应用中具有以下需求场景的时候：</p>
<ul>
<li>多个视图依赖于同一状态</li>
<li>来自不同视图的行为需要变更同一状态</li>
</ul>
<p>建议符合这种场景的业务使用 Vuex 来进行数据管理，例如非常典型的场景：购物车。</p>
<blockquote>
<p>注意：Vuex 不要滥用，不符合以上需求的业务不要使用，反而会让你的应用变得更麻烦。</p>
</blockquote>
<h3 data-id="heading-10">核心概念回顾</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30506fc6f37b4d209c4fa690180ecb51~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>Store（仓库）</strong>：Store是使用vuex应用程序的核心，每个应用只有一个Store，Store是一个容器，包含着应用中的大部分状态。当然我们不能直接改变应用中的状态，要通提交Mutations的方式改变状态。</li>
<li><strong>State（状态）</strong>：State保存在Store中，因为Store是唯一的，因此State也是唯一的，称为单一状态树。但是所有的状态都保存在State中的话，会让程序难以维护，可以通过后续的模块解决该问题。这里的状态是响应式的。</li>
<li><strong>Getter</strong>：Getter就像是Vuex中的计算属性，方便从一个属性派生出其他的值，它内部可以对计算的结果进行缓存，只有当依赖的状态发生改变的时候，才会重新计算。</li>
<li><strong>Mutations</strong>：状态的变化需要提交Mutations才能完成。</li>
<li><strong>Actions</strong>：Actions和Mutations类似，不同的是，Actions可以进行异步操作，内部改变状态的时候都需要提交Mutations。</li>
<li><strong>Module</strong>（模块）：由于使用单一状态树，应用的所有状态会集中到比较大的对象上来。当应用变得非常复杂时，Store就会变得相当臃肿。为了解决以上问题，Vuex允许将Stor分割成模块，每个模块拥有自己State、Getter、Mutations、Actions，甚至是嵌套的子模块。</li>
</ul>
<h3 data-id="heading-11">示例演示</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fjacy1016%2Fvuex-demo.git" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/jacy1016/vuex-demo.git" ref="nofollow noopener noreferrer">vuex-demo</a></p>
<p><strong>基本结构</strong></p>
<ul>
<li>导入 Vuex</li>
<li>注册 Vuex</li>
<li>注入 $store 到 Vue 实例</li>
</ul>
<p><strong>State</strong></p>
<p>Vuex 使用单一状态树，用一个对象就包含了全部的应用层级状态。</p>
<p>使用 mapState 简化 State 在视图中的使用，mapState 返回计算属性。</p>
<p>mapState 有两种使用的方式：</p>
<ul>
<li>接收数组参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 该方法是 vuex 提供的，所以使用前要先导入 </span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-comment">// mapState 返回名称为 count 和 msg 的计算属性</span>
<span class="hljs-comment">// 在模板中直接使用 count 和 msg</span>
<span class="hljs-attr">computed</span>: &#123;
  ...mapState([<span class="hljs-string">'count'</span>, <span class="hljs-string">'msg'</span>])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接收对象参数</li>
</ul>
<p>如果当前视图中已经有了 count 和 msg，如果使用上述方式的话会有命名冲突，解决的方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 该方法是 vuex 提供的，所以使用前要先导入</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-comment">// 通过传入对象，可以重命名返回的计算属性</span>
<span class="hljs-comment">// 在模板中直接使用 num 和 message</span>
<span class="hljs-attr">computed</span>: &#123;
  ...mapState(&#123;
    <span class="hljs-attr">num</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count, 
    <span class="hljs-attr">message</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.msg 
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Getter</strong></p>
<p>Getter 就是 store 中的计算属性，使用 mapGetter 简化视图中的使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-attr">computed</span>: &#123;
  ...mapGetter([<span class="hljs-string">'reverseMsg'</span>]),
  <span class="hljs-comment">// 改名，在模板中使用 reverse</span>
  ...mapGetter(&#123;
    <span class="hljs-attr">reverse</span>: <span class="hljs-string">'reverseMsg'</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Mutation</strong></p>
<p>更改 Vuex 的 store 中的状态的唯一方法是提交 mutation。Vuex 中的 mutation 非常类似于事件：每个 mutation 都有一个字符串的 事件类型 (type) 和 一个 回调函数 (handler)。这个回调函数就是我们实际进行状态更改的地方，并且它会接受 state 作为第一个参数。</p>
<p>使用 Mutation 改变状态的好处是，集中的一个位置对状态修改，不管在什么地方修改，都可以追踪到状态的修改。可以实现高级的 time-travel 调试功能</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-attr">methods</span>: &#123;
  ...mapMutations([<span class="hljs-string">'increate'</span>]),
  <span class="hljs-comment">// 传对象解决重名的问题</span>
  ...mapMutations(&#123;
    <span class="hljs-attr">increateMut</span>: <span class="hljs-string">'increate'</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Action</strong></p>
<p>Action 类似于 mutation，不同在于：</p>
<ul>
<li>Action 提交的是 mutation，而不是直接变更状态。</li>
<li>Action 可以包含任意异步操作。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapActions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-attr">methods</span>: &#123;
  ...mapActions([<span class="hljs-string">'increate'</span>]),
  <span class="hljs-comment">// 传对象解决重名的问题</span>
  ...mapActions(&#123;
    <span class="hljs-attr">increateAction</span>: <span class="hljs-string">'increate'</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Module</strong></p>
<p>由于使用单一状态树，应用的所有状态会集中到一个比较大的对象。当应用变得非常复杂时，store 对象就有可能变得相当臃肿。</p>
<p>为了解决以上问题，Vuex 允许我们将 store 分割成模块（module）。每个模块拥有自己的 state、mutation、action、getter,甚至是嵌套子模块。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8a92b3a86614b6e80a8546a093ab08c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            