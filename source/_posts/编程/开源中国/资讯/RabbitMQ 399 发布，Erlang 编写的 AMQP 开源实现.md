
---
title: 'RabbitMQ 3.9.9 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4646'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4646'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</p> 
<p>RabbitMQ 3.9.9 正式发布，该版本更新内容如下：</p> 
<h3>Core Server</h3> 
<p><strong>错误修复</strong></p> 
<ul> 
 <li>修正了一个问题：一个集群成员被重新启动时，节点监视器可能会产生一个错误的网络分区</li> 
 <li>消息存储弹性的改进</li> 
 <li>在选出新队列 Leader 的某些情况下，减少了日志噪音</li> 
 <li>队列 Leader 的重新平衡现在可以减少日志的记录了</li> 
</ul> 
<p><strong>增强</strong></p> 
<ul> 
 <li><code>cluster_formation.target_cluster_size_hint</code>是一个新的配置设置，可用于指定预期的初始集群大小。</li> 
</ul> 
<h3><strong>Prometheus 插件</strong></h3> 
<p><strong>增强</strong></p> 
<ul> 
 <li>预渲染 Prometheus 标签</li> 
</ul> 
<p><strong>错误修复</strong></p> 
<ul> 
 <li>支持 TLS 的普罗米修斯端点监听器端口在内部没有正确存储</li> 
</ul> 
<h3><strong>Management 插件</strong></h3> 
<p><strong>错误修正</strong></p> 
<ul> 
 <li>持续性的消息计数现在可以正确显示在各个队列页面上了</li> 
 <li>恢复与 IE 11的兼容性</li> 
</ul> 
<h3><strong>Consistent Hashing Exchange 插件</strong></h3> 
<p><strong>错误修正</strong></p> 
<ul> 
 <li>纠正了交换和队列之间重复绑定的删除问题</li> 
</ul> 
<h3><strong>依赖升级</strong></h3> 
<ul> 
 <li>Ra 升级至<code>2.0.2</code></li> 
 <li>Osiris 升级至<code>1.2.3</code></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.9.9" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.9</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            