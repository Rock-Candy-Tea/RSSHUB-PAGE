
---
title: 'CotEditor 4.2 发布，支持「通用控制」与「接力」'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7037'
author: 开源中国
comments: false
date: Wed, 11 May 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7037'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CotEditor 是一个轻量级、简洁、但功能强大的文本编辑器，用于编辑纯文本文件，如网页 HTML、CSS），程序源代码（Python、Ruby、Perl 等），结构化文本（Markdown、Textile、Tex 等）或任何其他类型的纯文本。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CotEditor 4.2 正式发布，该版本更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">系统要求：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>macOS 11 及以上版本</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>能够处理包含多种类型行尾的文档</li> 
 <li>在打开或重新加载时提醒文档中不一致的行尾</li> 
 <li>在检查器的警告窗格中列出不一致的行尾</li> 
 <li>在行尾选项中增加了次要的行尾，即 NEL（新行）、LS（行分隔符）和 PS（段落分隔符）（这些项目只有在按下 Option 键或文档的行尾是其中之一时才可见）。</li> 
 <li>增加了隐藏的 Paste Exactly 命令（Command-Option-V），该命令粘贴剪贴板中的文本而不做任何修改。</li> 
 <li>在 "打印" 对话框增加一个选项 "Selection to the Pages"，只打印文档中的选定文本。</li> 
 <li>为 Unicode 代码点输入增加历史记录。</li> 
 <li>支持 Handoff</li> 
 <li>只需从首选项中删除设置名称，即可将设置文件导出到访达（如主题或多个替换文件）。</li> 
 <li>通过 Universal Control（通用控制）在不同设备的 CotEditors 之间传输设置，方法是拖动设置名称并将其放到另一个 CotEditor 的设置列表区域。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新文档图标。</li> 
 <li>更智能地检测文档中的行尾。</li> 
 <li>将多行的片段文本缩进到将被插入部分的缩进水平。</li> 
 <li>通过仅在大型文档中启用非连续文本布局模式，改善正常尺寸文档的滚动行为。</li> 
 <li>优化语法解析。</li> 
 <li>当书写方向为从右到左时，将编辑器的垂直滚动器放在左侧。</li> 
 <li>如果书写方向是从右到左，在打印时将行号打印在右侧。</li> 
 <li>调整打印时行号的垂直位置。</li> 
 <li>当恢复上一个会话的文件时，即使是与文件编码不相容的字符也会被恢复。</li> 
 <li>在不兼容的字符列表中显示代码点，而不是在空白处留白。</li> 
 <li>更新 HTML 语法样式，在大纲中显示<span> </span><code>hr</code><span> </span>元素作为分隔符。</li> 
 <li>为字体设置控件添加步进器。</li> 
 <li>恢复用户在上次会话中明确设置的文件编码。</li> 
 <li>倾向于使用 .yml 而不是 .yaml 作为语法定义文件。</li> 
 <li>废弃大纲菜单模板中用行号替换<span> </span><code>$LN</code><span> </span>的功能。</li> 
 <li>删除 CoffeeScript 和 Tcl 的原始文档图标。</li> 
 <li>修改文字，使之更像 Mac 的表达方式。</li> 
 <li>更新帮助内容。</li> 
 <li>提高稳定性。</li> 
 <li>在 Basic Regular Expression Syntax 参考中，用<span> </span><code>\\R</code><span> </span>替换换行元字符<span> </span><code>\\n</code>。</li> 
 <li>调整 Anura 主题。</li> 
 <li>启用 macOS 12 中引入的安全状态恢复功能。</li> 
 <li>将 Yams从 5.0.0 更新到 5.0.1。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了启动后语法样式的变化没有应用到文件映射中的问题。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcoteditor%2FCotEditor%2Freleases" target="_blank">https://github.com/coteditor/CotEditor/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            