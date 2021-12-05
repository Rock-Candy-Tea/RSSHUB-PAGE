
---
title: 'Qt Creator 6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3050c6d89b43efac53ea0e4bd4dfa4ca33c.gif'
author: 开源中国
comments: false
date: Sun, 05 Dec 2021 07:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3050c6d89b43efac53ea0e4bd4dfa4ca33c.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#09102b">Qt Creator 6 现已发布，具体更新内容如下：</span></p> 
<h4 style="margin-left:.4em; margin-right:0; text-align:start"><span><span><span><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>General</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>Qt Creator 6 的预编译二进制文件现在是基于 Qt 6.2 的。</span></span></span></span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>为 macOS 提供通用的 Intel+ARM 二进制文件。</span></span></span></span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>将外部进程（如构建工具和 clang-tidy 和其他工具）的启动移至单独的服务器进程。这避免了 Linux 上的问题，即在 Linux 上，从大型应用程序分叉进程比从小型服务器进程分叉成本更高。</span></span></span></span></span></span></span></span></span></p> </li> 
</ul> 
<h4 style="margin-left:.4em; margin-right:0; text-align:start"><span><span><span><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Editing</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>文本编辑器现在支持一般的多光标编辑（使用 Alt+单击添加光标）。</span></span></span></span></span></span></span></span></span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-3050c6d89b43efac53ea0e4bd4dfa4ca33c.gif" width="320" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>C++ 代码模型升级到 LLVM 13。</span></span></span></span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>现在完全支持使用 clangd 编辑 C++，但默认情况下仍处于禁用状态。</span></span></span></span></span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b"><span><span><span><span>现在默认禁用集成的 Qt Quick Designer。Qt Creator 将在 Qt Design Studio 中打开 .ui.qml 文件。这是朝着 Qt Design Studio 和 Qt Creator 之间更加集成的工作流程迈出的一步（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Do3ESfuBOaiI" target="_blank">视频</a>）。Qt Quick Designer 仍然存在，你可以通过检查 <span><span><span>Help</span></span></span> > <span><span><span>About Plugins 中</span></span></span>的 QmlDesigner 插件再次手动启用它。</span></span></span></span></span></span></span></span></span></p> </li> 
</ul> 
<h4 style="margin-left:.4em; margin-right:0; text-align:start"><strong>Projects</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b">在项目树的上下文菜单中增加了显示在文件系统视图中。</span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b">在高级搜索中加入了全局搜索所有项目目录下的文件，类似于定位器过滤器。</span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b">对于 CMake 项目，删除了特殊的 Headers 节点，进而改进了 CMake 支持处理目标源中提到的 header files 的方式。首选方法是向目标源添加 headers，这有助于 Qt Creator 和其他工具（如 Clazy）做正确的事情。文件系统视图和所有项目目录中的文件定位器过滤器和高级搜索可以在其他情况下使用。有关详细信息，可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-6-cmake-update%3FhsLang%3Den" target="_blank">Qt Creator 6 - CMake 更新</a>博客文章。</span></span></span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><span><span style="color:#09102b">对在 Docker 容器中构建和运行的支持取得了进展。Qt Creator 内部越来越多的地方接受远程文件路径。Windows 用户现在也可以使用实验性支持。</span></span></span></span></span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#333333">更多详细内容可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-6-released" target="_blank">查看</a></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-6-released" target="_blank">官方公告</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            