
---
title: 'Vitess 14 发布，性能提升 10%、Gen4 正式取代 V3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3224'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3224'
---

<div>   
<div class="content">
                                                                                            <p>Vitess 是一个用于部署、扩展和管理大型 MySQL 实例集群的数据库解决方案。Vitess 集 MySQL 数据库的很多重要特性和 NoSQL 数据库的可扩展性于一体。它的架构设计使得您可以像在物理机上一样在公共云或私有云架构中有效运行。它结合并扩展了许多重要的 MySQL 功能，同时兼具 NoSQL 数据库的可扩展性。</p> 
<p>Vitess 可以帮助解决以下问题：支持对 MySQL 数据库进行分片来扩展 MySQL 数据库，应用程序无需做太多更改；从物理机迁移到私有云或公共云；部署和管理大量的 MySQL 实例。</p> 
<p>Vitess 14 正式发布，更新内容如下：</p> 
<h2>可用性</h2> 
<h3>命令行语法的弃用</h3> 
<p>这个版本标志着 Vitess 开始对其命令行和标志语法进行标准化。一些以前的语法已经被废弃，在下一个版本中会被删除。</p> 
<h3>VtctldServer 和 Client</h3> 
<p>用于 vtctld 集群管理的新 gRPC API —— VtctldServer 已经可以使用了。目标是在 Vitess 15 开始废除旧的接口，所以用户现在就应该开始进行过渡了。</p> 
<p>Vitess 14 还提供了一个新的 vtctld 客户端（ <code>vtctldclient</code> ）来对应新的 gRPC 服务器接口。在启用新服务后，用户可以开始使用新的客户端来执行集群管理命令。 <code>vtctldclient</code> 和传统的 <code>vtctlclient</code> 都提供了 <code>shim</code> 机制来使用对方的 CLI 语法，以缓解过渡。</p> 
<h3>VTAdmin</h3> 
<p>Vitess 14 包括 VTAdmin 的测试版本，这是 Vitess 的下一代集群管理 API 和 UI。VTAdmin 提供了一个单一的控制平面来管理多个 Vitess 集群，并将取代传统的 VTCtld Web UI。</p> 
<p>请注意，新的 <code>grpc-vtctld</code> 服务是 VTAdmin 向你想管理的集群进行 RPC 的必要条件，所以你必须在启用该服务的情况下运行你的 <code>vtctld</code> 组件。</p> 
<h2>GA 公告</h2> 
<h3>Online DDL</h3> 
<p>基于 Vitess-native 和 gh-ost 的 Online DDL 功能现在已是 GA。 <code>pt-osc</code> 仍被认为是实验性的，主要是因为还没有被社区充分采纳或获得反馈。</p> 
<h3>Query Planner</h3> 
<p>Vitess 团队在两年前就开始了新的 Query Planner（查询计划程序）的工作，这个查询计划程序被称为 Gen4，在 Vitess 14 成为了新的默认程序。它取代了旧的称为 V3 的查询计划程序。新的计划程序增加了对更多查询的支持。</p> 
<h2>可靠性</h2> 
<h3>VTOrc</h3> 
<p>VTOrc 在 Vitess 14 中仍然是实验性的。在这个版本中，使 VTOrc 成为 Vitess 的一流组件的工作又向前推进了一步。</p> 
<ul> 
 <li>VTOrc 现在与 VTCtld 完全继承，从 VTCtld 运行集群操作不会导致 VTOrc 采取不必要的操作</li> 
 <li>在这个版本中已经解决了联合问题，现在可以运行 VTOrc 的多个实例来观察同一组 keyspaces，而不会相互影响。</li> 
</ul> 
<p>持久性策略配置已被重构，现在它不再作为命令行配置提供，而是存储在拓扑服务器中。VTOrc 和 VTCtld 都将从那里读取它，并遵循所提供的耐久性策略</p> 
<h2>性能</h2> 
<p>利用基准测试系统 arewefastyet 对这个新版本的 Vitess 进行基准测试后发现，v14.0.0 和 v13.0.0 之间大约有 10% 的性能提升。这一改进主要来自于取消了内部的 SAVEPOINT 查询执行。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitess.io%2Fblog%2F2022-06-28-announcing-vitess-14%2F" target="_blank">https://vitess.io/blog/2022-06-28-announcing-vitess-14/</a></p>
                                        </div>
                                      
</div>
            