
---
title: '从原理角度分析var let const的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cdc27d86a86433d9446cf2e5cf19650~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 01:22:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cdc27d86a86433d9446cf2e5cf19650~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前言：本文主要从存储方式进行分析，如有错误感谢指教。</p>
<h3 data-id="heading-0">一、存储方式</h3>
<ol>
<li>
<p>var</p>
<p>1.1 变量的值是原始值</p>
<p>会在栈内存中预分配内存空间，当语句被执行时，会将变量存储到该内存空间。如下图所示：</p>
<p><a href="https://imgtu.com/i/2AvdJg" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cdc27d86a86433d9446cf2e5cf19650~tplv-k3u1fbpfcp-zoom-1.image" alt="2AvdJg.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>1.2 变量的值是引用值</p>
<p>会在堆内存里开辟一个内存空间存储实际值，在栈内存中会存储一个指向该堆内存的指针。如下图所示：</p>
<p><a href="https://imgtu.com/i/2AxDhD" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6953ef460f62449e98989835121c6864~tplv-k3u1fbpfcp-zoom-1.image" alt="2AxDhD.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</li>
<li>
<p>let</p>
<p>不会在栈内存里预分配内存空间。执行语句时，会在栈内存做一个检查，如果已经有相同变量名存在就会报错。</p>
</li>
<li>
<p>const</p>
<p>不会在栈内存里预分配内存空间。执行语句时，和let相同，会在栈内存检查是否存在相同变量名，存在则报错。</p>
<p>不过，const存储的变量是不可以修改的：</p>
<p>3.1 如果变量值是原始值，则无法修改该变量的值；</p>
<p>3.2 如果变量值是引用值，则无法修改栈内存里分配的指针，但是可以修改指针指向的对象里面的属性。</p>
</li>
</ol>
<p>可以看看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> num1 = <span class="hljs-number">10</span>;
<span class="hljs-keyword">var</span> num1 = <span class="hljs-number">20</span>;
<span class="hljs-built_in">console</span>.log(num1);<span class="hljs-comment">// 20</span>

<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">30</span>;
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">40</span>;<span class="hljs-comment">// Uncaught SyntaxError: Identifier 'num2' has already been declared</span>

<span class="hljs-keyword">const</span> num3 = <span class="hljs-number">50</span>;
num3 = <span class="hljs-number">60</span>;<span class="hljs-comment">// Uncaught TypeError: Assignment to constant variable</span>

<span class="hljs-keyword">const</span> obj1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
<span class="hljs-keyword">const</span> obj2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
obj1 = obj2<span class="hljs-comment">// Uncaught TypeError: Assignment to constant variable</span>

obj1.num4 = <span class="hljs-number">70</span>;
<span class="hljs-built_in">console</span>.log(obj1.num4)<span class="hljs-comment">// 70</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">二、区别</h3>
<ol>
<li>
<p>作用域</p>
<p>1.1 使用var进行声明的变量，变量会自动添加到最接近的上下文。</p>
<p>在函数中，最接近的上下文就是函数的局部上下文；在with语句中，最接近的上下文也是函数的局部上下文；如果变量未经声明就被初始化，则会被自动添加到全局上下文中。</p>
<p>如以下例子所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add1</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">var</span> sum = a + b;
  <span class="hljs-keyword">return</span> sum;
&#125;

<span class="hljs-keyword">let</span> result = add1(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>);
<span class="hljs-built_in">console</span>.log(result);<span class="hljs-comment">// 30</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add2</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-comment">// 在这里不对sum进行声明，直接初始化</span>
  sum = a + b
  <span class="hljs-keyword">return</span> sum;
&#125;
<span class="hljs-keyword">let</span> result = add2(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>);
<span class="hljs-built_in">console</span>.log(result);<span class="hljs-comment">// 30</span>
<span class="hljs-built_in">console</span>.log(sum);<span class="hljs-comment">// 30</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.2 let的作用域是块级的。块级的作用域由最近的一对包含花括号&#123;&#125;界定。</p>
<p>代码示例如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) &#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>
&#125;
<span class="hljs-built_in">console</span>.log(a)<span class="hljs-comment">// Uncaught ReferenceError: a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>变量声明</p>
<p>2.1 var声明会拿到函数或全局作用域的顶部，位于所有代码之前。声明的提升意味着会输出undefined而不是Reference Error，以下代码可以验证变量会被提升：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//undefined</span>
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'aki'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.2 严格来讲，使用let声明变量时也会发生变量提升的现象，但由于存在“暂时性死区”，不能在声明之前以任何方式引用未声明的let变量。因此，从写JavaScript的角度说，let的提升和var的提升是不一样的。</p>
<p>2.3 与var不同，使用let在全局作用域声明的变量不会被成为window对象的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name = <span class="hljs-string">'aki'</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.name);  <span class="hljs-comment">// 'aki'</span>

<span class="hljs-keyword">let</span> age = <span class="hljs-number">20</span>;
<span class="hljs-built_in">console</span>.lof(<span class="hljs-built_in">window</span>.age);  <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>const常量声明</p>
<p>使用const声明的变量必须同时进行初始化；const赋值的引用值变量不能再被重新赋值为其他引用值，但对象的键不受限制。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> num1;<span class="hljs-comment">// SyntaxError</span>
num1 = <span class="hljs-number">10</span>;

<span class="hljs-keyword">const</span> num2 = <span class="hljs-number">20</span>;
num2 = <span class="hljs-number">200</span>;<span class="hljs-comment">// TypeError</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            