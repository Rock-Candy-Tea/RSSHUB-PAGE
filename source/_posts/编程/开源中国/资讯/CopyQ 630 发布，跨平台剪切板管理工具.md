
---
title: 'CopyQ 6.3.0 发布，跨平台剪切板管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7567'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7567'
---

<div>   
<div class="content">
                                                                                            <p>CopyQ 是一个剪切板管理工具，可以监控系统剪贴板，并将其内容保存在自定义标签中。保存的剪贴板内容可以在以后直接复制和粘贴到任何应用程序中。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CopyQ 6.3.0 现已发布，该版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更改</strong></p> 
<ul> 
 <li> <p><span>UI 边距减少，为项目内容留下更多空间。</span></p> </li> 
 <li> <p><span>脚本函数<code>config()</code>现在列出每个选项的当前值 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F412" target="_blank">#412</a> )。<br> 新的<code>copyq config</code>输出示例：</span></p> 
  <div> 
   <pre><span><span><span><span><span><span><span><span><span><span style="background-color:var(--color-canvas-subtle)"><code>... clipboard_notification_lines=3 Number of lines to show for new clipboard content. Set to 0 to disable. clipboard_tab=&clipboard Name of tab that will automatically store new clipboard content. Leave empty to disable automatic storing. close_on_unfocus=false Close main window when other application has focus ... </code></span></span></span></span></span></span></span></span></span></span></pre> 
  </div> </li> 
 <li> <p><span>来自上游的 FakeVim 插件改进：</span></p> 
  <ul> 
   <li>仅忽略配置文件中的全行注释</li> 
   <li>支持替代命令模式中的 backslashes</li> 
   <li>部分支持多次重复命令 (:g, :v)</li> 
  </ul> </li> 
 <li> <p><span>提高渲染项目列表的速度。</span></p> </li> 
 <li> <p><span>从 Font-Awesome 6.2.0 更新图标字体</span></p> </li> 
</ul> 
<p style="text-align:start"><strong>修复</strong></p> 
<ul> 
 <li> <p><span>修复了在鼠标光标下显示窗口的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F2088" target="_blank">#2088</a>）。</span></p> </li> 
 <li> <p><span>在单击激活模式下，可以在按住 Shift 或 Ctrl 的同时选择多个项目（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F2056" target="_blank">#2056</a>）。</span></p> </li> 
 <li> <p><span>预定义命令“忽略没有或单个字符的项目”现在还可以避免同步选择，并在复制的字符少于两个时显示弹出窗口。</span></p> </li> 
 <li> <p><span>Wayland：修复了在各种情况下与剪贴板同步选择。</span></p> </li> 
 <li> <p><span>Wayland：修复了在访问托管剪贴板数据时可能发生的崩溃。</span></p> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Freleases%2Ftag%2Fv6.3.0" target="_blank">https://github.com/hluk/CopyQ/releases/tag/v6.3.0</a></p>
                                        </div>
                                      
</div>
            