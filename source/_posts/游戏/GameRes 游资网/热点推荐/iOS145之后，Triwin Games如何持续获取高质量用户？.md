
---
title: 'iOS14.5之后，Triwin Games如何持续获取高质量用户？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/26/114046n2didu40b2zp5qpq.jpg'
author: GameRes 游资网
comments: false
date: Mon, 26 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/26/114046n2didu40b2zp5qpq.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2506547">
Triwin Games 的定位是一家面向海外市场的休闲游戏发行商，之所以取这个名字，是因为在游戏发行的过程中，其实涉及到三方面：第一个是游戏的开发商，第二个是游戏的发行商，第三个就是游戏的最终用户，Triwin Games 希望这三方都能够从他们所做的游戏中获得他们想要的，从而实现“三方共赢”，但在 iOS14.5 之后，Triwin 的团队不可避免的在买量上受到一定的影响，Bidalgo 中国办公室将素材分析工具和优化方法论介绍给了 Triwin Games，希望能帮助客户减少 iOS14.5 带来的影响，重新把控买量的方向, 继续实现“三赢”。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_995351" aid="995351" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114046n2didu40b2zp5qpq.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114046n2didu40b2zp5qpq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114046n2didu40b2zp5qpq.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Triwin 总部办公区一角</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><strong><font color="#de5650">iOS14.5 给我们挖了哪些坑？</font></strong><br>
<br>
在 iOS 更新到 14.5 之后，广告主无法轻易获取用户的 IDFA，整个移动互联网的广告生态不可避免地从野蛮生长转向有限制、强隐私的时代；而且不仅仅是 iOS，其他操作系统的隐私政策的收紧也箭在弦上。这种趋势带来的变化是：素材变成了广告主在监测和优化广告时唯一的可控因素。<br>
<br>
这种变化的背后其实隐藏了很多“坑”，使得广告主在进行归因策略调整时很容易出现失误，比如：<br>
<br>
1. 用 SKAN 埋点，但埋的不够多。比如有的客户只埋 2 个 SKAN 事件。收集到的数据太少。很容易导致 SKAN timer 不容易被 trigger，从而导致苹果停止归因。同时还造成渠道能优化的数据也变少了。也影响渠道效果。这样的话客户会看到很高的 zero rate.zero rate 说明有安装，无转化；<br>
<br>
2. 用 SKAN 埋点，但埋的不够靠前。比如有的客户只埋 2 个 SKAN 事件。这些事件太靠后。24 小时之内用户只要不触发这 2 个事件，苹果就停止归因了。同上，也会造成极高的 zero rate；<br>
<br>
3. 广告主的 schema 的设置需要优化。有的事件发生次数太少，会触及苹果的另外一个新政策, 如果 conversion 数量很少就不回传 conversion 给渠道了，因此会触发极高的null rate（nullrate 就说明有安装也有转化conversion，但是无回传）为什么? 苹果需要 conversion 在 24 小时之内累积到一定数目才回传，我们的理解是，苹果也不希望少量的 conversion 发出去有机会被"猜"出来是谁带来的。而且，最绝的是，“数量很少”是什么意思？几个算少？行业里面没人知道。因此广告主需要确保有跟踪高频事件；<br>
<br>
4. 有的广告主一口气把 schema 用完了，意识到有问题再来修改也很难；<br>
<br>
5. 因为以上各种原因，iOS14.5 的广告收入有时候会掉到 organic里面去，因此广告收入下滑。但是实际上 BI 里面的整体收入并没有变少。但是广告主也可能因此而焦虑，导致停止投放 iOS 广告，预算的下降反而让收入下降变成了真正的事实。<br>
<br>
针对上述情况，Bidalgo 建议 install 一旦发生要立刻回传，高频事件（发生的次数最多的事件）一定要埋点，因为这些事件可以触发 timer 以便 SKAN 持续不断的进入下一个 24 小时的追踪。同时，如果购买等行为一般都发生在 24 小时之后，则需要在 BI 里面找出能识别高质量用户的 24 小时内会发生的替代事件。用高频事件+关键 CPA 或购买+关键 CPA 或购买的 24 小时内替代事件等等，尽可能减少 zero rate & null rate，同时多多关注包括 Organic 在内的整体收入，提升 iOS 数据获取和分析能力。<br>
<br>
<strong><font color="#de5650">Triwin Games：用正确的姿势拥抱 iOS14.5</font></strong><br>
<br>
在合作的过程中，Triwin Games 和 Bidalgo 共同测试了 Bidalgo 的素材优化方法论。Triwin Games 的联合创始人秦伟分享时提到：“在使用 Bidalgo 之前，我们对素材的分析一般采用“二八法则”，也就是大家常说的“抓大放小”，主要会关注头部的素材表现去得到一个大概的判断。素材之下的内容及元素，我们也尝试进行分析，但是当时苦于缺乏相关的工具，整个分析的过程比较费时费力。”<br>
<br>
Bidalgo 的海外客户已经意识到在 iOS14.5 之后，产品分析与广告分析不得不在两个不同 的 BI 界面里进行，所以他们尽可能地利用 Bidalgo 给创意标上产品标签，获得尽可能多的数据，以便分析创意带来的转化效果，但由于忙于用户分层和缺少合适的工具，国内出海企业只能把有限的精力和时间关注在头部的素材上，从而忽略了创意整体分析及深度分析。<br>
<br>
那么，Bidalgo 是如何帮助 Triwin Games 一步步实现全方位的素材层级数据分析和优化呢?<br>
<br>
<strong>Step 1：获取创意数据汇总</strong><br>
<br>
iOS14.5 后广告优化人员需要更多的去优化创意，然而光是创意数据整合对于广告主而言就已经是一个很大的挑战，因为长久以来创意数据都分散在不同的后台，比如一张图片可以出现在 3 个渠道/10 个 campaign/100 个 ad set 下面，想要知道哪些图 ROI 更高意味着需要做大量的数据整理工作，如下图所示(为保护广告主数据隐私，文章中所有截屏都用 DEMO 账户示例)：<br>
<br>
Bidalgo 作为一个数据整合的服务商，把分散在各方的创意数据整合在一个后台，使得创意数据查询及创意优化活动变得更加便捷，彻底解决了大家在各个后台切换查询数据并导出来做数据透视表的烦恼。<br>
<br>
<div align="center">
<img id="aimg_995352" aid="995352" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114046e1yy11wt44xyhzw4.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114046e1yy11wt44xyhzw4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114046e1yy11wt44xyhzw4.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>Step 2：素材数据纵向深挖</strong><br>
<br>
在获取多方创意数据后，我们会发现一些数据黑洞，比如 FB AAA 的创意数据和谷歌的 UAC 的创意数据在第三方监测里是缺乏监测数据的。鉴于广告优化需要建立在客观的第三方监测数据分析(SKAN & MMP)基础之上，Bidalgo 基于已有的数据通过算法去填补行业内的各种数据盲区。如下图所示，通过算法可以拆解 FB AAA 广告素材层级的第三方监测的数据，以便广告主在创意层面横向比对网盟等其它渠道效果的时候，能够使用一个统一的标杆。<br>
<br>
<div align="center">
<img id="aimg_995353" aid="995353" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114047uuup0v04r5vs0kj5.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114047uuup0v04r5vs0kj5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114047uuup0v04r5vs0kj5.jpg" referrerpolicy="no-referrer">
</div><br>
在得到素材层级的第三方监测数据之后，广告主可以设置自己的标签框架（如下图），进一步分析每一个素材表现优劣背后的原因，以便更好的把握下一步广告优化及素材制作的方向。如 Triwin Games 可以分析在第一梯队国家细分市场下，究竟是什么样的视频风格及玩法类型的视频更适合该细分市场，进而不断动态调整广告预算的分布，比如暂停效果欠佳的创意和针对效果更好的图片进行扩量，达到广告投放的成本更低，回收最高。<br>
<br>
<div align="center">
<img id="aimg_995354" aid="995354" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114047wffn7q377qnd37qn.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114047wffn7q377qnd37qn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114047wffn7q377qnd37qn.jpg" referrerpolicy="no-referrer">
</div><br>
框架搭建好之后，可以进行单个素材标签下的垂直比较，很容易发现每一个标签大类下，各个标签值的数据表现差异。<br>
<br>
<div align="center">
<img id="aimg_995355" aid="995355" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114047v9iginiujs20snp8.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114047v9iginiujs20snp8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114047v9iginiujs20snp8.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995356" aid="995356" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114047rpwi0s8560uss0s5.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114047rpwi0s8560uss0s5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114047rpwi0s8560uss0s5.jpg" referrerpolicy="no-referrer">
</div><br>
因此可以得到优化洞察：<br>
<br>
<ul><li>C3、C4 及 C6 关键 KPI 效果较差，建议暂停相关素材，并降低此类素材的预算比例</li><li>C5 关键 KPI 达 25%，具有较大潜力，建议增加测试预算<br>
</li></ul><br>
同时还可以即时获得制作洞察：<br>
<br>
C7 - C11 的素材数量较少，且预算较少，无法确定效果好坏，建议制作更多相关素材和增加预算进行测试。<br>
<br>
接下来还可以进行两个素材标签下的横向比较，比如 Triwin Games 可以进一步探究“玩法类型 C2”和“机台主题 D”如何搭配使用才会达到效果最佳。<br>
<br>
<div align="center">
<img id="aimg_995357" aid="995357" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114048dgqri992bdb00wrg.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114048dgqri992bdb00wrg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114048dgqri992bdb00wrg.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995358" aid="995358" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114048gy3lh5dpyhdh3xhp.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114048gy3lh5dpyhdh3xhp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114048gy3lh5dpyhdh3xhp.jpg" referrerpolicy="no-referrer">
</div><br>
优化洞察：<br>
<br>
<ul><li>C2 和 D1 及 D6 搭配使用时关键 KPI 表现更优秀，但 D6 获得的测试预算不足，建议加大预算进一步测试<br>
</li></ul><br>
制作洞察：<br>
<br>
<ul><li>D1 表现优异，但只有两支素材，建议迭代更多相关素材<br>
</li></ul><br>
在做完诸多分析之后，广告主完成大量的新素材制作，下一个难题是究竟该如何做 A/B 测试，以达到侦测优秀素材并持续放量呢？Bidalgo 建议大家参考以下测试方法论，通过两个测试阶段：(IOS14.5 后广告主可能需要将“支付”改为上文提到的 24 小时内会发生的关键 CPA 事件)<br>
<br>
<div align="center">
<img id="aimg_995359" aid="995359" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114048oh88jhch6w5cv6vh.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114048oh88jhch6w5cv6vh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114048oh88jhch6w5cv6vh.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995360" aid="995360" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114049pnq1v306ap433up0.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114049pnq1v306ap433up0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114049pnq1v306ap433up0.jpg" referrerpolicy="no-referrer">
</div><br>
在找到优秀素材之后，需要按照什么频率把新素材更新到已有的广告呢？通过以下测试，可以得出究竟是什么样的频次更新素材会对广告效果有正向影响，如下图所示，通过测试后发现第二个广告组效果最佳，那说明每两周一次的频率更新新素材的效果更好。<br>
<br>
<div align="center">
<img id="aimg_995361" aid="995361" zoomfile="https://di.gameres.com/attachment/forum/202107/26/114049i3xj6q6clmx9jlrr.jpg" data-original="https://di.gameres.com/attachment/forum/202107/26/114049i3xj6q6clmx9jlrr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/26/114049i3xj6q6clmx9jlrr.jpg" referrerpolicy="no-referrer">
</div><br>
“Triwin 和 Bidalgo 的合作已将近两年，Bidalgo 拥有非常强大的数据整合能力，帮助我们优化同学从纷杂的数据报表中解放出来，将更多的精力专注在素材及创意分析中，特别是标签分析功能让我们在 Casino 品类的素材中进一步深耕，对我们素材制作和新素材测试有很大的指导意义。”——Triwin Games 联合创始人秦伟<br>
<br>
<font size="2"><font color="#808080">来源：白鲸出海</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/yaoW8s9q5qjxjcqiZbPJQA</font></font><br>
</td></tr></tbody></table>



  
</div>
            