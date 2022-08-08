
---
title: '【安全团队：EGD_Finance被黑，导致池子中的EGD代币被非预期取出】8月8日消息，据慢雾区消息，BSC上的 EGD_Finance 项目遭受黑客攻击，导致其池子中资金被非预期...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=9306'
author: 金色财经
comments: false
date: Mon, 08 Aug 2022 05:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9306'
---

<div>   
【安全团队：EGD_Finance被黑，导致池子中的EGD代币被非预期取出】8月8日消息，据慢雾区消息，BSC上的 EGD_Finance 项目遭受黑客攻击，导致其池子中资金被非预期的取出。慢雾安全团队进行分析后以简讯的形式分享给大家 
1. 由于 EGD_Finance 合约中获取奖励的 claimAllReward 函数在计算奖励时会调用 getEGDPrice 函数来进行计算 EGD 的价格, 而 getEGDPrice 函数在计算时仅通过 pair 里的 EGD 和 USDT 的余额进行相除来计算 EGD 的价格 
2. 攻击者利用这个点先闪电贷借出池子里大量的 USDT, 使得 EGD 代币的价格通过计算后变的很小, 因此在调用 claimAllReward 函数获取奖励的时候会导致奖励被计算的更多, 从而导致池子中的 EGD 代币被非预期取出 
本次事件是因为 EGD_Finance 的合约获取奖励时计算奖励的喂价机制过于简单, 导致代币价格被闪电贷操控从而获利。<br><a href="https://bscscan.com/tx/0x50da0b1b6e34bce59769157df769eb45fa11efc7d0e292900d6b0a86ae66a2b3" target="_blank">原文链接</a>  
</div>
            