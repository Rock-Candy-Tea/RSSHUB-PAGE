
---
title: 'CKEditor 5 v33.0.0 发布，改进 conversion_reconversion 系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9dcbe35c9f397ede38b59c828daa0ffcc57.png'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 07:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9dcbe35c9f397ede38b59c828daa0ffcc57.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CKEditor 5 v33.0.0 已发布。更新内容包括：引入了改进和扩展的 conversion/reconversion 系统、修订历史功能现在与实时协作编辑兼容，并且协作功能支持在 DLL 构建中使用。另外，通用 HTML 支持功能也有所改进，还修复了几个重要的错误。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9dcbe35c9f397ede38b59c828daa0ffcc57.png" referrerpolicy="no-referrer"></p> 
<p><strong>改进的 conversion/reconversion 系统</strong></p> 
<p>CKEditor 5 编辑引擎的底层架构包括：模型和视图。conversion/reconversion 指的是两者之间的数据转换。由于更改了一些核心机制的大型清理工作，conversion 机制刚刚获得了重大、广泛的升级。最重要的是，<code>triggerBy</code>选项被替换为用于无缝重新 reconversion 的新 API，引入了新的向下转换助手，并对 conversion API 应用了一些更改。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0e4e43e0b2d8f0e8b9b0fcbe4039bd07434.png" referrerpolicy="no-referrer"></p> 
<p><strong>支持<code><style></code>标签</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fdocs%2Fckeditor5%2Flatest%2Ffeatures%2Fgeneral-html-support.html" target="_blank">通用 HTML 支持 (GHS) 功能</a>是一个特殊插件，支持将现有的专用 CKEditor 5 插件不支持的 HTML 元素引入到内容中。这些内容包括标签<code><span></code>，<code><iframe></code>或<code><cite></code>或标签属性，如<code>id</code>或类。CKEditor v33.0.0 版本扩展了 GHS 可用<code><style></code>标签支持的元素池。它用于提供指定元素的 CSS 信息。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Fckeditor-5-v33.0.0-with-improved-conversion-system-and-dll-builds-for-collaboration-features%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            