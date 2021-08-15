
---
title: 'Ohana，一个内部kubernetes管理平台'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=5456'
author: Dockone
comments: false
date: 2021-08-15 14:06:42
thumbnail: 'https://picsum.photos/400/300?random=5456'
---

<div>   
<br>【编者的话】本文是开源kubernetes管理平台：Ohana的功能简述，期待大家多多试用，共建共享。<br>
<br><h2>当前问题</h2>随着各类组织转向Kubernetes容器编排策略，问题出现了：如何让工程师能够创建自己的集群和命名空间，而又不给他们完全访问云仪表板的权限，因为完全权限有明显的安全和成本风险。<br>
<br>许多组织通过构建内部平台——创建一个抽象层，支持工程师的“自助服务”和DevOps管理，来解决这个问题。<br>
<br>这可能适用于那些有复杂流程的大公司，但我们想为各种规模的团队提供一种替代方案:一个开源的内部Kubernetes平台，它具有你需要的开箱即用的功能，同时也可以轻松定制以满足你的需求。<br>
<br><h2>介绍:Ohana</h2>我们在构建Ohana时考虑到了DevOps和工程师。对于DevOps，我们希望通过细粒度权限控制和健壮的监控使创建和管理用户变得容易。对于工程师来说，我们希望这是一个无缝的体验，以尽可能少的麻烦让他们能够访问他们自己需要的云资源。<br>
<br><h2>它是如何工作的</h2>Ohana构建在许多你可能已经在使用的工具之上。我们建议在容器中运行Ohana(你可以在我们的docker hub找到一个示例容器)，以实现所有环境的一致性。<br>
<br>前端是使用React构建的，使用React Context来管理状态。我们使用Node/Express后台，用Bcrypt进行加解密，使用PostgreSQL数据库。<br>
<br>Ohana预装了Google Kubernetes Engine (GKE)工作所需的所有工具：绑定了谷歌Cloud SDK,kubectl和helm。Ohana是通过一个多阶段构建Dockerfile实现的。这使得容器能够自动自旋并对谷歌Cloud进行身份验证——不需要额外的干预。<br>
<br>Ohana GUI允许创建和管理命名空间和集群，并附带了管理员用来管理用户和团队的工具。<br>
<br><h2>开始使用</h2>你还在犹豫什么?我们邀请你访问我们的文档，然后从我们的GitHub repo克隆，或简单地使用我们的docker镜像样例。<br>
<br>我们期待着简化和改进你的开发人员和DevOps工作流程。<br>
<br>我们期待收到反馈！通过我们的GitHub问题页面给我们留言，让我们知道你对后续版本的想法。请务必查看我们的产品路线图，看看即将推出哪些功能。Ohana是100%开源的，我们永远欢迎来自社区的贡献。请在这里查看我们的贡献指南。<br>
<br>Ohana由OS Labs提供支持，OS Labs是一个致力于构建开源工具，使开发人员的生活更轻松、更高效的技术加速器。<br>
<br>这个文章是整个Ohana团队合作的产物：Mika Todd, Lawrence Han, JeC Chen, Patrick Allen和Andy Kahn。来这里和我们会合。<br>
<br><strong>原文链接：Introducing Ohana, an internal kubernetes management platform（翻译：池剑锋）</strong>
                                
                                                              
</div>
            