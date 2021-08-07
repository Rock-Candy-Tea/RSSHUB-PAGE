
---
title: 'Apache Flink 1.13.2 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2104'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 09:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2104'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Flink 1.13.2 现已发布，这是 Apache Flink 1.13 系列的第二个错误修复版本，包括 127 个修复和小改进。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>ContinuousFileReaderOperator 不应在 close() 上关闭输出</li> 
 <li>HiveTableSourceITCase.testPartitionFilter 在 AZP 上失败</li> 
 <li>ParquetInputFormat 不应需要 Parquet 模式作为用户输入</li> 
 <li>应用程序模式在构建 PackagedProgram 时不设置配置</li> 
 <li>将所有 “Connection reset by peer” 异常包装为 RemoteTransportException</li> 
 <li>由于 ConcurrentModificationException，KafkaChangelogTableITCase.testKafkaCanalChangelogSource 失败</li> 
 <li>某些场景无法通过配置单元目录删除表</li> 
 <li>SequentialChannelStateReaderImpl 可能会回收缓冲区两次</li> 
 <li>在批处理模式下无法执行极长的 sql</li> 
 <li>在 flink-connector-kinesis 中升级 AWS SDK 以包含新区域 af-south-1</li> 
 <li>为 Python Table API 添加 TableResult.collect 的文档</li> 
 <li>支持模式注册表格式的 ssl 连接</li> 
 <li>实现 ParquetAvroInputFormat</li> 
 <li>记录状态访问的延迟跟踪指标</li> 
 <li>在对齐超时时保持通道阻塞</li> 
 <li>为 Kafka 新源添加文档</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2021%2F08%2F06%2Frelease-1.13.2.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            