
---
title: '一篇文章把RabbitMQ、RocketMQ、Kafka三元归一'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/40a022138eab382013a216d8b8a45494.png'
author: Dockone
comments: false
date: 2021-09-23 08:09:16
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/40a022138eab382013a216d8b8a45494.png'
---

<div>   
<br><h3>三大主流MQ的组织结构</h3><h4>RabbitMQ</h4><strong>RabbitMQ各组件的功能</strong><br>
<ul><li><code class="prettyprint">Broker</code>：一个RabbitMQ实例就是一个Broker</li><li><code class="prettyprint">Virtual Host</code>：虚拟主机。<strong>相当于MySQL的DataBase</strong>，一个Broker上可以存在多个vhost，vhost之间相互隔离。每个vhost都拥有自己的队列、交换机、绑定和权限机制。vhost必须在连接时指定，默认的vhost是/。</li><li><code class="prettyprint">Exchange</code>：交换机，用来接收生产者发送的消息并将这些消息路由给服务器中的队列。</li><li><code class="prettyprint">Queue</code>：消息队列，用来保存消息直到发送给消费者。它是消息的容器。一个消息可投入一个或多个队列。</li><li><code class="prettyprint">Banding</code>：绑定关系，用于<strong>消息队列和交换机之间的关联</strong>。通过路由键（<strong>Routing Key</strong>）将交换机和消息队列关联起来。</li><li><code class="prettyprint">Channel</code>：管道，一条双向数据流通道。不管是发布消息、订阅队列还是接收消息，这些动作都是通过管道完成。因为对于操作系统来说，建立和销毁TCP都是非常昂贵的开销，所以引入了管道的概念，以复用一条TCP连接。</li><li><code class="prettyprint">Connection</code>：生产者/消费者 与broker之间的TCP连接。</li><li><code class="prettyprint">Publisher</code>：消息的生产者。</li><li><code class="prettyprint">Consumer</code>：消息的消费者。</li><li><code class="prettyprint">Message</code>：消息，它是由消息头和消息体组成。消息头则包括<strong>Routing-Key</strong>、<strong>Priority</strong>（优先级）等。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/40a022138eab382013a216d8b8a45494.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/40a022138eab382013a216d8b8a45494.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>RabbitMQ的多种交换机类型</strong><br>
<br><code class="prettyprint">Exchange</code>分发消息给<code class="prettyprint">Queue</code>时，<code class="prettyprint">Exchange</code>的类型对应不同的分发策略，有3种类型的<code class="prettyprint">Exchange</code>：<strong>Direct</strong>、<strong>Fanout</strong>、<strong>Topic</strong>。<br>
<ul><li><strong>Direct</strong>： 消息中的<code class="prettyprint">Routing Key</code>如果和<code class="prettyprint">Binding</code>中的<code class="prettyprint">Routing Key</code>完全一致，<code class="prettyprint">Exchange</code>就会将消息分发到对应的队列中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/f28535b97d9594e333fba590be9b4634.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/f28535b97d9594e333fba590be9b4634.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><strong>Fanout</strong>： 每个发到 Fanout 类型交换机的消息都会分发到所有绑定的队列上去。Fanout交换机没有<code class="prettyprint">Routing Key</code>。<strong>它在三种类型的交换机中转发消息是最快的</strong>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/edd9ed62b00989fa3363d818865cb780.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/edd9ed62b00989fa3363d818865cb780.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><strong>Topic</strong>： Topic交换机通过模式匹配分配消息，将<code class="prettyprint">Routing Key</code>和某个模式进行匹配。它只能识别两个<strong>通配符</strong>：<strong>"#"和"*"</strong>。<code class="prettyprint">#</code>匹配0个或多个单词，<code class="prettyprint">*</code>匹配1个单词。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/58bee8accd8c8cf2d54457d6fb3c7f2e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/58bee8accd8c8cf2d54457d6fb3c7f2e.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br><strong>TTL</strong><br>
<br>TTL（Time To Live）：生存时间。RabbitMQ支持消息的过期时间，一共2种。<br>
<ul><li><strong>在消息发送时进行指定</strong>。通过配置消息体的<code class="prettyprint">Properties</code>，可以指定当前消息的过期时间。</li><li><strong>在创建Exchange时指定</strong>。从进入消息队列开始计算，只要超过了队列的超时时间配置，那么消息会自动清除。</li></ul><br>
<br><strong>生产者的消息确认机制</strong><br>
<br>Confirm机制：<br>
<ul><li>消息的确认，是指生产者投递消息后，如果Broker收到消息，则会给我们生产者一个应答。</li><li>生产者进行接受应答，用来确认这条消息是否正常的发送到了Broker，这种方式也是<strong>消息的可靠性投递的核心保障！</strong></li></ul><br>
<br>如何实现Confirm确认消息？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/712906b277deda0bad5c3894f7d766cb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/712906b277deda0bad5c3894f7d766cb.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li><strong>在channel上开启确认模式</strong>：<code class="prettyprint">channel.confirmSelect()</code></li><li><strong>在channel上开启监听</strong>：<code class="prettyprint">addConfirmListener</code>，监听成功和失败的处理结果，根据具体的结果对消息进行重新发送或记录日志处理等后续操作。</li></ol><br>
<br>Return消息机制：<br>
<br>Return Listener<strong>用于处理一些不可路由的消息</strong>。<br>
<br>我们的消息生产者，通过指定一个Exchange和Routing，把消息送达到某一个队列中去，然后我们的消费者监听队列进行消息的消费处理操作。<br>
<br>但是在某些情况下，如果我们在发送消息的时候，当前的exchange不存在或者指定的路由key路由不到，这个时候我们需要监听这种不可达消息，就需要使用到Returrn Listener。<br>
<br>基础API中有个关键的配置项<code class="prettyprint">Mandatory</code>：如果为true，监听器会收到路由不可达的消息，然后进行处理。如果为false，broker端会自动删除该消息。<br>
<br>同样，通过监听的方式，<code class="prettyprint">chennel.addReturnListener(ReturnListener rl)</code>传入已经重写过handleReturn方法的ReturnListener。<br>
<br><strong>消费端ACK与NACK</strong><br>
<br>消费端进行消费的时候，如果由于业务异常可以进行日志的记录，然后进行补偿。但是对于服务器宕机等严重问题，我们需要<strong>手动ACK</strong>保障消费端消费成功。<br>
<pre class="prettyprint">// deliveryTag：消息在mq中的唯一标识<br>
// multiple：是否批量(和qos设置类似的参数)<br>
// requeue：是否需要重回队列。或者丢弃或者重回队首再次消费。<br>
public void basicNack(long deliveryTag, boolean multiple, boolean requeue) <br>
</pre><br>
如上代码，消息在<strong>消费端重回队列</strong>是为了对没有成功处理消息，把消息重新返回到Broker。一般来说，实际应用中都会关闭重回队列（<strong>避免进入死循环</strong>），也就是设置为false。<br>
<br><strong>死信队列DLX</strong><br>
<br><strong><code class="prettyprint">死信队列（DLX Dead-Letter-Exchange）：</code></strong>  当消息在一个队列中变成死信之后，它会被重新推送到另一个队列，这个队列就是死信队列。<br>
<br>DLX也是一个正常的Exchange，和一般的Exchange没有区别，它能在任何的队列上被指定，实际上就是设置某个队列的属性。<br>
<br>当这个队列中有死信时，RabbitMQ就会自动的将这个消息重新发布到设置的Exchange上去，进而被路由到另一个队列。<br>
<h4>RocketMQ</h4>阿里巴巴双十一官方指定消息产品，支撑阿里巴巴集团所有的消息服务，历经十余年高可用与高可靠的严苛考验，是阿里巴巴交易链路的核心产品。<br>
<br>Rocket：火箭的意思。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/4d1f293e7e955021e671daf6148f3ef8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/4d1f293e7e955021e671daf6148f3ef8.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>RocketMQ的核心概念</strong><br>
<br>他有以下核心概念：<code class="prettyprint">Broker</code>、<code class="prettyprint">Topic</code>、<code class="prettyprint">Tag</code>、<code class="prettyprint">MessageQueue</code>、<code class="prettyprint">NameServer</code>、<code class="prettyprint">Group</code>、<code class="prettyprint">Offset</code>、<code class="prettyprint">Producer</code>以及<code class="prettyprint">Consumer</code>。<br>
<br>下面来详细介绍。<br>
<ul><li><br><strong>Broker</strong>：消息中转角色，负责<strong>存储消息</strong>，转发消息。<br>
<ul><li><strong>Broker</strong>是具体提供业务的服务器，单个Broker节点与所有的NameServer节点保持长连接及心跳，并会定时将<strong>Topic</strong>信息注册到NameServer，顺带一提底层的通信和连接都是<strong>基于Netty实现</strong>的。</li><li><strong>Broker</strong>负责消息存储，以Topic为纬度支持轻量级的队列，单机可以支撑上万队列规模，支持消息推拉模型。</li><li>官网上有数据显示：具有<strong>上亿级消息堆积能力</strong>，同时可<strong>严格保证消息的有序性</strong>。</li></ul></li><li><br><strong>Topic</strong>：主题！它是消息的第一级类型。比如一个电商系统可以分为：交易消息、物流消息等，一条消息必须有一个 Topic 。<strong>Topic</strong>  与生产者和消费者的关系非常松散，一个 Topic 可以有0个、1个、多个生产者向其发送消息，一个生产者也可以同时向不同的 Topic 发送消息。一个 Topic 也可以被 0个、1个、多个消费者订阅。</li><li><strong>Tag</strong>：标签！可以看作子主题，它是消息的第二级类型，用于为用户提供额外的灵活性。使用标签，同一业务模块不同目的的消息就可以用相同Topic而不同的<strong>Tag</strong>来标识。比如交易消息又可以分为：交易创建消息、交易完成消息等，一条消息可以没有<strong>Tag</strong>。标签有助于保持您的代码干净和连贯，并且还可以为<strong>RocketMQ</strong>提供的查询系统提供帮助。</li><li><strong>MessageQueue</strong>：一个Topic下可以设置多个消息队列，发送消息时执行该消息的Topic，RocketMQ会轮询该Topic下的所有队列将消息发出去。消息的物理管理单位。一个Topic下可以有多个Queue，Queue的引入使得消息的存储可以分布式集群化，具有了水平扩展能力。</li><li><strong>NameServer</strong>：类似Kafka中的ZooKeeper，但NameServer集群之间是<strong>没有通信</strong>的，相对ZK来说更加<strong>轻量</strong>。它主要负责对于源数据的管理，包括了对于<strong>Topic</strong>和路由信息的管理。每个Broker在启动的时候会到NameServer注册，Producer在发送消息前会根据Topic去NameServer<strong>获取对应Broker的路由信息</strong>，Consumer也会定时获取 Topic 的路由信息。</li><li><br><strong>Producer</strong>： 生产者，支持三种方式发送消息：<strong>同步、异步和单向</strong><br>
<ul><li><code class="prettyprint">单向发送</code>：消息发出去后，可以继续发送下一条消息或执行业务代码，不等待服务器回应，且<strong>没有回调函数</strong>。</li><li><code class="prettyprint">异步发送</code>：消息发出去后，可以继续发送下一条消息或执行业务代码，不等待服务器回应，<strong>有回调函数</strong>。</li><li><code class="prettyprint">同步发送</code>：消息发出去后，等待服务器响应成功或失败，才能继续后面的操作。</li></ul></li><li><br><strong>Consumer</strong>：消费者，支持<code class="prettyprint">PUSH</code>和<code class="prettyprint">PULL</code>两种消费模式，支持<strong>集群消费</strong>和<strong>广播消费</strong><br>
<ul><li><code class="prettyprint">集群消费</code>：该模式下一个消费者集群共同消费一个主题的多个队列，一个队列只会被一个消费者消费，如果某个消费者挂掉，分组内其它消费者会接替挂掉的消费者继续消费。</li><li><code class="prettyprint">广播消费</code>：会发给消费者组中的每一个消费者进行消费。相当于<strong>RabbitMQ</strong>的发布订阅模式。</li></ul></li><li><br><strong>Group</strong>：分组，一个组可以订阅多个Topic。分为ProducerGroup，ConsumerGroup，代表某一类的生产者和消费者，一般来说同一个服务可以作为Group，同一个Group一般来说发送和消费的消息都是一样的</li><li><strong>Offset</strong>：在RocketMQ中，所有消息队列都是持久化，长度无限的数据结构，所谓长度无限是指队列中的每个存储单元都是定长，访问其中的存储单元使用Offset来访问，Offset为Java Long类型，64位，理论上在 100年内不会溢出，所以认为是长度无限。也可以认为Message Queue是一个长度无限的数组，<strong>Offset</strong>就是下标。</li></ul><br>
<br><strong>延时消息</strong><br>
<br>开源版的RocketMQ不支持任意时间精度，仅支持特定的level，例如定时5s，10s，1min等。其中，level=0级表示不延时，level=1表示1级延时，level=2表示2级延时，以此类推。<br>
<br>延时等级如下：<br>
<pre class="prettyprint">messageDelayLevel=1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h<br>
</pre><br>
<strong>顺序消息</strong><br>
<br>消息有序指的是可以按照消息的发送顺序来消费（FIFO）。RocketMQ可以严格的保证消息有序，可以分为<code class="prettyprint">分区有序</code>或者<code class="prettyprint">全局有序</code>。<br>
<br><strong>事务消息</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/d2a58546f142fbbb1338094af69d13be.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/d2a58546f142fbbb1338094af69d13be.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
消息队列MQ提供类似X/Open XA的分布式事务功能，通过消息队列MQ事务消息能达到分布式事务的最终一致。上图说明了事务消息的大致流程：正常事务消息的发送和提交、事务消息的补偿流程。<br>
<br>事务消息发送及提交：<br>
<ol><li>发送half消息</li><li>服务端响应消息写入结果</li><li>根据发送结果执行本地事务（如果写入失败，此时half消息对业务不可见，本地逻辑不执行）；</li><li>根据本地事务状态执行Commit或Rollback（Commit操作生成消息索引，消息对消费者可见）。</li></ol><br>
<br>事务消息的补偿流程：<br>
<ol><li>对没有Commit/Rollback的事务消息（pending状态的消息），从服务端发起一次“回查”；</li><li>Producer收到回查消息，检查回查消息对应的本地事务的状态。</li><li>根据本地事务状态，重新Commit或RollBack</li></ol><br>
<br>其中，补偿阶段用于解决消息Commit或Rollback发生超时或者失败的情况。<br>
<br>事务消息状态：<br>
<br>事务消息共有三种状态：提交状态、回滚状态、中间状态：<br>
<ol><li>TransactionStatus.CommitTransaction：提交事务，它允许消费者消费此消息。</li><li>TransactionStatus.RollbackTransaction：回滚事务，它代表该消息将被删除，不允许被消费。</li><li>TransactionStatus.Unkonwn：中间状态，它代表需要检查消息队列来确定消息状态。</li></ol><br>
<br><strong>RocketMQ的高可用机制</strong><br>
<br>RocketMQ是天生支持分布式的，可以配置主从以及水平扩展。<br>
<br>Master角色的Broker支持读和写，Slave角色的Broker仅支持读，也就是 Producer只能和Master角色的Broker连接写入消息；Consumer可以连接 Master角色的Broker，也可以连接Slave角色的Broker来读取消息。<br>
<br>消息消费的高可用（主从）：<br>
<br>在Consumer的配置文件中，并不需要设置是从Master读还是从Slave读，当Master不可用或者繁忙的时候，Consumer会被自动切换到从Slave读。有了自动切换Consumer这种机制，当一个Master角色的机器出现故障后，Consumer仍然可以从Slave读取消息，不影响Consumer程序。这就达到了消费端的高可用性。<strong>RocketMQ目前还不支持把Slave自动转成Master</strong>，如果机器资源不足，需要把Slave转成Master，则要手动停止Slave角色的Broker，更改配置文件，用新的配置文件启动Broker。<br>
<br>消息发送高可用（配置多个主节点）：<br>
<br>在创建Topic的时候，把Topic的多个Message Queue创建在多个Broker组上（相同Broker名称，不同 brokerId的机器组成一个Broker组），这样当一个Broker组的Master不可用后，其他组的Master仍然可用，Producer仍然可以发送消息。<br>
<br>主从复制：<br>
<br>如果一个Broker组有Master和Slave，消息需要从Master复制到Slave 上，有同步和异步两种复制方式。<br>
<ul><li><strong>同步复制</strong>：同步复制方式是等Master和Slave均写成功后才反馈给客户端写成功状态。如果Master出故障， Slave上有全部的备份数据，容易恢复同步复制会增大数据写入延迟，降低系统吞吐量。</li><li><strong>异步复制</strong>：异步复制方式是只要Master写成功 即可反馈给客户端写成功状态。在异步复制方式下，系统拥有较低的延迟和较高的吞吐量，但是如果Master出了故障，有些数据因为没有被写 入Slave，有可能会丢失</li></ul><br>
<br>通常情况下，应该把Master和Save配置成同步刷盘方式，主从之间配置成异步的复制方式，这样即使有一台机器出故障，仍然能保证数据不丢，是个不错的选择。<br>
<br><strong>负载均衡</strong><br>
<br>Producer负载均衡：<br>
<br>Producer端，每个实例在发消息的时候，默认会<strong>轮询</strong>所有的Message Queue发送，以达到让消息平均落在不同的Queue上。而由于Queue可以散落在不同的Broker，所以消息就发送到不同的Broker下，如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/92f4bde1bf6b9c55b39e5081c0c7f127.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/92f4bde1bf6b9c55b39e5081c0c7f127.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Consumer负载均衡：<br>
<br>如果Consumer实例的数量比Message Queue的总数量还多的话，<strong>多出来的Consumer实例将无法分到Queue</strong>，也就无法消费到消息，也就无法起到分摊负载的作用了。所以需要控制让Queue的总数量大于等于Consumer的数量。<br>
<ul><li>消费者的集群模式：启动多个消费者就可以保证消费者的负载均衡（均摊队列）</li><li><strong>默认使用的是均摊队列</strong>：会按照Queue的数量和实例的数量平均分配Queue给每个实例，这样每个消费者可以均摊消费的队列，如下图所示6个队列和三个生产者。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/c9f2463ede2784832c3a8ec9771f7849.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/c9f2463ede2784832c3a8ec9771f7849.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>另外一种平均的算法<strong>环状轮流分Queue</strong>的形式，每个消费者，均摊不同主节点的一个消息队列，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/a9e48a72f3d6f1daea26f6125a512b07.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/a9e48a72f3d6f1daea26f6125a512b07.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br>对于广播模式并不是负载均衡的，要求一条消息需要投递到一个消费组下面所有的消费者实例，所以也就没有消息被分摊消费的说法。<br>
<br><strong>死信队列</strong><br>
<br>当一条消息消费失败，RocketMQ就会自动进行消息重试。而如果消息超过最大重试次数，RocketMQ就会认为这个消息有问题。但是此时，RocketMQ不会立刻将这个有问题的消息丢弃，而会将其发送到这个消费者组对应的一种特殊队列：死信队列。死信队列的名称是<code class="prettyprint">%DLQ%+ConsumGroup</code>。<br>
<br>死信队列具有以下特性：<br>
<ol><li>一个死信队列对应一个Group ID， 而不是对应单个消费者实例。</li><li>如果一个Group ID未产生死信消息，消息队列RocketMQ不会为其创建相应的死信队列。</li><li>一个死信队列包含了对应Group ID产生的所有死信消息，不论该消息属于哪个Topic。</li></ol><br>
<br><h4>Kafka</h4>Kafka是一个分布式、支持分区的、多副本的，<strong>基于ZooKeeper</strong>协调的分布式消息系统。<br>
<br>它最大的特性就是可以实时的处理大量数据以满足各种需求场景：比如基于Hadoop的批处理系统、低延迟的实时系统、Storm/Spark流式处理引擎，Web/Nginx日志、访问日志，消息服务等等，用<strong>Scala语言编写</strong>。属于Apache基金会的顶级开源项目。<br>
<br>先看一下Kafka的架构图 ： <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/09e78160e1da75484b6222f72474b314.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/09e78160e1da75484b6222f72474b314.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Kafka的核心概念</strong><br>
<br>在Kafka中有几个核心概念：<br>
<ul><li><strong>Broker</strong>：消息中间件处理节点，一个Kafka节点就是一个Broker，一个或者多个Broker可以组成一个Kafka集群</li><li><strong>Topic</strong>：Kafka根据topic对消息进行归类，发布到Kafka集群的每条消息都需要指定一个topic</li><li><strong>Producer</strong>：消息生产者，向Broker发送消息的客户端</li><li><strong>Consumer</strong>：消息消费者，从Broker读取消息的客户端</li><li><strong>ConsumerGroup</strong>：每个Consumer属于一个特定的ConsumerGroup，一条消息可以被多个不同的ConsumerGroup消费，但是一个ConsumerGroup中只能有一个Consumer能够消费该消息</li><li><strong>Partition</strong>：物理上的概念，一个topic可以分为多个partition，每个partition内部消息是有序的</li><li><strong>Leader</strong>：每个Partition有多个副本，其中有且仅有一个作为Leader，Leader是负责数据读写的Partition。</li><li><strong>Follower</strong>：Follower跟随Leader，所有写请求都通过Leader路由，数据变更会广播给所有Follower，Follower与Leader保持数据同步。如果Leader失效，则从Follower中选举出一个新的Leader。当Follower与Leader挂掉、卡住或者同步太慢，Leader会把这个Follower从<code class="prettyprint">ISR列表</code>中删除，重新创建一个Follower。</li><li><strong>Offset</strong>：偏移量。Kafka的存储文件都是按照offset.kafka来命名，用Offset做名字的好处是方便查找。例如你想找位于2049的位置，只要找到2048.kafka的文件即可。</li></ul><br>
<br>可以这么来理解Topic，Partition和Broker：<br>
<br>一个Topic，代表逻辑上的一个业务数据集，比如订单相关操作消息放入订单Topic，用户相关操作消息放入用户Topic，对于大型网站来说，后端数据都是海量的，订单消息很可能是非常巨量的，比如有几百个G甚至达到TB级别，如果把这么多数据都放在一台机器上可定会有容量限制问题，那么就可以在Topic内部划分多个Partition来分片存储数据，不同的Partition可以位于不同的机器上，相当于<strong>分布式存储</strong>。每台机器上都运行一个Kafka的进程Broker。<br>
<br><strong>Kafka核心总控制器Controller</strong><br>
<br>在Kafka集群中会有一个或者多个Broker，其中有一个Broker会被选举为控制器（Kafka Controller），可以理解为<code class="prettyprint">Broker-Leader</code>，它负责管理整个 集群中所有分区和副本的状态。<br>
<ul><li>当某个<code class="prettyprint">Partition-Leader</code>副本出现故障时，由控制器负责为该分区选举新的Leader副本。</li><li>当检测到某个分区的ISR集合发生变化时，由控制器负责通知所有Broker更新其元数据信息。</li><li>当为某个topic增加分区数量时，同样还是由控制器负责让新分区被其他节点感知到。</li></ul><br>
<br><strong>Controller选举机制</strong><br>
<br>在Kafka集群启动的时候，选举的过程是集群中每个Broker都会尝试在ZooKeeper上创建一个 /controller临时节点，ZooKeeper会保证有且仅有一个Broker能创建成功，这个Broker就会成为集群的总控器Controller。<br>
<br>当这个Controller角色的Broker宕机了，此时ZooKeeper临时节点会消失，集群里其他Broker会一直监听这个临时节 点，发现临时节点消失了，就竞争再次创建临时节点，就是我们上面说的选举机制，ZooKeeper又会保证有一个Broker成为新的Controller。 具备控制器身份的Broker需要比其他普通的Broker多一份职责，具体细节如下：<br>
<ol><li><strong>监听Broker相关的变化</strong>。为ZooKeeper中的/brokers/ids/节点添加BrokerChangeListener，用来处理Broker增减的变化。</li><li><strong>监听Topic相关的变化</strong>。为ZooKeeper中的/brokers/topics节点添加TopicChangeListener，用来处理Topic增减的变化；为ZooKeeper中的/admin/delete_topics节点添加TopicDeletionListener，用来处理删除Topic的动作。</li><li><strong>从ZooKeeper中读取获取当前所有与Topic、Partition以及Broker有关的信息并进行相应的管理</strong>。对于所有Topic所对应的ZooKeeper中的/brokers/topics/节点添加PartitionModificationsListener，用来监听Topic中的分区分配变化。</li><li><strong>更新集群的元数据信息，同步到其他普通的Broker节点中</strong></li></ol><br>
<br><strong>Partition副本选举Leader机制</strong><br>
<br>Controller感知到分区Leader所在的Broker挂了，Controller会从ISR列表（参数unclean.leader.election.enable=false的前提下）里挑第一个Broker作为Leader（第一个Broker最先放进ISR列表，可能是同步数据最多的副本），如果参数unclean.leader.election.enable为true，代表在ISR列表里所有副本都挂了的时候可以在ISR列表以外的副本中选Leader，这种设置，可以提高可用性，但是选出的新Leader有可能数据少很多。 副本进入ISR列表有两个条件：<br>
<ol><li>副本节点不能产生分区，必须能与ZooKeeper保持会话以及跟Leader副本网络连通</li><li>副本能复制Leader上的所有写操作，并且不能落后太多。（与Leader副本同步滞后的副本，是由replica.lag.time.max.ms配置决定的，超过这个时间都没有跟Leader同步过的一次的副本会被移出ISR列表）</li></ol><br>
<br><strong>消费者消费消息的Offset记录机制</strong><br>
<br>每个Consumer会定期将自己消费分区的Offset提交给Kafka内部Topic：consumer_offsets，提交过去的时候，key是consumerGroupId+topic+分区号，value就是当前Offset的值，Kafka会定期清理Topic里的消息，最后就保留最新的那条数据。<br>
<br>因为__consumer_offsets可能会接收高并发的请求，Kafka默认给其分配50个分区（可以通过offsets.topic.num.partitions设置），这样可以通过加机器的方式抗大并发。<br>
<br><strong>消费者Rebalance机制</strong><br>
<br>Rebalance就是说<strong>如果消费组里的消费者数量有变化或消费的分区数有变化，Kafka会重新分配消费者与消费分区的关系</strong>。 比如consumer group中某个消费者挂了，此时会自动把分配给他的分区交给其他的消费者，如果他又重启了，那么又会把一些分区重新交还给他。<br>
<br><strong>注意</strong>：Rebalance只针对subscribe这种不指定分区消费的情况，如果通过assign这种消费方式指定了分区，Kafka不会进行Rebalance。<br>
<br>如下情况可能会触发消费者Rebalance：<br>
<ol><li>消费组里的Consumer增加或减少了</li><li>动态给Topic增加了分区</li><li>消费组订阅了更多的Topic</li></ol><br>
<br>Rebalance过程中，消费者无法从Kafka消费消息，这对Kafka的TPS会有影响，如果Kafka集群内节点较多，比如数百 个，那重平衡可能会耗时极多，所以应尽量避免在系统高峰期的重平衡发生。<br>
<br><strong>Rebalance过程如下</strong><br>
<br>当有消费者加入消费组时，消费者、消费组及组协调器之间会经历以下几个阶段：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/5a67e06824b3237dcf72c5dbf0fed66a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/5a67e06824b3237dcf72c5dbf0fed66a.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
第一阶段：选择组协调器<br>
<br>组协调器GroupCoordinator：每个consumer group都会选择一个Broker作为自己的组协调器coordinator，负责监控这个消费组里的所有消费者的心跳，以及判断是否宕机，然后开启消费者Rebalance。 consumer group中的每个consumer启动时会向Kafka集群中的某个节点发送FindCoordinatorRequest请求来查找对应的组协调器GroupCoordinator，并跟其建立网络连接。 组协调器选择方式：通过如下公式可以选出consumer消费的Offset要提交到__consumer_offsets的哪个分区，这个分区Leader对应的Broker就是这个consumer group的coordinator公式：<br>
<br><code class="prettyprint">hash(consumer group id) % 对应主题的分区数</code><br>
<br>第二阶段：加入消费组JOIN GROUP<br>
<br>在成功找到消费组所对应的GroupCoordinator之后就进入加入消费组的阶段，在此阶段的消费者会向GroupCoordinator发送JoinGroupRequest请求，并处理响应。然后GroupCoordinator从一个consumer group中选择第一个加入group的consumer作为Leader（消费组协调器），把consumer group情况发送给这个Leader，接着这个Leader会负责制定分区方案。<br>
<br>第三阶段（SYNC GROUP）<br>
<br>consumer leader通过给GroupCoordinator发送SyncGroupRequest，接着GroupCoordinator就把分区方案下发给各个consumer，他们会根据指定分区的Leader Broker进行网络连接以及消息消费。<br>
<br><strong>消费者Rebalance分区分配策略</strong><br>
<br>主要有三种Rebalance的策略：<code class="prettyprint">range</code>、<code class="prettyprint">round-robin</code>、<code class="prettyprint">sticky</code>。<strong>默认情况为range分配策略</strong>。<br>
<br>假设一个主题有10个分区（0-9），现在有三个consumer消费：<br>
<br><strong>range策略</strong>：<code class="prettyprint">按照分区序号排序分配</code>，假设n＝分区数／消费者数量 = 3， m＝分区数%消费者数量 = 1，那么前 m 个消 费者每个分配 n+1 个分区，后面的（消费者数量－m ）个消费者每个分配 n 个分区。 比如分区0~ 3给一个consumer，分区4~ 6给一个consumer，分区7~9给一个consumer。<br>
<br><strong>round-robin策略</strong>：<code class="prettyprint">轮询分配</code>，比如分区0、3、6、9给一个consumer，分区1、4、7给一个consumer，分区2、5、 8给一个consumer<br>
<br><strong>sticky策略</strong>：  初始时分配策略与round-robin类似，但是在rebalance的时候，需要保证如下两个原则：<br>
<ol><li>分区的分配要尽可能均匀 。</li><li>分区的分配尽可能与上次分配的保持相同。</li></ol><br>
<br>当两者发生冲突时，第一个目标优先于第二个目标 。这样可以最大程度维持原来的分区分配的策略。 比如对于第一种range情况的分配，如果第三个consumer挂了，那么重新用sticky策略分配的结果如下： consumer1除了原有的0~ 3，会再分配一个7 consumer2除了原有的4~ 6，会再分配8和9。<br>
<br><strong>Producer发布消息机制剖析</strong><br>
<br>1、写入方式<br>
<br>producer采用push模式将消息发布到broker，每条消息都被append到patition中，属于顺序写磁盘（<strong>顺序写磁盘 比 随机写 效率要高，保障 kafka 吞吐率</strong>）。<br>
<br>2、消息路由<br>
<br>producer发送消息到broker时，会根据分区算法选择将其存储到哪一个partition。其路由机制为：<br>
<ol><li>指定了 patition，则直接使用；</li><li>未指定patition 但指定key，通过<code class="prettyprint">hash(key)%分区数</code>算出路由patition，如果patition和key都未指定，使用轮询选出一个patition。</li></ol><br>
<br>3、写入流程<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/9214d9344330028a373e25a348c6c10d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/9214d9344330028a373e25a348c6c10d.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li>producer先从ZooKeeper的 "/brokers/.../state" 节点找到该partition的leader</li><li>producer将消息发送给该leader</li><li>leader将消息写入本地log</li><li>followers从leader pull消息，写入本地log后向leader发送ACK</li><li>leader收到所有ISR中的replica的ACK后，增加HW（high watermark，最后commit的offset）并向producer发送ACK</li></ol><br>
<br><strong>HW与LEO</strong><br>
<br><code class="prettyprint">HW俗称高水位</code>，HighWatermark的缩写，取一个partition对应的ISR中最小的LEO（log-end-offset）作为HW， consumer最多只能消费到HW所在的位置。另外每个replica都有HW,leader和follower各自负责更新自己的HW的状 态。对于leader新写入的消息，consumer不能立刻消费，leader会等待该消息被所有ISR中的replicas同步后更新HW， 此时消息才能被consumer消费。<strong>这样就保证了如果leader所在的broker失效，该消息仍然可以从新选举的leader中获取。对于来自内部broker的读取请求，没有HW的限制。</strong><br>
<br><strong>日志分段存储</strong><br>
<br>Kafka一个分区的消息数据对应存储在一个文件夹下，以topic名称+分区号命名，消息在分区内是分段存储的， 每个段的消息都存储在不一样的log文件里，Kafka规定了一个段位的log文件最大为1G，做这个限制目的是为了方便把log文件加载到内存去操作：<br>
<pre class="prettyprint">1 # 部分消息的offset索引文件，kafka每次往分区发4K(可配置)消息就会记录一条当前消息的offset到index文件， <br>
2 # 如果要定位消息的offset会先在这个文件里快速定位，再去log文件里找具体消息 <br>
3 00000000000000000000.index <br>
4 # 消息存储文件，主要存offset和消息体 <br>
5 00000000000000000000.log <br>
6 # 消息的发送时间索引文件，kafka每次往分区发4K(可配置)消息就会记录一条当前消息的发送时间戳与对应的offset到timeindex文件， <br>
7 # 如果需要按照时间来定位消息的offset，会先在这个文件里查找 <br>
8 00000000000000000000.timeindex <br>
9 <br>
10 00000000000005367851.index <br>
11 00000000000005367851.log <br>
12 00000000000005367851.timeindex <br>
13 <br>
14 00000000000009936472.index <br>
15 00000000000009936472.log <br>
16 00000000000009936472.timeindex<br>
</pre><br>
这个9936472之类的数字，就是代表了这个日志段文件里包含的起始 Offset，也就说明这个分区里至少都写入了接近1000万条数据了。Kafka Broker有一个参数，log.segment.bytes，限定了每个日志段文件的大小，最大就是1GB。 一个日志段文件满了，就自动开一个新的日志段文件来写入，避免单个文件过大，影响文件的读写性能，这个过程叫做log rolling，正在被写入的那个日志段文件，叫做active log segment。<br>
<br><strong>最后附一张ZooKeeper节点数据图</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/79de107a93849be31ff2ae1107d96d84.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/79de107a93849be31ff2ae1107d96d84.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>MQ带来的一些问题、及解决方案</h3><h4>如何保证顺序消费？</h4><ul><li><strong>RabbitMQ</strong>：一个Queue对应一个Consumer即可解决。</li><li><br><strong>RocketMQ</strong><br>
<ul><li>全局有序：Topic里面只有一个MessageQueue即可。</li><li>局部有序: 根据路由算法，比如<code class="prettyprint">hash(key)%队列数</code>得到路由索引，使得需要保证有序的消息都路由到同一个MessageQueue。</li></ul></li><li><br><strong>Kafka</strong>：<br>
<ul><li>全局有序：Topic里面只有一个Partition即可。</li><li>局部有序：根据路由算法，比如<code class="prettyprint">hash(key)%分区数</code>得到路由索引，使得需要保证有序的消息都路由到同一个Partition。</li></ul></li></ul><br>
<br><h4>如何实现延迟消费？</h4><ul><li><br><strong>RabbitMQ</strong>：两种方案<br>
<ul><li>死信队列 + TTL</li><li>引入RabbitMQ的延迟插件</li></ul></li><li><br><strong>RocketMQ</strong>：天生支持延时消息。</li><li><br><strong>Kafka</strong>：步骤如下<br>
<ul><li>专门为要延迟的消息创建一个Topic</li><li>新建一个消费者去消费这个Topic</li><li>消息持久化</li><li>再开一个线程定时去拉取持久化的消息，放入实际要消费的Topic</li><li>实际消费的消费者从实际要消费的Topic拉取消息。</li></ul></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/0f0191e236346d8b0d233ae4c6f95fd0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/0f0191e236346d8b0d233ae4c6f95fd0.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>如何保证消息的可靠性投递</h4>RabbitMQ：<br>
<ul><li>Broker-->消费者：手动ACK</li><li>生产者-->Broker：两种方案</li></ul><br>
<br>数据库持久化：<br>
<pre class="prettyprint">1.将业务订单数据和生成的Message进行持久化操作（一般情况下插入数据库，这里如果分库的话可能涉及到分布式事务）<br>
2.将Message发送到Broker服务器中<br>
3.通过RabbitMQ的Confirm机制，在producer端，监听服务器是否ACK。<br>
4.如果ACK了，就将Message这条数据状态更新为已发送。如果失败，修改为失败状态。<br>
5.分布式定时任务查询数据库3分钟（这个具体时间应该根据的时效性来定）之前的发送失败的消息<br>
6.重新发送消息，记录发送次数<br>
7.如果发送次数过多仍然失败，那么就需要人工排查之类的操作。<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/3c1c625aa5a941f5ac21860e633f729d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/3c1c625aa5a941f5ac21860e633f729d.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
优点：能够保证消息百分百不丢失。<br>
<br>缺点：第一步会涉及到分布式事务问题。<br>
<br>消息的延迟投递：<br>
<pre class="prettyprint">流程图中，颜色不同的代表不同的message<br>
1.将业务订单持久化<br>
2.发送一条Message到broker(称之为主Message)，再发送相同的一条到不同的队列或者交换机(这条称为确认Message)中。<br>
3.主Message由实际业务处理端消费后，生成一条响应Message。之前的确认Message由Message Service应用处理入库。<br>
4~6.实际业务处理端发送的确认Message由Message Service接收后，将原Message状态修改。<br>
7.如果该条Message没有被确认，则通过rpc调用重新由producer进行全过程。<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/13ad2d03a1039b7ce9b4383ffbb6af69.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/13ad2d03a1039b7ce9b4383ffbb6af69.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>优点</strong>：相对于持久化方案来说响应速度有所提升<br>
<br><strong>缺点</strong>：系统复杂性有点高，万一两条消息都失败了，消息存在丢失情况，仍需Confirm机制做补偿。<br>
<br><strong>RocketMQ</strong><br>
<br>生产者弄丢数据：<br>
<br>Producer在把Message发送Broker的过程中，因为网络问题等发生丢失，或者Message到了Broker，但是出了问题，没有保存下来。针对这个问题，RocketMQ对Producer发送消息设置了3种方式：<br>
<ol><li><code class="prettyprint">同步发送</code>：天生保证了可靠性投递</li><li><code class="prettyprint">异步发送</code>：需要在回调函数中，根据broker响应的结果自定义实现。</li><li><code class="prettyprint">单向发送</code>：保证不了可靠性投递</li></ol><br>
<br>Broker弄丢数据：<br>
<br>Broker接收到Message暂存到内存，Consumer还没来得及消费，Broker挂掉了。<br>
<br>可以通过<code class="prettyprint">持久化</code>设置去解决：<br>
<ol><li>创建Queue的时候设置持久化，保证Broker持久化Queue的元数据，但是不会持久化Queue里面的消息</li><li>将Message的deliveryMode设置为2，可以将消息持久化到磁盘，这样只有Message支持化到磁盘之后才会发送通知Producer ack</li></ol><br>
<br>这两步过后，即使Broker挂了，Producer肯定收不到ack的，就可以进行重发。<br>
<br>消费者弄丢数据：<br>
<br>Consumer有消费到Message，但是内部出现问题，Message还没处理，Broker以为Consumer处理完了，只会把后续的消息发送。这时候，就要<code class="prettyprint">关闭autoack，消息处理过后，进行手动ack</code>, 多次消费失败的消息，会进入<code class="prettyprint">死信队列</code>，这时候需要人工干预。<br>
<h4>Kafka</h4><strong>生产者弄丢数据</strong><br>
<br>设置了 <code class="prettyprint">acks=all</code>，一定不会丢，要求是，你的 leader 接收到消息，所有的 follower 都同步到了消息之后，才认为本次写成功了。如果没满足这个条件，生产者会自动不断的重试，重试无限次。<br>
<br><strong>Broker弄丢数据</strong><br>
<br>Kafka 某个 broker 宕机，然后重新选举 partition 的 leader。大家想想，要是此时其他的 follower 刚好还有些数据没有同步，结果此时 leader 挂了，然后选举某个 follower 成 leader 之后，不就少了一些数据？这就丢了一些数据啊。<br>
<br>此时一般是要求起码设置如下 4 个参数：<br>
<ul><li>给topic设置 <code class="prettyprint">replication.factor</code> 参数：这个值必须大于 1，要求每个 partition 必须有至少 2 个副本。</li><li>在Kafka服务端设置 <code class="prettyprint">min.insync.replicas</code> 参数：这个值必须大于 1，这个是要求一个 leader 至少感知到有至少一个 follower 还跟自己保持联系，没掉队，这样才能确保 leader 挂了还有一个 follower 吧。</li><li>在 producer 端设置 <code class="prettyprint">acks=all</code>：这个是要求每条数据，必须是写入所有 replica 之后，才能认为是写成功了。</li><li>在 producer 端设置 <code class="prettyprint">retries=MAX</code>（很大很大很大的一个值，无限次重试的意思）：这个是要求一旦写入失败，就无限重试，卡在这里了。</li></ul><br>
<br>我们生产环境就是按照上述要求配置的，这样配置之后，至少在 Kafka broker 端就可以保证在 leader 所在 broker 发生故障，进行 leader 切换时，数据不会丢失。<br>
<br><strong>消费者弄丢数据</strong><br>
<br>你消费到了这个消息，然后消费者那边自动提交了 offset，让 Kafka 以为你已经消费好了这个消息，但其实你才刚准备处理这个消息，你还没处理，你自己就挂了，此时这条消息就丢咯。<br>
<br>这不是跟 RabbitMQ 差不多吗，大家都知道 Kafka 会自动提交 offset，那么只要<strong>关闭自动提交 offset，在处理完之后自己手动提交 offset，就可以保证数据不会丢。</strong>  但是此时确实还是可能会有重复消费，比如你刚处理完，还没提交 offset，结果自己挂了，此时肯定会重复消费一次，自己保证幂等性就好了。<br>
<h4>如何保证消息的幂等？</h4>以 RocketMQ 为例，下面列出了消息重复的场景：<br>
<br><strong>发送时消息重复</strong><br>
<br>当一条消息已被成功发送到服务端并完成持久化，此时出现了网络闪断或者客户端宕机，导致服务端对客户端应答失败。如果此时生产者意识到消息发送失败并尝试再次发送消息，消费者后续会收到两条内容相同并且Message ID也相同的消息。<br>
<br><strong>投递时消息重复</strong><br>
<br>消息消费的场景下，消息已投递到消费者并完成业务处理，当客户端给服务端反馈应答的时候网络闪断。为了保证消息至少被消费一次，消息队列RocketMQ版的服务端将在网络恢复后再次尝试投递之前已被处理过的消息，消费者后续会收到两条内容相同并且Message ID也相同的消息。<br>
<br><strong>负载均衡时消息重复</strong>（包括但不限于网络抖动、Broker重启以及消费者应用重启）<br>
<br>当消息队列RocketMQ版的Broker或客户端重启、扩容或缩容时，会触发Rebalance，此时消费者可能会收到重复消息。<br>
<br>那么，有什么解决方案呢？ 直接上图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/bc31b12325f06b3fd0aed2f3ed12f0e4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/bc31b12325f06b3fd0aed2f3ed12f0e4.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>如何解决消息积压的问题？</h4>关于这个问题，有几个点需要考虑：<br>
<br><strong>如何快速让积压的消息被消费掉？</strong><br>
<br>临时写一个消息分发的消费者，把积压队列里的消息均匀分发到N个队列中，同时一个队列对应一个消费者，相当于消费速度提高了N倍。<br>
<br>修改前：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/274a91b9684a66791ff1ce86baf526c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/274a91b9684a66791ff1ce86baf526c4.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
修改后：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210922/d9515f4ead50f44c519f634aa8b6b889.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210922/d9515f4ead50f44c519f634aa8b6b889.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>积压时间太久，导致部分消息过期，怎么处理？</strong><br>
<br>批量重导。在业务不繁忙的时候，比如凌晨，提前准备好程序，把丢失的那批消息查出来，重新导入到MQ中。<br>
<br><strong>消息大量积压，MQ磁盘被写满了，导致新消息进不来了，丢掉了大量消息，怎么处理？</strong><br>
<br>这个没办法。谁让【消息分发的消费者】写的太慢了，你临时写程序，接入数据来消费，消费一个丢弃一个，都不要了，快速消费掉所有的消息。然后走第二个方案，到了晚上再补数据吧。<br>
<br>原文链接：<a href="https://juejin.cn/post/7006958043833303048" rel="nofollow" target="_blank">https://juejin.cn/post/7006958043833303048</a>，作者：Boom
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            