
---
title: 'Fizz Gateway 2.2.0 版本，微服务编排支持灵活的流程控制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 01:17:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000">v2.2.0 Changelog:</span></p> 
<p><span style="color:#000000"><strong>主推功能：</strong></span></p> 
<p><span style="color:#000000">支持按appid和来源IP维度限流（精细化的限流手段，满足不同的业务场景）<br> 支持微服务编排灵活流程控制 ，支持条件判断组件和循环组件</span></p> 
<p><span style="color:#000000"><strong>修复功能：</strong></span></p> 
<p><span style="color:#000000">支持对HTTP请求头/Query参数/form-data配置多值<br> 支持配置引用值的默认值<br> 新增峰值QPS报表<br> 修复不记录取消的请求的访问日志问题<br> 修复把取消的请求当成异常请求的问题<br> 修复测试页面x-www-form-urlencoded请求头不能识别的问题<br> 优化多处提示语及更新插件示例代码</span></p> 
<p><span style="color:#000000">Support traffic limiting by appid and source IP dimensions<br> Support process control in aggregation<br> Support condition component and circle component<br> Support configuring multiple values for HTTP request headers /Query parameters /form-data<br> Support configuring default value for reference value<br> Add peak QPS report in homepage<br> Fix an access log issue where cancelled requests were not logged<br> Fix an issue where cancelled requests were treated as abnormal requests<br> Fix an issue where the x-www-form-urlencoded request header could not be recognized in test page<br> Optimize multiple prompts and update plug-in sample code</span></p> 
<h2 style="text-align:start"><span style="color:#000000">Fizz Gateway是什么？</span></h2> 
<p style="text-align:start"><span style="color:#000000">An Aggregation API Gateway in Java . Fizz Gateway 是一个基于 Java开发的微服务聚合网关，能够实现热服务编排聚合、自动授权选择、线上服务脚本编码、在线测试、高性能路由、API审核管理、回调管理等目的，拥有强大的自定义插件系统可以自行扩展，并且提供友好的图形化配置界面，能够快速帮助企业进行API服务治理、减少中间层胶水代码以及降低编码投入、提高 API 服务的稳定性和安全性。</span></p> 
<h2 style="text-align:start"><span style="color:#000000">演示环境（Demo）</span></h2> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2F" target="_blank"><span style="color:#000000">http://demo.fizzgate.com/</span></a></p> 
<p style="text-align:start"><span style="color:#000000">账号/密码:<code>admin</code>/<code>Aa123!</code></span></p> 
<p style="text-align:start"><span style="color:#000000">健康检查地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fadmin%2Fhealth" target="_blank"><span style="color:#000000">http://demo.fizzgate.com/admin/health</span></a><span style="color:#000000"> (线上版本请限制admin路径的外网访问)</span></p> 
<p style="text-align:start"><span style="color:#000000">API地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fproxy%2F%255B%25E6%259C%258D%25E5%258A%25A1%25E5%2590%258D%255D%2F%255BAPI_Path%255D" target="_blank"><span style="color:#000000">http://demo.fizzgate.com/proxy/[服务名]/[API_Path]</span></a></p> 
<h2 style="text-align:start"><span style="color:#000000">Fizz的设计</span></h2> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F184315%2F97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" target="_blank"><span style="color:#000000"><img src="https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" width="500" referrerpolicy="no-referrer"></span></a></p> 
<h2 style="text-align:start"><span style="color:#000000">Fizz典型应用场景</span></h2> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2Fwehotel%2Ffizz-gateway-community%2Fimg%2Fscene.png" target="_blank"><span style="color:#000000"><img src="https://raw.githubusercontent.com/wiki/wehotel/fizz-gateway-community/img/scene.png" width="90%" referrerpolicy="no-referrer"></span></a></p> 
<h2 style="text-align:start"><span style="color:#000000">产品特性</span></h2> 
<ul> 
 <li><span style="color:#000000">集群管理：Fizz网关节点是无状态的，配置信息自动同步，支持节点水平拓展和多集群部署。</span></li> 
 <li><span style="color:#000000">安全授权：支持内置的key-auth, JWT, basic-auth授权方式，并且可以方便控制。</span></li> 
 <li><span style="color:#000000">服务编排：支持HTTP、Dubbo、gRPC、Soap协议热服务编排能力，支持前后端编码，支持JSON/XML输出，随时随地更新API。</span></li> 
 <li><span style="color:#000000">负载均衡：支持round-robin负载均衡。</span></li> 
 <li><span style="color:#000000">服务发现：支持从Eureka或Nacos注册中心发现后端服务器。</span></li> 
 <li><span style="color:#000000">配置中心：支持接入apollo配置中心。</span></li> 
 <li><span style="color:#000000">HTTP反向代理：隐藏真实后端服务，支持 Rest API反向代理。</span></li> 
 <li><span style="color:#000000">访问策略：支持不同策略访问不同的API、配置不同的鉴权等。</span></li> 
 <li><span style="color:#000000">IP黑白名单：支持配置IP黑白名单。</span></li> 
 <li><span style="color:#000000">自定义插件：强大的插件机制支持自由扩展。</span></li> 
 <li><span style="color:#000000">可扩展：简单易用的插件机制方便扩展功能。</span></li> 
 <li><span style="color:#000000">高性能：性能在众多网关之中表现优异。</span></li> 
 <li><span style="color:#000000">版本控制：支持操作的发布和多次回滚。</span></li> 
 <li><span style="color:#000000">管理后台：通过管理后台界面对网关集群进行各项配置。</span></li> 
 <li><span style="color:#000000">回调管理：支持回调的管理、订阅、重放、以及日志。</span></li> 
 <li><span style="color:#000000">多级限流：细颗粒度的限流方式包含服务限流，接口限流，APP_ID限流，IP限流</span></li> 
</ul> 
<h2 style="text-align:start"><span style="color:#000000">基准测试</span></h2> 
<p style="text-align:start"><span style="color:#000000">我们将Fizz与市面上主要的网关产品进行比较，使用相同的环境和条件，测试对象均为单个节点。Mock接口模拟20ms时延，报文大小约2K。</span></p> 
<ul> 
 <li><span style="color:#000000">Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz * 4</span></li> 
 <li><span style="color:#000000">Linux version 3.10.0-957.21.3.el7.x86_64</span></li> 
 <li><span style="color:#000000">8G RAM</span></li> 
</ul> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th><span style="color:#000000">分类</span></th> 
   <th><span style="color:#000000">产品</span></th> 
   <th><span style="color:#000000">600并发<br> QPS</span></th> 
   <th><span style="color:#000000">600并发<br> 90% Latency(ms)</span></th> 
   <th><span style="color:#000000">1000并发<br> QPS</span></th> 
   <th><span style="color:#000000">1000并发<br> 90% Latency(ms)</span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><span style="color:#000000">后端服务</span></td> 
   <td><span style="color:#000000">直接访问后端服务</span></td> 
   <td><span style="color:#000000">23540</span></td> 
   <td><span style="color:#000000">32.19</span></td> 
   <td><span style="color:#000000">27325</span></td> 
   <td><span style="color:#000000">52.09</span></td> 
  </tr> 
  <tr> 
   <td><span style="color:#000000">流量网关</span></td> 
   <td><span style="color:#000000">kong<br> v2.4.1</span></td> 
   <td><span style="color:#000000">15662</span></td> 
   <td><span style="color:#000000">50.87</span></td> 
   <td><span style="color:#000000">17152</span></td> 
   <td><span style="color:#000000">84.3</span></td> 
  </tr> 
  <tr> 
   <td><span style="color:#000000">应用网关</span></td> 
   <td><span style="color:#000000">fizz-gateway-community<br> v2.0.0</span></td> 
   <td><span style="color:#000000">12206</span></td> 
   <td><span style="color:#000000">65.76</span></td> 
   <td><span style="color:#000000">12766</span></td> 
   <td><span style="color:#000000">100.34</span></td> 
  </tr> 
  <tr> 
   <td><span style="color:#000000">应用网关</span></td> 
   <td><span style="color:#000000">spring-cloud-gateway<br> v2.2.9</span></td> 
   <td><span style="color:#000000">11323</span></td> 
   <td><span style="color:#000000">68.57</span></td> 
   <td><span style="color:#000000">10472</span></td> 
   <td><span style="color:#000000">127.59</span></td> 
  </tr> 
  <tr> 
   <td><span style="color:#000000">应用网关</span></td> 
   <td><span style="color:#000000">shenyu<br> v2.3.0</span></td> 
   <td><span style="color:#000000">9284</span></td> 
   <td><span style="color:#000000">92.98</span></td> 
   <td><span style="color:#000000">9939</span></td> 
   <td><span style="color:#000000">148.61</span></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            