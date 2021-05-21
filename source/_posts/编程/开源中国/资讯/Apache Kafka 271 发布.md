
---
title: 'Apache Kafka 2.7.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9394'
author: 开源中国
comments: false
date: Fri, 21 May 2021 08:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9394'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Kafka 2.7.1 已发布，这是一个 bugfix 版本，<span style="color:#000000">其中包括来自 45 个 JIRA 的修复和改进，还修复了部分严重的错误。</span></p> 
<h2>改进</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10852" target="_blank">KAFKA-10852</a>] - 优化 AlterIsr 使用方式，不再被限制</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-12310" target="_blank">KAFKA-12310</a>] - 将 zookeeper 升级至 3.5.9</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-12400" target="_blank">KAFKA-12400</a>] - 升级 jetty 版本以修复 CVE-2020-27223</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-12409" target="_blank">KAFKA-12409</a>] - ReplicaManager 中的 Leaking gauge</li> 
</ul> 
<h2>Bugfix</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10021" target="_blank">KAFKA-10021</a>] - 当读取到配置日志的末端时，现在会检查 fetch.max.wait.ms 是否大于 worker.sync.timeout.ms</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10192" target="_blank">KAFKA-10192</a>] - Flaky test BlockingConnectorTest#testBlockInConnectorStop</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10340" target="_blank">KAFKA-10340</a>] - 修复尝试为不存在的 topic 生成记录而不是永久挂起时，源连接器没有报告错误的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10417" target="_blank">KAFKA-10417</a>] - 修复与 cogroup() 搭配使用的 suppress() 抛出 ClassCastException 的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10678" target="_blank">KAFKA-10678</a>] - 修复重新部署 Streams 应用程序会导致 rebalance 和任务迁移的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10705" target="_blank">KAFKA-10705</a>] - 避免使用 World Readable RocksDB</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-12193" target="_blank">KAFKA-12193</a> ]-客户端断开连接时重新解析 IP</li> 
 <li>……</li> 
</ul> 
<h2>Sub-task</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-10815" target="_blank">KAFKA-10815</a>] - 如果所有分区都经过验证，EosTestDriver#verifyAllTransactionFinished 应该会中断循环</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FKAFKA-12623" target="_blank">KAFKA-12623</a>] - 修复 2.7 中的 LICENSE</li> 
</ul> 
<p>Kafka 2.7.1 源代码或二进制文件下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkafka.apache.org%2Fdownloads%232.7.1" target="_blank">https://kafka.apache.org/downloads#2.7.1</a><br> release note：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.apache.org%2Fkafka%2F2.7.1%2FRELEASE_NOTES.html" target="_blank">https://downloads.apache.org/kafka/2.7.1/RELEASE_NOTES.html</a></p>
                                        </div>
                                      
</div>
            