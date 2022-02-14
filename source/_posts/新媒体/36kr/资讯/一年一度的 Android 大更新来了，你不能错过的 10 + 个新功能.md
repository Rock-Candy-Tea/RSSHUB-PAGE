
---
title: '一年一度的 Android 大更新来了，你不能错过的 10 + 个新功能'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220214/v2_5b9d30e2892e496ab8af85e18b4eab63_img_000'
author: 36kr
comments: false
date: Mon, 14 Feb 2022 06:44:37 GMT
thumbnail: 'https://img.36krcdn.com/20220214/v2_5b9d30e2892e496ab8af85e18b4eab63_img_000'
---

<div>   
<p>当部分 Pixel 用户还在纠结要不要试试面向大屏设备优化的 Android 12L Beta 时，Google 毫不客气地放出了 Android 13 首个开发者预览版本（以下简称 DP1）。</p> 
<p>作为开发者预览版本，比起 UI 上的变化 Android 13 DP1 更多地是向开发者展示即将在下一个版本中到来的新功能特性和 API 接口。比如主题图标 API、快速设置开关 API、系统相册选择器、独立应用语言设置等等。</p> 
<p>让我们<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>来看一看。</p> 
<h2><strong>测试版要提前了</strong></h2> 
<p>虽然首个开发者预览版放出的时间节点类似，但 Google 今年公布的 Android 13 整体更新规划和 Android 12 相比还是有些不同：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_5b9d30e2892e496ab8af85e18b4eab63_img_000" referrerpolicy="no-referrer"></p> 
<p>今年只会推出两个开发者预览版，第二个开发者预览版将在 3 月进行推送；</p> 
<p>测试版依然有四个，不过因为开发者预览版的减少，测试版的发布时间节点有所提前；</p> 
<p>正式版的发布日期待定。</p> 
<p>考虑到去年 Android 12 和 12L Beta 版的时间间隔不长，今年 Android 13 的正式版推送时间或许会早一点？</p> 
<h2><strong>Android 13 亮点更新</strong></h2> 
<h3><strong>单个应用的语言偏好</strong></h3> 
<p>你眼中的 Fall Out Boys、The Weeknd、Doja Cat，以往在那些系统语言为中文的 YouTube Music 用户眼中，则是打倒男孩、威肯和多杰猫 / 蜜桃朵加猫……因为不支持独立的应用语言设置，Android 版 YouTube Music 用户长久以来都只能忍受英文系统语言和应用内尴尬机翻二选一的情况。</p> 
<p>Android 13 终于补齐了这一缺憾。升级后，只需将手机连接至电脑然后通过 ADB 执行：</p> 
<p><strong>adb shell settings put global settings_app_language_selection true</strong></p> 
<p>即可在「系统 - 语言和输入法」设置中开启现阶段隐藏的「应用语言」选项；另外，开启后应用详情界面中也会多出一项直接设置应用运行语言的「语言」选项：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_ef788956bccd47cca69884dea889b0a2_img_000" referrerpolicy="no-referrer"></p> 
<p>初步体验下来，这个功能更像是一个「给了选项就能用」的存在，好在「虽迟但到」Google 终于在 2022 年给大家做了出来。如果应用本身没有提供应用内语言切换功能，也可以根据 Google 提供的 API 接口，简单适配后即可正常工作。</p> 
<h3><strong>Android 也有照片选择器</strong></h3> 
<p>尽管分区存储（也就是大家俗称的「沙盒」）机制的推进效果并不如人意，Android 13 还是在此基础上继续向 iOS 的文件管理体验靠拢。</p> 
<p>与 iOS 的「相册读取范围」类似，Android 13 也提供了一种无需授予完整媒体库访问权限即可开放特定照片或视频给第三方应用进行选取的新方案。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_5818c335c27c453ca56d590b1c707054_img_000" referrerpolicy="no-referrer"></p> 
<p>值得注意的是，尽管 Google 表示照片选择器是访问用户照片与视频的推荐方式，<strong>但目前在 DP1 阶段它的使用并非强制</strong>。运行在 Android 13 DP1 上的应用依然可以申请文件读写权限然后采用传统的方式访问存储目录。</p> 
<h3><strong>主题图标开放给第三方</strong></h3> 
<p>在 Android 12 中引入 Material You 的同时，Google 也为自家 Pixel 设备引入过一套基于壁纸动态取色的主题图标系统。这套系统能够抽取应用图标 logo 的主要特征，然后以更加贴合桌面色彩主题的样式重新呈现在启动器上，但此前仅适用于 Google 应用和 Pixel Launcher，在实际使用过程中一旦与第三方应用「混搭」观感就会大打折扣。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_618be28e8bd44488b1b0822d640309ea_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">实际使用往往就是这种观感</p> 
<p>为此，Google 在 Android 13 中将主题图标功能开放给了第三方应用开发者。开发者只需要提供满足特性尺寸和格式要求的、用于色彩绘制的单色图标素材，并在进行相关声明，即可让应用在 Pixel 启动器中调用 Material You 动态色彩渲染图标。这些单色图标素材同样也可以在状态栏通知图标中进行复用。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_b5a735af10e44e2cb7d058f46899860b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">单色主题图标尺寸规范示意图</p> 
<p>由于相关细节是在 <adaptive-icon>元素中进行声明的，<strong>已经适配了自适应图标的应用跟进起来应该会比较容易</strong>。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_5aa08f1459b6413a8d3ab52ad5f89b91_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>添加快速设置开关更容易</strong></h3> 
<p>Android 上的快速设置开关跟好用，快速设置开关的编辑过程却很让人头疼，尤其当快速设置开关太多，排列时需要跨显示区域上下拖动时。</p> 
<p>Android 13 引入了一套新的 tile placement API，开发者接入后可以让应用直接通过弹窗的方式方便用户将对应的快速设置开关添加至快速设置开关面板当中。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_bfb465e849634323969bcfd9ec395f3a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">快速设置开关添加提示面板示意图</p> 
<h3><strong>无需获取定位的附近 Wi-Fi 权限</strong></h3> 
<p>Android 今年推出了不少针对权限管理的完善和优化，但依然有不少相对粗糙的地方。在 Android 13 中，Google 为管理设备与周围 Wi-Fi 热点连接的应用专门添加了一个名为 NEARBY_WIFI_DEVICES 的运行时权限，调用这一权限后应用可以借助 Wi-Fi 来扫描并连接附近的设备，同时无需申请精确位置权限。在智能家居、物联网设备配置的过程中使用这个权限可以避免对用户位置信息的不必要请求。</p> 
<p>不过这一权限目前也是非强制性的，在 Google 的描述中，以 Android 13 为目标平台的应用可以通过 neverForLocation 属性来申请 NEARBY_WIFI_DEVICES 权限，「有助于促进隐私友好的应用设计」。因此对那些从来不把用户隐私放在心上的应用来说，这个权限可能又要被冷藏了。</p> 
<h2><strong>其它值得一提的内容</strong></h2> 
<h3><strong>更多系统功能加入 Project Mainline</strong></h3> 
<p>Google 在 Android 10 中引入的 Project Mainline 还在进化。在 Android 13 中，Google 不仅将蓝牙功能堆栈和超宽频通信功能堆栈作为新的模块加入了 Mainline 当中，上面提到的照片选择器以及新版 OpenJDK 11 也都有望在 Project Mainline 的帮助下、通过 Google Play 系统更新推送给旧设备。</p> 
<p>关联阅读：<a href="https://36kr.com/p/1614492411218697">译文 | 关于 Android Q 背后的新变化，我们和谷歌开发团队聊了聊</a></p> 
<h3><strong>媒体输出控制面板重新设计</strong></h3> 
<p>调节输出设备和对应音量更方便了，但目前在深色主题下可读性有点差。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_60cf51846ada4e2d8b1503186eabc60b_img_000" referrerpolicy="no-referrer"></p> 
<h3>媒体播放控制卡片布局调整</h3> 
<p>Google 今年似乎还想调整一下媒体播放控制卡片的设计，目前可以通过隐藏开关开启的样式移除了媒体封面并且加上了播放进度条控制，整体布局也有很大的变化：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_caf66569ae324f7381347a2d9762b0ed_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">新的媒体播放控制卡片样式 | 图：esper.io</p> 
<p>不过熟悉 Android 12 / 11 早期 DP / Beta 测试的读者，或许看到这里也都对这种改变提不起太多兴趣了：因为这个阶段 Android 往往会对 UI 进行各种测试，反映到系统中就是 UI 控件设计左右横跳，与最终版本差距甚远，是真正的「请以最终版本为准」，</p> 
<h3><strong>更多 Material You 风格界面</strong></h3> 
<p>比如运行时权限弹窗的操作按钮、弹窗菜单的操作按钮等等。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_dbb69c54489a43c7a951560accbf8734_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>通知使用权授予细节更清晰</strong></h3> 
<p>在 Android 12 中就有的通知使用权细分，在 Android 13 DP1 的弹窗提示中有了更明确的注释。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_bab9fbb82e364264bae105fccc8692e8_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>能否发出通知或需授权</strong></h3> 
<p>应用权限管理界面中，「不允许」一栏下多了「通知」这一选项，但目前实际跳转界面为应用通知管理界面。后续应该会有相应的功能和接口更新：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_861532d8463747ec8d6f2968f2e1cb3e_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>快捷设置卡片与二维码扫描</strong></h3> 
<p>在 Android 12 中新加入的单手模式以及颜色校正功能，在 Android 13 DP1 中新增了快捷设置卡片。另外之前在相关的曝光中就已经出现过的原生 QR 二维码扫描器功能，在 DP1 中也以卡片的形式加入（之前的曝光中还展示过加入锁屏界面的二维码扫描功能）不过目前这个卡片在 DP1 中还无法正常开启使用。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_560b3b5d83cf4b90a453b8bbe29161fd_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>快速轻触手势支持开启手电筒</strong></h3> 
<p>在 Pixel 5 以及之后发布的机型中加入的快速轻触，即敲击机身快速开启应用/控制功能的设置项。本次在 Android 13 中加入了闪光灯开启功能，为这个常用的功能增加了一种更快速启动方式。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_9b86e89435054131b03465a6d4fcba92_img_000" referrerpolicy="no-referrer"></p> 
<h3><strong>大量针对大屏设备的功能和交互优化</strong></h3> 
<p>除了大部分可以直接开启或看到的变化，Android 13 DP1 也包含了众多针对平板等大屏设备以及多用户使用场景的隐藏功能，比如锁屏 UI 支持横屏显示、可以直接在锁屏界面切换用户、可以更方便地向其它用户安装应用等等。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_acedb95e7a6e4b5592238628388ee03d_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">锁屏界面的用户切换入口 | 图：esper.io</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_58ca715695ac4a2cab7c050daa929c37_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">更方便地安装应用到其它用户 | 图：esper.io</p> 
<p>另外还有一些从 Android 12L 继承而来的内容。</p> 
<p>比如进入多任务界面后，分屏操作现在叫「上分屏」，分屏后，被分屏的应用之间还有与设备屏幕物理圆角相对应的圆角分隔设计；分屏时切换到多任务界面，会发现被分屏的应用以「组」的形式保留在同一张应用卡片上：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_9a1c78d1c6c04d1ea33977b2b3b9248a_img_000" referrerpolicy="no-referrer"></p> 
<p>再比如如果在画中画状态下打开其他应用，画中画窗口上也会出现一个「上分屏」选项，点击就能直接将正在播放的视频和刚刚打开应用以分屏状态显示。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_b7cde8b31c3345f2ab8eaa7d1759223f_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>小结：Google 的「组合拳」</strong></h2> 
<p>去年 Android 12 正式版发布之后没过多久，Google 便着手开始另一项 Beta 测试计划 —— 即 Android 12L 的开发者预览版计划发布。</p> 
<p>虽然 Android 12L 有着独立的 API 版本号，但从目前的节奏来看并未影响到主线 Android 13 测试计划的更新。而现在 Android 12L 正式版即将推送，尚处于早期的 Android 13 还有很长一段时间继续测试各种新功能。在 Android 13 DP1 中，我们则已经看到了很多 12L 中的功能被直接整合进来。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_f1ebd0ba8de54eafaee0a16cebbb8d64_img_000" referrerpolicy="no-referrer"></p> 
<p>从现在的角度来看，Android 12 不仅是测试周期跨度最长的一次大版本号更新，在主题引擎实现、隐私保护、以及小组件系统等很多「感知很强」的部分也做出了重大改变，为了不让这些改变显得曲高和寡，Google 接下来有个很重要的任务，就是如何推动第三方 Android 定制系统以及开发者们去实际应用。</p> 
<p>可以预见的是 Android 13 在本文介绍的功能基础上或许不会带来太多额外惊喜。Google 更多地会在已经奠定好的基础部分上进一步完善现有功能。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_d65fb93d44cf4b85a90947e656ae1eaf_img_000" referrerpolicy="no-referrer"></p> 
<p>从整个时间线上来看，在 Android 12 之后还有另一个同样重要的「大事件」：那就是被称为「组合拳」的 CES 2022 一系列动态。Google 在 CES 2022 上宣布了一系列改进，不仅包括现有 Fast Pair 快速配对系统对智能家居设备的支持，还有在 ChromeOS、Windows 两大桌面端系统与 Android 协作功能上的更新。</p> 
<p>在此之前的种种 Android 13 爆料与代码提交，也都透露过借助 UWB 超宽频、蓝牙、NFC 等技术让泛 Android 生态圈中的各种设备紧密连接的设计方案：类似「接力」的功能将加入 ChromeOS，对 Google 来讲相对不那么「自家」的 Windows 11 也将通过软件的方式加入 Nearby Share 以及 Fast Pair 的支持；剪贴板同步、耳机自动切换设备这些也都是会在 2022 年加入的功能。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_830e539a6c054fa8bffbbbabacad18a7_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220214/v2_d3266dcf14a04c1782badfe4fe75974a_img_000" referrerpolicy="no-referrer"></p> 
<p>整个泛 Android 生态的进化自然也离不开 Android 的加入，因此在「小修小补」的表面之下，「更紧密的生态协作」很可能是接下来一整年中，Android 13 的更新重点。毕竟在 DP1 中我们能够看到「真东西」向来不多，值得期待的好菜或许还在后面。</p> 
<h3>原文链接：</h3> 
<p>https://sspai.com/post/71407?utm_source=wechat&utm_medium=social</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247530628&idx=1&sn=ee5a0f7855abfa54ff0a5f56b514e584&chksm=fdb38deecac404f8f40e3800a035981a5939c8e4405735df39ea90d5156261387098dba466bb#rd">“少数派”（ID：sspaime）</a>，作者：克莱德，36氪经授权发布。</p>  
</div>
            