
---
title: 'Cmake 3.21.0 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3088'
author: 开源中国
comments: false
date: Fri, 16 Jul 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3088'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Cmake 3.21.0 已经发布，CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p>Cmake 3.21.0 中的一些重要变更有：</p> 
<ul> 
 <li>CMake 学会了将 "HIP"作为第一类语言来支持，可以通过"project() "和 "enable_language()"命令启用。</li> 
 <li>增加了实验性的"Visual Studio 17 2022"生成器，基于"Visual Studio 2022 Preview 1.1"。</li> 
 <li>Makefile 生成器和“Ninja”生成器学会了在"C"、"CXX"、"OBJC"和 "OBJCXX"语言的链接器中添加链接器启动工具。</li> 
 <li>"C_STANDARD"、"OBJC_STANDARD"和 "Compile Features"功能获得了对 C17 和 C23 的支持。</li> 
 <li>"cmake(1) "获得了 "-toolchain <path/to/file>" 命令行选项来指定一个工具链文件。</li> 
 <li>打印到终端的消息现在可以按消息类型着色。</li> 
 <li>add_custom_command(TARGET) 命令（针对 Build Events）获得了对解决依赖目标的生成器表达式的支持。</li> 
 <li>install(TARGETS)  命令获得了新的 RUNTIME_DEPENDENCIES 和 RUNTIME_DEPENDENCY_SET 参数，可以使用 file(GET_RUNTIME_DEPENDENCIES) 来安装运行时依赖项。</li> 
 <li>增加了一个新的 TARGET_RUNTIME_DLLS 生成器表达式。</li> 
 <li>ctest(1) 获得了一个 -output-junit 选项，可以将测试结果写到 一个 JUnit XML 文件。</li> 
 <li>foreach() 命令现在可以在循环范围内隔离循环变量。</li> 
 <li>......</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-21-0-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-21-0-available-for-download/</a></p>
                                        </div>
                                      
</div>
            