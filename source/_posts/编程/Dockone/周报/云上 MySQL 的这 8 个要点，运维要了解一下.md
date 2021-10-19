
---
title: '云上 MySQL 的这 8 个要点，运维要了解一下'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/7c90f7c8da35e3eab345027a032f28bd.png'
author: Dockone
comments: false
date: 2021-10-19 05:07:37
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/7c90f7c8da35e3eab345027a032f28bd.png'
---

<div>   
<br>使用云上的 MySQL 时，会遇到很多人询问 CDB 的 为了更好的了解云上的 MySQL，本文将介绍一些重要的知识点。<br>
<h3>实例类型</h3>目前云数据库 MySQL 支持三种架构：基础版、高可用版、单节点高 IO 版。<br>
<ul><li>基础版是单个节点部署，价格低，性价比非常高，由于是单节点，数据安全性以及可用性不能保证，不建议生产环境使用</li><li>高可用版采用一主 N 从的高可用模式，实时热备，提供宕机自动检测和故障自动转移。主从复制方式有三种：异步、半同步、强同步。高可用版默认一主一从异步复制方式，可以通过购买和升级迁移到一主二从强同步模式。</li><li>单节点高 IO 版采用单个物理节点部署，性价比高；底层存储使用本地 NVMe SSD 硬盘，提供强大的 IO 性能。目前应用于<strong>只读实例</strong>，帮助业务分摊读压力，适用于有读写分离需求的各个行业应用。</li></ul><br>
<br><h3>数据库实例复制方式</h3><h4>异步复制</h4>应用发起数据更新（含 insert、update、delete 等操作）请求，Master 在执行完更新操作后立即向应用程序返回响应，然后 Master 再向 Slave 复制数据。<br>
<br>数据更新过程中 Master 不需要等待 Slave 的响应，因此异步复制的数据库实例通常具有较高的性能，且 Slave 不可用并不影响 Master 对外提供服务。但因数据并非实时同步到 Slave，而 Master 在 Slave 有延迟的情况下发生故障则有较小概率会引起数据不一致。<br>
<br>腾讯云数据库 MySQL 异步复制采用一主一从的架构。<br>
<h4>半同步复制</h4>应用发起数据更新（含 insert、update、delete 操作）请求，Master 在执行完更新操作后立即向 Slave 复制数据，Slave 接收到数据并写到 relay log 中（无需执行） 后才向 Master 返回成功信息，Master 必须在接受到 Slave 的成功信息后再向应用程序返回响应。<br>
<br>仅在数据复制发生异常（Slave 节点不可用或者数据复制所用网络发生异常）的情况下，Master 会暂停（MySQL 默认 10 秒左右）对应用的响应，将复制方式降为异步复制。当数据复制恢复正常，将恢复为半同步复制。<br>
<br>腾讯云数据库 MySQL 半同步复制采用一主一从的架构。<br>
<h4>强同步复制</h4>应用发起数据更新（含 insert、update、delete 操作）请求，Master 在执行完更新操作后立即向 Slave 复制数据，Slave 接收到数据并执行完 后才向 Master 返回成功信息，Master 必须在接受到 Slave 的成功信息后再向应用程序返回响应。<br>
<br>因 Master 向 Slave 复制数据是同步进行的，Master 每次更新操作都需要同时保证 Slave 也成功执行，因此强同步复制能最大限度的保障主从数据的一致性。但因每次 Master 更新请求都强依赖于 Slave 的返回，因此 Slave 如果仅有单台，它不可用将会极大影响 Master 上的操作。<br>
<br>腾讯云数据库 MySQL 强同步复制采用一主两从的架构，仅需其中一台 Slave 成功执行即可返回，避免了单台 Slave 不可用影响 Master 上操作的问题，提高了强同步复制集群的可用性。<br>
<h3>高可用实现原理</h3>目前使用最多的就是高可用版本的一主一从架构，正常情况下，客户通过 VIP:Port 的方式链接到主库上，从库通过 binlog 和主进行同步。云上 MySQL 在数据库所在的物理机发生硬件故障时是如何保证高可用呢？<br>
<h4>主所在物理机发生故障</h4><ul><li>正常情况下，客户端通过 VIP:Port 的方式链接到主库上，从库通过 binlog 和主进行同步。如下图中的步骤 1</li><li>当主库所在的宿主机发生异常宕机，此时客户端的链接就会被切换到从库（客户端具有断线重连几乎不受影响），此时从库进行读写。主库故障后，云平台会自动生成一个新的主从高可用实例，将最近一天的冷备导入到新实例对，在和当前的旧的从库进行 binlog 的同步。如下图中的步骤 2</li><li>binlog 增量同步完成后，旧的从库会和新的实例对一直进行同步状态，直至维护时间再次进行主动切换，切换时存在秒级闪断，业务有重连可以忽略闪断。此时客户端直接通过 VIP+Port 的方式连接到新建的实例对。旧实例就会被删除。详细的步骤如下图步骤 3</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/7c90f7c8da35e3eab345027a032f28bd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/7c90f7c8da35e3eab345027a032f28bd.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>MySQL 主库故障切换示意图</em><br>
<h4>从所在的物理机发生故障</h4>从库所在的物理机发生故障是，对客户端来说业务是完全不受影响，在从库所在物理机异常后，云平台会自动发起重建从库的流程，在健康的物理机上新建一个从库，导入冷备数据后和主库进行同步，同步完毕后，此时数据库又恢复了主从高可用状态。<br>
<h3>实例升级</h3>数据库的升级不仅包含数据库版本升级，还包括硬件升配，当然硬件的降配具体的原理也是一样的。<br>
<ul><li>在控制台发起实例升级的任务后，云平台会自动创建一个新的实例对，该新实例对的配置是需要调整到的配置。先将最近一次的备份导出到新建实例对内，在和主实例进行 binlog 同步。如下图步骤 1</li><li>主实例和新建实例对同步完成后，用户可以自行选择立即切换或在维护期内切换。整个切换过程秒级即可完成，完成后吗，客户端连接数据库请求都会到目标实例对，源实例对则会被自动回收。如下图步骤 2</li></ul><br>
<br>从上面的步骤我们可以看到升级实例时，完全不影响数据库的正常使用。升级主要花费的时间是导入冷备和追 binlog 这两个步骤，而这两个环节的所需的时间取决于客户的数据量大小和产生的 binlog 的大小。一般导入冷备的速度是 50G/h（理论值仅供参考）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/7c866f4cb59684b553e021b94997da10.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/7c866f4cb59684b553e021b94997da10.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>数据库实例升级示意图</em><br>
<h3>binlog 介绍</h3>binlog 日志用于记录所有更改数据的语句，俗称二进制日志，主要用于复制和即时点恢复。主从复制也是依赖于 binlog 的。类似于 Oracle 的 archivelog，Mongodb的oplog，所有和写有关或者可能有关的语句，都会记录在 binlog 文件中。云上的 MySQL 数据库的 <strong>binlog 文件都是每 1G 自动生成一个（新购实例也可能 256M 做一次切割）</strong>，除非做了 flush logs 的操作。<br>
<br>MySQL 的 binlog 默认保留 5 天，所以如果需要回档的话，只能恢复到 5 天内的任意时间点。<br>
<br>另外控制台下载的 binlog 日志，需要在本地解析的话，须确保客户端的 MySQL 版本与 CDB for MySQL 的版本一致，否则会出现解析出乱码的情况，建议使用 3.4 或以上版本的 mysqlbinlog<br>
<h3>回档介绍</h3>回档是将数据库通过冷备和 binlog 恢复到之前的某个时间点的一种操作。 CDB 的回档分为普通回档、快速回档以及极速回档：<br>
<ul><li>普通回档：导入该实例的全量备份，再在对选中的库、表进行回档。该回档模式无限制，但回档速度较慢</li><li>快速回档：仅导入所选中库级别的备份和 binlog，如有跨库操作，且关联库未被同时选中，将会导致回档失败</li><li>极速回档：仅导入所选中表级别的备份和 binlog，如有跨表操作，且关联表未被同时选中，将会导致回档失败。极速模式下，请手动选择需要回档的表。如果表已经被删除，需要客户自行创建表在进行回档操作。</li></ul><br>
<br><h3>慢查询</h3>慢查询就是执行数据库查询时消耗时间比较大的 SQL 语句。MySQL CPU 利用率过高，大部分原因与低效 SQL 有关系，通过优化低效 SQL 基本可以解决大部分问题。MySQL 慢查询时间的默认值是 10s，在遇到性能问题时，若发现没有慢查询，建议将其参数调成 1s ，再观察业务周期内的慢查询，进而对其慢查询进行优化。<br>
<br>如果出现全表扫描较高的情况，可以打开 log_queries_not_using_indexes 参数，此时未使用索引的全表扫描也可以记录到慢查询里面。这个参数并不建议一直打开，会对数据库的磁盘造成较大影响。<br>
<h3>MySQL 空间</h3>用户使用查询语句得到的 MySQL 空间和控制台看到的已使用空间相比有很大出入，为什么？<br>
<br>MySQL 的空洞效应导致，使用过程中的一些碎片没有得到合理释放因此查询语句查出来的空间和控制台统计的实际已使用空间相比少了许多，这部分是碎片，彻底解决需要在夜深人静的时候执行 optimize table。<br>
<br>原文链接：<a href="https://cloud.tencent.com/developer/article/1579285" rel="nofollow" target="_blank">https://cloud.tencent.com/deve ... 79285</a>，作者：苏欣
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            