
---
title: '集群列表集成 KubePi，KubeOperator 开源容器平台 v3.12.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2ff0d95e00b7531c996ace43d7cce972a2d.png'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 17:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2ff0d95e00b7531c996ace43d7cce972a2d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0">12月13日，开源容器平台KubeOperator正式发布v3.12.0版本。在这一版本中，KubeOperator对KubePi开源可视化管理面板的支持由之前的工具启用方式修改为了通过集群列表直接跳转的方式，并且支持导入任意版本的集群，不再受到Kubernetes版本的限制。</p> 
<p style="margin-left:0; margin-right:0">同时，KubeOperator增加了对镜像仓库与集群工具OPA Gatekeeper的支持，并完成了若干功能的优化和Bug修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#fc6554">■  KubeOperator</span></strong></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 集群列表集成KubePi可视化管理面板</strong></p> 
<p style="margin-left:0; margin-right:0">在KubeOperator v3.12.0版本中，集群列表新增Dashboard功能，支持用户直接跳转至KubePi可视化管理面板。在这种方式下，用户无需在集群工具列表中单独启用KubePi。KubePi版本也将随 KubeOperator版本同步更新，不再需要进行单独升级，并且KubePi的数据将被持久化到KubeOperator部署机中。另外，在系统设置中，也支持同步修改KubePi的用户名及密码。</p> 
<p><img alt height="1530" src="https://oscimg.oschina.net/oscnet/up-2ff0d95e00b7531c996ace43d7cce972a2d.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>                                         ▲图1  KubeOperator集群列表集成KubePi</span></p> 
<p style="margin-left:0; margin-right:0"><strong>2. 工具列表支持OPA Gatekeeper</strong></p> 
<p style="margin-left:0; margin-right:0">为了确保Kubernetes集群的一致性和合规性，每个组织都需要具有在其环境中定义和执行策略的能力。OPA（Open Policy Agent）是一种策略引擎，可对云原生环境进行基于策略的控制。KubeOperator提供了在Kubernetes集群中启用OPA Gatekeeper的功能。</p> 
<p style="margin-left:0; margin-right:0">OPA Gatekeeper是一个支持OPA与Kubernetes集成的项目。OPA Gatekeeper提供的功能包括：</p> 
<p style="margin-left:0; margin-right:0">● 可扩展的参数化策略库；</p> 
<p style="margin-left:0; margin-right:0">● 用于实例化策略库的原生Kubernetes CRD（Custom Resource Definition），也被称为“约束”；</p> 
<p style="margin-left:0; margin-right:0">● 原生Kubernetes CRD，用于扩展策略库，也被称为“约束模板”；</p> 
<p style="margin-left:0; margin-right:0">● 审核功能。</p> 
<p><img alt height="1532" src="https://oscimg.oschina.net/oscnet/up-b301899b438c8683072ca687c29f2f1ac98.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>                                           ▲图2  KubeOperator的集群工具列表</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#fc6554">■  KubePi</span></strong></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 支持镜像仓库</strong></p> 
<p style="margin-left:0; margin-right:0">在此次发布的KubePi v1.3.0版本中，管理员可以添加Harbor、Nexus、Docker Registry三种类型的镜像仓库，并将仓库授权到目标集群。用户通过表单创建Workload时，支持选择镜像仓库中已有的镜像。用户可以启用工具列表中的Docker Registry，或者应用商店中的Harbor来搭建私有镜像仓库。</p> 
<p><img alt height="1534" src="https://oscimg.oschina.net/oscnet/up-0dd764fcc4f346a7d0f929ad5030ce4779d.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>                                                 ▲图3  KubePi的镜像仓库</span></p> 
<p style="margin-left:0; margin-right:0"><strong>2. 支持日志审计</strong></p> 
<p style="margin-left:0; margin-right:0">KubePi v1.3.0版本增加了日志审计功能，用以记录每个用户发起的系统事件信息。用户可以及时知道发生了什么？何时发生？谁发起的？同时也记录了KubePi API的所有请求和响应，包括使用KubePi UI和通过编程使用KubePi API的所有其他用途。</p> 
<p><img alt height="1532" src="https://oscimg.oschina.net/oscnet/up-ffb91fb884da732cc69c771816dd37cba6f.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>                                                      ▲图4  KubePi的操作日志</span></p> 
<p style="margin-left:0; margin-right:0"><strong>3. 支持Pod日志下载</strong></p> 
<p style="margin-left:0; margin-right:0">KubePi v1.3.0版本支持针对容器日志的定时定量下载。点击Pod列表中的“日志”按钮，可进入日志追踪界面实时跟踪容器的日志信息，还可以根据自定义时间和日志大小将目标容器的日志文件下载至本地。</p> 
<p><img alt height="1578" src="https://oscimg.oschina.net/oscnet/up-70682f9f367c7347b8ff02d873c6044703e.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>                                                     ▲图5  KubePi Pod日志下载</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#fc6554"><strong>■  KubeOperator</strong></span></p> 
<p style="margin-left:0; margin-right:0">● Kubernetes版本支持v1.20.12；</p> 
<p style="margin-left:0; margin-right:0">● 界面设置功能优化（X-Pack增强包）；</p> 
<p style="margin-left:0; margin-right:0">● CIS扫描功能重构；</p> 
<p style="margin-left:0; margin-right:0">● 用户列表增加重置密码功能；</p> 
<p style="margin-left:0; margin-right:0">● 集群导入取消Kubernetes版本限制；</p> 
<p style="margin-left:0; margin-right:0">● 初始化集群选择主机时默认主机名排序；</p> 
<p style="margin-left:0; margin-right:0">● 集群Worker节点扩容，增加初始化存储提供商步骤；</p> 
<p style="margin-left:0; margin-right:0">● 自动模式创建可用区后定时刷新可用区状态。</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#fc6554">■  KubePi</span></strong></p> 
<p style="margin-left:0; margin-right:0">● 增加应用市场Chart仓库同步功能；</p> 
<p style="margin-left:0; margin-right:0">● 支持表单创建Resource Quotas和Limit Ranges；</p> 
<p style="margin-left:0; margin-right:0">● 表单创建工作负载时，支持同步创建Service；</p> 
<p style="margin-left:0; margin-right:0">● 表单创建Namespace时，支持同步创建Resource Quotas和Limit Ranges；</p> 
<p style="margin-left:0; margin-right:0">● 支持修改LDAP用户角色；</p> 
<p style="margin-left:0; margin-right:0">● 修改Helm驱动类型为Secrets；</p> 
<p style="margin-left:0; margin-right:0">● Docker Registry Secrets支持custom、dockerhub、quay.io三种类型；</p> 
<p style="margin-left:0; margin-right:0">● 针对不满足命名规则的LDAP用户增加提示信息；</p> 
<p style="margin-left:0; margin-right:0">● 增加JWT认证方式；</p> 
<p style="margin-left:0; margin-right:0">● 优化导入集群证书审批的超时时间；</p> 
<p style="margin-left:0; margin-right:0">● 进入集群控制台增加状态判断；</p> 
<p style="margin-left:0; margin-right:0">● Dashboard点击Logo跳转至概览页；</p> 
<p style="margin-left:0; margin-right:0">● 部分页面国际化内容优化。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#fc6554"><strong>■  KubeOperator</strong></span></p> 
<p style="margin-left:0; margin-right:0">● 修复了自动模式创建虚拟机失败一直显示等待程序执行的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了由于datastore名称不符合规范导致服务器创建失败的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了kubeconfig文件API Server默认地址不正确的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了系统设置中邮箱密码明文显示的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了创建虚拟机配置没有校验名称重复的问题。</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#fc6554">■  KubePi</span></strong></p> 
<p style="margin-left:0; margin-right:0">● 修复了由于Pod名称过长导致显示不全的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了Web Kubectl Path路径错误的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了部分类型的Secret不能编辑的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了删除Pod Security Policies失败的问题。</p>
                                        </div>
                                      
</div>
            