
---
title: 'Cmake 3.24.1 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6357'
author: 开源中国
comments: false
date: Sun, 21 Aug 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6357'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CMake 3.24.1 现已发布，一些亮点更新内容如下：</p> 
<ul> 
 <li><span style="color:#000000">automoc：避免 linker-warning-silencing code 中的编译器警告</span></li> 
 <li>FindThreads：针对 MSVC ABI 时跳过检查 -pthread 标志</li> 
 <li>IPO：不要在 Windows 上的 GCC 10.x 中使用 -flto=auto</li> 
 <li>export：恢复对私有共享库依赖关系的排除检查</li> 
 <li>MinGW：当工具链前缀名称不可用时使用 windres 恢复</li> 
 <li>FindVulkan：恢复未知 FATAL_ERROR 组件的容差</li> 
 <li>Help：添加 3.24 版本关于 FindVulkan 组件执行的说明</li> 
 <li>TI compiler：添加对 COMPILE_WARNING_AS_ERROR 目标属性的支持</li> 
 <li>Help：列出 COMPILE_WARNING_AS_ERROR 支持的编译器 ID</li> 
 <li>Help：缺少对 --compile-no-warning-as-error 的 cross-reference</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kitware.com%2Fcmake-3-24-1-is-available-for-download%2F" target="_blank">https://www.kitware.com/cmake-3-24-1-is-available-for-download</a></p>
                                        </div>
                                      
</div>
            