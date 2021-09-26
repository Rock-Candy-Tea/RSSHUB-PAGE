
---
title: 'Kafka原理以及分区分配策略剖析'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/9accc565698a353480197e4e03fefff4.png'
author: Dockone
comments: false
date: 2021-09-26 01:53:11
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/9accc565698a353480197e4e03fefff4.png'
---

<div>   
<br><h3>简介</h3>Apache Kafka是一个分布式的流处理平台（分布式的基于发布/订阅模式的消息队列（Message Queue））。<br>
<br>流处理平台有以下3个特性：<br>
<ul><li>可以让你发布和订阅流式的记录。这一方面与消息队列或者企业消息系统类似。</li><li>可以储存流式的记录，并且有较好的容错性。</li><li>可以在流式记录产生时就进行处理。</li></ul><br>
<br><h4>消息队列的两种模式</h4><strong>点对点模式</strong><br>
<br>生产者将消息发送到Queue中，然后消费者从Queue中取出并且消费消息。消息被消费以后，Queue中不再存储，所以消费者不可能消费到已经被消费的消息。Queue支持存在多个消费者，但是对一个消息而言，只能被一个消费者消费。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/9accc565698a353480197e4e03fefff4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/9accc565698a353480197e4e03fefff4.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>发布/订阅模式</strong>  <br>
<br>生产者将消息发布到Topic中，同时可以有多个消费者订阅该消息。和点对点方式不同，发布到Topic的消息会被所有订阅者消费。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/d3bf3e2aa09d19019c8d6844601b8112.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/d3bf3e2aa09d19019c8d6844601b8112.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Kafka适合什么样的场景</h4>它可以用于两大类别的应用：<br>
<ul><li>构造实时流数据管道，它可以在系统或应用之间可靠地获取数据。（相当于Message Queue）。</li><li>构建实时流式应用程序，对这些流数据进行转换或者影响。（就是流处理，通过Kafka Stream Topic和Topic之间内部进行变化）。</li></ul><br>
<br>为了理解Kafka是如何做到以上所说的功能，从下面开始，我们将深入探索Kafka的特性。<br>
<br>首先是一些概念：<br>
<ul><li>Kafka作为一个集群，运行在一台或者多台服务器上。</li><li>Kafka通过Topic对存储的流数据进行分类。</li><li>每条记录中包含一个key，一个value和一个timestamp（时间戳）。</li></ul><br>
<br><h4>主题和分区</h4>Kafka的消息通过主题（Topic）进行分类，就好比是数据库的表，或者是文件系统里的文件夹。主题可以被分为若干个分区（Partition），一个分区就是一个提交日志。消息以追加的方式写入分区，然后以先进先出的顺序读取。注意，由于一个主题一般包含几个分区，因此无法在整个主题范围内保证消息的顺序，但可以保证消息在单个分区内的顺序。主题是逻辑上的概念，在物理上，一个主题是横跨多个服务器的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/c89667ee53b826bf0a1154862c9e5f6a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/c89667ee53b826bf0a1154862c9e5f6a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kafka集群保留所有发布的记录（无论他们是否已被消费），并通过一个可配置的参数——保留期限来控制（可以同时配置时间和消息大小，以较小的那个为准）。举个例子， 如果保留策略设置为2天，一条记录发布后两天内，可以随时被消费，两天过后这条记录会被抛弃并释放磁盘空间。<br>
<br>有时候我们需要增加分区的数量，比如为了扩展主题的容量、降低单个分区的吞吐量或者要在单个消费者组内运行更多的消费者（因为一个分区只能由消费者组里的一个消费者读取）。从消费者的角度来看，基于键的主题添加分区是很困难的，因为分区数量改变，键到分区的映射也会变化，所以对于基于键的主题来说，建议在一开始就设置好分区，避免以后对其进行调整。<br>
<br><strong>注意</strong>：不能减少分区的数量，因为如果删除了分区，分区里面的数据也一并删除了，导致数据不一致。如果一定要减少分区的数量，只能删除Topic重建。<br>
<h4>生产者和消费者</h4>生产者（发布者）创建消息，一般情况下，一个消息会被发布到一个特定的主题上。生产者在默认情况下把消息均衡的分布到主题的所有分区上，而并不关心特定消息会被写入哪个分区。不过，生产者也可以把消息直接写到指定的分区。这通常通过消息键和分区器来实现，分区器为键生成一个散列值，并将其映射到指定的分区上。生产者也可以自定义分区器，根据不同的业务规则将消息映射到分区。<br>
<br>消费者（订阅者）读取消息，消费者可以订阅一个或者多个主题，并按照消息生成的顺序读取它们。消费者通过检查消息的偏移量来区分已经读取过的消息。偏移量是一种元数据，它是一个不断递增的整数值，在创建消息时，Kafka会把它添加到消息里。在给定的分区里，每个消息的偏移量都是唯一的。消费者把每个分区最后读取的消息偏移量保存在ZooKeeper或者Kafka上，如果消费者关闭或者重启，它的读取状态不会丢失。<br>
<br>消费者是消费者组的一部分，也就是说，会有一个或者多个消费共同读取一个主题。消费者组保证每个分区只能被同一个组内的一个消费者使用。如果一个消费者失效，群组里的其他消费者可以接管失效消费者的工作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/f7763ac031d2a62350d55b1cd5538502.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/f7763ac031d2a62350d55b1cd5538502.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Broker和集群</h4>Broker：一个独立的Kafka服务器被称为Broker。Broker接收来自生产者的消息，为消息设置偏移量，并提交消息到磁盘保存。Broker为消费者提供服务，对读取分区的请求作出相应，返回已经提交到磁盘上的消息。<br>
<br>集群：交给同一个ZooKeeper集群来管理的Broker节点就组成了Kafka的集群。<br>
<br>Broker是集群的组成部分，每个集群都有一个Broker同时充当集群控制器的角色。控制器负责管理工作，包括将分区分配给Broker和监控Broker。在Broker中，一个分区从属于一个Broker，该Broker被称为分区的首领。一个分区可以分配给多个Broker（Topic设置了多个副本的时候），这时会发生分区复制。如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/331cbc81ce03db02ba9f7ec5b219e9d0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/331cbc81ce03db02ba9f7ec5b219e9d0.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Broker如何处理请求：Broker会在它所监听的每个端口上运行一个Acceptor线程，这个线程会创建一个连接并把它交给Processor线程去处理。Processor线程（也叫网络线程）的数量是可配的，Processor线程负责从客户端获取请求信息，把它们放进请求队列，然后从响应队列获取响应信息，并发送给客户端。如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/acfd3aa6305123ced5b1ae1b59a14ea1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/acfd3aa6305123ced5b1ae1b59a14ea1.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
生产请求和获取请求都必须发送给分区的首领副本（分区Leader）。如果Broker收到一个针对特定分区的请求，而该分区的首领在另外一个Broker上，那么发送请求的客户端会收到一个“非分区首领”的错误响应。Kafka客户端要自己负责把生产请求和获取请求发送到正确的Broker上。<br>
<br>客户端如何知道该往哪里发送请求呢？客户端使用了另外一种请求类型——元数据请求。这种请求包含了客户端感兴趣的主题列表，服务器的响应消息里指明了这些主题所包含的分区、每个分区都有哪些副本，以及哪个副本是首领。元数据请求可以发给任意一个Broker，因为所有的Broker都缓存了这些信息。客户端缓存这些元数据，并且会定时从Broker请求刷新这些信息。此外如果客户端收到“非首领”错误，它会在尝试重新发送请求之前，先刷新元数据。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/f6a3f2c53ecf16e212e068790b873f77.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/f6a3f2c53ecf16e212e068790b873f77.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Kafka基础架构</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/828ce668f730972f80da7864040b6c26.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/828ce668f730972f80da7864040b6c26.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Kafka架构深入</h3><h4>Kafka工作流程及文件存储机制</h4><strong>工作流程</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/b3d52517466d7cf1207104105a7419a0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/b3d52517466d7cf1207104105a7419a0.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kafka中消息是以Topic进行分类的，生产者生产消息，消费者消费消息，都是面向Topic的。<br>
<br>Topic是逻辑上的概念，而Partition（分区）是物理上的概念，每个Partition对应于一个log文件，该log文件中存储的就是Producer生产的数据。Producer生产的数据会被不断追加到该log文件末端，且每条数据都有自己的offset。消费者组中的每个消费者，都会实时记录自己消费到哪个offset，以便出错恢复时，从上次的位置继续消费。<br>
<br><strong>文件存储机制</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/a6bf0c8c51a0924d0fe24a5e9680a974.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/a6bf0c8c51a0924d0fe24a5e9680a974.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由于生产者生产的消息会不断追加到log文件末尾，为防止log文件过大导致数据定位效率低下，Kafka采取了分片和索引的机制，将每个Partition分为多个segment。（由log.segment.bytes决定，控制每个segment的大小，也可通过log.segment.ms控制，指定多长时间后日志片段会被关闭）每个segment对应两个文件——“.index”文件和“.log”文件。这些文件位于一个文件夹下，该文件夹的命名规则为：Topic名称+分区序号。例如：bing这个Topic有3个分区，则其对应的文件夹为：bing-0、bing-1和bing-2。<br>
<br>索引文件和日志文件命名规则：每个LogSegment都有一个基准偏移量，用来表示当前LogSegment中第一条消息的offset。偏移量是一个64位的长整形数，固定是20位数字，长度未达到，用0进行填补。如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/598dca298381a750963e0da410fb21aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/598dca298381a750963e0da410fb21aa.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
index和log文件以当前segment的第一条消息的offset命名。index文件记录的是数据文件的offset和对应的物理位置，正是有了这个index文件，才能对任一数据写入和查看拥有O(1)的复杂度，index文件的粒度可以通过参数log.index.interval.bytes来控制，默认是是每过4096字节记录一条index。下图为index文件和log文件的结构示意图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/ffb3ced67a735545d0cb7cb0128587c2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/ffb3ced67a735545d0cb7cb0128587c2.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
查找message的流程（比如要查找offset为170417的message）：<br>
<ol><li>首先用二分查找确定它是在哪个Segment文件中，其中0000000000000000000.index为最开始的文件，第二个文件为0000000000000170410.index（起始偏移为170410+1 = 170411），而第三个文件为0000000000000239430.index（起始偏移为239430+1 = 239431）。所以这个offset = 170417就落在第二个文件中。其他后续文件可以依此类推，以起始偏移量命名并排列这些文件，然后根据二分查找法就可以快速定位到具体文件位置。</li><li>用该offset减去索引文件的编号，即170417 - 170410 = 7，也用二分查找法找到索引文件中等于或者小于7的最大的那个编号。可以看出我们能够找到[4，476]这组数据，476即offset=170410 + 4 = 170414的消息在log文件中的偏移量。</li><li>打开数据文件（0000000000000170410.log），从位置为476的那个地方开始顺序扫描直到找到offset为170417的那条Message。</li></ol><br>
<br><strong>数据过期机制</strong>  <br>
<br>当日志片段大小达到log.segment.bytes指定的上限（默认是1GB）或者日志片段打开时长达到log.segment.ms时，当前日志片段就会被关闭，一个新的日志片段被打开。如果一个日志片段被关闭，就开始等待过期。当前正在写入的片段叫做活跃片段，活跃片段永远不会被删除，所以如果你要保留数据1天，但是片段包含5天的数据，那么这些数据就会被保留5天，因为片段被关闭之前，这些数据无法被删除。<br>
<h4>Kafka生产者</h4><strong>分区策略</strong><br>
<br>为什么要分区：<br>
<ol><li>多Partition分布式存储，利于集群数据的均衡。</li><li>并发读写，加快读写速度。</li><li>加快数据恢复的速率：当某台机器挂了，每个Topic仅需恢复一部分的数据，多机器并发。</li></ol><br>
<br>分区的原则：<br>
<ol><li>指明Partition的情况下，使用指定的Partition；</li><li>没有指明Partition，但是有key的情况下，将key的hash值与Topic的Partition数进行取余得到Partition值；</li><li>既没有指定Partition，也没有key的情况下，第一次调用时随机生成一个整数（后面每次调用在这个整数上自增），将这个值与Topic可用的Partition数取余得到Partition值，也就是常说的round-robin算法。</li></ol><br>
<br><pre class="prettyprint">public int partition(String topic, Object key, byte[] keyBytes, Object value, byte[] valueBytes, Cluster cluster) &#123;<br>
List<PartitionInfo> partitions = cluster.partitionsForTopic(topic);<br>
int numPartitions = partitions.size();<br>
if (keyBytes == null) &#123;<br>
    //key为空时，获取一个自增的计数，然后对分区做取模得到分区编号<br>
    int nextValue = nextValue(topic);<br>
    List<PartitionInfo> availablePartitions = cluster.availablePartitionsForTopic(topic);<br>
    if (availablePartitions.size() > 0) &#123;<br>
        int part = Utils.toPositive(nextValue) % availablePartitions.size();<br>
        return availablePartitions.get(part).partition();<br>
    &#125; else &#123;<br>
        // no partitions are available, give a non-available partition<br>
        return Utils.toPositive(nextValue) % numPartitions;<br>
    &#125;<br>
&#125; else &#123;<br>
    // hash the keyBytes to choose a partition<br>
    // key不为空时，通过key的hash对分区取模（疑问：为什么这里不像上面那样，使用availablePartitions呢？）<br>
    // 根据《Kafka权威指南》Page45理解：为了保证相同的键，总是能路由到固定的分区，如果使用可用分区，那么因为分区数变化，会导致相同的key，路由到不同分区<br>
    // 所以如果要使用key来映射分区，最好在创建主题的时候就把分区规划好<br>
    return Utils.toPositive(Utils.murmur2(keyBytes)) % numPartitions;<br>
&#125;<br>
&#125;<br>
<br>
private int nextValue(String topic) &#123;<br>
//为每个topic维护了一个AtomicInteger对象，每次获取时+1<br>
AtomicInteger counter = topicCounterMap.get(topic);<br>
if (null == counter) &#123;<br>
    counter = new AtomicInteger(ThreadLocalRandom.current().nextInt());<br>
    AtomicInteger currentCounter = topicCounterMap.putIfAbsent(topic, counter);<br>
    if (currentCounter != null) &#123;<br>
        counter = currentCounter;<br>
    &#125;<br>
&#125;<br>
return counter.getAndIncrement();<br>
&#125; <br>
</pre><br>
** 数据可靠性保证**<br>
<br>Kafka提供了哪些方面的保证：<br>
<ul><li>Kafka可以保证分区消息的顺序。如果使用同一个生产者往同一个分区写入消息，而且消息B在消息A之后写入，那么Kafka可以保证消息B的偏移量比消息A的偏移量大，而且消费者会先读取到消息A再读取消息B。</li><li>只有当消息被写入分区的所有副本时，它才被认为是“已提交”的。生产者可以选择接收不同类型的确认，比如在消息被完全提交时的确认、在消息被写入分区首领时的确认，或者在消息被发送到网络时的确认。</li><li>只要还有一个副本是活跃的，那么已经提交的信息就不会丢失。</li><li>消费者只能读取到已经提交的消息。</li></ul><br>
<br>复制：<br>
<br>Kafka的复制机制和分区的多副本架构是Kafka可靠性保证的核心。把消息写入多个副本可以使Kafka在发生奔溃时仍能保证消息的持久性。<br>
<br>Kafka的Topic被分成多个分区，分区是基本的数据块。每个分区可以有多个副本，其中一个是首领。所有事件都是发给首领副本，或者直接从首领副本读取事件。其他副本只需要与首领副本保持同步，并及时复制最新的事件。<br>
<br>Leader维护了一个动态的in-sync replica set（ISR），意为和Leader保持同步的follower集合。当ISR中的follower完成数据同步后，Leader就会发送ACK。如果follower长时间未向Leader同步数据，则该follower将被踢出ISR，该时间阈值由replica.lag.time.max.ms参数设定。Leader不可用时，将会从ISR中选举新的Leader。满足以下条件才能被认为是同步的：<br>
<ul><li>与ZooKeeper之间有一个活跃的会话，也就是说，它在过去的6s（可配置）内向ZooKeeper发送过心跳。</li><li>在过去的10s（可配置）内从首领那里获取过最新的数据。</li></ul><br>
<br>影响Kafka消息存储可靠性的配置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/17dc0074d63877388227e97c7d8d6e0c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/17dc0074d63877388227e97c7d8d6e0c.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
ACK应答机制：<br>
<br>对于某些不太重要的数据，对数据的可靠性要求不是很高，能够容忍数据的少量丢失，所以没有必要等ISR中的follower全部接收成功。所以Kafka提供了三种可靠性级别，用户可以根据对可靠性和延迟的要求进行权衡。ACK：<br>
<ul><li>0：Producer不等待Broker的ACK，这一操作提供了一个最低的延迟，Broker一接收到还没写入磁盘就已经返回，当Broker故障时可能丢失数据；</li><li>1：Producer等待Leader的ACK，Partition的Leader落盘成功后返回ACK，如果在follower同步成功之前Leader故障，那么将会丢失数据；</li><li>-1（all）：Producer等待Broker的ACK，Partition的Leader和ISR里的follower全部落盘成功后才返回ACK。但是如果在follower同步完成后，Broker发送ACK之前，Leader发生故障，那么会造成重复数据。（极端情况下也有可能丢数据：ISR中只有一个Leader时，相当于1的情况）。</li></ul><br>
<br>消费一致性保证：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/9e89572c24e6977622887aa4fbc42a22.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/9e89572c24e6977622887aa4fbc42a22.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
1、follower故障<br>
<br>follower发生故障后会被临时踢出ISR，待该follower恢复后，follower会读取本地磁盘记录的上次的HW，并将log文件高于HW的部分截取掉，从HW开始向Leader进行同步。<br>
<br>等该follower的LEO大于等于该Partition的HW，即follower追上Leader之后，就可以重新加入ISR了。<br>
<br>2、Leader故障<br>
<br>Leader发生故障后，会从ISR中选出一个新的Leader，之后为了保证多个副本之间的数据一致性，其余的follower会先将各自的log文件高于HW的部分截掉，然后从新的Leader同步数据。<br>
<br>注意：这只能保证副本之间的数据一致性，并不能保证数据不丢失或者不重复。<br>
<br><strong>消息发送流程</strong><br>
<br>Kafka的Producer发送消息采用的是异步发送的方式。在消息发送过程中，涉及到了两个线程——main线程和sender线程，以及一个线程共享变量——RecordAccumulator。main线程将消息发送给RecordAccumulator，sender线程不断从RecordAccumulator中拉取消息发送到Kafka Broker。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/6f3c136cd13eac4dbdf415803ee22a25.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/6f3c136cd13eac4dbdf415803ee22a25.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
为了提高效率，消息被分批次写入Kafka。批次就是一组消息，这些消息属于同一个主题和分区。（如果每一个消息都单独穿行于网络，会导致大量的网络开销，把消息分成批次传输可以减少网络开销。不过要在时间延迟和吞吐量之间做出权衡：批次越大，单位时间内处理的消息就越多，单个消息的传输时间就越长）。批次数据会被压缩，这样可以提升数据的传输和存储能力，但要做更多的计算处理。<br>
<br>相关参数：<br>
<ul><li>batch.size：只有数据积累到batch.size后，sender才会发送数据。（单位：字节，注意：不是消息个数）。</li><li>linger.ms：如果数据迟迟未达到batch.size，sender等待linger.ms之后也会发送数据。（单位：毫秒）。</li><li>client.id：该参数可以是任意字符串，服务器会用它来识别消息的来源，还可用用在日志和配额指标里。</li><li>max.in.flight.requests.per.connection：该参数指定了生产者在收到服务器响应之前可以发送多少个消息。它的值越高，就会占用越多的内存，不过也会提升吞吐量。把它设置为1可以保证消息时按发送的顺序写入服务器的，即使发生了重试。</li></ul><br>
<br><h4>Kafka消费者</h4><strong>消费方式</strong><br>
<br>consumer采用pull（拉）的模式从Broker中读取数据。<br>
<br>push（推）模式很难适应消费速率不同的消费者，因为消息发送速率是由Broker决定的。它的目标是尽可能以最快的速度传递消息，但是这样容易造成consumer来不及处理消息，典型的表现就是拒绝服务以及网络拥塞。而pull模式可以根据consumer的消费能力以适当的速率消费消息。<br>
<br>pull模式的不足之处是，如果Kafka没有数据，消费者可能会陷入循环中，一直返回空数据。针对这一点，Kafka的消费者在消费数据时会传入一个时长参数timeout，如果当前没有数据可消费，consumer会等待一段时间后再返回。<br>
<br><strong>分区分配策略</strong><br>
<br>一个consumer group中有多个consumer，一个Topic有多个Partition，所以必然会涉及到Partition的分配问题，即确定哪个Partition由哪个consumer来消费。Kafka提供了3种消费者分区分配策略：RangeAssigor、RoundRobinAssignor、StickyAssignor。<br>
<br>PartitionAssignor接口用于用户定义实现分区分配算法，以实现Consumer之间的分区分配。消费组的成员订阅它们感兴趣的Topic并将这种订阅关系传递给作为订阅组协调者的Broker。协调者选择其中的一个消费者来执行这个消费组的分区分配并将分配结果转发给消费组内所有的消费者。Kafka默认采用RangeAssignor的分配算法。<br>
<br>RangeAssignor：<br>
<br>RangeAssignor对每个Topic进行独立的分区分配。对于每一个Topic，首先对分区按照分区ID进行排序，然后订阅这个Topic的消费组的消费者再进行排序，之后尽量均衡的将分区分配给消费者。这里只能是尽量均衡，因为分区数可能无法被消费者数量整除，那么有一些消费者就会多分配到一些分区。分配示意图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/7d67555e1f3016caaadcc5bccff3477d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/7d67555e1f3016caaadcc5bccff3477d.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
分区分配的算法如下：<br>
<pre class="prettyprint">@Override<br>
public Map<String, List<TopicPartition>> assign(Map<String, Integer> partitionsPerTopic,<br>
                                            Map<String, Subscription> subscriptions) &#123;<br>
Map<String, List<String>> consumersPerTopic = consumersPerTopic(subscriptions);<br>
Map<String, List<TopicPartition>> assignment = new HashMap<>();<br>
for (String memberId : subscriptions.keySet())<br>
    assignment.put(memberId, new ArrayList<TopicPartition>());<br>
//for循环对订阅的多个Topic分别进行处理<br>
for (Map.Entry<String, List<String>> topicEntry : consumersPerTopic.entrySet()) &#123;<br>
    String topic = topicEntry.getKey();<br>
    List<String> consumersForTopic = topicEntry.getValue();<br>
<br>
    Integer numPartitionsForTopic = partitionsPerTopic.get(topic);<br>
    if (numPartitionsForTopic == null)<br>
        continue;<br>
    //对消费者进行排序<br>
    Collections.sort(consumersForTopic);<br>
    //计算平均每个消费者分配的分区数<br>
    int numPartitionsPerConsumer = numPartitionsForTopic / consumersForTopic.size();<br>
    //计算平均分配后多出的分区数<br>
    int consumersWithExtraPartition = numPartitionsForTopic % consumersForTopic.size();<br>
<br>
    List<TopicPartition> partitions = AbstractPartitionAssignor.partitions(topic, numPartitionsForTopic);<br>
    for (int i = 0, n = consumersForTopic.size(); i < n; i++) &#123;<br>
        //计算第i个消费者，分配分区的起始位置<br>
        int start = numPartitionsPerConsumer * i + Math.min(i, consumersWithExtraPartition);<br>
        //计算第i个消费者，分配到的分区数量<br>
        int length = numPartitionsPerConsumer + (i + 1 > consumersWithExtraPartition ? 0 : 1);<br>
        assignment.get(consumersForTopic.get(i)).addAll(partitions.subList(start, start + length));<br>
    &#125;<br>
&#125;<br>
return assignment;<br>
&#125; <br>
</pre><br>
这种分配方式明显的一个问题是随着消费者订阅的Topic的数量的增加，不均衡的问题会越来越严重，比如上图中4个分区3个消费者的场景，C0会多分配一个分区。如果此时再订阅一个分区数为4的Topic，那么C0又会比C1、C2多分配一个分区，这样C0总共就比C1、C2多分配两个分区了，而且随着Topic的增加，这个情况会越来越严重。分配结果：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/cff0c24d4d033667624aa9bfc487f832.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/cff0c24d4d033667624aa9bfc487f832.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
订阅2个Topic，每个Topic 4个分区，共3个Consumer：<br>
<ul><li>C0：[T0P0，T0P1，T1P0，T1P1]</li><li>C1：[T0P2，T1P2]</li><li>C2：[T0P3，T1P3]</li></ul><br>
<br>RoundRobinAssignor：<br>
<br>RoundRobinAssignor的分配策略是将消费组内订阅的所有Topic的分区及所有消费者进行排序后尽量均衡的分配（RangeAssignor是针对单个Topic的分区进行排序分配的）。如果消费组内，消费者订阅的Topic列表是相同的（每个消费者都订阅了相同的Topic），那么分配结果是尽量均衡的（消费者之间分配到的分区数的差值不会超过1）。如果订阅的Topic列表是不同的，那么分配结果是不保证“尽量均衡”的，因为某些消费者不参与一些Topic的分配。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/0327243a2905fc69e3fe136ff049f02c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/0327243a2905fc69e3fe136ff049f02c.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
以上两个Topic的情况，相比于之前RangeAssignor的分配策略，可以使分区分配的更均衡。不过考虑这种情况，假设有三个消费者分别为C0、C1、C2，有3个Topic T0、T1、T2，分别拥有1、2、3个分区，并且C0订阅T0，C1订阅T0和T1，C2订阅T0、T1、T2，那么RoundRobinAssignor的分配结果如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/f58751b70bb9b2bbbc5bd01e0ba5f572.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/f58751b70bb9b2bbbc5bd01e0ba5f572.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
看上去分配已经尽量的保证均衡了，不过可以发现C2承担了4个分区的消费而C1订阅了T1，是不是把T1P1交给C1消费能更加的均衡呢？<br>
<br>StickyAssignor：<br>
<br>StickyAssignor分区分配算法，目的是在执行一次新的分配时，能在上一次分配的结果的基础上，尽量少的调整分区分配的变动，节省因分区分配变化带来的开销。Sticky是“粘性的”，可以理解为分配结果是带“粘性的”——每一次分配变更相对上一次分配做最少的变动。其目标有两点：<br>
<ul><li>分区的分配尽量的均衡。</li><li>每一次重分配的结果尽量与上一次分配结果保持一致。</li></ul><br>
<br>当这两个目标发生冲突时，优先保证第一个目标。第一个目标是每个分配算法都尽量尝试去完成的，而第二个目标才真正体现出StickyAssignor特性的。<br>
<br>StickyAssignor算法比较复杂，下面举例来说明分配的效果（对比RoundRobinAssignor），前提条件：<br>
<ul><li>有4个Topic：T0、T1、T2、T3，每个Topic有2个分区。</li><li>有3个Consumer：C0、C1、C2，所有Consumer都订阅了这4个分区。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210924/f5c052074aca01282c945b99b4fc5f6b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210924/f5c052074aca01282c945b99b4fc5f6b.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上面红色的箭头代表的是有变动的分区分配，可以看出，StickyAssignor的分配策略，变动较小。<br>
<br><strong>offset的维护</strong><br>
<br>由于Consumer在消费过程中可能会出现断电宕机等故障，Consumer恢复后，需要从故障前的位置继续消费，所以Consumer需要实时记录自己消费到哪个位置，以便故障恢复后继续消费。Kafka 0.9版本之前，Consumer默认将offset保存在ZooKeeper中，从0.9版本开始，Consumer默认将offset保存在Kafka一个内置的名字叫_consumeroffsets的topic中。默认是无法读取的，可以通过设置consumer.properties中的exclude.internal.topics=false来读取。<br>
<br><strong>Kafka高效读写数据（了解）</strong><br>
<br>顺序写磁盘： <br>
<br>Kafka的Producer生产数据，要写入到log文件中，写的过程是一直追加到文件末端，为顺序写。数据表明，同样的磁盘，顺序写能到600M/s，而随机写只有100K/s。这与磁盘的机械结构有关，顺序写之所以快，是因为其省去了大量磁头寻址的时间。<br>
<br>零拷贝技术：<br>
<br>零拷贝主要的任务就是避免CPU将数据从一块存储拷贝到另外一块存储，主要就是利用各种零拷贝技术，避免让CPU做大量的数据拷贝任务，减少不必要的拷贝，或者让别的组件来做这一类简单的数据传输任务，让CPU解脱出来专注于别的任务。这样就可以让系统资源的利用更加有效。<br>
<br>参考文献：<br>
<ol><li><a href="https://kafka.apachecn.org/" rel="nofollow" target="_blank">https://kafka.apachecn.org/</a></li><li><a href="https://www.jianshu.com/p/b32ac197aacb" rel="nofollow" target="_blank">https://www.jianshu.com/p/b32ac197aacb</a></li><li><a href="https://www.bilibili.com/video/BV1a4411B7V9" rel="nofollow" target="_blank">https://www.bilibili.com/video/BV1a4411B7V9</a></li><li><a href="https://www.cnblogs.com/hzmark/p/sticky_assignor.html" rel="nofollow" target="_blank">https://www.cnblogs.com/hzmark ... .html</a></li><li><a href="https://zhuanlan.zhihu.com/p/65415304" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/65415304</a></li><li><a href="https://www.jianshu.com/p/fad3339e3448" rel="nofollow" target="_blank">https://www.jianshu.com/p/fad3339e3448</a></li><li>《Kafka权威指南》</li></ol><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/upMG8xUAXbN6R4EgqrHhTw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/upMG8xUAXbN6R4EgqrHhTw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            