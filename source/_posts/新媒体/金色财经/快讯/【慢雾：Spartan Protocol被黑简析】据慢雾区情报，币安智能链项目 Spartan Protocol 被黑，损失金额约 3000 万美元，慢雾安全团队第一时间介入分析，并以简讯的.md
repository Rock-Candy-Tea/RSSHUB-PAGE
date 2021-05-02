
---
title: '【慢雾：Spartan Protocol被黑简析】据慢雾区情报，币安智能链项目 Spartan Protocol 被黑，损失金额约 3000 万美元，慢雾安全团队第一时间介入分析，并以简讯的...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=985'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=985'
---

<div>   
【慢雾：Spartan Protocol被黑简析】据慢雾区情报，币安智能链项目 Spartan Protocol 被黑，损失金额约 3000 万美元，慢雾安全团队第一时间介入分析，并以简讯的形式分享给大家参考： 
1. 攻击者通过闪电贷先从 PancakeSwap 中借出 WBNB； 
2. 在 WBNB-SPT1 的池子中，先使用借来的一部分 WBNB 不断的通过 swap 兑换成 SPT1，导致兑换池中产生巨大滑点； 
3. 攻击者将持有的 WBNB 与 SPT1 向 WBNB-SPT1 池子添加流动性获得 LP 凭证，但是在添加流动性的时候存在一个滑点修正机制，在添加流动性时将对池的滑点进行修正，但没有限制最高可修正的滑点大小，此时添加流动性，由于滑点修正机制，获得的 LP 数量并不是一个正常的值； 
4. 随后继续进行 swap 操作将 WBNB 兑换成 SPT1，此时池子中的 WBNB 增多 SPT1 减少； 
5. swap 之后攻击者将持有的 WBNB 和 SPT1 都转移给 WBNB-SPT1 池子，然后进行移除流动性操作； 
6. 在移除流动性时会通过池子中实时的代币数量来计算用户的 LP 可获得多少对应的代币，由于步骤 5，此时会获得比添加流动性时更多的代币； 
7. 在移除流动性之后会更新池子中的 baseAmount 与 tokenAmount，由于移除流动性时没有和添加流动性一样存在滑点修正机制，移除流动性后两种代币的数量和合约记录的代币数量会存在一定的差值； 
8. 因此在与实际有差值的情况下还能再次添加流动性获得 LP，此后攻击者只要再次移除流动性就能再次获得对应的两种代币； 
9. 之后攻击者只需再将 SPT1 代币兑换成 WBNB，最后即可获得更多的 WBNB。详情见原文链接。<br><a href="https://bscscan.com/tx/0xb64ae25b0d836c25d115a9368319902c972a0215bd108ae17b1b9617dfb93af8" target="_blank">原文链接</a>  
</div>
            