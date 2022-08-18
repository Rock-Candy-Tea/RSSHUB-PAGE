
---
title: 'IntelliJ IDEA 2022.2.1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3286'
author: 开源中国
comments: false
date: Thu, 18 Aug 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3286'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA  2022.2 的第一个错误修复版本 2022.2.1 现已推出。Ubuntu 用户可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Ftoolbox-app%2F" target="_blank">Toolbox App</a> 或使用 snaps从 IDE 内部更新到此版本。也可以从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fidea%2Fdownload%2F" target="_blank">网站</a>下载。</p> 
<p style="margin-left:0px">此次要版本包括以下修复： </p> 
<ul> 
 <li>修复了导致包含非 ASCII 字符的美人鱼图预览渲染不正确的问题 。<span style="color:#27282c">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-289431%2F" target="_blank">IDEA-289431</a><span style="color:#27282c">]</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-166549%2F" target="_blank"> </a>正确支持 @SpringJUnitConfig 和 <em>@SpringJUnitWebConfig 注释。</em><span style="color:#27282c">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-166549%2F" target="_blank">IDEA-166549</a><span style="color:#27282c">]</span></li> 
 <li>修复了终端选项卡名称的问题。<span style="color:#27282c">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-297207%2FTerminal-tab-name-resets-when-activating" target="_blank">IDEA-297207</a><span style="color:#27282c">], </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-290225%2F" target="_blank">IDEA-290225</a><span style="color:#27282c">]</span></li> 
 <li>修复了使用 WSL时导致代码完成故障的问题。<span style="color:#27282c">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-297761" target="_blank">IDEA-297761</a><span style="color:#27282c">]</span></li> 
 <li>修复了在编辑标题并使用 Delete 键时，导致 shelf 条目被删除的问题。<span style="color:#27282c">[</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-293846%2F" target="_blank">IDEA-293846</a><span style="color:#27282c">]</span></li> 
 <li>修复了打开多个项目时，“<em>管理项目</em>”弹出窗口中的“<em>最近项目</em>”列表不正确的问题。 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-298207%2F" target="_blank">IDEA-298207</a>]</li> 
 <li>修复了在运行使用 JDK 18 的 Java 项目时，导致控制台输出的非 ASCII 字符不正确呈现的问题。[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-291006%2FRunning-the-Java-project-by-using-the-JDK-18-prints-the-garbled-characters-in-console-when-try-printing-the-non-ASCII-characters" target="_blank">IDEA-291006</a>]</li> 
 <li>修复了导致 <em>Search Everywhere </em>的文本结果不出现在“<em>查找”</em>工具窗口中的问题。 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-297670%2FText-results-from-Search-Everywhere-are-not-displayed-in-Find-tool-window" target="_blank">IDEA-297670</a>]</li> 
 <li>解决了在导入使用 JDK 1.7 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-298673%2FError-importing-maven-project-bound-to-max-JDK-17" target="_blank">IDEA-298673</a> ] 的 Maven 项目时导致 IDE 报告错误的问题。尽管从 v2022.2 开始，运行 Maven 集成代码至少需要 JDK 8，但此更改不会影响项目 JDK 设置或语言级别。JDK 1.7 仍然可以不受限制地使用。如果 Maven 项目导入器指向 JDK 1.7，它会默默地回退到 IDEA 的捆绑运行时。</li> 
</ul> 
<p style="margin-left:0px">有关详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-264%2FIntelliJ-IDEA-202221-222373954-build-Release-Notes" target="_blank">发行说明</a>。</p>
                                        </div>
                                      
</div>
            