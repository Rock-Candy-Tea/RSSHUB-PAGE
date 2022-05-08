
---
title: '【安全公司：BistrooIO遭受重入攻击，损失约47000美元】5月8日消息，据成都链安_链必应-区块链安全态势感知平台_安全舆情监控数据显示，BistrooIO 项目遭受重...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6235'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=6235'
---

<div>   
【安全公司：BistrooIO遭受重入攻击，损失约47000美元】5月8日消息，据成都链安“链必应-区块链安全态势感知平台“安全舆情监控数据显示，BistrooIO 项目遭受重入攻击，损失1,711,569个BIST（约47000美元），经成都链安技术团队分析，本次攻击原因是由于pTokens BIST代币支持ERC-777的代币标准，其合约在实现transfer调用的时候，会调用_callTokenToSend，进而调用tokensToSend()函数，攻击者在该函数中通过重入方式调用了EmergencyWithdraw函数，造成重入攻击。  
</div>
            