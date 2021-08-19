
---
title: '项目动态｜Apache Pulsar 2.7.3 版本介绍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9496'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 15:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9496'
---

<div>   
<div class="content">
                                                                                            <p>本文原文作者是 StreamNative 工程师丛搏、刘昱。译者刘梓霖，传智教育工程师。</p> 
<blockquote> 
 <h1>关于 Apache Pulsar</h1> 
 <p>Apache Pulsar 是 Apache 软件基金会顶级项目，是下一代云原生分布式消息流平台，集消息、存储、轻量化函数式计算为一体，采用计算与存储分离架构设计，支持多租户、持久化存储、多机房跨区域数据复制，具有强一致性、高吞吐、低延时及高可扩展性等流数据存储特性。GitHub 地址：http://github.com/apache/pulsar/</p> 
</blockquote> 
<p>近期，Apache Pulsar 社区发布了 Pulsar 2.7.3 版本！新版本涵盖 32 位贡献者提供的改进和错误修复，并提交了 79 次变更。</p> 
<p>版本亮点：</p> 
<p>•游标读取遵循调度字节率限制器的设置，不会再导致意外的结果。[1]•Ledger 滚动任务按预期执行。[2]</p> 
<p>本博客介绍了 2.7.3 版本最值得关注的进展，如需了解所有性能升级和 bug 修复的完整列表，请查阅 Pulsar 2.7.3 发布注记[3] 。</p> 
<h1>Bug 修复和性能升级</h1> 
<h2>Broker</h2> 
<p>PR-9826[4] : <strong>游标读取遵循调度字节率限制器的限制。</strong></p> 
<p><strong>问题：</strong>无论是命名空间还是主题策略在限制分发速率时都未考虑使用字节速率限制。</p> 
<p><strong>解决方案：</strong>修复了调度字节速率限制器设置的行为。游标读取会遵循此设置并且不会在导致意外的结果。</p> 
<p> </p> 
<p>PR-11226[5]: <strong>Ledger 滚动计划任务按照预期执行。</strong></p> 
<p><strong>问题：</strong>在此 PR 之前，ledger 在达到最大滚动时间之前执行滚动任务，导致 ledger 不能及时滚动。</p> 
<p><strong>解决方案：</strong>修复 ledger 滚动调度的时间，任务只能在 ledger 成功创建之后运行。</p> 
<p> </p> 
<p>PR-11136[6] : <strong>在重启 broker 时，主题级别的保留策略能正常工作。</strong></p> 
<p><strong>问题：</strong>在此 PR 之前，当为一个 topic 设置 topic 级保留策略然后重启 broker 时，该 topic 级别的保留策略不生效。</p> 
<p><strong>解决方案：</strong>修正了此策略的行为，使其在启动 <strong><code>policyCacheInitMap</code></strong> 后重放所有策略消息，并在重新启动 broker 时添加了保留策略检查测试。</p> 
<p> </p> 
<p>PR-10977[7]: <strong>调用 lastMessageId API 不会再导致内存泄露。</strong></p> 
<p><strong>问题：</strong>在此 PR 之前，调用<strong> <code>lastMessageId</code> </strong>API 时存在内存泄露，导致 broker 进程被 Kubernetes 停止。</p> 
<p><strong>解决方案：</strong>为<strong> <code>PersistentTopic.getLastMessageId</code> </strong>增加了缺失的 entry.release() 调用，以确保 broker 不会耗尽内存。</p> 
<p> </p> 
<p>PR-10594[8]: <strong>ZooKeeper 读取由 broker 缓存。</strong></p> 
<p><strong>问题：</strong>当执行管理操作以获取租户的命名空间时，是 ZooKeeper 使用在 ZooKeeper 客户端读取的， 而不是从broker 缓存中读取。</p> 
<p><strong>解决方案：</strong>修复 ZooKeeper 在为租户获取命名空间列表时的缓存问题。</p> 
<p> </p> 
<p>PR-10512[9]: <strong>调用</strong> <code>LeaderService.isLeader()</code> <strong>的监控线程不再被阻塞。</strong></p> 
<p><strong>问题：</strong>当<strong> <code>LeaderService</code> </strong>改变为 leadership 状态时，会被一个<strong> <code>synchronized</code> </strong>块锁定，这也阻止了其他线程调用<strong> <code>LeaderService.isLeader()</code> </strong>。</p> 
<p><strong>解决方案：</strong>通过修改<strong> <code>ClusterServiceCoordinator</code> </strong>和<strong> <code>WorkerStatsManager</code> </strong>以检查其是否来自<strong> <code>MembershipManager</code> </strong>的 leader ，修复了监控线程的死锁条件，使其不被 <strong><code>LeaderService.isLeader()</code> </strong>阻塞。</p> 
<p> </p> 
<p>PR-10414[10]: <code>hasMessageAvailable</code> <strong>可以成功读取消息。</strong></p> 
<p><strong>问题：</strong>因消息被<strong> <code>acknowledgmentsGroupingTracker</code> </strong>过滤，当<strong> <code>hasMessageAvailableAsync</code> </strong>返回<strong> <code>true</code> </strong>时无法读取消息。</p> 
<p><strong>解决方案：</strong>通过修改 <strong><code>acknowledgmentsGroupingTracker</code> </strong>过滤重复消息，并在之后连接打开时清理消息来修复竞争条件。</p> 
<h2>Proxy</h2> 
<p>PR-8048[11]：<strong>Proxy 支持自动创建分区 topic。</strong></p> 
<p><strong>问题：</strong>Proxy 因使用的是当前的 ZooKeeper 元数据而没有创建分区。</p> 
<p><strong>解决方案：</strong>通过从可用 broker 中选择和获取，而不是使用当前的 ZooKeeper 元数据来更改 proxy 以处理<strong> <code>PartitionMetadataRequest</code> </strong>。</p> 
<h2>Pulsar admin</h2> 
<p>PR-11140[12]：<strong>增加标识来表明是否在复制的集群上创建元数据路径。</strong></p> 
<p><strong>问题：</strong>在复制的命名空间上创建分区 topic时，没有在复制的集群上创建元数据路径 /<strong><code>managed-ledgers</code></strong>。</p> 
<p><strong>解决方案：</strong>增加了一个标识（createLocalTopicOnly），用来表明是否为复制集群中的分区 topic 创建元数据路径。</p> 
<p> </p> 
<p>PR-11131[13]：<strong>禁止为不存在的 topic 设置策略。</strong></p> 
<p><strong>问题：</strong>由于 topic 策略中存在重定向循环，用户可以为不存在的 topic 或者已分区的 topic 设置策略。</p> 
<p><strong>解决方案：</strong>此项修复为 topic 策略增加了一个权威标识，以避免重定向循环。用户无法为不存在的 topic 或单分区 topic 的分区设置 topic策略。如果你为 0 分区 topic 的分区设置策略，它会重定向到 broker 。</p> 
<p> </p> 
<p>PR-10806[14]：<strong>服务发现不再将 topic 硬编码为持久性。</strong></p> 
<p><strong>问题：</strong>当对分区的非持久 topic 使用查找服务发现时，就会返回 0 而不是分区数。Pulsar 客户端会以连接普通 topic 的方式尝试连接到该 topic。</p> 
<p><strong>解决方案：</strong>实现<strong> <code>topicName.getDomain().value()</code> </strong>而不是硬编码<strong> <code>persistent</code></strong>。现在用户可以成功地对一个分区的非持久 topic 使用服务发现。</p> 
<p> </p> 
<p>PR-10744[15]：<strong>其他连接器现在可以使用 Kinesis</strong> <code>Backoff</code> <strong>类</strong></p> 
<p><strong>问题：</strong>Pulsar 客户端实现项目中的 Kinesis sink 连接器 <strong><code>Backoff</code> </strong>类结合依赖 <strong><code>org.apache.pulsar:pulsar-client-original</code> </strong>增加了连接器的大小。</p> 
<p><strong>解决方案：</strong>在函数 io-core 项目中增加了一个新的类 <strong><code>Backoff</code> </strong>，以便 Kinesis sink 连接器和其他连接器可以使用此类。</p> 
<h2>客户端</h2> 
<p>PR-10506[16]：<strong>无法发送许可为零的 </strong><code>FLOW</code> <strong>请求。</strong></p> 
<p><strong>问题：</strong>当 broker 接收到一个零许可的 <strong><code>FLOW</code> </strong>请求时，会抛出异常并且关闭连接。这会引发频繁的重连，并导致重复或者乱序的消息。</p> 
<p><strong>解决方案：</strong>增加了一个在发送<strong> <code>FLOW</code> </strong>请求之前验证其许可的验证功能，如果请求是零许可，则不能发送 <strong><code>FLOW</code> </strong>请求。</p> 
<h2>函数和连接器</h2> 
<p>PR-10769[17] ：<strong>Kinesis sink 连接器确认成功的消息。</strong></p> 
<p><strong>问题：</strong>Kinesis sink 连接器在发送成功后没有确认消息。</p> 
<p><strong>解决方案：</strong>为 Kinesis sink 连接器增加了消息发送成功后的确认。</p> 
<h2>Docker</h2> 
<p>PR-10531[18] ：<strong>在使用 Kubernetes 运行时，Function 名称不能超过 52 个字符。</strong></p> 
<p><strong>问题：</strong>当使用 Kubernetes 运行时，如果提交的 function 长度有效（小于 55 个字符），就会创建一个无法产生 pod 的 StatefulSet。</p> 
<p><strong>解决方案</strong><strong>：</strong>将 Kubernetes 运行时的 function 名称的最大长度从 55 个字符改为 53 个字符。通过这一修复， function 名字的长度不能超过 52 个字符。</p> 
<h2>依赖</h2> 
<p>PR-10907[19]：<strong>启动 TLS 后，</strong><code>pulsar-admin</code><strong> 与 proxy 的连接稳定了。</strong></p> 
<p><strong>问题：</strong>因为 Jetty 9.4.39 中引入了 SSL 缓存的错误，<strong><code>pulsar-admin</code> </strong>在 TLS 连接中不稳定，，导致大型 function jar 包上传频繁失败。</p> 
<p><strong>解决方案：</strong>将 Jetty 升级到 9.4.42.v20210604，这样当启用 TLS 时，<strong><code>pulsar-admin</code> </strong>与 proxy 的连接是最稳定的。</p> 
<h1>参与其中</h1> 
<h2>新版本使用</h2> 
<p>欢迎大家下载[20]并使用新版本！如果在使用中遇到问题，可以通过提 issue[21] 或在微信群交流的方式抛出疑问并与社区交流。</p> 
<h2>加入 Apache Pulsar 社区</h2> 
<p>Pulsar 项目的成长来源于社区，也扎根于社区。一次次新版本的筹备与发布离不开社区伙伴们的贡献。你是否愿意成为其中的一员呢？</p> 
<p>参与开源，可以获得公司及社区内外的认可，结交来自各个领域、志同道合的小伙伴；同时也可以提高个人影响力，促进个人发展。参与开源不是码农的专属，社区、文档等各个方面都可以让大家发挥一技之长。</p> 
<p>作为全球性开源项目，截至目前，Apache Pulsar 已拥有 435 名贡献者、9.4K+ Star 、2.3 K+ Fork 。我们为大家提供了参与指南，欢迎越来越多的小伙伴助力 Apache Pulsar 项目的不断发展与前进。</p> 
<p>• Apache Pulsar 官方贡献指南[22] </p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUyMjkzMjA1Ng%3D%3D%26mid%3D2247488316%26idx%3D2%26sn%3D23bd1759ef2877145731028d0151dc0c%26scene%3D21%23wechat_redirect" target="_blank">• 加入 Apache Pulsar 志愿者大家庭</a></p> 
<blockquote> 
 <h1>译者信息</h1> 
 <p>Hi~ 我叫刘梓霖，一名会 code 的斜杠青年 ~</p> 
</blockquote> 
<h1>推荐阅读</h1> 
<p>•<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUyMjkzMjA1Ng%3D%3D%26mid%3D2247488586%26idx%3D1%26sn%3D599464b3394d15247f3da2fd364a642e%26chksm%3Df9c50e7dceb2876ba914234e98899a4ad350adec30e03000a065c4fb0fb607323ae492f0e72c%26scene%3D21%23wechat_redirect" target="_blank">Pulsar 2.8.0 新增特性概览：独占 Producer、事务等</a>•<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUyMjkzMjA1Ng%3D%3D%26mid%3D2247487181%26idx%3D1%26sn%3Db69cafbbefa2859b227ef3845efc3d77%26chksm%3Df9c514faceb29dec2eeaca322146887001382e6402992bb5723256f428625d1554971b001c65%26scene%3D21%23wechat_redirect" target="_blank">Apache Pulsar 2.7.1 版本正式发布！</a></p> 
<h4>引用链接</h4> 
<p><code>[1]</code> 游标读取遵循调度字节率限制器的设置，不会再导致意外的结果。: <em>https://github.com/apache/pulsar/pull/11249</em><br> <code>[2]</code> Ledger 滚动任务按预期执行。: <em>https://github.com/apache/pulsar/pull/11226</em><br> <code>[3]</code> Pulsar 2.7.3 发布注记: <em>https://pulsar.apache.org/en/release-notes/</em><br> <code>[4]</code> PR-9826: <em>https://github.com/apache/pulsar/pull/9826</em><br> <code>[5]</code> PR-11226: <em>https://github.com/apache/pulsar/pull/11226</em><br> <code>[6]</code> PR-11136: <em>https://github.com/apache/pulsar/pull/11136</em><br> <code>[7]</code> PR-10977: <em>https://github.com/apache/pulsar/pull/10977</em><br> <code>[8]</code> PR-10594: <em>https://github.com/apache/pulsar/pull/10594</em><br> <code>[9]</code> PR-10512: <em>https://github.com/apache/pulsar/pull/10512</em><br> <code>[10]</code> PR-10414: <em>https://github.com/apache/pulsar/pull/10414</em><br> <code>[11]</code> PR-8048: <em>https://github.com/apache/pulsar/pull/8048</em><br> <code>[12]</code> PR-11140: <em>https://github.com/apache/pulsar/pull/11140</em><br> <code>[13]</code> PR-11131: <em>https://github.com/apache/pulsar/pull/11131</em><br> <code>[14]</code> PR-10806: <em>https://github.com/apache/pulsar/pull/10806</em><br> <code>[15]</code> PR-10744: <em>https://github.com/apache/pulsar/pull/10744</em><br> <code>[16]</code> PR-10506: <em>https://github.com/apache/pulsar/pull/10506</em><br> <code>[17]</code> PR-10769: <em>https://github.com/apache/pulsar/pull/10769</em><br> <code>[18]</code> PR-10531: <em>https://github.com/apache/pulsar/pull/10531</em><br> <code>[19]</code> PR-10907: <em>https://github.com/apache/pulsar/pull/10907</em><br> <code>[20]</code> 下载: <em>https://pulsar.apache.org/en/download/</em><br> <code>[21]</code> 提 issue: <em>https://github.com/apache/pulsar/issues</em><br> <code>[22]</code> Apache Pulsar 官方贡献指南: <em>http://pulsar.apache.org/en/contributing/</em></p>
                                        </div>
                                      
</div>
            