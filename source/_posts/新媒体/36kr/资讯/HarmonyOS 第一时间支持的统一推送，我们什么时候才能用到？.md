
---
title: 'HarmonyOS 第一时间支持的统一推送，我们什么时候才能用到？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210615/v2_ad1a0c49e2c04a14b6c11a2b6a5d813e_img_000'
author: 36kr
comments: false
date: Mon, 14 Jun 2021 23:38:46 GMT
thumbnail: 'https://img.36krcdn.com/20210615/v2_ad1a0c49e2c04a14b6c11a2b6a5d813e_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/_oBiPCylwOzZmeS64hhFxw">“APPSO”（ID:appsolution）</a>，作者：吕朋铭，36氪经授权发布。</p> 
<p><a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>发布 HarmonyOS 2 的第二天，统一推送联盟就发布了鸿蒙支持统一推送标准及相关规范的公告。</p> 
<p>在拥抱新平台这件事上，统一推送联盟的速度很快。但「统一推送」这件事提了这么多年，怎么我们到现在还没用上？</p> 
<p class="image-wrapper"><img data-img-size-val="1080,608" src="https://img.36krcdn.com/20210615/v2_ad1a0c49e2c04a14b6c11a2b6a5d813e_img_000" referrerpolicy="no-referrer"></p> 
<p>早在 2017 年，统一推送联盟就由工信部牵头成立，主办方为工信部旗下的中国信息通信研究院泰尔终端实验室。</p> 
<p>当时的设想是：未来将由终端厂商提供系统级推送服务，不再允许各应用在后台保留常连接。与此同时，各终端厂商实现推送通道接口和功能统一，方便开发者接入。</p> 
<p>在这一标准下，消息将通过统一的服务器推送至用户设备，而无需应用驻于后台。</p> 
<p>四年过去了，虽然国内的 Android 厂商大多都支持了这一标准，但至今用户依然没有真正的用上这一推送服务，各个手机厂商使用的还是自家推送服务。</p> 
<p class="image-wrapper"><img data-img-size-val="832,252" src="https://img.36krcdn.com/20210615/v2_0874ffb0b97a4dc0ab67014c678c57e0_img_000" referrerpolicy="no-referrer"></p> 
<h2>为什么需要统一推送</h2> 
<p>Android 手机早已步入 6G 起步、16GB 顶配的大内存时代，隔壁 iPhone 还在用着 4G 的内存，内存最大的 iPhone 12 Pro 系列也不过 6G，这个配置在国内的 Android 手机市场上只是千元机的水平。</p> 
<p>不过，小内存并没有对 iPhone 的使用体验造成太大影响，除了 iOS 的后台机制需要的内存更少，还有另一个原因，那就是因为国内 Android 手机没有 FCM 推送，各个手机厂又没有统一的推送服务，如果应用想要推送通知，就必须常驻后台，大内存没有带来更出色的体验，不过是保持手机的流畅运行罢了。</p> 
<p>即便如此，如果放任各类应用都常驻后台的话，就算再大的内存都不够用。所以手机厂商自家的定制 UI 也制定了很多后台策略，用来限制应用。</p> 
<p class="image-wrapper"><img data-img-size-val="535,725" src="https://img.36krcdn.com/20210615/v2_dd0e76f254bc46e09d8e306947d32c80_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲MIUI 的「照明弹」功能</p> 
<p>不过，没有实时性的应用关闭推送并没有太大影响，可对于即时通讯软件来说，没了推送，还何谈「即时」？而且没了推送通知，用户的打开应用的概率也就更小了，这可是应用收入来源的基本盘，怎么可能轻易放弃。于是，也就催生了各种「毒瘤」应用，「保活」和「唤醒」在应用开发中的重要性也越来越高，为了防止系统「杀后台」，做得也越来越隐蔽了。</p> 
<p>iOS 一直是统一推送机制，应用依赖于苹果提供的 APNs 服务，则可以实现在不开启 应用时也能将通知推送到用户的手机上。这样不仅能用更少的后台服务收到更多的推送通知，还因此降低了手机的功耗，延长了续航的时间。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,693" src="https://img.36krcdn.com/20210615/v2_9bf24570da4a4918be8737d951ae93ed_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲基于 APNs 和 FCM 实现的各种推送 图源：GoodBarber</p> 
<p>Google 也为 Android 提供了 FCM 推送，不过国产应用支持较少，而且在国内也有较大的网络延迟，处于基本不可用的状态。</p> 
<p>所以说，如果没有一个真正的「统一推送」，要么忍受多个应用常驻后台耗电，要么承受可能错过重要消息的后果。</p> 
<h2>五花八门的第三方推送</h2> 
<p>国内不是没有「统一推送」，只不过没那么「统一」。各家手机厂商基本都有自家的推送服务，比如 MiPush、HUAWEI Push，除了手机厂商，也有一些其他的推送服务，比如 TPNS（<a class="project-link" data-id="24961" data-name="腾讯" data-logo="https://img.36krcdn.com/20201201/v2_016524a9a477434cb3584e1558f3257a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/24961" target="_blank">腾讯</a>）、<a class="project-link" data-id="8432" data-name="阿里云" data-logo="https://img.36krcdn.com/20210601/v2_3e6f3dfe2b83401382ba1dd8a53758a3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/8432" target="_blank">阿里云</a>消息推送、<a class="project-link" data-id="3932583" data-name="友盟" data-logo="https://img.36krcdn.com/20210601/v2_829d411b4bf143f6a6a652072a096294_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4838201012" target="_blank">友盟</a>、<a class="project-link" data-id="7583" data-name="个推" data-logo="https://img.36krcdn.com/20210601/v2_f8cbf32ab90d40b99cdab8b435cff3fa_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/7583" target="_blank">个推</a>……</p> 
<p class="image-wrapper"><img data-img-size-val="1080,364" src="https://img.36krcdn.com/20210615/v2_a085468678e24182974ecdfa5290f59c_img_000" referrerpolicy="no-referrer"></p> 
<p>虽然这些第三方推送服务都接入了相当多的国产应用，不过还是会有一些常用应用缺席，比如微信。而非手机厂商的这类推送服务也基本只支持自家应用，当然不可能支持对手应用的推送服务。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,453" src="https://img.36krcdn.com/20210615/v2_dd768e58787d42cf919d025e6d56f170_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲MiPush 支持的部分应用</p> 
<p>同时这些非手机厂商的推送服务平台又悖离了统一推送的初衷，实现推送的前提是要有应用在后台，才能连带其他应用的通知<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210601/v2_2bbe1c6ad79748b3be29e04d8999edac_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>推送，而这其中有些又会在应用间相互唤醒。借保留推送通道之名，成为更难被清理后台的毒瘤应用。</p> 
<p>而「毒瘤」之外的「纯净」应用恐怕对这些五花八门的推送服务也没什么适配的动力，需要适配的不同接口过多，而且其中很多还要再交一笔费用，大公司的应用尚且不愿适配，小型应用的个人开发者更是无力接入了。</p> 
<p>除此之外，很多应用也不愿意将自己的「命运」交给其他的公司把控，如果接入这些推送服务，通知和信息必然要先经过他们的服务器，没有竞争关系倒是好说，如果是竞争对手的话，谁能保证这些数据不会被盗取？而且推送服务平台出现安全问题，会不会也连带着自己的大量关键数据也泄露？如果推送服务不稳定，用户体验变差怎么办？这些都是应用厂商的顾虑，短时间内单靠这些平台也难以形成一个真正的统一推送服务。</p> 
<h2>统一推送是未来趋势，不过还有很长的路要走</h2> 
<p>虽然统一推送其实并不那么完美，即便是 iOS 的 APNs，也常常发生推送延迟的情况，但是相比于国内 Android 消息推送的乱象，早日将推送集中统一分发可能还是最好的解决办法。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/20210615/v2_5e2ba761accf4939b60aa9d55b0f7734_img_000" referrerpolicy="no-referrer"></p> 
<p>虽然统一推送联盟成立了好几年依然没在手机上搭载，但是也为未来在手机上普及做了不少努力。</p> 
<p>一方面是积极广泛地接纳各家厂商的接入，如今已经覆盖基本所有国产手机，就连三星这种国外手机厂商也接入了统一推送联盟，华为的鸿蒙 2.0 刚一发布，也迅速支持了统一推送联盟。</p> 
<p>另一方面也为统一推送服务制定了很多标准，先后发布了内容安全平台「推必安」、信令级推送「推必达」。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,497" src="https://img.36krcdn.com/20210615/v2_20c8a44af3a84bac9b97891689dad55a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲推必达官方介绍</p> 
<p>「推必安」能够有效减少骚扰信息和不良内容的推送，能够净化手机上的消息通知；「推必达」则类似短信，即便没有网络也能通过运营商进行消息推送。</p> 
<p>但这些的前提都是未来能够真的投入使用，可是按照目前的进度来看，可能距离我们还比较遥远。</p> 
<p>统一推送联盟为我们展现了一个很好的未来和更多的可能性，让我们看到了未来会有一个比 APNs 和 FCM 更好用的国内通知推送服务出现。可是提了这么多年，却迟迟还没用上，未免也有「画饼」的嫌疑。</p> 
<p>到底何时才能协调好手机厂商和应用程序来完成统一推送服务的落地，现在还是一个未知数。毕竟除了利益的分配，服务器的承载能力也是一个大问题，</p> 
<p>不过，当那一天到来之时，国内 Android 的通知推送也会变得省电又干净，这对于全体手机用户来说都是一项重大的进步。</p>  
</div>
            