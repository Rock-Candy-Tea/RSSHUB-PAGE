
---
title: 'TaiChi v0.9.0 发布，引入矩阵动态索引和更稳定的 API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8294'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8294'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Taichi（太极）0.9.0 已经发布，这是专为高性能计算机图形学设计的编程语言。该版本引进了</span>矩阵的动态索引（实验功能）、改善了当前 API 集的稳定性...</p> 
<h2>新特性</h2> 
<h3>1、矩阵的动态索引（实验功能）</h3> 
<p>之前版本的矩阵只能通过常量索引访问，导致有些操作无法执行。比如无法将<span style="background-color:#ffffff; color:#2e3033">向量中的最小元素钳制（</span><span style="background-color:#ffffff; color:#121212">clamp 运算</span><span style="background-color:#ffffff; color:#2e3033">）到 0 ：</span></p> 
<pre><code>@ti.kernel
def clamp():
    ...  # assume we have a n-d vector A
    min_index = 0
    for i in range(n):
        if A[i] < A[min_index]:
            min_index = i
    A[min_index] = 0</code></pre> 
<p>当然也可以利用循环展开，但这样写既不直观也不高效：</p> 
<pre><code>@ti.kernel
def clamp():
    ...  # assume we have a n-d vector A
    min_index = 0
    for i in ti.static(range(n)):
        if A[i] < A[min_index]:
            min_index = i
    for i in ti.static(range(n)):
        if i == min_index:
            A[i] = 0</code></pre> 
<p><span style="background-color:#ffffff; color:#2e3033">有了这个矩阵动态索引的新特性，现在就可以平稳地运行第一段代码。此外，</span>v0.9.0 版本添加了一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fblob%2Fmaster%2Fpython%2Ftaichi%2Fexamples%2Fsimulation%2Fimplicit_fem.py" target="_blank">新的隐式 FEM</a>（有限元方法）示例（），在这个例子中，为隐式时间积分构造了一个巨大的 (12 × 12) Hessian 矩阵。如果没有动态索引，整个矩阵构造循环需要展开，编译需要70秒；使用动态索引，可以应用传统的循环版本，编译时间缩短到2.5秒。</p> 
<p><span style="background-color:#ffffff; color:#2e3033">该</span>矩阵动态索引<span style="background-color:#ffffff; color:#2e3033">特性可以通过设置 <strong>ti.init(dynamic_index=True)</strong> 来启用。</span></p> 
<h3>2、macOS 上的 Vulkan 后端</h3> 
<p>在 macOS 10.15+ 上添加对 <strong>ti.vulkan</strong> 后端的支持，现在可以在 MacBook 上运行 GGUI，运行以下 GGUI 示例：</p> 
<pre><code># prerequisites: taichi >= v0.9.0 and macOS >= 10.15
# run GGUI examples
ti example fractal3d_ggui 
ti example fem128_ggui</code></pre> 
<h3>3、与 <span style="background-color:#ffffff; color:#24292f">Google Colab</span> 的兼容性</h3> 
<p><span style="background-color:#ffffff; color:#24292f">0.9.0 版本重构了编译器实现，使 Taichi 与 Google Colab 兼容。（如果在 Google Colab 笔记本环境中运行早期版本的 Taichi ，系统会崩溃 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fissues%2F235" target="_blank">#235</a><span style="background-color:#ffffff; color:#24292f">）</span></p> 
<p>在 <span style="background-color:#ffffff; color:#24292f">Google Colab</span> 中运行<code>!pip install taichi</code>以安装 Taichi 。</p> 
<h2>功能改进</h2> 
<h3>1.、更稳定、更完善的 API</h3> 
<p>0.9.0 版本重新组织包结构，并弃用一些过时或内部 API ：</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"> 
 <tbody> 
  <tr> 
   <th style="text-align:center"><strong>种类</strong></th> 
   <th style="text-align:center"><strong>已弃用的 API</strong></th> 
   <th style="text-align:center"><strong>替代品</strong></th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Builtin</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>max()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.max()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Builtin</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>min()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.min()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Atomic operation</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>obj.atomic_add()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.atomic_add()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Image-specific</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.imread()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.tools.imread()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Image-specific</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.imwrite()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.tools.imwrite()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Image-specific</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.imshow()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.tools.imshow()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Profiler-specific</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.print_profile_info()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.profiler.print_scoped_profiler_info()</code></td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px"><strong>Profiler-specific</strong></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.print_kernel_profile_info()</code></td> 
   <td style="border-style:solid; border-width:1px"><code>ti.profiler.print_kernel_profiler_info()</code></td> 
  </tr> 
 </tbody> 
</table> 
<p>完整的 API 更改列表请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1FMECCsPMVDjzFN9p3Xy2e4CaA-ru9-lIHb1if-7zgLY%2Fedit%23gid%3D0" target="_blank">此 Google 文档</a> 。</p> 
<h3>2、错误报告更简洁</h3> 
<p>该版本改善了错误报告的展示，在错误报告中删除了与开发人员无关的琐碎回溯，以改善调试体验。以下面这段代码为例：</p> 
<pre><code>import taichi as ti

ti.init()

@ti.func
def bar(a):
    a = a + 2j

@ti.kernel
def foo():
    bar(1)

foo()</code></pre> 
<p>0.9.0 版本之前，这段代码的错误报告如下：</p> 
<pre><code>[Taichi] Starting on arch=x64
Traceback (most recent call last):
  File "error.py", line 13, in 
    foo()
  File "/path_to_taichi/lang/kernel_impl.py", line 709, in wrapped
    return primal(*args, **kwargs)
  File "/path_to_taichi/lang/kernel_impl.py", line 636, in __call__
    key = self.ensure_compiled(*args)
  File "/path_to_taichi/lang/kernel_impl.py", line 627, in ensure_compiled
    self.materialize(key=key, args=args, arg_features=arg_features)
  File "/path_to_taichi/lang/kernel_impl.py", line 493, in materialize
    taichi_kernel = _ti_core.create_kernel(taichi_ast_generator,
  File "/path_to_taichi/lang/kernel_impl.py", line 488, in taichi_ast_generator
    compiled()
  File "error.py", line 11, in foo
    bar(1)
  File "/path_to_taichi/lang/kernel_impl.py", line 76, in decorated
    return fun.__call__(*args)
  File "/path_to_taichi/lang/kernel_impl.py", line 156, in __call__
    ret = self.compiled(*args)
  File "error.py", line 7, in bar
    a = a + 2j
  File "/path_to_taichi/lang/common_ops.py", line 16, in __add__
    return ti.add(self, other)
  File "/path_to_taichi/lang/ops.py", line 78, in wrapped
    return imp_foo(a, b)
  File "/path_to_taichi/lang/ops.py", line 63, in imp_foo
    return foo(x, y)
  File "/path_to_taichi/lang/ops.py", line 427, in add
    return _binary_operation(_ti_core.expr_add, _bt_ops_mod.add, a, b)
  File "/path_to_taichi/lang/ops.py", line 173, in _binary_operation
    a, b = wrap_if_not_expr(a), wrap_if_not_expr(b)
  File "/path_to_taichi/lang/ops.py", line 36, in wrap_if_not_expr
    return Expr(a) if not is_taichi_expr(a) else a
  File "/path_to_taichi/lang/expr.py", line 33, in __init__
    self.ptr = impl.make_constant_expr(arg).ptr
  File "/path_to_taichi/lang/util.py", line 196, in wrapped
    return func(*args, **kwargs)
  File "/path_to_taichi/lang/impl.py", line 414, in make_constant_expr
    raise ValueError(f'Invalid constant scalar expression: &#123;type(val)&#125;')
ValueError: Invalid constant scalar expression: </code></pre> 
<p>在 0.9.0 版本中，其错误报告如下：</p> 
<pre><code>Traceback (most recent call last):
  File "/path_to_test/error.py", line 13, in 
    foo()
  File "/path_to_taichi/lang/kernel_impl.py", line 732, in wrapped
    raise type(e)('\\n' + str(e)) from None
taichi.lang.exception.TaichiTypeError: 
On line 11 of file "/path_to_test/error.py", in foo:
    bar(1)
    ^^^^^^
On line 7 of file "/path_to_test/error.py", in bar:
    a = a + 2j
        ^^^^^^
Invalid constant scalar data type: </code></pre> 
<h3>3、官网文档页改版</h3> 
<p>为了提高文档的可读性和用户友好性，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taichi.graphics%2F" target="_blank">Taichi 的文档站点</a>已重构，并将 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taichi.graphics%2Fapi%2F" target="_blank">API 参考</a>纳入其中。</p> 
<p>除上述版本高光内容外，该版本还包含大量其他更新项，包含新的测试、修复、重构等，详情可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.9.0" target="_blank">发布公告</a>中阅览。</p>
                                        </div>
                                      
</div>
            