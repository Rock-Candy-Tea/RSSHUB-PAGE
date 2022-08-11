
---
title: '苹果M1与AMD Zen架构处理器易受侧信道SQUIP攻击影响'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202208/62f4a9768e9f091cac564bd0_1024.jpg'
author: ZAKER
comments: false
date: Wed, 10 Aug 2022 23:54:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202208/62f4a9768e9f091cac564bd0_1024.jpg'
---

<div>   
<p><strong>早前，安全研究人员发现了一个名为 "SQUIP"、并且波及苹果 M1 和 AMD Zen 架构 CPU 的新漏洞。</strong>SQUIP 是 " 调度器队列干扰探测 "（Scheduler Queue Usage via Interference Probing）的缩写，该漏洞与 CPU 中的多调度程序队列有关，导致相关芯片易受侧信道 SQUIP 攻击。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202208/62f4a9768e9f091cac564bd0_1024.jpg" data-height="709" data-width="1260" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202208/62f4a9768e9f091cac564bd0_1024.jpg" referrerpolicy="no-referrer"></div></div>（AMD-SB-1039 / CVE-2021-46778 | PDF）<p></p><p>与苹果相比，采用同步多线程（SMT）技术的 AMD 处理器受到的影响要大一些，以下是不受 SQUIP 漏洞影响的 AMD 锐龙 / 速龙 SKU 。</p><p><strong>Ryzen 1000 系列（Zen 1）：</strong></p><p>Ryzen 3 1200</p><p>Ryzen 3 1300X</p><p><strong>Ryzen 2000 系列（Zen 1+）：</strong></p><p>Ryzen 3 2300X</p><p><strong>Ryzen 3000 系列（Zen 2）：</strong></p><p>Ryzen 5 3500</p><p>Ryzen 5 3500X</p><p><strong>Athlon 3000 / 4000（Zen 2）：</strong></p><p>Athlon Gold 3150G / GE</p><p>Athlon Gold 4150G / GE</p><p>除了上述列出的 SKU，其它从 Zen 1 到 Zen 3、支持 SMT 的锐龙、速龙、线程撕裂者（Threadripper）和霄龙（EPYC）处理器都难以幸免。</p><p>AMD 表示，执行单元调度程序的潜在争用，可能导致在使用 SMT 技术的 Zen 1、Zen 2 和 Zen 3 微架构 CPU 时暴露侧信道漏洞。</p><p>通过测量调度程序队列的争用级别，攻击者可能会泄露系统上的敏感信息。有鉴于此，AMD 建议软件开发者采用最佳实践。</p><p>除了推荐恒定时间（constant-time）算法，还请在适当情况下规避对秘密控制流的依赖，从而有助于缓解这一潜在漏洞。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202208/62f4a9768e9f091cac564bd1_1024.jpg" data-height="394" data-width="700" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202208/62f4a9768e9f091cac564bd1_1024.jpg" referrerpolicy="no-referrer"></div></div>Apple Silicon 方面，据说 M1 易受 SQUIP 攻击影响。有趣的是，研究人员并未提到最新的 M2，推测相关缺陷已得到解决。<p></p><p>此外与苹果和 AMD 不同的是，英特尔在其架构中使用单一调度程序，因而幸运地避开了 SQUIP 的影响。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            