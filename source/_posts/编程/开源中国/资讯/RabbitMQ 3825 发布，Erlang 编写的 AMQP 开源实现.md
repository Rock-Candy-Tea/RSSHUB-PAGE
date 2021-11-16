
---
title: 'RabbitMQ 3.8.25 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1698'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1698'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，RabbitMQ 也继承了这些优点。 </span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ<span> </span><code>3.8.25</code><span> </span>是一个维护版本，建议所有用户升级到此版本。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>普罗米修斯插件（Prometheus Plugin）</strong></h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>增强功能<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F2653" target="_blank">#2653</a></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新的 Prometheus 警报指标：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>rabbitmq_alarms_file_descriptor_limit</code><span> </span>1|0</li> 
 <li><code>rabbitmq_alarms_free_disk_space_watermark</code><span> </span>1|0</li> 
 <li><code>rabbitmq_alarms_memory_used_watermark</code><span> </span>1|0</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">虽然有些警报具有集群范围的影响，但以上指标都是节点本地的。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">兼容性</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">如果从<span> </span><code>3.7.x</code><span> </span>发行版升级，先查看<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.0" target="_blank">3.8.0 发行说明</a>，以了解升级和兼容性说明。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">如果从<span> </span><code>3.6.x</code><span> </span>或以上版本升级，首先升级到<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.7.27" target="_blank"><code>3.7.27</code></a>，然后再升级到这个版本。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Erlang/OTP 兼容性</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本需要 Erlang 23.2，支持 Erlang 24。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            