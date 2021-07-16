
---
title: 'Flutter的框架开发与iOS 的学习结构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e45b722eef7143c18bdabe6734fe1cd2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:38:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e45b722eef7143c18bdabe6734fe1cd2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>项目开发</strong></p>
<p>这个框架旨在将常规的<strong>Flutter</strong>项目中使用到的通用《<strong>与业务无关》的功能从剥离出来</strong>，形成<strong>Flutter</strong>开发项目的框架，在开发新的<strong>Flutter</strong>项目时，可以直接引用本项目 ****import 'package:framework/framework.dart'<strong>来使用框架中相关的功能，提升开发效率</strong>。<strong>github项目地址</strong></p>
<p>适配测试、自定义此框架目前包含以下功能模块：接口请求API模块、消息提示模块、路由模块、统一错误处理、日志模块、屏幕义UI组件库、本地存储模块构成</p>
<p>*<strong>接下来是框架的使用</strong></p>
<p>引用与使用</p>
<p><code>jsimport 'package:framework/framework.dart</code></p>
<p><strong>参考Example中使用的例子</strong></p>
<h1 data-id="heading-0"><em>框架首业视图</em></h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e45b722eef7143c18bdabe6734fe1cd2~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-15 142815.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>HTTP的模块</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cd6dc7e0d2e4692a615445bcc7d1870~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-15 143221.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ROUTER的模块</p>
<p>Framework Router模块，它的一个封装库是封装NAVIGATOR库，对上层应用的需要提供不带参数跳转，带参数跳转，以下参考项：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f485a11fee4f56bad6f105fe9b5cc8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>消息提示模块;</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/574201972f9d4379993b23b898f82d22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>错误统一处理</strong> (收集的一张图）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e79362e0639545cd947a35babc97066b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>##为了能补获Flutter的错误还可以有以下处理：</p>
<p>加await
try&#123;
await Flutter.delayed(Duration(seconds:1
final_ = 100-/ 0.</p>
<p>其实学习一种东西需要的是方法，给大家整了这些大概:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc104366657944c2a688baf9a92eac5d~tplv-k3u1fbpfcp-watermark.image" alt="iOS.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/094d2707442345879e2116c54979e4c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天文章就到这里,希望给你们带来帮助，多多关注，后续会有续集哦</p></div>  
</div>
            