
---
title: '初探webpack的导入导出'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7110'
author: 掘金
comments: false
date: Mon, 03 May 2021 06:39:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=7110'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>之前在快手面试时，面试官问到了esmodule和commonjs两种方式下webpack的导入导出解析策略，然后不出意外地，我被问懵了。于是做了一些简单的小实验，之后可能会深入源码层面对这些现象做一个解析。</p>
<h2 data-id="heading-1">1.ES6导入导出方式</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// module.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span> <span class="hljs-comment">//具名导出</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> b <span class="hljs-comment">// 默认导出</span>
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> b, &#123; a &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./module'</span>
<span class="hljs-built_in">console</span>.log(a + b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将模块整个导出来看看</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./module'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>);
<span class="hljs-comment">/* &#123;a: 1
default: 2
Symbol(Symbol.toStringTag): "Module"
__esModule: true
&#125;*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，这种命名空间的导入方式会将整个模块导入进来，如果模块内有<strong>默认导出</strong>则会以default的方式出现，而为了防止命名冲突，<strong>default被设成了关键字</strong>。</p>
<p>顺便说一下<code>Symbol(Symbol.toStringTag)</code>这个属性</p>
<blockquote>
<p>这是一个内置 symbol，它通常作为对象的属性键使用，对应的属性值应该为字符串类型，这个字符串用来表示该对象的自定义类型标签，通常只有内置的 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/toString" target="_blank" rel="nofollow noopener noreferrer"><code>Object.prototype.toString()</code></a> 方法会去读取这个标签并把它包含在自己的返回值里</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ValidatorClass</span> </span>&#123;
  [<span class="hljs-built_in">Symbol</span>.toStringTag] = <span class="hljs-string">'Validator'</span>
  get [<span class="hljs-built_in">Symbol</span>.toStringTag]() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Validator"</span>;
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> ValidatorClass())); <span class="hljs-comment">// [object Validator]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当面试官问到获取对象类型的题目时又有新的东西能吹了（误）。</p>
<h2 data-id="heading-2">2.CommonJS</h2>
<p>使用commonjs的require返回的是一个js对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// module.js</span>
<span class="hljs-built_in">exports</span>.someValue = <span class="hljs-number">42</span>;
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./module'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>);
<span class="hljs-comment">/*&#123;someValue: 42&#125;*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-3"><code>exports</code> (CommonJS)</h3>
<p>该变量默认值为 <code>module.exports</code>（即一个对象）。 如果 <code>module.exports</code> 被重写的话， <code>exports</code> 不再会被导出。</p>
</blockquote>
<h2 data-id="heading-4">3.混合使用es语法和commonjs语法</h2>
<h3 data-id="heading-5">es引入common导出</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// module.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">someValue</span>: <span class="hljs-number">42</span>
&#125;;
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./module'</span>
<span class="hljs-comment">// 或者 import module from './module' 结果是一样的</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>);
<span class="hljs-comment">/*&#123;someValue: 42&#125;*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，如果导出是<code>module.export</code>的话，不论怎么导入，都是一个普通js对象。</p>
<p>如果采用下面这种方式的具名导入，则会额外<strong>将default值也初始化为本对象</strong>。也就是说，采用exports的方式导出时，在具名导入解析时，<strong>会为其适配两种es导入方式</strong>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// module.js</span>
<span class="hljs-built_in">exports</span>.someValue = <span class="hljs-number">42</span>;
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./module'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>);
<span class="hljs-comment">/* &#123;default: &#123;someValue: 42&#125;
someValue: (...)
Symbol(Symbol.toStringTag): "Module"
__esModule: true
&#125;*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">common引入es导出</h3>
<p>在这种情景下，<code>const ...= require(...)</code>可以等同于<code>import * as ... from '...'</code>，也就是会被当成具名引入解析。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// module.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> someValue = <span class="hljs-number">42</span>;
<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./module'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>);
<span class="hljs-comment">/* &#123;someValue: 42
Symbol(Symbol.toStringTag): "Module"
__esModule: true
&#125;*/</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            