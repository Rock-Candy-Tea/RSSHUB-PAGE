
---
title: 'Karafka v2.0.0.rc1 发布，基于 Apache Kafka 的应用程序开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1857'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1857'
---

<div>   
<div class="content">
                                                                                            <p>Karafka v2.0.0.rc1 现已发布。<span style="background-color:#ffffff; color:#333333">Krafka 是一个用于简化基于 Apache Kafka 的 Ruby 应用开发的框架，它允许开发者在使用异步 Kafka 消息时使用类似于标准 HTTP 约定（params 和 params_batch）的方法。Karafka 不仅可以处理传入的消息，而且还提供了用于构建接收和发送消息的复杂数据流应用程序的工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">此版本更新内容如下：</span></p> 
<ul> 
 <li>从侦听器内联代码中提取消费分区器。</li> 
 <li>引入虚拟分区器概念，用于并行处理来自单个主题分区的数据。</li> 
 <li>在轮询时发生 kafka 内部错误时提高稳定性。</li> 
 <li>修复了在 rebalance 时恢复 LRJ 分区的情况，在这种情况下，将在作业仍在运行时回收分区。</li> 
 <li>不要撤销丢失分区的 pauses。这将允许在 LRJ 作业完成时取消暂停回收的分区。</li> 
 <li>如果在 Karafka 服务器执行期间发生任何错误，默认情况下会失败集成（除非另行配置）。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Freleases%2Ftag%2Fv2.0.0.rc1" target="_blank">https://github.com/karafka/karafka/releases/tag/v2.0.0.rc1</a></p>
                                        </div>
                                      
</div>
            