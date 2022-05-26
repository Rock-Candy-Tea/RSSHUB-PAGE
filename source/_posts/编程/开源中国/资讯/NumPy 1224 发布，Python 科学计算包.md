
---
title: 'NumPy 1.22.4 发布，Python 科学计算包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=154'
author: 开源中国
comments: false
date: Thu, 26 May 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=154'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">NumPy 1.22.4 现已发布，这是一个维护版本，</span>修复了在 1.22.3 版本之后发现的错误。此外，此版本的 <span style="background-color:#ffffff; color:#24292f">wheels </span>是使用最近发布的 Cython 0.29.30 构建的，它应该可以修复报告的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fissues%2F21008" target="_blank">调试</a>问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#24292f">此版本支持的 Python 版本为 3.8-3.10。</span>Mac <span style="background-color:#ffffff; color:#24292f">wheels </span>现在基于 OS X 10.15，而不是以前 NumPy 发布周期中使用的 10.6。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">此版本共合并了 22 个拉取请求</span>：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21192" target="_blank">#21192</a>：TST：将 mypy 从 0.931 升级到 0.940</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21243" target="_blank">#21243</a>：MAINT：明确地重新导出 numpy._typing 中的类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21245" target="_blank">#21245</a>：MAINT：为 CI doc 构建指定 sphinx、numpydoc 版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21275" target="_blank">#21275</a>：BUG：修复错别字</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21277" target="_blank">#21277</a>：ENH，BLD：修复 wasm 的数学特征检测</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21350" target="_blank">#21350</a>：MAINT：修复失败的 simd 和 cygwin 测试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21438" target="_blank">#21438</a>：MAINT：修复失败的 Python 3.8 32 位 Windows 测试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21445" target="_blank">#21445</a>：BUG：允许旧 dtypes 再次转换为 datetime</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21446" target="_blank">#21446</a>：BUG：在 frombuffer 中使 mmap 处理更安全</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21447" target="_blank">#21447</a>：BUG：停止使用 Python 3.11 中已弃用的 PyBytesObject.ob_shash</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21448" target="_blank">#21448</a>：ENH：引入 numpy.core.setup_common.NPY_CXX_FLAGS</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21472" target="_blank">#21472</a>：BUG：确保正确引发编译错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21473" target="_blank">#21473</a>：BUG：修复分段错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21474" target="_blank">#21474</a>：MAINT：更新文档要求</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21475" target="_blank">#21475</a>：MAINT：在 clang 上用 no_sanitize("alignment") 标记 npy_memchr</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21512" target="_blank">#21512</a> : DOC：Proposal - 使文档登陆页面卡片更相似......</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21525" target="_blank">#21525</a>：MAINT：将 Cython 版本更新为 0.29.30</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21536" target="_blank">#21536</a>：BUG：修复构建配置期间的 GCC 错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21541" target="_blank">#21541</a>：REL：为 NumPy 1.22.4 版本做准备</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F21547" target="_blank">#21547</a>：MAINT：跳过在 PyPy 上失败的测试</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Freleases%2Ftag%2Fv1.22.4" target="_blank">https://github.com/numpy/numpy/releases/tag/v1.22.4</a></p>
                                        </div>
                                      
</div>
            