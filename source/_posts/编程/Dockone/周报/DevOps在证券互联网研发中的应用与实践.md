
---
title: 'DevOps在证券互联网研发中的应用与实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/98c5878407f76bb0e0dee2fd9e0e8760.png'
author: Dockone
comments: false
date: 2021-11-21 01:52:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/98c5878407f76bb0e0dee2fd9e0e8760.png'
---

<div>   
<br>近些年金融科技在证券行业发挥的作用越来越重要，运用金融科技赋能业务发展，通过个性化服务构建护城河，将金融科技与业务创收和降本增效相结合开始成为证券从业人员所关注的问题，如何提升研发交付效率、小步快跑、快速迭代是所有证券行业科技研发团队共同关心的话题。敏捷为快速迭代提供了理论思想和方法指导，DevOps为敏捷落地提供了补充和工具支持。<br>
<br>中泰证券股份有限公司互联网研发团队通过对DevOps相关理论和技术的研究、分析，设计并实现了蜂鸟效能管理平台。通过蜂鸟效能管理平台实现了编码后续研发环节的降本增效。DevOps是一套创新且有效的文化和思想，本平台借鉴其中的持续集成、持续交付和持续运营的关键思想，并结合互联网研发过程遇到的实际情况，解决了研发、测试和运维等角色沟通协作中遇到的一系列问题，实现了产品多环境交付、流程可视化、测试自动化、运维智能化、流程规范化和效能指标可视化等功能。蜂鸟效能平台上线后的应用实践结果表明，通过运用DevOps相关理论和技术能够提升互联网研发在市场快速变化的过程中实现产品应用的快速迭代，从而达到减少产品试错与迭代过程中的时间成本和技术人力成本，为公司业务创收提供技术保障的目的。<br>
<h3>背景及意义</h3>DevOps因其先进性和全面性，已被认为是软件工程的第三次革命；由PUPPET和DORA联合发布的《2017 State of DevOps Report》报告中，故障恢复时间缩短了96倍，业务需求从提出到投产的周期从3个月到6个月缩短到3周甚至更短，使得企业更好适应市场变化。DevOps已经被证实能在IT和商业两方面提升效率。<br>
<br>DevOps定义：DevOps（Development和Operations的组合词）是一组过程、方法与系统的统称，用于促进开发（应用程序/软件工程）、技术运营和质量保障（QA）部门之间的沟通、协作与整合。它是一种重视“软件开发人员（Dev）”和“IT运维技术人员（Ops）”之间沟通合作的文化、运动或惯例。透过自动化“软件交付”和“架构变更”的流程，来使得构建、测试、发布软件能够更加地快捷、频繁和可靠。它的出现是由于软件行业日益清晰地认识到：为了按时交付软件产品和服务，开发和运维工作必须紧密合作。特别是敏捷迭代已经成为金融行业研发团队的主流研发模式，这对开发、测试、运维提出了更高效的要求。<br>
<br>中泰证券互联网研发团队采用敏捷研发模式进行团队间的协作，敏捷的实施需要通过小迭代形式不断的交付应用产品。敏捷开发驱动开发人员更快的交付代码，新的代码需要被更快的测试，并需要频繁的被部署到开发、测试和生产，由于运维和测试不能尽快的参与到软件开发生命周期，导致交付流水线阻塞的情况，而通过DevOps的运用很好解决了这些问题。<br>
<br>在DevOps实施的过程中，涉及的角色主要包括开发、测试（质量）、运维三个角色，见下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/98c5878407f76bb0e0dee2fd9e0e8760.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/98c5878407f76bb0e0dee2fd9e0e8760.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1 开发、测试（质量保证）、运维</em><br>
<br>其中研发主要关注产品研发的高效、稳定、快速的实现，以及对应的产品开发完成后，交付制品对应上线时间点能够可预期；运维则更多的关注如何通过自动化运维和持续监控等工具降低产品上线后的维护成本；测试（质量保障）角色则关注研发提交过来的产品能够尽快的得到测试，因此在提高质量保障效率的过程中，该角色更多的关注产品的持续自动化测试，以及产品交付质量的提升。而DevOps实现了将研发、运维和质量三个角色统一起来，实现了研发、运维和质量的一体化，同时通过持续集成和持续交付的能力，使运维人员更早的参与到产品的交付过程中去，减少了不同角色之间的交付壁垒。<br>
<br>综上所述，尽管新工具思想的推进在一定程度上能够提升产品的交付效率，但由于企业自动化程度低、软件开发流程的不规范导致的交付效率慢、交付流程不规范、线上故障反映不及时、运营数据获取困难等问题的存在，使企业在实际的产品交付过程中依然不能实现快速交付有价值的产品给用户。这就需要一个平台解决以上问题，但是目前市面上已有的相关产品存在不能和流程结合以及不支持混合制品(容器和非容器)的持续集成与持续交付，且不能获取实际场景的业务数据。因此，一个能够解决当前困境的统一自研DevOps平台变得尤为重要。<br>
<h3>中泰证券DevOps蜂鸟效能平台整体功能规划</h3>蜂鸟效能平台是一个以DevOps相关理念为指导思想，结合证券行业安全、合规等需求特性实现的一个集多环境（开发、测试、预发布、生产）持续集成(CI)/持续发布(CD)、代码质量检测、自动化测试、上线流程审批、研发效能数据跟踪及报表统计的综合效能管理平台。通过蜂鸟效能平台在互联网研发过程中的应用，提升了互联网研发在市场快速变化的过程中实现产品应用的快速迭代，从而达到减少产品试错与迭代过程中的时间成本和技术人力成本,并为公司业务创收提供技术了保障的目标。<br>
<br>依托DevOps相关理念，结合当前互联网技术中最前沿的容器化技术、容器编排管理kubernetes、微服务架构、配置中心、静态代码扫描、接口管理和自动化测试（UI、接口、安全、性能）等技术，蜂鸟效能平台实现了具有持续集成、持续交付和持续运营能力的统一综合效能管理平台，各阶段详细技术如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/d228ac7d8e4d23aceba6a96db0077e68.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/d228ac7d8e4d23aceba6a96db0077e68.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2 蜂鸟效能平台技术架构</em><br>
<br>蜂鸟效能平台整体技术架构划分为三层，最底层为基础设施层，该层主要为各混合云环境下的基础环境，如私有云、华为云、阿里云和行业云等环境下的开发、测试和生产环境，建立在基础层之上搭建了支撑平台的工具，形成了平台的工具层，如需求管理Jira、代码管理Git、构建依赖工具、单元测试Junit、代码扫描工具、制品管理工具、自动化测试工具（接口、UI、安全）、配置管理工具、应用部署工具、容器管理Kubernetes和监控工具等，通过工具层提供的能力，建立并实现了价值流层，价值流层对应的功能直接为对应的职能化人员赋能，主要为持续集成、持续交付和持续运营等功能。<br>
<h3>蜂鸟效能平台相关技术节点简介</h3><h4>与项目管理平台Jira集成</h4>为了将具体需求与迭代上线进行对应，从而达到系统上线需求可追踪，同时也为后续对需求进行价值分析提供基础数据，因此需要将项目管理平台JIRA与蜂鸟效能平台持续交付进行打通。研发人员在蜂鸟效能平台进行提测和发布上线时可以根据提示选择对应的STORY，从而完成提测、上线与JIRA项目的关联打通。<br>
<h4>代码管理及构建</h4>代码的科学管理对团队高效协作以及流程规范具有特别重要的作用，蜂鸟效能平台采用Git作为代码管理工具。GitFlow模式是若干模式的集大成者，包含一个主干分支、一个开发分支、许多的特性分支、许多的发布发布分支和Hotfix分支，以及许多的合并规则，通过GitFlow模式的运用，能够解决开发过程中大部分代码协作的问题。同时通过分支的管理，也为后续开发环境的CI/CD奠定了基础。<br>
<h4>制品库管理</h4>蜂鸟效能平台的制品仓库在持续交付的过程中扮演着中转站的作用，如何结合制品仓库实现制品在不同环境中的流转对保持制品交付前后的一致性与可追溯性有着重要的作用。对于当前的制品主要分为Docker镜像类和非镜像类制品，为了能够对Docker镜像类进行管理，镜像仓库采用开源Harbor进行管理，对于非镜像类制品采用Artifactory进行管理，为了能够达到环境流转的效果，采用基于仓库的不同账号之间的权限管理方案，具体见关键模块方案。对于唯一性问题，容器类制品采用镜像id非容器类制品采用MD5码保证制品的唯一性。<br>
<h4>接口管理</h4>蜂鸟效能平台接口管理功能对于不同的研发角色作用不同，开发人员能够利用接口管理功能进行前后端接口调用、多项目接口统一管理、接口调试和多团队协同开发；测试人员能够基于接口管理功能中登记的接口进行简单接口测试、场景化接口测试；运维人员可以基于接口管理功能中登记的接口实现业务监控；产品人员可以快速进行数据统计。<br>
<h4>配置中心</h4>蜂鸟效能平台的配置中心能够实现对不同环境、多云环境的系统参数配置进行管理，同时配置中心也是多环境（开发、测试、仿真、生产）CI/CD的关键。蜂鸟效能平台的配置中心基于Apollo实现，Apollo是一个开源的分布式配置中心，能够集中化管理应用不同环境、不同集群的配置，配置修改后能够实时推送到应用端，并且具备规范的权限、流程治理等特性，适用于微服务配置管理场景。配置中心实现了开发、测试、生产多环境的系统参数配置功能，同时支持多云架构下的分布式系统配置管理。配置中心为CI、CD的平滑交付提供了技术保障。<br>
<h4>单元测试、静态代码扫描及开发环境CI/CD</h4>单元测试能够让开发人员在提测前发现新增变动对系统可能造成的不利影响，并通过将单元测试与开发环境CI/CD进行结合，当开发人员进行代码提交或者进行代码merge时将触发自动单元测试并将结果反馈给对应研发人员。<br>
<br>为了提高研发过程中的代码质量并尽快发现已有系统代码中存在的漏洞缺陷，蜂鸟效能平台提供了静态代码扫描功能，静态代码扫描功能可以对研发人员的代码进行分析并进一步提升编码规范。静态代码扫描功能需要能够识别代码中一些常见的漏洞，如资源类问题（资源释放、无效指针等）、安全性要求（数据污染、注入等）、潜在的缺陷（数组越界、初始化、除零错误、空指针引用等）、多线程和同步性（双重锁定、未释放的锁等）和异常处理（NullPointerException）等。静态代码扫描平台采用增量扫描和全面扫描相结合的方式，日常开发对于不断的代码提交采用自动增量扫描，便于快速发现新增代码中的缺陷，同时结合定时全量扫描和提测前全量扫描的方式，发现代码中所有的缺陷，只有当高危、中危、低危等级的缺陷全部修复完后才能由开发人员在蜂鸟效能平台上提测版本给测试人员，提升了开发人员提测版本的质量和安全性。<br>
<br>静态代码扫描关键截图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/b3e040e37e04f39c6856990446ab5b69.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/b3e040e37e04f39c6856990446ab5b69.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3 静态代码统计分析</em><br>
<br>通过静态代码扫描的报告详情，能够查看当前项目的缺陷情况，同时通过缺陷展示快速定位缺陷位置。<br>
<h4>自动化测试及测试环境CI/CD</h4>蜂鸟效能平台的自动化测试功能实现了互联网研发团队测试人员的效率飞跃，通过将自动化测试平台与持续交付的流程进行结合大大提升了测试效率。在蜂鸟效能平台上，测试人员能够看到研发人员提测的具体内容，并识别出具体的制品版本及唯一码，测试人员可以在蜂鸟效能平台上对开发人员提测的版本进行一键部署和一键自动化测试，最后测试的结果将以报告的方式反馈给研发人员。<br>
<br>通过蜂鸟效能平台的接口管理功能与自动化测试功能的集成。目前已经支持UI及接口自动化测试。UI自动化基于Appium框架实现，Appium要能真正自动化手机上的应用必须依赖于各个移动平台所带的自动化框架；IOS平台目前依赖于XCUITest实现，安卓目前主要依赖于uiautomator。框架提供的是运行库，运行库运行在移动设备上。<br>
<br>AppiumServer服务起来后会在移动设备上安装一个帮助自动化的应用，可理解为“控制许可”或者“代理”应用，通过这样应用可以编译我们自动化给出的指令，然后按指令测试移动设备上的应用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/d5defba59dae89eedd5af4d67051aedf.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/d5defba59dae89eedd5af4d67051aedf.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4 UI自动化流程</em><br>
<br>蜂鸟效能平台的接口自动化功能基于接口分层测试设计的思想，采用python+unittest+ddt框架自研实现。把测试数据与测试代码完全分离，将数据操作、用例配置、日志记录、接口请求等公用方法封装成单独类，使用DDT数据驱动工具管理每个接口的多种测试场景，使用unittest组织、执行多个接口的测试用例集合，通过添加多种断言形式，如接口的状态码、返回值、差异化（diff）对比等对接口测试结果进行判断，最后通过HtmlTestRunner生成测试报告，把返回的测试结果用图形和文本形式形象的展现出来。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/6fa46930dba0bf1a7ed6e4f32998eac7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/6fa46930dba0bf1a7ed6e4f32998eac7.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5 接口自动化体系</em><br>
<br>接口自动化测试功能是DevOps实践中不可或缺的一部分，具备持续测试能力，提升了测试效率，使测试人员快速适应敏捷开发工作模式，从而减少了产品迭代过程中的时间成本和技术人力成本，为产品快速迭代和发布提供了质量保障。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/66114d8548cacdc7ba2102dcbd2edcff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/66114d8548cacdc7ba2102dcbd2edcff.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6 接口自动化流程</em><br>
<br>通过自动化测试与CI/CD相结合，提升了测试效率与制品交付速度。<br>
<h4>安全测试</h4>蜂鸟效能平台将安全扫描评估系统融入到自动化流程中，实现研发人员自助式安全扫描测试。安全扫描评估系统是一套能够通过对系统整体架构进行扫描，从而发现系统整体架构中可能存在的安全漏洞和容易遭受网络攻击与计算机病毒攻击等风险。安全扫描评估系统会对具体的安全漏洞风险进行分析并给出具体的报告建议。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/4c8255cefeec406c0aa9c39be7eb0a86.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/4c8255cefeec406c0aa9c39be7eb0a86.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7 安全扫描漏洞分布报表</em><br>
<br>通过将安全扫描评估系统的安全扫描能力前置，在整体安全扫描效率上极大提升了研发的安全风险意识，并提高了安全漏洞的处置效率。<br>
<h4>CI/CD流水线整体设计</h4>蜂鸟效能平台CI/CD功能主要包括静态代码扫描、开发环境CI/CD、测试环境CI/CD和自动化测试、上线流程审批、生产环境CI/CD、交付制品的环境流转等功能。其中应用产品的制品在各环境中详细流转逻辑图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/dec9551f769b57f740d409863e5c1fa9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/dec9551f769b57f740d409863e5c1fa9.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图8 CI/CD流程</em><br>
<br>从上图可知，制品在多环境CI/CD流转的过程中，主要包括三个环境的流转，分别为开发环境、测试环境和生产环境，其中开发环境采用自动构建、自动集成和自动部署的方案，测试环境的流转与发布根据技术经理在蜂鸟效能平台上的提测，测试组人员可以根据自身需要进行按需自动化发布部署，发布部署完成后，可以对相应的功能模块进行自动化测试。制品在生产环境的流转与发布方式和测试环境的发布部署方式类似，在蜂鸟效能平台上走完审批流程后根据实际需要，运维人员按需自动化发布部署。蜂鸟效能平台实现了线上审批流程和测试、发布操作的关联控制，保证每次提测和发布上线都有严格的流程把控。<br>
<br>其中对于容器化应用各环境流转发布部署细节如下：<br>
<br>1、开发环境镜像生成与发布：在Gitlab上创建工程后，研发人员可以自助在平台上对该Gitlab工程绑定自动构建和部署模块，当该工程主分支发生branch合并时触发自动构建，镜像创建后，会将对应的镜像推送到镜像仓库，然后再触发自动化部署脚本将该镜像自动部署到开发环境。<br>
<br>2、测试环境下的镜像流转与发布：在开发人员将对应的需求开发完后，在蜂鸟效能平台上进行应用产品提测，提测后测试组能够在蜂鸟效能平台上的测试模块看到提测的具体镜像内容，根据提测详情，可以实现一键自动部署，然后再对测试环境的镜像进行自动化功能、接口、性能和UI测试。<br>
<br>3、生产环境下的镜像流转与发布：在走完产品上线流程审批后，运维人员能够在蜂鸟效能平台上看到具体的上线流程信息，根据实际情况进行自动化发布部署、回滚和复核。<br>
<br>通过CI/CD流水线，使产品、UED、研发、测试、运维和合规等职能化角色可以在其对应职责的权限下完成产品上线过程中对应的具体操作，如测试人员完成自动化测试操作、运维人员完成自动化部署操作和合规人员完成合规审核操作等，最终达到产品交付的目的。同时蜂鸟效能平台隔离了开发、测试、生产环境，对应的角色只能在对应的环境进行操作，操作环境的隔离符合《证券基金经营机构信息技术管理办法》的相关要求。<br>
<br>4、提测及上线流程跟踪如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/50ddf759f66d05835c8177b956752134.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/50ddf759f66d05835c8177b956752134.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图9 提测流程详情</em><br>
<br>该图为一个提测、上线发布流程部分截图，各职能化角色都有参与到该流程中，开发人员提测、测试人员执行测试、技术经理确认上线发布、产品经理发布前验收、产品及技术负责人确认上线、合规确认发布流程、运维人员A执行发布、运维人员B复核发布、业务部门生产验收。<br>
<h4>混合云管理及生产发布</h4>在真实的部署环境中，经常涉及多云环境下的发布管理，为了实现多云环境下的制品流转及发布部署，蜂鸟效能平台实现了一套混合云环境的发布管理功能。<br>
<br>中泰证券互联网应用系统的部署环境为一个混合云场景，蜂鸟效能平台通过对混合云环境资源的整合，解决了混合云环境的CI/CD发布部署和系统监控问题，具体方案如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/2cc41c0157c958173cc3a6accba5d1af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/2cc41c0157c958173cc3a6accba5d1af.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图10 混合云多云环境部署</em><br>
<br>通过该方案与CI/CD制品流转设计相结合，使研发人员交付的应用制品可以通过蜂鸟效能平台实现多环境流转，最终发布部署到混合云的环境中去。<br>
<h4>自动化监控及技术运营</h4>为提升线上问题和故障的发现、反馈效率，蜂鸟效能平台集成了自动化监控功能，自动化监控能够提高运维的效率，并能够满足频繁发布部署过程中的应用监控问题，通过对应用服务的自动化监控与故障自愈相结合能够在用户无感知的情况下修复线上故障，同时在蜂鸟效能平台上对线上故障数据进行跟踪收集分析，达到尽快反馈给研发人员并能够对故障回溯具有参考作用。<br>
<h4>效能指标跟踪及改善</h4>效能指标能够体现研发过程的实施情况，客观的效能数据可以对我们研发改进起到指导效果，没有客观数据和成功标准就无法做到持续反馈和持续改进。蜂鸟效能平台中关键效能指标见下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/0670f4f2d60c816aab6c7c81c2824a0e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/0670f4f2d60c816aab6c7c81c2824a0e.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图11 效能数据</em><br>
<br>研发效能数据多维度展示产品交付各阶段的数据，如开发阶段的代码数据统计、测试阶段的自动化测试数据统计、运维上线后的故障数据统计等；其中流水线指标从交付效率和吞吐率两方面主要反映研发过程整体效能情况；项目/需求指标能够从需求的成本和上线后的价值两个角度对需求进行价值数据衡量；研发指标反映了当前研发人员的工作负荷以及产出及质量情况；测试指标对产品质量保证具有关键指导的作用；运维指标能够反映运维工作效率的情况，如线上故障情况及功能上线发布效率。蜂鸟效能平台通过多维度对不同交付阶段进行数据跟踪并绘制全面的图表对全过程进行效能分析。<br>
<h3>总结</h3>中泰证券互联网研发团队基于DevOps思想构建的蜂鸟效能平台上线以来，接入项目模块220多个，支持容器及非容器应用，经过累计21万+次的CI/CD(持续集成/持续交付)，已经成为目前互联网研发过程中不可或缺的核心研发工具平台。带来的价值如下：<br>
<br>1、规范研发过程，实现安全可控<br>
<br>蜂鸟效能平台将开发、测试、生产环境进行了有效隔离，实现了各环节操作的安全可控及合规。所有的发布操作均通过蜂鸟效能平台留痕并且操作绑定流程制度，做到了问题可追溯、减少了误操作、操作符合公司IT管理规定。<br>
<br>2、提升交付效率，缩短交付时间<br>
<br>蜂鸟效能平台旨在缩短开发人员完成功能代码编写到生产发布过程中的时间消耗，提升研发交付效率。<br>
<br>缩短了开发时间周期，通过静态代码扫描可以在10~20分钟内实现对一个应用系统的代码检查，提升了开发人员CodeReview的效率。每个迭代的时间缩短0.5~1天。<br>
<br>缩短了测试时间周期，全功能回归测试从2~3天人工测试降低到自动化测试6~8小时。每个迭代的时间缩短2天左右。安全自动化测试，从3到5天人工进行，到目前的自助式服务30分钟。减少了等待3到5天。<br>
<br>缩短了各环节流转的时间，蜂鸟效能平台自动化CI/CD次数自上线以来达到21万+次，已经实现了从开发人员提交代码到生产发布过程中的自动化，节约了大量的人力成本。其中各环境下的发布部署改造前后具体参考图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211117/8a1279126a0036265263173a453f608a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211117/8a1279126a0036265263173a453f608a.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图12 CI/CD实施前后数据分析</em><br>
<br>从上图可知，通蜂鸟效能平台的实现与应用，使应用制品在开发、测试和运维阶段的发布部署过程中，对应的发布部署效率提升10倍以上。<br>
<br>3、提升交付质量，减少线上故障<br>
<br>静态代码扫描可以识别一定的代码逻辑设计、编码缺陷及安全漏洞，减少了程序问题导致的生产问题。<br>
<br>应用发布过程中，应用包在开发、测试和生产的环境流转过程中，应用包不用重新编译打包，实现了同一应用包多环境流转，系统、业务配置参数通过配置中心读取，减少了因为应用包变更和参数配置问题导致的生产发布问题。<br>
<br>通过容器化技术实现了各环境对应用的隔离性和封装性，减少了因为开发、测试、生产环境的差异性导致的生产发布问题。<br>
<br>4、减少了人力资源投入，节省了研发成本<br>
<br>在测试能力提升方面，目前自动化测试已经覆盖核心业务用例80%以上,核心业务主要为集中交易、两融、期权、理财、条件单、银证转等核心业务，通过自动化测试回归后保障线上无交易类业务生产故障。2020年下半年加强了自动化测试能力建设，通过自动化测试减少了人力资源投入，目前自动化测试团队6人，2020年自动化测试累计节省16人/年。UI回归次数安卓和iOS共回归65次，每次执行用例2500+，按照每人每天可执行55条计算，共节省约11人/年；接口自动化回归529次，按每人每天40接口计算，共节省约5人/年。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/_nD57Hvpb5fUAb3g8hDUEg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/_nD57Hvpb5fUAb3g8hDUEg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            