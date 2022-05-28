
---
title: 'CMake 3.23.2 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7087'
author: 开源中国
comments: false
date: Sat, 28 May 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7087'
---

<div>   
<div class="content">
                                                                                            <p>CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p>CMake 3.23.2 现已发布，具体更新内容如下：</p> 
<ul> 
 <li>CPack/NuGet：在 Windows 上恢复 component packaging</li> 
 <li>cmInstallCommand：调整错误信息</li> 
 <li>cmExportBuildFileGenerator：处理 genex-wrapped 的源路径</li> 
 <li>ci：使用 CMake 3.23.1</li> 
 <li>CheckLinkerFlag：当 checked flag 被忽略时，捕获 linker warning</li> 
 <li>CheckCompilerFlags：撤销 "Catch linker warning about ignored flags"</li> 
 <li>gitlab-ci：更新 macOS jobs 以使用 Xcode 13.3</li> 
 <li>FindBoost：增加对 Boost 1.79 的支持</li> 
 <li>cmGeneratedFileStream：不要删除空路径</li> 
 <li>gitlab-ci：更新 Windows builds 至 MSVC 19.32 toolset</li> 
 <li>productbuild：恢复 CPACK_PACKAGEMAKER_CHOICES 变量</li> 
 <li>CPackIFW：修复图标文件名中的回归</li> 
 <li>FindPython：添加对 pypy v7.3.9 和更高版本的支持</li> 
 <li>FindPython：修复拼写错误</li> 
 <li>FindJava、FindJNI：确保正确处理 Windows 上的版本</li> 
 <li>CMakePackageConfigHelpers：修复关于版本文件支持范围的说明</li> 
 <li>......</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kitware.com%2Fcmake-3-23-2-available-for-download%2F" target="_blank">https://www.kitware.com/cmake-3-23-2-available-for-download/</a></p>
                                        </div>
                                      
</div>
            