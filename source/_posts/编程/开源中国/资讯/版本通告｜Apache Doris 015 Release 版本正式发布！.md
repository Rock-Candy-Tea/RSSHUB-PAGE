
---
title: '版本通告｜Apache Doris 0.15 Release 版本正式发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1130/115645_kyPT_4937141.png'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 12:00:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1130/115645_kyPT_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="298" src="https://static.oschina.net/uploads/space/2021/1130/115645_kyPT_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>亲爱的社区小伙伴们，历时数个月精心打磨，我们很高兴地宣布， <strong>Apache Doris 于 2021 年 11 月 29 日迎来了 0</strong><strong>.15.0 Release 版本的正式发布</strong>！<strong>有 99 位 Contributor</strong>为 Apache Doris 提交了近 700 项优化和修复，在此我们也对所有贡献者表示最真诚的感激！</p> 
<p>在 0.15.0 Release 版本中，<strong>我们增加了诸多新功能，对 Apache Doris 的查询性能、易用性、稳定性方面等进行了全面优化</strong>：新增资源划分和隔离功能，用户可以通过资源标签的方式将集群中的 BE 节点划分为资源组，实现对在线、离线业务的统一管理和资源隔离；增加了 Runtime Filter 及 Join Reorder 功能，对多表 Join 场景的查询效率进行了大幅提升，在 Star Schema Benchmark 测试数据集下有 2-10 倍的性能提升；新增导入方式 Binlog Load ，使 Doris 可以增量同步 MySQL 中对数据更新操作的 CDC ；支持 String 列类型，长度最大支持 2GB ；支持 List 分区功能，可以通过枚举值创建分区；支持 Unique Key 模型上的 Update 语句；Spark-Doris-Connector 支持数据写入 Doris …… 还有更多重要特性。</p> 
<p>我们欢迎大家在使用过程中，有任何问题通过 GitHub Discussion 或者 Dev 邮件组与我们取得联系，也期待大家参与社区讨论和建设中 。</p> 
<h3><strong>重要更新</strong></h3> 
<p><strong>资源划分与隔离</strong></p> 
<p>用户可以通过资源标签的方式将一个 Doris 集群中的 BE 节点划分成多个资源组，从而可以进行在线、离线业务的统一管理和节点级别的资源隔离。</p> 
<p>同时，还可以通过限制单个查询任务的 CPU、内存开销以及复杂度，来控制单个查询的资源开销，从而降低不同查询之间的资源抢占问题。</p> 
<p><strong>性能优化</strong></p> 
<p>新增 Runtime Filter 及 Join Reorder 功能。Runtime Filter 功能通过使用 Join 算子中右表的 Join Key 列条件来过滤左表的数据，在大部分 Join 场景下可以显著提升查询效率。如在 Star Schema Benchmark (TPCH 的精简测试集) 下可以获得 2-10 倍的性能提升。</p> 
<p>Join Reorder 功能可以通过通过代价模型自动帮助调整 SQL 中 Join 的顺序，以帮助获得最优的 Join 效率。 可通过会话变量 set enable_cost_based_join_reorder=true 开启。</p> 
<p><strong>新增功能</strong></p> 
<ul> 
 <li>支持直接对接 Canal Server 同步 MySQL binlog 数据。</li> 
 <li>支持 String 列类型，长度范围 1-2GB 。</li> 
 <li>支持 List 分区功能，可以针对枚举值创建分区。</li> 
 <li>支持事务性 Insert 语句功能。可以通过 begin ; insert ; insert; ,… ; commit ; 的方式批量导入数据。</li> 
 <li>支持在 Unique Key 模型上的 Update 语句功能。可以在 Unique Key 模型表上执行 Update Set where 语句。</li> 
 <li>支持 SQL 阻塞名单功能。可以通过正则、Hash 值匹配等方式阻止部分 SQL 的执行。</li> 
 <li>支持 LDAP 登陆验证。</li> 
</ul> 
<p><strong>拓展功能</strong></p> 
<ul> 
 <li>支持 Flink-Doris-Connector 。</li> 
 <li>支持 DataX doriswriter 插件。</li> 
 <li>Spark-Doris-Connector 支持数据写入 Doris 。</li> 
</ul> 
<h3><strong>功能优化</strong></h3> 
<p><strong>查询</strong></p> 
<p>支持在 SQL 查询规划阶段，利用 BE 的函数计算能力计算所有常量表达式。</p> 
<p><strong>导入</strong></p> 
<ul> 
 <li>支持导入文本格式文件时，指定多字节行列分隔符或不可见分隔符。</li> 
 <li>支持通过 Stream Load 导入压缩格式文件。</li> 
 <li>Stream Load 支持导入多行格式的 Json 数据。</li> 
</ul> 
<p><strong>导出</strong></p> 
<ul> 
 <li>支持 Export 导出功能指定 where 过滤条件。支持导出文件使用多字节行列分隔符。支持导出到本地文件。</li> 
 <li>Export 导出功能支持仅导出指定的列。</li> 
 <li>支持通过 outfile 语句导出结果集到本地磁盘，并支持导出后写入导出成功的标记文件。</li> 
</ul> 
<p><strong>易用性</strong></p> 
<ul> 
 <li>动态分区功能支持创建、保留指定的历史分区、支持自动冷热数据迁移设置。</li> 
 <li>支持在命令行使用可视化的树形结构展示查询、导入的计划和 Profile。</li> 
 <li>支持记录并查看 Stream Load 操作日志。</li> 
 <li>通过 Routine Load 消费 Kafka 数据时，可以指定时间点进行消费。</li> 
 <li>支持通过 show create routine load 功能导出 Routine Load 的创建语句。</li> 
 <li>支持通过 pause/resume all routine load 命令一键启停所有 Routine Load Job。</li> 
 <li>支持通过 alter routine load 语句修改 Routine Load 的 Broker List 和 Topic。</li> 
 <li>支持 create table as select 功能。</li> 
 <li>支持通过 alter table 命令修改列注释和表注释。</li> 
 <li>show tablet status 增加表创建时间、数据更新时间。</li> 
 <li>支持通过 show data skew 命令查看表的数据量分布，以排查数据倾斜问题。</li> 
 <li>支持通过 show/clean trash 命令查看 BE 文件回收站的磁盘占用情况并主动清除。</li> 
 <li>支持通过 show view 语句展示一个表被哪些视图所引用。</li> 
</ul> 
<p><strong>新增函数</strong></p> 
<ul> 
 <li>bitmap_min , bit_length</li> 
 <li>yearweek , week , makedate</li> 
 <li>percentile 精确百分位函数</li> 
 <li>json_array，json_object，json_quote</li> 
 <li>支持为 AES_ENCRYPT 和 AES_DECRYPT 函数创建自定义公钥。</li> 
 <li>支持通过 create alias function 创建函数别名来组合多个函数。</li> 
</ul> 
<p><strong>其他</strong></p> 
<ul> 
 <li>支持访问 SSL 连接协议的 ES 外表。</li> 
 <li>支持在动态分区属性中指定热点分区的数量，热点分区将存储在 SSD 磁盘中。</li> 
 <li>支持通过 Broker Load 导入 Json 格式数据。</li> 
 <li>支持直接通过 libhdfs3 库访问 HDFS 进行数据的导入导出，而不需要 Broker 进程。</li> 
 <li>select into outfile 功能支持导出 Parquet 文件格式，并支持并行导出。</li> 
 <li>ODBC 外表支持 SQLServer。</li> 
</ul> 
<h3><strong>下载使用</strong></h3> 
<p><strong>下载地址</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoris.apache.org%2Fmaster%2Fzh-CN%2Fdownloads%2Fdownloads.html" target="_blank">http://doris.apache.org/master/zh-CN/downloads/downloads.html</a></p> 
<p><strong>升级说明</strong></p> 
<p>您可以从 Apache Doris 0.14.0 或 0.14.x 发行版本直接升级到 0.15.0 Release 版本，升级过程请参考文档：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoris.apache.org%2Fmaster%2Fzh-CN%2Finstalling%2Fupgrade.html" target="_blank">http://doris.apache.org/master/zh-CN/installing/upgrade.html</a></p> 
<p><strong>更新日志</strong></p> 
<p>详细 Release Note 请查看链接：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-doris%2Fissues%2F6806" target="_blank">https://github.com/apache/incubator-doris/issues/6806</a></p> 
<p><strong>意见反馈</strong></p> 
<p>如果您遇到任何使用上的问题，欢迎随时通过 GitHub Discussion 论坛或者 Dev 邮件组与我们取得联系。</p> 
<p>GitHub 论坛：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-doris%2Fdiscussions" target="_blank">https://github.com/apache/incubator-doris/discussions</a></p> 
<p>Dev 邮件组：dev@doris.apache.org</p> 
<h3><strong>致谢</strong></h3> 
<p>Apache Doris 0.15.0 Release 版本的发布离不开所有社区用户的支持，在此向所有参与版本设计、开发、测试、讨论的社区贡献者们表示感谢，他们分别是：</p> 
<p>一<strong>贡献者名单</strong>一</p> 
<ul> 
 <li>@924060929</li> 
 <li>@acelyc111</li> 
 <li>@Aimiyoo</li> 
 <li>@amosbird</li> 
 <li>@arthur-zhang</li> 
 <li>@azurenake</li> 
 <li>@BiteTheDDDDt</li> 
 <li>@caiconghui</li> 
 <li>@caneGuy</li> 
 <li>@caoliang-web</li> 
 <li>@ccoffline</li> 
 <li>@chaplinthink</li> 
 <li>@chovy-3012</li> 
 <li>@ChPi</li> 
 <li>@copperybean</li> 
 <li>@crazyleeyang</li> 
 <li>@dh-cloud</li> 
 <li>@DinoZhang</li> 
 <li>@dixingxing0</li> 
 <li>@dohongdayi</li> 
 <li>@e0c9</li> 
 <li>@EmmyMiao87</li> 
 <li>@eyesmoons</li> 
 <li>@francisoliverlee</li> 
 <li>@Gabriel39</li> 
 <li>@gaodayue</li> 
 <li>@GoGoWen</li> 
 <li>@HappenLee</li> 
 <li>@harveyyue</li> 
 <li>@Henry2SS</li> 
 <li>@hf200012</li> 
 <li>@huangmengbin</li> 
 <li>@huozhanfeng</li> 
 <li>@huzk8</li> 
 <li>@hxianshun</li> 
 <li>@ikaruga4600</li> 
 <li>@JameyWoo</li> 
 <li>@Jennifer88huang</li> 
 <li>@JinLiOnline</li> 
 <li>@jinyuanlu</li> 
 <li>@JNSimba</li> 
 <li>@killxdcj</li> 
 <li>@kuncle</li> 
 <li>@liutang123</li> 
 <li>@luozenglin</li> 
 <li>@luzhijing</li> 
 <li>@MarsXDM</li> 
 <li>@mh-boy</li> 
 <li>@mk8310</li> 
 <li>@morningman</li> 
 <li>@Myasuka</li> 
 <li>@nimuyuhan</li> 
 <li>@pan3793</li> 
 <li>@PatrickNicholas</li> 
 <li>@pengxiangyu</li> 
 <li>@pierre94</li> 
 <li>@qidaye</li> 
 <li>@qzsee</li> 
 <li>@shiyi23</li> 
 <li>@smallhibiscus</li> 
 <li>@songenjie</li> 
 <li>@spaces-X</li> 
 <li>@stalary</li> 
 <li>@stdpain</li> 
 <li>@Stephen-Robin</li> 
 <li>@Sunt-ing</li> 
 <li>@Taaang</li> 
 <li>@tarepanda1024</li> 
 <li>@tianhui5</li> 
 <li>@tinkerrrr</li> 
 <li>@TobKed</li> 
 <li>@ucasfl</li> 
 <li>@Userwhite</li> 
 <li>@vinson0526</li> 
 <li>@wangbo</li> 
 <li>@wangliansong</li> 
 <li>@wangshuo128</li> 
 <li>@weajun</li> 
 <li>@weihongkai2008</li> 
 <li>@weizuo93</li> 
 <li>@WindyGao</li> 
 <li>@wunan1210</li> 
 <li>@wuyunfeng</li> 
 <li>@xhmz</li> 
 <li>@xiaokangguo</li> 
 <li>@xiaoxiaopan118</li> 
 <li>@xinghuayu007</li> 
 <li>@xinyiZzz</li> 
 <li>@xuliuzhe</li> 
 <li>@xxiao2018</li> 
 <li>@xy720</li> 
 <li>@yangzhg</li> 
 <li>@yx91490</li> 
 <li>@zbtzbtzbt</li> 
 <li>@zenoyang</li> 
 <li>@zh0122</li> 
 <li>@zhangboya1</li> 
 <li>@zhangstar333</li> 
 <li>@zuochunwei</li> 
</ul>
                                        </div>
                                      
</div>
            