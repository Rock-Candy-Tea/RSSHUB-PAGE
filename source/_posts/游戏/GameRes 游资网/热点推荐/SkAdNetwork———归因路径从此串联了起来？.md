
---
title: 'SkAdNetwork———归因路径从此串联了起来？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://www.gameres.com/undefined'
author: GameRes 游资网
comments: false
date: Thu, 27 Jan 2022 00:00:00 GMT
thumbnail: 'https://www.gameres.com/undefined'
---

<div>   
<div align="center">
<img aid="1029641" zoomfile="https://di.gameres.com/attachment/forum/202201/27/123422uez0fftfglqlyryk.jpeg" data-original="https://di.gameres.com/attachment/forum/202201/27/123422uez0fftfglqlyryk.jpeg" width="600" id="aimg_1029641" inpost="1" src="https://www.gameres.com/undefined" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">背景铺垫</font></strong><br>
<br>
在WWDC 2020全球开发者大会，苹果提出了“App跟踪透明度”（App Tracking Transparency，简称ATT）的概念，其中一项政策是要求开发者在商店页提供隐私惯例摘要，向用户说明被收集的数据会去往何方。这个功能已于去年12月正式上线。而这个政策下另一项功能——App想要访问用户的IDFA/在其他公司所拥有的App和网站上跟踪用户之前，必须先经得用户许可同意，于今年4月正式上线的。<br>
<br>
这一举措不禁让人们联想到在2018年Apple提出的SkAdNetwork，一种不使用用户层级数据的推广活动监测方法。<br>
<br>
<strong>苹果公司</strong><br>
<br>
iOS14发布（iOS14.5实施）：<br>
<br>
<strong>1.ATT（App Tracking Transparency）框架</strong><br>
<br>
要求开发者在商店页提供隐私惯例摘要，向用户说明被收集的数据会去往何方。<br>
<br>
App想要访问用户的IDFA/在其他公司所拥有的App和网站上跟踪用户之前，必须先经得用户许可。<br>
<br>
<strong>2.SkAdNetwork框架</strong><br>
<br>
不触达用户层级（IDFA）条件下，对用户的点击和安装行为提供的一套追踪解决方案。<br>
<br>
收益源：<br>
<br>
主要来自于硬件，虽然已经推出ASA广告业务，但起步晚，所以苹果目前不主要依靠广告来挣钱（ASA）。<br>
<br>
能从图表中鲜明看出，近7年iphone的营收占苹果营收的大份额。而包含数字广告业务等的服务业务营收并不主要，但是从趋势来看，这一块是在持续上涨的。<br>
<br>
<div align="center">
<img aid="1029629" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120036kgwxjgm0dwm444zq.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120036kgwxjgm0dwm444zq.jpg" width="600" id="aimg_1029629" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120036kgwxjgm0dwm444zq.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>移动互联网广告</strong><br>
<br>
以往利益来源：<br>
<br>
利用IDFA来获取大量用户数据，从而进行精准的广告投放。<br>
<br>
现如今：<br>
<br>
取不到用户层级的数据，精准投放受限、用户的注册、付费等后续Action信息获取受限、Re-Targeting营销活动受限等等。<br>
<br>
收益源：<br>
<br>
利用大量用户数据做到广告效果最优<br>
<br>
简短描述中我们可以看出因苹果新规制定带来的利益对冲，一边想保护用户数据，一边的发展又离不开用户数据。简单明了来说，苹果公司为顺应时代的召唤-制定新规来保护用户隐私以及提出对应新归因方案，但是这一“小举动”却可能将对广告行业整个产业链产生”革命性“影响。接下来，我们将主要把目光聚焦在SkAdNetwork，仔细瞧瞧新归因方案下，移动广告产业链中归因路径为什么依靠SKAdNetwork API实现了串联。<br>
<br>
<strong><font color="#de5650">一、IDFA时代下的归因交互与环节</font></strong><br>
<br>
在iOS的IDFA还可以使用的时候，归因平台对于广告归因，最常见的归因方式就是匹配设备ID。简单来说，应用下载首次打开激活后，归因平台获取到设备ID，并查看自己库中这个设备ID是否发生过互动行为，基于此来判断这次互动行为是来自于哪个渠道的？是来自哪个Publisher的？<br>
<br>
<strong>归因交互链路</strong><br>
<br>
我们先来看看，设备ID匹配是如何发生的，即ID匹配交互流程。<br>
<br>
<div align="center">
<img aid="1029630" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120037r7g7obacgngbbknz.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120037r7g7obacgngbbknz.jpg" width="600" id="aimg_1029630" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120037r7g7obacgngbbknz.jpg" referrerpolicy="no-referrer">
</div><br>
为方便您理解利用DeviceID进行归因，特做下图搭配使用。<br>
<br>
<div align="center">
<img aid="1029631" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120038p0bjy5kgbaltlapk.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120038p0bjy5kgbaltlapk.jpg" width="600" id="aimg_1029631" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120038p0bjy5kgbaltlapk.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>归因环节</strong><br>
<br>
再了解完设备ID匹配流程后，我们单独来看具体匹配环节设备ID是如何被用来归因的。<br>
<br>
<strong>归因SDK</strong><br>
<br>
通过广告被用户下载的应用，在First Open的时候，归因SDK会接收到其上传的设备ID。<br>
<br>
归因SDK会向归因Sever发出询问：该设备ID之前是否有过互动行为记录？<br>
<br>
<strong>归因Sever</strong><br>
<br>
归因Sever调动”互动行为数据库“。若给出肯定，并返回相关信息，如渠道、click时间、设备ID等<br>
<br>

<img aid="1029632" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120038b1ita3cw38xaj88t.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120038b1ita3cw38xaj88t.jpg" width="600" id="aimg_1029632" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120038b1ita3cw38xaj88t.jpg" referrerpolicy="no-referrer">
<br>
<br>
至此，三方就利用了设备ID，来核验这个设备ID是否有过互动行为，从而判定这个用户是不是非自然安装带来的，如果是的话，又到底是通过哪个渠道哪个publisher带来的，进而也就完成了归因流程。<br>
<br>
在这条链路上，我们可以发现，广告追踪ID的链路只能追踪到调起应用商店，后续是需要应用激活后，才能通过matching手段进行归因。也就是说，matching设备ID的方式并没有实现跳转路径从广告曝光、点击、落地页及转化都串联起来。（可以理解为：而是在商店这一步追踪链路传递就断了。）<br>
<br>
(这也是有些作者表示如果系统愿意提供某些API接口，那么链路就可以实现串联并且不再依赖设备ID实现了，的原因。）<br>
<br>
<strong><font color="#de5650">二、SkAdNetwork下的归因链路</font></strong><br>
<br>
<strong>SKAN的解读</strong><br>
<br>
通过官方给出的SKAdNetwork的文件和SKAN交互流程图，我们来看看为什么说SKAN将广告归因路径串联了起来——<br>
<br>
Apple Developer Documentation<br>
<br>
<div align="center">
<img aid="1029633" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120039dbh11sg0qbhsjrox.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120039dbh11sg0qbhsjrox.jpg" width="600" id="aimg_1029633" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120039dbh11sg0qbhsjrox.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>交互流程图解读</strong><br>
<br>
1.已注册的广告平台为需要投放的广告主应用进行签名，提供给媒体（也叫源应用）。<br>
<br>
2.媒体显示已经带有签名的广告，用户点击广告后，媒体会调起AppStore，并将广告应用的签名和验证信息传给AppStore。（这样目的，Apple才能判断调用Apple Store的签名是哪个，并将签名带到下一流程中去）<br>
<br>
3.当广告主应用安装并被打开时，应用会调用系统函数（registerAppForAdNetworkAttribution()），发起应用安装验证通知。<br>
<br>
Apple会等广告主App24小时，若用户24小时内没有在广告主App上发生后续行为，（即广告主App没有进入下一流程），Apple会在之后的24小时之中任一随机时间点向广告平台发起回调。<br>
<br>
4.若用户在AppB上产生转化，AppB就要调用更新转化值方法，用updateConversionValue(_<img src="https://www.gameres.com/static/image/smiley/default/smile.gif" smilieid="1" border="0" alt referrerpolicy="no-referrer">函数。使用此方法，Apple回调的时间就会推迟24小时。<br>
<br>
【此方法可多次调用，但是距离上一次调用安装（registerAppForAdNetworkAttribution()）或转化（updateConversionValue(_:)）不能超过24小时，因为超过24小时的话Apple就会发起回调了。<br>
<br>
【多次调用时，后一次的Value要比前一次的大，否则相当于不生效。因此最多会导致64次调用后才会回传给广告平台信息。】<br>
<br>
（理解为：Apple有且仅有一次机会发起回调，默认24小时内无变动即回调）<br>
<br>
5.Apple把安装和转化信息发送给广告平台注册时填写的URL。<br>
<br>
6.广告平台验签收到的安装和转化信息。(ios15后，apple的Install postback一份发给ADN 一份发给广告主，前提是广告主进行了NSAdvertisingAttributionReportEndpoint 配置）<br>
<br>
7.list<br>
<br>
<div align="center">
<img aid="1029634" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120040yw4g4gxx4rcpgx8p.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120040yw4g4gxx4rcpgx8p.jpg" width="600" id="aimg_1029634" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120040yw4g4gxx4rcpgx8p.jpg" referrerpolicy="no-referrer">
</div><br>
关于SKAN交互流程图解读中的【注册广告平台】【签名是什么怎么生成】【源应用】【在SKAN框架下广告参与主体如何配置】【转化值6-bit 二进制】等技术层面问题，请参考树伦写的‣<br>
<br>
<strong>参与主体</strong><br>
<br>
在前面分析IDFA时代下的归因链路，我们从【publisher】【广告平台】【三方应用】及【广告主应用】这些主体分析了每个主体的职责，都承担了什么角色。这里我们继续看，这些主体在SKAN下又承担着什么角色以及有那些职责。<br>
<br>
<strong>广告平台</strong><br>
<br>
角色：投放广告的主体<br>
<br>
职责：<br>
<br>
1.要在Apple注册一个NetworkID：在这套机制下代表你是你自己。并把这个ID要提供给源应用，即publisher<br>
<br>
2.按照Apple算法，生成公私钥：私钥用于对签名参数进行加密；公钥用于解密，即当广告平台收到Apple回传的安装验证和转化信息时，广告平台要用公钥进行解密<br>
<br>
【我=广告平台用钥匙打开属于我自己门，门里是回传的信息】<br>
<br>
3.为广告设置签名参数：是一个带有签名参数的StoreKit，生成签名有三步骤：参数-字符串-加密签名<br>
<br>
3.把带有加密签名参数和ad network identifier（1中的ID）的广告给到publisher    （签名如何生成就请参考developer.apple）<br>
<br>
4.注册Postback URL：用来接受来自Apple回传的安装和转化信息<br>
<br>
<strong>Publisher</strong><br>
<br>
角色：展示广告的载体<br>
<br>
职责：<br>
<br>
1.接受广告平台注册后的NetworkID，并放入自己的info.plist<br>
<br>
2.展示已有签名的广告：To display a StoreKit-rendered ad and initiate a validation, an app must call ——[loadProduct(withParameters:completionBlock:)](<https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/1620632-loadproduct>)—— with a signature key that the ad network generates, ——[SKStoreProductParameterAdNetworkAttributionSignature](<https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkattributionsignature>)——.<br>
<br>
<strong>广告主应用</strong><br>
<br>
角色：投放活动最终目的实现的载体<br>
<br>
职责：<br>
<br>
1.在应用被安装激活时，调用系统的API registerAppForAdNetworkAttribution()<br>
<br>
2.在应用内用户产生后续行为时，调用更新转化值方法——updateConversionValue(_:)——<br>
<br>
<strong>Apple</strong><br>
<br>
角色：用户隐私保护者，“隐藏第三方”<br>
<br>
职责：<br>
<br>
1.Apple把安装和转化信息发送给广告平台注册时填写的URL，副本给广告主（option）。<br>
<br>
从参与主体来看，我们可以轻而易举发现，第三方并不在SKAN链路上产生任何行为，这也是为什么称Apple是“隐藏第三方”的原因。也可以暗暗推断出，苹果企图在保护用户隐私的旗号下，渐渐让自己成为ios广告行业的标准与裁判，实现在广告行业分一杯羹。<br>
<br>
<strong>归因环节</strong><br>
<br>
在有IDFA时代，归因平台将IDFA作为一个判定依据，来调用这个IDFA下这个设备的“互动行为数据”，从而实现Matching。但在SKAN框架下，苹果并没有担起上述这样的角色，而是将链路部分信息回传给广告平台和广告主。下面我们细数一下，苹果到底回传了哪些信息。<br>
<br>
<strong>接收带有归因的获胜回传</strong><br>
<br>
```json<br>
&#123; <br>
  "version": "3.0", <br>
  "ad-network-id": "example123.skadnetwork", <br>
  "campaign-id": 42, <br>
  "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e28", <br>
  "app-id": 525463029, <br>
  "attribution-signature": "MEYCIQD5eq3AUlamORiGovqFiHWI4RZT/PrM3VEiXUrsC+M51wIhAPMANZA9c07raZJ64gVaXhB9+9yZj/X6DcNxONdccQij", <br>
  "redownload": true, <br>
  "source-app-id": 1234567891, <br>
  "fidelity-type": 1, <br>
  "conversion-value": 20,<br>
  "did-win": true<br>
&#125;<br>
```<br>
<br>
Source：https://developer.apple.com/documentation/storekit/skadnetwork/verifying_an_install-validation_postback<br>
<br>
<ul><li>version：SKAN版本号（2.0及更高）</li><li>ad-network-id：ADN注册后获得的ID</li><li>campaign-id：广告活动id</li><li>transaction-id：此验证的唯一值;用于删除重复的安装验证消息。</li><li>app-id：广告主应用的App store ID</li><li>attribution-signature：用于需验证的苹果归因签名</li><li>redownload：true：用户是重新下载和重新安装（老客）</li><li>source-app-id：源应用的ID；源应用ID只有符合Apple的隐私门槛（Apple’s privacy threshold），才会出现在回传信息中。（隐含寓意是，广告主的app要是没有符合ATT，那么广告平台收到的回传信息不能确认是哪个广告主应用的，不过通过campaign是不是还是能知道是哪个广告主的呢？</li><li>fidelity-type：0代表View-through ad，1代表StoreKit-rendered ad。<br>
</li></ul><br>
苹果SKAN2.2版本后支持两种广告形式，一种是浏览型广告，开发者可自定义广告呈现的形式，例如banner、视频、音频、弹窗等，例如，当用户在App中点击banner广告时（banner没有接入StoreKit），用户可自行去App Store进行搜索下载，而这种行为也可以被归因到该渠道。<br>
<br>
一种是StoreKit-rendered ad（渲染型广告），接了StoreKit的广告可在直接调用AppStore里广告主应用的下载落地页，引导用户直接下载并归因到该渠道。<br>
<br>
<ul><li><strong>conversion-value：</strong>转化值，已安装的应用程序通过调用提供的无符号 6 位值；仅当安装的应用程序提供它，并且提供的参数满足 Apple 的隐私阈值时，才会出现在postback中。</li><li><strong>did-win：</strong>true是指表示该adn赢得归因，false表示未赢得。但是如果是false，则回传的样式应该是这个样子<br>
</li></ul><br>
<strong>接收没有获胜的回传</strong><br>
<br>
```json<br>
&#123; <br>
  "version": "3.0", <br>
  "ad-network-id": "example123.skadnetwork", <br>
  "campaign-id": 42, <br>
  "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e28", <br>
  "app-id": 525463029, <br>
  "attribution-signature": "MEYCIQD5eq3AUlamORiGovqFiHWI4RZT/PrM3VEiXUrsC+M51wIhAPMANZA9c07raZJ64gVaXhB9+9yZj/X6DcNxONdccQij", <br>
  "redownload": true, <br>
  "source-app-id": 1234567891, <br>
  "fidelity-type": 1, <br>
  "conversion-value": 20,<br>
  "did-win": true<br>
&#125;<br>
```<br>
<br>
<br>
按照苹果的归因规则（窗口期、优先级等），判定某一adn没有获胜也将收到回传，并且在没有获胜的回传信息中，source-app-id和conversion-value是没有显现的。个人理解：因为转化值是广告平台赋予用户产生行为的代表，如果未获胜的回传中并没回传转化值，这是不是也意味着，即便是最后归因不归于该渠道下，但该渠道下用户产生到哪一行为也是adn无法知晓的，进而影响到了adn做广告投放效果的评估。<br>
<br>
<strong><font color="#de5650">三、区别与联系</font></strong><br>
<br>
下面我们来仔细对比一下，在前面上述两个归因交互路径中IDFA时代和SKAN时代都怎么样的区别和联系，可以更清晰明了来理解串联。<br>
<br>
<strong>显性区别</strong><br>
<br>
1.参与主体变动：由原来的链路中拥有第三方 VS  现在Apple“充当”第三方<br>
<br>
2.广告平台前置化：广告平台自有平台创建投放活动 VS 广告平台需在Apple提供的平台注册ID 创建广告活动<br>
<br>
3.应用商店作用变更：以往itunes并没有记录这个用户是来自哪个adn clickid publisherid VS 媒体在调用AppStore时，即将广告应用的签名和验证信息透传给AppStore<br>
<br>
<strong>隐性区别</strong><br>
<br>
1.重定向取消：以往是用户点击广告链接先跳转一次广告平台http：//adnetwork.com/再跳到到第三方http：//app.appsflyer.com，再跳转至商店 VS  都聚合归因安装统计将来自一个渠道，Apple（skadnetworrk API）<br>
<br>
<strong>2.归因行为：</strong> 以往是应用app首次激活后获取IDFA，调用该IDFA之前有过的记录做匹配，VS 苹果回传的信息带有相关信息<br>
<br>
<strong>3.归因管理：</strong>以往是三方 VS 现在由广告平台（副本广告主也有）（这就蕴藏着一定风险）<br>
<br>
<strong>4.精准去重：</strong>以往利用IDFA归因可以实现精准去重 VS SKAN回传的是群组转化数据且具有延时性<br>
<br>
<strong>5.归因信息：</strong>apple回传信息里并没有click time/install time/event time等<br>
<br>
<strong><font color="#de5650">四、SKAN带来的一些挑战</font></strong><br>
<br>
SKAN的提出的确是存在利好的一面的，特别围绕我在前面强调的用户隐私和串联路径来说。但实际从SKAN更新版本这件事来看，它也是一个不断发展的事物，也就是说，现有SKAN也存在着明显的不足。<br>
<br>
<strong>1.数据颗粒度：</strong>只到广告系列层级，且无法设置超过 100 个广告系列。且SKAdNetwork 系统分享的数据都采取聚合形式，不提供用户层级上的精细数据。<br>
<br>
<strong>2.数据割裂：</strong>广告主在多家广告平台上投放广告，但转化数据都是单独回传给各家广告平台，广告主要想评估全平台的数据，还得单独跟各个不同的广告平台进行数据的对接。（如果广告主通过大量渠道投放广告，那么与每个广告平台对接所需的研发资源、对接成本和技术支持工作量都将是巨大的）<br>
<br>
<strong>3.回传延迟：</strong>24小时及以后才有回传。转化回传延时影响广告主对于投放素材优化的时效性，同时影响广告模型实时调节广告主成本，引起成本波动。<br>
<br>
<strong>4.深度链接：</strong>SKAdNetwork 没有提供延迟广告的深度链接的框架。这样会在很大程度上牺牲用户体验，而且转化率可能受到严重影响。<br>
<br>
<strong>5.再营销：</strong>只有redownload记录，但仍无法获取用户层级数据，RT活动变得艰难。<br>
<br>
<strong>6.web-app归因：</strong>这是SKAN框架下未解决的<br>
<br>
<strong>7.事件识别码只能向上叠进：</strong>例如，用户在游戏内达成了等级 1，应用为 "等级 1" 创建的事件识别码为 000001；然后用户购买了游戏内货币，这一事件的识别码为 000011。如果用户随后达成了 "等级 2"，比特值不会变为 000010，因为变化是单向的。要避免这个问题，开发者需要为排列组合中所有的可能性分配不同的比特值，而不是为每种事件分配比特值。SKAdNetwork 跟踪的数据无法与 MMP SDK 跟踪的应用内事件精细数据关联起来。（source：adjust）<br>
<br>
<strong><font color="#de5650">五、解决方案</font></strong><br>
<br>
俗话说得好，“上有政策下有对策”，既然苹果要迎合用户市场所趋而制定新规改变了归因链路，那么原本产业链中的三方和广告平台也不能背道而驰，毕竟用户才是金主爸爸 。前文也提到因不完善的SKAN，产业链部分主体的利益也受到了不同程度的影响，那么我们来看看在他们是如何迎接SKAN的挑战的。<br>
<br>
<strong>三方（以AppsFlyer为例）</strong><br>
<br>
前面也有提及到，即便是SKAN实现了归因路径的串联，但是Apple最终回传的信息是给了广告平台（副本给广告主），在这一维度可以看出数据还是割裂的。这一维度就好比，小明和小红离婚，都有证据证明孩子应该交给他们自己单独抚养，但每个人拥有的证据都不足以让对方信服，亦或让亲戚信服，那好，就把两方拥有的证据都交给法院，把孩子判给谁这个问题交给公平、公正 的第三方，第三方提供人力精力全方位组合分析证据，这个孩子到底该给谁。三方也承担着一样的角色，将广告平台和广告主/广告代理收到的回传进行汇总，并提供数据模型，提供服务，保证数据更加精准与公平公正。（只要SKAN一天没最终完善，产业链就还是需要三方一天！）一起来看看，AppsFlyer推出了哪些功能来应对SKAN所带来的挑战吧！<br>
<br>
<font color="#de5650">1.访问数据回传</font><br>
<br>
代表广告主，AppsFlyer终端收集每个广告平台收到的回传信息，并且确保Apple所有回传数据不可在途中更改。AppsFlyer针对SKAN为广告平台提供对接指南，以实现广告平台回传并收到AppsFlyer基于数据模型处理后的归因结果，进而完成活动优化。<br>
<br>
<div align="center">
<img aid="1029635" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120041sz8bembvlj6vyslb.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120041sz8bembvlj6vyslb.jpg" width="600" id="aimg_1029635" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120041sz8bembvlj6vyslb.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
从官方给的释义中，我们可以了解到，AF为ADN提供两种发送方式：<br>
<br>
<ul><li>间接方式：Enrich/补充数据维度再回传<br>
</li></ul><br>
广告平台将收到的apple的回传数据，进行字符串补充丰富，再回传给AF。补充信息如下<br>
<br>
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks' \<br>
 --header 'Content-type: application/json' \<br>
  --data-raw '&#123;<br>
      "version":"2.0",<br>
      "app-id": 888707086,<br>
      "ip": "192.0.2.0",<br>
      "ad-network-campaign-name": "skadnetwork_abc_campaign",<br>
      "source-app-id": 888707074,<br>
      "ad-network-id": "abcabcabc.skadnetwork",<br>
      "transaction-id": "68eb3d91-15f5-44ee-9267-25c7655c20b6",<br>
      "redownload": false,<br>
      "attribution-signature": "MDYCGQCsQ4y8d4BlYU9b8Qb9BPWPi+ixk/OiRysCGQDZZ8fpJnuqs9my8iSQVbJO/oU1AXUROYU=",<br>
      "timestamp": "1596525944",<br>
      "ad-network-campaign-id": "222222",<br>
      "conversion-value": 63,<br>
      "campaign-id": 99<br>
  &#125;'<br>
<br>
<br>
<ul><li>ad-network-campaign-id：为了确保广告主，广告平台和AppsFlyer之间语言一致，广告平台务必提供广告系列 ID</li><li>ad-network-campaign-name：这一名称将显示在数据面板和数据报告中与广告系列匹配的广告系列名称。</li><li>ad-network-adset-id：广告组ID</li><li>ad-network-adset-name：广告组名称</li><li>ad-network-ad-name：广告创意名称</li><li>ad-network-ad-id：广告创意ID</li><li>ip：苹果发送SKAdNetwork给广告平台时的客户端IP。支持iPv4 及 IPv6 地址，举例: "ip":"198.51.100.1"</li><li>时间戳：广告平台收到 SKAdNetwork 回传的时间精确到秒的10位UNIX 时间戳。[可选] 精确到毫秒的13位UNIX时间戳。示例：August 4, 2020, 07:25 UTC translates to "timestamp": "1596525944"<br>
</li></ul><br>
More：广告系列信息等参数有助于AF结合其与其他广告系列的数据来丰富SKAN数据，便于优化活动。<br>
<br>
<ul><li>直接方式：Redirect/重定向<br>
</li></ul><br>
<div align="center">
<img aid="1029636" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120042y424urp9xnibr4uc.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120042y424urp9xnibr4uc.jpg" width="600" id="aimg_1029636" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120042y424urp9xnibr4uc.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
重定向的方法是指广告平台使用HTTP307来实现iOS直接将postback回调给AF，（以前是ios只给adn），这样做一是利于避免数据造恶意修改（AF成直接的一手资料获取者），二是省去广告平台进行数据补充再转发给AF。<br>
<br>
<font color="#de5650">2.数据模型互补</font><br>
<br>
AF推出汇总归因解决方案，（概率性数据模型到底是怎么一回事这挺难的啊，这也是最核心的地方，AF的商业机密吧）但是通过官方宣传的来看：将 SKAdNetwork 信息与广告曝光、点击、成本、自然流量等数据进行匹配，形成完整 ROI；也就是说这个模型直接优势是在于：能实现更多用户后续行为的归因，广告平台收到AF回传信息也更多<br>
<br>
<font color="#de5650">3.一站式 SDK</font><br>
<br>
<div align="center">
<img aid="1029638" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120043acgngicgr4g4x8nb.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120043acgngicgr4g4x8nb.jpg" width="600" id="aimg_1029638" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120043acgngicgr4g4x8nb.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
和IDFA时代一样，广告主应用可以继续保持集成AF的SDK，用于收集广告主App上产生的行为数据。<br>
<br>
还有一个特别的优势：在SKAN框架下，广告主的转化值设定，是需要内置在应用代码中的，这也就意味着，每更新一次值，广告主就要更新一次App版本。而有了AFSDK，广告主可在AF提供的后台进行设置修改，SDK和整个系统也就会自动更新，修改发生在Sever端，广告主不需要再更新版本。相当于AFSDK在窗口期更新转化值。您可在SKAN Conversion Studio查阅AF针对转化值的相关建议<br>
<br>
隐藏信息：AFSDK可大量汇总用户在App产生的后续行为，虽到不了精准用户层级的信息，但是可以得到用户们在该广告应用上的共性，这样也有利于AF做数据模型，并在后续中推出“Predict“功能！<br>
<br>
<font color="#de5650">4.SK360</font><br>
<br>
SK360是AF完善之前所有解决方案基础上，提出来的最新的一站式解决方案，提供【优化】（转化值配置）【分析】（数据模型）【预测】（Predict）【保护】【连接】（合作伙伴对接）功能套件。其中，最值得关注的就是【预测】。<br>
<br>
<strong>PredictSK</strong><br>
<br>
SKAN框架下，apple因添置计时器导致回传的数据是24+后，且有且仅有一次数据回传，对于营销人员优化活动产生了一定影响。对此，AF提出预测分析工具PredictSK。<br>
<br>
AF官方声明：该PredictSK有利于广告主可基于早期的互动行为数据，预测长期广告效果并及时做优化决策；还可通过衡量无限量的应用内事件，预测每个用户的 LTV。广告主可将六比特的转化值用于 LTV 预测，无需将有限的转化值浪费在与 ROI 等关键指标无关的事件上。<br>
<br>
PredictSK 不是凭空想象，而是将大数据、机器学习，结合 AppsFlyer 对每个 App 的特定使用规律的深度分析形成的模型。基于各个 App 深度洞察的数据模型能够带来极为精准的预测结果。该模型不仅能够对每个应用形成精确的预测分析，还将数据分开储存，每个模型都独立存在且仅基于该特定 App 的数据。<br>
<br>
<strong>广告平台（以FB为例）</strong><br>
<br>
广告平台因回传信息变少导致营销活动受到一定冲击，Facebook虽然已经看似接受了Apple SkAdNetwok，但仍在开发各种产品和方法来帮助达成最佳化效能。<br>
<br>
<strong>网页转化的广告主</strong><br>
<br>
ios14为网站事件提供的PCM（Private Click Measurement）是不支持网站到应用的转化衡量也不支持跨网域成效衡量。对此，FB引入AEM协议（Aggregate Event Measurement）支持应用到网站的归因分析，灵活支持其他平台的隐私主张。但跨网域衡量成效的问题仍然待解决。目前从FB的产品来看，每个网域广告主最多设置8个用于优化和报告的事件（有优先顺序），若用户选择静止追踪，FB只能按照优先级传回单一事件。广告主想要更改事件时，最长推迟72小时才生效。<br>
<br>
<div align="center">
<img aid="1029637" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120042pywvy5g2lwvw2yad.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120042pywvy5g2lwvw2yad.jpg" width="600" id="aimg_1029637" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120042pywvy5g2lwvw2yad.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
参考：判断网域可配置的事件<br>
<br>
<strong>应用转化的广告主</strong><br>
<br>
Facebook将采用Apple的SKAdNetwork API在ios设备上投放应用广告，所有的应用实践数据将汇总展示并延迟，虽然接受着Apple的新规，但FB也在推出新的措施来适应SKAN，为广告主提供服务。<br>
<br>
<font color="#de5650">1.平台上线【归因设置】和【成效】</font><br>
<br>
之前广告主需在【Ad Account Setup】中针对【Ad Account Settings】中对事件窗口进行调整。<br>
<br>
<div align="center">
<img aid="1029639" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120044y4l5qlsb2r3p1q5b.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120044y4l5qlsb2r3p1q5b.jpg" width="600" id="aimg_1029639" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120044y4l5qlsb2r3p1q5b.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
1月19日之后，推出新的归因设置选项，在【广告系列】下的【广告组】设置中可以找到【隐藏选项】从热实现【Attribution Setting】，且可供选择的时间窗口和逻辑关系有四种。（以前最短1天最长28天，现在只有1和7）<br>
<br>
关于归因设定请参考官方文件：https://www.facebook.com/business/help/460276478298895?id=561906377587030<br>
<br>
<div align="center">
<img aid="1029640" zoomfile="https://di.gameres.com/attachment/forum/202201/27/120045cc5nhhbnn23wppe3.jpg" data-original="https://di.gameres.com/attachment/forum/202201/27/120045cc5nhhbnn23wppe3.jpg" width="512" id="aimg_1029640" inpost="1" src="https://di.gameres.com/attachment/forum/202201/27/120045cc5nhhbnn23wppe3.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<font color="#de5650">2.账户和活动管理</font><br>
<br>
每款应用只能关联到一个广告账户，并且最多只能创建9个广告系列，每个广告系列有5个广告组，这些广告组还必须使用相同优化类型（MAI（安装）AEO（事件）和VO（价值优化））。以往FB要求使用专门的广告账号来记录ios14的安装应用程序广告，现调整为支持广告商从现有广告账号为iOS14用户开展应用程序安装营销活动。<br>
<br>
<font color="#de5650">3.更新插件版本</font><br>
<br>
FB要求使用Facebook SDK、应用内事件、MMPSDK的不同广告主使用对应要求的更新版，但这些广告主需要准备使用“允许广告主追踪”标记，并将这个参数一并回传给FB。如果广告主只是使用应用事件API，请准备按照事件管理工具中的说明来集成SKAN API。详情请参考官方文档：https://www.facebook.com/business/help/2750680505215705?id=428636648170202<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
至此，我们就已经通过SKAN背景了解到了新老归因的区别与联系，从而理解到了SKAdNetwork API实现了归因路径的串联。也同时看到SKAN的出现所带来的挑战，而代表性归因平台和广告平台目前是如何应对SKAN所带来的挑战。由于SKAN是一个处于发展中的事物，无论是他到底怎么样发展，最终成为什么样，移动互联网广告的参与主体都将积极响应，结合大数据和机器学习算法，营造良性发展生态圈。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://opteam-meta-universe.notion.site/SkAdNetwork-80b41df524ec4ed8bc94c2ed5c00e347</font></font>  
</div>
            