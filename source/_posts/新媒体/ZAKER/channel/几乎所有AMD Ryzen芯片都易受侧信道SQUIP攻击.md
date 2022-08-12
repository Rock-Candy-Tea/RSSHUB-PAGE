
---
title: '几乎所有AMD Ryzen芯片都易受侧信道SQUIP攻击'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f5c978b15ec0581071b40a_1024.jpg'
author: ZAKER
comments: false
date: Thu, 11 Aug 2022 21:56:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f5c978b15ec0581071b40a_1024.jpg'
---

<div>   
<p>IT 之家 8 月 12 日消息，安全研究发现了一个新 CPU 漏洞 "SQUIP"，它是 Scheduler Queue Usage via Interference Probing 的缩写。基于 AMD Zen 架构的 Ryzen 芯片等很容易受到这一新安全漏洞的影响。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202208/62f5c978b15ec0581071b40a_1024.jpg" data-height="428" data-width="760" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f5c978b15ec0581071b40a_1024.jpg" referrerpolicy="no-referrer"></div></div>该漏洞与 CPU 中的多调度程序队列有关。与 AMD 不同，英特尔在其架构中使用单一调度程序，这意味着它不会受 SQUIP 影响。<p></p><p>在 AMD 方面，采用同步多线程 ( SMT ) 技术的 SKU 受到影响，这几乎包括了所有 AMD 处理器 SKU，除了少数型号（后面附有名单）。该问题在 ID"CVE-2021-46778" 下进行跟踪。</p><p>以下是 AMD 提供的总结和缓解措施：</p><p><strong>概括</strong></p><p>执行单元调度程序争用可能导致在使用同时多线程 ( SMT ) 的代号为 "Zen 1"、"Zen 2" 和 "Zen 3" 的 AMD CPU 微架构上发现的侧通道漏洞。通过测量调度程序队列的争用级别，攻击者可能会泄露敏感信息。</p><p><strong>缓解</strong></p><p>AMD 建议软件开发人员采用现有的最佳实践，包括恒定时间算法，并在适当的情况下避免依赖秘密的控制流，以帮助缓解这一潜在漏洞。</p><p>下面是不受 SQUIP 漏洞影响的 AMD Ryzen SKU，从第一代 Zen 1 到 Zen 3：</p><p>Ryzen 1000 ( Zen 1 ) </p><p>Ryzen 3 1200</p><p>Ryzen 3 1300X</p><p>Ryzen 2000 ( Zen 1+ ) </p><p>Ryzen 3 2300X</p><p>Ryzen 3000 ( Zen 2 ) </p><p>Ryzen 5 3500</p><p>Ryzen 5 3500X</p><p>Athlon 3000/4000 ( Zen 2 ) </p><p>Athlon Gold 3150G/GE</p><p>Athlon Gold 4150G/GE</p><p>除了上面列出的 CPU，所有其他 Ryzen、Athlon、Threadripper 和 EPYC 处理器都受到 SQUIP 的影响，因为它们支持 SMT。</p><p>另外需要注意的是，最初的报道声称苹果 M1 CPU 也易受 SQUIP 漏洞攻击。虽然 M1 也使用拆分调度器，但它应该不会受到影响，因为苹果不使用 SMT。M2 芯片可能也是如此。但是，如果未来的 CPU（例如 M3）迁移到具有相同调度程序设计的 SMT，那么它将很容易受到攻击。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            