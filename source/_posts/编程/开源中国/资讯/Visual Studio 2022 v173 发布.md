
---
title: 'Visual Studio 2022 v17.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202208/11072841_sSGJ.png'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 07:28:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202208/11072841_sSGJ.png'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio 2022 17.3 正式发布，新版本带来了不少微软此前承诺的新功能，如 .NET MAUI GA 工具、Azure Container 应用程序等；以及在开发者社区中建议的新功能。</p> 
<p>Visual Studio 2022 v17.3 更新内容如下：</p> 
<ul> 
 <li>MAUI 工作负荷 GA 生成</li> 
 <li>MAUI/Blazor CSS 热重载支持</li> 
 <li>现在，你将能够使用我们的新增功能在 Visual Studio 中使用每个更新试用一系列新功能。</li> 
 <li>选择每个功能以了解有关特定功能的详细信息。</li> 
</ul> 
<p><img alt="Visual Studio 中的新增功能" src="https://static.oschina.net/uploads/img/202208/11072841_sSGJ.png" referrerpolicy="no-referrer"></p> 
<p><strong>Apple 开发人员帐户</strong></p> 
<p>此预览版包括对非企业 Apple 开发人员所需的单个 AppStoreConnect 帐户的初始支持。</p> 
<ul> 
 <li>若要添加个人帐户，请打开“工具\选项”，然后选择位于 Xamarin 部分中的“Apple 帐户”项。 在“Apple 帐户”中，单击“添加帐户...”按钮并选择“添加个人帐户”，并输入 AppStoreConnect API 密钥信息。</li> 
 <li>创建帐户后，可以通过“查看详细信息”按钮访问证书和预配配置文件。</li> 
 <li>已知问题： 
  <ul> 
   <li>在某些情况下，对于个人帐户，自动预配可能无法正常工作。 若要解决此问题，请按照 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fxamarin%2Fios%2Fget-started%2Finstallation%2Fdevice-provisioning%2Fmanual-provisioning" target="_blank">手动预配</a>的说明进行操作。</li> 
  </ul> </li> 
</ul> 
<p><strong>编辑器中的音频提示</strong></p> 
<ul> 
 <li>我们在 Visual Studio 编辑器中引入了新的音频提示。 启用后，当编辑插入符号到达断点、错误或警告的行上时，Visual Studio 将播放声音。 默认情况下，Visual Studio 使用与Visual Studio Code相同的声音，但这些声音可以配置为用户的首选项。</li> 
 <li>若要 <em>启用</em> 音频提示，请转到“工具\选项”，并在“环境”下查找“预览功能”。 在预览功能中，新选项为“为编辑器启用音频提示”。 如果已选中，下次启动 Visual Studio 时，声音将播放。</li> 
 <li>若要<em>配置</em>单个音频提示，请点击Windows 10或Windows 11中的 Windows 键并搜索“更改系统声音”。 在“程序事件”下，在“程序事件”树中查找“Microsoft Visual Studio”节点。 新事件是“行有断点”、“行有错误”和“行有警告”。 这可用于自定义或禁用单个声音。</li> 
</ul> 
<p><img alt="Windows 中的声音控制面板" src="https://static.oschina.net/uploads/img/202208/11072841_sOq3.png" referrerpolicy="no-referrer"></p> 
<p>Git 工具</p> 
<p>行暂存支持，即交互式暂存，能够直接从编辑器和差异视图暂存特定行和/或代码块。 若要开始，请通过选择相应的颜色边距并利用速览差异 UI 暂存更改来暂存最近的更改之一。</p> 
<p>阅读我们的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fline-staging-blog-release" target="_blank">博客文章</a> ，了解详细信息并 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fline-staging-survey-release" target="_blank">分享你的反馈</a>。</p> 
<p><img alt="行暂存支持" src="https://static.oschina.net/uploads/img/202208/11072842_QxjL.png" referrerpolicy="no-referrer"></p> 
<p><strong>C++</strong></p> 
<ul> 
 <li>Arm64EC 工具链不再标记为实验性，可供生产使用。</li> 
 <li>Visual Studio 终端现在可以用作具有存储 SSH 连接的 SSH 客户端。 安装适用于 Linux 工具的 C++ 后，打开终端工具窗口，终端下拉列表将填充存储的连接。 如果选择，他们将在 Visual Studio 中打开一个新的终端窗口，并在远程系统上打开伪终端窗口。 支持控制字符、颜色和光标位置感知。</li> 
 <li>转到“定义”现在将记住以前的签名，并在更好的匹配项不可用 (时相应地导航，例如手动更改其中一对) 的签名后。</li> 
 <li>改进了“全部转到”的响应能力。 以前，停止键入后会显示结果。 在新体验中，结果会显示在键入时。</li> 
 <li>在需要枚举类型完成的上下文中， (例如枚举变量、标签、 <code>case</code> 返回枚举类型等的赋值，) 自动完成列表现在将筛选为仅匹配的枚举器和相关构造。</li> 
 <li>添加了针对面向 .NET Core 的 C++/CLI MSBuild 项目的 NuGet PackageReference 支持。 此更改用于取消阻止混合代码库，使其无法采用 .NET Core。 这不适用于其他 C++ 项目类型或任何面向.NET Framework的 C++ 项目类型。 没有计划将 PackageReference 支持扩展到其他 C++ 方案，因为团队正在处理涉及 vcpkg 的单独体验，这将适用于非 MSBuild 方案并添加其他功能。</li> 
 <li>添加了用于嵌入式开发的串行监视器窗口，可通过调试 > Windows > 串行监视器获得。</li> 
 <li>与 17.2 相比，C++ 索引提高了约 66%。</li> 
 <li>将 Visual Studio 附带的 CMake 版本更新为 3.23 版。 有关可用内容的详细信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcmake.org%2Fcmake%2Fhelp%2Fv3.23%2Frelease%2F3.23.html" target="_blank">，请参阅 CMake 3.23 发行说明</a> 。</li> 
 <li>将 Visual Studio 附带的 LLVM 工具版本升级到 v14。 有关可用内容的详细信息，请参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freleases.llvm.org%2F14.0.0%2Fdocs%2FReleaseNotes.html" target="_blank">LLVM</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freleases.llvm.org%2F14.0.0%2Ftools%2Fclang%2Fdocs%2FReleaseNotes.html" target="_blank">Clang</a> 发行说明。</li> 
 <li>将并行 Dev 16.11 C++ 工具集更新为版本 14.29.30145.00。 最新版本的 Dev 16.11 C++ 工具集包含重要的 bug 修复，包括修复所有剩余的 C++20 缺陷报告。 有关 bug 修复的信息，包括 Dev 16.11 中的 C++20 缺陷报告，请参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fvisualstudio%2Freleases%2F2019%2Frelease-notes%2316.11.14" target="_blank">https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes#16.11.14</a></li> 
 <li>我们对 C++ 模块的编辑器内体验进行了各种改进。 “我们正在不断努力提高体验质量，但鼓励你在 17.3 中尝试，并通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fhome" target="_blank">开发者社区</a>报告剩余的问题。</li> 
</ul> 
<p><strong>调试和诊断</strong></p> 
<ul> 
 <li>诊断分析工具现在包括一个分析器，该分析器列出了内存转储中的唯一调用堆栈以及执行这些堆栈的线程。</li> 
 <li>IEnumerable 可视化工具现在支持 CSV 格式的数据导出。 只需使用右上角的下拉列表并选择 CSV。可视化工具还允许筛选基于所需筛选字符串的数据。 可视化工具将返回包含与筛选器字符串匹配的值的所有行。 还可以以 CSV/Excel 格式导出筛选和排序结果。</li> 
</ul> 
<p><img alt="Visualizer_Filte" src="https://static.oschina.net/uploads/img/202208/11072842_lIcN.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>我们还添加了对 IEnumerable 和 DataTable/DataSet 可视化工具的主题支持，因此这两个可视化工具窗口都针对 Visual Studio 的深色、浅色和蓝色主题进行了主题。</li> 
</ul> 
<p><img alt="Visualizer_Filte" src="https://static.oschina.net/uploads/img/202208/11072842_HiJN.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>从 17.3 预览版 3 调试器开始，将自动重新加载伪装的反编译项目，如符号和 PDB 文件。 如果选择在任何以前的会话中反编译，则所有下一个会话都会自动重新加载项目，并让你在外部源节点中更快地进入反编译源。 这仍会遵循 JMC 设置。</li> 
 <li>调试器现在提供了一个新选项，用于禁用 NGEN 的加载或准备为托管代码加载 (RDR) 映像。 可以在模块加载上使用预编译图像的“工具 > 选项> 调试 > 常规 > 阻止”下更改设置，也可以使用 Visual Studio 搜索栏中的任何关键字轻松搜索设置。</li> 
 <li>现在，你将在“调用堆栈”窗口中看到异常堆栈帧，因此，对于所有异步异常，你可以快速加载符号或定位源并直接转到异常的站点。 调用堆栈窗口中的异常堆栈帧将提供实际调用堆栈的功能。自动导航、在帧之间快速切换以及符号加载/反编译选项等功能，以返回到引发异常的源代码。</li> 
</ul> 
<p><img alt="Visualizer_Filte" src="https://static.oschina.net/uploads/img/202208/11072842_K9uG.png" referrerpolicy="no-referrer"></p> 
<p><strong>常规</strong></p> 
<ul> 
 <li>现在，当使用同一个性化帐户登录新计算机上时，GitHub 帐户在计算机中漫游， (帐户显示在帐户设置对话框左上角) 。</li> 
</ul> 
<p><strong>安装程序</strong></p> 
<ul> 
 <li>现在，可以使用安装程序上的“全部更新”按钮更新 Visual Studio 的所有并行版本。</li> 
</ul> 
<p><strong>Microsoft Teams 开发工具 (Teams 工具包) </strong></p> 
<ul> 
 <li>Microsoft Teams 应用项目模板已得到改进，现在会创建各种类型的 Teams 应用，包括通知机器人、命令机器人、选项卡应用和消息扩展。 现在可以使用 Teams Toolkit for Visual Studio 创建和调试各种 Microsoft Teams 应用。</li> 
 <li>对于使用以前版本的 Teams 工具包创建的任何现有 Teams 应用，建议使用更新的模板创建新项目。</li> 
 <li>现在可以选择何时使用 M365 标识登录，并使用 Project > Teams Toolkit > Prepare Teams 应用依赖项菜单选项注册 Teams 应用资源。</li> 
 <li>准备 Teams 应用依赖项将为 Teams 项目注册 Teams 应用和机器人。</li> 
 <li>汇报 manifest.template.json 文件可以与 Teams 开发人员门户同步进行本地调试，方法是随时再次选择“准备 Teams 应用依赖项”菜单选项。</li> 
 <li>可以通过选择 Project > 与 Teams 开发人员门户同步到 manifest.template.json 文件的汇报，以便进行远程预览Teams 开发人员门户菜单中的 Teams 工具包>更新清单选项。</li> 
 <li>可以在同步前预览清单文件，方法是右键单击 manifest.template.json 文件并使用“预览清单文件”菜单选项。</li> 
 <li>使用云菜单中的 Project > Teams 工具包 > 预配在 Azure 订阅中创建资源。</li> 
 <li>使用“项目”>“Teams 工具包”>“部署到云”菜单将代码发布到这些资源。</li> 
 <li>可以使用预览版 Teams 应用菜单从“预配”菜单创建的浏览器中远程打开 Teams 应用。</li> 
 <li>可以通过选择 Project > Teams Toolkit > Zip 应用包菜单选项来压缩 Teams 应用并生成应用包，以便共享和上传目的。</li> 
 <li>可以通过右键单击 Teams 应用项目来查找所有 Teams 工具包菜单选项，它们与 Project > Teams 工具包菜单相同。</li> 
 <li>详细了解 Teams 工具包 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fteams-toolkit-vs-docs" target="_blank">https://aka.ms/teams-toolkit-vs-docs</a></li> 
</ul> 
<p><strong>.NET 效率</strong></p> 
<ul> 
 <li> <p>在 C# 10 中，我们引入了全局使用。 全局 Usings 会将 usings 添加到文件顶部，且不可见且自动。 现在，在文件顶部显示一个图标，告知你全局使用是否在你的文件中处于活动状态，如果单击该图标，它将向你显示这些全局用法。 <img alt="全局使用" src="https://static.oschina.net/uploads/img/202208/11072842_8Wak.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>速览定义现在支持源链接、嵌入源和反编译源。 <img alt="查看定义" src="https://static.oschina.net/uploads/img/202208/11072843_Kknj.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>我们添加了以下三个选项，用于在打开文件时折叠和大纲视图：</p> 
  <ul> 
   <li>打开文件时折叠#regions</li> 
   <li>在打开文件时折叠</li> 
   <li>从文件打开的元数据折叠实现</li> 
  </ul> </li> 
 <li> <p>现在可以将“全部修复”应用于 <code>Use expression body or block body</code> 和 <code>Convert to raw string literal</code> 重构。</p> </li> 
 <li> <p>我们现在有一个用于修复无效约束的代码修补程序。 将光标置于编辑器中的诊断波形曲线上。 按 (Ctrl+.) 触发“快速操作和重构”菜单。 选择“修复约束”。 <img alt="修复约束" src="https://static.oschina.net/uploads/img/202208/11072843_MKe8.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>我们现在有一个重构，可用于在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fcsharp%2Fwhats-new%2Ftutorials%2Ftop-level-statements" target="_blank">顶级语句</a>和 Program.Main 样式之间切换。 将光标置于顶级语句上。 按 (Ctrl+.) 触发“快速操作和重构”菜单。 选择“转换为‘Program.Main’样式程序”。 <img alt="转换为 Program.Main 重构" src="https://static.oschina.net/uploads/img/202208/11072843_PTHV.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>我们在“全部修复”操作中添加了更多范围。 除了将“全部修复”操作应用到文档、项目和解决方案之外，还可以将“全部修复”应用到包含成员和包含类型。 <img alt="修复所有包含成员和包含类型" src="https://static.oschina.net/uploads/img/202208/11072844_OMfK.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>现在，当你向单行注释添加额外的正斜杠时，我们会自动将单行注释转换为文档注释。</p> </li> 
 <li> <p>我们现在有一个代码样式选项，可用于在 foreach 循环中针对可能的异常发出警告。 根据设计，foreach 循环会隐式强制转换为派生类型。 这在泛型存在之前是必需的，但在某些情况下可能会导致运行时异常。</p> </li> 
</ul> 
<p><strong>个性化</strong></p> 
<ul> 
 <li>文档管理功能已更新。 阅读我们的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fdoc-management-personalization%2F" target="_blank">博客文章</a>，了解更多信息。</li> 
</ul> 
<p>这些功能包括：</p> 
<ul> 
 <li>按多行排列的选项卡。</li> 
 <li>还原最近的文档。</li> 
 <li>修改的脏指示器。</li> 
 <li>下拉列表显示斜体中不可见文档的名称。</li> 
</ul> 
<p><strong>Razor (ASP.NET Core) 编辑器</strong></p> 
<ul> 
 <li>新的 Razor 编辑器现在在 <code><attribute></code> 内部提供完全完成支持。</li> 
 <li>在键入 =“ ”时，新的 Razor 编辑器现在可正确处理 HTML 属性的完成。</li> 
 <li>新的 Razor 编辑器现在支持 HTML、JavaScript 和 CSS OnTypeFormatting。</li> 
</ul> 
<p>测试工具</p> 
<ul> 
 <li> <p>从测试资源管理器运行测试时，现在默认启用并行发现。 这使 Visual Studio 能够使用可用核心并行发现测试，并减少在测试资源管理器中查看测试的时间。</p> </li> 
 <li> <p>“Live Unit Testing”窗口现在有一个状态栏，类似于测试资源管理器。 这应该更深入地了解实时单元测试中正在进行的操作，以及明显地显示错误。 <img alt="Live Unit Testing 状态栏" src="https://static.oschina.net/uploads/img/202208/11072844_V49v.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>vstest.console 现在支持在一个请求中运行不同目标平台和目标框架的程序集。</p> </li> 
 <li> <p>代码覆盖率现在有一个用于静态检测的缓存，以提高性能。</p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fvisualstudio%2Ftest%2Fmicrosoft-code-coverage-console-tool%3Fview%3Dvs-2022" target="_blank">Microsoft.CodeCoverage.Console</a> 现已添加到命令行工具。</p> </li> 
 <li> <p>AnyCPU .NET Framework测试项目的默认体系结构已从 x86 更改为 x64。 此更改统一了默认体系结构在所有类型的测试项目中确定的方式，这些测试项目始终基于 Visual Studio 的体系结构。 这意味着，在 x64 版本的 VisualStudio 中，将使用 x64，将来将使用 ARM64 VisualStudio。 同一规则也适用于 <code>dotnet test</code>和 <code>vstest.console</code>。 若要还原为使用 x86，请导航到 <strong>AnyCPU 项目的>测试>处理器体系结构 x86</strong></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fvisualstudio%2Ftest%2Fremote-testing%3Fview%3Dvs-2022" target="_blank">远程测试</a>现在支持针对远程 arm64 Windows 环境运行测试。</p> </li> 
 <li> <p>[Live Unit Testing] 的新生成体验现已默认启用。 阅读我们的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Flive-unit-testing-preview-better-and-faster%2F" target="_blank">博客文章</a>，了解更多信息。</p> </li> 
 <li> <p>现在，通过在“代码覆盖率结果”窗口中选择“边距字形”，可以选择在编辑器边距上显示代码覆盖率信息。 <img alt="转换为原始字符串" src="https://static.oschina.net/uploads/img/202208/11072845_gvqw.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>Live Unit Testing 现在提供用于重置所有状态的按钮。 转到测试 > Live Unit Testing > 重置解决方案的 Live Unit Testing 状态。</p> </li> 
 <li> <p>Live Unit Testing 现在支持 Razor 文件。</p> </li> 
</ul> 
<p><strong>TypeScript 和 JavaScript 开发</strong></p> 
<ul> 
 <li> <p>JavaScript 和 TypeScript 文件项目现在已从程序分析中排除，除非它们由 tsconfig.json 或 jsconfig.json 文件引用。 结果应在具有大量 TypeScript 和 JavaScript 文件的大型项目中提高性能。</p> </li> 
 <li> <p>从 ASP.NET 项目中引用的 JavaScript (.esproj) 项目现在提供了一个选项，用于在 ASP.NET 项目发布中包含生产生成输出。</p> </li> 
 <li> <p>TypeScript 4.7 语言服务和编译器包含在 Visual Studio 中。 有关详细信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Ftypescript%2Fannouncing-typescript-4-7%2F" target="_blank">，请参阅 TypeScript 4.7 公告博客文章</a> 。</p> </li> 
 <li> <p>新的多目标 JavaScript 调试器现在默认在 Node.js (.njsproj) 项目中使用。</p> </li> 
 <li> <p>JavaScript 和 TypeScript React (.jsx/.tsx) 文件中的自动关闭 HTML 标记。</p> </li> 
 <li> <p>修复了选择默认 TypeScript 语言服务器时自动类型获取 (ATA) 不起作用的问题。</p> </li> 
 <li> <p>修复了以下问题：当使用 npm 7 或更高版本还原包时，Node.js (.njsproj) 项目中的依赖项节点显示间接依赖项。</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-3-is-now-available%2F" target="_blank">https://devblogs.microsoft.com/visualstudio/visual-studio-2022-17-3-is-now-available/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            