
---
title: 'Julia 1.8.0 发布，科学计算领域高性能语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9f7155165c01c81f7a019d2a8ab85064130.png'
author: 开源中国
comments: false
date: Sat, 20 Aug 2022 07:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9f7155165c01c81f7a019d2a8ab85064130.png'
---

<div>   
<div class="content">
                                                                                            <p>Julia 编程语言 1.8 版本已发布，这是一种通用的高性能语言，在科学计算和数值分析中较为流行。Julia 1.8 是 1.x 系列版本中的第八个次要版本，添加了一些新特性和功能，主要更改如下：</p> 
<h2><strong>可变结构字段上的 const</strong></h2> 
<p>Julia 支持使用 const 注释对可变结构的各个字段进行注释：</p> 
<pre><code>mutable struct T
    x::Int
    const y::Float64
end</code></pre> 
<p>这导致字段 y 保持不变（在创建类型后无法重新分配），可以用来强制执行不变量，编译器也可以利用它来改进生成的代码。</p> 
<h2><strong>Call site @inline</strong></h2> 
<p>在 Julia 1.8 之前，@inline 宏只能用于方法定义，且该函数将在方法的所有调用点内联。</p> 
<p>现在还可以将@inline 宏作为@inline f(x) 应用于给定的调用站点，告诉编译器在特定调用处内联该方法。</p> 
<h2><strong>类型化的全局变量</strong></h2> 
<p>Julia 中的非常量全局变量会带来性能损失，因为编译器无法推断它们的类型，它们在运行时可以重新分配给其他类型的另一个对象。</p> 
<p>在 Julia 1.8 中可以使用 x::T 语法指定非常量全局变量的类型，其中 T 是全局变量的类型。此时尝试将变量重新分配给另一种类型的对象时会出错：</p> 
<pre><code>julia> x::Int = 0
0

julia> x = "string"
ERROR: MethodError: Cannot `convert` an object of type String to an object of type Int64
...</code></pre> 
<p>类型化全局变量消除了使用非常量全局变量的大部分成本。</p> 
<h2>@threads 新的默认调度程序</h2> 
<p>在 Julia 1.3 中引入通用并行任务运行时之前，Julia 就有了用于并行化 for 循环的 @threads 宏。 由于这个历史原因，@threads 一直提供静态调度，以避免意外依赖这种严格行为而破坏程序。</p> 
<p>为了多任务系统能更好工作， Julia 1.5 中引入了 :static 调度程序，为将来更改默认调度行为做好准备。而在 Julia 1.8 中，使用 @threads 编写的程序可以充分利用动态和可组合的任务调度程序。在 Julia 1.8 之前，该程序模拟需要 6 秒钟才能完成：</p> 
<pre><code>julia> @time begin
            Threads.@spawn busywait(5)
            Threads.@threads for i in 1:Threads.nthreads()
                busywait(1)
            end
        end
6.003001 seconds (16.33 k allocations: 899.255 KiB, 0.25% compilation time)</code></pre> 
<p>在 1.8 版本中一个未占用的线程可以运行两次 1 秒的迭代来完成 for 循环，因此程序跑完只需要 2 秒：</p> 
<pre><code>julia> @time begin
            Threads.@spawn busywait(5)
            Threads.@threads for i in 1:Threads.nthreads()
                busywait(1)
            end
        end
2.012056 seconds (16.05 k allocations: 883.919 KiB, 0.66% compilation time)</code></pre> 
<h2>新的分配分析器 Profiling</h2> 
<p>不必要的堆分配会严重降低性能，而现有的跟踪工具（@time 和 --track-allocation）不能提供足够的细粒度细节、良好的可视化和易用性。</p> 
<p>Julia 1.8 有了新的分配分析器 (Profile.Allocs)，它使用每个类型、大小和堆栈跟踪来捕获堆分配，并使用 PProf.jl 轻松可视化。</p> 
<p>如下所示，VS Code 的 Julia 扩展通过 @profview_allocs 提供对图解分析功能：</p> 
<p><img alt height="497" src="https://oscimg.oschina.net/oscnet/up-9f7155165c01c81f7a019d2a8ab85064130.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>Packages 更新</h2> 
<p>添加了一个新工具（宏： InteractiveUtils.@time_imports），以深入了解加载依赖项对包加载时间的影响，该宏在 REPL 中直接可用。</p> 
<pre><code>julia> @time_imports using CSV
     50.7 ms  Parsers 17.52% compilation time
      0.2 ms  DataValueInterfaces
      1.6 ms  DataAPI
      0.1 ms  IteratorInterfaceExtensions
      0.1 ms  TableTraits
     17.5 ms  Tables
     26.8 ms  PooledArrays
    193.7 ms  SentinelArrays 75.12% compilation time
      8.6 ms  InlineStrings
     20.3 ms  WeakRefStrings
      2.0 ms  TranscodingStreams
      1.4 ms  Zlib_jll
      1.8 ms  CodecZlib
      0.8 ms  Compat
     13.1 ms  FilePathsBase 28.39% compilation time
   1681.2 ms  CSV 92.40% compilation time</code></pre> 
<p>编译时间以百分比显示。</p> 
<p> </p> 
<p>其他内容还包括改进的预编译、改进了对 Apple Silicon 的支持等，更多内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjulialang.org%2Fblog%2F2022%2F08%2Fjulia-1.8-highlights%2F" target="_blank">官方博客</a>中阅读。</p>
                                        </div>
                                      
</div>
            