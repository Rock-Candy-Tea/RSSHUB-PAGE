
---
title: 'Fizz Gateway 1.5.0 发布，首个支持 Dubbo、gRPC 聚合的高性能网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9285'
author: 开源中国
comments: false
date: Wed, 24 Mar 2021 09:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9285'
---

<div>   
<div class="content">
                                                                                            <p>Fizz Gateway 1.5.0 发布，首个支持Dubbo、gRPC聚合的高性能网关。这一期版本更新支持了大家心心念的Dubbo，gRPC支持，支持的团队内部复杂协议的场景。另外优化支持HTTP协议，以及数据转换的支持。</p> 
<p><strong>1.5.0新特性：</strong><br> 支持Dubbo接口<br> 支持gRPC接口<br> 支持波浪号通配符透传数组数据<br> 支持自定义默认透传的请求头<br> 支持配置服务编排的content-type请求头<br> 支持自定义网关上下文<br> 支持自定义备用的验签请求头<br> 修复请求头区分大小写的问题</p> 
<p>Support Dubbo API<br> Support gRPC API<br> Support tilde wild card to transfer array data<br> Support custom default request headers while call backend api in aggregation<br> Support to config content-type header in aggregation<br> Support custom context-path<br> Support custom backup verification headers<br> Fixed the case sensitive problem of headers in stepContext</p> 
<h2 style="text-align:left">Fizz Gateway是什么？</h2> 
<p style="text-align:left">A Managerment API Gateway in Java . Fizz Gateway 是一个基于 Java开发的微服务网关，能够实现热服务编排、自动授权选择、线上服务脚本编码、在线测试、高性能路由、API审核管理、回调管理等目的，拥有强大的自定义插件系统可以自行扩展，并且提供友好的图形化配置界面，能够快速帮助企业进行API服务治理、减少中间层胶水代码以及降低编码投入、提高 API 服务的稳定性和安全性。</p> 
<h2 style="text-align:left">产品特性</h2> 
<ul> 
 <li>集群管理：Fizz网关节点是无状态的，配置信息自动同步，支持节点水平拓展和多集群部署。</li> 
 <li>服务编排：支持HTTP、Dubbo、gRPC协议热服务编排能力，支持前后端编码，随时随地更新API。</li> 
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
 <li>回调管理：支持回调的管理、订阅、重放、以及日志</li> 
</ul>
                                        </div>
                                      
</div>
            