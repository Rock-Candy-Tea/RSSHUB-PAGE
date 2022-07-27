
---
title: 'IntelliJ IDEA 2022.2 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202207/27072912_yh3S.png'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 07:29:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202207/27072912_yh3S.png'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.2 为远程开发功能带来了多项质量改进，使其更美观、更稳定。 从 v2022.2 开始，IntelliJ IDEA 使用 JetBrains Runtime 17，后者可以从多方面增强 IDE 体验和性能。 IntelliJ IDEA Ultimate 添加了对 Spring 6 和 Spring Boot 3 功能的支持，也为多个其他框架引入了更新。 新版本还具有多项值得注意的升级和改进，具体内容如下：</p> 
<h2>主要更新</h2> 
<h3>远程开发改进</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/RD.png" src="https://static.oschina.net/uploads/img/202207/27072912_yh3S.png" referrerpolicy="no-referrer"></p> 
<p>IntelliJ IDEA 2022.2 中为远程开发引入了大量重大升级，让体验更稳定、功能更丰富。 新发布的更新具有多项质量改进。通过 SSH 将笔记本电脑连接到安装在远程服务器中的 IntelliJ IDEA，获得流畅的开发者体验。 如果您使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fzh-cn%2Fremote-development%2Fspace-dev-environments%2F" target="_blank">JetBrains Space</a> 在新版本中高效地编排后端，可以直接从 IntelliJ IDEA 管理开发环境。</p> 
<h3>从 JBR 11 转换到 JBR 17</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/JBR17.png" src="https://static.oschina.net/uploads/img/202207/27072912_7kj5.png" referrerpolicy="no-referrer"></p> 
<p>从 v2022.2 开始，所有 IntelliJ IDEA 更新都附带 JetBrains Runtime 17 (JBR 17)。这将显著提升 IDE 性能和安全性，同时，得益于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.apple.com%2Fmetal%2F" target="_blank">Metal API</a>，这还将增强 macOS 上的渲染性能。</p> 
<h3>对 Spring 6 和 Spring Boot 3 功能的支持</h3> 
<p>IntelliJ IDEA 2022.2 现已完全支持 Spring 6 和 Spring Boot 3 功能，包括新的 <code>@AutoConfiguration</code> 类和 <code>@ConfigurationProperties</code> 类，涵盖新的构造函数绑定语法，无需显式 <code>@ConstructorBinding</code>。</p> 
<h2>用户体验</h2> 
<h3>运行当前文件</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/Run_Current_File.png" src="https://static.oschina.net/uploads/img/202207/27072912_w9wg.png" referrerpolicy="no-referrer"></p> 
<p>Run/Debug（运行/调试）微件新增了 Run Current File（运行当前文件）功能，可供在没有专门的运行配置的情况下轻松运行和调试单个文件。 通过它运行和调试当前打开的文件时，IDE 将自动使用最适合该文件的运行配置类型。</p> 
<h3>全局更改字体大小的键盘快捷键</h3> 
<p>新增的键盘快捷键可以更改编辑器中所有位置的字体大小。 要增大字体，请按 ⌃⇧Period。 要减小字体，请按 ⌃⇧Comma。 此外还有一个字体大小指示器，它会显示当前字体大小并提供将其恢复为默认值的选项。</p> 
<h3>macOS 上的 Merge All Project Windows（合并所有项目窗口）操作</h3> 
<p>新版本为 macOS 用户引入了一项功能，利用此功能可以将所有打开的项目窗口合并成一个，将其变成选项卡。 转到 Window | Merge All Project Windows（窗口 | 合并所有项目窗口）即可执行此操作。</p> 
<h3>高亮显示检查的增强配置</h3> 
<p>现在，无需更改严重性级别即可配置配置检查在编辑器中的显示方式。 如需更改检查高亮显示样式，可以使用新的 Highlighting in editor（编辑器中的高亮显示）下拉菜单进行设置，该菜单清楚显示了所有可用选项。</p> 
<h3>Welcome（欢迎）屏幕上的 Cloning repository（正在克隆仓库）进度条</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/Cloning_repository_progress_bar.png" src="https://static.oschina.net/uploads/img/202207/27072913_Ozr9.png" referrerpolicy="no-referrer"></p> 
<p>Cloning repository（正在克隆仓库）进度条现在位于 IDE 的 Welcome（欢迎）屏幕上，并直接显示在 Projects（项目）列表中，更清晰、更易用。</p> 
<h3>助记书签的新 Description（描述）字段</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/Mnemonic_bookmarks.png" src="https://static.oschina.net/uploads/img/202207/27072913_PrLm.png" referrerpolicy="no-referrer"></p> 
<p>Add Mnemonic Bookmark（添加助记书签）对话框现已升级，增加了 Description（描述）字段，现在可以使用该字段直接向书签添加描述。</p> 
<h2>编辑器</h2> 
<h3>禁用自动块注释结束的新设置</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/block_comment_closure.png" src="https://static.oschina.net/uploads/img/202207/27072914_fpNX.png" referrerpolicy="no-referrer"></p> 
<p>现在，可以在按 Enter 键后禁用自动块注释结束。 为此，请转到 Settings / Preferences | Editor | Smart Keys（设置/偏好设置 | 编辑器 | 智能按键），取消选中 Enter 版块中的 Close block comment（结束块注释）复选框。</p> 
<h3>更快访问 Code Completion Settings（代码补全设置）</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/code_completion_settings.png" src="https://static.oschina.net/uploads/img/202207/27072914_8eiQ.png" referrerpolicy="no-referrer"></p> 
<p>现在，可以直接从代码补全弹出窗口中的垂直省略号菜单按钮访问 Code Completion Settings（代码补全设置）并配置偏好设置。</p> 
<h3>调整文件类型关联的新通知面板</h3> 
<p>当文件错误地与纯文本显式关联时，IntelliJ IDEA 现在会在通知中说明错误的文件类型关联并建议直接从编辑器中将其重置，无需在 Settings / Preferences（设置/偏好设置）中手动操作。</p> 
<h3>在 Markdown 文件中生成目录的新操作</h3> 
<p>现在，在 Markdown 文件中可以根据文档标题轻松生成目录。 新操作位于 Insert（插入）和 Generate（生成）弹出菜单中，可以通过 ⌘N 快捷键或右键点击调用。 IDE 将在当前文本光标处插入目录并以 <code>
  <!-- TOC --></code> 标记将其括起，后续调用相同的菜单可以对其进行更新。</p> 
<h2>Java</h2> 
<h3>改进的检查和代码补全</h3> 
<p>新版本对 Java 检查实现了一系列更改，这些更改有助于跟踪潜在错误和简化代码。 例如， Standard ‘Charset’ object can be used（可以使用标准 'Charset' 对象）检查已得到改进，现在可以识别 <code>.name()</code> 和 <code>.toString()</code>。 IDE 现在可以在模式变量隐藏字段时发出警告，还会捕获无意义的 <code>Objects.requireNonNullElse</code> 调用。 大量 JUnit 相关 Java 检查已转换为 JVM 检查，因此，它们现在也可以在 Kotlin 中使用。 此外，代码补全现在会在适用时建议 .class 文字。</p> 
<h2>Kotlin</h2> 
<h3>对 Kotlin 1.7.0 功能的支持</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/Support_for_Kotlin_1.7.0_features.png" src="https://static.oschina.net/uploads/img/202207/27072914_X1ZB.png" referrerpolicy="no-referrer"></p> 
<p>添加了对最新语言版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fwhatsnew17.html" target="_blank">Kotlin 1.7.0</a> 中引入的功能的支持。 IDE 现在可以正确呈现绝对不可空的类型，并提供选择加入要求的实用检查。</p> 
<h3>Kotlin 调试器中对数据流分析的支持</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/DFA_and_Kotlin_debugger.png" src="https://static.oschina.net/uploads/img/202207/27072914_xGuo.png" referrerpolicy="no-referrer"></p> 
<p>已将 Kotlin 调试器与数据流分析功能集成，因此现在它可以在 DFA 提示中显示哪些条件为 true 以及哪些分支将被执行。 先前，此集成<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2020%2F01%2Fdfa-debugger%2F" target="_blank">仅适用于 Java</a>，而现在也支持 Kotlin。</p> 
<h3>IntelliJ IDEA 原生构建器使用项目中配置的 Kotlin 编译器版本</h3> 
<p>从 v2022.2 开始，捆绑的 Kotlin 编译器不再与 IntelliJ IDEA 原生构建器搭配使用。本地和 CI 构建都将通过项目设置中声明的 Kotlin 编译器版本运行。这一更改消除了此前由于捆绑的编译器版本与项目构建文件中定义的版本不匹配而导致的本地和 CI 构建的不一致问题。</p> 
<h3>针对 Kotlin 改进的 IDE 性能</h3> 
<p>最近的索引优化工作对 IDE 在代码高亮显示、补全和 Find Usages（查找用法）方面的速度和性能产生了积极影响。</p> 
<h2>Groovy</h2> 
<h3>对 GINQ 的支持</h3> 
<p><img alt="https://www.jetbrains.com/idea/whatsnew/2022-2/img/Groovy_4.png" src="https://static.oschina.net/uploads/img/202207/27072914_kvgQ.png" referrerpolicy="no-referrer"></p> 
<p>添加了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroovy-lang.org%2Fusing-ginq.html%23_ginq_a_k_a_groovy_integrated_query" target="_blank">Groovy-Integrated Queries (GINQ)</a> 的支持。 IDE 现在为 Groovy 4 的此功能提供了语法高亮显示、代码补全和检查。</p> 
<h2>安全性</h2> 
<h3>导入受信任的 SSL 证书</h3> 
<p>IntelliJ IDEA 2022.2 现在可以帮助您从系统受信任存储区导入受信任的 SSL 证书。 它将自动使用特定于企业环境的自定义证书。 一切都开箱即用，无需额外操作。</p> 
<h2>Docker</h2> 
<h3>Testcontainers 的测试中 Docker 镜像补全</h3> 
<p>IntelliJ IDEA 2022.2 为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.testcontainers.org%2F" target="_blank">Testcontainers</a> API 引入了镜像补全，Testcontainers 包括所有可用 Docker 镜像及其版本。 点击引用即可在 Web 浏览器中打开相应的 Docker Hub URL。</p> 
<h3>上传本地 Docker 镜像到 Minikube 和其他连接</h3> 
<p>可以使用新的 Copy Docker Image（复制 Docker 镜像）操作将镜像从一个 Docker 守护进程复制到另一个，该操作会将镜像保存到文件中，然后将其推送到所选连接。</p> 
<h3>IDE 重启时 Docker 自动连接</h3> 
<p>重新启动 IDE 后，IntelliJ IDEA 2022.2 现在会自动连接到 Docker。 此新设置默认启用，也可以在 Settings / Preferences | Advanced Settings | Docker（设置/偏好设置 | 高级设置 | Docker）中进行切换。</p> 
<h3>不同 Docker 守护进程的 Docker 连接选项</h3> 
<p>从 v2022.2 开始，IntelliJ IDEA 与 Colima 和 Rancher 集成，支持更多用于建立与 Docker 守护进程的连接的选项。</p> 
<h2>QA 工具</h2> 
<h3>Page Object Editor 中的改进网页结构</h3> 
<p>网页结构 UI 得到了显著改进。 得益于文本格式高亮显示，可以轻松阅读最重要的部分，例如标记名称、ID 和应用的 CSS 类。</p> 
<h3>通过间距图标轻松导航</h3> 
<p>只需点击间距中的图标即可轻松导航回页面元素。</p> 
<h3>来自 URL 的页面对象命名</h3> 
<p>创建新的页面对象文件时，向导现在将提供一个可选的 URL 字段。 如果包含 Web 地址，向导会根据链接地址建议页面对象文件名。 此外，当 Page Object Editor 打开时，会自动加载插入的 URL。</p> 
<h3>文本光标自动移动到代码块末尾</h3> 
<p>在代码中添加新的页面元素时，文本光标现在将自动移动到添加的代码块的末尾，这样，您可以轻松导航并继续编辑。</p> 
<h3>从上下文菜单创建新的页面对象</h3> 
<p>在处理现有页面对象类时如果输入了新的非引用页面对象类，只需导航到警告的上下文菜单并创建新的页面对象即可修正未解决的代码警告。</p> 
<h2>Scala</h2> 
<h3>更出色的 Scala 3 支持</h3> 
<p>从 v2022.2 开始，IntelliJ IDEA 可以从 .tasty 文件读取 match 类型，正确解析类型，解析类型变量，将其用作类型实参，支持检查，以及将类型显示为文本。 另外，我们添加的支持还覆盖 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scala-lang.org%2Fscala3%2Freference%2Fchanged-features%2Fpattern-matching.html" target="_blank">无选项提取器</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scala-lang.org%2Fscala3%2Freference%2Fnew-types%2Ftype-lambdas.html" target="_blank">类型 lambda</a> 和*<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scala-lang.org%2Fscala3%2Freference%2Fnew-types%2Fpolymorphic-function-types.html" target="_blank">多态函数类型</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.scala-lang.org%2Fscala3%2Freference%2Fmetaprogramming%2Fcompiletime-ops.html%23the-scalacompiletimeops-package" target="_blank">类型级编译器内在函数</a>*以及作为通配符与 <code>_</code> 一起在 Scala 2.13.9 和 2.12.16 中使用的 <code>?</code>。 复制粘贴的代码现在也可正确缩进。</p> 
<h3>新的 Scala 检查</h3> 
<p>在匿名函数内部使用 <code>return</code> 关键字跳出函数而不执行其中的所有代码时，IntelliJ IDEA 2022.2 现在会发出警告。 这通常不是预期用法，并且可能导致泄漏的实现和隐藏的性能开销。 当 private 或 class 形参隐藏超类变量时将触发新警告。 此外，试图以编译器禁止的方式覆盖变量时会显示错误。 如果存在对应编译器选项（<code>-Xlint:nonlocal-return</code> 和 <code>-Xlint:private-shadow</code>），可以将这些新警告配置为显示。</p> 
<h3>将逗号分隔的元素列表拆分为单独的行</h3> 
<p>如果代码行因包含集合中的实参或元素列表而过长，您可以使用弹出菜单中的 Put arguments on separate lines（将实参放在单独的行中）操作快速将列表拆分为多个行。 同样，如果认为多行列表较短，可以使用 Put arguments on one line（将实参放在同一行中）操作将其合为一行。</p> 
<h3>适用于 Scala 的基于编译器的高亮显示</h3> 
<p>为了实现更好的资源利用，基于编译器的高亮显示已有所调整。 IDE 现在将考虑用户定义的文件高亮显示设置。 编译现在将更少触发并使用更少的后台线程。 编译范围已缩小到相关模块和源代码范围。</p> 
<h3>Safe Delete（安全删除）现在可用于类型形参</h3> 
<p>Safe Delete（安全删除）操作可以从定义及其所有调用中移除一个元素。 此操作现在也适用于类型形参。</p> 
<h2>其他</h2> 
<ul> 
 <li>IntelliJ IDEA 现在支持 Android Studio Chipmunk | 2021.2.1。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F07%2Fintellij-idea-2022-2%2F" target="_blank">https://blog.jetbrains.com/idea/2022/07/intellij-idea-2022-2/</a></p>
                                        </div>
                                      
</div>
            