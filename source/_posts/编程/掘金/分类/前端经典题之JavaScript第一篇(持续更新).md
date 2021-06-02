
---
title: '前端经典题之JavaScript第一篇(持续更新)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9135'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 04:09:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=9135'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、JavaScript第一篇</h2>
<blockquote>
<p>JavaScript在1995年由<a href="https://baike.baidu.com/item/Netscape/2778944" target="_blank" rel="nofollow noopener noreferrer">Netscape</a>公司的Brendan Eich，在网景导航者浏览器上首次设计实现而成。</p>
</blockquote>
<h3 data-id="heading-1">1.1什么是JavaScript</h3>
<p>JavaScript是客户端和服务端脚本语言，可以插入到HTML中，同时JavaScript也是面向对象的编程语言。</p>
<h3 data-id="heading-2">1.2 JavaScript和ASP脚本相比，哪个更快</h3>
<p>JavaScript更快。JavaScript是一种客户端语言，因为他不需要web服务器的协助来执行。</p>
<p>另一方面，ASP是服务端语言，因此总是比JavaScript更慢。</p>
<p>JavaScript现在可用于服务端语言(node.js)</p>
<h3 data-id="heading-3">1.3 什么是负无穷大</h3>
<p>负无穷大是JavaScript中的一个数字，可以通过负数除以零来得到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> res = -<span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(-<span class="hljs-number">1</span> / <span class="hljs-number">0</span>) <span class="hljs-comment">//Infinity</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.4 什么是未声明和未定义的变量</h3>
<p>**未声明的变量是程序中不存在且未声明的变量。**如果程序尝试读取未声明变量的值，则会遇到运行时错误。</p>
<p>**未定义的变量是在程序中声明但尚未给出任何值的变量。**如果程序尝试读取未定义变量的值，则返回未定义的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(res)  <span class="hljs-comment">// res is not defined</span>

<span class="hljs-keyword">let</span> res
<span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5 如何动态添加元素</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'li'</span>)
li.innerHTML = <span class="hljs-string">'我是新添加的标签'</span>
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>).appendChild(li)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> li = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'li'</span>)
li.innerHTML = <span class="hljs-string">'我是新插入的节点'</span>
<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>).insertAdjacentElement(<span class="hljs-string">'beforeBegin'</span>, li)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.6 什么是全局变量 如何声明 有哪些问题</h3>
<p>全局变量是整个代码长度可用的变量，也就是说这些变量没有任何作用域。<strong>var关键字用于声明局部变量或对象。如果省略var关键字，则声明一个全局变量。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 方法一</span>
 test = <span class="hljs-number">5</span>
 <span class="hljs-built_in">console</span>.log(test)
 <span class="hljs-built_in">window</span>.test2 = <span class="hljs-number">10</span>
 <span class="hljs-comment">// 方法二</span>
 <span class="hljs-built_in">console</span>.log(test2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用全局变量所面临的问题是本地和全局变量名称的冲突。此外，很难调试和测试依赖于全局变量的代码。</p>
<h3 data-id="heading-7">1.7 什么是=== 运算符</h3>
<p><strong>===被称为严格等式运算符，当两个操作数具有相同的值而没有任何类型转换时，该运算符返回true。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = <span class="hljs-string">'5'</span>
<span class="hljs-keyword">let</span> int = <span class="hljs-number">5</span>
<span class="hljs-built_in">console</span>.log(arr == int)  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(arr === int)  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1.8 如何使用JavaScript提交表单</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"http://www.baidu.com"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>JS提交表单<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><script>
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btn'</span>).addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'form'</span>).submit()
    &#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">1.9 JavaScript如何改变元素的样式/类</h3>
<p>行内样式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box p'</span>).style.color = <span class="hljs-string">'red'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置类</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box p'</span>).className = <span class="hljs-string">'p1'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">1.10 JavaScript循环结构都有什么</h3>
<p>for循环</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-built_in">console</span>.log(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>while循环</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">while</span> (i < <span class="hljs-number">5</span>) &#123;
  <span class="hljs-keyword">if</span> (i == <span class="hljs-number">2</span>) &#123;
    <span class="hljs-keyword">break</span>
  &#125;
  i++
&#125;
<span class="hljs-built_in">console</span>.log(i)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>do...while</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
  <span class="hljs-keyword">do</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'当前i的值为:'</span> + i)
    i++
  &#125; <span class="hljs-keyword">while</span> (i <= <span class="hljs-number">5</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">1.11 3 +2 + '7' 的结果是很么</h3>
<pre><code class="copyable">console.log(3 + 2 + '7')  // 7
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于3和2是整数，它们将直接相加。由于7是一个字符串，它将会被直接连接，所以结果将是57。</p>
<h3 data-id="heading-12">1.12 JavaScript中有哪些类型的弹出框</h3>
<pre><code class="hljs language-js copyable" lang="js">alert(<span class="hljs-string">'1'</span>)
confirm(<span class="hljs-string">'1'</span>)
prompt(<span class="hljs-string">'1'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">1.13  如何强制页面加载JavaScript中的页面</h3>
<pre><code class="hljs language-js copyable" lang="js">  <script language=<span class="hljs-string">"JavaScript"</span> type=<span class="hljs-string">"text/javascript"</span>>
    location.href = <span class="hljs-string">"http://baidu.com"</span>
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">1.14 escape字符是用来做什么的</h3>
<p>使用特殊字符（如单引号，双引号，撇号和＆符号）时，将使用转义字符（反斜杠）。在字符前放置反斜杠，使其显示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.write(<span class="hljs-string">"I \'m\ a \*boy\*"</span>)  <span class="hljs-comment">// I 'm a *boy*</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">1.15 什么是JavaScript Cookie</h3>
<p>Cookie是用来存储计算机中的小型测试文件，当用户访问网站以存储他们需要的信息时，它将被创建。</p>
<p>创建cookie</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.cookie = <span class="hljs-string">'username'</span> + <span class="hljs-string">'='</span> + <span class="hljs-string">'web_chicken'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">1.16 解释JavaScript中的pop()方法</h3>
<p>pop()方法与shift()方法类似，但不同之处在于shift()方法在数组开头工作</p>
<p>pop()的方法将最后一个元素从给定的数组中删除</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-string">'javascript'</span>, <span class="hljs-string">'Vue'</span>, <span class="hljs-string">'React'</span>, <span class="hljs-string">'Element ui'</span>]
<span class="hljs-keyword">let</span> res = arr.pop()
<span class="hljs-built_in">console</span>.log(res)    <span class="hljs-comment">// Element ui</span>
<span class="hljs-built_in">console</span>.log(arr)    <span class="hljs-comment">// ["javascript", "Vue", "React"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">1.17 在JavaScript中使用innerHTML的缺点是什么</h3>
<ul>
<li>内容随处可见</li>
<li>不能像“追加到innerHTML”一样使用</li>
<li>即使你使用+ = like“innerHTML = innerHTML +'html'”旧的内容仍然会被html替换</li>
<li>整个innerHTML内容被重新解析并构建成元素，因此它的速度要慢得多</li>
<li>innerHTML不提供验证，因此可能会在文档中插入有效的和破坏性的HTML并将其中断</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'p'</span>).innerHTML += <span class="hljs-string">'新添加的'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">1.18 break和continue语句的作用</h3>
<ul>
<li>break语句从当前循环中退出</li>
<li>continue语句结束本次循环继续下一个循环语句</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
      <span class="hljs-keyword">if</span> (i === <span class="hljs-number">2</span>) <span class="hljs-keyword">break</span>
        <span class="hljs-built_in">console</span>.log(i)  <span class="hljs-comment">//  0 1</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
      <span class="hljs-keyword">if</span> (i === <span class="hljs-number">2</span>) <span class="hljs-keyword">continue</span>
      <span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 0 1 3 4</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">1.19 在JavaScript中，data types的两个基本组是什么</h3>
<ul>
<li>Primitive 原始类型</li>
<li>Reference types 引用类型</li>
</ul>
<blockquote>
<p>原始类型是保存在栈内存中的简单的数据。基本类型的数据操作的是实际保存的值。</p>
</blockquote>
<p>原始类型是数字和布尔数据类型。引用类型是更复杂的类型，如字符串和日期。</p>
<h3 data-id="heading-20">1.20 如何创建通用对象</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> I = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            