
---
title: '服务端如何防止订单重复支付？ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=5174'
author: 技术头条
comments: false
date: 2021-12-05 02:34:12
thumbnail: 'https://picsum.photos/400/300?random=5174'
---

<div>   
如图是一个简化的下单流程，首先是提交订单，然后是支付。支付的话，一般是走支付网关（支付中心），然后支付中心与第三方支付渠道（微信、支付宝、银联）交互，支付成功以后，异步通知支付中心，支付中心更新自身支付订单状态，再通知业务应用，各业务再更新各自订单状态。
    
</div>
            