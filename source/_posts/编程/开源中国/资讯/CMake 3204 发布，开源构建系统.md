
---
title: 'CMake 3.20.4 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6317'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6317'
---

<div>   
<div class="content">
                                                                                            <p>CMake 3.20.4 已经发布，CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p>CMake 3.20.4 中的一些重要变更有：</p> 
<ul> 
 <li>ci：使用一致的 sccache 构建</li> 
 <li>VS: 在 VS 16.10 下增加'-T version=14.29.16.10'的特殊情况</li> 
 <li>gitlab-ci: 更新 Windows 构建至 MSVC 19.29-16.10 工具集</li> 
 <li>Makefiles: 修复 CMAKE_EXPORT_COMPILE_COMMANDS 在自定义编译规则下的崩溃问题</li> 
 <li>presets：修复 buildPreset "jobs" 字段的测试案例</li> 
 <li>IRSL：在 Windows 上添加 Intel oneAPI 的 redist 位置</li> 
 <li>fileapi：修复 codemodel-v2 链接命令片段的相对路径</li> 
 <li>FindBoost：在 Boost 1.75 以上版本中增加对 json component header 的检查</li> 
 <li>Help：cmake_path：修正 IS_PREFIX 的错误示例</li> 
 <li>MSVC：C++20 final flag，C++23 支持</li> 
 <li>Clang/MSVC：C++20 final flag，C++23 支持</li> 
 <li>presets：修复 buildPreset "jobs"</li> 
 <li>presets：修复 buildPreset "target "不允许使用单一字符串的问题</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-20-4-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-20-4-available-for-download/</a></p>
                                        </div>
                                      
</div>
            