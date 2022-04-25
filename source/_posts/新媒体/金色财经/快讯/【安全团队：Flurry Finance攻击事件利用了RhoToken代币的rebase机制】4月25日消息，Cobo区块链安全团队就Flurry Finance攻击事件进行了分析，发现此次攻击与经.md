
---
title: '【安全团队：Flurry Finance攻击事件利用了RhoToken代币的rebase机制】4月25日消息，Cobo区块链安全团队就Flurry Finance攻击事件进行了分析，发现此次攻击与经...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=1341'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=1341'
---

<div>   
【安全团队：Flurry Finance攻击事件利用了RhoToken代币的rebase机制】4月25日消息，Cobo区块链安全团队就Flurry Finance攻击事件进行了分析，发现此次攻击与经典的闪电贷操纵预言机的攻击手段不同，而是利用了Flurry Finance中RhoToken代币的rebase机制。漏洞的本质原因在于协议对RhoToken进行rebase时计算multiplier的公式中依赖于外部可控的数据（Bank中的token数量）。从而使攻击者通过闪电贷的方式实现了对multiplier的操纵，进而获利。虽然本次攻击中使用到了伪造ERC20重写approve方法再利用Rabbit Finance的StrategyLiquidate合约来执行任意代码的技巧，但这个技巧涉及到的合约代码本身其实并不存在安全问题。Cobo区块链安全团队提醒，开发者在进行项目开发时需要特别注意合约在计算资产数量、价格时是否有依赖外部某些可能被恶意操纵的数据。闪电贷操纵预言机的典型攻击模式其实也是项目中依赖于DEX池内代币价格进行了内部某些关键指标的计算导致的。 
此前消息，2月22日，BSC链上的Flurry Finance遭到闪电贷攻击，导致协议中Vault合约中价值数十万美元的资产被盗。<br><a href="https://mp.weixin.qq.com/s/6uBN4CprsTK5QooQpeeSmA" target="_blank">原文链接</a>  
</div>
            