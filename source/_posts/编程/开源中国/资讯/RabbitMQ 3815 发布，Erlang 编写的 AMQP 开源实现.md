
---
title: 'RabbitMQ 3.8.15 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3751'
author: 开源中国
comments: false
date: Tue, 04 May 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3751'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 3.8.15 已发布，RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</p> 
<h3>Core Server</h3> 
<p>Bug 修复：</p> 
<ul> 
 <li>在某些配置中，Quorum 队列没有像预期的那样频繁地保留快照，这导致没有有效积压队列的磁盘空间使用峰值大大增加；</li> 
 <li>Quorum 队列名称被无意中限制：虚拟主机和实际队列名称的长度被限制为 254 个字符。名字更长的 Quorum 队列未能被声明；</li> 
 <li>删除 Quorum 队列会留下它的一些内部指标数据；</li> 
 <li>客户端目标地址现在是根据代理协议设置获得的；</li> 
</ul> 
<p>增强：</p> 
<ul> 
 <li> <p>现在默认情况下，consume 消息但不确认消息的 Quorum 队列使用方将有 15 分钟的确认超时时间。如有必要，操作员可以增加超时时间;</p> <p>这样的使用方会延迟甚至阻止磁盘上的数据压缩，这可能会使一个节点的磁盘空间比预期的要早得多提前用完。</p> </li> 
 <li> <p>通道拦截器现在可以返回通道级别的异常。</p> </li> 
</ul> 
<h3>CLI 工具</h3> 
<p>Bug 修正：</p> 
<ul> 
 <li><code>rabbitmq-diagnostics status</code> 在格式化响应时可能会遇到节点异常，因为这些节点使用 advanced.config 配置了高 VM 内存水印。</li> 
 <li><code>rabbitmq-queues rebalance</code> 将不再挑选正在维护的节点作为新的队列领导位置候选。</li> 
</ul> 
<p>增强：</p> 
<ul> 
 <li><code>rabbitmq-diagnostics remote_shell</code> 是一个新的命令，可以打开一个远程 Erlang shell 到目标节点，这简化了运行中节点的故障排除。</li> 
 <li><code>rabbitmq-queues await_online_quorum_plus_one</code> 现在在单节点集群中是一个无用的选项，因为当只有一个节点时，该命令就没有意义了。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.15" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.15</a></p>
                                        </div>
                                      
</div>
            