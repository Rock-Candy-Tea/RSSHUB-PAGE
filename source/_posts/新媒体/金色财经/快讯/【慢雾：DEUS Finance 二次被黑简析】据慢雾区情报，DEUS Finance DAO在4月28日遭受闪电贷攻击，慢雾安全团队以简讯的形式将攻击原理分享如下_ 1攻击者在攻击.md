
---
title: '【慢雾：DEUS Finance 二次被黑简析】据慢雾区情报，DEUS Finance DAO在4月28日遭受闪电贷攻击，慢雾安全团队以简讯的形式将攻击原理分享如下_ 
1.攻击者在攻击...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=290'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=290'
---

<div>   
【慢雾：DEUS Finance 二次被黑简析】据慢雾区情报，DEUS Finance DAO在4月28日遭受闪电贷攻击，慢雾安全团队以简讯的形式将攻击原理分享如下: 
1.攻击者在攻击之前先往DeiLenderSolidex抵押了SolidexsAMM-USDC/DEI的LP。 
2.在几个小时后攻击者先从多个池子闪电贷借出143200000USDC。 
3.随后攻击者使用借来的USDC在BaseV1Pair进行了swap操作，兑换出了9547716.9个的DEI，由于DeiLenderSolidex中的getOnChainPrice函数是直接获取DEI-USDC交易对的代币余额进行LP价格计算。因此在此次Swap操作中将拉高getOnChainPrice函数获取的LP价格。 
4.在进行Swap操作后，攻击者在DeiLenderSolidex合约中通过borrow函数进行借贷，由于borrow函数中用isSolvent进行借贷检查，而在isSolvent是使用了getOnChainPrice函数参与检查。但在步骤3中getOnChainPrice的结果已经被拉高了。导致攻击者超额借出更多的DEI。 
5.最后着攻击者在把用借贷出来DEI兑换成USDC归还从几个池子借出来的USDC，获利离场。 
针对该事件，慢雾安全团队给出以下防范建议：本次攻击的原因主要在于使用了不安全的预言机来计算LP价格，慢雾安全团队建议可以参考Alpha Finance关于获取公平LP价格的方法。  
</div>
            