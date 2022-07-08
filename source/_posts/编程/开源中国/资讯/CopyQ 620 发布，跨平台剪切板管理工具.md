
---
title: 'CopyQ 6.2.0 发布，跨平台剪切板管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7251'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7251'
---

<div>   
<div class="content">
                                                                                            <p>CopyQ 是一个剪切板管理工具，可以监控系统剪贴板，并将其内容保存在自定义标签中。保存的剪贴板内容可以在以后直接复制和粘贴到任何应用程序中。</p> 
<p>CopyQ 6.2.0 现已发布，该版本更新内容如下：</p> 
<p><strong>新增</strong></p> 
<ul> 
 <li>Tabs 现在可以从部分损坏的数据文件中加载至少一些项目，从而删除其余项目。</li> 
 <li>使用 Qt 框架（QSaveFile）来保存数据，更简单、更安全。</li> 
 <li>脚本中的新<code>Settings</code>类可用于管理 INI 配置文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F1964" target="_blank">#1964</a> )。</li> 
</ul> 
<p><strong>更改</strong></p> 
<ul> 
 <li>隐藏的未经测试的保存按钮已从操作对话框中删除。</li> 
</ul> 
<p><strong>修复</strong></p> 
<ul> 
 <li> <p>修复了在循环中恢复窗口几何图形的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F1946" target="_blank">#1946</a> )。</p> </li> 
 <li> <p>修复了在极少数情况下在脚本中转换内部字节数组表示的问题。</p> </li> 
 <li> <p>修复 tray menu 外观以遵循配置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F1896" target="_blank">#1896</a> )。</p> </li> 
 <li> <p>如果鼠标滚轮滚动且鼠标指针位于菜单之外，则搜索历史弹出菜单将关闭（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F1980" target="_blank">#1980</a>）。</p> </li> 
 <li> <p>macOS：修复了粘贴问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fpull%2F2012" target="_blank">#2012</a> )。</p> </li> 
 <li> <p>Windows：修复了在注销时退出应用程序的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Fissues%2F1249" target="_blank">#1249</a> )。</p> </li> 
 <li> <p>Windows：正确处理本地路径分隔符的解决方法，而不是将其作为特殊转义字符。</p> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhluk%2FCopyQ%2Freleases%2Ftag%2Fv6.2.0" target="_blank">https://github.com/hluk/CopyQ/releases/tag/v6.2.0</a></p>
                                        </div>
                                      
</div>
            