
---
title: 'M1 Mac开源驱动开发者揭秘了苹果定制GPU解决方案的特殊渲染方法'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg'
author: cnBeta
comments: false
date: Mon, 16 May 2022 01:59:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg'
---

<div>   
<strong>尽管苹果一直在 M1 系列定制处理器的内部细节守口如瓶，但为 M1 Mac 硬件打造开源驱动程序的 Asahi Linux 发行版开发团队，还是努力在对其展开逆向工程。</strong>可知在艰苦的逆向工作期间，他们也发现了一些相当古怪且酷炫的地方。以 M1 开源图形驱动程序为例，Alyssa Rosenzweig 最近就在 M1 GPU 渲染管道中发现了一个化解错误的关键点。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>据悉，问题始于 GPU 对内存访问的不畅。作为一款性能超强的 GPU，它与 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a> 上的 A 系列移动SoC 一样，需要通过走一些捷径来保持高效率。</p><p>可知与独显相比，M1 没有直接渲染到帧缓冲区，而是对帧进行两次传递 —— 首先找到顶点，然后搞定其它更加密集的事务。</p><p><img src="https://static.cnbetacdn.com/article/2022/0516/f67f5a7aa83f316.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>为此，苹果利用了专用硬件将帧分割成小块（基本上是迷你帧），并于二传时一次取一个小块来处理。</p><p>平铺方案很好地化解了缓存资源不足的问题，但为了稍后将之凑成完整的一帧，GPU 需要保留每个顶点数据的缓冲区。</p><p>结果 Rosenzweig 发现，每当这个缓冲区溢出时、渲染就无法正常进行下去。</p><p><img src="https://static.cnbetacdn.com/article/2022/0516/448f1bf21061e1c.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>苹果在某个演示文稿中解释称，当缓冲区已满时，GPU 只会输出部分渲染（本例中为半只兔子）。</p><p>在第一方应用程序中，苹果称之为参数缓冲区，且这个名词术语似乎取自 Imagination 的 PowerVR 文档。</p><p>作为一家总部位于英国的、与 ARM 类似的芯片设计公司，Imagination 于 2020 年初与苹果签署了一项广泛的知识产权许可协议。</p><p>而 2020 下半年上市的 M1 定制 SoC，就以该公司的 PowerVR GPU 架构为其图形硬件的基础。</p><p><img src="https://static.cnbetacdn.com/article/2022/0516/fce2f926f123acc.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>言归正传，正如你可能已经猜到的那样，软件可通过将各部分渲染叠加到一起、以完成整只兔子的渲染（当然中间还有十几个额外的步骤）。</p><p>遗憾的是，这种渲染方式仍然不太准确（仔细留意兔子的足部）。Rosenzweig 指出，这是因为帧的不同部分在颜色 / 深度缓冲区之间被分割，而后者在加载部分渲染时会出现异常行为。</p><p>好消息是，得益于苹果驱动程序的逆向工程参考配置，Asahi Linux 开发团队最终搞定了这个问题，最终渲染输出的兔子如图所示。</p><p><img src="https://static.cnbetacdn.com/article/2022/0516/577a2ef033a2f26.jpg" alt="4.jpg" referrerpolicy="no-referrer"></p><p><a href="https://www.techspot.com/news/94593-inside-apple-m1-incredibly-quirky-gpu.html" target="_self">TechSpot</a> 总结道：不仅 Rosenzweig 的 M1 开源图形驱动程序跳过了相关环节来渲染图像，而是该 GPU 在架构设计之初就没有考虑到此类 3D 渲染应用场景。</p><p>即便如此，苹果还是相当巧妙地让 PowerVR 图形 IP 成为了可与独显相媲<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mideajiadian.jd.com/" target="_blank">美的</a>软硬件解决方案。即便在许多方面都没有实现完全的超越，其表现依然相当酷炫。</p><p>最后，想要深入了解 M1 GPU 渲染工作、以及针对 M1 逆向工程的其它探索，还请移步至 Rosenzweig 的<a href="https://rosenzweig.io/blog/asahi-gpu-part-5.html" target="_self">个人技术博客</a>和 Asahi Linux <a href="https://asahilinux.org/blog/" target="_self">发行版网站</a>查看。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1187369.htm" target="_blank">进展报告：Asahi Linux在苹果的M1架构上实现了基本可用的桌面功能</a></p><p><a href="https://www.cnbeta.com/articles/tech/1198359.htm" target="_blank">Asahi团队已在M1 Pro上顺利启动Linux：后续仍有很多工作</a></p><p><a href="https://www.cnbeta.com/articles/tech/1266475.htm" target="_blank">Asahi Linux致力于将M1 Mac NVMe驱动支持并入Linux 5.19主线内核</a></p></div>   
</div>
            