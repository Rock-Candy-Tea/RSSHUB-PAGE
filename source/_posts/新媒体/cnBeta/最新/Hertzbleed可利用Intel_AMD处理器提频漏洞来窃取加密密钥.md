
---
title: 'Hertzbleed可利用Intel_AMD处理器提频漏洞来窃取加密密钥'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0615/cecc3c5afeee5f9.jpg'
author: cnBeta
comments: false
date: Wed, 15 Jun 2022 08:13:46 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0615/cecc3c5afeee5f9.jpg'
---

<div>   
在 2017 年被影响现代 Intel、AMD 和 ARM 处理器的“幽灵”（Spectre）和“熔毁”（Meltdown）侧信道攻击漏洞给震惊之后，<strong>现又有安全研究人员曝光了利用 CPU 提频（Boost Frequencies）来窃取加密密钥的更高级漏洞 —— 它就是 Hertzbleed 。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0615/cecc3c5afeee5f9.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Hertzbleed <a href="https://www.hertzbleed.com/" target="_self">网站</a>）</p><p>该攻击通过监视任何加密工作负载的功率签名（power signature）侧信道漏洞而实现，与 CPU 中的其它因素一样，处理器功率会因工作负载的变化而有所调整。</p><p>但在观察到此功率信息之后，Hertzbleed 攻击者可将之转换为计时数据（timing data），进而窃取用户进程的加密密钥。</p><blockquote><p>● 目前 Intel 和 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 均已公布易受 Heartzbleed 漏洞攻击影响的系统，可知其影响 Intel 全系和 AMD Zen 2 / Zen 3 处理器。</p><p>● 前者被分配了 Intel-SA-00698 和 CVE-2022-24436 这两个漏洞 ID，后者则是 CVE-2022-23823 。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0615/2854f704ff1cf14.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">原理示意（图自：Intel <a href="https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/technical-documentation/frequency-throttling-side-channel-guidance.html#applying-solutions" target="_self">网站</a>）</p><p>更糟糕的是，攻击者无需物理访问设备、即可远程利用 Hertzbleed 漏洞。</p><p>之后两家芯片公司将提供基于微码的修补缓解措施，以防止此类漏洞被攻击者继续利用。</p><p>略为庆幸的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>声称此类攻击在实验室研究之外并不那么实用，因为据说窃取加密密钥需耗费数小时到数天。</p><p>至于漏洞补丁可能造成的 CPU 性能损失，还是取决于具体的应用场景。</p>   
</div>
            