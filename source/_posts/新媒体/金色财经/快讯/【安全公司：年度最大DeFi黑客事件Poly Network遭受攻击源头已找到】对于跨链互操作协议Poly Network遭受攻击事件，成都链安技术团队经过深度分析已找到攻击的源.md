
---
title: '【安全公司：年度最大DeFi黑客事件Poly Network遭受攻击源头已找到】对于跨链互操作协议Poly Network遭受攻击事件，成都链安技术团队经过深度分析已找到攻击的源...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=323'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=323'
---

<div>   
【安全公司：年度最大DeFi黑客事件Poly Network遭受攻击源头已找到】对于跨链互操作协议Poly Network遭受攻击事件，成都链安技术团队经过深度分析已找到攻击的源头。该笔交易对应的跨链交易由本体链上f771ba开头的这笔交易发出，并定位到本体链上AM2W2L开头的攻击者地址。攻击者在ONT链上进行攻击尝试发现有效后，通过这笔f771ba开头的地址交易批量向多个链发起更改Keeper的跨链消息，然后BSC链的relayer 0xa0872c79开头地址率先处理了该笔跨链交易，并将keeper设置为攻击者指定的以0xa87开头的地址。 
接着Ethereum、Polygon两条链上攻击者重放了BSC链的 relayer所使用的有效签名。Keeper地址更改为自己的地址后，攻击者使用自己可控的Keeper发起了提币交易，转移了跨链池中的资产。此处攻击成功表明PolyNetwork在对跨链交易事件的验证存在缺陷，导致了恶意的跨链消息被接收并在对应的链上进行了跨链消息所指定的操作。  
</div>
            