
---
title: 'LXQt 1.0 发布，轻量级 Qt 桌面环境'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9670'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 08:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9670'
---

<div>   
<div class="content">
                                                                                            <p>LXQt 1.0 现已发布，LXQt 是资源开支相对较低的开源桌面环境，由 LXDE 和 Razor-qt 项目合并而成。LXQt 1.0 依赖于 Qt 5.15 LTS，更新内容包括有文件管理器和图像查看器的改进、桌面通知的免打扰模式、两个新的桌面主题、翻译等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新亮点如下：</p> 
<h4 style="text-align:start">General</h4> 
<ul> 
 <li>LXQt 1.0.0 依赖于 Qt 5.15，这是 Qt5 的最后一个 LTS 版本。</li> 
 <li>除了错误修复和解决方法之外，LXQt 的文件管理器还添加了多项功能，例如处理标志、LXQt 文件对话框中的新选项、默认情况下使桌面项目具有粘性的选项、文件夹的递归自定义、使用鼠标滚轮平滑滚动的增强功能， 等等。</li> 
 <li>LXQt 的图像查看器已收到多项修复和新选项。</li> 
 <li>LXQt 桌面通知添加了免打扰模式。</li> 
 <li>LXQt Panel 有一个新的插件，叫做“Custom Command”。</li> 
 <li>可以在 LXQt 外观配置中保存和加载 Qt 调色板。</li> 
 <li>可以从 LXQt 电源管理器的托盘图标暂停空闲检查。</li> 
 <li>QTerminal 中引用了拖放文件的名称。</li> 
 <li>添加了两个 LXQt 主题并修复了现有主题中的问题。</li> 
 <li>翻译得到了许多更新。</li> 
 <li>以及可以在 LXQt 组件的变更日志中找到的其他更改。</li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LibFM-Qt / PCManFM-Qt</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>可以在“File Properties”对话框中添加/删除标志。</li> 
 <li>文件夹的递归定制成为可能。</li> 
 <li>添加了一个选项，用于在默认情况下使桌面项目 sticky。</li> 
 <li>挂载、卸载和弹出操作被添加到<code>computer:///</code>下的文件上下文菜单。</li> 
 <li>通过使用变通方法（针对 GLib、Qt 或两者中的问题），可以避免挂载加密卷时的 freeze。</li> 
 <li><code>GFileMonitor</code>有关文件夹符号链接内的文件监控的错误的解决方法。</li> 
 <li>在关闭主窗口时阻止关闭文件操作对话框。</li> 
 <li>在图标视图中使用 Shift+鼠标确保正确的选择顺序。</li> 
 <li>防止在文件提示对话框中的 self-overwriting。</li> 
 <li>修复了 Cyrillic case-insensitive regex 搜索。</li> 
 <li>增强和修复平滑滚轮滚动。现在，紧凑和列表模式默认也有它（但可以为它们禁用它）。</li> 
 <li>为 LXQt 文件对话框添加了选项，用于在列表和紧凑模式下显示隐藏文件和禁用平滑滚动。此外，列表模式下 LXQt 文件对话框的隐藏列也会被记住。</li> 
</ul> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXQt Panel</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li>添加了“Custom Command”插件。它是一个灵活的插件，可以以多种方式使用。</li> 
 <li>主菜单搜索结果的项目有上下文菜单，可以拖放。</li> 
 <li>状态通知程序中更好的图标处理。</li> 
 <li>修复了主菜单中的键盘导航。</li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>QTerminal / QTermWidget</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>拖放文件的名称是带引号的。</li> 
 <li>修剪 shell 字符串。</li> 
 <li>在打开新窗口或双击标签栏时遵循预设拆分。</li> 
 <li>修复了 (Plasma) Wayland 在打开标签和拆分时的崩溃。</li> 
 <li>添加了保持下拉窗口打开的选项。</li> 
 <li>在 Wayland 下添加了错误菜单位置的解决方法。</li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXQt Desktop Notifications</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新增免打扰模式。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXQt </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Power Management</h4> 
<ul> 
 <li style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Idleness checks 可以从托盘图标暂停 30 分钟到 4 小时。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXImage Qt</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>添加了用于隐藏/显示主工具栏和/或菜单栏、使用 Trash、更改缩略图尺寸以及更改缩略图停靠位置的选项。</li> 
 <li>修复了图像拟合、翻转和旋转中的错误。</li> 
 <li>修复了使用触摸板在图像上的滚轮滚动</li> 
 <li>允许直接图像重命名（使用快捷方式）。</li> 
 <li>记住 EXIF dock width。</li> 
 <li>添加了用于全屏启动的命令行选项。</li> 
 <li>添加了一个选项，用于在缩放时禁用图像平滑。</li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXQt Configuration</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>配置中心新增“Other Settings”。</li> 
 <li>外观配置支持 Qt 调色板的保存和加载。</li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>libQtXdg</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>添加了对默认终端的支持。</li> 
 <li>在查找图标时考虑 Qt 的 fallback 搜索路径（对于编码人员）。</li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXQt Global Keys</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了过滤以轻松查找快捷方式。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>LXQt Archiver</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>对于带有加密列表的档案，会显示密码提示。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更新说明：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flxqt%2Flxqt%2Freleases%2Ftag%2F1.0.0" target="_blank">https://github.com/lxqt/lxqt/releases/tag/1.0.0</a></p>
                                        </div>
                                      
</div>
            