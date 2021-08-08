
---
title: 'C语言 switch 语句 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7924'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 15:47:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=7924'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6993837800898445325#%E4%B8%80switch%E8%AF%AD%E5%8F%A5%E7%AE%80%E4%BB%8B" title="#%E4%B8%80switch%E8%AF%AD%E5%8F%A5%E7%AE%80%E4%BB%8B" target="_blank">一.switch 语句简介</a></li>
<li><a href="https://juejin.cn/post/6993837800898445325#%E4%BA%8Cswitch%E8%AF%AD%E5%8F%A5%E5%AE%9E%E6%88%98" title="#%E4%BA%8Cswitch%E8%AF%AD%E5%8F%A5%E5%AE%9E%E6%88%98" target="_blank">二.switch 语句实战</a></li>
<li><a href="https://juejin.cn/post/6993837800898445325#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">三.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<p>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer"><code>C</code> 语言</a>中，<code>switch</code> 语句和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7466.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7466.html" ref="nofollow noopener noreferrer"><code>if</code> / <code>else</code></a> 类似，都可以作为条件分支判断，当分支判断较少的适合推荐使用 <code>if</code> / <code>else</code> ；当分支判断比较多的时候推荐使用 <code>switch</code> 语句，具体使用请看下文;</p>
<h2 data-id="heading-0">一.<code>switch</code>语句简介</h2>
<p><code>switch</code> 语法如下：</p>
<pre><code class="copyable">switch (表达式)
&#123;

case 常量表达式1:
语句块1;
break;

case 常量表达式2:
语句块2;
break;

……

case 常量表达式m:
语句块m;
break;

default:
语句块n;
break;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用说明如下：</strong></p>
<ul>
<li><strong>1.程序执行时，首先计算表达式的值，与 <code>case</code> 后面的常量表达式值比较，若相等就执行对应部分的语句块，执行完后利用 <code>break</code> 语句跳出 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7782.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7782.html" ref="nofollow noopener noreferrer"><code>switch</code></a> 分支语句。若表达式的值与所有的 <code>case</code> 后的常量表达式均不匹配，则执行 <code>default</code> 项对应的语句 <code>n</code> ，执行后跳出 <code>switch</code> 分支语句。</strong></li>
<li><strong>2.<code>case</code> 后面的常量表达式只能是整型、字符型或枚举型常量的一种；各 <code>case</code> 语句表达式的值各不相同，只起到一个标号作用，用于引导程序找到对应入口。</strong></li>
<li><strong>3.这里的语句块可以是一条语句，或其它复合语句。语句块可以不用花括号<code>&#123;&#125;</code></strong></li>
<li><strong>4.各个 <code>case</code> 语句并不是程序执行的终点，通常需要执行 <code>break</code> 语句来跳出<code>switch</code>分支语句；若某 <code>case</code> 语句的语句块被执行后，若其后没有 <code>break</code> 语句，则顺序执行其它 <code>case</code> 语句，直到遇到 <code>break</code> 语句或后面所有 <code>case</code> 语句全部执行完，再跳出 <code>switch</code> 分支语句。</strong></li>
<li><strong>5. 多个 <code>case</code> 可以共用一组执行语句块。</strong></li>
<li><strong>6.各个 <code>case</code> 和 <code>default</code> 出现的先后次序，并不影响执行结果。</strong></li>
<li><strong>7. <code>default</code> 语句不是必须的，但建议加上作为默认情况处理项。</strong></li>
<li><strong>8.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7782.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7782.html" ref="nofollow noopener noreferrer"><code>switch</code> 语句</a>仅做相等性检测，不能像 <code>if</code> 语句那样做关系表达式或逻辑表达式计算，进行逻辑真假判断。</strong></li>
</ul>
<h2 data-id="heading-1">二.<code>switch</code>语句实战</h2>
<p>举个例子：根据数字判断今天星期几？</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - switch 语句
//@Time:2021/05/31 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include "stdio.h"
#include "windows.h"

int _tmain(int argc, _TCHAR* argv[])
&#123;
int i = 1;

switch (i)
&#123;

case 1:
printf("星期一");
break;

case 2:
printf("星期二");
break;
case 3:
printf("星期三");
break;

case 4:
printf("星期四");
break;

case 5:
printf("星期五");
break;

case 6:
printf("星期六");
break;

case 7:
printf("星期七");
break;


default:
printf("输入错误啦");
break;
&#125;

system("pause");
return 0;
&#125;
/*
输出结果：

星期一
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然你也可以写<code>8</code>个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7466.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7466.html" ref="nofollow noopener noreferrer"><code>if</code> / <code>else</code></a> 完成这个功能，不过这中多分支更加推荐使用通过 <code>switch</code> 完成；</p>
<h2 data-id="heading-2">三.<strong>猜你喜欢</strong></h2>
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
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7782.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7782.html" ref="nofollow noopener noreferrer">C 语言 switch 语句</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            