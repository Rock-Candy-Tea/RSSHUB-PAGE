
---
title: '华为鸿蒙 HarmonyOS 崩溃服务能力全新上线！解决卡顿、缓慢、闪退等'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/fbe77804-85d8-4f0b-bbdf-86ff637559c0.png'
author: IT 之家
comments: false
date: Wed, 18 May 2022 07:29:28 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/fbe77804-85d8-4f0b-bbdf-86ff637559c0.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1297186" rel="nofollow">肖战割割</a> 的线索投递！</div>
            <p data-vmark="ba81"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 18 日消息，华为鸿蒙宣布崩溃服务能力全新上线，帮你高效解决崩溃问题！</p><h3 data-vmark="c73a">一、为什么需要崩溃服务能力</h3><p data-vmark="0821">用户在使用原子化服务时，出现卡顿、缓慢、闪退等情况就是典型的崩溃。尽管原子化服务在发布前都会经过严格的测试，但服务发布之后，<span class="accentTextColor">面对多样的用户群、复杂的网络环境、各种类型的设备和场景时，崩溃问题不可避免。</span></p><p data-vmark="8dcc">崩溃问题会给用户带来非常糟糕的体验，可能会导致用户移除原子化服务卡片，或者在评论区给出较低评分，而开发者又很难根据用户的评价定位和复现问题。如果崩溃问题长期得不到解决，极可能会造成大量用户的流失，甚至可能会影响到品牌的形象和口碑。</p><p data-vmark="7083">为了助力开发者高效解决崩溃问题，HarmonyOS 服务开放平台推出了“崩溃服务能力”。你是否也好奇崩溃服务能力有哪些功能？如何集成该能力？让我们一起往下看吧~</p><p data-vmark="6481">注：HarmonyOS 服务开放平台是华为统一的原子化服务接入和分发平台。</p><p data-vmark="fe21">地址如下：</p><p data-vmark="18a1"><span class="link-text-start-with-http">https://developer.huawei.com/consumer/cn/console#/openCard/FastService/63</span></p><h3 data-vmark="c376">二、什么是崩溃服务能力</h3><p data-vmark="2d2f">崩溃服务能力是 HarmonyOS 服务开放平台（后文简称：服务开放平台）提供的一个功能强大、轻量级的崩溃解决方案。崩溃服务能力提供了崩溃自动上报和崩溃问题分析功能，原子化服务集成了崩溃服务能力后，崩溃问题会自动上报到服务开放平台，并自动、实时生成崩溃报告，开发者可以通过崩溃报告，复现并解决崩溃问题。</p><p data-vmark="deb2">崩溃服务能力的主要功能和描述如下表所示：</p><p data-vmark="7e0c" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/fbe77804-85d8-4f0b-bbdf-86ff637559c0.png" w="558" h="457" title="华为鸿蒙 HarmonyOS 崩溃服务能力全新上线！解决卡顿、缓慢、闪退等" width="558" height="457" referrerpolicy="no-referrer"></p><h3 data-vmark="74e5">三、如何集成崩溃服务能力</h3><p data-vmark="8f69">想拥有崩溃服务能力，首先需要进服务开放平台订阅该能力，然后下载崩溃 SDK 集成到原子化服务中。集成了崩溃 SDK 的原子化服务会在服务启动后自动初始化，当原子化服务发生崩溃时，SDK 会将崩溃的相关信息上报到服务开放平台。订阅了崩溃服务能力的开发者就可以在平台查看崩溃报告，从而快速定位并解决崩溃问题。</p><p data-vmark="5e8b">崩溃服务能力的集成步骤如图 1 所示，这些步骤分别在 HarmonyOS 服务开放平台和 DevEco Studio 中完成。</p><p data-vmark="78d8" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/2a655f28-21ea-4184-88c6-4eb4404a8731.png" w="600" h="917" title="华为鸿蒙 HarmonyOS 崩溃服务能力全新上线！解决卡顿、缓慢、闪退等" width="600" height="917" referrerpolicy="no-referrer"></p><p data-vmark="61b7">图 1 崩溃服务能力集成步骤图</p><p data-vmark="2293">注：只有实名且在受邀名单的开发者有【能力中心】</p><p data-vmark="4a49">步骤 1-4 是为了在服务开放平台订阅崩溃服务能力，以便后续方便查看崩溃报告。</p><p data-vmark="2000">步骤 5.1 和 5.2 是下载崩溃 SDK，开发者可以根据自身情况二选一。步骤 6 是将下载好的崩溃 SDK 集成到原子化服务中，崩溃 SDK 集成后，开发者就可以进入到步骤 7 调试日志接口，调试完成后到达步骤 8 上架原子化服务。之后就可以在服务开放平台查看崩溃报告。详细的崩溃 SDK 集成操作步骤请参考华为开发者论坛指导贴。</p><p data-vmark="d5b0">指导贴：</p><p data-vmark="934d"><span class="link-text-start-with-http">https://developer.huawei.com/consumer/cn/forum/topic/0204873279578010563?fid=17</span></p><h3 data-vmark="19fe">四、如何定位崩溃问题</h3><p data-vmark="52dd">如图 2 所示，开发者可以通过在服务开放平台的能力中心查看崩溃次数、崩溃率、崩溃用户数等指标，根据崩溃时间、服务版本、设备类型等筛选条件，找到需要解决的崩溃问题，然后进入问题详情后进一步查看该问题的详细崩溃信息，通过崩溃信息定位和复现问题。或者直接通过崩溃堆栈定位发生崩溃的代码，从而解决崩溃问题。</p><p data-vmark="ce65" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/3de3633a-22f0-4161-89ca-6ee588af5e4a.png" w="855" h="411" title="华为鸿蒙 HarmonyOS 崩溃服务能力全新上线！解决卡顿、缓慢、闪退等" width="855" height="394" referrerpolicy="no-referrer"></p><p data-vmark="dc31">图 2 统计报表</p>
          
</div>
            