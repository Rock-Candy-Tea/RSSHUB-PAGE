
---
title: '微软正式发布 Visual Studio 2022'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3622'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3622'
---

<div>   
<div class="content">
                                                                                            <p><strong>微软今天正式发布了 Visual Studio 2022，Visual Studio 2022 的主要功能包括：</strong></p> 
<p>64-bit</p> 
<ul> 
 <li>devenv.exe 现在仅支持 64 位</li> 
</ul> 
<p>Azure Cloud Services</p> 
<ul> 
 <li>现在支持 Azure 云服务（经典）和 Azure 云服务（扩展支持）项目</li> 
</ul> 
<p><strong>C++</strong></p> 
<ul> 
 <li>v143 构建工具现在可通过 Visual Studio 安装程序以及独立构建工具使用</li> 
 <li>在调试器下运行时，新的热重载现在可用于本机 C++ 应用程序。它支持 MSBuild 和 CMake 项目。</li> 
 <li>现在可以在 WSL2 上本地构建和调试，而无需建立 SSH 连接。支持跨平台 CMake 项目和基于 MSBuild 的 Linux 项目。</li> 
 <li>Visual Studio 现在支持 CMakePresets.json 中的 <code>buildPresets.targets</code> 选项。这允许你在 CMake 项目中构建目标的子集。</li> 
 <li>CMake 项目中的项目菜单已经过简化，并提供了“删除缓存和重新配置”和“查看缓存”的选项。</li> 
 <li>CMake 概览页面已更新为支持 CMakePresets.json。</li> 
 <li>现在可以使用 LLDB 从 Visual Studio 调试在远程系统上运行的进程。</li> 
 <li>将 Visual Studio 附带的 CMake 版本升级到 3.21 版。</li> 
 <li>Visual Studio 附带的 LLVM 工具已升级到 LLVM 12。</li> 
 <li>使用 C++ 工作负载的游戏开发现在安装支持 Visual Studio 2022 的最新虚幻引擎</li> 
 <li>在为来自导入的模块和 Header 单元的类型提供导航和语法突出显示时，对 C++ IntelliSense 进行了改进。</li> 
 <li>通过优化缓存 header 使用和符号数据库访问，改进了 C++ IntelliSense 性能，缩短了进入代码的加载时间。</li> 
 <li>用于 C++ 的 IntelliSense Code Linter 现在默认处于启用状态，提供即时的键入建议和常见代码缺陷的修复建议。</li> 
 <li>……</li> 
</ul> 
<p><strong>个性化</strong></p> 
<ul> 
 <li>为垂直和水平标签添加颜色标签</li> 
 <li>增加了主题包，并与 VS Code 主题作者合作，推出了自定义主题集合</li> 
 <li>建立了主题转换器，将 VS Code 主题转换到 Visual Studio 2022 中使用</li> 
 <li>增加了将 Visual Studio 主题与 Windows 主题同步的功能</li> 
 <li>增加了新的文档管理功能，包括自定义标签宽度，加粗活动文档，以及 docwell 中额外的关闭按钮。</li> 
</ul> 
<p><strong>编辑器</strong></p> 
<ul> 
 <li>添加 subword 导航</li> 
 <li>自动保存现在可用作预览功能</li> 
 <li>Multi-caret 复制/粘贴体验</li> 
</ul> 
<p><strong>可扩展性</strong></p> 
<ul> 
 <li> <p>从 Microsoft.VisualStudio.Language.Client 程序集中删除了 API</p> </li> 
 <li> <p>VS SDK 包含多项重大更改，Visual Studio 2019 扩展在 2022 将不起作用。</p> </li> 
 <li> <p>VS SDK Reference 程序集不再安装到该<code>VSSDK\\VisualStudioIntegration\\Common\\Assemblies</code></p> <p>文件夹中。如果你的构建依赖于这些程序集，请迁移项目以改用 NuGet 包。</p> </li> 
 <li> <p>添加了 ILanguageClient 重大更改修复</p> </li> 
</ul> 
<p><strong>Git 工具</strong></p> 
<ul> 
 <li>在创建 git 仓库的过程中，现在完全支持发布到 Azure DevOps</li> 
 <li>状态栏的增强，包括从空 VS 查看和打开仓库的新功能，并显示未拉取提交的数量</li> 
 <li>包含添加/删除行数和可发现配置选项的统一差异（Diff）工具栏</li> 
 <li>提交细节增强功能，包括响应速度更快且用户友好的 UI</li> 
 <li>……</li> 
</ul> 
<p>热重载</p> 
<ul> 
 <li>热重载现在可以通过 Visual Studio 调试器向 .NET 开发人员提供，对于许多 .NET 6 应用程序类型，不需要调试器。</li> 
 <li>在使用 Visual Studio 调试器时，热重载现在可供 C++ 开发人员使用。</li> 
</ul> 
<p><strong>IntelliCode</strong></p> 
<ul> 
 <li>整行补全可以根据你当前的上下文预测你的下一段 C# 代码，并在你的光标右边以内联建议的形式呈现。</li> 
 <li>整行补全现在与 JetBrains ReSharper 的最新版本兼容。</li> 
</ul> 
<p><strong>JavaScript/TypeScript</strong></p> 
<ul> 
 <li>JavaScript 和 TypeScript 测试现在可以在 Visual Studio Test Explorer 中进行</li> 
 <li>NPM GUI 可用，所以你现在可以像下载 Nuget 包一样下载 NPM 模块了</li> 
 <li>……</li> 
</ul> 
<p><strong>.NET 6 SDK</strong></p> 
<ul> 
 <li>.NET 6 SDK 已包含在 Visual Studio 2022 中</li> 
</ul> 
<p><strong>用户界面</strong></p> 
<ul> 
 <li>默认图标已更新和刷新</li> 
</ul> 
<p>……</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvisualstudio.microsoft.com%2Fdownloads%2F" target="_blank">https://visualstudio.microsoft.com/downloads/</a></p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fvisualstudio%2Freleases%2F2022%2Frelease-notes" target="_blank">https://docs.microsoft.com/en-us/visualstudio/releases/2022/release-notes</a></p>
                                        </div>
                                      
</div>
            