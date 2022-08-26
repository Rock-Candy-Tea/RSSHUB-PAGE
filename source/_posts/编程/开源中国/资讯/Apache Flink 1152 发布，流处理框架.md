
---
title: 'Apache Flink 1.15.2 发布，流处理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7679'
author: 开源中国
comments: false
date: Fri, 26 Aug 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7679'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Apache Flink 1.15.2 现已发布，这是<span> </span>Flink 1.15 系列的第二个错误修复版本；此版本包括 30 个错误修复、漏洞修复和 Flink 1.15 相关的一些小改进。Apache Flink 是一个开源的流处理框架，适用于分布式、高性能的数据流应用。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">具体更新内容如下：</span></p> 
<p style="text-align:start"><strong>Bug</strong></p> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-25097" target="_blank">FLINK-25097</a> ] - 当过滤条件为布尔类型时，内联接的错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-26931" target="_blank">FLINK-26931</a> ] - Pulsar sink 的 producer 名称应该是唯一的</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-27399" target="_blank">FLINK-27399</a> ] - Pulsar 连接器未正确设置开始消耗位置</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-27570" target="_blank">FLINK-27570</a> ] - Checkpoint 路径错误不会导致作业停止</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-27794" target="_blank">FLINK-27794</a> ] - 使用 MysqlCatalog 从 MySQL 获取的主键不正确</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-27856" target="_blank">FLINK-27856</a> ] - 添加没有规范的 pod 模板会使作业管理器崩溃</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28027" target="_blank">FLINK-28027</a> ] - 将 Async Sink 的最大 flight messages 数初始化为低数以用于速率限制策略</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28057" target="_blank">FLINK-28057</a> ] - LD_PRELOAD 在 flink-docker 上被硬编码为 x64</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28226" target="_blank">FLINK-28226</a> ] - “运行 kubernetes pyflink 应用程序测试”在拉取图像时失败</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28239" target="_blank">FLINK-28239</a> ] - Table-Planner-Loader 无法访问 commons-math3</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28240" target="_blank">FLINK-28240</a> ] - 当 NetworkBufferPool 的总段数为 0 时，NettyShuffleMetricFactory#RequestedMemoryUsageMetric#getValue 可能会抛出 ArithmeticException</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28250" target="_blank">FLINK-28250</a> ] - exactly-once sink kafka 导致内存不足</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28269" target="_blank">FLINK-28269</a> ] - Kubernetes 测试失败，权限被拒绝</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28322" target="_blank">FLINK-28322</a> ] - DataStreamScanProvider 的新方法不兼容</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28357" target="_blank">FLINK-28357</a> ] - 恢复 Finished sources 时的 Watermark 问题</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28404" target="_blank">FLINK-28404</a> ] - 注解 @InjectClusterClient 与 RestClusterClient 不能正常工作</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28454" target="_blank">FLINK-28454</a> ] - 修复 KafkaSource 错误时间戳示例</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28577" target="_blank">FLINK-28577</a> ] - 1.15.1 web ui 控制台报告关于 checkpoint size 的错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28602" target="_blank">FLINK-28602</a> ] - StateChangeFsUploader 在启用压缩时无法正常关闭流</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28817" target="_blank">FLINK-28817</a> ] - 从 checkpoint 恢复时 HybridSource 中的 NullPointerException</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28835" target="_blank">FLINK-28835</a> ] - Savepoint 和 checkpoint 功能和限制表不正确</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28861" target="_blank">FLINK-28861</a> ] - Non-deterministic UID 生成可能会导致 restore 期间出现问题</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28880" target="_blank">FLINK-28880</a> ] - 修复 CEP 文档中关于循环模式的严格连续的错误结果</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28908" target="_blank">FLINK-28908</a> ] - 在 PyFlink 中，LIST 类型的编码器选择错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28978" target="_blank">FLINK-28978</a> ] - Kinesis 连接器不适用于新的 AWS 区域</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28994" target="_blank">FLINK-28994</a> ] - 为 Flink UI 启用 withCredentials</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Improvement</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-27199" target="_blank">FLINK-27199</a> ] - 将 Pulsar 升级到 2.10.0 以修复不稳定的 Pulsar 测试环境。</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-27865" target="_blank">FLINK-27865</a> ] - 添加在 Kafka SQL 连接器文档中配置 SASL 和 SSL 的指南和示例</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28094" target="_blank">FLINK-28094</a> ] - 升级 AWS SDK 以支持 ap-southeast-3</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28140" target="_blank">FLINK-28140</a> ] - 通过添加 Python 示例改进文档</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-28486" target="_blank">FLINK-28486</a> ] - [docs-zh] Flink FileSystem SQL Connector Doc 不正确</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflink.apache.org%2Fnews%2F2022%2F08%2F25%2Frelease-1.15.2.html" target="_blank">https://flink.apache.org/news/2022/08/25/release-1.15.2.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            