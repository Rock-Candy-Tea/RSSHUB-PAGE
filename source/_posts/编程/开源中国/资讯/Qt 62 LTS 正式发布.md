
---
title: 'Qt 6.2 LTS 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-90f99c55622b858511684430e2326cb40b3.webp'
author: 开源中国
comments: false
date: Fri, 01 Oct 2021 08:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-90f99c55622b858511684430e2326cb40b3.webp'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#09102b">Qt 6.2 LTS 现已发布，这是 Qt 6 的第一个长期支持版本。该版本专注于提高稳定性、性能，并且包含 Qt 5.15 中的所有常用功能以及为 Qt 6 添加的新功能。此外，同时发布的 Qt Design Studio 2.2 和即将发布的 Qt Creator 6 beta 都基于 Qt 6.2 LTS。</span></p> 
<p><span style="background-color:#ffffff; color:#09102b"><img alt height="217" src="https://oscimg.oschina.net/oscnet/up-90f99c55622b858511684430e2326cb40b3.webp" width="600" referrerpolicy="no-referrer"></span></p> 
<h4>Qt 6 的架构变化</h4> 
<p>Qt 6 中进行了一些更广泛的架构更改，包括：</p> 
<ul> 
 <li>Qt 6 现在依赖于 C++17 兼容的编译器，这有助于清理和改进代码库，并为用户提供更现代的 API</li> 
 <li>在处理大型数据集和性能方面改进了低级容器类</li> 
 <li>持续更新 QML 语言，使其更安全、更易于使用</li> 
 <li>引入 C++ 属性绑定</li> 
 <li>Qt 6 在如何处理与底层操作系统 API 的集成方面采用了全新的图形架构。得益于新的渲染硬件接口 (RHI)，Qt 6 现在默认使用每个系统上可用的最佳图形 API，显着提高了兼容性 —— 尤其是在桌面和移动操作系统（如 Windows 和 macOS 以及 iOS）上。</li> 
 <li>简化了将 3D 内容集成到基于 QML 的应用程序的过程，并使混合 2D 和 3D 的同时从系统中获得最大性能。</li> 
 <li>将构建系统从 qmake 切换到 cmake，这是当今基于 C++ 的应用程序的标准构建系统。不过在 Qt 6 的整个生命周期内仍支持 qmake。</li> 
</ul> 
<h4>添加模块</h4> 
<p>除了极少数例外，Qt 5.15 支持的所有模块现在也适用于 Qt 6.2，包括：</p> 
<ul> 
 <li>Qt Bluetooth</li> 
 <li>Qt Multimedia</li> 
 <li>Qt NFC</li> 
 <li>Qt Positioning</li> 
 <li>Qt Quick Dialogs</li> 
 <li>Qt RemoteObjects</li> 
 <li>Qt Sensors</li> 
 <li>Qt SerialBus</li> 
 <li>Qt SerialPort</li> 
 <li>Qt WebChannel</li> 
 <li>Qt WebEngine</li> 
 <li>Qt WebSockets</li> 
 <li>Qt WebView</li> 
</ul> 
<p>这些模块的 API 主要向后兼容 Qt 5，并且在移植到 Qt 6 时只需要对用户代码进行少量调整。</p> 
<h4>Qt 6.2 中的新功能</h4> 
<ul> 
 <li>Qt Quick 3D 
  <ul> 
   <li>Qt Quick 3D 现在支持实例化渲染，允许使用不同的变换渲染大量相同的对象；添加了两个新 API，用于向场景添加 3D 粒子效果和从场景中的任意点进行基于光线的拾取</li> 
   <li>改进了输入处理，现在可以为嵌入在 3D 场景中的 2D 项目正确创建 Qt Quick 输入事件</li> 
  </ul> </li> 
 <li>QML 工具 
  <ul> 
   <li>Qt 6.2 现在有一个公共 CMake API，极大地简化了创建 QML 模块的过程</li> 
   <li>QML linter (qmlint) 现在可以完全配置，无论是在命令行级别，还是通过配置文件，甚至是 QML 文件本身中的各个块。此外，它现在可以生成 JSON 输出以简化与其他工具或自动化系统的集成</li> 
   <li>QML 格式化程序 (qmlformat) 现在使用 QML dom 库，改进了生成的输出</li> 
  </ul> </li> 
 <li>Qt 多媒体 
  <ul> 
   <li> Qt 多媒体现在支持一些从未在 Qt 5 中正确支持的高要求的功能，包括播放的字幕和语言选择支持以及媒体捕获的可配置设置</li> 
   <li>内部架构不再像 Qt 5 那样通过公共 API 公开。这有助于能够更快地修复错误，并使将来添加新功能变得更加容易</li> 
  </ul> </li> 
 <li>Qt Creator 和 Qt Design Studio 
  <ul> 
   <li>Qt Creator 5 包含 Qt 6.2 开发所需的所有功能</li> 
   <li>Qt Design Studio 2.2 基于 Qt 6.2，极大地支持在一个图形工具中创建基于 Qt Quick 和 Qt Quick 的 3D 用户界面</li> 
  </ul> </li> 
</ul> 
<h4>新平台</h4> 
<p><img alt height="363" src="https://oscimg.oschina.net/oscnet/up-6bdbc7ac046d6e9ef8f9403c9782760bc15.png" width="1079" referrerpolicy="no-referrer"></p> 
<p>Qt 6.2 大大扩展了支持平台的范围：</p> 
<ul> 
 <li>完全支持 Apple Silicon 上的 macOS。 Qt 现在可以轻松创建通用二进制文件并在 Intel 和 Apple Silicon 上为 macOS 进行开发，并提供了在 Apple 芯片上本地运行的完整支持</li> 
 <li>恢复了对 INTEGRITY 和 QNX 实时操作系统的支持。支持需要 C++17 工具链和最新版本的操作系统。 QNX 的最低要求是 7.1 版，而 INTEGRITY 是19.0.13 版。</li> 
 <li>针对 Qt 6.2 的 webOS 验证也已完成</li> 
 <li>有很多工作正在进行以支持 Windows 11，有望在 6.2 补丁级别版本中为其提供全面支持。Windows on ARM HW 也可作为 Qt 6.2 的技术预览提供</li> 
 <li>改进了对 WebAssembly 的支持，它在 Qt 6.2 中作为技术预览提供支持</li> 
 <li>扩展了对 Python 的支持</li> 
</ul> 
<h4>从 Qt 5 移植</h4> 
<p>在大多数情况下，从 Qt 5 移植到 Qt 6 很简单，一般步骤是：</p> 
<ul> 
 <li>检查是否使用了受支持的编译器和平台版本</li> 
 <li>在 Qt 6 模式下使用 Qt 5.15 编译（使用 QT_DISABLE_DEPRECATED_BEFORE 宏）</li> 
 <li>然后用 Qt 6.x 编译。如果需要，在移植阶段利用兼容性模块</li> 
 <li>开始使用 Qt 6 提供的所有新特性和功能。例如，如果应用程序使用 QML，请运行 qmlint 工具并修复它给出的警告</li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.2-lts-released" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            