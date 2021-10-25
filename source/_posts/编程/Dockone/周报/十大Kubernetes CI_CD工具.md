
---
title: '十大Kubernetes CI_CD工具'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7088'
author: Dockone
comments: false
date: 2021-10-25 06:10:16
thumbnail: 'https://picsum.photos/400/300?random=7088'
---

<div>   
<br>Kubernetes也被称为Kube，是一个用于容器调度的开源平台，在动态环境中管理容器的生命周期。<br>
<br>Kubernetes具有可移植、可扩展和可伸缩的特性。当下使用Kubernetes加CI/CD（持续集成/持续交付）已经是非常普遍的组合。<br>
<br>使用CI/CD工具部署云原生应用，能够简化开发和部署的每个阶段。将云原生应用的开发与CI/CD集成，可以使其更加健壮。<br>
<br>与传统的VM交付对比，Kubernetes的持续交付效率更高。在需要更新和变更时，你根本不需要让整个应用先停下来。<br>
<br>基于Kubernetes的CI/CD流水线通常包含4个主要的组件：<br>
<ul><li>版本控制系统Version Control System</li><li>CI系统</li><li>Docker仓库</li><li>Kubernetes集群</li></ul><br>
<br>上述各个部件的协调和自动化能使软件交付做到无缝、连续。<br>
<br>下面就是十大Kubernetes CI/CD工具：<br>
<h4>Helm</h4>Helm是Kubernetes最知名的包装管理器之一。它使用“charts”（图表），chart是Kubernetes包和应用程序需要的任何其他依赖项的定义。当你从命令行调用chart时，Helm为Kubernetes部署创建YAML文件，然后将它们添加到集群中。Helm是开源的，这意味着我们可以为自己的组织下载、更改和使用charts。<br>
<br>Helm最大的优点是，它使复杂应用的部署更具可移植性。Helm还支持自动回滚，并且对开发人员来说更容易理解。但Helm的缺点就是很难搭建和维护。<br>
<h4>Ksonnet和Jsonnet</h4>Ksonnet（构建于JSON模板语言Jsonnet之上的）是一个配置管理工具。它提供了一种打包Kubernetes资源的方法，随后可用于创建部署所需的配置文件。Ksonnet是基于命令行界面的，而Jsonnet作为一种数据模板语言，是用来描述应用程序的。<br>
<br>该工具的优点是，熟悉JSON的开发人员可以轻松使用JSON Net来部署他们的应用程序。然而，使用JSON和使用Jsonnet还是有一些区别的，对于开发人员来说也就存在学习成本。<br>
<h4>Draft</h4>Draft由微软开发的，是一个在Kubernetes上创建基于云的应用的部署工具。当代码经过持续集成后，Draft可以用来生成Docker镜像。还可以使用它来创建Helm图表，生成基于Kubernetes的应用的YAML文件。<br>
<br>该工具的优势在于，可以将其与Helm结合使用，打包并部署应用程序。缺点是它需要大量的配置。<br>
<h4>Jenkins X</h4>Jenkins X是Kubernetes部署中比较流行和强大的CI工具之一。作为一款开源的自动化工具，带有用于CI的内置插件，它由Java编写的。<br>
<br>可以使用Jenkins来持续构建和测试软件项目，这样可以更容易地对项目进行更改。同时，可以使用此工具通过集成大量测试和部署技术来持续交付项目。尽管这是个功能强大的工具，但同时也是比较复杂，容易出错的工具。<br>
<h4>CircleCI</h4>CircleCI是另一个持续集成和交付工具。它是一个基于云的工具，包括一个用于Kubernetes自动部署的API。<br>
<br>由于CircleCI是基于云的，所以不需要专门的服务器。<br>
<br>CircleCI的优势在于，它使用了许多测试方法，如单元测试、集成测试和部署前的功能测试。该工具的缺点是，它缺乏使它成为一个完整CD流水线的所有部件。<br>
<h4>Travis</h4>Travis是一款商业CI工具，这点不像Jenkins。我们可以使用该工具注册、链接代码仓库、构建以及测试应用。还可以将该工具与其他常见的云仓库集成，如Bitbucket和GitHub。<br>
<br>Travis是一个基于云计算的工具，不需要专用服务器。该工具允许我们在不同操作系统、不同机器上进行测试。<br>
<br>Travis对于开源项目是免费的，但是对于商业项目需要订阅，每个企业项目大概69美元/每月。<br>
<h4>GitLab</h4>GitLab是一个基于Web的工具，具有CI/CD流水线的特性。除了CI/CD部署工具外，它还拥有自己的代码库，其中包含wiki、代码审查、问题跟踪。GitLab是一个开源平台，可以毫不费力地在一台服务器上处理近25,000个用户。它还内置自动部署Kubernetes组件，并支持Helm图表。<br>
<h4>Weave Could</h4>Weave Cloud是一个CD工具，可以让你快速监控和管理Docker容器。它还提供了一种快速设置CI/CD流水线和Kubernetes集群的方法。它允许我们以更快的速度启动、更新和回滚来部署应用程序。该工具使用Git作为声明式基础设施和应用的唯一信任来源。<br>
<br>缺点是它需要相当多的配置才能正常工作。<br>
<h4>Spinnaker</h4>Spinnaker是Netflix开发的一款开源工具。它管理流水线和部署工作，也支持Helm图表。它是一个开源的、跨多云的工具，提供了非常高效的持续交付。缺点是，这个工具最初是为了支持VM而不是为Kubernetes构建的，因此设置起来有点复杂。<br>
<h4>Codefresh</h4>Codefresh是一个CD/CD流水线工具，也支持Helm图表。它允许我们使用自己的CI和镜像仓库。它帮助我们构建一个简单但功能强大的CI/CD流水线。它附带了一套广泛的插件，帮助我们集成我们想要的工具。缺点是，第三方工具是用它们的图形用户界面设置的，使得流水线增加了更多的复杂性。同时，Codefresh是一款商业工具，其价格从每月34美元起。<br>
<h4>结论</h4>最近，开发人员对持续集成和持续交付越来越熟悉。如果没有合适的CI/CD流水线，就无法创建新的软件。Kubernetes正在迅速流行起来，所有的工具都在升级以与Kubernetes集成。因此，在上面的文章中，我们试图汇编最流行的Kubernetes CI/CD工具清单。<br>
<br>大家都在使用哪些工具来创建和管理CI/CD流水线？欢迎在评论区留言。<br>
<br><strong>原文连接：<a href="https://medium.com/@asad_5112/top-10-kubernetes-ci-cd-tools-ede05a55ffd0">Top 10 Kubernetes CI/CD Tools</a>（翻译：伊海峰）</strong>
                                
                                                              
</div>
            