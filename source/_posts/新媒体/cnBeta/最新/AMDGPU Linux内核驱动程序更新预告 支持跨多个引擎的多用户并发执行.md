
---
title: 'AMDGPU Linux内核驱动程序更新预告 支持跨多个引擎的多用户并发执行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0307/3e6b27e7c6c5001.png'
author: cnBeta
comments: false
date: Mon, 07 Mar 2022 08:05:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0307/3e6b27e7c6c5001.png'
---

<div>   
<strong>Linux 内核驱动程序即将迎来一个 AMDGPU 的新接口，以支持用户空间的分配和在众多引擎中的并发实现。</strong>本周早些时候，长期 AMD 开源 Linux 驱动开发者 Christian König，向该平台的 AMDGPU 直接渲染管理器驱动程序提交了新一批接口补丁。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0307/3e6b27e7c6c5001.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">资料图</p><p>换言之，新驱动将允许 Linux 用户通过 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon 命令流（command stream），同时在不同引擎上添加和编辑 AMDGPU 上的任何工作。</p><blockquote><p>对于需要在多个引擎上提交并发运行工作任务的‘帮派’（gang），其所有成员都可获得相同的隐式、显式和 VM 依赖项。</p><p>但在其它一切准备就绪之前，任何成员都不会抢跑。而最后一项作业任务，则会被认为是‘帮派头目’（通常提交给 GFX 环），并用于指示输出依赖关系。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0307/9797fd1d21c4b94.png" referrerpolicy="no-referrer"></p><p>据悉，直接渲染管理器（Direct Rendering Manager）属于 Linux 内核中的一个子系统，主要负责与现代显卡的 GPU 实现连接。</p><blockquote><p>DRM 最初是作为 X 显示服务器的直接渲染基础设施（Direct Rendering Infrastructure）的内核空间组件而开发，但现在也有被其它图形堆栈选项（比如 Wayland）所使用。</p><p>DRM 有提供一个公开的应用程序接口（API），允许用户空间应用程序调用该 API 向 GPU 发送命令和信息并完成相关操作（比如自定义图形显示的模式设置）。</p></blockquote><p>感兴趣的朋友，可移步至 <a href="https://lists.freedesktop.org/archives/amd-gfx/2022-March/076261.html" target="_self">FreeDesktop.org</a>，以查看 Christian König 分享的更多细节。</p>   
</div>
            