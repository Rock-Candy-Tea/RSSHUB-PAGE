
---
title: 'GNU C Library放弃一系列SSSE3指令集优化的代码路径'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0416/96d6c017012a5ab.jpg'
author: cnBeta
comments: false
date: Sat, 16 Apr 2022 10:54:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0416/96d6c017012a5ab.jpg'
---

<div>   
本周最新的GNU C Library（Glibc）开发代码已经开始放弃各种SSSE3指令集优化代码路径。补充流SIMD扩展3指令集（SSSE3）可以追溯到十多年前的英特尔至强5100/酷睿2或AMD Bobcat/Bulldozer核心，当时的设想是作为SSE的一个迭代。<br>
 <p>但是由于Glibc也携带了与SSSE3差不多时间的旧版SSE2或SSE4.1的优化代码路径，加上用于较新的Intel/<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> CPU的AVX2和EVEX代码路径，SSSE3的代码路径实质上已经无人在使用或者均已被替代。</p><p>Glibc开发者认为，考虑到SSE2/SSE4.1/AVX2/EVEX代码路径的存在，已经不值得再提供SSSE3指令集优化的代码路径，因为很少有<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>/AMD CPU被留在SSSE3这条路径上，而在代码中提供SSSE3支持的成本却不低，因此从本周起，开发人员已经开始舍弃它。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0416/96d6c017012a5ab.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Xeon 5100系列引入了SSSE3支持</p><p>在删除的SSSE3支持中包括放弃mem&#123;move|cpy&#125;-ssse3-back、str&#123;p&#125;&#123;n&#125;cpy-ssse3、str&#123;n&#125;cat-ssse3、str&#123;n&#125;&#123;case&#125;cmp-ssse3和&#123;w&#125;memcmp-ssse3代码路径。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0416/f6da4fc51479b3e.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">SSSE3在Core 2时代很有用，但对于过去几年的CPU来说，Glibc AVX2代码路径更有利</p><p>围绕memmove/mempcpy/memcpy的SSSE3代码也有减少。提交人解释说。</p><p>我们的目标是删除大部分SSSE3功能，因为SSE4、AVX2和EVEX通常更受欢迎。memcpy/memmove是一个例外，对于某些目标来说，用`palignr`避免无符号负载很重要。</p><p>此提交用一个更好的优化和更低的代码占用率的版本替换了 memmove-ssse3。此外，它还将 memcpy 别名为 memmove。</p>   
</div>
            