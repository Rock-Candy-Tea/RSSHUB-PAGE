
---
title: 'RabbitMQ 3.8.19 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8454'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 06:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8454'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</p> 
<p>RabbitMQ 3.8.19 正式发布，该版本更新内容如下：</p> 
<h3><strong>Erlang/OTP 兼容性说明：</strong></h3> 
<ul> 
 <li>此版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2Fwhich-erlang.html" target="_blank">需要 Erlang 23.2</a> 并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.rabbitmq.com%2Fposts%2F2021%2F03%2Ferlang-24-support-roadmap%2F" target="_blank">支持 Erlang 24</a>；</li> 
</ul> 
<h3>Core Server：</h3> 
<p>增强：</p> 
<ul> 
 <li>节点启动时的绑定恢复现在更加有效，这意味着在有大量的队列和/或绑定的集群中，节点启动更快；</li> 
 <li>插件目录路径现在被重复利用了，所以如果一个目录被指定多次，节点也不会抱怨有重复的插件；</li> 
 <li>启动横幅和日志条目现在在 Windows 上更一致地使用路径分隔符；</li> 
</ul> 
<h3><strong>Shovel</strong> 插件：</h3> 
<p>错误修正：</p> 
<ul> 
 <li>当动态 Shovels 被启动时，该插件现在获得了一个分布式锁。这通常是没有必要的，但有助于避免重复的 Shovels 在集群形成过程中，通过在每个集群节点上导入定义文件而重复启动。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.19" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.19</a></p>
                                        </div>
                                      
</div>
            