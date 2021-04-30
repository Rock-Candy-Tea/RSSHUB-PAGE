
---
title: 'Apache Flink 1.12.3 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5210'
author: 开源中国
comments: false
date: Fri, 30 Apr 2021 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5210'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Flink 1.12.3 现已发布，这是 Apache Flink 1.12 系列的 bug 修复版本，包含 73 个修复和优化，因此官方强烈建议所有用户都升级到 1.12.3。</p> 
<p><strong>优化</strong></p> 
<ul> 
 <li>在 Datadog 报告中添加柱状图支持</li> 
 <li>独立 K8s 文档现在会解释备用 JobManagers 的用法</li> 
 <li>优化打印 K8s 规格</li> 
 <li>删除 CheckpointConfig 中的冗余 tolerableCheckpointFailureNumber 设置</li> 
 <li>强化 JobMaster＃updateTaskExecutionState（）</li> 
 <li>删除用于 AZP 运行的 Kafka 连接器的控制台日志记录</li> 
 <li>进行早期检查以确保结果的长度与 Pandas UDF 的输入相同</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>修复 CoordinatorEventsExactlyOnceITCase.checkListContainsSequence 在 CI 上失败的问题</li> 
 <li>修复批处理作业由于网络堆栈中的异常而失败的问题</li> 
 <li>未对齐的检查点恢复可能会导致数据流损坏</li> 
 <li>HiveTableSink 在将 RowData 转换为 Row 时应复制记录</li> 
 <li>FailureRateRestartBackoffTimeStrategy 允许的重启次数少于配置的重启次数</li> 
 <li>无法读取位置路径包含逗号的配置单元表 / 分区</li> 
 <li>AvroFileFormatFactory 使用不可反序列化的 lambda 函数</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2021%2F04%2F29%2Frelease-1.12.3.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            