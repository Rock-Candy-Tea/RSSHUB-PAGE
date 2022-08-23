
---
title: '英特尔将Meteor Lake逻辑块_拼图_中的大部分交给了台积电代工'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0823/556f3363eb75c49.png'
author: cnBeta
comments: false
date: Tue, 23 Aug 2022 04:31:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0823/556f3363eb75c49.png'
---

<div>   
英特尔计划量产的下一代 Meteor Lake 处理器，将首次体现该公司的 IDM 2.0 制造战略 —— <strong>构建具有多个逻辑块的处理器，并借助 Foveros 先进封装工艺和一个基础块（本质上算是一个中介层）互连。</strong>芯片中的每一块“瓦片”（Tile），都可选用其最适合的制程工艺，以兼顾性能功能和制造成本。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0823/556f3363eb75c49.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0823/556f3363eb75c49.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>举个例子，尽管 iGPU 与 SIMD 组件需要在更先进的低功耗节点上制造，但配套的显示控制器和媒体引擎等组件可以降级采用相对更成熟的次一级制程。</p><p>与此同时，日本科技媒体 <a href="https://pc.watch.impress.co.jp/docs/news/1433845.html" target="_self">PC Watch</a> 在英特尔 Hot Chips 34 预热活动后指出，“Meteor Lake”的片上系统（SoC）中，绝大多数逻辑裸片都是交由台积电代工的。</p><p><img src="https://static.cnbetacdn.com/article/2022/0823/300aaf590d072d0.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>首先，Meteor Lake 的 MCM 多芯片，是由 CPU、图形、SoC 和 I/O 这四个逻辑块组成的。</p><blockquote><p>它们位于同一个基于 22nm HKMG 工艺节点制造的“基础块”（Base Tile）上，有助于极端致密的逻辑块微观布线。</p><p>这一块未引入任何逻辑组件，仅用于各块之间的互连。</p></blockquote><p>相比之下，CPU 块采用了该公司最为先进的 Intel 4（7nm EUV）工艺节点。</p><blockquote><p>英特尔宣称 Intel 4 工艺可媲美台积电 N5 甚至更好，但更大的理由是希望将最主要的 CPU 内核部分的制造业务掌握在自家晶圆厂手上。</p><p>据悉，CPU 块包含了 CPU 内核、末级缓存、以及 Foveros 界面。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0823/7ad2f560684f1d2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0823/7ad2f560684f1d2.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>其次是第二重要的图形块，其包含了一个基于 Xe-LPG 图形架构的核显。</p><blockquote><p>作为 Xe-LP 的迭代版本，LPG 具备了实时光追功能，但英特尔为它选择了台积电 N5（5nm EUV）制程工艺。</p><p>当然并非所有 iGPU 组件都被放在了该图块上，比如显示引擎就可以放置于 I/O 块上。</p></blockquote><p>至于占更大面积的 SoC 块，其采用了台积电 N6（6nm）工艺节点，包含了内存控制器、PCIe root-complex、各种封装设备的控制器、以及 SerDes 串行-解串器。</p><p>最后，I/O 块的占地面积最小，因为它本质上是 SoC die 的扩展。其采用了台积电 N6 工艺节点，辅以各种 I/O 的物理层（PHY）组件。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1307543.htm" target="_blank">Hot Chip 34：英特尔分享Meteor/Arrow/Lunar Lake芯片设计</a></p></div>   
</div>
            