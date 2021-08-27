
---
title: 'CMake 3.21.2 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9022'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9022'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p>CMake 3.21.2 发布，更新内容如下：</p> 
<ul> 
 <li>Android：修复 arm64 mac 上的 NDK 工具链目录</li> 
 <li>NVHPC-CXX：添加对 C++20 的支持</li> 
 <li>CUDA/Clang：简化 --register-link-binaries 逻辑</li> 
 <li>NVHPC-C：添加对 C17 的支持</li> 
 <li>AUTOUIC：在 UI headers 和时间戳之间添加循环依赖性测试</li> 
 <li>FindMPI：不将 <code>framework</code> 检测为编译标志</li> 
 <li>VS：修复 INTERFACE 库中 INCLUDE_DIRECTORIES 上的断言失败；</li> 
 <li>VS：修复 v142 和 v143 的 /reference 和 /headerUnit 标志表条目；</li> 
 <li>CheckLanguage：避免 CMP0126 警告</li> 
 <li>VS：在 VS 16.11 下为 <code>-T version=14.29.16.11</code> 添加特殊情况</li> 
 <li>VS：为 Preview 3.1 更新 Visual Studio 17 2022 生成器</li> 
 <li>帮助：为 CPACK_DMG_FILESYSTEM 添加缺少的版本添加注释</li> 
 <li>BinUtils：避免搜索 CMAKE_PREFIX_PATH</li> 
 <li>macOS：恢复对 Mac OS X 10.4 (Tiger) 的支持</li> 
 <li>平台/Haiku：删除 include-once 的行为</li> 
 <li>CMakePresets：使用自己的文件版本检查预设</li> 
 <li>CTest：将多选项重置为持久性多选项</li> 
 <li><code>add_custom_command(DEPFILE)</code> 独立于 <code>CMAKE_DEPENDS_USE_COMPILER</code></li> 
 <li>帮助：get_filename_component：修复 cmake_path 的版本信息</li> 
 <li>帮助：cmake_path：添加缺少的参数</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-21-2-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-21-2-available-for-download/</a></p>
                                        </div>
                                      
</div>
            