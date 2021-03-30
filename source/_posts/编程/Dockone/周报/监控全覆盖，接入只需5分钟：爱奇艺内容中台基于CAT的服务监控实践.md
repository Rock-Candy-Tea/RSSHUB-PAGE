
---
title: '监控全覆盖，接入只需5分钟：爱奇艺内容中台基于CAT的服务监控实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/30a811f83cfa2e1a4005f89f0b8a00db.png'
author: Dockone
comments: false
date: 2021-03-30 00:25:20
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/30a811f83cfa2e1a4005f89f0b8a00db.png'
---

<div>   
<br>系统监控一直是项目完整性的一个要素，“不让没有监控的系统上线”，这条准则也逐渐得到越来越多的人的认可。如果一个系统监控缺失，我们就无法知道系统的运行状态，以及业务的各个方面的情况，甚至系统出现宕机或者重大故障也不得而知，以至于造成重大损失。<br>
<br>爱奇艺乐道中台是由爱奇艺内容中台团队建设的集视频、音频、字幕、图片等内容的全流程生产、发布及运营的中台服务。随着业务发展及微服务化的逐渐深入，系统项目越来越多，目前已有微服务100+，需要维护内容也越来越多，链路越来越长，现有的监控手段已不能满足业务发展的需要，涌现出更多更迫切的监控需求，如：<br>
<ul><li>高效及时的发现、定位系统异常问题。系统出现异常时需要立刻感知，在业务反馈之前发现问题，定位问题需要更加高效，可视化，不能仅去服务器查日志定位问题，这样通常需要花费很长时间才能定位原因，甚至如果日志过多还不能准确定位。</li><li>上线过程可监测，出现问题第一时间回滚。每次系统发布上线都是一次bug降生的窗口期，相当比例线上问题都是上线导致或者引入的，因为一个稳定的服务，你不去更新系统代码，正常情况下不会自发的产生问题。我们需要可监测的上线过程，及时修复问题。</li><li>全面准确的度量系统服务、接口、数据库等性能。我们需要更加全面和方便的监测整个系统对外提供的服务接口和系统依赖的外部服务接口性能，QPS、慢查询等其他性能指标，性能如果有潜在问题可能在关键时候，如流量突增，导致数据库连接池打满、长事务、拖垮整个网关等重大故障。</li><li>更加及时和稳定的监测服务健康情况。虽然目前部署的服务都是双份或者多备份部署，可用性有保证，但是还是往往会出现其中部分服务出现宕机等情况，我们需要第一时间感知到这种问题，并具有持续的稳定监测。</li><li>及时监测机器（容器）性能变化。当系统遇到突发流量或者攻击等原因时很可能导致连接池打满、OOM，数据库打满，CPU、内存、磁盘打满等基础问题，这些都会导致重大事故，无法及时的监控到，就无法及时的处理，导致重大线上故障。</li><li>更加完善清晰的业务监控。以上叙述了系统监控方面的迫切需求，在业务方面如果没有监控，如节目生产数量、成功率、时效等，那么整体业务运行情况对于维护者而言就是一个黑盒，这就会陷入一个被动局面，业务的发展是技术保障的目标，不知道目标发展情况，就会让许多工作失去意义。</li></ul><br>
<br>在业务量较少，系统较少，微服务较少的时候，我们对于监控系统的需求越少，随着业务、系统爆炸性的发展就会维护起来越来越吃力，我们需要建立完备的监控体系去补齐这个短板，对各个服务、业务心中有数，为业务快速发展提供保障。<br>
<h3>监控内容及技术选型</h3>经过梳理，目前我们服务系统需要监控的具体内容有：<br>
<br>1、机器监控<br>
<br>最基础的监控，主要监控承载各个系统的虚拟机或者容器的运行情况，主要有CPU、内存、磁盘、网络等大的方面，具体指标如：cpu.busy、cpu.idle、cpu.load.5min.per.core、mem.memfree、net.if.in.bytes、df.statistics.used.percent等。<br>
<br>2、系统监控<br>
<br>各个系统所有接口、服务的监控，主要如服务状态、qps、接口性能、成功率、错误日志等。<br>
<br>具体如：服务健康情况、服务api接口qps、服务api接口性能、成功率、集群中各个机器qps、集群中各个机器访问量、整个集群qps压力、整个系统异常日志趋势等数据。<br>
<br>3、业务监控<br>
<br>根据各个服务承载的具体业务，建立业务数据大盘及相对应的监测报警策略，方便观测业务发展情况、系统运行情况、以及为业务发展决策提供参考和帮助。<br>
<br>在本着不重复造轮子的原则下，首先我们调研了公司内部现有基础监控系统的功能、接入方式、侵入性、优缺点等，由于公司内部监控系统功能比较分散、单一，无法满足我们所需的全面监控需求，所以我们倾向于自建，于是调研了常见的开源监控系统：<br>
<br>1、OpenFalcon<br>
<br>OpenFalcon是小米开源的监控系统，能够提供丰富的基础监控指标。<br>
优势：易于接入，基本无入侵，可自定义上报数据<br>
劣势：主要监控机器指标,系统监控不足<br>
<br>2、Prometheus<br>
<br>Prometheus是由前谷歌员工2015年正式发布的开源监控系统。它和OpenFalcon最大不同在于：数据采集是基于Pull模式的，而不是Push模式，并且架构非常简单。<br>
<ul><li>优势：查询引擎强大，支持PromQL，可以对数据做各种实时计算。</li><li>劣势：不易用，学习成本高，功能不够完善，基本需要搭配Grafana创建仪表盘以及查看指标。</li></ul><br>
<br>3、开源监控系统CAT<br>
<br>CAT 是美团点评开源的实时应用监控平台，提供了比较全面的实时监控告警服务。<br>
<ul><li>优势：监控功能强大，基本上可以覆盖各种监控场景</li><li>劣势：接入成本较高、对业务代码侵入较大</li></ul><br>
<br>经过多方面比对以及结合我们系统业务的监控需求，最重要的是监控功能的全面、稳定、成熟的UI、报表、告警，所以我们最后选型CAT作为我们各个系统微服务的监控系统。<br>
<h3>LEDAO-CAT监控系统的落地</h3><h4>部署与迭代</h4>CAT的部署最初是以GitHub开源代码以及相关文档进行最小化部署和试用，最初用于虚机上的少量业务系统，通过实验发现试用效果很好，满足我们对于监控系统最初的需求，随后我们对CAT进行了若干次的升级改造，来逐渐优化以适用乐道中台的业务和环境。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/30a811f83cfa2e1a4005f89f0b8a00db.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/30a811f83cfa2e1a4005f89f0b8a00db.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
目前整个乐道中台部署的CAT监控系统分别服务于海外、中国大陆，每个区域都部署了一个集群服务于对应的业务系统，如图1所示，其中目前以中国大陆的集群服务最多，国内集群微服务接入量100+、TPS 1w+，每日处理数据量1.5TB 左右，业务系统与CAT监控系统的交互如图2所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/9d51be2eb491c67c516a6ab1fe59c0ae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/9d51be2eb491c67c516a6ab1fe59c0ae.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 1 LEDAO-CAT部署</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/e6fe335a6c4a5e10fbeba884a52702c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/e6fe335a6c4a5e10fbeba884a52702c5.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 2 交互流程</em><br>
<br>其中，目前CAT支持的业务应用包括物理机、虚机、QAE容器等系统运行环境，服务通过引入ledao-cat-client包后进行简单的环境配置和监控配置即可接入监控系统，对相关的服务进行全方面的监控。<br>
<br>主要流程是cat-client-proxy收集监控配置，与服务端建立连接，通过读取需要监控的项的配置，对要监控的数据进行上报，上传到CAT服务端后对于原始数据处理、聚合、告警等。<br>
<h4>升级和改造</h4><strong>CAT接入方式和监控埋点升级</strong><br>
<br>原生CAT在系统接入时的方式是在每各应用所在的虚机固定路径上配置client.xml，其中内容主要是服务端的连接地址和端口，这样就需要在服务部署的每台机器都去配置文件，运维成本极高，在公司无统一运维的情况下，接入和维护成本都很高，而且这种方式不适用于QAE容器部署。为了解决上述问题，我们对CAT接入配置模块进行了改造，使其支持三种方式的接入配置：传统xml文件，QAE环境变量，系统配置文件properties(xml)，使其配置与宿主机解耦，只依赖于应用本身。<br>
<br>另外，CAT监控是具有侵入性的监控系统，需要在监控的地方埋点上报数据进行监控，原生的埋点方式基本是切面方式，为了简化和细化监控埋点工作，我们开发了proxy代理包，方便用户接入，其中主要扩展的埋点方式为：传统切面、声明式注解（service、method、controller、dao），以及批量配置文件方式（properties），具体如图3所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/23f89ac94bf469e7c4d51e357e0e4ef6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/23f89ac94bf469e7c4d51e357e0e4ef6.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 3 接入方式</em><br>
<br><strong>新增CAT健康检查模块</strong><br>
<br>CAT的各项监控功能已经非常全面，但是却没有应用健康的监控，监控的方式是由客户端进行数据上报，当服务宕机时，业务不可用时往往就会停止数据上报，但是CAT目前无法检测到这种客户端宕机异常，所以我们对原生CAT进行了升级，加入cat-health健康检查模块到CAT系统中，通过CAT配置健康检查，以及客户端上报的应用信息，健康检查模块会定时从不同机房拨测应用来检测应用的健康状况，如果多次反复检测到应用异常，会根据一定的判定规则进行告警通知，通过新建健康检查模块填补了原生CAT监控的空白。具体如图4所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/513fe9c32df76f0ace27dffe91b2acba.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/513fe9c32df76f0ace27dffe91b2acba.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 4 健康检查</em><br>
<br><strong>告警方式升级</strong><br>
<br>此外，在原有开源CAT告警方式基础上，结合爱奇艺自有的告警体系，我们将两者进行了融合对接，通过整合完备了整个监控系统的告警体系，支持以爱奇艺邮件、热聊、短信的方式进行对异常、健康、业务等各方面的告警发送，大大提高了告警信息的触达率，使异常实时可见，及时处理和恢复。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/1060f9e9372da13f72f55b758ba3fb9b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/1060f9e9372da13f72f55b758ba3fb9b.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 5 告警升级</em><br>
<h3>实践成果</h3>通过对原生CAT的部署及相关改造升级，我们逐步建设了一套完整的乐道中台微服务监控体系，从机器指标监控、服务健康监控、系统异常监控、系统性能监控、慢查询监控等到相关业务监控，结合CAT强大的告警配置以及爱奇艺告警方式的多样，以及优化后的CAT快速接入及埋点方式，形成了从业务快速接入——监控快速埋点——告警配置——告警触达——告警处理一整条监控链路，完整的填补了监控体系的空白。<br>
<br>其中具体是：<br>
<ul><li>CAT接入方式多样，对接成本低，一个新业务接入在5min之内可以完成。</li><li>结合cat-client-proxy依赖包，埋点配置几乎可以做到无入侵，而且整个配置快速高效。</li><li>微服务系统从硬件指标、健康情况、异常情况、性能、业务等能够被全方位的监控，几乎覆盖了所有的方面。</li><li>强大的告警配置能够实时推送系统异常信息，使问题被快速感知，及时处理。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/8b76f71fc278d1790762d808b1e3ae3a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/8b76f71fc278d1790762d808b1e3ae3a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 6 各监控指标图</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/e4b24dc00337dc3b10386ae57b69567c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/e4b24dc00337dc3b10386ae57b69567c.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 7 热聊告警</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/0d68b507b76805e0ffed1cc70e827a95.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/0d68b507b76805e0ffed1cc70e827a95.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/d01d1cbabc66e99c1b435ac80cb3fccd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/d01d1cbabc66e99c1b435ac80cb3fccd.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 8 配置接入</em><br>
<br>从最小化部署实验，到功能升级改造，再到团队推广及同事认可，LEDAO-CAT逐步发展壮大，目前乐道中台整个团队统一使用LEDAO-CAT作为监控工具，目前分别部署了大陆和海外两大集群，保障线上服务稳定高效运行，为快速发展的业务保驾护航。<br>
<h3>总结展望</h3>监控系统一直是业务发展过程中不可或缺的重要一部分，对于服务稳定运行提供极其重要的保障作用，对于不同的业务系统当然也会有不同的与其适配的监控系统，目前在国内和国外，不同公司都提供了一些开源的监控服务，CAT作为一款优秀的开源监控系统，提供了非常全面和强大的监控功能，基本能够满足我们目前所有的监控需求。<br>
<br>本文大概介绍了CAT在爱奇艺乐道中台的一次落地实践，主要介绍了我们监控的需求、解决方案、优化改造以及阶段性成果，虽然目前的功能大概满足我们的需求，但是还是有如下几点不足仍在研究，如分布式Transaction、业务监控大盘、与nacos的深度整合等，这些都是后续我们要做的方向，使整个监控体系更加完善，更快更好更新的支撑业务快速发展。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/_sjwt6lxhyjNExO81gES9w" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/_sjwt6lxhyjNExO81gES9w</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            