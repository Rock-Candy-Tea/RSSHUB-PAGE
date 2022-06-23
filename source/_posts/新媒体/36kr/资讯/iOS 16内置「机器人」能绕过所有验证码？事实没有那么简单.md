
---
title: 'iOS 16内置「机器人」能绕过所有验证码？事实没有那么简单'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220623/v2_54064401d8624081a221302e7d13a1ed_img_000'
author: 36kr
comments: false
date: Thu, 23 Jun 2022 02:41:06 GMT
thumbnail: 'https://img.36krcdn.com/20220623/v2_54064401d8624081a221302e7d13a1ed_img_000'
---

<div>   
<p>就在前几天（6 月 20 日），许多媒体报道 XDA 论坛发现苹果发布的 iOS 16 系统中包含「验证码机器人」的新闻。</p> 
<p>升级到 iOS 16 开发者预览版后，你可以在「设置」app 中的 Apple ID 部分找到「密码与安全性」，拉到最底下，就有「自动验证」的开关。</p> 
<p class="image-wrapper"><img data-img-size-val="750,1334" src="https://img.36krcdn.com/20220623/v2_54064401d8624081a221302e7d13a1ed_img_000" referrerpolicy="no-referrer"></p> 
<p>如果你了解验证码（即 CAPTCHA）的全称与作用，那么就会对这个开关有许多疑问：既然验证码是「防止机器人」的，那这个功能岂不是要让验证码形同虚设？</p> 
<p>事实当然不是如此。这个功能不能被称为「验证码机器人」，它利用的是一种全新、开放的验证机制——私密证明令牌（Private Attestation Token，PAT）。</p> 
<h2><strong>验证码有什么问题？</strong></h2> 
<p>从电子邮件和 BBS 社区诞生以来，垃圾信息泛滥一直都是互联网上的「老大难」问题。而解决这个问题最有效的方法（几乎也是目前唯一方法），就是一种称作 CAPTCHA 的机制，即我们常说的「验证码」的一种（另一种用来进行实名制和信息验证的验证码，不在本文讨论范围内）。</p> 
<p>CAPTCHA 又称被作「反向图灵测试」。顾名思义，它通过一些对机器很困难、但对人类很简单的问题，来帮助网站验证用户是否是真人。</p> 
<p>这类验证码诞生差不多 20 年左右，基本原理几乎没有怎么变化，变的只是让用户判断歪歪扭扭的色块，变成在一堆图片中找出对应的物体。只不过只要是有过一定网络阅历的人，一定有过在十万火急的时候被「找出喷气式飞机的图片」的要求搞得特别想砸电脑手机的时刻，体验算不上良好。</p> 
<p class="image-wrapper"><img data-img-size-val="562,630" src="https://img.36krcdn.com/20220623/v2_dd746bf0e8064dab85901df6e959ab8e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲ 看见是不是心肺停止了？网页截屏来自 hCaptcha 官网</p> 
<p>目前，也有另一种区分人和机器的方法，即通过读取尽可能多的用户访问痕迹，用 AI 模型判断用户的行为是否是一个正常人。Google 推出的 noCAPTCHA 服务就是使用这种方式来判断用户的真实性。</p> 
<p>这种验证方式确实可以帮助用户尽可能绕过明显的验证过程，但同时也牺牲了隐私。毕竟，为了证明「我是人」，我需要把我的上网痕迹全部都告诉 Google 或者其他大公司，想想都有点不对劲。</p> 
<p class="image-wrapper"><img data-img-size-val="616,164" src="https://img.36krcdn.com/20220623/v2_e7223b6385864a28a9363758b539da5e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲ 「点一下」验证的背后，就是隐私的让渡. 图片来自 Google reCAPTCHA 官网</p> 
<h2><strong>PAT 是什么？它如何验证用户不是自动程序？</strong></h2> 
<p>PAT 并不指代某一种技术或某一种服务，而是一个验证用户的协议。它需要用户、硬件设备厂商和验证码服务提供商三方共同参与，才能完成验证过程。</p> 
<p>整个协议流程是这样的：</p> 
<ol> 
 <li>网站接入支持 PAT 的验证码服务</li> 
 <li>用户向网站发起请求，网站要求用户前往验证码服务进行验证</li> 
 <li>验证码服务向硬件制造商发起验证请求（帮我看看这台机器有没有被破解？）</li> 
 <li>硬件制造商检查用户所持硬件编号等，并通过类似 DeviceCheck 或 SafetyNet 等技术框架检查用户设备的完整性</li> 
 <li>确认用户硬件未被破解（越狱或 root）之后，硬件制造商要求验证码服务向用户发放证明</li> 
 <li>用户将证明随后续请求发送给网站，网站将证明拿给验证码服务进行验证</li> 
 <li>验证通过，请求正常处理</li> 
</ol> 
<p class="image-wrapper"><img data-img-size-val="1080,685" src="https://img.36krcdn.com/20220623/v2_b0f3c5e89d924fedb425acf1ae77cc06_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲ 完整的 PAT 验证流程示意图. 图片来自 Cloudflare 官方博客文章</p> 
<p>看起来很复杂，但整个流程的重点有两个：一是整个验证流程没有任何需要人工介入的验证过程（输入字符或点击图片等）；二是证明「我是人」的方式也从答题、隐私让渡，变成更合理的检查设备是否被破解等信息。</p> 
<p>因为 PAT 验证的重点，从「你是不是人」改为「你的设备是否被篡改而有滥用嫌疑」，自然也不需要用户输入复杂的验证码，也不再需要持续追踪用户的行为进行判断。</p> 
<h2><strong>是不是真的可以和「验证码」说拜拜了？</strong></h2> 
<p>还不一定——至少在未来几年里，我们还是得和验证码「斗智斗勇」。</p> 
<p>首先，技术推广需要一定时间。即使 PAT 是由 IETF、苹果、Google 和 Cloudflare 这样的大机构共同起草、推出的验证协议与标准，但目前只有 iOS 16 和 Cloudflare（防止网站被攻击的云服务商）支持这个验证协议（注：开发者和在线服务目前可以在 Cloudflare 和 Fastly 接入测试版 PAT 验证）。</p> 
<p>无论是终端用户的软硬件更新，还是验证码服务与各大网站与服务跟进，都需要一定的时间。</p> 
<p>其次，由于中国大陆 Android 系统生态的特殊情况，Android 机型并不能直接通过 Google Play 服务中内嵌的 SafetyNet 框架来完成验证。也就是说，每家 Android 系统厂商都要单独接入 PAT 协议，才能为自家产品添加 PAT 支持。</p> 
<p>另外，在桌面设备领域，还有许多 DIY 组装机的存在。由于此类设备无法找到可供担保的 PAT 验证人（设备制造商），因此也很有可能无法真正享受到 PAT 带来的便利。</p> 
<p>不过，对于大多数人而言，PAT 确实是一种能够兼顾体验和隐私的验证协议。我们期待国内的 Android 厂商和在线服务可以尽快跟进协议，让普通人也可以享受更好的互联网体验。</p> 
<p class="image-wrapper"><img data-img-size-val="445,250" src="https://img.36krcdn.com/20220623/v2_aeac3b08a6494c6d9b95b56acf8190cf_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">题图来自：Cloudflare 官方博客</p> 
<p class="editor-note">本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/yfky8P0QZCGPjs5sN0WV7A">“APPSO”（ID:appsolution）</a>，作者：郑智文，36氪经授权发布。</p>  
</div>
            