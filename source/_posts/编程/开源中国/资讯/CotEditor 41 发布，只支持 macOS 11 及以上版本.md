
---
title: 'CotEditor 4.1 发布，只支持 macOS 11 及以上版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6504'
author: 开源中国
comments: false
date: Wed, 16 Feb 2022 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6504'
---

<div>   
<div class="content">
                                                                                            <p>CotEditor 是一个轻量级、简洁、但功能强大的文本编辑器，用于编辑纯文本文件，如网页 HTML、CSS），程序源代码（Python、Ruby、Perl 等），结构化文本（Markdown、Textile、Tex 等）或任何其他类型的纯文本。</p> 
<p>CotEditor 4.1 正式发布，该版本更新内容如下：</p> 
<h3>新功能</h3> 
<ul> 
 <li>增加了在大纲窗格中过滤大纲项目的功能</li> 
 <li>增加打印时不绘制背景颜色的选项</li> 
 <li>在 “查找” 菜单中增加 "打开大纲菜单" 命令</li> 
 <li>增加土耳其语和英式英语的本地化</li> 
 <li>为文档对象引入一个新的 AppleScript 命令 <code>jump</code></li> 
 <li>为文档对象引入一个新的只读 AppleScript 参数 <code>has BOM</code>，为 <code>convert</code> 命令引入一个新选项 <code>BOM</code></li> 
 <li>如果书写方向是从右到左，在编辑器中把行号视图放在右边</li> 
 <li>为 Protocol Buffer 增加语法样式</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li><strong>将系统要求改为 macOS 11 Big Sur 及以上版本</strong></li> 
 <li>更新窗口尺寸设置，如果偏好设置>窗口中的宽度/高度设置为空白，则使用文档最后的窗口尺寸</li> 
 <li>允许菜单键绑定分配一个没有 Command 键的快捷方式</li> 
 <li>在控制字符的不兼容字符表中显示代码点而不是留空白</li> 
 <li>更新 Swift 语法样式，新增 Swift 5.5 中添加的关键字</li> 
 <li>更新 C++ 语法样式，增加更多文件扩展名</li> 
 <li>更新 Markdown 语法样式，以加快语法解析速度</li> 
 <li>当在 Go to Line 命令中或通过 AppleScript 指定具有负值的行时，改变行为以在计算中包括最后的空行</li> 
 <li>改进文档检查器中的字符信息部分，以显示所选字符的代码点列表，而不是只在选择单一Unicode 字符时显示</li> 
 <li>更新字符检查器的 Unicode 块名称列表，从 Unicode 13.0.0 更新到 Unicode 14.0.0。</li> 
 <li>确保在终止前，即使其他任务中断，应用程序也会重新启动</li> 
 <li>改进一些工具栏项目，使它们的状态即使在折叠时也能分辨出来</li> 
 <li>当键绑定的输入快捷方式已经被其他命令占用时，在错误信息中显示命令名称</li> 
 <li>改进 VoiceOver 的可访问性</li> 
 <li>更新帮助中的 AppleScript 指南</li> 
 <li>改进表格中的拖放动画</li> 
 <li>优化几个文件的解析</li> 
 <li>调整编辑器区域的边距</li> 
 <li>默认隐藏导出设置文件的扩展名</li> 
 <li>更新键绑定设置中快捷键的一些符号</li> 
 <li>更新构建环境至 Xcode 13.2（Swift 5.5）</li> 
 <li>删除 xcworkspace</li> 
 <li>[非 AppStore 版本] 更新 Sparkle 到 2.0.0</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcoteditor%2FCotEditor%2Freleases" target="_blank">https://github.com/coteditor/CotEditor/releases</a></p>
                                        </div>
                                      
</div>
            