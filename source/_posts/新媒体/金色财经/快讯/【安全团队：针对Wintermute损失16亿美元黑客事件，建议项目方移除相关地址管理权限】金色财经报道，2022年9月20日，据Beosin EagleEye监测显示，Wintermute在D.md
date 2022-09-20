
---
title: '【安全团队：针对Wintermute损失1.6亿美元黑客事件，建议项目方移除相关地址管理权限】金色财经报道，2022年9月20日，据Beosin EagleEye监测显示，Wintermute在D...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6937'
author: 金色财经
comments: false
date: Tue, 20 Sep 2022 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6937'
---

<div>   
【安全团队：针对Wintermute损失1.6亿美元黑客事件，建议项目方移除相关地址管理权限】金色财经报道，2022年9月20日，据Beosin EagleEye监测显示，Wintermute在DeFi黑客攻击中损失1.6亿美元，Beosin 安全团队发现，攻击者频繁的利用0x0000000fe6a...地址调用0x00000000ae34...合约的0x178979ae函数向0x0248地址（攻击者合约）转账，通过反编译合约，发现调用0x178979ae函数需要权限校验，通过函数查询，确认0x0000000fe6a地址拥有setCommonAdmin权限，并且该地址在攻击之前和该合约有正常的交互，那么可以确认0x0000000fe6a的私钥被泄露。结合地址特征（0x0000000），疑似项目方使用Profanity工具生成地址。该工具在之前发的文章中，已有安全研究者确认其随机性存在安全缺陷（有暴力破解私钥的风险），导致私钥可能泄漏。 
Beosin 安全团队建议：1.项目方移除0x0000000fe6a地址以及其他靓号地址的setCommonAdmin/owner等管理权限，并使用安全的钱包地址替换。2.其他使用Profanity工具生成钱包地址的项目方或者用户，请尽快转移资产。Beosin Trace正在对被盗资金进行分析追踪。  
</div>
            