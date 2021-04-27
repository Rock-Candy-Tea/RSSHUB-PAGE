
---
title: 'iOS架构设计系列-项目结构设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cea11482051e4a2aaef38245e11a725f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 17:40:55 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cea11482051e4a2aaef38245e11a725f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一. 项目结构意义</h2>
<ul>
<li>
<p><strong>项目结构是软件项目的门面担当，它不仅是软件功能模块的直观体现，也是项目可维护性、可扩展性的掌舵者。</strong></p>
</li>
<li>
<p><strong>层次清晰的项目结构不仅可以实现模块间解耦，还可以提升新手熟悉项目的效率</strong></p>
</li>
</ul>
<h2 data-id="heading-1">二. 如何设计项目结构</h2>
<p><strong>iOS项目结构设计大致可分为功能模块目录及资源配置文件目录：功能模块目录承载项目具体功能业务，如程序入口、通用工具栏等；资源配置目录存在项目的资源文件，如图片资源、字体库、项目配置文件等。如下图所示</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cea11482051e4a2aaef38245e11a725f~tplv-k3u1fbpfcp-watermark.image" alt="iOS工程目录.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7646c4fb123749e19323a635271069c8~tplv-k3u1fbpfcp-watermark.image" alt="WX20210424-092952@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>对于iOS项目来说，一级目录可以分为Classes和Resources两个文目录：</li>
</ul>
<h3 data-id="heading-2">1. Classes目录</h3>
<ul>
<li>Classes目录下包含：AppDelegate、Application、Networking、Utils、Lib、Business等文件目录如下图</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d84054db604b49d3ac78abd7a3a4f6d0~tplv-k3u1fbpfcp-watermark.image" alt="WX20210424-093029@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/834a15a1746649e3a87c4070bed62067~tplv-k3u1fbpfcp-watermark.image" alt="WX20210424-093106@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>AppDelegate存放程序入口文件</li>
<li>Application存放应用全局管理类（Manager），程序入口加载的TabBarController等</li>
<li>应用全局管理类（Manager）存在项目中通用管理类文件，例如单例等</li>
<li>Business 存放具体功能业务模块文件目录（例如Home，Mine，Login业务模块目录），以及网络业务层文件目录（Networking）等</li>
<li>Home（首页）功能模块目录下存在本功能具体业务文件目录，又可分为View（数据展示者）、Model(数据持有者，存储数据)、ViewModel（数据加工者，获取并加工数据）、Controller（数据协调者）、SubPages（子系统功能业务）等文件目录</li>
<li>ViewModel目录还可以细分为：BNHomeViewModel(数据请求业务)、BNHomeRequestManager（模块网络请求类）、BNHomeSegueManager（模块内部页面跳转类）等文件</li>
<li>Utils存放工具类，如Categories(扩展功能的分类)、EmptyView（缺省页）、Constant(常量，例如通知常量，第三方APPId常量等)等</li>
<li>Lib存放第三方库等</li>
</ul>
<h3 data-id="heading-3">2. Resources目录</h3>
<ul>
<li>Resources目录下包含：Assets、Info.plist、pch等文件及目录如下图</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00d21c11bbf949ce9c97cda27380db94~tplv-k3u1fbpfcp-watermark.image" alt="WX20210424-093132@2x.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            