
---
title: 'RabbitMQ 3.9.8 已发布，AMQP消息服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1209'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1209'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ 3.9.8 发布了，<span style="color:#333333">RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ 3.9.8 是 3.9.x 系列的一个维护版本，如果从 3.9.0 之前的版本升级，请先升级到 3.9 版本。此版本最少需要 Erlang 23.2，支持最新的 Erlang 24.1.2，主要更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">重点 bug 修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>如果发布到经典队列时用了强制性标志，<span style="color:#24292f">即使发布者没有确认，通道的内存使用也会无限增长。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3560" target="_blank">#3560</a></li> 
 <li>Rabbitmq-diagnostics 内存崩溃，无法读取连接<span style="color:#000000">读取器、写入器和通道</span>进程的内存。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3570" target="_blank">#3570</a></li> 
 <li><span style="color:#2e3033">修复了在某些环境中无法解析主机名的问题。现在，RabbitMQ 节点的主机名也会被发布，以便其他节点可以解析它们。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Fosiris%2Fissues%2F53" target="_blank"><span style="color:#2e3033"><span> </span> </span>#53</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Prometheus 插件增强</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">通过 GET /metrics/ 端公开更多数据。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3520" target="_blank">#3520</a></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Management 插件 bug 修复</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">修复了 rabbitmq-management-ui 中的客户端错误。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3545" target="_blank">#3545 </a></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">AWS Peer Discovery 插件增强</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">该插件现在会记录更多失败的 AWS API 请求的细节。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3579" target="_blank">#3579</a></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Web STOMP 插件增强</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">STOMP-over-WebSockets 连接现在可以从流中消费。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3509" target="_blank">#3509</a></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#000000"><strong>其他升级</strong></span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Osiris 升级到 1.2.2 。</span></p>
                                        </div>
                                      
</div>
            