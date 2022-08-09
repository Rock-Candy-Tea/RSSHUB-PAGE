
---
title: '微软确认Windows 10_11操作系统存在打不开XPS文档的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0809/935c999aefa7012.jpg'
author: cnBeta
comments: false
date: Tue, 09 Aug 2022 08:23:15 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0809/935c999aefa7012.jpg'
---

<div>   
由 Windows Health Dashboard 可知，微软已意识到一个问题 —— <strong>作为 Adobe PDF 的替代品，Windows 10 / 11 操作系统用户似乎很难打开特定的 XPS 文档。</strong>除了无法打开非英语语言的 XPS / OXPS 文档，XPS Viewer 查看器也会停止响应并蚕食 CPU / 内存资源，直至突破 2.5GB RAM 使用率时崩溃。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0809/935c999aefa7012.jpg" referrerpolicy="no-referrer"></p><p>具体说来是，在安装了 KB5014666 或更高版本的更新包后，XPS Viewer 可能无法打开某些非英语语言的 XML Paper Specification 文档（简称 XPS），比如日语和中文字符编码。</p><p>该 bug 影响 XPS 和 OXPS 格式的文件，用户可能在 XPS 查看器中见到“无法显示此页面”的报错、或因程序卡住导致高 CPU / 内存资源占用。</p><p>若用户没有立即结束 XPS 查看器的应用程序进程，它可能会不断不断蚕食系统资源，并在内存占用达到 2.5 GB 时发生崩溃。</p><p><img src="https://static.cnbetacdn.com/article/2022/0809/e8e849129cf0e3f.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：Microsoft <a href="https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h2#2878msgdesc" target="_self">Docs</a>）</p><p>微软证实，问题源于 6 月 26-28 日发布的 KB5014666（<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 19044.1806）和 KB5014666（Windows 11 22000.778）累积更新。</p><p>目前该公司正忙于调查该问题，并承诺在即将发布的新版本中予以修复。遗憾的是，目前尚不清楚有卸载累积更新之外的临时解决方案。</p><p>好消息是，至少大多数 Windows 10 / 11 用户不会被该问题所困扰。毕竟在推出多年后，XPS 格式一直没能成为文档市场的主流选择。</p><p><img src="https://static.cnbetacdn.com/article/2022/0809/0ea0940bff509aa.jpg" referrerpolicy="no-referrer"></p><p>此外从 1803 版本开始，微软就已不再将 Windows 10 和 XPS 查看器捆绑到一起。</p><p>实在有需要的话，你也可以移步至“设置”应用、并手动安装可选的 Windows 组件（<a href="https://allthings.how/how-to-install-xps-viewer-on-windows-11/" target="_self">教程</a>）。</p><p>最后，XPS Viewer 并不是当前微软正在排查的唯一问题。该公司早前证实， 6 月 28 日之后发布的 Windows 更新，可能会导致 USB 打印机出现问题。</p>   
</div>
            