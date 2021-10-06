
---
title: '百度信息流和搜索业务中的KV存储实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/a33dc1e11622b551b513a726378e7ddb.jpg'
author: Dockone
comments: false
date: 2021-10-06 03:08:40
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/a33dc1e11622b551b513a726378e7ddb.jpg'
---

<div>   
<br>【编者的话】近年来，云原生化、全用户态、软硬协同等技术对KV存储服务产生了巨大的影响，上述技术在极大提升了服务的性能和降低服务成本的同时，也对系统的架构和实现提出了新的要求。百度在信息流和搜索业务中大量使用了KV存储服务，服务每天响应近千亿次各类访问请求，如何运用上述技术提升系统的性能、稳定性和运维人效是我们重点考虑的问题。本文通过介绍我们应用上述技术打造高性能KV存储系统的实践过程，为大家分享了我们在单机性能优化，大规模集群设计、管理等方面的思路和实践经验。<br>
<br>自2016年起，百度进入『搜索+信息流』双引擎驱动构建内容生态的“信息分发2.0时代”，搜索、推荐的内容也不再局限于网页，而是引入越来越多的视频、图片、音频等多媒体资源。KV存储作为在搜索和推荐中台中被广泛使用的在线存储服务，更是受到了存储规模和访问流量的双重考验。<br>
<br>至2018年初，我们投入各类KV存储服务的服务器数量便超过万台，数据规模超过百PB，承接了每天近千亿次的各类访问请求。集群规模的增长除了资源成本的提升，还加剧了运维管理的难度。作为有状态服务，集群的故障机处理、服务器升级、资源扩缩容都需要专人跟进，运维人力随集群规模呈正比增长。彼时又逢推荐业务完成了微服务化改造，业务资源交付和上线都能当天完成，存储资源动辄周级的交付能力也成了业务上线效率的瓶颈。<br>
<br>这些都促使我们对原来的系统架构进行彻底升级，通过提升单机引擎性能和云原生化有效降低资源成本和运维人力成本。同时我们还要满足业务对服务的敏捷性要求，通过云基础设施提供的资源编排能力，使系统具备小时级服务交付能力。<br>
<h3>问题与挑战</h3><h4>性能挑战</h4>单机引擎性能是KV系统的关键指标，一般我们通过读写性能（OPS、延时（latency））和空间利用率来衡量引擎的性能，由于当前引擎架构和存储设备硬件性能的制约，我们在引擎中往往只能选择读性能、写性能和空间利用率中某个方向进行重点优化，比如牺牲空间利用率提升写吞吐，或者牺牲写吞吐、提升空间利用率和读吞吐。<br>
<br>这类优化对于业务单一的场景比较有效，之前我们的系统就针对大业务场景进行逐一调参优化，针对其他业务则使用读写性能和空间利用率均衡的『均衡型』引擎接入。<br>
<br>但是百度的信息流和搜索业务规模都非常庞大、业务场景极其复杂，我们接入的数千个业务中有每天更新PB级数据的业务，也有读写比超过100:1的业务，还有要求强一致性、存储规模数十PB的业务，不少业务还会体现出潮汐特性，全天流量都集中在某个特定时段。<br>
<br>因此我们通过引擎优化，既要解决如何在降低读写放大的同时，尽可能平衡空间放大的问题；又要在引擎内实现自适应机制，解决业务充分混布场景下，吞吐模式多变的问题。<br>
<h4>云原生化挑战</h4>云原生架构的主要价值在于效率的提升，包括<strong>资源利用效率和研发效率两个方面。</strong><br>
<br>百度信息流和搜索业务对其业务模块制定了统一的云原生化标准：<br>
<ol><li><strong>微服务化</strong>：每个服务粒度应该在限定的范围内。</li><li><strong>容器化封装</strong>：一个服务的部署，应该只依赖基础架构以及本容器内的组件，而不应该依赖其他业务服务。</li><li><strong>动态管理</strong>：每个服务应该可以动态调整部署，而不影响自身对外承诺的SLA。</li></ol><br>
<br>KV服务在对齐上述标准的过程中，主要难点在于<strong>容器化改造和动态管理两个方面。</strong><br>
<br>容器化改造方面，单机时代的KV服务以用满整机资源为目标，对内存资源和存储介质IO的使用往往不加任何限制。引擎的容器化改造，要求我们精细化控制对上述资源的使用：<br>
<ol><li><strong>内存资源</strong>：存储引擎除了显式使用系统内存，更多的是对page cache的使用，文件系统中诸如Buffered I/O和文件预读都会产生page cache。我们需要在引擎中对其加以控制，避免超过容器配额触发硬限。</li><li><strong>存储介质I/O</strong>：KV服务的主要介质是SSD，我们不少业务也需要使用SSD提升读写性能，这些业务本身往往只需要不到100GB，因此为了提升SSD的使用率，KV服务需要和这些业务进行混布。这也要求我们不但能有效利用SSD I/O，还要能对I/O加以控制，避免影响混布业务。</li></ol><br>
<br>动态管理则要求业务具有一定的容错能力和弹性伸缩能力，由于KV是典型的有状态服务，兼具了数据持久化、多分片、多副本等特点，我们在动态管理中需要关注：<br>
<ol><li><strong>服务可用性</strong>：与无状态服务不同，多分片服务不能看服务的整体可用性，而要确保每个分片都可用。比如一个服务有10个分片，每个分片有3个容器，服务整体可用度为90%。从无状态服务视角2个容器故障不会影响服务可用性，但是从KV服务视角，如果这两个容器正好服务同一个分片的两个数据副本，那么该服务就会出现数据不可用问题。因此服务在持续部署时，需要确保每个数据分片的可用性。</li><li><strong>数据可靠性</strong>：云原生化后为了提升资源利用率，在线数据迁移和动态伸缩频率将远高于物理机时代，数据的动态伸缩过程需要对业务透明，也不能出现数据丢失或一致性问题。</li><li><strong>管理效率</strong>：确保管理服务能即时响应管理操作，对系统的稳定性起着关键作用。随着集群规模的增加，并发的管理操作数量也会增加，如果响应操作的时间也逐渐增加，最终将导致系统雪崩，因此我们需要系统响应管理操作的能力也能水平伸缩。</li><li><strong>部署效率</strong>：KV服务的部署包括部署应用和完成数据迁移，因此我们不但要在功能上做到可迁移，还要确保数据迁移的效率。比如一个有100个实例的服务，如果迁移一个实例要12个小时，且每轮只允许迁移1个实例，遇到内核升级、操作系统升级等需要重启的操作，全服务迁移一轮就需要1个半月，这样的效率还不如人工操作。这样的服务就不能算支持动态管理，因为没有在线操作可以容忍这样低的迁移效率。</li></ol><br>
<br><h4>满足业务的特化需求</h4>之前也提到百度的信息流和搜索业务规模都非常庞大，一些大业务根据自身场景已经做了单机引擎的特化，有些特化还涉及修改Linux内核，通用引擎在性能上无法超越这些特化引擎，这就要求能从业务中提取共性，同时允许其保留特性，使业务团队能在<strong>资源利用效率和研发效率两个方面都获得收益</strong>。<br>
<br>为此我们提出了UNDB - NoSQL联合存储系统（United NoSQL Database）的概念，兼顾统一通用能力与保持业务特性：<br>
<ul><li><strong>统一框架</strong>：使用统一的云原生存储框架，打平各系统的运维、集群管理差异，同时打破原有的资源屏障。</li><li><strong>通用接口</strong>：各KV服务剥离业务协议，对齐基本KV接口协议，对用户提供基于基本KV接口封装的SDK，使业务可以在各服务间平滑迁移，降低学习成本。</li><li><strong>通用引擎</strong>：自研高性能通用KV引擎，便于其他NoSQL服务在此之上实现高性能的存储服务。</li><li><strong>分层可插拔架构</strong>：通过可插拔的接口层、数据模型层、数据同步层、引擎层设计，使接入系统能快速实现业务特性化差异。</li></ul><br>
<br><h3>引擎优化</h3>引擎是KV系统的核心组件，鉴于RocksDB在开源社区和工业界的广泛应用，我们一开始便直接使用RocksDB作为单机引擎。基于LSM-Tree实现，RocksDB在HDD介质上有良好的性能，但在SSD介质上的性能表现却并不出众，主要问题在于：<br>
<ul><li>RocksDB在设计实现中,为了避免随机I/O，增加了大量顺序I/O开销（读放大、写放大），而SSD介质的随机I/O尤其是随机读性能和顺序I/O差距不大，因此针对HDD介质的优化在SSD介质中反而造成了读写带宽浪费。</li><li>上述额外的I/O开销所产生的高写放大，还增加了SSD介质的寿命损耗，在高吞吐环境中，新盘的平均使用寿命不足2年。</li><li>LSM-Tree结构对业务数据长度也十分敏感，由于每层SST文件大小是固定的，数据长度越大，越容易触发Compaction，从而造成写放大；同时数据长度越大，每层SST文件能记录的数据条目数就越少，读请求向下层访问概率就越高，从而造成了读放大。</li></ul><br>
<br>我们业务场景中的value一般在KB ~ 百KB级别，为了降低LSM-Tree的写放大，我们在RocksDB基础上实现了Key-Value分离的单机存储引擎，如下图左侧引擎结构所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/a33dc1e11622b551b513a726378e7ddb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/a33dc1e11622b551b513a726378e7ddb.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1：普通引擎与基于OpenChannel SSD的软硬协同引擎的架构对比</em><br>
<ul><li>在RocksDB中存储Key和Value的地址索引（BlockID+Offset），RocksDB的Compaction只影响到索引，不会引起Value的变动。</li><li>Value单独持久化，我们称之Data Block文件，Data Block文件单独进行Compaction。</li></ul><br>
<br>为了进一部提升引擎的I/O效率，我们又对Compaction策略和压缩方式进行了优化：<br>
<ul><li><strong>自适应Compaction机制：</strong>综合引擎I/O和剩余存储空间，调节对Block文件空洞率的选择阈值，实现流量规避、动态调节空间放大能力。</li><li><strong>冷热分层：</strong>减少冷热混合导致的不必要Compaction，并选择流量空闲时段对冷数据进行Compaction，降低触发SSD静态磨损均衡频率。</li><li><strong>全局压缩：</strong>在Block File粒度支持了zstd-dict压缩方式，进一步提升了Block文件的压缩率。</li></ul><br>
<br>此外，我们在引擎中为同步框架封装了Log View，实现数据同步与引擎复用，WAL降低了数据同步造成的写放大。<br>
<br>通过上述优化，在软件层面，我们在空间放大 ＜1.6x的情况下，将写放大控制到了 ＜ 1.5x。在业务持续以30MB/s更新数据的场景下，单盘寿命由之前的半年内提升至3年左右。<br>
<br>但是，SSD的写放大并不限于软件层，物理特性决定其不支持覆盖写，只能先擦除旧数据再写入新数据，大部分SSD按4KB（Page）写入、按256KB ~ 4MB（Block）擦除数据。SSD在擦除一个Block时，需要迁移Block中仍然有效的Page，这个迁移动作导致了SSD硬件层的写放大，硬件层写放大又与SSD剩余空间密切相关，一般情况下，当SSD容量使用达90%时，写放大会超过3.5x。<br>
<br>细心的同学或许会发现，我们之前在计算SSD寿命时并没有提到这部分放大，这里其实包含了SSD厂商的优化：SSD介质的实际容量单位是GiB（Gibibyte），1GiB = 230bit，提供给用户的指标则是GB（Gigabyte），1GB = 109  bit，前者比后者多了7.374%的空间，被厂商用作了内部操作空间。加之我们在实际使用时，也会保持磁盘用量不超过80%，因此可以控制写放大。但是这些策略其实牺牲了SSD的容量。<br>
<br>为了进一步发掘设备潜能，我们和百度的基础架构部门合作，基于Open Channel SSD实现了一款软硬协同设计的引擎，如上图右侧引擎结构所示与传统用法相比：<br>
<ul><li>实现了全用户态I/O操作，降低了引擎读写延迟；</li><li>引擎直接管理Flash物理地址，避免了文件系统、LBA、PBA三层映射造成的性能损失和空间浪费；</li><li>将FTL中Wear Leveling、GC、PLP、Error Handling上移至引擎，和KV原有的Compaction，Crash Recovery逻辑合并，合并了软、硬两层操作空间。</li></ul><br>
<br>软硬协同引擎在性能上超过软件引擎 ＞ 30%，软硬整体放大率 ＜ 1.1x。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/2f00b48d037407b88f31a4563a76b055.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/2f00b48d037407b88f31a4563a76b055.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2：引擎性能对比，依次为：数据加载性能、读写吞吐（读写1：1）、99分位写延时、99分位读延时</em><br>
<br>上图是我们实现的KV分离引擎（Quantum）、软硬协同引擎（kvnvme）和开源Rocksdb在数据加载、随机读写场景下的性能对比。<br>
<br>测试中我们选用：NVME 1TB SSD（硬件指标：4KB随机写7万IOPS，随机读46.5万IOPS）。数据集选用：1KB、4KB、16KB和32KB共4组，每组数据集都随机预构建320GB初始数据，再采用齐夫分布（Zipf）进行读写测试，读写测试时保持读写比为1：1。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/635822b67ff16e6db5a7a3b5ba23f3bb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/635822b67ff16e6db5a7a3b5ba23f3bb.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从测试结果可以发现：<br>
<ul><li>Value越大，KV分离引擎和软硬协同引擎的读写优势就越为明显，在32KB时软硬协同引擎的吞吐是RocksDB的近5x。</li><li>软硬协同引擎在读写延时控制上，尤其是写延时控制上也明显优于其他引擎。</li></ul><br>
<br><h3>云原生实践</h3>上节中我们通过引擎优化重构解决了业务混布性能和容器化问题，这节将介绍一下我们是如何解决动态管理问题。<br>
<br>UNDB服务整体框架如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/d10dffe853f9d74545963393f01b3124.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/d10dffe853f9d74545963393f01b3124.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3：UNDB系统框架</em><br>
<br>架构上我们将服务分成了Operator（数据调度）、控制面和数据面三部分：<br>
<ul><li><strong>Operator</strong>：负责向PaaS传递控制面和数据面中所有容器的状态信息和进行用户数据调度</li><li><strong>控制面</strong>：包括元信息服务、集群控制服务、接入管理服务、路由服务和用户数据中心，负责管理一个IDC（Internet Data Center）中的所有存储集群（Store Clusters）和用户发现、接入存储集群的路由映射关系，不同IDC间部署不同的控制面服务。</li><li><strong>数据面</strong>：IDC中KV服务管理的所有存储集群的集合。存储集群按存储设备类型（比如：NVMe SSD、SATA SSD、OpenChannel SSD、HDD、……），存储机制的容量，引擎类型，以及引擎使用的CPU、内存资源数量进行划分。</li></ul><br>
<br>我们在系统设计、实现中主要考虑如何实现数据全局调度能力和海量存储实例的动态管理能力。<br>
<h4>数据全局调度能力</h4>数据全局调度指：<br>
<ul><li>用户数据可以在数据面中的不同存储集群间任意迁移、扩缩容。</li><li>用户数据可以在不同数据中心间任意迁移、复制。</li></ul><br>
<br>这种能力的意义在于：<br>
<ul><li>当业务形态、引擎技术和存储设备发生变化时，我们能用对业务无感的方法将数据迁移到合适的集群中。</li><li>当部门新建数据中心，业务新增、切换数据中心，或是数据中心数据恢复时，我们能以最低的运维成本实施数据迁移、恢复。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/5f8d9c1f6a9dc316bc76e832c88e8357.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/5f8d9c1f6a9dc316bc76e832c88e8357.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4：Table在UNDB集群间迁移示意</em><br>
<br>如上图（图4）所示，全局调度由Operator发起，通过控制面协调数据面中的存储实例完成操作，其中：<br>
<ul><li>元信息服务和集群控制服务，为Operator对用户数据进行全局调度从底层机制上提供了无损迁移和无损伸缩能力。</li><li><strong>数据中心：</strong>通过分析存储集群的流量、容量分布和业务数据的流量、容量增长趋势，向Operator提供了全局调度方案。</li><li><strong>Operator：</strong>基于Kubernetes Operator框架实现，通过声明式原语，引导控制面完成数据迁移。</li></ul><br>
<br>基于上述能力，我们除了支持即时集群容量均衡和即时业务容量调整，还实现了周级机房建设、搬迁。<br>
<h4>海量存储实例的动态管理能力</h4>之前提到我们在动态管理中需要关注服务可用性、数据可靠性、管理效率和部署效率，上节中我们通过引擎优化实现了小时级完成TB数据的迁移、恢复。这里我们将关注如何在动态管理中确保服务的可用性、数据可靠性和管理效率。<br>
<br>业务访问KV服务的过程可以简单概括为：<br>
<ol><li>业务通过路由发现数据所在的存储节点。</li><li>访问存储节点获取数据。</li><li>数据和存储节点映射关系发生变更时，通知业务更新路由。</li></ol><br>
<br>我们在数据面中：<br>
<ul><li>按3-2-1原则确保数据安全。</li><li>使用Multi-Raft确保数据一致性。</li><li>采用多地多活确保重要业务的可用性。</li></ul><br>
<br>由于数据中心间的元信息不尽相同，尤其是拓扑信息完全不同，且拓扑信息具有极强的时效性，冷备效果并不好，因此对于控制面我们采用了利用数据面，集群控制服务多级兜底的思路，如下图（图5）所示：<br>
<ul><li>冷备机制：对于低频更新的元信息，诸如业务数据属性、配额实时备份SQL数据库。</li><li>反向恢复机制：利用集群控制服务和存储集群都有拓扑镜像的特点，支持通过上述服务反向恢复拓扑信息。</li><li>异变拦截机制：在控制面、数据面及业务端（Client）拦截异常变更，避免拓扑异常时，服务迅速异常雪崩。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/5d9ac2c26a61b765f618cf3cde75d564.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/5d9ac2c26a61b765f618cf3cde75d564.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5：元信息多级拦截、反向恢复</em><br>
<br>另外我们还通过独立的路由服务向业务屏蔽了元信息服务，业务间通过多组路由服务进行物理隔离。并通过接入管理服务管理业务和路由服务间的映射关系，这样可以有效防止由于某个业务的异常访问（比如：连接泄露）影响其他业务的路由访问。<br>
<br>在提升管理效率方面，我们主要采用了元信息和集群控制分离的设计，由于元信息服务需要确保节点间数据一致性，我们的数据修改操作只能在Leader节点上进行，如果不采用分离设计，所有控制操作只有Leader节点才能进行，当集群规模和数量增加后，无法通过水平扩容节点增加控制面算力，因此我们选用了两种模块分离的方法，使控制面具备水平伸缩控制算力的能力以应对超大规模集群。<br>
<h3>多模型存储架构</h3>NoSQL概念发展至今，业界已经出现了数百种不同的开源和商业NoSQL数据库，当业务发展到一定程度，对标准数据库进行改造，使其更适合业务模型的需求也变得越来越普遍。因此我们在整合KV系统时，提出了整合通用功能保留业务特性的设计思路。在这个思路指导下，我们统一了控制面，用于实现统一的运维管理，数据面则分成了3个功能模块、6个分层向业务开放了对服务接口、数据模型、存储模式、以及对同步框架的定制化能力，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210930/67c5dfd1052f95df9cbe8258781e8a15.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210930/67c5dfd1052f95df9cbe8258781e8a15.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6：UNDB多模型存储架构</em><br>
<ul><li><br><strong>DbProxy模块</strong>：整个架构的第一层，是一个独立部署的模块，DBProxy是对所有代理存储节点（Store Node）的Proxy服务的总称，按功能不同还有诸如KvProxy，GraphProxy等，该模块主要用于：<br>
<ul><li><strong>分担存储节点（Store Node）访问压力</strong>：当业务存在大量的Fanout读，或离线任务（map reduce任务）存在大量写连接时，通过Proxy可以减少对存储节点的压力;</li><li><strong>减少上下游连接开销</strong>：主要用于超大规模业务，比如搜索业务的一张索引表就分布在上万个实例中，这也意味访问该表的每个下游都要维护上万个连接，因此需要通过Proxy减少客户端的连接开销。</li><li><strong>存算分离</strong>：当前通过NVMe-OF、RDMA技术网络已经不是系统的主要瓶颈，像图数据库这样的服务，一次请求需要访问多个存储节点才能完成，还需要通过本地缓存构建子图加速业务查询速度，整合在存储节点中几乎无法带来的性能收益，还容易出现热点查询，因此我们也通过Proxy实现存算分离。</li></ul></li><li><br><strong>libNode模块</strong>：该模块承担了存储节点的业务逻辑、节点管理和数据同步：<br>
<ul><li><strong>分布式管理层</strong>：通过CtrlService向业务提供了一组响应分布式状态管理的核心原语，并提供了默认原语实现。</li><li><strong>接口协议层 & 数据模型层</strong>：提供KvService作为所有服务共同遵守的最简KV协议，开放服务注册和模型层（Module）供业务组织管理自己的定制化服务接口以及数据结构。为了能让模型使用适应不同引擎，我们统一KV接口作为模型层的序列化反序列化接口。</li><li><strong>同步框架层</strong>：不同业务对服务的可用性、数据一致性的要求并不相同，比如用户模型关注可用性和吞吐能力，内容模型则关注读写延时和数据的强一致性。我们也针对业务的不同需求提供了最终一致性（高可用、高吞吐）、顺序一致（braft实现的一致性，介于最终一致和强一致性之间）和线性一致（强一致）三个层级的一致性保证，其中线性一致是我们在braft基础上，通过ReadIndex和LeaseRead算法满足的一致性语义。</li></ul></li><li><br><strong>引擎模块：</strong>也是6层架构中的最后一个分层『引擎层』，主要负责单机存储功能，与libnode共同组成了一个存储节点（Store Node）。上节提到的引擎优化，就是对这个模块的一系列优化工作。</li></ul><br>
<br><h3>总结</h3>UNDB系统自落地以来，已经覆盖了百度信息流和搜索主要业务场景，涉及集群规模数十万实例，每天承接了超过万亿次的各类访问流量，成本相较原先降低近50%。同时系统还保持着月级频率的全集群业务无感更新。在运维方面则实现了高度自动化，集群无专职运维，全部由研发团队自主管理。目前团队还在打造多模型数据库、单机性能优化、存储架构优化等方向持续努力，力求使UNDB具备更完善的业务生态。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/7lHja0Skf6bW6_FuerApkw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/7lHja0Skf6bW6_FuerApkw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            