
---
title: 'Zadig V1.6.0 新版发布：为效率而生，支持全局 Helm & K8s YAML 模板'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-02634f308226649a97f491df25def7dab9c.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 23:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-02634f308226649a97f491df25def7dab9c.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-02634f308226649a97f491df25def7dab9c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong><span>Zadig V1.6.0<span> </span></span></strong><span>经过社区小伙伴的千呼万唤，总算出来啦！</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>这次版本主要包含跨项目级的模版库管理功能，通过全局 Helm Chart 模板、 K8s YAML<span> </span><span>模板</span>、Dockerfile<span> </span><span>模板</span></span><span>，可以快速定义服务</span><span>和生成应用，<strong>减少<span> </span><strong>99%</strong><span> </span>维护工作量<span> </span></strong>，运维工程师<strong>只需配置一次模板</strong>，开发工程师即可<strong>快速定义和部署应用</strong>。</span><span>尤其适合服务体量大，服务配置同构的场景，Zadig 在不破坏原生性的基础上，能够真正实现</span><span>应用交付的</span><span>分层和便利性。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>对于已经初具规模、微服务达到数百甚至上千、使用 Helm 部署的用户也不用怕，Zadig 做了平滑接入，可以毫无心智负担、批量快速导入现有服务，即可获取 Zadig 环境复制和持续交付能力。同时，该版本也包含了不少社区用户反馈的功能优化和缺陷修复。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>以下为 1.6.0 版本亮点介绍：</span></p> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><strong><span style="color:#ff2968">支持全局 Helm、K8s YAML 模版库管理</span></strong></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>将 K8s 资源的 YAML 配置或者部署的 Helm Chart 文件抽象成通用的模板，创建服务时从模板库导入。极致情况下只需 2 步即可成功创建一个服务并应用到集成环境中。</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>第一步：定义服务模板（K8s YAML/Chart）：按需配置自定义变量</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>第二步：生成服务应用到环境：填写变量，保存服务，按需更新环境</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><strong><span>K8s YAML 模板使用示意图：</span></strong></p> 
<p style="margin-left:0; margin-right:0"><img src="https://static.oschina.net/uploads/space/2021/1111/074117_gJYg_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><strong style="color:#333333"><span>Helm Chart 模板使用示意图：</span></strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1111/074134_uD3x_2720166.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><span><strong><span style="color:#ff2968">Helm 部署场景批量导入服务</span></strong></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>对于现有服务配置的管理是<span> </span><strong>Helm Chart 模板 + 每个服务有独立的 values</strong><span> </span>文件这种方</span><span>式，通过Zadig Helm 项目场景批量导入服务，无任何迁移成本，平滑接入 Zadig 系统，获取环境复制和持续交付能力。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0eabc9a19326109f4a6f9409908b7d184e7.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><span><strong><span style="color:#ff2968">支持自定义交付物名称规则</span></strong></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在项目的高级配置中，支持通过以下变量和常量组合的方式生成镜像、TAR 包的名称规则。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9877cdb1ec5d69f724a387c6d86bf668116.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><span><strong><span style="color:#ff2968">云主机场景的交付能力增强</span></strong></span></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>支持批量导入主机列表并分组管理，在自动化部署环节可以批量部署，同时支持主机模式的交付物部署</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e7b5bc7aaf5bef3746f7d6d4a4e5fc6ae0a.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-681bdcc5004a29ab7f4f3e1ae611370c6db.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0"><span><strong><span style="color:#ff2968">Zadig V1.6.0 新增功能详情列表</span></strong></span></h3> 
<p style="margin-left:0; margin-right:0"><span>功能列表：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持全局 Helm Chart 模板库管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持全局  K8s YAML 模板库管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持全局 Dockerfile 模板库管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 Helm 部署场景批量导入配置</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持项目全局配置交付物的自定义名称规则</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持批量导入主机列表并分组管理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 Helm 部署场景的服务搜索和服务编排</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持主机场景的交付物部署 @似水流年</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持托管项目场景不同命名空间托管相同服务 @梦鸽  @Arnold</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>系统优化：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持在构建脚本中使用 commit id 变量</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持托管项目场景展示服务的 ingress 信息</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 Helm 部署场景的配置修改 @段子腾（Slack）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>若干体验优化和交互优化</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>缺陷修复：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修正删除托管项目时的错误提示信息 @梦鸽</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 Ubuntu 16.04 镜像中 Git 版本不支持使用 Pull Request 构建的问题 @guqs（Slack）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 Helm 部署场景显示服务数量不准确的问题</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span><strong><span style="color:#ff2968">Zadig v1.6.0 Release Note</span></strong></span></h3> 
<p style="margin-left:0; margin-right:0"><span>Features:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>Template function for helm charts, yaml, and dockerfile.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Batch load services from helm chart template.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Customizable image tag rules.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Batch load VMs.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Search function for helm services.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Deploy to VMs with artifacts.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Load services of the same name from different namespaces.</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>Improvments:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>Support using commit id in build scripts</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Show Ingress information for loaded services</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Support editing values for helm environment</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>UI/UX improvements</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>Bug fixes:</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>Service count for helm enviroment is now accurate</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Ubuntu 16.04 build image is now able to do git pull correctly.</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Error messages have been changed.</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span>特别感谢开源 Partner 合作伙伴企业为社区提供技术场景。</span></p> 
<p style="margin-left:0; margin-right:0"><span>更多详情请参见 Zadig GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkoderover%2Fzadig%2Freleases%2Ftag%2Fv1.6.0" target="_blank">https://github.com/koderover/zadig/releases/tag/v1.6.0</a></span></p> 
<h3 style="margin-left:0px; margin-right:0px"><strong><span>关于 Zadig</span></strong></h3> 
<p style="margin-left:0; margin-right:0">Zadig 是基于 Kubernetes 设计、研发的开源分布式持续交付 (Continuous Delivery) 产品，为开发者提供云原生运行环境，支持开发者本地联调、微服务并行构建和部署、集成测试等。</p> 
<p style="margin-left:0; margin-right:0">Zadig 内置了面向 Kubernetes、Helm、云主机、大体量微服务等复杂业务场景的最佳实践，为工程师一键生成自动化工作流 。</p> 
<p style="margin-left:0; margin-right:0">欢迎大家 Star、Fork、 Watch！和众多开发者一起探讨、交流，共建开源社区！</p>
                                        </div>
                                      
</div>
            