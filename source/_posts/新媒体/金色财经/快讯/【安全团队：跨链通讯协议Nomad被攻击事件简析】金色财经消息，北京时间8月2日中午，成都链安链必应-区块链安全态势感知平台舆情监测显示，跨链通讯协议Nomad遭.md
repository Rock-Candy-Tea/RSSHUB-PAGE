
---
title: '【安全团队：跨链通讯协议Nomad被攻击事件简析】金色财经消息，北京时间8月2日中午，成都链安链必应-区块链安全态势感知平台舆情监测显示，跨链通讯协议Nomad遭...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=1741'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=1741'
---

<div>   
【安全团队：跨链通讯协议Nomad被攻击事件简析】金色财经消息，北京时间8月2日中午，成都链安链必应-区块链安全态势感知平台舆情监测显示，跨链通讯协议Nomad遭遇攻击，成都链安安全团队现将解析结果分享如下，通过被攻击合约（0x88a69b4e698a4b090df6cf5bd7b2d47325ad30a3）的转账交易看到，许多地址都进行了攻击。通过找到一笔相关交易，可以到看到攻击者利用了（0xb36f6479b1aa5582ce862bfb6eb94591e1b0e0b977188c2e8ca85699efcd6183）合约中的process函数进行提取。 
在process函数中，可以看到合约对_messageHash进行了判断,而输入的messages[_messageHash]为0x000000....时，相当于任何未使用的hash，都可以判断通过。然后跟进acceptableRoot函数，因为_root设置为零（x000000....）,而confirmAt[_root]等于1，导致判断恒成立，攻击者就能提取资金。成都链安链必追平台将对被盗资金进行实时监控。  
</div>
            