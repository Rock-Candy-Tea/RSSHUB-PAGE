
---
title: 'Apache SkyWalking 8.6.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1349'
author: 开源中国
comments: false
date: Sun, 13 Jun 2021 06:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1349'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache SkyWalking 8.6.0 现已发布，SkyWalking 是观察性分析平台和应用性能管理系统 (APM)，提供分布式追踪、服务网格遥测分析、度量聚合和可视化一体化解决方案，支持 Java, .Net Core, PHP, NodeJS, Go, Lua 语言探针，支持 Envoy + Istio 构建的 Service Mesh。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>添加 OpenSearch 作为存储选项</li> 
 <li>将 Kubernetes Java 客户端依赖升级到 11.0</li> 
 <li>修复 macOS 中的插件测试脚本错误</li> 
 <li>添加 trace_segment_ref_limit_per_span 配置机制，避免 OOM</li> 
 <li>提高 GlobalIdGenerator 的性能。</li> 
 <li>添加代理插件以支持 elasticsearch7</li> 
 <li>添加 jsonrpc4j 代理插件</li> 
 <li>支持多 skywalking 集群的新选项使用相同的kafka集群（plugin.kafka.namespace）</li> 
 <li>如果引导时连接 kafka 集群失败，则解析代理不会重试</li> 
 <li>在组件定义中添加 Seata。 Seata 插件托管在 Seata 项目上</li> 
 <li>扩展 Kafka 插件以正确跟踪直接分配主题分区的消费者。</li> 
 <li>支持 Kafka 消费者 2.8.0</li> 
 <li>支持将 SkyWalking 上下文打印到日志中</li> 
 <li>在 pulsar 插件中添加 MessageListener 增强</li> 
 <li>修复如果控制器类注解实现了接口，spring-mvc 设置错误端点名称的错误</li> 
 <li>添加可选的代理插件以支持 mybatis</li> 
 <li>添加 spring-cloud-gateway-3.x 可选插件</li> 
 <li>添加 okhttp-4.x 插件</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202106.mbox%2F%253CCANh7qnQvJ4j%2BJgjGUokWoRPj4B29B%3DEggozA6chQNtTYaYa2kg%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            