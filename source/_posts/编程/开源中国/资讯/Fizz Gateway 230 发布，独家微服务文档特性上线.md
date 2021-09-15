
---
title: 'Fizz Gateway 2.3.0 发布，独家微服务文档特性上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://raw.githubusercontent.com/wiki/wehotel/fizz-gateway-community/img/icon-color.png'
author: 开源中国
comments: false
date: Wed, 15 Sep 2021 09:56:00 GMT
thumbnail: 'https://raw.githubusercontent.com/wiki/wehotel/fizz-gateway-community/img/icon-color.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <p>v2.3.0</p> 
  <p>changelog:</p> 
  <p>支持API文档管理<br> 支持配置公共函数<br> 支持对服务编排的步骤进行拖拽排序<br> 支持对服务编排的Query参数/请求头/form-data/x-www-form-urlencoded进行校验<br> 新增appid可访问的路由权限页面<br> 新增拒绝数图表<br> 新增开关来控制JSON序列化是否输出null字段<br> 新增插件分类，内置插件限制不能删除<br> 修复服务编排进行强制类型转换失败不抛出异常的问题<br> 修复组件导致后续步骤不执行的问题</p> 
  <p>Support API document management<br> Support configuration common functions<br> Support drag-and-drop sorting of steps in aggregation<br> Support validation of Query parameters/request headers /form-data/ x-www-form-urlencoded for service aggregation<br> Add page to manage route permission of appID<br> Add blocked requests chart in homepage<br> Add switch to control whether JSON serialization outputs null fields<br> Add plugin categories, Restrict built-in plugins cannot be deleted<br> Fix the issue that it will not throw exception when fail to cast<br> Fix the issue that component will causes subsequent steps not to be performed</p> 
  <p> </p> 
  <div> 
   <p style="color:#24292f"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.fizzgate.com%2F" target="_blank"><img src="https://raw.githubusercontent.com/wiki/wehotel/fizz-gateway-community/img/icon-color.png" width="70%" referrerpolicy="no-referrer"></a></p> 
   <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2F6b6bc5355bd5c21921580eb7fcfb2a88433e713c62dae09926cf1b7493ab8d6a%2F68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d322e332e302d626c75652e7376673f63616368655365636f6e64733d32353932303030" target="_blank"><img alt="Version" src="https://camo.githubusercontent.com/6b6bc5355bd5c21921580eb7fcfb2a88433e713c62dae09926cf1b7493ab8d6a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d322e332e302d626c75652e7376673f63616368655365636f6e64733d32353932303030" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.fizzgate.com%2Ffizz-gateway-community%2F" target="_blank"><img alt="Documentation" src="https://camo.githubusercontent.com/335378d3b5837f055d0c9bcab2850a8845250dbd39b91e91a7fee77b50a96cfb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63756d656e746174696f6e2d7965732d627269676874677265656e2e737667" referrerpolicy="no-referrer"><span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwehotel%2Ffizz-gateway-community%23" target="_blank"><img alt="License: GPL--3.0" src="https://camo.githubusercontent.com/d043e5ccecf2cd7dd15535c4f06bcb5bffd346e0876e141394e76fe14b321d57/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c2d2d332e302d79656c6c6f772e737667" referrerpolicy="no-referrer"><span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwehotel%2Ffizz-gateway-community%2Factions" target="_blank"><img alt="Java CI with Maven" src="https://github.com/wehotel/fizz-gateway-community/workflows/Java%20CI%20with%20Maven/badge.svg?branch=master" referrerpolicy="no-referrer"></a></p> 
   <ul> 
    <li><strong>最新QQ交流群</strong>: 512164278</li> 
   </ul> 
   <h2 style="text-align:start">Fizz Gateway是什么？</h2> 
   <p style="color:#24292f; text-align:start">An Aggregation API Gateway in Java . Fizz Gateway 是一个基于 Java开发的微服务聚合网关，能够实现热服务编排聚合、自动授权选择、线上服务脚本编码、在线测试、高性能路由、API审核管理、回调管理等目的，拥有强大的自定义插件系统可以自行扩展，并且提供友好的图形化配置界面，能够快速帮助企业进行API服务治理、减少中间层胶水代码以及降低编码投入、提高 API 服务的稳定性和安全性。</p> 
   <h2 style="text-align:start">演示环境（Demo）</h2> 
   <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2F" target="_blank">http://demo.fizzgate.com/</a></p> 
   <p style="color:#24292f; text-align:start">账号/密码:<code>admin</code>/<code>Aa123!</code></p> 
   <p style="color:#24292f; text-align:start">健康检查地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fadmin%2Fhealth" target="_blank">http://demo.fizzgate.com/admin/health</a><span> </span>(线上版本请限制admin路径的外网访问)</p> 
   <p style="color:#24292f; text-align:start">API地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.fizzgate.com%2Fproxy%2F%255B%25E6%259C%258D%25E5%258A%25A1%25E5%2590%258D%255D%2F%255BAPI_Path%255D" target="_blank">http://demo.fizzgate.com/proxy/[服务名]/[API_Path]</a></p> 
   <h2 style="text-align:start">Fizz的设计</h2> 
   <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F184315%2F97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" target="_blank"><img src="https://user-images.githubusercontent.com/184315/97130741-33a90d80-177d-11eb-8680-f589a36e44b3.png" width="500" referrerpolicy="no-referrer"></a></p> 
   <h2 style="text-align:start">Fizz典型应用场景</h2> 
   <p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2Fwehotel%2Ffizz-gateway-community%2Fimg%2Fscene.png" target="_blank"><img src="https://raw.githubusercontent.com/wiki/wehotel/fizz-gateway-community/img/scene.png" width="90%" referrerpolicy="no-referrer"></a></p> 
   <h2 style="text-align:start">产品特性</h2> 
   <ul> 
    <li>集群管理：Fizz网关节点是无状态的，配置信息自动同步，支持节点水平拓展和多集群部署。</li> 
    <li>安全授权：支持内置的key-auth, JWT, basic-auth授权方式，并且可以方便控制。</li> 
    <li>服务编排：支持HTTP、Dubbo、gRPC、Soap协议热服务编排能力，支持前后端编码，支持JSON/XML输出，随时随地更新API。</li> 
    <li>负载均衡：支持round-robin负载均衡。</li> 
    <li>服务发现：支持从Eureka或Nacos注册中心发现后端服务器。</li> 
    <li>配置中心：支持接入apollo配置中心。</li> 
    <li>HTTP反向代理：隐藏真实后端服务，支持 Rest API反向代理。</li> 
    <li>访问策略：支持不同策略访问不同的API、配置不同的鉴权等。</li> 
    <li>IP黑白名单：支持配置IP黑白名单。</li> 
    <li>自定义插件：强大的插件机制支持自由扩展。</li> 
    <li>可扩展：简单易用的插件机制方便扩展功能。</li> 
    <li>高性能：性能在众多网关之中表现优异。</li> 
    <li>版本控制：支持操作的发布和多次回滚。</li> 
    <li>管理后台：通过管理后台界面对网关集群进行各项配置。</li> 
    <li>回调管理：支持回调的管理、订阅、重放、以及日志。</li> 
    <li>多级限流：细颗粒度的限流方式包含服务限流，接口限流，APP_ID限流，IP限流</li> 
   </ul> 
   <h2 style="text-align:start">基准测试</h2> 
   <p style="color:#24292f; text-align:start">我们将Fizz与市面上主要的网关产品进行比较，使用相同的环境和条件，测试对象均为单个节点。Mock接口模拟20ms时延，报文大小约2K。</p> 
   <ul> 
    <li>Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz * 4</li> 
    <li>Linux version 3.10.0-957.21.3.el7.x86_64</li> 
    <li>8G RAM</li> 
   </ul> 
   <table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
    <thead> 
     <tr> 
      <th>分类</th> 
      <th>产品</th> 
      <th>600并发<br> QPS</th> 
      <th>600并发<br> 90% Latency(ms)</th> 
      <th>1000并发<br> QPS</th> 
      <th>1000并发<br> 90% Latency(ms)</th> 
     </tr> 
    </thead> 
    <tbody> 
     <tr> 
      <td style="border-style:solid; border-width:1px">后端服务</td> 
      <td style="border-style:solid; border-width:1px">直接访问后端服务</td> 
      <td style="border-style:solid; border-width:1px">23540</td> 
      <td style="border-style:solid; border-width:1px">32.19</td> 
      <td style="border-style:solid; border-width:1px">27325</td> 
      <td style="border-style:solid; border-width:1px">52.09</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">流量网关</td> 
      <td style="border-style:solid; border-width:1px">kong<br> v2.4.1</td> 
      <td style="border-style:solid; border-width:1px">15662</td> 
      <td style="border-style:solid; border-width:1px">50.87</td> 
      <td style="border-style:solid; border-width:1px">17152</td> 
      <td style="border-style:solid; border-width:1px">84.3</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">应用网关</td> 
      <td style="border-style:solid; border-width:1px">fizz-gateway-community<br> v2.0.0</td> 
      <td style="border-style:solid; border-width:1px">12206</td> 
      <td style="border-style:solid; border-width:1px">65.76</td> 
      <td style="border-style:solid; border-width:1px">12766</td> 
      <td style="border-style:solid; border-width:1px">100.34</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">应用网关</td> 
      <td style="border-style:solid; border-width:1px">spring-cloud-gateway<br> v2.2.9</td> 
      <td style="border-style:solid; border-width:1px">11323</td> 
      <td style="border-style:solid; border-width:1px">68.57</td> 
      <td style="border-style:solid; border-width:1px">10472</td> 
      <td style="border-style:solid; border-width:1px">127.59</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">应用网关</td> 
      <td style="border-style:solid; border-width:1px">shenyu<br> v2.3.0</td> 
      <td style="border-style:solid; border-width:1px">9284</td> 
      <td style="border-style:solid; border-width:1px">92.98</td> 
      <td style="border-style:solid; border-width:1px">9939</td> 
      <td style="border-style:solid; border-width:1px">148.61</td> 
     </tr> 
    </tbody> 
   </table> 
   <h2 style="text-align:start">版本对照</h2> 
   <ul> 
    <li> <p>Fizz-gateway-community： 社区版</p> </li> 
    <li> <p>Fizz-manager-professional：管理后台专业版（服务端）</p> </li> 
    <li> <p>Fizz-admin-professional：管理后台专业版（前端）</p> </li> 
   </ul> 
   <table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
    <thead> 
     <tr> 
      <th>Fizz-gateway-community</th> 
      <th>Fizz-manager-professional</th> 
      <th>Fizz-admin-professional</th> 
     </tr> 
    </thead> 
    <tbody> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.0.0</td> 
      <td style="border-style:solid; border-width:1px">v1.0.0</td> 
      <td style="border-style:solid; border-width:1px">v1.0.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.1.0</td> 
      <td style="border-style:solid; border-width:1px">v1.1.0</td> 
      <td style="border-style:solid; border-width:1px">v1.1.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.1.1</td> 
      <td style="border-style:solid; border-width:1px">v1.1.1</td> 
      <td style="border-style:solid; border-width:1px">v1.1.1</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.2.0</td> 
      <td style="border-style:solid; border-width:1px">v1.2.0</td> 
      <td style="border-style:solid; border-width:1px">v1.2.0</td> 
     </tr> 
    </tbody> 
   </table> 
   <p style="color:#24292f; text-align:start">从v1.3.0开始管理后台的前端和服务端合并成一个包</p> 
   <ul> 
    <li> <p>Fizz-gateway-community： 社区版</p> </li> 
    <li> <p>Fizz-manager-professional：管理后台</p> </li> 
   </ul> 
   <table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
    <thead> 
     <tr> 
      <th>Fizz-gateway-community</th> 
      <th>Fizz-manager-professional</th> 
     </tr> 
    </thead> 
    <tbody> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.3.0</td> 
      <td style="border-style:solid; border-width:1px">v1.3.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.4.0</td> 
      <td style="border-style:solid; border-width:1px">v1.4.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.4.1</td> 
      <td style="border-style:solid; border-width:1px">v1.4.1</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.5.0</td> 
      <td style="border-style:solid; border-width:1px">v1.5.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v1.5.1</td> 
      <td style="border-style:solid; border-width:1px">v1.5.1</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v2.0.0</td> 
      <td style="border-style:solid; border-width:1px">v2.0.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v2.1.0</td> 
      <td style="border-style:solid; border-width:1px">v2.1.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v2.2.0</td> 
      <td style="border-style:solid; border-width:1px">v2.2.0</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v2.2.1</td> 
      <td style="border-style:solid; border-width:1px">v2.2.1</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v2.2.3</td> 
      <td style="border-style:solid; border-width:1px">v2.2.3</td> 
     </tr> 
     <tr> 
      <td style="border-style:solid; border-width:1px">v2.3.0</td> 
      <td style="border-style:solid; border-width:1px">v2.3.0</td> 
     </tr> 
    </tbody> 
   </table> 
   <p style="color:#24292f; text-align:start">请根据社区版的版本下载对应的管理后台版本</p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            