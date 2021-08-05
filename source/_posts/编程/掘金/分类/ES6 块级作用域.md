
---
title: 'ES6 块级作用域'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3979'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 17:29:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=3979'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">let 与 const</h2>
<blockquote>
<p>ES5 中声明变量命令只有两种 var 和 function</p>
<p>ES6 中除了 var、function，新增了 let、const、class、import，一共六种</p>
</blockquote>
<ol>
<li>
<p>let 是 ES6 新增的声明命令，功能类似于 ES5 中的 var 关键字</p>
</li>
<li>
<p>let 声明的变量尽在所在代码块内有效</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>
    <span class="hljs-keyword">var</span> b = <span class="hljs-number">1</span>
&#125;
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// ReferenceError</span>
<span class="hljs-comment">// 这表明 let 声明的变量只在它所在的代码块有效</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>let 命令很适合在 for 循环中使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
  a[i] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i);
  &#125;;
&#125;
a[<span class="hljs-number">6</span>](); <span class="hljs-comment">// 10</span>
<span class="hljs-comment">// var 声明的 i，全局有效，每一次循环，新的 i 值都会覆盖旧值，导致最后输出的是最后一轮的 i 的值</span>

<span class="hljs-keyword">var</span> b = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-number">10</span>; j++) &#123;
  b[j] = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(j);
  &#125;;
&#125;
b[<span class="hljs-number">6</span>](); <span class="hljs-comment">// 6</span>
<span class="hljs-comment">// 变量 j 使用 let 声明，当前的 j 只在本轮循环有效，每一次循环的 j 其实都是一个新的变量，所以最后输出的是 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>let 命令不允许重复声明</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// SyntaxError</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
&#125;
<span class="hljs-comment">// SyntaxErrot</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
&#125;
<span class="hljs-comment">// SyntaxError</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test3</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>暂行性死区</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ReferenceError</span>
<span class="hljs-built_in">console</span>.log(a)
<span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同一代码块中，使用 let 命令声明的变量，不能在声明之前使用，会报引用错误</p>
<p>代码块中，变量声明前，该变量不可用，语法上称之为暂行性死区（temporal dead zone，简称 TDZ）</p>
</li>
<li>
<p>const 和 let 作用和特性类似，只在当前代码块有效，不能重复声明</p>
<p>const 声明时必须赋初值，且不可改变其值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>
a = <span class="hljs-number">2</span> <span class="hljs-comment">// TypeError</span>
<span class="hljs-keyword">const</span> b <span class="hljs-comment">// SyntaxError</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>let、const 变量提升</p>
<p>下面代码 let 重复声明会报语法错误，但在报错之前 console.log 不能正常输出</p>
<p>说明存在变量提升</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(a)
<span class="hljs-keyword">let</span> a = <span class="hljs-number">2</span> <span class="hljs-comment">// SyntaxError</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是由于暂行性死区的存在，我们无法在声明之前使用变量</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// ReferenceError</span>

<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：变量的定义分为创建 -> 初始化为 undefined -> 赋值三个阶段</p>
<p>let 的创建过程被提升，但是初始化没有提升</p>
<p>var 的创建和初始化被提升</p>
<p>function 的创建、初始化和赋值都被提升</p>
</blockquote>
</li>
</ol>
<h2 data-id="heading-1">块级作用域</h2>
<ol>
<li>
<p>ES5 中只有全局作用域和函数作用域</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 全局作用域</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 函数作用域</span>
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>存在的问题</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a)
    <span class="hljs-keyword">if</span>(<span class="hljs-literal">false</span>) &#123;
        <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
    &#125;
&#125;
test() <span class="hljs-comment">// undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数作用域下中 if 中 var a 命令变量提升，导致 a 为 undefined</p>
</li>
<li>
<p>ES6 中规定 &#123;&#125; 内部为一个独立的块级作用域</p>
<p>外层代码块不受内层代码块的影响</p>
<p>外层作用域无法读取内层作用域的变量</p>
<p>内层作用域可以定义外层作用域的同名变量</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>
  &#123;
      <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
      &#123;
          <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 报错</span>
      &#125;
  &#125;
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>块级作用域的出现让广泛运用的的立即执行函数不再必要</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// IIFE 写法</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> tmp = ...;
  ...
&#125;());

<span class="hljs-comment">// 块级作用域写法</span>
&#123;
  <span class="hljs-keyword">let</span> tmp = ...;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-2">函数声明</h2>
<ol>
<li>
<p>ES5 规定函数只能在全局作用域和函数作用域中声明</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 情况一</span>
<span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
&#125;

<span class="hljs-comment">// 情况二</span>
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
&#125; <span class="hljs-keyword">catch</span>(e) &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上为非法的声明，但是为了兼容旧代码，浏览器没有遵守此规定，可以运行，不会报错，但是严格模式下会报错</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ES5 严格模式</span>
<span class="hljs-meta">'use strict'</span>;
<span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
&#125;
<span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>ES6 引入块级作用域，明确允许可以在块级作用域声明函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ES6 严格模式</span>
<span class="hljs-meta">'use strict'</span>;
<span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
&#125;
<span class="hljs-comment">// 不报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>ES6 规定块级作用域中的函数声明，无法在作用域外引用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'outside'</span>) 
&#125;
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">false</span>) &#123;
    <span class="hljs-comment">// 重复声明一次函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123; 
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'inside'</span>)
    &#125;
  &#125;
  fn()
&#125;())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ES5 中会打印出 inside，因为 if 块里面的 fn 被提升到自执行函数头部</p>
<p>在 ES6 中则打印出 outside，因为在 if 块内声明的 fn，作用域外无法访问，只能执行外部声明的 fn</p>
<blockquote>
<p>由于行为差异较大，ES6 规定浏览器可以不遵守该项，有自己的行为方式</p>
<ol>
<li>允许在块级作用域内声明函数</li>
<li>函数声明类似于 var，即提升到全局作用域或函数作用域的头部</li>
<li>同时，函数声明会提升到所在的块级作用域的头部</li>
</ol>
</blockquote>
<p>上面示例代码在 chrome 环境中可能会报错，因为实际运行的代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'outside'</span>) 
&#125;
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> fn = <span class="hljs-literal">undefined</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">false</span>) &#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123; 
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'inside'</span>)
    &#125;
  &#125;
  fn()
&#125;())
<span class="hljs-comment">// Uncaught TypeError: fn is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            