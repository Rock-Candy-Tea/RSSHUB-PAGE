
---
title: 'StreamX 1.2.2 正式发布, 迄今最稳定可用版本重磅发布!'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c76fa30a02baeccd2e4463d09638ff884a2.jpg'
author: 开源中国
comments: false
date: Fri, 25 Mar 2022 08:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c76fa30a02baeccd2e4463d09638ff884a2.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span>​</span>今天 , StreamX 很高兴的宣布 1.2.2 版本正式发布。本次是 2022 开年之初发布的第一个正式版本, 修复已知历史 bug, 支持 Flink 所有部署模式，提升易用性和稳定性。2022 新年伊始, 春日正盛, 一片欣欣向荣之景象! 众多企业也在摩拳擦掌, 规划蓝图, 准备大干一场! 此时 StreamX 带来 <strong>稳定版本</strong>, 助力大家<strong>放心的上生产环境</strong>, 愿为大家在流处理领域带来一点方便, 为 Apache Flink 的落地和普及助一臂之力!<br>  </p> 
<p><img height="1757" src="https://oscimg.oschina.net/oscnet/up-c76fa30a02baeccd2e4463d09638ff884a2.jpg" width="3229" referrerpolicy="no-referrer"><br>  </p> 
<h4><strong>项目地址:</strong></h4> 
<p><span style="color:#1a439c">Gitee: <a href="https://gitee.com/streamxhub/streamx">https://gitee.com/streamxhub/streamx</a></span></p> 
<p><span style="color:#1a439c">Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamxhub%2Fstreamx" target="_blank">https://github.com/streamxhub/streamx</a></span><br>  </p> 
<h2>新增功能<br>  </h2> 
<p>本次新增 remote, yarn-session 部署模式, 到此 <span style="color:#1a439c"><strong>StreamX 已经完整的支持 Flink 所有部署模式</strong></span>(remote、yarn-perjob、yarn-session、yarn-application、 k8s-native-session、k8s-native-application ) 满足用户各种场景下的部署需求。 此外, 本次统一了程序打包pipeline, 简化了构建流程, 减少用户的学习成本, 使用起来更简单。新增功能明细如下:</p> 
<div> 
 <ul> 
  <li>新增 Remote 部署模式</li> 
  <li>新增 Yarn-session 部署模式</li> 
  <li>新增 Yarn-perjob 部署模式</li> 
  <li>统一项目构建上线流程</li> 
  <li>新增 Apache Doris datastream connector</li> 
  <li>新增 Redis datastream connector</li> 
  <li>新增 Flink Cluster集群管理</li> 
  <li>内置 maven 不强制要求部署机安装 maven</li> 
  <li>maven 支持设置远程仓库地址, 加速依赖下载</li> 
  <li>项目构建时支持指定 maven 构建参数</li> 
 </ul> 
 <p><img src="https://oscimg.oschina.net/oscnet/up-37a2aa4145cd48a83f7ba2f63f8bb221442.png" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center"><span style="color:#999999"> [ StreamX 打包构建流程 ]</span></p> 
 <p> </p> 
 <h2>修复增强<br>  </h2> 
 <ul> 
  <li>on Yarn 模式下在 hadoop 某些版本存在的任务提交失败的 bug</li> 
  <li>Flink Sql 添加依赖时检查到不匹配 scala 版本未能阻止添加的bug</li> 
  <li>Flink Sql 格式化存在的 bug</li> 
  <li>在 Flink 某些版本下关闭 packageProgram导致的 bug</li> 
  <li>任务编辑和添加切换Flink 部署模式导致页面错乱的 bug</li> 
  <li>任务在启动和停止时加入超时, 时间内未成功状态设置为失败<br> <br>  </li> 
 </ul> 
 <h2>感谢贡献者<br>  </h2> 
 <p>StreamX 的发展离不开社区的 Contributor 们的付出的积极努力, 很多开发者下班后忙碌到凌晨一两点, 周六日无休, 非常感谢贡献者们在测试和开发中做出的努力! 以下为 Contributor 名单, 排名不分先后:</p> 
 <p>Al-assad, czy006, daixiaoyu, honghaoli9898, JNSimba, lvshaokang, monrg, SoberChina, wolfboys, Whojohn, wysstartgo,xinzhuxiansheng,Zclhlmgqzc, zhangjun0x01</p> 
 <p> </p> 
 <h2>以梦为马<br>  </h2> 
 <p>在 StreamX 1.2.2 发布之际, 也快迎来 StreamX 开源一周年, 我们收到了一些用户的心声和大佬的寄语, 各位的勉励会时刻鞭策着我们, 努力做得更好!</p> 
 <h4>寄语</h4> 
 <blockquote> 
  <p>StreamX 社区一直以来都在用心做好流批一体一站式大数据平台，并有着非常多比如 Web IDE、CI/CD、on k8s 等关键能力，强烈推荐大家使用！也欢迎更多贡献者加入，一起把 StreamX 社区发展的更加繁荣！</p> 
  <p> </p> 
  <p>白鲸开源联合创始人 & Apache DolphinScheduler PMC Chair & Apache SeaTunnel PPMC & Mentor Apache 孵化器导师 & ASF Mentor   代立冬</p> 
 </blockquote> 
 <blockquote>
  从基础软件内核到用户侧解决方案，往往需要在用户体验上倾注大量的时间和精力，StreamX 正是为 Flink 和 Spark 应用量身定制的一个用户友好的控制平台。很高兴看到 StreamX 项目新版发布，期待 StreamX 在应用部署和管理方面的经验反馈到上游 Flink / Spark 社群，开源协同，把流批一体的数据处理能力带到更多的企业当中。 
  <p>                                                                                                                     </p> 
  <p> — Apache Flink Committer & Apache Curator PMC & ASF Member & <<夜天之书>>作者  & 2021中国开源先锋33人  tison<br>                                                                                                                                                        </p> 
 </blockquote> 
 <blockquote>
  在 StreamX 刚起步的时候就关注到了这个项目，见证了项目的一步步发展, 现在已经拥有一个活跃的开源社区，众多企业使用，已有头部IT教育机构的纳入课程，StreamX 为企业和开发者提供了标准化了配置、开发、测试、部署、监控、运维的全流程管理工具。大大提高了开发效率及降低成本，推荐更多的用户去使用StreamX，同时也希望大家积极的参与到StreamX中来，共建繁荣开源社区。
  <br> 
  <br> 
  <br> — Apache Doris PPMC  张家锋
 </blockquote> 
 <blockquote>
  StreamX 作为一个开源的数据处理平台，使数据处理变的更加容易，更好闭环了数据的开发与任务管理的环节，每次发版都越来越靠近他的终极目标：一站式数据处理平台。
  <br> 
  <br>                                                                                                                                                  
  <br>  — Apache SeaTunnel PPMC  Gary 
  <p> </p> 
 </blockquote> 
 <p> </p> 
 <h4><strong>用户代表</strong><br>  </h4> 
 <blockquote> 
  <p>StreamX 是一款非常优秀的 Flink&Spark 极速开发框架与一站式大数据流处理平台。开发者在使用StreamX时只需编写简单的配置文件，即可实现多个开箱即用功能的复用；通过简洁易用的Web页面，即可实现开发任务的编译、部署与管理监控。该框架一经问世便深受广大开发者的喜爱。目前，StreamX 的社区活跃度高，经过多个版本的更新迭代，已有较高的易用性和完成度。</p> 
  <p>StreamX 能让开发者减少重复代码，把精力更多集中于业务本身，让大数据流处理变得更加便捷！这也与尚硅谷教育“让天下没有难学的技术”的理念不谋而合。尚硅谷也本着非精品不用的原则，与 StreamX 主创团队达成合作，为 StreamX 提供高质量的使用教程与视频等配套资料！</p> 
  <p>强烈推荐各位大数据开发者学习并使用 StreamX，它将大大提高您的开发效率。也预祝 StreamX 发展越来越好！<br> <br>                                                                                                                                                <br> — 尚硅谷教育 大数据负责人  缪传海</p> 
 </blockquote> 
 <blockquote>
  StreamX优雅的编程框架、简单易用的WebIDE，沉淀了主创团队在 Flink&Spark 技术领域丰富的经验以及独到的平台观。数鑫科技在流批一体开源编程平台技术选型过程中，关注到 StreamX 在编程模型的高度抽象性、可扩展性、可配置性等方面设计的非常出色，因此毫不犹豫的选择 StreamX 作为自身可信数据流通引擎数据消费端配套的流批一体编程框架。相信: StreamX 一定会被越来越多的流批一体开发者深度关注和使用，无论是希望快速开发 Flink 数据加工处理逻辑的初学者、还是资深的平台架构师。StreamX 将会深刻的影响 Flink 开源社区。
  <br> 
  <br> 
  <br> — 深圳数鑫科技 CTO 廖炳才
 </blockquote> 
 <blockquote>
  StreamX 是一个非常好的 Flink 开发平台，功能完善，使用方便，在我们的生产使用过程中，主要是以 application方式将 Flink 任务部署到 k8s 容器，StreamX 帮助我们方便的管理 Flink 任务，大大的减少了运维成本，提高效率，欢迎大家使用，也祝愿StreamX 越来越好。
  <br> 
  <br>                                                                                                                                               
  <br> — Baidu 资深大数据开发工程师 张军
 </blockquote> 
 <blockquote>
  StreamX 是目前少有的实时计算平台项目，结合了当前最新的Flink流计算实现了基于Standalone、YARN、K8S 等多种模式的作业提交和管理模式，降低用户管理实时作业门槛，希望2022年能继续发力，往Flink SQL 平台迈进，同时2022年我也会持续关注StreamX 并且贡献自己一份力量!
  <br> 
  <br> 
  <br>  —  Apahce Flink 社区志愿者 & StreamX 贡献者  陈政羽 
  <p> </p> 
 </blockquote> 
 <blockquote>
  StreamX 秉承着开箱即用的思想，极大的简化了 Flink&Spark 开发部署流程，在框架中封装了很多源和接收器，让开发人员只专注业务逻辑，基于以上优势我司在实际生产中使用了 StreamX。强烈推荐更多的公司和开发者使用，祝愿 StreamX 发展的越来越好。
  <br> 
  <br> 
  <br>  — INMOBO中国 大数据团队负责人 于威
 </blockquote> 
 <blockquote>
  StreamX 作为运荔枝数据平台核心工具，解决了我们实时任务从开发、部署、运维各个环节的难题，保障了实时任务的稳定性；它直观可视化的操作界面，无论是基于 DataStream API 还是 Flink SQL 都能快速、方便的一站式完成业务逻辑的开发，使得流式任务整个开发过程更加敏捷。
  <br> 
  <br> 
  <br> — 成都运荔枝科技 大数据应用架构师  李建 
  <p> </p> 
 </blockquote> 
 <blockquote>
  StreamX 作为一款功能强大、场景覆盖广的数据开发框架平台，提供了非常优秀的产品化解决方案，化繁为简，降低了用户使用 Flink 等计算引擎的成本并提升了用户体验 。尘锋信息通过 StreamX 用极短的调研试用时间和极少的人力成本落地了实时计算平台，避免了在基础设施建设上浪费大量人力和时间，并快速服务业务为市场引得先机。 
  <p>作为一名数据开发，不仅可以通过 StreamX 提供的编程模型、计算引擎集成、依赖管理等功能，快速且优雅的完成需求开发及维护，并且能够从 StreamX 的源码中学习到非常多的底层知识，开发出更加优秀稳定的应用, 相信未来会有越来越多的数据开发同学发现 SteamX ，用上 StreamX ，爱上 StreamX ，并通过 StreamX 创造数据价值。</p> 
  <p><br> —北京尘锋信息技术有限公司 资深数据开发工程师  代欣雨</p> 
 </blockquote> 
 <blockquote>
  SteamX 是一套优秀的 Flink 任务管理工具，微品致远在数据处理平台流式数据处理选型的时候了解到 StreamX，在深入了解后，被 StreamX 流式计算的全流程打通所吸引，便毫不犹豫的纳入到了微品致远的数据处理平台中。引入 StreamX 后，从流式计算的 ide 开发，到后续的任务上线，完全打通，解决了之前 Flink 任务上线混乱，管理起来繁琐的问题，从而提高了提高了团队任务开发到上线的效率。相信随着 StreamX 的影响力的扩大，会有更多的 Flink 开发者将 StreamX 应用到自己的开发上线流程中。
  <br> 
  <br> 
  <br> — 深圳微品致远 大数据开发组长 张凌玮 
  <p> </p> 
 </blockquote> 
 <blockquote>
  第一次遇到 StreamX，就被它的友好的界面，丰富的功能所吸引。乐我无限 从 1.0 开始跟进，StreamX 有着活跃的社区，功能也在一步一步的迭代更新，越来越强大。通过 StreamX 我司成功的迁移了 50+ 个实时作业，做到了开发模式的统一管理，为我司的开发维护节省了许多时间。使用 StreamX 使得 Flink 作业开发更方便，管理更友好，维护更省心。StreamX 一直在追求做到更好，不断解决一些痛点问题，强烈推荐大家使用。
  <br> 
  <br> 
  <br> — 乐我无限 高级大数据开发工程师  秦基勇 
  <p> </p> 
 </blockquote> 
 <h2 style="text-align:center"> </h2> 
 <h2>未来规划<br>  </h2> 
 <p>目前StreamX 已完成 Flink 任务的托管, 从项目创建伊始, 我们就尝试系统性的解决 Flink 多版本的支持, 任务Jar包隔离, 同时支持 DataStream 和 FlinkSQL, 支持Flink 所有部署模式...等一系列的常见问题, 所幸的是这部分基础建设工作已经完成且趋于稳定, 这部分工作很有挑战, 也非常重要，感谢所有开发者们付出的努力。后面我们<span style="color:#1a439c"><strong>会逐步把 StreamX 里沉淀的一些好的经验反馈到上游 Flink / Spark 社群, 开源协同</strong></span>。接下来的 1.3.0 中我们关注的重点是流式数仓(Streaming-Warehouse)<strong> </strong>和 云原生(Cloud-Native)。会新增全新的开发工作台 - SQL Workbench(草稿、调试、预览、发布、锁定、版本管理...), 该部分的开发工作已经在进行中, 了解详情请移步 1.3.0的 roadmap。</p> 
 <p> </p> 
 <p><img height="800" src="https://oscimg.oschina.net/oscnet/up-2ce85c23a177e45ed71e4042abe61e2b297.png" width="1280" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center"><span style="color:#999999">[ SQL Workbench Preview ]</span></p> 
 <h2 style="text-align:center"> </h2> 
 <h2>加入我们<br>  </h2> 
 <p>StreamX 遵循 Apache-2.0 开源协议，将会是个长期更新的活跃项目，自项目开源以来就受到很多同行的关注和认可，目前已经登记生产使用的用户有: <span style="color:#1a439c"><strong>尚硅谷</strong>, <strong>INMOBI</strong>, <strong>JOYME</strong> , <strong>百丽国际</strong>, 中<strong>联重科... </strong></span>更有<strong>百度</strong>这样的一线大厂。StreamX 在没有任何形式推广的情况下，靠口碑在不到一年的时间里已经累计<strong> <span style="color:#1a439c">900 + star</span></strong><span style="color:#1a439c">，<strong>贡献者共计30位，总代码量已经突破10万行</strong></span>。StreamX 于 2021 年 11 月荣获开源中国<strong>「<span style="color:#1a439c">最有价值开源项目</span>」</strong>。随后荣获「2021 年度 OSC 中国开源项目评选」的<strong>「<span style="color:#1a439c">最受欢迎项目</span>」</strong>，非常感谢中国本土最大最权威的开源社区-开源中国的认可! 并且陆续有多家IT教育机构出相关课程, 更有<span style="color:#1a439c"><strong>尚硅谷</strong></span>这样的品质和口碑一流的 IT 教育机构和 StreamX 展开合作, 这对于一个开源不到一年的项目来说, 是非常少见的, 感谢大家支持, 我们会继续努力, 我们坚信未来会更好。</p> 
 <p><img height="622" src="https://oscimg.oschina.net/oscnet/up-9bb31b031cb377a8f7dae29038eb35c1a1a.png" width="2454" referrerpolicy="no-referrer"></p> 
 <p style="text-align:center"><span style="color:#999999">[StreamX 用户墙]</span></p> 
 <p style="text-align:center"> </p> 
 <p>流批一体，流式数仓，数据湖是大数据领域的趋势，StreamX 虽离这个目标还有一段距离，但我们始终坚信: 道阻且长，行则将至，行而不辍，未来可期。我们会积极进取，做好相关功能持续迭代优化，和社区所有小伙伴一起努力进一步建设好社区，让 StreamX 成为一个功能完善，体验更佳，用户更多的产品，再获得更多认可。真诚欢迎热爱开源的伙伴加入到社区中来，为做一个优秀实用的好项目献上一份自己的力量。</p> 
 <p> </p> 
 <p><img src="https://oscimg.oschina.net/oscnet/up-56380b04624bbd0bb8d102e366e924d1089.jpg" width="500" referrerpolicy="no-referrer"></p> 
</div>
                                        </div>
                                      
</div>
            