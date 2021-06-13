
---
title: '【V神提议对以太坊未来的分片和历史访问进行预编译】Vitalik Buterin（V神）发文研究对未来的分片和历史访问进行预编译。V神在文章中表示，当前以太坊设计中的向...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=402'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=402'
---

<div>   
【V神提议对以太坊未来的分片和历史访问进行预编译】Vitalik Buterin（V神）发文研究对未来的分片和历史访问进行预编译。V神在文章中表示，当前以太坊设计中的向后兼容性挑战之一是，历史访问需要在EVM中验证Merkle证明，该证明假设区块链将永远使用相同的格式和相同的密码。分片增加了这一点的重要性，因为用于rollups的欺诈证明和有效性证明需要指向分片数据的指针。V神提出了一种更加面向未来的方法：我们可以添加执行验证特定类型证明的抽象任务的预编译，而不是要求在EVM中验证历史和分片的证明。如果将来更改格式，预编译逻辑将自动更改。预编译甚至可以具有条件逻辑，用于验证转换前slots的一种证明和转换后slots的另一种证明。  
</div>
            