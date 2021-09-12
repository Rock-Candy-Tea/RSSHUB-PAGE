
---
title: '【慢雾：Avalanche链上Zabu Finance被黑简析】据慢雾区情报，9月12日，Avalanche上Zabu Finance项目遭受闪电贷攻击，慢雾安全团队进行分析后以简讯的形式分享给...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=7520'
author: 金色财经
comments: false
date: Sun, 12 Sep 2021 22:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7520'
---

<div>   
【慢雾：Avalanche链上Zabu Finance被黑简析】据慢雾区情报，9月12日，Avalanche上Zabu Finance项目遭受闪电贷攻击，慢雾安全团队进行分析后以简讯的形式分享给大家参考： 
1.攻击者首先创建两个攻击合约，随后通过攻击合约1在Pangolin将WAVAX兑换成SPORE代币，并将获得的SPORE代币抵押至ZABUFarm合约中，为后续获取ZABU代币奖励做准备。 
2.攻击者通过攻击合约2从Pangolin闪电贷借出SPORE代币，随后开始不断的使用SPORE代币在ZABUFarm合约中进行`抵押/提现`操作。由于SPORE代币在转账过程中需要收取一定的手续费(SPORE合约收取)，而ZABUFarm合约实际接收到的SPORE代币数量是小于攻击者传入的抵押数量的。分析中我们注意到ZABUFarm合约在用户抵押时会直接记录用户传入的抵押数量，而不是记录合约实际收到的代币数量，但ZABUFarm合约在用户提现时允许用户全部提取用户抵押时合约记录的抵押数量。这就导致了攻击者在抵押时ZABUFarm合约实际接收到的SPORE代币数量小于攻击者在提现时ZABUFarm合约转出给攻击者的代币数量。 
3.攻击者正是利用了ZABUFarm合约与SPORE代币兼容性问题导致的记账缺陷，从而不断通过`抵押/提现`操作将ZABUFarm合约中的SPORE资金消耗至一个极低的数值。而ZABUFarm合约的抵押奖励正是通过累积的区块奖励除合约中抵押的SPORE代币总量参与计算的，因此当ZABUFarm合约中的SPORE代币总量降低到一个极低的数值时无疑会计算出一个极大的奖励数值。 
4.攻击者通过先前已在ZABUFarm中有进行抵押的攻击合约1获取了大量的ZABU代币奖励，随后便对ZABU代币进行了抛售。 
此次攻击是由于ZabuFinance的抵押模型与SPORE代币不兼容导致的，此类问题导致的攻击已经发生的多起，慢雾安全团队建议：项目抵押模型在对接通缩型代币时应记录用户在转账前后合约实际的代币变化，而不是依赖于用户传入的抵押代币数量。  
</div>
            