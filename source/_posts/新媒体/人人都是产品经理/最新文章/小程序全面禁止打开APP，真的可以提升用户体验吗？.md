
---
title: '小程序全面禁止打开APP，真的可以提升用户体验吗？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/EmszyNpDrRE5XSQt1RER.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 27 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/EmszyNpDrRE5XSQt1RER.jpg'
---

<div>   
<blockquote><p>编辑导语：毫无疑问，小程序是微信生态极其重要的组成部分，也是继朋友圈之后推出的又一款跨时代产品。小程序已经上线4年多的时间，数量已超380万，日活跃用户超4亿，月活跃用户高达8.3亿。如今，微信不再提供小程序打开App技术服务，这样的方式真的可以提升用户体验吗？</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4610844" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/EmszyNpDrRE5XSQt1RER.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>5月14号，微信发布公告，宣布从5月20日开始，<strong>全面关闭“微信小程序打开app技术服务”</strong>。微信的官方说法是收到了大量用户投诉，为了“提升用户体验”，他们关闭了这个服务，这么做是为民请愿。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/4ncV1dOLJMoUQlIEZUTb.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="702" height="173" referrerpolicy="no-referrer"></p>
<p>且不论微信此举是否真的代表用户的诉求，对于小程序开发者来说，却是的的确确捅了马蜂窝。从微信社区的留言来看，似乎开发者们对微信这次的改动都持否定态度。我翻了几页，基本都是吐槽微信又在“瞎改”。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/RmKJpSrDLctwnjbU1p3d.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="701" height="393" referrerpolicy="no-referrer"></p>
<p>微信小程序在2017年初上线时，并没有提供“小程序打开app”服务。在小程序运营一年后，18年的v1.9.5版本中，微信才开放这个服务。三年之后，微信又关闭了这个服务。</p>
<p>小程序和app之间到底是什么关系？“小程序打开app”到底意味着什么？微信又为什么在这个问题上反复横跳呢？</p>
<h2 id="toc-1">一、微信小程序与APP的关系</h2>
<p><strong>什么是微信小程序？</strong></p>
<p>——按照张小龙的说法，<strong>微信小程序是一种不需要下载安装即可使用的应用。</strong></p>
<p>张小龙经历了<strong>PC、互联网</strong>和<strong>移动互联网</strong>时代。PC时代，那个时候电脑还不能联网，用户需要通过软盘或者光盘安装程序来访问服务。当然这时的程序，不能联网，也不能跟外界交互，又称之为单机程序。</p>
<p>到了互联网时代，服务依然被聚合在程序中，只不过此时的程序具备了访问网络的能力。另外随着www.web协议的出现，涌现了一大批网站。网站可以被任何连接网络的用户来访问，所以用户也可以通过访问网站来享受服务。<strong>商家既可以通过写一个程序来提供服务，也可以通过搭建一个网站来提供服务。</strong></p>
<p>而进入了移动互联网时代，用户访问网络服务的终端由电脑变成了手机。服务被聚合在app中，用户通过安装使用app来享受商家提供的服务。可是通过浏览器访问一个网站很简单，下载安装app却很费时间。</p>
<p><strong>我们可以一天访问20个网站，但是我们不会一天打开20个app。</strong>我们很懒，我们更倾向于每天只打开几个app，不喜欢下载安装很多app。这也是那些头部app变得越来越臃肿的原因，因为它把很多之前其他的app的活也给干了。</p>
<p>张小龙认为，移动互联网之后，<strong>未来的服务形态应该是所见即所得，随时可以访问的。</strong>比如，你去一个公园，公园门口有一个购票的应用程序，用户是可以直接启动访问的，不需要下载安装；你在公交车站等车，可以直接打开查询公交车实时位置的应用程序。</p>
<p>基于“无需安装，触手可及”的理念，微信推出了小程序。当然这句话深究起来是有问题的，用户其实是需要下载安装小程序的。只不过小程序的包体太小，一般不超过2M，它的下载安装过程对于用户来说近乎于无感知，所以说不需要下载安装也没什么问题。</p>
<p><strong>微信小程序代表了张小龙对于移动互联网时代之后，服务形态的一种思考。微信小程序的定位是“比网站体验更好，比app更触手可得”。</strong></p>
<p><strong>微信小程序作为一种比app更加灵活的组织形态，可以替代一些低频、核心流程简单的app。</strong>例如，我可能一年都不会来几次这个公园，为了购票花个几十M流量下载个app成本太高；再比如骑共享单车，我的操作就是扫码开车，这么简单的操作完全可以在微信小程序里完成。</p>
<h2 id="toc-2">二、“保守”的微信</h2>
<p>微信小程序可以看成是对于现在以app为主的服务形态的一种完善。那么微信小程序和app之间必然有很多交互，那么为什么微信小程序不在一上线之时就提供微信小程序打开app/app打开小程序的服务呢？</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/WeSnM47kkOsqrGlKh8Sv.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="604" height="535" referrerpolicy="no-referrer"></p>
<p>整理一下微信小程序的入口，会发现小程序的入口可以分为三类：<strong>线上、线下</strong>和<strong>服务</strong>。</p>
<ol>
<li>线上的发现入口：主页下拉、发现页、搜索结果、会话小程序卡片等；</li>
<li>线下的连接入口：线下扫小程序码访问；</li>
<li>服务与服务之间的入口：微信公众号与小程序互相访问、小程序与小程序互相访问；小程序和app互相访问；</li>
</ol>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/CT2BwaBgdRkkjTZ7yaaI.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="606" height="341" referrerpolicy="no-referrer"></p>
<p><strong>其中app与小程序之间的入口是最晚才开始接入的：</strong></p>
<ul>
<li>2017年3月，微信公众号支持跳转小程序；</li>
<li>2017年6月，小程序之间可以互相跳转；</li>
<li>2017年9月，小程序内支付完成可关注公众号；</li>
<li>2018年1月，小程序支持打开app；</li>
<li>2018年4月，app支持打开小程序；</li>
</ul>
<p><strong>微信小程序与app支持互相跳转可以带来无尽的可能性。</strong>微信小程序可以作为app的一个简易版应用，一些比较简单的功能，用户可以在微信小程序里直接完成。一些进阶的功能，用户直接从小程序里打开app来完成。</p>
<p>比如，你做一个旅行攻略的app，用户可能需要订机票、酒店、打车、门票、演出预约等服务，但是一款app可能无法覆盖这么多的服务。</p>
<p>那么可以让用户直接从app里直接打开特定的微信小程序来完成操作。这个小程序不一定非要你来开发，可以接入其他商家的小程序。你不需要把全部的活都给干了，每个商家只做自己最擅长的那一部分。</p>
<p><strong>可以预见的是，微信一旦放开小程序和app之间的互相跳转，必然会吸引更多的开发者入驻，小程序的流量将迎来暴涨。</strong>但是微信却表现的很克制，甚至是保守。</p>
<p>微信的“保守”同样体现在后面的视频号中。微信视频号在引入社交分发之前，依赖于算法分发。<strong>因为早期用户很少，内容质量较低；内容质量低，那么播放量就低；播放量低，内容生产者没有动力生产内容。</strong>这样形成了一个恶性循环，算法只能分发优质内容，无法创造优质内容。</p>
<p>这时就有一种声音——<strong>要不给内容生产者以流量或者现金扶持，吸引他们在视频号创造内容？</strong>但是还是被拒绝，视频号没有买内容，也没有给内容生产者以流量扶持。</p>
<p>到底谁给了微信这么高冷傲娇的底气呢？</p>
<p>微信是中国互联网的第一流量池，微信推出了什么新功能。很容易就会被炒成是下一个风口，各家想尽一切方法来透支他的流量。繁华过后，一地鸡毛。所以微信在上线新产品的时候，都奉行“先紧后松”的策略。</p>
<p>让这些新产品自己生长，当产品达到了一定的量级和活跃度，用户留存率开始上扬，流量循环可以正常的运转起来，代表产品真的活了起来之后，微信才会考虑完善基础功能的搭建。如果产品没有证明自己可以成为一个自行运转起来的生态，直接引入流量并不是一件好事。</p>
<p><strong>我们可以设想，如果微信提供了“小程序打开app”的服务，那么必然会吸引更多开发者入驻。他们会想各种方法来给app引流。</strong></p>
<p>比如，我通过小程序给用户发一张奖券，但是这个奖券，你必须在app里才能使用；你在小程序可以看到新闻，但是对查看评论的数量进行了限制，如果要查看全部评论，需要来app；你在小程序里可以看视频，但是对视频的清晰度进行限制。如果想要看到更清晰的视频，你得来app。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/NNUv1POdz54fNhLqCYv9.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="601" height="353" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">经典套路：在小程序里发一张在app里才能使用的券</p>
<p><strong>总之，商家会通过限制小程序里的功能，把小程序的流量往app引导。这一点微信当然不想看到，微信希望小程序可以形成一个闭环，在小程序里就可以解决用户所有的问题。而不是把小程序作为app的引流工具，或者更直白点说是app的启动器。</strong></p>
<p>那么微信是做了哪些事情来避免商家过度滥用“打开app”这个能力呢？</p>
<h2 id="toc-3">三、如何避免商家过度滥用</h2>
<p>首先微信出台了《微信小程序运营规范》，里面对于诱导用户打开/下载app进行了严格的限制。</p>
<p>为保障用户体验和用户权益，小程序提供的服务中，不得存在影响功能服务或业务流程完整性、顺畅性的诱导用户跳转/下载APP的行为，如利益诱导跳转/下载APP、强制用户跳转/下载APP、通过利用客服消息接口能力来达到诱导跳转/下载APP目的的行为；</p>
<p>以及在小程序已提供相关功能或服务时，仍诱导或强制用户跳转/下载APP等行为，包括但不限于以下类型：微信小程序运营规范 5.20 诱导下载行为。</p>
<p>除了运营层面，微信还在技术层面对“小程序打开app”进行了场景上的限制。在v1.9.5版本中，微信小程序的组件 button open-type 新增 launchApp 属性，实现微信小程序唤起app。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/3Tpbv43mzPhwNED3tTBk.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" referrerpolicy="no-referrer"></p>
<p>但是这个launchapp的方法可以调用的前提是启动小程序的场景值是否是1036或者1069。</p>
<ul>
<li><strong>1036:APP分享消息；</strong></li>
<li><strong>1069:APP打开小程序；</strong></li>
</ul>
<p>微信的规则是，当小程序从 APP 分享消息卡片的场景打开或从 APP 打开的场景打开时，小程序会获得打开 APP 的能力，此时用户点击按钮可以打开分享该小程序卡片/拉起该小程序的 APP。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/WFQhkIoKF5sTVN1wArWU.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="600" height="654" referrerpolicy="no-referrer"></p>
<p>以具体场景举例就是说：</p>
<ol>
<li>你通过app唤起微信，并且打开某个微信小程序，那么你可以从这个小程序回到app；</li>
<li>你在b站app里看到一个视频，觉得很有趣，你分享给微信好友。微信好友在微信中，是通过b站微信小程序打开你分享的视频。这时你的好友可以通过小程序直接打开b站app。</li>
</ol>
<p><strong>这两个场景中，用户能来到小程序，源头都是app。流量来自app，再让流量回到app，倒也合情合理。</strong><strong>除这两个以外，其余任何场景都不能从小程序里直接唤起app（ps.微信亲儿子们除外）。</strong></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/A7D0zKewu2JBl6DZDa3f.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="305" height="543" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">好友从app分享给我</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/VEE5mdaYHJG27uNaqW5g.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="300" height="533" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">通过搜索结果启动小程序</p>
<p>比如，你今天看了文章才知道b站有微信小程序，你很想去体验一波。搜索了一下“b站”关键词，找到b站小程序。这种情况，你启动b站小程序，观看视频，是不能够唤起app的。</p>
<p><strong>总之微信小程序允许从app流到小程序的流量回流到app，不允许小程序自己的流量主动流向app。</strong></p>
<h2 id="toc-4">四、商家如何应对？</h2>
<p><strong>那么微信禁止小程序唤起app之后，那么商家是如何应对的呢？</strong></p>
<h3>1. 商家妥协，进行整改</h3>
<p>让用户在微信小程序内形成闭环。例如，我在微信小程序里也能看到高清的视频，全部的评论。这是微信最希望看到的局面，这么做也的确可以提升用户体验。</p>
<h3>2. 商家选择逃离微信小程序</h3>
<p>需要注意的是，微信封禁的是从小程序直接打开app的能力。<strong>微信并没有完全封禁从微信其他地方打开app的能力</strong>，例如微信的开放标签功能，就可以支持微信里的h5直接唤起app。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/5QRHLyxoqnGPdL7tCvCI.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="300" height="534" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">曾经的小程序</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/VsvnGKXkLDwNTQA43F6W.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="301" height="536" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">现在的h5</p>
<p>或许我们注意到，之前我们分享B站视频和微博给微信好友，好友打开的是B站和微博的小程序，而现在改成了H5。</p>
<p>这是因为之前小程序具备直接唤起app的能力，所以你打开的是小程序；现在小程序不能直接打开app了，但是h5可以，所以你打开的就是h5。即使小程序的体验比h5更好，但用户体验这种无法量化的东西是不会出现在我的运营数据报表中的，增加app的uv和用户平均访问时长，更符合我的利益。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/7zFEQ2yizHNIFdPldWm1.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="304" height="541" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">微信里的h5依然具备直接打开app的能力</p>
<h3>3. 微信客服等其他方式</h3>
<p>正是因为微信浏览器依然具备唤起app的能力，所以很多商家会理所应当的思考如何从微信小程序跳转到微信浏览器里。</p>
<p>比较常见的方法就是通过小程序打开客服，当用户进入客服，其实用户已经离开了小程序。一旦用户离开了小程序，那就广阔天地，大有作为了。客服回复app下载引导页的地址。如果你没有安装app，那么就可以通过下载引导页引导安装app；如果你已经安装app，就可以直接唤起app。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/fSDFYiSulYiKsUMfKsH1.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="502" height="428" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">被明令禁止的客服引导用户下载</p>
<p><strong>当然通过客服引导用户跳转/下载app的方式也是被微信明令禁止，但是奇怪的是，微信并没有严格执行。</strong>典型例子，网易严选和腾讯地图。但是我最近又看了一下，发现网易严选已经做了整改了，而腾讯地图依然在继续使用被微信严厉禁止的客服跳转方式。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/2EYRmJCdDVdcxmlzRtoH.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="302" height="537" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/3gwQkntaomanm6DZe8r2.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="301" height="535" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/nibrTyob6Ki7Cc4iHgcB.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="299" height="532" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/G0UzoF3ek92QrGLpkI0r.png" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="303" height="539" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">腾讯地图：你也配姓赵？</p>
<p>“我的区长父亲”系列还有知乎，虽然微信说5月20号就禁用“微信打开app”，但是直到今天，知乎小程序依然可以打开知乎app。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/CsJ3IYyrBDqfxpMsLZWW.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="306" height="544" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="小程序全面禁止打开APP，真的可以提升用户体验吗？" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/QDgKB2PkEvBAeoNXtM5M.jpeg" alt="小程序全面禁止打开APP，真的可以提升用户体验吗？" width="298" height="530" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">腾讯参与知乎多轮融资</p>
<p>最后总结来看，微信关闭“小程序打开app”服务，的确可以迫使一些商家进行整改，让用户在小程序里形成闭环，而不是强迫用户必须去app才能继续操作，这一点的确可以提升用户体验。</p>
<p>但是微信在这件事上的一刀切和不公平执法，可能会迫使一些商家直接弃用微信小程序，转而继续使用h5，这就又回到了微信小程序出现之前的老路，等于直接否定小程序的存在意义。</p>
<p>代表张小龙对于后移动互联网时代应用形态思考的微信小程序，未来任重而道远。</p>
<h3>#专栏作家#</h3>
<p>王M争（微信公众号：王M争），人人都是经理专栏作家，资深互联网人，B站账号：王M争</p>
<p>本文原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4607775" data-author="219535" data-avatar="http://image.woshipm.com/wp-files/2017/03/Wxy3VtbyAZ8KvsKQjMb1.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            