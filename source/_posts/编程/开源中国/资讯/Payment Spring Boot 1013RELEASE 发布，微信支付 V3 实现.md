
---
title: 'Payment Spring Boot 1.0.13.RELEASE 发布，微信支付 V3 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://asset.felord.cn/blog/20220613092244.png'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 10:52:00 GMT
thumbnail: 'https://asset.felord.cn/blog/20220613092244.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>Payment Spring Boot</span></strong></span><span> 发布 </span><span><strong><span>1.0.13.RELEASE</span></strong></span><span> 版本，本次版本主要增加了V3新增智慧停车方案</span><span><strong><span>微信支付分停车服务</span></strong></span><span>的支持，增加了分账和支付分的一些新API，优化了原有部分 API 实现，升级了部分依赖的版本。</span></p> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot"><span>Payment Spring Boot</span></a></span><span> 是微信支付 V3 的 </span><span><strong><span>Java</span></strong></span><span> 实现，仅仅依赖 </span><span><strong><span>Spring</span></strong></span><span> 内置的一些类库。配置简单方便，可以让开发者快速为 </span><span><strong><span>Spring Boot</span></strong></span><span> 应用接入微信支付。更多更新信息请参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnotfound403.github.io%2Fpayment-spring-boot%2F%23%2Fchangelog" target="_blank"><span>changelog</span></a></span><span>。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>项目地址</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>Github：</span></strong></span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot" target="_blank"><span>https://github.com/NotFound403/payment-spring-boot</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>Gitee：</span></strong></span><span> </span><span><a href="https://gitee.com/felord/payment-spring-boot"><span>https://gitee.com/felord/payment-spring-boot</span></a></span></p> </li> 
</ul> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>欢迎 </span><span><strong><span>Star</span></strong></span><span> 、</span><span><strong><span>PR</span></strong></span><span>，有问题请 </span><span><strong><span>ISSUE</span></strong></span><span>。</span></p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>功能特性</span></h2> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span><img src="https://asset.felord.cn/blog/20220613092244.png" referrerpolicy="no-referrer"></span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPartnerProfitsharingApi</code></span><span> 微信支付服务商V3分账</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPayCallback</code></span><span> 微信支付V3回调通知工具封装</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatAllocationApi</code></span><span> 微信支付V2分账（未来会移除）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatMarketingFavorApi</code></span><span> 微信支付代金券V3</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatCombinePayApi</code></span><span> 微信支付合单支付V3</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPayScoreApi</code></span><span> 微信支付分V3</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPayRedpackApi</code></span><span> 微信支付V2现金红包</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatDiscountCardApi</code></span><span> 微信支付V3先享卡</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatProfitsharingApi</code></span><span> 微信支付直连商户V3分账</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPartnerPayApi</code></span><span> 微信支付服务商模式V3普通支付</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatMarketingBusiFavorApi</code></span><span> 微信支付V3商家券</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPayTransfersApi</code></span><span> 微信支付V2企业付款到零钱，目前不包括到银行卡</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatDirectPayApi</code></span><span> 微信支付直连模式V3普通支付</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatPayScoreParkingApi</code></span><span> 微信支付分V3停车服务</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><code>WechatBatchTransferApi</code></span><span> 微信支付V3批量转账到零钱 </span></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>依赖坐标</span></h2> 
<p style="color:#34495e; margin-left:.8em; margin-right:.8em; text-align:start"><span>最新版本 Maven 坐标为：</span></p> 
<pre style="margin-left:.8rem; margin-right:.8rem; text-align:left"> <span>  <dependency></span>
 <span>      <groupId>cn.felord</groupId></span>
 <span>      <artifactId>payment-spring-boot-starter</artifactId></span>
 <span>      <version>1.0.13.RELEASE</version></span>
 <span>  </dependency></span></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>1.0.13 更新日志</span></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>新特性</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>微信支付</span></h3> 
<h4 style="text-align:start"><span>商家券</span></h4> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feat: 商家券增加营销补差付款API</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feat: 商家券增加查询营销补差付款单详情API</span></p> </li> 
</ul> 
<h4 style="text-align:start"><span>微信分账</span></h4> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feat: 新增申请分账账单API</span></p> </li> 
</ul> 
<h4 style="text-align:start"><span>微信支付分</span></h4> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feat: 新增商户申请获取支付分对账单API</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>feat: 实现支付分停车服务API</span></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增查询车牌服务开通信息API</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增创建停车入场API</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增扣费受理API</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增查询订单API</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增停车入场状态变更通知API</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增订单支付结果通知API</span></p> </li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>修复</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix: NPE without notifyUrl（</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot%2Fissues%2F59" target="_blank"><span>#59</span></a></span><span>）</span></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>依赖升级</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级</span><span><strong><span>Spring Boot</span></strong></span><span> </span><span><code>2.4.2</code></span><span>到</span><span><code>2.7.0</code></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>升级</span><span><strong><span>alipay-sdk-java</span></strong></span><span> </span><span><code>4.10.167.ALL</code></span><span>到</span><span><code>4.31.7.ALL</code></span></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            