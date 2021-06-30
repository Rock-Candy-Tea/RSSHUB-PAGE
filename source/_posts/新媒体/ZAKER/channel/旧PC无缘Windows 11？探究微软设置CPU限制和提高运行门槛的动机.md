
---
title: '旧PC无缘Windows 11？探究微软设置CPU限制和提高运行门槛的动机'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202106/60dbe1e0b15ec061d35f6b18_1024.jpg'
author: ZAKER
comments: false
date: Tue, 29 Jun 2021 20:14:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202106/60dbe1e0b15ec061d35f6b18_1024.jpg'
---

<div>   
<p>在 Windows 11 首个预览版发布之后，虽然微软对 CPU 升级限制和最低设备要求进行了澄清，但依然存在模糊点。微软表示只有第 8 代英特尔芯片、Ryzen 2000 系列以上芯片才能升级 Windows 11 系统。那么之前的设备难道真的就无法运行 Windows 11 了吗？事实可能并非如此。</p><p>首先，从此前偷跑的 ISO 镜像以及当前 Windows Insider 分发的 Build 22000.51 镜像，Windows 11 在第 7 代处理器和更低的设备上也运行良好。当从 ISO 镜像安装的时候，Windows 11 绕过 TPM 2.0 限制是非常简单的，只需将一个 .dll 替换成 Windows 10 中的一个。根据 Albacore 在 Twitter 上的说法，如果你进行清洁安装，Windows 11 甚至不检查 CPU 世代。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202106/60dbe1e0b15ec061d35f6b18_1024.jpg" data-height="473" data-width="700" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202106/60dbe1e0b15ec061d35f6b18_1024.jpg" referrerpolicy="no-referrer"></div></div>对于那些想知道纯净安装 Windows 11 的最低硬件要求是什么（当你从 USB 启动安装时）<p></p><p>● 3686MB 内存</p><p>● 2 个 CPU 核心</p><p>● 1 GHz 基本速度</p><p>● TPM 1.2</p><p>● 支持 Secure Boot 的固件</p><p>如果你是在虚拟机或部署服务器，所有的检查都会被跳过。纯净安装的时候不会检查 CPU。</p><p><strong>那么</strong><strong>微软</strong><strong>为何要对 CPU 代数进行限制？</strong></p><p>那么微软为何要这么麻烦呢？首先，CPU 代数限制与 TPM 完全无关，它是为了 " 经验原因 "，正如操作系统安全总监大卫 · 韦斯顿所指出的："CPU 是出于经验的原因。和 TPM 的要求是不相关的 "。</p><p>在过去，只要他们的电脑符合最低规格（大多数第四代、第五代、第六代和第七代设备都符合，只要它们以某种方式启用 TPM），就可以由用户决定他们是否想要一个 " 伟大的体验 "。对于用户来说，如果因为他们完美的第六代设备不符合 CPU 限制而不得不花 1500 美元以上购买一台新机器，这真的是一种 " 伟大的体验 " 吗？</p><p>那么为何微软从一开始就引起了这些不安，外媒推测原因可能有两个</p><p><strong>a：让很多人感到不安，然后升级设备</strong></p><p>最被消费者接纳的说法就是微软想迫使用户购买新机器。当然，这对 OEM 厂商和微软来说都不是一件坏事，但如果有的话，Windows 11 可以让人们在 Windows 10 上停留更长时间。</p><p><strong>b：为了运行 Android 应用程序或者其他后续功能</strong></p><p>第二种可能涉及到 HVCI，这是一个管理程序的安全措施。它可能会影响到像 Windows Subsystem for Android 这样的东西，它被用来在 Windows 11 上运行 Android 应用程序。如果 Android 应用在旧版 CPU 上表现不佳，微软确实可能非常不愿意允许出现不合格的体验。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202106/60dbe1e0b15ec061d35f6b19_1024.jpg" data-height="317" data-width="700" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202106/60dbe1e0b15ec061d35f6b19_1024.jpg" referrerpolicy="no-referrer"></div></div>而另一个可能性是，微软仍对 Windows 11 有后续的发展计划，这些计划目前并未被披露，需要更现代的 CPU 来运行。从事 Azure 工作的微软资深人士 Carmen Crincoli（他在 Twitter 上明确表示，他 " 代表（他）自己，而不是微软 "）在 Twitter 上说，" 他的目标是创造一条前进的道路，使生态系统在几年后处于更强大的地位 "。<p></p><p>如果 ARM 上的 Windows 和 Android 的 Windows 子系统、HVCI，以及 Windows 11 和 Windows 10 之间的密切关系是这些硬件限制的原因，为什么不直接说出来？即使有最好的意图，有时微软也无法摆脱自己的方式。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            