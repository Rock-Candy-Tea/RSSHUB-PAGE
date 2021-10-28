
---
title: 'Vitess 12 正式发布，扩展 MySQL 实例集群的数据库解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7248'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7248'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvitessio%2Fvitess%2Freleases%2Ftag%2Fv12.0.0" target="_blank">Vitess 12</a> 正式版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitess.io%2Fblog%2F2021-10-26-announcing-vitess-12%2F" target="_blank">已发布</a>。</p> 
<blockquote> 
 <p style="color:#4a4a4a; margin-left:0; margin-right:0; text-align:start">Vitess 是一个用于部署、扩展和管理大型 MySQL 实例集群的数据库解决方案。Vitess 集 MySQL 数据库的很多重要特性和 NoSQL 数据库的可扩展性于一体。它的架构设计使得您可以像在物理机上一样在公共云或私有云架构中有效运行。它结合并扩展了许多重要的 MySQL 功能，同时兼具 NoSQL 数据库的可扩展性。Vitess 可以帮助解决以下问题：</p> 
 <ul style="margin-left:2em; margin-right:0px"> 
  <li>支持对 MySQL 数据库进行分片来扩展 MySQL 数据库，应用程序无需做太多更改</li> 
  <li>从物理机迁移到私有云或公共云</li> 
  <li>部署和管理大量的 MySQL 实例</li> 
 </ul> 
</blockquote> 
<p>在此版本中，Vitess 在多个方面取得了重大进展，包括 Gen4 planner、VTAdmin 和其他改进。</p> 
<p><strong>Gen4 Planner</strong></p> 
<p>Gen4 是最新版本的查询计划程序 (query planner)，在 Vitess 12 中属于实验性功能。如需使用 Gen4，VTGate 的<code>-planner_version</code><span style="background-color:#ffffff; color:#24292f"><span> </span>flag 需要被设置为</span><code>gen4</code>。</p> 
<p><strong>VTAdmin</strong></p> 
<p>在 Vitess 10.0 中引入的实验性多集群管理 API 和 Web UI 称为 VTAdmin，现在最新版本 Vitess 12 改进了基于<span style="background-color:#ffffff; color:#4a4a4a"><span> </span>vreplication 的 Reshard 工作流。</span></p> 
<p>Vitess 12.0 引入了基于角色的访问控制 (RBAC) 的实验性实现，允许 Vitess 运维人员根据其 Vitess 环境的特定授权实现来允许或拒绝 API 端点。这为即将到来的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvitessio%2Fvitess%2Fprojects%2F13" target="_blank"> vtctld2 UI 弃用计划</a>提供了基础。请注意，VTAdmin 不提供任何身份验证实现；用户可提供他们自己的，适用于他们部署的特定细节相关的认证。</p> 
<p>部署 vtadmin-api 和 vtadmin-web 组件是完全可选的。VTAdmin 依赖于新的 VtctldServer API，因此必须在 vtctlds 上运行新的 grpc-vtctld 服务才能使用它。</p> 
<p><strong>Benchmarking</strong></p> 
<p>根据官方的介绍，自上次发布以来，arewefastyet 发生了细微的变化。Web 服务器使用新的基准测试队列，该队列消耗更少的计算资源并避免两次运行相同的基准测试。为增强对新 Gen4 查询计划程序性能的信任，团队开发了一项功能，可以将宏基准测试生成的查询计划及其统计信息（执行时间、执行计数）可视化。在比较 V3 和 Gen4 的性能时提供了更多的优势。</p> 
<p><strong>使用更包容性的命名</strong></p> 
<p>此版本进行了重大的命名改变，例如删除 master，用 primary 或 source 代替，这些变化现在已向后兼容。在下一个版本中，废弃的命令将被删除，这意味着使用废弃命令的脚本应该被修改为使用新的命令。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvitessio%2Fvitess%2Freleases%2Ftag%2Fv12.0.0" target="_blank">下载地址</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitess.io%2Fblog%2F2021-10-26-announcing-vitess-12%2F" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            