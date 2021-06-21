
---
title: '_图_Chrome团队启动Aurora项目 优化网络开发'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0621/902191c52bc2246.jpg'
author: cnBeta
comments: false
date: Mon, 21 Jun 2021 06:54:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0621/902191c52bc2246.jpg'
---

<div>   
Google的 Chrome 团队曾推出多个项目，以协助框架作者采用他们认为的最佳做法，基本上都是基于 React 的 Next.js 开始的。<strong>本周早些时候，一个由 6 人组成的团队（Google内部称为 WebSDK）介绍了 Aurora 项目，被描述为“和多个框架作者合作”。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0621/902191c52bc2246.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0621/902191c52bc2246.jpg" alt="9r0jdumc.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在官方博文中谈到了该项目提供了“强大的默认值和有意见的工具”，而这些经验很多都来自 Maps、Search 等Google应用程序。Google表示，Aurora 项目能识别网络框架的弱点，特别是那些导致“用户体验痛点"的地方，然后以适应其他网络框架的方式修复它们。正如你对浏览器团队的期望，所有提到的框架都是 JavaScript 或 TypeScript（可编译为 JavaScript）。</p><p style="text-align: left;">目前该项目团队已经进行的工作包括 Next.js 的图像组件，然后移植到 Nuxt，Next.js 和 Angular 的网页字体的内联 CSS，以及 Next.js 中支持 ESLint（静态分析）的自定义插件。</p><p style="text-align: left;">一个名为 Conformance 的相关项目再次专注于最佳实践的默认值，但辅以“可操作的规则”。那些认为自己有能力编写可靠和高性能的 JavaScript 的开发者现在应该把目光移开，因为Google认为：“需要开发者做出任何决定的优化会给应用程序的性能带来风险”。</p><p style="text-align: left;">因此，该团队设计了一套静态代码分析规则和动态检查，横跨多个“<a data-link="1" href="https://microsoft.pvxt.net/9W473" target="_blank">Surface</a>s”，包括 ESLint、TypeScript、用户开发服务器的动态检查、Webpack 捆绑器和 CSS 工具。违反规则的开发人员将会被警告以修复代码。</p><p style="text-align: left;">这些创新首先出现在Next.js中，这就是为什么这些项目在本周的 Next.js 大会上被同时介绍给世界。在这次活动中，Next.js 11 被发布，Conformance 被吹捧为“一个提供精心设计的解决方案以支持最佳用户体验的系统”。</p><p style="text-align: left;">这一点，连同改进的性能和默认采用的Webpack 5，被认为是新版本的亮点。Next.js 的赞助商Vercel还展示了一个项目，将用 Create React App命令启动的React应用转换为与Next.js兼容，并预览了一个新的基于浏览器的云托管编码环境，名为Next.js Live。</p>   
</div>
            