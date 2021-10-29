
---
title: 'CMake 3.21.4 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2500'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 06:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2500'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CMake 3.21.4 现已发布。CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CMake 3.21.4 <span style="color:#333333">中的一些变更内容有：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#333333">Tests/RunCMake/Autogen：测试 CMP0111 behavior</span></li> 
 <li><span style="color:#333333">cmQtAutoGenInitializer：支持 IMPLIB-only imported targets</span></li> 
 <li><span style="color:#333333">Tests：为 Xcode 13.0 修复 RunCMake.XcodeProject XcodeIOSInstallCombined cases</span></li> 
 <li>gitlab-ci：更新 macOS jobs 以使用 Xcode 13.0</li> 
 <li>bootstrap：启用 cmake_language 命令以支持 Qt 6.2 的 cmake-gui</li> 
 <li>ci：启用 CTest.Update&#123;CVS,SVN,HG&#125; 测试</li> 
 <li>MSVC：在较早的编译器版本上容忍 cxx_std_23 功能</li> 
 <li>zstd：从 zstd 1.5.0 反向移植修复 armv6 上 SIGBUS</li> 
 <li>Source：修复 _WIN32 preprocessor checks 中的错字</li> 
 <li>CPack/IFW：添加对 QtIFW 4.1 的支持</li> 
 <li><span style="color:#333333">FindMatlab：添加 R2021b => 9.11 版本</span></li> 
 <li><span style="color:#333333">NVHPC：仅对 C 和 CXX 语言使用“-MD”</span></li> 
 <li><span style="color:#333333">FortranCInterface：修复时间戳检查中的回归</span></li> 
 <li>TestDriver：修复 C++ 模式下的 old-style-cast 警告</li> 
 <li>GNUInstallDirs：修复对 LIBEXECDIR 上 Debian Policy 的误解</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">更多详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-21-4-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-21-4-available-for-download/</a></p>
                                        </div>
                                      
</div>
            