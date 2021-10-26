
---
title: 'KubeOperator 开源容器平台 v3.11.0 发布，新增 KubePi 可视化管理面板、导入自建集群支持多种 Day2 操作'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-14e983651d3715ae1ff03045e429fc85d5e.png'
author: 开源中国
comments: false
date: Tue, 26 Oct 2021 06:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-14e983651d3715ae1ff03045e429fc85d5e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">10月25日，开源容器平台KubeOperator正式发布v3.11.0版本。在这一版本中，集群工具列表新增KubePi可视化管理面板，并且在导入KubeOperator自建集群时支持扩缩容、升级等Day2操作，同时还完成了若干的功能优化和Bug修复。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新增功能</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#fc6554">1. 新增KubePi可视化管理面板</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">作为一款简单易用的开源Kubernetes可视化管理面板，KubePi（<em>https://github.com/KubeOperator/KubePi</em>）允许管理员导入多个Kubernetes集群，并且通过权限控制将不同Cluster、Namespace的权限分配给指定的用户。KubePi允许开发人员管理Kubernetes集群中运行的应用程序，并对其进行故障排查，从而帮助开发人员更好地处理Kubernetes集群中的复杂性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>与同类型的集群可视化管理工具相比，KubePi更注重于集群内应用的部署、管理与纠错，将常用的<em>kubectl</em>命令可视化，以表单的形式代替了冗长复杂的YAML文件，力求实现人人可用。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">KubePi支持导入多个Kubenetes集群，当前版本支持token、kubeconfig、证书三种导入方式，能够实现对集群的零侵入。用户权限具体到命名空间，支持各类权限自定义。导入集群后，管理员可以为用户分配不同的集群角色与命名空间权限，从而实现对集群权限的管理与控制。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1636" src="https://oscimg.oschina.net/oscnet/up-14e983651d3715ae1ff03045e429fc85d5e.png" width="2874" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> ▲图1  KubeOperator集群工具列表</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1800" src="https://oscimg.oschina.net/oscnet/up-e53b1bbc86518e3c66e34f59482ee1474a7.png" width="2880" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图2  KubePi仪表盘</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong><span style="color:#fc6554">2. 导入KubeOperator自建集群时支持进行扩缩容、升级等Day2操作</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>KubeOperator v3.11.0版本支持导入自建的Kubernetes集群，并且支持用户进行Worker节点扩容、缩容、集群升级、备份、恢复、创建存储提供商等Day2操作。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1634" src="https://oscimg.oschina.net/oscnet/up-defad9ccfccead84323a5a765c2c45a098b.png" width="2874" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">▲图3  导入KubeOperator自建集群</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1636" src="https://oscimg.oschina.net/oscnet/up-d57144352994700f9561b637e31cce45bb1.png" width="2876" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图4  编辑KubeOperator自建集群</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能优化</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>初始化集群时，支持设置Master节点是否可调度；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>支持同步已启用工具状态和Chart仓库状态；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>支持Prometheus工具启用后跳转；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>工具列表增加详情信息展示；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 添加存储类时，支持自定义回收策略；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>集群、主机等列表页支持自定义排序；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 主机列表页增加凭据信息（默认隐藏）；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>创建vCenter可用区时，资源类型支持选择主机；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>创建可用区时，自定义模版支持自定义凭据和端口；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>部署计划、可用区和区域列表默认按照名称排序；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 系统设置添加仓库时，支持设置Nexus仓库密码；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>运行时选择Docker时，默认支持live-restore功能；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 添加集群配置预览时，手动集群节点超出后隐藏显示；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>集群评分功能优化（Kubernetes开源配置验证工具Polaris的版本升级至v4.1.0版本）；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>批量删除存储提供商时，增加状态判断选项；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>集群API健康检查增加“待解决”状态；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 集群删除逻辑优化。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Bug修复</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了Web Kubectl弹出时显示token错误的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了添加主机时，大内存主机获取不到内存的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 修复了提交类按钮双击导致重复提交的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了OpenStack集群创建可用区时，虚拟机没有创建在指定服务器的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了发生网络闪断后，Kobe服务中锁未释放的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■</span><span> 修复了在Ubuntu主机中输入<em>kubectl</em>命令没有自动补全的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了导入集群没有发送消息的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了导入集群删除后，消息详情没有获取到集群名称的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#fc6554">■ </span><span>修复了区域、消息中心高级搜索报错的问题。</span></p>
                                        </div>
                                      
</div>
            