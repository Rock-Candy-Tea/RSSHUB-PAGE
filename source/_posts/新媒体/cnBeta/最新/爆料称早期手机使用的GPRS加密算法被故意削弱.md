
---
title: '爆料称早期手机使用的GPRS加密算法被故意削弱'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0618/49504b44571de81.png'
author: cnBeta
comments: false
date: Fri, 18 Jun 2021 05:00:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0618/49504b44571de81.png'
---

<div>   
<strong>来自欧洲多所大学的研究人员团队，刚刚在一篇论文中指出了早期手机使用的 GPRS 加密算法的脆弱性并非偶然。</strong>随后的事实证明，他们的猜测是对的。正如 Vice 强调的那样，GEA-1 主要用于 1990 至 2000 年代的手机数据加密。该算法最初被认为提供了完整的 64-bit 加密安全性，但在他们的密码分析中，研究团队发现其安全性其实在设计时就被限定在了 40 位。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0618/49504b44571de81.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 1：GEA-1 密码流的结构（来自：<a href="https://link.springer.com/chapter/10.1007%2F978-3-030-77886-6_6" target="_self">Springer Link</a> | <a href="https://eprint.iacr.org/2021/819.pdf" target="_self">PDF</a>）</p><p>为进一步求证，研究团队还从不愿透露姓名的消息人士处获得了有关 GEA-A 和 GEA-2 算法的更多细节，以便他们能够开展全面分析并找出其中的弱点，结果证实了“不太可能发生”的偶然性。</p><p>TechSpot 指出，具有拦截<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>数据流量能力的攻击者，可领用该漏洞来解密会话中的所有消息。</p><p><img src="https://static.cnbetacdn.com/article/2021/0618/c3f4ebbca18f1d8.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 2：GEA-1 随机样本的线性初始化</p><p>外媒 Vice 也与设计 GEA-1 加密算法的欧洲电信标准协会（ETSI）取得了联系，该组织一位发言人在电子邮件声明中承认，该算法确实包含了一个弱点。</p><p>但它被引入的原因，是它被要求“必须存在”，因为 ETSI 需要遵守限制 GEA-1 强度的出口管制规定。</p><p><img src="https://static.cnbetacdn.com/article/2021/0618/031e75ba18902db.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 3：GEA-1 与 GEA-2 的密钥生成概述</p><p>考虑到当时的国际形势，这种出口管制规定确实相当普遍。此外据 The Register 报道称，法国方面制定了一项禁止任何超过 40-bit 加密的类似规则。</p><p>参与这项新研究的 Håvard Raddum 吐槽道：“为迎合这方面的限制政策，其导致数以百万计的用户在很长一段时间里，都无法获得本该拥有的安全上网保护”。</p><p><img src="https://static.cnbetacdn.com/article/2021/0618/f17555a8d742ef6.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究图表 - 4：GEA-X 的手机 / 基带支持状况概述</p><p>不过这项研究曝出的最大问题，就是当时在制定推出 GEA-1 标准时没有明确提及任何的出口管制。</p><p>而且研究团队发现，即使技术操作的难度有所提升，但 GEA-2 算法同样很容易受到攻击。</p><p>庆幸的是，这两项标准都没能得到广泛的使用，且厂商更倾向于选择更新后的安全加密算法 —— 尽管某些市场的网络仍将之作为后备。</p>   
</div>
            