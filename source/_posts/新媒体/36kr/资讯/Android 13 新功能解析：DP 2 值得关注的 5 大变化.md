
---
title: 'Android 13 新功能解析：DP 2 值得关注的 5 大变化'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220321/v2_d23526f59c784d3491f83357acc52170_img_000'
author: 36kr
comments: false
date: Mon, 21 Mar 2022 07:18:00 GMT
thumbnail: 'https://img.36krcdn.com/20220321/v2_d23526f59c784d3491f83357acc52170_img_000'
---

<div>   
<p>3 月 18 日凌晨，Google 面向自家 Pixel 设备推出了 Android 13 的第二个开发者预览版（以下简称 DP2）。和往年不同的是，这将是今年 Android 13 正式版发布前的最后一个开发者预览版本，接下来 Android 13 就会进入为期 4 个多月的 Beta <a class="project-link" data-id="8712" data-name="测试" data-logo="https://img.36krcdn.com/20220318/v2_d188db412f2e4db89c6424314ac39971_img_jpg" data-refer-type="2" href="https://36kr.com/projectDetails/8712" target="_blank">测试</a>阶段。 </p> 
<p>相比 首个开发者预览版   中海量的新特性，如独立的应用语言设置、系统级照片选择器、主题图标 API 等，Android 13 DP2 中加入的新内容不多。本文以 Google Pixel 5 的体验为例，为大家介绍当中值得关注的 Android 13 新功能。 </p> 
<p><strong>▍通知推送允许「一刀切」</strong></p> 
<p>Android 近年在通知交互和管理粒度方面的改进可以说是有目共睹，相比 iOS，Android 通知管理此前少有的缺憾应该就是初次启动应用时的通知授权了——和打磨得日臻完<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>通知管理系统相比，默认允许通知推送、需要用户跳转至二级甚至三级设置界面进行后续管理的体验，实在算不上「现代」。 </p> 
<p>此前在 Android 13 DP1 中已经出现的通知权限，在 Android 13 DP2 中正式生效，随之而来的是一项名为 POST_NOTIFICATIONS 的  运行时权限  ，实际效果与位置信息等其它运行时权限类似，即通过弹出对话框的方式询问用户是否允许应用发送通知。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_d23526f59c784d3491f83357acc52170_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">通知运行时权限的实际交互效果 </p> 
<p>关于这个功能，值得我们关注的细节有这么几点。 </p> 
<p>首先，这是一个面向 Android 13 的新特性，以不同系统版本为适配目标的应用，实际效果自然也会有所差异。具体而言：</p> 
<p>面向 Android 12L（API 32）及以下版本开发的应用，通知运行时权限弹窗仅会在应用首次启动并注册通知渠道时弹出。因此上图也是目前大部分应用在 Android 13 DP2 中的实际呈现效果</p> 
<ol class=" list-paddingleft-2"> 
 <li><p>面向 Android 13 进行适配的应用，则可以额外获得更符合实际上下文情境的弹窗时机。比如在应用引导界面中向用户阐明通知用途后，再弹出通知运行时权限授予对话框。</p></li> 
</ol> 
<p>因此这一特性的理想呈现效果可以参考 Google 在  对应文档  中给出的示意图： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_6568c6f9d68645ba8528ffcc3780004d_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">出现时机更符合实际使用上下文情境的通知运行时权限 </p> 
<p>另外，对于通知运行时权限弹窗的选项，如果我们在弹窗时选择了拒绝，则应用的所有通知都将被阻隔，<strong>效果相当于我们在此前的 Android 系统版本中手动关闭应用的通知总开关</strong>。 </p> 
<p>而除了允许和拒绝，我们实际上也可以通<a class="project-link" data-id="397908" data-name="知点" data-logo="https://img.36krcdn.com/20210811/v2_57f873f5620f40e09045a64895bca067_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397908" target="_blank">知点</a>击其它区域或使用返回手势等方式来手动忽略掉运行时权限弹窗，如果应用在升级到 Android 13 前已经通过通知渠道获得了某些通知的推送权限，忽略运行时权限弹窗则不会影响到这些通知的后续推送。 </p> 
<p><strong>▍自然畅快的分屏新方式</strong></p> 
<p>Android 12L 开始，Google 用实际行动表明了在<a class="project-link" data-id="498684" data-name="重拾" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/498684" target="_blank">重拾</a>平板、折叠屏等大屏设备体验这件事情上的信心和决心。虽然不久前刚刚推送的 Android 12L 正式版并没有在太多设备上<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>普及，Android 13 并没有停下对大屏设备多任务处理交互的探索。 </p> 
<p>在这次的 Android 13 DP2 中，最令人印象深刻的一项改动是围绕分屏操作的：如果你在使用某个应用的过程中收到了来自另一个应用的通知，并且希望接下来同时处理这两个应用中的任务，以往的操作一般是点击通知打开另一个应用，然后再进行分屏操作。 </p> 
<p>而在 Android 13 DP2 中，我们可以在不离开当前应用的前提下，按住需要分屏的应用的通知不放，然后便能看到分屏触发提示————将通知扔到屏幕一侧即可快速完成分屏。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_26630cef2ccc43d1b3c30dfdd4c5ef58_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">直接拖动通知实现分屏 </p> 
<p>虽然我们对 Android 平板是否会崛起持怀疑态度，但 Android 13 正式版对大屏设备而言至少会是交互和操作都相当友好的一个版本。 </p> 
<p><strong>▍重新设计媒体通知卡片</strong></p> 
<p>Android 的媒体通知卡片设计自 Android 8.0 以来一直在走下坡路，为了配合 Material You 动态颜色，Android 12 中的媒体通知卡片更是完全抹去了来自媒体内容本身的「个性」 。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_d1a24aeea827469095bcb2845d717020_img_000" referrerpolicy="no-referrer"></p> 
<p>Android 8.0 与 Android 12 的媒体通知对比  </p> 
<p>通知系统和媒体通知卡片可以说是每逢更新必「动刀」，这次 Android 13 在 DP2 中也直接对媒体通知卡片来了一次布局和设计上的「推倒重来」。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_846375b378d742f68686d27f90f27136_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Android 13 的媒体通知卡片仅提供一种尺寸  </p> 
<p>相比 Android 12，新的媒体通知卡片直接以媒体播放应用提供的专辑封面为背景，操控按钮、播放设备选择按钮的配色也直接提取自媒体封面，不再与 Material You 挂钩，某种程度上算是弥补了本部分开头提到的「个性化」问题。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_9994cd2e558442ffa7001d380977f9ef_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">媒体通知卡片配色方案由媒体封面决定 </p> 
<p>新的媒体通知卡片默认也只提供一种展示尺寸了，通知中心和快速设置开关面板中的呈现效果一致；布局上则更加强调播放/暂停控制，切歌、播放进度以及媒体播放应用提供的其它操作则被放在了底部位置。 </p> 
<p>不过根据惯例，在开发者预览版阶段评价媒体通知卡片设计往往都为时过早，这个阶段的设计一般都不会代表最终效果，所以如果你依旧不满意，暂时也不用感到太失望。 </p> 
<p><strong>▍快速设置面板布局调整</strong></p> 
<p>为了迎合某些战略上的调整，近年来越来越多的厂商都开始将电源键「改造」成为触发智能语音助理的新入口，毕竟理论上来说，比起开关机人们使用语音助理的频率要更高一些。 </p> 
<p>Google 也不例外，在 Android 12 中，Google 为 Pixel 设备带来了电源键唤醒 Google Assistant 的选项。为了解决随之而来的电源键交互问题，Android 13 DP2 则向三星 One UI「取经」，对快速设置面板进行了一些易用性改进。 </p> 
<p>在新的快速设置面板中，系统设置和电源设置入口都被直接放到了右下角，在大屏上单手操作起来更加方便： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_8bca51e26ea5469dba5fff18ff9431a6_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">新的快速设置面板布局与使用中的应用管理  </p> 
<p>此外，快速设置面板底部还额外增加了「使用中的应用」管理入口，我们可以在这里直接管理运行中的后台应用；如果你在设备上设置了多个用户，快速设置面板右下角也会增加一个用于快速切换用户的入口。 </p> 
<p>与快速设置面板相关的几个改动这里也顺带提一下：</p> 
<p>设备控制（Device controls）更名为家庭（Home）</p> 
<p>勿扰模式在 Android 13 中似乎打算更名为 Priority mode（优先模式）了，目前快速设置开关已经更名，但系统设置及相关翻译还未更新</p> 
<p>此前在 DP1 已经出现的二维码扫描开关已经正式可用了</p> 
<ol class=" list-paddingleft-2"> 
 <li><p>新增了一个名为「安全和隐私设置」的开关，添加后可通过它一键管理相机、麦克风和位置信息的全局开关状态（与已经存在的麦克风、相机全局开关功能有些重复）；同时提供一键跳转至系统安全设置界面的入口</p></li> 
</ol> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_6b700b5cfc7b4262a96372a86e5567ed_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">新增的快速设置开关与对应操作界面  </p> 
<p><strong>▍给非英语用户更多关注</strong></p> 
<p>首先值得祝贺的是，在上个版本中需要 adb 手动开启的独立应用语言设置界面，在 Android 13 DP2 中已经正式可用了，不过部分应用（尤其是内置了语言设置的应用）在正式版的语言设置中已经不支持手动设置应用语言了。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_f5cfe2f0f09945548250b49a99f4f3b8_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">独立的应用语言设置  </p> 
<p>除了应用语言设置，Android 13 DP2 也引入了不少针对日语、汉语等非英语语言用户的改进。比如在 Android 应用中被广泛使用的 TextView 控件现在可以按照文節（bunsetsu）或短语进行折行显示了，相比以往只能生硬地根据字符来折行的方式，应该能够带来更加舒适的文本显示和阅读体验。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_3fecab7bef61462ab4ea470effc93172_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">不启用 (上) 和启用 (下) 短语折行的日语文本对比 | 图：Google </p> 
<p>再比如非拉丁文字 (如泰<a class="project-link" data-id="258858" data-name="米尔" data-logo="https://img.36krcdn.com/20210809/v2_f5c592df594349a5809ca4fc41fdbd11_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/258858" target="_blank">米尔</a>语、缅甸语、泰卢固语和藏语) 在 Android 13 上也可以拥有更加舒适的显示效果了，开发者只需将应用的目标平台设定为 Android 13 即可拥有不剃头不剃尾的文本显示效果： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_eb75a1a5f2414776be02c7a03c48efc5_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">以 Android 13 为目标平台的应用中的非拉丁文字行高改进效果 (下) | 图：Google </p> 
<p>新的  文本转换 API   则主要用于提高汉语和日语用户的输入体验，这里 Google 举的例子是： </p> 
<blockquote> 
 <p>以前的搜索需要日语用户 (1) 输入平假名来表示搜索词的发音，可能是一个地名或一个应用名 (2) 使用键盘将平假名字符转换为汉字 (3) 使用汉字字符重新搜索 (4) 获得搜索结果。在新的文本转换 API 的帮助下，日语用户只需输入平假名，就可以立即看到日文汉字的搜索结果，相当于跳过了第 2 和第 3 步。  </p> 
</blockquote> 
<p>因为目前在 Android 13 DP2 中难以复现，我们也无从得知这一特性对中文用户而言究竟意味着什么——Pixel Launcher 和 Google 通讯录会因此支持国人更熟悉的拼音首字母搜索吗？ </p> 
<p>另外，去年 Android 12 测试阶段由热心用户提交的 CJK 可变字体支持请求至今没有得到实现，不知道 Android 13 能不能满足 CJK 用户一个心愿。 </p> 
<p><strong>▍小结</strong></p> 
<p>除了上述更新，Android 13 还有一些值得一提的小细节。比如支持了包括   COLRv1   字体格式、蓝牙低功耗（LE）音频以及 MIDI 2.0 在内的更多的现代化标准，重新设计、梳理了部分系统设置界面，包括显示大小、振动反馈、快速配对和屏幕保护等等，篇幅有限这里不再赘述。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220321/v2_0ab5a14ffb874ccdb12f250121fa13cd_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">新的文字和阅读选项、振动和触感反馈设置  </p> 
<p>接下来迎接我们的，就是更多 OEM 机型都能加入、更接近 Android 13 正式体验的 Beta 测试版本了。届时我们应该也会有更多功能和体验上的更新与大家分享，敬请关注。 </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247532188&idx=2&sn=2cb75b6413330a26dada1a61e8080dec&chksm=fdb38bf6cac402e0e38dccd37b083ae53dfb46cb9db4b9992111baad08cdb45a10cee5d4926c#rd">“少数派”（ID：sspaime）</a>，作者：克莱德，36氪经授权发布。</p>  
</div>
            