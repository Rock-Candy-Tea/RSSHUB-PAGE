
---
title: 'Newbe.Claptrap 0.10.2 发布，Blazor & Minion'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.newbe.pro/images/20210421-001.gif'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 10:41:00 GMT
thumbnail: 'https://www.newbe.pro/images/20210421-001.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#555555">Newbe.Claptrap 0.10.2 发布，我们为项目模板引入了 Minion 以及 Blazor 制作的交互界面。</span></p> 
<h2 style="text-align:justify">更新内容</h2> 
<h3 style="text-align:justify">类库常规升级</h3> 
<p style="text-align:justify">升级了相关的所有类库至最新版本。包括 Dapr SDK 1.1 等等。</p> 
<h3 style="text-align:justify">项目模板增强</h3> 
<p style="text-align:justify">现在，我们为最新的项目模板引入了 Minion 以演示如何使用 Minion 处理旁路业务逻辑。</p> 
<p style="text-align:justify">另外我们也引入了一个使用 <a href="https://ant-design-blazor.gitee.io/" target="_blank">ant-design-blazor</a> 制作的的模拟演示界面，用于展示拍卖竞价样例中的数据情况。</p> 
<p style="text-align:justify"><img alt="simulator web" src="https://www.newbe.pro/images/20210421-001.gif" style="margin-bottom:20px; margin-left:auto; margin-right:auto" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:justify">可自定义 Event 和 State 的序列化过程</h3> 
<p style="text-align:justify">现在，开发者可以自定义 Event 和 State 的序列化过程，从而定义更加自由的保存和加载过程。</p> 
<p style="text-align:justify">例如，在拍卖竞价示例中，我们使用到了 SortDictionary 作为 State 的一部分。但是，如果直接采用原生的 Json 序列化，将会导致 SortDictionary 的比较器丢失。因此，此时开发者可以使用自定义的 State Loader 来解决该问题。</p> 
<p style="text-align:justify">详细的使用方案可以常见最新的项目模板。</p> 
<p> </p> 
<h2 style="text-align:left">软件介绍</h2> 
<p style="text-align:left"><img src="https://www.newbe.pro/images/main_banner.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">这是以<code>反应式</code>、<code>事件溯源</code>和<code>Actor模式</code>作为基本理论的一套服务端开发框架。于此之上，开发者可以更为简单的开发出“分布式”、“可水平扩展”、“可测试性高”的应用系统。</p> 
<p style="text-align:start">该项目受启发于众多开源项目与博客文章：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRayTale%2FRay" target="_blank">基于Actor框架Orleans构建的分布式、事件溯源、事件驱动、最终一致性的高性能框架——Ray</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fprevious-versions%2Fmsp-n-p%2Fdn589792%2528v%253dpandp.10%2529" target="_blank">Event Sourcing Pattern</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.infoq.cn%2Farticle%2Fevent-sourcing" target="_blank">Event Sourcing Pattern 中文译文</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Forleans" target="_blank">Orleans - Distributed Virtual Actor Model</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.cnblogs.com%2Fnetfocus%2Fp%2F3149156.html" target="_blank">ENode 1.0 - Saga的思想与实现</a></li> 
</ul> 
<p style="text-align:justify">理论入门篇</p> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.newbe.pro%2FNewbe.Claptrap%2FOverview-Of-Newbe-Claptrap%2F" target="_blank">Newbe.Claptrap - 一套以 “事件溯源” 和 “Actor 模式” 作为基本理论的服务端开发框架</a></li> 
</ol>
                                        </div>
                                      
</div>
            