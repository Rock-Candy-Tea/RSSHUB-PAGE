
---
title: 'RabbitMQ 3.8.27 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1687'
author: 开源中国
comments: false
date: Fri, 07 Jan 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1687'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，RabbitMQ 也继承了这些优点。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ<span> </span><code>3.8.27</code>是一个维护版本，主要带来以下变更：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">核心服务器<strong>（Core Server）</strong></h2> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug修复</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 Windows 特有的<strong><span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferlang%2Fotp%2Fissues%2F5527" target="_blank">Erlang's<span> </span><code>file:read_file/1</code></a><span style="color:#24292f"><span> </span>泄露问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3936" target="_blank">#3936</a><span style="color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3906" target="_blank">#3906 </a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>增强功能</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">AMQP 0-9-1 操作现在消耗更少的CPU周期。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3934" target="_blank">#3934</a></li> 
 <li>Windows 的<span style="color:#2e3033">空闲磁盘空间监视的健壮性（</span><span style="color:#24292f">robustness）改进。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3895" target="_blank">#3895</a></li> 
 <li>经典健康检查（<span style="color:#24292f">classic health check</span>）资源密集程度较低（但与<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frabbitmq.com%2Fmonitoring.html%23health-checks" target="_blank">现代替代方案</a>相比仍然非常密集，因此不推荐使用）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.8.27" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.8.27</a></p>
                                        </div>
                                      
</div>
            