
---
title: '高性能、免运维，博云开源云原生本地存储方案：Carina'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/0952a55bb66b8bdefc378308e51f546a.jpg'
author: Dockone
comments: false
date: 2021-10-20 04:09:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/0952a55bb66b8bdefc378308e51f546a.jpg'
---

<div>   
<br>2021 年 10 月 11 日，博云正式开源 Carina 本地存储方案，Carina 基于 Kubernetes 及 LVM 实现，提供了数据库与中间件等有状态应用在 Kubernetes 中运行所必须的高性能的本地存储能力，极大减少了存储系统的运维压力。今年 9 月，Carina 还以首批成员身份加入了由中国信通院发起的可信开源社区共同体，并获得可信开源项目成员证书。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/0952a55bb66b8bdefc378308e51f546a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/0952a55bb66b8bdefc378308e51f546a.jpg" class="img-polaroid" title="博客图片.jpg" alt="博客图片.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Carina 最大的特点是高性能和免运维，为中间件、数据库等有状态服务提供了匹配本地磁盘的高 IOPS 和极低延迟的性能指标，同时易安装、自运维能力又极大的减轻了存储系统的运维压力。另外，Carina 还提供了本地磁盘管理能力、PV 高级调度能力、PV 自动分层技术、卷拓扑能力、自动 failover 能力、动态 IO 限速、监控告警、多种存储供给能力等高级功能。<br>
<br>目前， Carina 项目代码已在 Github 上开源，项目地址为：<a href="https://github.com/carina-io/carina" rel="nofollow" target="_blank">https://github.com/carina-io/carina</a>。欢迎广大技术开发者和爱好者前去试用。<br>
<br><h2>01 功能亮点</h2>灵活高效的供给高 IOPS、低延迟的存储<br>
免运维，自动管理本地磁盘、自动组建 RAID<br>
多种调度策略可配<br>
支持带宽 IOPS 限速<br>
支持 PV 数据自动分层<br>
支持 PV 自动扩容<br>
支持 RAID 管理能力<br>
支持容灾转移能力<br>
提供块和文件的访问方式<br>
<br><h2>02 Why Carina？</h2>Kubernetes 原生支持<br>
完全兼容的 Kubernetes API ，无需额外开发，依赖组件很少且均为通用开源组件。<br>
本地磁盘管理<br>
自动管理本地磁盘，提供 RAID 组建、数据分层、磁盘限速等高级功能。<br>
设备注册<br>
将本地磁盘注册为 Kubernetes 设备，参与容器调度评分。<br>
容灾转移<br>
支持在节点删除，将存储卷在其他节点重建。<br>
文件和块存储<br>
同时支持为容器提供文件存储和块存储，以及在线扩容。<br>
<br><h2>03 How it works</h2>云端是标准 Kubernetes 集群，可以使用任何 CSI 存储插件，比如 Ceph-CSI。在集群中运行 carina-controller carina-scheduler 在每个节点运行 carina-node。<br>
<br>Carina 主要有三部分组成，分别是 carina-controller、carina-scheduler 和 carina-node，其架构图如下所示：<br>
<br>如上图架构所示，Carina 能够自动发现本地裸盘，并根据其磁盘特性划分为 hdd 磁盘卷组及 ssd 磁盘卷组等，针对于本地数据高可用，Carina 推出了基于 bcache 的磁盘缓存功能以及自动组件 RAID 功能；<br>
<br>Carina-node 是运行在每个节点上的 agent 服务，利用 lvm 技术管理本地磁盘，按照类别将本地磁盘划分到不同的 VG 卷组，并从中划分 LV 提供给 POD 使用；<br>
<br>Carina-scheduler 是 kubernetes 的调度插件，负责基于申请的 PV 大小，节点剩余磁盘空间大小，节点负载使用情况进行合理的调度。默认提供了 spreadout 及 binpack 两种调度策略；<br>
<br>Carina-controller 是 Carina 的控制平面，监听 PVC 等资源，维护 PVC，LV 之间的关系。<br>
<br><h2>04 Carina VS Ceph-CSI / NFS-CSI</h2>Carina 不同于 Ceph-CSI，NFS-CSI 等 Kubernetes 网络存储插件。这些插件为网络存储插件，解决了应用在 Kubernetes 场景下数据跟随的问题，而 Carina 解决的是在数据库和中间件场景下对挂载设备高性能读写的问题。<br>
<br><h2>05 Carina 应用场景</h2>场景一：数据库 Redis、Mysql<br>
Redis 作为高性能的内存型数据库缓存服务，同样有数据落盘的需求，而使用网络存储往往有比较大延迟，在使用 Carina 情况下，能够提供和读写本地磁盘一致的性能。Redis 主从模式其本身已经解决了数据多地备份的问题，Carina 并不会提供更多冗余的数据备份，节省了磁盘空间。Mysql 作为严重依赖存储的数据库服务，使用 Carina 提供的存储卷使 Mysql 在云上运行可以获得更接近在物理机上运行的性能。<br>
<br>场景二：消息服务 rocketmq、activemq<br>
大多数消息中间件都是基于内存的，为了维持消息不丢失，消息中间件还是有落盘的需求，比如对于需要 ACK 应答的消息中间件，若是消息非常多，消息服务一般会选择将时间较久的消息落盘，对于消息中间件来说对磁盘性能要求可谓极高，Carina 恰恰提供了等同于本地磁盘的读写性能，且对于消息中间件并未有多副本存储需求，因此 Carina 也避免了存储多副本带来的性能消耗.<br>
<br>场景三：普通应用 POD<br>
Carina 的部署、运维、使用极其简易，可以被当做一般项目的本地存储使用，相当于 hostpath 。与 hostpath 不同的是 hostpath 要求在宿主机建立相关存储目录。Carina 则完全不用关心节点机器，直接创建原生 pvc 即可。<br>
<br><h2>06 Join Us</h2>Github：<a href="https://github.com/carina-io/carina"></a><a href="https://github.com/carina-io/carina" rel="nofollow" target="_blank">https://github.com/carina-io/carina</a><br>
官方网站: <a href="http://www.opencarina.io/"></a><a href="http://www.opencarina.io/" rel="nofollow" target="_blank">http://www.opencarina.io</a><br>
官方邮箱：<a href="mailto:carina@beyondcent.com">carina@beyondcent.com</a><br>
<strong>加粗文字</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            