
---
title: 'Cmake 3.24.0 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9697'
author: 开源中国
comments: false
date: Sun, 07 Aug 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9697'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CMake 3.24.0 现已发布，一些亮点更新内容如下：</p> 
<ul> 
 <li>“FetchContent”模块和“find_package()”命令现在支持集成功能。</li> 
 <li>添加了“LINK_LIBRARY”生成器表达式以管理在链接步骤中指定库的方式。</li> 
 <li>使用 VS 2019 Update 11 或更高版本时，Visual Studio Generators 现在支持“SYSTEM”headers。</li> 
 <li>"cmake(1) "获得了 "-fresh" 命令行选项， 以便在配置 build tree 时删除任何现有的 "CMakeCache.txt" 文件和关联的 "CMakeFiles/" 目录， 从而开始新的配置， 就好像 build tree 是新创建的一样。</li> 
 <li>添加了“CMAKE_COMPILE_WARNING_AS_ERROR”变量和相应的“COMPILE_WARNING_AS_ERROR”目标属性，以便在编译时使用特定的编译器标志，将 warnings 视为 errors，例如“-Werror”。</li> 
 <li>“find_file()”、“find_path()”、“find_library()”、“find_program()”和“find_package()”命令获得了“NO_CMAKE_INSTALL_PREFIX”选项来控制搜索 “CMAKE_INSTALL_PREFIX”。</li> 
 <li>“find_file()”、“find_path()”、“find_library()”、“find_program()”和“find_package()”命令能够指定必须查询哪些 Windows Registry 视图。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kitware.com%2Fcmake-3-24-0-is-available-for-download%2F" target="_blank">https://www.kitware.com/cmake-3-24-0-is-available-for-download/</a></p>
                                        </div>
                                      
</div>
            