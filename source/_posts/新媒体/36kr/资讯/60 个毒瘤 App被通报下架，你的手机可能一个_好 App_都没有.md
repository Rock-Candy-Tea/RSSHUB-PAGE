
---
title: '60 个毒瘤 App被通报下架，你的手机可能一个_好 App_都没有'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://36kr.com/p/1173003306986887'
author: 36kr
comments: false
date: Thu, 08 Apr 2021 07:35:45 GMT
thumbnail: 'https://36kr.com/p/1173003306986887'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/dZQ_ZSTzp39r5nrqKKsLDw">“少数派”（ID:sspaime）</a>，作者：Clyde，36氪经授权发布。<span style="letter-spacing: 0px;">原标题：《工信部干掉了 60 个毒瘤 App，你的手机可能一个「好 App」都没有》</span></p> 
<p>4 月 6 日，国家工业和信息化部信息通信管理局再度出击，对 60 款存在侵害用户权益的 App 进行了 <a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s?__biz=MjM5OTUwMTc2OA==&mid=2650836808&idx=1&sn=8608f9d5b0b2a7cfe898dea45a9c6f68&scene=21#wechat_redirect">通报下架</a> 处理，当中不乏<a class="project-link" data-id="41920" data-name="少数派" data-logo="https://img.36krcdn.com/20200729/v2_78a1528084614b23a143f977064acb76_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/41920" target="_blank">少数派</a>读者熟悉的应用。</p> 
<p>在 Android、iOS 纷纷将隐私保护作为系统更新重点功能的大环境之下，国内相关监管部分、定制系统厂商、用户开发者和用户的多方共同努力，让减少「毒瘤」Android 应用这个愿景成为了可能。但规范个人隐私信息收集行为仅仅只是第一步 —— 那些我们装在手机里的、很多从未被通报过的应用算得上「<a class="project-link" data-id="45627" data-name="好应用" data-logo="https://img.36krcdn.com/20200729/v2_8b727ed76aed410899cedb00d18bc207_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/45627" target="_blank">好应用</a>」吗？从「又不是不能用」到「愉悦的使用体验」之间，国内常见的 Android 应用还有哪些地方可以改进？</p> 
<p>我们整理了 Android 应用设计和开发规范中与用户体验直接相关的部分内容，希望能够同时为用户和厂商提供一些参考。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://36kr.com/p/1173003306986887" referrerpolicy="no-referrer"></p> 
<h2>可广泛套用的图标样式</h2> 
<p>虽然仍有部分定制系统依然还在为用户提供可选选项，但基本可以确定的是，到了 2021 年，规则图标与异形图标之争已经有了明确的结果：从隔壁的 iOS 到 Android 阵营的各大定制系统，不管是 One UI、MIUI、ColorOS、EMUI、Flyme 甚至 Google 自家的 Pixel，都选择了形状风格统一的规则图标作为默认的图标样式。</p> 
<p class="image-wrapper"><img data-img-size-val="740,370" src="https://img.36krcdn.com/20210408/v2_8b7a7d81f4d6435992856f377562f564_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">异形图标的理想效果（左）与现实（右）</p> 
<p>问题在于，即便规则图标已经成为了主流，不同定制系统对于图标形状的具体实现方式仍有差异。比如三星 One UI 所采用的 Squircle 形状就在很多人心中留下了深刻的印象，以至于前段时间小米更新品牌 logo 后在手机上安装了<a class="project-link" data-id="109650" data-name="小米商城" data-logo="https://img.36krcdn.com/20210322/v2_6206f0843cb94d808e62d002493457e5_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/109650" target="_blank">小米商城</a> app 的人惊呼自己「早就见过了新设计」：</p> 
<p class="image-wrapper"><img data-img-size-val="508,339" src="https://img.36krcdn.com/20210408/v2_b9209d3d9b32423a8e85f33cb6292e7f_img_000" referrerpolicy="no-referrer"></p> 
<p>而即便同样采用了圆角矩形图标形状的 MIUI、ColorOS、Flyme 和 EMUI，它们各自的主屏观感也能让人很快将其一一区分开来 —— 图标设计风格是一方面，圆角矩形的 R 角、主体元素的视觉比重等等都各不相同。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1085" src="https://img.36krcdn.com/20210408/v2_94c1e00361554387b9c262330837ee8c_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">ColorOS 与 MIUI</p> 
<p>为了减少应用开发者面对上述不同定制系统启动器外观时，进行图标适配的难度，Google 在四年前引入了自适应图标规范。</p> 
<p>自适应图标是一套出发点和解决方案都极为巧妙的设计规范。它只需要开发者根据参考线、安全区域和图标尺寸提供前景和背景两套图层，就能根据不同 Android 设备的实际情况渲染出自然、风格统一的图标样式。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,817" src="https://img.36krcdn.com/20210408/v2_fafda454a39d44cda5b19e3a05420523_img_000" referrerpolicy="no-referrer"></p> 
<p>你可以将开发者准备的素材看作是食物原料，不同定制系统的启动器则是厂商为用户选择的容器。因此自适应图标既能给定制厂商选择容器形状的自由，又能保证用户不管选择什么品牌的 Android 机型，最终都能吃到开发者最初想要呈现的东西。</p> 
<p>遗憾的是时至今日很多应用都没有针对这一规范进行适配，一方面自适应图标作为一项设计规范从未被 Google 纳入任何形式的强制规范当中，另一方面厂商定制系统中各式各样的「应用图标重绘」机制也纵容了很多应用开发商（尤其是国内应用）直接照搬 iOS 版本图标设计的偷懒做法。</p> 
<p class="image-wrapper"><img data-img-size-val="591,1280" src="https://img.36krcdn.com/20210408/v2_ad48c6c430a741db8d2210d6b2fab7bb_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">没有适配的应用图标效果</p> 
<p>值得一提的是，尽管像 ColorOS 这样的定制系统连系统应用（比如上图中的软件商店）都没有针对自适应图标规范进行适配，但也有好的例子 —— MIUI 12.5</p> 
<p>但其实从我个人就少数派 Android/PWA 客户端、Teambition、<a class="project-link" data-id="8301" data-name="钉钉" data-logo="https://img.36krcdn.com/20210407/v2_7424fdc78ab44d4ab4d3a2b8c2d2abdc_img_000" data-refer-type="1" href="https://www.36dianping.com/space/2220121250" target="_blank">钉钉</a>等应用反馈经历来看，适配自适应图标并不是一件难事，难的是改变大家对于 Android 应用规范化适配的态度，大家不妨从让他们知道还有自适应图标这件事开始。</p> 
<h2>更适合全面屏的应用设计</h2> 
<p>从机械式结构到「刘海」再到各种位置的前置摄像头挖孔，近几年 Android 设备的演变几乎算得上是一部「前置摄像头为『屏占比』让路」的发展史（当然你也可以说「毫无发展」）。虽然对各种形式的「异形屏」评判标准也各不相同，但 Android 设备屏占比越来越高、全面屏手势方案也在 Google 的强制要求下成为「标配」。</p> 
<p>硬件形态和交互方式的变化也对应用设计做出了新的要求，如何保证一款应用在各类「全面屏」应用上都能拥有美观、现代化的使用体验？Google 从 Android 10 开始陆续提出了两点要求。</p> 
<p>首先是「边到边」适配。</p> 
<p>边到边，即 edge-to-edge，通过字面意义与 Android 系统界面层级的结合，我们就能理解这个设计理念的核心：将内容的上下边界进一步推开，实现对状态栏和导航栏区域的完整覆盖。</p> 
<p class="image-wrapper"><img data-img-size-val="600,810" src="https://img.36krcdn.com/20210408/v2_25e44830210c4abfa5d26f3ea27764d4_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">从传统设计到「边到边」 | 图：谷歌开发者</p> 
<p>上图很形象地展示了这种适配的直观效果，尤其 Google 还采用了旗下最具代表性的机型 Pixel 3 XL 来进行演示：在没有「边到边适配」这一概念之前，很多应用无法有效利用该机型「刘海」区域两侧的「小耳朵」进行内容展示，取而代之的是状态栏直接采用纯黑背景的粗暴做法，配合导航栏区域的纯黑背景，仿佛硬件厂商在「全面屏」设备上的努力一夜之间又被应用开发者给打回了「原形」。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,2000" src="https://img.36krcdn.com/20210408/v2_4dad8498990f4dc0bde4ac22169d85d7_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">在京东启动闪屏界面，使用异形屏和全面屏手势的用户可以体验到这样的效果</p> 
<p>具体到国内应用，目前大部分国内应用都能做到对状态栏区域的适配，以此充分利用各种异形屏的顶部边角区域；但导航栏区域的适配依然称得上是「重灾区」，如果你的系统没有像 ColorOS 那样直接干掉导航横条区域，那上图这样的黑条就处处可见。</p> 
<p class="image-wrapper"><img data-img-size-val="640,320" src="https://img.36krcdn.com/20210408/v2_42c954005866476c970d7e315758fe11_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">最顶级的边到边导航栏适配：动态颜色适配 | 图：谷歌开发者</p> 
<p>值得一提的是在这方面定制系统依然有通过「魔改」来为实际体验「擦屁股」的习惯，比如之前索尼、一加、MIUI 等等系统都用过的「纯色填充大法」—— 花了那么多时间来「重新发明」，最后基本上都因为没有考虑到暗色主题、色彩不协调等问题而取消掉了。</p> 
<p>实现边到边体验的另一个环节是逐帧键盘动画。不得不说这一点对于国内应用来说这实在是有些强求了（毕竟我们还有微信这种一心一意只用土制自制方案的「神级」产品存在），但大家仍然有必要了解一下。</p> 
<p>在 Android 11 以前，Android 系统的软键盘动画缺少必要的 API 来与应用窗口动画进行同步，这就导致进入、退出文本编辑状态时，应用本身的窗口速度和输入法键盘的弹出 / 收起速度不太一致；Android 11 通过新的 WindowInsetsAnimation 类的引入解决了这个问题，在进行边到边适配的基础之上，开发者可以进一步实现像 iOS 那样顺滑的、与应用界面动画同步的键盘动画了。</p> 
<p>具体效果可以参考下面这张对比图：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/20210408/v2_79f8db4d1ea94de7a3d24c81685cb59c_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Android 10 对比 Android 11 | 图：谷歌开发者</p> 
<p>对于即时通信、文本编辑类应用而言，软键盘动画是高频出现、能够直接影响使用体验的核心动画，尽管大部分应用开发商都还没有注意到这个需求，少数派多次推荐过的纯纯写作已经对其进行了适配，你可以在 MIUI、ColorOS、One UI 等等已经跟进了 Android 11 的主流定制系统中安装体验。</p> 
<h2>清晰、明确的通知分类</h2> 
<p>如果说 Android 有哪一点一定能让 iOS「自愧不如」，个人认为一定是通知系统的分类。</p> 
<p>和 iOS 在通知管理上的理念不同，Google 从 Android 8.0 开始为应用引入了通知分类这一特性，通过更细致的管理粒度，来帮助用户更灵活地管理通知。比如针对这一特性进行了适配的<a class="project-link" data-id="3969200" data-name="高德地图" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969200" target="_blank">高德地图</a>，我们可以通过 Android 系统的通知设置根据自己的实际需要自由组合、控制想要接收的通知类型，甚至为不同优先级别的通知设定不同的通知提醒方式：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,3522" src="https://img.36krcdn.com/20210408/v2_6b022f682f6f4908b1954df72dc675eb_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">高德地图的最初适配效果，提醒一下，它现在已经变了</p> 
<p>遗憾的是作为一项推出已经 5 年之久的特性，Google 也始终没有（其实也没办法）将通知分类作为一项强制规范在 Android 开发生态中进行推广。目前我们能够接触到的大部分国内应用中，有照搬 iOS 版本将通知分类做进应用内设置的，也有做了分类但不想用户使用于是在分类名称上玩起了「近义词辨析」游戏的。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,2412" src="https://img.36krcdn.com/20210408/v2_d41d4c6ede7649fb8b4f0b3282b7d331_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">「应用通知」是指的「消息」还是「其它通知」呢？</p> 
<p>所以我甚至希望 iOS 能够在接下来的版本更新中将这<a class="project-link" data-id="66837" data-name="个通" data-logo="https://img.36krcdn.com/20200729/v2_63b69181aa5a41369459fccdd8c272b3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/66837" target="_blank">个通</a>知分类理念拿过去「发扬光大」，就像当初的暗色模式一样。Google 在这类规范的落实和推广上依然缺少必要的影响力和号召力。</p> 
<h2>高效、省电的推送接入</h2> 
<p>如果说 iOS 有哪一点一定能让 Android「自愧不如」，个人认为一定是通知系统的推送。</p> 
<p>和 iOS 的 APNs（Apple Push Notification service）推送服务类似，Google 也有一套名为 FCM（过去叫 GCM）的消息推送服务。不过由于众所周知的原因 FCM 在国内长期处于不稳定甚至被滥用的状态，实际预装在国内 Android 设备当中的推送服务选哪个就成为了颇具「本土特色」的问题。</p> 
<p>一般来说，大厂通常会有选择地接入适合自己的推送服务，并且有选择地不接入部分推送服务；对于中小规模的开发团队而言，因为 app 享受不到微信那种系统级别的白名单特权，要保障推送及时、有效就得尽可能多地同时接入多<a class="project-link" data-id="7583" data-name="个推" data-logo="https://img.36krcdn.com/20210407/v2_444b921706ea4a089ab0d1ce55e9a43c_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4376601213" target="_blank">个推</a>送服务。</p> 
<p>当一个 APP 同时接入了三方推送（如极光推送、友盟等）、系统级别推送（小米、<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>、OPPO、<a class="project-link" data-id="25856" data-name="魅族" data-logo="https://img.36krcdn.com/20210302/v2_71b4978c1aa74523b46999ad0ed0ea04_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25856" target="_blank">魅族</a>等）后，自然就不能坚持「小而美」了：</p> 
<p class="image-wrapper"><img data-img-size-val="970,1051" src="https://img.36krcdn.com/20210408/v2_05b3a97e9d73469593dca6e9592265ef_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">从 OPPO 软件商店下载的京东就内置了两套推送服务</p> 
<p>正因为如此，我们才格外关注统一推送联盟这个挂靠在电信终端产业协会（TAF）下、由国家工业和信息化部业务指导的项目。统一推送联盟要实现的目标和字面上基本一致，即通过一套统一的推送服务，提高国内 Android 应用通知推送的及时性和可靠性，减少 app 开发者的通知推送适配难度。</p> 
<p>截至 2021 年 1 月，统一推送联盟取得的 <a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s?__biz=MzUyODQzNDgxMw==&mid=2247484287&idx=1&sn=2e77ca3e55a752c865225b299c5a28ea&scene=21#wechat_redirect">成效</a> 也值得肯定：包括联想、小米、华为、OPPO、vivo、一加、三星等国内主流 Android 厂商及其子品牌均已完成了对统一推送系统的接入；OPPO 等厂商的机型还因此获得了更加可靠的灾害预警服务「<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s?__biz=MzUyODQzNDgxMw==&mid=2247484281&idx=1&sn=ba7d98a4e76f9638e8597fb27c3b4685&scene=21#wechat_redirect">推必达</a>」。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,608" src="https://img.36krcdn.com/20210408/v2_000280acbdc94b80878a1f4a5b12317f_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图：统一推送联盟</p> 
<p>最后值得一提的是，工信部可以说是为国内 Android 体验操碎了心 —— 推送服务其实只是一套「组合拳」的开始，去年 10 月征求意见稿后不久，统一推送联盟还发布了《T-UPA0007-2020 统一推送消息分类及运营规范》，针对滥用通知进行营销、广告骚扰的行为进行进一步规范。</p> 
<p>希望不久后大家也能在通知分类这件事情上看到文章开头那样的新闻吧。</p> 
<h2>干净、清爽的文件存储方式</h2> 
<p>你想要的「沙盒」究竟还有多远？我们曾说 Android 11 是非常关键的一个版本，遗憾的是我们目前依然没有看到多少成效，不知道即将到来的 Android 12 能不能为此事最终画上一个圆满的句号。</p> 
<p>Android「系统级沙盒」对采用规范文件存储方式的应用来说其实影响并不算大，引用存储空间隔离应用开发者的介绍来说，因为在「沙盒」引入前的 Android 系统存储权限设计过于简单，许多应用（尤其是国内应用）都有滥用存储权限的行为，一旦用户因为正常使用需要授予了存储读写权限，它们就会在存储空间内部根据不同的需求随意存储和读写，全然不顾美观性和用户隐私安全。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1509" src="https://img.36krcdn.com/20210408/v2_85be1164105c4f6799c42750ab6f0ce3_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">你的 Android 内部存储空间应该大同小异 | 图：存储空间隔离</p> 
<p>为了避免可以用于用户标识共享的文件被用户删除，这些应用甚至会用具有迷惑性的文件命名来试图骗过用户。</p> 
<p>根据 Google 此前公布的计划，应用的 SDK 不能比当前主要 Android 版本低一个版本以上，即 2021 年上架 Play 商店应用的 SDK 版本不能低于 Android 11（SDK 30），所以今年新上架 Google Play 商店的应用应该都是已经适配过 Android 11 分区存储特性的。</p> 
<p>而就国内来说，目前已知适配了分区存储特性的国产应用依然不多，微信、QQ 等应用的适配效果也依然不够规范。希望今年第三季度发布的 Android 12 正式版能够真正成为了结这一痼疾的那把利刃吧。</p> 
<h2>全天候、全场景的视觉体验</h2> 
<p>在 iOS 和 Android 系统级的先后推广下，「暗色模式」开始在 2019 年流行起来。</p> 
<p>在 Android 中，Google 将「暗色模式」叫做「深色主题」。深色主题不仅是「夜猫子」用户对于夜间使用的长期诉求，对于大规模使用 OLED 屏幕材质的 Android 设备而言，同时也能起到提升设备续航的作用。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,544" src="https://img.36krcdn.com/20210408/v2_bd53746e70d846d9af020f6d251d8c42_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Google 自家应用在明 / 暗主题下的耗电对比 | 图：Google</p> 
<p>虽然出于无障碍考虑 Google 并不建议将深色主题简单理解为纯黑背景，很多应用至今仍然连「纯黑」都没有。考虑到连微信这种几乎不可撼动的「老油条」都在 Apple 的号召和用户的强烈诉求下进行了适配，至今还在深夜用白底黑字照亮你我面庞的应用被「点名批评」一下不过分吧（比如少数派在用的这一款协作工具）？</p> 
<h2>小结：适配了，然后呢？</h2> 
<p>作为少数派的 Android 编辑，在与很多客户对接、沟通产品体验的过程中我也发现，很多时候并不是厂商不希望自己的应用拥有更好的使用体验，而是负责相关体验的开发人员不了解、不重视这些细节。</p> 
<p>另一方面，定制系统确实也应该适当反思一下为不规范应用体验「擦屁股」的投入是否值得了，图标重绘、导航栏背景填色、强制暗色主题…… 这些做法大多数都不能从根本上解决问题，同时也需要投入大量的人力、财力进行重新开发，效果也远没有要求开发者遵循 Android 设计和开发规范那么好，可谓得不偿失。</p> 
<p>最后，上述特性适配了也并不意味着就一定很好，比如番茄免费小说，他们对应用快捷方式（App Shortcuts）这一特性的用途理解是：</p> 
<p class="image-wrapper"><img data-img-size-val="697,1100" src="https://img.36krcdn.com/20210408/v2_8031567a977b40178e3c85b1c4aa6566_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">该公司招聘要求变成了「文案简洁有力」大家有什么头绪吗？| 图：白徵明</p> 
<p class="image-wrapper"><img data-img-size-val src="https://36kr.com/p/1173003306986887" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://36kr.com/p/1173003306986887" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://36kr.com/p/1173003306986887" referrerpolicy="no-referrer"></p>  
</div>
            