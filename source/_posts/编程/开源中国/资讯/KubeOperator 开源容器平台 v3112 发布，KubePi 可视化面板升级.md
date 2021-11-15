
---
title: 'KubeOperator 开源容器平台 v3.11.2 发布，KubePi 可视化面板升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b6948c641656edb6b6cb0a92706f6458f44.png'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 14:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b6948c641656edb6b6cb0a92706f6458f44.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0">11月15日，开源容器平台KubeOperator正式发布v3.11.2版本。在这一版本中，KubeOperator默认集成最新的KubePi可视化管理面板v1.2.0版本，同时对集群扩容步骤进行了分解，将集群创建、升级、扩缩容等Day2操作过程中产生的错误信息进行了格式化，并完成了若干功能的优化和Bug修复。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#fc6554">■ KubeOperator</span></strong></p> 
<p style="margin-left:0px; margin-right:0px"><strong>1. 集群扩容步骤分解</strong></p> 
<p style="margin-left:0; margin-right:0">在KubeOperator v3.11.2版本中，用户针对目标集群的Worker节点进行扩容操作时，后端拆分为了多个可单独执行的Ansible任务。Ansible任务拆分后，任务进度将更加清晰和直观。当Worker节点扩容失败后，用户也可以更加明确地查看到具体错误原因。用户点击“重试操作”选项时，可直接从当前失败任务处开始执行，无需再执行全部的Ansible任务。</p> 
<p><img alt height="1526" src="https://oscimg.oschina.net/oscnet/up-b6948c641656edb6b6cb0a92706f6458f44.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>▲图1  KubeOperator集群扩容状态详情</span></p> 
<p><strong>2. 集群创建、升级、扩缩容等Day2操作错误信息格式化</strong></p> 
<p style="margin-left:0; margin-right:0">在KubeOperator v3.11.2版本中，我们将集群进行创建、升级、扩缩容等Day2操作时所产生的错误信息进行了格式化。详情页以集群节点为分组条件，显示内容抽取了cmd、message、stderr和stdout等信息。用户可以更为直观地看到具体是哪台主机在执行什么任务时抛出的具体错误信息，极大地增加了错误信息的可读性。</p> 
<p><img alt height="1400" src="https://oscimg.oschina.net/oscnet/up-79d6653afb9ab8f7079f40e61ac37125769.png" width="2878" referrerpolicy="no-referrer"></p> 
<p><span>▲图2  集群创建错误信息显示</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#fc6554">■ KubePi</span></strong></p> 
<p style="margin-left:0; margin-right:0"><strong>1. 支持LDAP</strong></p> 
<p style="margin-left:0; margin-right:0">在此次发布的KubePi v1.2.0版本中，管理员可以通过配置LDAP（Lightweight Directory Access Protocol，轻型目录访问协议 ）的相关信息将企业用户同步到KubePi平台中。注意：没有邮箱的用户不会被同步，与本地用户登录名重复的用户也不会被同步。管理员可以基于标准的LDAP协议来实现统一的用户认证，便于管理员对企业用户进行统一管理。</p> 
<p><img alt height="1532" src="https://oscimg.oschina.net/oscnet/up-78198db9c64a9ee49bec158f7f9b00d2cd1.png" width="2880" referrerpolicy="no-referrer"></p> 
<p><span>▲图3  KubePi的LDAP配置界面</span></p> 
<p style="margin-left:0; margin-right:0"><strong>2. 集群列表支持分组管理</strong></p> 
<p style="margin-left:0; margin-right:0">KubePi v1.2.0版本支持集群管理员为已经导入KubePi平台的Kubernetes集群添加自定义标签，以方便管理员进行维护。集群列表同时支持根据集群名称和标签来快速定位至目标集群。</p> 
<p><img alt height="887" src="https://oscimg.oschina.net/oscnet/up-b62e35bfb116821100005dbe9285d23d963.png" width="1906" referrerpolicy="no-referrer"></p> 
<p><span>▲图4  KubePi的集群列表分组及标签</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#fc6554">■ KubeOperator</span></strong></p> 
<p style="margin-left:0px; margin-right:0px">● 支持实时查看集群备份、恢复的Ansible日志；</p> 
<p style="margin-left:0; margin-right:0">● 创建集群支持多个NTP Server；</p> 
<p style="margin-left:0; margin-right:0">● 增加SFTP类型的备份账号默认端口。</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#fc6554">■ KubePi</span></strong></p> 
<p style="margin-left:0; margin-right:0">● 增加Terminal权限控制，与用户的Dashboard权限保持一致；</p> 
<p style="margin-left:0; margin-right:0">● Pod列表支持CPU、内存使用率；</p> 
<p style="margin-left:0; margin-right:0">● Pod详情页增加容器详情信息展示；</p> 
<p style="margin-left:0; margin-right:0">● Workload详情页增加运行时、服务、路由、部署策略等信息显示；</p> 
<p style="margin-left:0; margin-right:0">● Workload详情页增加调整镜像版本、修改部署策略、暂停/启用等常用操作；</p> 
<p style="margin-left:0; margin-right:0">● Nodes详情页增加资源Allocatable、Capacity等信息；</p> 
<p style="margin-left:0; margin-right:0">● Namespaces详情页增加Resource Quotas、Limit Ranges等信息；</p> 
<p style="margin-left:0; margin-right:0">● 支持存储类（StorageClass）设置默认值；</p> 
<p style="margin-left:0; margin-right:0">● Persistent Volumes（持久卷）列表增加卷类型、回收策略等信息；</p> 
<p style="margin-left:0; margin-right:0">● 集群列表页CPU、内存等信息显示优化；</p> 
<p style="margin-left:0; margin-right:0">● Dashboard菜单增加Namespaced作用域标识。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0px; margin-right:0px"><strong><span style="color:#fc6554">■ KubeOperator</span></strong></p> 
<p style="margin-left:0px; margin-right:0px">● 修复了主机列表 、集群列表、节点列表刷新导致勾选失效的问题。</p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#fc6554">■ KubePi</span></strong></p> 
<p style="margin-left:0; margin-right:0">● 修复了Kubernetes v1.18版本创建Ingress失败的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了终端输入命令过长导致光标会跳至行首覆盖输入的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了用户列表分页显示错误的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了部分Kubernetes版本Resource Quotas列表获取不到CPU和内存信息的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了由于Metrics Server服务异常导致Dashboard页无法访问的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了Persistent Volumes（持久卷）创建失败后不能切换类型的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了二进制启动服务时，Flag没有生效的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了Secrets等详情页Token过长时没有换行的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了Service NodePort端口在列表页没有显示的问题；</p> 
<p style="margin-left:0; margin-right:0">● 修复了部分页面标签/注释显示错误的问题。</p>
                                        </div>
                                      
</div>
            