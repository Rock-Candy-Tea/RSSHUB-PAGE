
---
title: '网易有道Redis云原生实战'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/160314c8cfd06fe1292fae1337a628c3.png'
author: Dockone
comments: false
date: 2021-12-29 09:08:24
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/160314c8cfd06fe1292fae1337a628c3.png'
---

<div>   
<br>【编者的话】本次以Redis为范例，阐述了有道基础架构团队在基础设施容器化道路上的实践，主要将从声明式管理，Operator工作原理，容器编排，主从模式，集群模式，高可用策略，集群扩缩容等方面展开。<br>
<h3>背景</h3>Redis是业务系统中较为常用的缓存服务，常用于流量高峰、数据分析、积分排序等场景，并且通过中间件可以实现系统之间的解耦，提升系统的可扩展性。<br>
<br>传统物理机部署中间件，需要运维人员手动搭建，启动时间较长，也不利于后期维护，无法满足业务快速发展的需求。<br>
<br>云原生相较于传统IT，<strong>可以助力业务平滑迁移、快速开发、稳定运维，大幅降低技术成本，节约硬件资源。</strong><br>
<br>云原生中间件是指依托容器化、服务网格、微服务、Serverless等技术，构建可扩展的基础设施，持续交付用于生产系统的基础软件，在功能不变的前提下，提高了应用的可用性与稳定性。<br>
<br>在这种大趋势下，有道基础架构团队开始了云原生中间件的实践，除了本文介绍的Redis，还包括Elasticsearch、ZooKeeper等。<br>
<h3>面临的挑战</h3>利用云原生技术可以解决当前Redis部署缓慢，资源利用率低等问题，同时容器化Redis集群也面临着一些挑战：<br>
<ul><li>Kubernetes如何部署Redis有状态服务；</li><li>容器Crash后如何不影响服务可用性；</li><li>容器重启后如何保证Redis内存中的数据不丢；</li><li>节点水平扩容时如何做到Slots迁移时不影响业务；</li><li>Pod IP变化后集群的状态如何处理。</li></ul><br>
<br><h3>声明式管理</h3>对于一个Redis集群，我们的期望是能够7x24小时无间断提供服务，遇故障可自行修复。这与Kubernetes API的声明式特点如出一辙。<br>
<br>所谓“声明式”，指的就是我们只需要提交一个定义好的API对象来“声明”我所期望的状态是什么样子，Kubernetes中的资源对象可在无外界干扰的情况下，完成当前状态到期望状态的转换，这个过程就是Reconcile过程。例如，我们通过yaml创建了一个Deployment，Kubernetes将“自动的”根据yaml中的配置，为其创建好Pod，并拉取指定存储卷进行挂载，以及其他一系列复杂要求。<br>
<br>因此，我们的Redis集群是否可以使用一个类似的服务去完成这个过程呢？即我们需要定义这样的对象，定义服务Reconcile的过程。Kubernetes的Operator刚好可以满足这个需求，可以简单的理解Operator由资源定义和资源控制器构成，在充分解读集群和Operator的关系后，我们将整体架构图设计如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/160314c8cfd06fe1292fae1337a628c3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/160314c8cfd06fe1292fae1337a628c3.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Operator集群本身采用Deployment部署，由etcd完成选主，上层与Kubernetes的API Server、Controller Manager等组件进行通信，下层持续调和Redis集群状态。<br>
<br>哨兵模式中Redis服务用一套哨兵集群，使用StatefulSet部署，持久化配置文件。Redis server也采用StatefulSet部署，哨兵模式的实例为一主多从。<br>
<br>集群模式中的每个分片使用StatefulSet部署，代理采用Deployment部署。原生Pod、StatefulSet、Service、调度策略等由Kubernetes本身负责。<br>
<br>Redis的资源定义在ETCD中存储一份即可，我们只需要预先提交自定义资源的yaml配置。如下所示为创建三个副本的Redis主从集群：<br>
<pre class="prettyprint">apiVersion: Redis.io/v1beta1<br>
kind: RedisCluster<br>
metadata:<br>
name: my-release<br>
spec:<br>
size: 3<br>
imagePullPolicy: IfNotPresent<br>
resources:<br>
limits:<br>
  cpu: 1000m<br>
  memory: 1Gi<br>
requests:<br>
  cpu: 1000m<br>
  memory: 1Gi<br>
config:<br>
maxclients: "10000"<br>
</pre><br>
其中，kind定义使用的CR名称，size为副本数，resources定义资源配额，config对应Redis Server的config，该定义存储在Kubernetes的etcd数据库中，后续的具体资源申请与使用由Operator的Controller完成。<br>
<h3>Operator工作原理</h3>Operator是Kubernetes的扩展模式，由CRD、Controller构成。它利用定制资源管理特定应用及其组件，Operator遵循Kubernetes的理念。<br>
<br>Operator无需任何修改，即可从Kubernetes核心中获得许多内置的自动化功能，如使用Kubernetes自动化部署和运行工作负载，甚至可以自动化Kubernetes自身。<br>
<br>Kubernetes的Operator模式可在不修改Kubernetes自身的代码基础上，通过控制器关联到一个以上的定制资源，即可以扩展集群的行为。Operator是Kubernetes API的客户端，核心功能是充当定制资源的控制器。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/c3dd5c318515f0ba688108907394dd6e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/c3dd5c318515f0ba688108907394dd6e.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
CRD：Custom Resource Definition，在Kubernetes中一切皆是资源，资源就是CRD，用户自定义的Kubernetes资源是一个类型，比如默认自带的由Deployment，Pod，Service等。<br>
<br>CR：Custom Resource是实现CRD的具体实例。<br>
<br>用户创建一个CRD自定义资源，ApiServer把CRD转发给webhook，webhook进行缺省值配置验证配置和修改配置，webhook处理完成后的的配置会存入etcd中，返回给用户是否创建成功信息。Controller会监测到CRD，按照预先写的业务逻辑，处理这个CRD，比如创建Pod、处理新节点与旧集群关系等，保证运行的状态与期望的一致。<br>
<h3>容器编排</h3>Redis集群在Kubernetes中的最小部署单位为Pod，因此在架构设计之前，需预先考虑Redis特性、资源限制、部署形态、数据存储、状态维护等内容，为不同类型的Redis集群配置合适的部署方式。<br>
<h4>资源限制</h4>Kubernetes采用request和limit两种限制类型来对资源进行分配。<br>
<br>request（资源需求）：即运行Pod的节点必须满足运行Pod的最基本需求才能启动。<br>
<br>limit（资源限制）：即运行Pod期间，可能内存使用量会增加，那最多能使用多少内存，这就是资源限额。<br>
<br>Redis基本不会滥用CPU，因此配置1-2个核即可。内存根据具体业务使用分配，考虑到部分场景下会fork较多的内存，例如aof频繁刷写，aof重写过程中，Redis主程序称依旧可以接收写操作，这时会采用copy on write（写时复制）的方法操作内存数据，若业务使用特点为“写多读少”，那么刷写期间将产生大量的内存拷贝，从而导致OOM，服务重启。<br>
<br>一个有效的解决方式为减少刷写次数，将刷写操作放在夜间低流量时段进行。减少刷写次数的方法为适当增加auto-aof-rewrite-min-size的大小，可配置使用内存的5倍甚至更大的最小刷写量；其次可以主动触发刷写，判断内存使用达到的配额两倍时进行刷写，实际部署时一般也会预留50%的内存防止OOM。<br>
<h4>部署的基本形态</h4>依据数据是否需要持久化或是否需要唯一标识区分服务为无状态和有状态的服务，Redis集群需要明确主从、分片标识，大部分场景也需要数据持久化，Kubernetes使用StatefulSet来满足这一类需求。StatefulSet的顺序部署、逆序自动滚动更新更能提高Redis集群的可用性。<br>
<br>具体的：<br>
<br>Redis Server使用StatefulSet启动，为标识为&#123;StatefulSetName&#125;-0的Pod设置Master角色，给其他Pod设置为该Master的从节点。<br>
<br>Proxy无需存储任何数据，使用Deployment部署，便于动态扩展。<br>
<h4>配置文件</h4>Redis Server启动时需要一些配置文件，里面涉及到用户名和密码，我们使用ConfigMap和Secret来存储的。ConfigMap是Kubernetes的API对象，常用于存储小于1MB的非机密键值对。而Secret可以用于存储包含敏感信息的密码、令牌、密钥等数据的对象。<br>
<br>两种资源均可以在Pod运行的时候通过Volume机制挂载到Pod内部。<br>
<h4>存储</h4>存储使用的是PVC（PersistentVolumeClaim）加PV（Persistent Volumes），PV为Kubernetes集群中的资源，由存储类StorageClass来动态供应，PV支持多种访问模式：ReadWriteOnce、ReadOnlyMany或ReadWriteMany，通过PV定义存储资源，PVC申请使用该存储资源。另外通过根据存储的StorageClass字段可抽象不同的存储后端，如Cephfs、Cephrbd、Openebs、LocalStorage等。<br>
<h3>主从模式</h3><h4>主从拓扑图</h4>Redis容器化后建立的每个CR表示一个完整的Redis服务，具体的服务模式包括哨兵模式和集群模式两种，在进行容器化过程中，除覆盖裸服务器部署结构外，也对架构进行了一定程度的优化。<br>
<br>原哨兵模式：<br>
<br>原哨兵模式为每套实例配一组哨兵。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/b8616f884ac0270b3b6a33edae9149e1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/b8616f884ac0270b3b6a33edae9149e1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
共用哨兵模式：<br>
<br>所有实例共用一组哨兵将进一步提高实例启动速度，并在一定程度上可提高硬件资源利用率，实测单组哨兵可轻松应对百规模的主从集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/d34b9c9c7abf392d231acf57a0063e52.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/d34b9c9c7abf392d231acf57a0063e52.png" class="img-polaroid" title="640.png" alt="640.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>调和原理</h4>Reconcile实现持续监测并对主从集群进行修复的功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/ca9098f05b33a8070301ac85a33d49fe.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/ca9098f05b33a8070301ac85a33d49fe.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li>检查是否按照预期启动了全部的Pod，比如创建3个Server，那么需要按照预期启动三个才能继续进行后面的操作。</li><li>检查Master的数量，确保该实例仅有一个主节点（数量为0主动选一个；数量大于1手动修复）。</li><li><br>检查哨兵：<br>
<ol><li>所有的哨兵是否监控了正确的Master；</li><li>所有的哨兵均知道相同的Slave；</li><li>再次检查哨兵的数量，确保哨兵均可用。</li></ol></li><li><br>检查Service，使Service的Endpoints指向正确的Master。</li><li>检查Redis config是否有做修改，有则对所有节点重写config参数。</li></ol><br>
<br><h3>集群模式</h3><h4>集群拓扑图</h4>Redis Cluster + Proxy模式：<br>
<br>通过在传统Redis Cluster架构中引入代理功能，实现动态路由分发，并基于Kubernetes原生动态扩缩容特性，更易应对突发流量，合理分配使用资源。<br>
<br>代理基础转发规则如下：<br>
<br>对于操作单个Key的命令，Proxy会根据Key所属的Slot（槽）将请求发送给所属的数据分片。<br>
<br>对于操作多个Key的命令，如果这些Key是储存在不同的数据分片，Proxy会将命令拆分成多个命令分别发送给对应的分片。<br>
<br>服务部署前，也对代理的部分功能进行了补充，例如移除不可用节点等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/5bceb30c4fd698040ed7054852ead82c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/5bceb30c4fd698040ed7054852ead82c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>调和原理</h4>reconcile实现持续监测并对Redis Cluster进行修复功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211227/35892191f958073a2708a817c982ff6a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211227/35892191f958073a2708a817c982ff6a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
确保集群健康的步骤：<br>
<ol><li>等待所有Pod状态变为Ready且每个节点相互识别后，Operator会在每个StatefulSet的Pod中挑选一个作为Master节点，其余节点为该Master的Slave。</li><li>获取实例集群所有Pod的IP、所有Pod的cluster info（包含nodeIP，主从关系等）。</li><li><br>进入恢复流程：<br>
<ol><li>处理失败节点，对部分节点重启后的无效IP、状态为noaddr的僵尸节点进行forget操作；</li><li>处理不可信节点（所有handshake状态的节点），发生于某一个节点被移除（由forget node触发），但试图加入集群时，即该Pod在Operator角度下存在，但实际集群节点并不需要该节点，处理方式为删掉这个Pod，并再次做forget操作直到Pod被删除。</li></ol></li><li><br>任选一个节点，使用CLUSTER MEET给该节点加入所有已知节点。</li><li>为StatefulSet中的Pod建立主从关系，同时给其分配Slots。若当前Master数量同预期不一致，则对应扩缩容操作，具体见’集群扩缩容’的横向扩缩容小节。</li><li>检查Redis config是否有做修改，有则对所有节点重写config参数。</li></ol><br>
<br>确保代理健康的步骤：<br>
<ol><li>获取所有Running状态代理的Pod IP。</li><li>从代理获取Redis Server信息，将集群信息同步到所有的代理上，代理中不存在的Server IP做移除操作。</li><li>若代理中无可用Redis Server，表示被全部移除，则添加一个，代理可自动发现集群其他Redis节点。</li></ol><br>
<br><h3>高可用策略</h3><h4>Kubernetes保证的高可用</h4>容器部署保证高可用：<br>
<br>Redis部署最小资源对象为Pod，Pod是Kubernetes创建或部署的最小/最简单的基本单位。<br>
<br>当启动出错，例如出现“CrashLoopBackOff”时，Kubernetes将自动在该节点上重启该Pod,当出现物理节点故障时，Kubernetes将自动在其他节点上重新拉起一个。<br>
<br>Pod未出问题，但程序不可用时，依托于健康检查策略，Kubernetes也将重启该Redis节点。<br>
<br>滚动升级：<br>
<br>节点纵向扩容时，使用StatefulSet的滚动升级机制，Kubernetes将逆序重启更新每个Pod，提高了服务的可用性。<br>
<br>调度的高可用：<br>
<br>Kubernetes本身不处理Redis多个Pod组建的集群之间的部署关系，但提供了部署策略，为保证特定场景下的高可用，如因物理节点导致所有Redis节点均宕机，CRD在设计中加入了亲和与反亲和字段。<br>
<br>默认使用podAntiAffinity做节点打散，如下所示实例instance1的所有Pod将被尽可能调度到不同的节点上。<br>
<pre class="prettyprint">spec:<br>
  affinity:<br>
    podAntiAffinity:<br>
      preferredDuringSchedulingIgnoredDuringExecution:<br>
      - podAffinityTerm:<br>
          labelSelector:<br>
            matchLabels:<br>
              Redis.io/name: instance1<br>
          topologyKey: Kubernetes.io/hostname<br>
        weight: 1<br>
</pre><br>
<h4>Redis集群的高可用</h4>Redis服务运行期间不可避免的出现各种特殊情况，如节点宕机、网络抖动等，如何持续监测这类故障并进行修复，实现Redis集群的高可用，也是Operator需解决的问题，下面以哨兵模式模式为例描述集群如何进行故障恢复。<br>
<br>主节点宕机：因物理节点驱逐、节点重启、进程异常结束等导致的Redis主节点宕机情况，哨兵会进行切主操作，然后Kubernetes会在可用物理节点上重新拉起一个Pod。<br>
<br>从节点宕机：哨兵模式的Redis集群未开启读写分离，从节点宕机对服务无影响，后续Kubernetes会重启拉起一个Pod，Operator会将该Pod设置为新主节点的从节点。<br>
<br>集群全部节点宕机：发生概率极小，但基于持久化可将服务影响降至最低，集群恢复后可继续提供服务。<br>
<br>节点网络故障：主从模式下配置了三个哨兵用于集群选主操作，哨兵集群的每一个节点会定时对Redis集群的所有节点发心跳包检测节点是否正常。如果一个节点在down-after-milliseconds时间内没有回复Sentinel节点的心跳包，则该Redis节点被该Sentinel节点主观下线。<br>
<br>当节点被一个Sentinel节点记为主观下线时，并不意味着该节点肯定故障了，还需要Sentinel集群的其他Sentinel节点共同判断为主观下线才行。<br>
<br>该Sentinel节点会询问其他Sentinel节点，如果Sentinel集群中超过quorum数量的Sentinel节点认为该Redis节点主观下线，则该Redis客观下线。<br>
<br>如果客观下线的Redis节点是从节点或者是Sentinel节点，则操作到此为止，没有后续的操作了；如果客观下线的Redis节点为主节点，则开始故障转移，从从节点中选举一个节点升级为主节点。<br>
<br>集群模式故障转移与上述类似，不过不需要哨兵干预，而是由节点之间通过PING/PONG实现。<br>
<h3>监控观测</h3>Redis的监控采用经典的Exporter+Promethus的方案，Exporter用于指标采集，数据存储在Prometheus或其他数据库中，最终Grafana前端将服务状态可视化。<br>
<h3>集群扩缩容</h3><h4>纵向扩缩容</h4>纵向扩缩容主要指Pod的CPU、内存资源的调整，基于Kubernetes的特性，只需修改实例对应的spec字段，Operator的调和机制将持续监测参数变化，并对实例做出调整。当修改CPU、内存等参数时，Operator同步更新StatefulSet的limit、request信息，Kubernetes将逆序滚动更新Pod，滚动更新时，若停掉的是主节点，主节点的preStop功能会先通知哨兵或者集群进行数据保存，然后做主从切换操作，从而将服务的影响降至最低。更新后的主从关系建立以及哨兵monitor主节点功能也由Operator一并处理，全过程对客户端无感知。主从版、集群版在该场景下均支持秒级断闪。<br>
<h4>横向扩缩容</h4>横向扩缩容主要指副本数或节点数的调整，得益于Kubernetes的声明式API，可以通过更改声明的资源规模对集群进行无损弹性扩容和缩容。<br>
<br>Redis Server扩容操作时，主从版本中Operator将获取新节点IP，新启动节点将在下一轮调和时触发slaveof主节点操作，且同步过程中，哨兵不会将该节点选为主节点。集群版本中Operator将在同步节点信息后进行分片迁移，保证所有节点上的Slots尽可能均匀分布。<br>
<br>Redis Server缩容操作时，主从版本中Operator将逆序销毁Pod，销毁时会先询问哨兵，自己是否为主节点，若为主节点则进行先failover操作再退出。集群版本中Operator中会先进行分片迁移，再对该节点做删除操作。<br>
<br>代理的扩缩容，更易实现，根据流量波峰波谷规律，可手动定期在波峰到来时对Proxy进行扩容，波峰过后对Proxy进行缩容；也可根据HPA实现动态扩缩容，HPA也是Kubernetes的一种资源，可以依据Kubernetes的Metrics API的数据，实现基于CPU使用率、内存使用率、流量的动态扩缩容。<br>
<h3>总结与展望</h3>本次以Redis为范例，阐述了有道基础架构团队在基础设施容器化道路上的实践，Redis上云后将大幅缩短集群部署时间，支持秒级部署、分钟级启动、启动后的集群支持秒级自愈，集群依托于哨兵和代理的特性，故障切换对用户无感知。<br>
<br>有道架构团队最终以云平台的形式提供中间件能力，用户无需关注基础设施的资源调度与运维，重点关注具体业务场景，助力业务增长。未来，将进一步围绕Redis实例动态扩缩容、故障分析诊断、在线迁移、混合部署等内容展开探索。<br>
<h4>Redis容器化后有哪些优势？</h4>Kubernetes是一个容器编排系统，可以自动化容器应用的部署、扩展和管理。Kubernetes提供了一些基础特性：<br>
<br>部署：部署更快，集群建立无需人工干预。容器部署后可保证每个的Redis节点服务正常，节点启动后将由Operator持续监测调和Redis集群状态，包括主从关系、集群关系、哨兵监控、故障转移等。<br>
<br>资源隔离：如果所有服务都用同一个集群，修改了Redis集群配置的话，很可能会影响到其他的服务。但如果你是每个系统独立用一个Redis群的话，彼此之间互不影响，也不会出现某一个应用不小心把集群给打挂了，然后造成连锁反应的情况。<br>
<br>故障恢复：<br>
<ul><li>实例的重启：容器化后的健康检查可以实现服务自动重启功能；</li><li>网络故障：因宿主机网络故障带来的实例延迟高，哨兵可进行主从切换，而为了保证集群的健康，将由Operator负责同步集群信息。</li></ul><br>
<br>扩缩容：容器部署可根据limit和request限制实例的cpu和内存，也可以进行扩缩容操作，扩容后的故障恢复由Operator处理<br>
<br>节点调整：基于Operator对CRD资源的持续调和，可在Operator的Controller中为每个Redis实例进行状态维护，因此，节点调整后带来的主副关系建立、集群Slots迁移等均可自动完成。<br>
<br>数据存储：容器化可挂载Cephfs、LocalStorage等多种存储卷。<br>
<br>监控与维护：实例隔离后搭配Exporter、Prometheus等监控工具更容易发现问题。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/C7kXL8thMX8EnQufIFnueg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/C7kXL8thMX8EnQufIFnueg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            