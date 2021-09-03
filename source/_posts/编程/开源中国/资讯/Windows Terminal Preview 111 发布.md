
---
title: 'Windows Terminal Preview 1.11 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-631c423fe3138cc7e1fcf65ad90749333a6.png'
author: 开源中国
comments: false
date: Fri, 03 Sep 2021 06:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-631c423fe3138cc7e1fcf65ad90749333a6.png'
---

<div>   
<div class="content">
                                                                                            <p>Windows Terminal Preview 1.11 已发布，主要新特性如下：</p> 
<h4>Acrylic 标题栏</h4> 
<p>添加了一个新设置，用户可以在其中将标题栏设为 acrylic。此设置可以在 settings UI  的外观页面上找到，也可以在你的 settings.json 文件中使用 <code>"useAcrylicInTabRow":true</code>作为一个全局设置。值得注意的是，该设置需重启生效。</p> 
<p><img alt height="272" src="https://oscimg.oschina.net/oscnet/up-631c423fe3138cc7e1fcf65ad90749333a6.png" width="500" referrerpolicy="no-referrer"></p> 
<h4>最小化到系统托盘</h4> 
<p>增加了将 Terminal 最小化到系统托盘的能力。添加了两个新的全局 boolean 设置：minimizeToTray 和 alwaysShowTrayIcon。当 minimizeToTray 设置为"true"时，最小化一个窗口将把它发送到通知区并从任务栏中隐藏起来。当 alwaysShowTrayIcon 设置为“true”时，无论 minimizeToTray 设置如何，托盘图标都会显示。</p> 
<p>注意：这些设置还没有在 settings UI 中出现，只能在settings.json文件中设置。</p> 
<h4>Intense text style</h4> 
<p>现在你可以通过使用 intenseTextStyle 配置文件设置来选择你希望紧凑文本在你的终端出现的方式。你可以选择粗体和亮体、仅粗体、仅亮体或无样式呈现文本。此设置也可以在 Profile Appearance 页面的 settings UI 中找到。</p> 
<pre><code>// Renders intense text as both bold and bright
"intenseTextStyle": "all"

// Renders intense text as bold
"intenseTextStyle": "bold"

// Renders intense text as bright
"intenseTextStyle": "bright"

// Renders intense text as normal
"intenseTextStyle": "none"</code></pre> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-44db8a14fcc1cec9d0792d18b858bbd65b0.gif" width="500" referrerpolicy="no-referrer"></p> 
<h4>Font features and axes</h4> 
<p>字体对象现在可以在 settings.json 文件中接受 OpenType features 和 axes。 关于 OpenType 的更多详细信息，可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Ftypography%2Fopentype%2Fspec%2Ffeaturelist" target="_blank">docs for features</a> 以及 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Ftypography%2Fopentype%2Fspec%2Fdvaraxisreg" target="_blank">docs for axes</a>。</p> 
<pre><code>// Enables ss01 and disables ligatures
"font": &#123;
    "face": "Cascadia Code",
    "features": &#123;
        "ss01": 1,
        "calt": 0
    &#125;
&#125;

// Sets the font to italic
"font": &#123;
    "face": "Cascadia Code",
    "axes": &#123;
        "ital": 1
    &#125;
&#125;</code></pre> 
<h4>对默认终端行为的更改</h4> 
<p>当通过默认终端设置启动终端时，终端现在将使用无配置文件而不是默认配置文件。当作为默认终端调用时，适用于终端的设置将由设置中的"默认"部分，或 profiles.defaults 的内容决定。此外，启动默认终端现在将遵循 windowingBehavior 设置。</p> 
<h4>在“+”按钮中拖放路径</h4> 
<p>你现在可以把目录和文件拖到"+"按钮上，然后用给定的起始路径打开一个新的标签、窗格或窗口。 默认为打开一个新标签；但当按住 Alt 键时，可以在一个新窗格中打开路径 ；按住 Shift 时，将打开一个新窗口。</p> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-27e9046680c6e3be16a295a649fa67b8ab1.gif" width="500" referrerpolicy="no-referrer"></p> 
<h4><strong>窗格更新</strong></h4> 
<p>此版本的窗格功能有了很多改进：</p> 
<ul> 
 <li>使用<code>movePane</code>动作，现在可以将窗格移动到新的或现有的标签。还可以使用命令面板来移动你的窗格。</li> 
 <li>使用<code>swapPane</code>动作，现在可以在一个选项卡中交换两个窗格的位置。</li> 
 <li>现在可以右键单击选项卡并选择拆分选项卡将活动配置文件拆分为新窗格。</li> 
</ul> 
<h2>设置界面更新</h2> 
<ul> 
 <li>非重点配置文件的新外观设置</li> 
</ul> 
<p><img alt height="293" src="https://oscimg.oschina.net/oscnet/up-d43a93a7e79ac23dd7f3213a531be3b95bf.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p>在为你的操作添加键时，现在只需键入 key chord，而不是拼出所有键（如 c-t-r-l）。</p> </li> 
</ul> 
<h4><strong>其他改进</strong></h4> 
<ul> 
 <li>现在可以删除动态生成的配置文件。</li> 
 <li>在较新版本的 Windows 上，<code>startingDirectory</code>现在可以在启动 WSL 配置文件时接受 Linux 路径。</li> 
 <li>用<code>wt</code>和默认 terminal 实例创建的标签现在将以启动的命令行作为其标题，而不是默认的配置文件名称。</li> 
 <li>现在可以使用<code>nextPane</code>和<code>previousPane</code>按创建顺序浏览窗格。</li> 
 <li>使用<code>move-focus</code>动作在窗格中导航效果更好，而且现在在启动时也可以正确工作。</li> 
 <li>添加了<code>toggleSplitOrientation</code>动作，它将一对窗格从垂直布局切换为水平布局。</li> 
 <li>任务栏现在将显示组合的所有窗格/标签组合的进度状态，无论哪个处于焦点。</li> 
 <li>你现在可以使用<code>sc()</code>和<code>vk()</code>来绑定按键，这使得更多的按键可以被绑定。</li> 
</ul> 
<h4>Bug fixes</h4> 
<ul> 
 <li> <p>Alt+Space 现在可以从系统菜单中解除绑定，以便你可以将 ESC Space 发送到终端。</p> </li> 
 <li> <p>将“quake”窗口抓取到另一个显示器上，现在可以正确地更新其大小。</p> </li> 
 <li> <p>nextTab 和 prevTab 动作现在可以在通过 wt 或命令调色板使用时正确工作。</p> </li> 
 <li> <p>initialPosition 现在考虑到了 window borders。</p> </li> 
 <li> <p>生成 WSL 发行版配置文件现在应该更稳定了。</p> </li> 
 <li> <p>默认的配置文件下拉菜单在滚动时将不再进入空间。</p> </li> 
</ul> 
<p>详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-terminal-preview-1-11-release%2F" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            