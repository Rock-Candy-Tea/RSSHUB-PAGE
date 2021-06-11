
---
title: 'Mozilla继续炮轰谷歌FLoC广告追踪政策：隐私风险依然很大！'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0611/28cbff03eaae7b2.png'
author: cnBeta
comments: false
date: Fri, 11 Jun 2021 08:39:10 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0611/28cbff03eaae7b2.png'
---

<div>   
在周四的一篇博客文章中，Firefox 浏览器开发商 Mozilla 再次对谷歌的定向广告追踪新提案给出了警告。<strong>理由是这项简称 FLoC 的“联合学习队列”技术，仍有诸多对用户构成“重大”隐私风险的特性。</strong>文章作者 Eric Rescorla 表示，尽管谷歌宣称新的“隐私保护”机制可用于替代第三方 cookie 以开展广告追踪，但 FLoC 本身仍存在重大的隐私问题。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0611/28cbff03eaae7b2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://blog.mozilla.org/en/mozilla/privacy-analysis-of-floc/" target="_self">Mozilla Blog</a>）</p><p>据悉，谷歌为 FLoC 使用了新的“群组”标签。与更具个人针对性的 cookie 方案相比，“群组”标签会将具有相似兴趣的用户划入同一组别。</p><p>即便如此，广告商仍可将这些“群组”标签用于广告追踪目的，而无需参考特定用户的浏览器历史记录。</p><p>于是自 FLoC 提案宣布以来，包括 Brave、Vivaldi 和 Opera 在内的许多知名浏览器开发商，纷纷向谷歌表达了反对意见。</p><p><strong>Mozilla 更是在近日再次指出，相关“群组”可能仅包含数千名用户，意味着追踪器仍可非常迅速地缩小特定用户的范围。</strong></p><blockquote><p>例如，追踪公司可利用浏览器指纹识别技术，将范围精确收缩到‘群组’列表中的其中几个人。</p><p>当与 FLoC 技术配合使用时，追踪器更是只需‘相对少量的信息’即可达成这一目的。</p><p>此外追踪器能够在给定时间范围内使用 FLoC ID 的组合来区分特定用户，因为 FLoC 标识符或用户兴趣都是不恒定的。</p></blockquote><p>另一方面，FLoC 标识符泄露的信息，其实并不比 cookie 更少。与特定于某个站点的 cookie 追踪方案不同，FLoC 标识符支持跨网站使用。</p><p><strong>换言之，FLoC 将成为追踪器“借助外部关联来源数据”的共享密钥。</strong>比如拥有大量第一方兴趣数据的追踪器，可能会运行一项特定的服务 —— 仅回答有关 FLoC 标识符的兴趣话题。</p><blockquote><p>如果追踪器想要知晓‘带有该群组标签的人是否喜欢汽车？’，便可通过调用 FLoC API 来来获取‘群组’标识符，并利用它在服务中查找相关信息。</p><p>或者追踪器可结合指纹数据，来定位‘住在法国、使用 Mac、运行 Firefox 浏览器、且喜欢汽车’的特定用户。</p><p>最终结果就是，任何网站都能够通过比当下轻松得多的方式，来摸清每一个人的底细。</p></blockquote><p><strong>作为应对，谷歌也提出了某些隐私缓解对策，包括允许网站可选加入 FLoC 追踪，并限制其认为与“敏感”主题过于相关的群组。</strong></p><p>但在 Firefox 团队看来，这么做还远远不够！Eric Rescorla 写道：</p><blockquote><p>尽管这些缓解措施看起来很有用，但它们几乎都是不痛不痒的改变，无法从根本上解决上述问题。</p><p>基于此，我们建议社区需要就这些问题展开进一步的研究 —— 尤其是 FLoC 以当前的形式被推出的话！</p></blockquote>   
</div>
            