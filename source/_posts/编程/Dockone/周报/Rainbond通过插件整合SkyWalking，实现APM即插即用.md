
---
title: 'Rainbond通过插件整合SkyWalking，实现APM即插即用'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/SkyWalking-Rainbond.png'
author: Dockone
comments: false
date: 2021-12-04 02:26:49
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/SkyWalking-Rainbond.png'
---

<div>   
<br><blockquote><br>作者：张震</blockquote><h3>一. 简介</h3>SkyWalking 是一个开源可观察性平台，用于收集、分析、聚合和可视化来自服务和云原生基础设施的数据。支持分布式追踪、性能指标分析、应用和服务依赖分析等；它是一种现代 APM，专为云原生、基于容器的分布式系统而设计。<br>
<br>本文整合的目标要达成，运行在Rainbond上的应用，通过开启Rainbond的SkyWalking插件，自动对接SkyWalking Server，灵活开启APM，不需要时关闭插件，实现即插即用的APM。<br>
<br><h3>二. 整合架构</h3>SkyWalking对服务进行监控时服需要在被监控服务中启用agent服务，而SkyWalking agent需要配置到应用的启动命令，虽然对应用代码无侵入，但配置过程需要侵入应用。Rainbond通过插件实现对应用的无侵入，将SkyWalking的agent制作成Rainbond的 <a href="https://www.rainbond.com/docs/get-start/concept/plugin?channel=dockone">初始化类型插件</a>，在应用容器启动之前将agent的jar包拷贝到应用容器，应用容器就能加载agent并连接SkyWalking Server，整个过程对应用容器无侵入，且拓展性强。对接其他APM也可以用类似方式，使用用户通过替换插件实现对接不同的APM工具。<br>
<br>下图展示了在Rainbond中使用SkyWalking对应用进行监控的结构<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/SkyWalking-Rainbond.png" alt referrerpolicy="no-referrer"><br>
<br><h3>三. Agent插件实现原理</h3>Rainbond插件体系是相对于Rainbond应用模型的一部分，插件主要用来实现应用容器扩展运维能力。由于运维工具的实现有较大的共性，因此插件本身可以被复用。插件必须绑定到应用容器时才具有运行时状态，用以实现一种运维能力，比如性能分析插件、网络治理插件、初始化类型插件。<br>
<br>具有运行时的插件的运行环境与所绑定的组件从以下几个方面保持一致：<br>
<ul><li><strong>网络空间</strong> 这个一个至关重要的特性，网络空间一致使插件可以对组件网络流量进行旁路监听和拦截，设置组件本地域名解析等。</li><li><strong>存储持久化空间</strong> 这个特性使得插件与组件之间可以通过持久化目录进行文件交换。</li><li><strong>环境变量</strong> 这个特性使得插件可以读取组件的环境变量。</li></ul><br>
<br>SkyWalking与Rainbond融合的过程中，我们使用到了<strong>初始化类型</strong>插件，顾名思义这是一个在应用容器启动前能够进行初始化动作的的插件，其基本原理是利用 Kubernetes 的 <a href="https://kubernetes.io/zh/docs/concepts/workloads/pods/init-containers/">init容器</a> 实现的，Pod能够包含多个容器，应用运行在这些容器里面，同时Pod也能够有一个或者多个先于应用容器启动的init容器，只有init容器运行成功后才会运行应用容器，在Rainbond中开通了该类型插件的组件会在应用容器启动之前运行插件中已定义的任务直至完成。所以只需定义在应用容器启动前，使用初始化类型容器将agent所需数据拷贝至对应目录下，这样后续服务则可以直接使用这些数据。<br>
<br><h3>四. 通过Rainbond一键安装SkyWalking</h3>我们已将SkyWalking制作为应用并发布至应用市场，用户可基于开源应用商店一键安装。<br>
<ol><li>安装 <a href="https://www.rainbond.com/docs/quick-start/quick-install?channel=dockone">Rainbond</a>;</li><li>在开源应用商店搜索SkyWalking，点击安装即可一键安装；</li></ol><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/install.jpg" alt referrerpolicy="no-referrer"><br>
<br>3.安装完成，后续可通过Rainbond管理和运维SkyWalking。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/topology.jpg" alt referrerpolicy="no-referrer"><br>
<br>SkyWalking 服务端在架构上分为四个部分：探针服务、后端服务、存储服务和 UI：<br>
<ul><li><strong>平台后端(oap-server)</strong> 支持数据聚合、分析和流处理，包括跟踪、指标和日志。</li><li><strong>存储(elasticsearch-7.13.4)</strong> 通过开放/可插拔接口存储SkyWalking 数据。支持 ElasticSearch、H2、MySQL、TiDB、InfluxDB。</li><li><strong>UI(skywalking-ui)</strong> 是高度可定制的基于 Web 的界面，允许 SkyWalking 最终用户可视化和管理 SkyWalking 数据。</li><li><strong>探针(agent)</strong> 收集数据并根据 SkyWalking 要求重新格式化数据（不同的探针支持不同的来源）。</li></ul><br>
<br><h3>五. 使用SkyWalking对微服务进行监控</h3><h4>预先准备环境</h4><ul><li>拥有一套被监控服务，本文中示例应用为<a href="https://gitee.com/log4j/pig?_from=gitee_search">Spring Cloud微服务框架 Pig</a>，我们已将<a href="https://store.goodrain.com/markets/rainbond/apps/c6c8cafc79f740c38ffad3264ea10c4a">Spring Cloud-pig</a>制作为应用并发布至应用市场，用户可基于应用市场一键安装。</li></ul><br>
<br><h4>配置服务支持SkyWalking监控</h4><ul><li>部署插件</li></ul><br>
<br>在Rainbond团队界面点击插件后进入插件界面，点击新建插件，创建初始化类型插件<br>
<br>源码地址：<a href="https://github.com/goodrain/skywalking-agent.git" rel="nofollow" target="_blank">https://github.com/goodrain/skywalking-agent.git</a><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/plugin.jpg" alt referrerpolicy="no-referrer"><br>
<br>插件构建成功后即可使用，为pig服务的各组件开通此插件即可。<br>
<ul><li>挂载存储</li></ul><br>
<br>为pig服务的各组件挂载存储，使其与插件共享该存储。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/storage.jpg" alt referrerpolicy="no-referrer"><br>
<br>挂载路径为<code class="prettyprint">/tmp/agent</code>，挂载类型为<strong>共享存储</strong>；该存储为初始化插件及该组件提供共享存储，共享同一份数据。<br>
<ul><li>添加环境变量</li></ul><br>
<br>为pig各组件添加环境变量。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/env.jpg" alt referrerpolicy="no-referrer"><br>
<br>变量解释：<br>
<br>|变量值|简介|<br>
| :---: | :---- |<br>
|-Dskywalking.agent.service_name=** |在SkyWalking UI中展示的服务名|<br>
|-Dskywalking.collector.backend_service=Host:Port|SkyWalking oap-server的访问地址，用来接收skywalking trace数据|<br>
|-javaagent:/tmp/agent/skywalking-agent.jar|指定需要注入的jar包地址|<br>
<br>添加环境变量以后更新组件即可生效。<br>
<ul><li>建立依赖关系</li></ul><br>
<br>将需要监控的各组件建立与SkyWalking oap-server服务的依赖关系，使其能够通过127.0.0.1的地址连接oap-server，具体原理请参考<a href="https://www.rainbond.com/docs/user-manual/component-connection/regist_and_discover?channel=dockone">服务间通信</a>；或者开启oap-server的对外地址，在被监控端填写该地址，则无需建立依赖关系。<br>
<br><h4>访问SkyWalking</h4>访问 skywalking-ui 对外端口，进入可视化界面。<br>
<ul><li>仪表盘</li></ul><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/skywalking-page.png" alt referrerpolicy="no-referrer"><br>
<ul><li>服务调用拓扑图</li></ul><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/practices/skywalking/Service-Topology.jpg" alt referrerpolicy="no-referrer"><br>
<br><h3>六. 总结</h3>基于Rainbond的插件机制与SkyWalking结合，无需改变软件自身运行环境，不需要向项目构建脚本添加逻辑，实现SkyWalking能力即插即用。除此之外，Rainbond的插件机制具有开放性，通过插件机制对应用治理功能进行扩展，例如网络治理类、日志收集类、数据备份类插件，在对原应用逻辑无侵入的情况下，能够通过网络治理类插件对服务的性能进行分析，通过日志插件收集服务日志，对接ELK等日志收集系统；对于数据库等组件而言，使用备份插件对数据进行备份。<br>
<br>----------------<br>
<br><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a>是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/48fe05f5ab3d8cd3ab89e6e084f4cea9.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20211129/48fe05f5ab3d8cd3ab89e6e084f4cea9.gif" class="img-polaroid" title="公众号二维码.gif" alt="公众号二维码.gif" referrerpolicy="no-referrer"></a>
</div>

                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            