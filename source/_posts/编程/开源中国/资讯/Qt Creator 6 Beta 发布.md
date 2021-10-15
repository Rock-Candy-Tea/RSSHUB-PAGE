
---
title: 'Qt Creator 6 Beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8055'
author: 开源中国
comments: false
date: Fri, 15 Oct 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8055'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Qt Creator 6 Beta 现已发布，该版本包括一些错误修复和新功能，正式版预计于年底发布。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li>General 
  <ul> 
   <li>预建的 Qt Creator 6 二进制文件现在基于 Qt 6.2</li> 
   <li>为 macOS 提供通用的 Intel+ARM 二进制文件</li> 
   <li>将外部进程（如构建工具和 clang-tidy 和其他工具）的启动移至单独的服务器进程。这避免了 Linux 上的问题，在 Linux 上，从大型应用程序分叉进程比从小型服务器进程分叉成本更高</li> 
  </ul> </li> 
 <li>Editing 
  <ul> 
   <li>文本编辑器现在支持一般的多光标编辑（使用 Alt+单击添加光标）</li> 
   <li>C++ 代码模型升级到 LLVM 13</li> 
   <li>现在完全支持使用 clangd 编辑 C++，但默认情况下仍处于禁用状态，可以在 C++ > Clangd 选项中启用它</li> 
   <li>现在默认禁用集成的 Qt Quick Designer。 Qt Creator 将在 Qt Design Studio 中打开 .ui.qml 文件。这是朝着 Qt Design Studio 和 Qt Creator 之间更加集成的工作流程迈出的一步（视频）。 Qt Quick Designer 仍然存在，用户可以通过检查 Help > About Plugins 中的 QmlDesigner 插件再次手动启用它</li> 
  </ul> </li> 
 <li>Projects 
  <ul> 
   <li>将文件系统视图中显示添加到项目树的上下文菜单中。</li> 
   <li>添加了对所有项目目录中的文件的全局搜索以进行高级查找，类似于定位器过滤器</li> 
   <li>对于 CMake 项目，删除了特殊的 Headers 节点，进而改进了 CMake 支持处理目标源中提到的头文件的方式。首选方法是向目标源添加标头，这有助于 Qt Creator 和 Clazy 等其他工具做正确的事情。文件系统视图和所有项目目录定位器中的文件过滤器和高级搜索可用于其他情况</li> 
   <li>对在 Docker 容器中构建和运行的支持取得了进展。 Qt Creator 内部越来越多的地方接受远程文件路径</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-6-beta-released" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            