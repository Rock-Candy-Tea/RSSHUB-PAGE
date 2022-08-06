
---
title: '【慢雾：GenomesDAO被黑简析】据慢雾区hacktivist消息，MATIC上@GenomesDAO项目遭受黑客攻击，导致其LPSTAKING合约中资金被非预期的取出。慢雾安全团队进行分析...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=7540'
author: 金色财经
comments: false
date: Sat, 06 Aug 2022 03:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7540'
---

<div>   
【慢雾：GenomesDAO被黑简析】据慢雾区hacktivist消息，MATIC上@GenomesDAO项目遭受黑客攻击，导致其LPSTAKING合约中资金被非预期的取出。慢雾安全团队进行分析有以下原因： 
1.由于GenomesDAO的LPSTAKING合约的initialized函数公开可调用且无权限与不可能重复初始化限制，攻击者利用initialized函数将合约的stakingToken设置为攻击者创建的虚假LP代币。 
2.随后攻击者通过stake函数进行虚假LP代币的抵押操作，以获得大量的LPSTAKING抵押凭证。 
3.获得凭证后再次通过initialized函数将合约的stakingToken设置为原先真是的LP代币，随后通过withdraw函数销毁LPSTAKING凭证获取合约中真实的LP抵押物。 
4.最后将LP发送至DEX中移除流动性获利。 
本次事件是因为GenomesDAO的LPSTAKING合约可被任意重复初始化设置关键参数而导致合约中的抵押物被恶意耗尽。  
</div>
            