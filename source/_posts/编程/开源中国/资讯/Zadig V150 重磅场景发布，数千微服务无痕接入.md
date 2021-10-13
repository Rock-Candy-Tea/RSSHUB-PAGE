
---
title: 'Zadig V1.5.0 重磅场景发布，数千微服务无痕接入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8f133237bd75085a663f20cd4d1388f7c50.png'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 16:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8f133237bd75085a663f20cd4d1388f7c50.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-8f133237bd75085a663f20cd4d1388f7c50.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Zadig V1.5.0 版本来啦！这次版本主要包含拖管项目无痕接入 Zadig ，在不改变现有任何流程情况下，快速获得大规模微服务场景下的环境管理能力，同时加深了对 Helm 部署技术场景的支持力度。当然也包含了不少社区用户反馈的功能优化和缺陷修复。</span><span>亮点介绍：</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#ff2968">支持基于 Kubernetes 的托管项目</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>通过导入现有 Kubernetes 集群的命名空间资源，实现面向不同业务域、不同角色的环境管理。开发者可以快速获得本地联调、服务重启、日志查看、Pod Debug 等能力。通过 Zadig 工作流接入，可以利用自定义镜像缓存提升代码构建效率，并行构建部署多个微服务，实时更新测试环境。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5f2a4d83a4736dbd77a751df26ae3700a0f.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-34173a65c8979bd9f31a138082f0926e9cd.png" referrerpolicy="no-referrer"></p> 
<h3><strong><span style="color:#ff2968">基于 Helm 部署场景的项目</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Helm 是主流的云原生 Kubernetes 应用程序安装和管理工具，Zadig 新增 Helm 类型的项目实现大体量应用的持续交付，解决环境不够用的问题。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-10e9147eaa9478339ff7482718af0906a79.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-7f2c224479b551a89984ae01d210ad20225.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-adb113eb1d7651d3f2a52b55e51142cd2a2.png" referrerpolicy="no-referrer"></p> 
<h3><strong><span style="color:#ff2968">支持自定义镜像格式解析 Helm 部署类型的服务</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Helm 部署类型的服务，系统会解析镜像名为服务组件，除了内置的匹配规则，提供自定义规则做智能匹配。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bbc8c1b2f513e68531069502d40d05880cc.png" referrerpolicy="no-referrer"></p> 
<h3><strong><span style="color:#ff2968">支持集成环境创建自定义命名空间名称</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Zadig 项目中不同的集成环境会使用独立的 Kubernetes 命名空间实现环境和资源的隔离，创建集成环境时用户可自定义命名空间。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-293618c7a02657e2ddfe2b6fe6e8549eb7f.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><strong><span style="color:#ff2968">Zadig V1.5.0 新增功能详情列表</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>功能列表:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持基于 Kubernetes 的托管项目</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持基于 Helm 部署场景的项目  @A一朝醒来已是秋</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持集成环境创建自定义命名空间名称 @lo @t @波</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持自定义镜像格式解析 Helm 服务 @曼小魔</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>缺陷修复:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 Webhook PR 触发测试任务丢失信息的问题  @Nero.Cho  @MI manchi</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复集成 JIRA 系统 URL 解析的“/”问题  @guqs/Slack</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复添加多个共享服务后环境无法更新  @xxqin/Slack</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>系统优化:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化执行工作流时选择分支和 Pull Request 效率</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化操作日志内容</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化数据库性能</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>若干体验优化</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
</ul> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><strong><span style="color:#ff2968">Zadig v1.5.0 Release Note</span></strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Feature:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Load services from helm chart</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Load services from existing kubernetes namespace</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Customize naming rules of environments</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>Customize image analysis rules for services</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Bugfix:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>Jira integration bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Webhook didn't trigger deployment task</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Multiple shared services causing environment unable to be updated</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>Improvements</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>Multiple API performance has been improved</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Lower database QPS.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Improved system operation logs.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>UI/UX improvements</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:16px; margin-right:16px; text-align:left"><span>特别感谢 Partner 为社区提供技术场景。更多详情请参见：Zadig GitHub：</span><span>https://github.com/koderover/zadig/releases/tag/v1.5.0</span></p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><strong><span style="color:#ff2968">关于 Zadig</span></strong></h3> 
<p>Zadig 是基于 Kubernetes 设计、研发的开源分布式持续交付 (Continuous Delivery) 产品，为开发者提供云原生运行环境，支持开发者本地联调、微服务并行构建和部署、集成测试等。Zadig 内置了面向 Kubernetes、Helm、云主机、大体量微服务等复杂业务场景的最佳实践，为工程师一键生成自动化工作流。</p> 
<p>欢迎大家 Star、Fork、 Watch！和众多开发者一起探讨、交流，共建开源社区！</p>
                                        </div>
                                      
</div>
            