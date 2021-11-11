
---
title: '通过Rainbond的团队管理去管理已有的组织架构'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://pic.imgdb.cn/item/6178c9f52ab3f51d91aef694.png'
author: Dockone
comments: false
date: 2021-11-11 06:09:29
thumbnail: 'https://pic.imgdb.cn/item/6178c9f52ab3f51d91aef694.png'
---

<div>   
<br>针对于多团队管理我先列举几个小问题，看看大家有没有共鸣，我们在刚刚接触并使用Rainbond的时候，仅仅创建一个团队，里面创建一大堆应用，看起来特别乱，进行管理的时候呢，也会非常麻烦，尤其是当团队需要划分角色进行管理的时候，就会发现没有办法将权限分配的特别细化，体现不出来应用隔离性，操作安全性，进而没有办法将Rainbond的多团队多用户的功能发挥出来。<br>
<br>  通过这些问题，我们整理了一下，在使用平台的过程中可能遇到的组织架构，以及这些组织架构应该怎么去进行划分，怎么合理的去进行创建团队以及分配权限，希望通过本文档大家更够对Rainbond的多团队管理有更深层级的一个理解和使用。<br>
<br><h2>一.Rainbond 多团队架构模式</h2>  我们先一起来看一下在使用Rainbond的过程中，各种企业架构迁移上来的时候，应该怎么去合理划分团队以及角色。 <br>
<br>（1）项目型架构：通过不同的项目进行划分，每个项目里面包含的应用以及角色是不一样的。<img src="https://pic.imgdb.cn/item/6178c9f52ab3f51d91aef694.png" alt referrerpolicy="no-referrer"><br>
<br>（2）职能型架构：通过公司里不同的职能进行划分，将开发运维测试人员，分别加入各自的团队，对其他不可见。<img src="https://pic.imgdb.cn/item/617bc3df2ab3f51d9110dc28.png" alt referrerpolicy="no-referrer"><br>
<br>（3）大型企事业单位架构：通过将不同的供应商，进行区别划分，然后进行分类的一种。<img src="https://pic.imgdb.cn/item/617bc34e2ab3f51d91106c15.png" alt referrerpolicy="no-referrer">         <br>
<br>（4）复合型架构：一般用于体量大的公司，将职能，供应商，项目组一一进行划分，更加的细化。<img src="https://pic.imgdb.cn/item/6177c4542ab3f51d91e6c1a2.png" alt referrerpolicy="no-referrer"><br>
<br>  以上几种类型就是几种比较普遍的，每个公司都会有不同的部门团队，里面有不同的角色，不同的人员，不同的权限，例如：开发者权限：只能进行增，改，查，并不能执行删除操作，管理者权限：可以全面操作增删改查功能等等，大家看看有没有适合自己公司的，接下来我拿一个复合型的架构案例进行讲解，让大家理解是怎么进行管理分配的。<br>
<br><h2>二.真实场景的团队管理</h2>  拿我们的一个客户给大家更加详细的介绍他们是怎么用的，企业是一个研究院，他们的架构就是复合型的，因为体量非常的大，有自己的研发技术团队，有供应商进行供应服务，也有子团队的项目相互关联，而且有的应用之间还是有关联的，管理起来还是相对让人头痛的。<br>
<br>  而且他们不同的供应商，团队，项目之间面临的问题、人员以及要处理的应用关系也是完全不一样的，传统的方式进行管理，整体架构会很乱，而且容易出现权限分配过大或者过小的问题，一旦权限分配过大，对于我们的安全性来讲，其实是非常低的，一旦操作失误，就会带来不可估计的损失。<br>
<br>  针对于以上问题，我们详细进行了记录，拟定平台的解决方案：<br>
<br>  （1）根据用户的需求进行定制化团队建设，供应商，技术团队，项目进行划分，添加相应的人员，进行分配合理的权限，因为平台特有的权限机制是角色分配，（默认是开发，管理，观察）每个角色的权限不同，当然也可以自己进行定义角色名称权限，所以可以更好的细化分配，更加具体<br>
<br><img src="https://pic.imgdb.cn/item/6178a9a82ab3f51d91979f8b.png" alt referrerpolicy="no-referrer"> <br>
<br>  因为每个团队里面都有不同的角色，在这里着重说一下，平台的机制是每个团队是相互隔离的，通过不同角色进行登录所看到的应用以及可操作性是完全不一样的。<br>
<br><img src="https://pic.imgdb.cn/item/61711eec2ab3f51d9196c0a6.png" alt referrerpolicy="no-referrer"><br>
<br>该研究院的组织架构在平台上看起来非常清晰，最重要的是他们管理各项业务时只需要进入自己相应的团队即可，当然这是管理页面，会显示全部管理的团队，当不同的团队，不同的人员，进入他们的工作环境时，自己仅仅也只能看到跟自己相关的应用。<br>
<br>（2）建完团队，角色等，我们就可以添加用户了，只要注意选择他们所在的团队以及要赋予的角色就行了<br>
<br><img src="https://pic.imgdb.cn/item/61756c032ab3f51d914c238a.png" alt referrerpolicy="no-referrer">    <br>
<br>  可以通过管理账号增加用户，并且赋予指定的权限也可以让用户自己进行注册，然后申请加入自己要加的团队都可以。<br>
<br>  （3）根据平台的资源配额和限制的功能，解决客户资源浪费的情况。<br>
<br><img src="https://pic.imgdb.cn/item/617625df2ab3f51d91bd93f0.png" alt referrerpolicy="no-referrer"><br>
<br>通过集群里对不同团队资源限制和配额，一方面可以提高资源利用，另一方面我们可以更好的管理每个团队的资源实现最大化利用。<br>
<br>  （4）该研究院拥有多个集群，如何统一的管理这些集群呢？Rainbond 天生支持基于统一控制台的多集群管理。同个团队可以在多个集群之间同时开通，团队所辖的用户及对应的角色都可以在开通的多个集群中生效，这一点是 Rainbond 抽象出的团队概念，和一般租户概念的差别很大。用户通过团队中指向不同集群的入口，即可进入对应集群的工作空间之中，使用调度其中的资源。<br>
<br>该能力适用于独享或共享集群计算资源这一场景：<br>
<br>  当集群仅被一个团队开通时，其资源只会被当前团队所辖的用户使用，即独享了该集群的计算资源。研究院所对接的某集群仅供负责该项目的团队所开通，所以仅有该项目团队成员可以向这个集群交付应用。<br>
<br>  当集群被多个团队开通时，其资源被所有团队的成员共享使用，即共享了该集群的计算资源，企业管理员可以通过团队资源限额来管理所有团队的资源占用上限。该研究院自身运营的平台，面对所有开发团队、项目团队、供应商团队开放，就是一种共享资源的使用方式。 <img src="https://pic.imgdb.cn/item/617a17e82ab3f51d91a5bdfe.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://pic.imgdb.cn/item/6176264b2ab3f51d91bdda0b.png" alt referrerpolicy="no-referrer"><br>
<br>  （5）最后就是考虑到网络的隔离性  ，Rainbond平台是基于kubernetes之上做的云原生应用管理平台，所以底层隔离逻辑完全可以通过不同的SDN（软件定义网络）来达到我们想要的不同效果,<br>
<br>  例如：Calico从路由规则上隔离；<a href="https://github.com/coreos/flannel#flannel">Flannel</a> 是一个非常简单的能够满足 Kubernetes 所需要的覆盖网络。<a href="https://romana.io/">Romana</a> 是一个开源网络和安全自动化解决方案。 它可以让你在没有覆盖网络的情况下部署 Kubernetes。 Romana 支持 Kubernetes <a href="https://kubernetes.io/zh/docs/concepts/services-networking/network-policies/">网络策略</a>， 来提供跨网络命名空间的隔离。  <br>
<br>   平台能够进行定义不同的SDN是因为我们对于K8S是没有侵入的,用户完全可以根据自己的需求进行自主选择。<br>
<br><h2>三.多级团队管理解决思路</h2>通过上述大家应该对于如何去使用多团队管理有了一个非常好的认识，但只是针对于单层级的一个管理，那么多层级的管理是怎样的呢？单层级团队管理与多层级团队管理最大的区别，在于父级团队管理人员可以管理子级团队，简单实现只需要把父团队管理人员分别加入子团队，并且赋予相对应的角色权限，就能实现多级的管理。<br>
<br><h2>四.小结</h2>  相信看到这里，大家对多团队管理有了更深一个层级的理解，那么我们应该怎么去合理利用，并使用这些机制呢，大家可以参考<a href="https://www.rainbond.com/docs/get-start/team-management-and-multi-tenancy/">Rainbond团队管理操作文档</a>。<br>
<br><h2>五.关于Rainbond</h2> <a href="http://weekly.dockone.io/www.rainbond.com">Rainbond</a>是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。<br>
<br>已有上百家企业使用Rainbond管理关键业务场景，涵盖制造、能源、高校、公安、政府、交通、军工等十几个行业。客户有 京东方、百胜中国、中航信、中公高科等大型企业。
                                
                                                              
</div>
            