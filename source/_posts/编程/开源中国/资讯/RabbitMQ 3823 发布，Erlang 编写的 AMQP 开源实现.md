
---
title: 'RabbitMQ 3.8.23 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1977'
author: 开源中国
comments: false
date: Sat, 25 Sep 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1977'
---

<div>   
<div class="content">
                                                                                            <p>RabbitMQ 3.8.23 现已发布，这是一个维护版本，官方建议所有用户都进行升级。<span style="background-color:#ffffff; color:#333333">RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，因此它也继承了这些优点。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Core Server</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Bug Fixes</p> 
<ul> 
 <li> <p><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rabbitmq.com%2Fnetworking.html%23proxy-protocol" target="_blank">Proxy protocol header </a>中传递的 TLS 信息现在附加到连接指标，就好像它是由非代理客户端提供的一样。</span></p> <p><span>GitHub </span><span style="background-color:#ffffff; color:#333333">issue</span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3175" target="_blank">#3175</a></span></p> </li> 
 <li> <p><span>Classic 队列关闭现在使用更高的 timeout（最多 10 分钟而不是 30 秒）。</span></p> <p><span>在具有许多队列（尤其是镜像队列）和许多消费者的环境中，这意味着节点重新启动后队列索引重建的机会现在大大降低。</span></p> <p><span style="background-color:#ffffff; color:#333333">GitHub issue</span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3409" target="_blank">#3409</a></span></p> </li> 
</ul> 
<p style="text-align:start"><strong>Shovel Plugin</strong></p> 
<p style="text-align:start">Bug Fixes</p> 
<ul> 
 <li> <p><span>在某些情况下，可以使用凭据记录 Shovel URIs。</span></p> <p><span>GitHub </span><span style="background-color:#ffffff; color:#333333">issue</span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3476" target="_blank">#3476</a></span></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>依赖升级</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>observer_cli 已从<code>1.6.2</code>升级为<code>1.7.1</code></li> 
</ul> 
<p style="text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.23" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.23</a></p>
                                        </div>
                                      
</div>
            