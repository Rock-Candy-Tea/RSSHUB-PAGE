
---
title: '下载应用这件事，Play 商店为什么比国内软件商店更好？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/05/jhyLHF2g1chuYmjZyPEo.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 27 May 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/05/jhyLHF2g1chuYmjZyPEo.jpg'
---

<div>   
<blockquote><p>编辑导语：总会看到Google Play上有好多好用的App，同一款应用Play版更好的说法是Android圈的都市传说？为什么国产应用在 Play 商店中正变得越来越少了？本篇文章作者将为你详细解答。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-812673 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/jhyLHF2g1chuYmjZyPEo.jpg" alt referrerpolicy="no-referrer"></p>
<p>对有一定经验的 Android 玩家来说，在下载 App 这件事情上，Play 商店依然是那个值得排除万难、能上就上的选择，没有之一。坊间还流传着各种关于「Play 版」应用的传闻：Play 版应用有 FCM 推送、Play 版应用更省电、Play 版应用没广告、Play 版应用有更适合现代设备的 64 位版本……</p>
<p>今天这篇文章，我们从一个对普通用户而言可能会有点陌生的概念——目标 API 级别入手，希望能为你解答上面所提到的一部分问题。</p>
<h2 id="toc-1"><strong>一、</strong><strong>Android 有几种写法？</strong></h2>
<p>对 Android 系统而言，同一个系统版本一般都对应了不止一种名称，比如对消费者而言 Android 12 是 Android 12，或者根据 Google 按照字母表顺序命名的习惯叫做 Android S；而如果 2019 年 Google 没有官宣取消甜品代号命名方式，Android 12 的甜品代号Snow Cone应该也会更加为大众所熟知。</p>
<p>针对开发者，每个 Android 版本还会被分配到一个唯一的整数标识符，这个整数标识符就是 API 级别。针对这些不同的命名方式，GitHub 上也有人做了一个清晰明了的网站，有兴趣的朋友可以去看看。</p>
<p>从网站提供的表格不难看出，和一个甜品代号可以对应多个 Android 版本不同——比如 Android 7.0 和 Android 7.1 都可以叫「牛轧糖」——<strong>API 级别和 Android 版本是严格对应的</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="下载应用这件事，Play 商店为什么比国内软件商店更好？" src="https://image.yunyingpai.com/wp/2022/05/3kWgfp7CIPk6tTGVE2u6.png" alt="下载应用这件事，Play 商店为什么比国内软件商店更好？" width="400" height="360" referrerpolicy="no-referrer"></p>
<p>API 级别 32 只可能对应 Android 12L，Android 12L 的 API 级别也只能是 32。对于市面上运行系统版本千差万别的 Android 设备而言（你同样可以在上面那个网站中看到不同 Android 版本的累计用户占比），API 级别也成为了开发者辨别用户系统版本和应用运行环境、保证应用兼容性的重要参考。具体而言：</p>
<ul class="list-paddingleft-1">
<li>最低 API 级别：代表了应用可以运行的最低系统版本。如果一款应用的最低 API 级别为 28，那么这款应用只能保证在 Android 9 及以上系统版本中的兼容性</li>
<li>目标 API 级别：代表了应用被设计用于运行的系统版本。如果一款应用的目标 API 级别为 32，则代表这款应用被设计用于在 Android 12L 中运行，因此也理所当然地支持 Android 12L 引入的新特性</li>
</ul>
<h2 id="toc-2"><strong>二、</strong><strong>目标 API 级别与体验</strong></h2>
<p>聊完概念我们再来聊聊现象。即便不谈应用商店本身的使用体验，在能不能下到好应用这一核心需求上，Google Play 和各种国内应用商店都有着天壤之别。</p>
<p>对国内应用商店而言，兼容各种鱼龙混杂、质量参差不齐的应用才是头等大事。毕竟为了赚钱，大部分 Android 设备默认的应用商店也都是自家的，如果用户发现某个应用无法正常运行，即便这个应用本身做得非常糟糕，他们往往也会将「锅」扔给手机厂商。</p>
<p>一传十十传百，这家厂商的手机在这位朋友的圈子里就会被打上「不推荐」的评级。Google Play 商店不一样。在更广泛的 Android 生态里，大多数 Android 设备都会搭载 GMS 套件、不同厂商的 Android 设备也能从同一个 Google Play 商店中获取应用。</p>
<p>因此 Play 商店作为由 Google 直接控制的应用商店，需要做好的就是平台本身：如何规范应用行为、如何保证设备安全、如何进行高效分发……相对而言，Google 的地位也更加主动一点，如果某款 Play 商店的应用无法正常运行，用户只会将责任归咎于手机和手机系统本身，或是在商店里留个一星差评骂骂开发者。</p>
<p>解决方案藏在目标 API 级别这个概念里。通过读取应用开发者为应用声明的 <strong>targetSdkVersion</strong> 清单属性，Android 系统得以判断这款应用的目标 API 级别是多少，进而确定哪些新特性可以在这款应用中启用、哪些特性则需要做适当的兼容处理。</p>
<p>以前几年大家热切期盼的「沙盒」机制分区存储为例，应用必须首先通过清单属性告诉 Android 系统「我的目标 API 级别是 30，是支持最新特性的好应用」，系统在读取到这一声明后才会为应用启用分区存储机制；而对当时需要时间过渡的应用而言，它们在告诉系统自己的目标 API 级别不够 30 之后，系统则不会为这些应用启用「沙盒」机制。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="下载应用这件事，Play 商店为什么比国内软件商店更好？" src="https://image.yunyingpai.com/wp/2022/05/Epzl2MGHuqjYeokYHfdn.png" alt="下载应用这件事，Play 商店为什么比国内软件商店更好？" width="400" height="330" referrerpolicy="no-referrer"></p>
<p>所以在 Android 开发者网站所列出的各种 API 接口、声明数值、字符串等信息旁，也都会有一行小字说明这个功能是在哪一个 API 级别中所加入的；</p>
<p>在 Android 13 的介绍中，Google 也有一个专门的页面来说明目标 API 级别在 Android 13 及以上（另一种说法是「以 Android 13 或更高版本为目标平台」）的应用将受到哪些行为变更影响。</p>
<h2 id="toc-3"><strong>三、两年为期、相对严格</strong></h2>
<p>我们可以将 2017 年看作是 Google 开始着手治理 Android 系统「碎片化」问题的开始，这一年，Android 系统本身引入了著名的Project Treble，让那些有开发实力的团队在系统大版本更新这件事情上直接转入了「快车道」。</p>
<p>但系统更新仅仅是一方面，系统更新带来的各种新功能，除了手机厂商的配合，还是需要应用开发者这边积极响应，才能将 Google 所预想的 Android 体验带到用户手中。</p>
<p>因此也是在 2017 年，Google 开始通过 Play 商店对 Android 应用的最终体验进行干预，首先在 64 位应用支持这件事情上开始了筹备。2021 年 8 月，经过四年多的筹备和过渡，Play 商店中的所有应用都具备了向 64 位设备提供对应支持的能力。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="下载应用这件事，Play 商店为什么比国内软件商店更好？" src="https://image.yunyingpai.com/wp/2022/05/9kWgmub4jzew6By8U08O.png" alt="下载应用这件事，Play 商店为什么比国内软件商店更好？" width="401" height="226" referrerpolicy="no-referrer"></p>
<p>同时，近几年 Play 商店在 API 级别上的规范也逐渐成型。<strong>总体而言，对于那些需要在 Play 商店中持续提供更新的大部分应用，Google Play 商店一般会提供一年左右的时间来让开发者针对最新的目标 API 级别进行适配。</strong></p>
<p>这里 Play 商店将应用分成了三类：新应用、应用更新和现有应用，新应用指此前从未在 Play 商店发布过的应用，应用更新指已经在 Play 商店上架的应用所提供的更新版本，现有应用则对应那些已经发布在 Play 商店、但并不提供任何更新的应用。</p>
<p>举个例子，Android 11 正式版发布于 2020 年 9 月，目前 Google Play 管理中心的要求是：</p>
<ol class="list-paddingleft-1">
<li>2021 年 8 月 2 日之后，新应用必须将目标 API 级别设置为对应的 API 级别 30；</li>
<li>2021 年 11 月 1 日之后，应用更新必须将 API 级别设置为对应的 API 级别 30；</li>
<li>2022 年 11 月 1 日之后，现有应用必须将目标 API 级别设置为对应的 API 级别 30。</li>
</ol>
<p>如此一来，新应用开发和现有应用针对新版本系统特性跟进适配的窗口时间，便被控制在了系统更新后的一年左右时间内。</p>
<p>至于那些妄图通过不提供应用更新保留 Play 商店上架状态的应用，上述限制的存在也有一定的限制作用：2022 年 11 月 1 日之后，如果你的手机已经升级到了 Android 11 及以上系统版本，那些目标 API 级别低于 30 的应用就不会出现在 Play 商店的页面和搜索结果当中了。</p>
<p>我们姑且以「Play 商店中能否搜到」这个行为为前提，对应 Android 版本和 API 级别，梳理一下最近一段时间内 Play 版应用将会提供的一些体验。在 2022 年 11 月 1 日后：所有能在 Play 商店中下载到的应用，都将提供分区存储（也就是「沙盒」）机制支持。在数月未使用的情况下，已经授予的运行时敏感权限都会被系统自动重置；</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="下载应用这件事，Play 商店为什么比国内软件商店更好？" src="https://image.yunyingpai.com/wp/2022/05/I6wgiYFD38IfxhURX05W.png" alt="下载应用这件事，Play 商店为什么比国内软件商店更好？" width="601" height="642" referrerpolicy="no-referrer"></p>
<p>申请位置信息访问权限时，最高都只能申请到「仅在使用中允许」，「总是允许」只能在系统设置中手动开启；查询设备上已安装应用的列表时，则只能获取到系统过滤后的已安装应用列表。</p>
<p>另外，2022 年 11 月 1 日后，此前已上架应用的新版本都将支持<strong>Android 12 的新特性</strong>，比如自定义通知布局、应用休眠、传感器采样率限制、前台服务启动限制、更快的通知操作响应速度（trampoline 优化）。</p>
<h2 id="toc-4"><strong>四、国内还停留在三年前</strong></h2>
<p>如果用一句话从用户角度去概括本文第三部分的所有内容，那应该是：</p>
<p>在 Android 11 正式版发布两年后，所有 Play 商店中能够搜到的应用，无一例外都是支持 Android 11 新特性的。</p>
<p>所以我们说 Play 商店在目标 API 级别要求上的「严格」，其实也是一种相对而言的说法。<strong>因为国内主流应用商店在目标 API 级别的要求普遍还停留在 3 年前</strong>。</p>
<p>2018 年 7 月，电信终端产业协会（TAF）发布了一份《移动应用软件高API等级预置与分发自律公约》，这份公约由 OPPO、华为、百度、360、阿里、小米、vivo、腾讯发起，要求自 2019 年 5 月 1 日起，新上架和预置应用的目标 API 级别为 26 及以上，自 2019 年 8 月 1 日起，现有应用的更新则必须以目标 API 级别 26 及以上进行开发。</p>
<p>目标 API 级别 26 对应的版本是 Android 8.0，Android 8.0 的正式版发布时间是 2017 年 8 月。彼时的国内主流应用商店，还能给出一份与 Google Play 商店节奏一致的目标 API 级别要求。</p>
<p>不知道是电信终端产业协会后续在这方面没有持续跟进，还是 Google 在 2020 年的 Android 11 正式版中引入的分区存储机制过于激进，国内应用商店在目标 API 级别要求这件事情上自那之后便陷入了停滞。</p>
<p>目前，我们在 OPPO、小米等厂商的相关开发者文档中，能够检索到的目标 API 级别相关要求大多数都与三年前那份《移动应用软件高API等级预置与分发自律公约》有关。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="下载应用这件事，Play 商店为什么比国内软件商店更好？" src="https://image.yunyingpai.com/wp/2022/05/qMBIFl4wAR0Fo23euxyy.jpeg" alt="下载应用这件事，Play 商店为什么比国内软件商店更好？" width="401" height="860" referrerpolicy="no-referrer"></p>
<p>我所使用的设备上所安装应用的目标 API 级别统计换句话说，以五年前 Android 8.0 系统体验为基础的应用，依然存在于 2022 年的国内应用商店中。至于数量有多少，你可以下载 AppChecker 这类应用自行检查。</p>
<p>与 Play 商店实际仍有些保守的做法相比，国内应用商店还有更长的路要走，甚至应该先从态度上重视起来——比起最近在 64 位应用这件事情上的被动应战，国内应用商店、尤其是已经有着相当大影响力和号召力的 O、V、华、米几家国内应用商店，应该主动拥抱的「优秀品质」还有不少，与时俱进的目标 API 级别要求可以是其中之一。</p>
<p> </p>
<p>作者：克莱德</p>
<p>原文链接：https://sspai.com/post/73356?utm_source=wechat&utm_medium=social</p>
<p>本文由 @克莱德 授权发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
                      
</div>
            