
---
title: '关于移动游戏SDK，你想了解的都在这里'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202104/02/142350wlvbetlbkgutk5eu.jpg'
author: GameRes 游资网
comments: false
date: Fri, 02 Apr 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202104/02/142350wlvbetlbkgutk5eu.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2491385">
大家好，今天我们介绍一下手游SDK相关的知识，虽然SDK接入更多的工作内容是技术与技术之间的对接沟通，但是作为游戏运营或相关从业者，多多少少了解一些SDK基础，对于在协调对接的过程中也会变得更加高效、游刃有余！<br>
<br>
<strong><font color="#de5650">目录：</font></strong><br>
<br>
1. 认识什么是SDK<br>
<br>
2. SDK包含的功能<br>
2.1 账号注册登录<br>
2.2 支付<br>
2.3 防沉迷<br>
2.4 数据上报<br>
<br>
3. SDK接入前的准备<br>
<br>
3.1 简单的参数获取流程<br>
3.2 包名<br>
3.3 签名<br>
3.4 版本号<br>
<br>
其他<br>
<br>
关于MD5值<br>
关于文件名<br>
关于Appid<br>
<br>
<strong><font color="#de5650">1. 认识什么是SDK</font></strong><br>
<br>
<div class="quote"><blockquote>SDK全称Software Development Kit，也就是软件开发工具包，它是一些被软件工程师用于为特定的软件包、软件框架、硬件平台、操作系统等创建应用软件的开发工具的集合。<br>
<br>
<div align="right">——百度百科</div></blockquote></div><br>
当然，以上解释对于非技术的我们来说，还是稍微显得有点抽象。那么通俗来讲，SDK就是手游渠道（如应用宝、小米应用商店、华为应用商店等）提供的集成了账号注册登录、充值、防沉迷、游戏公告、分享、社区入口、push消息、数据上报、礼包或折扣券等功能的一个集合。<br>
<br>
作为游戏开发者，辛辛苦苦开发完游戏本身的玩法功能后，如果没有这样的SDK，那么势必要自己再去开发一个账号注册登录功能，再去支付宝和微信支付申请支付接口开发一套支付系统，再去研究防沉迷规则开发一套防沉迷系统等等。<br>
<br>
但是，现在有了这样的SDK，作为游戏开发者来说便只需要接入这个SDK，然后做好相关功能接口的联调即可，至于账号注册登录的底层逻辑和数据存储、不同第三方支付渠道的参数申请及接入等等都不需要去考虑，毕竟这些工作SDK已经完成了。<br>
<br>
<strong><font color="#de5650">2. SDK包含的功能</font></strong><br>
<br>
上面我们在介绍什么是SDK的时候其实提到了SDK主要包含的一些功能，对于不同的手游渠道来说，它们所支持的功能不尽相同。比如应用宝因为是腾讯旗下产品，可能集成了QQ和微信的分享功能，但是其他手游渠道SDK就未必会包含该功能。。<br>
<br>
对于SDK不包含的功能，如果涉及到第三方的服务（比如实时语音），可以协调平台SDK部门的同事进行功能新增或者自己申请第三方服务的相关参数直接去接第三方的功能SDK。<br>
<br>
不过，基本上像账号注册登录、支付、防沉迷和数据上报可能都是SDK必备的功能点。<br>
<br>
<strong>2.1 账号注册登录</strong><br>
<br>
一般来说，每个手游渠道都有自己的账号体系，玩家使用该渠道的账号登录从该渠道下载的游戏应用。<br>
<br>
这个账号多数情况对游戏开发者来说是不可见的，往往会以openid或类似的形式开放给开发者，通过这个openid字段开发者可以查询到玩家在游戏里的角色信息，而渠道方则可以通过该字段查询到玩家的账号信息。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_970162" aid="970162" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142350wlvbetlbkgutk5eu.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142350wlvbetlbkgutk5eu.jpg" width="572" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142350wlvbetlbkgutk5eu.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">简单的账号注册登录流程</font></font></div><br>
<strong>2.2 支付</strong><br>
<br>
一般来说，对于手游渠道而已，支付渠道有支付宝支付、微信支付等，对于苹果设备来说就是苹果支付了。<br>
<br>
还有一些其他常见的支付渠道：各渠道自己的钱包支付、云闪付、 QQ钱包、话费卡支付、话费支付等等。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_970163" aid="970163" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142350tdcr1uqad5rcuk1r.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142350tdcr1uqad5rcuk1r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142350tdcr1uqad5rcuk1r.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">小米渠道支付方式</font></font></div><br>
<strong>2.3 防沉迷</strong><br>
<br>
关于防沉迷系统其实包含以下几个部分：实名认证、未成年时长防沉迷和未成年人支付防沉迷。<br>
<br>
我们国家在对游戏的监管上越来越完备，2021年2月24日，中宣部出版局线上召开了“网络游戏防沉迷实名认证系统企业接入培训会”。其中提到，2021年5月31日前，所有游戏企业需完成在运营游戏的防沉迷系统的接入工作；6月1日起，未接入防沉迷系统运营游戏要停止运营。<br>
<br>
国家出台了统一的游戏防沉迷实名认证系统 ，所有游戏产品均需要接入。而各渠道已经开始针对性进行相关功能完善，并将集成在最新版本的SDK中。<br>
<br>
例如小米渠道：<br>
<br>
<div align="center">
<img id="aimg_970164" aid="970164" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142351rasf0mn1bbj1b1ji.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142351rasf0mn1bbj1b1ji.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142351rasf0mn1bbj1b1ji.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">小米渠道SDK防沉迷合规功能</font></font></div><br>
<strong>2.4 数据上报</strong><br>
<br>
数据上报是指将玩家在游戏中的行为数据上报并用于数据后台进行数据可视化报表展示，便于产品运营人员进行产品运营动作规划等。<br>
<br>
我们基于SDK必带的账号注册登录及支付功能，可以知道像账号维度的注册、登录和支付相关数据是可以采集到的。宽泛的来说，就是渠道一定知道这个产品基于用户账号维度下的 每天有多少新增用户、活跃用户、活跃用户活跃时长和留存等活跃项数据，以及他们的付费相关数据。<br>
<br>
如果，还想知道其他更详细的用户行为数据，就需要额外进行有关数据埋点及上报接入，而这一般来说可能开发者肯定会做但是不一定会上报给渠道。<br>
<br>
所以，对于渠道而言，他们知道一款产品的曝光量、点击量、下载量、安装量、账号注册量、活跃账号数以及付费数，可以看到这些基本面之间的转化，然后进行相关优化（如广告位调整、素材优化、账号注册流程优化、渠道侧的充值折扣活动等等）。<br>
<br>
对于开发者而言，他们更多的数据是用户在体验产品本身时的行为数据，各个新手流程后用户数、不同系统玩法参与情况、商城道具销售情况、活动效果等等，从而进行新手流程优化、系统玩法调整、游戏商业化设计迭代、活动规划等等。<br>
<br>
以下是某个埋点需求：<br>
<br>
<div align="center">
<img id="aimg_970165" aid="970165" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142351ccctf3r6f9k6y39k.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142351ccctf3r6f9k6y39k.jpg" width="394" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142351ccctf3r6f9k6y39k.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">案例：道具操作埋点</font></font></div><br>
<strong><font color="#de5650">3. SDK接入前的准备</font></strong><br>
<br>
到这里，我们已经多多少少对SDK有所了解了，那么在接入SDK之前我们需要准备什么呢？<br>
<br>
其实，SDK接入这件事情属于技术们的活，毕竟这是技术对接嘛。但是在SDK接入的时候，有很多前置参数需要用到，这些参数放在SDK里就可以告诉渠道这个应用是谁。<br>
<br>
<strong>3.1 简单的参数获取流程</strong><br>
<br>
一般来说，在渠道的开发者后台直接点击创建游戏应用，填写自己的游戏包名和应用名称就可进行游戏创建然后获取对应参数。（注意：这里的包名创建之后就不能改变了）<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_970166" aid="970166" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142351c17x3jwbr77qth7o.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142351c17x3jwbr77qth7o.jpg" width="572" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142351c17x3jwbr77qth7o.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">创建游戏应用并获取接入参数</font></font></div><br>
这里有两个概念：包名和应用名称。有时候，部分渠道在创建游戏应用获取有关功能时需要用到更多别的前置信息如 签名等，具体我们往下看。<br>
<br>
关于应用名称，其实就是你的这个应用叫啥，比如《王者荣耀》手游的应用名称叫“王者荣耀”。<br>
<br>
<strong>3.2 包名</strong><br>
<br>
关于包名，包名英文名称Package Name。<br>
<br>
<ul><li>基于Android标准的原则</li><li>安卓系统中以包名作为应用的唯一标识，也就是包名必须是唯一的，一个包名就代表一个应用</li><li>包名主要用于系统识别应用，用户其实是无感的</li><li>同一个包名的apk无法在手机系统中同时存在，后安装的会覆盖之前安装的同包名的应用</li><li>此外，对于在渠道发布的应用，如果修改了包名则旧版本用户无法收到渠道应用商店的更新提醒（当然一般这种情况下你的安装包也无法上传过审）<br>
</li></ul><br>
一般来说，各家手游渠道都有自己的apk包名命名规则，比如腾讯的是com.tencent.tmgp.xxxx，小米的是com.xx.mi。<br>
<br>
日常工作中，因为包名可能出现的问题：<br>
<br>
比如我们有两个包名的版本，一个是测试服一个是正式服的，那么他们其实就各有一套参数。如果，程序在打正式服的apk的时候用了测试服的参数，那么就会出现一些SDK功能无法使用的情况；同理，用正式服的参数给了测试服的apk使用亦然。<br>
<br>
<strong>3.3 签名</strong><br>
<br>
签名一词来源于生活中常用的术语，还记得刷信用卡会要求客户签名吗？这个签名的作用是确认这笔消费是本人经手的。计算机中所说的签名和生活中所说的签名在本质上是一样的，它所起到的作用也是一致的！为App签名的本质是说明这个App是我开发的，不是别人。用官方的话说，就是在应用和开发者之间建立可信任的关联。<br>
<br>
<font color="#de5650">签名的作用</font><br>
<br>
<ul><li>这个应用的apk，作者知道是不是他开发的（比如有人弄一个同名apk整非法玩意，反过来诬告y开发者，y开发者解包说签名和我们签名不一样，你这是诬陷！）</li><li>如果有人恶意修改应用apk，重新打包，签名就会不一致</li><li>当我们提交新的apk版本时候，填写签名对比可以用来验证是不是开发者的提交行为<br>
</li></ul><br>
一般来说，签名是打包的程序或者测试操作的，如果想知道签名信息，可以直接找他们了解即可。至于怎么确定签名内容和将签名打进包里，这些就不是我们需要去了解的了，完全属于技术范畴！<br>
<br>
<strong>日常工作中，关于签名我们可能会遇到的问题：</strong><br>
<br>
因为某些SDK功能在申请的时候需求填写签名信息，这些功能在实际使用的时候也是会校验该签名信息的，如果发现签名信息不一致，则该功能会无法使用。<br>
<br>
比如QQ和微信登录功能，在申请QQ和微信相关参数的时候就需要用到签名，签名不一致在选择QQ或微信登录的时候会提示“签名不一致”的错误提示而无法正常使用。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_970167" aid="970167" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142351jmrcc1wr9s5emqny.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142351jmrcc1wr9s5emqny.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142351jmrcc1wr9s5emqny.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏签名</font></font></div><br>
<strong>3.4 版本号</strong><br>
<br>
我们在渠道开发者后台提交新版本的时候，一般都会被要求填写版本号相关信息，当然也有的渠道后台能自动识别上传的apk包的版本号。那么版本号到底是什么呢？<br>
<br>
Google为APK定义了两个属性：VersionCode和VersionName，他们有不同的用途。<br>
<br>
<ul><li>VersionCode：对用户不可见，仅用于应用市场、程序内部识别版本，判断新旧等用途</li><li>VersionName：展示给用户，消费者会通过它认知自己安装的版本，下文提到的版本号都是说VersionName<br>
</li></ul><br>
<strong>比如，某应用商店里可以见的某游戏的版本号信息：</strong><br>
<br>
<div align="center">
<img id="aimg_970168" aid="970168" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142352g9etlffekt7byzf9.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142352g9etlffekt7byzf9.jpg" width="452" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142352g9etlffekt7byzf9.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">和平精英VersionName版本号</font></font></div><br>
从属性上看，用户能看到的版本号VersionName其实对于版本是否需要更新之类的没有任何影响，真正影响到版本更新的是VersionCode。<br>
<br>
如果你不确定版本号是多少，还是找之前负责打包的同学就行了。至于为什么打成这个数值，你自然也是不用去管的。<br>
<br>
<strong>那么，关于版本号我们可能遇到的问题</strong><br>
<br>
<ul><li>同一个版本号（VersionName），对应了多个VersionCode 的情况<br>
</li></ul><br>
比如发布了一个版本号为1.0.0.0的版本，然后发现出现了个小bug，但是需要换整包更新解决。然后开发者只是将VersionCode增加了，版本号没有变化。类似这样的情况，一般来说在渠道后台可能无法提交新的apk包，大多数后台会提示需要上传版本号更高的版本。这种情况，要么和渠道协商沟通特殊处理，要么就是将版本号一并进行增加。（如果将同版本号但是不同VersionCode）的apk包传到应用商店，可能会出现应用商店提示用户更新，但是用户自己感受上是已经是最新的版本号但是被要求更新到同一个版本号的情况）。<br>
<br>
当我们发布一个更高版本号的版本后，出现BUG导致被要求回退版本的情况<br>
<br>
首先需要明确一点：VersionCode的增加是不可逆的，也就更新后的版本无法回滚到旧的版本。这种情况 最好就是尽快解决bug，然后发布新的版本。<br>
<br>
<strong><font color="#de5650">其他</font></strong><br>
<br>
我们在版本管理过程中可能还会遇到一些其他的概念，比如MD5和文件名等等。<br>
<br>
<strong>关于MD5值</strong><br>
<br>
<div class="quote"><blockquote>MD5信息摘要算法（英语：MD5 Message-Digest Algorithm），一种被广泛使用的密码散列函数，可以产生出一个128位（16字节）的散列值（hash value），用于确保信息传输完整一致。<br>
<br>
<div align="right">——百度百科</div></blockquote></div><br>
咳咳，百科介绍，感觉我还是不明白，太抽象了（其实是介绍用的一系列名称我都不懂）。<br>
<br>
简单来说，MD5是每个文件都有的一个字符串，它的作用就是判断这个文件是不是原文件。<br>
<br>
比如，才哥通过邮件发给你一个文件A，同时用md5工具在本地获取了文件A的md5值也一并给你了；然后你收到邮件下载文件A到你的本地，接着用md5工具获取其md5值，发现是和才哥给你的md5值一样，那么文件A无误，反之，则你下载到本地的文件不是文件A。<br>
<br>
在日常工作中，可能有一些需要上传apk文件的地方会涉及到同时填写md5值做校验的情况。<br>
<br>
关于文件的md5值大家可以用Notepad++ 菜单栏中 工具—>md5—>从文件生成 来获取文件的md5值。<br>
<br>
<div align="center">
<img id="aimg_970169" aid="970169" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142352wqwrb8lvlpplt87z.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142352wqwrb8lvlpplt87z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142352wqwrb8lvlpplt87z.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">获取MD5值方式举例</font></font></div><br>
<strong>关于文件名</strong><br>
<br>
文件名就是字面意思，文件的名称。<br>
<br>
文件名可以自由重命名，它不影响什么。不过，在自己操作系统的同目录下不能出现同名文件哈。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_970170" aid="970170" zoomfile="https://di.gameres.com/attachment/forum/202104/02/142353fbtk8h2f2y8nnt2n.jpg" data-original="https://di.gameres.com/attachment/forum/202104/02/142353fbtk8h2f2y8nnt2n.jpg" width="168" inpost="1" src="https://di.gameres.com/attachment/forum/202104/02/142353fbtk8h2f2y8nnt2n.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">重命名文件名</font></font></div><br>
<strong>关于Appid</strong><br>
<br>
这个嘛，就是你在创建游戏应用的时候获取的参数，不再赘述。<br>
<br>
以上就是本次全部内容，主要关于游戏sdk的一些简单科普，以及一些我们在不同的开发者后台进行参数申请时的一些apk自身参数的意义介绍，希望能带给大家帮助！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：可以叫我才哥</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/cCMJ_XJPEfD-EquLCNCz5Q</font></font><br>
</td></tr></tbody></table>



  
</div>
            