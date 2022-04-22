
---
title: '【DeFi借贷协议YEED遭受攻击，黑客获利百万却被永久锁定】4月22日消息，据欧科云链链上天眼监测，近期BSC上刚上线ZEED生态系统的DeFi借贷协议YEED遭受攻击，攻击...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=4305'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=4305'
---

<div>   
【DeFi借贷协议YEED遭受攻击，黑客获利百万却被永久锁定】4月22日消息，据欧科云链链上天眼监测，近期BSC上刚上线ZEED生态系统的DeFi借贷协议YEED遭受攻击，攻击者获利逾100万美元。 
经链上天眼团队追踪分析，此次攻击，黑客将闪电贷借来的资金直接tranfer给YEED-USDT流动性池，触发其分配逻辑，其调用流动性池的skim接口，将池子原有的$YEED一并提取出来。黑客将skim出来的资产接收地址设置为流动性池地址，会自动再次触发transfer逻辑。攻击者用三个流动性池循环操作了300多次，最终将获利的$YEED资产转移到恶意合约，并兑换成USDT。 
但较为乌龙的是，在攻击成功后的15秒后，黑客在还未将获利所得提走时便直接调用了合约的自毁函数，导致该笔资金将永远锁定在其攻击合约里。  
</div>
            