
---
title: 'RabbitMQ 3.10.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3713'
author: 开源中国
comments: false
date: Thu, 02 Jun 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3713'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，RabbitMQ 也继承了这些优点。</p> 
<p>RabbitMQ 3.10.4 是一个维护版本，此版本至少需要 Erlang 23.2，并支持 Erlang 24 和 25 ，主要带来以下变更：</p> 
<h3><strong>核心服务器</strong></h3> 
<h4><strong>增强功能</strong></h4> 
<p>优化次要的仲裁队列。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F4873" target="_blank">#4873</a></p> 
<h4><strong>Bug修复</strong></h4> 
<ul> 
 <li><code>management.load_definitions</code> 选项已弃用，因此需要避免在仍使用它的的旧集群中播种默认用户，这可能会导致出现额外的用户、来宾或覆盖默认用户名：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F4904" target="_blank">#4904</a></li> 
 <li>修复在某些情况下，流可能会遇到异常，或获取陈旧的流位置数据。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F4898" target="_blank">#4898</a></li> 
 <li><code>rabbitmqctl set_log_level </code>对通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frabbitmq.com%2Flogging.html%23log-exchange" target="_blank"><code>amq.rabbitmq.log</code></a> 的日志记录没有任何影响。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F4891" target="_blank">#4891</a></li> 
</ul> 
<h3><strong>命令行工具</strong></h3> 
<h4><strong>错误修复</strong></h4> 
<ul> 
 <li><code>rabbitmq-diagnostics status</code> 更具弹性，即使可用磁盘空间监控在节点上反复失败（被禁用）也不会失败。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F4900" target="_blank">#4900</a></li> 
</ul> 
<h2><strong>依赖升级</strong></h2> 
<ul> 
 <li><code>ra</code>从升级<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Fra%2Fcompare%2Fv2.0.11...v2.0.13" target="_blank"><code>2.0.11</code>到<code>2.0.13</code></a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.10.4" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.10.4</a></p>
                                        </div>
                                      
</div>
            