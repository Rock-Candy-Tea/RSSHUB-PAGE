
---
title: '【GOTC 预告】王思宇：从 OpenKruise 看云原生应用负载发展趋势'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://intranetproxy.alipay.com/skylark/lark/0/2021/png/21156609/1625020372201-c3f3b566-f07a-4011-9ee4-28398c97b812.png#clientId=u64fb794f-1abc-4&from=ui&height=255&id=ue47ed5e7&margin=%5Bobject%20Object%5D&name=%E5%A4%B4%E5%9B%BE.png&originHeight=720&originWidth=1080&originalType=binary&ratio=2&size=388505&status=done&style=none&taskId=u75105266-9d86-4274-8a9d-688f4b4be03&width=382'
author: Dockone
comments: false
date: 2021-07-01 08:07:55
thumbnail: 'https://intranetproxy.alipay.com/skylark/lark/0/2021/png/21156609/1625020372201-c3f3b566-f07a-4011-9ee4-28398c97b812.png#clientId=u64fb794f-1abc-4&from=ui&height=255&id=ue47ed5e7&margin=%5Bobject%20Object%5D&name=%E5%A4%B4%E5%9B%BE.png&originHeight=720&originWidth=1080&originalType=binary&ratio=2&size=388505&status=done&style=none&taskId=u75105266-9d86-4274-8a9d-688f4b4be03&width=382'
---

<div>   
<br><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/21156609/1625020372201-c3f3b566-f07a-4011-9ee4-28398c97b812.png#clientId=u64fb794f-1abc-4&from=ui&height=255&id=ue47ed5e7&margin=%5Bobject%20Object%5D&name=%E5%A4%B4%E5%9B%BE.png&originHeight=720&originWidth=1080&originalType=binary&ratio=2&size=388505&status=done&style=none&taskId=u75105266-9d86-4274-8a9d-688f4b4be03&width=382" alt="头图.png" referrerpolicy="no-referrer"><br>
​<br>
<br>2021 年 7 月 9 日至 10 日，GOTC 全球开源技术峰会（The Global Opensource Technology Conference）上海站即将拉开大幕。大会由开源中国和 Linux 软件基金会（The Linux Foundation）联合发起，全球头部开源公司和顶级开源项目将一起亮相，覆盖云原生、大数据、人工智能、物联网、区块链、DevOps、开源治理等多个技术领域，为开发者带来全球最新、最纯粹的开源技术，同时传播开源文化和理念，推动开源生态的建设和发展。<br>
<br>7 月 10 日， CNCF Sandbox 项目 OpenKruise 作者 & 社区负责人、阿里云技术专家王思宇将在 GOTC 上海站 「开源云原生计算时代论坛」专题论坛带来主题分享。OpenKruise 是由阿里开源的云原生应用自动化扩展套件，它在完全兼容标准的 Kubernetes 之上，围绕云原生应用场景提供多种丰富的自动化能力。目前 OpenKruise 在 Github 上已经有 2300+ star， 50+ 贡献者，已登记生产使用的用户包括来自国内外的阿里、蚂蚁、携程、苏宁、OPPO、有赞、斗鱼TV、申通、小红书、Lyft、Spectro Cloud 等 25+ 企业。<br>
​<br>
<br>在本次论坛上，王思宇将分享哪些在社区中观察到的云原生趋势，又将介绍哪些值得关注的 OpenKruise 最新动态？让我们先睹为快。<br>
​<br>
<br><h1>GOTC 讲师王思宇：从 OpenKruise 看云原生应用负载发展趋势</h1>​<br>
<br><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/21156609/1625020412079-24d2ceda-6190-4ba9-8c62-81b6463478e3.png#clientId=u64fb794f-1abc-4&from=ui&height=669&id=u36dcb1e6&margin=%5Bobject%20Object%5D&name=1.png&originHeight=710&originWidth=399&originalType=binary&ratio=2&size=290723&status=done&style=none&taskId=ua7674e93-8514-4ef0-b2b8-6f6104fd9ae&width=376" alt="1.png" referrerpolicy="no-referrer"><br>
​<br>
<br><h2>讲师简介</h2>​<br>
<br>王思宇，OpenKruise 作者&负责人，阿里云技术专家，Kubernetes、OAM 社区贡献者。长期从事云原生、容器、调度等领域研发；阿里巴巴百万容器调度系统核心研发成员，多年支撑阿里双十一超大规模容器集群经验。<br>
​<br>
<br><h2>议题介绍</h2>​<br>
<br>云原生的应用负载从 Kubernetes 原生的 workloads（Deployment、StatefulSet）为人所熟知，但在另一方面，我们也看到从中小型的创业公司到大型互联网公司，越是大规模的应用场景下这些原生的 workloads 越是无法满足复杂的业务部署诉求。因此，不少公司都自研了适用于自身场景的自定义 workload，但其中真正在通用化、全面性、稳定性等多方面做到成熟的开源组件，只有阿里云开源的、已经成为 CNCF Sandbox 项目的 OpenKruise。<br>
​<br>
<br>本次分享中，我们将从 Kubernetes 原生 workloads 开始介绍云原生应用负载的职责、实现基础，而后分析在超大规模业务场景下对应用负载的真实诉求，OpenKruise 是通过什么样的方式来满足这些需求，以及后续开源生态下的发展趋势，包括：<br>
​<br>
<ol><li>云原生应用部署的问题与挑战。</li><li>K8s 原生应用负载的基本能力。</li><li>OpenKruise 如何满足超大规模业务场景下的部署发布诉求。</li><li>以阿里巴巴应用场景为例，介绍使用 OpenKruise 做应用管理的实践。</li><li>未来云原生下，应用负载领域的发展趋势与方向。<br>
​</li></ol>
                                
                                                              
</div>
            