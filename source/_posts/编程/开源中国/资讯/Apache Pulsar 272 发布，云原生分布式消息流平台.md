
---
title: 'Apache Pulsar 2.7.2 发布，云原生分布式消息流平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9025'
author: 开源中国
comments: false
date: Tue, 25 May 2021 06:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9025'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Pulsar 2.7.2 现已发布。Apache Pulsar 是 Apache 软件基金会顶级项目，是下一代云原生分布式消息流平台，集消息、存储、轻量化函数式计算为一体，支持多租户、持久化存储、多机房跨区域数据复制，具有强一致性、高吞吐以及低延时的高可扩展流数据存储特性。该系统源于 Yahoo，最初在 Yahoo 内部开发和部署，后于 2016 年由 Yahoo 开源并捐赠给 Apache 软件基金会进行孵化，2018 年成为 Apache 软件基金会顶级项目。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>Broker 
  <ul> 
   <li>修复当达到最大订阅数时无用的重试问题 </li> 
   <li>修复更新 lastLedgerCreationInitiationTimestamp 时的错误时间单位 </li> 
   <li>避免在 BK 问题的情况下出现垃圾日志</li> 
   <li>通过 startCursorPosition 大于 lastConfirmedEntry 来修复 NonDurableCursorImpl 的初始位置问题</li> 
   <li>修复 8115 有些分区在向 KEY_SHARED 订阅号添加额外的消费者后被卡住的问题</li> 
   <li>在主题内部统计中添加 underReplicate 状态</li> 
   <li>允许使用 bookkeeper_ 前缀配置 BookKeeper 所有 BK 客户端功能</li> 
   <li>修复 PersistentReplicator 中的 NPEs 和线程安全问题</li> 
   <li>修复非持久性订阅中 key_shared 子类型的消息不派发问题</li> 
   <li>使 PersistentDispatcherMultipleConsumers.readMoreEntries 同步化</li> 
   <li>修复在订阅没有模式的空主题时没有添加模式的问题 </li> 
   <li>修复删除命名空间时的 CPU 100% 问题</li> 
   <li>增加返回语句，在失败时提前退出 asyncMarkDelete</li> 
  </ul> </li> 
 <li>Bookie 
  <ul> 
   <li>如果没有定义 BOOKIE_GC，则返回到 PULSAR_GC</li> 
   <li>如果没有定义 BOOKIE_EXTRA_OPTS，则返回到 PULSAR_EXTRA_OPTS</li> 
  </ul> </li> 
 <li>Proxy 
  <ul> 
   <li>修复使用代理和前缀订阅认证模式时的授权错误</li> 
  </ul> </li> 
 <li>Pulsar Admin 
  <ul> 
   <li>为 pulsar rest api、pulsar-admin、pulsar-client 增加 get version 命令</li> 
  </ul> </li> 
 <li>Pulsar SQL 
  <ul> 
   <li>现在使用 pulsar 的 SQL 查询信息会出现 NoSuchLedger...</li> 
  </ul> </li> 
 <li>Docker 
  <ul> 
   <li>允许从源码 tarball 构建 DockerImage</li> 
   <li>修复 docker 独立镜像错误</li> 
   <li>禁止在启动脚本中打印 "跳过处理" 行</li> 
   <li>将 apply-config-from-env.py 注释为默认值</li> 
  </ul> </li> 
 <li>Client 
  <ul> 
   <li>[Java] 修复看似相等的 ClientConfigurationData 的对象最终不相等的问题</li> 
   <li>[Java] 修复 AutoConsumeSchema KeyValue 编码</li> 
   <li>[Java] 修复使用 KeyValue<GenericRecord, GenericRecord> 时的 OutOfMemoryError 错误</li> 
   <li>[Java] 修复增量纪元的并发问题</li> 
   <li>[Java] 允许 pulsar 客户端接收外部定时器</li> 
   <li>[Java] 处理为已关闭的生产者接收 Ack 时的 NPE 问题</li> 
   <li>[Java] 修复从字节数组反序列化时未设置批量大小的问题</li> 
   <li>[Java] 确保单一主题的消费者可以被关闭</li> 
   <li>[Java] 删除断开连接的消费者以允许自动发现</li> 
   <li>[Python] 支持 Python Avro 模式设置默认值</li> 
   <li>[Python] 修复模式中嵌套的 Map 或 Array 不工作的问题</li> 
   <li>[C++,Python] [PIP-60] 为 cpp 和 python 客户端增加 TLS SNI 支持</li> 
   <li>[C++] 修复 C++ 客户端无法在 Windows 上构建的问题</li> 
   <li>[C++] 修复暂停的零队列消费者仍然预取消息的问题</li> 
   <li>[C++] 修复从收到的消息 ID 获取主题名称时的分离故障</li> 
   <li>[C++] 修复 SinglePartition message router 总是选择相同分区的问题</li> 
   <li>[C++] 降低 ack-grouping 跟踪器的日志级别</li> 
   <li>[WebSocket 客户端] WebSocket 网址标记参数值优化</li> 
   <li>[WebSocket 客户端] 使浏览器客户端支持令牌验证</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fpulsar.apache.org%2Frelease-notes%2F" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            