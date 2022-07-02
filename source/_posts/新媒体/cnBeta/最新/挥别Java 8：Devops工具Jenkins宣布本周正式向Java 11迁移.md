
---
title: '挥别Java 8：Devops工具Jenkins宣布本周正式向Java 11迁移'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0702/cf8010affedefc2.png'
author: cnBeta
comments: false
date: Sat, 02 Jul 2022 05:38:39 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0702/cf8010affedefc2.png'
---

<div>   
由 Kohsuke Kawaguchi 打造的 Jenkins（最初被称作 Hudson）Devops 工具，转眼已经过去了十个年头。在 Oracle / Sun 收购引发的分叉之前，用 Java 编写的该平台在持续集成和交付领域相当受欢迎。<strong>最新消息是，Jenkins 项目组刚刚表示，本周的 2.357 和即将于 9 月到来的 LTS 版本，都将需要在 Java 11 的基础上运行。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0702/cf8010affedefc2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0702/cf8010affedefc2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（来自：<a href="https://www.jenkins.io/" target="_self">Jetkins.io</a>）</p><p>虽然 Jenkins LTS 核心支持 Java 11 已有一段时间，但作为一个“长期支持版本”（LTS），Java 11 本身已可追溯到 2018 年。</p><p>此外作为向 2014 年发布的 Java 8 告别的一部分（供应商将持续支持到 2030 年），六月 LTS 也已经支持 Java 17（Java SE 的最新 LTS）。</p><p>Jenkins 团队指出，虽然项目会在可预见的一段时间内保留在 Java 8 上，但这么做将是不够严谨的。</p><p>毕竟 Jenkins 使用的多个第三方库，都依赖于更高的 Java 版本，因而坚持使用 Java 8 会导致上游项目的更新变得更少。</p><p><img src="https://static.cnbetacdn.com/article/2022/0702/75ddfd7fab6c35e.jpg" referrerpolicy="no-referrer"></p><p>问题在于，从 Java 8 / 9 向更高版本的转变，同时也会给诸多开发者带来各式各样的挑战 —— 无论是语言 / 运行时等方面的技术支持、还是法律层面的许可政策问题。</p><p>痛定思痛之后，Jenkins 最终还是在 2018 年开启了对 Java 11 的支持工作，并随着本周的发布而正式提出了这一要求。</p><p>另外 Jenkins 也将带来对 Java 17 的全新支持，只是目前尚未抵达可向社区快速推广开来的阶段。</p><p>好消息是，未来从 Java 11 向 Java 17 迁移的过程，肯定不会像从 Java 8 向 Java 11 迁移那样痛苦。</p>   
</div>
            