
---
title: 'Apache Dubbo 3.0.1 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8359'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8359'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Dubbo 3.0.1 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<h3>优化</h3> 
<ul> 
 <li>将 NameMapping 重构为 Metadata，支持 MigrationRule 中的应用字段；</li> 
 <li>为扫描结果添加缓存；</li> 
 <li>改进方法和参数的配置覆盖；</li> 
 <li>支持 servlet 接管模式；</li> 
 <li>为 ServiceConfig 添加 ServiceListener；</li> 
 <li>改进方法回调；</li> 
 <li>Fix NPE in MetadataInfo (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8131" target="_blank">#8131</a>)</li> 
 <li>Fix customizer not changed (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8137" target="_blank">#8137</a>)</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>增加强制检查；</li> 
 <li>修复多注册表将破坏不可用的集群；</li> 
 <li>删除不必要的 toString 转换和默认启用检查；</li> 
 <li>忽略无效的 MetadataReportConfig；</li> 
 <li>修复 consumer 启动时的 NPE；</li> 
 <li>修复一些兼容的问题；</li> 
 <li>优化 Service 相关问题；</li> 
 <li>优化迁移和修复 ServiceDiscovery 的 reSubscribe；</li> 
 <li>修复 MetadataInfo 中的 NPE；</li> 
 <li>修复定制器未更改的问题；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.1" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.1</a></p>
                                        </div>
                                      
</div>
            