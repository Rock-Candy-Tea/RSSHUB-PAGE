
---
title: '微软 Win11_10 免费工具集 PowerToys v0.47.0 版本更新'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/613ff97cb15ec0785e7fab70_1024.jpg'
author: ZAKER
comments: false
date: Thu, 30 Sep 2021 05:24:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/613ff97cb15ec0785e7fab70_1024.jpg'
---

<div>   
<p>IT 之家 9 月 30 日消息 感谢 IT 之家网友热心线索投递，微软 PowerToys Release v0.47.0 现已发布。根据社区反馈，微软重新为 PowerToys 引入了呼声很高的按住 Win 键来激活快捷指南的功能。</p><p>此外，该版本还修复了重新启动计算机会导致用户布局重置为默认设置的问题。据悉，PowerToys ( v0.48 ) 的实验版本将在 10 月 4 日那一周发布，对视频会议静音实用程序进行改进，v0.47.0 版本的所有更新仍将适用于 v0.48。</p><p>IT 之家了解到，PowerToys 是微软的开源项目，它提供了一系列工具，人们可以使用这些工具来根据自己的喜好自定义 Win10/Win11 UI 和体验。此外，根据反馈和总体稳定性，一些实用程序也会内置于操作系统中。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202109/613ff97cb15ec0785e7fab70_1024.jpg" data-height="445" data-width="536" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202109/613ff97cb15ec0785e7fab70_1024.jpg" referrerpolicy="no-referrer"></div></div>以下是本次更新的详细内容：<p></p><p>WinUI 升级到 2.7.0 版本。</p><p>通过压缩 GIF 减小安装程序大小。</p><p>用 MarkdownTextblock 替换 ShortcutTextContorl。</p><p>添加了在打开 / 关闭缩略图提供程序时调用 SHCangeNotify SHCNE_ASSOCCHANGED 的功能。</p><p>合并 nuget 包。</p><p>可将额外的日志记录和 bug 处理添加到 PowerToys Run。</p><p>去除旧版 windevbuildagents。</p><p>在 PowerToys 中添加了对嵌入式 MSIX 应用程序的支持。</p><p>将 ListView 替换为 ComboBox 用于图像调整器。</p><p>bug 修复：</p><p>一般的 bug</p><p>修复了新更新更改 PowerToys 安装位置的问题。</p><p>修复了 NumberBox 元素与删除按钮重叠的设置。</p><p>修复了错误报告工具不生成 .zip 文件的问题。</p><p>更新了设置中的快捷方式配置体验。</p><p>修复了侧边栏图标宽度不一致的问题。</p><p>修复了侧边栏 UI 在某些本地化中无法针对较长文本字符串进行缩放的问题。</p><p>修复了设置不显示无效按键分配的问题。</p><p>设置为 " 欢迎使用 PowerToys" 时添加了用户定义的快捷方式，而不是默认快捷方式。</p><p>颜色选择器</p><p>解决了可访问性问题。</p><p>添加了 CIELAB 和 CIEXYZ 颜色格式。</p><p>修复了手动更改 RGB 值不会自动更新显示颜色的错误。</p><p>FancyZones</p><p>修复了重新启动计算机会将用户定义的布局重置为默认选择的回归。</p><p>修复了网格布局编辑器不显示 " 保存 " 和 " 取消 " 按钮的问题。</p><p>修复了用户无法使用键盘添加或合并区域的可访问性问题。</p><p>添加了一个浮出控件，描述了 " 允许区域跨越监视器 " 选项的先决条件。</p><p>修复了各种崩溃错误。</p><p>文件资源管理器插件</p><p>为 Windows 资源管理器添加了 PDF 缩略图提供程序。</p><p>图像调整器</p><p>为新添加的尺寸添加了默认值。</p><p>修复了无法注册文件名格式设置中的空格的回归。</p><p>更正了 Image Resizer Window 的缩放问题。</p><p>修复了当 json 设置格式不正确时 PowerToys 崩溃的问题。</p><p>键盘管理器</p><p>修复了添加快捷方式时崩溃的问题。</p><p>修复了重新映射窗口不显示的问题。</p><p>修复了将快捷方式重新映射到 Alt+Tab 时使用箭头键破坏 Alt+Tab 导航的问题。</p><p>PowerToys Run</p><p>改进了设置插件的字幕布局。</p><p>通过 > 键为设置插件添加了路径过滤器。</p><p>设置插件的翻译改进。</p><p>添加了对设置插件的翻译支持。</p><p>修复了 PowerToys Run 在启动时未聚焦的问题。</p><p>修复了更改后更新变量时空 / 删除的环境变量崩溃的问题。</p><p>更正了注册表插件查询结果。</p><p>修复了注册表插件查询中的崩溃问题。</p><p>修复了 Windows 关闭时的崩溃问题。</p><p>在插件的全局结果设置中添加了更好的描述。</p><p>在运行系统命令之前添加了一个确认框。</p><p>添加了使用系统本地化的选项，这是我们系统命令的通用术语。</p><p>捷径指南</p><p>重新添加了长 Win 按键以激活实用程序。</p><p>视频会议静音</p><p>修复了页面加载时聚焦设置中的第一个热键输入的问题。防止无意中重新分配快捷方式。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            