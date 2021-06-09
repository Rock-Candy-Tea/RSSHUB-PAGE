
---
title: 'Greenplum 关键组件版本更新：GPSS 1.6.0 和 GPCC 6.5 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1995'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 15:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1995'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Greenplum商业版具有众多扩展组件来帮助用户更便捷的使用Greenplum，其中Greenplum监控管理平台GPCC和数据加载解决方案GPSS均是其中关键组件之一，在过去的一个月中，GPSS和GPCC均进行了版本更新，现在让我们带大家了解一下，新版本的GPSS和GPCC都带来了哪些新功能。</p> 
<p><strong>GPSS (Greenplum stream server) 1.6.0 发布</strong></p> 
<p>GPSS 1.6.0已于5日28日正式发布。Greenplum Stream Server（简称GPSS）是Greenplum下一代数据加载解决方案，能将不同源端的增量数据同步到Greenplum中。</p> 
<p><strong>GPSS 1.6.0 新功能</strong></p> 
<ol> 
 <li> <p>gpss增加-c选项, 用于指定配置文件路径</p> </li> 
 <li> <p>gpsscli的--version参数也会打印gpss server的版本信息</p> </li> 
 <li> <p>gpss和gpsscli日志支持--color和--csv格式, 默认为空格分隔的文本格式</p> </li> 
 <li> <p>gpss的Kafka job配置新增IDLE_DURATION 参数, 当超过IDLE_DURATION 时间后对应的kafka topic中没有新消息, GPSS将会释放目标表的锁</p> </li> 
 <li> <p>gpss新增SCHEMA_PATH_ON_GPDB 参数, 支持从Greenplum集群的segment节点上获取avro的schema</p> </li> 
 <li> <p>gpss新增FALLBACK_OFFSET 参数, 可以设置当消息的offset不连续时(未及时加载就被清空)时,从何处继续加载消息</p> </li> 
 <li> <p>gpss支持基于HTTPS的scheme service服务</p> </li> 
 <li> <p>gpss支持了kafka的group.id 配置, 可通过第三方工具监控加载进度</p> </li> 
 <li> <p>除了exactly once, gpss支持最多一次和最少一次一致性保证</p> </li> 
 <li> <p>gpss支持通过custom formatter方式实现自定义消息格式</p> </li> 
</ol> 
<p><strong>实验功能</strong></p> 
<ol> 
 <li> <p>gpss新增了RECOVER_FAILING_BATCH 配置, 可以将Greenplum无法处理的事务中的错误数据暂存</p> </li> 
 <li> <p>gpss组件增加了新的dataflow extension, 包含gp_jsonb数据类型和text_in formatter</p> </li> 
</ol> 
<p><strong>GPCC（Greenplum Command Center） 6.5 发布</strong></p> 
<p>GPCC 6.5已于5月31日正式发布。Greenplum Command Center 6.5 为 Tanzu Greenplum Database 6 提供管理和监控功能。</p> 
<p>Greenplum Command Center 6.5 与以下平台兼容。</p> 
<ul> 
 <li> <p>Tanzu Greenplum 数据库 6.x。</p> </li> 
 <li> <p>Redhat 企业版 Linux 6.x1 和 7.x</p> </li> 
 <li> <p>CentOS 6.x1 和 7.x</p> </li> 
 <li> <p>SUSE 企业版 Linux 12</p> </li> 
 <li> <p>Ubuntu 18.04</p> </li> 
</ul> 
<p>有关最新的兼容性信息，请参阅 Tanzu Greenplum Command Center支持平台相关文档：https://gpcc.docs.pivotal.io/supported-platforms/gpcc.html）</p> 
<p><strong>GPCC 6.5 版本增强功能</strong></p> 
<ol> 
 <li> <p>查询监视器（Query Monitor）页面现允许用户根据查询的状态（正在运行、已排队或已阻止）过滤显示的查询。更多信息，请参阅查询监视器文档（https://gpcc.docs.pivotal.io/650/topics/ui/query-monitor.html）。</p> </li> 
 <li> <p>查询监视器页面现包含高级搜索工具。该工具允许用户根据查询指标（例如查询 ID、数据库名称、资源组等）过滤显示的查询。有关更多信息，请参阅查询监视器文档页面（https://gpcc.docs.pivotal.io/650/topics/ui/query-monitor.html）。</p> </li> 
 <li> <p>用户现在可以暂停查询监视器以查看查询的快照。有关更多信息，请参阅查询监视器文档页面（https://gpcc.docs.pivotal.io/650/topics/ui/query-monitor.html）</p> </li> 
 <li> <p>查询监视器现在显示有关会话的各种信息，例如会话状态、关联的用户和数据库、空闲时间和关联的查询等。具有管理员或操作员权限的用户可以查看和取消所有用户的会话，以及将会话详细信息导出到 CSV 文件。有关更多信息，请参阅查询监视器文档页面（https://gpcc.docs.pivotal.io/650/topics/ui/query-monitor.html）。</p> </li> 
 <li> <p>实时查询详细信息页面现在可以显示查询的查询标签。</p> </li> 
 <li> <p>查询历史详情页面现在可以显示查询的查询标签。</p> </li> 
 <li> <p>在历史记录页面上，高级搜索工具现在允许用户过滤查询的查询标签。有关更多信息，请参阅历史文档页面。（https://gpcc.docs.pivotal.io/650/topics/ui/history.html）</p> </li> 
 <li> <p>用户可以创建工作负载规则来终止空闲会话，并可以检查终止会话的规则日志。有关更多信息，请参阅工作负载管理文档页面。（https://gpcc.docs.pivotal.io/650/topics/ui/workload-management.html）</p> </li> 
 <li> <p>用户可以通过溢出文件大小创建规则。有关更多信息，请参阅工作负载管理文档页面。（https://gpcc.docs.pivotal.io/650/topics/ui/workload-management.html）</p> </li> 
 <li> <p>gpmetrics 模式包含一个新的 gpmetrics.gpcc_queries_now 表，用于存储实时查询指标数据。</p> </li> 
 <li> <p>gpcc_wlm_rule 表增加了两行：一个用于存储空闲会话终止规则的参数，另一个用于存储溢出文件大小。更多信息，请参阅gpmetrics 架构参考文档（https://gpcc.docs.pivotal.io/650/topics/ref-gpmetrics.html）</p> </li> 
 <li> <p>Greenplum Command Center将不再支持Microsoft IE 浏览器。</p> </li> 
</ol>
                                        </div>
                                      
</div>
            