
---
title: '全票通过！数据集成平台 SeaTunnel 成功进入 Apache 孵化器！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f26f80d35442a2e21810d5144dce964028e.png'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 20:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f26f80d35442a2e21810d5144dce964028e.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="text-align:left"><span style="color:#000000">美国时间 2021 年 12 月 9 日，</span><span style="color:#3498db"><strong style="color:#000000">SeaTunnel(原名Waterdrop) 正式通过 </strong><strong style="color:#000000">Apache 软件基金会</strong><strong style="color:#000000">的投票决议，以全票通过的优秀表现正式成为 Apache 孵化器项目</strong><strong style="color:#000000">。</strong></span></p> 
 <div> 
  <p style="text-align:left"><span style="color:#404040">根据 Apache 基金会</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.apache.org%2Fthread%2F70yywsx4r8y5o91twnp13s671q8j4dng" target="_blank"><u>邮件列表</u></a><span style="color:#404040">显示，在包含 14 个约束性投票 (binding votes) 和 9 个无约束性投票(non-binding votes) 的投票，评委全部持赞同意见，无弃权票和反对票。这也是 Apache 基金会中诞生的第一个来自中国的数据集成平台项目。</span></p> 
  <h2><span style="color:#3498db"><strong style="color:#000000">SeaTunnel 的前世今生</strong></span></h2> 
  <p style="text-align:left"><span style="color:#34495e">SeaTunnel 是一个非常易用、高性能、支持实时流式和离线批处理的海量数据集成平台，架构于 Apache Spark 和 Apache Flink 之上，支持海量数据的实时同步与转换。</span></p> 
  <p style="text-align:left"><span style="color:#000000">SeaTunnel 原名 </span><span style="color:#34495e">Waterdrop，于 2017 年由乐视创建，并于同年在 GitHub 上开源，2021 年 10 月改名为 SeaTunnel。</span></p> 
  <p style="text-align:left"><span style="color:#34495e">之所以要研发 SeaTunnel ，主要是因为当时市面上没有很好的、简单易用的、支持每天数百亿条数据同步的开源软件，SeaTunnel 的使命就是要将海量数据同步的能力传播到全世界，同时大大降低用户利用 Spark、Flink 等技术做数据集成的门槛。</span></p> 
  <p style="text-align:left"><span style="color:#000000">从技术维度来谈，SeaTunnel 的目标可以归纳为：</span></p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">使用 Spark、Flink 作为底层数据同步引擎使其具备分布式执行能力，提高数据同步的吞吐性能；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#333333">集成多种能力缩减 Spark、Flink 应用到生产环境的周期与复杂度；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#333333">利用可插拔的插件体系支持超过 100 种数据源；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#333333">引入管理与调度能力做到自动化的数据同步任务管理；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#333333">特定场景做端到端的优化提升数据同步的数据一致性；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#333333">开放插件化与 API 集成能力帮助企业实现快速定制与集成；</span></p> </li> 
  </ul> 
  <h2><strong style="color:#000000">SeaTunnel 系统架构、工作流程与特性</strong></h2> 
  <p style="text-align:left"><span style="color:#000000">在团队的努力下，SeaTunnel 的系统架构逐渐成型，2017 年对外开源后，SeaTunnel 很快获得了开发人员的认可。迄今为止，SeaTunnel 已经发布了 31 个版本 （目前推荐使用 1.5.6），在 </span><span style="color:#202124">Bilibili、</span><span style="color:#000000">新浪、水滴筹、搜狗、趣头条、唯品会等公司的生产实践中发挥着关键作用。</span></p> 
  <p style="text-align:left"><span style="color:#333333">Input/Source[数据源输入] -> Filter/Transform[数据处理] -> Output/Sink[结果输出]</span></p> 
  <p style="text-align:center"><img alt height="705" src="https://oscimg.oschina.net/oscnet/up-f26f80d35442a2e21810d5144dce964028e.png" width="600" referrerpolicy="no-referrer"></p> 
  <p style="text-align:center"><span style="color:#000000">SeaTunnel 工作流程图</span></p> 
  <p style="text-align:left"><span style="color:#000000">上图为 SeaTunnel 的整个工作流程，数据处理流水线由多个过滤器构成，以满足多种数据处理需求。如果用户习惯了 SQL，也可以直接使用 SQL 构建数据处理管道，更加简单高效。目前，SeaTunnel 支持的过滤器列表也在扩展中。</span></p> 
  <p style="text-align:left"><span style="color:#000000">在插件方面，SeaTunnel 已支持 </span><span style="color:#003366">File、Hive/Hdfs、Kafka、Jdbc、ClickHouse、TiDB、HBase、Kudu 等 20 多种插件，同时也支持添加、校验、转换、日期、SQL等处理插件，整体上基于系统非常易于拓展，</span><span style="color:#000000">用户还可以自行开发数据处理插件。</span></p> 
  <p style="text-align:left"><span style="color:#000000">在这样的易拓展架构设计下，SeaTunnel 具有以下核心特性：</span></p> 
  <ul style="list-style-type:square"> 
   <li> <p style="text-align:left"><span style="color:#000000">组件丰富：内置丰富插件，</span><span style="color:#000000">支持各种数据产品的传输和集成；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#000000">高扩展性：模块化和插件化，支持热插拔, 带来更好的扩展性；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#000000">简单易用：特有的架构设计下，使得开发配置简单，无使用成本；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#000000">成熟稳定：经历大规模生产环境使用和海量数据的检验；</span></p> </li> 
   <li> <p style="text-align:left"><span style="color:#000000">支持通过 SQL 进行数据处理和聚合；</span></p> </li> 
  </ul> 
  <h2><strong style="color:#000000"> 使用场景</strong></h2> 
  <p style="text-align:left"><span style="color:#000000">SeaTunnel 的使用场景包括</span><span style="color:#000000">海量数据集成、数据 ETL、数据聚合以及多源数据处理等。</span><span style="color:#000000">如今，SeaTunnel 已应用于数十家企业生产环境，日均可稳定高效地同步数百亿条数据。</span></p> 
  <p style="text-align:left"><span style="color:#000000">比如， SeaTunnel 解决了唯品会数据仓库入仓出仓、人群计算等场景中的难题；作为 B 站数据平台离线出入仓核心工具，SeaTunnel 在 B 站每天完成千亿级记录、百T级数据的出入仓，解决了我们电商、直播、创作中心等场景核心任务出入仓难题；微博一直播内部使用 SeaTunnel 的魔改定制源码搭建了实时的直播数仓入仓工具；趣头条数据中心使用 SeaTunnel 作为Hive 到 Clickhouse 的离线同步工具；永辉云创科技旗下的新零售品牌永辉生活使用 SeaTunnel 进行电子商务用户行为数据的实时流式和离线 SQL 计算。</span></p> 
  <p style="text-align:left"><strong style="color:#000000">“Welcome to Apache incubator，SeaTunnel！”</strong></p> 
  <p style="text-align:left"><img alt height="507" src="https://oscimg.oschina.net/oscnet/up-aa57b7762ae847fb9424e1508bdf162d42c.png" width="600" referrerpolicy="no-referrer"></p> 
  <p style="text-align:left"><span style="color:#191919">从 2017 年创立，到如今进入 Apache 孵化器，SeaTunnel 正在进入一个全新的发展阶段。</span><span style="color:#191919">SeaTunnel 一进入孵化器就得到众多开源社区大咖们的祝福，包括 Apache</span><span style="color:#191919"> </span><span style="color:#191919">基金会董事吴晟、Apache</span><span style="color:#191919"> </span><span style="color:#191919">基金会成员 JiangNing, Ted Liu, GuoWei、腾讯开源联盟主席单致豪，PingCAP 联合创始人& CTO 黄东旭、涛思数据 TDengine 创始人陶建辉、SphereEx 联合创始人 & CTO 潘娟、Apache HAWQ PMC 主席常雷、Apache Hudi PMC 李少峰、DataStax（Apache Cassandra 社区）中国总经理卢东明、Apache Doris PPMC 陈明雨、Apache RocketMQ PMC 杜恒， Elastic 中文社区创始人曾勇、巨杉数据库技术生态资深总监萧少聪等诸多开源数据生态大咖的联名祝贺。</span></p> 
  <p style="text-align:left"><span style="color:#191919">其实 SeaTunnel 在孵化器讨论阶段就</span><span style="color:#191919">曾</span><span style="color:#191919">引起全球 Apache 孵化器导师的</span><span style="color:#191919">关注</span><span style="color:#191919">，</span><span style="color:#191919">“</span><span style="color:#191919">导师</span><span style="color:#191919">”报名数量</span><span style="color:#191919">远超过普通孵化项目，以至于 Apache 孵化器负责人 Justin 邮件提醒</span><span style="color:#191919">“</span><span style="color:#191919">导师不能过多</span><span style="color:#191919">”。也有</span><span style="color:#191919">导师在全球 Apache 孵化器讨论邮件列表里</span><span style="color:#191919">表示</span><span style="color:#191919">遗憾</span><span style="color:#191919"> —— </span><span style="color:#191919">Apache 孵化器项目 “旱的旱死，涝的涝死”，形容有的项目还要四处寻求导师才可以进入孵化器，有的项目</span><span style="color:#191919">则需要</span><span style="color:#191919">大家争抢导师职位，而 SeaTunnel 无疑是后者。</span></p> 
  <p style="text-align:left"><span style="color:#191919">SeaTunnel </span><span style="color:#191919">社区</span><span style="color:#191919"> PPMC 们</span><span style="color:#191919">表示：</span><span style="color:#191919">“</span><span style="color:#191919">始终以开放的心态，致力于让全球所有优秀的数据存储和计算引擎高效、准确、快速地进行跨数据源的同步、转化数据，让人们在多数据源场景下，可以快速、简单的完成自己的目标。</span><span style="color:#191919">我们相信在「The Apache Way」的指导下，社区将秉持更加开放包容的心态，欢迎更多贡献者加入，共同为中国开源事业添砖加瓦！”</span></p> 
  <p style="text-align:center"><strong style="color:#000000"> 感谢每一位贡献者！</strong></p> 
  <p style="text-align:left"><span style="color:#000000">SeaTunnel 凝聚了贡献者的智慧和心血，感谢项目的 Mentor 和 Committer 给予项目的指导，以及所有贡献者的参与！ </span></p> 
  <p style="text-align:left"><strong style="color:#000000">Champion</strong></p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#172b4d">Willem Ning Jiang （</span><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Aningjiang%40apache.org" target="_blank"><u>ningjiang@apache.org</u></a><span style="color:#172b4d"> ）</span></p> </li> 
  </ul> 
  <p style="text-align:left"><strong style="color:#000000">Mentors</strong></p> 
  <p style="text-align:left"><img alt height="290" src="https://oscimg.oschina.net/oscnet/up-3b0a2af2b70daba80d175d8a94a2430fa5a.png" width="600" referrerpolicy="no-referrer"></p> 
  <p style="text-align:left"><strong style="color:#000000">PPMCs</strong></p> 
  <p style="text-align:left"><img alt height="252" src="https://oscimg.oschina.net/oscnet/up-45e352ac3e283321ec38af75ad6b3f574a8.png" width="600" referrerpolicy="no-referrer"></p> 
  <p style="text-align:center"><strong style="color:#000000">贡献者</strong></p> 
  <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgaryelephant" target="_blank"><u>garyelephant</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRickyHuo" target="_blank"><u>RickyHuo</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkid-xiong" target="_blank"><u>kid-xiong</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCalvinKirs" target="_blank"><u>CalvinKirs</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyx91490" target="_blank"><u>yx91490</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fleo65535" target="_blank"><u>leo65535</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcnmac" target="_blank"><u>cnmac</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsimon824" target="_blank"><u>simon824</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwuchunfu" target="_blank"><u>wuchunfu</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhongjiajie" target="_blank"><u>zhongjiajie</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnielifeng" target="_blank"><u>nielifeng</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F296431555" target="_blank"><u>296431555</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdpchenxk" target="_blank"><u>dpchenxk</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhuangdeheng" target="_blank"><u>huangdeheng</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkezhenxu94" target="_blank"><u>kezhenxu94</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxtr1993" target="_blank"><u>xtr1993</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzixi0825" target="_blank"><u>zixi0825</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwolfboys" target="_blank"><u>wolfboys</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodliness" target="_blank"><u>godliness</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdailidong" target="_blank"><u>dailidong</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmdianjun" target="_blank"><u>mdianjun</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchoucmei" target="_blank"><u>choucmei</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwntp" target="_blank"><u>wntp</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhuangchong" target="_blank"><u>zhuangchong</u></a><span style="color:#000000">、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJNSimba" target="_blank"><u>JNSimba</u></a></p> 
  <p style="text-align:center"><strong style="color:#000000">项目详情</strong></p> 
  <p style="text-align:left"><span style="color:#000000">目前 SeaTunnel 的所有源代码和所有相关文档已捐赠给 Apache Software Foundation。这些代码已经在 Apache License Version 2.0 下：</span></p> 
  <p style="text-align:left"><span style="color:#000000"><strong>仓库地址：</strong> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-seatunnel" target="_blank"><u>https://github.com/apache/incubator-seatunnel</u></a></p> 
  <p style="text-align:left"><strong><span style="color:#000000">网址</span><span style="color:#000000">：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fseatunnel.apache.org%2F" target="_blank"><u>https://seatunnel.apache.org/</u></a></p> 
  <p style="text-align:left"><strong><span style="color:#000000">Proposal：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcwiki.apache.org%2Fconfluence%2Fdisplay%2FINCUBATOR%2FSeaTunnelProposal" target="_blank"><u>https://cwiki.apache.org/confluence/display/INCUBATOR/SeaTunnelProposal</u></a></p> 
  <h4 style="text-align:left"><strong style="color:#1a1a1a">附录：</strong></h4> 
  <p style="text-align:left"><strong style="color:#000000">以祝福和希望为翼，直冲云霄！(以收到寄语时间为序)</strong></p> 
  <p style="text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">很高兴能做为 SeaTunnel 的领路人，带领项目进入 Apache 孵化器， 希望 SeaTunnel 在后续孵化过程中能茁壮成长，构建健康发展的社区，成为有国际影响力的开源项目。 </span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">——Apache 软件基金会 Member 姜宁，SeaTunnel Champion</span></p> 
  <p style="text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">初心涓滴成流 (Waterdrop) 志向海纳百川 (SeaTunnel)，祝贺 SeaTunnel 加入 Apache 孵化器大家庭! </span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">——Apache 软件基金会 Member 刘天栋.Ted，SeaTunnel Mentor</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">祝贺 SeaTunnel 成功进入 Apache 孵化器，预祝 SeaTunnel 做大做强，再创辉煌，顺利毕业！ </span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— Apache 软件基金会 IPMC 柯振旭，SeaTunnel Mentor</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">祝贺SeaTunnel进去Apache孵化器，期待看到他们在Apache孵化器的成长，建立更为成熟的社区。 </span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">——Apache 软件基金会 董事 吴晟 Sheng Wu</span></p> 
  <p style="text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p><span style="color:#000000">"There is high demand for convenient, easy to use and powerful tools</span> <span style="color:#000000">for transferring and transforming large amounts of data. I'm happy to</span> <span style="color:#000000">see that SeaTunnel has joined Apache incubator and I will follow its</span> <span style="color:#000000">growth!"</span></p> </li> 
  </ul> 
  <p style="margin-left:32.581759999999996px; text-align:right"><span style="color:#333333">——</span><span style="color:#000000">Alexey Milovidov, ClickHouse.</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel 进入 Apache 孵化器，希望 SeaTunnel 在社区中吸收更多营养茁壮成长。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 腾讯开源联盟主席 单致豪</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel 进入 Apache 孵化器，很开心看到越来越多的中国开源项目发展壮大，预祝 SeaTunnel 早日发展成为一个成熟健康的开源社区，壮大中国开源力量。</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">——SphereEx 联合创始人 & CTO，Apache ShardingSphere PMC 潘娟（Trista）</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 加入Apache孵化器！SeaTunnel 作为一款简单易用、性能突出的海量数据处理产品，今年我们也实现了 SeaTunnel 的 Doris Spark/Flink Sink，希望打通从数据处理到数据分析的通路，能更好服务所有开源用户。我们也相信SeaTunnel进入孵化器后，在Apache 之道的指引下社区可以进一步发展，有更多热爱开源的企业和个人开发者一同参与进来！最后预祝SeaTunnel 可以早日毕业！</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— Apache Doris PPMC 陈明雨</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel 成功进入 Apache 孵化器，很高兴看到围绕着数据流转又有一个新的优秀的开源项目出现，现在这个时代，说数据作为业务的核心一点不为过，而且数据存储方面的技术又在这个时代高度的细分化，数据库之间的同步和转化非常有必要，希望 SeaTunnel 成为打通数据孤岛的「桥梁」！</span></p> </li> 
  </ul> 
  <p><span style="color:#333333">                                                                                                                                                                                         — PingCAP 联合创始人 & CTO 黄东旭</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">祝贺 SeaTunnel 进入 Apache 孵化器，越来越多的来自中国的孵化器项目表明了中国开源社区的活跃和技术贡献，非常高兴看到 SeaTunnel 社区在数据处理方面的新思考，期待再孵化过程中看到 SeaTunnel 社区的成长！</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— Apache Kylin PMC Luke Han</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel 成功进入Apache孵化器。现在是一个异构数据的时代，各种数据库、大数据平台之间需要一个开源、高效的连接器，希望 SeaTunnel 成为这个细分领域的领军者！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 涛思数据 TDengine 创始人陶建辉</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">可喜可贺，恭喜 SeaTunnel 成功进入Apache孵化器，预祝团队再创辉煌！作为同是Apache 基金会的 Cassandra 项目，期待与SeaTunnel深度整合。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— DataStax(Cassandra) China总经理 卢东明</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 进入 Apache孵化器，SeaTunnel 是一个简单易用的数据同步组件，通过SeaTunnel 可将数据更方便导入 Apache Hudi 数据湖中，也期待两个社区后续进行更深度的合作！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— Apache Hudi PMC 李少锋</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">只有流动的数据，才能激发其价值的释放，SeaTunnel 以海纳百川的志向，为上下游提供数据流动的利器。祝贺 SeaTunnel 成功进入 Apache 孵化器，预祝 SeaTunnel 成为成熟的技术社区。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 巨杉数据库 技术生态资深总监 萧少聪</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">SeaTunnel, 愿你们的技术在 Apache 孵化器里真正成长为数据海洋里具有无敌穿透力和超强连接力的平台。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— OpenTEKr 创始人 狄安</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 进入 Apache 孵化器，希望 SeaTunnel 社区快速成长，传播 Apache way，服务更多开发者，成为海量数据处理领域明星级产品。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">——Apache RocketMQ PMC 杜恒</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#000000">恭喜 SeaTunnel 进入 Apache 孵化器，感谢项目对开源事业的贡献，这是一个好的开始，希望项目在开源大家庭中更好成长。</span></p> </li> 
  </ul> 
  <p style="margin-left:42.666666666666664px; text-align:right"><span style="color:#333333">—— AWS 开发者运营 郭悦</span></p> 
  <p style="margin-left:42.666666666666664px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#000000">SeaTunnel（原名水滴 / Waterdrop）通过提供如同《三体》中“水滴”探测器般强大的技术能力，为开源数据技术的发展做出了卓越贡献，成功入选 Apache 孵化器。我们期望看到越来越多像 SeaTunnel 这样的中国开源项目和社区涌现出来，中国开源事业的未来将是星辰大海！</span></p> </li> 
  </ul> 
  <p style="margin-left:42.666666666666664px; text-align:right"><span style="color:#333333">—— NEAR Foundation  Robert Yan</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel，成为Apache孵化项目中的新成员，更希望 SeaTunnel 社区能够更好的践行 Community Over Code 的理念，不断发展壮大，百尺竿头更进一步，早日毕业成为 Apache 顶级项目。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 开源社理事长 庄表伟</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel，</span><span style="color:#000000">进入 Apache 孵化器，为我们有树立了一个学习的榜样！希望未来 SeaTunnel 社区能够发展壮大，我们多多交流，向你们学习！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 云溪数据库 吴昱</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel，成功进入 Apache 孵化器，成为 Apache 项目中的一员。希望 SetTunnel 能够更好的发展好社区，吸引更多的人参与到开源贡献中来，让大家体会到参与开源的乐趣。</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— 极狐(GitLab) 马景贺</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel，希望在 ASF 的孵化下，SeaTunnel 能够发展成为一个更加健康的开源项目社区，并调动国内更多参与者的积极性。</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— 开源中国(OSChina) 林日华</span></p> 
  <p style="text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">在开源同仁的大力支持下，SeaTunnel 得以成功加入 Apache 孵化器，这是社区的力量。这意味着 SeaTunnel 迈入了一个新的阶段，未来会变得更活跃、更规范、更国际化，服务更多开发者。祝贺 SeaTunnel！加油！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 马红伟 百度开源办公室产品运营经理</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 成功进入 Apache 孵化器，希望这个项目能够发展壮大，引导更多的技术人才理解开源精神，践行开源理念完成社会创新，大家一起 Tech4Good！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 图鸥公益（NGO2.0)张倩</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 顺利进入 Apache 软件基金会孵化，希望未来能有机会在 The Apache Way 的引领下和 Kyuubi 社区产生更多交流与合作。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— Kent Yao, Apache Kyuubi PPMC</span></p> 
  <p style="text-align:right"> </p> 
  <p style="text-align:left"><span style="color:#333333">● 恭喜 SeaTunnel 进入 Apache 软件基金会孵化，滴水成河，绵延不绝，携手共进，汇聚开源星海。</span></p> 
  <p style="text-align:right"><span style="color:#333333">—— 开源之夏 李梦</span></p> 
  <p style="text-align:right"> </p> 
  <p style="text-align:left"><span style="color:#333333">● 恭喜 SeaTunnel，希望在 ASF 的孵化下，项目更加成熟稳健，更多开发者、用户从中受益，推动大数据开源和领域向前发展。</span></p> 
  <p style="text-align:right"><span style="color:#333333">—— Apache InLong PPMC 张超</span></p> 
  <p style="margin-left:42.666666666666664px; text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 顺利进入 Apache 软件基金会孵化，预祝项目越来越好，社区越来越活跃，践行开源精神，服务更多开发者！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— InfoQ 用户运营负责人 赵萌</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">集聚开源力量，向世界展示中国。我们的征途是星辰大海。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— GoodERP 开源俱乐部发起人 Jeff Wang</span></p> 
  <p style="text-align:center"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel，希望 SeaTunnel 不断践行开源精神，活跃技术社区，成为有国际影响力的项目。同时，也希望更多的中国开源项目和SeaTunnel一同走向国际！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 稀土掘金 月影（吴亮）</span></p> 
  <p style="text-align:left"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel 进入Apache 孵化器！期待能和 SeaTunnel 互勉互助，携手并进，汇聚更多同行者，把 Apache 孵化器里的中国宝宝们早日培养壮大，共赴星辰大海。</span></p> </li> 
  </ul> 
  <p style="text-align:justify"><span style="color:#333333">                                                                                                                                                                                                     —— Apache Linkis PPMC, 邸帅</span></p> 
  <p style="text-align:justify"> </p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜 SeaTunnel 进入 Apache 孵化器，开源力量不断积累壮大。随着数字化进程加速，产业对数据集成管理的需求会愈加迫切，希望 SeaTunnel 不断发展壮大，通过开源推动产业数字化发展。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 信通院 郭雪</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">祝贺 SeaTunnel 成功进入 Apache 孵化器，期待未来在海量数据处理领域大放异彩！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 迪码科技 孙乐</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">数据“水管”和数据“水库”是数字时代的两大基础设施，目前国内外有很多不同类型的“水库”，然而优秀的开源“水管”却很少。很高兴看到这一领域出现了一个优秀的开源项目，恭喜 SeaTunnel 成功进入Apache孵化器！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">——</span><span style="color:#333333"> </span><span style="color:#333333">Greenplum中国开源社区发起人，四维纵横创始人 姚延栋</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">SeaTunnel 以出色的插件化和模块化架构设计，帮助用户灵活高效地构建 Pipeline 通道，轻松应对了各种复杂业务场景。SeaTunnel 开源社区也日益壮大，群英荟萃，未来可期！</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— Apache Druid PMC </span><span style="color:#333333">金嘉怡</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 成功进入 Apache 孵化器，很高兴看到又一个中国的优质开源项目走上国际舞台，开源路漫漫但水滴石穿，加油！</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">— Elastic 中文社区创始人、INFINI Labs 创始人 曾勇</span></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">数据引擎进入场景时代，越来越丰富的数据引擎之间的数据同步、转化有大量的需求存在，希望SeaTunnel 可以全球开发者提供高效、稳定的数据传输工具。</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— Apache Foundation Member 郭炜，SeaTunnel Mentor</span></p> 
  <p style="margin-left:34.13333333333333px; text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">SeaTunnel 有望成为 Apache 生态里支持海量数据同步与转换的强大平台，想做好并不容易、是一个有技术挑战的旅程，但我非常看好一起做开源贡献的这帮伙伴们，加油，同时欢迎更多伙伴的加入，共建开源伊甸园。</span></p> </li> 
  </ul> 
  <p style="margin-left:34.13333333333333px; text-align:right"><span style="color:#333333">—— 白鲸开源联合创始人 & Apache DolphinScheduler VP 代立冬，SeaTunnel Mentor</span></p> 
  <p style="text-align:justify"> </p> 
  <p style="text-align:justify"><span style="color:#333333">在加入孵化器之际，社区也收到了来自用户代表的祝福。</span></p> 
  <p style="text-align:justify"> </p> 
  <p style="text-align:justify"><strong style="color:#333333">用户代表</strong></p> 
  <p style="text-align:justify"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:justify"><span style="color:#333333">恭喜SeaTunnel顺利进入Apache孵化器，感谢它解决了我们数据仓库入仓出仓、人群计算等场景中的难题。衷心祝愿SeaTunnel茁壮成长，在开源的道路上，百尺竿头，更进一步！</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 唯品会 Olap 团队负责人 王玉</span></p> 
  <p style="text-align:right"> </p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#333333">恭喜 SeaTunnel 顺利进入Apache孵化器，SeaTunnel作为B站数据平台离线出入仓核心工具，在B站每天完成千亿级记录、百T级数据的出入仓，解决了我们电商、直播、创作中心等场景核心任务出入仓难题。祝愿SeaTunnel早日成为Apache顶级项目，成为又一个优秀的开源项目。</span></p> </li> 
  </ul> 
  <p style="text-align:right"><span style="color:#333333">—— 哔哩哔哩资深开发工程师 张宗耀</span></p> 
  <p style="text-align:left"> </p> 
  <p style="text-align:left"><strong style="color:#000000">衷心欢迎更多人加入！</strong></p> 
  <p style="text-align:left"><span style="color:#000000">能够进入 Apache 孵化器，SeaTunnel 新的路程才刚刚开始，但社区的发展壮大需要更多人的加入。我们相信，在「</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwillemjiang.github.io%2Fopensource%2F2018%2F10%2F21%2Fasf-introduction.html%23%25E7%25A4%25BE%25E5%258C%25BA%25E5%25A4%25A7%25E4%25BA%258E%25E4%25BB%25A3%25E7%25A0%2581-community-over-code" target="_blank"><u>Community Over Code</u></a><span style="color:#000000">」（社区大于代码）、「</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwillemjiang.github.io%2Fopensource%2F2018%2F10%2F21%2Fasf-introduction.html%23%25E5%25BC%2580%25E6%2594%25BE%25E7%259A%2584%25E5%258D%258F%25E4%25BD%259C%25E6%2596%25B9%25E5%25BC%258F-open-and-cooperation" target="_blank"><u>Open and Cooperation</u></a><span style="color:#000000">」（开放协作）、「</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwillemjiang.github.io%2Fopensource%2F2018%2F10%2F21%2Fasf-introduction.html%23%25E7%25B2%25BE%25E8%258B%25B1%25E7%25AE%25A1%25E7%2590%2586-meritocracy" target="_blank"><u>Meritocracy</u></a><span style="color:#000000">」（精英管理）、以及「多样性与共识决策」等 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.apache.org%2Ftheapacheway%2Findex.html" target="_blank"><u>The Apache Way</u></a><span style="color:#000000"> 的指引下，我们将迎来更加多元化和包容的社区生态，共建开源精神带来的技术进步！</span></p> 
  <p style="text-align:left"><span style="color:#000000">我们诚邀各位有志于让本土开源立足全球的伙伴加入 SeaTunnel 贡献者大家庭，一起共建开源!</span></p> 
  <ul style="list-style-type:disc"> 
   <li> <p style="text-align:left"><span style="color:#000000"><strong>提交问题和建议</strong>：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-seatunnel%2Fissues" target="_blank"><u>https://github.com/apache/incubator-seatunnel/issues</u></a></p> </li> 
   <li> <p style="text-align:left"><strong><span style="color:#000000">贡献代码：</span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-seatunnel%2Fpulls" target="_blank"><u>https://github.com/apache/incubator-seatunnel/pulls</u></a></p> </li> 
   <li> <p style="text-align:left"><span style="color:#000000"><strong>订阅社区开发邮件列表 :</strong> </span><span style="color:#333333">dev-subscribe@seatunnel.apache.org</span></p> </li> 
  </ul> 
  <p style="text-align:left"><strong><span style="color:#000000">联系我们：</span></strong></p> 
  <p><strong><span style="color:#000000">开发邮件列表：</span></strong><a href="https://www.oschina.net/news/dev@seatunnel.apache.org"><u>dev@seatunnel.apache.org</u></a><span style="color:#000000">. </span></p> 
  <p style="text-align:left"><strong><span style="color:#000000">加入 Slack: </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjoin.slack.com%2Ft%2Fapacheseatunnel%2Fshared_invite%2Fzt-10u1eujlc-g4E%7EppbinD0oKpGeoo_dAw" target="_blank"><u>https://join.slack.com/t/apacheseatunnel/shared_invite/zt-10u1eujlc-g4E~ppbinD0oKpGeoo_dAw</u></a></p> 
  <p style="text-align:left"><strong><span style="color:#000000">关注 Twitter: </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2FASFSeaTunnel" target="_blank"><u>https://twitter.com/ASFSeaTunnel</u></a></p> 
  <p style="text-align:left"><span style="color:#000000">秉持开源精神，乐视、白鲸开源科技与开源社区一起致力于 SeaTunnel 的发展完善及与 Apache 等生态圈的融合。</span><span style="color:#000000">目前，SeaTunnel 已经与多个 Apache 项目完成整合，包括 Apache DolphinScheduler，Apache Spark, Apache Flink, Apache Hadoop, Apache Hudi，Apache HBase ，Apache Kudu 等等。</span></p> 
  <p style="text-align:left"><span style="color:#000000">成立四年以来，SeaTunnel 已通过组织不同形式的活动，如 Meetup 收获了无数开发者、运营和布道者人才加入，用户群体目前已超过 2000 人。</span></p> 
  <p style="text-align:left"><span style="color:#000000">未来，我们欢迎有更多志同道合的人加入开源共建，在遵循 Apache 原则的基础上，共同让 SeaTunnel 在众多开源项目中成为一颗耀眼的新星！</span></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            