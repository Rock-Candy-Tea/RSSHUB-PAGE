
---
title: 'Qt Creator 4.15 发布，Qt 集成开发环境'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f5455b78232e5ec6df396424106a851e5dc.png'
author: 开源中国
comments: false
date: Tue, 13 Apr 2021 06:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f5455b78232e5ec6df396424106a851e5dc.png'
---

<div>   
<div class="content">
                                                                                            <p>Qt Creator 4.15 已经发布，本次更新主要包括 CMake 项目管理器的功能更新和错误修复。</p> 
<h4>多配置支持</h4> 
<p>在 Qt Creator 4.15 之前，只有第一个 CMake 文件的 api json 导出被解析。现在，Qt Creator 支持 Xcode、Visual Studio 和 Ninja Multi-Config 等多配置生成器，用户只需要配置一次 CMake，而能够更快地在构建类型之间切换。在 CMake 项目设置中，有一个 " Build type" 字段，需要匹配单配置生成器（Ninja、Makefile）的 CMAKE_BUILD_TYPE 变量。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f5455b78232e5ec6df396424106a851e5dc.png" referrerpolicy="no-referrer"></p> 
<h4>用初始参数重新配置</h4> 
<p>此前，在项目获得 CMakeCache.txt 文件之前，会使用初始的 CMake 参数值。之后项目设置的所有变化都会导致参数为 -D<variable>:<type>=<value> 或 -U<variable>cmake 的命令行调用，这些参数将存储在 CMakeCache.txt 中，并通过 file-api json 文件提供给 Qt Creator。而 Qt Creator 4.15 增加了一个名为 "Re-configure with initial parameters" 的按钮，它可以进行 "Clear CMake configuration"，然后用 "Initial CMake parameters" 列表的值运行 cmake。只有初始cmake配置成功，才能添加编辑 CMake 变量。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a4299b9f30eecf6bcffb7db39ab0f5a0357.png" referrerpolicy="no-referrer"></p> 
<h4>复制和批量编辑 CMake 变量</h4> 
<p>当项目初步配置好，Qt Creator 可以读取 CMake 文件-api json文件后，就可以添加修改 CMake 变量。通过 "Copy" 和 " Batch Edit…" 功能，用户可以比以前更快地配置一个 CMake 项目。这些变量会被发送到 cmake，并且会被持久化在 <BuildDir>CMakeCache.txt 中。如果想保留这些值，可以把它们保存到 "Initial CMake parameters" 列表中。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f458de3cb36da389d8a188a13c67163ab73.gif" referrerpolicy="no-referrer"></p> 
<h4>自动备份 CMake 配置</h4> 
<p>Qt Creator 4.15 会在运行 CMake 之前，用 -D<variable>:<type>=<value> 或 -U<variable> 参数复制 CMakeCache.txt 和 .cmake/api/v1/reply json 目录。<br> 如果 CMake 因为某些原因失败了，备份会被恢复，这样用户就能得到之前的工作配置。同时，修改的内容仍然会出现在对话框中，用户将有机会调整它们。</p> 
<h4>快速访问 CMake 目标定义</h4> 
<p>在定位器中，可以通过 Ctrl + K，然后输入 "cmo"，打开目标对应的 CMakeLists.txt 文件。但如果用户有一个 CMake API，并使用函数调用创建目标，那么用户将得到 CMake API cmake 文件定义，而不是调用该函数的 CMakeLists.txt 文件。Qt Creator 4.15 已经修复了这个问题。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cf6254fb0cd1bb65bc7bb6dca888e226a24.gif" referrerpolicy="no-referrer"></p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-creator-4.15-cmake-new-features" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            