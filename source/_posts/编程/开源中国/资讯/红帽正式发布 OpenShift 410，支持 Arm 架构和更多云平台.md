
---
title: '红帽正式发布 OpenShift 4.10，支持 Arm 架构和更多云平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cb3fe1d581daed3d6981352be22b5ebf759.png'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 07:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cb3fe1d581daed3d6981352be22b5ebf759.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>红帽上个月正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcloud.redhat.com%2Fblog%2Fintroducing-red-hat-openshift-4.10" target="_blank">发布</a>了 OpenShift 4.10，新版本使用 <span style="background-color:#ffffff; color:#151515">CRI-O 1.23 运行时和 </span>Kubernetes 1.23、增加了对 AI 的支持以及 NVIDIA AI Enterprise 2.0 认证、使用更智能的 OpenShift 控制台、支持 Arm 架构和更多的公私有云平台、沙盒容器 (OpenShift Sandboxed Containers) 正式 GA。</p> 
<p>红帽没有公开发布 OpenShift Container Platform 4.10.0，而是发布了<strong> OpenShift Container Platform 4.10.3</strong> 作为 GA 版本。OpenShift Container Platform 4.10 需要运行在 Red Hat Enterprise Linux(RHEL)8.4 和 8.5 上，以及 Red Hat Enterprise Linux CoreOS 4.10 上。</p> 
<hr> 
<p><strong>沙盒容器</strong></p> 
<p><span style="background-color:#ffffff; color:#222222">沙盒容器 </span>(OpenShift Sandboxed Containers) <span style="background-color:#ffffff; color:#222222">为具有严格应用级安全要求的工作负载提供可选的额外隔离层。OpenShift在断开连接或气隙设置中也进行了改进，简化了断开连接的 OpenShift 集群的安装过程。从而简化了 OpenShift 镜像的维护，并使镜像保持最新状态，就如同它们是一个互相连接的集群一样。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cb3fe1d581daed3d6981352be22b5ebf759.png" referrerpolicy="no-referrer"></p> 
<p><strong>支持 Arm 架构</strong></p> 
<p style="color:#252525; margin-left:0; margin-right:0; text-align:left">OpenShift Container Platform 4.10 现在<strong>支持基于 AWS EC2 A1 和裸机平台的 ARM</strong>。实例可用性和安装文档包括在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faccess.redhat.com%2Fdocumentation%2Fen-us%2Fopenshift_container_platform%2F4.10%2Fhtml-single%2Finstalling%2F%23supported-installation-methods-for-different-platforms" target="_blank">不同平台支持的安装方法</a>。</p> 
<p style="color:#252525; margin-left:0; margin-right:0; text-align:left">ARM 上的 OpenShift Container Platform 支持以下功能：</p> 
<div style="text-align:left"> 
 <ul style="list-style-type:disc"> 
  <li>OpenShift 集群监控</li> 
  <li>RHEL 8 Application Streams</li> 
  <li>OVNKube</li> 
  <li>AWS Elastic Block Store(EBS)</li> 
  <li>AWS .NET 应用程序</li> 
  <li>裸机上的 NFS 存储</li> 
 </ul> 
</div> 
<p style="color:#252525; margin-left:0; margin-right:0; text-align:left">ARM 上的 OpenShift Container Platform 支持以下 Operator：</p> 
<div style="text-align:left"> 
 <ul style="list-style-type:disc"> 
  <li>Node Tuning Operator</li> 
  <li>Node Feature Discovery Operator</li> 
  <li>Cluster Samples Operator</li> 
  <li>Cluster Logging Operator</li> 
  <li>Elasticsearch Operator</li> 
  <li>Service Binding Operator</li> 
 </ul> 
</div> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-01aa388eaf447bfe0e2fb87705ccfda2690.png" referrerpolicy="no-referrer"></p> 
<p><strong>更智能的 OpenShift 控制台</strong></p> 
<p>新版本改进了控制台，优化了开发者体验，主要变化：</p> 
<ul> 
 <li>显示集群支持级别</li> 
 <li>支持动态插件（技术预览阶段）</li> 
 <li>支持在调试模式下运行 pod</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.10%2Fcicd%2Fpipelines%2Fop-release-notes.html" target="_blank">OpenShift Pipelines</a><span style="background-color:#ffffff; color:#151515"> as code（技术预览阶段）</span></li> 
 <li>使用 <span style="background-color:#ffffff; color:#151515">Tekton Chains<span> 签署和验证管道（开发者预览阶段）</span></span></li> 
 <li>Argo CD 仪表板支持显示 OpenShift 资源的健康状态</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d3120acf35957a614f4ce859b8007b50a4e.png" referrerpolicy="no-referrer"></p> 
<p><strong>支持更多云平台</strong></p> 
<p>新版本扩展了受支持的云平台，包括 IBM Cloud（技术预览阶段）、阿里云（技术预览阶段）和 Azure Stack Hub。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6b5ce2f0597462ec0b81c5ecd55ab78fe75.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4be7393154f6fe70b5fcbdea7f50729f20b.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faccess.redhat.com%2Fdocumentation%2Fzh-cn%2Fopenshift_container_platform%2F4.10%2Fhtml%2Frelease_notes%2Focp-4-10-release-notes" target="_blank">详细更新内容查看 release note</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            