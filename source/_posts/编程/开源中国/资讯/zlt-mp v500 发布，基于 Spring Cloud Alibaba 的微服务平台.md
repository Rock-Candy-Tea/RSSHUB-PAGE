
---
title: 'zlt-mp v5.0.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 08:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><img alt height="275" src="https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png" width="500" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left">功能介绍</h1> 
<p style="text-align:left"><img alt height="414" src="https://oscimg.oschina.net/oscnet/up-b7726359902d450aab833cda3b17a69b85c.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">更新内容<strong>更新内容</strong></h2> 
<h3 style="text-align:left">特性/增强</h3> 
<ul> 
 <li> <p>升级spring-boot到2.5.4</p> </li> 
 <li> <p>升级spring-cloud到2020.0.3</p> </li> 
 <li> <p>升级spring-cloud-alibaba到2021.1</p> </li> 
 <li> <p>升级druid-spring-boot-starter到1.2.6</p> </li> 
 <li> <p>升级elasticsearch到7.14.0</p> </li> 
 <li> <p>升级spring-boot-admin到2.5.1</p> </li> 
</ul> 
<h3 style="text-align:left">新增工程/分支</h3> 
<ul> 
 <li> <p>新增zlt-loadbalancer-spring-boot-starter工程</p> </li> 
 <li> <p>增加分支4.x（该分支不会更新）</p> 
  <ul> 
   <li> <p>Spring Boot 2.3.12.RELEASE</p> </li> 
   <li> <p>Spring Cloud Hoxton.SR12</p> </li> 
   <li> <p>Spring Cloud Alibaba 2.2.6.RELEASE</p> </li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:left">移除工程</h3> 
<ul> 
 <li> <p>移除zlt-ribbon-spring-boot-starter工程</p> </li> 
 <li> <p>移除zuul-gateway工程</p> </li> 
</ul> 
<h2 style="text-align:left">内容说明</h2> 
<p style="text-align:left">本版本主要为升级 Spring Boot 与 Spring Cloud 到最新的 GA 版本，与旧版本属于非兼容性升级。</p> 
<p style="text-align:left">由于最新版本的 Spring Cloud <strong>彻底删除</strong> 掉了 Netflix 除了 Eureka 外的 <strong>所有组件</strong>，所以作出了以下改动：</p> 
<ul> 
 <li> <p>移除 Netflix 相关的两个工程：zlt-ribbon-spring-boot-starter 和 zuul-gateway</p> </li> 
 <li> <p>新增 zlt-loadbalancer-spring-boot-starter 工程用于代替 ribbon 组件</p> </li> 
</ul> 
<h1>版本说明</h1> 
<table border="1" cellpadding="1" cellspacing="1" style="width:500px"> 
 <tbody> 
  <tr> 
   <td>分支</td> 
   <td>Spring Boot</td> 
   <td>Spring Cloud</td> 
   <td>是否更新</td> 
  </tr> 
  <tr> 
   <td>master</td> 
   <td>2.5.x</td> 
   <td>2020.x</td> 
   <td>是</td> 
  </tr> 
  <tr> 
   <td>4.x</td> 
   <td>2.3.x.RELEASE</td> 
   <td>Hoxton</td> 
   <td>否</td> 
  </tr> 
  <tr> 
   <td>3.x</td> 
   <td>2.1.x.RELEASE</td> 
   <td>Greenwich</td> 
   <td>否</td> 
  </tr> 
  <tr> 
   <td>2.x</td> 
   <td>2.0.x.RELEASE</td> 
   <td>Finchley</td> 
   <td>否</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left"><strong>项目地址</strong></h2> 
<p style="text-align:left">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="text-align:left">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="text-align:left">项目文档</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="text-align:left">项目更新日志</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/936235</a></p>
                                        </div>
                                      
</div>
            