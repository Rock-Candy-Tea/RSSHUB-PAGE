
---
title: 'Chrome 94 开发者工具新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/747d0737a71b466cb65e374c925a0410~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 22:29:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/747d0737a71b466cb65e374c925a0410~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>参考源:</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Fnew-in-devtools-94%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/blog/new-in-devtools-94/" ref="nofollow noopener noreferrer">What's New In DevTools (Chrome 94)</a></p>
<p>⚠️ 新特性都是先在 Chrome 的 Canary 通道中发布的，要想体验本文提到的新特性，请下载 Canary 通道版本的 Chrome。本文中的所有链接都需要自备梯子。</p>
<h3 data-id="heading-0">新特性一： 操作界面开始支持多种语言</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/747d0737a71b466cb65e374c925a0410~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">新特性二：设备模式列表新增 Nest Hub 和 Nest Hub Max 两款设备</h3>
<p>Nest Hub 是谷歌生产的一款智能家居设备，产品图如下：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37514db889364c2c84750f4f93027f41~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
在打开开发者工具后，进入响应式显示模式，即可在设备列表中找到这两款设备：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fdf5553c50a41a480126af597774ad8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">新特性三：Application 面板支持显示 Frame 部署了的 Origin trial</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d995723154c74c55b83cb0a6909b9423~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">新特性四：CSS 容器查询元素上新增一个徽标</h3>
<p>在 Elements 面板中，作为容器查询的容器元素（即应用了 @container 规则的元素），现在会显示一个“Container”徽标，选中后该元素在页面上会用边线把它标示出来<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b6d354a80634a29b76bbc4b6623e04b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">新特性五： Network 面板的筛选支持一键反向筛选</h3>
<p>通过下图中新增了的 Invert （反向）复选框即可实现反向筛选。下图中原本筛是状态码为 404 的请求，选中 Invert 后，就变成了筛选不是 404 的请求。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6cf29f98cfa4716a5e9e2dfaad7fa84~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">新特性六：Console 的侧边栏新增侧边栏即将移除的告示</h3>
<p>如下图。Chrome 开发者工具准备将 Console 的侧边栏转移到工具栏，所以在这个版本中事先贴下告示。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53434408f13441e1b0d567d96a253d84~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">新特性七：Issues 标签和 Network 面板支持显示错误的 Set-Cookie 头</h3>
<p>在之前，如果 Set-Cookie 响应头的值设置不正确时（例如设置了 SameSite 属性，但没有设置 Secure 标识：<code>Set-Cookie: cookie_name=value; SameSite=Lax</code>），Network 面板是不会将其展示出来的。现在借助 response-header-set-cookie 筛选条件，可以对错误的 Set-Cookie 做筛选。另外，在 Issues 标签中，现在也会给出具体的错误的 Set-Cookie，点击还可以跳转到具体的请求。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a31bb3b41bcf483c84f9887f1f672cc4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">新特性八：Console 打印对象时，对计算属性也会进行求值显示</h3>
<p>在这之前，属性如果是计算属性，即 getter (如 <code>Object.defineProperty(obj, prop, &#123; get() &#123;...&#125; &#125;)</code>)，默认是不会进行求值展示的，而是显示 <code>(...)</code>, 需要点击之后才会显示</p>
<p>左边是之前的效果，右边是新版本的效果<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9245830412b74cc894430cf3948bca03~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">新特性九：内联脚本报错信息支持以 SourceMap 为准</h3>
<p>之前，当内联脚本报错时，显示的报错位置是以 html 为准的，现在可以以 source map 为准了：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3c645dbd43b4398a82b7bfc1b91b094~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">新特性十：CSS 的计算属性面板中的颜色值也开始支持切换显示格式</h3>
<p>通过按住 Shift 键点击颜色值，即可切换显示格式，如（RGB 到 HSL）<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/648b55345ea74e61ac62c29322a0f7bb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>往期文档</strong><br>
Chrome 93 开发者工具新特性<br>
待更新<br>
Chrome 更新日志目录<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmubu.com%2Fdoc%2FAObcWURc20" target="_blank" rel="nofollow noopener noreferrer" title="https://mubu.com/doc/AObcWURc20" ref="nofollow noopener noreferrer">mubu.com/doc/AObcWUR…</a><br>
<strong>其他说明</strong><br>
本文同时发布与于<br>
幕布平台：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mubucm.com%2Fdoc%2F2gonWxcpXt" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mubucm.com/doc/2gonWxcpXt" ref="nofollow noopener noreferrer">www.mubucm.com/doc/2gonWxc…</a><br>
掘金平台：<a href="https://juejin.cn/post/7001735350217359390/" target="_blank" title="https://juejin.cn/post/7001735350217359390/">juejin.cn/post/700173…</a><br>
作者：西楼听雨（微信 tt-far）</p></div>  
</div>
            