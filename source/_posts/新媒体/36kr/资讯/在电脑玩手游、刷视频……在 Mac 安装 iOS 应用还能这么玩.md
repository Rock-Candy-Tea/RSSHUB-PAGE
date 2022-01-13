
---
title: '在电脑玩手游、刷视频……在 Mac 安装 iOS 应用还能这么玩'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220113/v2_e4fb7edb524543e4acde3aaabff63d09_img_000'
author: 36kr
comments: false
date: Thu, 13 Jan 2022 06:49:08 GMT
thumbnail: 'https://img.36krcdn.com/20220113/v2_e4fb7edb524543e4acde3aaabff63d09_img_000'
---

<div>   
<p>让 macOS 直接运行 iOS 程序已经不是什么新鲜的事情了。自从 M1 系列的 Mac 问世以来，我们在 Mac App Store 甚至可以直接下载安装受支持的 iOS 应用，并用键盘鼠标来模拟触摸操作在 macOS 上使用这些 iOS 应用。虽然已经有很多 iOS 应用直接支持了在 macOS 上的安装，还是有一些应用开发者为了减少开发成本或者担心其他因素，选择将自己的 iOS 应用从 Mac App Store 上移除。 </p> 
<p>如果我们依旧希望<strong>在系统架构完全支持的 M1 系列 Mac 上面</strong>运行这些应用，那么就需要特殊的手段 —— 旁加载，也就是 sideloading—— 才能安装这些 iOS 应用。这是 macOS 11.2.3 之前的常规操作，我们称这段时期为「前 macOS 旁加载」时代。 </p> 
<p>显然，Apple 并不想让我们轻松地就将未经验证、不受支持的 iOS 应用直接在 macOS 上成功运行。曾被允许的简单「旁加载」在 macOS 11.3 的更新中被 Apple 禁用，自然最新的 macOS Monterey 12.1 也不受支持。因此，在「后 macOS 旁加载」时代，我们需要 PlayCover —— 一个专门用于在 M1 Mac 上安装 iOS 应用的辅助程序的帮助，才能够完整地在 M1 Mac 上面安装并体验未受支持的 iOS 应用。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_e4fb7edb524543e4acde3aaabff63d09_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>在 M1 Mac 上面运行由 PlayCover 安装的「原神」 </p> 
<h2 label="一级标题" style><strong>PlayCover 简介</strong></h2> 
<p label="正文" style>后 macOS 旁加载时代 PlayCover 的优势</p> 
<p>如前面提到，虽然依旧是「旁加载」的原理，但是 PlayCover 本身已经是一套完整的在 macOS 上运行 iOS 程序的辅助软件，相比于「前 macOS 旁加载」时代，PlayCover： </p> 
<p>能够非常方便地在 M1 Mac 上面通过解密的 IPA 来安装 iOS 应用；</p> 
<p>有着完整的键盘快捷键映射和鼠标操作映射，且支持快捷键映射导出导入；</p> 
<p>也是我们在「后 macOS 旁加载」时期唯一的于 M1 Mac 上安装 iOS 应用的途径；</p> 
<p>另外，PlayCover 的官<a class="project-link" data-id="4051878" data-name="方维" data-logo="https://img.36krcdn.com/20220109/v2_75ea89a449dc4bc493dc4a4accaf72e4_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4411601033?mp=zzquote" target="_blank">方维</a>护团队响应问题及时，社区资源丰富，开发者更新维护地也非常频繁，因此更是推荐大家安装使用。 </p> 
<h2 label="一级标题" style><strong>安装 PlayCover</strong></h2> 
<p>虽然 PlayCover 已经发布一段时间且也有自己的官方网站 （https://www.playcover.me） ，其依旧处于测试阶段，开发者的公告和发布渠道都集中于 PlayCover 官方 Discord 服务器 。推荐大家优先加入官方 Discord 来获取最新的开发进度、更新日志以及疑难杂症的支持。 </p> 
<p>目前最新的 PlayCover 版本是 0.9.63，加入官方 Discord 之后可以看到开发者在 #announcements 频道发布的更新信息，点击附件下载安装即可。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_619de8378aa048f38ae9dc84e427c9fa_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>PlayCover 的官方 Discord 服务器 </p> 
<p>另外需要注意的是：由于 PlayCover 开发者并没有为自己的软件签名，因此首次打开 PlayCover 的时候需要进入 macOS 的「应用程序」文件夹，找到 PlayCover 之后「右键 - 打开」才能正常运行，从而不被 macOS 直接禁止运行并提示我们将软件移入废纸篓。 </p> 
<h2 label="一级标题" style><strong>使用 PlayCover 安装 iOS 应用</strong></h2> 
<h2 label="一级标题" style><strong style="font-size: 18px; color: rgb(51, 51, 51);">获取已解密的 iOS 应用 IPA 安装包</strong></h2> 
<p>需要注意的是，PlayCover 是通过 IPA 文件来安装 iOS 应用的，且 PlayCover 仅支持安装由已越狱 iOS 设备上面导出的 IPA 文件，并不支持「前 macOS 旁加载」时代用比如 iMazing 导出的未解密 IPA 文件。这也就意味着，如果我们想要安装某个 iOS 应用，那么我们要么需要一台已越狱的 iOS 设备来导出相应的 IPA 文件，要么等待其他乐于助人的同学分享其导出的已解密 IPA 文件。 </p> 
<p>幸好，PlayCover 社区有着丰富的已解密 IPA 资源，由官方 Discord 服务器的成员上传分享。我们可以在 #decrypted-ipas 频道找到可供下载的 IPA 文件，使用 Discord 在本频道中搜索关键词寻找相应的 IPA，<a class="project-link" data-id="395913" data-name="并点" data-logo="https://img.36krcdn.com/20210811/v2_0587def072a34bdb8b8bfc7d8c5b3807_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/395913" target="_blank">并点</a>击分享链接将已经解密的 IPA 下载到 M1 Mac 中，准备安装。部分 IPA 也已经上传整理到 PlayCover IPA 分享站 ，我们也可以直接前往搜索下载。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_24e8939f048447678c6d450fb6636269_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>PlayCover 官方 Discord 服务器中的已解密 IPA 分享频道 </p> 
<h2 label="一级标题" style><strong>使用 PlayCover 安装 IPA</strong></h2> 
<p><a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>我们已解密的 IPA 安装文件之后，我们打开 PlayCover，选择 Add app，并在 Finder 中选择刚刚下载的 IPA 进行安装，PlayCover 就会对应用进行一系列的签名、修改等操作，绕过 Apple 的限制，将 iOS 应用在 M1 Mac 上成功安装，并安装如 PlayTools 的一系列辅助工具，让我们在 Mac 上面使用 iOS 应用更加方便。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_77345ac4b29f409d95214acbf7b3e201_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>PlayCover 应用主界面 </p> 
<p>这样安装的应用在 PlayCover 主界面可以直接看到并单击运行，部分受支持的应用（比如原神）也可以点击绿色最大化按钮将窗口全屏显示，右键已安装的 iOS 应用还可以对其进行后续操作（比如启用 PlaySign、在 Finder 中打开安装的应用位置、清除应用缓存、导入导出键盘映射等等）。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_4a1a967e2c8343c9857ec05231e947d7_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>通过 PlayCover 安装的应用，右键菜单对应用进行配置 </p> 
<p>另外大家可能已经看到 PlayCover 已经在主界面提供了部分可供下载的 IPA 链接，但是这里提供的 IPA 并不全面，有些 IPA 链接给到的 iOS 软件版本已经落后，因此推荐大家优先在 Discord 服务器中寻找合适的 IPA 文件。 </p> 
<h2 label="一级标题" style><strong>特殊 iOS 应用安装的必要操作</strong></h2> 
<p>部分 iOS 应用有特殊的安装步骤，很多需要注意的内容都在 Discord 服务器的 #faq-read-first 进行了详细的说明，因此如果遇到 PlayCover 无法安装应用或已经安装的应用无法打开的问题，建议去此频道寻找解决方案。 </p> 
<p>其中，很大一部分 PlayCover 用户都是为了在 macOS 上运行原神。在 PlayCover 0.9.63，原神 2.4 版本的情况下，我们可以： </p> 
<p>进入 Recovery 模式暂时关闭 macOS 的 SIP 保护：</p> 
<p>重启 Mac 并按住电源键进入 Recovery 模式，选择 Options；</p> 
<p>进入 Recovery 之后点击菜单栏的 Utilities，打开终端 Terminal；</p> 
<p>输入 csrutil disable 并确认，输入密码完成命令执行后重启 Mac；</p> 
<p>在关闭了 SIP 保护的 macOS 中，打开终端并执行 sudo nvram boot-args="amfi_get_out_of_my_way=1"，来允许 nvram boot-args，并再次重启 Mac；</p> 
<p>打开 PlayCover 之后点击界面下方的 Enable PlaySign 按钮；</p> 
<p>打开安装好的原神，这里我们就应该能够正常登录了，但此时需要立刻快捷键 Command + Q 关闭原神，并重新启用 macOS 的 SIP 保护：</p> 
<p>同样的进入 Recovery 模式并在终端 Terminal 中输入 csrutil enable并确认；</p> 
<p>再次输入密码等待命令执行完成后重启 Mac；</p> 
<p>此时我们再打开 PlayCover 启动原神，就可以正常进入游戏了。</p> 
<p>由于每个版本的 PlayCover 和原神都有不同的特殊安装操作，因此还请具体版本具体分析，在 PlayCover 的官方 Discord 服务器中及时查看相应的安装解决方法。 </p> 
<h2 label="一级标题" style><strong>方便地使用键鼠模拟触屏操作</strong></h2> 
<p>PlayCover 除了解决了在 M1 Mac 上安装 iOS 应用的一大难题外，还能够通过键鼠操作映射（keymapping）来模拟触屏的操作，让在 Mac 上面使用 iOS 应用更为顺畅（让在 Mac 上玩原神等游戏 iOS 版本的体验更加接近 PC 端的操作）。 </p> 
<p>我们在 PlayCover 安装的应用中，使用快捷键 Ctrl + P 可以进入键鼠映射界面，其中： </p> 
<p><strong>Ctrl + J</strong>：添加 WASD 映射的移动摇杆</p> 
<p><strong>Ctrl + M</strong>：添加鼠标移动区域（用来使用鼠标移动视角）</p> 
<p><strong>Ctrl + N</strong>：添加键盘某个按键的屏幕按钮映射（其中 Shift + L 表示鼠标左键，Shift + R 表示鼠标右键）</p> 
<p><strong>Ctrl + '+/-'</strong>：增大/缩小按钮大小</p> 
<p><strong>Ctrl + Delete (Backspace)</strong>：移除某个按键映射</p> 
<p><strong>Ctrl + W/A/S/D</strong>：微调按钮位置</p> 
<p><strong>Alt / Option</strong>：显示或隐藏鼠标</p> 
<p>另外 PlayCover 也支持使用 <strong>Ctrl + U</strong> 开启宏的录制，<strong>Ctrl + I</strong> 结束录制，<strong>Ctrl + O</strong> 播放录制的宏。 </p> 
<p>当然，如果我们想要自己进行复杂的快捷键绑定，也可以直接导入其他已经设计好的键盘映射。在 PlayCover 官方 Discord 的 #keymap-showcase 频道，我们可以找到其他同学分享的键鼠映射，直接下载导入相应的游戏，从而更加方便快捷的使用键盘鼠标来操作。 </p> 
<p>对原神来说，其相应的键鼠映射位于： https://sspai.com/s/BLVL ，加入 Discord 服务器的同学可以直接点击进入频道下载，并在 PlayCover 主界面中安装好的游戏图标上右键，导入设置好的键盘映射文件。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_aa0128dd7f0945d4b966071a7e591a34_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>来自 Discord 服务器同学提供的完善的「原神」键鼠操作映射 </p> 
<p>另外，PlayCover 安装的原神也原生支持了手柄操作，原神官方支持 Xbox 和 PlayStation 系列手柄，通过蓝牙连接到 Mac 上面之后，原神可以直接转换为手柄操作，无需经过键盘映射操作，和在 PC 或 PlayStation 主机上的游玩体验一致。 </p> 
<h2 label="一级标题" style><strong>尾巴</strong></h2> 
<p>不得不说，很大程度上是「在 macOS 上打原神」的需求，促使了 PlayCover 的诞生，但是 PlayCover 事实上已经发展成为一整套完善的「M1 Mac 运行 iOS 应用」的基础设施。同时 PlayCover 自己亦是不断迭代更新，不仅在尝试去除一些比如「关闭 SIP 保护」等看起来非常可疑的操作需要，还在继续添加更多丰富的应用和功能支持。 </p> 
<p>虽然目前 PlayCover 仅支持 Apple silicon 版本也就是搭载 M1 系列芯片的 Mac，根据官网信息显示，开发团队也将在未来增加对于 Intel 芯片 Mac 的支持，届时你也能在 Intel 芯片 Mac 装上 iOS 应用和游戏。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220113/v2_504da5a77baa4e1197e05dfcbb961a1a_img_000" referrerpolicy="no-referrer"></p> 
<p>有着完善开发和社区支持的 PlayCover 的确是如今在 M1 Mac 上安装运行 iOS 应用的不二之选 —— 不论是游戏还是常规应用。 </p> 
<p>最后，要知道如今 PlayCover 提供的一些顽固应用安装的 workaround，很大一部分都是针对特定应用的特定版本，本文提到的部分方法也是很可能在某个应用版本更新之后直接失效的，因此再次提醒各位准备使用 PlayCover 的同学加入官方 Discord 来获取更多、更及时的安装方法支持。 </p> 
<p>本文的介绍就到这里，感谢大家的阅读。 </p> 
<p>原文链接：https://sspai.com/post/70602 </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247529439&idx=2&sn=a5df0599bf685829215774318ade089f&chksm=fdb386b5cac40fa3274c04224de817892f16f12a2f569234eece932de3ecceb9346d611eb9af#rd">“少数派”（ID：sspaime）</a>，作者：SpencerWoo ，责编：waychane ，36氪经授权发布。</p>  
</div>
            