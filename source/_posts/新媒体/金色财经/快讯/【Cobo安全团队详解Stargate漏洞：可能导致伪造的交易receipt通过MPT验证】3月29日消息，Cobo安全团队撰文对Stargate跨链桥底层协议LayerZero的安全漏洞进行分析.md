
---
title: '【Cobo安全团队详解Stargate漏洞：可能导致伪造的交易receipt通过MPT验证】3月29日消息，Cobo安全团队撰文对Stargate跨链桥底层协议LayerZero的安全漏洞进行分析...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6712'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=6712'
---

<div>   
【Cobo安全团队详解Stargate漏洞：可能导致伪造的交易receipt通过MPT验证】3月29日消息，Cobo安全团队撰文对Stargate跨链桥底层协议LayerZero的安全漏洞进行分析，称原始漏洞代码在进行MPT 验证时，没有限制pointer 在proofBytes 长度内，这个漏洞有可能让攻击者伪造hashRoot，导致伪造的交易receipt 可以通过MPT 验证。最终可造成的后果是，在预言机完全可信的前提下，Relayer 仍可以单方面通过伪造receipt 数据的方式来实现对跨链协议的攻击。 
值得注意的是，此次爆出漏洞的代码是LayerZero协议中最核心的MPT交易验证部分的代码，是整个LayerZero及上层协议（例如Stargate）正常运作的基石。Cobo安全团队还表示，LayerZero项目的关键合约目前大都还被EOA控制，没有采用多签机制或者时间锁机制。如果这些特权EOA的私钥一旦泄漏，也可能会导致所有上层协议的资产受到影响。<br><a href="https://mp.weixin.qq.com/s/qcqK7NDPtzy6fTY_0sNZGA" target="_blank">原文链接</a>  
</div>
            