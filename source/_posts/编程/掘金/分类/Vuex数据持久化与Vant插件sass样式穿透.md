
---
title: 'Vuex数据持久化与Vant插件sass样式穿透'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6184'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 03:16:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=6184'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、Vuex数据持久化</h2>
<p>Vuex 解决了多视图之间的数据共享问题。但是运用过程中又带来了一个新的问题是，Vuex 的状态存储并不能持久化。也就是说当你存储在 Vuex 中的 store 里的数据，只要一刷新页面，数据就丢失了。</p>
<p>引入<strong>vuex-persist</strong> 插件，它就是为 Vuex 持久化存储而生的一个插件。不需要你手动存取 storage ，而是直接将状态保存至 cookie 或者 localStorage 中。（真香）具体用法如下
<strong>安装指令：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install --save vuex-persist
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>引入:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> VuexPersistence <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex-persist'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>引入进vuex插件：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123; ... &#125;,
  <span class="hljs-attr">mutations</span>: &#123; ... &#125;,
  <span class="hljs-attr">actions</span>: &#123; ... &#125;,
  <span class="hljs-attr">plugins</span>: [vuexLocal.plugin]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>详细链接参考如下：</strong>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvuex-persistedstate" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vuex-persistedstate" ref="nofollow noopener noreferrer">www.npmjs.com/package/vue…</a></p>
<h2 data-id="heading-1">二、Vant插件sass样式穿透</h2>
<p><strong>Scoped CSS</strong>
当  标签有 scoped 属性时，它的 CSS 只作用于当前组件中的元素。这类似于 Shadow DOM 中的样式封装。它有一些注意事项，但不需要任何 polyfill。它通过使用 PostCSS 来实现以下转换：
</p><pre><code class="hljs language-javascript copyable" lang="javascript"><style scoped>
.example &#123;
  <span class="hljs-attr">color</span>: red;
&#125;
</style>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example"</span>></span>hi<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><style>
.example[data-v-f3f3eg9] &#123;
  <span class="hljs-attr">color</span>: red;
&#125;
</style>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"example"</span> <span class="hljs-attr">data-v-f3f3eg9</span>></span>hi<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>混用本地和全局样式</strong>
你可以在一个组件中同时使用有 scoped 和非 scoped 样式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><style>
<span class="hljs-comment">/* 全局样式 */</span>
</style>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-comment">/* 本地样式 */</span>
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>子组件的根元素</strong>
使用 scoped 后，父组件的样式将不会渗透到子组件中。不过一个子组件的根节点会同时受其父组件的 scoped CSS 和子组件的 scoped CSS 的影响。这样设计是为了让父组件可以从布局的角度出发，调整其子组件根元素的样式。</p>
<p><strong>#深度作用选择器</strong>
如果你希望 scoped 样式中的一个选择器能够作用得“更深”，例如影响子组件，你可以使用  操作符：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><style scoped>
.a >>> .b &#123; <span class="hljs-comment">/* ... */</span> &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>上述代码编译：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.a[data-v-f3f3eg9] .b &#123; <span class="hljs-comment">/* ... */</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>动态生成的内容</strong>
通过 v-html 创建的 DOM 内容不受 scoped 样式影响，但是你仍然可以通过深度作用选择器来为他们设置样式。</p></div>  
</div>
            