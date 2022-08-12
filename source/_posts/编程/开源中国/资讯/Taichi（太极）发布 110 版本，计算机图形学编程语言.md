
---
title: 'Taichi（太极）发布 1.1.0 版本，计算机图形学编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
author: 开源中国
comments: false
date: Fri, 12 Aug 2022 07:03:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Taichi（太极）v1.1.0 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="287" src="https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif" width="512" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<h2><strong>新的功能</strong></h2> 
<h3><strong>量化数据类型</strong></h3> 
<p>高分辨率模拟可以提供出色的视觉质量，但通常受到板载 GPU 内存容量的限制。此版本添加了量化数据类型，允许定义自己的整数、定点数或任意位数的浮点数，在硬件限制和模拟效果之间取得平衡。</p> 
<p>有关该特性的全面介绍，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taichi-lang.org%2Fdocs%2Fmaster%2Fquant" target="_blank">使用量化数据类型。</a></p> 
<h3><strong>离线缓存</strong></h3> 
<p>Taichi 内核在第一次被调用时被隐式编译。编译结果保存在<strong><em>在线内存缓存</em></strong>中，以减少后续函数调用的开销。只要内核功能不变，就可以直接加载启动。</p> 
<p>但是当程序终止时，缓存不再可用。 如果再次运行该程序，Taichi 必须重新编译所有内核函数并<em><strong>重建在线内存缓存</strong></em>。由于编译开销，Taichi 函数的第一次启动总是很慢。</p> 
<p>为了解决这个问题，这个版本增加了<em>离线</em>缓存功能，它将编译缓存转储到磁盘以供将来运行。在随后的运行中，第一次启动的开销可以大大减少。</p> 
<p>Taichi 现在默认构建并维护一个离线缓存。</p> 
<h3>正向模式自动微分</h3> 
<p>通过 ti.ad.FwdMode 添加正向模式自动微分。</p> 
<p>与现有的计算向量雅可比积 (vJp) 的反向模式自动微分不同，正向模式在评估导数时计算雅可比向量积 (Jvp)。 因此，在函数的输出数量大于其输入的情况下，正向模式自动微分效率更高。</p> 
<p>该<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fblob%2Fmaster%2Fpython%2Ftaichi%2Fexamples%2Fautodiff%2Fjacobian.py" target="_blank">例子</a>演示了正向模式和反向模式下的雅可比矩阵计算。</p> 
<h3>SharedArray（实验性）</h3> 
<p>GPU 的共享内存是在每个线程块（或 Vulkan 中的工作组）中可见的快速小型内存，广泛用于性能优先的场景。</p> 
<p>为了访问 GPU 的共享内存，此版本在命名空间 ti.simt.block 下添加了 SharedArray API。下图说明了 Taichi 的 SharedArray 的性能优势。 使用 SharedArray，Taichi Lang 可以媲美甚至优于等效的 CUDA 代码。</p> 
<p><img alt height="450" src="https://oscimg.oschina.net/oscnet/up-ebf8465db5ef6bede41e5b46f8d417bf60f.png" width="600" referrerpolicy="no-referrer"></p> 
<h3>纹理（实验性）</h3> 
<p>Taichi 现在支持 Vulkan 和 OpenGL 后端的纹理双线性采样和原始纹理提取。此功能利用硬件纹理单元，并减少了在图像处理任务中手动组合双线性插值代码的需要。</p> 
<p>此功能还为光栅化或光线跟踪等任务中的纹理映射提供了一种简单的方法。在 Vulkan 后端，Taichi 还支持图像加载和存储。可以直接操作图像的纹素，并在随后的纹理映射中使用该图像。</p> 
<p>当前的纹理和图像 API 处于早期阶段，可能会发生变化。未来计划支持无绑定纹理以，扩展到光线追踪等任务。还计划将完整的纹理支持扩展到支持纹理 API 的所有后端。</p> 
<p> </p> 
<p>其他一般改进和修复可查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv1.1.0" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v1.1.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            