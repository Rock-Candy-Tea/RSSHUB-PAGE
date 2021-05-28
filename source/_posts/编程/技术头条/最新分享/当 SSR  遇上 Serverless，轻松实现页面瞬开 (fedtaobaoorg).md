
---
title: '当 SSR  遇上 Serverless，轻松实现页面瞬开 (fed.taobao.org)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=5112'
author: 技术头条
comments: false
date: 2021-05-28 08:33:32
thumbnail: 'https://picsum.photos/400/300?random=5112'
---

<div>   
最近随着 Rax SSR 完成渲染性能 6x React 的提升，以及工程上 Serverless 发布形式的对接，我想是时候跟大家介绍下 Rax SSR 了。

SSR 的全称是 Server Side Rendering，对应的中文名是：服务器端渲染，顾名思义是将渲染的工作放在 Server 端进行。

而与之对应的是 CSR ，客户端渲染，也就是目前 Web 应用中主流的渲染模式，一般由 Server 端返回的初始 HTML 页面，然后再由 JS 去异步加载数据，然后完成页面的渲染。
    
</div>
            