
---
title: 'SteamOS 3.3 发布，Steam 平台游戏操作系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6236'
author: 开源中国
comments: false
date: Fri, 05 Aug 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6236'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">SteamOS 是 V 社发行的基于 Linux 的游戏操作系统，该系统基于 Arch Linux 的软件堆栈，主要运行在 Steam Deck 设备上。SteamOS 现已发布 3.3 版本，带来如下内容：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>一般更新</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 Steam 叠加层中添加了“成就”和“指南”页面。</li> 
 <li>温度超出安全操作范围时添加通知</li> 
 <li>添加了预定夜间模式功能，允许玩家选择何时自动开启夜间模式</li> 
 <li>添加了一个按钮以清除搜索栏中输入的文本</li> 
 <li>修复了无休止地触发数字奖励的通知</li> 
 <li>修复了主菜单叠加层中的中等长度游戏名称无法正确滚动的问题</li> 
 <li>修复了领取 Steam Deck 数字奖励的一些问题</li> 
 <li>修复了成就进度通知的声音播放</li> 
 <li>修复了与特定主机一起玩时，远程播放客户端中褪色的颜色</li> 
 <li>修复了 Flight Simulator 和 Halo Infinite 的 Xbox 登录窗口无法正确渲染某些角色的问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>键盘</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了对简体中文、繁体中文、日文和韩文键盘的支持。</li> 
 <li>在桌面上为中文、日文和韩文键盘添加了初始 IBus IME 输入支持</li> 
 <li>修复了桌面模式键盘有时无法显示或关闭的问题</li> 
 <li>修复了 Steam 或快速访问菜单下显示的屏幕键盘</li> 
 <li>更新了键盘行为，改进触控板和触摸屏上的快速打字。</li> 
 <li>修复了虚拟键盘的一些触摸样式问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>性能/稳定性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了屏幕截图较多的用户的一些性能问题</li> 
 <li>修复了与管理屏幕截图相关的几个崩溃</li> 
 <li>修复了几个与非 Steam 快捷方式相关的崩溃问题</li> 
 <li>修复了通过 Steam 强制退出时，一些原生 Linux 游戏不退出的问题</li> 
 <li>修复了通过 Steam 退出时， flatpak Chrome 关闭不正确的问题</li> 
 <li>修复了一些 flatpak 应用程序（如 Edge）无法成功退出的错误</li> 
 <li>修复了背光改变强度时，某些游戏的性能问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>桌面模式</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将 Firefox 更新为作为 Flatpak 安装而不是从操作系统存储库中安装，以确保及时更新</li> 
 <li>首次从桌面启动 Firefox 现在将提示通过 Discover Software Center 进行安装，该中心将在更新发布时进行处理。</li> 
 <li>更新了在桌面上创建/编辑的网络连接以默认为系统范围，确保它们在游戏模式下可用</li> 
 <li>添加了 VGUI2 Classic Plasma 桌面主题</li> 
 <li>将桌面模式下的虚拟键盘大小调整为适当的尺寸</li> 
 <li>在桌面模式下添加了对 Qanba Obsidian 和 Qanba Dragon 街机摇杆的支持</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>对接模式</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了为外部显示器缩放 Steam 平台用户界面的选项</li> 
 <li>添加了用于自动缩放外部显示器的 Steam 平台用户界面的切换</li> 
 <li>增加了为存在过扫描问题的外部显示器调整图像显示设置的功能</li> 
 <li>修复了从睡眠状态恢复后不久从坞站断开时面板保持关闭的问题</li> 
 <li>修复了对接时面板背光保持亮着的问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>音频/蓝牙</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了从桌面模式切换时未保存蓝牙配置文件选择</li> 
 <li>修复了未使用麦克风时的回声消除 CPU 开销</li> 
 <li>修复了外部显示器上的多声道音频</li> 
 <li>修复了某些采集卡上的音频输出</li> 
 <li>修复了从睡眠中恢复后音频损坏的一些实例</li> 
 <li>修复了一些使用 ALSA 的 32 位游戏的音频输出</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>驱动程序/固件</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新了具有兼容性和性能修复的图形驱动程序</li> 
 <li>更新了无线驱动程序，修复了 5Ghz 上的 WiFi 断开连接问题</li> 
 <li>更新了控制器固件实用程序以支持未来的控制器硬件版本</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">其他内容详见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsteamcommunity.com%2Fgames%2F1675200%2Fannouncements%2Fdetail%2F3401924854795478415" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            