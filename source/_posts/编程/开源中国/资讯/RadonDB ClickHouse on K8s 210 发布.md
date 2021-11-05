
---
title: 'RadonDB ClickHouse on K8s 2.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2f9e40d0b565b71f138fd26021aaa18574e.png'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 13:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2f9e40d0b565b71f138fd26021aaa18574e.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">RadonDB ClickHouse Kubernetes 于 10 月 29 日发布了第三个版本 2.1.0 [1]。该版本也是由 Operator 方式实现的第二个版本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-2f9e40d0b565b71f138fd26021aaa18574e.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">致谢</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">首先感谢<span> </span><a href="https://my.oschina.net/dbkernel">@dbkernel</a><span> </span>@su-houzhen @TCeason @wufan @molliezhang 提交的修改。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">什么是 RadonDB ClickHouse？</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-c7db1581073909aef590b362b0fe7fa65cd.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>RadonDB ClickHouse</strong><span> </span>是一个分布式实时分析型列式存储数据库。具备高性能，支撑PB级数据，提供实时分析，稳定可扩展等特性。适用于数据仓库、BI报表、监控系统、互联网用户行为分析、广告投放业务以及工业、物联网等分析和时序应用场景。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>RadonDB ClickHouse Kubernetes</strong><span> </span>支持在<span> </span><strong>Kubernetes</strong><span> </span>和<span> </span><strong>KubeSphere</strong><span> </span>上安装部署和管理，自动执行与运行 RadonDB ClickHouse 集群有关的任务。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>RadonDB ClickHouse Kubernetes</strong><span> </span>从 2.0.0 开始，已经由 Helm 迁移至 Operator 方式实现，并且完全兼容 1.0 版本的所有功能特性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>RadonDB ClickHouse Kubernetes</strong><span> </span>基于<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAltinity%2Fclickhouse-operator" target="_blank">https://github.com/Altinity/clickhouse-operator</a><span> </span>实现并改进，后续会持续回馈给社区。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>代码仓库地址</strong>：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Operator：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradondb%2Fradondb-clickhouse-operator" target="_blank">https://github.com/radondb/radondb-clickhouse-operator</a></li> 
 <li>Helm Chart：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradondb%2Fradondb-clickhouse-kubernetes" target="_blank">https://github.com/radondb/radondb-clickhouse-kubernetes</a></li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">新版本功能一览</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1. 支持自动创建ZooKeeper 依赖</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开启该功能后，ZooKeeper 集群将由 Operator 创建并配置到 ClickHouse 集群中，用户无需再额外创建和管理。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2. 丰富集群状态粒度</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在原有三种集群状态（处理中、处理完成、删除中）的基础上，新增创建中、运行中、创建失败、删除失败四种状态。原处理相关状态则转而代表更新状态。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>3. 支持磁盘动态扩容</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可修改 yaml 存储容量，自动升级扩容存储，并升级数据库集群。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>4. 支持 ClickHouse 集群监控</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开启监控功能后，将创建监控服务并自动对接 Prometheus。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>5. 优化代码和迭代更新</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>6. 完善单元测试</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">RoadMap</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">后续 RadonDB ClickHouse Kubernetes 的技术路线：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>增加 Secret 支持</li> 
 <li>支持更细粒度的配置更新</li> 
 <li>支持集群层面的数据库备份恢复</li> 
 <li>进一步提升服务质量，减少特殊场景下启停时间</li> 
 <li>支持自动化 e2e 测试</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>期待更多开发者参与到开源项目中来！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以下是 2.1.0 和 2.0.0 版本完整的 Release Notes 。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">2.1.0 Release Notes</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Features</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Change version from 2.0 to 2.1</li> 
 <li>Create/delete zookeeper when create/delete clickhouse</li> 
 <li>Rename<span> </span><code>status</code><span> </span>to<span> </span><code>state</code></li> 
 <li>Add describle about cluster parameter</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">2.0.0 Release Notes</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Features</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Support deploy ClickHouse & ClickHouse Operator via Helm Charts</li> 
 <li>Support create ClickHouse cluster based on Custom Resource specification provided</li> 
 <li>Support customizing K8S resources through templates, include Pod, Service, VolumeClaimTemplates</li> 
 <li>ClickHouse configuration and settings, including Zookeeper integration</li> 
 <li>CRD Compatible api extension version v1</li> 
 <li>Pod Disk expansion support qingcloud-csi</li> 
 <li>Remote server config add physical & logical cluster</li> 
 <li>ClickHouse Cluster scaling including automatic schema propagation</li> 
 <li>Support ClickHouse version upgrades</li> 
 <li>Exporting ClickHouse metrics to Prometheus</li> 
 <li>Node management、Automatic failover、Automatic rebuild node</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Improvements</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Add the README and deploy documents</li> 
 <li>Modify grafana dashboard: ck query dashboard</li> 
 <li>Add more clickhouse cluster status:<span> </span><code>create</code>,<span> </span><code>running</code>,<span> </span><code>create failed</code>,<span> </span><code>update failed</code></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Bug fixes</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Fix api extension version error</li> 
 <li>Fix remote server config generate</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎大家下载体验！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">参考及下载链接</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">[1]. Release Notes:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradondb%2Fradondb-clickhouse-operator%2Freleases" target="_blank">https://github.com/radondb/radondb-clickhouse-operator/releases</a></p>
                                        </div>
                                      
</div>
            