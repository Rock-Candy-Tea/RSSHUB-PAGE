
---
title: 'RetroArch 1.9.3 发布，跨平台模拟器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4567'
author: 开源中国
comments: false
date: Thu, 20 May 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4567'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RetroArch 1.9.3 现已发布。RetroArch 是款功能强大的跨平台模拟器，不但能够模拟许多不同的游戏主机，还能在 Windows、MacOS、Linux、Android、iOS 以及多种游戏主机上执行。</p> 
<p>主要更新内容如下：</p> 
<ul> 
 <li>3DS：禁用 XMB/GLUI 中的菜单屏幕保护程序动画</li> 
 <li>COMMAND：在 recvfrom() 之前初始化 netcmd->cmd_source_len</li> 
 <li>CONTENT LOADING/STATICALLY LINKED：通过文件浏览器加载内容时，确保应用了“Always Reload Core on Run Content”设置</li> 
 <li>CONTENT LOADING/EMSCRIPTEN：修复了在有"broken"核心处理的平台上通过文件浏览器加载的内容（即 emscripten）</li> 
 <li>CORE INFO：写入压缩的 core info 缓存文件时跳过空白部分</li> 
 <li>CORE INFO/FILE IO：Core Info cache；在磁盘文件 I/O 速度较慢的系统上显著提高了文件 I/O 性能</li> 
 <li>CORE INFO/FILE IO：默认情况下，在所有“console”平台上启用 core info cache</li> 
 <li>FREEBSD：FreeBSD 构建修复</li> 
 <li>LAKKA：支持调整 CPU governors/scaling 策略</li> 
 <li>LAKKA：添加了管理策略和设置，以存储它们并在启动时重新加载它们</li> 
 <li>LIBRETRO API：为 cores 添加 API 扩展，以覆盖前端的 fast-forward 状态</li> 
 <li>MENU/RGUI：修复了启用“锁定菜单宽高比”时保存配置 files/overrides 的问题</li> 
 <li>SHADERS：修复了“Auto-Shader Delay”功能</li> 
 <li>UWP/D3D11：禁用 Mipmap 生成</li> 
 <li>UWP/XBOX：添加“Force 4K resolution”选项（在 Xbox 上强制分辨率为全屏尺寸，如果设置为 0，将使用 3840 x 2160 的固定值）</li> 
</ul> 
<p>详细说明见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibretro%2FRetroArch%2Fblob%2Fmaster%2FCHANGES.md%23193" target="_blank">https://github.com/libretro/RetroArch/blob/master/CHANGES.md#193</a> </p>
                                        </div>
                                      
</div>
            