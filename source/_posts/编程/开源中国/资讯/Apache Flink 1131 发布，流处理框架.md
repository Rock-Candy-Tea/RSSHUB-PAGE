
---
title: 'Apache Flink 1.13.1 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6238'
author: 开源中国
comments: false
date: Sat, 29 May 2021 06:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6238'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Flink 1.13.1 现已发布，这是 Apache Flink 1.13 系列的首个 bug 修复版本，包含 82 个修复和优化，因此官方强烈建议所有用户都升级到 1.13.1。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>修复在 TIMESTAMP_LTZ 列上声明 SOURCE_WATERMARK 时类型不匹配的问题</li> 
 <li>使结构化类型的字段在构造过程中更加宽松</li> 
 <li>启用对象重用时，AsyncWaitOperator 应深度复制 StreamElement</li> 
 <li>修复无法通过使用 kinesis 消费者的保存点停止流媒体工作的问题</li> 
 <li>修复 flink iceberg table map<string,string> 无法转换为数据流的问题</li> 
 <li>使用保存点停止，对于链接到 MultipleInputStreamTask 的源，drain 不会提前设置水印</li> 
 <li>修复当 SQL 中的 sum/count 和 avg 同时出现时，SplitAggregateRule 会出现异常的问题</li> 
 <li>作业完成后，不会删除 leader 和 leaderlatch 下的 Zookeeper 节点</li> 
 <li>修复 flink-sql-parser 模型类 ParserResource 缺少 ParserResource.properties 的问题</li> 
 <li>修复在 Web UI 中没有显示 Statebackend 和 CheckpointStorage 类型的问题</li> 
 <li>重构基于 TVF 窗口的一些接口，以提高可扩展性</li> 
 <li>从所有 jar 中筛选 maven 元数据</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2021%2F05%2F28%2Frelease-1.13.1.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            