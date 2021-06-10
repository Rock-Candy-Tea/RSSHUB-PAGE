
---
title: 'iOS 微信万众期待的Callkit 功能要回归了？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210610/v2_43de409ba39e430a8308fda75eaf81fc_img_000'
author: 36kr
comments: false
date: Thu, 10 Jun 2021 11:57:55 GMT
thumbnail: 'https://img.36krcdn.com/20210610/v2_43de409ba39e430a8308fda75eaf81fc_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/9xxfamlkmGKSu-fQEQu3BQ">“科技兽”（ID:KeJiShouX）</a>，作者：小兽，36氪经授权发布。</p> 
<p>最近有不少 iPhone 用户表示，微信语音竟然可以通过系统通话界面接听了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,2077" src="https://img.36krcdn.com/20210610/v2_43de409ba39e430a8308fda75eaf81fc_img_000" referrerpolicy="no-referrer"></p> 
<p>小编也测试了自己的微信，发现确实有一个微信号的设置界面出现「语音通话用系统电话接听」选项（iOS 14.6 系统，微信 8.0.7 版本），开启后可以在不打开微信的情况下接听语音，然而另一个微信号没有出现这一选项。可见目前该功能并未向全体 iOS 微信用户开放，仅仅是在灰度测试中，感兴趣的用户可以测试一下自己是否在测试范围内。</p> 
<p>打开微信「设置—新消息通知」，查看是否出现「语音通话用系统电话接听」选项。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1038" src="https://img.36krcdn.com/20210610/v2_7c5c65f8a5544deaa982f0cb6fcbd043_img_000" referrerpolicy="no-referrer"></p> 
<p>通过系统电话接听语音，其实 iOS 微信几年前就曾支持过这项功能，利用的是苹果的 「Callkit」 技术，然而由于种种原因，2018 年 5 月以后这项功能就下线了。</p> 
<h2> </h2> 
<h2>Callkit 是什么</h2> 
<h2> </h2> 
<p>先来给不了解的小伙伴解释一下什么是 Callkit。</p> 
<p class="image-wrapper"><img data-img-size-val="773,515" src="https://img.36krcdn.com/20210610/v2_5e7d528955cd4787a3823e68d06b645a_img_000" referrerpolicy="no-referrer"></p> 
<p>Callkit 是苹果公司在 iOS 10 推出的开发框架，开发者可通过 CallKit 提供的 API 向系统请求诸如来电、拔出等展现服务，由 Call Service 统一安排调度这些请求以达成统一的交互响应，实现类似传统来电呼叫的体验。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,997" src="https://img.36krcdn.com/20210610/v2_b6d48386f8a84ea38acd3b6d04c5286b_img_000" referrerpolicy="no-referrer"></p> 
<p>失去Callkit的微信只能进入App才能接听语音</p> 
<p>简单来说，「如果没有 Callkit，用户需要打开 App 才能接听语音」，现在的 iOS 微信就是如此。「有了 Callkit 以后，即使在锁屏、应用后台关闭等情况下，我们无需打开 App 就能像接听普通电话一样接听语音」。</p> 
<p>然而这么好用的功能在国内一直是不可用的状态。</p> 
<h2>Callkit 为什么被封</h2> 
<p>苹果 Callkit 功能一直是正常的，苹果只是禁止上架国内 App Store 的应用使用 Callkit 功能，「这一限制从 2018 年 5 月开始，苹果向开发者发送邮件告知之所以这样做是来自工信部的要求」。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,693" src="https://img.36krcdn.com/20210610/v2_2238ead08d0c4f8891094f2ea50c0778_img_000" referrerpolicy="no-referrer"></p> 
<p>一提到 Callkit 被禁，许多人会首先想到是「为了维护运营商的利益」，运营商短信、通话功能被互联网服务取代后将彻底沦为流量管道，显然这不是三大运营商期望看到的结果。</p> 
<p>但如果真是出于这个原因禁止 Callkit，权限更为开放的安卓系统却一直能实现锁屏接听语音与视频通话，且国内安卓用户比苹果多，是不是安卓更要限制一下，为什么偏偏对苹果“动刀”呢？</p> 
<p class="image-wrapper"><img data-img-size-val="765,380" src="https://img.36krcdn.com/20210610/v2_cfa1de3d828c4c32a689bc41ec13bed7_img_000" referrerpolicy="no-referrer"></p> 
<p><a class="project-link" data-id="25386" data-name="中国移动" data-logo="https://img.36krcdn.com/20201104/v2_4df18e31afc64e72b99489dc0bdc15bc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25386" target="_blank">中国移动</a>通话业务收入持续萎缩 来源：塔坚研究</p> 
<p>深究禁止 Callkit 的原因已经没有意义，「当前三大运营商的语音通话业务收入一直是连年下滑的状态，话音被流量取代已是大势所趋，不如顺应这一趋势，放开对 Callkit 的限制」。</p> 
<h2>Callkit 有多好用</h2> 
<p>以 iOS 微信为例，不同于安卓系统必须保持微信处在后台状态，开启「语音通话用系统电话接听」功能后，即使 iOS 微信处于关闭状态，好友发起的语音通话同样会显示在来电界面，接听、挂断方式与普通来电无异。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1038" src="https://img.36krcdn.com/20210610/v2_47ff6fe48dc14e1db0f6aca3010687dd_img_000" referrerpolicy="no-referrer"></p> 
<p>并且，「通过系统电话接听的微信语音会显示在电话 App 的最近通话列表中」，用户可点击通话记录跳转到 iOS 微信直接发起语音，非常方便。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,2077" src="https://img.36krcdn.com/20210610/v2_c74bbe854d4442f4b46b5240d8bc6838_img_000" referrerpolicy="no-referrer"></p> 
<p>iOS 微信自从 v6.6.2 版本取消 Callkit 功能后，一直有用户寻求开启 Callkit 的方法，甚至有人只为使用 Callkit 功能而甘愿不升级新版微信，可见它的魅力有多强大。</p> 
<p>只是「目前 iOS 微信只为少部分用户开启了这项功能，小编也不清楚微信是否真的会全面开放 Callkit」，还是说这只是一个内部 Bug，过不久就会修复。如果未来 iOS 微信的 Callkit 正式回归，绝对是一件可喜可贺的事情，iOS 系统下的微信语音体验会有极大提升。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,720" src="https://img.36krcdn.com/20210610/v2_571978bfabcc4b21a11d633fbb4db127_img_000" referrerpolicy="no-referrer"></p> 
<p>需要注意的是，iOS 微信 Callkit 仅支持语音通话，「视频通话还是会显示为通知横幅」，但视频通话的体验同样有望<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>改善。</p> 
<h2>微信视频通话</h2> 
<p>iOS 微信的另一个痛点是当进行视频通话时将微信切到后台或使用其它 App，视频画面会卡住。其实不止微信视频如此，iOS 平台下的任何 App 进行视频通话都会这样，原因是来自苹果的限制。</p> 
<p>一个好消息是，据小编的了解「苹果将在 iOS 15 中开放多任务下使用相机的接口」，App 开发人员适配后可以令 App 在后台继续访问设备相机，这意味着 iOS 微信进行视频通话时，切换 App 视频画面便定格的情况彻底消失。更进一步的话，「iOS 微信还有望在 iOS 15 系统下支持视频画中画功能」，目前 iOS 14 系统下只有 FaceTime 视频有这项能力。</p> 
<p>期待 iOS 15 正式版推送后（时间大概是 9 月末），我们能有不一样的微信音视频通话体验。</p>  
</div>
            