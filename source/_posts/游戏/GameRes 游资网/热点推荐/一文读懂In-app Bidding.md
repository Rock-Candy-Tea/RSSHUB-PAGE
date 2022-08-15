
---
title: '一文读懂In-app Bidding'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/12/112610g6cfbnautkt26esv.jpg'
author: GameRes 游资网
comments: false
date: Fri, 12 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/12/112610g6cfbnautkt26esv.jpg'
---

<div>   
近期Google面向第三方聚合工具开放Bidding功能。Applovin Max、Chartboost Helium等聚合工具也已经宣布支持Google Bidding。这也为大部分开发者使用Google Bidding带来了进一步的便利。Bidding相对于传统的Waterfall来讲有着十分明显的优势：更低的认知成本、更便捷的运营维护方式、更高的收益。<br>
<br>
（关于传统Waterfall的内容大家可以参考《Bidding时代全面到来之前，如何实现Waterfall调优》这篇文章）<br>
<br>
这次主要想和大家聊聊Bidding的交互逻辑、分析优化、以及个人对Bidding的看法。<br>
<br>
<strong><font color="#de5650">Bidding的实现逻辑</font></strong><br>
<br>
（对实现逻辑不感兴趣的盆友可以直接跳过这段）<br>
<br>
Bidding的实现需要从两方面来说：<br>
<br>
1.Network对Bidding接口的支持实现；<br>
<br>
2.聚合工具对Bidding的支持实现；<br>
<br>
<strong><font color="#de5650">Network对Bidding接口的支持实现</font></strong><br>
<br>
应用内竞价（in-app bidding）是一种程序化的交易技术，开发者应用作为“拍卖方”向各个广告平台发起询价，出价最高的广告平台胜出并获得为此次展现广告的机会。<br>
<br>
支持应用内竞价的广告平台会提供应用内竞价的接口给开发者使用。<br>
<br>
接口主要实现的功能：<br>
<br>
<ul type="1" class="litype_1"><li>实时处理竞价请求与竞价响应，并定义接口参数；</li><li>对每一次广告展示机会提供出价；</li><li>处理获胜通知；<br>
</li></ul><br>
<br>
接口一般会参考「OpenRTB协议」进行设计。<br>
<br>
以ORTB Request/Response and Supported Ad Formats 为例<br>
<br>
OpenRTB protocol v2.5<br>
<br>
链接：<br>
<br>
https://www.iab.com/wp-content/uploads/2016/03/OpenRTB-API-Specification-Version-2-5-FINAL.pdf?fbclid=IwAR2_Q65g0z4wKs3hh1tSi_vmC9Ye0OkxRrgbBx5S94ZxjGl7HHfsTIs08-c<br>
<br>
<div align="center">
<img aid="1049887" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112610g6cfbnautkt26esv.jpg" data-original="https://di.gameres.com/attachment/forum/202208/12/112610g6cfbnautkt26esv.jpg" width="600" id="aimg_1049887" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112610g6cfbnautkt26esv.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1049888" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112615fivavitx9px3xow9.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112615fivavitx9px3xow9.png" width="600" id="aimg_1049888" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112615fivavitx9px3xow9.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">S2S和C2S两种接入方式的区别</font></strong><br>
<br>
Network的in-app bidding接口一般支持S2S与C2S两种方式，其中S2S的接入方式最为普遍。<br>
<br>
<strong>S2S</strong><br>
<br>
竞价交互主要是在服务器之间进行交互。<br>
<br>
在使用S2S方式接入时，需要客户端先获得「竞价token」，再经由应用端服务器向「network服务器」发出竞价请求。<br>
<br>
竞价请求从应用服务器端（也可能是聚合服务器端）向network的服务器发出，network服务器再向应用服务器端返回竞价响应，然后进行比价。<br>
<br>
<div align="center">
<img aid="1049889" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112618merkfkputit11wi1.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112618merkfkputit11wi1.png" width="600" id="aimg_1049889" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112618merkfkputit11wi1.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（图：Facebook Server-to-Server Integration Architecture）</font></font></div><br>
<strong>C2S</strong><br>
<br>
开发者无需自建服务器，即可在应用客户端调用广告平台竞价接口进行询价和完成比价。在使用C2S方式接入时，通常只需要由广告平台SDK向自己的服务端发送符合要求的竞价请求信息即可。<br>
<br>
<div align="center">
<img aid="1049890" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112621md7q1udc7hhe99ig.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112621md7q1udc7hhe99ig.png" width="600" id="aimg_1049890" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112621md7q1udc7hhe99ig.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（截图来自Mintegral 应用头部竞价集成文档）</font></font></div><br>
另外，部分广告平台为了方便会直接在返回的竞价响应信息中直接包含广告素材，这种做法可能增加客户端的负荷、增加应用崩溃的可能性。<br>
<br>
<strong><font color="#de5650">聚合工具对Bidding的支持实现</font></strong><br>
<br>
聚合工具必须要兼容各个network的竞价接口，并且按照一定规则做比价处理，最终实现把价格高的广告展现给用户。<br>
<br>
比价过程一般可以通过三种方式解决：<br>
<br>
<ul type="1" class="litype_1"><li>自建in-house服务器，运行自定义竞价规则</li><li>第三方竞价服务器（主要是聚合工具）</li><li>在用户的客户端进行比价<br>
</li></ul><br>
通过聚合工具实现应用内竞价因为既不用自己编写竞价逻辑，也不需要搭建自己的服务器，成为了很多开发者的选择。<br>
<br>
<strong><font color="#de5650">聚合工具如何实现应用内竞价</font></strong><br>
<br>
大部分聚合工具都会提前与各个network做好bidding的相关对接，开发者的接入成本也很低。不同的聚合工具对于bidding的实现主要区别在于支持bidding的network数量、比价逻辑、与混合（传统waterfall的兼容）三方面。<br>
<br>
<strong>各聚合对network bidding的支持情况</strong><br>
<br>
一般来说聚合工具都会背靠自己的network，所以一般有聚合产品的network为了保护自身聚合工具的优势不对第三方聚合工具开放bidding接口，如ironSource、Applovin就不对第三方聚合开放bidding接口。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049891" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112623crftlgkcokpofdgr.jpg" data-original="https://di.gameres.com/attachment/forum/202208/12/112623crftlgkcokpofdgr.jpg" width="600" id="aimg_1049891" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112623crftlgkcokpofdgr.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">‍OPMETA优化研习社公众号后台回复</font></font></div><div align="center"><font size="2"><font color="#808080">「聚合」可获得高清表格</font></font></div><br>
<strong>比价逻辑</strong><br>
<br>
基本所有聚合工具都会遵循“价高者获胜”的原则进行比价。但由于竞价响应时间、预加载广告数量、兼容非bidding广告等因素在具体规则上各有差异。<br>
<br>
有些童鞋会问聚合工具是否会存在比价公平性的问题？竞价环节是否存在黑盒成分，使得竞价结果倾向某个利益方角色？凭作者自身经历来说并不能排除这种可能。<br>
<br>
如何验证聚合工具的竞价公平性？<br>
<br>
<ul type="1" class="litype_1"><li>如果聚合工具已经提供竞价日志的查询功能，可以遍历或者抽查检验每次广告展现机会对应的竞价情况和获胜情况；</li><li>某些聚合工具若在客户端进行比价可以通过抓包进行检验，偏技术的童鞋可以尝试；<br>
</li></ul><br>
某些聚合工具会在服务端做一次比价再在客户端做一次比价，这样做的原因多数是适配一些只提供C2S bidding接口方案的network。<br>
<br>
<strong>与混合（传统waterfall的兼容）</strong><br>
<br>
虽然bidding很美好，但并不是开发者使用的所有network都能支持bidding的方式进行广告投放。也不能由于某些network用不了bidding功能，我们就放弃这个network。所以混合模式应运而生，以下给出一种参考方便大家简单理解：<br>
<br>
<div align="center">
<img aid="1049892" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112626ik8ccmi46au7002a.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112626ik8ccmi46au7002a.png" width="600" id="aimg_1049892" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112626ik8ccmi46au7002a.png" referrerpolicy="no-referrer">
</div><br>
对于bidding和waterfall的合并到比价的过程中，一般聚合工具都会对waterfall中广告的价格进行预估（根据历史数据或设定底价）。<br>
<br>
<strong><font color="#de5650">Bidding的分析优化</font></strong><br>
<br>
<strong>关键指标</strong><br>
<br>
在上文的竞价逻辑中，大家不难发现bidding相对于传统的waterfall主要多了竞价的一轮交互过程，所以整个的漏斗分析也多了几个独特的数据指标。<br>
<br>
<div align="center">
<img aid="1049893" zoomfile="https://di.gameres.com/attachment/forum/202208/12/112627u55rillklwhs9259.png" data-original="https://di.gameres.com/attachment/forum/202208/12/112627u55rillklwhs9259.png" width="600" id="aimg_1049893" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/112627u55rillklwhs9259.png" referrerpolicy="no-referrer">
</div><br>
<strong>Bid Requests（竞价请求数）</strong><br>
<br>
每个应用内竞价广告源收到竞价请求的次数（每有一次广告展示机会，每个竞价广告源就会收到一次竞价请求）。<br>
<br>
说明：在理想情况下，每个竞价广告源收到的来自某一地区单个广告位的请求数量应该基本相等；<br>
<br>
<strong>Bids in auction（竞价参与数）</strong><br>
<br>
也称为竞价响应数（bid responses），每个广告源都可以选择是否出价，当广告源使用有效的出价进行响应时，即记为一次竞价响应。<br>
<br>
<strong>Bid Rate（竞价参与率）</strong><br>
<br>
竞价参与率=竞价参与次数/竞价请求数*100%<br>
<br>
说明：反映的是一个广告源对广告机会展现的意愿程度，可以类比下非bidding情况的填充率。额外需要说的是一般bidding中的填充率都是接近100%。<br>
<br>
<strong>Win （获胜数）</strong><br>
<br>
一般指一个竞价广告源在竞价中获胜的次数。<br>
<br>
<strong>Win Rate（胜出率）</strong><br>
<br>
胜出率= 竞价胜出次数/竞价参与次数*100%<br>
<br>
<strong>Estimated Revenue（预估收益）</strong><br>
<br>
Estimated Revenue=SUM(win price)/1000<br>
<br>
<strong>Estimated eCPM（预估eCPM）</strong><br>
<br>
Estimated eCPM=(Estimated Revenue/ Impressions) * 1000<br>
<br>
说明：这个数据指标不代表具体某次的出价高低，而是代表一个综合整体的出价情况。<br>
<br>
对于以上Bidding的相关指标，我们一般都要精细到“广告源+广告位+国家”的粒度进行分析，横向对比各个广告源竞价的意愿和出价能力。<br>
<br>
在分析过程中，由于数据指标不同一般也会与非bidding的广告源分开分析。大部分聚合工具也对bidding和非bidding的数据进行了拆表处理。<br>
<br>
在竞价过程公平的情况下，bidding部分是没有多少调优空间的，降低调优成本也是bidding的优势。对于低竞价参与率、低收入占比的广告源，我们可以去掉这个广告源，优化整体的运行效率，降低负载。<br>
<br>
另外，对于部分广告源（如Facebook、Admob），大家可以测试下「请求频次」对「竞价参与率」和「出价」的影响，以此来优化整体收益。<br>
<br>
<strong><font color="#de5650">如何看待应用内竞价</font></strong><br>
<br>
从2019年开始，各大广告平台都相继推出了自己应用内竞价方案，并提出了bidding的优势有多么的明显。淘汰传统的waterfall模式逐渐成了行业里的趋势。<br>
<br>
但这几年，随着使用bidding的越来越多，我们的收益真的提升了吗？<br>
<br>
好像没有，反而eCPM似乎是越来越低了。<br>
<br>
<strong>个人认为：</strong><br>
<br>
以开发者角度来看，bidding不是作为提升收益的有效手段，而是收益不被降低得太严重、运营精力不被陷得太深的无奈选择。从去年开始Facebook已经不再支持非bidding模式的应用变现，如果想用Facebook变现的开发者最简单的方式就是找一个支持Facebook bidding的聚合工具来实现变现功能的使用。<br>
<br>
以广告平台角度来看，一方面，bidding作为行业里公认的趋势，如果不支持bidding便是自身技术能力弱的表现，所以无论有没有效果跟随大厂也要先支持上。其实真正bidding效果的实现，不仅仅需要bidding接口上的支持，也需要network通过历史效果数据的大量积累对单次展现广告价值的准确预估。在数据效果预测这一点，可能只有大厂才能有实力做得准确；<br>
<br>
另一方面，大厂们通过bidding提升了开发者使用其变现的门槛，也巧妙地解决了在行业效果整体不好的状态下低填充的问题（Facebook bidding正好就在苹果隐私政策之后变得急迫）。<br>
<br>
所以，bidding要不要用？如果bidding问题影响了你使用主流的广告源进而导致收益与行业benchmark相差很多，要重点考虑下bidding的问题；如果你的广告变现效果和行业benchmark差不太多，没必要把bidding作为有效提升收益的手段，可以抱着测试的心态去试。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：OPMETA优化研习社</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/rVZq8iQ0n63VAc9wT9BF3A</font></font><br>
<br>
  
</div>
            