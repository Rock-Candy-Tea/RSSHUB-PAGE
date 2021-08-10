
---
title: 'C语言 sizeof 和 strlen 函数区别 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8441'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 17:36:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=8441'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6994609063027802149#%E4%B8%80sizeof%E5%87%BD%E6%95%B0%E4%B8%8Estrlen%E5%87%BD%E6%95%B0%E5%8C%BA%E5%88%AB" title="#%E4%B8%80sizeof%E5%87%BD%E6%95%B0%E4%B8%8Estrlen%E5%87%BD%E6%95%B0%E5%8C%BA%E5%88%AB" target="_blank">一.sizeof 函数与 strlen 函数区别</a>
<ul>
<li><a href="https://juejin.cn/post/6994609063027802149#1%E8%8E%B7%E5%8F%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%95%BF%E5%BA%A6_-_%E9%92%88%E5%AF%B9%E5%AD%97%E7%AC%A6%E4%B8%B2" title="#1%E8%8E%B7%E5%8F%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%95%BF%E5%BA%A6_-_%E9%92%88%E5%AF%B9%E5%AD%97%E7%AC%A6%E4%B8%B2" target="_blank">1.获取字符串长度 – 针对字符串</a></li>
<li><a href="https://juejin.cn/post/6994609063027802149#2%E8%8E%B7%E5%8F%96%E6%8C%87%E9%92%88%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6_-_%E9%92%88%E5%AF%B9%E6%8C%87%E9%92%88%E6%95%B0%E7%BB%84" title="#2%E8%8E%B7%E5%8F%96%E6%8C%87%E9%92%88%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6_-_%E9%92%88%E5%AF%B9%E6%8C%87%E9%92%88%E6%95%B0%E7%BB%84" target="_blank">2.获取指针/数组长度 – 针对指针/数组</a></li>
<li><a href="https://juejin.cn/post/6994609063027802149#3sizeof_%E8%8E%B7%E5%8F%96%E5%86%85%E5%AD%98%E5%A4%A7%E5%B0%8F" title="#3sizeof_%E8%8E%B7%E5%8F%96%E5%86%85%E5%AD%98%E5%A4%A7%E5%B0%8F" target="_blank">3.sizeof 获取内存大小</a></li>
<li><a href="https://juejin.cn/post/6994609063027802149#4%E7%BB%8F%E5%85%B8%E6%A1%88%E4%BE%8B" title="#4%E7%BB%8F%E5%85%B8%E6%A1%88%E4%BE%8B" target="_blank">4.经典案例</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6994609063027802149#%E4%BA%8C%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E4%BA%8C%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">二.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.sizeof 函数与 strlen 函数区别</h2>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer"><code>C</code> 语言</a>中，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7834.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7834.html" ref="nofollow noopener noreferrer"><code>strlen</code> 函数</a>和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7851.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7851.html" ref="nofollow noopener noreferrer"><code>sizeof</code> 函数</a>都能获取字符串长度，但是两者之间到底有什么区别呢，下面我们一一道来；</p>
<h3 data-id="heading-1">1.获取字符串长度 – 针对字符串</h3>
<p><strong><code>sizeof</code> 函数数获取的长度是整个内存大小的长度，返回的长度包括<code>'\0'</code>；<code>strlen</code> 函数获取的长度以<code>'\0'</code>结尾，返回的长度不包括<code>'\0'</code>；</strong></p>
<p><strong>a.获取常规字符串长度 – 使用 strlen 和 sizeof 都一样</strong></p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 sizeof 和 strlen 函数区别
//@Time:2021/06/03 07:40
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

char p[4] = "abc";
printf("字符串：%s   sizeof长度：%d\n", p, sizeof(p));
printf("字符串：%s   strlen长度：%d\n", p, strlen(p));
/*
输出：

字符串：abc   sizeof长度：4
字符串：abc   strlen长度：3
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>sizeof</code> 求的是字符串在内存中的长度，所以它是加上最后的 <code>'\0'</code> 的，所以一般而言 <code>sizeof</code> 函数的长度会比 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7834.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7834.html" ref="nofollow noopener noreferrer"><code>strlen</code> 函数</a>的长度多 1。</strong></p>
<p><strong>b.获取非常规字符串长度 – 使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7865.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7865.html" ref="nofollow noopener noreferrer">strlen 和 sizeof 不一样</a></strong></p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 sizeof 和 strlen 函数区别
//@Time:2021/06/03 07:40
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

char str[1char str[100] = &#123;0&#125;;
strcpy(str, "abcd");
int str_len = strlen(str);
int str_size = sizeof(str);
printf("strlen(str) = %d\n", (str_len));
printf("sizeof(str) = %d\n", (str_size));
/*
输出：

strlen(str) = 4
sizeof(str) = 100
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这个例子可以充分说明：strlen 计算的是字符串到<code>'\0'</code>位置的大小，<code>sizeof</code> 计算的字符串占的内存大小，这也是 <code>strlen</code> 函数和 <code>[sizeof](https://www.codersrc.com/archives/7851.html)</code> 不同之处；</strong></p>
<h3 data-id="heading-2">2.获取指针/数组长度 – 针对指针/数组</h3>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 sizeof 和 strlen 函数区别
//@Time:2021/06/03 07:40
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

char p1[] = "abcdefg"; //数组
printf("字符串：%s   sizeof长度：%d\n", p1, sizeof(p1));
printf("字符串：%s   strlen长度：%d\n", p1, strlen(p1));
printf("----------------------------\n");
char* p2 = "abcdefg"; //指针
printf("字符串：%s   sizeof长度：%d\n", p2, strlen(p2));
printf("字符串：%s   strlen长度：%d\n", p2, sizeof(p2));
/*

输出：

字符串：abcdefg   sizeof长度：8
字符串：abcdefg   strlen长度：7
----------------------------
字符串：abcdefg   sizeof长度：7
字符串：abcdefg   strlen长度：4

*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>值得注意的是：指针占用的内存大小始终为 4 个字节；</strong></p>
<h3 data-id="heading-3">3.sizeof 获取内存大小</h3>
<p><strong><code>strlen</code> 函数只能计算字符串长度，<code>sizeof</code>能获取 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7409.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7409.html" ref="nofollow noopener noreferrer">int / float / bool / char</a> 等等所有类型的内存占用大小</strong>，比如：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 sizeof 和 strlen 函数区别
//@Time:2021/06/03 07:40
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

printf("int=%d\nshort=%d\ndouble=%d\n", sizeof(int), sizeof(short), sizeof(double));
/*
输出：

int=4
short=2
double=8
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4.经典案例</h3>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 sizeof 和 strlen 函数区别
//@Time:2021/06/03 07:40
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include<stdlib.h>
#include<stdio.h>
void main()
&#123;
    int arr[] = &#123; 1, 2, 3 &#125;;
    printf("sizeof(arr) : %d\n",sizeof(arr));
    for (int i = 0; i < sizeof(arr); i++)&#123;
        printf("%d,", arr[i]);
    &#125;
    printf("\n");
    system("pause");
&#125;
/*
输出结果：

sizeof(arr) : 12
1,2,3,-858993460,9697168,11737625,1,13017304,13018680,123799719,11735310,11735310,
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是很懵逼，，除了会输出 <code>1</code>，<code>2</code>，<code>3</code> 以外，还会输出杂乱无章的数字，但一共是输出 <code>12</code> 个。<strong>因为数组的内存是动态分配的，到了元素 <code>3</code> 以后的元素都是新分配的，并不一定是空，随机数。</strong></p>
<p>因为数组是一片连续的空间，有可能元素 <code>3</code> 的空间是有数据的，那么 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer"><code>C</code> 语言</a>会将其读取出来，当然是一些没有实际意义的杂乱无章的数字，但你不要想着去操作，否则可能导致数据错乱，所以有可能你运行好几次，后面的值都不会有变化。正确版本如下：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 sizeof 和 strlen 函数区别
//@Time:2021/06/03 07:40
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

int arr[] = &#123; 1, 2, 3 &#125;;
printf("sizeof(arr)/sizeof(int) : %d\n", sizeof(arr) / sizeof(int));
for (int i = 0; i < sizeof(arr) / sizeof(int); i++)&#123;
    printf("%d,", arr[i]);
&#125;
/*
输出：

sizeof(arr)/sizeof(int) : 3
1,2,3,
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">二.猜你喜欢</h2>
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
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7865.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7865.html" ref="nofollow noopener noreferrer">C 语言 sizeof 和 strlen 函数区别</a></p>
<p>[喜欢(3)](javascript:😉 [打赏](javascript:😉</p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            