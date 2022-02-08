
---
title: 'Magisk Manager 详解'
categories: 
 - 新媒体
 - 少数派 sspai
 - 专题内文章更新
headimg: 'https://cdn.sspai.com/2019/03/31/33b4ff7cca69e217ae4e12e27d640165.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sun, 31 Mar 2019 05:09:28 GMT
thumbnail: 'https://cdn.sspai.com/2019/03/31/33b4ff7cca69e217ae4e12e27d640165.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-0b37afcb><div class="update-wrap" data-v-0b37afcb></div><div class="content wangEditor-txt minHeight" data-v-0b37afcb><p>久等了。</p>
<p>在本系列的前两篇文章中，我们介绍了 Magisk 这个（相对而言）兼具稳定性和可玩性的「神器」:作为一个 root 方案，它能在不破坏系统实现无痛 OTA，作为一个插件扩展平台，它又能提供丰富的自定义模块来满足多样化的定制需求。</p>
<p>但也正如我们在本系列第一篇中所言， Magisk 本质上是一种文件挂载系统。我们大多数时候所接触到的那个图标为面具的应用，其实只是我们与之发生各种交互行为的「媒介」。</p>
<p>今天我们就来介绍一下这个「媒介」的四大功能。</p>
<h2 id="ss-2-1554264202389">隐藏 root 事实「无痛」玩机</h2>
<p>从某种角度上来说，是 Magisk Hide 让「刷入 Magisk」这件事情从可选项变成了推荐项。</p>
<blockquote>
<p>大家好，我是一名 Android 玩家，自从看了少数派的文章给手机解 BL 锁、Root 了之后，奇怪的事情便接踵而至：没办法从 Play Store 中搜索到 Netflix、心爱的宝可梦走等一些游戏没办法玩耍、朋友推荐我下载的 App 居然提示不兼容此设备、看视频的时候清晰度死活上不去……</p>
</blockquote>
<p>难道是我的手机坏了？</p>
<p>许多新手玩家都有这样的疑惑。事实上，包括谷歌服务在内的许多 Android 上的应用、游戏、服务都十分重视保护自己的版权内容，当这些软件检测到你的手机遭到「魔改」后，便会拒绝认证你的设备。</p>
<p>好在道高一尺魔高一仗，我们现在可以通过 Magisk Hide 来绕过这些检测。</p>
<p>在我们设置 Magisk Hide 前，先进入 Magisk Manager 检测是否通过了谷歌服务中的 SafetyNet 安全性测试。想要通过 SafetyNet 测试，最好使用原厂系统，或者是值得信赖的第三方 ROM 正式版（也就是 Official Builds），以减少不必要的麻烦。</p>
<p></p><figure tabindex="0" class="ss-img-wrapper"><img src="https://cdn.sspai.com/2019/03/31/33b4ff7cca69e217ae4e12e27d640165.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="主界面中的 SafetyNet 检测" title="主界面中的 SafetyNet 检测" width="450" data-original="https://cdn.sspai.com/2019/03/31/33b4ff7cca69e217ae4e12e27d640165.png" referrerpolicy="no-referrer"><figcaption class="ss-image-caption">主界面中的 SafetyNet 检测</figcaption></figure><p></p>
<p>如果是 <strong>basic integrity</strong> 这一项没有通过认证，那说明你遇到了大麻烦：试着开启「Magisk 核心功能模式」或者卸载所有模块，如果还是没有通过，那么你可能需要换一个系统或者第三方 ROM 了。</p>
<p>如果是 <strong>ctsProfile</strong> 这一项没有通过，那说明你的 ROM 没有通过其兼容性测试，一些 beta 版本或者国内厂商的 ROM 可能出现这种问题。这时我们下载使用 <a href="https://forum.xda-developers.com/apps/magisk/module-magiskhide-props-config-t3789228" title="MagiskHide Props Config">MagiskHide Props Config</a> 这个模块往往能够解决问题。</p>
<p>确保 SafetyNet 检测无虞后，我们才能开始「蒙眼」行动，即对指定的某些 App 隐藏 Magisk 的存在。</p>
<p>在 Magisk Manager 的侧边菜单中找到 Magisk Hide 项，选中我们想要隐藏的目标 App 即可。最近更新的 Magisk 19.0 版本还加入了「应用组件」层面进行 Magisk Hide 的功能。</p>
<p></p><figure tabindex="0" class="ss-img-wrapper"><img src="https://cdn.sspai.com/2019/03/31/f82b48893ee0033fc4248c97b7ceed25.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="Magisk Hide 界面" title="Magisk Hide 界面" width="450" data-original="https://cdn.sspai.com/2019/03/31/f82b48893ee0033fc4248c97b7ceed25.png" referrerpolicy="no-referrer"><figcaption class="ss-image-caption">Magisk Hide 界面</figcaption></figure><p></p>
<p>至于对哪些应用进行 Magisk Hide，这个就要看每个读者的具体需要了。一般来说，Google Play 服务和商店是必须的，但也请注意这条来自开发者的注意事项：如无必要，不要<strong>随意</strong>在 Magisk Hide 列表添加 App 而造成滥用（<strong>Do not abuse MagiskHide!</strong>）。</p>
<p>如果你还不放心，还可以去 Magisk Manager 的设置中打开「隐藏 Magisk Manager」。此时 Magisk Manager 将会进行一次重新安装，以便打乱软件包名来躲过对 Magisk Manager 的检测。</p>
<p>至此，Magisk 已经能比较好地向那些对「系统完整性」有苛刻要求的应用隐藏自己。</p>
<h2 id="ss-2-1554264202389">替代 SuperSU 进行 root 权限管理</h2>
<p>大多数用户刷 Magisk ，就是奔着超级用户权限（Superuser）去的，这也是 Magisk 的核心功能。</p>
<p>身兼 root 工具的 Magisk，在这方面的功能可以说是稳扎稳打。用户不必要过度操心，直接使用 Magisk Manager 中的默认设置就能用得舒心。App 向你提请超级用户权限的时候，用户可以选择永久同意、一定时间内同意或者是拒绝，超时之后没有进行选择，那么便会选择拒绝。</p>
<p>进入菜单中的超级用户项，你还可以手动管理已经进行操作过的 App，进行通过或者拒绝，亦或者是删除操作让 App 在下次打开时再次弹窗申请权限。子项目里你可以关闭 App 在使用超级用户权限时的浮动提醒或者是记录。虽然我并不建议这么做，实在厌烦的话还是从心关闭提醒吧。</p>
<p></p><figure tabindex="0" class="ss-img-wrapper"><img src="https://cdn.sspai.com/2019/03/31/31c0bfe67eb16b3561b1bdfbd64fff1a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="关于超级用户的设置" title="关于超级用户的设置" data-original="https://cdn.sspai.com/2019/03/31/31c0bfe67eb16b3561b1bdfbd64fff1a.png" referrerpolicy="no-referrer"><figcaption class="ss-image-caption">关于超级用户的设置</figcaption></figure><p></p>
<p>Manager 设置中的关于超级用户的并不多，但是用户还是可以自定义请求权限弹窗的倒计时时长（默认 10 秒）、对于请求权限的默认处理、开启指纹认证等等。</p>
<h2 id="ss-2-1554264202389">获取、管理 Magisk 模块</h2>
<p>「模块」这个字眼，让许多用户把 Magisk 和 Xposed 这两件完全不同的工具混淆在了一起。</p>
<p>模块的本质，是将原本需要玩家繁复操作的玩机过程与 Magisk「不改动系统」（Systemless-ly） 的特性结合在一起，并进行打包和分发。模块极大地简易了玩机操作，一个小小的 .zip 包文件可能包含了另一套全字重字体，可能囊括了一整套内核参数调教方案，可能附加了一些额外的小功能或是界面美化……模块只是简易了玩机操作的实践，但并没有将它无害化，该翻车的操作还是会翻车，这个时候模块的管理就变得尤其重要。</p>
<p>从获取模块的角度来说，与 Xposed 类似，Magisk Manager 内集成了一个官方的模块仓库，用户在侧边菜单栏中切换到下载便可以查看这个模块仓库。最新更新的模块会显示在靠前位置，方便我们优先挑选那些仍在活跃更新的模块。但令人遗憾的是，模块仓库至今没有分类，你只能选择从这个单一的漫长的列表向下滑去，逐一阅读模块的简介（大多为英文）。</p>
<p>这个时候，英语这门语言工具终于派上了用场，点击模块卡片会具现出模块开发者的说明，里面会标明这个模块的用途、<strong>要求</strong>、<strong>用法</strong>、更新说明、相关的帖子群组链接等等重要内容。我强烈建议<strong>对于未知的模块，应该先仔细完整地阅读一遍此说明</strong>。</p>
<p></p><figure tabindex="0" class="ss-img-wrapper"><img src="https://cdn.sspai.com/2019/03/31/afdb9b939382b1a92def9257a6cb559d.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="以 NotoCJK 为例，仔细查看模块说明" title="以 NotoCJK 为例，仔细查看模块说明" width="450" data-original="https://cdn.sspai.com/2019/03/31/afdb9b939382b1a92def9257a6cb559d.png" referrerpolicy="no-referrer"><figcaption class="ss-image-caption">以 NotoCJK 为例，仔细查看模块说明</figcaption></figure><p></p>
<p>当然了，任何有能力制作模块的开发者都能分发自己制作的模块，也可以选择是否提交到官方的模块仓库。玩机论坛里面你可以看到更多玩家的刷入反馈和测试，著名国外玩机论坛 XDA 还有专门的 Magisk 板块，国内的酷安等交流地也有不少活跃制作模块的开发者。</p>
<p>知道模块可以从哪里得到后，我们要讨论的就是管理问题。管理主要是刷入和卸载两方面。广义地说，任何能给手机刷入 .zip 包的工具都可以进行模块的刷入，比如 TWRP、Magisk Manager 和 Franco Kernel Manager 等，操作也都简单得类似，刷入、重启生效。</p>
<p>今次我们主要讲讲 Magisk Manager：在模块仓库中点击下载，便会自动开始下载、刷入的步骤，刷入完成后你可以选择关闭或者是直接重启生效。模块更新也是一样的步骤。但如果你是手动下载的模块 .zip 包，一切都需要手动。进入模块菜单项，点击下方的加号图标进入文件目录选取目标模块 .zip 包，即可开始模块的刷入或是更新。</p>
<p></p><figure tabindex="0" class="ss-img-wrapper"><img src="https://cdn.sspai.com/2019/03/31/0820b89096fa698160b078fcc0d91b18.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="对模块进行管理" title="对模块进行管理" width="450" data-original="https://cdn.sspai.com/2019/03/31/0820b89096fa698160b078fcc0d91b18.png" referrerpolicy="no-referrer"><figcaption class="ss-image-caption">对模块进行管理</figcaption></figure><p></p>
<p>如果你刷入模块重启能顺利进入系统，那么意味着这个模块的刷入还算安全。在能够进入 Magisk Manager 的情况下，停用某个模块只需要把相应模块的钩子取消掉即可，如果你还想删掉这个模块，一并点击垃圾桶图标删除。停用和卸载都需要重启生效。</p>
<p>可是如果「翻车」进不了系统，那该如何停用和卸载问题模块呢？</p>
<ol>
<li>无论是提前安装好，还是翻车后进入 TWRP 安装，你都需要用到 Magisk Manager for Recovery Mode 模块（仓库中搜索 mm 即可）。翻车后进入 TWRP 中的终端输入使用指令即可开始管理模块，详见该模块的使用说明。</li>
<li>部分模块可以以「同样的模块包，再刷入一次便是卸载」的方式对应进行停用卸载。</li>
<li>痛定思痛，进入 TWRP 刷入 Magisk 的卸载包，卸载一整个 Magisk。</li>
<li>没有 TWRP，保留数据刷写当前系统的完整包。</li>
</ol>
<p>玩机千万条，数据第一条；模块不规范，机主两行泪。</p>
<h2 id="ss-2-1554264202390">Magisk 安装与升级</h2>
<p>Magisk Manager 不光是用于管理 Magisk 的功能行使，也时刻承载着其版本更迭。</p>
<p>每当 Magisk 进行版本更迭的时候，用户就会在 Manager 收到更新推送，一般是先更新 Magisk Manager，再由其来更新 Magisk 本体。有趣的是，和 Google Chrome 类似，Magisk 也具有稳定版、beta 测试版和 Canary 金丝雀版三个版本，都是由开发者官方推出，用户可以根据自己的经验和需要选择对应的版本。</p>
<p>同时，Magisk 是一个开源项目，不少开发者对它也有自己的想法和设计，比如开发 MD2 设计的 Manager，甚至是在 github 上维护一个自己的 Magisk 版本，提供更新链接供用户在 Manager 的设置中填入，从而跟随此版本的开发线。</p>
<p></p><figure tabindex="0" class="ss-img-wrapper"><img src="https://cdn.sspai.com/2019/03/31/574ad91c6d7c8caebb3bbf0106b2914a.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="由开发者 @vsmhell 制作的 MD2 风格的 Magisk Manager" title="由开发者 @vsmhell 制作的 MD2 风格的 Magisk Manager" data-original="https://cdn.sspai.com/2019/03/31/574ad91c6d7c8caebb3bbf0106b2914a.jpg" referrerpolicy="no-referrer"><figcaption class="ss-image-caption">由开发者 @vsmhell 制作的 MD2 风格的 Magisk Manager</figcaption></figure><p></p>
<p>没有刷入 Magisk 的时候，Manager 能做的事情很有限，主要功能就是将原厂的 boot 分区镜像打包成具有 root 权限的镜像，供玩家启动和刷入。详细的步骤已经在本系列第一篇 <a href="https://sspai.com/post/53043" title="《每个 Android 玩家都不可错过的神器（一）：Magisk 初识与安装》">《每个 Android 玩家都不可错过的神器（一）：Magisk 初识与安装》</a> 详细介绍，这里就不多赘述。</p>
<h2 id="ss-2-1554264202390">结语</h2>
<p>Magisk 的设计包含了许多奇妙的构想，呈现到功能上来让人惊呼 Magic。如果想要最大程度地对 Magisk 魔法般的功能善加利用，必须足够熟悉 Magisk Manager。大胆尝试、谨慎操作，补全系统的特性，或是增加自己想要的功能，让手中的设备成为一台梦想机，享受美好的数字生活。</p>
<p><strong>关联阅读</strong>：</p>
<ul>
<li><strong><a href="https://sspai.com/post/53043" title="每个 Android 玩家都不可错过的神器（一）：Magisk 初识与安装">每个 Android 玩家都不可错过的神器（一）：Magisk 初识与安装</a></strong></li>
<li><strong> <a href="https://sspai.com/post/53075" title="每个 Android 玩家都不可错过的神器（二）：保留 Magisk 进行「无痛 OTA」">每个 Android 玩家都不可错过的神器（二）：保留 Magisk 进行「无痛 OTA」</a></strong></li>
</ul>
<p>> 下载少数派 <a href="https://sspai.com/page/client" title="客户端">客户端</a>、关注 <a href="http://sspai.com/s/KEPQ" title="少数派公众号">少数派公众号</a>，发现更多 Android 玩机技巧 😃<br>> 特惠、好用的硬件产品，尽在 <a href="https://sspai.com/post/https-//shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc" title="少数派sspai官方店铺">少数派sspai官方店铺</a> 🛒</p>
</div><div class="update-details-wrap" data-v-0b37afcb></div><!----></div><div style="border:1px solid transparent;" data-v-0b37afcb></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-0b37afcb><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>194</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>9</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-2782" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90Magisk%20Manager%20%E8%AF%A6%E8%A7%A3%E3%80%91Magisk%20%E6%9C%AC%E8%B4%A8%E4%B8%8A%E6%98%AF%E4%B8%80%E7%A7%8D%E6%96%87%E4%BB%B6%E6%8C%82%E8%BD%BD%E7%B3%BB%E7%BB%9F%EF%BC%8C%E8%80%8C%E5%AE%89%E8%A3%85%E5%90%8E%E5%87%BA%E7%8E%B0%E5%9C%A8%E6%89%8B%E6%9C%BA%E9%87%8C%E7%9A%84%20Magisk%20Manager%20%E6%89%8D%E6%98%AF%E6%88%91%E4%BB%AC%E8%A6%81%E9%A2%91%E7%B9%81%E6%8E%A5%E8%A7%A6%E5%88%B0%E7%9A%84%E4%B8%9C%E8%A5%BF%E3%80%82%E4%BB%8A%E5%A4%A9%E6%88%91%E4%BB%AC%E5%B0%86%E4%BB%8B%E7%BB%8D%E5%A6%82%E4%BD%95%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2Farticle%2F7b70798b-da2b-5190-8389-4b7b2ae24a11.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-6822" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90Magisk%20Manager%20%E8%AF%A6%E8%A7%A3%E3%80%91Magisk%20%E6%9C%AC%E8%B4%A8%E4%B8%8A%E6%98%AF%E4%B8%80%E7%A7%8D%E6%96%87%E4%BB%B6%E6%8C%82%E8%BD%BD%E7%B3%BB%E7%BB%9F%EF%BC%8C%E8%80%8C%E5%AE%89%E8%A3%85%E5%90%8E%E5%87%BA%E7%8E%B0%E5%9C%A8%E6%89%8B%E6%9C%BA%E9%87%8C%E7%9A%84%20Magisk%20Manager%20%E6%89%8D%E6%98%AF%E6%88%91%E4%BB%AC%E8%A6%81%E9%A2%91%E7%B9%81%E6%8E%A5%E8%A7%A6%E5%88%B0%E7%9A%84%E4%B8%9C%E8%A5%BF%E3%80%82%E4%BB%8A%E5%A4%A9%E6%88%91%E4%BB%AC%E5%B0%86%E4%BB%8B%E7%BB%8D%E5%A6%82%E4%BD%95%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            