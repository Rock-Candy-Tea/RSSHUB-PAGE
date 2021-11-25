
---
title: 'CMake 3.22.0 发布，开源构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6469'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6469'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CMake 是一个跨平台的自动化构建系统，它使用一个名为 CMakeLists.txt 的文件来描述构建过程，可以产生标准的构建文件，如 Unix 的 Makefile 或 Windows Visual C++ 的 projects/workspaces 。文件 CMakeLists.txt 需要手工编写，也可以通过编写脚本进行半自动的生成。</p> 
<p>CMake 3.22.0 发布，更新内容如下：</p> 
<ul> 
 <li>命令： 
  <ul> 
   <li><code>cmake_host_system_information()</code> 命令现在能够从 <code>/etc/os-release</code> 文件中查询操作系统识别变量。</li> 
   <li><code>string(TIMESTAMP)</code> 命令现在支持用于 ISO 8601 周数的 %V 指定符。</li> 
  </ul> </li> 
 <li>变量： 
  <ul> 
   <li>新增了 <code>CMAKE_BUILD_TYPE</code> 环境变量，为 <code>CMAKE_BUILD_TYPE</code> 变量提供了一个默认值。</li> 
   <li>增加了 <code>CMAKE_CONFIGURATION_TYPES</code> 环境变量，为 <code>CMAKE_CONFIGURATION_TYPES</code> 变量提供默认值。</li> 
   <li>新增了 <code>CMAKE_INSTALL_MODE</code> 环境变量，用于告诉 install() 规则安装符号链接而不是复制文件。</li> 
   <li>新增了 <code>CMAKE__LINK_WHAT_YOU_USE_FLAG</code> 和 <code>CMAKE_LINK_WHAT_YOU_USE_CHECK</code> 变量，用于控制 <code>LINK_WHAT_YOU_USE</code> 目标属性使用的链接器标志和检查。</li> 
   <li>新增了 <code>CMAKE_REQUIRE_FIND_PACKAGE_</code> 变量，用于将非必需的 find_package() 调用变成必需的。</li> 
  </ul> </li> 
 <li>属性： 
  <ul> 
   <li>现在 _EXTENSIONS 目标属性被初始化为 <code>CMAKE__EXTENSIONS_DEFAULT</code>，由编译器检测。</li> 
   <li>VS_SETTINGS 源文件属性现在支持所有源文件类型，之前它只对非构建的源文件起作用。</li> 
  </ul> </li> 
 <li>弃用和删除的功能： 
  <ul> 
   <li>Visual Studio 10 2010 生成器现在已被弃用，并将在未来的 CMake 版本中被移除。</li> 
  </ul> </li> 
 <li>其他变化： 
  <ul> 
   <li>当没有指定标准级别时，编译功能现在可以正确地禁用或启用编译器扩展，并且如果要求的设置与编译器的默认值一致，则可以避免不必要地添加语言标准标志。</li> 
   <li>编译特性功能现在会忽略未启用的语言的特性。</li> 
   <li>Ninja 生成器现在使用 ccmake(1) 来实现 edit_cache 目标（如果有的话）。</li> 
   <li>CPack NSIS 生成器现在需要 NSIS 3.03 或更高版本。</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.kitware.com%2Fcmake-3-22-0-available-for-download%2F" target="_blank">https://blog.kitware.com/cmake-3-22-0-available-for-download/</a></p>
                                        </div>
                                      
</div>
            