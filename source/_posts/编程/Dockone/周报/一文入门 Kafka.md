
---
title: '一文入门 Kafka'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/d1847df4bf1937430ffac0b15d8d05ac.jpg'
author: Dockone
comments: false
date: 2021-05-30 12:26:53
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/d1847df4bf1937430ffac0b15d8d05ac.jpg'
---

<div>   
<br>Kafka 由 LinkedIn 公司推出的一个高吞吐的分布式消息系统，通俗的说就是一个基于发布和订阅的消息队列，官网地址：<a href="https://kafka.apache.org/intro" rel="nofollow" target="_blank">https://kafka.apache.org/intro</a><br>
<h3>应用场景</h3><ul><li>异步解构：在上下游没有强依赖的业务关系或针对单次请求不需要立刻处理的业务；</li><li>系统缓冲：有利于解决服务系统的吞吐量不一致的情况，尤其对处理速度较慢的服务来说起到缓冲作用；</li><li>消峰作用：对于短时间偶现的极端流量，对后端的服务可以启动保护作用；</li><li>数据流处理：集成 spark 做实事数据流处理。</li></ul><br>
<br><h3>Kafka 拓扑图（多副本机制）</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/d1847df4bf1937430ffac0b15d8d05ac.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/d1847df4bf1937430ffac0b15d8d05ac.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
由上图我们可以发现 Kafka 是分布式，同时对于每一个分区都存在多副本，同时整个集群的管理都通过 ZooKeeper 管理。<br>
<h3>Kafka 核心组件</h3><h4>broker</h4>Kafka 服务器，负责消息存储和转发；一 broker 就代表一个 Kafka 节点。<strong>一个 broker 可以包含多个 topic</strong>。<br>
<h4>topic</h4>消息类别，Kafka 按照 topic 来分类消息。<br>
<h4>partition</h4><ul><li>topic 的分区，一个 topic 可以包含多个 partition，topic 消息保存在各个 partition 上；由于一个 topic 能被分到多个分区上，给 Kafka 提供给了并行的处理能力，这也正是 Kafka 高吞吐的原因之一。</li><li>partition 物理上由多个 segment 文件组成，每个 segment 大小相等，<strong>顺序读写（这也是 Kafka 比较快的原因之一，不需要随机写）</strong>。每个 Segment 数据文件以该段中最小的 offset ，文件扩展名为 .log。当查找 offset 的 Message 的时候，通过二分查找快找到 Message 所处于的 Segment 中。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/2523870c8164fab2266fc1437c5bb5e1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/2523870c8164fab2266fc1437c5bb5e1.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>offset</h4><ul><li>消息在日志中的位置，可以理解是消息在 partition 上的偏移量，也是代表该消息的<strong>唯一序号</strong>。</li><li>同时也是主从之间的需要同步的信息。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/5bba5f823b733c55146ac6280b1aa696.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/5bba5f823b733c55146ac6280b1aa696.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Producer</h4>生产者，负责向 Kafka Broker 发消息的客户端。<br>
<h4>Consumer</h4>消息消者，负责消费 Kafka Broker 中的消息。<br>
<h4>Consumer Group</h4>消费者组，每个 Consumer 必须属于一个 group；（<strong>注意的是 一个分区只能由组内一个消费者消费，消费者组之间互不影响。</strong>）<br>
<h4>ZooKeeper</h4>管理 Kafka 集群，负责存储了集群 broker、topic、partition 等 meta 数据存储，同时也负责 broker 故障发现，partition leader 选举，负载均衡等功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/0f68834dde18c603244d117f50115f83.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/0f68834dde18c603244d117f50115f83.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>服务治理</h3>既然 Kafka 是分布式的发布/订阅系统，这样如果做的集群之间数据同步和一致性，Kafka 是不是肯定不会丢消息呢？以及宕机的时候如果进行 Leader 选举呢？<br>
<h4>数据同步</h4>在 Kafka 中的 Partition 有一个 leader 与多个 follower，producer 往某个 Partition 中写入数据是，只会往 leader 中写入数据，然后数据才会被复制进其他的 Replica 中。而每一个 follower 可以理解成一个消费者，定期去 leader 去拉去消息。而只有数据同步了后，kafka 才会给生产者返回一个 ACK 告知消息已经存储落地了。<br>
<br><strong>ISR</strong><br>
<br>在 Kafka 中，为了保证性能，Kafka 不会采用强一致性的方式来同步主从的数据。而是维护了一个：in-sync Replica 的列表，Leader 不需要等待所有 Follower 都完成同步，只要在 ISR 中的 Follower 完成数据同步就可以发送 ack 给生产者即可认为消息同步完成。同时如果发现 ISR 里面某一个 follower 落后太多的话，就会把它剔除。<br>
<br>具体流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/08189bdfe18cd471af512dc1df1ccfb0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/08189bdfe18cd471af512dc1df1ccfb0.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/c8e9414c80dd2b6ee2441d1610f5f0d9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/c8e9414c80dd2b6ee2441d1610f5f0d9.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/7611559b3bfed1182335d055f835db14.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/7611559b3bfed1182335d055f835db14.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/b26141a25587b1ac8f4545344293ac86.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/b26141a25587b1ac8f4545344293ac86.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>上述的做法并无法保证 Kafka 一定不丢消息。</strong>  虽然 Kafka 通过多副本机制中最大限度保证消息不会丢失，但是如果数据已经写入系统 page cache 中但是还没来得及刷入磁盘，此时突然机器宕机或者掉电，那消息自然而然的就会丢失。<br>
<br><strong>Kafka 故障恢复</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/f1f572b5643b47a804fdd9dc3740ef48.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/f1f572b5643b47a804fdd9dc3740ef48.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Kafka 通过 ZooKeeper 连坐集群的管理，所以这里的选举机制采用的是 Zab（ZooKeeper 使用）。<br>
<ul><li>生产者发生消息给 leader，这个时候 leader 完成数据存储，突然发生故障，没有给 producer 返回 ack；</li><li>通过 ZooKeeper 选举，其中一个 follower 成为 leader，这个时候 producer 重新请求新的 leader，并存储数据。</li></ul><br>
<br><h3>Kafka 为什么这么快</h3><h4>顺序写磁盘</h4>Kafka 采用了顺序写磁盘，而由于顺序写磁盘相对随机写，减少了寻地址的耗费时间。（在 Kafka 的每一个分区里面消息是有序的。<br>
<h4>Page Cache</h4>Kafka 在 OS 系统方面使用了 Page Cache 而不是我们平常所用的 Buffer。Page Cache 其实不陌生，也不是什么新鲜事物。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/047369ca460480a96b679e3b48953ef0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/047369ca460480a96b679e3b48953ef0.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
我们在 Linux 上查看内存的时候，经常可以看到 buff/cache，两者都是用来加速 IO 读写用的，而 cache 是作用于读，也就是说，磁盘的内容可以读到 cache 里面这样，应用程序读磁盘就非常快；而 buff 是作用于写，我们开发写磁盘都是，一般如果写入一个 buff 里面再 flush 就非常快。而 Kafka 正是把这两者发挥了极致：Kafka 虽然是 scala 写的，但是依旧在 Java 的虚拟机上运行，尽管如此，Kafka 它还是尽量避开了 JVM 的限制，它利用了 Page cache 来存储，这样躲开了数据在 JVM 因为 GC 而发生的 STW。另一方面也是 Page Cache 使得它实现了零拷贝，具体下面会讲。<br>
<h4>零拷贝</h4>无论是优秀的 Netty 还是其他优秀的 Java 框架，基本都在零拷贝减少了 CPU 的上下文切换和磁盘的 IO。当然 Kafka 也不例外。零拷贝的概念具体这里不作太详细的复述，大致的给大家讲一下这个概念。<br>
<br><strong>传统的一次应用程请求数据的过程</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/21760c1628abba066934120e93fbd3f5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/21760c1628abba066934120e93fbd3f5.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这里大致可以发传统的方式发生了 4 次拷贝，2 次 DMA 和 2 次 CPU，而 CPU 发生了 4 次的切换。（DMA 简单理解就是，在进行 I/O 设备和内存的数据传输的时候，数据搬运的工作全部交给 DMA 控制器，而 CPU 不再参与任何与数据搬运相关的事情）。<br>
<br><strong>零拷贝的方式</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/740c39bb25df172d81d616d81f154e8c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/740c39bb25df172d81d616d81f154e8c.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
通过优化我们可以发现，CPU 只发生了 2 次的上下文切换和 3 次数据拷贝。（Linux 系统提供了系统事故调用函数“sendfile()”，这样系统调用，可以直接把内核缓冲区里的数据拷贝到 socket 缓冲区里，不再拷贝到用户态）。<br>
<br><strong>分区分段</strong><br>
<br>我们上面也介绍过了，Kafka 采取了分区的模式，而每一个分区又对应到一个物理分段，而查找的时候可以根据二分查找快速定位。这样不仅提供了数据读的查询效率，也提供了并行操作的方式。<br>
<br><strong>数据压缩</strong><br>
<br>Kafka 对数据提供了：Gzip 和 Snappy 压缩协议等压缩协议，对消息结构体进行了压缩，一方面减少了带宽，也减少了数据传输的消耗。<br>
<h3>Kafka 安装</h3><h4>安装 JDK</h4>由于使用压缩包还需要自己配置环境变量，所以这里推荐直接用 yum 安装，熟悉查看目前 Java 的版本：<br>
<pre class="prettyprint">yum -y list Java* <br>
</pre><br>
安装你想要的版本，这里我是 1.8：<br>
<pre class="prettyprint">yum install java-1.8.0-openjdk-devel.x86_64 <br>
</pre><br>
查看是否安装成功：<br>
<pre class="prettyprint">Java -version  <br>
</pre><br>
<h4>安装 Zookeeper</h4>首先需要去官网下载安装包，然后解压：<br>
<pre class="prettyprint">tar -zxvf zookeeper-3.4.9.tar.gz <br>
</pre><br>
<strong>要做的就是将这个文件复制一份，并命名为：zoo.cfg，然后在 zoo.cfg 中修改自己的配置即可</strong><br>
<pre class="prettyprint">cp zoo_sample.cfg zoo.cfg  <br>
vim zoo.cfg  <br>
</pre><br>
主要配置解释如下：<br>
<pre class="prettyprint"># ZooKeeper内部的基本单位，单位是毫秒，这个表示一个tickTime为2000毫秒，在 ZooKeeper的其他配置中，都是基于 tickTime 来做换算的  <br>
tickTime=2000  <br>
# 集群中的 follower 服务器 (F) 与 leader 服务器 (L) 之间初始连接时能容忍的最多心跳数（tickTime 的数量）。  <br>
initLimit=10  <br>
<h1>syncLimit：集群中的follower服务器(F)与leader服务器(L)之间 请求和应答 之间能容忍的最多心跳数（tickTime的数量）</h1>syncLimit=5  <br>
# 数据存放文件夹，zookeeper运行过程中有两个数据需要存储，一个是快照数据（持久化数据）另一个是事务日志  <br>
dataDir=/tmp/zookeeper  <br>
## 客户端访问端口  <br>
clientPort=2181<br>
</pre><br>
配置环境变量：<br>
<pre class="prettyprint">vim ~/.bash_profile  <br>
export ZK=/usr/local/src/apache-zookeeper-3.7.0-bin  <br>
export PATH=$PATH:$ZK/bin  <br>
export PATH  <br>
// 启动  <br>
zkServer.sh start  <br>
</pre><br>
下面能看启动成功：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/193b5b33201ebe2840717f1945a7e558.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/193b5b33201ebe2840717f1945a7e558.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/c0b8927ea397210ecde61dde62015abc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/c0b8927ea397210ecde61dde62015abc.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>安装 Kafka</h4>下载 Kafka：<br>
<pre class="prettyprint">https://www.apache.org/dyn/closer.cgi?path=/kafka/2.8.0/kafka-2.8.0-src.tgz<br>
</pre><br>
安装 Kafka：<br>
<pre class="prettyprint">tar -xzvf kafka_2.12-2.0.0.tgz<br>
</pre><br>
配置环境变量：<br>
<pre class="prettyprint">export ZK=/usr/local/src/apache-zookeeper-3.7.0-bin  <br>
export PATH=$PATH:$ZK/bin  <br>
export KAFKA=/usr/local/src/kafka  <br>
export PATH=$PATH:$KAFKA/bin<br>
</pre><br>
启动 Kafka：<br>
<pre class="prettyprint">nohup kafka-server-start.sh 自己的配置文件路径/server.properties &<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/d6a55826e1505f96fac33a9781245780.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/d6a55826e1505f96fac33a9781245780.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
大功告成！<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/vzvmOXGcsX7rwY4J_--onw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/vzvmOXGcsX7rwY4J_--onw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            