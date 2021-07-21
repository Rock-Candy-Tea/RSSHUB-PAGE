
---
title: 'NumPy 1.21.1 发布，Python 科学计算包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6751'
author: 开源中国
comments: false
date: Wed, 21 Jul 2021 06:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6751'
---

<div>   
<div class="content">
                                                                    
                                                        <p>NumPy 1.21.1 现已发布，这是一个维护版本，修复了 1.21.0 版本之后发现的错误，并将 OpenBLAS 更新到 v0.3.17 以处理 arm64 上的问题。此版本支持的 Python 版本为 3.7-3.9。1.21.x 系列与开发中的 Python 3.10 兼容。Python 3.10 将在发布后得到官方支持。</p> 
<p>使用 gcc-11.1 编译 NumPy 1.20.0 时尚存在一些未解决的问题：</p> 
<ul> 
 <li>在运行测试时，Optimization level -O3 会导致许多不正确的警告。</li> 
 <li>在某些硬件上，NumPY 将陷入无限循环。</li> 
</ul> 
<p>此版本共合并了 26 个拉取请求：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19311" target="_blank">#19311</a>：REV,BUG：替换<code>NotImplemented</code>为<code>typing.Any</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19324" target="_blank">#19324</a>：MAINT：修复了<code>ndarray.real</code>和<code>imag</code>的返回数据类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19342" target="_blank">#19342</a>：DOC：修复一些导致 pdf 生成崩溃的文档字符串。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19348" target="_blank">#19348</a>：ENH：添加<code>numpy.f2py.get_include</code>函数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19366" target="_blank">#19366</a>：MAINT：删除 distutils 模板处理中的<code>print()</code>'s</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19430" target="_blank">#19430</a>：MAINT：使用 arm64-graviton2 在 travis 上进行测试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19495" target="_blank">#19495</a>：BUILD：将 OpenBLAS 更新到 v0.3.17</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19496" target="_blank">#19496</a>：MAINT：避免在 division SIMD 代码注释中使用 unicode 字符</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19499" target="_blank">#19499</a>：BUG, SIMD：修复 GCC-11 上计数非零时的无限循环</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19500" target="_blank">#19500</a>：BUG：修复 npyiter_multi_index_set 中的 numpy.npiter 泄漏</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F19501" target="_blank">#19501</a>：TST：修复python 3.9.0 中的<code>GenericAlias</code>测试故障</li> 
 <li>......</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Freleases%2Ftag%2Fv1.21.1" target="_blank">https://github.com/numpy/numpy/releases/tag/v1.21.1</a></p>
                                        </div>
                                      
</div>
            