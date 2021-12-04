
---
title: 'RabbitMQ 3.9.11 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3680'
author: 开源中国
comments: false
date: Sat, 04 Dec 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3680'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，RabbitMQ 也继承了这些优点。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ<span> </span><code>3.9.11</code><span> </span>是<span> </span><code>3.9.x</code><span> </span>系列的一个维护版本，此版本至少需要 Erlang 23.2，并支持 Erlang 24，主要变更如下：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">核心服务器（<strong>Core Server</strong>）</h2> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug修复</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>当启用 TLS 的侦听器无法停止时，它会记录其所有可能包含敏感值的设置。</li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3803" target="_blank">#3803</a> </p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>增强功能</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>仲裁队列在磁盘上以更紧凑的格式存储排队消息的命令（删除了一些派生数据）。</li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3804" target="_blank">#3804</a></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">在 AMQP 0-9-1 的响应中，客户端操作流时可能会返回一个“准备交付”的消息计数值，该值与流的首副本不同步。</span></li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3814" target="_blank">#3814</a></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>经典队列在消费者操作期间更改全局 QoS 的通道上更有效地交付。</li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3805" target="_blank">#3805</a> </p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>普罗米修斯插件（Prometheus Plugin）</strong></h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>增强功能</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>GET /metrics/detailed</code><span> </span>端点提供新的可选指标，这些指标是<strong>集群范围的</strong>，因此不能聚合。</li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3779" target="_blank">#3779</a> </p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>管理插件（Management Plugin）</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>页面上的帮助提示放错了位置。</li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3825" target="_blank">#3825</a> </p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>管理代理插件（Management Agent Plugin）</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>禁用插件将停止由队列、流、连接等定期执行的指标收集。</li> 
</ul> 
<p style="color:#000000; margin-left:40px; margin-right:0; text-align:start">GitHub 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3800" target="_blank">#3800</a> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.9.11" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.11</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            