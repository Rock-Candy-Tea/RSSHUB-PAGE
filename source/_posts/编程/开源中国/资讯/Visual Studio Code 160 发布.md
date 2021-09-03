
---
title: 'Visual Studio Code 1.60 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fdda984b6fe2baf84c2f71bd10216e6f218.gif'
author: 开源中国
comments: false
date: Fri, 03 Sep 2021 07:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fdda984b6fe2baf84c2f71bd10216e6f218.gif'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio Code 1.60 现已发布，其中一些主要亮点内容如下：</p> 
<ul> 
 <li>自动语言检测</li> 
</ul> 
<p>上一个版本，VSC 为无标题文件引入了一项实验性功能，该功能会根据内容自动设置文件的语言模式。自动语言检测功能使用机器学习来猜测语言，并且机器学习模型完全在用户机器本地运行。现在，VSC 默认启用自动语言检测，并扩展检测以包括没有文件扩展名的文件。下面是从网上获取一个示例并将其粘贴到一个无标题的编辑器中：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-fdda984b6fe2baf84c2f71bd10216e6f218.gif" referrerpolicy="no-referrer"></p> 
<p>Notebooks 语言选择器中的自动检测选项：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7634597d5e12df5b54d2b8ff38ed52a6c3a.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>高性能的括号着色</li> 
</ul> 
<p>编辑器现在支持原生括号对着色。可以通过设置 "editor.bracketPairColorization.enabled": true 来启用括号对着色。所有颜色都是主题化的，最多可以配置六种颜色。实施此功能是为了解决 CoenraadS 著名的 Bracket Pair Colorizer 扩展的性能问题。现在，即使是在大文件中，变化也会立即反映出来：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-813f4b0041ce2499dc6011a4b7278400b76.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>设置编辑器中代码块的语法高亮显示</li> 
</ul> 
<p>现在支持设置描述中的代码块语法高亮显示：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-531b25dcef2cf6c562bf9b31ac95ece34a5.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>自定义渲染框图和块状元素的字符</li> 
</ul> 
<p>当 GPU 加速开启时（terminal.integrated.gpuAcceleration），方框绘制和块元素字符现在使用 pixel-perfect 的自定义字形而不是使用字体。这意味着，即使用户在终端中设置了行高或字母间距，方框的绘制也是没有间隙的。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f1d918258d93a0f18aaec02bbd7fd12395e.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>在 WATCH 视图中设置值</li> 
</ul> 
<p>现在可以在 WATCH 视图中使用上下文菜单中的 "设置值" 操作来设置被监视表达式的值。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1e6f83b4a73165d3c4b9b25b36ca60a1664.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>锁定的编辑器组</li> 
</ul> 
<p>现在支持锁定编辑器组，不仅适用于终端，也适用于任何编辑器。如果用户打开了多个编辑器组，现在可以使用新命令或从溢出菜单锁定它：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c733d0944dd06ba1409cf21d2e481dc69df.png" referrerpolicy="no-referrer"></p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_60%23_web-extensions" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            