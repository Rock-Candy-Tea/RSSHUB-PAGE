
---
title: 'C语言 函数声明和定义 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1370'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 17:42:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=1370'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/7001661431321985061#%E4%B8%80%E7%AE%80%E4%BB%8B" title="#%E4%B8%80%E7%AE%80%E4%BB%8B" target="_blank">一.简介</a></li>
<li><a href="https://juejin.cn/post/7001661431321985061#%E4%BA%8C%E5%87%BD%E6%95%B0%E8%BF%94%E5%9B%9E%E5%80%BC" title="#%E4%BA%8C%E5%87%BD%E6%95%B0%E8%BF%94%E5%9B%9E%E5%80%BC" target="_blank">二.函数返回值</a>
<ul>
<li><a href="https://juejin.cn/post/7001661431321985061#1%E5%87%BD%E6%95%B0%E6%B2%A1%E6%9C%89%E8%BF%94%E5%9B%9E%E5%80%BC" title="#1%E5%87%BD%E6%95%B0%E6%B2%A1%E6%9C%89%E8%BF%94%E5%9B%9E%E5%80%BC" target="_blank">1.函数没有返回值</a></li>
<li><a href="https://juejin.cn/post/7001661431321985061#2%E5%87%BD%E6%95%B0%E6%9C%89%E8%BF%94%E5%9B%9E%E5%80%BC" title="#2%E5%87%BD%E6%95%B0%E6%9C%89%E8%BF%94%E5%9B%9E%E5%80%BC" target="_blank">2.函数有返回值</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/7001661431321985061#%E4%B8%89%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0" title="#%E4%B8%89%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0" target="_blank">三.函数参数</a>
<ul>
<li><a href="https://juejin.cn/post/7001661431321985061#1%E5%87%BD%E6%95%B0%E6%B2%A1%E6%9C%89%E5%8F%82%E6%95%B0" title="#1%E5%87%BD%E6%95%B0%E6%B2%A1%E6%9C%89%E5%8F%82%E6%95%B0" target="_blank">1.函数没有参数</a></li>
<li><a href="https://juejin.cn/post/7001661431321985061#2%E5%87%BD%E6%95%B0%E6%9C%89%E5%9B%BA%E5%AE%9A%E5%8F%82%E6%95%B0" title="#2%E5%87%BD%E6%95%B0%E6%9C%89%E5%9B%BA%E5%AE%9A%E5%8F%82%E6%95%B0" target="_blank">2.函数有固定参数</a></li>
<li><a href="https://juejin.cn/post/7001661431321985061#3%E5%87%BD%E6%95%B0%E6%9C%89%E4%B8%8D%E5%AE%9A%E9%95%BF%E5%BA%A6%E5%8F%82%E6%95%B0" title="#3%E5%87%BD%E6%95%B0%E6%9C%89%E4%B8%8D%E5%AE%9A%E9%95%BF%E5%BA%A6%E5%8F%82%E6%95%B0" target="_blank">3.函数有不定长度参数</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/7001661431321985061#%E5%9B%9B%E5%87%BD%E6%95%B0%E5%A3%B0%E6%98%8E%E5%92%8C%E5%AE%9A%E4%B9%89" title="#%E5%9B%9B%E5%87%BD%E6%95%B0%E5%A3%B0%E6%98%8E%E5%92%8C%E5%AE%9A%E4%B9%89" target="_blank">四.函数声明和定义</a>
<ul>
<li><a href="https://juejin.cn/post/7001661431321985061#1%E5%87%BD%E6%95%B0%E5%A3%B0%E6%98%8E%EF%BC%9A%E4%B8%8D%E9%9C%80%E8%A6%81%E5%AE%9E%E7%8E%B0%E8%BF%99%E4%B8%AA%E5%87%BD%E6%95%B0%E7%9A%84%E5%8A%9F%E8%83%BD" title="#1%E5%87%BD%E6%95%B0%E5%A3%B0%E6%98%8E%EF%BC%9A%E4%B8%8D%E9%9C%80%E8%A6%81%E5%AE%9E%E7%8E%B0%E8%BF%99%E4%B8%AA%E5%87%BD%E6%95%B0%E7%9A%84%E5%8A%9F%E8%83%BD" target="_blank">1.函数声明：不需要实现这个函数的功能</a></li>
<li><a href="https://juejin.cn/post/7001661431321985061#2%E5%87%BD%E6%95%B0%E5%AE%9A%E4%B9%89%EF%BC%9A%E5%BF%85%E9%A1%BB%E5%AE%9E%E7%8E%B0%E8%BF%99%E4%B8%AA%E5%87%BD%E6%95%B0%E7%9A%84%E5%8A%9F%E8%83%BD" title="#2%E5%87%BD%E6%95%B0%E5%AE%9A%E4%B9%89%EF%BC%9A%E5%BF%85%E9%A1%BB%E5%AE%9E%E7%8E%B0%E8%BF%99%E4%B8%AA%E5%87%BD%E6%95%B0%E7%9A%84%E5%8A%9F%E8%83%BD" target="_blank">2.函数定义：必须实现这个函数的功能</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/7001661431321985061#%E4%BA%94%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E4%BA%94%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">五.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.简介</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer"><code>C</code> 语言</a>中的函数是一段可以重复使用的代码，用来独立地完成某个功能，它可以接收用户传递的参数，也可以不接收；将代码段封装成函数的过程叫做函数定义。</p>
<pre><code class="copyable">/*
dataType 是返回值类型，它可以是C语言中的任意数据类型，例如: int、float、char 等。

functionName 是函数名，它是标识符的一种，命名规则和标识符相同。函数名后面的括号( )不能少。

body 是函数体，它是函数需要执行的代码，是函数的主体部分。即使只有一个语句，函数体也要由&#123; &#125;包围。

*/

dataType  functionName()
&#123;
    //body
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果有返回值，在函数体中使用 <code>return</code> 语句返回。<code>return</code> 出来的数据的类型要和 <code>dataType</code> 一样。</strong></p>
<h2 data-id="heading-1">二.函数返回值</h2>
<h3 data-id="heading-2">1.函数没有返回值</h3>
<p><strong>如果函数没有返回值，函数名前面用 <code>void</code> 修饰</strong>，例如：</p>
<pre><code class="copyable">void func(); //声明一个函数，该函数没有返回值
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.函数有返回值</h3>
<p>如果<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8708.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8708.html" ref="nofollow noopener noreferrer">函数</a>有返回值，函数名前面用返回值类型,可以用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7426.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7426.html" ref="nofollow noopener noreferrer"><code>int</code> / <code>float</code> / <code>double</code> /</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7815.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7815.html" ref="nofollow noopener noreferrer"><code>char</code></a> 等等修饰，例如：</p>
<pre><code class="copyable">int func1();          //声明一个函数，该函数返回值是整数int类型
float func2();        //声明一个函数，该函数返回值是浮点数float类型
double func3();       //声明一个函数，该函数返回值是浮点数double类型
char func4();         //声明一个函数，该函数返回值是字符char类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">三.函数参数</h2>
<h3 data-id="heading-5">1.函数没有参数</h3>
<p>函数没有参数，就表示没有参数列表，例如：</p>
<pre><code class="copyable">int func1();    //声明一个函数，该函数返回值是整数int类型
float func2();  //声明一个函数，该函数返回值是浮点数float类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.函数有固定参数</h3>
<pre><code class="copyable">dataType  functionName( dataType1 param1, dataType2 param2 ...)
&#123;
    //body
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dataType1 param1, dataType2 param2 ...</code>是参数列表。函数可以只有一个参数，也可以有多个，多个参数之间由,分隔。参数本质上也是变量，定义时要指明类型和名称。与无参函数的定义相比，有参函数的定义仅仅是多了一个参数列表,例如：</p>
<pre><code class="copyable">int func1(int x);          //声明一个函数，该函数返回值是整数int类型
float func2(int x,int y);  //声明一个函数，该函数返回值是浮点数float类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3.函数有不定长度参数</h3>
<p>函数的不定长参数，指函数的参数个数不固定，可以是两个，也可以是三个或者更多，例如最常见的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7464.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7464.html" ref="nofollow noopener noreferrer"><code>printf</code> 函数</a>:</p>
<pre><code class="copyable">printf("%s","hello world");
printf("%d-%d-%d",1,2,3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于函数的不定长参数，这里暂时不做讲解，后面文章再做详细介绍；</p>
<h2 data-id="heading-8">四.函数声明和定义</h2>
<p>函数声明只是一个空壳，不会有具体的函数实现，而定义要实现函数的实现;</p>
<h3 data-id="heading-9">1.函数声明：不需要实现这个函数的功能</h3>
<pre><code class="copyable">int add(int x,int y); //只需要声明即可，不需要实现这个函数的功能
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.函数定义：必须实现这个函数的功能</h3>
<pre><code class="copyable">int add(int x,int y) 需要实现这个函数的功能
&#123;
    return (x+y);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">五.猜你喜欢</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7548.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7548.html" ref="nofollow noopener noreferrer">C 语言逻辑运算符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7558.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7558.html" ref="nofollow noopener noreferrer">C 语言三目运算符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7577.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7577.html" ref="nofollow noopener noreferrer">C 语言逗号表达式</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7865.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7865.html" ref="nofollow noopener noreferrer">C 语言 sizeof 和 strlen 函数区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7945.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7945.html" ref="nofollow noopener noreferrer">C 语言 strcpy 和 strcpy_s 函数区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7973.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7973.html" ref="nofollow noopener noreferrer">C 语言 memcpy 和 memcpy_s 区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8159.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8159.html" ref="nofollow noopener noreferrer">C 语言 数组定义和使用</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8186.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8186.html" ref="nofollow noopener noreferrer">C 语言 数组遍历</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8257.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8257.html" ref="nofollow noopener noreferrer">C 语言 数组下标越界</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8270.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8270.html" ref="nofollow noopener noreferrer">C 语言 数组内存溢出</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8331.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8331.html" ref="nofollow noopener noreferrer">C 语言 数组下标越界和内存溢出区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8338.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8338.html" ref="nofollow noopener noreferrer">C 语言 二维数组定义和使用</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8343.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8343.html" ref="nofollow noopener noreferrer">C 语言 二维数组行数和列数计算</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8349.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8349.html" ref="nofollow noopener noreferrer">C 语言 指针声明和定义</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8456.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8456.html" ref="nofollow noopener noreferrer">C 语言 指针 p++ / p–</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8520.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8520.html" ref="nofollow noopener noreferrer">C 语言 <em>p++/</em>§++/_(p++)/_p++</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8540.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8540.html" ref="nofollow noopener noreferrer">C 语言 使用指针遍历数组</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8564.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8564.html" ref="nofollow noopener noreferrer">C 语言 指针和数组区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8606.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8606.html" ref="nofollow noopener noreferrer">C 语言 数组指针</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8597.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8597.html" ref="nofollow noopener noreferrer">C 语言 指针数组</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8613.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8613.html" ref="nofollow noopener noreferrer">C 语言 指针数组和数组指针区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8674.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8674.html" ref="nofollow noopener noreferrer">C 语言 空指针 NULL</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8690.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8690.html" ref="nofollow noopener noreferrer">C 语言 void 指针</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8700.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8700.html" ref="nofollow noopener noreferrer">C 语言 野指针</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8708.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8708.html" ref="nofollow noopener noreferrer">C 语言 函数声明和定义</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8708.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8708.html" ref="nofollow noopener noreferrer">C 语言 函数声明和定义</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            