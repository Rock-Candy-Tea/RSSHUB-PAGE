
---
title: 'NumPy 1.22.1 发布，Python 科学计算包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6002'
author: 开源中国
comments: false
date: Sun, 16 Jan 2022 08:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6002'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">NumPy 1.22.0 现已发布，这是一个维护版本，其中包含了来自 14 位贡献者的 20 个 PR。</span>修复了在 1.22.0 版本之后发现的错误。一些值得注意的修复有：</p> 
<ul> 
 <li>修复 f2PY 文档字符串问题 (SciPy)</li> 
 <li>修复 <span style="background-color:#ffffff; color:#24292f">reduction </span>类型问题 (AstroPy)</li> 
 <li>修复各种 <span style="background-color:#ffffff; color:#24292f">typing bug</span>。</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本支持的 Python 版本为 3.8-3.10。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>共合并了 20 个拉取请求：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20702" target="_blank">#20702</a>：MAINT，DOC：1.22.0 发布后的修复。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20703" target="_blank">#20703</a>：DOC，BUG：使用 pngs 而不是 svgs。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20704" target="_blank">#20704</a>：DOC：修复了用户指南登陆页面上的链接</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20714" target="_blank">#20714</a>：BUG：恢复 vc141 支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20724" target="_blank">#20724</a>：BUG：修复多维参数的数组维度求解器...</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20725" target="_blank">#20725</a>：TYP：将<code>__array_namespace__</code>的类型注释更改为ModuleType</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20726" target="_blank">#20726</a>：TYP，MAINT：允许<code>ndindex</code>接受整数元组</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20757" target="_blank">#20757</a>：BUG：在减少中放松 dtype 身份检查</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20763" target="_blank">#20763</a>：TYP：允许时间操作函数接受<code>date</code>和<code>timedelta</code>......</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20768" target="_blank">#20768</a>：TYP：放松<code>ndarray.__array_finalize__</code>类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20795" target="_blank">#20795</a>：MAINT：如果 setuptools 版本太新，会引发 RuntimeError。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20796" target="_blank">#20796</a>：BUG，DOC：修复 SciPy docs 构建警告</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20797" target="_blank">#20797</a>：DOC：在发行说明中修复 OpenBLAS 版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Fpull%2F20798" target="_blank">#20798</a>：PERF：优化数组检查有界 0,1 值</li> 
 <li>......</li> 
</ul> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#24292f">详情可查看更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Freleases%2Ftag%2Fv1.22.1" target="_blank">https://github.com/numpy/numpy/releases/tag/v1.22.1</a></p>
                                        </div>
                                      
</div>
            