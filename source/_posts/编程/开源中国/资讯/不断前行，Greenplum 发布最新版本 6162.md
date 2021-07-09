
---
title: '不断前行，Greenplum 发布最新版本 6.16.2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7479'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 16:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7479'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>了解更多Greenplum相关内容，欢迎访问<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcn.greenplum.org%2F%3Fhmsr%3D%25E5%25BC%2580%25E6%25BA%2590%25E4%25B8%25AD%25E5%259B%25BD%26hmpl%3D%26hmcu%3D%26hmkw%3D%26hmci%3D">Greenplum中文社区网站</a></p> 
</blockquote> 
<p>Greenplum 6.0自正式版发布以来，Greenplum保持每月一个小版本的迭代速率，持续为用户提供新功能和修复补丁，目前的最新版6.16.2。Greeplum 6.16.2于2021年6月4日发布。相关更新内容请查看下面详情。</p> 
<h2>Greenplum 6.16.2</h2> 
<h3><strong>修复bug列表</strong></h3> 
<p><strong>服务器</strong></p> 
<ul> 
 <li> <p>解决了分区键类型和搜索值类型不同时 Postgres planner 分区选择的问题；</p> </li> 
 <li> <p>解决了以下问题：在具有 exec 位置 INITPLAN 的函数上运行 \df+ 时，Execute on 列未正确显示“initplan”；</p> </li> 
 <li> <p>解决了由于服务器保存某些数据上下文的时间超过所需时间而可能发生的内存不足情况；</p> </li> 
 <li> <p>修复了创建 DOMAIN 时 master 和 segment 之间 collname 值的不一致；</p> </li> 
 <li> <p>解决了在指定 CREATE MATERIALIZED VIEW 失败并显示 ERROR:division by zero when WITH NO DATA was being specified；</p> </li> 
</ul> 
<p><strong>执行器</strong></p> 
<ul> 
 <li> <p>解决了由于内存上下文 TupleSort 的双重释放导致数据库出现 PANIC 的问题；</p> </li> 
</ul> 
<p><strong>gpload</strong></p> 
<ul> 
 <li> <p>解决了 gpload 会因列名使用大写或混合大小写字符而失败的问题。gpload 现在会自动为 YAML 控制文件中尚未引用的列名添加双引号；</p> </li> 
</ul> 
<h2>Greenplum 6.16.1</h2> 
<h3><strong>修复bug列表</strong></h3> 
<p><strong>gprecoverseg</strong></p> 
<ul> 
 <li> <p>解决了使用 gprecoverseg 执行增量恢复从 pg_log 目录中删除日志文件的问题。gprecoverseg 现在将文件保留在 pg_log 下，以便它们可以在增量恢复后用于故障排除；</p> </li> 
</ul> 
<p><strong>集群管理</strong></p> 
<ul> 
 <li> <p>解决了取消gpconfig 时由于主机无法访问而挂起的问题；</p> </li> 
 <li> <p>gprecoverseg 忽略无法访问主机上的segments的新功能由于会跳过了新主机替换无法访问主机的情况，从而导致 gprecoverseg -p newhost 选项的问题，已解决；</p> </li> 
 <li> <p>解决了当gpmovemirror 提供的配置文件出现问题时， 会导致打印错误的错误消息；</p> </li> 
</ul> 
<p><strong>查询优化器</strong></p> 
<ul> 
 <li> <p>解决了优化器在查询视图时因segments错误而失败的问题，如果视图在表之间有连接并且任何表有一个在视图创建后被删除的列；</p> </li> 
 <li> <p>解决了优化器在内存不足时崩溃（而不是简单地抛出错误）的问题；</p> </li> 
 <li> <p>解决了当查询涉及带有 EXCEPT 子句的 CTE 时优化器返回错误结果的问题。出现此问题是因为查询优化器没有为类型与 SetOp 的输出类型不匹配的任何输入列添加标量转换；</p> </li> 
</ul> 
<p><strong>服务器</strong></p> 
<ul> 
 <li> <p>解决了如果 WHERE 子句包含嵌入式查询，则 REFRESH MATERIALIZED QUERY 失败的问题；</p> </li> 
 <li> <p>解决了某些查询由于跟踪临时文件的方式而导致 master 崩溃的问题；</p> </li> 
 <li> <p>解决了在子句中使用 NOT 时导致视图创建查询性能缓慢的问题；</p> </li> 
 <li> <p>解决了 VACUUM FULL ANALYZE 无法清除某些膨胀表的问题；</p> </li> 
 <li> <p>解决了由于删除恢复所需的 WAL 文件，在必须恢复充当primary节点的故障segment时，增量恢复的相关问题；</p> </li> 
 <li> <p>解决了由于列未正确从 cstring 类型转换为date 类型而无法恢复具有未知字段的视图的问题；</p> </li> 
 <li> <p>解决了 gpload 中，重置会话时未中止全局事务的问题；</p> </li> 
</ul> 
<p><strong>执行器</strong></p> 
<ul> 
 <li> <p>解决了由于如何处理新分配的内存而导致多个段失败并出现 PANIC 错误的问题；</p> </li> 
</ul> 
<h2>Greenplum 6.16.0</h2> 
<h3><strong>新增功能</strong></h3> 
<ul> 
 <li> <p>除了现有的弹性模式之外，Greenplum 资源组现支持一种新的模式用于按百分比分配 CPU 资源：天花板强制模式；</p> </li> 
 <li> <p>此版本提供 PXF 6.0.0 发行版；</p> </li> 
 <li> <p>此版本提供GPSS 1.53发行版；</p> </li> 
 <li> <p>此版本提供MADlib 1.18.0的发行版，包括深度学习的新特性、改进和bug修复；</p> </li> 
 <li> <p>gp_sparse_vector 模块现在将其函数和对象安装到名为 sparse_vector 的模式中；</p> </li> 
 <li> <p>optimizer_join_order 服务器配置参数的默认值从exhaustive2 更改为exhaustive，这是Greenplum 6.14.0 版本之前的默认值。Greenplum 数据库查询优化器 (GPORCA) 使用此配置参数来识别查询的连接枚举算法。</p> </li> 
</ul> 
<h3><strong>修复bug列表</strong></h3> 
<p><strong>查询优化器</strong></p> 
<ul> 
 <li> <p>解决了在 Greenplum 数据库版本 6.15.0 上使用 GPORCA 查询优化器的查询需要更长的时间才能完成的问题，其中 optimizer_join_order 服务器配置参数默认值为exhaustive2。此配置参数的默认值已更改为（回）exhaustive；</p> </li> 
 <li> <p>在查询定义为开放边界的分区表时，查询优化器会执行不必要的扫描。此问题已得到解决；</p> </li> 
 <li> <p>修复了查询分区表时在缓存中查找对象 0.0.0.0 失败的错误；</p> </li> 
</ul> 
<p><strong>gp_sparse_vector</strong></p> 
<ul> 
 <li> <p>解决了 gp_sparse_vector array_agg() 函数覆盖系统 pg_catalog.array_agg() 函数并返回不同类型的数组的问题。gp_sparse_vector 模块现在将其函数和对象安装到名为 sparse_vector 的单独模式中；</p> </li> 
</ul> 
<p><strong>优化器</strong></p> 
<ul> 
 <li> <p>GPORCA 会为投影列表中带有标量子查询的某些查询以及可以使用基础索引的谓词生成无效计划。这可能会导致 Greenplum 数据库在启用优化器的情况下运行某些功能时出现 PANIC。此问题现已解决。</p> </li> 
</ul> 
<p><strong>服务器</strong></p> 
<ul> 
 <li> <p>修复了将日志记录配置为写入 NOTICE 级别消息时查询挂起的问题；</p> </li> 
 <li> <p>修复了在没有目标的情况下定义 VIEW 并且在 pg_attribute 中没有条目时 gpcheckcat 报告错误的问题；</p> </li> 
 <li> <p>修复了位图索引扫描与完整位图页面上的索引 INSERT 同时运行的问题，偶尔无法读取正确的 tid的问题；</p> </li> 
</ul> 
<p><strong>Data Flow</strong></p> 
<ul> 
 <li> <p>在双栈 IPv4 和 IPv6 主机中，如果有另一个进程侦听同一个 IPv6 端口，gpfdist 将绑定到 IPv4 端口但无法绑定到 IPv6 端口。此问题已得到解决。</p> </li> 
</ul> 
<p><strong>集群管理</strong></p> 
<ul> 
 <li> <p>当没有进行扩展，且 gpstate -s 输出显示健康的集群状态时，gpstate 将记录与 gpexapnd.status 相关的 ERROR/FATAL 消息。此问题已得到解决。</p> </li> 
</ul> 
<h2>Greenplum 6.15</h2> 
<h3><strong>新增功能</strong></h3> 
<ul> 
 <li> <p>gprecoverseg 现在重新平衡主机可达的segments，即使有其他segments的主机不可达；对于无法访问的主机上的segments，gprecoverseg 现在会发出警告消息；</p> </li> 
 <li> <p>GPSS（Greenplum Streaming Server）在Greenplum这一版本升级至1.5.2版本；</p> </li> 
 <li> <p>analyzedb utility有一个新的 --skip_orca_root_stats 选项。指定此选项后，analyzedb 将不会更新根分区统计信息。仅当禁用 GPORCA 时才应使用此选项；</p> </li> 
</ul> 
<h2><strong>修复bug列表</strong></h2> 
<p><strong>服务器</strong></p> 
<ul> 
 <li> <p>修复了错误资源组等待队列损坏 (resgroup.c:3502)导致Greenplum Master PANIC 的错误；</p> </li> 
 <li> <p>解决了使用分组功能时返回结果不一致的问题；</p> </li> 
 <li> <p>修复了由于计划程序问题导致查询因 FailedAssertion 错误而崩溃的计划程序问题；</p> </li> 
 <li> <p>禁止在 WHERE 子句中执行带有 set 返回函数的查询，这会导致segment panic。Greenplum 现在会生成类似以下内容的error信息：set-returning functions are not allowed in WHERE clause；</p> </li> 
</ul> 
<p><strong>外部表</strong></p> 
<ul> 
 <li> <p>修复了 escape='OFF' 时 Web External Tables的问题；</p> </li> 
</ul> 
<p><strong>查询优化器</strong></p> 
<ul> 
 <li> <p>某些使用 random() 或 timeofday() 等函数在分区表中选择随机行的查询会导致主机PANIC。此问题已得到解决；</p> </li> 
 <li> <p>修复了针对 CDOUBLE 类型（例如时间戳）的点查询的基数估计的优化器问题；</p> </li> 
</ul> 
<p><strong>analyzedb</strong></p> 
<ul> 
 <li> <p>添加了--skip_orca_root_stats 选项，该选项可防止analyzedb 更新根分区统计信息；</p> </li> 
</ul> 
<p><strong>Data Flow</strong></p> 
<ul> 
 <li> <p>dblink 包括跳过身份验证检查的函数 dblink_connect_no_auth；</p> </li> 
 <li> <p>解决了 gpfdist 从外部表读取导致“No route to host”错误的问题；</p> </li> 
</ul> 
<p><strong>Interconnect</strong></p> 
<ul> 
 <li> <p>解决了当 gp_interconnect_type = proxy 时代理后台工作进程内存使用率高的问题，暂停/恢复流控制进程导致繁忙的接收器缓存或复制数据包，同时等待后端使用它们。Greenplum 数据库现在使用更主动的流控制机制来控制数据包缓冲和传输；</p> </li> 
</ul> 
<p><strong>集群管理</strong></p> 
<ul> 
 <li> <p>gpinitsystem 现在将等效的语言环境等效对待（例如，en_US.UTF-8 现在被视为与 en_US.utf8 相同）；</p> </li> 
 <li> <p>因为 gprecoverseg 现在会报告增量和完整segment恢复的进度，因此不再需要调用 gpstate -m 来确定恢复进度；</p> </li> 
</ul> 
<h2>Greenplum 6.14.1</h2> 
<h3><strong>新增功能</strong></h3> 
<ul> 
 <li> <p>PostGIS 2.5.4+pivotal.4版本已升级，解决了PostGIS ticket中描述的segfault；</p> </li> 
</ul> 
<h3><strong>修复bug列表</strong></h3> 
<p><strong>服务器</strong></p> 
<ul> 
 <li> <p>解决了带有运算符的视图定义中操作数的array类型转换被错误地转换为 anyarray 类型转换的问题。这会导致视图定义的备份和恢复出错；</p> </li> 
 <li> <p>优化了锁以解决 pg_partitions 系统视图上某些 SELECT 查询会等待其他操作获取的锁定的问题；</p> </li> 
 <li> <p>解决了从 5.28 版升级到 6.12 版本后，涉及外部表的查询执行导致查询 PANIC 和segment故障的问题。此问题已通过优化查询子计划解决；</p> </li> 
</ul> 
<p><strong>查询优化器</strong></p> 
<ul> 
 <li> <p>解决了当查询优化器尝试访问函数的参数（例如 random() 或 timeofday()）时，Greenplum 数据库在查询执行期间造成 PANIC，但查询未使用参数调用该函数的问题；</p> </li> 
 <li> <p>此版本优化了 Greenplum 数据库对具有多个连接谓词的连接的性能；</p> </li> 
</ul> 
<p><strong>gpfdist</strong></p> 
<ul> 
 <li> <p>当使用转换配置外部表时，gpfdist 偶尔会返回error 404 Multiple reader to a pipe is forbidden。此问题已解决；</p> </li> 
</ul> 
<h2>Greenplum 6.14.0</h2> 
<h3><strong>新增功能</strong></h3> 
<ul> 
 <li> <p>CentOS/RHEL 8 和 SUSE Linux Enterprise Server x86_64 12 (SLES 12) 客户端软件包以在此 Greenplum 数据库版本中支持；</p> </li> 
 <li> <p>PXF已升级至5.16.1版本；</p> </li> 
 <li> <p>optimizer_join_order 服务器配置参数的默认值从exhaustive更改为exhaustive 2；</p> </li> 
 <li> <p>optimizer_cost_model默认成本模型的服务器配置参数，calibrated已得到增强；GPORCA 现在更有可能使用嵌套循环连接而不是散列连接选择更快的位图索引；</p> </li> 
 <li> <p>GPORCA 通过改进其分区选择算法以更频繁地消除默认分区来提高查询执行性能；</p> </li> 
 <li> <p>GPORCA 会生成一个从left outer join变换为right outer join的等效替代方案；</p> </li> 
 <li> <p>gprecoverseg -a -s 命令的输出已更新以显示更详细的进度信息。用户现在可以以增量模式监视恢复segments的进度；</p> </li> 
 <li> <p>gpcheckperf 命令已更新为支持 Internet 协议版本 6 (IPv6)；</p> </li> 
</ul> 
<h3><strong>修复bug列表</strong></h3> 
<p><strong>服务器</strong></p> 
<ul> 
 <li> <p>解决了在使用非视图关系调用 pg_get_viewdef_name_ext() 函数时 Greenplum 数据库PANIC 的问题；</p> </li> 
 <li> <p>解决了当 gp_workfile_compression=on 时查询异常终止并出现错误 Context should be init first 的问题，因为 Greenplum 数据库忽略了来自 ZSTD 初始化函数的失败返回值；</p> </li> 
 <li> <p>当在实用程序模式连接中运行的查询调用 gp_toolkit.gp_param_setting() 函数时，Greenplum 数据库会 PANIC。此问题已解决；Greenplum 现在在实用模式下会忽略函数的 EXECUTE ON 选项，并且仅在本地节点上执行该函数；</p> </li> 
 <li> <p>在发生故障后的Segment节点的并行恢复和重新平衡过程中，如果Segment重新同步过程中发生错误，主恢复过程将停止并无限期等待。这个问题已被解决；</p> </li> 
</ul> 
<p><strong>查询优化器</strong></p> 
<ul> 
 <li> <p>解决了当查询中的筛选条件匹配多个分区时 GPORCA 无法始终消除默认分区的性能问题；</p> </li> 
 <li> <p>修复了计划优化器问题，该问题由于计划时间由无关索引的排序过程支配，导致查询失败；</p> </li> 
 <li> <p>解决了 GPORCA 不使用动态分区消除并花费很长时间规划包含联合、外连接和子查询混合的查询的问题；</p> </li> 
 <li> <p>解决了 Greenplum 数据库返回错误 no hash_seq_search scan for hash table "Dynamic Table Scan Pid Index" 的问题，因为 GPORCA 生成的查询计划在动态分区消除期间错误地重新扫描了分区选择器。GPORCA 现在会生成不需要这种重新扫描的计划；</p> </li> 
 <li> <p>解决了优化器问题，其中带有 RETURNING 子句的 CTE 查询会失败并显示error：INSERT/UPDATE/DELETE must be execution by a writer segworker group；</p> </li> 
</ul> 
<p><strong>集群管理</strong></p> 
<ul> 
 <li> <p>解决了 gprecoverseg、gpaddmirrors、gpmovemirrors、gpinitstandby 实用程序的文档和 --help 输出问题，其中之前缺少 --hba-hostnames 命令行标志详细信息；</p> </li> 
</ul> 
<p><strong>计划器</strong></p> 
<ul> 
 <li> <p>解决了为涉及系统表和复制表的查询生成的索引扫描可能返回不正确结果的问题。在这种情况下，Greenplum 不再生成索引扫描。</p> </li> 
</ul> 
<h2><strong>Greenplum</strong><strong>大数据平台简</strong><strong>介</strong></h2> 
<p>Greenplum 大数据平台基于MPP（大规模并行处理）架构，具有良好的弹性和线性扩展能力，内置并行存储、并行通讯、并行计算和优化技术，兼容 SQL 标准，具备强大、高效、安全的PB级结构化、半结构化和非结构化数据存储、处理和实时分析能力，同时支持涵盖OLTP型业务的混合负载，为客户打通业务-数据-洞见-业务的闭环，可部署于企业裸机、容器、私有云和公有云中，支撑着全球金融、证券、电信、政府、制造、交通运输等各行业的大量核心生产系统。Greenplum 大数据平台为全球各行各业提供具备实时处理、弹性扩容、弹性计算、混合负载、云原生和集成数据分析能力的强大的大数据引擎，目前广泛的应用于包括金融、保险、证券、通信、航空、物流、零售、媒体、政府、医疗、制造、能源等行业。</p>
                                        </div>
                                      
</div>
            