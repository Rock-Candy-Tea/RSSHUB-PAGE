
---
title: 'Julia 1.6.0 发布，高性能动态高级编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eaba9e9f170d8467422167fc0e080149ccc.png'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 23:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eaba9e9f170d8467422167fc0e080149ccc.png'
---

<div>   
<div class="content">
                                                                                            <p>Julia 1.6.0 现已发布。Julia 是一个高性能动态高级编程语言。其拥有丰富的函数库，提供了数字精度、精致的增幅器和分布式并行运行方式。核心函数库等大多数库由 Julia 编写，但也用成熟的 C 和 FORTRAN 库来处理线性代数、随机数产生和字符串处理等问题。 </p> 
<p><img alt height="100" src="https://oscimg.oschina.net/oscnet/up-eaba9e9f170d8467422167fc0e080149ccc.png" width="155" referrerpolicy="no-referrer"></p> 
<p>官方表示，Julia 1.6.0  很可能会成为下一个长期支持（LTS）版本。因此，其花了很多时间来开发这个版本，以确保那些对生态系统未来健康发展所需的功能能够被纳入到这个版本中。此外，开发团队还针对所有已注册的开源软件包对该版本进行了回归测试，并对问题进行了跟踪和修正。关于 Julia 1.6 是否会成为新的 LTS，最终的决定将在经过实战测试后，也就是 1.7 版本进入稳定状态前后做出。</p> 
<p>此版本的一些更新亮点如下：</p> 
<ul> 
 <li><strong>并行预编译：</strong>执行一个模块中的所有语句往往涉及到编译大量的代码，所以 Julia 创建了模块的预编译缓存来减少这个时间。在 1.6 中，这个包的预编译速度更快，并且在退出<code>pkg></code>模式之前发生。</li> 
</ul> 
<pre><code><strong>(v1.6) pkg></strong> add DifferentialEquations
...
Precompiling project...
  Progress [========================================>]  112/112
112 dependencies successfully precompiled in 72 seconds

<strong>julia></strong> <strong>@time</strong> <strong>using</strong> DifferentialEquations
  4.995477 seconds …</code></pre> 
<ul> 
 <li><strong>编译时间百分比</strong></li> 
 <li><strong>消除不必要的重新编译</strong></li> 
 <li><strong>减少编译器延迟：</strong>开发团队一直在尝试加快编译器本身的速度。此版本中没有任何重大突破，但鉴于在方法表数据结构上的工作，还是实现了一些适度的改进。</li> 
 <li><strong>帮助优化程序包延迟的工具：</strong>Julia 1.6 与 SnoopCompile v2.2.0 或更高版本相结合，为 compiler introspection 提供了新的工具，特别是（但不限于）类型推理。开发人员可以使用新工具来分析类型推断，并确定特定的包实现选择如何与编译时间交互。早期采用者已经使用这些工具消除了从百分之几到大部分的首次使用延迟。</li> 
 <li><strong>二进制加载加​​速</strong></li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-055bd90058de0c728eadb01b6cad87bc32f.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>下载和网络选项：</strong>在 Julia 1.6 中，所有的下载都是通过新的 Download.jl 标准库用 libcurl-7.73.0 完成的。下载是在进程中完成的，TCP+TLS 连接是共享和重用的。如果服务器支持 HTTP/2，向该服务器发出的多个请求甚至可以复用到同一个 HTTPS 连接上。所有这些都意味着下载速度更快。</li> 
 <li><strong>CI Robustness</strong></li> 
 <li><strong>改进的 stacktrace 格式</strong></li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6ed25e7158c109db330f46bb236d75e3b87.png" referrerpolicy="no-referrer"></p> 
<p>更多详细内容可查看官方博客： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjulialang.org%2Fblog%2F2021%2F03%2Fjulia-1.6-highlights%2F" target="_blank">https://julialang.org/blog/2021/03/julia-1.6-highlights/</a></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjulialang.org%2Fdownloads%2F" target="_blank">https://julialang.org/downloads/</a></p>
                                        </div>
                                      
</div>
            