
---
title: 'Apache Flink 1.12.4 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5643'
author: 开源中国
comments: false
date: Tue, 25 May 2021 06:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5643'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Flink 1.12.4 现已发布，这是 Apache Flink 1.12 系列的 bug 修复版本，包含 21 个修复和优化，因此官方强烈建议所有用户都升级到 1.12.4。</p> 
<p><strong>优化</strong></p> 
<ul> 
 <li>在 DataStream API 文档中增加 10 分钟的阅读内容</li> 
 <li>为新的 Kafka 源添加端到端测试案例</li> 
 <li>在某些情况下，编译作业时遇到的异常的根本原因没有暴露给用户</li> 
 <li>重构 Python 依赖性管理文档</li> 
 <li>添加缺少的关于 PyFlink 的命令行选项的文档</li> 
 <li>过滤所有 jar 中的 maven 元数据</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>无法通过使用 kinesis 消费者的 savepoint 停止流媒体工作</li> 
 <li>修复一些与 KafkaSource 相关的bug</li> 
 <li>修复取消通过定时器输出数据时，缓冲池被破坏的问题</li> 
 <li>如果嵌套函数的参数数不正确，会出现误导性的异常信息</li> 
 <li>修复 UnalignedCheckpointITCase 在 zure 上挂起的问题</li> 
 <li>写入已经释放的缓冲区可能会在工作故障转移/取消期间造成数据损坏</li> 
 <li>为 Async IO 添加 numRecordsOut 指标</li> 
 <li>使用 scala api 来改变 PatternStream 的 TimeCharacteristic 是无效的</li> 
 <li>修复 flink-python jars 中的 LGPL-2.1 文件</li> 
 <li>修复 Japicmp 在 1.12 分支上失效的问题</li> 
 <li>修复 KubernetesLeaderElectionAndRetrievalITCase 出现故障的问题</li> 
 <li>修复 JobMaster 不能被重启的问题</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2021%2F05%2F21%2Frelease-1.12.4.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            