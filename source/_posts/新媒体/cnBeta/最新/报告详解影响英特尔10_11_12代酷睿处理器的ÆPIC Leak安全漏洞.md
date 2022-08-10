
---
title: '报告详解影响英特尔10_11_12代酷睿处理器的ÆPIC Leak安全漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0810/7c00c62a76b8cdd.jpg'
author: cnBeta
comments: false
date: Wed, 10 Aug 2022 09:28:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0810/7c00c62a76b8cdd.jpg'
---

<div>   
<strong>在“幽灵”（Spectre）和“熔毁”（Meltdown）漏洞曝出后，近年来针对 Intel 和 AMD x86 CPU 的侧信道攻击也愈演愈烈。</strong>本周二，英特尔推送了 20220809 微码更新，以修补影响包括 10 / 11 / 12 代酷睿在内的大量处理器的 Intel-SA-00657 安全漏洞。不久后，我们又看到了详细的分析报告。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0810/7c00c62a76b8cdd.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：ÆPIC Leak <a href="https://aepicleak.com/#attack" target="_self">专题网站</a>）</p><p>来自罗马第一大学、格拉茨理工 / 科技大学、以及亚马逊 AWS 公司的研究人员们指出：</p><blockquote><p>该漏洞名叫 ÆPIC Leak，它以处理中断请求的高级可编程中断控制器（APIC）而命名，并且是首个 CPU 架构级敏感数据泄露漏洞。</p></blockquote><p>据悉，在大多数 10、11、12 代酷睿处理器上，APIC MMIO 未对从缓存层次结构返回的陈旧数据施加适当的范围定义。</p><p>与 Spectre 和 Meltdown 等瞬态执行攻击相比，ÆPIC Leak 漏洞要更贴近于架构层面 —— 敏感数据会被直接泄露，而不依赖于任何嘈杂的侧信道。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=372956086&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">ÆPIC LEAK IN ACTION - Demo 1（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzcyOTU2MDg2LnNodG1s.html" target="_self">via</a>）</p><p>换言之，ÆPIC Leak 就像是在 CPU 本体中读取的未初始化内存。庆幸的是，访问 APIC MMIO 将需要特定的权限（管理员或 root），因而大多数系统不会受到该漏洞的直接影响。</p><p>另一方面，依赖<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> SGX 软件防护扩展功能，来保护数据免受特权攻击的系统，将面临更大的风险 —— 这也是 Intel 积极推送 CPU 微码补丁的一个重要原因。</p><p><img src="https://static.cnbetacdn.com/article/2022/0810/438dd433dd2e461.gif" alt="Demo 2.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">ÆPIC LEAK IN ACTION - Demo 2</p><p>目前该漏洞的概念演示，已由格拉茨理工学院开源（<a href="https://github.com/IAIK/AEPIC" target="_self">GitHub</a>）。至于英特尔那边，这家芯片巨头已于 2021 年 12 月知悉此事，并且分配了 <a href="https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/advisory-guidance/stale-data-read-from-xapic.html" target="_self">CVE-2022-21233</a> 这个通用漏洞披露编号。</p><p>最后，如果没有第一时间部署 20220809 CPU 微码更新，也可通过禁用 APIC MMIO 或绕开 SGX，以临时躲开基于该漏洞的攻击利用。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1302729.htm" target="_blank">英特尔推送20220809 CPU微码更新 修补Intel-SA-00657安全漏洞</a></p></div>   
</div>
            