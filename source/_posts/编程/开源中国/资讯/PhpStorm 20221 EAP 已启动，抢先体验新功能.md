
---
title: 'PhpStorm 2022.1 EAP 已启动，抢先体验新功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0130/072637_XuuB_5430600.png'
author: 开源中国
comments: false
date: Sun, 30 Jan 2022 07:27:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0130/072637_XuuB_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#27282c">PhpStorm 2022.1 的早期访问计划 (</span>Early Access Program - <span style="color:#27282c">EAP)已启动，第一个 PhpStorm 2022.1 EAP 版本引入了全新的通知工具窗口、改进的 Markdown 支持、新的高级 PHP 元数据功能等，可在此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fphpstorm%2Fnextversion%2F" target="_blank">下载最新 EAP 版本</a>。</span></p> 
<h2 style="margin-left:0px">新的高级 PHP 元数据功能</h2> 
<p style="margin-left:0px">除了内置的“代码感知”能力，PhpStorm 还依赖于外部的代码知识。这些知识以 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2018%2F03%2Fhow-to-provide-stubs-for-phpstorm%2F" target="_blank">PHP 存根</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Fide-advanced-metadata.html" target="_blank"><strong>.phpstorm.meta.php</strong></a>文件的形式出现。</p> 
<h3 style="margin-left:0px">支持 magic __call 和 __callStatic</h3> 
<p style="margin-left:0px">之前如果你依赖 <span style="color:#27282c">magic 方法的 </span>__call 或者 __callStatic ，则可能失去其自动补全功能，因为这些方法未定义。在 2022.1 EAP 中，<span style="color:#27282c">可以添加相应的元数据条目，并获得此类调用的自动补全功能：</span></p> 
<p style="margin-left:0px"><img alt height="363" src="https://static.oschina.net/uploads/space/2022/0130/072637_XuuB_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px"><span style="color:#27282c">甚至可以自动处理动态调用，从参数值接收特定的方法名称：</span></p> 
<p style="margin-left:0px"><img alt height="286" src="https://static.oschina.net/uploads/space/2022/0130/073059_zdDJ_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">支持@|MyClass 类型</h3> 
<p style="margin-left:0px"><span style="color:#27282c">现在可以将联合类型指定为 @|MyClass ：</span></p> 
<p style="margin-left:0px"><img alt height="420" src="https://static.oschina.net/uploads/space/2022/0130/073032_NAlY_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Fide-advanced-metadata.html" target="_blank">在文档</a>中了解有关其他元数据功能的更多信息。</p> 
<h2 style="margin-left:0px">新的通知工具窗口</h2> 
<p style="margin-left:0px">用新的<em>通知 </em>工具窗口替换了<em>事件日志实例，</em>可以帮助用户更好地了解来自 IDE 的通知。默认情况下，新工具窗口位于 IDE 窗口的右下角，通知可以分为两类：<em>建议 </em>和 <em>时间线</em>。</p> 
<p style="margin-left:0px"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072700_FIFO_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px">Markdown 改进</h2> 
<ul> 
 <li>从 Markdown 文件运行命令</li> 
</ul> 
<p style="margin-left:0px"><span style="color:#27282c">README 文件一般用来描述一个软件的运行步骤，</span>PhpStorm 2022.1 将允许直接从这类 Markdown 文件运行命令 —— 只需单击命令左侧装订线中的 <em>运行 </em>图标即可。</p> 
<p style="margin-left:0px"><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072716_8ptv_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px">新选项可以通过 <em>Detect 命令进行管理，这些命令可以直接从 Preferences / Settings | </em>中的 Markdown 文件运行。</p> 
<ul> 
 <li>复制 Markdown 的代码片段</li> 
</ul> 
<p>新版本向 Markdown 块添加了一个新的<em>复制代码片段 </em>操作，可以快速复制 Markdown 的代码到剪贴板。</p> 
<p><img alt height="350" src="https://static.oschina.net/uploads/space/2022/0130/072730_2T9m_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px">LightEdit 模式下的代码重新格式化</h2> 
<p style="margin-left:0px">在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fphpstorm%2Flightedit-mode.html" target="_blank"><em>LightEdit </em>模式下</a>，无需创建或加载整个项目即可快速编辑文件。现在也可以在 <em>LightEdit </em>模式下重新格式化代码。</p> 
<p style="margin-left:0px">有关 PhpStorm 2022.1 EAP  的更多详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FWI-A-8%2FPhpStorm-2022.1-EAP-1-%28221.3427.92-build%29-Release-Notes" target="_blank">发行说明</a>中提供的完整更改列表。</p> 
<p style="margin-left:0px">发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2022%2F01%2Fphpstorm-2022-1-early-access-program-is-open%2F" target="_blank">https://blog.jetbrains.com/phpstorm/2022/01/phpstorm-2022-1-early-access-program-is-open/</a></p>
                                        </div>
                                      
</div>
            