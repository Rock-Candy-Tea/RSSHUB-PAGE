
---
title: 'RabbitMQ 3.9.12 发布，Erlang 编写的 AMQP 开源实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4938'
author: 开源中国
comments: false
date: Sat, 08 Jan 2022 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4938'
---

<div>   
<div class="content">
                                                                                            <p><span data-darkreader-inline-color style="--darkreader-inline-color:#e8e6e3; color:#000000">RabbitMQ 是一个 Advanced Message Queuing Protocol（AMQP）的开源实现，由以高性能、健壮以及可伸缩性出名的 Erlang 编写而成，RabbitMQ 也继承了这些优点。</span></p> 
<p>RabbitMQ <code>3.9.12</code> 是 <code>3.9.x</code>发布系列中的一个维护版本，带来如下变更：</p> 
<h2 style="margin-left:0.6em"><strong>核心服务器（Core Server）</strong></h2> 
<h4 style="margin-left:0.6em"><strong>Bug修复</strong></h4> 
<ul> 
 <li>修复 Windows 特有的<strong> </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferlang%2Fotp%2Fissues%2F5527">Erlang's <code>file:read_file/1</code></a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"> 泄露问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3936">#3936</a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">, </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3906">#3906 </a></li> 
 <li><code>log.file.rotation.date</code> 模式解析器现在支持更多值，并且在 RabbitMQ 3.7 和更早版本中更接近于 Lager 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3831" target="_blank">#3831</a></li> 
 <li>定义导入忽略了用户限制。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3458" target="_blank">#3458</a></li> 
 <li>某些情况下，流协调器可能会遇到异常。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3908" target="_blank">#3908</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">在节点关闭时，有时会无意地以错误级别记录已停止的应用程序。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3900" target="_blank">#3900</a></li> 
</ul> 
<h4 style="margin-left:0.6em"><strong>增强功能</strong></h4> 
<ul> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">AMQP 0-9-1 操作现在消耗更少的CPU周期。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3934">#3934</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">更高效的(多67%)用户添加和更新，包括定义导入期间。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3894" target="_blank">#3894</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">身份验证和授权后端异常可能会将用户提供的凭证泄露到节点日志中。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3903" target="_blank">#3903</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">请求一个不存在的流偏移量时，服务器将返回一个更合适的错误代码。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3783" target="_blank">#3783</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">由于一个不可用的 leader 而失败的流操作，现在使用一个新的错误代码，与流不存在的情况区分。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F3874" target="_blank">#3874</a></li> 
 <li>经典健康检查（<span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">classic health check</span>）资源密集程度较低（但与<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frabbitmq.com%2Fmonitoring.html%23health-checks">现代替代方案</a>相比仍然非常密集，因此不推荐使用）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3905" target="_blank">#3905</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">操作符和常规策略合并现在支持使用布尔值的键，operator 值覆盖常规策略值。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3880" target="_blank">#3880</a></li> 
 <li>Windows 的<span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">空闲磁盘空间监视的健壮性（</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">robustness）改进。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3895">#3895</a></li> 
 <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">定义文件中的未命名参数和策略将被视为无效而拒绝。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fissues%2F971" target="_blank">#971</a></li> 
</ul> 
<h3><strong>OAuth 2 插件</strong></h3> 
<h4><strong>增强功能</strong></h4> 
<p>HTTPS 客户端和 JWKS URL 的相关改进。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Fpull%2F3887" target="_blank">#3887</a></p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frabbitmq%2Frabbitmq-server%2Freleases%2Ftag%2Fv3.9.12" target="_blank">https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.12</a></p>
                                        </div>
                                      
</div>
            