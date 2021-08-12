
---
title: '【安全公司：Punk Protocol被黑因其CompoundModel的Initialize函数未做重复初始化检查】据慢雾区消息，去中心化年金协议 Punk Protocol 在公平启动的过程中遭遇...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=7569'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=7569'
---

<div>   
【安全公司：Punk Protocol被黑因其CompoundModel的Initialize函数未做重复初始化检查】据慢雾区消息，去中心化年金协议 Punk Protocol 在公平启动的过程中遭遇攻击，慢雾安全团队以简讯形式将攻击原理分享如下： 
1.攻击者调用CompoundModel合约的Initialize函数进行重复初始化操作，将合约Forge角色设置为攻击者指定的地址。 
2.随后攻击者为了最大程度的将合约中资金取出，其调用了invest函数将合约中的资金抵押至Compound中，以取得抵押凭证cToken。 
3.最后攻击者直接调用withdrawToForge函数将合约中的cToken转回Compound获取到对应的底层资产并最终将其转给Forge角色。 
4.withdrawToForge函数被限制只有Forge角色可以调用，但Forge角色已被重复初始化为攻击者指定的地址，因此最终合约管理的资产都被转移至攻击者指定的地址。总结：本次攻击的根本原因在于其CompoundModel的Initialize函数未做重复初始化检查，导致攻击者直接调用此函数进行重复初始化替换Forge角色，最终造成合约管理的资产被盗。 
总结：本次攻击的根本原因在于其 CompoundModel 的 Initialize 函数未做重复初始化检查，导致攻击者直接调用此函数进行重复初始化替换 Forge 角色，最终造成合约管理的资产被盗。  
</div>
            