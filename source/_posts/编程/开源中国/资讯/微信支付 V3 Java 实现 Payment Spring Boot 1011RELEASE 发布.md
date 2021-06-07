
---
title: '微信支付 V3 Java 实现 Payment Spring Boot 1.0.11.RELEASE 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da2bee3feb3b45cebf75ebfce2f85e24~tplv-k3u1fbpfcp-zoom-1.image'
author: 开源中国
comments: false
date: Mon, 07 Jun 2021 09:30:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da2bee3feb3b45cebf75ebfce2f85e24~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">微信支付API V3版本的Java实现<strong>Payment Spring Boot</strong>发布<strong>1.0.11.RELEASE</strong>版本，本次版本主要增加了对V3版本分账的支持，优化了部分API实现。同时感谢YoungBreezeM和AmazingDM两位同学的PR。更多的细节请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot%2Freleases%2Ftag%2F1.0.11.RELEASE" target="_blank">更新日志</a>。</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot">Payment Spring Boot</a> 是微信支付V3的Java实现，仅仅依赖Spring内置的一些类库。配置简单方便，可以让开发者快速为Spring Boot应用接入微信支付。</p> 
<blockquote> 
 <p>欢迎Star 、PR，有问题请ISSUE。</p> 
</blockquote> 
<h2 style="text-align:start">功能特性</h2> 
<ul> 
 <li> <p>实现微信支付多商户</p> </li> 
 <li> <p>集成支付宝SDK、快速接入Spring Boot</p> </li> 
 <li> <p>实现微信支付V3 基础支付</p> </li> 
 <li> <p>实现微信支付V3 合单支付</p> </li> 
 <li> <p>实现微信支付V3 代金券</p> </li> 
 <li> <p>实现微信支付V3 微信支付分</p> </li> 
 <li> <p>实现微信支付V3 先享卡</p> </li> 
 <li> <p>实现微信支付V3 商家券</p> </li> 
 <li> <p>实现微信支付V3 批量转账到零钱</p> </li> 
</ul> 
<p style="text-align:start"><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da2bee3feb3b45cebf75ebfce2f85e24~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">依赖坐标</h2> 
<p style="text-align:start">最新版本Maven坐标为：</p> 
<pre style="text-align:left">  <dependency>
      <groupId>cn.felord</groupId>
      <artifactId>payment-spring-boot-starter</artifactId>
      <version>1.0.11.RELEASE</version>
  </dependency></pre> 
<h2 style="text-align:start">更新日志</h2> 
<ul> 
 <li> <p>微信支付</p> 
  <ul> 
   <li> <p>feat: bcprov-jdk15to18算法库从1.66 升级到 1.67</p> </li> 
   <li> <p>feat: 微信支付 《支付通知API》新增优惠功能（promotion_detail）字段</p> </li> 
   <li> <p>feat: 微信支付基础支付《申请退款API》、《查询退款API》新增字段 from（退款出资账户及金额）</p> </li> 
   <li> <p>feat: 现在支持V3分账功能，目前只支持直连商户分账<code>WechatProfitsharingApi</code>和服务商分账<code>WechatPartnerProfitsharingApi</code>。</p> </li> 
   <li> <p>feat: 完善V3批量转账到零钱API，增加实现：转账明细电子回单受理API、查询转账明细电子回单受理结果API、查询账户实时余额API、查询账户日终余额API、商户银行来账查询API</p> </li> 
   <li> <p>refactor: 微信支付分分账标记默认改为不分账</p> </li> 
   <li> <p>refactor: 平台证书刷新逻辑优化 (<a href="https://gitee.com/felord/payment-spring-boot/issues/I3NGSB">#I3NGSB</a>)</p> </li> 
   <li> <p>refactor: 交易账单和资金账单现在能够正常的下载文件了，可以根据参数自动选择下载为gzip或者txt文件</p> </li> 
   <li> <p>fix: 批量转账到零钱:微信明细单号查询明细单API,商家明细单号查询明细单API 参数错误</p> </li> 
   <li> <p>fix: 修复查询代金券参数的错误</p> </li> 
  </ul> </li> 
 <li> <p>支付宝</p> 
  <ul> 
   <li> <p>feat: 支付宝增加字段<code>classpathUsed</code>来标识是否使用类路径，默认<code>true</code>。证书路径可依此来决定是使用绝对路径还是类路径</p> </li> 
  </ul> </li> 
</ul> 
<p style="text-align:start">演示项目： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot-samples">payment-spring-boot-samples</a></p> 
<p style="text-align:start">文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnotfound403.github.io%2Fpayment-spring-boot%2F%23%2F">Payment Spring Boot文档</a></p>
                                        </div>
                                      
</div>
            