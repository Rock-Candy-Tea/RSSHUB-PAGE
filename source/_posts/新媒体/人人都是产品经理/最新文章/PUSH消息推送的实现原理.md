
---
title: 'PUSH消息推送的实现原理'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/hBoJEGgkbvNmy4sKo4Pw.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 10 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/hBoJEGgkbvNmy4sKo4Pw.jpg'
---

<div>   
<blockquote><p>编辑导语：如今，push已经成为了我们手机信息流的一种推广方式，那么push消息推送是如何实现的呢？作者总结了几种消息推送的类型以及实现原理，一起来看看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5481067 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/hBoJEGgkbvNmy4sKo4Pw.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、消息推送的类型</h2>
<h3>1. 短信推送</h3>
<p>指通过运营商将文本或数字消息传递至用户手机或其他电信终端。它凭借着优秀的发送率和到达率，一度成为最受欢迎的营销工具之一。</p>
<p>一般企业不太会直接对接移动、联通、电信来实现短信发送，而是通过中间的服务商将各地区的运营商资源整合后提供统一、便捷的短信服务，这类服务商叫短信服务商，也可叫短信SP。</p>
<p>目前，支持个人短信服务的厂商有阿里云、腾讯云，其他厂商都是需要认证为企业用户才能使用短信服务平台。短信供应商根据发送量进行收费，发送越多单价越便宜。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/srBQPRv5P5oBxv1JRGU0.png" alt width="794" height="478" referrerpolicy="no-referrer"></p>
<h3>2. 邮件推送</h3>
<p>EDM（Email Direct Marketing），即电子邮件营销。企业可以通过EDM建立同目标顾客的沟通渠道，向其直接传达相关信息，用来促进销售。邮件推送具有精准送达、个性化定制、内容格式丰富的特点。亚马逊就曾凭借优秀的电子邮件营销出圈。</p>
<h3>3. 微信消息推送</h3>
<p>截至2022年3月31日，微信及WeChat的合并月活跃账户数为12.883亿。随着微信的影响力的增强，越来越多的企业也逐渐重视微信生态的布局，微信消息推送就是其一，它的到达率高、支持精准推送。不足的是，其内容受限于模板，且微信提供的模板数量有限，一个公众号最多选用25种模板。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/r8CM3pqeO1DrBJj5pqeb.png" alt width="622" height="1106" referrerpolicy="no-referrer"></p>
<h3>4. 通知栏推送</h3>
<p>通知栏推送，也被称为PUSH推送，即在手机终端锁屏状态下通知栏展示或在操作前台顶端弹出的消息通知。用户可以在移动设备锁定屏幕和通知栏看到push消息通知，通知栏点击可唤起APP并去往相应页面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/BANrge0c3GuW8AyvkLDR.jpeg" alt width="632" height="410" referrerpolicy="no-referrer"></p>
<h3>5. 应用内推送</h3>
<p>应用内推送常见的形式有弹窗、顶部悬浮通知、收件箱等，可由应用自行控制样式和内容格式。不足的是只能在用户在线时查看，触达有限。</p>
<h2 id="toc-2">二、移动推送的三种实现方式</h2>
<p>在本篇文章中主要介绍通知栏推送的实现方法。在了解具体的推送原理之前，我们先来了解下移动推送的三种实现方式。</p>
<h3>1. 轮询方式（PULL）</h3>
<p>客户端和服务器定期地建立连接，通过消息队列等方式来查询是否有新的消息，需要控制连接和查询的频率，频率不能过慢或过快，过慢会导致部分消息更新不及时，过快会消耗更多的资源（流量、电量等），对用户体验有较大伤害。</p>
<h3>2. 短信推送方式（SMS PUSH）</h3>
<p>通过短信发送推送消息，并在客户端植入短信拦截模块（主要针对 Android 平台），可以实现对短信进行拦截并提取其中的内容转发给 App 应用处理，这个方案借助于运营商的短消息，能够保证最好的实时性和到达率，但此方案对于成本要求较高，开发者需要为每一条 SMS 支付费用。</p>
<h3>3. 长连接方式（PUSH）</h3>
<p>客户端主动和服务器建立 TCP 长连接之后, 客户端定期向服务器发送心跳包用于保持连接, 有消息的时候, 服务器直接通过这个已经建立好的 TCP 连接通知客户端。</p>
<p>尽管长连接也会造成一定的开销，对于轮询和 SMS 方案的硬伤来说，目前已经是最优的方式，而且通过良好的设计，可以将损耗降至最低。不过，随着客户端数量和消息并发量的上升，对于消息服务器的性能和稳定性要求提出了非常大的考验。因此，就难度而言，此方式代价最高。</p>
<p>基于上面的介绍，我们可以知道长连接方式是移动推送中目前最优的方案，它也是当前主流的推送方式，基于该推送方式逐步发展出系统级、应用级一系列的推送解决方案。</p>
<h2 id="toc-3">三、系统级推送解决方案</h2>
<h3>1. iOS 平台（APNs）</h3>
<p>iOS 在系统层面与苹果 APNs（Apple Push Notification service）服务器建立连接，不论App是在线状态还是离线状态，消息推送至iOS的APNS服务器，APNS再根据设备标识推送至指定设备，用户即可接收到消息。</p>
<p>大致链路为：业务系统（发起推送）——第三方消息推送服务商或自建消息推送系统的服务器（推送逻辑控制、推送下发）——苹果APNS服务器——指定用户设备。</p>
<p>整个过程很清晰，并且所有 APP 都共用同一个系统级的连接，减少了系统开销，虽然 APNs 能无障碍的访问，但实际使用过程中，也会存在延时和丢消息的情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/zjlfFNxSBlLT4F9TIr9j.png" alt referrerpolicy="no-referrer"></p>
<h3>2. Android 平台</h3>
<p>Android 的 C2DM（Android Cloud to Device Messaging）采取与 iOS 类似的机制，都是由系统层面来支持消息推送，但是由于 Google 的服务在国内不能稳定的访问，此方案对于中国用户来说基本是无法使用的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Zo2ZtP7IoRp8EIvClLCV.png" alt referrerpolicy="no-referrer"></p>
<p>除了 Google 官方提供的方案，中国众多的手机厂商在其定制的系统中也内置了推送功能，如小米、华为等。不过在建立推送服务之前，需要申请开发者账号并绑定App，在开放平台开通厂商通道推送的权限。这类厂商机型支持在线离线状态的消息推送。</p>
<p>消息推送大致链路为：业务系统（发起推送）——第三方消息推送服务商或自建消息推送系统的服务器（推送逻辑控制、推送下发）——厂商服务器——指定用户设备。</p>
<h2 id="toc-4">四、应用级推送解决方案</h2>
<h3>1. 第三方推送服务</h3>
<p>鉴于 Android 平台 C2DM 推送的不可用性，国内涌现出大量的第三方推送服务提供商。目前应用最为广泛的第三方推送服务提供商包括个推、极光、友盟、小米、华为、BAT 等，绝大部分 APP 都会优先考虑采用第三方推送服务。</p>
<h3>2. 自建推送服务</h3>
<p>第三方服务在开发成本和消息到达率上表现都不错，但所有信息会经过第三方服务器，对于信息敏感类 APP 而言，有必要考虑自建一套消息推送服务，能最大化保证安全，但自建推送服务需要对 App 客户端海量长连接的维护管理且面临保证 Push Service 常驻的难题等。</p>
<h2 id="toc-5">五、PUSH推送实现方法总结</h2>
<p>综合以上分析，推送实现方式可以简单概括为：</p>
<p>PUSH消息在消息系统创建好后进入发送阶段，服务端根据用户终端信息进行路由，调用苹果自身的推送通知服务（APNs）或根据根据不同的安卓厂商去调用对应的SDK，最后下达到用户设备。</p>
<p>当然，如果是通过之前说过的个推、极光等推送服务商，那么内部的服务端就无需做这些繁琐的开发工作。他们不仅集成了APNS、小米、华为等大部分厂商通道，还可覆盖微信公众号、微信小程序、短信、邮件、支付宝生活号、钉钉 、企业微信、5G消息、飞书等，同时在补发策略、数据监控等层面也有较为成熟的方案。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/58P06GmGG1bWLQWENHxI.jpeg" alt width="823" height="509" referrerpolicy="no-referrer"></p>
<p>话又说回来，对于产品经理来说，上述内容只需要了解就可以了，我们更关注的还是如何利用推送提升业务转化和用户体验。至于你问我那为什么还要写，当你从0搭建一个app时，就能感同身受了。</p>
<p> </p>
<p>作者：阿宅的产品笔记；公众号：阿宅的产品笔记（PMZZnote）</p>
<p>本文由 @公众号阿宅的产品笔记 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5480930" data-author="830739" data-avatar="http://image.woshipm.com/wp-files/2020/11/gQKSAinApDQ3e0QF6ITC.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            