
---
title: 'ElasticJob 3.0.0：打造面向互联网生态和海量任务的分布式调度解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8b3c6f5b2710171500eebcf87307577645a.JPEG'
author: 开源中国
comments: false
date: Fri, 30 Jul 2021 11:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8b3c6f5b2710171500eebcf87307577645a.JPEG'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">ElasticJob 于 2020 年 5 月 28 日重启并成为 Apache ShardingSphere 子项目。新版本借鉴了 ShardingSphere 可拔插架构的设计理念，对内核进行了大量解耦和重构，打造了全新的作业 API，提升项目的易用性。自重启以来，社区活跃度大幅增加，目前项目累计收获超过 7,000 Star，贡献了超过 2,000 次 commits，<span style="color:#0052ff">面向互联网生态和海量数据的分布式调度平台将进一步被大规模使用，解决用户的作业调度难以水平扩展、可用性有限的问题。</span></span></p> 
<p>本文将给各位介绍 ElasticJob 3.0.0 究竟做出了怎样的改变。</p> 
<p><strong>作者｜吴伟杰</strong></p> 
<p><span style="color:#000000"><span style="background-color:null">SphereEx 中间件研发工程师，Apache ShardingSphere committer，ElasticJob 3.0.0 版本 Release Manager。目前专注于 Apache ShardingSphere 及其子项目 ElasticJob 的研发。</span></span></p> 
<h2><strong>ElasticJob 简介</strong></h2> 
<p>ElasticJob 是面向互联网生态和海量任务的分布式调度解决方案，由两个相互独立的子项目 ElasticJob-Lite 和 ElasticJob-Cloud 组成。它通过弹性调度、资源管控、以及作业治理的功能，打造一个适用于互联网场景的分布式调度解决方案，并通过开放的架构设计，提供多元化的作业生态。它的各个产品使用统一的作业 API，开发者仅需一次开发，即可随意部署。</p> 
<p style="text-align:center"><img height="470" src="https://oscimg.oschina.net/oscnet/up-8b3c6f5b2710171500eebcf87307577645a.JPEG" width="1080" referrerpolicy="no-referrer"></p> 
<h2><strong>3.0 的改变</strong></h2> 
<p><strong><span style="color:#0052ff">一、全新作业 API，作业类型可灵活扩展</span></strong></p> 
<p><span style="color:#0052ff">新版本的 ElasticJob ，打造了全新的作业 API。</span>开发者不再局限于框架预置的作业类型，能够借助 SPI 扩展作业执行器类型，打造更贴合实际场景的作业逻辑。除此之外，得益于新的模块化架构，开发者可以方便地向社区回馈独立、通用的作业类型。</p> 
<p>以 ElasticJob 2.1.5 版本为例，作业执行器的类型已经固定在代码逻辑中，传入的参数如果不是内置的作业执行器类型，则直接抛出异常，开发者无法直接扩展。</p> 
<blockquote> 
 <p><span style="color:#000000"><span style="background-color:#ffffff">public static AbstractElasticJobExecutor getJobExecutor(final ElasticJob elasticJob, final JobFacade jobFacade) &#123;</span><br> <span style="background-color:#ffffff">    if (null == elasticJob) &#123;</span><br> <span style="background-color:#ffffff">        return new ScriptJobExecutor(jobFacade);</span><br> <span style="background-color:#ffffff">    &#125;</span><br> <span style="background-color:#ffffff">    if (elasticJob instanceof SimpleJob) &#123;</span><br> <span style="background-color:#ffffff">        return new SimpleJobExecutor((SimpleJob) elasticJob, jobFacade);</span><br> <span style="background-color:#ffffff">    &#125;</span><br> <span style="background-color:#ffffff">    if (elasticJob instanceof DataflowJob) &#123;</span><br> <span style="background-color:#ffffff">        return new DataflowJobExecutor((DataflowJob) elasticJob, jobFacade);</span><br> <span style="background-color:#ffffff">    &#125;</span><br> <span style="background-color:#ffffff">    throw new JobConfigurationException("Cannot support job type '%s'", elasticJob.getClass().getCanonicalName());</span><br> <span style="background-color:#ffffff">&#125;</span></span></p> 
</blockquote> 
<p><span style="color:#000000">在 ElasticJob 3.0.0，作业执行器经过重新设计，分为 Classed 与 Typed 两类。需要编写作业逻辑的 Simple、Dataflow 作业属于 Classed 类型作业，通过配置执行的 Script、HTTP 作业属于 Typed 类型作业。</span></p> 
<p style="text-align:center"><img height="347" src="https://oscimg.oschina.net/oscnet/up-07ea0bfff15c4d24e556c461d03c442f1f0.png" width="1080" referrerpolicy="no-referrer"></p> 
<p>基于这种设计，开发者只需要三个步骤就可以自行扩展更贴合业务场景的 Class 类型作业执行器。</p> 
<p><strong>举个例子：</strong></p> 
<p><span style="color:#000000">1. 先扩展 ElasticJob 顶层接口定义作业逻辑的执行接口：</span></p> 
<blockquote> 
 <p><span style="color:#955ae7"><span style="background-color:#ffffff">public</span></span><span style="color:#585260"><span style="background-color:#ffffff"> </span></span><span style="color:inherit"><span style="color:#955ae7"><span style="background-color:#ffffff">interface</span></span><span style="background-color:#ffffff"> </span><span style="color:#576ddb"><span style="background-color:#ffffff">BackupJob</span></span><span style="background-color:#ffffff"> </span><span style="color:#955ae7"><span style="background-color:#ffffff">extends</span></span><span style="background-color:#ffffff"> </span><span style="color:#576ddb"><span style="background-color:#ffffff">ElasticJob</span></span><span style="background-color:#ffffff"> </span></span><span style="color:#585260"><span style="background-color:#ffffff">&#123;</span></span><br> <br> <span style="color:#585260"><span style="background-color:#ffffff">    </span></span><span style="color:inherit"><span style="color:#955ae7"><span style="background-color:#ffffff">void</span></span><span style="background-color:#ffffff"> </span><span style="color:#576ddb"><span style="background-color:#ffffff">backup</span></span><span style="color:#aa573c"><span style="background-color:#ffffff">(Collection<AvailableData> availableData)</span></span><span style="background-color:#ffffff"> </span><span style="color:#955ae7"><span style="background-color:#ffffff">throws</span></span><span style="background-color:#ffffff"> IOException</span></span><span style="color:#585260"><span style="background-color:#ffffff">;</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">&#125;</span></span></p> 
</blockquote> 
<p><span style="color:#000000">2. 然后实现一个 ClassedJobItemExecutor<BackupJob> 命名为 MyBackupJobExecutor：</span></p> 
<blockquote> 
 <p><span style="color:#955ae7">public</span> <span style="color:inherit"><span style="color:#955ae7">class</span> <span style="color:#576ddb">MyBackupJobExecutor</span> <span style="color:#955ae7">implements</span> <span style="color:#576ddb">ClassedJobItemExecutor</span><<span style="color:#576ddb">BackupJob</span>> </span>&#123;<br> <br>     <span style="color:#aa573c">@SneakyThrows</span><br>     <span style="color:#aa573c"><a href="https://my.oschina.net/u/1162528" target="_blank">@Override</a></span><br>     <span style="color:inherit"><span style="color:#955ae7">public</span> <span style="color:#955ae7">void</span> <span style="color:#576ddb">process</span><span style="color:#aa573c">(BackupJob elasticJob, JobConfiguration jobConfig, JobFacade jobFacade, ShardingContext shardingContext)</span> </span>&#123;<br>         Collection<AvailableData> availableData = getAvaiableData(shardingContext);<br>         elasticJob.backup(availableData);<br>     &#125;<br> <br>     <span style="color:#aa573c"><a href="https://my.oschina.net/u/1162528" target="_blank">@Override</a></span><br>     <span style="color:inherit"><span style="color:#955ae7">public</span> Class<BackupJob> <span style="color:#576ddb">getElasticJobClass</span><span style="color:#aa573c">()</span> </span>&#123;<br>         <span style="color:#955ae7">return</span> BackupJob.class;<br>     &#125;</p> 
</blockquote> 
<p style="text-align:start">3. 把自己实现的 MyBackupJobExecutor 通过 Java SPI 的方式声明实现类。</p> 
<p>如果是扩展 Type 类型的作业执行器，只需要进行后面两步。完成了以上步骤，就可以在作业中使用自己定制的作业执行器了。</p> 
<h3><strong><span style="color:#0052ff">二、作业调度方式多元化</span></strong></h3> 
<p><span style="color:#0052ff">全新引入的“一次性调度”让 ElasticJob Lite 的作业调度不再局限于“定时”。</span>原本基于 Cron 表达式调度的方式重构为 ScheduleJobBootstrap，OneOffJobBootstrap 是 ElasticJob 3.0.0 新增的调度方式。</p> 
<p style="text-align:center"><img height="300" src="https://oscimg.oschina.net/oscnet/up-70d0c5224d988652401a99ec15642ee350c.png" width="1012" referrerpolicy="no-referrer"></p> 
<p>使用 ElasticJob 2.x 时，如果要实现一个能够自由触发的作业，需要经过以下步骤：</p> 
<p style="text-align:justify"><span style="color:#000000">1. 创建一个短时间内不会触发的作业，例如设置 Cron 表达式为</span><span style="color:#0052ff"> <span style="background-color:#f8f8f8; color:#0074ff !important">59 59 23 31 12 ? 2099</span></span><span style="color:#000000">；</span></p> 
<p style="text-align:justify"><span style="color:#000000">2. 在项目中引入</span> <span style="background-color:#f8f8f8; color:#0052ff">elasticjob-lite-lifecycle</span> <span style="color:#000000">模块依赖；</span></p> 
<p style="text-align:justify"><span style="color:#000000">3. 创建一个</span> <span style="background-color:#f8f8f8; color:#0052ff">JobOperationAPI</span> <span style="color:#000000">的实例；</span></p> 
<p style="text-align:justify"><span style="color:#000000">4. 调用 </span><span style="color:#0052ff"><span style="background-color:#f8f8f8; color:#0074ff !important">JobOperationAPI</span> </span><span style="color:#000000">的</span> <span style="background-color:#f8f8f8; color:#0052ff">trigger</span> <span style="color:#000000">方法。</span></p> 
<p>在 ElasticJob 3.0.0 可以这么操作：</p> 
<blockquote> 
 <p><span style="color:#585260"><span style="background-color:#ffffff">OneOffJobBootstrap job = </span></span><span style="color:#955ae7"><span style="background-color:#ffffff">new</span></span><span style="color:#585260"><span style="background-color:#ffffff"> OneOffJobBootstrap(regCenter, elasticjob, jobConfig);</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">job.</span></span><span style="color:#955ae7"><span style="background-color:#ffffff">execute</span></span><span style="color:#585260"><span style="background-color:#ffffff">();</span></span></p> 
</blockquote> 
<p><span style="color:null">无论是操作复杂度还是代码优雅性，新的 API 都更胜一筹。新的调度方式将为 ElasticJob 的应用增加更多的可能性。</span></p> 
<h3><strong><span style="color:#0052ff">三、微内核 & 生态分离</span></strong></h3> 
<p>作业错误处理器、执行轨迹追踪等可扩展模块从内核模块完全抽离，<span style="color:#0052ff">全新的 API 结合 SPI 机制，让开发者可以灵活扩展各个模块的功能，促成 ElasticJob 生态对接。</span></p> 
<p><span style="color:#0052ff">在 3.0.0 版本中，作业错误处理器预置了企业微信、钉钉、邮件 3 种通知渠道。</span></p> 
<p style="text-align:center"><img height="735" src="https://oscimg.oschina.net/oscnet/up-98eb3d864ad5e9e469f75f628c499baf0e8.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><span style="color:null">执行轨迹追踪模块数据源不再局限于 MySQL，现已支持 PostgreSQL、Oracle、H2、DB2、SQLServer 以及其他遵循 SQL92 标准的数据库。</span></p> 
<p> </p> 
<p style="text-align:center"><img height="872" src="https://oscimg.oschina.net/oscnet/up-50ec21ba4ea4e39d6d37303f4cc9f63a85e.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><span style="color:#0052ff">值得一提的是，以上提到的 ElasticJob 3.0.0 生态扩充的内容，均是由社区的同学们贡献的。</span></p> 
<h3><strong><span style="color:#0052ff">四、ElasticJob Lite 提供官方的 Spring Boot Starter</span></strong></h3> 
<p>Spring 应用引入 ElasticJob Lite 时可以不再编写繁琐的 XML 文件了。新版本提供了全新的 Spring Boot Starter，在项目中使用 ElasticJob 定时调度只需两个步骤。</p> 
<p style="text-align:justify"><span style="color:#000000">1. 在作业逻辑的类上加上 </span><span style="color:#0052ff"><span style="background-color:#f8f8f8; color:#0074ff !important"><a href="https://my.oschina.net/u/3907912" target="_blank">@Component</a></span> </span><span style="color:#000000">注解：</span></p> 
<blockquote> 
 <p style="text-align:justify"><span style="color:#aa573c"><a href="https://my.oschina.net/u/3907912" target="_blank"><span style="background-color:#ffffff">@Component</span></a></span><br> <span style="color:#955ae7"><span style="background-color:#ffffff">public</span></span><span style="color:#585260"><span style="background-color:#ffffff"> </span></span><span style="color:inherit"><span style="color:#955ae7"><span style="background-color:#ffffff">class</span></span><span style="background-color:#ffffff"> </span><span style="color:#576ddb"><span style="background-color:#ffffff">DataRefreshJob</span></span><span style="background-color:#ffffff"> </span><span style="color:#955ae7"><span style="background-color:#ffffff">implements</span></span><span style="background-color:#ffffff"> </span><span style="color:#576ddb"><span style="background-color:#ffffff">SimpleJob</span></span><span style="background-color:#ffffff"> </span></span><span style="color:#585260"><span style="background-color:#ffffff">&#123;</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">    </span></span><span style="color:#aa573c"><span style="background-color:#ffffff">@Override</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">    </span></span><span style="color:inherit"><span style="color:#955ae7"><span style="background-color:#ffffff">public</span></span><span style="background-color:#ffffff"> </span><span style="color:#955ae7"><span style="background-color:#ffffff">void</span></span><span style="background-color:#ffffff"> </span><span style="color:#576ddb"><span style="background-color:#ffffff">execute</span></span><span style="color:#aa573c"><span style="background-color:#ffffff">(</span><span style="color:#955ae7"><span style="background-color:#ffffff">final</span></span><span style="background-color:#ffffff"> ShardingContext shardingContext)</span></span><span style="background-color:#ffffff"> </span></span><span style="color:#585260"><span style="background-color:#ffffff">&#123;</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">        </span></span><span style="color:#655f6d"><span style="background-color:#ffffff">// Do something here</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">    &#125;</span></span><br> <span style="color:#585260"><span style="background-color:#ffffff">&#125;</span></span></p> 
</blockquote> 
<p><span style="color:#000000"><span style="background-color:#ffffff">2. 在 Spring 配置文件中配置作业：</span></span></p> 
<blockquote> 
 <p>elasticjob:<br>   regCenter:<br>     serverLists: zookeeper0:<span style="color:#aa573c">2181</span>,zookeeper1:<span style="color:#aa573c">2181</span>,zookeeper2:<span style="color:#aa573c">2181</span><br>     <span style="color:#955ae7">namespace</span>: schedule-jobs<br>   jobs:<br>     dataRefreshJob:<br>       elasticJobClass: org.path.<span style="color:#955ae7">to</span>.DataRefreshJob<br>       cron: <span style="color:#aa573c">0</span> <span style="color:#aa573c">0</span> <span style="color:#aa573c">0</span>/<span style="color:#aa573c">6</span> * * ?<br>       shardingTotalCount: <span style="color:#aa573c">3</span><br>       shardingItemParameters: <span style="color:#aa573c">0</span>=Beijing,<span style="color:#aa573c">1</span>=Shanghai,<span style="color:#aa573c">2</span>=Guangzhou</p> 
</blockquote> 
<p>完成以上配置后，ElasticJob 的作业就会随着 Spring Boot 启动了。</p> 
<p>后续版本还将实现基于注解配置作业，提供更多样化的配置方式，更进一步简化配置。</p> 
<h3><strong><span style="color:#0052ff">五、可观测性</span></strong></h3> 
<p>通过 APM，辅以 ElasticJob 的作业执行轨迹追踪模块，<span style="color:#0052ff">以 ElasticJob 调度为起点的作业全链路可以一览无余。</span>后续计划基于 OpenTracing 等方式开发托管在 ElasticJob 仓库的 Agent。</p> 
<p>例如，SkyWalking 实现了支持 ElasticJob 3.x 版本的自动探针。</p> 
<p style="text-align:center"><img height="640" src="https://oscimg.oschina.net/oscnet/up-77ac19bd324c2879dec567e59dd0c74713c.png" width="1080" referrerpolicy="no-referrer"></p> 
<h3><strong><span style="color:#0052ff">六、对多网卡环境的支持更完善</span></strong></h3> 
<p>ElasticJob 在运行过程中会获取当前进程所在环境的 IP 地址，在一些多网卡的环境下，自动获取 IP 地址的逻辑可能会获取到非用户所预期的地址，对管控界面的展示或作业管理对带来一些不便之处。ElasticJob 3.0.0 将允许用户指定优先使用的网卡，使节点信息更符合用户的预期。在后续版本计划支持正则表达式匹配等方式进行网卡的选择。</p> 
<h2><strong>社区</strong></h2> 
<p style="text-align:justify"><span style="color:#000000">自 ShardingSphere ElasticJob 重启以来，有至少 62 位 Contributors（部分 Contributors 邮箱设置不正确没有被统计到）的 653 个 PR 被合并，感谢各位 Contributors！</span></p> 
<p style="text-align:center"><img height="729" src="https://oscimg.oschina.net/oscnet/up-78583c0328473c750b1d721c5fcd4f2f24d.png" width="1080" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            