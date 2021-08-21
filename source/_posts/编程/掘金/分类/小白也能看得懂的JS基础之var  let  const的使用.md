
---
title: '小白也能看得懂的JS基础之var  let  const的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/368f3326d62444ad971166b3d47ff315~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 23:45:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/368f3326d62444ad971166b3d47ff315~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">var</h3>
<blockquote>
<p>在js中，万物皆可var</p>
</blockquote>
<p>当你需要声明一个数字，字符串，布尔值甚至是数组或者对象的时候你都可以</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用var声明数字，字符串，布尔值，数组，对象</span>
<span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;

<span class="hljs-keyword">var</span> str = <span class="hljs-string">'Hello World'</span>;

<span class="hljs-keyword">var</span> bool = <span class="hljs-literal">true</span>;

<span class="hljs-keyword">var</span> arr = [];

<span class="hljs-keyword">var</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'hulh'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">23</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">'male'</span> &#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本上，你可以用var声明所有的数据类型</p>
<p>使用var声明变量的时候，你可以不用初始化值，只是声明。此时所声明变量的值为undefined。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name;
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，我们还是建议：尽量在声明变量的时候给它指定一个初始值，以免发生不可预知的错误。</p>
<p>使用var声明变量，你还可以重复声明同一变量，因为Javascript是逐行编译，因此后面声明的同名变量会覆盖前者。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'hlh'</span>;
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// hulh</span>

<span class="hljs-keyword">var</span> name = <span class="hljs-string">'HLH'</span>;
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// HLH (不会报错)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，用var声明变量，会发生“变量提升”的现象，何为变量提升呢？通俗点说就是，你可以在定义这个值之前去使用它。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// 不会报错，而是会输出undefined(当然，仅限非严格模式下)</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'hulh'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为何会发生这个现象呢？是因为Javascript编译器在编译时会将所有的声明提升到作用域的顶部，所以上述代码看起来就像是下面这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name;
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// 不会报错，而是会输出undefined(当然，仅限非严格模式下)</span>
name = <span class="hljs-string">'hulh'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Javascript中有全局变量和局部变量，用var声明的变量，在浏览器环境中默认会挂载到window对象下，成为window对象的一个属性。
而当不使用var声明变量的时候，在浏览器环境中也会自动挂载到window对象下(相当于声明了一个全局变量，容易污染全局变量)。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/368f3326d62444ad971166b3d47ff315~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-1">let</h3>
<p>let的作用与var差不多，但有一些区别：</p>
<p><strong>let</strong> 声明的范围是块级作用域(ES6中新增了块级作用域)，块级作用域由最近的一对大括号界定&#123;&#125;，而 <strong>var</strong> 的声明范围是函数作用域
因此而发生的改变有：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// var</span>
<span class="hljs-keyword">if</span> (<span class="hljs-number">1</span>) &#123;
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'hlh'</span>;
&#125;
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// hlh</span>

<span class="hljs-comment">// let</span>
<span class="hljs-keyword">if</span> (<span class="hljs-number">1</span>) &#123;
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'hlh'</span>;
&#125;
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// 报错 name is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>let</strong> 声明的变量会形成暂时性死区，在这个块作用域内用 <strong>let</strong> 声明的变量，都不可以再重复声明，也不能在声明之前使用。
严格来讲，其实使用 <strong>let</strong> 声明的变量也会存在“变量提升”现象，但是因为暂时性死区的缘故，“变量提升”现象能够比较好的避免。
从某种角度来说，<strong>var</strong> 和 <strong>let</strong> 的“变量提升”是不一样的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 不能在声明之前使用</span>
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'hlh'</span>;
<span class="hljs-comment">// 不能重复声明</span>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">'HLH'</span>; <span class="hljs-comment">// Uncaught SyntaxError: Identifier 'name' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器环境下，使用let声明的变量不会挂载到window上成为window的属性，避免了全局变量的污染。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db9b4b8f7cb748c2a648709eeb621ea6~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-2">const</h3>
<p><strong>var</strong>和<strong>let</strong>用于定义变量，即可变的量
而 <strong>const</strong> 用于定义常量，即不可变的量
用 <strong>const</strong> 定义的常量是只读的，无法修改</p>
<p>一个很经典的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*
 * 我们都知道圆的面积计算公式是 S = π * r * r
 * π 是一个永恒不变的值，假如我们用 var 或者 let 
 * 去声明的话，这个值就可能会意外的被改变
 * 此时我们用 const 去声明，就可以避免值被改变
*/</span>
<span class="hljs-keyword">let</span> PI = <span class="hljs-number">3.1415926</span>;
PI = <span class="hljs-number">3.1233333</span>; <span class="hljs-comment">// 不可</span>

<span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.1415926</span>;
PI = <span class="hljs-number">3.1233333</span>; <span class="hljs-comment">// Uncaught TypeError: Assignment to constant variable.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <strong>const</strong> 声明常量，一旦声明就必须赋值，否则会报错</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> PI; <span class="hljs-comment">// Uncaught SyntaxError: Missing initializer in const declaration</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>const</strong> 声明的常量与  <strong>let</strong>  声明的变量一样，同样存在暂时性死区，声明的范围也是块级作用域，同样不可重复声明</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 暂时性死区</span>
<span class="hljs-built_in">console</span>.log(PI); <span class="hljs-comment">// ReferenceError: Cannot access 'PI' before initialization</span>
<span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.1415926</span>;

<span class="hljs-comment">// 块级作用域范围</span>
<span class="hljs-keyword">if</span> (<span class="hljs-number">1</span>) &#123;
<span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.1415926</span>;
<span class="hljs-built_in">console</span>.log(PI); <span class="hljs-comment">// 3.1415926</span>
&#125;
<span class="hljs-built_in">console</span>.log(PI); <span class="hljs-comment">// ReferenceError: PI is not defined</span>

<span class="hljs-comment">// 不可重复声明　</span>
<span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.1415926</span>;
<span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.14</span>; <span class="hljs-comment">// SyntaxError: Identifier 'PI' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也许有些人会问，当我用 <strong>const</strong> 声明对象的时候，为什么对象的属性可以被改变？</p>
<p>大家都知道，声明对象时，javascript编译器会在堆内存中开辟出一块地址用以存放该对象，而 <strong>const</strong> 定义的常量存放的只是该对象的地址指针而已，只要地址指针没有改变，就没有违背不可改变的原则
我们修改对象的属性时，操作的是堆内存中的对象，并非 <strong>const</strong> 定义的这个常量本身，假如我们修改了这个常量的值，才会报错</p>
<p>更详细的解释可以参见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Flet" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/let" ref="nofollow noopener noreferrer">ECMAScript6入门(阮一峰) let和const命令 const 本质</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'hlh'</span>,
<span class="hljs-attr">age</span>: <span class="hljs-number">23</span>,
&#125;;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before'</span>, obj);
obj.name = <span class="hljs-string">'HLH'</span>; <span class="hljs-comment">// 不会报错</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'after'</span>, obj);

<span class="hljs-comment">/**
 * if we change the constant obj,
 * we actually modify the address of the obj.
 */</span>
obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'HuLiehao'</span>,
<span class="hljs-attr">age</span>: <span class="hljs-number">23</span>,
<span class="hljs-attr">gender</span>: <span class="hljs-string">'male'</span>,
&#125;; <span class="hljs-comment">// Uncaught TypeError: Assignment to constant variable.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-3">综上所述</h4>
<p>我们在声明变量时应该优先使用 <strong>let</strong> ，定义常量则使用 <strong>const</strong></p>
<h4 data-id="heading-4">以上</h4>
<p>仅为本人拙见，如有错误或遗漏，请不吝赐教</p></div>  
</div>
            