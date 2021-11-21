
---
title: 'RabbitMQ 发布 3.9.10 和  3.8.26 版本，修复 OAuth 2 插件 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7650'
author: 开源中国
comments: false
date: Sat, 20 Nov 2021 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7650'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ 在 11 月 20 日 发布了 3.9.10 和 3.8.26 版本<strong>，</strong>RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，RabbitMQ 也继承了这些优点。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">RabbitMQ 3.9.10</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RabbitMQ<span> </span><code>3.9.10</code><span> </span>是<span> </span><code>3.9.x</code><span> </span>系列的一个维护版本，此版本至少需要 Erlang 23.2，支持 Erlang 24。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Core Server</strong></h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug Fixes：</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现在<span style="color:#2e3033">流协调器对于快速声明和删除周期更具防御能力。</span><span style="color:#24292f">GitHub issue:<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3731" target="_blank">#33731631</a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">功能改进</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">现在暴露几个节点间通信监听器设置给<span> </span></span><code>rabbitmq.conf</code>：<span style="color:#24292f">GitHub issue:<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3739" target="_blank">#3739</a></li> 
</ul> 
<pre><code># this port range is used by default
distribution.listener.port_range.min = 25675
distribution.listener.port_range.max = 25675
# instead of listening on all interfaces
distribution.listener.interface = 192.168.0.1</code></pre> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">OAuth 2 插件</h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug Fixes</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在<span> </span><code>rabbitmq.conf</code><span> </span>中指定的签名键没有被正确翻译，导致权限检查时出现异常。GitHub issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3759" target="_blank">#3759</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">依赖升级</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Ra 更新到<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Fra%2Fcompare%2Fv2.0.2...v2.0.3" target="_blank">2.0.3 版本</a>。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>RabbitMQ 3.8.26</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">RabbitMQ 3.8.26 为维护版本，建议所有用户升级到该版本，</span>此版本需要 Erlang 23.2 并支持 Erlang 24。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">OAuth 2 插件更新</h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug Fixes</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在<span> </span><code>rabbitmq.conf</code><span> </span>中指定的签名键没有被正确翻译，导致权限检查时出现异常。GitHub issue:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3759" target="_blank">#3759</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases</a></p>
                                        </div>
                                      
</div>
            