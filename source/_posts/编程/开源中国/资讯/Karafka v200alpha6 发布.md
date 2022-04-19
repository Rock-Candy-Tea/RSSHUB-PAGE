
---
title: 'Karafka v2.0.0.alpha6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9558'
author: 开源中国
comments: false
date: Tue, 19 Apr 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9558'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Karafka v2.0.0.alpha6 现已发布。<span style="background-color:#ffffff; color:#333333">Krafka 是一个用于简化基于 Apache Kafka 的 Ruby 应用开发的框架，它允许开发者在使用异步 Kafka 消息时使用类似于标准 HTTP 约定（params 和 params_batch）的方法。Karafka 不仅可以处理传入的消息，而且还提供了用于构建接收和发送消息的复杂数据流应用程序的工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">此版本更新内容：</span></p> 
<ul> 
 <li>修复了一个 BUG，在缺少启动文件和 Rails 时，railtie 出现 generic exception 而失败（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F818" target="_blank">#818</a>）</li> 
 <li>修复了在捆绑安装过程中，<span style="background-color:#ffffff; color:#24292f">并行</span>原始规范相互冲突的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F820" target="_blank">#820</a>)</li> 
 <li>替换<code>consumer.consume</code>为<code>consumer.consumed</code>事件，以符合行为规范</li> 
 <li>确保 offset committing 发生在<code>consumer.consumed</code>事件传播之前</li> 
 <li>修复未安装时失败的问题（只是一个依赖项）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F817" target="_blank">#817</a>）</li> 
 <li>从 rebalancing 时丢失的分区中 evict messages（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F825" target="_blank">#825</a>）</li> 
 <li>不要在失去的分区上运行<code>#revoked</code>，并在 rebalancing 时分配回来（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F825" target="_blank">#825</a>）</li> 
 <li>移除重新分配的分区在重新平衡时可能出现的重复（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F825" target="_blank">#825</a>）</li> 
 <li>优化集成测试套件额外消费者关闭过程（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Fissues%2F828" target="_blank">#828</a>）</li> 
 <li>优化消息驱逐和因缺乏消息而停止的轮询时的重复删除</li> 
 <li>添加静态组成员身份集成规范</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkarafka%2Fkarafka%2Freleases%2Ftag%2Fv2.0.0.alpha6" target="_blank">https://github.com/karafka/karafka/releases/tag/v2.0.0.alpha6</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            