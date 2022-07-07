
---
title: 'Windows Terminal Preview 1.15 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9c908c11443d5996f2a986a2288b1a1bb27.gif'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 07:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9c908c11443d5996f2a986a2288b1a1bb27.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Windows Terminal Preview 已更新到 1.15 版，此版本带来如下内容：</span></p> 
<h2 style="text-align:left">键盘选择（标记模式）</h2> 
<ul> 
 <li>现在可以使用键盘以标记模式选择文本缓冲区中的任何文本。</li> 
 <li>可以通过键入Ctrl+ Shift+ M 进入标记模式 。在标记模式下，可以使用箭头键移动到起始位置，然后按住 Shift你并使用箭头键进行选择。</li> 
 <li>Esc 将退出标记模式，Ctrl+A 选择缓冲区中的所有文本。</li> 
</ul> 
<p><img alt height="427" src="https://oscimg.oschina.net/oscnet/up-9c908c11443d5996f2a986a2288b1a1bb27.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>标记模式操作</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span> <code><span>markMode</span></code>：切换标记模式。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span> <code><span>toggleBlockSelection</span></code>：允许仅使用键盘创建块选择。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span> <code><span>switchSelectionEndpoint</span></code>：使用键盘修改选择时，此操作将焦点切换到另一个选择标记。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h2 style="text-align:left">滚动标记（实验性）</h2> 
<p>Windows 终端现在支持滚动标记，可以通过添加 experimental.autoMarkPrompts 设置为输入的每个命令自动添加滚动标记。</p> 
<p><img alt height="427" src="https://oscimg.oschina.net/oscnet/up-c3e29a1cb20e65ba1bba27ebb1f10b9faf3.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left"><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>滚动标记动作</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span>addMark</span></code>：向文本缓冲区添加滚动标记。如果有选择，则标记放置在选择处，否则将放置在光标行。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span>addMark</span></code>操作有一个可选的<code><span>color</span></code>参数，可让您设置滚动标记的颜色。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span>scrollToMark</span></code>：在给定方向滚动到滚动标记。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span>scrollToMark</span></code>的<code><span>direction</span></code>参数接受<code><span>first</span></code>、<code><span>previous</span></code>、<code><span>next</span></code>和<code><span>last</span></code>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span>clearMark</span></code>：清除当前位置的滚动标记（如果有选择），或者光标位置的滚动标记。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span>clearAllMarks</span></code>：清除文本缓冲区中的所有滚动标记。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h2 style="text-align:left"><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PowerShell “黑条”补丁删除</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本删除了 Windows Terminal 防止 PowerShell 运行时出现意外黑色背景（可能表现为横跨屏幕的黑条）的补丁。选择删除此补丁，是因为较新版本的 PowerShell 的 PSReadline 组件已包含该问题的修复程序。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>由于此更改，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fohmyposh.dev%2F" target="_blank">Oh-My-Posh</a> 又能使用黑色背景颜色显示提示元素。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:left">其他改进</h2> 
<ul> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Windows 终端现在支持<code><span>DECPS</span></code>转义序列，允许通过终端播放声音</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果启动时 Windows 终端预览设置文件为空，该文件将作为 Windows 终端设置的副本启动</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>配色方案现在接受<code><span>"magenta"</span></code>并<code><span>"brightMagenta"</span></code>代替<code><span>"purple"</span></code>and <code><span>"brightPurple"</span></code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Windows 终端项目现在使用单一坐标类型，更改为 +3610，-3906 行差异。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-terminal-preview-1-15-release%2F" target="_blank">发布博客</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p> </p>
                                        </div>
                                      
</div>
            