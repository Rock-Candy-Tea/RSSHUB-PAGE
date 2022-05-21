
---
title: '微软 Win11 安卓子系统更新：底层升至 Android 12L，App 提示整合到系统通知'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/38cc2214-d806-4718-9652-f7e5fd6bf02e.png'
author: IT 之家
comments: false
date: Fri, 20 May 2022 22:48:52 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/38cc2214-d806-4718-9652-f7e5fd6bf02e.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D2010825" rel="nofollow">软媒新友2010825</a> 的线索投递！</div>
            <p data-vmark="b4a5"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 21 日消息，微软更新了 Win11 系统上的 WSA（基于 Android 的 Windows 子系统）（版本 2204.40000.15.0），系统版本更新 Android 12.1，也就是 Android 12L。</p><p data-vmark="27ee">得益于此，Android 应用程序现在可以更好地与 Windows 集成，你现在可以在 Windows 任务栏托盘上看到哪些 App 正在使用你的麦克风，以及位置等隐私信息。</p><p data-vmark="0a0f">此外，你还可以看到来自 Android 应用程序的提示（集成到 Windows 通知），而且 Android 应用程序现在也已经支持 Windows 11 的高级网络功能，允许它们连接到你局域网中的其他智能设备 (如摄像头或音箱) 。</p><p data-vmark="1992">IT之家了解到，微软在这一版本中对 WSA 设置进行了重大调整，将类似的设置和选项并入分组以带来更好的体验。</p><p data-vmark="2058">微软还为 WSA 添加了一个诊断数据查看器，其中包含子系统收集的所有数据的信息，并在默认情况下禁用了可选的诊断数据。</p><p data-vmark="2e70">此外，对于较新的 Insider Preview 版本（OS Build 22621+），当您的设备脱离待机状态时，Android 应用程序不会重新启动，而是会从您离开的地方继续（大概是指后台热启动）。</p><p data-vmark="b83c">其他方面，新版本还升级了一些硬件方面的支持，例如 VP8 和 VP9 解码的支持，以及 Chromium 100 的支持；而且相机 App 也得到了一些改进，甚至连输入设备也得到了微软关注，并将带来更好的鼠标滚轮支持，支持 App 大小调整和方向键，还有固定的屏幕键盘以及新键盘外观等等。</p><h3 data-vmark="7ce6">完整的变更日志</h3><ul class=" list-paddingleft-2"><li><p data-vmark="c06a">适用于 Android 的 Windows 子系统已更新至 Android 12.1</p></li><li><p data-vmark="4f60">较新的 x64 Windows 版本默认启用高级网络</p></li><li><p data-vmark="97ae">更新了适用于 Android 设置应用程序的 Windows 子系统：添加了重新设计的 UX 和诊断数据查看器</p></li><li><p data-vmark="ed73">Simpleperf CPU 分析器记录现在适用于 Android 的 Windows 子系统</p></li><li><p data-vmark="4c39">Windows 任务栏现在显示哪些 Android 应用正在使用麦克风和位置</p></li><li><p data-vmark="7778">改进了显示为 Windows 通知的 Android 应用程序通知</p></li><li><p data-vmark="bd36">减少 App 从最小化状态恢复时的闪烁</p></li><li><p data-vmark="e52d">在最近的 Windows 版本中，当设备脱离连接待机状态时，应用程序不会重新启动</p></li><li><p data-vmark="2027">新的视频硬件解码（VP8 和 VP9）</p></li><li><p data-vmark="a6cc">修复了应用程序中的屏幕键盘</p></li><li><p data-vmark="57eb">修复全屏 Android 应用程序和自动隐藏的 Windows 任务栏</p></li><li><p data-vmark="d62f">使用 Chromium WebView 100 更新的适用于 Android 的 Windows 子系统</p></li><li><p data-vmark="1b00">除了 GpsLocationProvider 之外，还添加了对 Android NetworkLocationProvider 的支持</p></li><li><p data-vmark="3faf"><span class="accentTextColor">优化系统流畅度，提高系统稳定性</span>、性能和可靠性</p></li></ul><h2 data-vmark="2c92">已知的问题</h2><ul class="ai-word-checked list-paddingleft-2"><li><p data-vmark="eb26">ARM 设备上的摄像头不稳定</p></li><li><p data-vmark="23ba">通过 Android 应用程序打印不稳定</p></li><li><p data-vmark="ef69">某些以较低分辨率呈现的应用程序可能布局不正确</p></li><li><p data-vmark="1e33">某些 VPN 可能不适用于高级网络。如果您使用 VPN 并发现 Android 应用程序没有网络连接，请在 Windows Subsystem for Android Settings 应用程序中禁用高级网络</p></li><li><p data-vmark="e5cf">某些以前可用的应用程序可能会从体验中丢失、无法启动或因各种已知问题而无法正常运行。我们正在与我们的合作伙伴一起尽快解决这些问题。</p></li></ul><p data-vmark="0f72" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/38cc2214-d806-4718-9652-f7e5fd6bf02e.png" w="1440" h="810" title="微软 Win11 安卓子系统更新：底层升至 Android 12L，App 提示整合到系统通知" width="1440" height="461" referrerpolicy="no-referrer"></p><p data-vmark="b6ee">微软博客原文：<a href="https://blogs.windows.com/windows-insider/2022/05/20/update-to-windows-subsystem-for-android-on-windows-11/" target="_blank">点此</a>。</p>
          
</div>
            