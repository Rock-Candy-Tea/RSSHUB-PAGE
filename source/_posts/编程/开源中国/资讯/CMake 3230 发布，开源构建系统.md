
---
title: 'CMake 3.23.0 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4829'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4829'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CMake 3.23.0 现已发布，亮点更新内容如下：​​</p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>“cmake-presets(7)”文件现在有一个可选的“include”字段，允许文件包含其他文件。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>适用于 VS 2019 及更高版本的 Visual Studio 生成器学会了支持 C# 项目的 .NET SDK-style 的项目文件（“.csproj”）。参阅“DOTNET_SDK”目标属性和相应的“CMAKE_DOTNET_SDK”变量。.NET SDK-style 的项目尚不支持“add_custom_command()” 。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>现在支持基于 LLVM 的 IBM Open XL C/C++ 编译器，编译器 ID 为“IBMClang”。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>现在支持 MCST LCC 编译器，编译器 ID 为“LCC”。参见 policy “CMP0129”。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>“install(TARGETS)”命令获得了一个新的“FILE_SET”参数，可用于安装与目标关联的 header file sets。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>“target_sources()”命令获得了一个新的“FILE_SET”模式，可用于将 headers 添加为目标的 header-only source files。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>“CMAKE_CUDA_ARCHITECTURES”变量和关联的“CUDA_ARCHITECTURES”目标属性现在支持 CUDA 工具包 7.0+ 的“all”和“all-major”值。</span></span></p> </li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kitware.com%2Fcmake-3-23-0-is-available-for-download%2F" target="_blank">https://www.kitware.com/cmake-3-23-0-is-available-for-download/</a></p>
                                        </div>
                                      
</div>
            