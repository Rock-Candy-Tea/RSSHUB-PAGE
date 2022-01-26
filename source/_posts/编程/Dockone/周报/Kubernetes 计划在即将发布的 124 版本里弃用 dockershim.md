
---
title: 'Kubernetes 计划在即将发布的 1.24 版本里弃用 dockershim'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220122/5c82e2e49918b2012afab0cf7bf1e283.jpeg'
author: Dockone
comments: false
date: 2022-01-26 13:12:27
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220122/5c82e2e49918b2012afab0cf7bf1e283.jpeg'
---

<div>   
<br>【编者的话】Kubernetes 计划在即将发布的 1.24 版本里弃用并移除 dockershim。<br>
<br>Kubernetes 计划在<a href="https://kubernetes.io/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/">即将发布的 1.24 版本</a>里弃用并移除 dockershim。使用 Docker 引擎作为其 Kubernetes 集群的容器运行时的工作流或系统需要在升级到 1.24 版本之前进行迁移。1.23 版本将会保留 dockershim，对该版本的支持则会再延长一年。<br>
<br>Docker 是 Kubernetes 使用的第一个容器运行时。最开始对于 Docker 的支持部分被硬编码在 Kubernetes 的代码里，但是随着项目的发展，Kubernetes 开始添加更多的运行时支持。Kubernetes 社区决定转向更加结构化和标准化的接口，而不是直接把第三方的解决方案集成到核心代码里。这就有了<a href="https://github.com/kubernetes/cri-api">容器运行时接口（CRI）</a>，<a href="https://github.com/containernetworking/cni">容器网络接口（CNI）</a>以及<a href="https://github.com/container-storage-interface/spec">容器存储接口（CSI）</a>这些标准。<br>
<br>正如 Mirantis 的 CTO <a href="https://www.linkedin.com/in/adamparco/">Adam Parco</a> <a href="https://www.mirantis.com/blog/mirantis-to-take-over-support-of-kubernetes-dockershim-2/">所说</a>：<br>
<br><blockquote><br>对于大多数人来说，弃用 dockershim 不是什么问题，因为他们甚至可能都感觉不到，他们实际上并没有使用 Docker 本身，他们用的是符合 CRI 标准的 containerd。对于那些人来说，这跟之前没什么两样。</blockquote>由于 Docker 不符合 CRI 标准，dockershim 更多充当的是 kubelet 和 Docker 之间的一个翻译层。然后 Docker 再通过接口形式调用 containerd 来执行容器。containerd 之前是作为一个自包含的容器运行时从 Docker 项目里提取出来，随后它便成为第一个符合 CRI 标准的运行时。可以看到，弃用 dockershim 以后 kubelet 便可以和 containerd 这样的容器运行时直接通信。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220122/5c82e2e49918b2012afab0cf7bf1e283.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220122/5c82e2e49918b2012afab0cf7bf1e283.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>分别采用 containerd 和 dockershim 的 Kubernetes 工作流对比（来源: <a href="https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-deprecation-affects-you/">Kubernetes</a>）</em><br>
<br>正如 Kubernetes 博客上<a href="https://kubernetes.io/blog/2020/12/02/dockershim-faq/">最近的一篇文章</a>所提到的，从 dockershim 迁移出去是为了让 Kubernetes 的代码库能够更好地和新的接口模型保持一致。一些新开发的功能，比如 cgroups v2 还有用户命名空间，它们和 dockershim 在很大程度上是不兼容的。正如最近这篇<a href="https://kubernetes.io/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/">博客文章</a>的作者所说：“对 Docker 和 dockershim 的依赖已经渗透到 CNCF 生态系统的各种工具和项目里，这会导致我们的代码变得更加脆弱。”<br>
<br>如果你当前使用的是 Docker 来构建应用容器的话，那这些容器仍然可以在其他的容器运行时上运行。但是一旦使用替代的容器运行时，Docker 的一些命令可能就不起作用了或者会产生不同的结果。举个例子，<code class="prettyprint">docker ps</code> 或者 <code class="prettyprint">docker inspect</code> 无法再获取容器的信息了，<code class="prettyprint">docker exec</code> 也不工作了。<br>
<br>在<a href="https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-deprecation-affects-you/">梳理对 dockershim 的依赖</a>的时候还有一些额外的注意事项，这包括需要确保没有用到特权 Pod 来执行一些 Docker 命令，比如 <code class="prettyprint">docker ps</code>，重启 Docker service，或者是修改 Docker 的一些特定文件。我们还需要留意一下 Docker 配置文件里有没有私有镜像仓库或者镜像同步源的设置。如果有的话，其他运行时也需要重新配置一下这些设置。<br>
<br>我们还应该检查跑在 Kubernetes 基础设施之外的一些脚本，识别出用到 Docker 命令的部分。这也许包括 SSH 到机器上排障，节点的启动脚本，又或者是直接装在节点上的一些<a href="https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/">监控和安全客户端</a>。<br>
<br>Mirantis 和 Docker 已经达成一致，他们将会共同维护 dockershim 的代码，后续它将作为一个相对于 Kubernetes 而言更加独立、<a href="https://github.com/Mirantis/cri-dockerd">开源</a>并且符合 CRI 接口的项目存在。这意味着 Mirantis 容器运行时（MCR）将会是符合 CRI 标准的运行时。如果遇到不希望或者不能接受 dockershim 下线的情况，他们的 <a href="https://github.com/Mirantis/cri-dockerd">cri-dockerd</a> 将可以用作 dockershim 的一个外部替代品。<br>
<br>Kubernetes 1.24 版本的发布团队和 CNCF 已经承诺了将会及时提供此次发布相关的文档，目前计划是在 4 月份。这里面包含了博客文章，更新代码示例，教程，以及一份迁移指南。<br>
<br>该团队认为，继续进行迁移已经不存在任何主要障碍。他们确实有注意到，最近的 11 月 11 日 <a href="https://docs.google.com/document/d/1Ne57gvidMEWXR70OxxnRkYquAoMpt56o75oZtg-OeBg/edit#bookmark=id.r77y11bgzid">SIG Node 兴趣小组</a>以及 12 月 6 日 <a href="https://docs.google.com/document/d/1qazwMIHGeF3iUh5xMJIJ6PDr-S3bNkT8tNLRkSiOkOU/edit#bookmark=id.m0ir406av7jx">Kubernetes 指导委员会</a>会议上有关推迟弃用 dockershim 的讨论。然而，此时他们已经同意继续推进在即将发布的 1.24 版本里移除 dockershim 的工作。<br>
<br><strong>原文链接：<a href="https://www.infoq.com/news/2022/01/kubernetes-dockershim-removal/">Kubernetes Proceeding with Deprecation of Dockershim in Upcoming 1.24 Release</a>（翻译：吴佳兴)</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            