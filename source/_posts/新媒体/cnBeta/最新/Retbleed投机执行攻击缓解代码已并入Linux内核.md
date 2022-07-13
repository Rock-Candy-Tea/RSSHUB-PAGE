
---
title: 'Retbleed投机执行攻击缓解代码已并入Linux内核'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0713/f480062956d3e84.jpg'
author: cnBeta
comments: false
date: Wed, 13 Jul 2022 02:27:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0713/f480062956d3e84.jpg'
---

<div>   
本周迎来的 RETBLEED 补丁，修复了影响当今硬件的两个新投机执行攻击漏洞。Phoronix 指出 —— <strong>Retbleed 会利用返回指令、并能够破坏针对“幽灵”（Spectre）分支目标注入（BTI）的现有防御措施。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0713/f480062956d3e84.jpg" referrerpolicy="no-referrer"></p><p>在四年前之时，人们还不怎么相信会受到 BTI 攻击。但这种“不切实际”的设想，最终还是被现实给打了脸。</p><p>Computer Security Group 安全研究人员发现 —— Retbleed 不仅能够绕过“retpolines”防御，还证明了返回指令可被实际利用。</p><p><img src="https://static.cnbetacdn.com/article/2022/0713/c51a0e56db3c4d9.png" referrerpolicy="no-referrer"></p><p>据悉，该问题影响 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Zen 1 / 1+ / 2，以及 Intel 6~8 代酷睿处理器。<strong>此外从今天的披露来看，处理器也面临性能开销增加的压力。</strong></p><p>想要在 Linux 内核层面缓解 Retbleed 攻击，需要付出巨大的努力。涉及修改 68 处文件，引入 1783 行新代码、同时剔除 387 行旧代码。</p><p><img src="https://static.cnbetacdn.com/article/2022/0713/0661c5455f43cbe.png" referrerpolicy="no-referrer"></p><p>性能评估表明，缓解 Retbleed 的代价非常高昂 —— 实测 AMD（<a href="https://www.cve.org/CVERecord?id=CVE-2022-29900" target="_self">CVE-2022-29900</a>）/ Intel（<a href="https://www.cve.org/CVERecord?id=CVE-2022-29901" target="_self">CVE-2022-29901</a>）补丁的开销，有在 14% 到 39% 之间。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=364774411&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">RETBleed Leaking root password hash from _etc_shadow（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzY0Nzc0NDExLnNodG1s.html" target="_self">via</a>）</p><p>最后，Retbleed 缓解工作已于今早被合并到 Linux 内核中。至于更多细节，还请移步至 Retbleed 专题网站（via <a href="https://comsec.ethz.ch/research/microarch/retbleed/" target="_self">ComSec</a>）了解。</p>   
</div>
            