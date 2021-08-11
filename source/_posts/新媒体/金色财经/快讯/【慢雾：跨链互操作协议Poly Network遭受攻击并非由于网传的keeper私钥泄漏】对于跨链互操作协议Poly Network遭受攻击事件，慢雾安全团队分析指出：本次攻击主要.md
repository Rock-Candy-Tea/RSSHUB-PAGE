
---
title: '【慢雾：跨链互操作协议Poly Network遭受攻击并非由于网传的keeper私钥泄漏】对于跨链互操作协议Poly Network遭受攻击事件，慢雾安全团队分析指出：本次攻击主要...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=365'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=365'
---

<div>   
【慢雾：跨链互操作协议Poly Network遭受攻击并非由于网传的keeper私钥泄漏】对于跨链互操作协议Poly Network遭受攻击事件，慢雾安全团队分析指出：本次攻击主要在于EthCrossChainData合约的keeper可由EthCrossChainManager合约进行修改，而EthCrossChainManager合约的verifyHeaderAndExecuteTx函数又可以通过_executeCrossChainTx函数执行用户传入的数据。因此攻击者通过此函数传入精心构造的数据修改了EthCrossChainData合约的keeper为攻击者指定的地址，并非网传的是由于keeper私钥泄漏导致这一事件的发生。  
</div>
            