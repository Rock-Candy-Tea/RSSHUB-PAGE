
---
title: '3x1 精读Vue官方文档 -  自定义指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=831'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 17:58:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=831'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<h2 data-id="heading-1">简介</h2>
<p>Vue 指令可以分为”内置指令（例如：v-once，v-cloak等）“与“自定义指令“。
Vue 指令提供了操作底层 DOM 的能力，增强了 Vue 模板的处理功能。</p>
<ul>
<li><strong>局部注册指令</strong>，可以使用组件选项  <code>directives</code> 。</li>
<li><strong>全局注册指令</strong>，需要调用 Vue 构造函数的 <code>Vue.directive()</code> 方法</li>
</ul>
<h2 data-id="heading-2">钩子函数</h2>
<p>“指令”的构成与组件选项类似，有着自己独特的钩子函数。</p>
<ul>
<li><strong><code>bind</code></strong>: 只调用一次，当指令与元素进行绑定时调用，此时可以对元素进行初始化操作（比如事件的绑定）。</li>
<li><strong><code>inserted</code></strong>: 被绑定元素插入父节点时调用（但不能保证父节点本身已经插入到文档中）。</li>
<li><strong><code>update</code></strong>: 组件更新之前调用。</li>
<li><strong><code>componentUpdated</code></strong>: 组件更新之后调用。</li>
<li><strong><code>unbind</code></strong>: 只调用一次，当指令与元素解绑时调用，例如 <code>v-if</code> 控制的组件。</li>
</ul>
<p><strong><code>bind</code> 与 <code>inserted</code> 区别</strong></p>





















<table><thead><tr><th><strong>bind</strong></th><th><strong>inserted</strong></th></tr></thead><tbody><tr><td>是在元素（Vdom）被创建后并与指令进行绑定时调用。</td><td>元素与指令绑定完成，并被插入到父节点时调用。</td></tr><tr><td>触发时元素没有插入到父节点中，所以 <code>el.parentNode</code> 返回为 <code>null</code>。</td><td>调用在 <code>bind</code> 之后，此时元素已经插入到父节点中，所以 <code>el.parentNode</code> 可以正确返回父节点的引用。</td></tr><tr><td>是在 <code>DOM</code> 树绘制之前调用，因而获取不到有关元素渲染的信息。</td><td>函数是在 <code>DOM</code> 树绘制之后调用，因而可以获取到有关元素渲染的信息。</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js">Vue.directive(<span class="hljs-string">'dom'</span>,&#123;
  <span class="hljs-function"><span class="hljs-title">bind</span>(<span class="hljs-params">el</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(el.offsetWidth); <span class="hljs-comment">//0</span>
    <span class="hljs-built_in">console</span>.log(el.parentNode);  <span class="hljs-comment">//null</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(el.offsetWidth); <span class="hljs-comment">//1170</span>
    <span class="hljs-built_in">console</span>.log(el.parentNode);  <span class="hljs-comment">//<div msg="Welcome to Your Vue.js App"><button>click</button><div>false</div></div></span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>update</code> 与 <code>componentUpdated</code> 差异</strong></p>
<p>它们的区别更像是 <code>beforeUpdate</code> 与 <code>updated</code>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = !show"</span>></span>click<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-dom</span>></span>&#123;&#123; show &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，点击按钮切换响应式数据 <code>show</code> 的值为 <code>true</code>，观察自定义指令的输出：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.directive(<span class="hljs-string">"dom"</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"update"</span>, el.innerHTML); <span class="hljs-comment">//'update false'</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">componentUpdated</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentUpdated"</span>, el.innerHTML); <span class="hljs-comment">//'componentUpdated true'</span>
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>自定义指令钩子中没有 Vue 实例，<code>this</code> 默认指向 <code>undefined</code>。</p>
</blockquote>
<h2 data-id="heading-3">钩子函数参数</h2>
<p>完整的指令结构：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-directiveName:argument.modifier</span>=<span class="hljs-string">"show"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是否很抽象，那么代入实际例子去理解：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-on:mousemove.passive</span>=<span class="hljs-string">"doSomeThing"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 指令的钩子方法会接收以下四个参数：</p>
<ol>
<li><code>el</code> : 当前指令所绑定的元素。</li>
<li><code>binding</code> : 指令本身的信息，值为一个对象。
<ul>
<li><code>name</code> : 指令的名称。</li>
<li><code>rawName</code> : 完整原始名称，含 <code>v-*</code> 前缀。</li>
<li><code>value</code>: 指令的值。</li>
<li><code>expression</code> : 指令的表达式。</li>
<li><code>arg</code> : 传给指令的参数，支持动态参数。</li>
<li><code>modifiers</code> : 指令的修饰符。</li>
<li><code>oldValue</code> : 指令绑定的前一个值，仅在 update 和 componentUpdated 钩子中可用。无论值是否改变都可用。</li>
</ul>
</li>
<li><code>vnode</code> : Vue 编译生成的虚拟节点。</li>
<li><code>oldVnode</code> : 上一个虚拟节点，仅在 update 和 componentUpdated 钩子中可用。</li>
</ol>
<p><strong><code>value</code> 与 <code>expression</code> 的联系</strong></p>
<p>Vue 指令被调用时可以接收一个符合 JavaScript 规定的字符串形式的“表达式”的值（核心就是指令的值）。而 <code>value</code> 则是 <code>expression</code> 执行最终计算后的值。</p>
<pre><code class="hljs language-text copyable" lang="text">v-calc="1 + 1"
//expression "1+1"
//value 2;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常见的表达式，例如原始表达式、算术表达式、对象和数组的初始化表达式、调用表达式等。</p>





































<table><thead><tr><th align="left">expression</th><th align="left">value</th></tr></thead><tbody><tr><td align="left">"true"</td><td align="left">true</td></tr><tr><td align="left">"1"</td><td align="left">1</td></tr><tr><td align="left">"'hello'"</td><td align="left">"hello"</td></tr><tr><td align="left">"show"(响应式变量)</td><td align="left">false</td></tr><tr><td align="left">"&#123;x: 2.3, y: -1.2&#125;"</td><td align="left">&#123;x: 2.3, y: -1.2&#125;</td></tr><tr><td align="left">"1 + 2"</td><td align="left">3</td></tr><tr><td align="left">"(v)=>&#123;&#125;"</td><td align="left">ƒ (v)</td></tr></tbody></table>
<p><strong>动态指令参数</strong></p>
<p>指令的参数可以是动态的。例如，在 v-dom:[argument]="value" 中，argument 参数可以根据组件实例的响应式数据进行更新，这使得自定义指令可以在应用中被灵活使用。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.directive(<span class="hljs-string">"dom"</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">bind</span>(<span class="hljs-params">el, binding</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (binding.arg === <span class="hljs-string">"color"</span>) &#123;
      el.style.color = binding.value;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (binding.arg === <span class="hljs-string">"background"</span>) &#123;
      el.style.background = binding.value;
    &#125;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用指令的方式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-dom:background</span>=<span class="hljs-string">"'red'"</span>></span>&#123;&#123; show &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-dom:color</span>=<span class="hljs-string">"'green'"</span>></span>&#123;&#123; show &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">返回已注册的指令</h2>
<pre><code class="hljs language-js copyable" lang="js">Vue.directive(<span class="hljs-string">'directiveName'</span>); 
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            