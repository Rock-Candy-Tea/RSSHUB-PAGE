
---
title: '集群高可用部署支持 VIP，KubeOperator 开源容器平台 v3.10.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f26a3eed09a16cf8d3e92474154e8b25d1b.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 12:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f26a3eed09a16cf8d3e92474154e8b25d1b.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">8月16日，开源容器平台KubeOperator正式发布v3.10.0版本。在这一版本中，KubeOperator支持用户在部署Kubernetes集群过程中配置VIP实现高可用，支持自定义Kubernetes集群的NodePort端口范围和地址，支持在Kubernetes集群扩容过程中查看日志和错误重试，同还完成了若干功能的优化和Bug修复。</p> 
<h2 style="text-align:left">新增功能</h2> 
<p style="text-align:left"><strong>1. 集群高可用部署支持VIP</strong></p> 
<p style="text-align:left">KubeOperator v3.10.0版本在部署Kubernetes集群时支持通过“HAProxy+Keepalived”实现针对APIServer服务的高可用，用户在创建集群的过程中填写正确且有效的VIP地址后，KubeOperator在部署Kubernetes集群时，会自动使用用户填写的VIP地址配置HAProxy和Keepalived，此后所有Worker节点组件均使用VIP地址访问APIServer。</p> 
<p style="text-align:left">注意: 使用VIP的前提是需要有三个Master节点，或者部署计划配置的是多Master节点。</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-f26a3eed09a16cf8d3e92474154e8b25d1b.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>2.  集群节点扩容支持实时查看日志和错误重试</strong></p> 
<p style="text-align:left">KubeOperator v3.10.0版本支持集群在扩容Worker节点的过程中实时查看任务日志，以方便定位排查问题。并且在扩容失败后，用户可以通过“重试”操作继续完成节点的扩容工作。</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-2ebe8f3d590a907ea85b12b61b8c43a9246.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>3. 集群节点支持强制删除</strong></p> 
<p style="text-align:left">使用KubeOperator可以自动完成Kubernetes集群节点的扩容、缩容等工作，节点的生命周期较为可控。在特殊情况下，例如集群节点所在服务器由于断电、磁盘损坏等因素导致节点无法正常启动，此时为了保证集群节点的信息一致，可以通过“强制删除”功能来删除集群中异常的节点。</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a7526623fab0f003f5d218335a3a643baba.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>4. 支持自定义NodePort端口和地址范围</strong></p> 
<p style="text-align:left">在进行Kubernetes服务暴露时，若用户使用的服务类型为NodePort，每个服务就需要在每个主机上占用固定的端口。Kubernetes集群默认的NodePort端口范围是30000-32767。KubeOperator v3.10.0版本支持在集群部署时自定义NodePort端口范围和NodePort端口监听的IP地址。</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-7ac2b70750e9cdff343170a6a78a5fa7601.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">优化改进</h2> 
<p style="text-align:left">■ 支持修改非绑定状态的主机；</p> 
<p style="text-align:left">■ 支持自定义NodePort端口范围和地址；</p> 
<p style="text-align:left">■ 创建集群时支持设置Service CIDR；</p> 
<p style="text-align:left">■ 集群节点扩容时同步设置DNS缓存；</p> 
<p style="text-align:left">■ 集群节点添加、删除时同步刷新节点hosts记录；</p> 
<p style="text-align:left">■ Prometheus服务类型修改为NodePort；</p> 
<p style="text-align:left">■ 导入集群支持设置架构信息；</p> 
<p style="text-align:left">■ 实时同步集群状态；</p> 
<p style="text-align:left">■ 集群备份逻辑优化；</p> 
<p style="text-align:left">■ 集群诊断功能优化；</p> 
<p style="text-align:left">■ 集群备份功能优化；</p> 
<p style="text-align:left">■ 集群强制删除功能优化。</p> 
<h2 style="text-align:left">BUG 修复</h2> 
<p style="text-align:justify">■ 修复了导入集群使用集群评分功能异常的问题；</p> 
<p style="text-align:justify">■ 修复了集群节点没有根据名称排序的问题；</p> 
<p style="text-align:justify">■ 修复了部分编辑页面刷新后定位错误的问题。</p>
                                        </div>
                                      
</div>
            