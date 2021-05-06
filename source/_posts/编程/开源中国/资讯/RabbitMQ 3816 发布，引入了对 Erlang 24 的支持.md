
---
title: 'RabbitMQ 3.8.16 发布，引入了对 Erlang 24 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4863'
author: 开源中国
comments: false
date: Thu, 06 May 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4863'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 3.8.16 已发布，RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</p> 
<h3><strong>Core Server</strong></h3> 
<p>Erlang 新版本支持：</p> 
<ul> 
 <li> <p>这个版本引入了对 Erlang 24 的支持，并放弃了对 Erlang 22 的支持。Erlang 24 为许多 RabbitMQ 安装和工作负载提供了显著的实际吞吐量改进，预计它将于 2021 年 5 月推出。</p> <p>同时，请参见配置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2Fwhich-erlang.html%23erlang-repositories" target="_blank">最新的 Erlang 版本</a>，以了解如何配置最新版本的 Erlang 23.3。</p> </li> 
</ul> 
<h3><strong>AWS Peer Discovery 插件</strong></h3> 
<p>错误修正</p> 
<ul> 
 <li>在 3.8.15 版本中，这个插件被无意中排除在发行版之外了，现在已经被添加回来了。</li> 
</ul> 
<h3>管理插件</h3> 
<p>增强</p> 
<ul> 
 <li>消息轮询的 HTTP API 端点在轮询超时的情况下泄露了它使用的临时连接。请注意，这个端点不建议在 QA 环境之外使用。</li> 
</ul> 
<h3>依赖升级</h3> 
<ul> 
 <li>Cuttlefish 已经从 2.6.0 升级到了 3.0.0；</li> 
 <li>Lager 已从 3.8.2 升级到 3.9.1。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.16" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.16</a></p>
                                        </div>
                                      
</div>
            