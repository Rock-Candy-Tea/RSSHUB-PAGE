
---
title: 'iOS隐私保护时代，CEO关心的5个问题'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202108/18/173218h3s3vvvf15fh3v5d.png'
author: GameRes 游资网
comments: false
date: Wed, 18 Aug 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202108/18/173218h3s3vvvf15fh3v5d.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2510632">
随着ATT（AppTrackingTransparency）框架上线，移动行业进入了一个营销新模式，整个行业将会更加深切体会到，在尊重用户隐私新模式下，用户获取的方式将与过去5年大不相同。<br>
<br>
iOS14.5 ATT 框架的正式推出意味着此前 iOS平台IDFA的广泛使用将不再可行，移动营销效果将难以衡量，加上以往的 LTV 模型或将被淘汰，广告campaign和在广告渠道的出价和预算优化等方面将面临巨大挑战<br>
<br>
尽管许多UA买量和分析专业人士已经在为这种转变做准备，但从长远来看，对于以app发展为基础的公司而言，思考并构建能够适应iOS14.5 的解决方案才是重中之重。如果解决方案的框架和执行没有得到公司各部门最高领导层的严格评估，UA买量的利益相关者都有可能受到新的移动营销模式影响。<br>
<br>
在本文中，我们将分享公司的决策层（特别是CEO）在移动应用UA 买量和分析层面关注的5个问题，确保UA买量能够应对新的 ATT 框架带来的挑战。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">1. SKAdNetwork广告campaign将如何生成ROAS报告？</font></strong><br>
<br>
现在，绝大多数的广告主都会使用cohort同期群LTV模型来衡量广告campaign的效果。但由于iOS14.5导致预测LTV的关键信息的缺失（包括campaign ID、campaign名称、来源名称等），基于cohort同期群的LTV 模型实际已经失效。由于缺少 IDFA，SKAdNetwork提供的安装数据与广告campaign无法进行关联。传统的7日ROAS（D7 ROAS）报告将失去效力。<br>
<br>
SKAdNetwork可以提供D0 KPI数据报告，但不提供较长的预测窗口，移动营销人员将无法获取较长时间的“广告转化价值”（ ConversionValue），比如 D7、 D30、 D180和 D365。<br>
<br>
CEO对UA买量及分析团队提出的问题：<br>
<br>
· 如何衡量ROAS？<br>
<br>
· 如何预测和报告移动营销广告campaign的长期效果？<br>
<br>
如果想知道近期获取的cohort同期群是如何随时间推移而不断成熟的，要对基于以往cohort同期群数据的ROAS分析进行什么更新？<br>
<br>
<div align="center">
<img id="aimg_1001698" aid="1001698" zoomfile="https://di.gameres.com/attachment/forum/202108/18/173218h3s3vvvf15fh3v5d.png" data-original="https://di.gameres.com/attachment/forum/202108/18/173218h3s3vvvf15fh3v5d.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/18/173218h3s3vvvf15fh3v5d.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">2. 要使用哪部分数据来衡量广告效果？</font></strong><br>
<br>
由于无法获取与安装相关的设备IDFA，SKAdNetwork广告campaign带来的效果就无法被精准衡量，这会导致安装后用户产生的收入和应用内互动事件的报告受限。大多数广告主只能利用SKAdNetwork所提供的报告来衡量广告campaign效果，评估的数据将仅限于 D0 KPI，如“完成教程”或“完成购买”。<br>
<br>
CEO对UA买量及分析团队提出的问题：<br>
<br>
· 除了 SKAdNetwork 的数据之外，我们还将使用哪些额外的数据来衡量广告效果？<br>
<br>
· 如何使用应用内用户数据来建立统计模型，并对安装后产生的收入进行归因？<br>
<br>
· 如何衡量增量? 如何理解自然安装的价值？<br>
<br>
<div align="center">
<img id="aimg_1001699" aid="1001699" zoomfile="https://di.gameres.com/attachment/forum/202108/18/173218a8vgv4c03bo72y7o.png" data-original="https://di.gameres.com/attachment/forum/202108/18/173218a8vgv4c03bo72y7o.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/18/173218a8vgv4c03bo72y7o.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">3. 报告数据不完整，如何使用广告转化价值数据？</font></strong><br>
<br>
广告主很快意识到：作为SKAdNetwork的一部分，Apple实施的隐私门槛限制了他们期望收集的数据量。来源app ID 和广告转化价值数据是用来确定某个安装是在何处产生的，并能够粗略估计用户安装后的 LTV。然而，大部分这些数据广告主们都无法获取。一些广告主表示，高达80% 的广告转化价值数据会丢失，那些他们希望能够回传给MMP的数据将不复存在了。<br>
<br>
CEO对UA买量及分析团队提出的问题：<br>
<br>
· 当缺少广告转化价值数据时，如何衡量广告campaign效果？<br>
<br>
· 如果没有一个完整的短期广告campaign效果记录，该如何优化广告campaign效果？<br>
<br>
<div align="center">
<img id="aimg_1001700" aid="1001700" zoomfile="https://di.gameres.com/attachment/forum/202108/18/173218vu5iqttlyrkzlwlt.png" data-original="https://di.gameres.com/attachment/forum/202108/18/173218vu5iqttlyrkzlwlt.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/18/173218vu5iqttlyrkzlwlt.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">4. 如何使用建模后的广告转化价值数据（即SKAdNetwork无法追踪的广告转化价值）？</font></strong><br>
<br>
Google和Facebook均表示，当SKAdNetwork缺少广告转化价值这部分数据时，他们可以为广告主提供建模后的转化值。但目前无法对这一模型及其精准度进行验证。甚至在某些情况下，这个模型也有可能对其他广告联盟同样缺失广告转化价值的安装产生竞食效应。此外，也存在所谓“缺失”的广告转化价值的数据是来自于自然量的可能性。<br>
<br>
CEO对UA买量及分析团队提出的问题：<br>
<br>
· 要如何使用建模后的广告转化价值？<br>
<br>
· 如何协调该建模数据集和来自SKAdNetwork的实际数据？<br>
<br>
· 缺失的广告转化价值数据会如何影响预算决策？<br>
<br>
<div align="center">
<img id="aimg_1001701" aid="1001701" zoomfile="https://di.gameres.com/attachment/forum/202108/18/173218y6jj4srokno6r2cj.png" data-original="https://di.gameres.com/attachment/forum/202108/18/173218y6jj4srokno6r2cj.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/18/173218y6jj4srokno6r2cj.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">5. 如何优化不同UA campaign及针对不同渠道的预算及竞价？</font></strong><br>
<br>
受SKAdNetwork隐私保护限制，大多数UA买量团队无法通过SKAdNetwork campaign获得长期 ROAS 报告，并且仅能获取部分 D0 KPI数据报告。这极大地限制了UA买量团队在不同campaign和不同渠道的预算分配。<br>
<br>
CEO对UA买量及分析团队提出的问题：<br>
<br>
· 将如何在SKAdNetwork 各广告campaign之间分配预算？<br>
<br>
· 将使用哪些数据来决定预算分配？<br>
<br>
如何分配渠道级别的预算？<br>
<br>
<div align="center">
<img id="aimg_1001702" aid="1001702" zoomfile="https://di.gameres.com/attachment/forum/202108/18/173219gorlruuyzzjrhlel.png" data-original="https://di.gameres.com/attachment/forum/202108/18/173219gorlruuyzzjrhlel.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202108/18/173219gorlruuyzzjrhlel.png" referrerpolicy="no-referrer">
</div><br>
要解决摆在面前的这些难题，绝非易事。在踏入这个充斥着不确定性的时代之际，对任何一个基于app并依赖 UA 买量实现业务增长的公司来说，UA买量和分析团队能对他们所做的决定负责至关重要，这也关乎公司是否能够实现长期健康发展。<br>
<br>
Vungle旗下AlgoLift致力于帮助广告主实现iOS平台UA买量的成功，为广告主提供相关问题的解决方案。<br>
<br>
</td></tr></tbody></table>



  
</div>
            