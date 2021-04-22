
---
title: 'Apple iOS 14 新政真的要落地了？别慌，Facebook正全力帮助手游应用广告主应对'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202104/15/094423ifgbvuvhavibbkiu.jpg'
author: GameRes 游资网
comments: false
date: Thu, 15 Apr 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202104/15/094423ifgbvuvhavibbkiu.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2492818">
为 Apple iOS 14 App Tracking Transparency (ATT) 框架所要求的变更做好准备，并了解Facebook为降低这一影响而改进了哪些产品内体验。<br>
<br>
<div align="center">
<img id="aimg_972182" aid="972182" zoomfile="https://di.gameres.com/attachment/forum/202104/15/094423ifgbvuvhavibbkiu.jpg" data-original="https://di.gameres.com/attachment/forum/202104/15/094423ifgbvuvhavibbkiu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/15/094423ifgbvuvhavibbkiu.jpg" referrerpolicy="no-referrer">
</div><br>
2020 年，Apple 宣布了几项产品和政策变更，iOS 系统的数据共享将因此受到影响。此番变更可能会带来诸多限制，令广告主无法在移动设备以及网络上高效触达、了解和吸引潜在玩家，因此引起了游戏业的广泛关注。<br>
<br>
Facebook Gaming 的首要任务是一如既往地为广大企业和广告主提供稳定的服务。与业界同行一样，Facebook也一直在等待 Apple 公布其政策变更的更多细节。与此同时，Facebook将协助广告主了解这些变更内容并减轻其所带来的冲击。<br>
<br>
本文将简要回顾 iOS 14 政策的要求和影响，并帮助广告主了解能够应对此番变更的业务工具全新体验。大家也可以去观看Facebook上线的最新网络研讨会（名为“助力手游广告主做好应对准备的全新 Facebook 产品体验”），以便深入了解相关主题。<br>
<br>
<strong><font color="#de5650">Apple iOS 14 的政策要求</font></strong><br>
<br>
去年 6 月，Apple 在其年度全球开发者大会上宣布了两项政策：<br>
<br>
<ul type="1" class="litype_1"><li>新的“数据营养标签”，即，自 12 月起，大多数应用必须通过 Apple 的 App Store Connect 提交有关其应用的数据使用实践的信息。</li><li>App Tracking Transparency (ATT) 提示，即，如果应用执行被 Apple 称为“跨第三方应用和网站追踪”的操作，则必须请求用户授权。<br>
</li></ul><br>
尽管 Apple 在去年年底就已推出“营养标签”和 App Tracking Transparency 提示这两项功能，但其目前仅要求实施“营养标签”功能。<br>
<br>
<strong><font color="#de5650">对 Facebook 核心广告产品的影响</font></strong><br>
<br>
这一转变可能会降低系统数据的精细度，进而影响转化的归因方式。这将对系统的许多方面造成影响，包括长期以来一直通过业务工具提供并用于优化、定位和成效衡量的事件数据。<br>
<br>
以下是Facebook为应对变更所做的一些调整：<br>
<br>
<strong>归因设置</strong><br>
<br>
Facebook将帐户层级的归因报告时间窗和广告组转化时间窗合二为一，统称“归因设置”。如下表所示，粉色一列显示的是 Android 和非 iOS 14 移动应用安装广告 (MAI)、应用事件优化 (AEO)、价值优化 (VO) 和自动应用广告 (AAA) 的统计时间窗。<br>
<br>
与此同时，所有 iOS 14 广告都将使用 SKAdNetwork API（基于最后点击归因）并通过其读取数据。<br>
<br>
<div align="center">
<img id="aimg_972183" aid="972183" zoomfile="https://di.gameres.com/attachment/forum/202104/15/094424x7z2avkj26acom66.jpg" data-original="https://di.gameres.com/attachment/forum/202104/15/094424x7z2avkj26acom66.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/15/094424x7z2avkj26acom66.jpg" referrerpolicy="no-referrer">
</div><br>
广告主会在广告组层级的广告创建流程看到这一变化，即，原来的“转化时间窗”现已被“归因设置”所取代。这些设置将自动纳入广告管理工具报告。<br>
<br>
<strong>在事件管理工具中配置应用事件</strong><br>
<br>
Facebook之前曾分享过，在 Apple 要求实施 ATT 提示功能之前，针对应用事件进行优化的广告主必须采取以下 3 个关键操作：<br>
<br>
1. 确保更新至 Facebook SDK 8.0 或更高版本（或者如果与 MMP 合作，确保对方已更新 SDK）。如果未更新至 SDK 8.0 或更高版本，广告主就将无法面向 iOS 14 用户投放应用广告；若要使用 Facebook 登录功能，广告主必须更新至 SDK 9.0。<br>
<br>
2. 如果广告主目前在使用任何一款基于应用的业务工具，则需要针对每个应用事件设置“Advertiser Tracking Enabled”(ATE) 标记。Facebook仅根据 ATE 标记来判断广告主是否希望Facebook将某事件视为拒绝追踪。如果Facebook未收到表示事件允许追踪的标记（包括未收到标记值的情况），那么Facebook会限制该事件的使用。<br>
<br>
3. 不论广告主的业务工具是怎样集成的（SDK、MMP 或应用事件 API），如果想要运行应用安装广告 (App Install Ad)，就必须在事件管理工具中配置转化方案。<br>
<br>
4. 由于 SKAdNetwork 的限制，广告主必须对应用广告业务加以整合，确保每个应用拥有一个广告帐户和 9 个广告系列，且每个广告系列拥有 5 个广告组。<br>
<br>
今年 1 月，Facebook推出了两项全新体验，旨在协助广告主执行上述建议措施。<br>
<br>
1. 广告主将可以根据业务工具集成选择和配置转化方案类型。<br>
<br>
2. 为了帮助广告主适应新的广告限制，Facebook将支持测试基于 SKAdNetwork API 的广告，并且支持在广告管理工具中进行报告。<br>
<br>
<strong>自动应用广告的优势</strong><br>
<br>
自动应用广告 (AAA) 是在 Facebook 投放应用安装广告的全新方式，有助于广告整合。这种广告可以让广告主事半功倍，达到提升成效、扩大规模并提高效率的效果。<br>
<br>
Facebook打造 AAA 的目的是为了进一步提升关键成效、在扩大营销规模的同时获得稳定成效以及简化广告和创意管理以使其比现行应用广告解决方案更加高效，进而帮助企业实现发展。<br>
<br>
AAA 的下一个目标是弥补先前应用广告解决方案的不足，帮助改善应用广告表现的稳定性。<br>
<br>
自动应用广告适用于应用安装目标，并且即将推出更多功能。Facebook预计，在 Apple 推出 ATT 提示功能后，AAA 将延续其效能优势，为企业带来一如既往或更加亮眼的成效。<br>
<br>
<div align="center">
<img id="aimg_972184" aid="972184" zoomfile="https://di.gameres.com/attachment/forum/202104/15/094425obp5lfbl8imezndd.jpg" data-original="https://di.gameres.com/attachment/forum/202104/15/094425obp5lfbl8imezndd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/15/094425obp5lfbl8imezndd.jpg" referrerpolicy="no-referrer">
</div><br>
<font size="2"><font color="#808080">原文：<a href="https://mp.weixin.qq.com/s/ffQD5SaesgEWQjm3w1ssmw" target="_blank">https://mp.weixin.qq.com/s/ffQD5SaesgEWQjm3w1ssmw</a></font></font><br>
</td></tr></tbody></table>



  
</div>
            