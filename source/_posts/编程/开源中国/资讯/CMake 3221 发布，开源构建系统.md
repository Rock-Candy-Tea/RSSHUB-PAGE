
---
title: 'CMake 3.22.1 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2170'
author: 开源中国
comments: false
date: Fri, 10 Dec 2021 06:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2170'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CMake 3.22.1 发布，更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>gitlab-ci：修复 comment typo</li> 
 <li>gitlab-ci：缩短 job prefixes</li> 
 <li>ci：在 Debian 基础镜像中加入 gmock</li> 
 <li>try_compile：不要使用 CMAKE_BUILD_TYPE 或 CMAKE_CONFIGURATION_TYPES 环境变量</li> 
 <li>Help：记录更多CMAKE_POLICY_DEFAULT_CMPNNN的使用情况</li> 
 <li>gitlab-ci：更新 macOS jobs 以使用 Xcode 13.1</li> 
 <li>CompilerId：通过避免 C++风格的注释来恢复对 classic C 的支持</li> 
 <li>file(RPATH)：如果新的 RPATH 为空，则恢复未知格式的容忍度</li> 
 <li>FindPkgConfig：恢复在 pkgconf 之前 finding pkg-config 的功能</li> 
 <li>ci：启用更多使用托管代码的 VS 测试</li> 
 <li>Utilities/Release：添加脚本以签署/公证 macOS 应用程序捆绑包</li> 
 <li>HIP：为 HIP 启用 CMAKE_EXPORT_COMPILE_COMMANDS</li> 
 <li>mingw：修正 strftime() 的调用规则</li> 
 <li>Help：明确声明 if(ENV&#123;some_var&#125;) 始终为 false</li> 
 <li>Help：更明确地说明 if(<string>) 的行为</li> 
 <li>UseSWIG：确保存在 depfile 目录</li> 
 <li>FindPython：阐明静态库使用提示</li> 
 <li>CMakeParseLibraryArchitecture：修复解析 /lib/<arch> 的隐式对象路径的问题</li> 
 <li>......</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-22-1-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-22-1-available-for-download/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            