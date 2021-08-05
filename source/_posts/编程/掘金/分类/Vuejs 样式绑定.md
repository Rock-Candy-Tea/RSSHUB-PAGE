
---
title: 'Vue.js 样式绑定'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee2cadea4424917af8db5d3ddfabc3d~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:12:36 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee2cadea4424917af8db5d3ddfabc3d~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee2cadea4424917af8db5d3ddfabc3d~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="画板 61.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">Vue.js class</h2>
<p>class 与 style 是 HTML 元素的属性，用于设置元素的样式，我们可以用 v-bind 来设置样式属性。</p>
<p>Vue.js v-bind 在处理 class 和 style 时， 专门增强了它。表达式的结果类型除了字符串之外，还可以是对象或数组。</p>
<h3 data-id="heading-1">class 属性绑定</h3>
<p>我们可以为 v-bind:class 设置一个对象，从而动态的切换 class:</p>
<p><strong>实例 1</strong></p>
<p>实例中将 isActive 设置为 true 显示了一个绿色的 div 块，如果设置为 false 则不显示：</p>
<pre><code class="hljs language-js copyable" lang="js"><div v-bind:<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"&#123; 'active': isActive &#125;"</span>>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实例 div class 为：</p>
<pre><code class="hljs language-js copyable" lang="js">
<div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"active"</span>>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以在对象中传入更多属性用来动态切换多个 class 。</p>
<p><strong>实例 2</strong></p>
<p>text-danger 类背景颜色覆盖了 active 类的背景色：</p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"static"</span> v-bind:<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"&#123;
 'active' : isActive, 'text-danger' : hasError &#125;"</span>>
 </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实例 div class 为：</p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"static active text-danger"</span>>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以直接绑定数据里的一个对象：</p>
<p><strong>实例 3</strong></p>
<p>text-danger 类背景颜色覆盖了 active 类的背景色：</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"classObject"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例 3 与 实例 2 的渲染结果是一样的。</p>
<p>此外，我们也可以在这里绑定返回对象的计算属性。这是一个常用且强大的模式：</p>
<p><strong>实例 4</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123; <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>, <span class="hljs-attr">data</span>: &#123;
 <span class="hljs-attr">isActive</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">error</span>: &#123;
 <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'fatal'</span> &#125; &#125;,
 <span class="hljs-attr">computed</span>: &#123; <span class="hljs-attr">classObject</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">base</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">active</span>:
<span class="hljs-built_in">this</span>.isActive && !<span class="hljs-built_in">this</span>.error.value,
<span class="hljs-string">'text-danger'</span>: <span class="hljs-built_in">this</span>.error.value && <span class="hljs-built_in">this</span>.error.type === <span class="hljs-string">'fatal'</span>, &#125;
&#125; &#125;
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>更多学习内容来自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codeforest.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codeforest.cn/" ref="nofollow noopener noreferrer">代码森林</a></strong></p>
<h3 data-id="heading-2">数组语法</h3>
<p>我们可以把一个数组传给 v-bind:class ，实例如下：</p>
<p><strong>实例 5</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div v-bind:<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"[activeClass, errorClass]"</span>>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实例 div class 为：</p>
<pre><code class="hljs language-js copyable" lang="js"><div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"active text-danger"</span>>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以使用三元表达式来切换列表中的 class ：</p>
<p><strong>实例 6</strong></p>
<p>errorClass 是始终存在的，isActive 为 true 时添加 activeClass 类：</p>
<pre><code class="hljs language-js copyable" lang="js"><div v-bind:<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"[errorClass ,isActive ? activeClass : '']"</span>>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Vue.js style(内联样式)</h2>
<p>我们可以在 v-bind:style 直接设置样式：</p>
<p><strong>实例 7</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:style</span>=<span class="hljs-string">"&#123; color: activeColor, fontSize: fontSize + 'px' &#125;"</span>></span>
智一面教程<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实例 div style 为：</p>
<pre><code class="hljs language-js copyable" lang="js"><div style=<span class="hljs-string">"color: green; font-size: 30px;"</span>>
智一面教程
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以直接绑定到一个样式对象，让模板更清晰：</p>
<p><strong>实例 8</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:style</span>=<span class="hljs-string">"styleObject"</span>></span>
智一面教程
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>v-bind:style 可以使用数组将多个样式对象应用到一个元素上：</p>
<p><strong>实例 9</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind:style</span>=<span class="hljs-string">"[baseStyles, overridingStyles]"</span>></span>
智一面教程
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：当 v-bind:style 使用需要特定前缀的 CSS 属性时，如 transform ，Vue.js 会自动侦测并添加相应的前缀。</p></div>  
</div>
            