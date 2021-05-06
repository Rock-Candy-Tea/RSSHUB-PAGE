
---
title: '什么是CI_CD流水线？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/9a6f6dd7d2a0171318904bda486f0555.png'
author: Dockone
comments: false
date: 2021-05-06 04:01:50
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/9a6f6dd7d2a0171318904bda486f0555.png'
---

<div>   
<br>【编者的话】在CI/CD和DevOps领域中，持续交付和持续部署是一个老生常谈的话题。持续集成这个术语最早是在1994年由Grady Booch提出。微服务提出者Martin Flower在2014年发表的论文《Microservice》中也对软件开发持续集成提供了可参考原则。持续集成是借助工具对软件项目进行持续的自动化的编译打包构建测试发布，来检查软件交付质量的一种行为。而持续部署是基于持续交付的优势自动将经过测试的代码推入生产环境的过程。下文从细节描述了持续集成和持续部署各阶段的关键步骤，以下是原文。<br>
<br>本文将探讨CI（持续集成）/CD（持续部署）流程中的各个阶段；以及从快速、规模交付的视角探讨为什么CI/CD流水线对于我们的组织是必不可少的。<br>
<br>CI/CD流水线工作流包括CI/CD流程开始时所有阶段等一系列步骤，负责创建自动、连贯的软件交付模型。<br>
<br>通过CI/CD流水线，软件研发可以实现从代码签入、测试、构建和部署直至生产阶段都在流水线中向前推进。此概念之所以高大上，是因为一旦实施了流水线，就可以将其部分或全部自动化，从而加快开发流程并减少错误。 换句话说，CI/CD流水线使企业可以更轻松地应对软件的自动、快速、持续交付。<br>
<br>DevOps工程师经常会将CI/CD各阶段的和其CI/CD流水线混淆。尽管不同的工具可以将每个复杂阶段自动化完成分阶段的CI/CD，但是整体CI/CD软件链仍然可能由于不可避免的人工干预而中断。因此我们首先需要了解<a href="https://dzone.com/refcardz/getting-started-with-feature-flags">CI/CD流程</a>中的各个阶段，以及从快速、规模交付的视角探讨为什么CI/CD流水线对于我们的组织是必不可少的。<br>
<h3>CI/CD 阶段：理解参与者、流程、技术</h3>企业应用程序开发参与者通常由开发人员，测试人员/QA工程师，运维工程师以及SRE（站点可靠性工程师）或IT运营团队组成。 他们紧密合作，目标是高质量软件交付。 CI/CD是两个独立过程的组合：持续集成和持续部署。下面列出了每个步骤中的主要步骤：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210504/9a6f6dd7d2a0171318904bda486f0555.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/9a6f6dd7d2a0171318904bda486f0555.png" class="img-polaroid" title="01-cicd.png" alt="01-cicd.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>持续集成</h3>持续集成（CI）是构建软件和完成初始测试的过程。持续部署（CD）是将代码与基础设施相结合的过程，确保完成所有测试并遵循策略，然后将代码部署到预期环境中。当然，许多公司也有自己特有流程，但主要步骤如下。<br>
<h4>CI：代码提交阶段</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210504/04125977e2207f24e41125ea0375bc8b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/04125977e2207f24e41125ea0375bc8b.png" class="img-polaroid" title="02.png" alt="02.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参与者：开发工程师，数据库管理员（DBA），基础架构团队<br>
<br>技术：GitHub，GitLab，SVM，BitBucket<br>
<br>流程：代码提交阶段也称为版本控制。提交是将开发人员编写的最新代码变更发送到代码存储库的操作。开发人员编写的代码的每个版本都被无限期地存储。在与合作者讨论和审查变更之后，开发人员将编写代码，并在软件需求、特性增强、bug修复或变更请求完成后提交。管理编辑和提交变更的存储库称为源代码管理工具（配置管理工具）。在开发人员提交代码（代码推送请求）后，代码更改被合并到主线代码分支中，这些主线代码分支存储在GitHub这样的中央存储库中。<br>
<h4>CI：静态代码检查阶段</h4>参与者：开发工程师，数据库管理员（DBA），基础架构团队<br>
<br>技术：GitHub，GitLab，SVM，BitBucket<br>
<br>流程：开发人员编写代码并将其推送到存储库后，系统将自动触发以启动下一个代码分析过程。开发过程中存在这种情况：提交的代码可以构建成功，但在部署期间构建失败。无论从机器还是人力资源的利用率而言，这都是一个缓慢而昂贵的过程。因此必须检查代码中的静态策略。SAST（静态应用程序安全性测试）：SAST是一种白盒测试方法，可以使用SonarQube，Veracode，Appscan等SAST工具从内部检查代码，以发现软件缺陷，漏洞和弱点（例如SQL注入等）。 这是一个快速检查过程，其中检查代码是否存在语法错误。 尽管此阶段缺少检查运行时错误的功能，但该功能将在以后的阶段中执行。<br>
<br>将额外的策略检查加入自动化流水线中可以显著减少流程中稍后发现的错误数量。<br>
<h4>CI：构建</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210504/d167a9739b7d9eee53293c17d355e3d3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/d167a9739b7d9eee53293c17d355e3d3.png" class="img-polaroid" title="03.png" alt="03.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参与者：开发工程师<br>
<br>技术：Jenkins，Bamboo CI，Circle CI，Travis CI，Maven，Azure DevOps<br>
<br>流程：持续集成过程的目标是提交的代码持续构建为二进制文件或构建产物。通过持续集成来检查添加的新模块是否与现有模块兼容，不仅有助于更快地发现bug，还有助于减少验证新代码更改的时间。构建工具可以根据几乎所有编程语言的源代码创建可执行文件或包（.exe，.dll，.jar等）。在构建过程中，还可以生成SQL脚本，配合基础设施配置文件一起进行测试。简而言之，构建阶段就是编译应用程序的阶段。Artifactory存储、构建验证测试和单元测试也可以作为构建过程的一部分。<br>
<br>构建验证测试（BVT）/冒烟测试/单元测试：<br>
<br>创建构建后立即执行冒烟测试。BVT将检查所有模块是否正确集成，以及程序的关键功能是否正常运行。 这样做的目的是拒绝严重损坏的应用程序，以使QA团队不会在安装和测试软件应用程序步骤浪费时间。<br>
<br>在完成这些检查后，将向流水线中执行UT（单元测试），以进一步减少生产中的故障。单元测试可验证开发人员编写的单个单元或组件是否按预期执行。<br>
<br>构建产物存储：<br>
<br>一旦构建就绪，程序包就会存储在称为Artifactory或Repository工具的中央数据库。 随着每天构建量的增加，跟踪所有构建产物也会变得愈加困难。因此，一旦生成并验证了构建产物，就将其发送到存储库进行存储管理。 诸如Jfrog Artifactory之类的存储库工具可用于存储诸如.rar，.war，.exe，Msi等之类的二进制文件。测试人员可以从此处手动进行选择，并在测试环境中部署构建产物以进行测试。<br>
<h4>CI：测试阶段</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210504/fee216fb8a01dd405eff67fae0074efd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/fee216fb8a01dd405eff67fae0074efd.png" class="img-polaroid" title="04.png" alt="04.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参与者：测试人员、QA<br>
<br>技术：Selenium，Appium，Jmeter，SOAP UI，Tarantula<br>
<br>过程：发布构建过程后的一系列自动测试将验证代码的准确性。此阶段可帮助避免生产中的错误。 根据构建的大小，此检查可能持续数秒至数小时。对于由多个团队提交和构建代码的大型组织，这些检查在并行环境中运行，以节省宝贵的时间并尽早将错误通知开发人员。<br>
<br>测试人员（或称为QA工程师）基于用户描述的测试用例和场景设置自动化测试用例。他们执行回归分析、压力测试来检查与预期输出的偏差。测试中涉及的活动有完整性测试、集成测试、压力测试。这是一个高层次测试方法。在这个阶段，可以发现开发人员忽视的某些代码问题。<br>
<br>集成测试：<br>
<br>集成测试是使用Cucumber、Selenium等工具执行的，在这些工具中，单个应用程序模块被组合起来并作为一组进行测试，同时评估其是否符合指定的功能需求。在集成测试之后，需要有人批准该组中的更新集应该移到下一个阶段，这通常是性能测试。这个验证过程可能很麻烦，但它是整个过程的一个重要部分。验证这个过程业界有很多优秀的方案。<br>
<br>性能和压力测试：<br>
<br>Selenium、JMeter等自动化测试工具也可执行性能和压力测试，以检查应用程序在面对高负载时是否稳定和性能良好。该测试流程通常不会在每个更新提交上运行，因为完整的压力测试是长期运行的。当发布主要的新功能时，将对多个更新进行分组，并完成完整的性能测试。在单个更新被转移到下一阶段的情况下，流水线可能将金丝雀测试加入作为可选。<br>
<h3>持续部署：Bake和部署</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210504/3a46d7f38a2f7b23c5198f946d87463e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/3a46d7f38a2f7b23c5198f946d87463e.png" class="img-polaroid" title="05.png" alt="05.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参与者：基础架构工程师，SRE，运维工程师<br>
<br>技术：Spinnaker，Argo CD，Tekton CD<br>
<br>过程：在测试阶段完成之后，可以部署到服务器的标准代码准备就绪。 在部署到生产中之前，它们将被部署到产品团队内部使用的测试环境或beta环境。 在将构建移至这些环境之前，构建必须经过Bake和Deploy的子阶段。 这两个阶段都是Spinnaker所支持存在的。<br>
<h4>CD：Bake</h4>Baking是指在生产时使用当前配置从源代码创建不可变的镜像实例。这些配置可能是数据库更改和其他基础结构更新之类的事情。Spinnaker可以触发Jenkins执行此任务，并且某些组织更喜欢使用Packer。<br>
<h4>CD：部署</h4>Spinnaker自动将已bake的镜像发送到部署阶段。这是将服务器组设置为部署到集群的位置。 与上述测试过程类似，在部署阶段将执行功能相同的过程。首先将部署移至测试阶段，然后最终移至生产环境，以进行批准和检查。这个处理过程可以由Spinnaker等工具支持。<br>
<h4>CD：验证</h4>这也是团队优化整个CI/CD流程的关键位置。因为现在已经进行了如此多的测试，所以失败很少见。但是，此时必须尽快解决所有故障，以最大程度地减少对最终客户的影响。团队也应该考虑使流程的这一部分自动化。<br>
<br>使用蓝绿部署、金丝雀分析、滚动更新等策略部署到产品。在部署阶段，将监视正在运行的应用程序以验证当前部署是否正确或是否需要回滚。<br>
<h4>CD：监控</h4>参与者：站点可靠性工程师（SRE）、运营团队<br>
<br>技术：Zabbix、Nagios、Prometheus、Elastic Search、Splunk、Appdynamics、Tivoli<br>
<br>过程：为了使软件发行版具有故障安全性和健壮性，在生产环境中跟踪发行版的运行状况至关重要。应用程序监视工具将跟踪性能指标，例如CPU利用率和发行版延迟。日志分析器将扫描由底层中间件和操作系统产生的大量日志，以识别行为并跟踪问题的根源。如果生产中出现任何问题，将通知利益相关者以确保生产环境的安全性和可靠性。此外，监视阶段可帮助组织收集有关其新软件更改如何为收入贡献的情报，帮助基础设施团队跟踪系统行为趋势并进行容量规划。<br>
<h3>持续交付（CD）：反馈和协作工具</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210504/d38f8dcb4a486a5604cf46f38f346740.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210504/d38f8dcb4a486a5604cf46f38f346740.png" class="img-polaroid" title="06.png" alt="06.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参与者：站点可靠性工程师（SRE）、运营和维护团队。<br>
<br>技术：JIRA、ServiceNow、Slack、电子邮件、Hipchat。<br>
<br>过程：DevOps团队的目标是更快地持续发布，然后不断减少错误和性能问题。这是通过不时地通过发送电子邮件向开发人员、项目经理提供有关新版本的质量和性能的反馈。通常情况下，反馈系统是整个软件交付过程的一部分。因此，交付中的任何更改都会频繁地录入系统，以便交付团队可以对它采取行动。<br>
<h3>总结</h3>企业必须评估一个整体的持续交付解决方案，该解决方案可以自动化或促进上述这些阶段的自动化。<br>
<br><strong>原文链接：<a href="https://dzone.com/articles/what-is-a-cicd-pipeline">What Is a CI/CD Pipeline?</a>（翻译：张亚龙）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            