
---
title: 'AMD Zen 3小芯片使用了环形总线 但未来核心增长或依赖网状拓补'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0908/46f65a2fdd19f1a.jpg'
author: cnBeta
comments: false
date: Wed, 08 Sep 2021 08:49:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0908/46f65a2fdd19f1a.jpg'
---

<div>   
AMD 在采用 Zen 架构的锐龙 / 霄龙 CPU 上使用了独特的 Compute Complex Die 设计（简称 CCD），但受带宽密集型组件的互连方式的影响，其内核数量的增长也可能存在限制。<strong>然而 AnandTech 援引某位研究人员的话称，这可能只是 AMD 在 CCD 交换结构上提供的第一层见解，因为背后还有环形总线的身影。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0908/46f65a2fdd19f1a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0908/46f65a2fdd19f1a.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>更确切的说，Zen 3 CCD 使用了双向环形总线，以将 8 个 CPU 内核与 32 MB 共享 L3 缓存和其它关键组件连接起来，比如用于 CCD 模组间通信的 IFOP 接口芯片（IOD）。</p><blockquote><p>如果将 Zen 3 CPU 想象成一座城市，信号沿着公交车在城市街区周围行驶，并于四栋建筑物之间接送人员。</p><p>此时总线就扮演者红绿灯的角色，建筑物为核心组件，而公交车站就是环形总线的停靠站。</p><p>在需要让环形总线屏蔽掉某个坏块的时候，SKU 设计人员只需将它设置得无法访问。</p></blockquote><p>双向环形则意味着公交车在城市街道上沿着两个不同的方向行驶，但环形总线拓补也不是没有短板。</p><p>比如由于过多的 ring-stop 停靠极大地增加了延迟，导致 Ring Bus 的规模也会碰到上限，这也是同轴环形拓补在网络中逐渐消失的一个主要原因。</p><p><a href="https://static.cnbetacdn.com/article/2021/0908/c5e58a6073976a3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0908/c5e58a6073976a3.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>有趣的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>早在 2010 年代初期就意识到，其无法将单个 CPU 上的内核数量，扩展到环形总线承载能力的某个顶点，于是引入了创新的网状拓补设计。</p><p>据悉，Mesh 是一种更加先进的环形总线，但在组件之间具有额外的连接点，介于环形总线和完全互连之间 —— 其中每个组件直接相互连接，但在大规模部署的时候，它又显得不切实际。</p><blockquote><p>于是在 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 的旗舰 CPU 上，比如 64 核的 EPYC SKU，该公司就选用了让 8 个 CCD 模块通过 sIOD 连接到一起的方案、且每个 CCD 内部都有一个双向环形总线。</p><p>不过在采用 4 个 CCX（CPU Complex）设计的上一代 Zen 2 小芯片方案中，AMD 并未采用环形总线，而是让它们完全互连（但每组 CCX 的 L3 缓存并不共享），我们可从演示文稿中知晓更多细节。</p></blockquote><p>权衡利弊之后，AMD 最终为 Zen 3 产品线使用了性能更具优势的 CCX 方案（单个 CCX 可拥有 8 个核心）。</p><p>最后，<a href="https://www.anandtech.com/show/16930/does-an-amd-chiplet-have-a-core-count-limit" target="_self">AnandTech</a> 推测 AMD 或在将来放弃环形总线，以进一步释放 CCD / CPU 内核数量的潜力 —— 这样又与英特尔在高核心数量 CPU SKU 上放弃 Ring Bus 殊途同归了。</p><p>猜测未来的 CCD 将由三个不同的裸片堆叠而成，顶部为缓存、中间为 CPU 核心、底下则是网状互连裸片。</p><p>再接下去，合乎逻辑的操作就是将这个互连层扩展到一个硅中介层，并在上面堆叠几个 CPU + 缓存芯片。</p>   
</div>
            