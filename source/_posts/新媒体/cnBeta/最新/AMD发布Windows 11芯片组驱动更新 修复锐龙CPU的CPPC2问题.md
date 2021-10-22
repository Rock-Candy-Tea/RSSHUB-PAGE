
---
title: 'AMD发布Windows 11芯片组驱动更新 修复锐龙CPU的CPPC2问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1022/9760e7bdd2edbe2.png'
author: cnBeta
comments: false
date: Fri, 22 Oct 2021 02:09:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1022/9760e7bdd2edbe2.png'
---

<div>   
<strong>随着 3.10.08.506 芯片组驱动的发布，AMD 终于给锐龙 CPU 打上了运行 Windows 11 操作系统的性能补丁。</strong>此前由于协处理器无法为程序正确调用最佳性能的内核（CPPC 机制），某些多线程优化不佳的应用程序会受到较大的影响。此外 Windows 11 首发时还遇到了锐龙 CPU 的 L3 缓存延迟异常，这点还得看微软的后续补丁优化。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1022/9760e7bdd2edbe2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1022/9760e7bdd2edbe2.png" alt="0.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：AMD <a href="https://www.amd.com/en/support/kb/release-notes/rn-ryzen-chipset-3-10-08-506" target="_self">Release Notes</a>）</p><p>AMD 在芯片组驱动程序的发行说明中写道，该 3.10.08.506 版本已经修复了锐龙处理器在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 Build 22000.189 及以上平台的一个性能问题，恢复了 UEFI CPPC2（首选核心）的预期功能和行为。</p><blockquote><p>具体说来是，新驱动引入了 7.0.3.5 版本的锐龙电源管理计划，其中包含了针对 Windows 11 操作系统的专属优化，以修复 CPPC2 方面的性能调度问题。</p><p>需要注意的是，由于 Windows 11 官方最低指定了 AMD 锐龙 2000 系列（以及<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> 8 代酷睿）CPU，所以新版驱动程序也仅与基于 Zen+（及以上）的 AMD 锐龙 CPU 兼容。</p></blockquote><p>另一方面，新版芯片组驱动程序同样适用于在 Windows 10 操作系统上运行的、所有基于 Zen 架构的锐龙 CPU 。</p><p>与此同时，AMD 顺带修复了一个 OpenGL 报错弹窗问题，并将 UART 驱动程序版本号升级到了 1.2.0.113，以加入对 4Mbps 波特率的支持。</p><p><strong>以下是 AMD 新版芯片组驱动尚未解决的一些已知问题：</strong></p><blockquote><p>· 若使用自定义安装，有时可能无法升级到最新版本的驱动程序。</p><p>· 在俄语系统中，可能遇到文本对齐问题。</p><p>· 安装完成后，非英语操作系统可能需要手动重启。</p><p>· 安装过程中，可能出现 Windows Installer 弹出消息。</p><p>· 在非英语操作系统上，卸载摘要日志时，可能错误地将卸载状态显示为失败。</p><p>· 启动安装程序并点击 UI 屏幕时，或观察到‘AMD 芯片组软件没有响应’的弹窗消息。</p></blockquote><p><strong>AMD 锐龙芯片组驱动程序（3.10.08.506）下载地址：</strong></p><blockquote><p>· <a href="https://drivers.amd.com/drivers/amd_chipset_software_3.10.08.506.exe" target="_self">适用于 Windows 10 / 11 64-bit</a>（51.6 MB）</p></blockquote>   
</div>
            