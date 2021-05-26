
---
title: '谷歌披露新型Rowhammer攻击 可突破访问多行内存地址上的内容'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0526/8d11dd2c10a2e44.jpg'
author: cnBeta
comments: false
date: Wed, 26 May 2021 11:43:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0526/8d11dd2c10a2e44.jpg'
---

<div>   
早在 2014 年，就有许多研究人员讨论过影响当时主流的 DDR3 内存的 Rowhammer 漏洞。2015 年的时候，谷歌发布了一个可利用该漏洞的利用程序。<strong>可知通过对一个内存地址的多次访问请求，将使得攻击者能够篡改其它内存地址中存储的内容。</strong>更糟糕的是，由于该漏洞源于硅芯片中的电耦合现象，所以相关漏洞攻击将能够绕过基于软件和硬件层面的防护。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0526/8d11dd2c10a2e44.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">DRAM 颗粒资料图（来自：Samsung）</p><p>为堵上这一缺陷，许多 DRAM 制造商在自家芯片产品中部署了相应的逻辑检测功能，以便在检测到非法访问时进行溯源和阻止。</p><p>然而现实是，即便市面上主流的 DRAM 芯片已经升级到了 DDR4，但攻击者仍可通过 TRRespass 之类的手段来利用 Rowhammer 漏洞。</p><p>以谷歌最新披露的“半双”（<a href="https://security.googleblog.com/2021/05/introducing-half-double-new-hammering.html" target="_self">Half-double</a>）技术为例，其危险程度比初始版本还要高得多。</p><p>此前只需通过重复访问一个内存地址，即可访问相邻一行的 DRAM 地址。但谷歌现已证明，即使效力有所降低，他们还是成功地将非法地址访问多加了一行。</p><p>如图所示，研究人员先是尝试多次访问地址“A”，然后顺利实现了对地址“B”的数十次访问，接着又向地址“C”发起了攻击。</p><p><img src="https://static.cnbetacdn.com/article/2021/0526/49254ddc84d349f.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">谷歌希望促成跨行业合作，以封堵 Rowhammer 内存访问漏洞。</p><p>谷歌解释称，Half-double 与 TRRespass 有很大的不同。旧攻击利用了制造商在相关防御上的盲点，而新手段直接砸到了轨基板底层的固有属性。</p><p>考虑到电耦合（Electrical Coupling）与距离相关，随着芯片制程的不断发展，DRAM 的单元尺寸也会跟着缩小，导致 Rowhammer 攻击的波及范围也变得更广（大于两行的概念验证也将是可行的）。</p><p>在最坏的情况下，恶意代码或可借此逃脱沙箱环境、甚至接管系统。为堵上这个大漏洞，谷歌正在与 JEDEC 等半导体行业的工贸组织和软硬件研究人员展开密切合作，以寻求潜在的解决方案。</p><p>感兴趣的朋友，可查阅谷歌发布的有关缓解技术的两份文档：</p><blockquote><p><a href="https://www.jedec.org/standards-documents/docs/jep300-1" target="_self">（1）</a>《NEAR-TERM DRAM LEVEL ROWHAMMER MITIGATION》</p><p><a href="https://www.jedec.org/standards-documents/docs/jep301-1" target="_self">（2）</a>《SYSTEM LEVEL ROWHAMMER MITIGATION》</p></blockquote>   
</div>
            