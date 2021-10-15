
---
title: 'Rancher 2.6.1 Stable，默认集成 Harvester！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0dada141da06f486599d7e9e4086b89afb9.png'
author: 开源中国
comments: false
date: Fri, 15 Oct 2021 07:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0dada141da06f486599d7e9e4086b89afb9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0">2021年9月1日，企业级开源解决方案领导者SUSE正式发布Rancher 2.6，这是SUSE完成收购Rancher Labs以来，Rancher首个重大版本更新。</p> 
<p style="margin-left:0; margin-right:0">Rancher 2.6发布之后，Rancher的研发和测试团队根据用户的反馈结合产品需求对Rancher 2.6的功能、稳定性和安全性进行了大量的测试和优化。Rancher 2.6.1已于昨天正式发布，这是Rancher 2.6.x 第一个stable版本，也是SUSE Rancher官方推荐所有用户用于生产环境的稳定版本。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong><span style="color:#3cbc7d">Rancher 2.6.1新特性</span></strong></h2> 
<h3 style="margin-left:0px; margin-right:0px"><strong><span style="color:#3cbc7d">集成Harvester （技术预览）</span></strong></h3> 
<p style="margin-left:0; margin-right:0">Harvester是业界第一款基于Kubernetes的开源超融合基础架构软件，Rancher 2.6.1中默认集成了Harvester 0.3.0版本，这也是Harvester最新的Beta版本。这一集成仅支持Harvester 0.3.0及以上版本：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">用户可以导入多个Harvester集群进行多集群管理或multi-site管理</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">可以使用Rancher RBAC及企业身份验证来登录Harvester集群</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">可以在Harvester中使用Rancher项目特性使得各个团队可以将他们的虚拟机分开进行管理和组织起来</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">通过内置的Harvester Node Driver，用户可以在Harvester集群上创建基于RKE1或者RKE2的Kubernetes集群。用户可以为Kubernetes集群的工作负载使用Harvester内置的CSI驱动和LoadBalancer类型的负载均衡器。</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">Rancher的虚拟化多集群管理：</p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-0dada141da06f486599d7e9e4086b89afb9.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-5c0b66925c6975c286fc100c3ad341aa499.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">想要了解更多内容，请访问：<br> <u>https://docs.harvesterhci.io/v0.3/rancher/rancher-integration/</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">此外，Harvester 0.3.0增强了网络功能，首先在Harvester裸机集群中增加了<span style="color:#3cbc7d"><strong>虚拟（浮动）IP支持</strong></span>，它将成为访问Harvester UI/API server的默认IP；另外，v0.3.0支持了<span style="color:#3cbc7d"><strong>Bond网卡</strong></span>，用户现在可以为Harvester网络接口配置多个网卡。    </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-56038c12544aed32d13a8573ccd07b17f06.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#3cbc7d"><strong>存储功能</strong></span>在这一新版本中也得到优化，用户现在可以在正在运行的虚拟机中<span style="color:#3cbc7d"><strong>热插拔卷</strong></span>。<span style="color:#3cbc7d"><strong>多磁盘管理功能</strong></span>也已经上线，用户现在可以在节点配置中配置额外的磁盘来增加节点的存储容量。<span style="color:#3cbc7d"><strong>本地镜像现在可以直接上传到Harvester集群</strong></span>，并且能够从一个已存在的volume中创建一个新镜像。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">在运维侧，Harvester 0.3.0也新增了几个新特性帮助用户轻松运维。首先，我们现在有了一个用于Harvester的<span style="color:#3cbc7d"><strong>Terraform程序</strong></span>。其次，最新版的Dashboard<span style="color:#3cbc7d"><span style="color:#3cbc7d"><strong>增强了监控功能</strong></span>，用</span>户可以在Harvester的dashboard中查看实时的系统利用率。此外，用户可以驱逐节点进行维护。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">从仪表板页面，用户可以分别查看集群指标和前 10 个最常用的虚拟机指标。此外，用户可以单击 Grafana 仪表板链接，从而可以在 Grafana UI 上查看更多仪表板。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9ceab1eb4c5d41e2883daa4dce0a4ad5528.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">用户可以通过虚拟机的详细信息页面点击查看虚拟机的详情指标。</p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-a79c73237432fbf1e754b3966bc134ae1e9.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px"><span style="color:#3cbc7d">安全性增强</span></h3> 
<p>RKE和RKE2支持新版本的Kubernetes，解决了symlink交换可能允许主机文件系统访问的问题。具体详情，请参阅CVE-2021-25741（<u>https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741</u>）。</p> 
<h3 style="margin-left:0px; margin-right:0px"><span style="color:#3cbc7d">Fleet优化</span></h3> 
<p>Fleet现在可以管理运行其他Fleet实例的集群。这使Rancher能够管理Harvester集群、其他Rancher实例或独立的Fleet。由于这一变化，一个集群中可能有两个Fleet agent。</p> 
<h3 style="margin-left:0px; margin-right:0px"><span style="color:#3cbc7d">修复了2.6.0以来的重要Bug</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Istio chart可以在离线环境中升级Istio，但仅限于可用版本。#30842</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">从Rancher v2.5.x升级到Rancher 2.6.x，并启用Istio v1后，侧面导航不再在顶部显示错误的"Istio "菜单项。#4072</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复了当系统命名空间不存在时，Fleet会无限地创建集群密钥的问题。#34776</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">对于自定义RKE2集群中的Windows节点，现在可以正确检索外部IP地址了。#91</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">将集群迁移到不同的<span style="background-color:rgba(0, 0, 0, 0.05); color:#3cbc7d">FleetWorkspace</span>不再导致管理集群被删除。#34744</p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:center"><strong><span style="color:#3cbc7d">升级与更新</span></strong></h2> 
<p style="margin-left:0; margin-right:0">更多Rancher 2.6.1的升级、版本信息等内容，请查阅以下链接：</p> 
<p style="margin-left:0; margin-right:0"><u>https://github.com/rancher/rancher/releases/tag/v2.6.1</u></p>
                                        </div>
                                      
</div>
            