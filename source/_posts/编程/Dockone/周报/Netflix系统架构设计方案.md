
---
title: 'Netflix系统架构设计方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/77132ff186523f95ac4bed4ac20866bb.jpeg'
author: Dockone
comments: false
date: 2021-12-31 13:16:46
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/77132ff186523f95ac4bed4ac20866bb.jpeg'
---

<div>   
<br>【编者的话】Netflix是全球最大的在线视频网站之一，它是怎么设计的呢？这篇文章介绍了Netflix系统架构的设计方案。原文：<a href="https://medium.com/interviewnoodle/netflix-system-architecture-bedfc1d4bce5">Netflix System Architecture</a>。<br>
<br>我们来讨论一下如何设计Netflix。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/77132ff186523f95ac4bed4ac20866bb.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/77132ff186523f95ac4bed4ac20866bb.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
相信每个人都会通过某些网站或应用在线追剧或者看电影，而Netflix是我最喜欢的在线视频网站，不过今天我不推荐任何电影，相反，我想展示的是Netflix背后令人惊艳的系统逻辑。<br>
<h3>需求</h3><h4>功能性需求</h4><ol><li>创建帐户、登录、删除帐户</li><li>订阅或取消订阅不同的计划</li><li>允许用户拥有和处理多个帐户</li><li>允许用户观看视频</li><li>允许用户下载视频并离线观看</li><li>允许用户通过视频标题搜索和发现视频</li><li>Netflix制作人可以从后台上传视频并在平台上展示</li><li>平台可以显示趋势、最受欢迎的视频和分类，以方便用户选择</li><li>可以选择不同语言的字幕，这样用户即使听不懂这些语言，也可以观看视频</li><li>视频分组（剧集、娱乐节目、电影，单独处理每个视频）</li><li>根据用户行为进行分析，为用户推荐类似的视频</li><li>在同一账号下的不同设备之间进行同步，用户可以使用不同的设备继续观看同一视频而无需重播</li><li>支持全天候（24/7）回放</li><li>支持回退</li></ol><br>
<br><h4>非功能性需求</h4><ol><li>用户可以观看实时视频流，没有任何卡顿或延迟问题</li><li>系统是高度可靠的</li><li>高可用</li><li>可扩展</li><li>视频数据持久化且易于访问</li></ol><br>
<br><h3>容量预估</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/f927c3a5b92fd4242f73de601afc23c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/f927c3a5b92fd4242f73de601afc23c7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们可以基于一些数学计算来估计所需的带宽和存储空间。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/717570d8a083a3ab6fe31562e0fef7cc.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/717570d8a083a3ab6fe31562e0fef7cc.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/177bce63b9cda594fb3cf4d93d6106fb.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/177bce63b9cda594fb3cf4d93d6106fb.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>假设</h4><ol><li>日活用户总数 = 1亿</li><li>日活峰值用户：1亿 * 3 = 3亿</li><li>3个月最大日活峰值用户：3亿 * 2 = 6亿</li><li>每个用户每天平均观看的视频数 = 5</li><li>视频平均大小 = 500 MB</li><li>后台平均每天上传的视频数 = 1000</li><li>每天观看的总视频数 = 1亿*5 = 5亿</li><li>每天观看的总视频峰值 = 15亿</li><li>每天观看的最大视频峰值 = 30亿</li><li>每天总出口流量 = 5亿* 500 MB = 250 PB (Peta Byte)</li><li>出口带宽 = 29.1 GB/秒</li><li>每天上传总入口流量 = 1000 * 500MB = 500 GB</li><li>入口带宽 = 5.8 MB/秒</li><li>5年所需的总存储空间 = 500 GB * 5 * 365 = 912.5 TB（请注意，Netflix会为每个视频准备多种格式和分辨率的版本，可针对不同类型设备进行优化，所以存储空间将超过912.5 TB）。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/ce73dd2bf82a71e79f180bcf9e26b560.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/ce73dd2bf82a71e79f180bcf9e26b560.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/5dc64d7c5d0a17357076cda652a1456c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/5dc64d7c5d0a17357076cda652a1456c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>系统组件</h3><h4>系统组件详细设计</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/1096862bddd80bc7889832e4f6e88d86.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/1096862bddd80bc7889832e4f6e88d86.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/7c70231d75400988604b6342e2275496.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/7c70231d75400988604b6342e2275496.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
1、客户端应用<br>
<ul><li>手机（iOS，Android，华为，等等）</li><li>平板（iPad，Android，Windows）</li><li>电视</li><li>电脑</li></ul><br>
<br>基于React.js实现的前端可以拥有较好的加载/启动速度、持久性/模块化和运行时性能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/4ed1c9880b0f85aecafd2a1618d99d77.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/4ed1c9880b0f85aecafd2a1618d99d77.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2、后端<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/26ef6bb6d634a9ba6d5b99aa6372fd1a.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/26ef6bb6d634a9ba6d5b99aa6372fd1a.jpeg" class="img-polaroid" title="10.jpeg" alt="10.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
Netflix从2011年开始实施微服务架构，完全基于云来管理工作负载。通过小型、可管理的API组件支持并处理来自应用程序和网站的请求，微服务内部通过请求和获取数据而相互依赖。后端技术栈包括了Java，MySQL，Gluster，Apache Tomcat，Chukwa，Cassandra，Kafka和Hadoop。后端系统不单单需要处理流媒体视频，还需要处理其他所有事情，比方说数据处理、加载新内容、网络流量管理、全球资源分发等。Netflix目前部署在AWS之上。<br>
<br>数据处理涉及点击视频后发生的所有事件，系统需要在几纳秒的时间内处理完视频并将其传输给用户。整个系统每天大约需要处理6000亿个事件，产生1.5PB的数据，在高峰期（傍晚和夜间）每秒大约需要处理800万个事件。这些事件包括UI活动、视频查看活动、日志错误、故障排除、诊断事件、处理事件和性能事件等。所有这些事件都是通过Kafka和Apache Chukwe完成的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/ace5788f28172809861ac4be529e0460.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/ace5788f28172809861ac4be529e0460.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kafka和Apache Chukwe：<br>
<ul><li>从系统的不同部分获取产生的数据。</li><li>Apache Chukwe是一个开源数据收集系统，用于从分布式系统中收集日志或事件。它建立在HDFS和Map-reduce框架之上，具有Hadoop的可伸缩性和健壮性特性。此外，它还包含许多功能强大、灵活的工具箱，用于显示、监控和分析结果。Chukwe从系统的不同部分收集事件，并提供仪表盘帮助我们进行事件的查看、监控和分析。Chukwe以Hadoop文件序列格式（S3）写入事件，大数据团队可以处理这些S3 Hadoop文件，并以Parque格式将数据写入Hive。这个过程被称为批处理，基本上以每小时或每天的频率扫描整个数据。为了将在线事件上传到EMR/S3，Chukwa还向Kafka（实时数据处理的入口）提供流量。Kafka负责将数据从前端Kafka注入到不同的后端：S3，Elasticsearch和下游Kafka，消息的路由可以通过Apache Samja框架完成。通过Chukwe发送的流量既可以是完整的流也可以是过滤过的流，所以有时候你可能需要对Kafka流量进行进一步过滤，这就是我们需要考虑将流量从一个Kafka topic路由到另一个Kafka topic的原因。</li></ul><br>
<br>Elastic Search：<br>
<ul><li>Netflix目前有大约150个Elastic Search集群，其实例分布在3500个主机上。</li><li>Netflix通过Elastic Search来实现数据的可视化、客户支持以及系统中的错误检测。例如，如果客户无法播放视频，那么客户服务主管将利用Elastic Search来解决问题。回放团队会去Elastic Search搜索该用户，试图找到为什么视频不能在用户设备上播放的原因。他们可以了解特定用户所发生的所有信息和事件，知道是什么导致了视频流出错。系统管理员还可以基于Elastic Search跟踪某些信息，比如跟踪资源使用情况、检测注册或登录问题等。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/36360818e9f0887c0bc6b86d8fa6d21d.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/36360818e9f0887c0bc6b86d8fa6d21d.jpeg" class="img-polaroid" title="12.jpeg" alt="12.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
后端服务：<br>
<ul><li>用户和认证服务（主要负责用户认证和配置文件）。数据存储在关系型数据库中，如MySQL或PostgreSQL。</li><li>订阅管理服务（管理用户的订阅）。由于该服务处理的数据本质上是高度事务性的，因此RDBMS是一个合适的选择。</li><li>视频服务（向终端用户提供视频）。这个服务将视频元数据存储在RDBMS中，比如MySQL或PostgreSQL。为了获得更快的响应时间，该服务将使用Redis或Memcached这样的内存缓存来实现绕写（write-around）缓存。</li><li>转码服务（检查上传视频的质量，用不同的编解码器压缩视频，创建不同分辨率版本）。一旦视频被上传到Transcoder服务，它将把视频上传到内部分布式存储，比如S3，并向数据库添加条目。Kafka或RabbitMQ在队列中处理消息，后端工作组件收到队列的消息，内部S3下载视频，并将其转码为不同的格式。转码完成后，后端工作组件将视频上传到外部S3，并将数据库中的视频状态更新为active，供终端用户查看。后端工作组件还会在支持全文搜索的搜索数据库中添加视频元数据条目，这样终端用户就能够使用标题或摘要搜索视频。外部S3存储的视频也将通过CDN缓存，以减少延迟，提高播放性能。</li><li>全球搜索服务（允许终端用户使用元数据，如标题、摘要等搜索视频）。元数据存储在Elastic Search数据库中，因此可以基于Elasticsearch或Solr支持全文搜索，用户可以根据标题搜索电影、剧集或与视频相关的任何元数据。该服务还可以根据最近观看、评论、推荐和流行程度对结果进行排名，以获得更好的用户体验。此外，Elastic Search可以在失败的情况下跟踪用户事件，客户服务团队可以使用Elastic Search来解决问题。</li></ul><br>
<br>3、云<br>
<ul><li>Netflix将其IT基础设施迁移到公共云上。使用的云服务是AWS和Open connect（Netflix的定制CDN）。这两种云服务并行工作，用于视频处理和向终端用户分发内容。</li></ul><br>
<br>4、CDN<br>
<br>一个全球分布的服务器网络集群。当我们播放视频的时候，设备上显示的视频将从最近的CDN服务器获取，从而极大降低响应时间。<br>
<ul><li>CDN在多个地方复制内容，这样视频可以更贴近用户，传输距离更短。</li><li>CDN机器大量使用缓存，所以即使没有从服务器上找到视频，也可以从缓存中获取。</li><li>CDN不会缓存不太受欢迎的视频（比方说每天只有不到20次观看量的视频）</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/66eec1f78bee357359e899b1b2311ec0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/66eec1f78bee357359e899b1b2311ec0.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
5、Open connect<br>
<br>Netflix的内部定制全球CDN，负责向全球Netflix用户存储和传送电影和电视节目。当我们按下播放按钮，视频就会从全球不同位置的Open connect服务器中传输给我们。如果视频已经缓存在Open connect服务器上，客户端可以轻松访问到，而如果视频没有被缓存，Netflix必须从AWS的S3存储中获取并处理该视频，然后Open connect才可以将该视频流推送到客户端应用程序。<br>
<br>6、缓存<br>
<br>Redis和Memcached以键值对的方式缓存数据库中的数据，可以有效减少对数据库的访问。客户端通过服务器访问数据库之前，系统会检查缓存中是否有数据，如果有，就可以绕过数据库访问。但是，如果数据不在缓存中，必须访问数据库并获取数据，并在缓存中填充相同的数据。因此，随后的请求就不需要访问数据库了。这种缓存策略称为绕写（write-around）缓存。我们使用最近最少使用（LRU）策略作为缓存数据的驱逐策略，最早获取的缓存将会被丢弃。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/4a292ccb18f8e8ab19025da17e4fe452.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/4a292ccb18f8e8ab19025da17e4fe452.jpeg" class="img-polaroid" title="14.jpeg" alt="14.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>EV缓存实际上是Memcached的包装器</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/7a9f0c4f83d34a941543d3271402e066.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/7a9f0c4f83d34a941543d3271402e066.jpeg" class="img-polaroid" title="15.jpeg" alt="15.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
Netflix在AWS EC2上部署了很多集群，这些集群包含有很多Memcached节点以及缓存客户端。数据在同一个分区的集群中共享，多个缓存副本存储在分片节点中。每次当客户端写入数据时，所有集群中的所有节点都会被更新，但当读取数据时，读取操作只会被发送到最近的集群及其节点上，如果某个节点不可用，则从另一个可用节点读取。这种方法提高了性能、可用性和可靠性。<br>
<br>7、可扩展性<br>
<ul><li>水平扩展——在负载均衡器后面增加更多的应用服务器，以增加服务的容量。</li><li>数据库备份——关系数据库配置为主从关系，写操作发生在主数据库上，从从数据库读取数据。读操作不会因为写操作而被锁住，因此可以提高读查询的性能。当数据写入主数据库并复制到从数据库时，会有轻微的复制延迟（几毫秒）。</li><li>数据库分片——将数据分布到多个服务器上，以便高效的进行读写操作。比方说，我们可以使用video_id对视频元数据数据库进行分片，哈希函数把每个video_id随机映射到一个服务器上，从而存储对应的视频元数据。</li><li>缓存分片——将缓存分发到多个服务器上。Redis支持跨多个实例划分数据，为数据分布使用一致的哈希算法确保在一个实例消失时保持负载均匀分布。</li><li>搜索数据库分片——Elasticsearch原生支持分片和备份。通过在多个分片上并行运行分片，有助于改进查询运行时。</li></ul><br>
<br>8、安全<br>
<ul><li>HTTPS——通过HTTPS加密客户端和服务器之间的通信，确保中间没有人能够看到数据（特别是密码）。</li><li>身份验证——每个API请求必须完成登录验证，通过检查授权HTTP报头中auth_token的有效性来进行身份验证，确保请求是合法的。</li></ul><br>
<br>9、弹性<br>
<ul><li>备份——通过主从部署备份数据库。如果一个节点宕机，其他节点将按预期提供服务并继续运行。</li><li>队列——在处理上传的视频时使用。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/73d5a79d3b53bbf7b2d69b98ee06bdda.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/73d5a79d3b53bbf7b2d69b98ee06bdda.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
10、负载均衡<br>
<ul><li>一个负载均衡器后面有多个服务器，包括冗余资源。负载均衡器将持续对其背后的服务器进行健康检查，如果发现任意一个服务器停止工作，负载均衡器将停止向它转发流量，并将其从集群中移除，从而确保请求不会因为服务器没有响应而失败。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/22a37e811c819af7f7f99b511e2065b2.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/22a37e811c819af7f7f99b511e2065b2.jpeg" class="img-polaroid" title="17.jpeg" alt="17.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
负载均衡器负责将流量路由到前端服务。ELB（Elastic load balancing，弹性负载均衡）执行两层负载均衡方案，首先基于区域（zone）进行负载均衡，然后对实例（服务器）进行负载均衡。<br>
<ul><li>第一级由基础DNS组成，提供基于轮询的负载均衡（Round Robin Balancing）。当请求到达第一个负载均衡器时，它会根据配置选择一个区域（使用轮询机制）。</li><li>第二级是一组负载均衡器实例，执行轮询负载均衡，将请求分发到位于同一区域的多个业务实例中。</li></ul><br>
<br>11、Geo-redundancy<br>
<ul><li>在跨多个地理位置的数据中心部署服务的精确副本，一旦某个数据中心无法提供服务，仍然可以由其他数据中心提供服务。</li></ul><br>
<br>12、ZUUL<br>
<br>提供动态路由、监控、弹性和安全性，支持基于查询参数、URL路径的简单路由。<br>
<ul><li>Netty服务器负责处理网络协议、web服务、连接管理和代理工作。当请求到达Netty服务器时，它负责将请求转发到入口过滤器。</li><li>入口过滤器（The inbound filter）负责身份验证、路由或装饰请求。然后将请求转发给端点过滤器。</li><li>端点过滤器（Endpoint filter）用于返回静态响应，或者将请求转发到后端服务。一旦它从后端服务接收到响应，就将请求发送到出口过滤器。</li><li>出口过滤器（Outbound filter）用于压缩内容、计算指标或添加/删除自定义标头。在此之后，响应被发送回Netty服务器，然后发送给客户端。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/2ecfecfae1eb9bc0d06853c0af7d7b60.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/2ecfecfae1eb9bc0d06853c0af7d7b60.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
优势：<br>
<ol><li>可以创建规则，将流量的不同部分分配到不同的服务器，从而实现对流量的分片。</li><li>开发人员可以在某些机器上对新部署的集群进行负载测试，可以在这些集群上路由部分现网流量，并检查特定服务器可以承受多少负载。</li><li>可以用于测试新服务。当我们需要升级服务并希望检查该服务如何处理实时API请求时，可以将特定服务部署在一台服务器上，并将部分流量重定向到新服务，以便实时检查该服务状态。</li><li>可以通过在端点过滤器或防火墙上设置自定义规则来过滤恶意请求。</li></ol><br>
<br>13、Hystrix<br>
<br>在一个复杂的分布式系统中，一个服务器可能依赖于另一个服务器的响应。这些服务器之间的依赖关系可能会造成延迟，如果其中一个服务器在某个时刻不可避免的出现故障，整个系统可能都会停止工作。为了解决这个问题，可以将主机应用程序与这些外部故障隔离开来。Hystrix库就是为此而设计的，通过添加延迟容忍和容错逻辑，帮助我们控制分布式服务之间的交互。Hystrix通过隔离服务、远程系统和第三方库之间的访问点来实现这一点。Hystrix可以帮助我们实现：<br>
<ul><li>阻止复杂分布式系统中的级联故障。</li><li>控制由于第三方客户端访问（通常通过网络）依赖项带来的延迟和故障。</li><li>快速失败、快速恢复。</li><li>在可能的情况下，回滚以及优雅降级。</li><li>启用近实时监控、警报和运维控制。</li><li>并发感知的请求缓存，通过请求崩溃实现自动批处理</li></ul><br>
<br><h3>数据库组件</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/c7482a26cf117f145b5248c44ceaaade.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/c7482a26cf117f145b5248c44ceaaade.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Netflix使用不同的DB来存储不同类型的文件，例如用于不同目的的SQL和NoSQL。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/14c4703975feca529bcd2d145b7182da.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/14c4703975feca529bcd2d145b7182da.jpeg" class="img-polaroid" title="20.jpeg" alt="20.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/0850585191299b1837515e3da6b67ab4.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/0850585191299b1837515e3da6b67ab4.jpeg" class="img-polaroid" title="21.jpeg" alt="21.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/d0675af82d744895bd714aa816b87f44.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/d0675af82d744895bd714aa816b87f44.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>MySQL</h4><ul><li>符合ACID，因此可用于管理影片标题、计费和事务用途。</li><li>在AWS EC2上部署MySQL来存储数据</li><li>MySQL配置为主主模式，在大型AWS EC2实例上使用InnoDB引擎构建。</li><li>设置遵循“同步复制协议（Synchronous replication protocol）”。数据复制是同步完成的，表明节点之间存在主主关系，只有当数据由本地和远程节点同步以确保高可用性时，才会认为主节点上的任何写操作已经完成。读查询不是由主节点处理，而是由副本处理，只有写查询是由主数据库处理。在故障转移的情况下，副节点将作为主节点，并将负责处理写操作。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/abe154a6f5c23e6915885a2797794639.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/abe154a6f5c23e6915885a2797794639.jpeg" class="img-polaroid" title="23.jpeg" alt="23.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/264801c53477b3444b14ad72f3ebd9ce.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/264801c53477b3444b14ad72f3ebd9ce.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Cassandra（NoSQL）</h4><ul><li>Cassandra是开源的、分布式的、基于列的NoSQL数据库，可以在服务器上存储大量数据。Netflix使用Cassandra来存储用户历史。它可以有效处理大量读请求，并优化大量读请求的延迟。随着用户群的增长，存储多行数据变得越来越困难，而且成本高且速度慢。所以，Netflix设计了基于时间框架和最近使用的新数据库。</li><li>当Netflix的用户越来越多时，每个用户的观看历史数据也开始增加。</li><li>更小的存储空间开销。</li><li>随着用户查看次数的增长而增长的一致性读写性能（在Cassandra中查看历史数据写读比约为9:1）。</li><li>非规范化数据模型</li><li>超过50个Cassandra集群</li><li>超过500个节点</li><li>每天超过30TB的备份数据</li><li>最大集群有72个节点</li><li>每个集群超过250K每秒写操作</li><li>最初，观看历史记录存储在Cassandra的单行中。当Netflix的用户越来越多，行数和总体数据大小都增加了。这导致了更高的存储成本、更高的操作成本和更低的应用程序性能。解决方案是压缩旧的行……</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/606f0173422472b57391e15bf9a3e378.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/606f0173422472b57391e15bf9a3e378.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>LiveVH（实时观看历史记录）——只保存更新频繁的最近的数据，以未压缩的形式存储较少的行，可用于许多分析操作，比如在执行ETL（提取，转换和加载）后对用户提供建议。</li><li>CompressedVH（压缩观看历史）——压缩后保存的用户浏览及观看历史旧数据，几乎不更新。存储大小也减少了，每行只存储一列。</li></ul><br>
<br>数据库定义：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/f4b2b6b10dfca0c5b474edee37f72b25.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/f4b2b6b10dfca0c5b474edee37f72b25.jpg" class="img-polaroid" title="26.jpg" alt="26.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>API</h3><h4>使用REST API</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/dd602e0521e1a68bcd157adaa3b5e1d5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/dd602e0521e1a68bcd157adaa3b5e1d5.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>用户注册</strong><br>
<br>请求：<br>
<pre class="prettyprint">POST /api/v1/users<br>
X-API-Key: api_key<br>
&#123;<br>
name:<br>
email:<br>
password:<br>
&#125; <br>
</pre><br>
通过HTTP POST方法，在数据库中创建一个资源或新条目。X-API-Key是传递给HTTP报头的API key，用于识别不同的客户端并进行速率限制。<br>
<br>响应：<br>
<pre class="prettyprint">201 Created<br>
&#123;<br>
message:<br>
&#125; <br>
</pre><br>
HTTP状态码201告诉用户已成功注册。用于失败情况的其他可能的HTTP状态码：<br>
<pre class="prettyprint">400 Bad Request<br>
409 Conflict<br>
500 Internal Server Error<br>
</pre><br>
<strong>用户登录</strong><br>
<br>请求：<br>
<pre class="prettyprint">POST /api/v1/users/session<br>
X-API-Key: api_key<br>
&#123;<br>
email:<br>
password:<br>
&#125; <br>
</pre><br>
响应：<br>
<pre class="prettyprint">200 OK<br>
&#123;<br>
auth_token:<br>
&#125; <br>
</pre><br>
API应该返回一个auth_token，它可以在header中传递给需要认证的后续API调用。auth_token可以使用JWT生成。<br>
<br><strong>用户登出</strong><br>
<br>请求：<br>
<pre class="prettyprint">DELETE /api/v1/users/session<br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
</pre><br>
使用HTTP DELETE方法删除数据库中的行条目，意味着我们正在终止一个会话。<br>
<br>响应：<br>
<pre class="prettyprint">200 OK<br>
</pre><br>
HTTP状态码200表示成功登出。<br>
<br><strong>订阅</strong><br>
<br>请求：<br>
<pre class="prettyprint">POST /api/v1/subscription<br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
</pre><br>
HTTP POST方法创建一个新的订阅，在Authorization头中传递auth-token来验证用户。<br>
<br>响应：<br>
<pre class="prettyprint">201 Created<br>
&#123;<br>
subscription_id:<br>
plan_name:<br>
valid_till:<br>
&#125; <br>
</pre><br>
HTTP状态码201与subcription_id、plan_name和valid_till一起在用户界面中呈现。<br>
<br>可能的HTTP失败状态码：<br>
<pre class="prettyprint">401 Unauthorized<br>
400 Bad request<br>
</pre><br>
<strong>取消订阅</strong><br>
<br>请求：<br>
<pre class="prettyprint">DELETE /api/v1/subscription<br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
</pre><br>
HTTP DELETE方法是可以取消订阅，该接口将从订阅数据库中删除一个行条目。<br>
<br>响应：<br>
<pre class="prettyprint">200 OK<br>
</pre><br>
HTTP状态码200意味着成功完成。<br>
<br><strong>批量获取视频</strong><br>
<br>请求：<br>
<pre class="prettyprint">GET /api/v1/videos?page_id=<page_id><br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
</pre><br>
该API用于在登录后呈现主页，包含了由机器学习模型确定的推荐视频。page_id用于API中的分页，next_page_id用于从下一页请求结果。<br>
<br>响应：<br>
<pre class="prettyprint">200 OK<br>
&#123;<br>
page_id:<br>
next_page_id:<br>
videos: [<br>
&#123;<br>
  id:<br>
  title:<br>
  summary:<br>
  url:<br>
  watched_till:<br>
&#125;,...<br>
]<br>
&#125; <br>
</pre><br>
HTTP状态码200表示操作成功。<br>
<br>其他故障状态码：<br>
<pre class="prettyprint">401 Unauthorized<br>
500 Bad request<br>
429 Too many requests<br>
</pre><br>
HTTP状态码429意味着用户达到速率限制，需要等待一段时间才能再次发出请求，以避免拒绝服务攻击。<br>
<br><strong>搜索API</strong><br>
<br>请求：<br>
<pre class="prettyprint">GET /api/v1/search?q=<query>&page_id=<page_id><br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
</pre><br>
通过标题搜索视频。<br>
<br>响应：<br>
<pre class="prettyprint">200 OK<br>
&#123;<br>
page_id:<br>
next_page_id:<br>
videos: [<br>
&#123;<br>
  id:<br>
  title:<br>
  summary:<br>
  url:<br>
  watched_till:<br>
&#125;,...<br>
]<br>
&#125; <br>
</pre><br>
HTTP状态码200表示操作成功，响应中包括了id、title、summary、url和watched_till等信息，不过也有可能找不到相关视频。<br>
<br><strong>获取视频</strong><br>
<br>请求：<br>
<pre class="prettyprint">GET /api/v1/videos/:video_id<br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
</pre><br>
<br>播放特定视频。<br>
<br>响应：<br>
<pre class="prettyprint">200 OK<br>
&#123;<br>
id:<br>
title:<br>
summary:<br>
url:<br>
watched_till:<br>
&#125; <br>
</pre><br>
HTTP状态码200表示匹配到了视频。<br>
<br>其他故障状态码：<br>
<pre class="prettyprint">401 Unauthorized<br>
404 Video not found<br>
429 Too many requests<br>
500 Internal server error<br>
</pre><br>
<strong>上传API</strong><br>
<br>请求：<br>
<pre class="prettyprint">POST /api/v1/videos<br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
&#123;<br>
title:<br>
summary:<br>
censor_rating:<br>
video_contents:<br>
&#125; <br>
</pre><br>
从后台上传视频。<br>
<br>响应：<br>
<pre class="prettyprint">202 Accepted<br>
&#123;<br>
video_url:<br>
&#125; <br>
</pre><br>
HTTP状态代码202表示视频已经排队进行异步处理和质量检查，处理结果可以通过电子邮件或其他告警机制发送给用户。<br>
<br>一些HTTP失败的场景：<br>
<pre class="prettyprint">401 Unauthorized<br>
400 Bad request<br>
500 Internal server error<br>
</pre><br>
<strong>更新观看时间戳</strong><br>
<br>请求：<br>
<pre class="prettyprint">PUT /api/v1/videos/:video_id/watched_till<br>
X-API-Key: api_key<br>
Authorization: auth_token<br>
&#123;<br>
watched_till:<br>
&#125; <br>
</pre><br>
之所以使用HTTP PUT方法，是因为我们需要用其他数据替换同一个数据库表中的行条目，或者我们需要更新服务器上的资源。这个API将用于更新时间戳，直到用户看完了特定的视频。<br>
<br>响应：<br>
<pre class="prettyprint">200 OK<br>
</pre><br>
HTTP状态码200表示操作成功。<br>
<br>其他HTTP失败状态码：<br>
<pre class="prettyprint">401 Unauthorized<br>
400 Bad request<br>
500 Internal server error<br>
</pre><br>
<h3>微服务架构</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/b3eedacf42b6159fe16db50f37b85b50.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/b3eedacf42b6159fe16db50f37b85b50.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/d14e49f1672de7ef388aef4678d41d1d.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/d14e49f1672de7ef388aef4678d41d1d.jpeg" class="img-polaroid" title="29.jpeg" alt="29.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
由于服务中的任何更改都可以很容易完成，因此微服务可以更快的完成部署。可以跟踪每个服务的性能，如果有任何问题，则可以快速将其与其他正在运行的服务隔离开来。<br>
<ol><li>关键服务——为经常与该服务交互的用户提供服务。这些服务独立于其他服务，以便在进行任何故障转移时，用户可以继续执行基本操作。</li><li>无状态服务——向客户端提供API请求，即使有任何服务器出现故障，也可以继续与其他实例一起工作，从而确保高可用性。例如，REST API服务为最多的用户提供服务。</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/bc878a34b0fd759df10460080676819f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/bc878a34b0fd759df10460080676819f.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>上传内容</h4>上传的内容是视频格式的电影或剧集，处理单元包括了输入协议、输入编解码器、输出编解码器和输出协议，以服务于各种设备和不同的网络速度。当我们在高速网络上观看视频时，视频的质量很好。Netflix为同一部电影创建不同分辨率的多个副本（大约1100-1200个）。Netflix将原始视频分成不同的小块，并在AWS中使用并行工作单元将这些小块转换成不同的格式。这些处理单元用于编码或转码，即将视频从一种格式转换为另一种格式，如改变分辨率，高宽比，减少文件大小等。在转码之后，一旦我们拥有同一电影的多个文件副本，这些文件就被传输到Open connect服务器。<br>
<h3>系统架构概要设计</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/57d5ecabd298499392eef0bb36d29539.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/57d5ecabd298499392eef0bb36d29539.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>数据架构</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/6d0a2499f6fc017b6b3bfd8cbaab4373.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/6d0a2499f6fc017b6b3bfd8cbaab4373.png" class="img-polaroid" title="32.png" alt="32.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/c9b47936921c41ee69e9b87abcada22c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/c9b47936921c41ee69e9b87abcada22c.png" class="img-polaroid" title="33.png" alt="33.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/60923ade505460b5d8a17e593e1bea84.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/60923ade505460b5d8a17e593e1bea84.jpeg" class="img-polaroid" title="34.jpeg" alt="34.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>电影推荐</h3><ul><li>电影推荐使用Apache Spark和机器学习。当载入所观看的首页时，会有好几行不同类型的电影。</li><li>Netflix希望用户最大限度的点击视频，而这些点击取决于标题图像。Netflix必须为特定的视频选择正确的引人注目的标题图像。为了做到这一点，Netflix为一部特定的电影创建了多个艺术作品，并随机向用户展示这些图像。对于同一部电影，不同的用户可以使用不同的图像。根据用户的喜好和观看历史，Netflix会预测用户最喜欢哪类电影，或者最喜欢哪位演员。Netflix将根据用户的口味，显示合适的图像。</li><li>Netflix会分析数据，从而决定应该向用户展示什么样的电影，这是基于用户的历史数据和偏好计算的。此外，Netflix还会对电影进行排序，并计算这些电影在其平台上的相关性排名。大多数机器学习流水线都运行在这些大型Spark集群上，然后使用这些流水线进行选择、排序、标题相关性排名和艺术品个性化等操作。当用户打开Netflix的首页时，用户就会被每个视频显式的图像所吸引。</li><li>现在，Netflix还会计算特定图像被点击的次数。如果电影的中心图像的点击量是1500次，而其他图像的点击量更少，那么Netflix就会让中心图像永远作为电影《心灵捕手》的标题图像。这被称为数据驱动，Netflix用这种方法执行数据分析。为了做出正确的决策，需要根据与每张图片关联的访问数量计算数据。</li><li>用户与服务的交互（观看历史记录以及评价）。</li><li>有相似品味和喜好的其他用户。</li><li>用户先前观看的视频的元数据信息，如标题、类型、类别、演员、发行年份等。</li><li>用户的设备、活跃时间以及活跃时长。</li><li><br>两种类型的算法：  <br>
<ul><li>协同过滤算法：这种算法的思想是，如果两个用户有相似的评级历史，那么他们将在未来的行为相似。例如，假设有两个人，一个人喜欢这部电影，给它打了高分，那么另一个人也很可能会喜欢这部电影。  </li><li>基于内容的推荐：这个算法的思想是，过滤那些与用户之前喜欢的视频相似的视频。基于内容的过滤高度依赖于电影名称、发行年份、演员、类型等信息。因此，要实现这种过滤，重要的是要知道描述每个项目的信息，还需要一些描述用户喜好的用户配置文件。</li></ul></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/e43f4fd89eabbd660595d88b3175fad8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/e43f4fd89eabbd660595d88b3175fad8.png" class="img-polaroid" title="35.png" alt="35.png" referrerpolicy="no-referrer"></a>
</div>
<br>
译文链接：<a href="https://mp.weixin.qq.com/s/NukLmTlhbGVXQ5SnovajZQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/NukLmTlhbGVXQ5SnovajZQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            