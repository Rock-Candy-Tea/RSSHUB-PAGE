
---
title: 'Karafka v2.0.6 发布，基于 Apache Kafka 的应用程序开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9213'
author: 开源中国
comments: false
date: Sun, 04 Sep 2022 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9213'
---

<div>   
<div class="content">
                                                                                            <p>Karafka v2.0.6 现已发布。<span style="background-color:#ffffff; color:#333333">Krafka 是一个用于简化基于 Apache Kafka 的 Ruby 应用开发的框架，它允许开发者在使用异步 Kafka 消息时使用类似于标准 HTTP 约定（params 和 params_batch）的方法。Karafka 不仅可以处理传入的消息，而且还提供了用于构建接收和发送消息的复杂数据流应用程序的工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">此版本更新内容如下：</span></p> 
<ul> 
 <li>改善 client closing。</li> 
 <li>修复：多个 LRJ 主题同时获取会阻碍 LRJ 启动的能力（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F1002" target="_blank">#1002</a>）</li> 
 <li>引入 pre-enqueue 同步执行层以防止 LRJ 出现 starvation cases</li> 
 <li>在严重错误时关闭管理以防止分段故障</li> 
 <li>添加对手动订阅组管理的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F852" target="_blank">#852</a> / feature）</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">订阅组功能说明可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkarafka.io%2Fdocs%2FConcurrency-and-multithreading%2F%23consumer-groups-and-topics-structure" target="_blank">这里</a>找到。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Freleases%2Ftag%2Fv2.0.6" target="_blank">https://github.com/karafka/karafka/releases/tag/v2.0.6</a></p>
                                        </div>
                                      
</div>
            