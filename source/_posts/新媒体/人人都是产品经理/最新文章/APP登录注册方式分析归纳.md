
---
title: 'APP登录注册方式分析归纳'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/x9AsnPguxpVi10mCqsXE.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 14 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/x9AsnPguxpVi10mCqsXE.jpg'
---

<div>   
<blockquote><p>导读：不同的产品有不同的登录注册方式，且大部分产品并不是采用单一的登录注册方式，而是采用多种登录注册方式的混合。究其根源产品的登录注册方式往往是其产品属性和商业模式决定的。不同的产品类型，对登录注册模块的需求也不同。本文作者总结了一些APP的登录注册方式，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5044069 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/x9AsnPguxpVi10mCqsXE.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>针对市面上的十款主流APP登录注册方式做了一个小调研，在此做一下分析归纳：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Ky8mgN605mLlb16d9pV1.png" referrerpolicy="no-referrer"></p>
<p>不同的产品有不同的登录注册方式，且大部分产品并不是采用单一的登录注册方式，而是采用多种登录注册方式的混合。究其根源产品的登录注册方式往往是其产品属性和商业模式决定的。不同的产品类型，对登录注册模块的需求也不同。</p>
<h2 id="toc-1">一、登录注册方式</h2>
<h3>1. 本机号码一键登录</h3>
<p>不需要输入密码或验证码，只需要同意相应的运营商认证服务条款点击按钮就直接登录了。目前主流的APP都在使用和推荐这种登录方式，真的是懒癌患者的福音啊！</p>
<p>可国民社交软件微信却没有采用这种登录方式？本机号码一键登录其实也算是一种特殊的三方授权登录方式，而目前来说应用最广的三方授权登录方式仍然是微信授权，这也就不难看出微信为啥不采用本机号码一键登录的方式了。</p>
<p>不过这种登录方式需要运营商进行本机手机号的认证，认证的过程会把网络切换为移动网络，在关闭移动网络或者没有插手机卡的情况下，是无法完成认证的。所以设计产品的时候应该考虑其兼容性，在认证失败的情况下，允许用户手动输入手机号登录。比如说小红书在关闭移动网络的情况下，重新打开应用，登录页面手机一键登录变为了手机号登录，点击手机号登录可以手动输入“手机号+验证码”进行登录。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZnL9zGNn82eZP2B6KMO7.jpeg" referrerpolicy="no-referrer"></p>
<h3>2. 手机号+验证码</h3>
<p>未注册的手机号验证后自动创建账户，后期可以填写或修改密码，就获得了以手机号码为帐号的登录方式。可以说这是目前来说比较主流的登录注册方式。但是这样的登录方式也有一定的弊端，第三方短信平台一旦出问题或者手机信号异常等使用户收不到验证码，就会给登录造成麻烦。</p>
<h3>3. 第三方授权登录（微信、QQ、微博、其他）</h3>
<p>通过第三方授权进行登录，如微信、qq、微博等。这种登录方式可以减少因为注册繁琐带来的用户损失。不过三方登录也有要注意的事项：</p>
<p><strong>1）第三方授权登录方式，不能获取用户的手机号</strong></p>
<p>相关法规要求网络运营者为用户提供特定服务时，必须要求其实名制，是需要用户手机号的。所以有些产品在用户确定授权之后，会强制让用户绑定手机号；有些则可以选择跳过，后续需要用户手机号时再让用户进行绑定。这就相当于让用户在第三方快捷登录后又进行了手机验证登录，对于用户来说并不是省时省力的方法。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dec5Ap83aXz6TC8KcR8k.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>2）第三方授权登录可能还会造成同一个用户在一个平台有多个账号的情况发生</strong></p>
<p>三方授权登录后强制让用户绑定手机号可以解决这个问题。但正如上文所说的用户刚刚授权三方登录又让用户手机验证登录，极大的降低了用户体验。</p>
<p>1/2/3为快捷登录方式，注册跟登录同步，如果产品处于快速发展期，以增加用户量为主要目的时，可考虑优先采用快捷登录方式。不过这要根据产品具体情况具体分析，不能一概而论。</p>
<h3>4. 手机号+密码</h3>
<p>手机号+密码是前几年比较主流的登录注册方式，由于手机上APP的增多，我们不可能每个APP的密码都记得住。但这个却可以作为手机号+验证码登录方式的一个补充。大部分APP用手机号+验证码登录注册后，都会有设置账号密码的功能。当第三方短信平台出问题或者用户信号异常收不到短信验证码时，用户就可以用手机号+密码进行登录。并且一般在手机号+验证码登录的界面都会有手机号+密码登录的切换入口。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/XwOSI8mcvf0DfK3eJVbV.jpeg" referrerpolicy="no-referrer"></p>
<h3>5. 邮箱+密码</h3>
<p>邮箱验证注册的方式是pc时代盛行的，随着移动互联网的发展，国内主流的APP已抛弃了邮箱验证注册的方式，但有些还保留着邮箱+密码这样的登录方式，也是为了兼容pc端和老用户。如哔哩哔哩APP端不再提供邮箱验证注册方式，但登录还保留着邮箱登录方式就是为了兼容老用户。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/MVIWXkaAXA2FbkS0uPnk.jpeg" referrerpolicy="no-referrer"></p>
<h3>6. 用户名+密码</h3>
<p>这种方式的存在是依赖于产品的功能，也可能是为了兼容pc端。比如说淘宝从pc时代就开始盛行，从那时开始用淘宝的人肯定都熟悉旺旺，卖家和买家通过旺旺进行聊天。每个人的旺旺号是唯一的，通过旺旺号卖家可查询买家在本店的交易记录，这个旺旺号就是淘宝会员名。等到移动app时代，淘宝app就保留了淘宝会员名+密码这样的登录方式。相应的支付宝也继承了淘宝会员名+密码的登录方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/4jvIXFAfAh5KDh9jkZ8W.jpeg" referrerpolicy="no-referrer"></p>
<p>4/5/6注册跟登录异步,也表明了APP端注册的方式和登录的方式并不一定是一一对应的，可能是为了兼容pc端和老用户。</p>
<h3>7. 特殊方式「刷脸登录/指纹登录/声音锁登录/手势登录」</h3>
<p>一般作为登录后的二次验证，适用于保密性较强、或者信息安全层级较高产品的验证。例如支付宝APP和招商银行APP，当我们离开应用一段时间后，再次打开应用就支持指纹/手势二次登录验证。这样既可以保证我们账户信息的安全，也可以使我们在使用APP时不用每次都进行繁琐的登录过程。但是在不设置指纹/手势登录验证时，支付宝和招商银行登录状态处理机制又有一定的不同：离开应用一段时间后，支付宝始终处于登录状态，而招商银行却每次都需要进行重新登录。支付宝APP退出登录后还支持刷脸/声音锁登录。微信也可以通过声音锁登录。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/RfMinhE3eQ7F2OpCkJ8w.jpeg" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、写在最后</h2>
<p>并不是所有的APP都需要登录注册，一些纯工具类的产品就不用进行登录注册，比如说计算器、指南针、天气、日历等。</p>
<p>还有些APP会为用户提供游客身份，在非注册登录的情况下允许用户浏览，充分体验产品之后，在需要账户信息时才提醒用户注册或登录。先让用户进行登录注册再浏览还是先浏览再登录注册，取决于产品的功能是否基于用户或用户与用户之间的关系来触发。</p>
<p>登录注册模块“这潭水”真的很深。文章就先写到这里了，还有好多逻辑没能思考到和写进去，只能等着后续“小步快跑，快速迭代”了！</p>
<p> </p>
<p>本文由 @汪仔4029 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5032195" data-author="1040304" data-avatar="https://static.qidianla.com/woshipm_def_head_1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            