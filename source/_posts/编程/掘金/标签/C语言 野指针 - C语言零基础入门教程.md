
---
title: 'C语言 野指针 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d89d4db5ff435c9a89c16745f2c818~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 17:42:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d89d4db5ff435c9a89c16745f2c818~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/7001660622437875743#%E4%B8%80%E7%AE%80%E4%BB%8B" title="#%E4%B8%80%E7%AE%80%E4%BB%8B" target="_blank">一.简介</a></li>
<li><a href="https://juejin.cn/post/7001660622437875743#%E4%BA%8C%E9%87%8E%E6%8C%87%E9%92%88%E4%BA%A7%E7%94%9F%E7%9A%84%E5%8E%9F%E5%9B%A0" title="#%E4%BA%8C%E9%87%8E%E6%8C%87%E9%92%88%E4%BA%A7%E7%94%9F%E7%9A%84%E5%8E%9F%E5%9B%A0" target="_blank">二.野指针产生的原因</a>
<ul>
<li><a href="https://juejin.cn/post/7001660622437875743#1%E6%8C%87%E9%92%88%E5%8F%98%E9%87%8F%E6%9C%AA%E5%88%9D%E5%A7%8B%E5%8C%96" title="#1%E6%8C%87%E9%92%88%E5%8F%98%E9%87%8F%E6%9C%AA%E5%88%9D%E5%A7%8B%E5%8C%96" target="_blank">1.指针变量未初始化</a></li>
<li><a href="https://juejin.cn/post/7001660622437875743#2%E6%8C%87%E9%92%88%E9%87%8A%E6%94%BE%E5%90%8E%E4%B9%8B%E5%90%8E%E6%9C%AA%E7%BD%AE%E7%A9%BA" title="#2%E6%8C%87%E9%92%88%E9%87%8A%E6%94%BE%E5%90%8E%E4%B9%8B%E5%90%8E%E6%9C%AA%E7%BD%AE%E7%A9%BA" target="_blank">2.指针释放后之后未置空</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/7001660622437875743#%E4%B8%89%E9%81%BF%E5%85%8D%E9%87%8E%E6%8C%87%E9%92%88%E4%BA%A7%E7%94%9F" title="#%E4%B8%89%E9%81%BF%E5%85%8D%E9%87%8E%E6%8C%87%E9%92%88%E4%BA%A7%E7%94%9F" target="_blank">三.避免野指针产生</a>
<ul>
<li><a href="https://juejin.cn/post/7001660622437875743#1%E5%88%9D%E5%A7%8B%E5%8C%96%E6%97%B6%E7%BD%AE_NULL" title="#1%E5%88%9D%E5%A7%8B%E5%8C%96%E6%97%B6%E7%BD%AE_NULL" target="_blank">1.初始化时置 NULL</a></li>
<li><a href="https://juejin.cn/post/7001660622437875743#2%E9%87%8A%E6%94%BE%E6%97%B6%E7%BD%AE_NULL" title="#2%E9%87%8A%E6%94%BE%E6%97%B6%E7%BD%AE_NULL" target="_blank">2.释放时置 NULL</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/7001660622437875743#%E5%9B%9B%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E5%9B%9B%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">四.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.简介</h2>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8700.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8700.html" ref="nofollow noopener noreferrer">野指针</a>就是指针指向的位置是不可知的（随机的、不正确的、没有明确限制的）；</strong></p>
<h2 data-id="heading-1">二.野指针产生的原因</h2>
<h3 data-id="heading-2">1.指针变量未初始化</h3>
<p><strong>任何<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8349.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8349.html" ref="nofollow noopener noreferrer">指针</a>变量刚被创建时不会自动成为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8674.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8674.html" ref="nofollow noopener noreferrer"><code>NULL</code> 指针</a>，它的缺省值是随机的。</strong></p>
<p><strong>所以，指针变量在创建的同时应当被初始化，要么将指针设置为 <code>NULL</code> ，要么让它指向合法的内存。</strong></p>
<p><strong>如果没有初始化，编译器会报错<code>‘point’ may be uninitializedin the function</code>。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d89d4db5ff435c9a89c16745f2c818~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.指针释放后之后未置空</h3>
<p><strong>指针在 <code>free</code> 或 <code>delete</code> 后未赋值 <code>NULL</code> ，它们只是把指针所指的内存给释放掉，但并没有处理指针本身。此时指针指向不可知的（随机的、不正确的、没有明确限制的）。</strong></p>
<p><strong>释放后的指针应立即将指针置为<code>NULL</code>，防止产生野指针。</strong></p>
<h2 data-id="heading-4">三.避免野指针产生</h2>
<h3 data-id="heading-5">1.初始化时置 NULL</h3>
<p><strong>指针变量一定要初始化为 <code>NULL</code>，因为任何指针变量(除了 <code>static</code> 修饰的指针变量)刚被创建时不会自动成为 <code>NULL</code> 指针，它的缺省值是随机的。</strong></p>
<h3 data-id="heading-6">2.释放时置 NULL</h3>
<p>当指针 <code>p</code> 指向的内存空间释放时，没有设置指针 <code>p</code> 的值为 <code>NULL</code> 。<code>delete</code> 和 <code>free</code> 只是把内存空间释放了，但是并没有将指针 <code>p</code> 的值赋为 <code>NULL</code> 。</p>
<p><strong>通常判断一个指针是否合法，都是使用 <code>if</code> 语句测试该指针是否<code>为 NULL</code></strong>。例如：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 野指针
//@Time:2021/06/20 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include<stdlib.h>
#include<stdio.h>
void main()
&#123;
    int *p = new int(6);
    printf("释放内存之前 p:%p\n", p);
    //delete 释放内存
    delete p;
    if (p != NULL) //delete 之后指针指向未知/随机内存
        printf("释放内存之后 p:%p\n", p);
    //*p = 7; //操作未知/随机的内存地址，程序异常崩溃
    system("pause");
&#125;
/*
输出：
释放内存之前 p:016950E8
释放内存之后 p:00008123
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重上面的代码输出结果可以看出：<strong><code>delete</code> 之后，指针 <code>p</code> 地址并没有被置为 <code>NULL</code> ，<code>p</code> 此时指向一块随机/未知的内存地址，一旦对未知的内存地址操作或者访问，程序崩溃</strong>；</p>
<h2 data-id="heading-7">四.猜你喜欢</h2>
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
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8700.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8700.html" ref="nofollow noopener noreferrer">C 语言 野指针</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            