
---
title: 'DevOps CI_CD流水线设计实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/25eb1336c6d2a737361fe26b90dd7866.jpeg'
author: Dockone
comments: false
date: 2021-11-25 04:09:45
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/25eb1336c6d2a737361fe26b90dd7866.jpeg'
---

<div>   
<br>在不同的环境中，最适合的CICD流水线会有所差异，尤其是在工具链层面，但大致的流程和思路应该是一致的。<br>
<h3>背景</h3>在项目建设初期，架构师要求我们设计一个<strong>DevOps CI/CD持续集成，持续部署/交付</strong>方案，提升生产效率。<br>
<br>通过参考一些业界的最佳实践，结合自身的特点，我们设计了一个较为通用，且能兼顾安全、审批和接管本地已有基础设施与服务的DevOps CICD流水线方案。最后成功落地实施，并在公司内的其它项目中进行了推广。<br>
<h3>什么是DevOps</h3><h4>汽车工业</h4>众所周知，大多数工厂都已经有了产品的自动化生产线。<br>
<br>特别是汽车行业，大约在一百年前，汽车是由人手工制造的，经过多次演变，从手工制造的高度定制的汽车，到手工组装的自动化零件生产，再到目前完全自动化的装配流水线，汽车工业已经具备了精益的自动化制造方案。<br>
<br>与汽车工业相比，我们的传统软件开发模式，已经落后了很多。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/25eb1336c6d2a737361fe26b90dd7866.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/25eb1336c6d2a737361fe26b90dd7866.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>DevOps是一种文化</h4>什么是DevOps?<br>
<br>有些人认为，Devps就是一堆软件和工具的集合，可以用来优化开发和部署。<br>
<br>DevOps不仅仅是这些，它更是一种文化，它更多的是关于团队和组织，强调的是整个团队都应该参与到开发、测试和部署的自动化流程设计中，在出现问题时共同承担责任，协同处理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/7d2b1adf94d83c835feb7869480ac5f5.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/7d2b1adf94d83c835feb7869480ac5f5.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>DevOps工具链与生命周期</h4>DevOps的生命周期从计划、构建、持续集成和部署开始，接着运维，然后反馈和再次计划。围绕在整个生命周期的各个部分，都有很多的应用和服务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/3626b075bfb635c6fd854275ef070687.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/3626b075bfb635c6fd854275ef070687.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>传统的开发模式有哪些缺点</h3><h4>传统制造业的七种浪费</h4>对于传统的制造业来说，非常容易在过度生产、运输、移动、过度加工、等待、库存和产品缺陷等方面浪费大量的时间和资源。因为这些过程大多数仍然需要手工作业，缺乏持续的自动化流程进行管理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/e249053038b96311baed89431330eb45.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/e249053038b96311baed89431330eb45.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>传统软件开发模式的弊端</h4>传统的软件开发模式有以下弊端：<br>
<ul><li>人工干预，人工干预往往会导致难以重复的操作并引入人为错误，尤其是在测试和部署时。</li><li>不一致的环境，导致团队经常浪费几天甚至几周的时间来修复由环境不一致造成的问题，浪费了资源和时间。</li><li>监测不足，依赖于人工监测，很容易造成疏忽，导致部署出现问题，延迟产品的交付时间。</li><li>缺乏共同承担责任，团队成员缺乏共同承担责任的理念，导致在组织中存在各种沟通问题。</li></ul><br>
<br><h3>值得参考的DevOps CI/CD最佳实践</h3><h4>轻量级且简单</h4>由GitLab + Docker + Ansible组成的轻量级、简单的CI/CD流水线解决方案，来自一家快速成长的初创公司。其中，GitLab作为源代码管理和持续集成工具，Docker用于容器，Ansible用于配置即代码。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/8ba1d34f09f054b00e7228afbb784ca7.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/8ba1d34f09f054b00e7228afbb784ca7.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>All on Kubernetes</h4>基于云服务和Kubernetes的CICD流水线，被称为“All on Kubernetes”，比较流行。<br>
<br>但由于“All on Kubernetes”需要确保所有的应用和服务都容器化，因此对比较复杂的环境和传统软件都不友好。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/3bfe766df9281eb2181871f40723969a.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/3bfe766df9281eb2181871f40723969a.jpeg" class="img-polaroid" title="6.jpeg" alt="6.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>IBM DevOps解决方案</h4>IBM的解决方案建议使用DevOps和云平台来帮助企业加速应用开发和交付的生命周期。<br>
<br>这个架构非常完善，包含了DevOps的各个方面。更多详情：<a href="https://www.ibm.com/cloud/architecture/architectures/devOpsArchitecture" rel="nofollow" target="_blank">https://www.ibm.com/cloud/arch ... cture</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/fdd7d0640509ee630645238ebaca95d8.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/fdd7d0640509ee630645238ebaca95d8.jpeg" class="img-polaroid" title="7.jpeg" alt="7.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>端到端的CI/CD流水线</h4>端到端的CICD持续集成和部署交付流水线，包括了IBM DevOps解决方案中的大多数步骤，并且在每个步骤中，都推荐了相关服务和工具。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/71f9debd683c3a6da5609a0bc2225224.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/71f9debd683c3a6da5609a0bc2225224.jpeg" class="img-polaroid" title="8.jpeg" alt="8.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>设计最适合的DevOps CI/CD流水线</h3><h4>DevSecOps</h4>我们最关心的是安全，所以需要DevSecOps，而不仅仅是DevOps。<br>
<br>DevSecOps并非一定要牺牲自动化流程，而是需要加入安全保障过程，在实施变化之前先进行审计。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/229aac52f0b24388b63c5105dd32245e.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/229aac52f0b24388b63c5105dd32245e.jpeg" class="img-polaroid" title="9.jpeg" alt="9.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>开发与测试环境</h4>为了在测试环境中进行安全的开发和部署，以及上传和下载软件包，我们设计了四个网络区域，其中：<br>
<ul><li>在A区域中，可以连接到数据中心和共享服务，如JIRA、GitLab和Nexus。</li><li>在B区域中，可以创建服务器和部署服务。</li><li>在C区域中，可以连接到一些受信任的官方仓库，如Maven，在Nexus中集成安全扫描，如Symantec和Nessus。</li><li>在W区域中，可以在安全扫描和审计下进行开发。</li></ul><br>
<br>通过这些方式，我们可以确保在测试环境中的所有软件包都经过了安全扫描。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/75d387dea57a62a1e8efbcc45143fb51.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/75d387dea57a62a1e8efbcc45143fb51.jpeg" class="img-polaroid" title="10.jpeg" alt="10.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>最适合的端到端DevSecOps CI/CD流水线</h4>最终，我们确定了一个最适合自己的端到端DevSecOps CI/CD流水线。<br>
<br>它包括所有必要的步骤，跨越三个不同的环境，使用最流行的自动化工具和云服务，包括基础设施即代码和配置即代码，与安全工具集成，支持基于测试报告和安全报告的人工审批。<br>
<br>它包括以下内容：<br>
<ul><li>项目管理，构思一个故事，在Confluence上记录，在JIRA上创建任务，将GitLab与JIRA集成。</li><li>代码管理，代码审查，将代码提交到GitLab，然后由GitLab自动触发相关的Jenkins任务，进行代码分析，构建和单元测试，并打包上传到Nexus仓库。</li><li>制品库，通过Nessus自动扫描所有上传到Nexus中的软件包。</li><li>基础设施即代码与配置即代码，检查所需的基础设置是否已经就绪，如果没有，自动创建基础设施，然后将软件包通过配置即代码部署到服务器或Kubernetes集群。</li><li>集成测试与安全测试，对应用服务的可用性和安全性进行测试。</li><li>审计和审批，对整个流水线的各个过程进行安全审计，并在部署上线时进行人为审批，审批通过后自动到下一个环境中进行部署和测试。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/dfe09be78b3f0274cdf7265721e76966.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/dfe09be78b3f0274cdf7265721e76966.jpg" class="img-polaroid" title="AnyConv.com__11_.jpg" alt="AnyConv.com__11_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
最后设计的这个DevSecOps CI/CD流水线比较通用，能兼顾安全，审批和接管本地已有的基础设施与服务。<br>
<br>在此仅供参考，实际上在不同的环境中，最适合的CI/CD流水线会有所差异，尤其是在工具链层面，但大致的流程和思路应该是一致的。<br>
<br>原文链接：<a href="https://blog.heylinux.com/2021/11/devops-cicd" rel="nofollow" target="_blank">https://blog.heylinux.com/2021/11/devops-cicd</a>流水线设计实践/
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            