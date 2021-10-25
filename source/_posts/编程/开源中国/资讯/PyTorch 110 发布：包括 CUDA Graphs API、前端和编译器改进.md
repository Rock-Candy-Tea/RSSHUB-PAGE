
---
title: 'PyTorch 1.10 发布：包括 CUDA Graphs API、前端和编译器改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-94eb020006369bb8d21b637fc8c23762e33.png'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 23:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-94eb020006369bb8d21b637fc8c23762e33.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">PyTorch 1.10 现已</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fblog%2Fpytorch-1.10-released%2F" target="_blank">发布</a><span style="background-color:#ffffff; color:#333333">，该版本包含了自 1.9 以来的 3400 多个 commit ，有 426 位贡献者参与更新。</span>PyTorch 1.10 更新侧重于改进 PyTorch 的训练和性能以及开发人员的可用性。完整的发行说明可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch%2Freleases%2Ftag%2Fv1.10.0" target="_blank">在此处获得</a>。<span style="background-color:#ffffff; color:#333333">主要亮点内容包括：</span></p> 
<ul> 
 <li>集成了 CUDA Graphs API 以减少 CUDA 工作负载的 CPU 开销。</li> 
 <li>FX、torch.special 和 nn.Module Parametrization 等几个前端 API 已从测试版变为稳定版。</li> 
 <li>除了 GPU 之外，JIT Compiler 中对自动融合的支持扩展到 CPU。</li> 
 <li>Android NNAPI 支持现已进入测试阶段。</li> 
</ul> 
<p>除了 PyTorch 1.10 外，PyTorch 团队还发布了针对 PyTorch 库的重大更新，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fblog%2Fpytorch-1.10-new-library-releases%2F" target="_blank">点此查看</a>关于库更新的详细消息。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">PyTorch 版本中的功能分为稳定版 (Stable)、测试版 (Beta) 和原型版 (Prototype)。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="86" src="https://oscimg.oschina.net/oscnet/up-94eb020006369bb8d21b637fc8c23762e33.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><span><span><span><span><span><span style="color:#262626"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>(Beta) CUDA Graphs API 集成</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:left"><span style="color:#000000">PyTorch 现在集成了 CUDA Graphs API 以减少 CUDA 工作负载的 CPU 开销。</span></p> 
<p style="text-align:left"><span style="color:#000000">CUDA Graphs 大大降低了 CPU 绑定 cuda 工作负载的 CPU 开销，从而通过提高 GPU 利用率来提高性能。对于分布式工作负载，CUDA Graphs 还可以减少 jitter，并且由于并行工作负载必须等待最慢的工作负载，因此减少 jitter 可以提高整体并行效率。</span></p> 
<p style="text-align:left"><span style="color:#000000">集成允许 cuda graphs 捕获的网络部分与由于 graph 限制而无法捕获的网络部分之间的无缝互操作。</span></p> 
<p style="text-align:left"><strong><span><span><span><span><span><span style="color:#262626"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>（Beta）CPU 融合</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:left"><span style="color:#000000"><span style="background-color:#ffffff">开发团队在 PyTorch 1.10 中为 CPU 添加了一个基于 LLVM 的 JIT compiler，可以将<code class="language-plaintext">torch</code>库调用序列融合在一起以提高性能。这是 PyTorch 团队第一次将编译引入 CPU。</span></span></p> 
<p style="text-align:left">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpytorch.org%2Fblog%2Fpytorch-1.10-released%2F" target="_blank">https://pytorch.org/blog/pytorch-1.10-released/</a></p>
                                        </div>
                                      
</div>
            