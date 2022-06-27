
---
title: 'Fizz Gateway 2.6.5 发布，安全修复版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 10:34:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png'
---

<div>   
<div class="content">
                                                                                            <p>v2.6.5<br> changelog:</p> 
<p>修复一些安全漏洞<br> 更新一些后台文案提示<br> 优化统计数据上报接口</p> 
<p>Fix some security vulnerabilities<br> Update some tips messages of fizz manager<br> Optimize reporting interfaces of statistics</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Fizz Gateway 是什么？</h2> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">An Aggregation API Gateway in Java . Fizz Gateway 是一个基于 Java 开发的微服务聚合网关，能够实现热服务编排聚合、自动授权选择、线上服务脚本编码、在线测试、高性能路由、API 审核管理、回调管理等目的，拥有强大的自定义插件系统可以自行扩展，并且提供友好的图形化配置界面，能够快速帮助企业进行 API 服务治理、减少中间层胶水代码以及降低编码投入、提高 API 服务的稳定性和安全性。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">演示环境（Demo）</h2> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2F" target="_blank">http://demo.fizzgate.com/</a></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">账号 / 密码:<code>admin</code>/<code>Aa123!</code></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">健康检查地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fadmin%2Fhealth" target="_blank">http://demo.fizzgate.com/admin/health</a><span> </span>(线上版本请限制 admin 路径的外网访问)</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">API 地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fproxy%2F%255B%25E6%259C%258D%25E5%258A%25A1%25E5%2590%258D%255D%2F%255BAPI_Path%255D" target="_blank">http://demo.fizzgate.com/proxy/[服务名]/[API_Path]</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">Fizz 的设计</h2> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F184315%2F97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" target="_blank"><img src="https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" width="500" referrerpolicy="no-referrer"></a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">产品特性</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>集群管理：Fizz 网关节点是无状态的，配置信息自动同步，支持节点水平拓展和多集群部署。</li> 
 <li>安全授权：支持内置的 key-auth, JWT, basic-auth 授权方式，并且可以方便控制。</li> 
 <li>服务编排：支持 HTTP、Dubbo、gRPC、Soap 协议热服务编排能力，支持前后端编码，支持 JSON/XML 输出，随时随地更新 API。</li> 
 <li>负载均衡：支持 round-robin 负载均衡。</li> 
 <li>多注册中心：支持从 Eureka 或 Nacos 注册中心进行服务发现。</li> 
 <li>配置中心：支持接入 apollo 配置中心。</li> 
 <li>HTTP 反向代理：隐藏真实后端服务，支持 Rest API 反向代理。</li> 
 <li>访问策略：支持不同策略访问不同的 API、配置不同的鉴权等。</li> 
 <li>IP 黑白名单：支持配置 IP 黑白名单。</li> 
 <li>自定义插件：强大的插件机制支持自由扩展。</li> 
 <li>可扩展：简单易用的插件机制方便扩展功能。</li> 
 <li>高性能：性能在众多网关之中表现优异。</li> 
 <li>版本控制：支持操作的发布和多次回滚。</li> 
 <li>管理后台：通过管理后台界面对网关集群进行各项配置。</li> 
 <li>回调管理：支持回调的管理、订阅、重放、以及日志。</li> 
 <li>多级限流：细颗粒度的限流方式包含服务限流，接口限流，APP_ID 限流，IP 限流。</li> 
 <li>微服务文档：企业级管理开放微服务文档管理，系统集成更方便。</li> 
 <li>公网专线：建立公网中受到完全保护的私有连接通道。</li> 
 <li>策略熔断：根据服务或者具体地址进行多种恢复策略熔断配置。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">基准测试</h2> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">我们将 Fizz 与市面上主要的网关产品进行比较，使用相同的环境和条件，测试对象均为单个节点。Mock 接口模拟 20ms 时延，报文大小约 2K。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz * 4</li> 
 <li>Linux version 3.10.0-957.21.3.el7.x86_64</li> 
 <li>8G RAM</li> 
</ul> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>分类</th> 
   <th>产品</th> 
   <th>600 并发<br> QPS</th> 
   <th>600 并发<br> 90% Latency(ms)</th> 
   <th>1000 并发<br> QPS</th> 
   <th>1000 并发<br> 90% Latency(ms)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">后端服务</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">直接访问后端服务</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">23540</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">32.19</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">27325</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">52.09</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">流量网关</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">kong<br> v2.4.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">15662</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">50.87</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">17152</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">84.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">应用网关</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">fizz-gateway-community<br> v2.0.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">12206</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">65.76</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">12766</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">100.34</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">应用网关</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">spring-cloud-gateway<br> v2.2.9</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">11323</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">68.57</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">10472</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">127.59</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">应用网关</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">shenyu<br> v2.3.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">9284</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">92.98</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">9939</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">148.61</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:start">版本对照</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Fizz-gateway-community： 社区版</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fizz-manager-professional：管理后台专业版（服务端）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fizz-admin-professional：管理后台专业版（前端）</p> </li> 
</ul> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Fizz-gateway-community</th> 
   <th>Fizz-manager-professional</th> 
   <th>Fizz-admin-professional</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.0.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.0.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.0.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.1.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.1.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.1.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.1.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.1.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.2.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.2.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.2.0</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">从 v1.3.0 开始管理后台的前端和服务端合并成一个包</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Fizz-gateway-community： 社区版</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fizz-manager-professional：管理后台</p> </li> 
</ul> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Fizz-gateway-community</th> 
   <th>Fizz-manager-professional</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.3.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.3.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.4.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.4.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.4.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.4.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.5.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.5.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.5.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v1.5.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.0.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.0.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.1.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.1.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.2.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.2.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.2.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.2.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.2.3</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.2.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.3.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.3.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.3.2</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.3.2</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.3.3</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.3.3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.4.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.4.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.4.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.4.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.5.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.5.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.5.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.5.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.5.2</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.5.2</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.0</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.0</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.1</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.2</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.2</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.3</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">v2.6.3</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">请根据社区版的版本下载对应的管理后台版本</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">部署说明</h2> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.fizzgate.com%2Fguide%2Finstallation%2F" target="_blank">详细部署教程 >>></a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">安装依赖</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">安装以下依赖软件：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Redis 2.8 或以上版本</li> 
 <li>MySQL 5.7 或以上版本</li> 
 <li>Apollo 配置中心 (可选)</li> 
 <li>Eureka 或 Nacos 服务注册中心 (可选)</li> 
</ul> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">依赖的安装可参考详细部署教程</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">安装 Fizz</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:start">一、安装管理后台</h4> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">从 github 的 releases (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwj.qq.com%2Fs2%2F8682608%2F8fe2%2F" target="_blank">https://wj.qq.com/s2/8682608/8fe2/</a>) 下载 fizz-manager-professional 安装包</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">管理后台（fizz-manager-professional）</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">说明：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>以下安装步骤出现的<span> </span><code>&#123;version&#125;</code><span> </span>表示所使用管理后台的版本号，例如<span> </span><code>1.3.0</code>。</li> 
</ol> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">安装方式一：二进制安装包</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>解压<span> </span><code>fizz-manager-professional-&#123;version&#125;.zip</code><span> </span>安装包</li> 
 <li>首次安装执行<span> </span><code>fizz-manager-professional-&#123;version&#125;-mysql.sql</code><span> </span>数据库脚本，从低版本升级至高版本选择执行 update 目录下对应升级脚本</li> 
 <li>修改<span> </span><code>application-prod.yml</code><span> </span>文件，将相关配置修改成部署环境的配置</li> 
 <li>Linux 启动 执行<span> </span><code>chmod +x boot.sh</code><span> </span>命令给<span> </span><code>boot.sh</code><span> </span>增加执行权限；执行<span> </span><code>./boot.sh start</code><span> </span>命令启动服务，支持 start/stop/restart/status 命令</li> 
 <li>Windows 启动 执行<code>.\boot.cmd start</code><span> </span>命令启动服务，支持 start/stop/restart/status 命令</li> 
</ol> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">安装方式二（v2.0.0 或以上版本）：docker:</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>下载对应版本的镜像：docker pull fizzgate/fizz-manager-professional:&#123;version&#125;</li> 
 <li>通过环境变量方式修改 redis 配置、database 配置（其它配置同理）并运行镜像</li> 
</ol> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1"><span style="color:#6f42c1">docker</span></span> <span style="color:#032f62"><span style="color:#032f62">run --rm -d -p 8000:8000 \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.redis.host=&#123;your redis host IP&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.redis.port=&#123;your redis port&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.redis.password=&#123;your redis password&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.redis.database=&#123;your redis database&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.datasource.url=jdbc:mysql://&#123;your MySQL database host IP&#125;:3306/fizz_manager?useSSL=false&useUnicode=true&characterEncoding=utf-8&zeroDateTimeBehavior=convertToNull&transformedBitIsBoolean=true&serverTimezone=GMT%2B8&nullCatalogMeansCurrent=true&allowPublicKeyRetrieval=true</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.datasource.username=&#123;your MySQL database username&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">spring.datasource.password=&#123;your MySQL database password&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
fizzgate/fizz-manager-professional:&#123;version&#125;</span></span></pre> 
</div> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">或通过映射目录方式使用外部配置文件和输出日志到宿主机，配置文件可从安装包里获取，在宿主机创建 fizz-manager-professional/config 和 fizz-manager-professional/logs 目录，把 application-prod.yml 配置文件放置 config 下，在 fizz-manager-professional 目录下运行镜像</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#6f42c1"><span style="color:#6f42c1">cd</span></span></span> <span style="color:#032f62"><span style="color:#032f62">fizz-manager-professional</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">docker</span></span> <span style="color:#032f62"><span style="color:#032f62">run --rm -d -p 8000:8000 \
-v </span></span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#032f62"><span style="color:#032f62">$PWD</span></span></span><span style="color:#032f62"><span style="color:#032f62">/config:/opt/fizz-manager-professional/config \
-v </span></span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#032f62"><span style="color:#032f62">$PWD</span></span></span><span style="color:#032f62"><span style="color:#032f62">/logs:/opt/fizz-manager-professional/logs fizzgate/fizz-manager-professional:&#123;version&#125;</span></span></pre> 
</div> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">服务启动后访问 http://&#123;部署机器 IP 地址&#125;:8000/#/login，使用超级管理员账户<span> </span><code>admin</code><span> </span>密码<span> </span><code>Aa123!</code><span> </span>登录</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">二、安装 fizz-gateway-community 社区版</h4> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">说明：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>支持配置中心：apollo、nacos，支持注册中心：eureka、nacos，详细配置方法查看 application.yml 文件。</li> 
 <li>如果使用 apollo 配置中心，可把 application.yml 文件内容迁到配置中心（apollo 上应用名为：fizz-gateway）；如果不使用 apollo 可去掉下面启动命令里的 apollo 参数。</li> 
 <li>以下安装步骤出现的<span> </span><code>&#123;version&#125;</code><span> </span>表示所使用网关的版本号，例如<span> </span><code>1.3.0</code>。</li> 
</ol> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">安装方式一：二进制安装包</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>下载 fizz-gateway-community 的二进制安装包，解压修改 application.yml 配置文件里配置中心、注册中心、redis (redis 配置需与管理后台一致) 的配置</li> 
 <li>根据需要修改 boot.sh 脚本的 apollo 连接，不使用 apollo 配置中心可跳过</li> 
 <li>Linux 启动 执行<span> </span><code>./boot.sh start</code><span> </span>命令启动服务，支持 start/stop/restart/status 命令</li> 
 <li>Windows 启动 执行<code>.\boot.cmd start</code><span> </span>命令启动服务，支持 start/stop/restart/status 命令</li> 
</ol> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">安装方式二：源码安装:</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>本地 clone 仓库上的最新代码，修改 application.yml 配置文件里配置中心、注册中心、redis (redis 配置需与管理后台一致) 的配置</li> 
 <li>在项目根目录 fizz-gateway-community 下执行 Maven 命令<span> </span><code>mvn clean package install -DskipTests=true</code></li> 
 <li>在项目目录 fizz-gateway-community/fizz-bootstrap 下执行 Maven 命令<span> </span><code>mvn clean package -DskipTests=true</code></li> 
 <li>进入 fizz-gateway-community/fizz-bootstrap/target/fizz-gateway-community 目录，执行<span> </span><code>./boot.sh start</code><span> </span>命令启动服务，支持 start/stop/restart/status 命令</li> 
</ol> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">安装方式三（v2.0.0 或以上版本）：docker:</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>下载对应版本的镜像：docker pull fizzgate/fizz-gateway-community:&#123;version&#125;</li> 
 <li>通过环境变量方式修改 redis 配置（其它配置同理）并运行镜像</li> 
</ol> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1"><span style="color:#6f42c1">docker</span></span> <span style="color:#032f62"><span style="color:#032f62">run --rm -d -p 8600:8600 \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">aggregate.redis.host=&#123;your redis host IP&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">aggregate.redis.port=&#123;your redis port&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">aggregate.redis.password=&#123;your redis password&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
-e </span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span><span style="color:#032f62"><span style="color:#032f62">aggregate.redis.database=&#123;your redis database&#125;</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62"><span style="color:#032f62">"</span></span></span></span><span style="color:#032f62"><span style="color:#032f62"> \
fizzgate/fizz-gateway-community:&#123;version&#125;</span></span></pre> 
</div> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">或通过映射目录方式使用外部配置文件和输出日志到宿主机，配置文件可从安装包或源码里获取，在宿主机创建 fizz-gateway-community/config 和 fizz-gateway-community/logs 目录，把 application.yml 和 log4j2-spring.xml 配置文件放置 config 下，在 fizz-gateway-community 目录下运行镜像</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#6f42c1"><span style="color:#6f42c1">cd</span></span></span> <span style="color:#032f62"><span style="color:#032f62">fizz-gateway-community</span></span>
<span style="color:#6f42c1"><span style="color:#6f42c1">docker</span></span> <span style="color:#032f62"><span style="color:#032f62">run --rm -d -p 8600:8600 \
-v </span></span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#032f62"><span style="color:#032f62">$PWD</span></span></span><span style="color:#032f62"><span style="color:#032f62">/config:/opt/fizz-gateway-community/config \
-v </span></span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#032f62"><span style="color:#032f62">$PWD</span></span></span><span style="color:#032f62"><span style="color:#032f62">/logs:/opt/fizz-gateway-community/logs fizzgate/fizz-gateway-community:&#123;version&#125;</span></span></pre> 
</div> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">最后访问网关，地址形式为：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F127.0.0.1%3A8600%2Fproxy%2F%255B%25E6%259C%258D%25E5%258A%25A1%25E5%2590%258D%255D%2F%255BAPI_Path%255D" target="_blank">http://127.0.0.1:8600/proxy/[服务名]/[API_Path]</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            