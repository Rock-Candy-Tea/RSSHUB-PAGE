
---
title: '中国工商银行DevOps工具链建设之路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/eb430bccab4a968d153bd97056740505.png'
author: Dockone
comments: false
date: 2021-03-30 08:09:44
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/eb430bccab4a968d153bd97056740505.png'
---

<div>   
<br>【编者的话】新技术发展迅猛，金融产品和服务模式创新加快，快速增长的产品需求与有限研发资源之间的矛盾长期存在。如何提高研发效能，快速上线业务需求，支撑业务创新发展，是金融机构产品研发部门面临的挑战。传统银行的产品、架构体系庞大复杂，对研发效能提升带来更大挑战，无论流程改进还是工具支撑，都需兼顾现有系统的安全稳定运行。系统建设是在不断重构中向前演进，DevOps工具链建设也是如此。首先要适应当前流程和用户工作习惯，然后工具改进和流程改进同步进行，工具体系不能脱离技术和管理现状，而是要随着技术和管理的优化不断改进。因此打造适合自身的DevOps平台，对传统大型研发企业来说尤为重要。<br>
<h3>DevOps平台探索之路</h3>中国工商银行一直致力于研发效能的提升，从2009年开启了工具化的建设道路，对应用版本构建和部署进行了工具统一，并对构建和部署行为进行了约束及一定程度上的标准化，应用版本构建和部署效率得到了较大提升。2013年开始了持续集成之路，使用Jenkins串联了构建、部署，并推出了代码扫描、单元测试、自动化测试、冒烟、打桩等一系列自动化工具，持续提升版本流转效率。2018年初首先从持续交付工具链开始，启动了DevOps平台建设。经过两年左右的建设，打通了开发、测试、运维，实现了版本构建、质量保证、交付、交接及投产部署的自动化、线上化。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/eb430bccab4a968d153bd97056740505.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/eb430bccab4a968d153bd97056740505.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>DevOps平台建设成果</h3>中国工商银行的工具链总视图主要包括开发者门户、持续交付流水线、运维平台等。开发者门户是工具链的“一站式”门户，为开发人员提供统一的操作入口；持续交付流水线打造了产品研发、质量保证、投产部署的价值交付链，通过Jenkins将各项基本服务串接起来；运维平台统筹生产运维、应用监控、性能容量等领域，为投产上线、日常运维提供服务。<br>
<h4>概要视图</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/e04f37b72540ed8d0910d16939e881ee.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/e04f37b72540ed8d0910d16939e881ee.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>开发者门户</h4>基于现有系统和工具进行集成、整合、创新，建设面向开发人员的门户，实现从需求受理到版本发布的一站式、可回溯、自动化处理。通过信息聚合，实现需求维度的端到端研发支撑体系，将局部能力整合为组织级能力，通过标准化的流程、自动化的体系，提升研发流程的自动化程度。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/33a80d4b23b8bf94d8729befe261102e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/33a80d4b23b8bf94d8729befe261102e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>流水线</h4>中国工商银行搭建了一套适合我行版本管理流程的自动化版本持续交付系统，实现版本的持续集成、持续交付、持续部署。通过流水线，单个应用完成构建、部署、冒烟测试的周期缩短至2小时，部署时间缩短至0.5小时，目前已在各产品线全面推广使用。<br>
<br>通过持续交付系统贯通各个环节，将软件交付过程通过可视化的方式呈现给用户，展现了从代码提交、代码扫描、构建、部署、自动化测试、交付的整个过程可视化，降低协作沟通成本。<br>
<ul><li><br>提交构建流水线：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/256d65014c0e8a807adf812914f5ba21.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/256d65014c0e8a807adf812914f5ba21.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><br>持续集成流水线：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/5af8a57c91bc50831a95ed544cbb2df6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/5af8a57c91bc50831a95ed544cbb2df6.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><br>交接部署流水线：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/f5354d45239056dd37779d9d2670728f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/f5354d45239056dd37779d9d2670728f.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br><h4>质量门禁</h4>提交构建流水线（“第一次就做对”）：在开发提交代码变更时自动触发流水线执行，检测开发人员本次代码提交的质量，例如代码扫描是否有高级别的问题、单元测试行覆盖率是否达到一定的标准，协助开发者发现问题，并提醒修改，各指标必须达标才能将代码合入主干，降低发现问题和解决问题的成本。<br>
<br>持续交付流水线（“交付准出门禁”）：多人代码合并到主干后，对主干分支开展代码扫描、构建、部署、自动化测试等环节并获取测试结果，在提交构建门禁基础上增加了冒烟测试成功率指标，所有指标达标才能将版本交付出去，确保交付质量。所有门禁指标分级制定，给团队成长的台阶。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/e7a183c899bc3ae905c98a20e957ad21.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/e7a183c899bc3ae905c98a20e957ad21.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>运维平台</h4>统一的生产运维平台，集生产运维、应用监控、性能容量等于统一门户，为投产上线、日常运维提供服务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/694327a07ddb69bbe8b41349e1cafafa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/694327a07ddb69bbe8b41349e1cafafa.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>标准化建设</h3>通过两年多的DevOps实践，逐步暴露出应用代码管理、版本构建、生产部署等领域的标准化程度不足，制约了工具平台的自动化、智能化提升。2020年，工商银行建立了交付过程的标准化技术规范，同时对工具链和各系统进行标准化重构。目的是降低系统使用门槛，赋能产品研发团队。<br>
<h4>聚集流动效率</h4>目标实现真正意义上的自助化，降低操作门槛，减少手工介入。由开发团队驱动版本全流程运转，真正实现“谁开发，谁运维”，配置管理、测试、运维工具提升，各类运维服务自供应。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/66fcf61fb57ffe4e8ade36a9c46d5f8e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/66fcf61fb57ffe4e8ade36a9c46d5f8e.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>标准化发布单元</h4>标准化改造是对当前版本管理的一次重新定义，需要试点应用结合业务架构、应用架构的充分解耦，对代码库组织、构建方式、部署目录结构、应用环境定义等进行标准化改造。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/2a158634920a010b9701131c5c3de2da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/2a158634920a010b9701131c5c3de2da.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>构建、部署即代码；构建、部署过程云化</h4>以“构建部署过程即代码”为目标，即构建、部署过程使用标准的yaml文件描述构建定义。通过构建、部署分层的构建云、部署云建设分模块、分层级的标准化工具。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/4f1e0bd013ed772500e56831742a5b8d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/4f1e0bd013ed772500e56831742a5b8d.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>组件化流水线</h4>标准化组件接入，设立组件接入规范；重构流水线以达到灵活可编排，“横向可定制流程，纵向可定制任务”。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/3815ecd98c1dc03cc4696aa027b48e47.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/3815ecd98c1dc03cc4696aa027b48e47.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>度量平台</h4>可视化与度量：基于各系统数据打通，以可视化赋能研发改进，多维度、可定制、全程透明，不同角色，各取所需。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/6f0d8426def078e4ab66f5fa667f1a4a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/6f0d8426def078e4ab66f5fa667f1a4a.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>全功能视图</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210328/f98ca51a53b05f0bae94b5798199fc2a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210328/f98ca51a53b05f0bae94b5798199fc2a.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>未来展望</h3>目前整个DevOps工具链的建设，还是遵循既有工作流程。随着工具的完备，流程会逐步发生转变，很多管控环节的要求将会消失，同时对工具平台会提出更高的要求，工具体系将进入良性循环。我们希望通过不断完善工具支撑，不断消减人工介入，最终将发布和运维的能力赋予产品团队，让产品团队从交付版本向交付用户可使用的服务转变。同时，进一步加强运维和开发的融合，未来要以SRE思想推动运维转型，通过一系列DevOps工程建设和方法落地，打造自动化、自助化、智能化的DevOps平台，降低软件交付门槛，赋能产品团队，实现开发和运维深度融合，助力IT效能提升。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/qqOHrc4QWc4wnNO3sS8BXg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/qqOHrc4QWc4wnNO3sS8BXg</a><br>
作者：龚光庆，中国工商银行软件开发中心总经理助理
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            