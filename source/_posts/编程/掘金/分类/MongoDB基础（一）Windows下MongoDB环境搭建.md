
---
title: 'MongoDB基础（一）Windows下MongoDB环境搭建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb4fb4daf7234ec7a9743a9e0f41a8df~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 23:27:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb4fb4daf7234ec7a9743a9e0f41a8df~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<ul>
<li>由于工作和项目需求，需要掌握基础的MongoDB使用方法，我将自己的学习过程一一记录下来，希望能够对读者有所帮助。</li>
</ul>
<h1 data-id="heading-1">1 MongoDB的基本概念</h1>
<p>MongoDB 是由C++语言编写的，基于分布式文件存储的开源NoSQL数据库系统。</p>
<ul>
<li>NoSQL指的是非关系型的数据库，与之对应的是关系型数据库RDBMS（SQL），两者在储存形式上不同，SQL通常以表的形式存储数据（结构化数据），NoSQL则以键值的形式存储数据（非结构化数据）。</li>
</ul>
<p>MongoDB是最接近SQL的NoSQL数据库，因此在学习MongoDB时，可以与SQL进行对比，以加深理解。</p>
<ul>
<li>MongoDB中的集合可以理解为SQL中的表。</li>
<li>MongoDB中的文档可以理解为SQL中表的每一行，数据结构由键值对组成，类似于JSON对象。</li>
</ul>
<h1 data-id="heading-2">2 MongoDB下载安装</h1>
<h2 data-id="heading-3">2.1 MongoDB下载</h2>
<p>可以到MongoDB官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mongodb.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mongodb.com" ref="nofollow noopener noreferrer">www.mongodb.com</a> 下载Community version，我下载的是MongoDB 4.4.6(64bit)版本。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb4fb4daf7234ec7a9743a9e0f41a8df~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 133811.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2.2 MongoDB安装</h2>
<p>安装过程比较简单，基本一直点next，最后install就行，安装过程中有两点需要注意：</p>
<ol>
<li>选择Custom可以自定义安装，同时可以选择安装路径，安装路径最好全英文，否则可能会出问题，我这里选择Complete安装在默认路径。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c2811e357674b37b42bab1187afcd13~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 134926.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>勾选Install MongoDB Compass会安装图形化界面，但是安装速度巨慢，建议去掉勾选</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43c7e071ee454affb79f080b4002ada9~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 135914.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">3 MongoDB基本配置</h1>
<p>较新版本的MongoDB好像不需要像其他帖子中绕来绕去的操作就可以顺利配置和使用，对于初学者更加友好了，只需几个小步骤：</p>
<ol>
<li>设置环境变量，我的是默认安装路径，如果是自定义安装路径，则需要修改成自己的路径。</li>
</ol>
<p><code>C:\Program Files\MongoDB\Server\4.4\bin</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d61fd98ce544d59a87976180af75110~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 141443.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>然后win+R，输入cmd，打开命令提示符，输入<code>mongo</code>，若弹出如下界面，那恭喜你成功进入数据库啦。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b769bc9a724b4c07829f87a8cfc7b54b~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 143446.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>输入<code>show dbs</code> 可以查看所有的数据库，输入<code>exit</code> 则可以退出数据库。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bb8f3488375400a912bae02499c3c61~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 144804.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>以管理员身份运行cmd，输入以下指令可以开启/关闭mongoDB服务。</li>
</ol>
<p>开启mongoDB服务： <code>net start mongodb</code><br>
关闭mongoDB服务： <code>net stop mongodb</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba5543aecfe54f11b997816bb50a06ed~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 145241.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">4 使用Navicat查看MongDB数据库</h1>
<ol>
<li>首先需要安装Navicat Premium,安装和破解过程很多帖子上都有，就自行搞定叭~</li>
<li>在Navicat中新建连接：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/042f220261af4295a5fbea35cb177efe~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 150629.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>编辑连接：连接到本地数据库只要设置连接名就搞定了，其他都默认即可，连接远程的数据库则需要视情况填写。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889e29246c794e58852a95325c0bc108~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-10 150325.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>设置完成后就可以在Navicat上连接本地的MongoDB数据库，愉快地开始学习了~</li>
</ol></div>  
</div>
            