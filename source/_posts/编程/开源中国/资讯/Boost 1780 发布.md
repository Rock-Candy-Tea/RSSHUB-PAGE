
---
title: 'Boost 1.78.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5491'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5491'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Boost 是一套用于 C++ 编程语言的库，为线性代数、伪随机数生成、多线程、图像处理、正则表达式和单元测试等任务和结构提供支持。它包含了 164 个单独的库（截至 1.76 版）。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新库</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>该版本没有新的库</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">更新的库</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Asio:</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>增加了一个 io_uring 后端，可以选择用于所有 I/O 对象</li> 
   <li>在 POSIX 和 Windows 上增加了对便携式管道的支持</li> 
   <li>增加了对注册缓冲区的支持</li> 
   <li>实现了对<span> </span><code>experimental::coro</code><span> </span>的改进</li> 
   <li>当使用 MSVC 运行时，禁用了 clang 上的<span> </span><code>aligned_alloc</code></li> 
   <li>将<span> </span><code>io_context</code><span> </span>执行器的大小减少到一个指针</li> 
   <li>增加了<span> </span><code>execution::any_executor</code><span> </span>和<span> </span><code>any_io_executor</code><span> </span>的小对象缓冲区的大小</li> 
   <li>修正了与新版 gcc 和 clang 的兼容性</li> 
   <li>修正了在 Solaris 上的编译</li> 
   <li>修正了 bind_executor 与完成 token 的兼容性</li> 
   <li>修正了定义<span> </span><code>BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT</code><span> </span>时的构建错误</li> 
   <li>修复了各种警告</li> 
   <li>……</li> 
  </ul> </li> 
 <li><strong>Assert:</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>添加 <code>source_location::to_string</code></li> 
  </ul> </li> 
 <li><strong>Atomic:</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>在 macOS 10.12、iOS 10.0、tvOS 10.0 或 watchOS 3.0 之后的 Darwin 系统上，增加了一个用于等待和通知操作的 ulock 后端</li> 
   <li>在 Windows 上，纠正了针对 Windows 8 或更高版本时，<span> </span><code>atomic-type::always_has_native_wait_notify</code><span> </span>与相应能力宏之间的差异</li> 
   <li>添加了一个解决 Visual Studio 2015 Update 3 之前的编译错误的方法</li> 
   <li>对于枚举、类和浮点类型，atomic 和 ipc_atomic 的初始化构造函数现在是 constexpr</li> 
   <li>根据 C++20，atomic 和 ipc_atomic 现在执行所含对象的值初始化</li> 
   <li>为 AIX 上因汇编工具不支持数字标签而导致的编译错误添加了一个解决方法</li> 
   <li>……</li> 
  </ul> </li> 
 <li><strong>Beast:</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>本次维护更新带来了小的错误修复和更新的 CI 报告</li> 
   <li>修复了 zlib 实现中的安全漏洞 CVE-2016-9840</li> 
   <li>修正了 WebSocket permessage_deflate 的实现，这应该会使使用 Beast WebSockets 时的压缩性能提高。</li> 
   <li>……</li> 
  </ul> </li> 
 <li><strong>Core:</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>在 <boost/core/cmath.hpp> 中增加了一个通用的实现</li> 
   <li>添加了 boost::core:type_name，这是一个以字符串形式返回类型名称的实用函数。</li> 
   <li>添加了 boost::span，这是 C++20 的 std::span 的 C++11 实现</li> 
  </ul> </li> 
 <li><strong>DLL:</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修正了缺失的 #include</li> 
   <li>弃用 TravisCI，改用 GithubAction CI</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">……</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fboostorg%2Fboost%2Freleases%2Ftag%2Fboost-1.78.0" target="_blank">https://github.com/boostorg/boost/releases/tag/boost-1.78.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            