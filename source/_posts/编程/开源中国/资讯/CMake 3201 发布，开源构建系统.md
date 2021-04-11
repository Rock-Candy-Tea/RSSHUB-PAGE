
---
title: 'CMake 3.20.1 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=698'
author: 开源中国
comments: false
date: Sun, 11 Apr 2021 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=698'
---

<div>   
<div class="content">
                                                                                            <p>CMake 3.20.1 已经发布，CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p>CMake 3.20.1 中的一些重要变更有：</p> 
<ul> 
 <li>Help：添加 Q_NAMESPACE_EXPORT 到 CMAKE_AUTOMOC_MACRO_NAMES 的默认值</li> 
 <li>FindHDF5：搜索新的 Fortran HL 库名</li> 
 <li>gitlab-ci：更新 Windows 构建到 MSVC 19.28-16.9 工具集</li> 
 <li>FindIntl：修正 C 库中内置的 intl 检测</li> 
 <li>Ninja Multi-Config：修正自定义命令配置时无输出的崩溃</li> 
 <li>Tests：增加 RunCMake helper 来运行普通脚本</li> 
 <li>UseSWIG：将 swig 部署文件转换为与 Ninja generator 路径匹配的文件</li> 
 <li>恢复对初始语言标志中反斜杠的支持</li> 
 <li>CPack：验证并记录 NSIS branding text trim positions</li> 
 <li>Cleanup：修正本地 C++ 变量名称的拼写错误</li> 
 <li>Apple：在非 macOS 上也设置 CMAKE_SHARED_LIBRARY_RUNTIME_C_FLAG</li> 
 <li>Android：修复 search for binutils</li> 
 <li>Cray：检测 Fortran 编译器版本补丁级别（如果有的话）</li> 
 <li>......</li> 
</ul> 
<p>详细信息可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-20-1-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-20-1-available-for-download/</a></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcmake.org%2Fdownload%2F" target="_blank">https://cmake.org/download/</a></p>
                                        </div>
                                      
</div>
            