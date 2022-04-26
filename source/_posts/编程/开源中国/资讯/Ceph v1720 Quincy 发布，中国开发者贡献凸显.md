
---
title: 'Ceph v17.2.0 Quincy 发布，中国开发者贡献凸显'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3598'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3598'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#222222">Ceph v17.2.0 Quincy 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FiQLW9cLomavN7Y61ZsPPMg" target="_blank">发布</a>。Quincy<span> </span>是 Ceph 的第 17 个稳定版本</span><span style="background-color:#ffffff; color:#222222">，</span><span style="background-color:#ffffff; color:#222222"><span> </span>它以海绵宝宝的章鱼 </span><span style="background-color:#ffffff; color:#222222">Quincy </span><span style="background-color:#ffffff; color:#222222">触</span><span style="background-color:#ffffff; color:#222222">手</span><span style="background-color:#ffffff; color:#222222">命名，</span><span style="background-color:#ffffff; color:#222222">这是 Ceph Quincy 的第一个稳定版本。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000"><strong>相比于 Pacific 版本的大变化有：</strong></span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span>FileStore在 Quincy 中已被弃用。BlueStore 成为 Ceph 的默认存储引擎。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><code><span>ceph-mgr-modules-core</span></code><span>debian 软件包不再</span><code><span>ceph-mgr-rook</span></code><span>推荐. </span><code><span>ceph-mgr-rook</span></code><span>依赖于，当版本早于 1.19</span><code><span>python3-numpy</span></code><span>时，不能在不同的 Python 子解释器中多次导入。</span><code><span>python3-numpy</span></code><span>因为默认</span><code><span>apt-get</span></code><span>安装软件包，所以总是与debian 软件包一起作为间接依赖安装。如果您的工作流程取决于此行为，您可能需要单独安装。</span><code><span>Recommends</span></code><code><span>ceph-mgr-rook</span></code><code><span>ceph-mgr</span></code><code><span>ceph-mgr-rook</span></code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><code><span>device_health_metrics</span></code><span>池已重命名</span><code><span>.mgr</span></code><span>。它现在用作所有</span><code><span>ceph-mgr</span></code><span>模块的公共存储。升级到 Quincy 后，该</span><code><span>device_health_metrics</span></code><span>池将</span><code><span>.mgr</span></code><span>在现有集群上重命名。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>该</span><code><span>ceph pg dump</span></code><span>命令现在打印三个附加列：</span><code><span>LAST_SCRUB_DURATION</span></code><span>显示最后完成的擦洗的持续时间（以秒为单位）；</span><code><span>SCRUB_SCHEDULING</span></code><span>传达一个 PG 是否被安排在指定</span><span>时间被擦洗，它是否排队等待擦洗，或者它是否正在被擦洗；</span><code><span>OBJECTS_SCRUBBED</span></code><span>显示擦洗开始后在 PG 中擦洗的对象数量。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><code><span>require-osd-release</span></code><span>如果在集群升级后未将标志设置为适当的版本，现在会报告运行状况警告。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>LevelDB 支持已被删除。</span><code><span>WITH_LEVELDB</span></code><span>不再是受支持的构建选项。用户 - 应该 - 在升级到 Quincy 之前将他们的监视器和 OSD 迁移到 RocksDB。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Cephadm：</span><code><span>osd_memory_target_autotune</span></code><span>默认启用，设置</span><code><span>mgr/cephadm/autotune_memory_target_ratio</span></code><span>为</span><code><span>0.7</span></code><span>总 RAM。这不适合超融合基础架构。对于超融合 Ceph，请参考文档或设置</span><code><span>mgr/cephadm/autotune_memory_target_ratio</span></code><span>为</span><code><span>0.2</span></code><span>.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>遥测：改进了选择加入流程，以便用户可以继续共享相同的数据，即使有新的数据收集可用。现在可以选择使用一个新的“性能”频道来收集各种性能指标：</span><code><span>ceph telemetry on</span></code><span> </span><code><span>ceph telemetry enable channel perf</span></code><span>查看带有 的示例报告</span><code><span>ceph telemetry preview</span></code><span><span>。请注意，在大型集群中使用“perf”通道数据生成遥测报告可能需要一些时间。有关更多详细信息，请参阅：</span>https ://docs.ceph.com/en/quincy/mgr/telemetry/</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>MGR：progress 模块默认禁用 pg 恢复事件，因为该事件代价高昂，并且当有 OSD 被标记为从集群中进入/退出时会中断其他服务。但是，用户仍然可以随时启用此事件。有关更多详细信息，请参阅</span>https://docs.ceph.com/en/quincy/mgr/progress/</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>https://tracker.ceph.com/issues/55383<span>是一个已知问题。</span></span><code><span>mon_cluster_log_to_journald</span></code><span>当设置为 true 时需要设置为 false</span><code><span>mon_cluster_log_to_file</span></code><span>以在日志轮换后继续将集群日志消息记录到文件中。</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#000000"><strong>Cephadm</strong></span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span>SNMP 支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>守护进程托管 (mgr, mds, rgw)</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>osd内存自动调整</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>与新的 NFS 管理模块集成</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>能够在 osd 被删除时对其进行删除</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>用于提高性能/可扩展性的 cephadm 代理</span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:justify"><span style="color:#000000"><strong>Dashboard </strong></span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span>第 1 天：新的“集群扩展向导”将引导用户完成安装后的步骤：添加新主机、存储设备或服务。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>NFS：仪表板现在允许用户从一个地方完全管理所有 NFS 导出。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新的 mgr 模块（反馈）：用户可以直接从 Dashboard 或 CLI 快速报告 Ceph 跟踪器问题或建议。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新的“每日消息”：集群管理员可以在横幅中发布自定义消息。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Cephadm 集成改进：</span></p> 
  <ul> 
   <li> <p style="margin-left:0; margin-right:0"><span>​​​​​​​</span>主机管理：维护、规格和标签，</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">服务管理：编辑和显示日志，</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">守护进程管理（启动、停止、重启、重新加载），</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">支持的新服务：入口（HAProxy）和 SNMP 网关。</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>监控和警报：</span></p> 
  <ul> 
   <li> <p style="margin-left:0; margin-right:0"><span>​​​​​​​</span>添加了 43 个新警报（总共 68 个），提高了对影响以下事件的可观察性：集群运行状况、监视器、存储设备、PG 和 CephFS。</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">现在可以通过新的 SNMP 网关服务（提供 MIB）将警报作为 SNMP 陷阱发送到外部。</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">改进的集成完整/接近完整事件通知。</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">Grafana 仪表板现在使用 grafonnet 格式（尽管它们仍以 JSON 格式提供）。</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">堆栈更新：用于监控容器的图像已更新。Grafana 8.3.5、Prometheus 2.33.4、Alertmanager 0.23.0 和 Node Exporter 1.3.1。这减少了对多个 Grafana 漏洞（CVE-2021-43798、CVE-2021-39226、CVE-2021-43798、CVE-2020-29510、CVE-2020-29511）的暴露。</p> </li> 
  </ul> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:justify"><span style="color:#000000"><strong>RADOS </strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>OSD</span><span>：Ceph 现在</span><code><span>mclock_scheduler</span></code><span>默认使用 BlueStore OSD</span><code><span>osd_op_queue</span></code><span>来提供 QoS。Filestore OSD 不支持“mclock_scheduler”。因此，默认的 'osd_op_queue' 设置为</span><code><span>wpq</span></code><span>用于 Filestore OSD，即使用户尝试更改它也会强制执行。有关配置 mclock 的更多详细信息，请参阅，</span></p> <p style="margin-left:0; margin-right:0"><span>https://docs.ceph.com/en/quincy/rados/configuration/mclock-config-ref/</span></p> <p style="margin-left:0; margin-right:0"><span>运行时存在一个突出问题，在使用命令切换到</span><code><span>custom</span></code><span>mclock 配置文件后，无法修改与预留、重量和限制相关的 mclock 配置选项。</span><code><span>ceph config set ...</span></code><span><span>这由</span>https://tracker.ceph.com/issues/55153<span>跟踪。在问题得到解决之前，建议用户避免使用“自定义”配置文件或使用跟踪器中提到的解决方法。</span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>MGR：pg_autoscaler 现在可以使用标志在全局范围内</span><code><span>on</span></code><span>转动。默认情况下，它设置为，但此标志可以派上用场，以防止在集群升级和维护期间由自动缩放触发重新平衡。现在可以使用该标志创建池，这允许自动缩放器将更多 PG 分配给此类池。这对于为数据密集型池获得更好的开箱即用性能很有用。</span><code><span>off</span></code><code><span>noautoscale</span></code><code><span>on</span></code><code><span>--bulk</span></code></p> <p style="margin-left:0; margin-right:0"><span><span>有关自动缩放的更多详细信息，请参阅：</span>https ://docs.ceph.com/en/quincy/rados/operations/placement-groups/</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><code><span>off</span></code><span>OSD：默认支持 osd-osd 通信的在线压缩。</span></p> <p style="margin-left:0; margin-right:0"><span><span>有关压缩模式的更多详细信息，请参阅：</span>https ://docs.ceph.com/en/quincy/rados/configuration/msgr2/#compression-modes</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>OSD：集群日志中慢速操作的简明报告。可以通过设置</span><code><span>osd_aggregated_slow_ops_logging</span></code><span>为 false 来恢复旧的和更详细的日志记录行为。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>“kvs” Ceph 对象类不再打包。“kvs” Ceph 对象类提供了在 librados 对象 omap 之上实现的分布式平面 b 树键值存储。由于该对象类没有现有的内部用户，因此不再对其进行打包。</span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:justify"><span style="color:#000000"><strong>RBD block storage</strong></span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span>rbd-nbd：</span><code><span>rbd device attach</span></code><span>和</span><code><span>rbd device detach</span></code><span>添加的命令，这些允许在</span><code><span>rbd-nbd</span></code><span>守护进程自 Linux 内核 5.14 以来重新启动后安全重新连接。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>rbd-nbd：</span><code><span>notrim</span></code><span>添加了映射选项以支持厚配置映像，类似于 krbd。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span>SSD 设备上客户端持久缓存的大量稳定工作，也可在 16.2.8 中使用。有关使用的详细信息，请参阅</span>https://docs.ceph.com/en/quincy/rbd/rbd-persistent-write-log-cache/</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>使用快速差异图像特征 + 整个对象（不精确）模式时，差异计算中的几个错误修复。在极少数情况下，这些长期存在的问题可能会导致不正确的</span><code><span>rbd export</span></code><span>. 也在 15.2.16 和 16.2.8 中修复。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复了在 krbd 上运行 Windows VM 时潜在的性能下降问题。详情见</span><code><span>rxbounce</span></code><span><span>地图选项说明：</span>https ://docs.ceph.com/en/quincy/man/8/rbd/#kernel-rbd-krbd-options</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#000000"><span style="background-color:#ffffff">RGW object storage</span></span></strong></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span>RGW 现在支持按用户和/或按桶进行速率限制。使用此功能，可以限制用户和/或存储桶，可以交付总操作数和/或每分钟字节数。此功能允许管理员仅限制 READ 操作和/或 WRITE 操作。通过使用全局配置，可以将限速配置应用于所有用户和所有存储桶。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><code><span>radosgw-admin realm delete</span></code><span>已重命名为</span><code><span>radosgw-admin realm rm</span></code><span>. 这与帮助信息一致。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>S3 存储桶通知事件现在包含一个</span><code><span>eTag</span></code><span>键而不是</span><code><span>etag</span></code><span>，并且 eventName 值不再带有</span><code><span>s3:</span></code><span>前缀，从而修复了与在 AWS 上观察到的消息格式的偏差。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>现在可以为野兽前端指定 ssl 选项和密码。默认 ssl 选项设置为“no_sslv2:no_sslv3:no_tlsv1:no_tlsv1_1”。如果要返回旧行为，请将 'ssl_options='（空）添加到</span><code><span>rgw frontends</span></code><span>配置中。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>分段上传的行为已修改，以便在分段上传结束时仅发送 CompleteMultipartUpload 通知。上传开始时的 POST 通知和每个部分上发送的 PUT 通知不再发送。</span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#000000"><strong>CephFS distributed file system</strong></span></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span>fs：可以使用特定 ID（“fscid”）创建文件系统。这在某些恢复方案中很有用（例如，当监视器数据库丢失并重新构建时，并且恢复的文件系统预计具有与以前相同的 ID）。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>fs：可以使用该</span><code><span>fs rename</span></code><span>命令重命名文件系统。任何为旧文件系统名称授权的 cephx 凭据都需要重新授权为新文件系统名称。由于使用这些重新授权的 ID 的客户端的操作可能会中断，因此该命令需要“--yes-i-really-mean-it”标志。此外，预计将在文件系统上禁用镜像。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>MDS 升级不再需要在升级文件系统的唯一活动 MDS 之前停止所有备用 MDS 守护程序。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>CephFS：如果备用重放守护进程重放日志失败，现在会导致等级被标记为“损坏”。</span></p> </li> 
</ul> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FiQLW9cLomavN7Y61ZsPPMg" target="_blank">查看官方公告</a>。 </p>
                                        </div>
                                      
</div>
            