
---
title: '_技巧_如何为Windows 11 Build 25136文件资源管理器开启选项卡'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0611/07d194ff1abe035.jpg'
author: cnBeta
comments: false
date: Sat, 11 Jun 2022 07:30:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0611/07d194ff1abe035.jpg'
---

<div>   
<strong>微软在今年早些时候预告了 Windows 11 文件资源管理器的选项卡功能，但我们还等待了许久，才迎来首个公开预览版本。</strong>随着 Build 25136 被推向开发通道，Insider 测试者们已经能够抢先体验。不过在限量预览期间，运气不佳的测试者仍需借助流行的 Vivotool 应用程序来启用。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0611/07d194ff1abe035.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.neowin.net/news/guide-how-to-enable-tabs-in-file-explorer-in-windows-11-build-25136/" target="_self">Neowin</a>）</p><p>在启用 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 的选项卡式文件资源管理器功能前，你需要先将计算机更新到 Dev 频道 Build 25136 编译版本。</p><p>尽管早期预览版本也有一个隐藏设置项，但现在它已不再起作用。此外就算在 Build 2516 中强行开启，你也需要对潜在的 Bug 和功能不稳定做好心理准备。</p><p>基于此，我们并不建议大家在生产主机上安装 Dev 通道的 Windows 11 预览。</p><p><img src="https://static.cnbetacdn.com/article/2022/0611/7e785346725bc91.png" alt="2-0.png" referrerpolicy="no-referrer"></p><p><strong>以下是 Vivetool 的使用方法：</strong></p><blockquote><p>（1）从 GitHub 存储库下载 Vivetool，然后在指定文件提取路径。</p><p>（2）使用 WinKey + R 组合键，唤出 运行 窗口。</p><p>（3）通过 Ctrl + Shift + Enter 组合键，以管理员身份运行 cmd 命令提示符。</p><p>（4）使用 CD 命令进入 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://vivo.jd.com/" target="_blank">vivo</a>tool 文件路径，比如 CD C:\Vivetool 并回车。</p><p>（5）键入 <strong>vivetool addconfig 37634385 2</strong> 命令，并按回车键确认执行。</p><p>（6）重启计算机，以应用更改。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0611/4293f61867f8a2f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0611/4293f61867f8a2f.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p>重启计算机后，你便能够在文件资源管理器（Explorer.exe）中查看选项卡式界面。</p><p>不过需要注意的是，这项配置只能和 Windows 11 重新设计的导航窗格“二选一”。</p><p>如需在 Build 25136 中禁用文件资源管理器的选项卡功能，请参考如上过程、并在第 5步执行 <strong>delconfig 37634385</strong> 命令。</p>   
</div>
            