
---
title: 'Fizz Gateway 2.2.3 发布，微服务编排流程组件更稳定'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202104/23101302_b6yA.png'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 13:18:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202104/23101302_b6yA.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><span style="color:#000000">v2.2.3</span></p> 
<p style="text-align:start"><span style="color:#000000">changelog:</span></p> 
<p style="text-align:start"><span style="color:#000000">修复不能导入导出用户的问题<br> 修复因未设置超时时间导致报错的问题<br> 修复循环组件因下一个循环对象为空时抛异常的问题<br> 修复fallback报文因没有默认content-type请求头不能解析的问题<br> 打印网关运行时异常日志<br> 添加上下文信息到网关运行时异常里方便后续排查</span></p> 
<p style="text-align:start"><span style="color:#000000">Fix the issue that users could not be imported or exported<br> Fix the issue that an exception was threw because the timeout was not set<br> Fix the issue that loop component will throw exception when the next item is null<br> Fix the issue that fallback json can not be parsed due to no default content-type header<br> Print fizz runtime exception log<br> Add step context to FizzRunTimeException for further investigation</span></p> 
<div style="text-align:start"> 
 <div> 
  <h2>软件简介</h2> 
 </div> 
 <div> 
  <div> 
   <div> 
    <div style="text-align:left"> 
     <p style="text-align:start"><span style="color:#000000">A Managerment API Gateway in Java . Fizz Gateway 是一个基于 Java开发的微服务网关，能够实现热服务编排、自动授权选择、线上服务脚本编码、在线测试、高性能路由、API审核管理、回调管理等目的，拥有强大的自定义插件系统可以自行扩展，并且提供友好的图形化配置界面，能够快速帮助企业进行API服务治理、减少中间层胶水代码以及降低编码投入、提高 API 服务的稳定性和安全性。</span></p> 
     <h2 style="text-align:start"><span style="color:#000000">演示环境（Demo）</span></h2> 
     <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2F" target="_blank"><span style="color:#000000">http://demo.fizzgate.com/</span></a></p> 
     <p style="text-align:start"><span style="color:#000000">账号/密码:<code>admin</code>/<code>Aa123!</code></span></p> 
     <p style="text-align:start"><span style="color:#000000">健康检查地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fadmin%2Fhealth" target="_blank"><span style="color:#000000">http://demo.fizzgate.com/admin/health</span></a><span style="color:#000000"> (线上版本请限制admin路径的外网访问)</span></p> 
     <p style="text-align:start"><span style="color:#000000">API地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fproxy%2F%255B%25E6%259C%258D%25E5%258A%25A1%25E5%2590%258D%255D%2F%255BAPI_Path%255D" target="_blank"><span style="color:#000000">http://demo.fizzgate.com/proxy/[服务名]/[API_Path]</span></a></p> 
     <h2 style="text-align:start"><span style="color:#000000">Fizz的设计</span></h2> 
     <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F184315%2F97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" target="_blank"><span style="color:#000000"><img src="https://static.oschina.net/uploads/img/202104/23101302_b6yA.png" width="500" referrerpolicy="no-referrer"></span></a></p> 
     <h2 style="text-align:start"><span style="color:#000000">产品特性</span></h2> 
     <ul> 
      <li><span style="color:#000000">集群管理：Fizz网关节点是无状态的，配置信息自动同步，支持节点水平拓展和多集群部署。</span></li> 
      <li><span style="color:#000000">服务编排：支持HTTP、Dubbo、gRPC协议热服务编排能力，支持前后端编码，随时随地更新API。</span></li> 
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
      <li><span style="color:#000000">回调管理：支持回调的管理、订阅、重放、以及日志</span></li> 
     </ul> 
     <h2 style="text-align:start"><span style="color:#000000">基准测试</span></h2> 
     <p style="text-align:start"><span style="color:#000000">我们将Fizz与Spring官方spring-cloud-gateway进行比较，使用相同的环境和条件，测试对象均为单个节点。</span></p> 
     <ul> 
      <li><span style="color:#000000">Intel(R) Xeon(R) CPU X5675 @ 3.07GHz * 4</span></li> 
      <li><span style="color:#000000">Linux version 3.10.0-327.el7.x86_64</span></li> 
      <li><span style="color:#000000">8G RAM</span></li> 
     </ul> 
     <table cellspacing="0" style="width:max-content"> 
      <thead> 
       <tr> 
        <th><span style="color:#000000">产品</span></th> 
        <th><span style="color:#000000">QPS</span></th> 
        <th><span style="color:#000000">90% Latency(ms)</span></th> 
       </tr> 
      </thead> 
      <tbody> 
       <tr> 
        <td style="border-color:#dddddd"><span style="color:#000000">直接访问后端服务</span></td> 
        <td style="border-color:#dddddd"><span style="color:#000000">9087.46</span></td> 
        <td style="border-color:#dddddd"><span style="color:#000000">10.76</span></td> 
       </tr> 
       <tr> 
        <td style="border-color:#dddddd"><span style="color:#000000">fizz-gateway</span></td> 
        <td style="border-color:#dddddd"><span style="color:#000000">5927.13</span></td> 
        <td style="border-color:#dddddd"><span style="color:#000000">19.86</span></td> 
       </tr> 
       <tr> 
        <td style="border-color:#dddddd"><span style="color:#000000">spring-cloud-gateway</span></td> 
        <td style="border-color:#dddddd"><span style="color:#000000">5044.04</span></td> 
        <td style="border-color:#dddddd"><span style="color:#000000">22.91</span></td> 
       </tr> 
      </tbody> 
     </table> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            