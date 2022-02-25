
---
title: '美、英发现新的僵尸网络恶意程序 Cyclops Blink'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0225/f80deddb3723a13.png'
author: cnBeta
comments: false
date: Fri, 25 Feb 2022 04:32:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0225/f80deddb3723a13.png'
---

<div>   
英国国家网络安全中心（National Cyber Security
Centre，NCSC）以及美国联邦调查局（FBI）等组织近日指出，俄罗斯黑客集团 Sandworm 自 2019 年 6
月就开始利用僵尸网络恶意程序 Cyclops Blink 来感染连网设备，并且主要锁定由 WatchGuard
所开发的防火墙设备，相关单位并未公布 Cyclops Blink 僵尸网络的规模，<strong>而 WatchGuard 则表示只有不到 1% 的设备被感染，但已释出检测工具和整治计划。</strong><br>
 <p>Sandworm 在 2015 年和 2016 年间曾针对乌克兰的电厂展开攻击，也曾在全球大规模散布 NotPetya 勒索软件。Sandworm 先前使用的僵尸网络恶意程序为 VPNFilter，在 2018 年 5 月遭到思科（Cisco）威胁情报组织 Talos 揪出，VPNFilter 当时已经感染了全球 50 万台网络设备，被黑的设备主要位于乌克兰，同月 FBI 即藉由接管 VPNFilter 的网域，摧毁了这个僵尸网络。</p><p>上述组织相信 Cyclops Blink 是 Sandworm 用来取代 VPNFilter 的作品，而且从 2019 年便开始部署，意味着 Cyclops Blink 已潜伏超过两年，而且主要部署在 WatchGuard 防火墙设备上。</p><p>黑客针对 WatchGuard 设备的 Firebox 软件更新程序进行了反向工程，并找到该程序中的弱点，可重新计算用以验证软件更新映像档的 HMAC 值，<strong>让 Cyclops Blink 得以常驻于 WatchGuard 设备上，不论重新启动还是更新软件都无法移除它。</strong></p><p>Cyclops Blink 还具备读写设备档案系统的能力，可置换合法的档案，因此就算上述弱点已被修补，黑客依旧能够部署新功能来维持 Cyclops Blink 的存在，属于很高阶的恶意程序。</p><p>WatchGuard 在同一天给出了检测工具及整治计划，表示只有不到 1% 的 WatchGuard 防火墙设备受到感染，<strong>若未配置允许来自网络的无限制存取，便不会有危险，且并无证据显示 WatchGuard 或客户资料外泄。</strong></p><p><img src="https://static.cnbetacdn.com/article/2022/0225/f80deddb3723a13.png" referrerpolicy="no-referrer"><br></p><p>WatchGuard 提供了 3 种检测工具，包括可从网络存取的 Cyclops Blink Web Detector，还有必须下载并执行安装的 WatchGuard System Manager Cyclops Blink Detector，两者的主要差异是前者必须与 WatchGuard 分享诊断纪录，后者则不需要，此外还有一款是专供拥有 WatchGuard Cloud 帐号使用的 WatchGuard Cloud Cyclops Blink Detector。</p><p><strong>如果设备遭到感染，那么就必须依照 WatchGuard 的指示重置设备到干净状态，再升级到最新的 Fireware OS 版本。</strong>不仅如此，用户也必须更新管理帐号的密码短语，以及更换所有该设备先前所使用的凭证或短语，最后要确认该防火墙的管理政策并不允许来自网络的无限制存取。</p><p>WatchGuard 还建议所有用户，不管有无受到感染都应升级到最新的 Fireware OS，因为它修补了最新的漏洞，也提供了自动化的系统完整性检查能力，得以强化对软件的保护。</p>   
</div>
            