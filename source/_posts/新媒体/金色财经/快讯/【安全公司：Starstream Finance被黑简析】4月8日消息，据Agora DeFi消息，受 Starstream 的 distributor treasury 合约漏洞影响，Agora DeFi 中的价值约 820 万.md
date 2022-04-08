
---
title: '【安全公司：Starstream Finance被黑简析】4月8日消息，据Agora DeFi消息，受 Starstream 的 distributor treasury 合约漏洞影响，Agora DeFi 中的价值约 820 万...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6181'
author: 金色财经
comments: false
date: Fri, 08 Apr 2022 09:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6181'
---

<div>   
【安全公司：Starstream Finance被黑简析】4月8日消息，据Agora DeFi消息，受 Starstream 的 distributor treasury 合约漏洞影响，Agora DeFi 中的价值约 820 万美金的资产被借出。慢雾安全团队进行分析后以简讯的形式分享给大家。 
1. 在 Starstream 的 StarstreamTreasury 合约中存在 withdrawTokens 函数，此函数只能由 owner 调用以取出合约中储备的资金。而在 April-07-2022 11:58:24 PM +8UTC 时，StarstreamTreasury 合约的 owner 被转移至新的 DistributorTreasury 合约(0x6f...25)。 
2. 新的 DistributorTreasury 合约中存在 execute 函数，而任意用户都可以通过此函数进行外部调用，因此攻击者直接通过此函数调用 StarstreamTreasury 合约中的 withdrawTokens 函数取出合约中储备的 532,571,155.859 个 STARS。 
3. 攻击者将 STARS 抵押至 Agora DeFi 中，并借出大量资金。一部分借出的资金被用于拉高市场上 STARS 的价格以便借出更多资金。  
</div>
            