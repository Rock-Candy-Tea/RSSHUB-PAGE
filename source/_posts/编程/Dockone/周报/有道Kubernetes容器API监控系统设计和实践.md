
---
title: '有道Kubernetes容器API监控系统设计和实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/4c54fed46e9376bc4de1ee9c30a3f078.png'
author: Dockone
comments: false
date: 2021-06-01 12:38:29
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/4c54fed46e9376bc4de1ee9c30a3f078.png'
---

<div>   
<br>【编者的话】本篇文章将分享有道容器服务API监控方案，这个方案同时具有轻量级和灵活性的特点，很好地体现了Kubernetes集群化管理的优势，解决了静态配置的监控不满足容器服务监控的需求。并做了易用性和误报消减、可视化面板等一系列优化，目前已经超过80%的容器服务已经接入了该监控系统。<br>
<h3>背景</h3>Kubernetes 已经成为事实上的编排平台的领导者、下一代分布式架构的代表，其在自动化部署、监控、扩展性、以及管理容器化的应用中已经体现出独特的优势。<br>
<br>在Kubernetes容器相关的监控上， 我们主要做了几块工作，分别是基于Prometheus的Node、Pod、Kubernetes资源对象监控，容器服务API监控以及基于Grafana的业务流量等指标监控。<br>
<br>在物理机时代，我们做了分级的接口功能监控——域名级别接口监控和机器级别监控，以便在某个机器出现问题时，我们就能快速发现问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/4c54fed46e9376bc4de1ee9c30a3f078.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/4c54fed46e9376bc4de1ee9c30a3f078.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图中，左边是物理机时代对应的功能监控，包括域名级别接口监控和3台物理机器监控。右边是对应的Kubernetes环境，一个Service的流量会由Kubernetes负载均衡到pod1，pod2，pod3中，我们分别需要添加的是Service和各个Pod的监控。<br>
<br>由于Kubernetes中的一切资源都是动态的，随着服务版本升级，生成的都是全新的Pod，并且Pod的IP和原来是不一样的。<br>
<br>综上所述，传统的物理机API不能满足容器服务的监控需求，并且物理机功能监控需要手动运维管理，<strong>为此我们期望设计一套适配容器的接口功能监控系统，并且能够高度自动化管理监控信息，实现Pod API自动监控。</strong><br>
<h3>技术选型</h3>为了满足以上需求，我们初期考虑了以下几个方案。<br>
<ol><li>手动维护各个Service和Pod监控到目前物理机使用的PodMonitor开源监控系统。</li><li>重新制定一个包含Kubernetes目录树结构的系统，在这个系统里面看到的所有信息都是最新的， 在这个系统里面，可以做我们的目录树中指定服务的发布、功能监控、测试演练等。</li><li>沿用PodMonitor框架，支持动态获取Kubernetes集群中最新的服务和Pod信息，并更新到监控系统中。</li></ol><br>
<br><h4>方案分析</h4>针对方案一，考虑我们服务上线的频率比较高，并且Kubernetes设计思想便是可随时自动用新生成的Pod（环境）顶替原来不好用的Pod，手动维护Pod监控效率太低，该方案不可行。<br>
<br>第二个方案应该是比较系统的解决办法，但需要的工作量会比较大，这种思路基本全自己开发，不能很好的利用已有的功能监控系统，迁移成本大。<br>
<br><strong>于是我们选择了方案三</strong>，既能兼容我们物理机的接口功能监控方案，又能动态生成和维护pod监控。<br>
<h3>整体设计思路</h3>Kubernetes监控包括以下几个部分：  其中API功能监控，是我们保证业务功能正确性的重要监控手段。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/d999ead3b85c2b94cd60d260cbdf2119.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/d999ead3b85c2b94cd60d260cbdf2119.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通常业务监控系统都会包含监控配置、数据存储、信息展示，告警这几个模块，我们的API功能监控系统也不例外。<br>
<br>我们沿用API Monitor框架功能，并结合了容器服务功能监控特点，和已有的告警体系，形成了我们容器API功能监控系统结构： <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/a4eb3856634f256c878da3da9c89cf14.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/a4eb3856634f256c878da3da9c89cf14.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
首先介绍下目前我们物理机使用的API Monitor监控：一个开源的框架 <a href="https://gitee.com/ecar_team/apimonitor" rel="nofollow" target="_blank">https://gitee.com/ecar_team/apimonitor</a><br>
<br>可以模拟探测http接口、http页面，通过请求耗时和响应结果来判断系统接口的可用性和正确性。支持单个API和多个API调用链的探测。<br>
<br>如下图所示，第一行监控里面监控的是图片翻译服务域名的地址，后边的是各台物理机的IP：端口。 <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/84452810ca140d55b3a91fa0481fcc48.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/84452810ca140d55b3a91fa0481fcc48.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
点开每条监控 ：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/9ccd583ac47a6d0c3018f4d94a716c1a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/9ccd583ac47a6d0c3018f4d94a716c1a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们沿用API Monitor框架的大部分功能，其中主要的适配和优化包括：<br>
<ol><li>监控配置和存储部分：一是制定容器服务Service级别监控命名规则：集群.项目.命名空间.服务；（和Kubernetes集群目录树保持一致，方便根据Service生成Pod监控），二是根据Service监控和Kubernetes集群信息动态生成Pod级别监控</li><li>监控执行调度器部分不用改动</li><li>信息展示部分，增加了趋势图和错误汇总图表</li><li>告警部分，和其它告警使用统一告警组。</li></ol><br>
<br><h3>具体实践操作</h3><h4>添加Service级别API监控告警</h4>需要为待监控服务，配置一个固定的容Service级别监控。<br>
<br>Service级别监控命名规则：集群.项目.命名空间.服务。<br>
<br>以词典查词服务为例，我们配置一条Service级别的多API监控（也可以是单API监控）。<br>
<ul><li>单API：一个服务只需要加一条case用</li><li>多API：如果一个服务需要加多条功能case </li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/bd05ed80fd0b4afe156bdc08d8cca256.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/bd05ed80fd0b4afe156bdc08d8cca256.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其中“所属系统”是服务所属的告警组，支持电话、短信、popo群、邮件等告警方式（和其它监控告警通用）。<br>
<br>任务名称：取名规则，Rancher中<strong>Kubernetes集群名字.项目名字.命名空间名字.service名字</strong>（一共四段）。<br>
<br>告警消息的字段含义：<br>
<ul><li>docker-dict：告警组，订阅后会收到告警消息</li><li>k8s-prod-th：集群</li><li>dict：项目</li><li>dict：命名空间</li><li>data-server：workload名字</li><li>data-server-5b7d996f94-sfjwn：Pod名字</li><li>&#123;&#125;：接口返回内容，即：response.content</li><li><a href="http://dockermonitor.xxx.youdao.com/monitorLog?guid=61bbe71eadf849558344ad57d843409c&name=k8s-prod-th.dict.dict.data-server.data-server-5b7d996f94-sfjwn" rel="nofollow" target="_blank">http://dockermonitor.xxx.youda ... sfjwn</a>：告警详细链接</li></ul><br>
<br><h4>自动生成Pod API监控</h4>自动生成下面三行监控任务：（第一行监控是按上面方法配置的容器Service IP监控，后边三行是自动生成Pod监控任务 ）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/c710eb58326ce4e4903610d554193e9b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/c710eb58326ce4e4903610d554193e9b.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
监控Service级别是单API，则自动生成的是单API，Service级别是多API，则自动生成的是多API监控。<br>
<br>自动生成的Pod级别监控，除了最后两行标红处（ip: port）和Service级别不一样，其他都一样。 <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/691af712d1d55836a872628bc00d90f3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/691af712d1d55836a872628bc00d90f3.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
实现Pod自动生成的方法：<br>
<ol><li>给Pod Monitor（改框架是Java语言编写的），增加一个Java模块，用来同步Kubernetes信息到Pod Monitor中。考虑到修改Pod Monitor中数据这个行为，本身是可以独立于框架的，可以不修改框架任何一行代码就能实现数据动态更新。</li><li>对比Pod Monitor数据库和Kubernetes集群中的信息，不一致的数据，通过增删改查DB，增加Pod的监控。由于数据之间存在关联性，有些任务添加完没有例行运行，故采用了方法三。</li><li>对比Pod Monitor数据库和Kubernetes集群中的信息，不一致的数据，通过调用Pod Monitor内部接口添加/删除一项监控，然后调接口enable /disable job等。按照可操作性难易， 我们选择了方法三。</li></ol><br>
<br>针对于Kubernetes集群中查到的一条Pod信息，总共有三种情况：<br>
<ol><li>对于表中存在要插入Pod的监控信息记录，并且enable状态为1。则认为该Pod的监控不需要改变</li><li>对于表中存在要插入Pod的监控信息记录（删除操作并不会删除源数据信息），并且enable状态为0。则认为该Pod的监控已被删除或者被停止。调用删除操作， 清空QRTZ （例行任务插件）表中的响应内容， 调用delete db操作清出监控信息相关表中的内容（使得监控记录不至于一直在增长）</li><li>对于表中不存在Pod相关信息记录， 则需要新增加的一个Pod。调用post创建监控任务接口（根据Service监控配置）， 并调用get请求设置接口为监控enabled状态。</li></ol><br>
<br>另外对于已经在物理机Pod Monitor中添加了监控的服务，提供了一个小脚本，用于导出物理机Pod Monitor域名级别监控到Docker Monitor监控中。<br>
<h3>难点和重点问题解决</h3><h4>误报消减</h4><strong>上线告警抑制</strong><br>
<br>由于服务重启期间，会有removing状态和未ready状态的Pod，在Docker Monitor系统中存在记录，会引起误报。 我们的解决方法是提供一个通用脚本，根据Kubernetes服务的存活检查时间，计算容器服务的发布更新时间，确定再自动开启服务监控的时机。实现在服务重启时间段，停止该服务的接口功能告警；存活检查时间过了之后，自动开启监控。 如下如所示，即Health Check中的Liveness Check检查时间。 <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/b493b2f093b4cd98aaa17e8c496f74da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/b493b2f093b4cd98aaa17e8c496f74da.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在我们上线发布平台上衔接了该告警抑制功能。<br>
<br><strong>弹性扩缩容告警抑制</strong><br>
<br>原来我们通过查询Rancher的API接口得到集群中全量信息，在我们服务越来越多之后， 查询一次全量信息需要的时间越来越长，基本需要5 min左右。在这个过程中，存在docker-monitor和Kubernetes集群中的信息不一致的情况。一开始试图通过按照业务分组，并行调用Rancher接口得到业务Kubernetes集群信息。时间从5 min缩短到1 min多钟。误报有一定的减少， 但从高峰期到低谷期时间段， 仍然会有若干Pod在Kubernetes集群中缩掉了， 但docker-monitor中仍有相应的告警。<br>
<br>在调研了一些方案之后，<strong>我们通过Kubernetes增量事件（如Pod增加、删除）的机制，拿到集群中最新的信息，Pod的任何变更，3s钟之内就能拿到。</strong><br>
<br>通过ES的查询接口，使用filebeat-system索引的日志， 把Pod带有关键字Releasing address using workloadID （更及时），或kube-system索引的日志：Deleted pod: xx delete 。<br>
<br>通过这个方案，已经基本没有误报。<br>
<h4>策略优化</h4>为了适配一些API允许一定的容错率，我们在API Monitor框架中增加了重试策略（单API和多API方式均增加该功能）。<br>
<br>为了适配各类不同业务，允许设置自定义超时时间。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/edb9db1b27e6188898b2d6f5964bad0e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/edb9db1b27e6188898b2d6f5964bad0e.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>易用性</h4>增加复制等功能，打开一个已有的告警配置，修改后点击复制， 则可创建一个新的告警项 使用场景：在多套环境（预发、灰度和全量）监控，以及从一个相似API接口微调得到新API监控。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/a7c519016d36e6d53c457bd589fc2b96.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/a7c519016d36e6d53c457bd589fc2b96.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>5业务适配</h4>精品课对服务的容器化部署中使用了接口映射机制，使用自定义的监听端口来映射源端口，将Service的监听端口作为服务的入口port供外部访问，如下图所示。当Service的监听端口收到请求时，会将请求报文分发到Pod的源端口，因此对Pod级别的监控，需要找到Pod的源端口。 <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/151957eabc8e7946dd6823a69963c79c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/151957eabc8e7946dd6823a69963c79c.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们分析了Rancher提供的服务API文件后发现，在端口的配置信息中，port.containerPort为服务的监听端口，port.sourcePort为Pod的监听端口，port.name包含port.containerPo -rt和port.sourcePort的信息，由此找到了Pod的源端口与Service监听端口的关键联系，从而实现了对精品课服务接入本平台的支持。 <br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/fb114a70f89fea9746415dc8cd95c4fc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/fb114a70f89fea9746415dc8cd95c4fc.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>上线效果</h3>1、容器服务API监控统一，形成一定的规范，帮助快速发现和定位问题。<br>
<br>通过该容器API监控系统，拦截的典型线上问题有：<br>
<ul><li>xx上线误操作</li><li>依赖服务xxxlib版本库问题</li><li>DNS server解析问题</li><li>xxx服务OOM问题</li><li>xxx服务堆内存分配不足问题</li><li>xx线上压测问题</li><li>多个业务服务日志写满磁盘问题</li><li>各类功能不可用问题</li><li>……</li></ul><br>
<br>2、同时增加了API延时趋势图标方便评估服务性能：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/68d08d39be850a619e367ee209d3bf97.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/68d08d39be850a619e367ee209d3bf97.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
错误统计表方便排查问题：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210528/717b5c799e6748531e5e1a929a3721ac.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210528/717b5c799e6748531e5e1a929a3721ac.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
结合我们Kubernetes资源对象监控，和Grafana的业务流量等指标监控，线上故障率显著减少，几个业务的容器服务0故障。<br>
<h3>总结与展望</h3><h4>总结</h4>本期文章中我们介绍了基于静态API监控和Kubernetes集群化管理方案，设计了实时的自动容器API监控系统。<br>
<br>通过上述方案，我们能够在业务迁移容器后，很快地从物理机监控迁移到容器监控。统一的监控系统，使得我们线上服务问题暴露更及时、故障率也明显减少<br>
<h4>展望</h4><ol><li>自动同步Kubernetes服务健康检查到docker-monitor系统，保证每一个服务都有监控。</li><li>集成到容器监控大盘中，可以利用大盘中Kubernetes资源目录树，更快查找指定服务，以及关联服务的Grafana指标等监控。</li><li>自动恢复服务，比如在上线指定时间内，发生API监控告警，则自动回滚到上一版本，我们希望监控不仅能发现问题，还能解决问题。</li></ol><br>
<br>监只是手段，控才是目标。<br>
<h3>结语</h3>Docker技术将部署过程代码化和持续集成，能保持跨环境的一致性，在应用开发运维的世界中具有极大的吸引力。<br>
<br>而Kubernetes做了Docker的集群化管理技术，它从诞生时就自带的平台属性，以及良好的架构设计，使得基于Kubernetes容器可以构建起一整套可以解决上述问题的“云原生”技术体系，也降低了我们做持续集成测试、发布、监控、故障演练等统一规划和平台的难度。目前有道业务服务基本都上线到容器，后续我们将陆续迁移基础服务，实现整体的容器化。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/K6UJnnpbhciHyvrACo1xAw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/K6UJnnpbhciHyvrACo1xAw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            