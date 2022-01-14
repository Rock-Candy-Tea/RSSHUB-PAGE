
---
title: 'Podman 和Docker对比'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220114/81a528cca31cca0eb4791067d0077723.jpg'
author: Dockone
comments: false
date: 2022-01-14 09:08:49
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220114/81a528cca31cca0eb4791067d0077723.jpg'
---

<div>   
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220114/81a528cca31cca0eb4791067d0077723.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220114/81a528cca31cca0eb4791067d0077723.jpg" class="img-polaroid" title="podman-vs-docker.jpg" alt="podman-vs-docker.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
容器编排工具作为当今最重要的web开发技术之一，众多强者都在尝试争夺这一行业的主导地位。<br>
Podman是RedHat的一款产品，旨在使用类似于Kubernets的方法来构建、管理和运行容器，作为一款主流容器的可靠替代产品，它吸引了开发人员的关注。 <br>
Podman和Docker这两种标准的容器化工具已经有近十年的历史了，我们将对它们进行一下对比，这两种技术虽有本质的不同，但还是非常适合一起使用。<br>
<br><strong>目录</strong><br>
<br>容器编排是什么？<br>
Docker是什么？<br>
Podman是什么？<br>
Podman和Docker的区别<br>
➤架构<br>
➤Root特权<br>
➤安全<br>
➤Systemd<br>
➤镜像制作<br>
➤Docker Swarm<br>
➤All in one vs模块化<br>
Podman vs Docker：他们能一起使用吗 <br>
<br><strong>容器编排是什么？</strong><br>
<br>容器作为独立的软件包，包含代码及其依赖项：库、工具、设置和运行时。由于容器提供了更快的部署和可伸缩性，并且可以在开发和阶段之间统一工作，所以业界很快就采用了容器作为容器化架构的核心组件。<br>
容器的轻量化、便携、安全，提供了与任何环境兼容的独立空间。通过将软件与操作系统分离，容器可以被移植到任何地点(例如，从Linux到Windows系统)，从而避免了一些不必要的bug和报错。<br>
比较流行的编排技术有Docker，Docker Swarm, Kubernetes和Nomad，所有这些我们已经在我们的博客中分析和比较了。<br>
（<a href="https://page.imaginarycloud.com/cs/c/?cta_guid=6e2dcfab-0694-46d0-ab42-ce74a2f8779d&signature=AAH58kEdWeZo-3FuimUxNVr-gqvSlgnihw&placement_guid=ffca1738-261b-4665-a206-de11d00709a3&click=d9dfbb98-8a6e-4359-a5bf-3ccb90c05275&hsutk=5060fa86a387ce9e44ef5d7f6b589cdb&canon=https%3A%2F%2Fwww.imaginarycloud.com%2Fblog%2Fpodman-vs-docker%2F&portal_id=19894455&redirect_url=APefjpGatxODI97Pku1-V1_xVsIDi6AkMzCM6i8dXIrOLxkgQ5N0I55UE6r83nvlv7-BpKnL5HtVZvEpP5_hy_sFieOKBvUyfUMkMXI6YnBVHWoWIqzdeMDMrvSOmowW1VdQ9j_37zGjFi7250YLfqgR0BRF15YkGTem_Ip4knbYCdJ7SxKLV0Y&__hstc=248802264.5060fa86a387ce9e44ef5d7f6b589cdb.1641454075651.1641454075651.1641454075651.1&__hssc=248802264.1.1641454075651&__hsfp=112366145">正在寻找开发人员来开发你的软件、网站或应用？我们为您量身打造团队</a>）<br>
<br><strong>Docker什么？</strong><br>
<br>Docker是标准的容器管理技术。Docker在行业中举足轻重，以至于大多数人一想到容器，就会想到Docker。<br>
Docker容器编排世界的一把瑞士军刀，在其他替代方案出现之前就已经提供了诸多特性。随着容器管理复杂度的增加，它也必须成长为一个独立的、自给自足的工具，以便能提供开发人员的所有需求。<br>
Docker也在很短的时间内，就成为All-in-one解决方案的关键工具之一。其中一款就是Docker Swarm，这是一款由Docker原生的，可以让你组建群集和调度Docker引擎，以及用来创建和管理容器群的解决方案。<br>
Docker的诸多辅助工具处理所有与容器编排相关的任务，从负载均衡到网络，使其成为行业的首选，不光是作为行业技术参考。<br>
尽管Docker是一个强大的系统，但这种自给自足的模式也有它的缺点。虽然可以在开发的所有阶段创建和运行容器，但其他工具在与Docker集成交互时或多或少存在些困难。近年来，随着许多其他用于特定任务的专用工具的出现，Docker成为许多开发人员的起点，随之，他们将一些任务分配给其他更轻量级的平台和工具。<br>
<br><strong>Podman是什么？</strong><br>
<br>Podman是一种开源的Linux原生工具，旨在根据开放容器倡议（Open Container Initiative,OCI）标准开发、管理和运行容器和Pods。Podman是RedHat开发的一个用户友好的容器调度器，是RedHat 8和CentOS 8中默认的容器引擎。<br>
它是一款集合了命令集的工具，设计初衷是为了处理容器化进程的不同任务，可以作为一个模块化框架工作。它的工具集包括：<br>
Podman-Pods和容器镜像管理器<br>
Buildah-容器镜像生成器<br>
Skopeo-容器镜像检查管理器<br>
Runc-容器运行器和特性构建器，并传递给Podman和Buildah<br>
Crun-可选运行时，为Rootless容器提供更大的灵活性、控制和安全性<br>
这些工具还可以与任何OCI兼容的容器引擎(如Docker)一起工作，使其易于转换到Podman或与现有的Docker安装一起使用。Kubernetes可以使用Podman吗？答案是：是的。事实上，Kubernetes和Podman在某些方面是相似的。<br>
Podman对于容器有着不同的方法论。正如它的名字所暗示的那样，Podman可以创建一起工作的容器“Pods”，这是一个类似Kubernetes里Pods的特性。Pods在一个共同的名称空间里，作为一个单元来管理容器。<br>
比较主要的好处是开发人员可以共享资源，在一个Pod中为同一个应用程序使用不同的容器：一个容器用于前端，另一个容器用于后端，还有一个数据库。Pod的配置可以导到Kubernetes兼容的YAML文件，并应用到Kubernetes集群中，从而允许容器更快地进入生产。<br>
Podman的另一个特性是它是无守护进程的。守护进程是在后台运行的程序，它处理服务、进程和请求，没有用户界面。Podman是一种独特的容器引擎，因为它实际上并不依赖于守护进程，而是作为子进程启动容器和Pod。<br>
你可能会问:“我为什么要使用Podman？”作为一种开发和管理工具，Podman具有独特的优势，这使得它在适当的环境中成为Docker的可行和有趣的替代品。或者一个与Docker并肩工作的强大补充，因为它支持与Docker兼容的CLI接口。<br>
为IT专业人士提供的最佳见解，每月一次。<a href="https://page.imaginarycloud.com/cs/c/?cta_guid=fc060a9a-9588-4f11-8dc9-48041de50798&signature=AAH58kHK_oMNn5U8NwdjZXCqRirxxEL_NA&placement_guid=52392abd-3445-4008-a9fa-1dfba7a24ff0&click=2c590c2c-d723-43b4-9ff3-a8c70a6ee929&hsutk=5060fa86a387ce9e44ef5d7f6b589cdb&canon=https%3A%2F%2Fwww.imaginarycloud.com%2Fblog%2Fpodman-vs-docker%2F&portal_id=19894455&redirect_url=APefjpFIxX9WL5PRmsc_zx6hBwh6bmpULPmxW5ITC6jTpci9nE2w0DsJkIYQVl7FNC2cGNDjRZon2dHO08hmWeTEtJDZZJ7jwTfp-gET9cRKbHwzP3MSsgMhpFEUw1IBz9HNX7r7KOwZzPhsTpJsqXhNBIr-udOhOofPrQUda1yq3IexfCVxJsTaCN4gMb1zOyAvCbU3RMAkwRiaTFBt0yiARNHU1hgdhy9JhtWjA3mbzCevLkbG79IR2vOx9lryr-EE-9Ki8Vfm&__hstc=248802264.5060fa86a387ce9e44ef5d7f6b589cdb.1641454075651.1641454075651.1642142995538.2&__hssc=248802264.1.1642142995538&__hsfp=2126071286">订阅</a>我们的通讯。 <br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220114/2d5ac794b9409227f0621ea28c6abbf4.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220114/2d5ac794b9409227f0621ea28c6abbf4.jpg" class="img-polaroid" title="podman-vs-docker-2.jpg" alt="podman-vs-docker-2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>Podman vs Docker：区别</strong><br>
<br>Podman和Docker有许多共同的特性，但也有一些根本的区别。技术不分好坏，只是着重于哪个更适用于某些特定的场景。<br>
架构：<br>
Docker使用守护进程，一个正在后台运行的程序，来创建镜像和运行容器。Podman是无守护进程的架构，这意味着它可以在启动容器的用户下运行容器。Docker有一个由守护进程引导的客户端-服务器逻辑架构；但Podman不需要此类守护进程。<br>
Root特权：<br>
由于Podman没有守护进程来管理其活动，也无需为其容器分配Root特权。Docker最近在其守护进程配置中添加了Rootless模式，但Podman首先使用了这种方法，并将其作为基本特性进行了推广。原因如下<br>
安全：<br>
Podman比Docker安全吗？Podman允许容器使用Rootless特权。Rootless容器被认为比Root特权的容器更安全。在Docker中，守护进程拥有Root权限，这使得它们易成为攻击者的首选入侵点。Podman中的容器默认情况下不具有Root访问权限，这在Root级别和Rootless级别之间添加了一个自然屏障，提高了安全性。不过，Podman可以同时运行Root容器和Rootless容器。<br>
Systemd：<br>
如果没有守护进程，Podman需要另一个工具来管理服务并支持后台运行的容器。Systemd为现有容器创建控制单元或用来生成新容器。Systemd还可以与Podman集成，允许它在默认情况下运行启用了Systemd的容器，从而无需进行任何修改。<br>
通过使用Systemd，供应商可以将他们的应用程序封装为容器用来安装、运行和管理，因为现在大多数应用程序都是通过这种方式打包和交付的。<br>
构建镜像：<br>
作为一款自给自足的工具，Docker可以自己构建容器镜像。Podman则需要另一种名为Buildah的工具的辅助，该工具充分体现了它的特殊性:它是为构建镜像而设计的，而不是为构建容器而生。<br>
Docker Swarm：<br>
Podman不支持Docker Swarm，这可能会在某些项目中被刨除在外，因为使用Docker Swarm命令会产生一个错误。然而，Podman最近增加了对Docker Compose的支持，使其与Swarm兼容，从而克服了这个限制。当然，Docker由于其原生的特性，与Swarm当然融合得很好。<br>
All in one vs模块化：<br>
也许这就是这两种技术的关键区别：Docker是一个独立的、强大的工具，在整个循环中处理所有的容器化任务，有优点也有缺点。Podman采用模块化的方法，依靠专门的工具来完成特定的任务。<br>
Podman vs Docker：他们能合作吗？<br>
作为最好的、最易应用于Docker的替代方案——用户可以将Docker别名设置为Podman（别名Docker=Podman），且不会出现任何问题，正如本演示中所示——Podman是一个非常强大的容器化任务工具。<br>
Podman会是Docker的替代品吗？<br>
如果您要从头开始一个项目，Podman可以是一个首要的容器化技术选项。如果项目正在进行，并且已经在使用Docker，这还需要具体情况具体分析，实际情况并不一定值得去改。而且作为一款Linux原生的应用，它要求相关开发人员具备Linux的相关技能。<br>
开发人员可以在开发阶段依赖Docker，然后在运行时环境中将项目推向Podman，从而结合使用这两种工具，并受益于Podman所提供的更安全性。由于它们都是OCI兼容的，因此，兼容性不是个问题。<br>
Docker和Podman能共存吗？是的，而且会很好。许多开发人员一直在合用Docker和Podman来创建更安全、更高效、更敏捷的框架。它们有很多共同之处，无论是从Docker到Podman的转变，亦或是二者合并使用，都可以做到无缝衔接。<br>
您可以通过此<a href="https://github.com/containers/podman">链接</a>在Linux机器上直接使用Podman，如果手边没有，也可以<a href="https://www.katacoda.com/courses/containers-without-docker/running-containers-with-podman">在线</a>试用一下。<br>
<br>想了解更多关于容器编排的信息吗？<br>
每年有超过50万人阅读我们的博客，我们在容器编排等主题排名Google搜索的前列。如果你喜欢这篇博文，并想阅读我们所有关于容器业务流程的博文，请按<a href="https://page.imaginarycloud.com/cs/c/?cta_guid=50591d7b-3042-4f9c-b08a-49bf633b1662&signature=AAH58kFCMUgc6VdwWQ_Yfj18FUGcPgVcrQ&placement_guid=abdb99de-4fd7-4f7f-9138-4c84b3337533&click=48e5f5f3-395b-465d-bfff-0b86ba47fdc2&hsutk=5060fa86a387ce9e44ef5d7f6b589cdb&canon=https%3A%2F%2Fwww.imaginarycloud.com%2Fblog%2Fpodman-vs-docker%2F&portal_id=19894455&redirect_url=APefjpEE1iljJRVfrPqmJp-Ey86rDvXIhO8_7rQxePX9SwukRLzF1eS0zWjcM9NqjtUJMHDEBfYiqw5B61yWTWU7Mc8RC4ZW5P3uyexj3sgnb7Xji0W30RPSaO8zhKpz0COztIdU4sC_NpufrH5YPY3Aa1s02C1l5g&__hstc=248802264.5060fa86a387ce9e44ef5d7f6b589cdb.1641454075651.1641454075651.1641454075651.1&__hssc=248802264.1.1641454075651&__hsfp=112366145">这里</a>。<br>
在你的收件箱里找到最好的内容<br>
除了我们的博客外，我们还每月为IT专业人士提供新闻、趋势和工具等内容。你可以了解更多，查看过去的版本，并在这里<a href="https://page.imaginarycloud.com/newsletter-subscription">订阅</a>。<br>
<br>原文链接：<a href="https://www.imaginarycloud.com/blog/podman-vs-docker/" rel="nofollow" target="_blank">https://www.imaginarycloud.com ... cker/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            