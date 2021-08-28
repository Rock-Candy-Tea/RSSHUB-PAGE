
---
title: 'Qt Creator 5.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6140'
author: 开源中国
comments: false
date: Sat, 28 Aug 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6140'
---

<div>   
<div class="content">
                                                                                            <p>Qt Creator 5.0 正式发布，本次更新带来以下几点重要变化：</p> 
<h3>实验性功能</h3> 
<p>Qt Creator 5.0 实验性地支持 Clangd 作为 C/C++ 代码模型的后端。这个功能是可选的，默认情况下是关闭的。它取代了建立在 LSP 上基于 libclang 的代码模型。如果你想尝试该功能，请在 Tools > Options > C++ > Clangd（或 Qt Creator > Preferences > C++ > Clangd on macOS）中启用 "Use clangd"，并提供一个最近的 Clangd 可执行文件。</p> 
<p>另一个与 5.0 一起交付的实验性功能是对在 Docker 容器中构建和运行应用程序的一些支持。该实验性功能目前只能在使用 CMake 作为项目构建系统的 Linux 主机上工作。当你在 Help > About Plugins（或在 macOS 上的 Qt Creator > About Plugins）中启用了这个实验性插件后，你可以在设备设置中创建一个 Docker 设备，并在 Kit 中的将其设置为 "Build device "和 "Device"。</p> 
<h3>编辑</h3> 
<p>C++ 代码模型得到了各种修复。当你重命名一个符号时，我们不再默认选择与你的项目没有直接关系的文件。对 <code>.ui</code> 和 <code>.scxml</code> 文件的修改现在会立即反映在代码模型中，而无需重新编译。</p> 
<p>我们将 QML 代码模型更新到 Qt 6.2，并修复了 QML 较新功能的各种问题。</p> 
<p>如果你的语言服务器支持进度通知，我们现在也会在 Qt Creator 中显示它们，我们还增加了对服务器提供的代码片段的支持。</p> 
<h3>项目</h3> 
<p>一般来说，我们致力于减少在 Qt Creator 中加载大型项目后可能发生的冻结现象。现在这个问题应该会好很多。</p> 
<p>我们更新了 Qbs 到最新的 1.20 版本，并减少了 Qbs 项目管理在你有很多 kits 时对启动的影响。</p> 
<h3>平台</h3> 
<p>我们增加了对 MSVC ARM 工具链的支持，并改进了在 M1 Mac 上运行英特尔构建的 Qt Creator 的体验。Android 12 现在可以在 Qt Creator 中正确处理。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.qt.io%2Fcgit%2Fqt-creator%2Fqt-creator.git%2Ftree%2Fdist%2Fchanges-5.0.0.md%3Fh%3D5.0" target="_blank">https://code.qt.io/cgit/qt-creator/qt-creator.git/tree/dist/changes-5.0.0.md?h=5.0</a></p>
                                        </div>
                                      
</div>
            