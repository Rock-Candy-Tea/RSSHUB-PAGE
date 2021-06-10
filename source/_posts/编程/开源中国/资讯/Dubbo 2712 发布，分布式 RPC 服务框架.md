
---
title: 'Dubbo 2.7.12 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6820'
author: 开源中国
comments: false
date: Thu, 10 Jun 2021 06:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6820'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Dubbo 2.7.12 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<p><strong>特性：</strong></p> 
<ul> 
 <li>Injvm 协议支持异步调用；</li> 
 <li>广播模式支持收集每个 Dubbo 提供商发送的服务响应；</li> 
 <li>增加 msgpack 序列化支持；</li> 
 <li>为 MetadataReportConfig 添加可配置的文件参数；</li> 
 <li>由 DubboReference 生成的实例支持 AOP；</li> 
 <li>支持以 JSON 格式发送通用请求；</li> 
 <li>增加一个新的 Router 类，用于向指定的 IP 和端口发出请求；</li> 
 <li>支持在提供商一方进行超时拦截；</li> 
 <li>支持忽略的网络接口；</li> 
 <li>支持 url 合并处理器扩展；</li> 
 <li>SSL 支持密码和协议；</li> 
</ul> 
<p><strong>Bug 修复：</strong></p> 
<ul> 
 <li>修复 ZookeeperServiceDiscovery#getInstances 不能处理 healthyOnly 的问题；</li> 
 <li>修复了使用 Gson 序列化会导致异常信息丢失的问题；</li> 
 <li>修复 url 被预期截断的问题；</li> 
 <li>当使用多个协议并有指定的端口时，服务不能被启动；</li> 
 <li>修复方法注释回调不工作的问题；</li> 
 <li>处理 TypeDefinition#properties，当它不是一个原始类型对象时；</li> 
 <li>修复：支持 Lazy 注释；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-2.7.12" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-2.7.12</a></p>
                                        </div>
                                      
</div>
            