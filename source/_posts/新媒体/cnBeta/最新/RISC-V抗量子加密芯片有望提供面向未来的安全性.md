
---
title: 'RISC-V抗量子加密芯片有望提供面向未来的安全性'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0824/6d08824a0cd63e0.jpg'
author: cnBeta
comments: false
date: Tue, 24 Aug 2021 01:29:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0824/6d08824a0cd63e0.jpg'
---

<div>   
为了抵御未来使用量子计算机可完成的强大攻击，许多研究人员都在潜心开发新型加密技术。通常情况下，这些应对措施需要耗费巨大的处理能力。<strong>不过德国的科学家们，已经开发出了一种能够非常高效地实施此类技术的微芯片，有助于推动“后量子密码学”时代走向现实。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0824/6d08824a0cd63e0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0824/6d08824a0cd63e0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：TUM / Astrid Eckert）</p><p>据悉，现代密码学的大部分内容，都依赖于经典计算机在处理大量数字等数学问题时所面临的极端困难。但理论上，量子计算机可以快速找到经典计算机可能需要数亿年才能解决的问题的答案。</p><p>为保持加密算法相对于量子计算机性能的领先性，世界各地的研究人员们正在设计让传统和量子计算机都难以破解的“后量子加密算法”。</p><blockquote><p>慕尼黑工业大学电气工程师 Georg Sigl 解释称，此类算法多依赖于一种基于格（lattice-based）的密码学，围绕基于多点或向量的问题而展开。</p><p>简而言之，基于格的加密算法，通常在格中选择秘密消息所依赖的目标点，然后添加随机噪声，使之接近但不完全在某个其它格点上。</p></blockquote><p>在不知道添加了何种噪声的情况下，想要找到原始目标点和相应的秘密信息的话，对于经典和量子计算机来说都是极具挑战性的，尤其当晶格非常庞大时。</p><p>另一方面，在生成随机性和多项式相乘等操作时，这种加密算法也要消耗大量的算力。好消息是，Georg Sigl 及其同事们已经开发出了一种带有定制加速器的微芯片，能够非常高效地执行这些步骤。</p><p><img src="https://static.cnbetacdn.com/article/2021/0824/f858b7e9f66c68f.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图（来自：<a href="https://dl.acm.org/doi/10.1145/3457388.3458869" target="_self">ACS</a>）</p><p><a href="https://spectrum.ieee.org/risc-v-chip-delivers-quantum-resistant-encryption" target="_self">IEEE Spectrum</a> 指出，新芯片基于开源的 RISC-V 标准，并通过硬件组件和控制软件来相互补充，以有效地生成随机性、并降低多项式乘法的复杂性。</p><p>这项工作的合作伙伴，包括西门子、英飞凌、Giesecke+Devrient 等德国工业巨头。以 Kyber 加密为例，与完全基于软件解决方案的芯片相比，新芯片可提速约 10 倍、且能耗仅为 1/8 。</p><p>早在 2020 年的 IACR《密码硬件与嵌入式系统汇刊》上，研究团队就已经详细介绍了这些发现。此外这种微芯片足够灵活，能够支持另一种不基于格的 SIKE 后量子算法。</p><p>Kyber 被视为最具前途的后量子点阵密码算法之一，但 SIKE 需要消耗更多的算力。预计新芯片的速度，是基于纯软件方案的加密芯片的 21 倍。</p>   
</div>
            