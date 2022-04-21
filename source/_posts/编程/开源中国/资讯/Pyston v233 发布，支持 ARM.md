
---
title: 'Pyston v2.3.3 发布，支持 ARM'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2020/1103/181239_UVR7_2720166.png'
author: 开源中国
comments: false
date: Thu, 21 Apr 2022 07:14:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2020/1103/181239_UVR7_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Pyston 是 Python 的高度兼容实现，自称比 Python 更快。最新发布的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.pyston.org%2F2022%2F04%2F" target="_blank">Pyston v2.3.3 </a>提供了对 64 位 ARM 的支持，因此 Pyston 现可运行于 ARM 服务器、Docker 上的 M1 Mac、搭载 64 位操作系统的树莓派以及其他 64 位 ARM 系统之上。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpyston%2Fpyston%2Freleases%2Ftag%2Fpyston_2.3.3" target="_blank">https://github.com/pyston/pyston/releases/tag/pyston_2.3.3</a></p> 
<blockquote> 
 <p>如果你使用的是 Intel 或 AMD x86_64 CPU，请下载“amd64”包；如果使用的是 aarch64 ARM CPU（Raspberry Pi 4、AWS Graviton、Apple Silicon M1），请下载“arm64”包。请注意，对于这些架构，均需要运行 64 位操作系统。</p> 
</blockquote> 
<p>根据开发团队的介绍，他们在 ARM 上实现的速度提升（在 Graviton EC2 实例上测得的提升情况为 30%）与在 x86 上的速度提升（在英特尔 i7-6700 上为 34%）相当。因为预热时间很短，所以即使是低功率的处理器，如树莓派，也会从 Pyston 中受益。这些数字来自于他们的宏基准测试套件，因此这些速度提升有望成为用户在实践中实现的目标。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Pyston v2 重点对网络服务工作负载进行了优化，在许多工作负载上提供了显著加速。其开发团队整理了一个新的公共 Python 宏基准测试套件，用于测试多个常用的 Python 项目性能表现。Pyston v2 在微基准测试上也显示了其加速性能，在诸如 chaos.py 和 nbody.py 之类的测试中，其速度是标准 Python 的两倍。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下图的测试结果显示了性能测试结果，在目标基准 (djangocms + flaskblogging) 中，Pyston v2 实现了平均延迟 1.22x 加速、p99 延迟 1.18x 加速，并且每个进程使用的内存仅多使用了几 MB。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2020/1103/181239_UVR7_2720166.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开发团队简单介绍了 Pyston v2 使用的一些技术：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fluajit.org%2Fdynasm.html" target="_blank">DynASM</a> 的低开销 JIT</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue14757" target="_blank">Quickening</a></li> 
 <li>常规 CPython 优化</li> 
 <li>改进构建过程</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">兼容性方面，由于 Pyston 是 CPython 的分支，开发团队表示它是当今可用的最兼容的 Python 实现替代方案之一，Pyston 支持 CPython 的所有功能和 C API。</p>
                                        </div>
                                      
</div>
            