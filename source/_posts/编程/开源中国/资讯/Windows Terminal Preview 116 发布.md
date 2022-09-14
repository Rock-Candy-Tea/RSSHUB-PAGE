
---
title: 'Windows Terminal Preview 1.16 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-dd8913f16390a3fbd079221f52cd7af16af.png'
author: 开源中国
comments: false
date: Wed, 14 Sep 2022 08:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-dd8913f16390a3fbd079221f52cd7af16af.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Windows Terminal Preview 1.16 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-terminal-preview-1-16-release%2F" target="_blank">发布</a>，具体更新内容如下：</p> 
<p><img alt height="333" src="https://oscimg.oschina.net/oscnet/up-dd8913f16390a3fbd079221f52cd7af16af.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">Theming</h2> 
<p>通过引入 themes，为用户增添了更多可自定义的可能</p> 
<p><img alt height="334" src="https://oscimg.oschina.net/oscnet/up-b382035a22c7182aff9da08db72a4ac82c9.png" width="500" referrerpolicy="no-referrer"></p> 
<p>themes 是一个全局属性，可以包含各种 themes 对象，这些对象将出现在设置用户界面的外观页面的主题下拉菜单中。下面是每个 themes 对象可以接受的对象。<strong style="color:#333333">注意：</strong>主题只能使用 JSON 文件进行编辑，但它们会出现在设置 UI 的主题下拉菜单中。</p> 
<p><img alt height="264" src="https://oscimg.oschina.net/oscnet/up-cc8aeab30dc35533e40e92aa3714db4c995.png" width="500" referrerpolicy="no-referrer"></p> 
<h3>Sample JSON</h3> 
<pre><code><span style="color:#0c6d22"><span style="color:#0c6d22">"themes"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> 
</span></span><span style="color:#666600"><span style="color:#666600">[</span></span><span style="color:#000000"><span style="color:#000000">
    </span></span><span style="color:#666600"><span style="color:#666600">&#123;</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"name"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"Grace Kelly"</span></span><span style="color:#666600"><span style="color:#666600">,</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"tab"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> 
        </span></span><span style="color:#666600"><span style="color:#666600">&#123;</span></span><span style="color:#000000"><span style="color:#000000">
            </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"background"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"#00515EFF"</span></span><span style="color:#666600"><span style="color:#666600">,</span></span><span style="color:#000000"><span style="color:#000000">
            </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"showCloseButton"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"always"</span></span><span style="color:#666600"><span style="color:#666600">,</span></span><span style="color:#000000"><span style="color:#000000">
            </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"unfocusedBackground"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#000088"><span style="color:#000088">null</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#666600"><span style="color:#666600">&#125;,</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"tabRow"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> 
        </span></span><span style="color:#666600"><span style="color:#666600">&#123;</span></span><span style="color:#000000"><span style="color:#000000">
            </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"background"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"#061612FF"</span></span><span style="color:#666600"><span style="color:#666600">,</span></span><span style="color:#000000"><span style="color:#000000">
            </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"unfocusedBackground"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"#061612FF"</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#666600"><span style="color:#666600">&#125;,</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"window"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> 
        </span></span><span style="color:#666600"><span style="color:#666600">&#123;</span></span><span style="color:#000000"><span style="color:#000000">
            </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"applicationTheme"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"dark"</span></span><span style="color:#000000"><span style="color:#000000">
        </span></span><span style="color:#666600"><span style="color:#666600">&#125;</span></span><span style="color:#000000"><span style="color:#000000">
    </span></span><span style="color:#666600"><span style="color:#666600">&#125;</span></span><span style="color:#000000"><span style="color:#000000">
</span></span><span style="color:#666600"><span style="color:#666600">]</span></span></code></pre> 
<h3><strong style="color:#333333">Tab</strong></h3> 
<p>可以通过主题对象内的 tab 对象来修改应用于 tab 的设置。tab 对象支持 background、unfocusedBackground 和 showCloseButton 属性。background 将设置 tab 活动时的背景颜色，并且总是以全不透明度显示颜色。unfocusedBackground 设置 tab 不活动时的颜色，showCloseButton 则切换 tab 上关闭按钮的外观。</p> 
<h3 style="text-align:left">Tab row</h3> 
<p>可以通过主题对象内的 tabRow 对象修改应用于 tab row 的设置。tabRow 对象支持 background 和 unfocusedBackground 属性。background 将设置窗口聚焦时 tab row 背景的颜色。unfocusedBackground 将设置非聚焦时 tab row 背景的颜色。</p> 
<h3 style="text-align:left">Window</h3> 
<p>可以通过主题对象内的 window 对象修改应用于 window 的设置。window 对象支持 applicationTheme。除非指定其他颜色，applicationTheme 将把选定的应用程序主题的颜色应用于终端窗口。</p> 
<h2>New default colors</h2> 
<p>修改了 Windows <span style="background-color:#ffffff; color:#333333">Terminal </span>中的一些默认颜色。默认终端使用 <span style="background-color:#ffffff; color:#333333">dark </span>主题，而不是遵循系统主题。</p> 
<h3><strong style="color:#333333">New colors</strong></h3> 
<p><img alt height="46" src="https://oscimg.oschina.net/oscnet/up-880bd79ef9d0f56494595dbbfd342906d00.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="46" src="https://oscimg.oschina.net/oscnet/up-d5d9942e3db372c921a46f5ab390df93522.png" width="500" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">Old colors</h3> 
<p><img alt height="44" src="https://oscimg.oschina.net/oscnet/up-44764338249030d01548c0e03b43c931d7e.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="44" src="https://oscimg.oschina.net/oscnet/up-b5e475df0c0d984bcadecd803c918f8877a.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的文本渲染引擎</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p>发布了新的实验性文本渲染引擎，你<span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可以为一个配置文件启用该功能（</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><code><span>experimental</span><span>.</span><span>useAtlasEngine</span></code><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>）。在这个版本中，开发团队将这个新的渲染器作为所有配置文件的默认文本渲染器。新的渲染器性能更强，现在支持额外的像素着色器（包括复古效果）、粗体字和下划线/上划线/超级链接线。如果你的机器没有GPU，或者你远程到一个没有 GPU 的虚拟机上，它将退回到一个不需要硬件支持的更高性能的模式。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span><span style="color:inherit">设置新 tabs 出现的位置</span></span></span></span></span></h2> 
<p><span><span>现在可以使用新的<code><span>newTabPosition</span></code>全局设置设置新 tabs 的打开位置。此设置也出现在设置 UI 的外观页面上。你您可以将新 tabs 设置为在所有 tabs 的末尾或当前选定的 tabs 之后打开。</span></span></p> 
<pre><span><span><span><span><span style="color:#212529"><span style="background-color:#f0f0f0 !important"><code><span><span style="color:#0c6d22"><span><span style="color:#0c6d22">"newTabPosition"</span></span></span></span><span><span style="color:#666600"><span><span style="color:#666600">:</span></span></span></span> <span><span style="color:#0c6d22"><span><span style="color:#0c6d22">"atTheEnd"</span></span></span></span><span><span style="color:#666600"><span><span style="color:#666600">,</span></span></span></span> <span><span style="color:#0c6d22"><span><span style="color:#0c6d22">"newTabPosition"</span></span></span></span><span><span style="color:#666600"><span><span style="color:#666600">:</span></span></span></span> <span><span style="color:#0c6d22"><span><span style="color:#0c6d22">"afterCurrentTab"</span></span></span></span></code></span></span></span></span></span></span></pre> 
<h2><span><span><span><span><span style="color:inherit">重新设计的配色方案页面</span></span></span></span></span></h2> 
<p><span><span>设计了一个更直观的配色方案页面。更新了设置 UI 配色方案页面以改进其 styling 和 user flow。还添加了“设置为默认”按钮，该按钮将在所有配置文件中应用一个配色方案作为你的默认配色方案。指定颜色方案的配置文件将使用其指定的方案而不是默认方案。</span></span></p> 
<h3 style="text-align:left">New design</h3> 
<p><img alt height="375" src="https://oscimg.oschina.net/oscnet/up-55adb2dfeb9bd956c70ca53415c38df434f.png" width="500" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">Old design</h3> 
<p><img alt height="366" src="https://oscimg.oschina.net/oscnet/up-e2fd0f59b27233766c5eb4a5e25a30e6dd0.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">New actions</h2> 
<h3 style="text-align:left">Expand selection to word</h3> 
<p>新的<span> </span><code><span>expandSelectionToWord</span></code><span> </span>action 扩展了一个文本选择的开头和结尾，以包括该选择所涉及的单词。</p> 
<pre><code><span style="color:#666600"><span style="color:#666600">&#123;</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"command"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#0c6d22"><span style="color:#0c6d22">"expandSelectionToWord"</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#666600"><span style="color:#666600">&#125;,</span></span></code></pre> 
<h2><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Mark mode 键绑定现在先于自定义键绑定。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 mark mode 下，现在可以在超链接之间使用 Tab 和 Shift+ Tab。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>调整无差别文本颜色的设置现在默认为启用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修改了默认的深色和浅色主题颜色，以在选项卡和文本缓冲区之间实现更无缝的外观。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>命令面板中的后退按钮现在返回到过滤操作列表中先前选择的项目。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<h2 style="text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>当 BEL 在 light terminal 中发出时，窗格中的 flash 现在将变暗而不是变亮。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>粘贴多行时，不再删除空格。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果终端由进程启动，<code><span>CloseOnExit</span></code>现在将在终止时自动关闭终端，否则终端将会以<code><span>graceful</span></code>行为关闭。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-terminal-preview-1-16-release%2F" target="_blank">查看官方博客</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            