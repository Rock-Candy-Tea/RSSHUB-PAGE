
---
title: 'Redis生产架构选型解决方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/66b803ea464fc5dd22f4b8dcc099bf12.png'
author: Dockone
comments: false
date: 2021-07-27 01:56:37
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/66b803ea464fc5dd22f4b8dcc099bf12.png'
---

<div>   
<br>【编者的话】在写开源项目的时候，想到了要支持多种redis部署方式，于是对于这块的生产环境的架构选型展开调研。<br>
<h3>引擎版本</h3>推荐使用更新的引擎版本以支持更多的特性。<br>
<h4>Redis 6.0新特性说明</h4><ul><li>模块系统新增多个API。</li><li>支持SSL/TLS加密。</li><li>支持新的Redis协议：RESP3。</li><li>服务端支持多模式的客户端缓存。</li><li>支持多线程IO。</li><li>副本中支持无盘复制（diskless replication）。</li><li>Redis-benchmark新增了Redis集群模式。</li><li>支持重写Systemd。</li><li>支持Disque模块。</li></ul><br>
<br><h4>Redis 5.0新特性说明</h4><ul><li>云数据库Redis 5.0版本大幅度优化内核，运行更加稳定，同时新增Stream、账号管理、审计日志等多种特性，满足您更多场景下的使用需求。</li><li>新的数据类型：流数据（Stream）。详细说明请参见<a href="https://redis.io/topics/streams-intro">Redis Streams</a>。</li><li>新增账号管理功能。</li><li>新增日志管理功能，支持审计日志、运行日志和慢日志，您可以通过日志管理查询读写操作、敏感操作（如KEYS、FLUSHALL）和管理类命令的使用记录以及慢日志。</li><li>新增基于快照的缓存分析功能。</li><li>新的定时器（Timers）、集群（ Cluster）和字典（Dictionary）模块的API。</li><li>RDB中增加LFU和LRU信息。</li><li>集群管理器从Ruby （redis-trib.rb）移植到了redis-cli中的C语言代码。</li><li>新增有序集合（Sorted Set）命令ZPOPMIN、ZPOPMAX、BZPOPMIN和BZPOPMAX。</li><li>升级Active Defragmentation至v2版本。</li><li>增强HyperLogLog的实现。</li><li>优化内存统计报告。</li><li>为许多有子命令的命令增加了HELP子命令。</li><li>提高了客户端频繁连接和断开连接时的性能表现。</li><li>升级Jemalloc至5.1版本。</li><li>新增命令CLIENT ID和CLIENT UNBLOCK。</li><li>新增了为艺术而生的LOLWUT命令。</li><li>弃用slave术语（需要API向后兼容的情况例外）。</li><li>对网络层进行了多处优化。</li><li>进行了一些Lua相关的改进。</li><li>新增动态HZ（Dynamic HZ）以平衡空闲CPU使用率和响应性。</li><li>对Redis核心代码进行了重构并在许多方面进行了改进。</li></ul><br>
<br><h3>架构</h3>你需要根据业务需求选择：<br>
<ul><li><strong>集群架构</strong>，可轻松突破Redis自身单线程瓶颈，满足大容量、高性能的业务需求。</li><li><strong>主从架构</strong>，提供高性能的缓存服务和数据高可靠。</li><li><strong>读写分离架构</strong>，提供高可用、高性能、高灵活的读写分离服务，解决热点数据集中及高并发读取的业务需求，最大化地节约用户运维成本。</li></ul><br>
<br><h4>主从架构-双副本</h4>采用主从（master-replica）模式搭建。主节点提供日常服务访问，备节点提供HA高可用，当主节点发生故障，系统会自动在30秒内切换至备节点，保证业务平稳运行。<br>
<br>可靠性：<br>
<ul><li>服务可靠采用双机主从（master-replica）架构，主从节点位于不同物理机。主节点对外提供访问，用户可通过Redis命令行和通用客户端进行数据的增删改查操作。当主节点出现故障，HA系统会自动进行主从切换，保证业务平稳运行。</li><li>数据可靠默认开启数据持久化功能，数据全部落盘。支持数据备份功能，用户可以针对备份集回滚实例或者克隆实例，有效地解决数据误操作等问题。</li></ul><br>
<br>使用场景：<br>
<ul><li>Redis作为持久化数据存储使用的业务标准版提供持久化机制及备份恢复机制，极大地保证数据可靠性。</li><li>单个Redis性能压力可控的业务由于Redis原生采用单线程机制，性能在10万QPS以下的业务建议使用。如果需要更高的性能要求，请选用集群版本。</li><li>Redis命令相对简单，排序、计算类命令较少的业务由于Redis的单线程机制，CPU会成为主要瓶颈。如排序、计算类较多的业务建议选用集群版配置。</li></ul><br>
<br><h4>主从架构-单副本</h4>可以在没有数据可靠性要求的纯缓存场景充分发挥性能优势。<br>
<br>使用场景：<br>
<ul><li>纯缓存类业务场景，单副本版本只有一个数据库节点，节点出现故障时，系统会重新拉起一个Redis进程（没有数据），当节点故障业务自动切换完成后，应用程序需要将数据重新预热，以免对后端数据库产生访问压力冲击。 单副本架构不能提供数据可靠性，如果发生节点故障，您需要重新对业务进行预热，因此，在对数据可靠性要求较高的敏感性业务中，建议选用双副本架构。</li><li>单个Redis性能压力可控，由于Redis原生采用单线程机制，CPU为单核能力，性能在8万QPS的业务建议使用。如果需要更高的性能要求，请选用集群版配置。</li><li>Redis命令相对简单，排序、计算类命令较少，由于Redis的单线程机制，CPU为主要瓶颈。如排序、计算类较多的业务建议选用集群版配置。</li></ul><br>
<br><h4>集群版-双副本</h4>可轻松突破Redis自身单线程瓶颈，满足大容量、高性能的业务需求。双副本集群版实例采用集群架构，每个分片服务器采用主从（master-replica）双副本模式。<strong>集群版支持代理和直连两种连接模式</strong>，你可以根据本章节的说明，选择适合业务需求的连接模式。<br>
<br>代理模式：<br>
<br><strong>集群架构的本地盘实例默认采用代理（Proxy）模式</strong>，支持通过一个统一的连接地址（域名）访问Redis集群，客户端的请求通过代理服务器转发到各数据分片，代理服务器、数据分片和配置服务器均不提供单独的连接地址，降低了应用开发难度和代码复杂度。代理模式的服务架构图和组件说明如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/66b803ea464fc5dd22f4b8dcc099bf12.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/66b803ea464fc5dd22f4b8dcc099bf12.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/a503bccf7ee3998fe5c505ccc3ebf50d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/a503bccf7ee3998fe5c505ccc3ebf50d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
直连模式：<br>
<br>因所有请求都要通过代理服务器转发，代理模式在降低业务开发难度的同时也会小幅度影响Redis服务的响应速度。如果业务对响应速度的要求非常高，您可以使用直连模式，绕过代理服务器直接连接后端数据分片，从而降低网络开销和服务响应时间。直连模式的服务架构和说明如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/7f176e4c1bb7ba727e46738b123b6217.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/7f176e4c1bb7ba727e46738b123b6217.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
前提条件 使用Jedis、PhpRedis等支持Redis Cluster的客户端。<br>
<ul><li>使用不支持Redis Cluster的客户端，可能因客户端无法重定向请求到正确的分片而获取不到需要的数据。</li><li>Jedis对于Redis Cluster的支持是基于JedisCluster这个类，详细说明请参见Jedis文档。</li><li>你可以在Redis官网的客户端列表里查找更多支持Redis Cluster的客户端。</li></ul><br>
<br>使用自定义连接池的示例代码：<br>
<pre class="prettyprint">import redis.clients.jedis.*;<br>
import java.util.HashSet;<br>
import java.util.Set; <br>
public class main &#123;<br>
private static final int DEFAULT_TIMEOUT = 2000; <br>
private static final int DEFAULT_REDIRECTIONS = 5;<br>
private static final JedisPoolConfig DEFAULT_CONFIG = new JedisPoolConfig();<br>
<br>
<br>
public static void main(String args[])&#123;<br>
JedisPoolConfig config = new JedisPoolConfig();<br>
// 最大空闲连接数, 根据业务需要设置，不能超过实例规格规定的最大的连接数<br>
config.setMaxIdle(200);<br>
// 最大连接数, 根据业务需要设置，不能超过实例规格规定的最大的连接数<br>
config.setMaxTotal(300);<br>
config.setTestOnBorrow(false);<br>
config.setTestOnReturn(false);<br>
<br>
// 开通直连访问时申请到的直连地址<br>
String host = "r-bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com"; <br>
int port = 6379;<br>
// 实例的密码<br>
String password = "xxxxx";<br>
<br>
Set<HostAndPort> jedisClusterNode = new HashSet<HostAndPort>();<br>
jedisClusterNode.add(new HostAndPort(host, port));<br>
JedisCluster jc = new JedisCluster(jedisClusterNode, DEFAULT_TIMEOUT, DEFAULT_TIMEOUT,<br>
        DEFAULT_REDIRECTIONS,password, "clientName", config);<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>集群版-单副本</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/ff7330a77ccdf144af6730ffee23c618.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/ff7330a77ccdf144af6730ffee23c618.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/4740ed218d2bf411a379a14dfa5504a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/4740ed218d2bf411a379a14dfa5504a4.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>读写分离版</h4>针对读多写少的业务场景，提供高可用、高性能、灵活的读写分离服务，满足热点数据集中及高并发读取的业务需求，最大化地节约运维成本。 读写分离版主要由主备节点、只读节点、Proxy（代理）节点和高可用系统组成。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/e8a8cfa608303c72b92a342944cea23d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/e8a8cfa608303c72b92a342944cea23d.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210725/0f72f0e60396de3a9f27620b731305e2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210725/0f72f0e60396de3a9f27620b731305e2.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
特点：<br>
<ul><li><br>高可用<br>
<ul><li>通过自研的高可用系统自动监控所有数据节点的健康状态，为整个实例的可用性保驾护航。主节点不可用时自动选择新的主节点并重新搭建复制拓扑。某个只读节点异常时，高可用系统能够自动探知并重新启动新节点完成数据同步，下线异常节点。</li><li>Proxy节点实时感知每个只读实例的服务状态。在某个只读实例异常期间，Proxy会自动降低该节点的服务权重，发现只读节点连续失败超过一定次数以后，会停止异常节点的服务权利，并具备继续监控后续重新启动节点服务的能力。</li></ul></li><li><br>高性能<br>
<ul><li>读写分离版采取链式复制架构，<strong>可以通过扩展只读实例个数使整体实例性能呈线性增长</strong>，同时基于源码层面对Redis复制流程的定制优化，可以最大程度地提升线性复制的系统稳定性，充分利用每一个只读节点的物理资源。</li></ul></li></ul><br>
<br>使用场景：<br>
<br>读取请求QPS（Queries Per Second）压力较大，标准版Redis无法支撑较大的QPS，如果业务类型是读多写少类型，需要采用多个只读节点的部署方式来突破Redis单线程的性能瓶颈。Redis集群版提供1个、3个、5个只读节点的配置，相比标准版可以将QPS提升近5倍。<br>
<br>对Redis协议兼容性要求较高的业务 读写分离版完全兼容Redis协议命令，可将自建Redis数据库迁移至读写分离版，同时支持从Redis标准版（双副本）一键平滑升级至读写分离版。<br>
<br>建议与使用须知：<br>
<ul><li><strong>当一个只读节点发生故障时，请求会转发到其他节点；如果所有只读节点均不可用，请求会全部转发到主节点。只读节点异常可能导致主节点负载提高、响应时间变长，因此在读负载高的业务场景建议使用多个只读节点。</strong></li><li><strong>某些场景会触发只读节点的全量同步，例如在主节点触发高可用切换后。全量同步期间只读节点不提供服务并返回-LOADING Redis is loading the dataset in memory\r\n信息。</strong></li></ul><br>
<br>原文链接：<a href="https://juejin.cn/post/6955355807231770631" rel="nofollow" target="_blank">https://juejin.cn/post/6955355807231770631</a>，作者：小热爱  
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            