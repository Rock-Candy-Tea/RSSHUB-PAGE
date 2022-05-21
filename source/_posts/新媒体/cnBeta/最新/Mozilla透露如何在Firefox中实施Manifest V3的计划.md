
---
title: 'Mozilla透露如何在Firefox中实施Manifest V3的计划'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0521/c4852f8cfde4810.png'
author: cnBeta
comments: false
date: Sat, 21 May 2022 12:31:53 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0521/c4852f8cfde4810.png'
---

<div>   
<strong>Mozilla已经透露了它计划如何在Firefox中采用Manifest V3。</strong>该公司表示，Firefox浏览器将在2022年底前全面采用网络扩展平台的下一次迭代，在这之前，它将推出一个新的开发者预览计划，以收集网络开发者的反馈。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0521/c4852f8cfde4810.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0521/c4852f8cfde4810.png" title alt="3VAH~O9IZ9@&#125;`&#125;SE839$$4J.png" referrerpolicy="no-referrer"></a></p><p><strong>什么是Manifest V3？</strong></p><p>Manifest V3是网络扩展平台的最新一组变化，以使扩展更安全、更快速和对隐私友好。它是由Google在2019年首次宣布的，Manifest V3中最有争议的变化之一是取消了Web Request API，转而使用新的Declarative Net Request API。开发者社区广泛批评了这一变化，因为它剥夺了扩展的许多有用的功能，使它们变得不那么有效。Google Chrome已经停止接受基于Manifest V2的新扩展，而现有的Manifest V2扩展将在2023年1月后停止工作。</p><p><strong>Mozilla希望以不同的方式实现</strong></p><p>Mozilla表示，它已经意识到Manifest V3中提出的一些有争议的变化，以及它对广告拦截器和其他扩展的削弱作用。为此，Mozilla说它在实施Manifest V3时将采取与Google浏览器不同的方法。Mozilla认为，新的声明式网络请求API并不完全是WebRequest API的完美替代品，它限制了广告屏蔽器和隐私扩展的范围。因此，Firefox将在Manifest V3中保留对"阻止WebRequest"的支持，同时也支持DeclarativeNetRequest。</p><p>"Mozilla将在MV3中保持对阻止WebRequest的支持。为了最大限度地与其他浏览器兼容，我们还将发货支持DeclarativeNetRequest。我们将继续与内容封锁者和该API的其他主要消费者合作，以确定当前和未来适当的替代方案，"Mozilla高级软件工程师Rob Wu写道。</p><p>Mozilla也不喜欢Chrome使用的后台服务，因为它不支持许多用例，而且要求开发者重写很大一部分扩展代码。Mozilla在去年提出了Event Pages来解决这些缺点，并表示这一建议受到了社区的欢迎，接下来在Firefox的Manifest V3的实施中得到全面支持。Mozilla说，出于兼容性的考虑，它还将支持Service Workers，因为Mozilla认同他们是一个具有定义寿命的事件驱动环境，已经是网络平台的一部分并具有良好的跨浏览器支持。</p><p>"在Firefox中，我们已经决定在MV3中支持事件页，我们的开发者预览版将不包括Service Workers（正在继续努力为未来的版本支持这些服务工作者）。这将帮助开发者更容易地迁移现有的持久性背景页面以支持MV3，同时保留对MV2中所有DOM相关功能的访问。"</p>   
</div>
            