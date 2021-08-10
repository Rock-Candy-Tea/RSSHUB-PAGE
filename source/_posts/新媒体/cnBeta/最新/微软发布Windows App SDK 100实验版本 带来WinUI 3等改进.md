
---
title: '微软发布Windows App SDK 1.0.0实验版本 带来WinUI 3等改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0327/aa30e76f39c56e2.jpg'
author: cnBeta
comments: false
date: Tue, 10 Aug 2021 06:18:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0327/aa30e76f39c56e2.jpg'
---

<div>   
微软刚刚发布了 Windows App SDK 1.0.0-experimental 实验工具包，<strong>旨在帮助桌面应用程序开发者能够高效构建具有现代用户界面（Windows UI）、应用程序接口（API）、以及各项平台功能的软件产品。</strong>随着 1.0.0 版软件开发套件（SDK）的发布，开发者们又迎来了以下特性和改进。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0327/aa30e76f39c56e2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0327/aa30e76f39c56e2.jpg" referrerpolicy="no-referrer"></a></p><p>首先是 WinUI 3，其专注于完善 1.0 稳定版的新功能和 bug 修复：</p><blockquote><p>● 新功能：支持为每个窗口（而不是每个线程）显示一个内容对话框（ContentDialog）。</p><p>● Bug 修复：详见 GitHub 存储库中的完整列表（<a href="https://github.com/microsoft/microsoft-ui-xaml/issues/5651" target="_self">传送门</a>）。</p><p>● 示例：要体验试验中的 WinUI 3 控件和功能，可参阅 GitHub 上的 WinUI 3 应用程序 ，或下载 Microsoft Store 中的相关资源。</p></blockquote><p>其次是推送通知方面的改进（实验性功能），它适用于通过 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>X 打包的 Azure 桌面应用程序，但前提是必须注册<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的封闭预览（以下是主要限制）：</p><blockquote><p>● 仅限 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 2004（build 19041）及更高版本的 MSIX 封装应用；</p><p>● 微软保留在封闭预览期间，禁用或撤回这项通知功能的权利。</p><p>● 微软不不担保推送通知的延迟与可靠性。</p><p>● 封闭预览期间，推送通知量的上限为 100 万条 / 月。</p></blockquote><p>然后是窗口化（同是一项实验性功能），此版本包含了窗口 API 的更新，是一组以 AppWindows 类为中心的高级窗口化 API 。</p><p>其允许开发者轻松地与其它应用程序集成，与通用 Windows 应用类似，但不完全相同。以下是窗口化功能的一些主要限制：<br></p><blockquote><p>● 此版 AppWindow 仅适用于 Win32 应用程序（打包和未打包）。</p><p>● Windows 应用 SDK 暂不支持将 UI 框架内容附加到 AppWindow，开发者只能够使用基于 HWND 的互操作访问方法。</p><p>● 当前 Windowing API 暂不适用于 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>64 的 Windows 版本（1809 和 1903）。</p></blockquote><p>最后是部署未打包的应用程序（也是实验性功能），此版本引入了动态依赖项的功能更新（包括引导程序 API），以下是它的一些主要限制：</p><blockquote><p>● 动态依赖项功能仅支持未打包的应用程序（即不将 MSIX 用于其部署技术的应用程序）。</p><p>● 不支持提升调用。</p></blockquote><p><a href="https://github.com/microsoft/ProjectReunion/issues/921" target="_self">已知问题</a>和其它限制：</p><blockquote><p>● 由于 Windows 应用 SDK 是由本机代码编写的，因而不支持任何 CPU 编译配置<br></p><p>● .NET 应用程序必须设置 18362 或更高版本目标，TFM 必须为 net5.0-windows10.0.18362 及以上。</p></blockquote><p>至于更多细节，还请移步至微软官网（<a href="https://docs.microsoft.com/en-us/windows/apps/windows-app-sdk/experimental-channel#version-10-experimental-100-experimental1" target="_self">传送门 1</a>）或 GitHub 项目主页（<a href="https://github.com/microsoft/WindowsAppSDK/issues/921" target="_self">传送门 2</a>）查看。</p><blockquote><p>下载地址：<a href="https://marketplace.visualstudio.com/items?itemName=ProjectReunion.MicrosoftProjectReunionPreview" target="_self">Version 1.0 Experimental</a> (1.0.0-experimental1) <br></p></blockquote>   
</div>
            