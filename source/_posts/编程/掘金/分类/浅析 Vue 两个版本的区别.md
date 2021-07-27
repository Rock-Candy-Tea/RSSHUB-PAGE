
---
title: '浅析 Vue 两个版本的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c954c5ce6784a889e1767d5cb7c35cf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 20:39:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c954c5ce6784a889e1767d5cb7c35cf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文件名不同（分别通过 <code>bootcdn</code> 引入如下）：</h3>
<ul>
<li>完整版：<code>vue.js</code></li>
</ul>
<pre><code class="copyable">链接：https://cdn.bootcdn.net/ajax/libs/vue/2.6.12/vue.js
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>非完整版（只包含运行时版）: <code>vue.runtime.js</code></li>
</ul>
<pre><code class="copyable">链接：https://cdn.bootcdn.net/ajax/libs/vue/2.6.12/vue.runtime.js
<span class="copy-code-btn">复制代码</span></code></pre>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c954c5ce6784a889e1767d5cb7c35cf~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-1">完整版体积更大</h3>
<p>完整版比非完整版多一个 <code>compiler</code> （编译器，用来将模板字符串编译成为 <code>JavaScript</code> 渲染函数的代码），代码体积会比非完整版的大 <strong>40%</strong> 左右</p>
<h3 data-id="heading-2">用法</h3>
<ul>
<li>使用完整版，引入 <code>vue.js</code> 时，视图写在 <code>HTML</code> 里或 <code>template</code> 中</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div @click="add">&#123;&#123;n&#125;&#125; <button>+1</button></div>
  `</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.n += <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用非完整版，引入 <code>vue.runtime.js</code> 时，视图写在 <code>render</code> 中</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span>&#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">"div"</span>, [<span class="hljs-built_in">this</span>.n, h(<span class="hljs-string">"button"</span>, &#123;<span class="hljs-attr">on</span>:&#123;<span class="hljs-attr">click</span>: <span class="hljs-built_in">this</span>.add&#125;&#125;, <span class="hljs-string">"+1"</span>)])
  &#125;,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.n += <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">注意：</h4>
<p>以上两个版本，在生产环境下，应使用后缀为 <code>.min.js</code> 的文件</p>
<pre><code class="copyable">.min.js是压缩出去空格、回车的文件，主要用于开发用
.js是未经压缩的源码，自带的格式更方便用户查看源码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">补充：除 <code>bootcdn</code> 以外的其它引入方法</h3>
<ul>
<li><code>webpack</code> 引入：</li>
</ul>
<p>默认使用非完整版，使用完整版需要配置 <code>alias</code></p>
<ul>
<li><code>@vue/cli</code> 引入：</li>
</ul>
<p>默认使用非完整版，使用完整版也需要额外配置</p>
<h3 data-id="heading-5">总结：</h3>
<p>平时最好默认使用代码体积小的非完整版，编译的工作交给 <code>vue-loader</code> 去做</p>
<p>这样选择的优点如下：</p>
<ol>
<li>保证用户体验，用户下载的 <code>JS</code> 文件体积更小，但只支持 <code>h</code> 函数。</li>
<li>保证开发体验，开发者可直接在 <code>vue</code> 文件里写 <code>HTML</code> 标签，而不写 <code>h</code> 函数。</li>
<li>简化操作流程， <code>vue-loader</code> 会把 <code>vue</code> 文件里的 <code>HTML</code> 转为 <code>h</code> 函数,这样我们就不需要写太多麻烦的 <code>h</code> 函数就可做到和完整版一样的事</li>
</ol>
<pre><code class="copyable">h 函数是 vue 中的 createElement 方法
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            