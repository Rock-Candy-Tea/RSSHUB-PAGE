
---
title: '微信支付 V3 的 Java 实现 Payment Spring Boot-1.0.9.RELEASE 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da2bee3feb3b45cebf75ebfce2f85e24~tplv-k3u1fbpfcp-zoom-1.image'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 09:23:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da2bee3feb3b45cebf75ebfce2f85e24~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">今天微信支付API V3版本的Java实现<strong>Payment Spring Boot</strong>发布了<strong>1.0.9.RELEASE</strong>版本，本次更新主要为Bug修复，具体更新详情参见文末，同时对热心的一些同学提出的建议和Bug进行了修复。</p> 
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
<pre style="text-align:left"> <dependency>
     <groupId>cn.felord</groupId>
     <artifactId>payment-spring-boot-starter</artifactId>
     <version>1.0.9.RELEASE</version>
 </dependency></pre> 
<h2 style="text-align:start">本次更新</h2> 
<ul> 
 <li> <p>微信支付</p> 
  <ul> 
   <li> <p>refactor: 服务商支付 <code>WechatPartnerPayApi</code> 加入<strong>Spring IOC</strong></p> </li> 
   <li> <p>fix: 支付分支付成功回调反序列化异常 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot%2Fissues%2F21" target="_blank">#21</a>）</p> </li> 
   <li> <p>fix: 修复枚举空指针问题 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot%2Fissues%2F22" target="_blank">#22</a>）</p> </li> 
  </ul> </li> 
</ul> 
<p style="text-align:start"> </p> 
<p style="text-align:start">演示项目： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNotFound403%2Fpayment-spring-boot-samples">payment-spring-boot-samples</a></p> 
<p style="text-align:start">文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnotfound403.github.io%2Fpayment-spring-boot%2F%23%2F">Payment Spring Boot文档</a></p>
                                        </div>
                                      
</div>
            