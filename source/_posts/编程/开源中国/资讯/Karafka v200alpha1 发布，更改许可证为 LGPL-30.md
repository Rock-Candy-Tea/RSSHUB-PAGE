
---
title: 'Karafka v2.0.0.alpha1 发布，更改许可证为 LGPL-3.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8752'
author: 开源中国
comments: false
date: Tue, 01 Feb 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8752'
---

<div>   
<div class="content">
                                                                                            <p>Karafka v2.0.0.alpha1 现已发布。<span style="background-color:#ffffff; color:#333333">Krafka 是一个用于简化基于 Apache Kafka 的 Ruby 应用开发的框架，它允许开发者在使用异步 Kafka 消息时使用类似于标准 HTTP 约定（params 和 params_batch）的方法。Karafka 不仅可以处理传入的消息，而且还提供了用于构建接收和发送消息的复杂数据流应用程序的工具。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">此版本更新内容：</span></p> 
<ul> 
 <li>将许可证更改为<code>LGPL-3.0</code></li> 
 <li>引入 Pro subscription</li> 
 <li>从<code>ruby-kafka</code>切换到<code>librdkafka</code>作为底层驱动程序</li> 
 <li>引入贯穿整个服务器生命周期的全自动集成测试</li> 
 <li>将 WaterDrop 与自动配置继承紧密结合，并提供重新定义的选项</li> 
 <li>对并发作业消耗的多线程支持（在单独的主题和/或分区中）</li> 
 <li>引入订阅组概念以更好地管理资源</li> 
 <li>完全删除所有回调以支持 finalizer 方法 <code>#on_shutdown</code></li> 
 <li>提供<code>on_revoked</code>方法，以在主题撤销时采取行动的</li> 
 <li>移除单条消息消费模式，并提供文档说明如何自己轻松完成</li> 
 <li>提供同步和异步偏移管理，首选异步</li> 
 <li>通过<code>Rails::Railte</code>引入 Ruby on Rails 的无缝集成</li> 
 <li>更新<code>cli info</code>以反映<code>2.0</code>详细信息</li> 
 <li>移除 responders 以支持 WaterDrop<code>2.0</code>producer</li> 
 <li>删除 pidfiles 支持</li> 
 <li>删除 daemonization 支持</li> 
 <li>......</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Freleases%2Ftag%2Fv2.0.0.alpha1" target="_blank">https://github.com/karafka/karafka/releases/tag/v2.0.0.alpha1</a></p>
                                        </div>
                                      
</div>
            