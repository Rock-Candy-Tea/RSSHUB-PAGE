
---
title: 'CurveFS beta 版首发，Curve 锚定云原生软件定义存储'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1dfbbb4a1cb7c7a8605d24605b55c4c3bd3.png'
author: 开源中国
comments: false
date: Thu, 16 Dec 2021 11:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1dfbbb4a1cb7c7a8605d24605b55c4c3bd3.png'
---

<div>   
<div class="content">
                                                                                            <p>近日，Curve 开源存储社区发布了 CurveFS 的第一个 beta 版本，旨在解决 CephFS 在云原生场景下存在的一系列性能及功能问题，并提供了全新的部署工具 <span style="background-color:#ffffff; color:#333333">CurveAdm </span>，以简化用户对 Curve 集群的部署和管理。</p> 
<p>Curve 是由网易数帆发起的一款开源存储系统，定位于高性能、易运维、支持广泛场景的开源云原生软件定义存储系统。项目包括 CurveFS 和 CurveBS，其中 CurveBS 此前已经开源。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">CurveFS <span>beta 版地址：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#0052ff">https://github.com/opencurve/curve/releases/tag/v0.1.0-beta</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><strong>架构设计</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>CurveFS的架构如下图所示：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img height="1" src="https://oscimg.oschina.net/oscnet/up-1dfbbb4a1cb7c7a8605d24605b55c4c3bd3.png" width="1" referrerpolicy="no-referrer"><img alt height="502" src="https://oscimg.oschina.net/oscnet/up-bcf39a8d2b93a6ba8c3f48b219328125190.png" width="1239" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>CurveFS由三个部分组成：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>客户端curve-fuse，和元数据集群交互处理文件元数据增删改查请求，和数据集群交互处理文件数据的增删改查请求。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>元数据集群metaserver cluster，用于接收和处理元数据(inode和dentry)的增删改查请求。metaserver  cluster的架构和CurveBS类似，具有高可靠、高可用、高可扩的特点：</span></p> 
  <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:0; margin-right:0"><span>MDS用于管理集群拓扑结构，资源调度。</span></p> </li> 
   <li> <p style="margin-left:0; margin-right:0"><span>metaserver是数据节点，一个metaserver对应管理一个物理磁盘。</span><span>CurveFS使用Raft保证元数据的可靠性和可用性，Raft复制组的基本单元是copyset。</span><span>一个metaserver上包含多个copyset复制组。</span></p> </li> 
  </ol> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>数据集群data  cluster，用于接收和处理文件数据的增删改查。</span><span>data  cluster目前支持两存储类型：</span><span>支持S3接口的对象存储以及CurveBS（开发中）。</span></p> </li> 
</ol> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">核心特性</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>当前版本CurveFS主要具有如下特性：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>POSIX兼容:  像本地文件系统一样使用，业务可以无缝接入</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>高可扩：元数据集群规模可以线性扩展</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>高速缓存：客户端有内存和磁盘两级缓存加速</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持数据存储到S3接口的对象存储和CurveBS（开发中）</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left"><strong>Client</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>CurveFS的client通过对接fuse，实现完整的文件系统功能，称之为curve-fuse。curve-fuse支持数据存储在两种后端，分别是S3兼容的对象存储和Curve块存储中（其他块存储的支持也在计划中），目前已支持S3存储后端，存储到CurveBS后端尚在完善中，后续还可能支持S3和Curve块混合存储，让数据根据冷热程度在S3与Curve块之间流动。curve-fuse的架构图如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="371" src="https://oscimg.oschina.net/oscnet/up-eb483b4f9e3f8b25237f4ca37aecd0567c9.png" width="831" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><span>curve-fuse架构图</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>curve-fuse包含几个主要模块：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>libfuse，对接了其lowlevel fuse api，支持fuse用户态文件系统；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>元数据cache，包含fsinfo, inode cache, dentry cache, 实现对元数据的缓存；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>meta rpc client， 主要对接元数据集群，实现meta op的发送，超时重试等功能；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>S3 client， 通过对接S3接口，将数据存储在s3中；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>S3 data cache， 这是S3数据存储的缓存层，作为数据缓存，加速S3数据的读写性能；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>curve client 通过对接Curve块存储SDK，实现将数据存储在Curve块存储集群中；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>volume data cache，这是当数据存储在Curve块存储中的缓存层，以加速数据读写性能（开发中）；</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>c</span><span>urv</span><span>e-fuse现已对接完整的fu</span><span>se模块，基本实现<span>POSIX</span>的兼容，目前pjdtest测试通过率100%。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>S3存储引擎支持</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>S3 client负责将文件的读写语义转换成S3存储的数据读写（upload，download）语义。考虑到S3存储性能较差，我们在这一层对数据做了级缓存：内存缓存（dataCache）和磁盘缓存（diskCache），整体架构如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="602" src="https://oscimg.oschina.net/oscnet/up-1f9ad9e652ccfd5fa3e14fddbc18bb9e42b.png" width="584" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>S3ClientAdaptor主要包含以下几个模块：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(255, 255, 255, 0.01)">FsCacheManager：负责管理整个文件系统的缓存，包括inode到FileCacheManager的映射、读写cache大小统计和控制</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(255, 255, 255, 0.01)">FileCacheManager：负责管理单个文件的缓存</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(255, 255, 255, 0.01)">ChunkCacheManager：负责单个文件内某个chunk的缓存</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(255, 255, 255, 0.01)">DataCache：缓存管理的最小粒度，对应一个chunk内一段连续的数据空间。数据最终在DataCache这一层映射为S3存储的一个或多个对象，进行upoload</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(255, 255, 255, 0.01)">diskCache：负责本地磁盘缓存管理，数据持久化可以先写到本地磁盘上，再异步的写到S3存储上，能够有效的降低时延，提高吞吐</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="background-color:rgba(255, 255, 255, 0.01)">S3Client：负责调用后端的S3存储接口，目前使用的是AWS的SDK</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left"><strong>MDS</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>MDS是指元数据管理服务，CurveFS的MDS类似于CurveBS的MDS（CurveBS的MDS介绍：</span><span style="color:#003884">https://zhuanlan.zhihu.com/p/333878236</span><span>），提供中心化的元数据管理服务。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>CurveFS的MDS有以下功能：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>通过topology子模块，管理的整个集群的topo信息，以及整个topo的生命周期管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>通过fs子模块，管理fs的super block信息；提供文件系统的创建，删除，挂卸载，查询等功能；负责fs的inode、dentry等元数据在metaserver的分布</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>通过heartbeat子模块，维持和metaserver的心跳，并收集metaserver的状态</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>通过调度系统进行调度。curvefs的元数据使用一致性协议保证可靠性，当出现某副本不可用的时候，调度器会自动的进行recover。调度功能正在开发中</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>作为一个中心化的元数据管理服务，其性能、可靠性、可用性也十分重要。</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><strong>在性能上：</strong>首先，MDS上元数据都会全部缓存在内存里，加速其查找。其次，在fs创建之后，MDS会为fs分配用来保存inode、dentry信息的分片，在系统中，一个分片被称为一个partition。完成partition分配之后，fs的元数据操作会由client直接发向metaserver。此后的fs的inode、dentry的元数据管理并不经过MDS</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><strong>在可靠性和可用性上：</strong>MDS的元数据持久化到etcd中，依靠3副本的etcd保证元数据的可靠性。可以选择部署多个MDS服务，但是同时之后有一个MDS对外提供服务，当主MDS因为特殊原因挂掉之后，会在自动的在剩下的MDS中，通过选主算法选择一个新的主MDS继续提供服务</span></p> </li> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left"><strong>MetaServer</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>MetaServer是分布式元数据管理系统，为客户端提供元数据服务。文件系统元数据进行分片管理，每个元数据分片以三副本的形式提供一致性保证，三个副本统称为Copyset，内部采用Raft一致性协议。同时，一个Copyset可以管理多个元数据分片。所以，整个文件系统的元数据管理如下所示：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="461" src="https://oscimg.oschina.net/oscnet/up-b18f9084e983fc85e97023ece33c0d6b365.png" width="1639" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>图中共有两个Copyset，三个副本放置在三台机器上。</span><span>P1/P2/P3/P4表示文件系统的元数据分片，其中P1/P3属于一个文件系统，P2/P4属于一个文件系统。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>元数据管理</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>文件系统的元数据进行分片管理，每个分片称为Partition，Partition提供了对dentry和inode的增删改查接口，同时Partition管理的元数据全部缓存在内存中。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>Inode对应文件系统中的一个文件或目录，记录相应的元数据信息，比如atime/ctime/mtime。当inode表示一个文件时，还会记录文件的数据寻址信息。每个Parition管理固定范围内的inode，根据inodeid进行划分，比如inodeid [1-200] 由Partition 1管理，inodeid [201-400] 由Partition 2管理，依次类推。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>Dentry是文件系统中的目录项，记录文件名到inode的映射关系。一个父目录下所有文件/目录的dentry信息由父目录inode所在的Partition进行管理。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>一致性</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>文件系统元数据分片以三副本形式存储，利用raft算法保证三副本数据的一致性，客户端的元数据请求都由raft leader进行处理。在具体实现层面，我们使用了开源的braft(</span><span style="color:#003884">https://github.com/baidu/braft</span><span>)，并且一台server上可以放置多个复制组，即multi-raft。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>高可靠</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>高可用的保证主要来自两个方面。首先，raft算法保证了数据的一致性，同时raft心跳机制也可以做到在raft leader异常的情况下，复制组内的其余副本可以快速竞选leader，并对外提供服务。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>其次，Raft基于Quorum的一致性协议，在三副本的情况下，只需要两副本存活即可 。但是长时间的两副本运行，对可用性也是一个考验。所以，我们在Metaserver与MDS之间加入了定时心跳，Metaserver会定期向MDS发送自身的统计信息，比如：内存使用率，磁盘容量，复制组信息等。当某个Metaserver进程退出后，复制组信息不再上报给MDS，此时MDS会发现一些复制组只有两副本存活，因此会通过心跳下发Raft配置变更请求，尝试将复制组恢复到正常三副本的状态。</span></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><span style="background-color:#ffffff; color:#333333">CurveAdm</span></h2> 
<p><span style="background-color:#ffffff; color:#333333">此外，为了提升 Curve 的运维便利性，Curve 社区设计开发了 CurveAdm 项目，其主要用于部署和管理 Curve 集群，目前已支持部署 CurveFS（CurveBS 的支持正在开发中）。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>与之前的 Ansible 部署工具相比较，CurveAdm 带来了</span><span>如下优势：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持跨平台运行，独立打包无其他依赖，可以一键安装，易用性较好</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Curve组件运行在容器里，解决组件依赖问题和发行版适配问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>使用Golang开发，开发迭代速度快，可定制化程度高</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>可自助收集集群日志并打包加密上传给Curve团队，便于分析解决问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>本身支持一键自我更新，方便升级</span></p> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">当前版本是CurveFS的第一个beta版本，不建议在生产环境使用，但</span>读者<span style="background-color:#ffffff; color:#333333">可以抢先体验，并在GitHub上提交issue和bug，或者添加微信号opencurve邀请您入群交流。</span></p> 
<h2>未来规划</h2> 
<p>按照 Curve 社区的规划，Curve 将作为多种存储系统（如 HDFS、S3 兼容对象存储等）的统一存储层，接管并加速各系统访问。后续将支持接管多种存储系统，并进行统一的cache加速。</p> 
<p><img alt height="752" src="https://oscimg.oschina.net/oscnet/up-4d33c524c3aad0f51a2b49bc5bfe90e1b2a.png" width="1220" referrerpolicy="no-referrer"></p> 
<p>CurveFS 下个大版本的主要开发目标为（可能会根据实际需求进行部分调整）：</p> 
<ul> 
 <li>CurveBS存储引擎支持</li> 
 <li>数据跨引擎生命周期管理</li> 
 <li>CSI插件</li> 
 <li>部署工具完善</li> 
 <li>基于K8s集群部署：目前已经支持Helm部署方式，后续将继续优化，支持更高等级的云原生运维级别</li> 
 <li>多写多读</li> 
 <li>运维工具优化（监控告警、问题定位）</li> 
 <li>回收站</li> 
 <li>HDD场景适配优化</li> 
 <li>NFS、S3、HDFS等兼容性</li> 
 <li>快照</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">CurveFS更多细节详见：</span><a href="https://my.oschina.net/u/4565392/blog/5371485">https://my.oschina.net/u/4565392/blog/5371485</a></p>
                                        </div>
                                      
</div>
            