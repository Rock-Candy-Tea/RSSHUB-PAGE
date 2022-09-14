
---
title: 'LPC 2022：MGLRU页面回收改进有望并入Linux 6.1内核主线'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0914/b8c0a8ae434b2c9.jpg'
author: cnBeta
comments: false
date: Wed, 14 Sep 2022 07:24:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0914/b8c0a8ae434b2c9.jpg'
---

<div>   
<strong>在爱尔兰都柏林举办的 LPC 2022 活动期间，我们看到了有望在 Linux 6.1 中并入主流的 Multi-Gen LRU 项目的最新进展。</strong>作为当前 Linux 内核页面回收代码的一个更好替代方案，如果 MGLRU 能够在 2022 的最后一个完整内核周期内登陆 Linux 6.1，那它也将成为年内最激动人心的创新之一。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0914/b8c0a8ae434b2c9.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>Phoronix 指出，从 ChromeOS / Android，到台式机、工作站、甚至服务器领域，MGLRU 普遍能够在各项工作负载和各类硬件平台上提供更好的性能。</p><p><img src="https://static.cnbetacdn.com/article/2022/0914/83218a97f2c82ad.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p>Google 的 Jesse Barnes 和 Rom Lemarchand 在昨日的 LPC 2022 活动期间指出，现有的页面回收代码总被吐槽做出了糟糕的驱逐选择。</p><p><img src="https://static.cnbetacdn.com/article/2022/0914/26b4ef2077db9be.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>好消息是，俩人重申了 MGLRU 有望并入 Linux 6.1 的期望。可知目前已有不少内核下游和反向移植在生产环境中使用相关代码，且基准测试成绩的前景也显得相当光明。</p><p><img src="https://static.cnbetacdn.com/article/2022/0914/32e435a8b1b5f52.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p>一旦走入主线，Google 工程师团队将致力于让 MGLRU 达到和默认安全启用的水平。</p><p><img src="https://static.cnbetacdn.com/article/2022/0914/729fc497d3ebcfc.webp" alt="4.webp" referrerpolicy="no-referrer"></p><p>尽管在这之前，他们还需要开展各种基准测试，以确保 MGLRU 处理良好状态、且不会使现有工作负载出现性能退化。同时他们希望将 MGLRU 与 eBPF 集成，以开辟更多可能性。</p><p><img src="https://static.cnbetacdn.com/article/2022/0914/7168e5a3c69bee8.webp" alt="5.webp" referrerpolicy="no-referrer"></p><p>最后，在今日的 LPC 2022 会议期间的 Android 小分会上，Google 公司的 Kalesh Singh 就 Android 设备上的 MGLRU 性能进行了演示。</p><p><img src="https://static.cnbetacdn.com/article/2022/0914/571ef7613519d85.jpg" alt="6.jpg" referrerpolicy="no-referrer"></p><p>此外 Andrew Morton 评论称，其希望在本周晚些时候将 MGLRU  补丁挪到“mm-stable”分支。如果一切顺利，我们可期待在 10 月开启的下一个 Linux 6.1 合并窗口。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1315525.htm" target="_blank">LPC 2022：谷歌工程师介绍Ghost Linux内核调度API的最新进展</a></p></div>   
</div>
            