
---
title: '仓储系统中，如果库存货物是服务器，配置根据需求来发货到仓库，sku该怎么设计？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 天天问
headimg: 'https://picsum.photos/400/300?random=9232'
author: 人人都是产品经理
comments: false
date: Wed, 06 Jul 2022 11:09:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=9232'
---

<div>   
<p>目前有个仓储系统的项目</p><p>库存货物是服务器，比如A服务器标配是2TX2=4T硬盘，内存是256G</p><p>先从销售端提起出库申请，比如客户要A服务器，配置要求8T硬盘+512G内存，采购拿到后，向供货商购买，此时有两种情况：</p><ol style="list-style-type: decimal;"><li><p>供货商提供标配+增配4T硬盘和256G内存，但是增配的4T硬盘可能是1TX4，2Tx2，4Tx1，内存条也不一定。</p></li><li><p>供货商提供标配+增配256G内存，然后采购向单独的硬盘厂家采购4T硬盘，也不一定是1TX4，2Tx2，4Tx1。</p></li></ol><p>基于这种情况，A服务器的sku应该怎么设计，库存中的A可能是标配的，也可能是增配的，如果按照配置分开sku，库存有4T+256G的库存但没有4T+512G的库存时，销售提交出库申请，系统怎么判断是否有货。</p><p><br></p>  
</div>
            