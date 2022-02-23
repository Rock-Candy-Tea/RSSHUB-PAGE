
---
title: '_技巧_如何剔除Windows 11_不符系统要求_水印？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0223/1441c7cc09d9872.jpg'
author: cnBeta
comments: false
date: Wed, 23 Feb 2022 09:37:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0223/1441c7cc09d9872.jpg'
---

<div>   
本月早些时候，有爆料称 Windows 11 即将在那些不受支持 PC 上显示“不符系统要求”的通知提醒。<strong>而在近日向 Dev 通道推送的 Build 22557 编译版本中，就有不少尝鲜者发现自己已躺枪。</strong>虽然当前并未对用户体验造成显著的影响，但若你看这水印着实碍眼，那不妨参考下 DeskModder 分享的清理小技巧。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0223/1441c7cc09d9872.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图 via <a href="https://www.neowin.net/news/want-to-remove-the-windows-11-system-requirements-not-met-watermark-here039s-how/" target="_self" textvalue="Neowin">Neowin</a>）</p><p>与往常一样，DeskModder 给出的建议是 ——“遇事不决”就可以找注册表编辑器。</p><p>在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 Build 22557 编译版本中，你只需在注册表中对设置项展开轻微的修改。</p><p>不过在操作之前，还是建议大家不要在生产设备上这么做、同时做好注册表和系统 / 个人数据备份，任何风险都请自担。</p><p><a href="https://static.cnbetacdn.com/article/2022/0223/477d735970dc696.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0223/477d735970dc696.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自： <a href="https://www.deskmodder.de/blog/2022/02/22/windows-11-systemanforderungen-werden-nicht-erfuellt-in-den-einstellungen-und-wasserzeichen-einfach-entfernen/" target="_self">DeskModder</a>）</p><p>首先，使用 WinKey + R 组合键召唤“运行”窗口（或在任务栏搜索框中），输入“regedit”以打开注册表编辑器。</p><p>其次，转到“HKEY_CURRENT_USER\Control Panel\UnsupportedHardwareNotificationCache”分支。</p><p>接着将 SV2 的 DWORD 值从“1”改为“0”，然后保存并刷新。</p><p><a href="https://static.cnbetacdn.com/article/2022/0223/aaf49b3191bbdfc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0223/aaf49b3191bbdfc.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>如果没有找到“UnsupportedHardwareNotificationCache”，也可参考如下方法来创建条目：</p><blockquote><p>● 在注册表编辑器的文件夹（路径图标）上点击鼠标右键（或点击工具栏上的“编辑”）；</p><p>● 选择 新建 → 项目，并将其命名为“UnsupportedHardwareNotificationCache”；</p><p>● 在此文件夹中添加 SV2 的 DWORD 子键；</p><p>● 将其 DWORD 值从“1”修改为“0”；</p><p>● 最后保存并刷新。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0223/1c9cc8b13e4ed8e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0223/1c9cc8b13e4ed8e.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p>如果一切顺利，你应该在刷新后就不再看到 Windows 11 的“系统不符要求”水印和设置通知。</p>   
</div>
            