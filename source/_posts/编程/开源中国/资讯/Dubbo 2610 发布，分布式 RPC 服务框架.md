
---
title: 'Dubbo 2.6.10 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6915'
author: 开源中国
comments: false
date: Sat, 22 May 2021 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6915'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Dubbo 2.6.10 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<p>此版本更新内容如下：</p> 
<ul> 
 <li>疏散不必要的实例初始化，创建 Resource cost</li> 
 <li>修复动态配置下 TPS 限制器不工作的问题</li> 
 <li>解决 lazy 模式下不共享共享连接的问题</li> 
 <li>修复 FailoverClusterInvoker 中的 methodName 和 retries 问题</li> 
 <li>修复 Dubbo qos 命令不适用于 offline provider 的问题</li> 
 <li>将 socks5 代理支持添加到 netty4 客户端</li> 
 <li>支持高版本的 Nacos</li> 
 <li>添加一些序列化检查</li> 
 <li>修复MonitorService 丢失 side = consumer 参数问题</li> 
 <li>修复 netty3 backlog</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-2.6.10" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-2.6.10</a></p>
                                        </div>
                                      
</div>
            