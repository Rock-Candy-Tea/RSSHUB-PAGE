
---
title: 'Qt Creator 8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=941'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=941'
---

<div>   
<div class="content">
                                                                                            <p>Qt Creator 是一个跨平台的 C++、JavaScript 和 QML 集成开发环境，它简化了 GUI 应用的开发。它是 Qt GUI 应用开发框架的 SDK 的一部分。该编辑器具有语法高亮和自动补全等功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Qt Creator 8 正式发布，更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span><span><span><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>C++</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>删除了基于 libclang 的代码模型回退，现在依赖于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fclangd.llvm.org%2F" target="_blank">Clangd</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmicrosoft.github.io%2Flanguage-server-protocol%2F" target="_blank">LSP</a> 客户端实现。Clangd 在 Qt Creator 7 中已经是默认设置，在此之前是可选的。内部代码模型仍然存在，可以通过在设置中关闭 Clangd 作为备用。如果你的开发机器内存很小，Qt Creator 会默认关闭 Clangd 并通知你。无论如何，你始终可以打开并使用 Clangd。但值得注意的是，Clangd 相对来说是很耗费资源的。还改进了为 Clangd 生成<code>compile_command.json</code>的性能，并修复了许多其他问题。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>QML</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复了 JavaScript 字符串模板的处理，以及 nullish 合并运算符的问题。当跟踪一个符号时，Qt Creator 可能会从构建目录而不是源目录打开相应的 QML 文件，这一点现在应该已被修复。如果你设法从构建目录打开这样的 QML 文件，编辑器现在会显示一条警告，提示你将要编辑生成的文件。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>默认切换到<code>python-lsp-server</code>。可以在 Python > Language Server Configuration 使用单独的 preferences 页面配置新语言服务器。还使代码模型意识到 UI 文件中未保存的变化，并修复了一些性能问题。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>CMake</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>CMake 项目现在提供了一个新的“Profile”构建配置模板，它将“RelWithDebInfo”CMake 构建类型与“QML debugging and profiling”相结合。不再在项目模板中为“Debug”和“RelWithDebInfo”CMake 构建类型硬编码 QML 调试选项，而是仅依赖 Qt Creator 中的“QML debugging and profiling”选项，现在 "Debug" 和 "Profile" 构建配置都默认打开了。现有的构建目录不受影响。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>已知问题：Android NDK 22.1 附带的 CMake 工具链文件会覆盖用于 QML 调试的默认设置。在这种情况下，用户需要在构建设置中将“QML debugging and profiling”切换为“Enable”，并首先手动选择“Run CMake”。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong>New Plugins</strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了对代码覆盖率分析工具 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fproduct%2Ftesting-tools%3FhsLang%3Den" target="_blank">Coco</a> 的实验性支持。该集成在 Qt Creator 的代码编辑器中以注释的形式显示代码覆盖率。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2F" target="_blank">添加了对 GitLab</a> 的实验性支持。浏览和克隆项目，并将你的 checkouts 与 GitLab 实例连接，以在版本控制视图中接收事件通知。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong>Windows</strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>删除了对通用 Windows 平台 (UWP) 的支持。现在可以在 Windows 主机上检测到 ARM MSVC 工具链。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Android</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>对于 Android，添加了通过 WiFi 连接设备的选项，并修复了新 SDK 工具的问题。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>iOS</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在开发过程中提高了连续部署的速度，仅部署与之前部署的文件不同的部分。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong>Docker</strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>对 Docker 的支持正在取得进展，修复了一些错误，并对支持远程进程和文件进行了大量的内部重构。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>发布公告：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-8-released" target="_blank">https://www.qt.io/blog/qt-creator-8-released</a></p>
                                        </div>
                                      
</div>
            