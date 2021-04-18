
---
title: 'Boost 1.76.0 发布，可移植的 C++ _后备_标准库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3861'
author: 开源中国
comments: false
date: Sun, 18 Apr 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3861'
---

<div>   
<div class="content">
                                                                                            <p>可移植的 C++ “后备”标准库 Boost 发布了 1.76.0 版本，Boost 库是一个经过千锤百炼、可移植、提供源代码的 C++ 库，作为标准库的后备，是 C++ 标准化进程的发动机之一，由 C++ 标准委员会库工作组成员发起。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>Asio 
  <ul> 
   <li>添加了 ip::scope_id_type 类型别名</li> 
   <li>添加了 ip::port_type 类型别名</li> 
   <li>重构 SFINAE 用法以缩短编译时间</li> 
   <li>将 any_io_executor 改为 "强 typedef" 风格的类</li> 
   <li>确保在所有平台上清除 pthread 条件变量属性</li> 
  </ul> </li> 
 <li>Atomic 
  <ul> 
   <li>修复了 ARM 的 MSVC 编译问题</li> 
  </ul> </li> 
 <li>Bind 
  <ul> 
   <li>在 boost::bind 中增加对使用标准 C++11 占位符的支持</li> 
   <li>更新 boost:: 以适用于可变参数模板</li> 
  </ul> </li> 
 <li>Container 
  <ul> 
   <li>在所有容器中添加了 no-discard 属性，以捕获与未使用返回值有关的错误</li> 
   <li>用 Boost.Container 自己的类替换了默认的标准异常类，大大减少了包含的文件开销。例如：在MSVC 19 boostcontainervector.hpp 中，预处理文件大小从 1.5MB 减少到 930KB。如果你还想使用标准异常类，可以在使用任何 Boost.Container 类之前定义 BOOST_CONTAINER_USE_STD_EXCEPTIONS</li> 
  </ul> </li> 
 <li>Core 
  <ul> 
   <li>在兼容的参考包装器之间添加隐式转换</li> 
   <li>添加 boost/core/cmath.hpp，这是来自 cmath 的浮点分类函数的可移植实现</li> 
   <li>添加 boost/core/bit.hpp，这是 C ++ 20 标准头文件 bit 的可移植实现</li> 
   <li>修复 C++20 下字符类型的 BOOST_TEST_EQ、BOOST_TEST_NE</li> 
  </ul> </li> 
 <li>DLL 
  <ul> 
   <li>boost::dll::import 改名为 boost::dll::import_symbol，以避免与 C++20 的导入关键字冲突</li> 
  </ul> </li> 
 <li>Filesystem 
  <ul> 
   <li>更新了与 ​​WASI 平台的兼容性</li> 
   <li>修复了 path::remove_filename 在路径为 "////" 时引发的异常</li> 
   <li>修复了 create_directories 无视内部发出的文件状态查询操作的错误。这可能导致 create_directories 返回错误代码</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.boost.org%2Fusers%2Fhistory%2Fversion_1_76_0.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            