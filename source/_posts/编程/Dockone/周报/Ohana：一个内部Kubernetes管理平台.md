
---
title: 'Ohana：一个内部Kubernetes管理平台'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=8979'
author: Dockone
comments: false
date: 2021-08-18 04:09:12
thumbnail: 'https://picsum.photos/400/300?random=8979'
---

<div>   
<br>【编者的话】本文是开源Kubernetes管理平台Ohana的功能简述，期待大家多多试用，共建共享。<br>
<h3>当前问题</h3>随着各类组织转向Kubernetes容器编排策略，问题出现了：如何让工程师能够创建自己的集群和命名空间，而又不给他们完全访问云仪表板的权限，因为完全权限有明显的安全和成本风险。<br>
<br>许多组织通过构建内部平台——创建一个抽象层，支持工程师的“自助服务”和DevOps管理，来解决这个问题。<br>
<br>这可能适用于那些有复杂流程的大公司，但我们想为各种规模的团队提供一种替代方案：一个开源的内部Kubernetes平台，它具有你需要的开箱即用的功能，同时也可以轻松定制以满足你的需求。<br>
<h3>介绍：Ohana</h3>我们在构建Ohana时考虑到了DevOps和工程师。对于DevOps，我们希望通过细粒度权限控制和健壮的监控使创建和管理用户变得容易。对于工程师来说，我们希望这是一个无缝的体验，以尽可能少的麻烦让他们能够访问他们自己需要的云资源。<br>
<h3>它是如何工作的</h3>Ohana构建在许多你可能已经在使用的工具之上。我们建议在容器中运行Ohana（你可以在我们的<a href="http://dockerhub.io/">Docker Hub</a>找到一个示例容器），以实现所有环境的一致性。<br>
<br>前端是使用React构建的，使用React <a href="https://reactjs.org/docs/context.html">Context</a>来管理状态。我们使用Node/Express后台，用<a href="https://www.npmjs.com/package/bcrypt">Bcrypt</a>进行加解密，使用PostgreSQL数据库。<br>
<br>Ohana预装了Google Kubernetes Engine（GKE）工作所需的所有工具：绑定了谷歌Cloud SDK，kubectl和Helm。Ohana是通过一个多阶段构建Dockerfile实现的。这使得容器能够自动自旋并对谷歌Cloud进行身份验证——不需要额外的干预。<br>
<br>Ohana GUI允许创建和管理命名空间和集群，并附带了管理员用来管理用户和团队的工具。<br>
<h3>开始使用</h3>你还在犹豫什么？我们邀请你访问我们的<a href="http://ohana-app.io/docs/ohana">文档</a>，然后从我们的<a href="https://github.com/oslabs-beta/ohana">GitHub repo</a>克隆，或简单地使用我们的<a href="http://dockerhub.io/">Docker镜像</a>样例。<br>
<br>我们期待着简化和改进你的开发人员和DevOps工作流程。<br>
<br>我们期待收到反馈！通过我们的<a href="https://github.com/oslabs-beta/ohana">GitHub</a>问题页面给我们留言，让我们知道你对后续版本的想法。请务必查看我们的<a href="http://ohana-app.io/docs/getting-started/features">产品路线图</a>，看看即将推出哪些功能。Ohana是100%开源的，我们永远欢迎来自社区的贡献。请在这里查看我们的<a href="http://ohana-app.io/docs/getting-started/community">贡献指南</a>。<br>
<br>Ohana由<a href="https://opensourcelabs.io/">OS Labs</a>提供支持，OS Labs是一个致力于构建开源工具，使开发人员的生活更轻松、更高效的技术加速器。<br>
<br>这个文章是整个Ohana团队合作的产物：<a href="https://www.linkedin.com/in/mika-todd-b37328105/">Mika Todd</a>，<a href="https://www.linkedin.com/in/lawrence-han">Lawrence Han</a>，<a href="https://www.linkedin.com/in/jalexchen/">JeC Chen</a>，<a href="https://www.linkedin.com/in/patrickallendfs/">Patrick Allen</a>和<a href="https://www.linkedin.com/in/andykahn">Andy Kahn</a>。来<a href="http://ohana-app.io/meet-the-team">这里</a>和我们会合。<br>
<br><strong>原文链接：<a href="https://adkahn.medium.com/introducing-ohana-an-internal-kubernetes-management-platform-e21516a69cca">Introducing Ohana, an internal kubernetes management platform</a>（翻译：池剑锋）</strong>
                                
                                                              
</div>
            