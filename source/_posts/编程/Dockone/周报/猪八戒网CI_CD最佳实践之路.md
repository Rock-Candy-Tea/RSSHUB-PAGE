
---
title: '猪八戒网CI_CD最佳实践之路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/bad27dc8de4575136826967f5b3cac64.jpg'
author: Dockone
comments: false
date: 2021-07-24 14:05:44
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/bad27dc8de4575136826967f5b3cac64.jpg'
---

<div>   
<br><h3>序言</h3>本文旨在介绍ZBJ DevOps团队倾力打造的DevOps平台中关于CI/CD流水线部分的实践。历经三次大版本迭代更新的流水线，完美切合ZBJ各种业务发展需求，在满足高频率交付的同时，提高了研发效率，降低了研发成本，保证了交付质量。<strong>在此，谨向在职和已离职的贡献者表示感谢。</strong><br>
<br>持续集成（Continuous Integration）简称CI，持续集成强调开发人员提交了新代码之后，立刻进行构建、（单元）测试。根据结果，我们可以确定新代码和原有代码能否正确地集成在一起。持续集成过程中很重视自动化测试验证结果，对可能出现的一些问题进行预警，以保障最终集成的代码没有问题。持续交付（Continuous Delivery）简称CD，持续交付在持续集成的基础上，将集成后的代码部署到更贴近真实运行环境的「类生产环境」（test，testing）中，然后交付给质量团队，以供评审。如果评审通过，代码就进入生产阶段。持续交付并不是指软件每一个改动都要尽快部署到产品环境中，它指的是任何的代码修改都可以在任何时候实施部署。有的人也把CD称为Continuous Deployment（持续部署），持续部署是指当交付的代码通过评审之后，可以部署到生产环境中。这里需要注意的是，持续部署应该是持续交付的最高阶段，持续交付是一种能力，持续部署是一种持续交付的表现方式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/bad27dc8de4575136826967f5b3cac64.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/bad27dc8de4575136826967f5b3cac64.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>CI/CD过程示意图</em><br>
<h3>猪八戒网的CI/CD之路</h3><h4>背景介绍</h4>在提到ZBJ DevOps流水线之前，先交代一下历史背景。2015年前，猪八戒网80%的项目都是用PHP语言开发的，剩下的少部分使用的是Nodejs和Java。2015年，ZBJ研发中心进行了自发性的“工业革命”——腾云七号行动——使用Java语言将核心业务代码进行了重构和拆解，建立了以Dubbo为核心的SOA微服务框架，使用ZooKeeper+Swoole为核心的业务调用提供机制。满足新业务使用Java语言编写、老业务仍然使用PHP编写，同时支持两种语言（Nodejs&PHP）调用Dubbo服务的能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/82916cccd02189ed579574f4b15ad74e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/82916cccd02189ed579574f4b15ad74e.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
之后，开始全面推行前后端分离，于是流行了沿用至今的主流架构：<br>
<ul><li>Nodejs：负责前端</li><li>Java：负责后端</li><li>PHP：负责老项目维护</li></ul><br>
<br>剩余部分小系统或者边缘化的工具使用其他语言开发，或者在此三种语言基础上的一些变种：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/d9dfebe33403bd30e04b6ce4e7a655c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/d9dfebe33403bd30e04b6ce4e7a655c5.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
随着业务的重构和拆解，以前一个个庞大的系统被拆解成若干个独立的小系统，使得交付变得更加容易。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/bcf23c24d02c50008770be28bfb28943.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/bcf23c24d02c50008770be28bfb28943.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
而随着项目工程数量的快速增长，交付开始变得频繁，传统开发模式的一两个月交付一次远远不能满足交付要求，改变迫在眉睫。<br>
<br>2016年Q3季度，感受到改变迫在眉睫，ZBJ研发中心经充分准备后决定抽调部分运维同学和开发同学组建一支名为“DevOps取经团”的团队，力图打造属于ZBJ自己的以提高研发效率为目标的平台。<br>
<h4>ZBJ CI/CD发展史</h4><strong>第一阶段：2015年以前</strong><br>
<br>2015年以前，此时“工业革命”还未开始，ZBJ所谓的流水线先后经历了“大锅饭年代”、“公交车模式”。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/40706779c9915d8635a3ac55e1796c15.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/40706779c9915d8635a3ac55e1796c15.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>大锅饭年代（本图由DevOps团队提供）</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/d2442c7bf46246d2ffa2099c7515d814.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/d2442c7bf46246d2ffa2099c7515d814.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>公交车模式（本图由DevOps团队提供）</em><br>
<br>可以看到，无论是“大锅饭年代”，还是“公交车模式”都会面临很多问题：<br>
<ol><li>项目耦合度太高，容易导致合并冲突，环境冲突等。</li><li>集成过程中未对代码进行审查，错误代码发布到测试环境后，会影响依赖方的测试。</li><li>发布受限制，必须在专门时间由专人发布。</li><li>发布异常时，回滚工作异常艰难。</li></ol><br>
<br><strong>第二阶段（2016-2017）：私家车模式</strong><br>
<br>通过“工业革命”的变革，对系统的重构和拆解，同时引入工程责任制，给每个工程指定负责人，对工程的各种权限进行了管控，业务范围和边界变得更加清晰，使得项目耦合度太高的问题得到了很大的缓解。<br>
<br>解决了项目耦合度高的问题，接下来解决如何实现随时由开发团队自主发代码的问题。<br>
<br>用Jira做研发流程管理，制定针对ZBJ需求上线的流程：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/bd86830edae33018f9ec4f431c4e56d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/bd86830edae33018f9ec4f431c4e56d1.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
需求上线流程每个环节对应流水线的每个环境，只有到达某个环节，才能推送对应环境，每个环节会制定对应的准入准出，保证每走到的下一步都离成功部署更近一步。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/c361e696eec9bb71063323d05056b161.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/c361e696eec9bb71063323d05056b161.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>推送环境示意图</em><br>
<br>每个环境制定不一样的执行任务，基本包括Jira状态校验，代码审查（单元测试），编译构建，上传包到制品库，拉取制品库中的包部署到对应环境。<br>
<br>值得注意的是，我们引入了Docker发布，所以我们的流水线是支持容器和虚拟机的混合发布的。虚拟机发布方式的制品是存放在一个叫做文件服务器的地方，容器发布方式的制品是push到Harbor仓库的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/0fa9824794bee7b688ff77a82bb1fc95.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/0fa9824794bee7b688ff77a82bb1fc95.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>容器发布&虚拟机构建打包示意图</em><br>
<br>采用的分支策略是：branches开发，master发布，tags存档（我们使用GitLab作为源码管理工具）。在测试环境通常为非master分支，测试完毕后合并到master，推送预发布，并针对当前版本打一个tag。针对这种情况，我们的“一次构建，处处使用”指的是测试环境用测试环境构建好的包，其他环境用预发布构建好的包。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/697939fb61cfdea584e642fec57a58e6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/697939fb61cfdea584e642fec57a58e6.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>各环境使用制品示意图</em><br>
<br>在推送每一个环境（test环境除外）时，都会校验当前版本的代码是否为前置环境推送过的最新代码，保证不会将没有经过审查的代码交付到线上。<br>
<br>在测试环境每一次编译构建之前，都会对代码进行一次安全扫描，Java语言的工程通过解析pom文件对其所有的依赖进行递归扫描，Nodejs语言的工程通过对node_module里下载的包进行递归扫描，确保有安全漏洞的代码不会被带入到生产环境。<br>
<br>编译构建时，会根据开发语言的不同，执行不同的编译脚本，根据发布方式的不同（虚拟机发布或者容器发布），执行不一样的后续操作步骤。<br>
<br>我们将Jenkins作为后台编译服务器，采用的是多master多slave的架构，我们并未直接使用Jenkins的流水线，而是开发了一个叫Pipeline的系统，与Jenkins做对接（此时的对接方式是调用Jenkins的API），由Pipeline系统提供Jenkins作业所需要的全部信息，另外编写了整个过程需要具体执行操作的脚本，通过Jenkins的job配置“Execute shell”的方式每次在构建之前导入到工作空间。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/dedff2b97eb705b385e33f48b2f368ec.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/dedff2b97eb705b385e33f48b2f368ec.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
流水线标准生产过程大体如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/c9048878a0332174588932ccad29ed58.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/c9048878a0332174588932ccad29ed58.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>流水线标准生产过程示意图</em><br>
<br>另外，针对回滚的情况，因为每次在上线前都会在预发布会构建一个稳定的版本，并打一个tag，并且记录下tag对应的制品（包或者镜像）版本，所以在回滚的时候，只要选择要回滚的版本，便能找到对应版本的制品，进行重新发布，以此达到回滚的目的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/6d6228aa0c3aadfe8e5ba882d0d015a6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/6d6228aa0c3aadfe8e5ba882d0d015a6.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>回滚流程</em><br>
<br>至此，第二阶段大体实现了以下功能：<br>
<ul><li>通过用Jira需求上线流程和流水线做整合，以及多种推送前的校验，保证了上线过程的每一步都是可靠的</li><li>每一个环境的集成和发布都是自动化的</li><li>因为过程变得可靠且自动化，使得将发布过程开放给研发团队成为了可能，达到了随时自主上线的目的。</li></ul><br>
<br>然而这样的流水线也有诸多问题：<br>
<ul><li>不够灵活，如在推送测试环境时，整个过程执行的步骤是固定的的，即第一步做什么，第二步做什么都是固定的，不能新增也不能删减，如某些团队需要进行单元测试，有的不需要，但流水线都会去执行单元测试，通常情况下单元测试过程是一个花费时间比较长的过程，这对于需要频繁更改和部署的业务是不友好的。</li><li>推送成功率不高，因为整个过程是串联的，某一个环节出现错误，将会导致本次推送失败，而某些环节本不应该影响构建结果的，最后导致了构建失败。</li></ul><br>
<br><strong>第三阶段（2017-2019）：拥有灵活车道的私家车模式</strong><br>
<br>考虑到前面提到的两点，ZBJ DevOps团队在17年底对流水线做了二次改造：<br>
<br>1、所有执行步骤拆解成独立原子任务，建立原子任务库；<br>
<br>2、将原子任务根据功能性分为两种，校验类以及执行类，校验类原子任务主要是是做准入准出的判断，执行类主要是编译构建，打镜像，上传hub仓库以及部署。<br>
<br>3、将原子任务根据执行载体分为两种，Java类和Jenkins类，直接用Java程序执行的任务为Java类，需要Jenkins执行的任务为Jenkins类。<br>
<br>4、根据开发语言、发布方式、业务类型的不同，从原子任务库中选取不同原子任务组成一条标准有序的执行流水线。<br>
<br>5、提供工程特殊配置，如有些工程需要增强校验，有的工程需要减少校验，则可以通过启用和禁用的方式进行特殊配置，如下图所示，根据1、2和3步骤后可最终生成一条本次执行的流水线任务列表。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/2d50e43e4386b2c59387c1a38d6e0be2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/2d50e43e4386b2c59387c1a38d6e0be2.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>原子任务一览表</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/5dc9bb64acc202fc2f57179612f32940.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/5dc9bb64acc202fc2f57179612f32940.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>执行效果图</em><br>
<br>6、根据原子任务的制定，我们将Jenkins执行的job也拆分成了对应的几类，每一类拥有足够多数量的job进行任务的执行。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/ac58d5b44ed25b7fa3bf4dfe5e19948a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/ac58d5b44ed25b7fa3bf4dfe5e19948a.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/68c3774370c50b5763fe41f3ecb20fb5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/68c3774370c50b5763fe41f3ecb20fb5.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
7、升级了Pieline系统和Jenkins通信架构，通过编写一个RabbitMQ的插件植入到Jenkins Master上，从原来调用API的方式，改成用RabbitMQ的方式进行通信，大大提高了效率和成功率。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/fcd192398006df7d353dcde455c1c0bc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/fcd192398006df7d353dcde455c1c0bc.jpg" class="img-polaroid" title="18.jpg" alt="18.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>通信示意图</em><br>
<br>8、升级了Jenkins架构，构建一个能适配ZBJ所有开发语言的镜像，利用Jenkins Master的Kubernetes插件，将原来的虚拟机slave节点全部替换成容器slave节点，并且这个slave集群完全由Jenkins Master的Kubernetes插件调度，不论在高并发和低并发的时候都能及时扩缩容，满足业务需求。<br>
<br><strong>第四阶段（2020-至今）：智能驾驶模式</strong><br>
<br>可以看到，到第三个阶段为止，我们的每一次编译过程，都需要研发同学“推送一下”，而且这个过程也是需要花费一些时间的，比如一个正常的Nodejs工程平均编译时长至少需要花费100+s以上，一个正常的Java工程平均编译时长至少也是需要30s以上，由于我们提供了推送过程“可视化”的功能，且没有执行结果的通知，导致用户必须关注推送过程以确保本次推送是成功的，大大浪费了研发同学的时间。<br>
<br>在此基础上，我们进一步做出了以下优化：<br>
<br>1、为每一个GitLab上的工程添加一个Webhook，每当开发人员向仓库push一次，便会触发Webhook，调用Pipeline系统接口进行一次快速构建。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/5c2f937cccc409b918ac712d3183998b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/5c2f937cccc409b918ac712d3183998b.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
注意：并不是每次push都会进行一次快速构建，为了防止开发同学频繁修改少量代码提交到版本库，我们规定了一个“暗号”，只有当开发同学在commit message中添加这个“暗号”，才会触发一次快速构建。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/6252c0e33c9e221e1baadd97647a9326.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/6252c0e33c9e221e1baadd97647a9326.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>auto_trigger_build就是暗号内容</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/26633e61ec38616976cc7790ef7c7787.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/26633e61ec38616976cc7790ef7c7787.jpg" class="img-polaroid" title="21.jpg" alt="21.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
2、快速构建的结果是构建一个包或者一个镜像，存放在前文提到过的文件服务器或者Harbor仓库。在下一次用户“推送”的时候，便会根据分支和版本判断是否存在已编译过的包或者镜像，如果存在，则直接使用，跳过编译过程。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/03015838f813ae19e26688b18fa57c73.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/03015838f813ae19e26688b18fa57c73.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
3、增加快速构建结果通知，因为整个快速构建过程是后台执行的，所以流水线系统通过企业微信的方式通知到用户本次快速构建的结果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/4fb078456a214c7b820ac0625c6035f0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/4fb078456a214c7b820ac0625c6035f0.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>快速构建前通知</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/40dfcba24483be031f063f832691461d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/40dfcba24483be031f063f832691461d.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>快速构建完成后结果通知</em><br>
<br>4、除了增加快速构建的通知，我们还增加了推送的通知。用户再也不用关注推送过程，只需要在推送后继续做其他事情，推送结果由企业微信通知到用户。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/92592a257d5c453c7225166aeef60c75.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/92592a257d5c453c7225166aeef60c75.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/953ed47699e9b47843c30feb2b608266.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/953ed47699e9b47843c30feb2b608266.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
值得注意的是，当推送失败后，流水线系统也会通知到用户，进行对应问题的排查。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210723/46eda0580ffa92c6583a991df7429d58.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210723/46eda0580ffa92c6583a991df7429d58.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
至此，ZBJ的CI/CD实践之路基本介绍完毕，当然，其中也还有很多细节方面，因为涉及的东西太多，不便铺开来讲。<br>
<h3>总结三次重大改造的结果</h3>第一次改造：奠定了ZBJ的CI/CD基础，打造了一条标准的流水线，解放了运维劳动力（过程全自动化），提高了研发效率，降低了研发成本（运维同学由最多时候的三四十个减少到了不到十个人）。<br>
<br>第二次改造：流水线实现了高可用，同时其灵活的配置能完美满足不同业务团队的需求。<br>
<br>第三次改造：提升了流水线效率，弱化推送过程，增强以人为本的体验，使推送过程更加智能化。<br>
<h3>谈谈未来</h3>CI/CD实践之路还在继续，因为不同公司有不同的业务场景，而同一公司的业务也会随着时代的发展不断变化，<strong>只有适合自己的才是最好的，只有能拥抱变化的才是最好的</strong>，但万变不离其宗的，我觉得应该有一下几点：<br>
<ul><li>CI/CD应该是以提高研发效率为目标的实践，一切脱离这个目标只是为了迎合什么口号而做什么的是都是耍牛氓。而实现这个目标是一个比较漫长的过程，一开始会比较容易，后面就会越来越难，这需要不断思考和学习的过程。</li><li>CI/CD应该是紧贴业务的，因为业务的不同，要求的技术架构也会有所不同，随之而来，要求的交付方式也会有所不同。</li><li>CI/CD应该是以人为本的，我们应该尽可能地将一切繁琐的过程交给程序去执行，而人只需要“坐享其成”或者做少量的决策即可。</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/jU7n7MhZXnygb1-I8rHPsg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/jU7n7MhZXnygb1-I8rHPsg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            