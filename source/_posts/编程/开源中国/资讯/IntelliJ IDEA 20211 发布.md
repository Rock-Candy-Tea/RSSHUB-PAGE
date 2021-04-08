
---
title: 'IntelliJ IDEA 2021.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8c6d8753f4057785c31a338b34890b391cf.png'
author: 开源中国
comments: false
date: Thu, 08 Apr 2021 00:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8c6d8753f4057785c31a338b34890b391cf.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>IntelliJ IDEA 2021.1 现已发布。该版本解决了一些麻烦的问题，并引入了许多新功能。现在，用户可以在 WSL 2 中与其 Java 项目一起工作、使用集成的 Space、直接从 IDE 安排视频通话以使用 Code With Me 进行协作开发，并在 SSH 主机和 Docker 容器中运行代码。同时，该版本还增加了对 Java 16 的基本支持、一些有用的新检查，以及 IDE 内部的 HTML 预览窗口。</p> 
<p><img alt height="350" src="https://oscimg.oschina.net/oscnet/up-8c6d8753f4057785c31a338b34890b391cf.png" width="700" referrerpolicy="no-referrer"></p> 
<p>具体更新内容如下：</p> 
<h4><strong>关键更新</strong></h4> 
<ul> 
 <li>一旦你在 JetBrains Space 中登录到你的组织，你就可以查看和克隆项目仓库，审查你的队友的代码，并编写 Space 自动化脚本。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fspace%2F2021%2F04%2F07%2Fspace-code-reviews-in-intellij-idea-2021-1%2F" target="_blank">了解更多</a>。</li> 
 <li>支持 WSL 2 for Java projects。</li> 
 <li>Code With Me，一个用于协作开发和配对编程的服务，现在开箱即用，具有视频和音频通话功能。</li> 
 <li>新的 Run Targets 功能允许你在 Docker 容器或远程机器上运行、测试、配置文件和调试您的应用程序</li> 
</ul> 
<h4><strong>User experience</strong></h4> 
<ul> 
 <li>你的 IDE 具有内置的 HTML 文件浏览器预览功能。当你改变你的 HTML 或链接的 CSS 和 JavaScript 文件时，预览会实时更新。</li> 
 <li>可以在搜索范围中包括或排除外部依赖关系。</li> 
 <li>标记了几个 UI 和 gutter elements，以便使用已启用的屏幕阅读器正确读取这些元素。</li> 
 <li>如果在 Windows 上使用高对比度模式，则 IDE 会在首次启动时自动应用高对比度主题。</li> 
 <li>如果你是 Windows 用户，则可以通过右键单击任务栏或“开始”菜单上的 IntelliJ IDEA 图标来打开最近的项目。</li> 
</ul> 
<h4><strong>Version Control</strong></h4> 
<ul> 
 <li>这个版本为 Pull Request 引入了一些更新，包括更快的创建速度、快速打开 in-editor diff 的能力，以及对 pull request 模板的支持。</li> 
 <li>增加了对 Git commit templates 的支持，你可以在 commit message 中列出需要的自定义信息。</li> 
 <li>现在，你可以在提交更改到 VCS 之前轻松地选择代码检查配置文件--只需点击齿轮图标来显示提交选项，勾选分析代码复选框，点击选择配置文件，然后选择所需的配置文件。</li> 
 <li>在"<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Fcomparing-file-versions.html%23compare-revisions-another-branch" target="_blank">Compare with branch</a>"对话框的"Show diff"旁边的新的向下箭头图标允许你从另一个分支获取文件。</li> 
 <li>通过新的“Save to Shelf”操作，可以将你的更改复制到 Shelf，同时将它们保留在本地更改中。</li> 
 <li>Perforce 插件现在与 IntelliJ IDEA 社区版完全兼容，并与你的 IDE 捆绑在一起。</li> 
</ul> 
<h4><strong>Editor</strong></h4> 
<ul> 
 <li>在 Preferences / Settings | Editor | Fonts 中的新排版设置，让你可以微调主字体和粗体字体的重量。</li> 
 <li>每当打开几个用于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2020%2F10%2Fintellij-idea-2020-3-eap-3-debugger-inline-watches-reader-mode-and-more%2F" target="_blank">垂直拆分编辑器的</a>选项卡时，你都可以双击其中一个以最大化该特定选项卡的编辑器窗口。</li> 
 <li>你的 IDE 支持使用 Goessner 或 Jayway 语法的 JSONPath 表达式。新的 Evaluate JSONPath Expression action 用于在 JSONPath 中编写查询并测试它们，可通过 Edit | Find 进行。</li> 
 <li>IntelliJ IDEA 支持 JSON Lines 格式，可识别.jsonl、.jslines、.ldjson和.ndjson文件类型。</li> 
</ul> 
<h4><strong>Profiler</strong></h4> 
<ul> 
 <li>重新设计了Profiler UI，并添加了两个新操作，你可以通过右键单击正在运行的应用程序来访问它们。Capture Memory Snapshot action 允许你采取 *.hprof snapshots 你的应用程序，和 CPU 和内存实时图表打开一个选项卡，用于跟踪和可视化资源消耗的工具。</li> 
</ul> 
<h4><strong>Java</strong></h4> 
<ul> 
 <li>IntelliJ IDEA 具有对 Java 16 的基本支持，该支持于2021年3月发布。</li> 
 <li>添加了几项新检查，包括用于数据流分析的检查。</li> 
 <li>为 chained builder 方法引入了新的 formatting 选项，以帮助提高其可读性。</li> 
</ul> 
<h4><strong>Database tools</strong></h4> 
<ul> 
 <li>在修改对象时添加了一个用于编辑授权的用户界面。此更新适用于PostgreSQL、Redshift、Greenplum、MySQL、MariaDB、DB2、SQL Server和Sybase</li> 
 <li>我们添加了实时模板，这些模板允许直接从数据库资源管理器生成简单的语句。</li> 
 <li>改进了数据排序。</li> 
 <li>Ctrl/Cmd+C/V/X 现在可以用来复制、剪切和粘贴数据源</li> 
 <li>现在可以编辑 MongoDB 集合中的数据。还可以进行语句预览</li> 
</ul> 
<h4><strong>Build tools</strong></h4> 
<ul> 
 <li> <p>已经恢复了导入 Maven 项目时的自定义设置功能。</p> </li> 
</ul> 
<h4><strong>Frameworks & Technologies</strong></h4> 
<ul> 
 <li>新的 inspection 突出了 http:// 协议用法，并提出要改成 https://。</li> 
 <li>HTTP客户端附带了一些更新。你可以折叠返回的 HTML、JSON 或 XML，也可以复制它的主体、隐藏行号、选择显示格式，并快速滚动到响应的顶部和底部。</li> 
 <li>如果你使用 SSL 客户端认证的 https://协议，则你可以在 HTTP 客户端配置 SSL 设置。</li> 
 <li>当你创建 Spring、Micronaut、Quarkus 和 MicroProfile 项目时，只需要两步就可以开始使用它们。你可以在更新的向导的第一个屏幕上输入所有的关键信息，并在第二个屏幕上配置框架的特定设置。</li> 
 <li>为包含 JPA entities的项目添加了重新设计的可点击图标。还改进了对 Kotlin 和多模块项目的 JPA 支持。</li> 
 <li>你可以使用 JPA console 在 Jakarta EE 9 项目中编写和运行 JPQL 查询。</li> 
 <li>如果你使用浅色主题，则 UML Diagrams 将更新为新的配色方案。</li> 
 <li>Swagger 支持带有外部文件引用 ($ref) 的规范，并在 Structure 视图中为规范文件提供更多节点。</li> 
 <li>添加了一个新的实验工具，用于检测 Web 应用程序的 DOM 元素。用户可以通过 Tools | Generate Selenium Page Object 访问它<em>。</em></li> 
</ul> 
<h4><strong>Other</strong></h4> 
<ul> 
 <li>IntelliJ IDEA 社区版中嵌入了对公共可用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fidea%2Fshared-indexes.html" target="_blank">共享索引的</a>支持。</li> 
 <li>IntelliJ IDEA 现在支持所有 Android Studio 4.1.1 更新。</li> 
 <li>IntelliJ IDEA 现在可以从 bnd-maven-plugin 导入 OSGI facet 设置<em>。</em></li> 
</ul> 
<p><em>......</em></p> 
<p>更多详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2021%2F04%2Fintellij-idea-2021-1%2F" target="_blank">发行说明</a>。</p>
                                        </div>
                                      
</div>
            