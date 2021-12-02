
---
title: 'Windows 11 安卓子系统：一个半成品'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/8qPWAkFxggm8ME8lyjp0.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 02 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/8qPWAkFxggm8ME8lyjp0.jpg'
---

<div>   
<blockquote><p>编辑导读：Windows是应用最为广泛的系统之一，它的更新设计和技术一直备受互联网人关注。本文作者以Windows 11 安卓子系统为例，对其进行了分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5236903 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/8qPWAkFxggm8ME8lyjp0.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>Windows 11 自公布之日起就承诺要原生兼容 Android 应用，吊足了人们的胃口。这一功能最终命名为“适用于 Android 的Windows 11 子系统”（Windows Subsystem for Android, WSA），10 月底向开发者公布。</p>
<p>航通社对于 Windows 11 以及 WSA 始终保持密切的关注，写了一系列稿件来详细解析。</p>
<p>5 月底的前瞻稿《我们永远也够不着的“下一代 Windows”》已经提到，WSA 将集成开源的 Android 系统（AOSP），但不会内置谷歌服务套件 GMS。</p>
<p>此后，Win11 Build 21996 提前泄露，向外界证实了 Windows 11 的新名称，但没有如约加入对安卓应用的支持，甚至在 Win11 推出第一个正式版时也没有及时上线。</p>
<p>在等待过程中，社长写了《在电脑上装安卓摸鱼，你要感谢一位中国工程师》，详细解释了 Windows 跑安卓的关键技术“英特尔 Bridge”，其前身 Houdini 以及领衔开发的中国工程师李剑慧。</p>
<p>如今，WSA 推出已经一个月，社长也是时候总结一下它阶段性的使用体验了。很遗憾，只能说现在的 WSA 还是一个“半成品”，有很多缺陷，而且更面向开发者而非普通用户。鉴于以往经验，微软也有可能长期无法修补这些缺陷和问题。</p>
<h2 id="toc-1">一、安装过程极其复杂</h2>
<p>两周前，在微软中国官方微信号“微软科技”上，发布了一篇教程《抢先体验！如何在 Windows 11 上运行 Android 应用》。其中涉及大量的命令行以及复杂的文件名，甚至还包含一个非微软官方的网址。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/BrhmFxXVulijPSDNyPnY.png" referrerpolicy="no-referrer"></p>
<p>大哥，你是微软官方号啊……</p>
<p>这说明什么？现在体验 WSA 的过程就是如此繁琐，没法更简单了。</p>
<p>WSA 刚推出的时候，号称在微软商店（Microsoft Store）下载“亚马逊应用商店”即可自动安装，无需手动配置。但是首先，你需要加入 Windows Insider 将你的系统变成不那么稳定的测试版。</p>
<p>你的电脑需要满足 Windows 11 的最低系统要求，包括 CPU 在支持列表内，且内存大于 8 GB，还需要在 BIOS/UEFI 启用虚拟化功能。</p>
<p>对于 Surface 等特殊机型而言，开启虚拟化意味着你需要首先启用 Hyper-V 功能，而这是仅在 Win11 专业版才有的功能，大多数机型预装的正版 Windows 都是家庭版。Hyper-V 也可能会跟其它虚拟化技术比如 VMWare 相冲突。</p>
<p>接下来，要将微软商店更新到最新；将电脑的区域设置为美国，使用美国 IP 并申请一个美亚账户，来使用“亚马逊应用商店”。这些都搞完以后，你会发现亚马逊应用商店只有 50 几款应用可供选择。</p>
<p>在中国境内完全无法使用“亚马逊应用商店”，你可以用亚马逊国区账号登录，但接下来就是白屏，显示此服务不在你的国家提供。将账单地址改为美国也不行。</p>
<p>国内用户不论电脑配置是否符合要求，都必须通过上述“微软科技”提供的复杂方式间接安装，在非官方的网站获取 WSA 安装包的下载地址。</p>
<p>如果挂上魔法工具直通美利坚，那么跟 Linux 子系统（WSL）的情况一样，整个虚拟机都无法上网了，百度也打不开。这个问题目前没有完美的解决办法。有的资料说，对于 WSL 而言，可以在主机的“设备管理器”禁用 Linux 虚拟机的网卡，待主机连接虚拟专用网后再启用，但 Android 系统就没有网卡这种东西。</p>
<p>好在 WSA 支持侧载，也就是可以直接安装 APK 包，我们也只能用这个方式。但过程相当复杂，需要使用多个命令行条目。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/xIuQw19Ex5vMRjX7MgYO.png" referrerpolicy="no-referrer"></p>
<p>侧载 APK 包的步骤是：下载 ADB 调试工具 → 在命令行中运行并连接到虚拟机 → 输入命令以安装 APK（具体方法可以参考上述教程）。安装好的应用会出现在开始菜单，并且可以用开始菜单的右键，或者“设置-应用”等方式卸载。</p>
<p>一位意大利开发者 Simone Franco 开发了图形界面工具 WSATools，它让 APK 安装变得简单：只需双击一下就可以，不需要了解和安装 ADB。如果在你的 PATH 中已经有了 ADB 包，它将直接调用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/qamXbLUzgAnJEraNQ4f1.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/HkEJDzy1OAPOziPHLTb9.png" referrerpolicy="no-referrer"></p>
<p>当然，侧载 APK 并不能解决对谷歌服务的依赖。同样，也有国外大神研究出了让谷歌 Play 商店进驻 WSA 的方法，但难度比上面说的还要高，似乎让人又回到了当年折腾安卓刷机的那段日子。因为我们不能使用魔法，所以不必考虑谷歌的问题。</p>
<p>WSATools 上架微软商店后一度被下架，引发猜测。微软后来跟作者解释说，他需要做一个微小的改动，且最好不要使用 WSA 这种容易和微软官方混淆的名称。在满足条件后，即可恢复上架。</p>
<p>WSATools 入住商店代表了 Win11 带来的一个好的迹象，即商店开始吸引更多的开发者。微软对作者“无微不至”的关怀也是想给其它开发者吃下定心丸，不过带来了一个副作用——让人觉得微软已经放弃了官方改善 WSA 易用性的努力。</p>
<h2 id="toc-2">二、应用适配非常“拉胯”</h2>
<p>在可以用正常方式体验 WSA 的美国，The Verge 编辑 Tom Warren 分别在 Surface Pro X 和一台基于酷睿 i9-11900K 的游戏台式机上开展了体验。由于 Surface Pro X 是 ARM 架构，它并不需要 Bridge 转译机制，理论上可以更平滑地运行。</p>
<p>这两个机型都满足（大大超越了）WSA 最小系统需求，因此可以不用破解安装。在官方商店安装“亚马逊应用商店”的过程相当简便，Windows 11 会在后台静默安装 WSA。</p>
<p>如同上面讲过的，Android 应用和原生 Windows 应用、固定在开始菜单的网页应用（PWA）看起来一样，用户可以将其随意固定到开始菜单或任务栏上、支持全局搜索、窗口缩放和多任务同时运行。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/229nvfisdt1AGuJ0D4dP.jpeg" referrerpolicy="no-referrer"></p>
<p>亚马逊应用商店里的 50 款 Android 应用包含 Kindle……以及一系列冷门手游。不过在 Surface Pro X 上运行游戏的体验也相当不友好，低帧率和卡顿是常态。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/MnImYCzPU6uHXsEgdPQX.jpeg" referrerpolicy="no-referrer"></p>
<p>在体验《最终幻想 15》游戏和某些应用时，如果你尝试调节窗口大小，就会闪退。如果尝试让四个 Android 游戏并排放置那就会突然变卡，直到 CPU 占用率在几秒钟后恢复正常。</p>
<p>当然，这已经是最规矩和最理想的用法了。那么在社长的电脑上呢？</p>
<p>社长使用的是 Surface Go，它的 CPU 并不满足 Win11 系统要求，平时写稿都可能偶尔崩溃；而且因为在中国，就只能用非官方手段安装 WSA，也加重了不稳定性。再加上我们需要测试一些国产应用，它们的开发方式各不相同，可能出现奇怪的症状。</p>
<p>不过，之前用的 VMWare 和网易 Mumu、雷电之流（以 VirtualBox 为基础开发）都还好好的。那么，运行 WSA 的效果如何？</p>
<ul>
<li>淘宝：可以打开，会在登录页面强退。</li>
<li>央视频：多试几次以后才能跳过引导画面进入首页，只要打开视频或直播就会强退。</li>
<li>应用宝：APK 下载后不知道存在哪里，也不能用文件关联打开，所以没有用处。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ISmTl26JUXmMIBmA9NaV.png" referrerpolicy="no-referrer"></p>
<p>ES 文件管理器：可以使用非 Root 功能。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/FcItioFNDFfolcnnbFka.png" referrerpolicy="no-referrer"></p>
<p>微软亲儿子“你的手机助手”：提示“设备不支持运行所需的移动服务”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ZKIdndTdwOWPt9MgYMWX.png" referrerpolicy="no-referrer"></p>
<p>抖音：强退 4-5 次以后才能进入，偶尔可以显示视频，偶尔黑屏。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/d4NXGk4ojo2wv1LdpHEv.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ZvswsbJxs0MjRkniYAPp.png" referrerpolicy="no-referrer"></p>
<p>微信：视账号不同，有的可以正常进入，有的停留在“微信安全”验证界面不动。由于有封号的风险，所以每个负责任的教程都会让你谨慎使用微信。</p>
<p>大型游戏：没有亲测，但有人测试说打完一局《王者荣耀》就被封号了两小时。</p>
<p>总结下来，WSA 在社长的电脑上有以下问题：</p>
<ul>
<li>不能调用摄像头（前后都是）。</li>
<li>硬件加速不可用（因为 Surface 系列用了特殊的显卡驱动），所以除抖音之外，没有成功在其它应用上看视频，游戏也就用不着测试了。</li>
<li>闪退频繁，且不知道原因。</li>
<li>遇到账号验证和登陆环节，大概率都会闪退。</li>
</ul>
<p>上述问题使得眼下的 WSA 基本不可用。而它至少会占用你 5GB 的硬盘空间；装好以后，再装一个淘宝或一个抖音就 200-300M 了，而如果敢装微信，用上半年以后就是十几个 G 的空间占用了。</p>
<h2 id="toc-3">三、有趣的地方：安卓与 Win11 深度耦合</h2>
<p>WSA 尽管可用性差，但它野心勃勃。跟我们熟悉的安卓模拟器相比，它并非在“沙箱”里运行，也不是完全隔离于 Windows 主机，正是这些对原生安卓的“魔改”一定程度上拖累了它的性能，但也预示着一些有趣的变化。</p>
<p>WSA 的设置界面只能访问安卓子系统的“文件”应用，其自带的系统设置被隐藏了。但是我们可以另辟蹊径去看看，方法是安装一个第三方的启动器（Launcher），例如微软的“微软桌面”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/T3MthoADmzcXyb81bUaP.png" referrerpolicy="no-referrer"></p>
<p>虽然装好后启动要等待一阵，也可能会突然强退，但进入桌面以后你就可以看到熟悉的齿轮图标，点击即可进入安卓系统的设置界面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/wlX5pKCriRxA4rq0exSO.png" referrerpolicy="no-referrer"></p>
<p>在这里可以发现，WSA 提供了 256GB 的虚拟存储空间（非实际占用），存储空间满了也是要清理的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/SDlR5WffBB1z3XFGaJcG.png" referrerpolicy="no-referrer"></p>
<p>但是如图所示，社长只装了 5 个应用，实际占用硬盘空间不到 6G，在虚拟机中却显示已使用 50% 即 128 G；其中应用所占的空间 3.1G 是正常计数的。——反正不影响使用，不管了。</p>
<p>此外，不同于 WSL 可以在“此电脑”访问 Linux 盘符，Android 的存储系统不能在主机的“此电脑”显示，主机的硬盘内容也不能在 Android 里调用，是相互隔离的。</p>
<p>网络连接里面有一个虚拟的 WiFi 信号连接到外部 Win11 主机的网络，电池则永远是 100%。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/qVO2Xxyx59NZgoQfOppU.png" referrerpolicy="no-referrer"></p>
<p>声音部分，它的音量是不可调节的，跟外部一致。你在外部主机的音量多大，它的音量就多大。</p>
<p>设置项中的“应用和通知”“隐私权”“位置信息”“无障碍”等，点击以后都会直接打开上层 Win11 系统“设置”的相应项目，这一点非常神奇。</p>
<p>比如，点进“应用和通知”，点“默认应用”就会弹出主机的“默认应用”设置界面。这里也不提供卸载功能，用户需要在主机的开始菜单或设置里卸载应用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/EjvjVWSPj7JK3VVpehmQ.png" referrerpolicy="no-referrer"></p>
<p>“无障碍”部分的“显示大小”即 dpi 设置，与你主机上的 dpi 设置相同，例如图中是放大到 200%。不过，深色主题是可以与系统设置不同的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/9IrxPbB03ROIVbmC2jR9.png" referrerpolicy="no-referrer"></p>
<p>WSA 输入字符时会调用主机 Win11 的输入法，即使你自行安装了别的输入法 APK，也不会调用。</p>
<p>上面已经说过，WSA 的文件关联也被 Win11 接管了，所以才会出现打开 APK 安装包时弹出了 Win11“打开方式”对话框的问题。这也意味着你可以将安卓应用设置为打开电脑上文件的方式；</p>
<p>然而又因为上面说的文件系统不互通问题，实际上你是打不开的。例如，你在 WSA 装了一个 WPS 手机版，尝试打开电脑上的文档时，会停留在 WPS 的首页，因为它找不到你的文档。</p>
<p>因此，我们可以推测出 WSA 在今后一段时期迭代更新所需要攻关解决的突出问题，最重要的就是打通文件系统。</p>
<p>Android 是基于 Linux 但又不完全是 Linux，而且谷歌不断在大版本更新之后，逐级提升 Android 文件系统的安全性，使得对其逆向工程越来越困难。社长并不确定微软真的能最终搞定两个系统互相访问文件的问题。</p>
<p>另外，如果最终目标是让消费者像安装 x86 应用一样简单方便地安装使用 APK，两个系统的设置界面还需要在此基础上进一步整合。</p>
<p>不过，如今的 WSA 显然并不是为普通用户准备的，只是希望开发者过来看看而已，所以社长也并不确定微软是否还有意改善产品的易用性。</p>
<h2 id="toc-4">四、结论</h2>
<p>WSA 消息一出，各大安卓模拟器厂商都在颤抖。有个梗图（假的）说蓝叠（Bluestacks）在推特发了一条消息：“Fuck”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/YHeQTdHvn7yD7Tn3QUd4.jpeg" referrerpolicy="no-referrer"></p>
<p>（顺便一提，蓝叠开发了在浏览器中运行安卓“云游戏”的技术。）</p>
<p>但现在看来模拟器们可以大大的松一口气了。</p>
<p>不得不遗憾的说，WSA 到目前为止还是一个“半成品”。之前承诺的安装安卓应用的能力，实际上大打折扣。</p>
<p>相比之下，苹果推出的 Rosetta 2 转译功能是完成度非常高的，加上一体化的 M1 处理器，达到了基本不需要等待的效果。Windows 10 开始引入的 Linux 子系统的运行效果也好很多，这也许是因为不需要跨指令集。</p>
<p>但 WSA 是真的不行。这个测试阶段的体验，远远不能达到微软在发布会上所宣传的那种程度。</p>
<p>就像 Windows 此前的很多功能一样，WSA 是还在开发中就被人研究了个底朝天，没有半点神秘感。苹果不可能干出这种事情。它不会轻易许下承诺，不希望外界窥探到正在开发中的半成品，也不会容忍半成品推向市场，比如放弃了 AirPower。</p>
<p>好在，换个方式理解，这就意味着 WSA 还有很大的潜力，可以在日后开发中逐渐把当初的坑都填上。只是我们不知道它会不会最终成功填坑，这取决于 Windows 开发部门设定的目标，以及具体开发是否会更困难——如果太困难了，就可能干脆整个扔掉了。</p>
<p>对于翘首以盼 Windows 兼容安卓然后上班摸鱼的用户，一个最简单的建议是：</p>
<p>再等等吧。</p>
<p>📕 参考资料</p>
<ul>
<li>https://mp.weixin.qq.com/s/LuZT8j0xpaMxR7EEQ7PXKA</li>
<li>https://www.microsoft.com/zh-cn/p/app/9n4p75dxl6fg</li>
<li>https://www.theverge.com/22737102/microsoft-windows-11-android-apps-support-feature-hands-on</li>
</ul>
<h3>#专栏作家#</h3>
<p>书航，微信公众号：航通社 （ID：lifeissohappy），人人都是产品经理专栏作家。提供全原创科技新闻和观点。为您呈现文字有力、观点鲜明、打动人心的文章。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5235250" data-author="662354" data-avatar="http://image.woshipm.com/wp-files/2019/03/fFpQLZFQwHw7mXx5HRl7.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            