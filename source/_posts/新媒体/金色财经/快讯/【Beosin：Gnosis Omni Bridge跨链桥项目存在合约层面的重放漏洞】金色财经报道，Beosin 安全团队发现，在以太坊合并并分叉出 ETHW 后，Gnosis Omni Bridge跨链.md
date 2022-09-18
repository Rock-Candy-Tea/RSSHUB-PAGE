
---
title: '【Beosin：Gnosis Omni Bridge跨链桥项目存在合约层面的重放漏洞】金色财经报道，Beosin 安全团队发现，在以太坊合并并分叉出 ETHW 后，Gnosis Omni Bridge跨链...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=8128'
author: 金色财经
comments: false
date: Sun, 18 Sep 2022 05:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8128'
---

<div>   
【Beosin：Gnosis Omni Bridge跨链桥项目存在合约层面的重放漏洞】金色财经报道，Beosin 安全团队发现，在以太坊合并并分叉出 ETHW 后，Gnosis Omni Bridge跨链桥项目，由于合约代码中固定写死了chainID，而未真正验证当前所在链的chainID，导致合约在验证签名时能够在分叉链上验证通过。攻击者首先在 ETH 主网上通过omni Bridge 转移 WETH，随后将相同的交易内容在 ETHW 链上进行了重放，获取了等额的 ETHW。目前攻击者已经转移了 741 ETHW 到交易所。 
Beosin 安全团队建议如果项目方合约里面预设了chainID，请先手动将chainId更新，即使项目方决定不支持ETHW，但是由于无法彻底隔绝通过跨链桥之间的资产流动，建议都在ETHW链上更新。  
</div>
            