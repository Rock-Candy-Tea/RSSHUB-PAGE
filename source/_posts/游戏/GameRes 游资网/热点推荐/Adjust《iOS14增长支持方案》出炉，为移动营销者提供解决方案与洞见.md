
---
title: 'Adjust《iOS14增长支持方案》出炉，为移动营销者提供解决方案与洞见'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202105/11/110916deg2k6zzbdb2rztg.png'
author: GameRes 游资网
comments: false
date: Tue, 11 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/11/110916deg2k6zzbdb2rztg.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2496292">
北京，2021年5月10日讯，全球应用营销平台 Adjust今日推出《iOS14增长支持方案》，旨在帮助移动营销者在后iOS14的世界中继续以数据为基础，做出明智的决策以保持业务增长。该方案分析了iOS 14.5 后移动应用行业发展的关键趋势，结合iOS 14 应用变现最佳做法示例，以及Airship 和 Smadex 等合作伙伴就 iOS 14 对行业产生的影响提供专业见解提供了全面的解析。<br>
<br>
<div align="center">
<img id="aimg_977455" aid="977455" zoomfile="https://di.gameres.com/attachment/forum/202105/11/110916deg2k6zzbdb2rztg.png" data-original="https://di.gameres.com/attachment/forum/202105/11/110916deg2k6zzbdb2rztg.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/11/110916deg2k6zzbdb2rztg.png" referrerpolicy="no-referrer">
</div><br>
自Apple 宣布 iOS 14 和 AppTrackingTransparency 框架 (ATT) 以来，整个生态系统中围绕这一变化出现了许多困惑。许多人都不明白在新规之下哪些做法符合规定，哪些不符。<br>
<br>
需要切记的一点是，Apple 推出 ATT 的初衷与各类隐私法规 (如 GDPR) 的目的非常类似。这些规则之所以会存在，是为了让用户自主决定第一方是否可以与第三方分享可用来识别具体用户的持久性唯一数据。<br>
<br>
听起来很简单？但为何这一规则的适用范围会激起如此多的争论？出现困惑的部分原因，是整个行业缺乏通用的标准化用语。类似的概念在不同行业参与者那里会有不同的称谓。此外，行业内一直将实际指纹识别与概率归因两种方法统称为 "指纹识别"，这让如今的形势更为复杂。为应对 iOS 14.5，一些公司 (包括 Adjust) 都用概率归因完全取代了指纹识别。这就意味着我们要区分并明确人们对 "指纹识别" 这个术语的理解，并阐释哪些做法是被允许的。<br>
<br>
为此，Adjust对几个重要的术语进行了定义，帮助移动营销者更好的理解。<br>
<br>
<strong>1.指纹识别 (fingerprinting)</strong><br>
<br>
指纹识别是一种跨媒界跟踪用户的办法，会利用设备信息创建持续而唯一的 ID。该方法背后的技术例如会捕捉字体度量 (font metrics) 和利用 WebGL (以及 canvas) 属性，同时结合特定的硬件属性。这些数据让设备指纹具有持久性，且能被用来识别具体用户。不同网站和应用之间不会共享 ID，因此要想跨网站和应用跟踪用户，指纹识别和指纹 ID 就成了行业中的主流做法。例如，指纹识别可以用来绘制设备图表 (device graph)，但这种做法明显有违 Apple 的新规。<br>
<br>
<strong>2.概率 (probabilistic)</strong><br>
<br>
作为一家 MMP，Adjust 不会跨网站或应用跟踪或定向用户。其目标是以一定程度的准确性将安装归因到交互。80% 的安装都发生在广告点击后的第一个小时内，这类安装的归因不需要任何持久性 ID。Adjust可以使用临时数据进行预测，这些数据可能在几个小时内就会失效。因此对Adjust来说，概率归因只基于设备的熵 (entropy，在计算机领域，熵用来描述系统的混乱无序程度。操作系统和应用会收集熵用于加密或其他需要随机数据的操作。) 和运行规律等信息。此外，Adjust会分析点击时间、安装时间和基本设备信息等有限的参数，从而在点击后几小时内推测安装的来源。<br>
<br>
<strong>3.转化模型 (conversion modeling)</strong><br>
<br>
转化模型会对已授权用户的行为进行分析，据此推测所有用户的聚合行为，并建立模型。据我们所知，目前可行的转化模型有两类。第一类是用于归因目的。数据分析公司会跟踪已授权用户的数据，了解这些用户在安装后的行为，之后基于这些数据，在所有用户中应用类似指标。这样，广告主就可以获得同期群指标数据，例如 LTV 和 ROAS。营销人员手上的数据必须精确，所以营销者始终需要考虑此类数据的精确性。转化模型的精准度取决于用户的选择加入率。第二类是用于定向广告目的。同样，媒体公司会使用已授权用户的数据，基于相似的上下文线索，向拒绝授权的用户投放广告。<br>
<br>
<strong>4.SKAdNetwork</strong><br>
<br>
SKAdNetwork 是 Apple 的归因框架。在这个隐私为重的新时代，媒体渠道可以将该框架作为真实归因数据来源。SKAdNetwork 的优势在于能提供几乎 100% 精确的归因。对此Adjust开展了测试，与 IDFA 精确归因相比，SKAdNetwork 的准确性只差了 2%。如果某个推广活动之前通过 IDFA 归因获得了 1000 次安装归因，SKAdNetwork 可能会归因 900 次安装和 100 次重装。这是因为 SKAdNetwork 只会为每个 iTunes 账户归因一次安装。因此，为了与 ATT 执行前的情况保持一致，分析安装和重装的总量非常重要。<br>
<br>
还有一点不容忽视：SKAdNetwork 尚未覆盖所有可用的广告位，而各个广告发行商与该框架的集成还在进行中。在覆盖率接近 100% 之前，SKAdNetwork 报告的安装量会比 iOS 14.5 前通过 IDFA 精确归因得出的安装量少。<br>
<br>
<strong>5.合理预估用户选择加入率</strong><br>
<br>
25% 的用户已在机器层级上禁止 IDFA 分享，因此，剩余 75% 的用户可以看到许可请求。根据Adjust分析表明，这部分剩余用户中大约 40% 的人会同意分享 IDFA，因此营销者的IDFA 授权率大约可达到 30%。<br>
<br>
那么，新规落地会对不同参与者带来怎样的影响？每一次平台变化都是有人欢喜有人忧。对这次变化带来的影响了解不足的移动公司注定会错过一次增长机遇，而那些反应迅速的公司则能推动创新，抢占先机。因此，既有第一方数据又能随机应变的竞争者最有可能胜出。<br>
<br>
进一步了解 Adjust的最新《iOS 14 增长支持方案》，请点击https://www.adjust.com/zh/resources/ebooks/how-adjust-is-supporting-growth-through-ios-14/下载。<br>
<br>
<strong><font color="#de5650">关于 Adjust</font></strong><br>
<br>
Adjust 是一个全球应用营销数据分析平台，秉承最高的隐私和效果标准。Adjust 的解决方案包含归因服务、数据监测、防作弊、网络安全及自动化产品。公司使命是让营销变得更简单、更智能、更安全，为使用 Adjust 的 50,000 多个应用提供帮助。<br>
<br>
媒体联络<br>
崔诗悦<br>
大中华地区高级市场经理<br>
pr@adjust.com<br>
<br>
</td></tr></tbody></table>



  
</div>
            