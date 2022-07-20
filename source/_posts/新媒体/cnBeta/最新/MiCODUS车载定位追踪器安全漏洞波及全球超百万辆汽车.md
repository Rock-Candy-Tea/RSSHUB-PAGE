
---
title: 'MiCODUS车载定位追踪器安全漏洞波及全球超百万辆汽车'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0720/668d73e23047bc1.png'
author: cnBeta
comments: false
date: Wed, 20 Jul 2022 02:39:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0720/668d73e23047bc1.png'
---

<div>   
一项新研究表明，<strong>某厂商制造的一款流行的 GPS 车辆追踪器，存在一个极易被利用来跟踪和远程切断全球超百万车辆动力输出的安全漏洞。</strong>网络安全初创公司 BitSight 表示，其在 MV720 中发现了六个漏洞。但更糟糕的是，该厂商并无去积极修复的意愿。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0720/668d73e23047bc1.png" referrerpolicy="no-referrer"></p><p>报告指出，这款由 MiCODUS 制造的硬连线 GPS 追踪器，拥有全球 42 万+ 客户和 150 万终端部署量。</p><blockquote><p>除了私家车、执法机构、以及军队和政府客户，<a href="https://www.bitsight.com/blog/bitsight-discovers-critical-vulnerabilities-widely-used-vehicle-gps-tracker" target="_self">BitSight</a> 还发现，财富 50 强公司和一家核电运营商也在使用这款 GPS 追踪器。</p><p>危险的是，攻击可在远程轻松利用相关安全漏洞来实时追踪任何车辆、访问路线历史记录、甚至切断形式中的车辆引擎。</p></blockquote><p>BitSight 首席安全研究员 Pedro Umbelino 补充道：</p><blockquote><p>这些漏洞的利用难度并不高、且其性质揭示了其它模型的重大问题 —— 暗示 MiCODUS 品牌的其它 GPS 追踪器型号也可能存在相关风险。</p></blockquote><p>鉴于漏洞的严重性、且没有修复程序，BitSight 和美国政府的网络安全咨询机构 <a href="https://www.cisa.gov/uscert/ncas/current-activity/2022/07/19/cisa-released-security-advisory-micodus-mv720-global-positioning" target="_self">CISA</a> 都发出了警告，提醒车主尽快移除这些设备以降低风险。</p><blockquote><p>这六个漏洞的严重性和可利用性各不相同，除了其中一个、其它几个都为‘高’或更严重。</p><p>部分 bug 存在于 GPS 追踪器本身，而客户用于追踪其车队的 Web 仪表板也漏洞百出。</p></blockquote><blockquote></blockquote><p>但最让安全研究人员感到担心的，还是硬编码密码方面的缺陷。</p><blockquote><p>由于密码直接嵌入到 Android 应用程序的代码中，任何人都可挖掘、找到、并利用。</p><p>其可被用于完全控制任何 GPS 追踪器、访问车辆实时位置和路线历史、乃至远程切断动力输出。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0720/e3647bd4257aaf0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0720/e3647bd4257aaf0.png" referrerpolicy="no-referrer"></a></p><p>此外研究发现这款 GPS 追踪器的默认密码为 123456，且任何人都可访问未修改过密码的 GPS 追踪器。</p><blockquote><p>BitSight 测试发现，1000 台设备样本中，有 95% 在使用未更改的默认密码来访问。</p><p>这或许是在初始配置时，设备就没有提醒用户变更密码。</p></blockquote><p>另外两个是“不安全的直接对象引用”漏洞（简称 IDOR）：</p><blockquote><p>IDOR 漏洞使得登录用户能够访问不属于他们的、易受攻击的 GPS 追踪器的数据。</p><p>电子表格中包括了设备生成的活动记录，比如历史位置和行驶路线。</p></blockquote><p>最后，研究人员在世界各地都发现了易受攻击的 MiCODUS GPS 追踪器。</p><blockquote><p>其中乌克兰、俄罗斯、乌兹别克斯坦、巴西，以及包括西班牙、波兰、德国和法国在内的整个欧洲地区的设备集中度最高。</p><p>BitSight 发言人 Kevin Long 指出，即使美国市场的问题设备比例较小，也确切数字也可能有成千上万。</p></blockquote><p>遗憾的是，尽管这些漏洞可能对车主造成灾难性的影响，但在 2021 年 9 月首次联系 MiCODUS 之后，该公司仍未在报告发布前积极修复。</p><p>通常情况下，安全研究人员会被厂商留下三个月的缓冲时间。不过截稿时，MiCODUS 并未立即回应外媒的置评请求。</p>   
</div>
            