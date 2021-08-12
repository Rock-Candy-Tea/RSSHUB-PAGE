
---
title: 'C语言 memcpy 函数 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=2496'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 17:53:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=2496'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6995355814819004452#%E4%B8%80memcpy%E5%87%BD%E6%95%B0%E7%AE%80%E4%BB%8B" title="#%E4%B8%80memcpy%E5%87%BD%E6%95%B0%E7%AE%80%E4%BB%8B" target="_blank">一.memcpy 函数简介</a></li>
<li><a href="https://juejin.cn/post/6995355814819004452#%E4%BA%8Cmemcpy%E5%87%BD%E6%95%B0%E5%AE%9E%E6%88%98" title="#%E4%BA%8Cmemcpy%E5%87%BD%E6%95%B0%E5%AE%9E%E6%88%98" target="_blank">二.memcpy 函数实战</a>
<ul>
<li><a href="https://juejin.cn/post/6995355814819004452#1memcpy%E5%87%BD%E6%95%B0%E7%AE%80%E5%8D%95%E4%BD%BF%E7%94%A8" title="#1memcpy%E5%87%BD%E6%95%B0%E7%AE%80%E5%8D%95%E4%BD%BF%E7%94%A8" target="_blank">1.memcpy 函数简单使用</a></li>
<li><a href="https://juejin.cn/post/6995355814819004452#2strcpy%E5%87%BD%E6%95%B0%E5%B1%9E%E4%BA%8E%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8B%B7%E8%B4%9D" title="#2strcpy%E5%87%BD%E6%95%B0%E5%B1%9E%E4%BA%8E%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8B%B7%E8%B4%9D" target="_blank">2.strcpy 函数属于字符串拷贝</a></li>
<li><a href="https://juejin.cn/post/6995355814819004452#3memcpy%E5%87%BD%E6%95%B0%E5%B1%9E%E4%BA%8E%E5%86%85%E5%AD%98%E6%8B%B7%E8%B4%9D" title="#3memcpy%E5%87%BD%E6%95%B0%E5%B1%9E%E4%BA%8E%E5%86%85%E5%AD%98%E6%8B%B7%E8%B4%9D" target="_blank">3.memcpy 函数属于内存拷贝</a></li>
<li><a href="https://juejin.cn/post/6995355814819004452#4memcpy%E5%87%BD%E6%95%B0%E6%B3%A8%E6%84%8F%E5%B4%A9%E6%BA%83%E9%97%AE%E9%A2%98" title="#4memcpy%E5%87%BD%E6%95%B0%E6%B3%A8%E6%84%8F%E5%B4%A9%E6%BA%83%E9%97%AE%E9%A2%98" target="_blank">4.memcpy 函数注意崩溃问题</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6995355814819004452#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">三.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.memcpy 函数简介</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer"><code>C</code> 语言</a>在 <code>string.h</code> 中 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7891.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7891.html" ref="nofollow noopener noreferrer"><code>strcpy</code> 函数</a>和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7918.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7918.html" ref="nofollow noopener noreferrer"><code>strcpy_s</code> 函数</a>,可用完成 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7815.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7815.html" ref="nofollow noopener noreferrer">char 字符串</a>拷贝，对于字符串拷贝，还有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8005.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8005.html" ref="nofollow noopener noreferrer"><code>memcpy</code> 函数</a>也能完成，语法如下：</p>
<pre><code class="copyable">/*
*描述：此类函数是用于对字符串进行复制（拷贝），属于内存拷贝！
*
*参数：
*   [out] dst：拷贝完成之后的字符串
*   [in] src ：需要拷贝的字符串
*   [in] n   ：需要拷贝的字节数
*
*返回值：指向 dst 这个字符串的指针
*注意：如果需要拷贝的字节数n 大于 dst 的内存大小，程序会崩溃
*/
void *memcpy(void *dst, void *src, unsigned int n);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<p><strong>1.<code>strcpy</code> 函数和 <code>strcpy_s</code> 函数在拷贝过程中，如果遇到<code>'\0'</code>结束符，那么直接结束拷贝；<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8005.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8005.html" ref="nofollow noopener noreferrer">memcpy 函数</a>拷贝过程中就算遇到<code>'\0'</code>结束符也不会结束；</strong></p>
<pre><code class="copyable">strcpy 函数和 strcpy_s 函数 属于字符串拷贝;
memcpy 函数属于内存拷贝;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.如果使用 memcpy 函数提示 error：4996，请参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8057.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8057.html" ref="nofollow noopener noreferrer">error C4996: ‘fopen’: This function or variable may be unsafe</a></p>
<pre><code class="copyable">error C4996: 'memcpy': This function or variable may be unsafe. Consider using memcpy_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.必须保证 <code>dst</code> 空间足够大，能够容纳 <code>src</code> ，如果 <code>dst</code> 内存空间大小比 <code>src</code> 更小，会导致溢出错误，引起程序崩溃！可以通过 <code>sizeof</code> 函数查看内存内存大小</strong>，举个例子：<code>50ml</code> 的水杯能倒进 <code>500ml</code> 的水杯没问题，<code>500ml</code> 的水杯倒进 <code>50ml</code> 的水杯，会溢出很多水；</p>
<h2 data-id="heading-1">二.memcpy 函数实战</h2>
<h3 data-id="heading-2">1.memcpy 函数简单使用</h3>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 memcpy 函数
//@Time:2021/06/03 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include "windows.h"
//error C4996: 'memcpy': This function or variable may be unsafe. Consider using memcpy_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
#pragma warning( disable : 4996)
void main()
&#123;
    char src[1024] = &#123; "C/C++教程-memcpy函数 - www.codersrc.com" &#125;;
    char dst[1024] = &#123; 0 &#125;;
    printf("memcpy之前 dst:%s\n", dst); //空字符串
    memcpy(dst, src , sizeof(src)/sizeof(char));
    printf("memcpy之后 dst:%s\n", dst);//
    printf("\n");
    system("pause");
&#125;
/*
输出：
memcpy之前 dst:
memcpy之后 dst:C/C++教程-memcpy函数 - www.codersrc.com
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.strcpy 函数属于字符串拷贝</h3>
<p>**在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7815.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7815.html" ref="nofollow noopener noreferrer"><code>char</code> 字符串</a>中有作介绍，字符串默认都是<code>'\0'</code>结尾，<code>strcpy</code> 函数或者 <code>strcpy_s</code> 函数在拷贝过程中，如果遇到<code>'\0'</code>结束符，那么直接结束拷贝，**看下面例子：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 memcpy函数
//@Time:2021/06/03 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

char src[1024] = &#123; "C/C++教程-strcpy函数\0 - www.codersrc.com" &#125;;
char dst[1024] = &#123; 0 &#125;;
printf("strcpy之前 dst:%s\n", dst);
strcpy(dst, src );
printf("strcpy之后 dst:%s\n", dst);
printf("\n");
system("pause");

/*
输出：
strcpy之前 dst:
strcpy之后 dst:C/C++教程-strcpy函数
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重上面的输出结果可以看出：<code>strcpy</code> 函数在拷贝的时候，如果遇到<code>'\0'</code>，那么拷贝直接结束，所以上面使用 <code>strcpy</code> 拷贝的时候，<code>dst</code> 字符串明显少了一段字符<code>" - www.codersrc.com"</code>;</p>
<h3 data-id="heading-4">3.memcpy 函数属于内存拷贝</h3>
<p><strong>而 memcpy 函数不同，memcpy 属于内存拷贝，即便在拷贝过程中遇到<code>'\0'</code>结束符，也不会结束拷贝</strong>，举个例子：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 memcpy函数
//@Time:2021/06/03 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

char src[1024] = &#123; "C/C++教程-memcpy函数\0 - www.codersrc.com" &#125;;
char dst[1024] = &#123; 0 &#125;;
printf("memcpy之前 dst:%s\n", dst);
memcpy(dst, src, sizeof(src)/sizeof(char));
printf("memcpy之后 dst:%s\n", dst);
printf("\n");
system("pause");

/*
输出：

memcpy之前 dst:
memcpy之后 dst:C/C++教程-memcpy函数\0 - www.codersrc.com
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，<code>memcpy</code> 函数内存拷贝的时候，<code>'\0'</code>仅仅是当作了内存中的数据，并不代表拷贝结尾；</p>
<h3 data-id="heading-5">4.memcpy 函数注意崩溃问题</h3>
<p><strong>如果使用 <code>memcpy</code> 的时候需要拷贝的字符大小比 <code>dst</code> 内存大时，程序运行会崩溃，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8005.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8005.html" ref="nofollow noopener noreferrer"><code>memcpy</code> 函数</a>在字符串拷贝的时候并不会检查两个字符串空间大小，所有很容易产生崩溃，这也是 <code>error C4996</code> 的原因之一</strong>，举个例子：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 memcpy函数
//@Time:2021/06/03 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include "windows.h"
//error C4996: 'memcpy': This function or variable may be unsafe. Consider using memcpy_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
#pragma warning( disable : 4996)
void main()
&#123;
    char src[1024] = &#123; "C/C++教程-memcpy函数\0 - www.codersrc.com" &#125;;
    char dst[10] = &#123; 0 &#125;;
    int len_src = sizeof(src)/sizeof(char); // 1024
    int len_dst = sizeof(dst) / sizeof(char); //10
    printf("len_src:%d len_dst:%d\n", len_src,len_dst);
    printf("memcpy之前 dst:%s\n", dst);
    memcpy(dst, src, len_src);  // 很明显 dst 的空间大小只有10个字节并不能完全存放 src 1024个字节，程序崩溃
    printf("memcpy之后 dst:%s\n", dst);
&#125;
/*
输出：
len_src:1024 len_dst:10
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">三.猜你喜欢</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer">安装 Visual Studio</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7280.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7280.html" ref="nofollow noopener noreferrer">安装 Visual Studio 插件 Visual Assist</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7288.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7288.html" ref="nofollow noopener noreferrer">Visual Studio 2008 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7292.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7292.html" ref="nofollow noopener noreferrer">Visual Studio 2003/2015 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7284.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7284.html" ref="nofollow noopener noreferrer">设置 Visual Studio 字体/背景/行号</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7460.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7460.html" ref="nofollow noopener noreferrer">C 语言格式控制符/占位符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7548.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7548.html" ref="nofollow noopener noreferrer">C 语言逻辑运算符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7558.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7558.html" ref="nofollow noopener noreferrer">C 语言三目运算符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7577.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7577.html" ref="nofollow noopener noreferrer">C 语言逗号表达式</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7579.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7579.html" ref="nofollow noopener noreferrer">C 语言自加自减运算符(++i / i++)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7581.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7581.html" ref="nofollow noopener noreferrer">C 语言 for 循环</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7583.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7583.html" ref="nofollow noopener noreferrer">C 语言 break 和 continue</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7585.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7585.html" ref="nofollow noopener noreferrer">C 语言 while 循环</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7587.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7587.html" ref="nofollow noopener noreferrer">C 语言 do while 和 while 循环</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7782.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7782.html" ref="nofollow noopener noreferrer">C 语言 switch 语句</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7796.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7796.html" ref="nofollow noopener noreferrer">C 语言 goto 语句</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7815.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7815.html" ref="nofollow noopener noreferrer">C 语言 char 字符串</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7834.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7834.html" ref="nofollow noopener noreferrer">C 语言 strlen 函数</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7851.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7851.html" ref="nofollow noopener noreferrer">C 语言 sizeof 函数</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7865.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7865.html" ref="nofollow noopener noreferrer">C 语言 sizeof 和 strlen 函数区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7891.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7891.html" ref="nofollow noopener noreferrer">C 语言 strcpy 函数</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7918.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7918.html" ref="nofollow noopener noreferrer">C 语言 strcpy_s 函数</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8005.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8005.html" ref="nofollow noopener noreferrer">C 语言 memcpy 函数</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8005.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8005.html" ref="nofollow noopener noreferrer">C 语言 memcpy 函数</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            