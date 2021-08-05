
---
title: 'Zadig 新版本 V1.3.0 来啦：易用性大大提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e86175585e2b93003ae142fc0414796fe22.png'
author: 开源中国
comments: false
date: Thu, 05 Aug 2021 07:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e86175585e2b93003ae142fc0414796fe22.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-e86175585e2b93003ae142fc0414796fe22.png" referrerpolicy="no-referrer"></p> 
<p>Zadig V1.3.0 版本来啦！我们把开源社区用户的反馈进行收集、整理、消化，把一些千呼万唤的功能点给安排上了，该版本核心支持了在 Kubernetes  集群无外网访问情况下的离线安装能力，同时提升了面向诸多云厂商（阿里、腾讯、华为等）的兼容性，在安装流畅度、文档入口、系统易用性方面也做了诸多优化。亮点如下：</p> 
<h3><strong>支持离线安装方案</strong></h3> 
<p>该版本我们新增了对离线安装的支持，目前已经在<strong>多家云厂商</strong>的集群中（阿里云 ACK、腾讯云 TKE、华为云 CCE）测试通过，可以正常离线安装并使用，后续我们将持续优化，提供对更多云厂商的支持。具体使用请参考离线安装文档。</p> 
<h3><strong>云厂商兼容性支持</strong></h3> 
<p>Zadig 面向云厂商 Kubernetes 资源管理、镜像仓库、对象存储做深度兼容，目前已全面支持阿里云、腾讯云、华为云、七牛云等。细节如下：</p> 
<ul> 
 <li> <p>资源管理全面对接阿里云 ACK、腾讯云 TKE、华为云 CCE、其他标准 K8s 集群。</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2df5542fed5af455db17eb15af280d6ad71.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p>镜像仓库完成了对阿里云 ACR、腾讯云 TCR、华为云 SWR、其他标准 Registry 的全面支持。</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9de4606c3f1e36367a5e2e5d3add63addca.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p>对象存储支持标准的 S3 协议，完成了对阿里云 OSS，腾讯云 COS，华为云 OBS，七牛云 Kodo 的全面支持。</p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a37b60c34068270c6d1f3fecb27ed4dd75f.png" referrerpolicy="no-referrer"></p> 
<h3><strong>安装体验及易用性优化</strong></h3> 
<p>我们针对安装过程增加了安装检查步骤和等待页面，进一步优化用户的安装体验。同时调整了文档站首页的结构，方便用户第一时间快速了解试用 Zadig ，同时也新增了 Zadig 教程的入口，供大家学习查阅。</p> 
<p>与此同时，安装配置中新增了兼容性列表。建议准备安装体验 Zadig 的用户，优先了解兼容性信息，提前按照相关信息准备环境，避免浪费时间。</p> 
<p>目前兼容性列表还不是很完善，也欢迎大家一起提交 Pull Request 进行反馈和贡献，让 Zadig 适配更广泛的环境。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-72bbf6da3b0ac4252038009539cac4c3fdc.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-502e4efaa7ade408b7c67d1658d78f361b1.png" referrerpolicy="no-referrer"></p> 
<p> <strong>Zadig V1.3.0 新增功能详细列表</strong></p> 
<ul> 
 <li> <p>针对内网环境用户支持离线安装(有 Kubernetes 集群)</p> </li> 
 <li> <p>支持多家云厂商并通过兼容性测试</p> 
  <ul> 
   <li> <p>代码仓库增加华为代码源 CodeHub 的集成</p> </li> 
   <li> <p>镜像仓库增加华为云 SWR 的集成</p> </li> 
   <li> <p>对象存储增加阿里云 OSS 的支持</p> </li> 
  </ul> </li> 
 <li> <p>易用性优化</p> 
  <ul> 
   <li> <p>系统自动配置代码仓库 Webhook</p> </li> 
   <li> <p>安装优化，增加安装检查和等待页面</p> </li> 
   <li> <p>系统配置模块添加文档站指引</p> </li> 
   <li> <p>Helm 更新环境支持失败时回滚</p> </li> 
  </ul> </li> 
</ul> 
<p>特别感谢以下社区贡献者宝贵建议：</p> 
<p>@lesterhnu @liuflylove666 @jiangpeipei327 @piao100101</p> 
<p><strong>Zadig V1.3.0 Release Note</strong></p> 
<ul> 
 <li> <p>Installation</p> 
  <ul> 
   <li> <p>Improved installation check & guide page</p> </li> 
  </ul> </li> 
 <li> <p>Environment</p> 
  <ul> 
   <li> <p>Automatic environment rollback when helm upgrade failed</p> </li> 
  </ul> </li> 
 <li> <p>System</p> 
  <ul> 
   <li> <p>Webhooks no longer require manually configuration on GitHub/GitLab</p> </li> 
   <li> <p>Codehub integration support</p> </li> 
   <li> <p>Docker registry for HUAWEI cloud (SWR)  integration</p> </li> 
   <li> <p>Fixed a bug which caused Aliyun OSS integration failure</p> </li> 
  </ul> </li> 
</ul> 
<p>Special thanks to the community memmbers for their suggestions: </p> 
<p>@lesterhnu @liuflylove666 @jiangpeipei327 @piao100101</p> 
<h4><strong>关于 Zadig</strong></h4> 
<p>通过在包括头条、腾讯、七牛云、非码等企业的多年上千次迭代，今天的 Zadig 已经成为微服务 + Kubernetes 技术栈团队的最佳研发交付方案，同时无缝兼容任何研发团队现有交付工具链和研发流程，无缝集成 GitHub/GitLab、Jenkins、多家云厂商，帮助团队一步到位打造强大的 DevOps 和 CI/CD 工程基建能力，变云原生为生产力。</p> 
<p>Zadig 本身是基于 Kubernetes 设计、研发的开源分布式持续交付 (Continuous Delivery) 产品，为开发者提供云原生运行环境，支持开发者本地联调、微服务并行构建和部署、集成测试等。Zadig 内置了面向 Kubernetes、Helm、云主机、大体量微服务等复杂业务场景的最佳实践，为工程师一键生成自动化工作流 。</p>
                                        </div>
                                      
</div>
            