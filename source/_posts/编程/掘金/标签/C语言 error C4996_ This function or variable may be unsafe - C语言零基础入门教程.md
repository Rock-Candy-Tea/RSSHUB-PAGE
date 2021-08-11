
---
title: 'C语言 error C4996_ This function or variable may be unsafe - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6821'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 17:50:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=6821'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6994983844029939725#%E4%B8%80error_C4996_%E7%AE%80%E4%BB%8B" title="#%E4%B8%80error_C4996_%E7%AE%80%E4%BB%8B" target="_blank">一.error C4996 简介</a></li>
<li><a href="https://juejin.cn/post/6994983844029939725#%E4%BA%8Cerror_C4996_%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95" title="#%E4%BA%8Cerror_C4996_%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95" target="_blank">二.error C4996 解决办法</a>
<ul>
<li><a href="https://juejin.cn/post/6994983844029939725#1%E9%87%87%E7%94%A8_s%E7%BB%93%E5%B0%BE%E7%9A%84%E5%AE%89%E5%85%A8%E7%89%88%E6%9C%AC" title="#1%E9%87%87%E7%94%A8_s%E7%BB%93%E5%B0%BE%E7%9A%84%E5%AE%89%E5%85%A8%E7%89%88%E6%9C%AC" target="_blank">1.采用_s 结尾的安全版本</a></li>
<li><a href="https://juejin.cn/post/6994983844029939725#2%E5%8E%BB%E6%8E%89_visual_studio_%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9FSDL%E6%A3%80%E6%9F%A5" title="#2%E5%8E%BB%E6%8E%89_visual_studio_%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9FSDL%E6%A3%80%E6%9F%A5" target="_blank">2.去掉 visual studio “安全开发生命周期(SDL)检查”</a></li>
<li><a href="https://juejin.cn/post/6994983844029939725#3pragma_warning_disable_4996" title="#3pragma_warning_disable_4996" target="_blank">3.#pragma warning( disable : 4996)</a></li>
<li><a href="https://juejin.cn/post/6994983844029939725#4_CRT_SECURE_NO_WARNINGS" title="#4_CRT_SECURE_NO_WARNINGS" target="_blank">4._CRT_SECURE_NO_WARNINGS</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6994983844029939725#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">三.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.error C4996 简介</h2>
<pre><code class="copyable">error C4996: 'fopen': This function or variable may be unsafe. Consider using fopen_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>正常调用 <code>fopen</code> / <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8005.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8005.html" ref="nofollow noopener noreferrer">memcpy</a> / <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7891.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7891.html" ref="nofollow noopener noreferrer">strcpy</a> 等函数<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8057.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8057.html" ref="nofollow noopener noreferrer">报错 error C4996</a>，是因为许多函数、 成员函数，模板函数和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer"><code>Visual Studio</code></a> 中的库中的全局变量标记为弃 用</strong>。 这些函数被弃用，因为它们可能具有不同的首选的名称，可能不安全或具有更加安全的变体，或可能已过时。 许多弃用消息包括不推荐使用的函数或全局变量的建议的替换。</p>
<h2 data-id="heading-1">二.error C4996 解决办法</h2>
<h3 data-id="heading-2">1.采用_s 结尾的安全版本</h3>
<p>将上面的 <code>fopen</code> 函数改为 <code>fopen_s</code> 函数，例如：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 error C4996:  This function or variable may be unsafe
//@Time:2021/06/03 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include "windows.h"
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
&#123;
    //FILE* fp = fopen("d:/12345633.txt", "r"); //error c4996
    FILE* fp = NULL;
    fopen_s(&fp, "d:/12345633.txt", "r"); // ok版本
    if (fp)
    &#123;
        printf("打开文件成功  \n");
        fclose(fp);
    &#125;
    else
        printf("打开文件失败，失败错误号：%d  \n",GetLastError());
    system("pause");
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.去掉 visual studio “安全开发生命周期(SDL)检查”</h3>
<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-CT05UKpd-1628646342860)(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fwp-content%2Fuploads%2F2021%2F06%2Fc81e728d9d4c2f6.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/wp-content/uploads/2021/06/c81e728d9d4c2f6.png" ref="nofollow noopener noreferrer">www.codersrc.com/wp-content/…</a> “C 语言 error C4996: This function or variable may be unsafe-猿说编程”)]</p>
<h3 data-id="heading-4">3.#pragma warning( disable : 4996)</h3>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - C语言 error C4996:  This function or variable may be unsafe
//@Time:2021/06/03 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include "windows.h"
using namespace std;
#pragma warning( disable : 4996)
int _tmain(int argc, _TCHAR* argv[])
&#123;
    FILE* fp = fopen("d:/12345633.txt", "r");
    if (fp)
    &#123;
        printf("打开文件成功  \n");
        fclose(fp);
    &#125;
    else
        printf("打开文件失败，失败错误号：%d  \n",GetLastError());
    system("pause");
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4._CRT_SECURE_NO_WARNINGS</h3>
<p>项目 =》属性 =》<code>c/c++</code> =》预处理器=》点击预处理器定义，编辑，加入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8057.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8057.html" ref="nofollow noopener noreferrer"><code>_CRT_SECURE_NO_WARNINGS</code></a>，如下图：</p>
<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-NMo8zwGU-1628646342862)(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fwp-content%2Fuploads%2F2021%2F06%2Fc4ca4238a0b9238.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/wp-content/uploads/2021/06/c4ca4238a0b9238.png" ref="nofollow noopener noreferrer">www.codersrc.com/wp-content/…</a> “C 语言 error C4996: This function or variable may be unsafe-猿说编程”)]</p>
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
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8016.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8016.html" ref="nofollow noopener noreferrer">C 语言 memcpy_s 函数</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8057.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8057.html" ref="nofollow noopener noreferrer">C 语言 error C4996: This function or variable may be unsafe</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8057.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8057.html" ref="nofollow noopener noreferrer">C 语言 error C4996: This function or variable may be unsafe</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            