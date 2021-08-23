
---
title: 'C语言 二维数组遍历 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7cc698d37824c4fb6cba38827bfc6ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 17:55:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7cc698d37824c4fb6cba38827bfc6ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6999438298078773255#%E4%B8%80%E8%AE%A1%E7%AE%97%E4%B8%80%E7%BB%B4%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6" title="#%E4%B8%80%E8%AE%A1%E7%AE%97%E4%B8%80%E7%BB%B4%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6" target="_blank">一.计算一维数组长度</a></li>
<li><a href="https://juejin.cn/post/6999438298078773255#%E4%BA%8C%E8%AE%A1%E7%AE%97%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6" title="#%E4%BA%8C%E8%AE%A1%E7%AE%97%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6" target="_blank">二.计算二维数组长度</a>
<ul>
<li><a href="https://juejin.cn/post/6999438298078773255#1%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E8%A1%8C%E6%95%B0" title="#1%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E8%A1%8C%E6%95%B0" target="_blank">1.二维数组行数</a></li>
<li><a href="https://juejin.cn/post/6999438298078773255#2%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E5%88%97%E6%95%B0" title="#2%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E5%88%97%E6%95%B0" target="_blank">2.二维数组列数</a></li>
<li><a href="https://juejin.cn/post/6999438298078773255#3%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E7%9A%84%E5%85%83%E7%B4%A0%E4%B8%AA%E6%95%B0_%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E8%A1%8C%E6%95%B0_%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E5%88%97%E6%95%B0" title="#3%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E7%9A%84%E5%85%83%E7%B4%A0%E4%B8%AA%E6%95%B0_%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E8%A1%8C%E6%95%B0_%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E5%88%97%E6%95%B0" target="_blank">3.二维数组的元素个数 = 二维数组行数 * 二维数组列数</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6999438298078773255#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E4%B8%89%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">三.猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<h2 data-id="heading-0">一.计算一维数组长度</h2>
<p>对于 <code>type array[A]</code>形式的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8159.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8159.html" ref="nofollow noopener noreferrer">数组</a>，可以通过计算 <code>sizeof</code> 函数获取数组长度，举个例子：</p>
<pre><code class="copyable">int len = sizeof(array)/sizeof(array[0]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二.计算二维数组长度</h2>
<p>对于 <code>type array[A][B]</code> 形式的二维数组，可以通过计算 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7851.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7851.html" ref="nofollow noopener noreferrer"><code>sizeof</code> 函数</a>获取二维数组的行数/列数；</p>
<h3 data-id="heading-2">1.二维数组行数</h3>
<pre><code class="copyable">二维数组行数 = sizeof(array)/sizeof(array[0]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.二维数组列数</h3>
<pre><code class="copyable">二维数组列数 = sizeof(array[0])/sizeof(array[0][0]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.二维数组的元素个数 = 二维数组行数 * 二维数组列数</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7cc698d37824c4fb6cba38827bfc6ea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8338.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8338.html" ref="nofollow noopener noreferrer">二维数组</a>，我们可以通过前面介绍的原理来<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8343.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8343.html" ref="nofollow noopener noreferrer">计算二维数组的行数和列数</a>，并<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8346.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8346.html" ref="nofollow noopener noreferrer">遍历二维数组</a>，示例代码如下：</p>
<pre><code class="copyable">/******************************************************************************************/
//@Author:猿说编程
//@Blog(个人博客地址): www.codersrc.com
//@File:C语言教程 - 二维数组遍历
//@Time:2021/06/12 08:00
//@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
/******************************************************************************************/

#include<stdlib.h>
#include<stdio.h>
void main()
&#123;
    int rows = 0;    //行数
    int columns = 0; //列数
    int arr[3][4] = &#123;
            &#123;1,3,5,7&#125;,
            &#123;9,11,13,15&#125;,
            &#123;17,19,21,23&#125;
        &#125;;
    rows = sizeof(arr) / sizeof(arr[0]);
    columns = sizeof(arr[0]) / sizeof(arr[0][0]);
    printf("数组行数：%d  列数：%d  总元素个数：%d * %d = %d \n",rows,columns,rows,columns, rows*columns);
    for (int i = 0;i<rows;i++)
    &#123;
        for (int j = 0;j<columns;j++)
        &#123;
            printf("arr[%d][%d] = %d \n",i,j,arr[i][j] );
        &#125;
        printf("\n");
    &#125;
    system("pause");
&#125;
/*
输出：
数组行数：3  列数：4  总元素个数：3 * 4 = 12
arr[0][0] = 1
arr[0][1] = 3
arr[0][2] = 5
arr[0][3] = 7
arr[1][0] = 9
arr[1][1] = 11
arr[1][2] = 13
arr[1][3] = 15
arr[2][0] = 17
arr[2][1] = 19
arr[2][2] = 21
arr[2][3] = 23
请按任意键继续. . .
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">三.猜你喜欢</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer">安装 Visual Studio</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7280.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7280.html" ref="nofollow noopener noreferrer">安装 Visual Studio 插件 Visual Assist</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7288.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7288.html" ref="nofollow noopener noreferrer">Visual Studio 2008 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7292.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7292.html" ref="nofollow noopener noreferrer">Visual Studio 2003/2015 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7460.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7460.html" ref="nofollow noopener noreferrer">C 语言格式控制符/占位符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7548.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7548.html" ref="nofollow noopener noreferrer">C 语言逻辑运算符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7558.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7558.html" ref="nofollow noopener noreferrer">C 语言三目运算符</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7577.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7577.html" ref="nofollow noopener noreferrer">C 语言逗号表达式</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7865.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7865.html" ref="nofollow noopener noreferrer">C 语言 sizeof 和 strlen 函数区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7945.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7945.html" ref="nofollow noopener noreferrer">C 语言 strcpy 和 strcpy_s 函数区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7973.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7973.html" ref="nofollow noopener noreferrer">C 语言 memcpy 和 memcpy_s 区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8159.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8159.html" ref="nofollow noopener noreferrer">C 语言 数组定义和使用</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8186.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8186.html" ref="nofollow noopener noreferrer">C 语言 数组遍历</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8204.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8204.html" ref="nofollow noopener noreferrer">C 语言 数组排序 – 冒泡法排序</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8221.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8221.html" ref="nofollow noopener noreferrer">C 语言 数组排序 – 选择法排序</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8230.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8230.html" ref="nofollow noopener noreferrer">C 语言 数组排序 – 插入法排序</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8239.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8239.html" ref="nofollow noopener noreferrer">C 语言 数组排序 – 快速法排序</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8257.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8257.html" ref="nofollow noopener noreferrer">C 语言 数组下标越界</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8270.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8270.html" ref="nofollow noopener noreferrer">C 语言 数组内存溢出</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8331.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8331.html" ref="nofollow noopener noreferrer">C 语言 数组下标越界和内存溢出区别</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8334.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8334.html" ref="nofollow noopener noreferrer">C 语言 数组长度计算</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8349.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8349.html" ref="nofollow noopener noreferrer">C 语言 指针声明和定义</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8346.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8346.html" ref="nofollow noopener noreferrer">C 语言 二维数组遍历</a></li>
</ol>
<p>未经允许不得转载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com" ref="nofollow noopener noreferrer">猿说编程</a> » <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F8346.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/8346.html" ref="nofollow noopener noreferrer">C 语言 二维数组遍历</a></p>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            