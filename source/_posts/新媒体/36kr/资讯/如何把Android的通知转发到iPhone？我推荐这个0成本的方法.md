
---
title: '如何把Android的通知转发到iPhone？我推荐这个0成本的方法'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220126/v2_609f4f342085466eab456572666f9642_img_000'
author: 36kr
comments: false
date: Wed, 26 Jan 2022 05:00:38 GMT
thumbnail: 'https://img.36krcdn.com/20220126/v2_609f4f342085466eab456572666f9642_img_000'
---

<div>   
<p>为了能够用两个<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>彻底分离工作和生活，又苦于 iPhone 不能双开微信，我开始使用 Android 手机作为工作备用机，无奈之下加入了双机党的阵营。</p> 
<p>我有两个号码：A 和 B，因为号码 A 流量多，就把它留在了主力机上，号码 B 挪到了备用机。可大部分服务都是用号码 B 注册的，使用主力机时，时常因为各种原因，需要填写号码 B 收到的短信验证码，此时又得拿起备用机查看验证码。如此反复，真的令人非常不爽。</p> 
<p>为此我开始寻找 Android 短信转发的解决方案，最终通过 SmsForwarder + Bark 解决了这个问题，经过一段时间的使用，效果非常不错。现在我把这个 Android 手机短信转发给 iPhone 的方案分享给大家，有需要的朋友可以作为参考。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_609f4f342085466eab456572666f9642_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>短信转发至 iPhone 效果</p> 
<h2 label="一级标题" style><strong>在 iPhone 中安装 Bark App</strong></h2> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_94b7012518f649b9b45f2d8b85190e56_img_000" referrerpolicy="no-referrer"></p> 
<p>Bark 是一款 Apple 生态内的自定义推送服务，它充分利用了 Apple 推送通知服务 (APNs) 进行工作，原理是将自定义推送内容通过 发送端 > Bark 服务端 > 苹果 APNs 服务器 > 你的设备 > Bark App 进行传递。由于完全依赖 Apple 推送通知服务，App 本身无需前台运行，几乎不会对 iPhone 的续航产生影响。</p> 
<p>第一次打开 Bark App 时，会自动为你的设备生成 key ，复制 App 首页自动生成的第一个带有 key 参数的 URL 备用。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_d01b06f7283e4e0f902797d2a0a85d77_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Bark App</p> 
<h2 label="一级标题" style><strong>在 Android 手机中安装短信转发器 SmsForwarder</strong></h2> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_9840e08550044732895af696915ead11_img_000" referrerpolicy="no-referrer"></p> 
<p>SmsForwarder 是我在酷安找到的开源 Android 短信转发工具（https://github.com/pppscn/SmsForwarder），它有一个简单直白的中文名称「短信转发器」，这款 App 在转发短信时，能设置转发模板，还能对短信内容设置多种筛选条件，可以利用<a class="project-link" data-id="8301" data-name="钉钉" data-logo="https://img.36krcdn.com/20220124/v2_9360cb73af2946bdaf1bcc006fa5c695_img_000" data-refer-type="1" href="https://www.36dianping.com/space/2220121250?mp=zzquote" target="_blank">钉钉</a>、<a class="project-link" data-id="1657051" data-name="飞书" data-logo="https://img.36krcdn.com/20220125/v2_421cb14103d64f8ca176b9b1d9a48e90_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4727300221?mp=zzquote" target="_blank">飞书</a>、邮箱、<a class="project-link" data-id="8304" data-name="企业微信" data-logo="https://img.36krcdn.com/20220120/v2_3b21f33e96a7496ea64878258c4ac87d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/3898012115?mp=zzquote" target="_blank">企业微信</a>、Server 酱、Telegram 等多种渠道进行推送。</p> 
<p>打开「短信转发器」，依次点击「发送通道」-「添加发送通道」，选择「Bark」，填入上一步在 iPhone 端 Bark App 中生成的推送地址，点击「确定」保存设置。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_ae55523681ec4b41abf0b6ad9ff17112_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>将 Bark 设置为发送通道</p> 
<p>返回 App 首页，点击「转发规则 - 添加短信转发」，设置好你自己的短信转发规则。比如：当你只想转发备用机的验证码短信时，可以将短信内容匹配关键字设置为「验证码」，这样只有包含验证码的短信才会被转发，其他诸如广告营销、公益宣传等内容的短信则不会被转发。此处也可以根据自己的需要添加其他规则。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_9271845efbde4807bf84dfd61ba5b262_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>设置短信转发规则</p> 
<p>除了转发短信，SmsForwarder 还可以转发 Android 手机的未接来电和应用通知，因为与本文主题无关，感兴趣的朋友可以自行下载体验。</p> 
<h2 label="一级标题" style><strong>为 SmsForwarder 设置应用权限 ⚠️</strong></h2> 
<p>出于续航因素考虑，Android 手机的后台策略都非常保守，致使 SmsForwarder 在后台运行时，容易被系统 kill 软件后台进程。为保证短信转发功能的正常运作，需要在手机系统中设置好 App 的自启动、后台运行、电池优化等必要权限。由于各品牌手机的设置方式存在差异，在此不做详细说明。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_89cf7abfbfb64e1d9b26f7f356b5296e_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>示例：realme UI 后台权限设置</p> 
<p>出于隐私角度考虑，一些国内的定制系统会默认隐藏包含验证码的短信，第三方应用即使被授予短信权限，也无法读取到这类型的短信。因此需要在手机短信设置中关闭相关防护功能，此类短信才能被读取并转发至其他设备。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220126/v2_82bcec292aaa4b9daf0be9f2cd2cb55e_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>realme UI 验证码安全保护</p> 
<h2 label="一级标题" style><strong>将 Android 手机收到的验证码转发至 Mac</strong></h2> 
<p>根据同样的原理，你也可以在 Mac App Store 中搜索安装 Bark，生成推送地址后，在 SmsForwarder 中将其设置为第二<a class="project-link" data-id="7583" data-name="个推" data-logo="https://img.36krcdn.com/20220120/v2_36285bc5bdd948668c363be6927c18f3_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4376601213?mp=zzquote" target="_blank">个推</a>送通道。这样你就可以在 iPhone 和 Mac 上同时收到来自 Android 手机的验证码短信，方便你在使用 Mac 时填写验证码。</p> 
<h2 label="一级标题" style><strong>总结</strong></h2> 
<p>得益于Apple 推送通知服务的稳定性，无论是 WiFi 还是蜂窝数据，这一套短信转发方案几乎都没有延迟，使用起来非常的方便。缺点是两台设备必须都要联网才能实现转发和接收，而且只能从 Android 转发短信到 iPhone，反向无效。</p> 
<p>如果对 Bark 提供的后端服务有隐私方面的顾虑，你也可以通过该项目在 GitHub 公开的后端代码自行搭建后端服务。除了本文中提到的 Bark，你还可以使用 PushDeer 等其他类似的推送服务进行转发，工作原理和配置方法也是类似的。</p> 
<p>原文链接： </p> 
<p>https://sspai.com/post/71054?utm_source=wechat&utm_medium=social </p> 
<p>作者：JLDUAN </p> 
<p>题图来自 Unsplash：@neonbrand </p> 
<p>本文来自微信公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247530061&idx=1&sn=415252bb020134e7f7880a6816af64da&chksm=fdb38327cac40a31bde59fabab47a9eabd89ee925b786fdc8216e14721508267798d0c7209d3#rd">“少数派”（ID：sspaime）</a>，作者：JLDUAN，36氪经授权发布。</p>  
</div>
            