
---
title: '【Cream Finance遭到闪电贷攻击原因系AMP代币合约存在可重入漏洞】8月30日，PeckShield派盾发推表示，CreamFinance遭闪电贷攻击是因为AMP代币合约引入了一个可重...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=4238'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=4238'
---

<div>   
【Cream Finance遭到闪电贷攻击原因系AMP代币合约存在可重入漏洞】8月30日，PeckShield派盾发推表示，CreamFinance遭闪电贷攻击是因为AMP代币合约引入了一个可重入漏洞。AMP是一种类似erc777的代币，在更新第一次借款之前，它被用来在转移资产的过程中重新借入资产。在tx示例中，黑客进行了500ETH的闪电贷，并将资金存入作为抵押品。然后黑客借了1900万美元AMP并利用可重入漏洞在AMPtokentransfer()中重新借入了355ETH。然后黑客自行清算借款。黑客在17个不同的交易中重复上述过程，总共获得5.98KETH（约1880万美元）。资金仍存放在以0xCE1F的地址中。派盾正在积极监控此地址的任何移动。据此前报道，抵押借贷平台CreamFinance遭遇闪电贷攻击，损失1800万美元。  
</div>
            