
---
title: 'RetroArch 1.10.0 发布，跨平台模拟器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4390'
author: 开源中国
comments: false
date: Tue, 25 Jan 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4390'
---

<div>   
<div class="content">
                                                                                            <p>RetroArch 1.10.0 现已发布。RetroArch 是款功能强大的跨平台模拟器，不但能够模拟许多不同的游戏主机，还能在 Windows、MacOS、Linux、Android、iOS 以及多种游戏主机上执行。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul> 
 <li>3DS：添加 Jaxe、A5200 和 WASM4 内核</li> 
 <li>3DS：修复 rotation</li> 
 <li>ARCHIVE：允许从归档子目录加载文件</li> 
 <li>AUDIO：从音频批处理回调中删除帧限制。以前，如果 core 使用音频批处理回调，在可以发送的音频帧数上会有一个 1024 的隐藏上限。如果一个 core 超过了这个值，任何多余的样本都会被默默地丢弃。虽然这对于“正常”采样率/帧率来说已经足够了，但这意味着例如一个 core 使用批处理回调以 30 fps 发送 44100 Hz 音频，声音将会被完全破坏。这已通过删除音频批处理帧限制得到解决。</li> 
 <li>AUDIO/RESAMPLER/NEON：实现 sinc kaiser NEON 功能</li> 
 <li>CHEEVOS：将 hardcore default 重置为启用；尝试在 hardcore 中加载状态时显示消息</li> 
 <li>CHEEVOS：修复内存映射转换</li> 
 <li>CHEEVOS：解锁成就时检查 netplay 状态</li> 
 <li>CHEEVOS：支持散列缓冲 NDS ROM</li> 
 <li>CHEEVOS：修复挂起的任务，徽章不存在</li> 
 <li>CLI：从命令行或播放列表加载保存状态</li> 
 <li>CORE INFO CACHE/SETTINGS：恢复丢失的“Cache Core Info Files”菜单项</li> 
 <li>DATABASE：对 Gamecube/MegaCD/SegaCD/Saturn/PSX/PSP/Dreamcast/Wii 进行串行扫描</li> 
 <li>D3D10/D3D11：添加 Vsync swap interval</li> 
 <li>EMSCRIPTEN：添加 Jaxe、WASM4 内核</li> 
 <li>FILE IO：当内容路径没有前面的斜杠时，修复重映射文件的错误文件名</li> 
 <li>INPUT/OVERLAY：增加了对在菜单后面而不是前面显示 overlay  的支持。目前仅 GL、Vulkan、D3D 9/10/11/12 和 3DS 驱动程序支持此功能。</li> 
 <li>INPUT/UDEV：将 abs 鼠标从屏幕转换为视口坐标；修复相对鼠标坐标</li> 
 <li>INPUT/WAYLAND：添加 scroll wheel 支持</li> 
 <li>LINUX：增加了对 Linux GameMode ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFeralInteractive%2Fgamemode" target="_blank">https://github.com/FeralInteractive/gamemode</a> ) 的支持，可以在电源管理或延迟设置菜单中打开/关闭。</li> 
 <li>LOCALIZATION：从 Crowdin 获取翻译</li> 
 <li>LOCALIZATION：添加印度尼西亚语、瑞典语和乌克兰语选项</li> 
 <li>LOCALIZATION/MENU/RGUI：为 RGUI 启用印度尼西亚语和瑞典语本地化</li> 
 <li>LOGGING：Logging cleanups</li> 
 <li>LOGGING： 停止记录退出时的两次 FPS 统计数据</li> 
 <li>LOGGING：只记录一次字体渲染后端</li> 
 <li>HOTKEYS：为屏幕技术统计添加了热键切换。</li> 
 <li>HOTKEYS：为音量热键添加延迟 + 加速</li> 
 <li>MENU：添加仅在菜单中显示通知的选项</li> 
 <li>MENU/RGUI：将芬兰语添加到支持的语言</li> 
 <li>MENU/XMB：可选的垂直列表项淡入淡出</li> 
 <li>MENU/XMB/OZONE：Category + History/Favorites 图标</li> 
 <li>NETWORK：修复虚拟通知 - 当 netplay 未被启用时，不再显示 netplay 初始化失败的通知。</li> 
 <li>NETWORK：仅用于 UPnP 的 LAN 地址 - 某些路由器设备可能会接受 non-LAN 地址而不会引发错误。</li> 
 <li>UWP/XBOX：添加代码以自动设置权限，以便非 VFS 内核可以访问文件（尚不支持 exFAT 或 FAT32）</li> 
 <li>......</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibretro%2FRetroArch%2Fblob%2Fmaster%2FCHANGES.md%231100" target="_blank">https://github.com/libretro/RetroArch/blob/master/CHANGES.md#1100</a></p>
                                        </div>
                                      
</div>
            