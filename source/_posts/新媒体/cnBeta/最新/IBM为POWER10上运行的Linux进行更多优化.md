
---
title: 'IBM为POWER10上运行的Linux进行更多优化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0425/31432d6384188d5.jpg'
author: cnBeta
comments: false
date: Sun, 25 Apr 2021 11:52:21 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0425/31432d6384188d5.jpg'
---

<div>   
随着IBM POWER10
Linux支持的所有基本要素的到位，最近几天，我们看到IBM工程师在POWER10性能优化方面的补丁增加了。<strong>本周最值得一提的是对sched/fair的wake_affine改进。在IBM发现
"POWER10的基准数据比预期的要少"之后，他们将部分原因追溯到Linux调度代码。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0425/31432d6384188d5.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0425/31432d6384188d5.jpg" title alt="1817324666582887240.jpg" referrerpolicy="no-referrer"></a></p><p>由于POWER10的二级缓存是在核心层面上的，所以为POWER10做了一些调度/公平性方面的调整，包括对空闲的CPU核心和缓存亲和性的偏好。这组补丁加上四月初的这个早期补丁系列已经有了进展。早期的系列补丁是为了确保正确发现二级缓存并将最后一级缓存（LLC）域设置为SMT调度域。</p><p>这些补丁的效果非常明显，像Java DayTrader基准测试的案例显示吞吐量提高了44%，合成调度基准测试也得到了有效提升的报告。但是这些补丁仍然需要进一步审查，而且还没有对现有的POWER9硬件进行测试，以确保对于旧体系没有退步。不过随着合并窗口的临近，这些补丁对于Linux 5.13来说已经太晚了，但也许今年晚些时候的5.14内核会完成上游合并。</p><p>最近几天和几周，整个Linux/开源生态系统也对POWER10有一些较小的补丁，比如Glibc为POWER10优化Strlen，它对字符串长度函数也有一些不错的改进。</p><p>IBM POWER10体系设备预计将在今年年底开始进入客户手中，因此预计在未来几个月会有更多的调整。</p>   
</div>
            