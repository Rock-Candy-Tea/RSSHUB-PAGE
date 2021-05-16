
---
title: 'OTP 24 正式发布，Erlang 应用服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3401'
author: 开源中国
comments: false
date: Sat, 15 May 2021 08:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3401'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OTP 24 现已发布。OTP (Open Telecom Platform) 是一个用 Erlang 编写的应用服务器，它是一套 Erlang 库，由 Erlang 运行时系统、主要使用 Erlang 编写的许多随时可用的组件以及 Erlang 程序的一组设计原则组成。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>编译器现在会在定义后立即内联那些只使用一次的函数</li> 
 <li>编译器警告和错误现在除了行号外还包括列号</li> 
 <li>绑定在关键字 "try" 和 "of" 之间的变量现在可以在关键字 "of" 之后的子句中使用</li> 
 <li>如果生成器的类型不正确，将引发一个 &#123;bad_generator,Generator&#125; 异常。如果过滤器的值不是布尔值，将引发一个<br> &#123;bad_filter,Filter&#125; 异常</li> 
 <li>现在可以使用以 “_” 开头的变量来禁止使用匿名变量 “_”</li> 
 <li>选择性接收优化现在将被更多地应用</li> 
 <li>二进制模块中增加了十六进制编码和解码功能</li> 
 <li>BeamAsm JIT-compiler 已被添加到 Erlang/OTP 中，并将为许多应用带来显著的性能提升。在大多数拥有可以编译 C++17 的 C++ 编译器的 x86 64 位平台上，JIT-compiler 是默认启用的</li> 
 <li>一个用于 gen_tcp 的兼容适配器已经被实现，以使用新的套接字 API(gen_tcp_socket)</li> 
 <li>EEP 54 中提出的 BIF 调用失败的扩展错误信息已经实现</li> 
 <li>引入了 EEP53 所概述的流程别名</li> 
 <li>在监督员中实现了 EEP 56。它增加了重要子代的概念以及 auto_shutdown 监督器标志</li> 
 <li>增加对 FTPES 的支持（通过 TLS 的显式 FTP）</li> 
</ul> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erlang.org%2Fnews%2F148" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            