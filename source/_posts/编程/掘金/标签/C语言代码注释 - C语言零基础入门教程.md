
---
title: 'C语言代码注释 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3051'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 16:25:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=3051'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6990879363558277157#%E6%96%B9%E6%B3%95%E4%B8%80_%E4%BD%BF%E7%94%A8" title="#%E6%96%B9%E6%B3%95%E4%B8%80_%E4%BD%BF%E7%94%A8" target="_blank">方法一:使用//</a></li>
<li><a href="https://juejin.cn/post/6990879363558277157#%E6%96%B9%E6%B3%95%E4%BA%8C_%E4%BD%BF%E7%94%A8" title="#%E6%96%B9%E6%B3%95%E4%BA%8C_%E4%BD%BF%E7%94%A8" target="_blank">方法二:使用/* */</a></li>
<li><a href="https://juejin.cn/post/6990879363558277157#%E6%96%B9%E6%B3%95%E4%B8%89_%E4%BD%BF%E7%94%A8%E5%AE%8F_if_else_end" title="#%E6%96%B9%E6%B3%95%E4%B8%89_%E4%BD%BF%E7%94%A8%E5%AE%8F_if_else_end" target="_blank">方法三:使用宏 #if #else #end</a></li>
<li><a href="https://juejin.cn/post/6990879363558277157#%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<p>注释是为了使别人能看懂你写的程序，也为了使你在若干年后还能看得懂你曾经写的程序而设定的。</p>
<p>注释是写给程序员看的，不是写给电脑看的。所以注释的内容，C 语言编译器在编译时会被自动忽略，不会执行<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7404.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7404.html" ref="nofollow noopener noreferrer">注释的代码</a>！</p>
<h2 data-id="heading-0">方法一:使用//</h2>
<pre><code class="copyable">/************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言代码注释
//@Time:2021/05/21 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/************************************************************************/

#include "stdafx.h"

//main函数 ：程序的入口函数，就好比吃饭一样，饭得重嘴进
//尽是说屁话，不从嘴巴进，难道重屁眼进？？？？
int main(int argc, _TCHAR* argv[])
&#123;
//结束main函数，返回0
return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">方法二:使用/* */</h2>
<pre><code class="copyable">/************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言代码注释
//@Time:2021/05/21 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/************************************************************************/

#include "stdafx.h"

/*
    main函数 ：程序的入口函数，就好比吃饭一样，饭得重嘴进
    尽是说屁话，不从嘴巴进，难道重屁眼进？？？？
*/

int main(int argc, _TCHAR* argv[])
&#123;
/*结束main函数，返回0*/
return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">方法三:使用宏 #if #else #end</h2>
<pre><code class="copyable">/************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言代码注释
//@Time:2021/05/21 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/************************************************************************/

#include "stdafx.h"

//main函数 ：程序的入口函数，就好比吃饭一样，饭得重嘴进
//尽是说屁话，不从嘴巴进，难道重屁眼进？？？？


int main(int argc, _TCHAR* argv[])
&#123;
#if 0
    //结束main函数，返回0
    return 0; //该行代码不会被执行
#else
    //结束main函数，返回1
    return 1;
#endif
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7404.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7404.html" ref="nofollow noopener noreferrer">if #else #end</a> 留到后面的文章在做详细讲解！</p>
<h2 data-id="heading-3">猜你喜欢</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer">安装 Visual Studio</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7280.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7280.html" ref="nofollow noopener noreferrer">安装 Visual Studio 插件 Visual Assist</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7288.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7288.html" ref="nofollow noopener noreferrer">Visual Studio 2008 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7292.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7292.html" ref="nofollow noopener noreferrer">Visual Studio 2003/2015 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7284.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7284.html" ref="nofollow noopener noreferrer">设置 Visual Studio 字体/背景/行号</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7387.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7387.html" ref="nofollow noopener noreferrer">C 语言 Hello World</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7404.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7404.html" ref="nofollow noopener noreferrer">C 语言代码注释</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7404.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7404.html" ref="nofollow noopener noreferrer">C 语言代码注释</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            