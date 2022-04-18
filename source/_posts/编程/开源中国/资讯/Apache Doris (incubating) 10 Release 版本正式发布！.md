
---
title: 'Apache Doris (incubating) 1.0 Release 版本正式发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0418/184914_5Rgc_4252687.jpg'
author: 开源中国
comments: false
date: Mon, 18 Apr 2022 18:42:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0418/184914_5Rgc_4252687.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>亲爱的社区小伙伴们，历时数月，我们很高兴地宣布，Apache Doris (incubating) 于 2022 年 4 月 18 日迎来了</span><strong><span style="color:#0052ff"> </span></strong><span>1.0 Release 版本的正式发布！<strong style="color:#0052ff">这是 Apache Doris 在进入 Apache 基金会孵化以来的第一个 1 位版本，也是迄今为止对 Apache Doris 核心代码重构幅度最大的一个版本</strong></span><strong><span style="color:#0052ff">！</span></strong><span>有<span> </span><strong style="color:#0052ff">114 位 Contributor </strong>为 Apache Doris 提交了<strong style="color:#0052ff">超过 660 项优化和修复</strong>，感谢每一个让 Apache Doris 变得更好的你！</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>在 1.0 版本中，我们引入了向量化执行引擎、Hive 外部表、Lateral View 语法及 Table Function 表函数、Z-Order 数据索引、Apache SeaTunnel 插件等重要功能，增加了对 Flink CDC 同步更新和删除数据的支持，优化了诸多数据导入和查询过程中的问题，对 Apache Doris 的查询性能、易用性、稳定性等多方特效进行了全面加强，欢迎大家下载使用！</span></p> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:center"><strong>特别鸣谢</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>每一个不曾发版的日子，背后都有无数贡献者枕戈待旦</span><span>，不敢停歇半分。在此我们尤其要感谢来自</span><span style="color:#0052ff"><strong>向量化执行引擎、查询优化器、可视化运维平台 等 SIG （专项兴趣小组）的小伙伴</strong></span><span>。自 2021 年 8 月 Apache Doris 社区 SIG 小组成立以来，</span><span style="color:#0052ff"><strong>来自百度、美团、小米、京东、蜀海、字节跳动、腾讯、网易、阿里巴巴、PingCAP、Nebula Graph 等十余家公司的数十名贡献者</strong></span><span>作为首批成员加入到 SIG 中，第一次以专项小组的开源协作形式完成了向量化执行引擎、查询优化器、 Doris Manager 可视化监控运维平台等如此重大功能的开发，</span><span style="color:#0052ff"><strong>历时半年以上、开展技术调研和分享数十次、召开远程会议近百次、累计提交 Commits 多达数百个、涉及代码行数高达十余万行</strong></span><span>，正是因为有他们的贡献，才有 1.0 版本的问世，让我们再次对他们的辛勤付出表示最真诚的感谢！</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>与此同时，Apache Doris 的贡献者数量已超过 300 人（ 点击回顾：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MDEyODc1OA%3D%3D%26mid%3D2247508593%26idx%3D1%26sn%3Ded11b54d8412b675e385b30d0529cade%26chksm%3Dcfe3b268f8943b7e4d3393aa6e11c4a59a6652269a9444591a0ed982c6f007f4c5f9bf006b6b%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0052ff">社区动态｜Apache Doris 迎来第 300 位 Contributor ！</span></a><span>），每月活跃的贡献者数量超过了 60 人，近几周平均每周提交的 Commits 数量也超过 80，社区聚集的开发者规模及活跃度已经有了极大的提升。我们十分期待有更多的小伙伴参与社区贡献中来，与我们一道把 Apache Doris 打造成全球顶级的分析型数据库，也期待所有小伙伴可以与我们一起收获宝贵的成长。如果你想参与社区，欢迎通过开发者邮箱<span> </span></span><span style="color:#0052ff">dev@doris.apache.org</span><span> 与我们取得联系。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><img alt height="296" src="https://static.oschina.net/uploads/space/2022/0418/184914_5Rgc_4252687.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><strong style="color:#000000"><span>重要更新 </span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">过去 Apache Doris 的 SQL 执行引擎是基于行式内存格式以及基于传统的火山模型进行设计的，在进行 SQL 算子与函数运算时存在非必要的开销，导致 Apache Doris 执行引擎的效率受限，并不适应现代 CPU 的体系结构。</span><span style="color:rgba(0, 0, 0, 0.85)">向量化执行引擎的目标是替换 Apache Doris 当前的行式 SQL 执行引擎，充分释放现代 CPU 的计算能力，突破在 SQL 执行引擎上的性能限制，发挥出极致的性能表现。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">基于现代 CPU 的特点与火山模型的执行特点，向量化执行引擎重新设计了在列式存储系统的 SQL 执行引擎：</span></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">重新组织内存的数据结构，用 Column替换 Tuple，提高了计算时 Cache 亲和度，分支预测与预取内存的友好度</span></p> </li> 
 <li style="text-align:left"> <p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">分批进行类型判断，在本次批次中都使用类型判断时确定的类型，将每一行类型判断的虚函数开销分摊到批量级别。</span></p> </li> 
 <li style="text-align:left"> <p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">通过批级别的类型判断，消除了虚函数的调用，让编译器有函数内联以及 SIMD 优化的机会</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">从而大大提高了 CPU 在 SQL 执行时的效率，提升了 SQL 查询的性能。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">在 Apache Doris 1.0 版本中，通过 </span><span style="background-color:#d6d6d6; color:rgba(0, 0, 0, 0.85)"> set batch_size = 4096 </span><span style="color:rgba(0, 0, 0, 0.85)"> 和<span style="background-color:#ffffff"> </span><span style="background-color:#d6d6d6"> set enable_vectorized_engine = true </span>开启向量化执行引擎，多数情况下可显著提升查询性能。在 SSB 和 OnTime 标准测试数据集下，多表关联和宽列查询两大场景的整体性能分别有 3 倍和 2.6 倍的提升。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><img alt height="323" src="https://static.oschina.net/uploads/space/2022/0418/184930_mhsH_4252687.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><img alt height="379" src="https://static.oschina.net/uploads/space/2022/0418/184941_H0Be_4252687.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  </span></strong><strong><span>Lateral View 语法 <strong><span>[Experimental</span></strong></span></strong><strong><span><strong><span>]</span></strong></span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">通过 Lateral View 语法，我们可以使用 explod_bitmap 、explode_split、explode_jaon_array  等 Table Function 表函数，将 bitmap、String 或 Json Array 由一列展开成多行，以便后续可以对展开的数据进行进一步处理（如 Filter、Join 等）。</span></p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  Hive 外表 <strong><span>[Experimental]</span></strong></span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">Hive External Table 为用户提供了通过 Doris 直接访问 Hive 表的能力，外部表省去了 繁琐的数据导入工作，可以借助 Doris 本身 OLAP 的能力来解决 Hive 表的数据分析问题。当前版本支持将 Hive 数据源接入 Doris，并支持通过 Doris 与 Hive 数据源中的数据进行联邦查询，进行更加复杂的分析操作。</span></p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  支持 Z-Order 数据排序格式</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">Apache Doris 数据是按照前缀列排序存储的，因此在包含前缀查询条件时，可以在排序数据上进行快速的数据查找，但如果查询条件不是前缀列，则无法利用数据排序的特征进行快速数据查找。通过 Z-Order Indexing 可以解决上述问题，在 1.0 版本中我们增加了 Z-Order 数据排序格式，在看板类多列查询的场景中可以起到很好过滤效果，加速对非前缀列条件的过滤性能。</span></p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  支持 Apache SeaTunnel (incubating) 插件</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">Apache SeaTunnel 是一个高性能的分布式数据集成框架，架构于 Apache Spark 和 Apache Flink 之上。在 Apache Doris 1.0 版本中，我们增加了 SaeTunnel 插件，用户可以借助 Apache SeaTunnel 进行多数据源之间的同步和 ETL。</span></p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  新增函数</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:rgba(0, 0, 0, 0.85)">支持更多 bitmap 函数，具体可查看函数手册：</span></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_max</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_and_not</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_and_not_count</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_has_all</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_and_count</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_or_count</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_xor_count</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">bitmap_subset_limit</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">sub_bitmap</span></p> </li> 
</ul> 
<p><span style="color:rgba(0, 0, 0, 0.85)">支持国密算法 SM3/SM4；</span></p> 
<p><span style="color:rgba(0, 0, 0, 0.85)"><strong style="color:#222222"><span>注意</span></strong><span style="background-color:#ffffff">：以上标记 <span>[Experimental]</span> 的功能为实验性功能，我们将会在后续版本中对以上功能进行持续优化和迭代，并后续版本中进一步完善。在使用过程中有任何问题或意见，欢迎随时与我们联系。</span></span></p> 
<p style="text-align:center"><span style="color:#000000"><strong><span> 重要优化 </span></strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  功能优化</span></strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">降低大批量导入时，生成的 Segment 文件数量，以降低 Compaction 压力。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">通过 BRPC 的 attachment 功能传输数据，以查询过程中的降低序列化和反序列化开销。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">支持直接返回 HLL/BITMAP 类型的二进制数据，用于业务在外侧解析。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)"><span style="background-color:#ffffff">优化并降低 BRPC 出现 OVERCROWDED 和 NOT_CONNECTED 错误的概率，增强系统稳定</span>性<span style="background-color:#ffffff">。</span></span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">增强导入的容错性。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">支持通过 Flink CDC 同步更新和删除数据。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">支持自适应的 Runtime Filter。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">显著降低 insert into 操作的内存占用</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"> </p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  易用性改进</span></strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">Routine Load 支持显示当前 offset 延迟数量等状态。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">FE audit log 中增加查询峰值内存使用量的统计。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">Compaction URL 结果中增加缺失版本的信息，方便排查问题。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">支持将 BE 标记为不可查询或不可导入，以快速屏蔽问题节点。</span></p> </li> 
</ul> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  重要 Bug 修复</span></strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">修复若干查询错误问题。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">修复 Broker Load 若干调度逻辑问题。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">修复 STREAM 关键词导致元数据无法加载的问题。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">修复 Decommission 无法正确执行的问题。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">修复部分情况下操作 Schema Change 操作可能出现 -102 错误的问题。</span></p> </li> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0"><span style="color:rgba(0, 0, 0, 0.85)">修复部分情况下使用 String 类型可能导致 BE 宕机的问题。</span></p> </li> 
</ul> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  其他</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.85)">增加 Minidump 功能；</span></p> 
<p><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  补充说明</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.85)">Doris Manger 可视化监控运维平台也将在近期发布 1.0 版本，目前已经进入 Release 流程中，后续将独立发布发版通告，请大家持续关注。</span></p> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:center"><strong><span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.85)">下载使用</span></strong></p> 
<p><span><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  下载使用</span></strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#0052ff">http://doris.apache.org/zh-CN/downloads/downloads.html</span></p> 
<p><span><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  升级说明</span></strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>您可以从 Apache Doris 0.15.0 或 0.15.x 发行版本直接升级到 1.0 Release 版本，升级过程请参考文档：</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#0052ff">http://doris.apache.org/zh-CN/installing/upgrade.html</span></p> 
<p><span><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  更新日志</span></strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>详细 Release Note 请查看链接：</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#0052ff">https://github.com/apache/incubator-doris/issues/8549</span></p> 
<p><span><strong><span style="background-color:#0052ff"> </span></strong><strong><span>  意见反馈</span></strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>如果您遇到任何使用上的问题，欢迎随时<span style="background-color:#ffffff">通过 GitHub Discussion 论坛或者 Dev 邮件组</span>与我们取得联系。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>GitHub 论坛：</span><span style="color:#0052ff">https://github.com/apache/incubator-doris/discussions</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>Dev 邮件组：</span><span style="background-color:#ffffff; color:#0052ff">dev@doris.apache.org‍</span></p> 
<p style="text-align:center"><strong style="color:#000000"><span> 致 谢</span></strong></p> 
<p><span style="background-color:#ffffff; color:#222222">Apache Doris(incubating) 1.0 Release 版本的发布离不开所有社区用户的支持，在此向所有参与版本设计、开发、测试、讨论的社区贡献者们表示感谢。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">他们分别是：</span></p> 
<p style="margin-left:0; margin-right:0"><span>@924060929</span></p> 
<p style="margin-left:0; margin-right:0"><span>@adonis0147</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Aiden-Dong</span></p> 
<p style="margin-left:0; margin-right:0"><span>@aihai</span></p> 
<p style="margin-left:0; margin-right:0"><span>@airborne12</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Alibaba-HZY</span></p> 
<p style="margin-left:0; margin-right:0"><span>@amosbird</span></p> 
<p style="margin-left:0; margin-right:0"><span>@arthuryangcs</span></p> 
<p style="margin-left:0; margin-right:0"><span>@awakeljw</span></p> 
<p style="margin-left:0; margin-right:0"><span>@bingzxy</span></p> 
<p style="margin-left:0; margin-right:0"><span>@BiteTheDDDDt</span></p> 
<p style="margin-left:0; margin-right:0"><span>@blackstar-baba</span></p> 
<p style="margin-left:0; margin-right:0"><span>@caiconghui</span></p> 
<p style="margin-left:0; margin-right:0"><span>@CalvinKirs</span></p> 
<p style="margin-left:0; margin-right:0"><span>@cambyzju</span></p> 
<p style="margin-left:0; margin-right:0"><span>@caoliang-web</span></p> 
<p style="margin-left:0; margin-right:0"><span>@ccoffline</span></p> 
<p style="margin-left:0; margin-right:0"><span>@chaplinthink</span></p> 
<p style="margin-left:0; margin-right:0"><span>@chovy-3012</span></p> 
<p style="margin-left:0; margin-right:0"><span>@ChPi</span></p> 
<p style="margin-left:0; margin-right:0"><span>@DarvenDuan</span></p> 
<p style="margin-left:0; margin-right:0"><span>@dataalive</span></p> 
<p style="margin-left:0; margin-right:0"><span>@dataroaring</span></p> 
<p style="margin-left:0; margin-right:0"><span>@dh-cloud</span></p> 
<p style="margin-left:0; margin-right:0"><span>@dohongdayi</span></p> 
<p style="margin-left:0; margin-right:0"><span>@dongweizhao</span></p> 
<p style="margin-left:0; margin-right:0"><span>@drgnchan</span></p> 
<p style="margin-left:0; margin-right:0"><span>@e0c9</span></p> 
<p style="margin-left:0; margin-right:0"><span>@EmmyMiao87</span></p> 
<p style="margin-left:0; margin-right:0"><span>@englefly</span></p> 
<p style="margin-left:0; margin-right:0"><span>@eyesmoons</span></p> 
<p style="margin-left:0; margin-right:0"><span>@freemandealer</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Gabriel39</span></p> 
<p style="margin-left:0; margin-right:0"><span>@gaodayue</span></p> 
<p style="margin-left:0; margin-right:0"><span>@GoGoWen</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Gongruixiao</span></p> 
<p style="margin-left:0; margin-right:0"><span>@gwdgithubnom</span></p> 
<p style="margin-left:0; margin-right:0"><span>@HappenLee</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Henry2SS</span></p> 
<p style="margin-left:0; margin-right:0"><span>@hf200012</span></p> 
<p style="margin-left:0; margin-right:0"><span>@htyoung</span></p> 
<p style="margin-left:0; margin-right:0"><span>@jacktengg</span></p> 
<p style="margin-left:0; margin-right:0"><span>@jackwener</span></p> 
<p style="margin-left:0; margin-right:0"><span>@JNSimba</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Keysluomo</span></p> 
<p style="margin-left:0; margin-right:0"><span>@kezhenxu94</span></p> 
<p style="margin-left:0; margin-right:0"><span>@killxdcj</span></p> 
<p style="margin-left:0; margin-right:0"><span>@lihuigang</span></p> 
<p style="margin-left:0; margin-right:0"><span>@littleeleventhwolf</span></p> 
<p style="margin-left:0; margin-right:0"><span>@liutang123</span></p> 
<p style="margin-left:0; margin-right:0"><span>@liuzhuang2017</span></p> 
<p style="margin-left:0; margin-right:0"><span>@lonre</span></p> 
<p style="margin-left:0; margin-right:0"><span>@lovingfeel</span></p> 
<p style="margin-left:0; margin-right:0"><span>@luozenglin</span></p> 
<p style="margin-left:0; margin-right:0"><span>@luzhijing</span></p> 
<p style="margin-left:0; margin-right:0"><span>@MeiontheTop</span></p> 
<p style="margin-left:0; margin-right:0"><span>@mh-boy</span></p> 
<p style="margin-left:0; margin-right:0"><span>@morningman</span></p> 
<p style="margin-left:0; margin-right:0"><span>@mrhhsg</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Myasuka</span></p> 
<p style="margin-left:0; margin-right:0"><span>@nimuyuhan</span></p> 
<p style="margin-left:0; margin-right:0"><span>@obobj</span></p> 
<p style="margin-left:0; margin-right:0"><span>@pengxiangyu</span></p> 
<p style="margin-left:0; margin-right:0"><span>@qidaye</span></p> 
<p style="margin-left:0; margin-right:0"><span>@qzsee</span></p> 
<p style="margin-left:0; margin-right:0"><span>@renzhimin7</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Royce33</span></p> 
<p style="margin-left:0; margin-right:0"><span>@SleepyBear96</span></p> 
<p style="margin-left:0; margin-right:0"><span>@smallhibiscus</span></p> 
<p style="margin-left:0; margin-right:0"><span>@sodamnsure</span></p> 
<p style="margin-left:0; margin-right:0"><span>@spaces-X</span></p> 
<p style="margin-left:0; margin-right:0"><span>@sparklezzz</span></p> 
<p style="margin-left:0; margin-right:0"><span>@stalary</span></p> 
<p style="margin-left:0; margin-right:0"><span>@steadyBoy</span></p> 
<p style="margin-left:0; margin-right:0"><span>@tarepanda1024</span></p> 
<p style="margin-left:0; margin-right:0"><span>@THUMarkLau</span></p> 
<p style="margin-left:0; margin-right:0"><span>@tianhui5</span></p> 
<p style="margin-left:0; margin-right:0"><span>@tinkerrrr</span></p> 
<p style="margin-left:0; margin-right:0"><span>@ucasfl</span></p> 
<p style="margin-left:0; margin-right:0"><span>@Userwhite</span></p> 
<p style="margin-left:0; margin-right:0"><span>@vinson0526</span></p> 
<p style="margin-left:0; margin-right:0"><span>@wangbo</span></p> 
<p style="margin-left:0; margin-right:0"><span>@wangshuo128</span></p> 
<p style="margin-left:0; margin-right:0"><span>@wangyf0555</span></p> 
<p style="margin-left:0; margin-right:0"><span>@weajun</span></p> 
<p style="margin-left:0; margin-right:0"><span>@weizuo93</span></p> 
<p style="margin-left:0; margin-right:0"><span>@whutpencil</span></p> 
<p style="margin-left:0; margin-right:0"><span>@WindyGao</span></p> 
<p style="margin-left:0; margin-right:0"><span>@wunan1210</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xiaokang</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xiaokangguo</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xiedeyantu</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xinghuayu007</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xingtanzjr</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xinyiZzz</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xtr1993</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xu20160924</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xuliuzhe</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xuzifu666</span></p> 
<p style="margin-left:0; margin-right:0"><span>@xy720</span></p> 
<p style="margin-left:0; margin-right:0"><span>@yangzhg</span></p> 
<p style="margin-left:0; margin-right:0"><span>@yiguolei</span></p> 
<p style="margin-left:0; margin-right:0"><span>@yinzhijian</span></p> 
<p style="margin-left:0; margin-right:0"><span>@yjant</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zbtzbtzbt</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zenoyang</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zh0122</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zhangstar333</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zhannngchen</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zhengshengjun</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zhengshiJ</span></p> 
<p style="margin-left:0; margin-right:0"><span>@ZhikaiZuo</span></p> 
<p style="margin-left:0; margin-right:0"><span>@ztgoto</span></p> 
<p style="margin-left:0; margin-right:0"><span>@zuochunwei</span></p> 
<hr> 
<p><span>相关链接：</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#15a9ca"><strong>Apache Doris官方网站：</strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>http://doris.incubator.apache.org</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#15a9ca"><strong>Apache Doris Githu</strong><strong>b：</strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>https://github.com/apache/incubator-doris</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#15a9ca"><strong>Apache Doris 开发者邮件组：</strong></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span>dev@doris.apache.org</span><span> </span></p>
                                        </div>
                                      
</div>
            