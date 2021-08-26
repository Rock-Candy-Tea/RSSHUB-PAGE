
---
title: 'AMD霄龙Milan-X服务器CPU曝光：最高64核 集成3D V-Cache缓存'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2020/1214/a7919947b78879a.jpg'
author: cnBeta
comments: false
date: Thu, 26 Aug 2021 06:53:05 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2020/1214/a7919947b78879a.jpg'
---

<div>   
<strong>@Momomo_US 刚刚在 Twitter 上分享了采用 3D Chiplet 封装的下一代 AMD Zen 3 霄龙（EPYC）Milan-X CPU 的一些信息。</strong>按照该公司的计划，3D V-Cache 芯片堆叠技术将率先在下一代锐龙台式 CPU 产品线上引入，同时 EPYC Milan-X 也将作为 2022 ~ 2023 年间推出的 Zen 4 EPYC Genoa 产品线的过渡产品。<br>
 <p><img src="https://static.cnbetacdn.com/article/2020/1214/a7919947b78879a.jpg" referrerpolicy="no-referrer"></p><p>据悉，Milan-X 与现有的 Milan EPYC 7003 CPU 类似，只是用上了更先进的小芯片堆叠工艺。</p><p>在一连串推文中，@Momomo_US 提到了以下几款 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> EPYC 7003 Milan-X CPU SKU：</p><blockquote><p>● EPYC 7773X -- 64 核 / 128 线程（100-000000504）</p><p>● EPYC 7573X -- 32 核 / 64 线程（100-000000506）</p><p>● EPYC 7473X -- 24 核 / 48 线程（100-000000507）</p><p>● EPYC 7373X -- 16 核 32 线程（100-000000508）</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0826/2aecc4a5cf99d79.png" referrerpolicy="no-referrer"></p><p>这里提到的四款 EPYC Milan-X CPU SKU，都保留了与当前对应版本相同的核心数量，因而我们不大可能看到 CCD 堆叠方式的变化。</p><p>不过小芯片设计的引入，还是能够为 Milan-X 添加额外的 SRAM 缓存，从而带来近似于架构迭代的整体性能提升。</p><p><img src="https://static.cnbetacdn.com/article/2021/0826/43c65ef70767def.png" referrerpolicy="no-referrer"></p><p>早些时候，AMD 已经详细介绍过 3D V-Cache 的技术理念，可知其使用了键距 9 微米的 3D 微凸（Micro Bump）、硅通孔（TSV）互连方案、亲水介电与 Direct CU-CU 键合等方案，来实现小芯片的堆叠。</p><p>单个 3D V-Cache 堆栈包含了 64MB L3 缓存，位于现有的 Zen 3 CCD 已具备的 TSV 之上。通过增加现有的 32MB L3 缓存，单个 CCD 模块将总计拥有 96MB 的缓存。</p><p><img src="https://static.cnbetacdn.com/article/2021/0826/e32704a06f9b752.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（截图 via <a href="https://wccftech.com/amd-epyc-milan-x-server-cpus-leak-out-up-to-64-zen-3-cores-possibly-3d-v-cache-stacks/" target="_self">WCCFTech</a>）</p><p>此外 AMD 声称 V-Cache 堆栈可达到 8-hi，意味着除了每个 CCD 的 32MB 缓存，加上 8 组 3D V-Cache CCD 堆栈的 512MB 缓存，Milan-X 理论上可堆砌高达 768MB 的缓存。</p><p>最后，随着 7nm 工艺的不断成熟，EPYC Milan-X 服务器处理器将迎来更快的时钟频率。而新曝光的 OPN 代码，意味着 AMD 或已做好在 2022 年末推出 Milan-X 系列 3D V-Cache 芯片的准备。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1169545.htm" target="_blank">AMD向多层小芯片设计转进 Zen 3处理器将试水3D堆叠V-Cache技术</a></p></div>   
</div>
            