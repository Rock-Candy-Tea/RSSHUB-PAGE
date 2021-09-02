
---
title: '大数据技术漫谈 ——从Hadoop、Storm、Spark、HBase到Hive、Flink、Lindorm'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ea1bfeca794fcba4b338d61bb8e159~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 18:42:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ea1bfeca794fcba4b338d61bb8e159~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>笔者曾效力于新浪广告DMP组，跑过MapReduce，也写过Storm、Spark Streaming、Hive；也曾作为阿里巴巴回血红包的技术负责人，使用Blink扛住双十一80万QPS流量洪峰，负责数十亿现金红包的发放，该项目代码的精简脱敏版本在阿里云上开放，作为Blink在电商领域的最佳实践；也曾在支撑了阿里十余个团队、数十个业务的技术产品——任务引擎中大胆弃用传统的分库分表数据库，而采用超前的云原生多模数据库Lindorm，有丰富的使用和踩坑经验。</p>
<p>基于以上个人经历，我想简单讲讲最近五年间大数据领域技术栈的演进史，并对其中提到的部分关键技术做展开说明。</p>
<p>本文重点在于总括性的概述，部分论点来源于个人使用经历，并不是行业公认的结论，如有谬误欢迎指正。</p>
<h2 data-id="heading-1">二、大数据技术划分</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ea1bfeca794fcba4b338d61bb8e159~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三、大数据技术历史演进</h2>
<h3 data-id="heading-3">3.1 流式计算历史演进</h3>
<p>目前主流的流式计算框架有Storm/Jstorm、Spark Streaming、Flink/Blink三种。</p>
<p>Apache Storm是一个分布式实时大数据处理系统。Storm设计用于在容错和水平可扩展方法中处理大量数据。它是一个流数据框架，具有最高的摄取率。在Storm中，需要先设计一个实时计算结构，我们称之为拓扑（topology）。之后，这个拓扑结构会被提交给集群，其中主节点（master node）负责给工作节点（worker node）分配代码，工作节点负责执行代码。在一个拓扑结构中，包含spout和bolt两种角色。数据在spouts之间传递，这些spouts将数据流以tuple元组的形式发送；而bolt则负责转换数据流。Jstorm则是阿里巴巴使用Java语言复刻的Apache Storm，号称性能四倍于Apache Storm，于2016年停止更新。</p>
<p>Spark Streaming，即核心Spark API的扩展，不像Storm那样一次处理一个数据流。相反，它在处理数据流之前，会按照时间间隔对数据流进行分段切分。Spark针对连续数据流的抽象，我们称为DStream（Discretized Stream）。DStream是小批处理的RDD（弹性分布式数据集），RDD则是分布式数据集，可以通过任意函数和滑动数据窗口（窗口计算）进行转换，实现并行操作。</p>
<p>Apache Flink是针对流数据+批数据的计算框架。把批数据看作流数据的一种特例，延迟性较低（毫秒级），且能够保证消息传输不丢失不重复。Flink创造性地统一了流处理和批处理，作为流处理看待时输入数据流是无界的，而批处理被作为一种特殊的流处理，只是它的输入数据流被定义为有界的。Flink程序由Stream和Transformation这两个基本构建块组成，其中Stream是一个中间结果数据，而Transformation是一个操作，它对一个或多个输入Stream进行计算处理，输出一个或多个结果Stream。</p>
<p>这三种计算框架的对比如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36769b17167748eab8374c93bc115c91~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fjiangjunshow%2Farticle%2Fdetails%2F100798240%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/jiangjunshow/article/details/100798240%EF%BC%89" ref="nofollow noopener noreferrer">blog.csdn.net/jiangjunsho…</a></p>
<p>通过以上分析可知，Flink/Blink是当前流式计算领域的主流框架。</p>
<h3 data-id="heading-4">3.2 离线计算历史演进</h3>
<p>离线计算就是在计算开始前已知所有输入数据，输入数据不会产生变化。离线计算领域主要有Hadoop MapReduce、Spark、Hive/ODPS等计算框架。</p>
<p>使用Hadoop MapReduce进行数据处理，需要用java、python等语言进行开发调试，分别编写Map、Reduce函数，并需要开发者自己对于Map和Reduce过程做性能优化，开发门槛较高，计算框架提供给开发者的助益并不多。在性能优化方面，常见的有在做小表跟大表关联的时候，可以先把小表放到缓存中（通过调用MapReduce的api），另外可以通过重写Combine跟Partition的接口实现，压缩从Map到reduce中间数据处理量达到提高数据处理性能。</p>
<p>Spark基于内存计算的准MapReduce，在离线数据处理中，一般使用Spark SQL进行数据清洗，目标文件一般是放在HDFS或者NFS上。</p>
<p>Hive是一种建立在Hadoop文件系统上的数据仓库架构，并对存储在HDFS中的数据进行分析与管理。Hive在Hadoop上架了一层SQL接口，可以将SQL翻译成MapReduce去Hadoop上执行，这样就使得数据开发和分析人员很方便的使用SQL来完成海量数据的统计和分析，而不必使用编程语言开发MapReduce，从而降低了数据开发的门槛。</p>
<p>目前业内离线数据处理，阿里的Odps平台（阿里内部的离线处理平台）底层利用自己的一套Hadoop集群每天提供PB级的数据处理，华为目前还是在基于Hadoop集群云化ETL处理数据，而字节跳动的数据平台在离线计算方向也主要运用Hive。</p>
<p>综合来看，Hive的学习成本最低，各大公司应用最广泛。</p>
<h3 data-id="heading-5">3.3 列式存储NOSQL数据库历史演进</h3>
<p>NOSQL的概念博大精深，有键值（Key-Value）数据库、面向文档（Document-Oriented）数据库、列存储（Wide Column Store/Column-Family）数据库、图（Graph-Oriented）数据库等，本章节主要讲述列存储数据库中最流行的HBase及其替代品Lindorm。</p>
<p>HBase是一个基于HDFS的、分布式的、面向列（列族）的非关系型数据库（NOSQL）。HBase巧妙地将大而稀疏的表放在商用的服务器集群上，单表可以有十亿行百万列，而且可以通过线性方式从下到上增加节点来进行横向扩展，读写性能优秀，支持批量导入，无需分库分表，存储计算分离，成本低，弹性好。</p>
<p>Lindorm是新一代面向在线海量数据处理的分布式数据库，适用于任何规模、多种模型的云原生数据库服务，其基于存储计算分离、多模共享融合的云原生架构设计，具备弹性、低成本、稳定可靠、简单易用、开放、生态友好等优势。</p>
<p>总体来说，Lindorm是HBase的升级版本，性能和稳定性等等通通优于HBase，如果需要使用海量数据提供在线服务，可以考虑Lindorm。</p>
<h3 data-id="heading-6">3.4 大数据开发语言历史演进</h3>
<p>Scala语言曾是大数据开发的宠儿，行业内热度最高的消息中间件kafka就是使用Scala写就的，而大数据领域杀手级框架Spark也是由Scala编写的。另外，Scala语言函数式编程风格、天然适合处理大规模数据的Lambda表达式、简洁优雅的语法糖、陡峭的学习曲线也深受对代码美感有极致追求的程序员所喜爱。</p>
<p>曾经，Kafka + Scala + Spark + Spark Streaming的技术体系可以通吃批处理和流处理，直到一统批流、学习曲线也更平缓的Flink/Blink出现，彻底打破了这个局面，SQL语言在大数据处理中的占比大大提高。</p>
<p>当前，大数据开发语言可谓百花齐放、各领风骚。其中，SQL语言（编写Flink/Blink、Hive任务）在数据仓库建设和数据分析领域应用广泛，JVM语系（Java、Scala为主）在Hadoop生态中举足轻重并且是数据平台开发的首选，Python在人工智能方向极为受宠，R语言则是数据建模和数据可视化的利器。每种语言都有自己的适用场景，建议根据自身的工种和兴趣来做选择。</p>
<h3 data-id="heading-7">3.5 大数据学习建议</h3>
<p>基于上述章节大数据技术栈演进史的分析，建议对数据开发感兴趣的同学学习以下大数据组件：</p>
<p>1）流式、实时计算：Flink</p>
<p>2）离线计算：Hive</p>
<p>3）列式存储NOSQL数据库：Lindorm</p>
<h2 data-id="heading-8">四、云原生多模数据库Lindorm介绍</h2>
<h3 data-id="heading-9">4.1 Lindorm介绍</h3>
<blockquote>
<p>Lindorm是一款适用于任何规模、多种模型的云原生数据库服务，支持海量数据的低成本存储处理和弹性按需付费，提供宽表、时序、搜索、文件等多种数据模型，兼容HBase、Cassandra、Phoenix、OpenTSDB、Solr、SQL等多种开源标准接口，是为阿里巴巴核心业务提供关键支撑的数据库之一。</p>
</blockquote>
<blockquote>
<p>Lindorm创新性地使用存储计算分离、多模共享融合的云原生架构，以适应云计算时代资源解耦和弹性伸缩的诉求。其中云原生存储引擎LindormStore为统一的存储底座，向上构建各个垂直专用的多模引擎，包括宽表引擎、时序引擎、搜索引擎、文件引擎。在多模引擎之上，Lindorm既提供统一的SQL访问，支持跨模型的联合查询，又提供多个开源标准接口(HBase/Phoenix/Cassandra、OpenTSDB、Solr、HDFS)，满足存量业务无缝迁移的需求。最后，统一的数据Stream总线负责引擎之间的数据流转和数据变更的实时捕获，以实现数据迁移、实时订阅、数湖转存、数仓回流、单元化多活、备份恢复等能力。</p>
</blockquote>
<blockquote>
<p>对于目前使用类HBase+ElasticSearch或HBase+OpenTSDB+ES的应用场景，比如监控、社交、广告等，利用Lindorm的原生多模能力，将很好地解决架构复杂、查询痛苦、一致性弱、成本高、功能不对齐等痛点，让业务创新更高效。</p>
</blockquote>
<p>官网的介绍比较晦涩，我用人话翻译一下：Lindorm团队最初都是做阿里内部HBase的，他们基于HBase做了一系列优化，解决了HBase的一系列问题，并以此为基点，慢慢研发出自己的多模引擎，试图一统存储分析技术，凭一己之力，实现MySQL、HBase、时序数据库等等的完整功能。Lindorm支持类SQL和类HBase两种访问方式，分别对标MySQL和HBase，作为其的升级替代品。</p>
<p>Lindorm号称云原生，但笔者看来它并不是真正的云原生，我们最初使用Lindorm的时候还是在云下场景，当时Lindorm也没有云原生数据库的提法。</p>
<h3 data-id="heading-10">4.2 Lindorm与MySQL对比</h3>
<p>过去 10 年，随着互联网技术的快速发展，数据库呈现井喷式发展，出现了各式各样的产品，如文件存储数据库、列存储数据库、NewSQL 数据库。之所以如此，归结于数据量不断快速膨胀，传统数据库在大数据上的处理性能不能满足需求等。企业和开发者趋于去针对不同应用类型开发不同的数据库，来满足对特定数据处理的需求。</p>
<p>Lindorm相比于MySQL，第一个优点，我称之为存储伸缩性。MySQL的数据表，容量是有界的，而号称支持单表百万亿行规模、千万级并发、百PB级数据存储的Lindorm，你基本上可以认为它的数据是无界的，其存储伸缩性轻易地支持数据表的水平扩展。</p>
<p>Lindorm相比于MySQL，第二个优点，是可以免除分库分表的困扰。还记不记得MySQL我们怎么去应对海量数据？我们会去做分库分表，我们会对业务做垂直分表，从而不能使用数据宽表的便利；更复杂的，我们还需要去做水平分表，按照特定的分片算法去对同一张数据表做横向切分。数据库领域很多高深晦涩的问题，都是分库分表引入的，比如分布式事务问题、横向扩容问题、跨库join问题、跨表结果集合并问题、历史库清理问题等。</p>
<p>所以，如果告诉你，用了Lindorm之后，你不用去处理大部分的数据库层面的分布式事务问题，也不用担心横向扩容问题，而且可以像处理单表一样用简单的方式实现跨分表键的查询、排序、count、group，你是否也会对Lindorm有些心动呢？</p>
<h3 data-id="heading-11">4.3 Lindorm与HBase对比</h3>
<p>HBase的优点：读写性能优秀，支持批量导入，无需分库分表，存储计算分离，成本低，弹性好。</p>
<p>随着时代的发展HBase的缺点也体现出来了：</p>
<ul>
<li>Row Key设计复杂，无数据类型缺乏约束。只能基于主键查询，不能很好支持复杂业务场景</li>
<li>读写毛刺影响业务使用体感</li>
<li>客户端逻辑过重，CPU承载高，客户端需要直连ZK，Meta表获取路由信息，出现BUG难以排查</li>
<li>主备集群切换无法保证一致性，备集群只接受复制流量，资源严重浪费</li>
</ul>
<p>HBase的这些缺点，导致了我们很少在真正的线上服务中使用HBase，即使它有着听上去天花乱坠的强大性能。而HBase的升级版本Lindorm破解了这一切。两者的性能对比见Lindorm官网。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F181750.html%3Fspm%3Da2c4g.11186623.6.546.35bb4ccaPnpgwj" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/181750.html?spm=a2c4g.11186623.6.546.35bb4ccaPnpgwj" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddbd6c540c0e4a00a0cd6b8852e8da19~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单来说，Lindorm主要解决了HBase的读写毛刺和无二级索引的问题。</p>
<h3 data-id="heading-12">4.4 Lindorm实战的一些坑</h3>
<h4 data-id="heading-13">4.4.1 Lindorm 二级索引</h4>
<p>Lindorm真正强大的地方，在于他支持海量数据之后，居然还能支持二级索引，这恰恰是HBase所不能做到的事情。只支持Row Key维度查询的HBase，只能通过讨巧的Row Key设计来部分模拟二级索引的功能。</p>
<p>但Lindorm二级索引也恰恰是它坑的地方，因为，它每创建一个二级索引就是重新copy一份数据，所以Lindorm的运维和开发同学会建议你慎用二级索引。</p>
<h4 data-id="heading-14">4.4.2 Lindorm 超大分页</h4>
<p>Lindorm的一大优势就是可以在海量数据场景依然可以免除分库分表的困扰，所以自然而然地，我们会使用跨分表键的大数量查询（举个栗子：使用分库分表数据库，你很难用在线服务去做随机抽奖和跨用户的统计，只能离线跑数据，但是用Lindorm可以），但是Lindorm并不能支持像Hive的API那种任意分页查询，因为它在大数据量下也会遭遇大分页问题。</p>
<p>“10万行中的第5万行到第5万零20行”，需要先去获取前5万行，接下来才能获取到你需要的20行数据，所以这个过程是极为低效的。这是因为Lindorm的 <em>select * from tableName limit i,n</em> 底层的实现类似于HBase的scan，先按Row Key去scan到全量数据，然后再返回所需要的数据。</p>
<p>实际应用中，大约分页的offset在3万左右的时候，请求RT就已经超过3s超时（标准型存储，2019年性能数据），所以，不要简简单单地把Lindorm当做类似于Hive一样的数据宽表使用，还是老老实实地使用应对大分页问题的系列最佳实践。</p>
<h4 data-id="heading-15">4.4.3 Lindorm region划分</h4>
<p>同HBase一样，Lindorm针对数据量扩充会优雅地做region的切分，但这个切分也不是毫无槽点，如果某些区段的Row Key数据量或者请求比较集中，Lindorm也会遇到数据倾斜和热点region问题。但好在，对于region的切分可以人工介入，对Row Key按照更合理的方式进行rehash。</p>
<h3 data-id="heading-16">4.5 Lindorm相关QA</h3>
<p><strong>Q</strong>：HBase的读写毛刺是怎么产生的，Lindorm如何解决HBase的读写毛刺?</p>
<p><strong>A</strong>：HBase底层是Java写的，毛刺的一大来源是JVM GC。Lindorm针对这个问题，一方面从HBase源码级别进行了优化，大幅度减少了系统运行时对象的创建，从而降低了GC的压力；另一方面也是和阿里内部jvm团队合作，使用了更加适合Lindorm的GC算法。Lindorm团队是阿里内部最早使用ZGC的两个团队之一，至少在2019年，ZGC还在实验阶段的时候，Lindorm就已经全量使用上ZGC了。</p>
<p><strong>Q</strong>：Lindorm有ACID特性吗?</p>
<p><strong>A</strong>：Lindorm对于单行跟MySQL对ACID的支持是等同的，但跨行是不支持事务的。</p>
<h3 data-id="heading-17">4.6 Lindorm总结</h3>
<p>Lindorm可以作为HBase的完美上位替代，所有之前使用HBase的场景都可以迁移到Lindorm上来。但是相较于MySQL，并不建议直接迁移到Lindorm，但如果满足以下条件，可以考虑使用Lindorm：</p>
<ul>
<li>真正的海量数据，10亿+，且增长量无法预估</li>
<li>不做范围查询，或者仅在主键索引、二级索引上使用范围查询 （类比HBase的scan）</li>
<li>不需要多行事务</li>
</ul>
<p>笔者本不建议交易订单、金融类业务使用Lindorm，但从官网看，Lindorm都有相关的应用案例。Lindorm的性能型存储访问延迟低至0.2ms~0.5ms（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F181971.html%25EF%25BC%2589%25EF%25BC%258C%25E6%2580%25A7%25E8%2583%25BD%25E4%25B8%258A%25E6%25AF%2594MySQL%25E4%25B9%259F%25E4%25B8%259D%25E6%25AF%25AB%25E4%25B8%258D%25E5%25BC%25B1%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/181971.html%EF%BC%89%EF%BC%8C%E6%80%A7%E8%83%BD%E4%B8%8A%E6%AF%94MySQL%E4%B9%9F%E4%B8%9D%E6%AF%AB%E4%B8%8D%E5%BC%B1%E3%80%82" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a></p>
<h2 data-id="heading-18">五、流批一体——大数据计算引擎Fink介绍</h2>
<h3 data-id="heading-19">5.1 Flink介绍</h3>
<p>在国外一些社区，有很多人将大数据的计算引擎分成了 4 代。</p>
<p>第一代计算引擎，无疑是Hadoop MapReduce。它将计算分为两个阶段，分别为 Map 和 Reduce。上层应用需要自己手写map任务和reduce任务。</p>
<p>第二代计算引擎，支持 DAG（有向无环图） 的框架： Tez ，主要还是批处理任务</p>
<p>第三代计算引擎，以 Spark 为代表，特点主要是 Job 内部的 DAG 支持（不跨越 Job），以及强调的实时计算。</p>
<p>第四代计算引擎，以Flink、Blink为代表，一统批流，支持DAG运算，并具备进一步的实时性。</p>
<p>自 Google Dataflow 模型被提出以来，流批一体就成为分布式计算引擎最为主流的发展趋势。流批一体意味着计算引擎同时具备流计算的低延迟和批计算的高吞吐高稳定性，提供统一编程接口开发两种场景的应用并保证它们的底层执行逻辑是一致的。对用户来说流批一体很大程度上减少了开发维护的成本，但同时这对计算引擎来说是一个很大的挑战。虽然 Spark 是最早提出流批一体理念的计算引擎之一，但由于其本质还是基于批（mini-batch）来实现流，在流计算语义和延迟上存在硬伤，难以满足复杂、大规模实时计算场景的极致需求。</p>
<p>Flink 遵循 Dataflow 模型的理念: 批处理是流处理的特例。不过出于批处理场景的执行效率、资源需求和复杂度各方面的考虑，在 Flink 设计之初流处理应用和批处理应用尽管底层都是流处理，但在编程 API 上是分开的。这允许 Flink 在执行层面仍沿用批处理的优化技术，并简化掉架构移除掉不需要的 watermark、checkpoint 等特性。</p>
<h3 data-id="heading-20">5.2 Blink介绍</h3>
<p>Blink是阿里巴巴内部研发的Flink版本，2015 年，针对搜索推荐业务做新的大数据计算引擎选型时，阿里云实时计算团队对流批一体的技术方向就已经有初步设想。在经过深度调研、可行性验证和对未来可能遇到的问题进行推演之后，团队最终决定引入 Flink。虽然当时 Flink 整个系统还不是特别成熟，但团队认为 Flink 以流计算为核心的设计理念更符合未来数据计算实时化发展的大趋势。在阿里内部有一句土话，叫“路走对了，就不怕远”，从后续这几年的发展情况来看，Flink 确实进展顺利，甚至超过团队当时的预期。</p>
<p>在很长一段时间内，Blink的功能和性能都是远超社区版的Flink的。阿里 2019 年收购 Flink 的创始公司 Ververica 后，投入近百名工程师到 Flink 技术研发和社区工作中，Blink 在 Table/SQL 上做了大量的优化，为了合并 Blink 的先进特性到 Flink，阿里的工程师推进社区重构了 Table 模块的架构并将 Table/SQL API 提升为主要编程 API。</p>
<p>Blink 流批一体成功落地双 11 天猫核心数据场景，在2020年双十一，面对 58.3 万笔 / 秒的交易峰值和上亿 / 秒的无线流量洪峰，天猫的所有任务都达到了秒级延时，整个实时计算集群峰值 TPS 达到 40 亿条 / 秒。同时，集群资源利用率也得到了大幅提升，批任务可以错峰执行。</p>
<h3 data-id="heading-21">5.3 Flink与Blink对比</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8be633e56c7340e7905d3904990393ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>(图片来源：阿里云Blink官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument%255C_detail%2F110778.html%3Fspm%3Da2c4g.11186623.6.545.7dfb5da7jiRXUe" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document%5C_detail/110778.html?spm=a2c4g.11186623.6.545.7dfb5da7jiRXUe" ref="nofollow noopener noreferrer">help.aliyun.com/document\_d…</a>)</p>
<h3 data-id="heading-22">5.4 Flink使用</h3>
<h4 data-id="heading-23">5.4.1 创建数据源表</h4>
<p>Flink的数据源表能同时支持流式数据存储和离线数据存储，甚至两者可以在同一个Flink任务中作为数据源。流式数据包括kafka、阿里云SLS日志、数据总线DataHub、RocketMQ/MetaQ等数十种类型。离线数据包括Hive、odps等等。</p>
<pre><code class="copyable">CREATE TABLE dwd_tb_trd_pay_ri(
        biz_order_id    VARCHAR, -- '订单ID' 
        auction_id      VARCHAR, -- '商品ID'
        auction_title   VARCHAR, -- '商品标题' 
        buyer_id        VARCHAR, -- '买家ID'
        buyer_nick      VARCHAR, -- '买家昵称'
        pay_time        VARCHAR, -- '支付时间'
        gmt_create      VARCHAR, -- '创建时间'
        gmt_modified    VARCHAR, -- '修改时间'
        biz_type        VARCHAR, -- '交易类型'
        pay_status      VARCHAR, -- '支付状态' 
        `attributes`    VARCHAR, -- '订单标记'
        from_group      VARCHAR, -- '订单来源'
        div_idx_actual_total_fee   DOUBLE  --'成交金额'        
) WITH (
    type='datahub',
    endPoint='http://dh-cn-hangzhou.aliyun-inc.com',
    project='yourProjectName',-- '您的project'
    topic='yourTopicName',--'您的topic'
    roleArn='yourRoleArn',-- '您的roleArn'
    batchReadSize='500'
);   
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">5.4.2 创建数据结果表</h4>
<p>Flink的运算结果可以存储到数十种存储引擎中，包括消息队列（比如kafka、RocketMQ/MetaQ、DataHub）、数据库（比如MySQL、Oracle）、NOSQL存储（Redis、HBase、Lindorm）、日志服务（SLS）等。</p>
<pre><code class="copyable">CREATE TABLE tddl_output(
    gmt_create   VARCHAR, --'创建时间'
    gmt_modified VARCHAR, --'修改时间'
    buyer_id     BIGINT, --'买家ID'
    cumulate_amount BIGINT, --'金额'
    effect_time BIGINT, --'支付时间'
    primary key(buyer_id,effect_time)
) WITH ( 
        type= 'rds', 
        url = 'yourDatabaseURL',  --'您的数据库url' 
        tableName = 'yourTableName', --'您的表名 '
        userName = 'yourUserName',  --'您的用户名' 
        password = 'yourDatabasePassword' --'您的密码' 
    );  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">5.4.3 编写业务逻辑</h4>
<p>采用类SQL语言编写业务逻辑，还能使用各类内置函数、窗口函数，并可自定义函数（UDF、UDAF、UDTF）。</p>
<pre><code class="copyable">INSERT INTO tddl_output
SELECT
    gmt_create,
    gmt_modified,
    buyer_id,
    div_idx_actual_total_fee
from dwd_tb_trd_pay_ri
where div_idx_actual_total_fee >0;   
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">5.4.4 性能调优</h4>
<p>实时计算作业开发过程中，完成了业务逻辑实现、作业上线和启动运行后，为了满足实时计算作业的性能需求，还需对作业进行调优。</p>
<p>作业调优主要做SQL优化和参数调优。Blink开发了自动配置调优的功能，一定程度降低了参数调优的门槛，但效果一般低于人工调优。性能调优的好坏对性能和吞吐作用极大，笔者曾经通过性能调优在相同资源消耗下将作业吞吐量提升4倍。</p>
<h3 data-id="heading-27">5.5 Flink优点</h3>
<ul>
<li>极低的学习成本，在有经验的同学的指导下，可以在一天以内完成语法的熟悉和demo的编写。</li>
<li>流批一体，只需学习使用一套 SQL 就可以基于 Flink 进行流批一体的开发，降低了开发的门槛。</li>
</ul>
<h2 data-id="heading-28">六 、大数据在字节跳动</h2>
<p>字节跳动虽然没有在大数据领域贡献多个开源框架，但就笔者的使用体验来说，字节的大数据技术实力还是非常强的，内部工程师自研了诸多数据平台和数据库产品，支撑着抖音、TikTok、今日头条等多个爆款APP的飞速发展。</p>
<h3 data-id="heading-29">6.1 数据平台</h3>
<p>字节跳动数据平台，横向支持公司的所有业务线，包括今日头条、抖音、西瓜、教育等，并可扩展至外部公司，解决EB级别大数据问题。字节跳动数据平台有多个数据产品，包括风神、Dorado、Libra等。</p>
<p>风神是数据平台自研的敏捷BI平台，提供了灵活易用的查询分析服务、报表制作能力。 风神的数据内容来源于各业务线，中台部门。 丰富多元的内容和灵活强大的平台能力，为业务快速发展，提供了不可或缺的数据支持。</p>
<p>Dorado是集数据集成、数据开发、任务调度、运维管理等功能为一体的大数据研发平台，提供一站式大数据开发解决方案，帮助业务部门简单高效构建自己的数据中心，专注于数据价值的挖掘和探索。通过Dorado，你可以对离线数据和流式数据写各类调度任务，比如离线数据同步、存储转换，也可以做数据开发，编写Hive、Spark、Flink任务。</p>
<p>Libra是提供大规模在线实验和统计评估能力的A/B测试平台。覆盖推荐、广告、搜索、UI、产品功能等实验场景，支撑业务在快速迭代的试错之路上，大胆假设、小心求证。</p>
<p>风神等数据平台，底层都是ClickHouse。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fclickhouse.yandex%2Fdocs%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://clickhouse.yandex/docs/zh/" ref="nofollow noopener noreferrer">ClickHouse</a> 开源版是一个用于联机分析（Online Analytical Processing：OLAP）的列式数据库管理系统，支持用户从多个角度交互地分析多维数据。OLAP-ClickHouse 是字节跳动研发同学基于开源 ClickHouse 进行了深度优化的版本，提供海量数据上更强的查询服务和数据写入性能，应用包括海量数据多维分析、机器学习模型评估、微服务监控和统计等。</p>
<h3 data-id="heading-30">6.2 存储系统</h3>
<p>字节跳动自研了多个存储系统，涉及SQL、NoSQL、NewSQL等多种数据库类型，包括ByteKv、ByteSQL、ByteGraph等多种数据库产品。</p>
<p>ByteKv是字节跳动自研的一个分布式的、支持分布式事务的强一致性的面向在线场景的KV数据库系统。适用于数据量大（TB~几十PB）、需要强一致、事务、顺序扫描的场景。比如钱、币、元数据、订单、商品、内容等。</p>
<p>ByteSQL是字节跳动基础架构基于分布式KV服务 ByteKV 研发的一款支持高并发的高性能分布式表格存储服务，面向强一致的在线事务处理（OLTP）需求。适用于单表巨大（TB~几十PB）、强一致、事务、全局二级索引的场景。</p>
<p>ByteGraph是字节跳动自研的分布式图数据存储系统，支持有向属性图数据模型，支持Gremlin图数据库语言，读写吞吐可扩展到千万QPS，延迟毫秒级。目前，ByteGraph已经部署了200+集群，遍布全球机房，支持了今日头条、抖音、TikTok、西瓜、火山、风控、知识图谱等几乎公司全部产品线，广泛应用于社交、PUGC、推荐、风控等业务场景。</p>
<p>以上只是字节跳动自研的数据库产品的一小部分，很多产品还未对外宣传，因此在此不多做说明。</p>
<h2 data-id="heading-31">七、结语</h2>
<p>本文对近五年来大数据技术栈的变迁做了粗浅的论述，并加入了个人工作实战过程中的所见所闻，限于个人认知和篇幅，也许只展现了大数据技术魅力的万分之一。数据、算法、算力的发展，极大地丰富了我们的生活，也推动着经济社会的飞速发展，作为这个大数据时代的亲历者我深感荣幸，希望更多的开发者们加入进来，一起推动人工智能技术奇点的早日到来，共同见证这前所未有的科技革命。</p>
<h2 data-id="heading-32">参考文献</h2>
<ol>
<li>流式计算的三种框架 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fjiangjunshow%2Farticle%2Fdetails%2F100798240" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/jiangjunshow/article/details/100798240" ref="nofollow noopener noreferrer">blog.csdn.net/jiangjunsho…</a></li>
<li>四种数据处理方式比较：传统 ETL 工具、MapReduce、Hive、Spark <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sohu.com%2Fa%2F230352341%255C_151779%25C2%25A0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sohu.com/a/230352341%5C_151779%C2%A0" ref="nofollow noopener noreferrer">www.sohu.com/a/230352341…</a></li>
</ol>
<p>**作者：**王伟强</p></div>  
</div>
            