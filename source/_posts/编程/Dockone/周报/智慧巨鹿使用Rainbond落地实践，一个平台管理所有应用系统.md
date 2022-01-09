
---
title: '智慧巨鹿使用Rainbond落地实践，一个平台管理所有应用系统'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://tva1.sinaimg.cn/large/008i3skNly1gxox5ylsdqj31h30rj424.jpg'
author: Dockone
comments: false
date: 2022-01-09 05:09:48
thumbnail: 'https://tva1.sinaimg.cn/large/008i3skNly1gxox5ylsdqj31h30rj424.jpg'
---

<div>   
<br><h2>背景</h2>大家好，我是北京数立通科技有限公司的李栋。最近几年，我一直负责“智慧巨鹿”这一智慧城市项目的运行与维护工作。这个项目涉及到10多家供应商开发的 30 多套智慧城市应用的运维管理，使用传统方式进行部署与管理肯定会造成混乱。我们在项目开始之初，就试图借助云原生相关的技术来提高部署与管理效率。<br>
<br><h2>初识 Rainbond</h2>选型的目光，在一开始就落在了基于容器化技术实现的 Kubernetes 和 Docker Swarm 这两个编排工具上。那时候国内应用云原生技术的场景还很少，项目组内的运维工程师们也并不是很擅长容器化等相应技术。为了进一步了解这些编排工具，我发动了工程师们分别去进行调研，当我拿到调研结果时，尴尬的发现光是这些编排工具的安装方式，每个工程师带回来的方案都不一样。云原生的入门门槛之高，出乎我的意料。<br>
<br>退而求其次，我决定引入一款方便工程师们上手的应用管理平台，来代替运维工程师完成和 Kubernetes 等编排工具的复杂交互工作。至此， Rainbond 第一次进入我的视野。<br>
<br><h2>上手 Rainbond</h2>我算是 Rainbond 的老用户了，从 3.X 版本开始就一直在使用它来管理智慧巨鹿项目的所有智慧城市应用。目前，共计有 30 多套智慧城市应用稳定运行于两个 Rainbond 集群中，我们正致力于将智慧城市应用从较老的 3.X 版本 Rainbond 集群迁移至比较新的 5.X 版本 Rainbond 集群中。<br>
<br>回想最初开始使用 Rainbond 时，其易用性给我留下了深刻的印象。我们的工程师不再需要直接面对学习门槛极高的 Kubernetes ，甚至连将智慧城市应用进行容器化的操作流程也不需要关注，Rainbond 自带的源码构建功能直接接手了容器化工作。<br>
<br>经过两年多的运行，Rainbond 的稳定性也令人满意，目前智慧巨鹿项目团队已经完全掌控了这款应用管理平台。<br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1gxox5ylsdqj31h30rj424.jpg" alt="WechatIMG17" referrerpolicy="no-referrer"><br>
<br><h2>最有价值的场景</h2>使用 Rainbond 这几年，我认为给它带来了很多价值点：<br>
<ul><li>稳定性保证</li></ul><br>
<br>真正能够让 Rainbond 在智慧巨鹿项目中扎根的，是它体现出的稳定性，产品本身没有严重的BUG，老版本中的一些小毛病团队也都已经克服。作为一款运行在智慧城市数据中心中的应用管理平台，稳定性的重要程度是要高于其他因素的。在这一点上，Rainbond 表现的很好，即使遭遇了宿主机服务器宕机，应用也可以自动故障迁移、快速恢复。出了问题的宿主机，在问题修复之后，也可以自动重新加入集群。<br>
<ul><li>便捷的图形化管理界面</li></ul><br>
<br>作为智慧城市数据中心的应用管理平台，它辅助我们管理了所有智慧城市应用。借助图形化的界面，运维工程师可以很方便的针对这些应用进行操作，包括启停、编排、伸缩等。由于不必编写复杂的 Yaml 配置文件，也没有命令行交互，智慧巨鹿项目团队的工程师们都得以很快上手。<br>
<ul><li>突出的易用性</li></ul><br>
<br>我认为易用性是 Rainbond 最大的特点。它以应用为核心抽象，围绕应用所设计的诸多功能都十分有用。比如自动伸缩、健康检测等都是非常实用的功能。网关策略的配置也非常友好，操作难度基本为零，绑定域名匹配证书都非常方便。<br>
<br><img src="<a href="https://grstatic.oss-cn-shanghai.aliyuncs.com/images/docs/3.6/micro-service/horizen.png%22" rel="nofollow" target="_blank">https://grstatic.oss-cn-shangh ... ot%3B</a> alt="实例伸缩" style="zoom: 67%;" /><br>
<ul><li>合理的可观测性</li></ul><br>
<br>Rainbond 提供了全面的监控报警系统，无论是计算资源还是上层的应用系统，一旦出现问题都可以很快暴露出来。结合自动化运维能力，问题应用系统可以做到自愈自恢复。而通过观察应用系统访问量和资源消耗情况，可以更合理的进行资源分配工作。<br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1gxvy97d56yj31h60k20ue.jpg" alt="image-20211230164119378" referrerpolicy="no-referrer"><br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1gxvx34pmmej31qg0u0qaj.jpg" alt="image-20211230160050171" referrerpolicy="no-referrer"><br>
<ul><li>补足供应商管理流程</li></ul><br>
<br>智慧城市应用来自于很多不同的供应商，在以往使用传统模式部署与运维时，每一家供应商的套路都不一样。这种不同不仅仅体现在开发语言、技术架构上，也体现在具有各自不同的部署方式与运维管理方式。这可苦了我们的运维管理人员，接手的每一套智慧城市应用的运维管理方式都不一样。<br>
<br>这样的境况在引入 Rainbond 之后好了很多。运维管理团队依靠 Rainbond 建立起一套专门针对外部供应商的准入机制，利用统一的规范管理所有智慧城市应用，极大提高了管理效率，也使得运维管理团队可以在脱离供应商支持的情况下，将智慧城市应用管理的很好。目前的管理模式，是将供应商准入环境与最终生产环境按照团队的方式隔离开，供应商开发人员，仅需要关注业务代码的开发过程，智慧巨鹿运维管理团队，会根据代码将业务上线到生产环境中去。真正落地了开发与生产隔离的管理方式。<br>
<br><img src="https://tva1.sinaimg.cn/large/008i3skNly1guqjpwi6k1j61gp0u0q9g02.jpg" alt="image-20210923142933743" referrerpolicy="no-referrer"><br>
<br><h2>总结</h2>我在智慧巨鹿项目中引入 Rainbond 这款产品已经两年多了，作为应用管理平台，它切实助力到智慧城市应用的日常运维管理工作。目前正处于一个将老版本 Rainbond 集群迁移到新版本的过渡阶段，相信以后还会继续携手 Rainbond 同行。
                                
                                                              
</div>
            