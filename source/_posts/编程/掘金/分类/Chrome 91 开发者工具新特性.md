
---
title: 'Chrome 91 开发者工具新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36406a67d17d4e24ab8e25dcb66f627a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 22:52:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36406a67d17d4e24ab8e25dcb66f627a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">说明</h3>
<p>1. 点击每个节点左侧的加号可展开该节点下的详情<br>
2. 点击每个节点左侧的实心圆可沉浸到该节点中<br>
[1] What's New In DevTools (Chrome 91)<br>
<a href="https://developer.chrome.com/blog/new-in-devtools-91/#web-vitals" target="_blank" rel="nofollow noopener noreferrer">developer.chrome.com/blog/new-in…</a><br>
新特性都是先在 Chrome 的 Canary、Beta 通道中发布的，要想第一时间体验新特性，请下载 Canary 或 Beta 通道版本的 Chrome。本文中的所有链接都需要自备梯子。</p>
<h3 data-id="heading-1">新特性一：性能标签中 Web Vitals 时间线上的标记光标悬停会气泡显示详情</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36406a67d17d4e24ab8e25dcb66f627a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">新特性二：支持可视化 css 的 scroll-snap 属性</h3>
<p>在 Elements 面板中，设置了 scroll-snap-type 属性的元素上会显示一个 scroll-snap 徽标，点击即可查看<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaa11ab14ca249149328fe426b868100~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">新特性三： 新增 ArrayBuffer 和 wasm 内存查看器</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5973df8e8bb84ab285cf2b0609d51b8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
关于这个工具的使用，可查看 Inspect JavaScript ArrayBuffer with the Memory inspector. <a href="https://developer.chrome.com/docs/devtools/memory-inspector/" target="_blank" rel="nofollow noopener noreferrer">developer.chrome.com/docs/devtoo…</a></p>
<h3 data-id="heading-4">新特性四： Elements 面板中的徽标显示支持手动设置</h3>
<p>在 Elements 面板中，选择任意 DOM 节点右击，选择 Badge Settings 即可设置<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c26b55c6494348baaba3a6f6166726~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">新特性五： 图片语言气泡的信息更详细了</h3>
<p>如下图<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7dcd4f13cbe418c94ebed577098f14b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b9a415f9f3415fb01b316f6d4ef957~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">新特性六：Network 面板新增网络环境控制项</h3>
<p>点击网络图标，可以看到新增了一个 Accepted Content-Encodings 选择，可以用于测试不支持某项时的效果<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/854a53c7fa694a9cacaf601cab35906a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">新特性七：Styles 面板相关的完善</h3>
<p>1. 新增快捷方式查看光标下 css 属性的 computed value<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeb81f66463840b1a732b82dd1ec56b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
2. 新增 accent-color 属性补全<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a7b910565124a0f9bf9c6c7334f9f45~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">新特性八：分类化的 issues</h3>
<p>如下图，红色图标表示页面级错误，如 CORS 异常；黄色图标表示后续版本兼容性警告；蓝色图标表示存在优化的可能性。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a20c4bbb6ad4685841da04a6fe20895~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">新特性九：Application 新增 Trust Token 删除按钮</h3>
<p>关于 Trust Token, 可查看 <a href="https://web.dev/trust-tokens/" target="_blank" rel="nofollow noopener noreferrer">get started with Trust Tokens</a><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aaab55711f043ae8b54bc7b69eba6c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">新特性十：查看受 Permission 政策所影响的特性</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70ef5badb30b471d82330c1d1fc3e1c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">往期文档</h3>
<p>Chrome 90 开发者工具新特性<br>
<a href="https://share.mubu.com/doc/3vOaXg9qQ1" target="_blank" rel="nofollow noopener noreferrer">share.mubu.com/doc/4fYPxZF…</a><br>
Chrome 更新日志目录<br>
<a href="https://mubu.com/doc/AObcWURc20" target="_blank" rel="nofollow noopener noreferrer">mubu.com/doc/AObcWUR…</a></p>
<h3 data-id="heading-12">其他说明</h3>
<p>本文同时发布与于<br>
幕布平台：<a href="https://share.mubu.com/doc/12DAtdu5ft" target="_blank" rel="nofollow noopener noreferrer">share.mubu.com/doc/12DAtdu…</a><br>
掘金平台：<a href="https://juejin.cn/post/6957206118368018468/" target="_blank">juejin.cn/post/695720…</a><br>
作者：西楼听雨（微信名 t.t.）联系 & 交流 & 聘用</p></div>  
</div>
            