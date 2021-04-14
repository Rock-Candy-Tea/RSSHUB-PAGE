
---
title: 'CopyQ 4.0.0 发布，剪切板管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1391'
author: 开源中国
comments: false
date: Wed, 14 Apr 2021 06:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1391'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CopyQ 是一个剪切板管理工具，可以监控系统剪贴板，并将其内容保存在自定义标签中。保存的剪贴板内容可以在以后直接复制和粘贴到任何应用程序中。</p> 
<h3>特性：</h3> 
<ul> 
 <li>同步插件新近使多个应用程序实例之间的新项目顺序保持一致，一个实例中新添加的项目将出现在其他实例的顶部；</li> 
 <li>现在，如果禁用了正则表达式，则搜索将查找单独的单词，搜索“ foo bar”将找到同时包含“ foo”和“bar”的项目，并且单词的相对位置不再重要；</li> 
 <li>现在使用系统通知弹出窗口代替了自己的实现；</li> 
 <li>主窗口和托盘菜单中的项目行现在默认从索引 1 开始，而不是从索引 0 开始。这可以通过使用 命令 <code>copyq config row_index_from_one false</code> 改变。</li> 
 <li>标签可以在配置中被标记为"锁定"。带有这种标签的项目不能被删除，直到标签被删除或 "解锁"。</li> 
 <li>bash 命令行完成；</li> 
 <li>当打开 Action 对话框时，历史记录组合框被集中，以便于调用最近的命令。注意：MacOS上不支持聚焦组合框；</li> 
 <li>Web 插件已被完全放弃（维护不到位产生的性能和安全问题）；</li> 
 <li>高级选项 window_paste_with_ctrl_v_regex 改变默认的粘贴方式，特定窗口的快捷键 Shift+Insert 改为 Ctrl+V（仅在 Windows 和 Linux/X11）。</li> 
 <li>新的高级选项允许设置复制、粘贴和窗口焦点的间隔和等待时间； 
  <ul> 
   <li><code>script_paste_delay_ms</code> - <code>paste()</code>后的延迟，默认为 250ms；</li> 
   <li>window_waiting_before_raise_ms；</li> 
   <li>window_wait_raised_ms；</li> 
   <li>window_wait_after_raised_ms；</li> 
   <li>window_key_press_time_ms；</li> 
   <li>window_wait_for_modifiers_release_ms；</li> 
  </ul> </li> 
 <li>格式 "text/plain;charset=utf-8" 现在优于 "text/plain"；</li> 
 <li>FakeVim: 在添加新行时自动缩进；</li> 
</ul> 
<h3>平台：</h3> 
<ul> 
 <li>Wayland 支持，特别是剪贴板访问和窗口大小恢复；</li> 
 <li>Windows：现在编译是 64 位的；</li> 
 <li>使用应用程序菜单或启动器中的已安装条目在桌面环境中选择应用程序图标，立即显示主窗口。以前，该应用程序以托盘或最小化状态静默启动；</li> 
 <li>Linux/X11：修复从 VirtualBox 复制的问题；</li> 
 <li>macOS：修复版本信息；</li> 
</ul> 
<h3>用户界面：</h3> 
<ul> 
 <li>默认主题与系统主题保持一致，这也允许在自定义样式表文件中使用新的特殊占位符，如 default_bg 和 default_text；</li> 
 <li>命令对话框总是在顶部显示命令类型；</li> 
 <li>更新了图标（Font Awesome 5.15.3）；</li> 
 <li>FakeVim：命令行不支持更好的文本交互（选择、复制、剪切、粘贴）；</li> 
</ul> 
<h3>修复：</h3> 
<ul> 
 <li>修复了一些自定义系统主题时崩溃的问题；</li> 
 <li>修复导入已保存的旧标签/配置；</li> 
 <li>修复复制命令中的尾部空格；</li> 
 <li>修正偏好设置中的过滤快捷方式；</li> 
 <li>修正恢复窗口几何形状的问题；</li> 
 <li>托盘菜单项仅在菜单显示前更新；</li> 
 <li>避免在默认情况下存储 "text/richtext"，因为不支持显示这种格式的内容；</li> 
 <li>更新同步项目时性能更佳；</li> 
 <li>各种外观和主题修复。</li> 
</ul> 
<h3>Various：</h3> 
<ul> 
 <li>代码库现在遵循 C++17 标准；</li> 
 <li>GitHub Actions 现在可以持续为 Linux 和 macOS 进行构建和测试，并且为 macOS 提供了开发构建。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Freleases%2Ftag%2Fv4.0.0" target="_blank">https://github.com/hluk/CopyQ/releases/tag/v4.0.0</a></p>
                                        </div>
                                      
</div>
            