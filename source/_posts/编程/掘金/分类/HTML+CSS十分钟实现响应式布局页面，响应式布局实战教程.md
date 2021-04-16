
---
title: 'HTML+CSS十分钟实现响应式布局页面，响应式布局实战教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6f57dfbec24f5faa92aba61fa8c7ce~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:21:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6f57dfbec24f5faa92aba61fa8c7ce~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="20210117163335400.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6f57dfbec24f5faa92aba61fa8c7ce~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">1 什么是响应式布局？</h2>
<p> 响应式布局指的是同一页面在不同屏幕尺寸下有不同的布局。在移动互联网高度发达的今天，我们在桌面浏览器上开发的网页已经无法满足在移动设备上查看的需求。传统的开发方式是PC端开发一套页面，手机端再开发一套页面。但是这样做非常麻烦，随着不同的终端越来越多，你需要开发多个不同版本的页面。而使用响应式布局只要开发一套就够了。EthanMarcotte在2010年5月份提出了响应式布局的概念，简而言之，就是一个网站能够兼容多个终端。
————————————————
版权声明：本文为CSDN博主「Albert Yang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：<a href="https://blog.csdn.net/qq_23853743/article/details/112751229" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/qq_23853743…</a></p>
<p>响应式开发与移动端与PC端分别开发的区别：响应式开发只编写一套界面，通过检测视口分辨率，针对不同客户端在客户端做代码处理，来展现不同的布局和内容。移动端与PC端分别开发，通过检测视口分辨率，来判断当前访问的设备是pc端、平板、手机， 从而请求服务器，返回不同的页面</p>
<h1 data-id="heading-1">2 响应式开发的原理？</h1>
<p>响应式开发的原理是使用CSS3中的Media Query（媒体查询）针对不同宽度的设备设置不同的布局和样式，从而适配不同的设备。</p>
<p>CSS3 @media 查询定义和使用:</p>
<p>使用 @media 查询，你可以针对不同的媒体类型定义不同的样式。@media 可以针对不同的屏幕尺寸设置不同的样式，特别是如果你需要设置设计响应式的页面，@media 是非常有用的。当你重置浏览器大小的过程中，页面也会根据浏览器的宽度和高度重新渲染页面。</p>
<p>例如屏幕宽度小于 500 像素则修改背景颜色(background-color)为红色。
————————————————</p>
<pre><code class="copyable">@media screen and (max-width: 300px) &#123;
    body &#123;
        background-color: red;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设备的划分情况为：</p>
<p>小于768的为超小屏幕（手机）</p>
<p>768~992之间的为小屏设备（平板）</p>
<p>992~1200的中等屏幕（桌面显示器）</p>
<p>大于1200的宽屏设备（大桌面显示器）</p>
<p>但是我们也可以根据实际情况自己定义划分情况。</p>
<h1 data-id="heading-2">3 响应式页面开发实战</h1>
<h1 data-id="heading-3">3.1 视频</h1>
<p>视频地址：<a href="https://www.bilibili.com/video/BV1mr4y1T7w5" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV1mr…</a></p>
<h2 data-id="heading-4">3.2 HTML</h2>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>响应式页面入门教程：Albert Yang</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
        integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
</head>
 
<body>
    <header>
        <a href="#" class="logo">AlbertYang</a>
        <ul class="navigation">
            <li><a href="#">首页</a></li>
            <li><a href="#">博客</a></li>
            <li><a href="#">联系我</a></li>
            <li><a href="#">留言板</a></li>
            <li><a href="#">关于我</a></li>
            <li><a href="#">照片墙</a></li>
        </ul>
        <div class="search">
            <input type="text" placeholder="Search">
            <i class="fa fa-search" aria-hidden="true"></i>
        </div>
    </header>
    <div class="banner">
        <div class="content">
            <h2>响应式布局</h2>
            <p>
                响应式布局指的是同一页面在不同屏幕尺寸下有不同的布局。
                传统的开发方式是PC端开发一套，手机端再开发一套，而使用响应式布局只要开发一套就够了。
                响应式设计与自适应设计的区别：响应式开发一套界面，
                通过检测视口分辨率，针对不同客户端在客户端做代码处理，
                来展现不同的布局和内容；自适应需要开发多套界面，
                通过检测视口分辨率，来判断当前访问的设备是pc端、平板、手机，
                从而请求服务层，返回不同的页面。CSS3媒体查询可以让我们针对不同的媒体类型定义不同的样式，
                当重置浏览器窗口大小的过程中，页面也会根据浏览器的宽度和高度重新渲染页面。
            </p>
            <a href="#">阅读全文</a>
        </div>
        
        <img src="1.jpg" class="image">
    </div>
</body>
 
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3.3 CSS</h2>
<pre><code class="copyable">/* 清除浏览器默认边距，
使边框和内边距的值包含在元素的width和height内 */
* &#123;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
&#125;
header &#123;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 100px;
    z-index: 10;
    background: #5b639c;
&#125;
header .logo &#123;
    position: relative;
    font-size: 1.5em;
    color: #fff;
    text-decoration: none;
    font-weight: 600;
&#125;
header .navigation &#123;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    margin: 10px 0;
&#125;
header .navigation li &#123;
    list-style: none;
    margin: 0 20px;
&#125;
header .navigation li a &#123;
    text-decoration: none;
    color: #fff;
    font-weight: 600;
    letter-spacing: 1px;
&#125;
header .navigation li a:hover&#123;
    color: #ffed3b;
&#125;
header .search &#123;
    position: relative;
    width: 300px;
    height: 40px;
&#125;
header .search input &#123;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    color: #fff;
    background: transparent;
    outline: none;
    border: 1px solid #fff;
    border-radius: 5px;
    padding: 0 10px 0 45px;
&#125;
header .search input::placeholder &#123;
    color: #fff;
&#125;
header .search .fa-search &#123;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    left: 10px;
    color: #fff;
    border-right: 1px solid #fff;
    padding-right: 10px;
&#125;
.banner &#123;
    background: #eee;
    padding: 200px 100px 100px;
    min-height: 100vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
&#125;
.banner .content &#123;
    max-width: 1000px;
&#125;
.banner .content h2 &#123;
    font-size: 2.5em;
    color: #333;
    margin-bottom: 20px;
&#125;
.banner .content p &#123;
    font-size: 1em;
    color: #333;
&#125;
.banner .content a &#123;
    display: inline-block;
    background: #434978;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    font-weight: 600;
    margin-top: 20px;
&#125;
.banner .image &#123;
    max-width: 500px;
    margin-left: 50px;
&#125;
/*屏幕宽度小于991px,改变布局和样式*/
@media screen and (max-width:991px) &#123;
    header &#123;
        padding: 10px 20px;
        flex-direction: column;
    &#125;
    .banner &#123;
        padding: 150px 20px 50px;
        flex-direction: column-reverse;
    &#125;
    .banner .image &#123;
        max-width: 80%;
        margin-left: 0;
    &#125;
    .banner .content h2 &#123;
        font-size: 2em;
    &#125;
&#125;
/*屏幕宽度小于600px,改变布局和样式*/
@media screen and (max-width:600px) &#123;
    header .search &#123;
        width: 100%;
    &#125;
    .banner .image &#123;
        margin-top: 30px;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3.4 图片</h2>
<p><img alt="20210117164601758.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66bfd2585f89445e926649601d5f8d22~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">                                      文章来自CSDN博主:@Albert Yang
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            