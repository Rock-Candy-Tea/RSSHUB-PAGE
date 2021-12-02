
---
title: 'IntelliJ IDEA 2021.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1413cbaf6916e2f43efd2d180f97c2bdcc3.png'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 07:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1413cbaf6916e2f43efd2d180f97c2bdcc3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">IntelliJ IDEA 2021.3 现已发布，这是 </span><span style="background-color:#ffffff; color:#27282c">2021 年的最后一个版本。此版本提供了一些新的功能和质量改进，以提升用户体验。</span></p> 
<p><span style="background-color:#ffffff; color:#27282c"><img alt height="234" src="https://oscimg.oschina.net/oscnet/up-1413cbaf6916e2f43efd2d180f97c2bdcc3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#ffffff; color:#333333">具体</span>更新内容如下：</p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>关键更新</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持远程开发。<span style="background-color:#ffffff; color:#27282c">此功能允许软件工程师连接到运行 IDE 后端的远程计算机，并像在本地机器上一样处理位于该端的项目。</span></li> 
 <li><span style="background-color:#ffffff; color:#27282c">查看诊断和修复 IDE 问题的新的、更快的方法。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">Smart Step Into action<span> </span></span>现在适用于 Kotlin 代码。它允许你使用链式方法调用和 lambda 来调试表达式，突出显示你可以进入的方法和 lambda。它允许你调试一个带有链式方法调用和 lambdas 的表达式，突出显示你可以 step into 的方法和 lambdas。</li> 
 <li>调试器可以检测 Kotlin 内联函数，并在堆栈跟踪面板中显示内联函数调用。</li> 
 <li>Kotlin 的新 Constant conditions inspection。</li> 
</ul> 
<p><strong>编辑器</strong></p> 
<ul> 
 <li>可以使用 macOS 上的 ⌘+鼠标滚轮<em> </em>或 Windows 和 Linux 上的 Ctrl+鼠标滚轮 同时更改所有打开的 tab 中的字体大小。</li> 
 <li>现在可以轻松地在 Markdown 文件中插入表格。</li> 
 <li>使用 editor tabs 变得更容易。只需单击 tab 窗格右上角的三个点即可访问所有 tab actions。</li> 
 <li>意图预览现在适用于 Kotlin 中的更多意图操作和快速修复，并显示不支持预览的意图操作的 HTML 描述。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>用户体验</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>当你在 macOS 上使用 F3 快捷方式或在 Windows 和 Linux上使用 F11 时，你的文件、文件夹和类将出现在新的 Bookmarks 工具窗口中。</li> 
 <li>已经可以使用选项卡拆分运行工具窗口。这允许你同时运行多个配置并查看所有结果。</li> 
 <li>在搜索操作时，IntelliJ IDEA 中的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Fsearching-everywhere.html" target="_blank">Search Everywhere</a> 使用机器学习对结果进行排序。</li> 
 <li>New Project wizard 窗口中重新设计的 Empty Project 节点允许你创建一个基本项目来处理不同类型的单独文件，你还可以在其中添加 Java 和 Kotlin 类。</li> 
 <li>新的 Multi-Module Project 节点可让你从头开始创建具有复杂结构的项目。</li> 
 <li>默认情况下，当你使用 macOS 上的 ⌥ F7 或 Windows 和 Linux 上的 Alt+F7 搜索方法实现的用法时，IntelliJ IDEA 现在使用顶级层次结构方法作为目标。</li> 
 <li>“Show Usages”对话框现在包括每个找到的用法的源代码预览、更改搜索范围的功能以及查看你正在搜索的代码元素类型和找到的用法数量的选项。</li> 
</ul> 
<p><strong>Java</strong></p> 
<ul> 
 <li>IntelliJ IDEA 添加了一个新的检查“Non-safe string passed to a safe method”，这有助于避免在使用org.checkerframework.checker.tainting.qual注释的项目中把不安全的数据传递到安全方法。可以通过这个检查发现的问题包括 SQL 注入和 XSS 缺陷。</li> 
 <li>添加了两个可以帮助简化代码的新检查。第一个建议你将 collect(toList()) 替换为 .toList()<em>。</em>可以在 Java 16 及更高版本中使用它。另一个检查提示你将 collection.addAll(List.of(“x”)) 替换为 collection.add(x)，并将 map.putAll(Map.of(“a”, “b”)) 替换为 map.put(“a”, “b”)。</li> 
 <li>在 Java 中引入局部变量的设置不再出现在弹出窗口中，用于隐藏你正在编写的代码。现在可以通过变量旁边的齿轮图标或使用 macOS 上的<em> </em>⌥+⇧ +O 快捷方式或 Windows 上的 Alt+Shift+ O <em>来</em>访问它们。</li> 
 <li>当调用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Fextract-parameter.html" target="_blank">Introduce 参数</a>重构时，IDE 会询问你要替换出现的位置。在你做出选择后，将出现一个齿轮图标，允许你为重构配置更多设置。</li> 
 <li>你可以在 Run/Debug Configurations 对话框中，通过选择 Modify options | Modify classpath，以每个配置为基础定义自定义classpath。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>Kotlin</strong></p> 
<ul> 
 <li>引入了新的重构，可让你在 Kotlin 中提取常量。</li> 
 <li>非阻塞上下文检查中的可能阻塞调用现在可自定义，涵盖更多情况，并提供快速修复。</li> 
 <li>添加了内联提示，使用简单的数学符号来解释范围内的单词或符号的作用。</li> 
 <li>通过为所有字段添加工具提示、删除一些不受欢迎的模板并添加一个新模板来让你创建 Compose Web 应用程序并简化项目设置步骤，重新设计了 New Project<span style="background-color:#ffffff; color:#27282c"><span> </span>wizard </span>的布局。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>JavaScript</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>直接从编辑器将你的 npm 包更新到最新版本。</li> 
 <li>代码完成在 HTML 中的工作方式已得到改进。每当你在编辑器中键入标签名称或缩写或调用代码完成时，IntelliJ IDEA 都会立即向你显示相关建议。</li> 
</ul> 
<p><strong>Scala </strong></p> 
<ul> 
 <li>此版本的一大重点是对 Scala 3 的支持。添加了高亮显示，导航和自动完成的功能，包括结束标记、给定、使用和导出关键字、soft keywords 和 quiet syntax。此外，TASTy 阅读器现在可以解析包对象，以及更高类型的 variance 和 bounds。</li> 
 <li>Scala 3/Scala 2 交叉编译项目可以作为 Scala 2 项目打开。</li> 
 <li>Scala 插件现在支持数据流分析，可以帮助你更轻松地检测编程错误。</li> 
 <li>Scala 编译器选项现在可以自动完成，你甚至可以查看每个选项的 Quick Documentation。</li> 
 <li>嵌入提示可用于 Scala 中的范围。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了对 Android Studio Arctic Fox 2020.3.1 的支持。</li> 
 <li>IntelliJ IDEA 现在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-275560" target="_blank">支持 Groovy 4</a>，包括成熟的代码洞察、功能检查和意图操作。还支持其他功能，例如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroovy-lang.org%2Freleasenotes%2Fgroovy-4.0.html" target="_blank">switch 表达式和密封类型</a>。</li> 
</ul> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2021%2F11%2Fintellij-idea-2021-3%2F" target="_blank">查看官方博客</a>。 </p>
                                        </div>
                                      
</div>
            