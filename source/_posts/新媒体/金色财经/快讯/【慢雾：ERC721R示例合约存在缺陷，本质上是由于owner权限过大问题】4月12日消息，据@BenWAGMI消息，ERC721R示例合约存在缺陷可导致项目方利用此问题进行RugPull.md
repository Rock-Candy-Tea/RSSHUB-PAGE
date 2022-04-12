
---
title: '【慢雾：ERC721R示例合约存在缺陷，本质上是由于owner权限过大问题】4月12日消息，据@BenWAGMI消息，ERC721R示例合约存在缺陷可导致项目方利用此问题进行RugPull...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6503'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=6503'
---

<div>   
【慢雾：ERC721R示例合约存在缺陷，本质上是由于owner权限过大问题】4月12日消息，据@BenWAGMI消息，ERC721R示例合约存在缺陷可导致项目方利用此问题进行RugPull。据慢雾安全团队初步分析，此缺陷本质上是由于owner权限过大问题，在ERC721R示例合约中owner可以通过setRefund Address函数任意设置接收用户退回的NFT地址。 
当此退回地址持有目标NFT时，其可以通过调用refund函数不断的进行退款操作从而耗尽用户在合约中锁定的购买资金。且示例合约中存在owner Mint函数，owner可在NFT mint未达总供应量的情况下进行mint。因此ERC721R的实现仍是防君子不防小人。慢雾安全团队建议用户在参与NFTmint时不管项目方是否使用ERC721R都需做好风险评估。  
</div>
            