
---
title: 'Qunar 容器化落地过程踩过的那些坑'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/8a79f596ade05a59bd6f458769e49b7f.png'
author: Dockone
comments: false
date: 2021-06-17 13:20:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/8a79f596ade05a59bd6f458769e49b7f.png'
---

<div>   
<br><h3>背景</h3>近几年，容器技术非常火爆，且日趋成熟，众多企业慢慢开始容器化建设，并在云原生技术方向上不断的探索和实践。基于这个大的趋势， 2020 年底 Qunar 也向云原生迈出了第一步——容器化。为了完成容器化这个目标，我们基础平台、TCDEV、Ops、数据组、业务线等多个团队一起协作配合，终于在公司内部把容器化成功落地。截止到今年六月初，我们生产环境已经接入了 150 多个应用，其余应用也在陆续接入中，这个成果还是蛮让人惊喜的。回顾整个容器化落地过程其实有不少技术难点的，在这篇文章中我会分享下我们遇到的几个问题和解决思路，希望对还在云原生路上探索的同学有些借鉴意义。<br>
<h3>容器化方案架构简介</h3>Qunar 在做容器化过程中，各个系统 Portal 平台、中间件、Ops 基础设施、监控等都做了相应的适配改造，改造后的架构矩阵如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/8a79f596ade05a59bd6f458769e49b7f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/8a79f596ade05a59bd6f458769e49b7f.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>Portal</strong>：Qunar 的 PaaS 平台入口，提供 CI/CD 能力、资源管理、自助运维、应用画像、应用授权（db 授权、支付授权、应用间授权）等功能</li><li><strong>运维工具</strong>：提供应用的可观测性工具, 包括 Watcher（监控和报警）、Bistoury（Java 应用在线 debug）、QTrace（Tracing 系统）、Loki/ELK（提供实时日志/离线日志查看）</li><li><strong>中间件</strong>：应用用到的所有中间件，MQ、配置中心、分布式调度系统 QSchedule、Dubbo 、MySQL SDK等  </li><li><strong>虚拟化集群</strong>：底层的 Kubernetes 和 OpenStack 集群  </li><li><strong>Noah</strong>：测试环境管理平台，支持应用 KVM/容器混合部署  </li></ul><br>
<br>在 Portal PaaS 平台中，一个应用的容器发布流具体程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/0fb6ab8893f0c3061e17a12818ae74da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/0fb6ab8893f0c3061e17a12818ae74da.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>容器化落地过程中碰到的问题</h3><h4>如何兼容过去 KVM 的使用方式，并支持 preStart、preOnline hook 自定义脚本</h4>KVM 场景中 hook 脚本使用场景介绍：<br>
<ul><li><strong>preStart hook</strong>：用户在这个脚本中会自定义命令，比如环境准备</li><li><strong>preOnline hook</strong>：用户会定义一些数据预热操作等，这个动作需要在应用 checkurl 通过并且接入流量前执行</li></ul><br>
<br>问题点：Kubernetes 原生只提供了 preStop、postStart 2 种 hook，它们的执行时机没有满足上述 2 个 KVM 场景下业务用到的 hook。<br>
<br>分析与解决过程：<br>
<ul><li><strong>preStart hook</strong>：在 ENTRYPOINT 中注入 preStart hook 阶段，容器启动过程中发现有自定义的 preStart 脚本则执行该脚本，至于这个脚本的位置目前规范是定义在代码指定目录下</li><li><strong>preOnline hook</strong>：由于 preOnline 脚本执行时机是在应用 checkurl 通过后，而应用容器是单进程，所以在应用容器中执行这个是行不通的。而 postStart hook 的设计就是异步的，和应用容器的启动是解耦的， 所以我们初步的方案选择了 postStart hook 中这个事情。实施方案是 postStart hook执行后会不断轮询应用的健康状态，如果健康检测 checkurl 通过了, 则执行 preOnline 脚本。脚本成功后则进行上线操作，即在应用目录下创建 healthcheck.html 文件，OpenResty 和中间件发现这个文件后就会把流量接入到这个实例中</li></ul><br>
<br>按照上面的方案，Pod 的组成设计如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/3aff37af92d66bda51f28d9bb2966b65.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/3aff37af92d66bda51f28d9bb2966b65.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>发布过程缺少日志 定位问题困难</h4>场景介绍：在容器发布过程中如果应用启动失败，我们通过 Kubernetes API 是拿不到实时的标准输入输出流，只能等到发布设置的超时阈值，这个过程中发布人员心里是很焦急的，因为不确定发生了什么。如下图所示，部署过程中应用的更新工作流中什么都看不到。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/86e508cf8e5a808c8833af490d4d584a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/86e508cf8e5a808c8833af490d4d584a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
问题点：Kubernetes API 为什么拿不到标准输入输出。<br>
<br>分析与解决过程：<br>
<ul><li>通过 kubectl logs 查看当时的 Pod 日志，什么都没有拿到，超时时间过后才拿到。说明问题不在程序本身，而是在 Kubernetes 的机制上；</li><li>查看 postStart Hook 的相关文档，有一段介绍提到了 postHook 如果执行时间长或者 hang 住，容器的状态也会hang 住，不会进入 running 状态, 看到这条信息，大概猜测到罪魁祸首就是这个 postStart hook 了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/6d746224d3cab2e1468fa92cadcecab0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/6d746224d3cab2e1468fa92cadcecab0.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br>基于上面的猜测，把 postStart hook 去掉后测试，应用容器的标准输入可以实时拿到了。<br>
<ul><li>找到问题后，解决方法也就简单了，把 postStart hook 中实现的功能放到 sidecar 中就可以解决。至于 Sidecar 如何在应用容器的目录中创建 healthcheck.html 文件，就需要用到共享卷了。新的方案设计如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/2af9e2746a30cf1c6d0474b19fa00a08.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/2af9e2746a30cf1c6d0474b19fa00a08.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>使用上述方案后，发布流程的标准输入输出、自定义 hook 脚本的输出、pod 事件等都是实时可见的了, 发布过程更透明了。</li></ul><br>
<br><h4>Java 应用在容器场景下如何支持远程 debug</h4>KVM 场景 debug 介绍：在开发 Java 应用的过程中，通过远程 debug 可以快速排查定位问题，因此是开发人员必不可少的一个功能。<br>
<br>debug 具体流程：开发人员在 Noah 环境管理平台的界面点击开启 debug，Noah 会自动为该 Java 应用配置上 debug 选项，-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=127.0.0.1:50005，并重启该 Java 应用，之后开发人员就可以在 IDE 中配置远程 debug 并进入调试模式了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/de46830d2f00581a6fb6e2a01e2884e9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/de46830d2f00581a6fb6e2a01e2884e9.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
容器场景的 debug方案：测试环境的 Java 应用默认开启 debug 模式，这样也避免了更改 debug 重建 Pod 的过程，速度从 KVM 的分钟级到现在的秒级。当用户想开启 debug 时，Noah 会调用 Kubernetes exec 接口执行 socat 相关命令进行端口映射转发，让开发人员可以通过 socat 开的代理连接到 java 应用的 debug 端口。<br>
<br>问题点：容器场景下在用户 debug 过程中，当请求走到了设置的断点后，debug 功能失效。<br>
<br>分析与解决过程：<br>
<ul><li>复现容器场景下 debug，观察该 Pod 的各项指标，发现 debug 功能失效的时候系统收到了一个 Liveness probe failed，kill Pod 的事件。根据这个事件可以判断出当时 Liveness check 失败，应用容器 才被 kill 的，应用容器重启代理进程也就随之消失了， debug 也就失效了。</li><li>关于 debug 过程 checkurl 为什么失败的问题，特地找了 TCDEV 的同学咨询了下，得到的答案是 debug 时当请求走到断点时，整个 JVM 是 hang 住的，这个时候任何请求过来也会被 hang 住，当然也包括 checkurl，于是我们也特地在 KVM 场景和容器场景分布做了测试，结果也确实是这样的。</li><li>其他同事也提了个临时解决方案，把断点的阻断级别改为线程级的，这样就不会阻断 checkurl 了，IDEA 中默认的选项是 Suspend All，改为 Suspend Thread 即可。不过这个也不是最优解，因为这个需要用户手工配置阻断级别，有认知学习成本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/a9868d98934cce083860bf59813c2f85.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/a9868d98934cce083860bf59813c2f85.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>回到最初的问题上，为什么容器场景下遇到这个问题， 而 KVM 没有，主要是因为容器场景 Kubernetes 提供了自愈能力，Kubernetes 会定时执行 Liveness check，当失败次数达到指定的阈值时 Kubernetes 会 kill 掉容器并重新拉起一个新的容器。</li><li>那我们只好从 Kubernetes 的 Liveness 探针上着手了，探针默认支持 exec、TCP 、HttpGet 3种模式， 当前使用的是 HttpGet，这种方式只支持一个 url，无法满足这个场景需求。经过组内讨论， 最后大家决定用这个表达式 ( checkurl == 200) || (socat process && java process alive) 在作为应用的 Liveness 检测方式，当 debug 走到断点的时候, 应用容器就不会阻断了， 完美的解决了这个问题。</li></ul><br>
<br><h4>多集群方案 Rancher 2.5 可能存在性能问题</h4>Rancher 使用场景介绍：最初我们是采用的 Rancher 作为多集群管理方案，主要是因为 Rancher 代码开源，对运维友好、可以统一入口等优点。我们使用的方式是每个应用单独一个 namespace , 这样方便资源隔离和权限设置。<br>
<br>问题点：随着接入应用的数量增多，Rancher 接口性能越来越慢，当 namespace 数量达到 3000 后，几个查询请求之间把 Rancher 服务打挂了。（可能我们使用有误？欢迎指正）<br>
<br>分析与解决：Ops 同学通过查看代码和资料分析确认这个是 Rancher 的 bug，并且短时间也没计划修复。后来 Ops 调研并对比了其他的多集群方案 KubeFed，KubeSphere 等，最终选择了 KubeSphere 作为集群方案。迁移到 KubeSphere 后就没有这些性能问题了。<br>
<br>最初我们是采用的 Rancher 作为多集群管理方案，主要是因为 Rancher 代码开源，对运维友好、可以统一入口等优点。我们使用的方式是每个应用单独一个 namespace，这样方便资源隔离和权限设置。<br>
<h3>总结与展望</h3><h4>总结</h4>以上就是我们落地容器化过程中遇到的几个问题与解决思路， 其中从 KVM 迁移到容器需要考虑用户使用习惯还有历史功能等因素，兼容和适配是难免的，总是要做取舍的。我们的云原生之路的探索刚刚迈出一小步，任重而道远，后续我们会持续关注云原生最新的技术趋势和最佳实践，并在我们 Qunar PaaS 平台落地，同时也会把我们遇到的一些问题分享出来，避免大家踩同样的坑。<br>
<h4>展望</h4><ul><li>集群稳定性治理，为了保障业务应用在 Kubernetes 集群的稳定运行，我们会关注更多的集群稳定性指标并做好闭环处理，同时也探索和落地混沌工程在容器场景下的实践</li><li>提高资源利用率，目前业内某些大厂的 Kubernetes 集群资源利用率达到了 60%，我们目前离这个目标还有很大距离，下个阶段我们会在资源动态压缩、节点资源动态超卖等方向做探索和实践</li></ul><br>
<br>作者：邹晟，2017 年加入 Qunar，目前在基础平台做 Portal PaaS 平台的运维和开发，近期一直在做容器化落地方面的工作。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/5bEORRFZqGFnKZShtxWxJA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/5bEORRFZqGFnKZShtxWxJA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            