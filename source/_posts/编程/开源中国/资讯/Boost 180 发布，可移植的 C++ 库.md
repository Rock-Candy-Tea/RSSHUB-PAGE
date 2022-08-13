
---
title: 'Boost 1.80 发布，可移植的 C++ 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1600'
author: 开源中国
comments: false
date: Sat, 13 Aug 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1600'
---

<div>   
<div class="content">
                                                                                            <p>Boost 是一套用于 C++ 编程语言的库，为线性代数、伪随机数生成、多线程、图像处理、正则表达式和单元测试等任务和结构提供支持。它包含了 164 个单独的库（截至 1.76 版）。</p> 
<h3>已知问题</h3> 
<p>这些是库的作者提出的补丁，由于发现得太晚，所以在发行版中没有修复。</p> 
<ul> 
 <li>Boost.Filesystem 目录迭代器在 Windows 10 之前可能无法为网络共享构建</li> 
 <li>在 Windows 上的 Boost.Filesystem 中， <code>weakly_canonical</code> 无法处理以 "\\?\" 开头的路径</li> 
</ul> 
<h3>更新的库</h3> 
<ul> 
 <li>Asio: 
  <ul> 
   <li>将 <code>append</code>、 <code>predpend</code>、 <code>as_tuple</code> 和 <code>deferred</code> 移至 boost::asio 命名空间，并使它们与 C++11 兼容。</li> 
   <li>使得 <code>experimental::parallel_group</code> 与 C++11 兼容</li> 
   <li>为连续的容器（如 <code>std::span</code>）增加了 <code>buffer()</code> 重载</li> 
   <li>……</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.boost.org%2Flibs%2Fatomic%2F" target="_blank">Atomic</a>: 
  <ul> 
   <li>改进了 ARM、AArch32 和 AArch64 目标上的字节数检查的可移植性</li> 
   <li>修正了 MSVC 14.0（Visual Studio 2015）在 C++17 模式下的编译</li> 
  </ul> </li> 
 <li>文件系统。 
  <ul> 
   <li>在 Windows 上，增加了一个回退实现，用于在文件因 <code>ERROR_ACCESS_DENIED</code> 错误而无法打开的情况下查询文件属性。</li> 
   <li>在 Windows 上，为 FAT/exFAT 文件系统增加了一个解决方法，在查询文件属性时产生 <code>ERROR_INVALID_PARAMETER</code>。</li> 
   <li>解决了 RTEMS 上的一个编译问题</li> 
   <li>在 Linux 上，如果 copy_file_range 在运行时与 ENOSYS 一起失败，纠正了切换到 sendfile copy_file 的实现。</li> 
   <li>在支持 openat 和 POSIX.1-2008 中定义的相关 API 的 POSIX 系统上，以及在 Windows Vista 和更高版本上，改进了针对 CVE-2022-21658 的 <code>remove_all</code> 保护</li> 
  </ul> </li> 
 <li>GIL：计划在 Boost 1.80 之后的一到两个版本中，将 C++17 作为最低要求的 C++ 语言版本</li> 
 <li>迭代器 
  <ul> 
   <li>对于 C++11 和更高版本，增加了对写给 <code>function_output_iterator</code> 的值的完美转发的支持</li> 
   <li>增加了对向 <code>function_output_iterator</code> 写入一个取消引用另一个 <code>function_output_iterator</code> 的结果的保护。</li> 
  </ul> </li> 
 <li>JSON 
  <ul> 
   <li>增加了 string::subview() 重载。</li> 
   <li>修正了 array::erase(it) 的 segfault。</li> 
   <li>修正了 libc++ 上序列化的低性能</li> 
   <li>修正了在 big-endian 平台上的解析问题</li> 
   <li>修正了对尾部逗号后的注释的处理。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.boost.org%2Flibs%2Flocale%2F" target="_blank">Locale</a>: 
  <ul> 
   <li>废弃了对 C++03 和更早版本的支持</li> 
   <li>修复了ICU整理器在转换空字符串时出现的UB/断言故障</li> 
   <li>修复一些与共享库中类的可见性有关的问题</li> 
   <li>修复与 C++20 模式的兼容性</li> 
   <li>修复与 BOOST_USE_WINDOWS_H 的兼容性问题</li> 
   <li>修复了由于缺失包含物而导致的构建失败问题</li> 
   <li>处理或压制许多警告，使构建日志更清晰</li> 
  </ul> </li> 
</ul> 
<h3>Boost 的主要测试编译器是</h3> 
<ul> 
 <li>Linux: 
  <ul> 
   <li>Clang: 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 12.0.0, 13.0.0, 14.0.0</li> 
   <li>Clang, C++11: 3.4, 11.0.0, 13.0.0, 14.0.0</li> 
   <li>Clang, C++14: 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 5.0, 12.0.0, 13.0.0, 14.0.0</li> 
   <li>Clang, C++17: 6.0.1, 7.0.0, 8.0.0, 9.0.0, 10.0.0, 11.0.0, 12.0.0, 13.0.0, 14.0.0</li> 
   <li>Clang, C++20: 11.0.0, 12.0.0, 13.0.0, 14.0.0</li> 
   <li>GCC: 4.6.3, 11, 12</li> 
   <li>GCC, C++11: 4.7.3, 4.8.5, 11, 12</li> 
   <li>GCC, C++14: 5.4.0, 6.4.0, 7.3.0, 8.0.1, 9.1.0, 11, 12</li> 
   <li>GCC, C++17: 7.3.0, 8.0.1, 9.1.0, 11, 12</li> 
   <li>GCC, C++20: 8.0.1, 9.1.0, 10, 11, 12</li> 
  </ul> </li> 
 <li>OS X: 
  <ul> 
   <li>Apple Clang: 11.0.3</li> 
   <li>Apple Clang, C++11: 11.0.3</li> 
   <li>Apple Clang, C++14: 11.0.3</li> 
   <li>Apple Clang, C++17: 11.0.3</li> 
   <li>Apple Clang, C++20: 11.0.3</li> 
  </ul> </li> 
 <li>Windows: 
  <ul> 
   <li>Visual C++: 10.0, 11.0, 12.0, 14.0, 14.1, 14.2, 14.3</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fboostorg%2Fboost%2Freleases%2Ftag%2Fboost-1.80.0" target="_blank">https://github.com/boostorg/boost/releases/tag/boost-1.80.0</a></p>
                                        </div>
                                      
</div>
            