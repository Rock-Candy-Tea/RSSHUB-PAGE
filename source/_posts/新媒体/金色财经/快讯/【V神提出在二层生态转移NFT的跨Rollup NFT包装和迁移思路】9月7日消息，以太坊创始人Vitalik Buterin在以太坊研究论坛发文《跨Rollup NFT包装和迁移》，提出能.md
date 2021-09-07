
---
title: '【V神提出在二层生态转移NFT的跨Rollup NFT包装和迁移思路】9月7日消息，以太坊创始人Vitalik Buterin在以太坊研究论坛发文《跨Rollup NFT包装和迁移》，提出能...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=4052'
author: 金色财经
comments: false
date: Tue, 07 Sep 2021 15:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4052'
---

<div>   
【V神提出在二层生态转移NFT的跨Rollup NFT包装和迁移思路】9月7日消息，以太坊创始人Vitalik Buterin在以太坊研究论坛发文《跨Rollup NFT包装和迁移》，提出能够在整个二层生态中转移 NFT的思路。 
他表示，NFT将在一个Rollup中注册，可以通过创建Wrapper NFT在其他二层方案中进行跨链。具体过程为：在Rollup A中，将NFT发送到Wrapper管理器合约，指定目标Rollup和初始所有者锁定合约，然后在储存中保存一条记录，并给NFT分配新的序列号R。在Rollup B中，任何人都可以使用Rollup B上的Wrapper管理器合约中指定源Rollup和序列号，创建包装NFT。当NFT取回时，当前所有者必须将其发送回Wrapper管理器，从带有序列号R、源Rollup的初始所有者中解除包装，将NFT交给新的所有人。NFT取回会有时间延迟，因为Optimistic Rollup状态根需要大约1周的时间延迟才能最终确定，以便收据可以被验证。到目前为止，更快地进行多条链间的跨链，唯一的办法是进行多层包装。  
</div>
            