
---
title: '微软推出Windows Terminal 1.12预览版：支持设置为默认终端'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1021/7b74022828cf54d.png'
author: cnBeta
comments: false
date: Thu, 21 Oct 2021 03:53:37 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1021/7b74022828cf54d.png'
---

<div>   
<strong>Windows Terminal 刚刚迎来了 1.12 预览版，主要变化是允许用户将这个稳定编译版本设为 Windows 的默认终端模拟器。</strong>之后当你执行任何命令行应用程序时，它都会自动在 Windows 终端内启动。感兴趣的朋友，需要先加入 Windows 11 的 Insider Dev 测试通道，才能享用本次更新的完整功能。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1021/7b74022828cf54d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1021/7b74022828cf54d.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：<a href="https://devblogs.microsoft.com/commandline/windows-terminal-preview-1-12-release/" target="_self">Dev Blogs</a>）</p><p>Windows Terminal Preview 1.12 中的其它变化，还包括配置文件匹配（Profile Matching）、窗口复位（Window Restoration）、完全透明（Full Transparency），以及各种 Bug 修复和体验改进。</p><p><a href="https://static.cnbetacdn.com/article/2021/1021/c38218eef2343b4.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1021/c38218eef2343b4.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>（1）Windows Terminal 现在会适当地处理终端配置文件的可执行启动匹配，以便在符合条件的情况下启用所有自定义设置。比如点击“开始”菜单中的命令提示符，将打开对应的 CMD 配置文件，而不是调用 cmd.exe 的默认配置文件。目前该功能仅可在 Widnows 终端的预览版本中可用，正式引入还要再等待一段时间。</p><p><img src="https://static.cnbetacdn.com/article/2021/1021/e076d44f9935c13.gif" alt="3.gif" referrerpolicy="no-referrer"></p><p>（2）Windows 终端现允许用户指定“在重启后恢复之前的选项卡和窗格”，有需要的朋友，可在 settings.json 文件的“启动页面 - 全局设置”项下，将“firstWindowPreference”偏好设置改为“persistedWindowLayout”窗口布局。</p><p><img src="https://static.cnbetacdn.com/article/2021/1021/dc7795e014bc545.png" alt="4.png" referrerpolicy="no-referrer"></p><p>（3）除了亚克力（Acrylic），Windows 终端现还支持全透明效果，就像最初的控制台中可用的透明度变化一样。有需要的朋友，可通过 Ctrl + Shift + Scroll 组合键来调节窗口的透明度。不过当背景变为透明时，控制台中的文本将保持不透明，以便在不失去对比度的情况下阅读终端提示。</p><p><img src="https://static.cnbetacdn.com/article/2021/1021/01200504f816b13.gif" alt="5.gif" referrerpolicy="no-referrer"></p><p><strong>其它改进：</strong></p><blockquote><p>· 可使用键盘选择已打印在缓冲区中的文本。</p><p>· 自动生成 <a data-link="1" href="https://microsoft.pvxt.net/zaZYr" target="_blank">Visual Studio</a> Developer Command Prompt（VS2017+）和 Visual Studio Developer PowerShell（VS2019.2+）的配置文件。</p><p>· 提升的终端窗口，会在选项卡的左侧显示一个盾牌图标，让窗口更易分辨。</p><p>· 可启用 adjustIndistinguishableColors 配置文件设置，以根据背景颜色调整前景色、并使之更加明显。</p><p>· 可选择窗格的子树、并与之交互。</p><p>· 拆分新窗格时，SplitState 现可接受方向修饰符。</p><p>· 现可以使用 Alt + Space 组合键打开系统菜单，以及 openSystemMenu 的新操作。</p></blockquote><p><strong>BUG修复：</strong></p><blockquote><p>· 在控制台窗口内点击时，现可正确调用触摸键盘。</p><p>· 当所有事件的视口滚动时，鼠标坐标现已恒定。</p><p>· 运行多组操作时，焦点可立即切换到选中的新选项卡。</p><p>· 现可导航窗格焦点，而无需将之缩小。</p></blockquote>   
</div>
            