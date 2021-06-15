
---
title: 'Android 12 Beta 2 更新详解：更好看的主题和动画，原生「照明弹」上线'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210615/v2_df585567a0eb487faa65e50a2d77604c_img_000'
author: 36kr
comments: false
date: Tue, 15 Jun 2021 06:56:14 GMT
thumbnail: 'https://img.36krcdn.com/20210615/v2_df585567a0eb487faa65e50a2d77604c_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/frKTqWY-fcUAZjYmEd5NGw">“少数派”（ID:sspaime）</a>，作者：Clyde，36氪经授权发布。原标题：</p> 
<p>尽管此前 Google 在 I/O 2021 Keynote 上公布了大量 Android 12 的设计和功能细节，彼时放出的 Beta 1 完成度依然有限。由于很多功能都未实装，很多参与测试的开发者和用户甚至都为 Android 12 最终正式版能够实现多少功能捏了一把汗。</p> 
<p>这种担忧很快便<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了排解 —— 6 月 10 日凌晨，Google 向自家的 Pixel 设备正式推送 Android 12 第 2 个测试版本（以下简称 Beta 2），相比此前的开发者预览版和首个公开测试版本，Beta 2 终于将那些大家期待已久的功能和设计下放到了 Pixel 设备上，我们也得以在实际设备上一睹 Android 12 的完整面貌。</p> 
<p>让我们照例对这次的 Beta 2 来一次完整梳理吧。</p> 
<h2 label="一级标题" style>覆盖到图标的多彩主题</h2> 
<p>Material Design 迎来了自 2014 年面世以来最大的一次更新 —— Material You，和当年的一样，这套新的设计语言也将在 Android 12 中得到应用。</p> 
<p>具体而言，Google 基于色彩科学、交互设计与工程学设计了一套壁纸取色算法，在 Android 12 Beta 2 中，以这套算法为核心的主题系统也正式<a class="project-link" data-id="187722" data-name="上线了" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/187722" target="_blank">上线了</a>。我们在更换壁纸的同时，Android 12 Beta 2 也会从壁纸中进行取色，目前最新的一种说法是，这里至少会提取 2 种色调、最多 6 种不同色彩（这组数字来源于 Arstechnica 编辑 Ron Amadeo）。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_df585567a0eb487faa65e50a2d77604c_img_000" data-img-size-val="1080,788" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>基于壁纸的取色系统</p> 
<p>这些色彩的应用范围可谓广阔，目前我们可以从 Beta 2 中观察到的有：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>锁屏的时间字体、PIN 码键盘</p></li> 
 <li><p>快速设置面板中的开关和下方的媒体播放卡片</p></li> 
 <li><p>通知中心以及采用标准 Android 通知图标设计样式的通知小图标</p></li> 
 <li><p>解锁、充电等动画的动画效果</p></li> 
 <li><p>系统设置中的部分控件，比如开关</p></li> 
</ul> 
<p>除此之外，根据 Google 的设计构想，这套基于色彩主题系统也会影响第三方应用的配色，目前在 Beta 2 中可以观察到的除了部分采用系统默认样式的自适应图标能够跟随变色外，Gboard Beta 版本通过对配置文件的简单修改也能应用主题色彩。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_509ed280590b4ede9afc50b4b3660f0b_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>自适应图标与 Gboard 键盘也能覆盖</p> 
<p>事实上不少 Google 应用已经在悄悄进行适配了，除了应用内的界面配色，启动器中对应的应用图标甚至也在这套配色系统的覆盖范围内。以下是著名开发者 kdrag0n 成功开启相关功能后提供的截图，从图中可以看出，Android 12 甚至会根据系统深色主题的开关状态选择不同的配色。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_a2f4ed2fcb9545d1abc413a4998c483b_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>应用图标甚至也能应用主题色 | 图：kdrag0n</p> 
<h2 label="一级标题" style>贯穿锁屏与主屏的呼吸感</h2> 
<p>此前 Google 在介绍 Android 12 的系统动画改进时，曾用「能够相互感知」这样的描述来强调过系统控件之间的动画联系。而随着 Beta 2 的上线和大量新动画的加入，这样的细节也越来越多，让 Android 12 整体给人的「呼吸感」更为强烈。</p> 
<p>比如此前我们已经提到过的锁屏。</p> 
<p>按下电源键锁屏时，屏幕内容会从四周向电源键所在位置「熄灭」，如果使用电源键解锁，屏幕会从刚好相反的路径进行点<a class="project-link" data-id="328832" data-name="亮屏" data-logo="https://img.36krcdn.com/20201107/v2_6f0810abbad341819bd7b5c6b3dcd604_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/328832" target="_blank">亮屏</a>幕，如果你在设置中开启了「拿起手机即显示（Lift to check phone）」这个功能，点亮动画的初始位置则是屏幕底部。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_c019e86fea8842a8a53712f3a96e3303_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>通过电源键锁屏、点亮屏幕的动画效果</p> 
<p>借助 Roboto VF 可变字体，在 AOD 和锁屏之间转换时，时间字体的粗细也会自动变化；此外对通过人脸识别解锁的 Pixel 4 系列来说，成功解锁进入主屏的同时还会有一个从屏幕顶部传感器区域向下扩散的波纹动画。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_572ac47b1dbe48468c26572cbf4eafa8_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>拿起手机并通过人脸解锁的动画效果</p> 
<p>来到主屏。</p> 
<p>Pixel Launcher 在 Beta 2 中虽然看上去没太大变化，但出现极为高频的桌面弹出菜单，包括应用快捷方式（App Shortcuts）和长按菜单都换上了更加符合操作直觉的展开动画：如果图标在屏幕下方，应用快捷方式菜单会自下往上以非线性动画的方式呈现；长按屏幕上半部分时，启动器菜单则会自上而下展开。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_459f4ea2fcee4c9a94da018a302fad9a_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>桌面菜单的动画效果</p> 
<p>除了动画，Pixel Launcher 在 Beta 2 中还通过提高视觉对比度的方式来营造另一种「呼吸感」：概览小组件和主屏文本标签都采用了更粗的 Google Sans 字体，极具品牌辨识度的同时也让时间天气、应用名称等主屏信息更易阅读；但同时又通过去除 Z 轴层级感的方式，来将整个桌面「拍扁」——主屏与应用抽屉之间的转换动画变成了渐隐效果的淡入淡出，所有应用图标统一去除边缘阴影，无论在主屏还是应用抽屉内视觉效果都更和谐了。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_0b9cab437be24aec9855bb79c4ee9efa_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>字体更粗、图标阴影被去除（自带阴影的除外）</p> 
<p>最后，整理桌面内容时，图标和小部件有了框线提示，顶部的操作提示也有了色块和按钮；从 Play 商店中安装应用时，主屏会像 iOS 那样提前摆好图标，然后在图标上展示安装进度。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_e9252a16126c4d35a12b35ea54406326_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>桌面整理与应用安装进度</p> 
<h2 label="一级标题" style>从对话泡到对话小组件</h2> 
<p>提到桌面，就不得不提 Android 12 的小组件（widgets）。</p> 
<p>或许是受到了 iOS 14 的鞭策，小组件也成为了 Android 12 的核心更新内容之一：Google 在开发者预览版阶段不断对小组件功能进行着微调，小组件菜单也一步步从简陋的选单变成了集搜索、推荐和应用分类为一体的面板：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_be0602a60fab41e1ac2ed9ddeecc39b2_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>小组件面板</p> 
<p>此前 5 月 Beta 1 更新的同时，Google 推出了完整的小组件 适配翻<a class="project-link" data-id="64727" data-name="新指南" data-logo="https://img.36krcdn.com/20200729/v2_1ede9a573cbe43388c116d74aff1b44e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/64727" target="_blank">新指南</a>。本次 Beta 2 则终于为我们带来了已经反复出镜过的「对话」小组件。</p> 
<p>在 Beta 2 中，你可以通过长按桌面呼出启动器菜单的方式来添加对话小组件，但这种方式需要系统积累一定数量的「对话空间」内容，全新升级到 Beta 2 的用户大概率看不到任何应用。因此更可靠的触发方式是，在某条对话通知出现的同时长按通知，然后将其标记为「优先」。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_18f36793d886434789d651bdd61e034d_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>对话小组件添加方式</p> 
<p>在 Android 11 中，标记为「优先」的对话通知会以「对话泡」的方式进行呈现，Android 12 Beta 2 则会额外弹出提醒，询问用户是否将对应的对话以对话小组件的形式添加到桌面。</p> 
<p>对话小组件会在不同的尺寸状态下展示不同的内容，较小时仅包含一个可以直接跳转打开对话泡或对话窗口的头像，较大时则能呈现对话内容。不过目前对话内容仅支持文本。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_85da5ab7a2b44d569c40fc78170f1244_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>小组件到应用的跳转动画</p> 
<p>最后，小组件动画在 Android 12 Beta 2 中也得到了翻新，从小组件点击跳转应用时应用界面会像 iOS 那样从小组件扩展开来。</p> 
<h2 label="一级标题" style>快速设置面板与通知</h2> 
<p>介绍完主屏，目光往上，来到我们在日常使用中需要高频交互的下拉通知和快速设置面板。</p> 
<h3 label="二级标题" style>快速设置面板</h3> 
<p>首先引起我们注意的是快速设置面板。和 Android 11 不同，Android 12 的快速设置开关单个尺寸更大、能够呈现的信息也更多， 相比此前 Beta 1 中的设计，Android 12 Beta 2 中的快速设置开关圆角弧度更为明显。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_1f0df8dfad5f473facf07f222c4535d3_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>快速设置面板充满了圆角与色块</p> 
<p>交互方面最大的改进在于，能够跳转到更多设置的开关因为内容区域的增加，现在也有了一个额外的小箭头用于提示。比起旧版本永远分不清哪个点击切换哪个长按跳转的设计要友好不少；另外由于电源键在 Android 12 Beta 2 中也可以被设置为 Google Assistant 唤醒方式，所以原本放在电源键交互上的设备电源选项、设备控制器和卡包支付也拥有了独立的快速设置开关。</p> 
<p>快速设置开关本身的改动也不少。</p> 
<p>Wi-Fi 开关和移动数据网络开关在 Android 12 Beta 2 中合二为一。点击新的「网络」开关后会弹出一个利用 Settings Panel API 设计的底部弹出窗口，我们可以直接在这个窗口中快速切换 Wi-Fi 网络和移动数据。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_d5d306ed202d476fb5f0edcfdb50be7c_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>随时都能呼出的整合式网络控制面板</p> 
<p>换句话说我们在任何界面、任何应用中都可以无需跳转进行网络切换了，说实话，这还是 Settings Panel API 自 Android 10 引入以来个人见过的最巧妙的运用实例。</p> 
<p>最后，快速设置面板这里非常值得称道的地方在于，从这里也可以看出 Google 在上文「小组件 > 应用」跳转动画的选择上并非单纯借鉴 iOS。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_55af3d9dd0ec487491c7482fb510ed58_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>快速设置开关跳转到设置的动画</p> 
<p>Android 开发团队显然认为这个动画是一种非常舒适也非常具有通用性的设计，因此从快速设置开关跳转到对应设置界面的动画也采用类似的设计。这种处处呼应的动画和细节也为 Android 12 Beta 2 带来了极强的整体感。</p> 
<h3 label="二级标题" style>通知中心</h3> 
<p>通知中心在 Android 12 Beta 2 中也终于迎来了新设计。</p> 
<p>新版通知中心通过纯色背景的方式和固定为纯黑背景的快速设置面板区分开来，由于通知中心顶部的圆角与设备屏幕本身的圆角在曲率上保持了一致，配合新的下拉动画，很容易给人一种整个屏幕内容被向下拉出、快速设置面板从设备顶部区域和通知中心间出现的观感，舒适而细腻。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_041a57383f244629bdc0cffe53f3b129_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>下拉动画</p> 
<p>配合上面提到的 Material You 取色系统、媒体通知卡片、快速设置面板以及全新的自定义通知布局，「下拉操作」的交互和设计几乎成为了 Android 12 的颜值担当。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_de1c679039594baea13a75ee5bd89ae6_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>收起动画</p> 
<p>最后额外提一句，状态栏在 Android 12 中其实也将迎来不小的变化，主要表现为时间一侧的通知图标被大幅精简——和 Android 11 不同，勿扰模式、振动/静音甚至闹钟图标都不会再出现在状态栏里了，麦克风、相机使用提示出现时，对应的动画甚至会将整个时间显示区域暂时隐藏掉。对用户习惯来说算得上是一种挑战。</p> 
<h2 label="一级标题" style>原生「照明弹」上线</h2> 
<p>既然说到了麦克风和相机使用提示，就不得不展开聊一聊 Android 12 的隐私功能改动。</p> 
<h3 label="二级标题" style>隐私仪表板</h3> 
<p>在 Android 12 Beta 2 中，Google 第一时间对 OEM 定制系统中的「照明弹」功能进行了跟进，是为「隐私仪表板（Privacy Dashboard）」。</p> 
<p>隐私仪表板位于「系统设置 > 隐私」设置中，设计上借鉴了「数字健康」中的使用情况统计圆环，主界面顶部会展示过去 24 小时内摄像头、定位和麦克风三大隐私权限的调用情况分布，下方则是对应的权限和使用详情。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_d11a042cdd3b4ec4b3fc2e60e9f869c8_img_000" data-img-size-val="1080,788" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>隐私仪表板</p> 
<p>三大隐私权限的使用详情界面采用了国内定制 UI 用户比较熟悉的垂直时间轴设计，可以更为清楚地看到哪款应用在什么时候调用了对应权限，如果发现可疑的权限行为，点击时间轴上的事件就能跳转到对应应用的权限管理页面进行处理，或通过时间轴页面底部的 Tab 按钮对该类权限做统一管理。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_6be4e144298b4af49e933e21f9a6fe90_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>MIUi 的应用行为记录</p> 
<p>如果从 MIUI 用户的角度来评价，Android 12 的隐私仪表板相比 MIUI 的「应用行为记录」还是显得简陋了些——后者同时针对所有应用行为（包括自启动、链式启动、权限使用、敏感行为）和单个应用行为提供时间轴视图，更为直观、详尽，可以说是目前 Android 生态内的标杆级实现了，希望后续原生 Android 这边能像其他 OEM 厂商一样多多学习借鉴。</p> 
<h3 label="二级标题" style>指示器与屏蔽开关</h3> 
<p>除了隐私仪表板，针对麦克风和摄像头这两大隐私权限的使用指示器与全局屏蔽开关也在 Android 12 Beta 2 中正式上线了。</p> 
<p>使用指示器会在对应权限被调用时首先以「小药丸」的样式出现在屏幕右上角、状态栏最右侧的位置，即上文介绍状态栏改动时提到的，出现时甚至会暂时隐藏掉时间显示。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_3da65ea00429488d952565b1d7211a0c_img_000" data-img-size-val="720,312" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>指示器动画</p> 
<p>随后「小药丸」会变成一个绿色小圆点在权限被调用期间持续出现在时间右侧，但这个绿点无论截图还是录屏都无法被捕获到。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_ed35d1e1aedc45afbb565633b0c2428c_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>指示器效果</p> 
<p>除了让我们明白什么时候被什么应用调用了，Android 12 Beta 2 还正式上线了全局屏蔽开关。全局屏蔽开关在「系统设置 > 隐私」中可以找到，也可以作为单独的开关按钮添加到快速设置面板中。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_052485388d8e4bd59a8c8c21c017aaf8_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>摄像头与麦克风屏蔽开关</p> 
<p>全局屏蔽开关的原理也很有意思，它并非通过关闭对应硬件的方式来屏蔽使用，毕竟这种方式会带来不少预料之外的兼容性问题，甚至影响部分 app 的正常运行；相反，在屏蔽麦克风或相机后，应用依然能够在 Android 12 中正常使用对应功能，但通过相机、麦克风获取到的信息都是空白信息。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_a3beea65799049dd850bbeeea01788a8_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>更多隐私控制选项</p> 
<p>除了上述功能外，「系统设置 > 隐私」设置中也提供了很多此前不曾向用户开放的隐私开关或实用小功能，比如在应用调用剪贴板时提供 toast 通知，针对本地机器学习任务（如智能回复）提供数据管理功能等等。</p> 
<h2 label="一级标题" style>更顺滑的画中画体验</h2> 
<p>画中画窗口在 Android 12 Beta 2 中无法通过边角拖放的方式改变尺寸了。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_cf347a28374b421581ee3832c619edae_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>双指自由缩放尺寸</p> 
<p>Google 表示点击拖放更改尺寸这种操作太容易误触也太容易与拖放更改位置的操作混淆了，所以将画中画窗口大小调节交互改成了双指缩放，就像查看照片时那样。好在 Android 12 的其他画中画特性还在，比如边缘堆叠与无级尺寸调节。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_fa73a18516bc40aab1118bc4b408fe3c_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>从 PiP 回到应用的过渡动画</p> 
<p>当然，画中画在 Beta 2 中最大的进步在于动画——Android 这边的画中画动画终于也像 iOS 那样自然、平滑了，无论从应用到画中画窗口还是从画中画窗口回到应用，切换过程都会有一个缩放动画用来过渡，不像早前版本那样生硬。</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_293a64f4938e4207af3278868eb6e861_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>从应用进入 PiP 的过渡动画（目前会导致桌面图标 bug）</p> 
<h2 label="一级标题" style>更多有意思的小细节</h2> 
<p>最后，本次 Beta 2 还有不少值得拿出来单独提一下的小细节，这里也为大家简单整理一下。</p> 
<p>和快速设置面板、通知中心类似，多任务界面现在也采用了纯色背景设计：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_a58ba2d65dee41058618274dcbe2ee99_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>多任务界面的纯色背景</p> 
<p>Google 没想到的是，Beta 1 中上线的全新点按动画因为效果太像图形 bug，发布后收到了大量的用户反馈，因此在这个版本中几乎被移除干净了：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_170e3525779d49258463508e8f3524e4_img_000" data-img-size-val="998,456" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>这个动画没了 | 图：AndroidPolice</p> 
<p>同样的，Beta 1 中那个新旧<a class="project-link" data-id="181350" data-name="设计元" data-logo="https://img.36krcdn.com/20200729/v2_c271db76e4f944069ebbeb59f4941ec0_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/181350" target="_blank">设计元</a>素混杂、观感非常难受的音量控制面板也用上了宣传片中的新设计：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_6979f2825b4347cebbfc4ed294da3c22_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>和新设计更一致的音量控制面板</p> 
<p>如果你依然习惯使用电源键呼出电源菜单，会发现电源菜单在 Android 12 Beta 2 中换上了圆角弹窗设计，关机、重启等操作则变成了大大的圆形按钮；此外新版电源菜单在出现、消失的过程中，桌面背景会随之出现缩放效果（有点奇怪的是桌面图标竟然不会跟着缩放）：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_63366d80f95748878bad5def99e1aaaf_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>电源菜单动画</p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>除了上文提到的动画，有线充电和无线充电在 Android 12 Beta 2 中也有了跟随系统配色的全局动画。其中无线充电动画为屏幕中心向四周扩散的涟漪，呼应无线充电线圈的实际位置；有线充电动画则是从底部向四周扩散的涟漪，呼应 Type-C 接口的实际位置：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_97a288ec485a4d9dba6d3060e6983c36_img_000" data-img-size-val="450,950" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>无线充电和有线充电动画</p> 
<p>来到设置这边，系统设置中总控开关（比如开发者选项顶部的那个）样式得到了翻新，并且能够跟随系统配色进行变化。唯一的问题是这个开关在「换皮」之后竟然不是水平居中的：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_c8d4adc3ed9149b59ffbe0ba906e11f0_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>新的设置开关样式，但竟然没居中</p> 
<p>应用后台限制设置也进行了梳理，无限制、优化使用、限制后台三种选项更加直观易懂：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_73a5705fccff4001bf1a611a9ef5e828_img_000" data-img-size-val="583,1241" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>更直观的后台控制选项，得为这个单独写一篇了</p> 
<p>最后，Android 12 Beta 2 竟然会在深色主题关闭和开启状态下自动调用不同的字体，有说法是为了保证不同背景下的文本对比度，可谓魔鬼级细节（但总感觉又有点像 bug）：</p> 
<p><img src="https://img.36krcdn.com/20210615/v2_8c14762e9b6b4b6db8f15e60fefa3a92_img_000" data-img-size-val="1080,1175" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>深色主题关闭和开启状态下时间字体略有不同</p> 
<p>以上便是本次 Android 12 Beta 2 更新中值得关注的全部细节，你喜欢 Google 为 Pixel 准备的这套新 UI 吗？</p>  
</div>
            