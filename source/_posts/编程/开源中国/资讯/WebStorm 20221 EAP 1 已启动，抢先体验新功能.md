
---
title: 'WebStorm 2022.1 EAP 1 已启动，抢先体验新功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0130/074700_Cs7w_5430600.gif'
author: 开源中国
comments: false
date: Sun, 30 Jan 2022 07:51:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0130/074700_Cs7w_5430600.gif'
---

<div>   
<div class="content">
                                                                                            <p>WebStorm <span style="background-color:#ffffff; color:#27282c">2022.1 的早期访问计划 (</span><span style="background-color:#ffffff; color:#333333">Early Access Program -<span> </span></span><span style="background-color:#ffffff; color:#27282c">EAP)已启动，用户可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fwebstorm%2Fnextversion" target="_blank">在此下载</a>，尝试该 IDE 的最新特性。</span></p> 
<p>注意：由于是抢先体验版本，WebStorm EAP 的构建未经过全面测试，功能可能不稳定。</p> 
<h2 style="margin-left:0px">Join Lines 操作适用于嵌套 if 的语句</h2> 
<p style="margin-left:0px">此前 WebStorm 允许使用 Join Lines 操作（<em>⌃⇧J / Ctrl+Shift+J ）</em>连接代码行或代码块，现在该操作也适用于嵌套的 if 语句 ，产生与 Merge if 语句相同的效果。</p> 
<p style="margin-left:0px">此外，当你在 if, while, for-of 和其他类似的单行语句块上使用 Join Lines 操作时，WebStorm 会删除多余的大括号。</p> 
<p><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/074700_Cs7w_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3>合并 Flow 和 Problems 工具窗口</h3> 
<p>该版本将 Flow 语言服务集成到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fwebstorm%2Fresolving-problems.html%23apply-quick-fixes" target="_blank"><em>Problems </em>工具窗口</a> 中，并删除了专用的 <em>Flow </em>工具窗口，以帮助开发者从一个位置查看代码中的所有关键问题。</p> 
<p><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/075047_9e9M_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p>要访问以前在 <em>Flow </em>工具窗口中可用的一些按钮，可以使用状态栏上的新 <em>Flow 小部件。</em>从那里可以重新启动 Flow 服务并跳转到配置设置。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新的通知工具窗口</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">用新的<em>通知<span> </span></em>工具窗口替换了<em>事件日志实例，</em>可以帮助用户更好地了解来自 IDE 的通知。默认情况下，新工具窗口位于 IDE 窗口的右下角，通知可以分为两类：<em>建议<span> </span></em>和<span> </span><em>时间线</em>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072700_FIFO_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Markdown 改进</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>从 Markdown 文件运行命令</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#27282c">README 文件一般用来描述一个软件的运行步骤，</span>PhpStorm 2022.1 将允许直接从这类 Markdown 文件运行命令 —— 只需单击命令左侧装订线中的<span> </span><em>运行<span> </span></em>图标即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072716_8ptv_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新选项可以通过<span> </span><em>Detect 命令进行管理，这些命令可以直接从 Preferences / Settings |<span> </span></em>中的 Markdown 文件运行。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>复制 Markdown 的代码片段</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本向 Markdown 块添加了一个新的<em>复制代码片段<span> </span></em>操作，可以快速复制 Markdown 的代码到剪贴板。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072730_2T9m_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">LightEdit 模式下的代码重新格式化</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Flightedit-mode.html" target="_blank"><em>LightEdit<span> </span></em>模式下</a>，无需创建或加载整个项目即可快速编辑文件。现在也可以在<span> </span><em>LightEdit<span> </span></em>模式下重新格式化代码。</p> 
<p style="margin-left:0px">从 WebStorm 中删除了<em>HTML4 </em>和 <em>XHTML </em>的文件模板，因为它们未被广泛使用。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-54062" target="_blank">WEB-54062</a> )</p> 
<p style="margin-left:0px">现在可以将拆分选项卡配置为具有相同的宽度。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-231376" target="_blank">IDEA-231376</a> )</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fwebstorm%2Fcommand-line-formatter.html" target="_blank">命令行格式化程序</a>现在支持空运行模式，用于验证项目文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-181641" target="_blank">IDEA-181641</a> )。</li> 
 <li><em>提交详细信息 </em>窗格现在包含有关 GPG 签名和构建状态的信息。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-278968" target="_blank">IDEA-278968</a> )</li> 
</ul> 
<p>关于 WebStorm 2022.1 EAP #1 中最新改进的完整列表，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconfluence.jetbrains.com%2Fdisplay%2FWI%2FWebStorm%2B221.3427.92%2BRelease%2BNotes" target="_blank">发行说明</a>。</p> 
<p>发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fwebstorm%2F2022%2F01%2Fwebstorm-2022-1-eap-1%2F" target="_blank">https://blog.jetbrains.com/webstorm/2022/01/webstorm-2022-1-eap-1/</a></p>
                                        </div>
                                      
</div>
            