
---
title: 'RabbitMQ 3.9.1 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=15'
author: 开源中国
comments: false
date: Sun, 01 Aug 2021 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=15'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</p> 
<p>RabbitMQ 3.9.1 正式发布，该版本更新内容如下：</p> 
<h3><strong>Core Server</strong></h3> 
<p>错误修正：</p> 
<ul> 
 <li>使用全局 QoS 预取的客户端（从 3.9.0 开始已废弃）在确认交付时遇到了一个异常；</li> 
 <li>改进了流协调器在某些情况下的弹性；</li> 
 <li>当主机名包含非 ASCII 字符时，节点无法启动；</li> 
</ul> 
<h3><strong>CLI 工具</strong></h3> 
<p>错误修复：</p> 
<ul> 
 <li>rabbitmq-diagnostics stream_status 在使用 --tracking 选项时出现异常而失败；</li> 
 <li>rabbitmq-diagnostics stream_status 使用了一个过时的文档指南链接；</li> 
</ul> 
<h3><strong>RabbitMQ Erlang</strong> 客户端</h3> 
<p>错误修复：</p> 
<ul> 
 <li>客户端的新版本再次发布到 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhex.pm%2F" target="_blank">Hex.pm</a>；</li> 
 <li>connection_timeout 被调整以避免出现混乱的警告；</li> 
 <li>纠正了直接连接 net tick 时间调整中的一个拼写错误；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.9.1" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.1</a></p>
                                        </div>
                                      
</div>
            