
---
title: 'C语言 strcat_s 函数 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=4735'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 16:12:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=4735'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6996442358162145317#%E4%B8%80strcat_s%E5%87%BD%E6%95%B0%E7%AE%80%E4%BB%8B" title="#%E4%B8%80strcat_s%E5%87%BD%E6%95%B0%E7%AE%80%E4%BB%8B" target="_blank">一.strcat_s 函数简介</a></li>
<li><a href="https://juejin.cn/post/6996442358162145317#%E4%BA%8Cstrcat_s%E5%87%BD%E6%95%B0%E5%8E%9F%E7%90%86" title="#%E4%BA%8Cstrcat_s%E5%87%BD%E6%95%B0%E5%8E%9F%E7%90%86" target="_blank">二.strcat_s 函数原理</a></li>
<li><a href="https://juejin.cn/post/6996442358162145317#%E4%B8%89strcat_s%E5%87%BD%E6%95%B0%E5%AE%9E%E6%88%98" title="#%E4%B8%89strcat_s%E5%87%BD%E6%95%B0%E5%AE%9E%E6%88%98" target="_blank">三.strcat_s 函数实战</a></li>
<li><a href="https://juejin.cn/post/6996442358162145317#%E5%9B%9B%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E5%9B%9B%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">四.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.strcat_s 函数简介</h2>
<p>前面文章中介绍了关于字符串拼接函数 <code>strcat</code> ，而 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8110.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8110.html" ref="nofollow noopener noreferrer"><code>strcat_s</code> 函数</a>和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8108.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8108.html" ref="nofollow noopener noreferrer"><code>strcat</code> 函数</a>一样，主要用于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7815.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7815.html" ref="nofollow noopener noreferrer">字符串</a>拼接；</p>
<p><code>strcat_s</code> 是系统的安全函数，微软在 <code>2005</code> 后建议用一系统所谓安全的函数，这中间就有 <code>strcat_s</code> 取代了 <code>strcat</code> ，原来 <code>strcat</code> 函数，没有方法来保证有效的缓冲区尺寸，所以它只能假定缓冲足够大来容纳要拷贝的字符串,容易产生程序崩溃。而<code>strcat_s</code>函数能很好的规避这个问题，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8110.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8110.html" ref="nofollow noopener noreferrer"><code>strcat_s</code>函数</a>语法如下：</p>
<pre><code class="copyable">/*
*描述：此类函数是用于对字符串进行拼接， 将两个字符串连接再一起
*
*参数：
*   [in] strSource：需要追加的字符串
*   [in] numberOfElements：拼接后的字符串大小（并非目标字符串大小也并非原始字符串大小）
*   [out] strDestination：目标字符串
*
*返回值：errno_t是微软新定义的一种类型，这种类型是一种整型，
*       代表错误代码，若果是0 则代表没有错误，如果是其他的值 ，则会抛出一个值；
*/
//头文件：string.h
errno_t strcat_s(char *strDestination , size_t numberOfElements , const char *strSource );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.<code>strcat_s</code> 函数把 <code>strSource</code> 所指向的字符串追加到 <code>strDestination</code> 所指向的字符串的结尾，所以必须要保证 <code>strDestination</code> 有足够的内存空间来容纳 <code>strSource</code> 和 <code>strDestination</code> 两个字符串，否则会导致溢出错误。</strong></p>
<blockquote>
<p><strong><code>strcat_s</code> 函数原理：<code>dst</code>内存空间大小 = 目标字符串长度 + 原始字符串场地 + ‘\0’；</strong></p>
</blockquote>
<p><strong>2.<code>strDestination</code> 末尾的<code>\0</code>会被覆盖，<code>strSource</code> 末尾的<code>\0</code>会一起被复制过去，最终的字符串只有一个<code>\0</code>;</strong></p>
<h2 data-id="heading-1">二.strcat_s 函数原理</h2>
<blockquote>
<p><strong><code>strcat_s</code> 函数原理：<code>dst</code> 内存空间大小 = 目标字符串长度 + 原始字符串场地 + ‘\0’；</strong></p>
<p><strong>获取内存空间大小使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7851.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7851.html" ref="nofollow noopener noreferrer"><code>sizeof</code> 函数</a>（获取内存空间大小）</strong>；<strong>获取字符串长度使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7834.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7834.html" ref="nofollow noopener noreferrer"><code>strlen</code> 函数</a>（查字符串长度）</strong></p>
</blockquote>
<h2 data-id="heading-2">三.strcat_s 函数实战</h2>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 strcat_s 函数
//@Time:2021/06/05 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include "windows.h"

//error C4996: 'strcat': This function or variable may be unsafe. Consider using strcat_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
#pragma warning( disable : 4996)

void main()
&#123;
    char src[1024] = &#123; "C/C++教程-strcat_s函数" &#125;;
    char dst[1024] = &#123; "www.codersrc.com" &#125;;
    //注意：strcat_s第二个参数的计算，该参数是拼接后的字符串大小，并非原字符串大小或者目标字符串大小
    int len = strlen(src) + strlen(dst) + 1;
    printf("strcat_s之前 dst:%s\n", dst); //
    strcat_s(dst, len, src);
    printf("strcat_s之后 dst:%s\n", dst);//
    system("pause");
&#125;
输出结果：
strcat_s之前 dst:www.codersrc.com
strcat_s之后 dst:www.codersrc.comC/C++教程-strcat_s函数
请按任意键继续. . .
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8110.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8110.html" ref="nofollow noopener noreferrer"><code>strcat_s</code></a> 第二个参数的计算，该参数是拼接后的字符串大小，并非原字符串大小或者目标字符串大小;</strong></p>
<h2 data-id="heading-3">四.猜你喜欢</h2>
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
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7945.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7945.html" ref="nofollow noopener noreferrer">C 语言 strcpy 和 strcpy_s 函数区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7973.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7973.html" ref="nofollow noopener noreferrer">C 语言 memcpy 和 memcpy_s 区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8108.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8108.html" ref="nofollow noopener noreferrer">C 语言 strcat 函数</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8110.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8110.html" ref="nofollow noopener noreferrer">C 语言 strcat_s 函数</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8110.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8110.html" ref="nofollow noopener noreferrer">C 语言 strcat_s 函数</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            