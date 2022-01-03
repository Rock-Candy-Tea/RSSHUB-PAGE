
---
title: 'NumPy 1.22.0 发布，Python 科学计算包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8426'
author: 开源中国
comments: false
date: Mon, 03 Jan 2022 08:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8426'
---

<div>   
<div class="content">
                                                                                            <p>NumPy 1.22.0 现已发布，这是一个大型版本，其中包含了来自 153 位贡献者的 609 个 PR。有很多改进之处，主要亮点在于：</p> 
<ul> 
 <li>主命名空间的注解基本完成。上游是一个不断变化的目标，因此可能会有进一步的改进，但主要工作已经完成。这可能是此版本中用户最明显的增强功能。</li> 
 <li>提供了提议的 Array-API 的初步版本。这是创建可跨应用程序（如 CuPy 和 JAX）使用的标准函数集合的一步。</li> 
 <li>NumPy 现在有一个 DLPack 后端。DLPack 为数组（张量）数据提供了一种通用的交换格式。</li> 
 <li><code>quantile</code>、<code>percentile</code>和相关函数的新方法。该新方法提供了一套完整的常见方法的文献。</li> 
 <li>供下游项目使用的新的可配置分配器。</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这些是对为常用 functions 提供 SIMD 支持、对 F2PY 的改进和更好的文档的持续工作的补充。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>官方指出，此版本支持的 Python 版本为 3.8-3.10，Python 3.7 已被删除。值得注意的是，仅在 Windows 上为 Python 3.8 和 3.9 提供 32 bit wheels，其他所有的都是 64 位，因为 Ubuntu、Fedora 和其他 Linux 发行版放弃了 32 位支持。所有的 64 bit wheels 也与 64 bit integer OpenBLAS 相关联，这应该可以解决使用 truly huge arrays 偶尔遇到的问题。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy%2Freleases%2Ftag%2Fv1.22.0" target="_blank">查看更新说明</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            