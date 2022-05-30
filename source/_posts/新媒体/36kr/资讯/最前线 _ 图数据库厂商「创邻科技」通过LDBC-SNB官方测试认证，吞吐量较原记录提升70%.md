
---
title: '最前线 _ 图数据库厂商「创邻科技」通过LDBC-SNB官方测试认证，吞吐量较原记录提升70%'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220530/v2_5cc7c8e8ba404a40a2bf6a75b31aeb3a_img_png'
author: 36kr
comments: false
date: Mon, 30 May 2022 06:59:18 GMT
thumbnail: 'https://img.36krcdn.com/20220530/v2_5cc7c8e8ba404a40a2bf6a75b31aeb3a_img_png'
---

<div>   
<p>作者｜程一城</p> 
<p>编辑｜王与桐</p> 
<p><br>Gartner发布的《2021年十大数据和分析技术趋势报告》中指出，数据和分析活动将转变为组织的一项核心业务功能，图技术在数据和分析创新中的占比将会在2025年达到80%。图数据库技术是使用图数据结构进行存储并实现语义查询的非关系型数据管理系统，在金融、零售、软件、医疗、供应链、航空、电信等行业已有广泛应用。作为数据分析的一项基础技术，图数据库在近年来也在加快影响业务的决策速度。而随着腾讯、阿里、字节等互联网巨头的入局，国内的图数据库应用也逐渐成为蓝海市场。</p> 
<p><a class="project-link" data-id="1678309340738565" data-name="创邻科技" data-logo="https://img.36krcdn.com/20220329/v2_dbdeed1720f94457b0d3bf5086cb295b_img_png" data-refer-type="1" href="https://36kr.com/project/1678309340738565" target="_blank">创邻科技</a>是<a target="_blank" rel="noopener noreferrer" href="https://36kr.com/p/1514429954201608">36氪曾报道过的一家企业</a>。该公司自成立以来一直聚焦高性能性能图数据库技术，原生分布式并行图平台产品Galaxybase复杂关联查询性能较现存同类技术有百倍提升，核心代码100%自研、安全自主可控，目前已在金融、能源、互联网、公安等多个行业应用落地。据了解，今年年初，创邻科技已联合中山大学团队，依托国家超级计算广州中心环境，完成了Galaxybase的安装部署，并实现5万亿点边规模交易数据智能挖掘性能测试，打破了美国头部技术厂商与21年创造的图处理世界记录。 </p> 
<p>近日，创邻科技宣布其全自主研发的高性能图数据库Galaxybase已通过国际关联数据基准委员会（Linked Data Benchmark Council，LDBC）的LDBC-SNB（Linked Data Benchmark Council-Social Network Benchmark）的测试认证，在系统稳定性、可用性、结果正确性、事务支持性和可恢复性上均达到官方标准，并较LDBC之前公布的最高记录吞吐量提升了70%，查询性能最高提升72倍，平均查询性能提升超6倍。</p> 
<p class="image-wrapper"><img data-img-size-val="866,618" src="https://img.36krcdn.com/20220530/v2_5cc7c8e8ba404a40a2bf6a75b31aeb3a_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">（审计测试成功的声明页截图）</p> 
<p>此次的测试由LDBC-SNB指定的第三方评估师在其租用的标准云系统上执行完成，测试环境准备、测试数据生成和导入、测试例程序的安装和执行、结果正确性的验证方面均严格遵守LDBC-SNB规范。</p> 
<p>读者可以通过访问以下网址查看正式公布的测试结果，并下载测试报告、程序、说明文档以及软硬件信息：https://ldbcouncil.org/benchmarks/snb/</p> 
<h3><strong>关于LDBC和SNB测试</strong></h3> 
<p>LDBC（Linked Data Benchmark Council，国际关联数据基准委员会）是图数据库领域权威的基准指南制定者与测试标准发布机构，汇聚了包括Oracle，Intel等软硬件巨头和全球图数据库领域的专家学者，旨在制定一套公平、诚信、可对比的方法和机制来衡量图数据库管理系统，共同推进这项前沿技术的发展。</p> 
<p>SNB（Social Network Benchmark，社交网络基准测试）是由关联数据基准委员会（LDBC）开发的面向图数据库的基准测试（Benchmark）之一，分为交互式查询（Interactive）和商业智能（BI）两个场景。SNB提供了一套模拟真实社交网络场景的测试，衡量图数据在交互式查询和商业智能查询中的性能表现。与基于单项测试的评测方法相比，LDBC-SNB不仅更接近真实的业务查询场景，同时对图数据库系统的并发执行能力和事务处理能力提出了更高的要求。</p> 
<h3><strong>关于测试详情</strong></h3> 
<p>据创邻科技创始人&CEO张晨博士介绍，此次创邻科技采用LDBC-SNB提供的交互式（Interactive）查询任务，就结果正确性、事务、系统可恢复性、以及测试超时情况、吞吐量、响应时间等性能指标进行验证和测试。结果显示，Galaxybase通过正确性测试，所测结果与LDBC提供的第三方图数据库测试结果相同；LDBC审计表示，Galaxybase测试结果达到<strong>序列化</strong>级别，事务验证超过标准；同时，Galaxybase通过可恢复性验证，在基准测试执行2小时的时候关机重启，LDBC日志中最后插入成功的测试项数据仍然完整保存在图数据库中。</p> 
<p>性能测试中，Galaxybase采用48个客户端并行请求的方式，超越了LDBC要求的5%以内超时，实现了<strong>零超时</strong>。在超时数量符合条件并满足30分钟预热和2小时测试的前提下，Galaxybase在30 G（8千万点，5亿边）、100 G（3亿点，18亿边）、300 G（8亿点，53亿边）三个数据集的吞吐量均打破了LDBC已经公布的最高记录（由TuGraph保持），性能提升了<strong>70%</strong>，查询性能平均快超6倍。同时，在请求发送频率更高的情况下，Galaxybase的平均响应时间、50分位、90分位、95分位、99分位的响应时间亦均快于前记录保持者。其中,平均响应时间最快超过原纪录41倍，90分位响应时间最快超过原纪录72倍。不管是在<strong>同一测试项下不同数据量</strong>的查询上，还是在<strong>不同测试项不同复杂度</strong>的查询上，Galayxbase均展现了更佳性能，且这种优势随着数据集规模的增加而增加，充分体现了Galaxybase在大规模数据处理上的优秀支撑能力。</p> 
<p>下表为Galaxybase在不同数据级下的测试结果，吞吐率（OPS）表示每秒完成的操作次数：</p> 
<p class="image-wrapper"><img data-img-size-val="1538,418" src="https://img.36krcdn.com/20220530/v2_7a016ce546ec4ad08d170b696f1ed4da_img_png" referrerpolicy="no-referrer"></p> 
<p class="img-desc">（SF-30、SF-100、SF-300对应原始数据集大小分别为30 G、100 G、300 G）</p> 
<p>创邻科技CTO周研表示，Galaxybase可以同时支持联机事务处理（OLTP）和联机分析处理（OLAP），对比其他图数据库产品，响应时间更短、吞吐量更大、支持分布式水平扩展，能够更好满足企业在对关联数据进行分析中越来越高的实时性需求，是一款面向大规模数据的国产高性能图数据库。</p> 
<p>Galaxybase图数据库由Java语言和C++语言混编而成，充分利用了C++语言的运行性能和内存控制优势，以及Java语言在复杂可靠系统开发中的编码效率和故障排查优势。在存储设计上，Galaxybase使用完全自主研发的原生图数据存储结构，针对图数据的免索引邻接进行了专项优化，使得点边查询能够以极高效的方式完成。核心存储引擎不依赖任何第三方开源组件，确保自主可控的同时也能够让图查询和图计算更好地和底层存储层进行协同优化。在查询执行层，Galaxybase通过自研的内存分配和管理机制，更加紧凑地编排内存数据，并通过使用堆外内存大大降低了JVM的GC时间。在并行控制上，Galaxybase提供了并行迭代的图遍历方式，使用了多版本控制的方式来减少锁竞争，并且在邻居迭代时可以根据邻居的数量自适应分配并行迭代的线程数，实现系统资源的最佳利用。Galaxybase提供了丰富的开发和查询接口，全面支持描述式的OpenCypher查询语言，可以使用OpenCypher编写完成LDBC-SNB基准测试的全部测试案例。</p> 
<p>本次审计测试中，Galaxybase通过OpenCypher完成了图数据库的耐用性测试。Galaxybase同时提供了包括Java、Python、Golang等在内的多种编程语言接口，可以通过各自的驱动包来连接图数据库进行开发。在一些对系统资源占用和执行性能要求很高的场景中，Galaxybase还提供了PAR（Parameterized Algorithm Routine）API接口，允许用户通过Java代码实现在服务端运行的自定义过程和函数，以获得对查询执行过程更好的控制，追求极致的性能。用户在实际使用中，可以根据不同的场景和需求，权衡易用性、开发人力、系统资源、性能要求等多方面因素，选择最合适的方案。</p> 
<p>据了解，创邻科技创始人&CEO张晨博士将于6月17日北京时间23:00pm（美国东部夏令时11：00 am）, 于ACM SIGMOD 2022 数据管理国际会议发表New LDBC SNB benchmark record by Galaxybase: more than 6 times faster and 70% higher throughput主题演讲，公开披露测试细节。</p> 
<p>读者可届时前往以下网址观看演讲：https://ldbcouncil.org/event/fifteenth-tuc-meeting/</p>  
</div>
            