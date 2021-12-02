
---
title: 'Julia 1.7 版本发布，科学计算领域高性能语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=724'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=724'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Julia 编程语言 1.7 版本已发布，这是一种通用的高性能语言，在科学计算和数值分析中较为流行。Julia 1.7<span> </span><span style="color:#24292f">是 1.x 系列版本中的第七个次要版本，</span>添加了一些新特性和功能，主要更改如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新的 Xoshiro256 系列随机数生成器（RNG）</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#212529">Julia 一开始使用流行的 Mersenne Twister 算法作为其默认的随机数生成器，但 Mersenne Twister 的计算周期较长，而且会带来较大的开销。1.7 版本引进了开销较小的<span> </span></span>Xoshiro256 系列随机数生成器。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新的线程功能</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#212529">解决了运行时中的大量竞争条件，追踪了同步错误，改进了对多线程调度工作负载的支持，使默认的随机数生成器对线程更加友好，并添加了原子</span><span style="color:#2e3033">（</span><span style="color:#24292f">atomic</span><span style="color:#2e3033">）</span><span style="color:#212529">作为原始语言功能。</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现在为特定的字节大小定义了原子指针操作 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fissues%2F37847" target="_blank">#37847</a><span> </span>)。</li> 
 <li><span style="color:#2e3033">支持声明和使用可变结构的单个字段作为原子;查看新的@atomic宏</span><span> </span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fissues%2F37847" target="_blank">#37847</a><span> </span>)。</li> 
 <li>如果<span> </span><code>JULIA_NUM_THREADS</code><span> </span>环境变量设置为<code>auto</code>，则线程数将设置为 CPU 线程数 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fissues%2F38952" target="_blank">#38952</a><span> </span>)。</li> 
 <li>每个<span> </span><code>Task</code><span> </span>对象都有一个本地随机数生成器状态，默认情况下提供并行模拟代码的可重复执行（独立于调度）。默认生成器的并行速度也明显快于以前的版本 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fissues%2F40546" target="_blank">#40546</a><span> </span>)。</li> 
 <li>任务现在可以在重新调度时在线程之间迁移。（以前任务始终在最先执行它的线程上运行）(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fissues%2F40715" target="_blank">#40715</a><span> </span>)。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">包管理器</h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">自动安装包</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">如果注册表中有一个没有安装的包，那么当在 REPL 中尝试加载包时会自动安装。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">之前：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> using Foo
ERROR: ArgumentError: Package Foo not found in current path:
- Run `import Pkg; Pkg.add("Foo")` to install the Foo package.

Stacktrace:
 [1] require(into::Module, mod::Symbol)
   @ Base ./loading.jl:871

(@1.6) pkg> add Foo
...

julia> using Foo

julia> Foo
Foo</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在轻松安装</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> using Foo
 │ Package Foo not found, but a package named Foo is available from a registry.
 │ Install package?
 │   (@v1.7) pkg> add Foo
 └ (y/n) [y]: y
 ...
julia> Foo
Foo</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">默认情况下，软件包将安装到当前活动环境中，通过<span> </span><code>y</code><span> </span>或<span> </span><code>return</code><span> </span>键选择。要取消选择用<span> </span><code>n</code><span> </span>或<span> </span><code>Ctrl-c</code>。</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">新的清单格式</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">用户在 Julia 中添加包时，包管理器 (Pkg) 都会写出一个名为“清单（<span style="color:#212529">"manifest"</span>）”的 TOML 文件，里面包含该包所有依赖项的准确版本。但不同的包版本可能与不同的 Julia 版本兼容，因此，之前不建议将在一个 Julia 版本中创建的清单与另一个 Julia 版本一起使用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">1.7 版中更改了此清单格式，以便所有依赖项都放在一个公共<code>[deps]</code>密钥下，这释放了全局命名空间，以便<code>julia_version<span> </span></code>可以添加条目 。读取新清单的能力也将向后移植到 Julia 1.6，因此在 Julia 1.6.2 及更高版本中，Pkg 将保留现有清单的格式，只有新建的清单才会采用新的清单格式。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">推理改进</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本附带了许多类型推断改进。通过这些改进，Julia 1.7 将更“聪明地”推断程序类型，以提高性能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">1.7 可以传播在过程间（<em>inter-procedurally，</em>即跨任何函数调用）派生的类型约束<span> </span><code>isa<span> </span></code>和<span> </span><code>===</code><span> </span>条件<span style="color:#2e3033">某些 Julia 程序的编写方式是：行为会根据运行时类型而改变，而这种改进的推论性能使这些程序运行得更快。例如，现在在 x === nothing和 isnothing(x) 之间没有推断性差异：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> code_typed((Union&#123;Nothing,Int&#125;,); optimize=false) do x
           return isnothing(x) ? 0 : x
       end |> first</pre> 
<pre style="margin-left:0; margin-right:0; text-align:start">--- v1.6
+++ v1.7
@@ -1,6 +1,6 @@
 CodeInfo(
 1 ─ %1 = Main.isnothing(x)::Bool
 └──      goto #3 if not %1
 2 ─      return 0
-3 ─      return x
-) => Union&#123;Nothing, Int64&#125;
+3 ─      return x::Int64
+) => Int64</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#212529">这种过程间约束传播适用于任意泛型函数：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> ispositive(a) = isa(a, Number) && a > 0;
julia> code_typed((Union&#123;Nothing,Int&#125;,); optimize=false) do x
           return ispositive(x) ? x : 0
       end |> first</pre> 
<pre style="margin-left:0; margin-right:0; text-align:start">--- v1.6
+++ v1.7
@@ -1,6 +1,6 @@
 CodeInfo(
 1 ─ %1 = Main.ispositive(x)::Bool
 └──      goto #3 if not %1
-2 ─      return x
+2 ─      return x::Int64
 3 ─      return 0
-) => Union&#123;Nothing, Int64&#125;
+) => Int64</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">另一个显著变化是：Julia 1.7 可以用预先计算的常量替代更多的运行时计算，并通过在编译时解析条件分支来消除死代码。例如，在1.7中，特殊函数的计算可以在编译时完全折叠：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> code_typed((Int,)) do n
           n + sin(sum(sincos(42))) # no runtime computation of `sum(sincos(42))` in 1.7!
       end |> first</pre> 
<pre style="margin-left:0; margin-right:0; text-align:start">--- v1.6
+++ v1.7
@@ -1,32 +1,5 @@
 CodeInfo(
-1 ─ %1  = Base.muladd_float(0.16933292771007588, 2.7557313707070068e-6, -0.0001984126982985795)::Float64
-│   %2  = Base.muladd_float(0.16933292771007588, %1, 0.00833333333332249)::Float64
-│   %3  = Base.muladd_float(0.16933292771007588, 1.58969099521155e-10, -2.5050760253406863e-8)::Float64
-│   ... many runtime computations ...
-│   %27 = invoke Main.sin(%26::Float64)::Float64
-│   %28 = Base.sitofp(Float64, n)::Float64
-│   %29 = Base.add_float(%28, %27)::Float64
-└──       return %29
+1 ─ %1 = Base.sitofp(Float64, n)::Float64
+│   %2 = Base.add_float(%1, -0.9678422808766897)::Float64
+└──      return %2
 ) => Float64</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">以下是此版本的推理改进 PR 列表：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>过程间条件约束传播（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F38905" target="_blank">#38905</a>）</li> 
 <li>联合拆分调用站点的常量传播 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F39305" target="_blank">#39305</a><span> </span>)</li> 
 <li><code>invoke</code><span> </span>呼叫站点的持续传播(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F41383" target="_blank">#41383</a><span> </span>)</li> 
 <li>更多条件约束传播（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F39936" target="_blank">#39936</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Fpull%2F40832" target="_blank">#40832</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这些推理改进最初是由<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Faviatesk%2FJET.jl" target="_blank">JET.jl</a><span> </span>的需求推动的，JET.jl 是 Julia 的静态分析器，由 Julia 编译器的类型推理实现提供支持。1.7 中的这些推理改进使 JET 能够更准确、更快地分析程序。</p> 
<h2 style="color:#000000; margin-left:0px; margin-right:0px; text-align:start">多维数组改进</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#212529">多维数组，尤其是 3 维或更多维的数组，是科学编程和机器学习的有用结构。</span>在 Julia v1.7 中添加了相关语法：能够为多维数组编写文字。这种新语法使 Julia 中的多维数组比以前更容易操作</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">Julia v1.7:
[1 2 ; 3 4 ;;; 5 6 ; 7 8]
or
[1 ; 3 ;; 2 ; 4 ;;; 5 ; 7 ;; 6 ; 8]

Python with Numpy:
import numpy as np
np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

MATLAB:
A = [1 2; 3 4]
A(:,:,2) = [5 6; 7 8]

R:
array(c(1, 3, 2, 4, 5, 7, 6, 8), dim = c(2, 2, 2))</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#212529">该语法是当前语法的直接扩展：一个额外的分号 == 一个额外的维度：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> [1 2 ; 3 4]
2×2 Matrix&#123;Int64&#125;:
 1  2
 3  4

julia> [1 2 ;;; 3 4]
1×2×2 Array&#123;Int64, 3&#125;:
[:, :, 1] =
 1  2

[:, :, 2] =
 3  4

julia> [1 2 ;;;; 3 4]
1×2×1×2 Array&#123;Int64, 4&#125;:
[:, :, 1, 1] =
 1  2

[:, :, 1, 2] =
 3  4

julia> using BenchmarkTools

julia> @btime [1 2 ;;;; 3 4];
  44.838 ns (2 allocations: 160 bytes)

julia (v1.6)> @btime cat([1 2], [3 4], dims = 4); # clear, but slow, and gets worse with more dimensions
  1.380 μs (23 allocations: 1.05 KiB)

julia (v1.6)> @btime reshape([1; 2; 3; 4], (1, 2, 1, 2)); # fast, but intent less clear
  65.884 ns (2 allocations: 192 bytes)</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">对于多维数组基本操作有性能的显着改进，随着涉及更多维度，差异会大大提高。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">为了便于阅读较大的数组表达式，也可以接受换行符：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> [ 1 2
         3 4
         ;;;
         5 6
         7 8 ]
2×2×2 Array&#123;Int64, 3&#125;:
[:, :, 1] =
 1  2
 3  4

[:, :, 2] =
 5  6
 7  8</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此语法还可以按列优先顺序而不是行优先顺序编写数组，使用<code>;;</code>行代替空格：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">julia> [1 ; 2 ;; 3 ; 4 ;;; 5 ; 6 ;; 7 ; 8]
2×2×2 Array&#123;Int64, 3&#125;:
[:, :, 1] =
 1  3
 2  4

[:, :, 2] =
 5  7
 6  8
</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">1.7 版本是一个大版本更新，除了以上内容，此版本还包含一些语言功能和语法的改动，更多亮点更新可阅览<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjulialang.org%2Fblog%2F2021%2F11%2Fjulia-1.7-highlights%2F" target="_blank">官方公告</a>，完整修改列表可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJuliaLang%2Fjulia%2Freleases%2Ftag%2Fv1.7.0" target="_blank">在 GitHub 查看</a>。</p>
                                        </div>
                                      
</div>
            