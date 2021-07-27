
---
title: 'RabbitMQ 3.9.0 发布，支持 Erlang 24 并引入 Streams 数据结构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=121'
author: 开源中国
comments: false
date: Tue, 27 Jul 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=121'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</p> 
<p>RabbitMQ 3.9.0 正式发布，该版本更新内容如下：</p> 
<h2>重点更新：</h2> 
<h3><strong>Streams</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Frabbitmq.com%2Fstreams.html" target="_blank">Streams</a> 是 RabbitMQ 中一种新的持久化和复制的数据结构（" queue 类型"），它是一种具有非破坏性消费者语义的 append-only 日志模型。</p> 
<p>它们可以作为常规 AMQP 0.9.1 队列使用，也可以通过新的二进制协议插件和相关客户端使用，Streams 可以实现以前不可能或不实际的消息传递模式。</p> 
<h3><strong>Erlang 24 支持</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.rabbitmq.com%2Fposts%2F2021%2F03%2Ferlang-24-support-roadmap%2F" target="_blank">Erlang 24</a> 为许多工作负载提供了 20%-50% 的吞吐量提升。支持最新的运行时版本还允许 RabbitMQ 用由运行时提供的库取代一些外部依赖。</p> 
<p>Erlang 24 现在默认用于社区 RabbitMQ Docker 镜像。</p> 
<h3><strong>Kubernetes</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2Fkubernetes%2Foperator%2Foperator-overview.html" target="_blank">RabbitMQ Cluster Operator</a> 可自动配置、管理和操作在 Kubernetes 上运行的 RabbitMQ 集群。该 Operator 不仅是针对 3.9 版本的，也可用于最新的 3.8.x 版本系列。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2Fkubernetes%2Foperator%2Foperator-overview.html%23topology-operator" target="_blank">Messaging Topology Operator</a> 使得将 RabbitMQ 资源（虚拟主机、用户、权限、拓扑结构、策略等）定义为 Kubernetes 对象成为可能。该 Operator 可用于 3.8.x 版本系列。</p> 
<h3><strong>用 JSON 记录</strong></h3> 
<p>从 Lager 切换到新的 Erlang Logger API 进行日志记录引入了一个 JSON 结构化日志的选项。</p> 
<h3><strong>Erlang/OTP 的兼容性说明</strong></h3> 
<p>此版本需要 Erlang 23.2 或更高版本，建议使用 Erlang 24。</p> 
<h3><strong>升级到 3.9</strong></h3> 
<p>RabbitMQ 3.9.0 节点可以与 <code>3.8.x</code> 节点一起运行， <code>3.9.x</code>的特定功能只有在集群中的所有节点升级到 3.9.0 或该系列中的任何其他补丁版本时才能实现。</p> 
<h3><strong>错误修复</strong></h3> 
<ul> 
 <li><code>powershell.exe</code> 现在可以在没有配置文件的情况下运行；</li> 
 <li>队列索引恢复现在可以在恢复过程中强制关闭节点后继续进行；</li> 
 <li>纠正 <code>num_acceptors.ssl</code> 应用的配置值不正确的问题；</li> 
 <li>纠正了如果在<code>rabbitmqctl add_vhost</code>命令中没有指定 <code>-description</code>， <code>-tags</code> 标志会被忽略的问题；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.9.0" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.0</a></p>
                                        </div>
                                      
</div>
            