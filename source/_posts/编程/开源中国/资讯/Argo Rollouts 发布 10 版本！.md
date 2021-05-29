
---
title: 'Argo Rollouts 发布 1.0 版本！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/a4e5dc71-5482-4726-9058-75d926c6a794.jpg'
author: 开源中国
comments: false
date: Sat, 29 May 2021 08:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/a4e5dc71-5482-4726-9058-75d926c6a794.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><em>文章来自 Henrik Blixt 和 Argo 维护者</em></p> 
<p><img src="https://oscimg.oschina.net/oscnet/a4e5dc71-5482-4726-9058-75d926c6a794.jpg" referrerpolicy="no-referrer"></p> 
<p>这是非常自豪和兴奋，我们宣布[1]推出 Argo Rollouts 1.0 版本！该项目已经被迅速采用和生产使用，甚至是在它的 0.x 发布后，已经拥有了一批令人印象深刻的用户[2]。</p> 
<h2>Argo Rollouts 是什么？</h2> 
<p>Argo Rollouts[3]是一个部署（deployment）控制器，它填补了 Kubernetes deployment 的空白，通过基于蓝/绿、灰度（金丝雀）、分析和实验的部署策略，为你的云原生应用程序和服务提供了自动化的、基于 GitOps 的渐进交付，为其提供了先进的应用程序部署能力。</p> 
<p>通常与Argo CD[4]一起使用，这是 Argo Rollouts 实现中的一个关键考虑因素，即允许简单的集成、可扩展性和灵活性，以确保它既可以作为独立组件使用，也可以与其他项目和框架集成。其他 CNCF 项目，如Backstage[5]，已经与 Rollouts 集成，并支持开箱即用。</p> 
<p>与其他社区支持的项目的灵活性和集成，体现在从流量整形到监控和分析的大量支持选项上。</p> 
<h2>Argo Rollouts 的价值是什么？</h2> 
<p>Argo Rollouts 是 Kubernetes Deployment 资源的替代，提供了应用程序生命周期的管理。Rollouts 允许用户为其部署使用各种策略，以更低的风险逐步部署其应用程序，并具有快速（甚至自动）终止或回滚到以前稳定版本的功能。这从本质上降低了发布软件的成本和风险，从而提高了开发速度。</p> 
<h2>1.0 中包含的关键特性</h2> 
<p>支持蓝/绿、灰度（金丝雀）、分析和实验部署策略</p> 
<p>用户有许多部署策略可供选择，以确保有一个适合他们的用例，从基本的蓝/绿策略到更高级的规则和基于实验的策略。</p> 
<h2>UI 仪表板</h2> 
<p>对一个新版本的健康状况具有可见度是至关重要的。Argo Rollout 1.0 包含一个仪表板，提供发布状态和健康状况的概述，并允许从 UI 交互启动操作。</p> 
<h2>工作负载引用</h2> 
<p>一种通过内联引用执行迁移到 Rollouts 的新方法，使得从现有的 Kubernetes Deployment 可以快速无缝地迁移到 Rollouts。它允许用户继续管理针对 Deployment 对象的 pod 规范补丁，但使用 Rollouts 规范指定更新策略。</p> 
<h2>更多特性和增强</h2> 
<p>想要了解 1.0 所包含内容的完整列表，请访问博客[6]或日志[7]。</p> 
<h2>鸣谢</h2> 
<p>许多人和公司都为这个版本投入了时间和资源，如果没有快速发展的 Argo Rollouts 社区的支持，这是不可能的！我们特别希望鸣谢以下公司的支持，没有他们，这个发布不可能：Bilibili、Bucketplace、Codefresh、DataDog、Datawire、Dynatrace、Intuit、NewRelic、Onfido、Paypal、Quizlet、Salesforce、Shipt、Skillz 和 Spotify。</p> 
<h3>参考资料</h3> 
<p>[1]宣布: <em>https://blog.argoproj.io/introducing-argo-rollouts-v1-0-803e87f76ef7</em></p> 
<p>[2]用户: <em>https://github.com/argoproj/argo-rollouts/blob/master/USERS.md</em></p> 
<p>[3]Argo Rollouts: <em>https://argoproj.github.io/argo-rollouts/</em></p> 
<p>[4]Argo CD: <em>https://github.com/argoproj/argo-cd</em></p> 
<p>[5]Backstage: <em>https://backstage.io/</em></p> 
<p>[6]博客: <em>https://blog.argoproj.io/introducing-argo-rollouts-v1-0-803e87f76ef7</em></p> 
<p>[7]日志: <em>https://github.com/argoproj/argo-rollouts/releases/tag/v1.0.0</em></p>
                                        </div>
                                      
</div>
            