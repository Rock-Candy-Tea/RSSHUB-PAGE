
---
title: '新鲜出炉：Zadig v1.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-dc5b6f73cee4c0adf76ae5585c62ff35369.JPEG'
author: 开源中国
comments: false
date: Sat, 17 Jul 2021 07:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-dc5b6f73cee4c0adf76ae5585c62ff35369.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="298" src="https://oscimg.oschina.net/oscnet/up-dc5b6f73cee4c0adf76ae5585c62ff35369.JPEG" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>Zadig 又发版啦</strong></p> 
<p>虽然距离上次 v1.1.0 发版仅 2 周，但本版本我们新添了不少重磅支持，包括：</p> 
<ul> 
 <li> <p>开放对Helm 以及云主机场景的支持，扩展了服务的类型。至此 Zadig 共计支持三种服务部署场景，分别是：Kubernetes、Helm、以及云主机。用户可以根据实际业务需求，去创建适合自己的项目。</p> </li> 
 <li> <p>同时，集成环境新增了环境托管功能，支持用户将现有云厂商的 Kubernetes 环境一键托管在系统，可以统一对服务进行管理和更新，开发者可以非常方便的做服务查看、Pod Debug、实时日志查看。<img alt height="325" src="https://oscimg.oschina.net/oscnet/up-72679419f3709f3f823fb7194444fcdb03f.gif" width="700" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>到目前为止，Zadig 的业务能力已经 100% 开源出去，Zadig 的研发团队将完全基于 Zadig 库进行日常开发和业务迭代，欢迎更多同学加入到开源建设中。</p> </li> 
</ul> 
<p><img alt height="288" src="https://oscimg.oschina.net/oscnet/up-e2bede2374f7d23a5417c549796b28ba25c.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong><strong>Zadig V1.2.0 新增功能详细列表</strong></strong></p> 
<p>项目</p> 
<ul> 
 <li> <p>支持 Helm 服务类型项目</p> </li> 
 <li> <p>支持云主机服务部署类型项目</p> </li> 
</ul> 
<p>集成环境</p> 
<ul> 
 <li> <p>支持 Helm Chart 部署服务</p> </li> 
 <li> <p>支持云主机模式服务部署</p> </li> 
 <li> <p>支持现有云厂商 Kubernetes 环境托管</p> </li> 
 <li> <p>集成环境支持定时回收功能</p> </li> 
</ul> 
<p>系统配置</p> 
<ul> 
 <li> <p>支持主机管理</p> </li> 
 <li> <p>支持多集群管理</p> </li> 
 <li> <p>支持系统配额设置</p> </li> 
 <li> <p>支持 Jira 集成</p> </li> 
 <li> <p>支持 SSO/AD/LDAP集成</p> </li> 
</ul> 
<p>交付中心</p> 
<ul> 
 <li>支持版本管理</li> 
</ul> 
<p>特别感谢以下社区贡献者宝贵建议：</p> 
<p>@nic-6443 @piao100101 @nanzm @solomon-cc @KevinWu0904</p> 
<p><strong>Zadig V1.2.0 Release Note</strong></p> 
<p>New Features</p> 
<ul> 
 <li> <p>Project</p> 
  <ul> 
   <li> <p>Support helm charts based service projects</p> </li> 
   <li> <p>Support virtual machine based service projects</p> </li> 
  </ul> </li> 
 <li> <p>Environment</p> 
  <ul> 
   <li> <p>Service can now be imported from helm charts</p> </li> 
   <li> <p>Service can now be deployed to virtual machine</p> </li> 
   <li> <p>Import environment from existing Kubernetes namespace</p> </li> 
   <li> <p>Scheduled environment recycling</p> </li> 
  </ul> </li> 
 <li> <p>System</p> 
  <ul> 
   <li> <p>Virtual machine management</p> </li> 
   <li> <p>Multi-cluster management</p> </li> 
   <li> <p>Garbage collection for existing workflow task</p> </li> 
   <li> <p>Jira integration</p> </li> 
   <li> <p>SSO/AD/LDAP integration</p> </li> 
  </ul> </li> 
 <li> <p>Delivery Center</p> 
  <ul> 
   <li>Support version management</li> 
  </ul> </li> 
</ul> 
<p>Special thanks to the community memmbers for their suggestions:</p> 
<p>@nic-6443 @piao100101 @nanzm @solomon-cc @KevinWu0904</p> 
<h4><strong>关于 Zadig</strong></h4> 
<p>通过在包括头条、腾讯、七牛云、非码等企业的多年上千次迭代，今天的 Zadig 已经成为微服务 + Kubernetes 技术栈团队的最佳研发交付方案，同时无缝兼容任何研发团队现有交付工具链和研发流程，无缝集成 GitHub/GitLab、Jenkins、多家云厂商，帮助团队一步到位打造强大的 DevOps 和 CI/CD 工程基建能力，变云原生为生产力。</p> 
<p>Zadig 本身是基于 Kubernetes 设计、研发的开源分布式持续交付 (Continues Delivery) 产品，为开发者提供云原生运行环境，支持开发者本地联调、微服务并行构建和部署、集成测试等。Zadig 内置了面向 Kubernetes、Helm、云主机、大体量微服务等复杂业务场景的最佳实践，为工程师一键生成自动化工作流 。</p> 
<p><strong>欢迎参与开源</strong></p> 
<p>_github.com/koderover/zadig |_<em>源码</em></p> 
<p>_koderover.com |_<em>官网</em></p> 
<p>_space.bilibili.com/502473428 |_<em>Bilibili</em></p> 
<p>_zhihu.com/org/koderover |  _<em>知乎</em></p> 
<p>_blog.csdn.net/koderover | _<em>CSDN 博客</em></p> 
<p>欢迎大家 Star、Fork、 Watch！和众多开发者一起探讨、交流，共建开源社区！</p> 
<p><strong>KodeRover</strong></p> 
<p>KodeRover 是开源、分布式持续交付（CD）产品 Zadig 背后的团队，专注于云原生软件交付产品的研发。我们的目标是通过云原生技术的运用和工程产品赋能，打造极致、高效、愉悦的开发者工作体验，让工程师成为企业创新的核心引擎。</p>
                                        </div>
                                      
</div>
            