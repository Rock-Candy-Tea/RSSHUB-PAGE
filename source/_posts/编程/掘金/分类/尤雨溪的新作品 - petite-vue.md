
---
title: '尤雨溪的新作品 - petite-vue'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8971'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 00:49:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=8971'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>petite-vue</code> 是针对渐进增强进行优化的 Vue 的替代发行版。它提供了与标准 Vue 相同的模板语法和反应性思维模型。但是，它专门针对在服务器框架呈现的现有 HTML 页面上“喷洒”少量交互进行了优化。</p>
<ul>
<li>仅 ~5.8kb</li>
<li>Vue 兼容的模板语法</li>
<li>基于 DOM，就地变异</li>
<li>通过驱动 @vue/reactivity</li>
</ul>
<h1 data-id="heading-0">地位</h1>
<ul>
<li>这是很新的。可能存在错误，并且可能仍然存在 API 更改，因此<strong>使用风险自负</strong>。不过能用吗？非常。查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fpetite-vue%2Ftree%2Fmain%2Fexamples" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/petite-vue/tree/main/examples" ref="nofollow noopener noreferrer">示例</a>以了解它的功能。</li>
<li>问题列表被故意禁用，因为我现在有更高优先级的事情要关注并且不想分心。如果您发现了错误，则必须解决它或提交 PR 以自行修复。也就是说，请随时使用讨论选项卡来互相帮助。</li>
<li>目前不太可能接受功能请求 - 该项目的范围有意保持在最低限度。</li>
</ul>
<h1 data-id="heading-1">用法</h1>
<p><code>petite-vue</code> 无需构建步骤即可使用。只需从 CDN 加载它：</p>
<pre><code class="hljs language-html copyable" lang="html">< script  src =" https://unpkg.com/petite-vue "延迟 初始化> </ script >

<span class="hljs-comment"><!-- 页面任意位置 --></span> 
< div  v-scope =" &#123; count: 0 &#125; " >
  &#123;&#123; 数数 &#125;&#125;
  < button  @click =" count++ " > inc </ button > 
</ div >
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用<code>v-scope</code>到标志区应当由被控制在页面上<code>petite-vue</code>。</li>
<li>该<code>defer</code>属性使脚本在解析 HTML 内容后执行。</li>
<li>该<code>init</code>属性告诉<code>petite-vue</code>自动查询和初始化<code>v-scope</code>页面上的所有元素。</li>
</ul>
<h1 data-id="heading-2">手动初始化</h1>
<p>如果您不想要自动初始化，请删除该init属性并将脚本移动到 end of <code><body></code>：</p>
<pre><code class="hljs language-html copyable" lang="html">< script  src =" https://unpkg.com/petite-vue " > </ script > 
< script > 
  PetiteVue 。创建应用程序（）。挂载( ) 
</脚本>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，使用 ES 模块构建：</p>
<pre><code class="hljs language-html copyable" lang="html">< script  type =" module " > 
  import  &#123;  createApp  &#125;  from  'https://unpkg.com/petite-vue?module' 
  createApp ( ) 。挂载( ) 
</脚本>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">生产 CDN URL</h1>
<p>简短的 CDN URL 用于原型设计。对于生产用途，请使用完全解析的 CDN URL 以避免解析和重定向成本：</p>
<ul>
<li>全局构建：<code>https://unpkg.com/petite-vue@0.2.2/dist/petite-vue.iife.js</code></li>
<li>公开PetiteVue全局，支持自动初始化</li>
<li>ESM 构建：<code>https://unpkg.com/petite-vue@0.2.2/dist/petite-vue.es.js</code></li>
<li>必须与 <code><script type="module"></code></li>
</ul>
<h1 data-id="heading-4">根范围</h1>
<p>该<code>createApp</code>函数接受一个数据对象，作为所有表达式的根作用域。这可用于引导简单的一次性应用程序：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>

  createApp(&#123;
    <span class="hljs-comment">// exposed to all expressions</span>
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    <span class="hljs-comment">// getters</span>
    <span class="hljs-keyword">get</span> <span class="hljs-title">plusOne</span>() &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.count + <span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-comment">// methods</span>
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.count++
    &#125;
  &#125;).mount()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!-- v-scope value can be omitted --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Note <code>v-scope</code>不需要在此处具有值，仅用作<code>petite-vue</code>处理元素的提示。</p>
<p>原文自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fpetite-vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/petite-vue" ref="nofollow noopener noreferrer">petite-vue</a> 具体各位去尤大仓库看</p></div>  
</div>
            