
---
title: 'Unity Ads 针对 iOS 14 ATT 的准备指南'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202103/26/133115sbbzafo95fm5miao.jpg'
author: GameRes 游资网
comments: false
date: Fri, 26 Mar 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202103/26/133115sbbzafo95fm5miao.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2490520">
2021 年，新隐私保护条例的出台将给移动广告行业带来翻天覆地的变化。作为 iOS 14 更新的一部分，Apple 发布了广告跟踪变更和数据收集声明，这将迫使开发者从技术和战略层面为其应用做好准备。<br>
<br>
为帮助应用开发者和广告主做好准备，本指南提供了一份详尽的步骤清单，以确保 Unity Ads 的变现和用户获取功能在新条例下仍然有效。<br>
<br>
这是一个将影响到整个移动广告行业的重大变化。但请放心，Unity Ads 已做好充足准备，可随时满足开发者和广告主的需求，竭力助你取得成功。<br>
<br>
<div align="center">
<img id="aimg_968413" aid="968413" zoomfile="https://di.gameres.com/attachment/forum/202103/26/133115sbbzafo95fm5miao.jpg" data-original="https://di.gameres.com/attachment/forum/202103/26/133115sbbzafo95fm5miao.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/26/133115sbbzafo95fm5miao.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">应用程序准备工作</font></strong><br>
<br>
如果您在使用 Unity Ads 进行应用变现、获取用户，请确保完成以下重要步骤。<br>
<br>
<strong>对于应用开发者</strong><br>
<br>
<ul><li>A 检查当前用户的数据跟踪设置：如果你的应用使用了 Unity Ads，则可在变现后台访问这一新功能。</li><li>B 确保广告瀑布流优化已完成。</li><li>C 为用户分组制定实时运营策略。</li><li>D 优化 Opt-in 用户追踪流程，以实现收入最大化。<br>
</li></ul><br>
<strong>对于应用广告主</strong><br>
<br>
<ul><li>A 确保你的广告网络平台已注册 SKAdNetwork ID。</li><li>B 将你的第三方 SDK 更新到最新版本：这将确保 ATT 强制执行后，你可以继续优化广告</li><li>C 做好计费更改准备（因为 ATT 会影响安装后的数据回传）：广告网络平台可能无法再按 CPI 计费，而需要转为按 CPM 计费。</li><li>D 确保使用最新版本的 reporting API，以便能够使用新的 SKAdNetwork 报告选项。</li><li>E 确保你的应用已完成 Apple 隐私调查，并且了解合作伙伴的数据收集流程和政策。</li><li>F 与广告合作伙伴一起探索新的优化广告的最佳实践。<br>
</li></ul><br>
<strong>对于应用开发者兼广告主</strong><br>
<br>
<ul><li>A 从第三方 SDK 收集 Apple 隐私调查所需的一切信息。</li><li>B 将你的第三方 SDK 更新到最新版本。<br>
</li></ul><br>
<strong><font color="#de5650">SDK 对于广告主的重要性日益突显</font></strong><br>
<br>
一直以来，MMP 从不同来源收集和汇总推广效果数据，为广告主提供相关 KPI。Apple 的 SKAdNetwork 有可能改变这一局面。由于一些数据缺乏参考性，广告合作伙伴（包括广告网络平台和 MMP）必须找到替代方案来向广告主提供相关 KPI。目前，业界正在探索和引入多种标准和数据格式，帮助优化基于推广效果的机器学习。<br>
<br>
为此，许多广告网络平台（例如 Unity Ads）都在开发和发布针对广告主的 SDK。这些 SDK 旨在让广告主可以优化他们的广告，有助于加强广告网络对正在收集的数据的控制权，以及通过汇总的用户行为数据来完善其算法。<br>
<br>
<div align="center">
<img id="aimg_968414" aid="968414" zoomfile="https://di.gameres.com/attachment/forum/202103/26/133115hv3vckgvxkockl22.jpg" data-original="https://di.gameres.com/attachment/forum/202103/26/133115hv3vckgvxkockl22.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/26/133115hv3vckgvxkockl22.jpg" referrerpolicy="no-referrer">
</div><br>
此外，随着广告网络平台发布面向广告主的 SDK，这将成为广告平台发布产品更新的首选途径。对广告主来说，保持最新 SDK 集成，从最新的产品开发中受益将变得至关重要。<br>
<br>
虽然 SDK 是开发者（supply 端）经常用到的一部分，但广告主也应该意识到未来会有更多广告网络平台专用的 SDK 出现。<br>
<br>
最近 Unity Ads 已经推出了针对广告主的 SDK，如果你同时是我们变现和推广的合作伙伴，需确保你变现端的 Ads SDK 更新到最新版本。如果你只是广告主，为了你的推广活动在 ATT 生效后尽量不受影响，则需要接入我们针对广告主的 SDK。更多详情，可以直接联系你们的客户经理，我们会提供相关协助。<br>
<br>
<strong><font color="#de5650">基于安装成本的计费方式将不再流行</font></strong><br>
<br>
当前有多种计费选项可供广告主选择，例如基于单次点击成本 (CPC)、单次展示成本(CPM) 和单次安装成本(CPI) 计费。<br>
<br>
当前能够进行按安装成本计费的原因是 MMP 传递的是（用户级）未汇总的数据。这让广告网络平台能够将具体的安装归因到具体的广告系列上去，然后相应地向广告主收取成功安装的费用。这形成了一个清晰的检查流程。<br>
<br>
一旦 Apple 实施其 ATT 框架，回传数据将被汇总。这意味着广告合作伙伴（包括 MMP 和广告网络平台）可能无法再为安装归因提供清晰的检查流程。<br>
<br>
<div align="center">
<img id="aimg_968415" aid="968415" zoomfile="https://di.gameres.com/attachment/forum/202103/26/133116b9kzk495lafbkmlb.jpg" data-original="https://di.gameres.com/attachment/forum/202103/26/133116b9kzk495lafbkmlb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/26/133116b9kzk495lafbkmlb.jpg" referrerpolicy="no-referrer">
</div><br>
简而言之，iOS 的广告系列将通过点击或者展示成本计费而不是按安装计费。将来，基于安装成本的计费方式可能仅适用于安卓的广告系列，或者将完全消失。<br>
<br>
从 3 月 22 日起到 3 月底，Unity Ads 会自动地把所有 iOS Campaign，从 CPI 的结算方式陆续迁移至 CPM 结算。这种结算方式是根据 Campaign 所收到的曝光总数来收费的。意味着你目前在跑的 CPI Campaign 将来会变成 target CPI（tCPI）Campaign，而你的优化目标，比如安装，付费或者留存的优化目标不会改变。另外，从 3 月 24 日开始，CPM 结算将会是新的 iOS Campaign的唯一结算方式。结算方式的改变不会影响用户池以及你的 Campaign 接收曝光，点击和安装。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：Unity官方平台</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/LUFFUprku2akGNZfZg-ePA</font></font><br>
</td></tr></tbody></table>



  
</div>
            