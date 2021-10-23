
---
title: '微软在最后一刻砍掉.NET 6热重载代码 结果惹恼开源社区'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1023/fa1fba798a907e9.jpg'
author: cnBeta
comments: false
date: Sat, 23 Oct 2021 05:56:43 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1023/fa1fba798a907e9.jpg'
---

<div>   
在萨蒂亚·纳德拉接管了微软 CEO 的职务之后，这家软件巨头一直在过去 10 年里积极拥抱开源，并且主动传达了对 Linux 和开源社区的热爱。五年前，该公司更是加入了 Linux 基金会，且官方对此表示了赞许。<strong>然而由于 .NET 社区正在酝酿的一场风暴，所有这些善意，都正处于一触即溃的危险边缘。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1023/fa1fba798a907e9.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>据悉，微软内部的一项有争议的商业决策，让许多人都开始质疑该公司对开源的承诺。多个消息来源向 TheVerge 透露，此举同样激怒了微软自家的许多开发者，但他们却被压着不许公开抱怨。</p><p>具体说来是，在本周即将发布的 .NET 6 中，这家雷德蒙德软件巨头悄然删除了 Hot Reload 的一个关键部分。该功能基本上允许开发者在创建项目时获得即时反馈、并更改代码以立即查看结果。</p><blockquote><p>与竞争对手 Google 家的 Dart 编程语言和 Flutter 开发工具包来说，这是微软 .NET 框架的一个极大卖点，且该公司一直在积极将它引入 .NET 和 <a data-link="1" href="https://microsoft.pvxt.net/zaZYr" target="_blank">Visual Studio</a> 集成开发环境。</p><p>微软最初的计划描述，是将 Hot Reload 带给尽可能多的 .NET 开发者。然而最后一刻的更改，又将它局限在了 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 平台上的 Visual Studio 开发人员，而不是走向开放与跨多个平台使用。</p></blockquote><p>微软一直在测试接近最终版本的 .NET 6 候选发布（RC）版本，其允许开发者通过 dotnet watch 在各种环境和平台上使用热重载，包括流行的 VS Code 开发环境。</p><p>候选发布通常意味着功能完好、做好了投入生产的准备、且尽可能修复了测试期间发现的各种错误。</p><p><img src="https://static.cnbetacdn.com/article/2021/1023/34b7c6e44bc5216.png" alt="2.png" referrerpolicy="no-referrer"></p><p>然而本周早些时候宣布的最后一分钟修改，又仅在 Visual Studio 2022 中启用了热重载功能。负责该功能的微软项目经理 Dmitry Lyalin 给出的理由是，其旨在为大多数用户提供最佳体验。</p><p>但是在 GitHub 上，还是有大量开发者对此表达了严重的挫败感，Hacker News 和微软官方播客文章下的评论也是一篇骂声。曾在微软 F# 团队工作的 Phillip Carter 在评论中写道：</p><blockquote><p>在查看了源码之后，我发现了一个更让人感到失望的事实 —— Hot Reload 的支持代码只有 1~2 千行左右，但它们还是在最后一刻被撕票了。</p><p>作为一项起初并不局限于 Visual Studio 的功能，这是一个明显的倒退，我真不希望微软就此走上回头路。</p></blockquote><p>The Verge 了解到，从 .NET 6 中删除该功能的决定，是由微软开发部门负责人 Julia Liuson 做出的。消息人士称，此举是一项以业务为主导的决定。</p><p><img src="https://static.cnbetacdn.com/article/2021/1023/6673e8ea496cc73.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（传送门：<a href="https://github.com/dotnet-foundation/Home/discussions/40" target="_self">GitHub</a>）</p><p>显然，微软本想着偷偷引入这项变化，且预计不会引发强烈的反对。</p><p>但是对于长期在开源社区从事 .NET 相关工作的微软自家工程师看来，连他们都感到了深深的伤害与背叛，甚至担心这一决定会对微软后续的开源工作产生持久不利的影响。</p><p>最初在 GitHub 上曝光此事的独立开发者 Reily Wood 写道：</p><blockquote><p>如果你想获得良好的开发体验，Visual Studio 无疑是最佳的选择。但 .NET 团队的所作所为，又与所有跨平台工作背道而驰。</p></blockquote><p>回顾 2014 年，当时微软宣布了要将 .NET 开源。之后其本应保持独立自治，以期改善 .NET 开源软件的开发与写作。</p><p>然而近日，一位卸任的董事会成员对 .NET 基金会的角色提出了质疑，询问它是否仅代表微软的意愿行事、还是致力于帮助培养和促进一个健康的社区？</p><p>更让广大开发者感到愤怒的是，微软还锁定并限制了一个查询请求，以删除 .NET 6 中用于 dotnet watch 的热重载功能 —— 这严重阻碍了社区评论、以及拒绝最后一分钟的更改。</p><p>即使目前社区已经提交了自己的查询请求，以撤销微软的这项变动，但现在看来也是不大可能得到回应的。</p>   
</div>
            