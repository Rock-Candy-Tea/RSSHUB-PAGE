
---
title: 'Apache Flink 1.14.0 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ea34aeb86ea10766cc686ea47d73a8cd7c6.png'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 23:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ea34aeb86ea10766cc686ea47d73a8cd7c6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache Flink 1.14.0 现已发布，Apache Flink 是一个开源的流处理框架，适用于分布式、高性能的数据流应用，是 Apache 软件基金会最活跃项目前 5 名。此版本在 SQL API、更多连接器支持、检查点和 PyFlink 等领域带来了许多新功能和改进。</span></p> 
<h4><span style="background-color:#ffffff; color:#333333">统一的批处理和流处理体验</span></h4> 
<ul> 
 <li>检查点和有界流 
  <ul> 
   <li>通过 FLIP-147，Flink 现在支持任务完成后的检查点，并在有界流的末尾获取最终检查点，确保在作业结束之前提交所有接收器数据（类似于 stop-with-savepoint 的行为）。要激活此功能，请将 execution.checkpointing.checkpoints-after-tasks-finish.enabled: true 添加到配置中。</li> 
  </ul> </li> 
 <li>混合数据流和表/SQL 应用程序的批处理执行 
  <ul> 
   <li>在 Flink 1.14 中，有界批处理执行的 SQL/Table 程序可以将中间 Table 转换为 DataStream，应用一些 DataSteam API 操作，并将其转换回 Table。此外，Flink 构建了一个数据流 DAG，将声明式优化的 SQL 执行与批处理执行的 DataStream 逻辑混合在一起。</li> 
  </ul> </li> 
 <li>混合源 
  <ul> 
   <li>现在支持来自多个源的组合流，通过一个接一个地读取这些源，实现从一个源无缝切换到另一个源。比如从分层存储设置中读取流，就好像有一个跨所有层的流。混合源可以将其作为一个连续的逻辑流读取，从 S3 上的历史数据开始，过渡到 Kafka 中更新的数据。<img alt height="820" src="https://oscimg.oschina.net/oscnet/up-ea34aeb86ea10766cc686ea47d73a8cd7c6.png" width="2388" referrerpolicy="no-referrer"></li> 
  </ul> </li> 
</ul> 
<h4>操作改进</h4> 
<ul> 
 <li><span style="background-color:#ffffff; color:#182026">缓冲区的去浮动化</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#182026">Buffer Debloating 是 Fl​​ink 中的一项新技术，可以最大限度地减少检查点延迟和成本。它通过自动调整网络内存的使用来确保高吞吐量，同时最大限度地减少传输中的数据量。因此，Flink 现在可以为背压下的对齐检查点提供稳定且可预测的对齐时间，并且可以大大减少背压下未对齐检查点中存储的动态数据量。</span><img alt src="https://oscimg.oschina.net/oscnet/up-54bf322b7a80d8fb997702280479c001bb6.png" referrerpolicy="no-referrer"></li> 
  </ul> </li> 
 <li>细粒度资源管理 
  <ul> 
   <li>细粒度资源管理是一项高级新功能，可提高大型共享集群的资源利用率。通过细粒度的资源管理，TaskManager 插槽现在可以动态调整大小。转换和操作符可以指定资源配置文件（CPU 大小、内存池、磁盘空间），并由 Flink 的资源管理器和任务管理器将任务管理器总资源的特定部分切掉。<img alt height="544" src="https://oscimg.oschina.net/oscnet/up-7cde945a552a4bb626984750395cae6ffc4.png" width="1029" referrerpolicy="no-referrer"></li> 
  </ul> </li> 
</ul> 
<h4>连接器</h4> 
<ul> 
 <li>连接器指标 
  <ul> 
   <li>此版本中已对连接器的度量标准进行了标准化。社区将逐渐通过所有连接器提取指标然后在下一个版本中将它们重新设计到新的统一 API 上。</li> 
  </ul> </li> 
 <li><span style="background-color:#ffffff; color:#182026">脉冲式连接器</span> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#182026">在这个版本中，Flink 添加了 Apache Pulsar 连接器。Pulsar 连接器从 Pulsar 主题读取数据，并支持流和批处理两种执行模式。在事务功能的支持下（在 Pulsar 2.8.0 中引入），Pulsar 连接器提供了一次性传递语义，以确保消息只传递给消费者一次，即使生产者重试发送消息。该连接器当前支持 DataStream API，表 API/SQL 绑定预计将在未来版本中提供</span>​​​​​​​。​​​​​​​</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2021%2F09%2F29%2Frelease-1.14.0.html" target="_blank">更新公告</a>。 </p>
                                        </div>
                                      
</div>
            