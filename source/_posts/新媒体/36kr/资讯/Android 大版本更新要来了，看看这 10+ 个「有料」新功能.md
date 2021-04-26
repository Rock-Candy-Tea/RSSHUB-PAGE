
---
title: 'Android 大版本更新要来了，看看这 10+ 个「有料」新功能'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210426/v2_e99ba542d8544b1d89936a5e172a8829_img_000'
author: 36kr
comments: false
date: Mon, 26 Apr 2021 11:25:08 GMT
thumbnail: 'https://img.36krcdn.com/20210426/v2_e99ba542d8544b1d89936a5e172a8829_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/jWMo6ApiMCzmcgx8S4eVPw">“少数派”（ID:sspaime）</a>，作者：化学心情下2，36氪经授权发布。</p> 
<p>跳票一周之后，北京时间 4 月 22 日凌晨，第三个 Android 12 开发者预览版（以下简称 Android 12 DP3 或 DP3）终于发布。至此，Android 12 最后一个开发者预览版也已经面世，接下来等待我们的将是面向消费者的、适配更多 OEM 机型的 Beta 测试版本。</p> 
<p>距离 Beta 版公布的 I/O 21 只剩下不到一个月时间，而这次的 DP3 依然在系统主题和设计上持续发力，同时也为新世代 Android 设备提供了更多的原生 API 支持，可以说仍然「有料」。</p> 
<p>和往常一样，我们第一时间刷入了新系统尝鲜，如果你也对 DP3 中的新功能和新特性感兴趣，不妨跟随本文<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210422/v2_9d94d5f89e394f8082c3b500e50c340d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>来探索一番。</p> 
<h2>▍设计还在演进，更多圆角、更多动画</h2> 
<p>Android 12 的 UI 设计一直在改动，考虑到正在酝酿中的全新主题引擎，这些改动最终会将 Android 的视觉风格导向何方也让人格外期待。</p> 
<p>在这次的 Android 12 DP3 中，不少系统组件都迎来了一次「圆角化」翻新。</p> 
<p>比如应用快捷方式菜单、桌面长按菜单、文件夹背景甚至系统音量调节面板，都套上了一层弧度略显夸张的圆角。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,765" src="https://img.36krcdn.com/20210426/v2_e99ba542d8544b1d89936a5e172a8829_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">应用快捷方式、主屏长按菜单和音量调节</p> 
<p>类似的圆角同样也能在多任务卡片、设置弹窗等界面中看到：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1125" src="https://img.36krcdn.com/20210426/v2_55ef902532284a0cb4f86c83564bdba5_img_000" referrerpolicy="no-referrer"></p> 
<p>虽然现在整体效果似乎还是有那么一点奇怪，考虑到近两年手机屏幕圆角化已经是一个再明显不过的趋势，将系统进行圆角化处理的确能让手机在软硬件观感上变得更加协调统一。</p> 
<p>Android 12 DP3 还引入了一套应用启动闪屏 API。</p> 
<p>这一 API 的主要作用在于让应用在冷启动加载过程中都能用上基于应用图标的过渡动画。开发者可以通过 XML 文件来自定义在这一过程中显示的矢量图形以及图标背景。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1139" src="https://img.36krcdn.com/20210426/v2_4147c0c7ff274d08834b57bf3c34414c_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">适配说明 | 图：Google</p> 
<p>不过就 Android 12 DP3 来讲，目前大部分应用都尚未根据这一 API 做出适配，所以目前我们能看到的实际效果都不怎么协调。对于尚未适配的应用，有时甚至还会看到由不完整应用图标和应用内建闪屏组成的奇怪组合……</p> 
<p class="image-wrapper"><img data-img-size-val="1080,778" src="https://img.36krcdn.com/20210426/v2_d1f9bb9899bb4e0e8b9d0dc1601e8423_img_000" referrerpolicy="no-referrer"></p> 
<p>系统动画方面，Android 12 DP3 还对全局回弹动画进行了更新。在系统设置、应用菜单、下滑通知栏等操作中都能看到新的回弹动效，个人感觉比起之前的「戛然而止」要舒适不少。</p> 
<p class="image-wrapper"><img data-img-size-val="474,1000" src="https://img.36krcdn.com/20210426/v2_19af1b22fe1d490b845999f6bfc930a4_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">新的列表回弹动画</p> 
<p>更重要的是，因为这里更新的动画效果是系统级的，一些采用 Android 标准动画的第三方 App 也能因此用上新的回弹动画，比如 Spotify 在 Android 12 DP3 中的效果是这样的：</p> 
<p class="image-wrapper"><img data-img-size-val="332,700" src="https://img.36krcdn.com/20210426/v2_b7c0530954da4945939ad1408a0b21c4_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Spotify 等第三方应用也能用上新动画</p> 
<p>而到了通知中心在 DP3 中的改进，就不得不再次提到 Android 12 早前曝光的概念截图，其实当时已经出现过关于「通知计数」这一概念；直到 DP3，这一特性才正式加入。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,2280" src="https://img.36krcdn.com/20210426/v2_6c74770e6b724cdaba99c5366ad8bbd4_img_000" referrerpolicy="no-referrer"></p> 
<p>同时，通知中心在布局上还做了一些微调：比如取消了对话通知顶部的提示，但考虑到这反而与早先概念图设计有出入，所以这一改动最终是否会保留到 Android 12 正式版还有待观察。</p> 
<p>至于同样在 Android 12 发布之前就已经曝光的小部件菜单，在 DP3 中也朝着之前的曝光概念图更近一步，加入了搜索栏方便你直接输入关键字或是通过应用名称来找到对应的小部件。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1043" src="https://img.36krcdn.com/20210426/v2_26b9b102930b44c590f12ec03db76d89_img_000" referrerpolicy="no-referrer"></p> 
<p>说到小部件，可能 Google 也是受到隔壁 iOS14 更新的敲打，开始重新重视起了小部件的优化；在 DP3 中，小部件更是和系统 UI 的变化保持一致，为每一个小部件套上了圆角，让那些原本为更低版本 Android 系统适配的小部件看起来潮流了不少……</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1167" src="https://img.36krcdn.com/20210426/v2_915f1e4aee6546cc93171cf424264993_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">真的不打算整一个微件设计规范吗？</p> 
<h2>▍表情消息动起来，快速回复能贴图</h2> 
<p>UI 设计和动画上的变化之外，Android 12 DP3 就开发者层面带来的改进也有不少。</p> 
<p>应用待机存储分区（此前又叫「应用待机桶」）中新增了限制更大、后台资源消耗更小的受限（Restricted）级别；增加了更多的振动模式（如 low tick），同时还允许开发者通过 VibratorManager 分别控制、管理多个振动马达，共同营造出更为细腻、更有沉浸感的振动反馈体验；某些对触发时间要求特别精确的应用，在 Android 12 DP3 之后还必须申请一项新的「闹钟与提醒」权限，比如第三方闹钟应用、任务规划应用等等，相关设置目前可以在「应用 > 特殊权限」中找到。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1176" src="https://img.36krcdn.com/20210426/v2_0c780eee9ce64e658bcf4ae33de81f7a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">闹钟与提醒权限</p> 
<p>最重要的是，从 Android 12 DP3 开始，Google 为通知系统带来了 GIF 动图支持，并且快速回复也支持回复图片了。</p> 
<p>Android 12 DP3 开始，Google 为 MessagingStyle() 和 BigPictureStyle() 两种通知样式引入了动图支持，这两种通知类型其实往往也是通知中最常出现图片的地方，比如即时通信应用的消息对话，再比如带有封面预览的剧集上线提醒。</p> 
<p>动图支持自然就为这类通知带来了更加丰富的展示效果，聊天消息中的表情、截取自剧集预告的精彩片段，都能直接在通知中直接呈现出来 —— 与之对应的，以往只支持文本消息的通知快速回复功能，在 Android 12 DP3 中也支持插入图片了。</p> 
<p class="image-wrapper"><img data-img-size-val="452,799" src="https://img.36krcdn.com/20210426/v2_d000271a77bc499c8c242897f46e99ce_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">以后可以用类似的样式展示聊天中的动图表情了 | 图：Adobe Experience League</p> 
<p>这里还是要给大家泼一盆冷水：经过测试我们发现，不管是通知内容的动图支持还是通知快速回复的图片支持，都需要应用进行适配后才能启用。因此我们基本可以放心地推断，未来几年内是没有太大可能性看到那款绿色国民应用进行适配的 —— 毕竟它现在连通知快速回复都还没适配。</p> 
<p>另外，Pixel 机型独占的截图标注应用 Markup 不仅在设计上跟进了前文提到的圆角视觉风格，功能上也新增了文本标注的字体选项，偶尔用来做做水印还不错。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1176" src="https://img.36krcdn.com/20210426/v2_ff1268729df040b3b02d4220764962bf_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">截图标注工具与标注字体设置</p> 
<p>不过整体来看截图标注功能这一块 Google 相比 OEM 厂商还是落后了一大截，所以这一点只能算是 Google 在 Android 12 中对 Pixel 的一种补偿吧。</p> 
<h2>▍拥抱新技术，为新硬件带来系统级支持</h2> 
<p>厂商在硬件和技术上的迭代速度越来越快了，从超宽屏幕比例到多摄再到折叠屏设备，Android 系统也一直在通过提供原生接口的方式为这些不断涌现的新需求提供系统层面的支持。</p> 
<p>比如相机，在 Android 12 DP3 中，Google 一方面将 CameraX 资源库中的 供应商扩展 推向了整个 Android 平台生态，方便应用直接通过调用、适配 Camera2 的方式，在不同厂商的手机上获得对应的相机能力和更好的拍摄效果；另一方面还终于为近年来在智能手机相机上出场率越来越高的 Quad Bayer 四合一像素传感器提供了 API 支持。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,550" src="https://img.36krcdn.com/20210426/v2_4c7f38632f13458c969db7bbb49042f0_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Bayer vs. QuadBayer | 图：字节社的字节君</p> 
<p>当然，关于这一点我们也有一点额外的解读。</p> 
<p>要知道此前几个 Android 版本更新中相机方面的新技术支持和 API 更新几乎都与历代 Pixel 有关，比如景深信息支持、多摄支持等等，所以这次 Android 12 DP3 引入的四合一像素传感器原生 API 支持或许也在暗示一件事 —— Pixel 6 可能（终于）要换传感器了！</p> 
<p>再比如机器学习，Android 12 DP3 通过引入填充、栅格同步、执行对象重复利用等等机制进一步提高了 Neural Networks API 的执行效率，同时还将用于机器学习加速的相关驱动从 Android 平台更新中独立出来，使之可以借助 Play 服务进行更快、更灵活地迭代更新，不知道这些改进能否为 Android 带来更多借力 AI 的相关应用功能，比如 Android 用户期待了很久的<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>待办自然语义识别、熊猫吃短信等等。</p> 
<p>其他更新则是「查漏补缺」为主：目标 API 版本为 Android 12 及以上的应用终于能够像部分国产机型那样在息屏状态下调用 NFC 进行移动支付了；针对不同的文件类型、体积，开发者也能根据实际情况灵活声明应用数据的备份和恢复方式，比如利用更快、更省流量的设备间迁移（D2D）来传输大体积应用数据。</p> 
<p>最后，自 Android 3.0 时代开始就用于高负载图形任务处理的 RenderScript APIs 也从 Android 12 DP3 开始被正式弃用，但并非强制（只会发出提醒）。Google 此前也发布过一篇 博文 来介绍这件事，你可以简单理解为，Google 更希望今后在 Android 平台上的应用能够采用效率更高、更现代的跨平台图形接口来负责高负载图形任务，比如 Vulkan。</p> 
<p>以上便是本次 Android 12 DP3 更新中值得关注的新内容，总体来看，开发者相关的接口和功能更新都已经「铺设」完毕，新的界面风格和设计语言应该很快就会随 Android 12 一同亮相，就像当年随 Android L 一同亮相的 Material Design 一样。</p> 
<p>所以本次 Android 12 DP3 中照例也有不少值得关注的「隐藏内容」，如果你对这些内容感兴趣，也可以留意<a class="project-link" data-id="41920" data-name="少数派" data-logo="https://img.36krcdn.com/20200729/v2_78a1528084614b23a143f977064acb76_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/41920" target="_blank">少数派</a>的后续文章。</p>  
</div>
            