
---
title: '不想被 XX 卫士、XX 管家拖慢电脑？你还可以试试这 10 个小巧精致的 Windows 软件'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220207/v2_745793aaa227443f9364066ba8694fb9_img_000'
author: 36kr
comments: false
date: Mon, 07 Feb 2022 05:41:14 GMT
thumbnail: 'https://img.36krcdn.com/20220207/v2_745793aaa227443f9364066ba8694fb9_img_000'
---

<div>   
<p>在几年前下定决心告别 Windows 上的 xx 大师、xx 卫士后，在一段时间内我会感到些许不适。倒不是因为不习惯没有人告诉我开机花了几分几秒，而是这些无所不包的管家们的确能提供一些特别好用的小工具，比如解除文件占用、右键编辑、广告弹窗拦截等等。</p> 
<p>好在后来我发现这些小功能可以用一些更简单纯<a class="project-link" data-id="186586" data-name="净的" data-logo="https://img.36krcdn.com/20210809/v2_efedefef3f9d405ea92899564441aa2a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/186586" target="_blank">净的</a>应用来实现。本文介绍的就是我搜集到的一些工具，它们绝大部分为便携软件，无需安装、点开即用，体积也非常小巧，大都保持在几 MB 内。</p> 
<p>需要说明的是，因为功能场景和所应对的需求特殊，本文提到的大部分应用都会访问系统内核、修改注册表或某些关键文件，因而可能会被一些安全软件误认为是病毒，保证下载来源正规的前提下需要手动将它们添加进白名单。另外，使用前也请做好备份以防万一。</p> 
<h2 label="一级标题" style><strong>OpenArk：快速定位快捷键和文件占用</strong></h2> 
<p>🔗 下载链接：https://github.com/BlackINT3/OpenArk/</p> 
<p>Windows 应用可以注册两类快捷键：适用于特定线程的快捷键和全局快捷键，前者只有当特定窗口被激活时才会响应，而后者则全局生效。当某应用注册的全局快捷键和其他程序调用的按键冲突，应用功能就会异常。</p> 
<p>想要知道究竟是哪个应用占用了快捷键，可以打开 OpenArk，进入 <strong>内核 > 系统热键</strong> 界面，然后选择 <strong>进入内核模式</strong>。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_745793aaa227443f9364066ba8694fb9_img_000" referrerpolicy="no-referrer"></p> 
<p>此时应用会列出已注册的全局快捷键供我们搜索。譬如说，我们需要知道哪个应用占用了 <strong>Ctrl + Alt + Up</strong>（注意输入顺序），可以在界面下方的过滤器拦中输入相应的快捷键名称，不难发现是<a class="project-link" data-id="30367" data-name="网易" data-logo="https://img.36krcdn.com/20210806/v2_cef2901dde7f474d9121c11fec2c841d_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/30367" target="_blank">网易</a>云音乐注册了此按键组合。接下来，在网易云中做修改即可解除占用状态。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_9abd94ff70254fa89a33a3a87c298fc0_img_000" referrerpolicy="no-referrer"></p> 
<p>与快捷键被占用的情况类似，我们偶尔也会遇到某些文件无法打开，无法删除的情形。这大概率是因为该文件正在被其他应用使用。OpenArk 同样为此情况提供了解决方案：进入 <strong>内核 > 存储管理界面</strong>，选择 <strong>进入内核模式</strong>，键入文件路径，点击查看占用，应用便会展示所有使用了该文件的进程。之后，利用界面右下侧的解锁选项便能再次自由操作此文件了。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_d66f0ef4759e4c82a26851fbcc4fda7e_img_000" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style><strong>Cursor Highlighter：高亮鼠标光标</strong></h2> 
<p>🔗 下载链接：</p> 
<p>https://github.com/wendoufu/surl/releases/tag/CusorHighlighter</p> 
<p>在录制软件教程亦或线上教学时，收到最多的是观众或学生们「看不见您鼠标<a class="project-link" data-id="636965" data-name="光标" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/636965" target="_blank">光标</a>在哪」的反馈。Windows 默认给的鼠标光标过小，要是对方用的还是移动设备，能看得清鼠标才奇怪。解决方案是像下图一样用显眼的色块标注鼠标位置，或者制造局部高亮效果。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_c044e763a7304bdbaf4e61d22a2ae626_img_000" referrerpolicy="no-referrer"></p> 
<p>Kevin Stratvert 用一个浅显易懂的视频介绍了高亮鼠标的几种方案，其中属 Cursor Highlighter 功能最全，使用最简单。这个小巧的应用允许用户使用快捷键在正常/色块/高亮三种模式下快速切换，不同模式下鼠标的显示效果也能完全自定义。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_f0e103b2815241eda043958d1658ea7e_img_000" referrerpolicy="no-referrer"></p> 
<p>下载 exe 文件后，双击即可运行。其设置界面需要通过右键系统托盘的图标唤出。</p> 
<h2 label="一级标题" style><strong>Context Menu Manager：编辑右键菜单</strong></h2> 
<p>🔗 <strong>下载链接</strong></p> 
<p>Windows 10：</p> 
<p>https://github.com/BluePointLilac/ContextMenuManager</p> 
<p>Windows 11： </p> 
<p>https://github.com/ikas-mc/ContextMenuForWindows11</p> 
<p>Windows 的右键菜单由分散在各处的注册表控制，不少用户有精简或者自定义右键菜单的需求。但无论是在不同应用中分别设置，还是手动编辑注册表值实际上都不太方便，Context Menu Manager 则整合了系统各处的右键注册表条目，并赋予它们简单的 GUI，使这项任务方便了不少。</p> 
<p>如下图所示，该应用将右键条目们按位置分门别类，从 Windows 徽标到某个具体文件类型，无所不包。具体到某个条目，我们能调整其图标、条目位置、命令等属性。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_686e3140eae94d9e8a2eef1eac4c2ce4_img_000" referrerpolicy="no-referrer"></p> 
<p>Windows 11 的新式右键菜单不能使用该软件编辑。我们要么利用注册表文件全局还原旧的菜单样式，要么使用 Custom Context Menu。</p> 
<p>Custom Context Menu 可以向 Windows 11 的新右键添加一个自定义菜单分组。分组的名称可以在应用右下方的设置中定义。需要添加新条目时，先点击应用界面左上方的加号，键入菜单详情，点击保存，最后重启资源管理器即可生效。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_9e3c972909954cdc9196698a55670f94_img_000" referrerpolicy="no-referrer"></p> 
<p>向右键添加命令的方式和要点可以参看另一篇文章：<a href="https://36kr.com/p/1604583201671688">巧用注册表和命令行，把鼠标右键打造成你的专属工具箱</a>。</p> 
<h2 label="一级标题" style><strong>O&O ShutUp10++：Windows 隐私设置整合</strong></h2> 
<p>🔗 下载链接：</p> 
<p>https://www.oo-software.com/en/shutup10</p> 
<p>如果你和笔者一样，不太喜欢 Windows 默认启用的各种使用建议和数据收集，例如锁屏的小提示、开始菜单的 Edge 推广，那么就一定能理解在注册表、设置、组策略等各处翻转腾挪的痛苦。O&O ShutUp10++ 正为了解决这一困境而生。</p> 
<p>它采用了修改注册表的方式，将百余个 Windows 建议、数据收集相关的开关集中在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>。除了包含设置面板中已有的各类隐私设置，也有诸如彻底关闭数据上传、关闭网络搜索等被系统隐藏的选项。首次配置后，可以使用导出功能将配置保存以供下次直接导入。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_c72793e8c4a04bbebdbdd8425dabec20_img_000" referrerpolicy="no-referrer"></p> 
<p>ShutUp10++ 的中文翻译质量不佳，读者只要记得：绿色状态意味着更少的数据上传和建议，红色反之。部分条目关闭后会影响系统安全或更新，应用有特殊标注。</p> 
<h2 label="一级标题" style><strong>AdwCleaner：删除恶意软件和广告</strong></h2> 
<p><strong>注意：此软件默认会卸载腾讯系软件。</strong></p> 
<p>🔗 下载链接：</p> 
<p>https://www.malwarebytes.com/adwcleaner</p> 
<p>AdwCleaner 由老牌安全公司 Malwarebytes 开发，免费开放给公众使用。麻雀虽小，五脏俱全。它主要的作用是比对云端数据库，删除本地的各类恶意软件，某些应用注册的弹窗程序、在注册表做的小动作它也能检测出来并删除。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_45c30e2d13e6454294b87db7addf3e77_img_000" referrerpolicy="no-referrer"></p> 
<p>此外，应用也提供了重置 Hosts、重置浏览器策略等实用功能，在遇到浏览器主页或域名被劫持时可以尝试。</p> 
<h2 label="一级标题" style><strong>WinDirStat：磁盘占用分析</strong></h2> 
<p>🔗 下载链接：https://windirstat.net/download.html</p> 
<p>如果读者时常有「我的硬盘空间都<a class="project-link" data-id="3968556" data-name="去哪儿" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968556" target="_blank">去哪儿</a>」的疑问，那么 WinDirStat 可能很适合你。这款 开源 小工具能分析指定磁盘或文件夹，然后给出不同目录及不同种类文件的空间占用情况。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_1c5df9a8eb5e4d6d9248dd6dc3990733_img_000" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style><strong>Autoruns：应用自启动管理</strong></h2> 
<p>🔗 下载链接：</p> 
<p>https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns</p> 
<p>Windows 第三方应用想要自启动大致有三种实现方式：注册自动运行的服务、创建开机启动的计划任务、写入特定注册表。而任务管理器和 Windows 设置中的「启动」面板只会显示采用最后一种形式的应用，因而会出现一些应用明明开机自启，用户却找不到开关入口的情况。</p> 
<p>Autoruns 将系统各个启动项整合在了一起，方便用户统一查看管理。以管理员权限打开此应用，Logon 栏是所有利用注册表自启的应用，Scheduled Tasks 栏展示注册了任务计划的应用，Service 栏中有所有设定为自动启动的服务项。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_64bd70148d834fbeaa108e47990c4099_img_000" referrerpolicy="no-referrer"></p> 
<p>选中条目右键即可禁用或者删除这些项目。编辑时应注意两点：首先，建议勾选 Entry > Hide Windows Entries 以防止对 Windows 本体的误操作；其次，只编辑自己了解作用的条目。</p> 
<p>Autoruns 是<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a> Azure 现任 CTO Mark Russinovich 领导开发的 Sysinternals Suite 的几十个小工具之一。除了能通过文中给的链接获得，也能直接在 Microsoft Store 下载。</p> 
<h2 label="一级标题" style><strong>Process Monitor：应用进程监控</strong></h2> 
<p>🔗 下载链接：</p> 
<p>https://docs.microsoft.com/en-us/sysinternals/downloads/procmon</p> 
<p>Process Monitor 同属 Sysinternals Suite，其作用是监控一个进程读写了哪些文件、哪些注册表、进行了哪些网络通信。</p> 
<p>如图所示，打开应用后，利用工具栏中的窗口选择工具（瞄准镜头图标），拖动鼠标到目标进程，Process Monitor 就会展示其应用活动。工具栏右侧为控制监控类型的开关。我们亦能通过 Filter 功能进一步控制监控的内容。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_f3618d8de6fa4b789e681ecd874ebe73_img_000" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style><strong>UsbEAm Hosts Editor：管理和修改 Hosts</strong></h2> 
<p>🔗 下载链接：</p> 
<p>https://www.dogfight360.com/blog/475/</p> 
<p>虽然市面上已经有不少 Hosts 管理工具，但它们大多数都只是一个编辑器，什么域名映射到什么 IP 还得用户自己去试。UsbEAm Hosts Editor 的特色是将测试延迟 > 记录 IP > 编辑 Hosts 集成在一起，并预置了大多数游戏平台和联机游戏的域名，用户不必再去自行搜索。我们仅需两三次点击，就能应用到理想的 Hosts。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_06507384b158442e95abbe1265eb6a6f_img_000" referrerpolicy="no-referrer"></p> 
<p>除了对游戏玩家较为友好，此应用还预置了 Microsoft Store、GitHub 等平台，有相关需求的读者亦可以尝试。</p> 
<h2 label="一级标题" style><strong>NirSoft 工具</strong></h2> 
<p>提到小工具，自然少不了声名远扬的 NirSoft，它们十余年来开发了百余个免费的 Windows 工具，这里仅举几例。</p> 
<p>要是读者曾经使用过注册表编辑器，就不难发现这个历史悠久的 Windows 组件非常难用。现代编辑器该有的撤销、导出单个条目等功能它一概没有，尤其是查找命令，一次只显示一个结果，非常低效。RegScanner 就是对编辑器查找功能的增强：除了更复杂的匹配命令，它的优势在于一次展示所有结果。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_76394ddd85af491493b9ba24f78aa1fa_img_000" referrerpolicy="no-referrer"></p> 
<p>再比如 WirelessNetView，它也像系统的 WIFI 连接指示器一样显示所有 WIFI，但提供了更详细的信息。其中最有用的莫过于连接强度了。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220207/v2_09bfc9963e30403a9b9f959498a21bb6_img_000" referrerpolicy="no-referrer"></p> 
<p>从上面的例子可以看出，NirSoft 的应用大多是对 Windows 系统功能的扩展或增强。不少工具除了有 GUI，也提供了命令调用的方式，倒是很符合「Do one thing, do it well」的哲学。</p> 
<p>NirSoft 所有工具能在 https://www.nirsoft.net/utils/index.html 的列表中找到。</p> 
<p>当然了，Windows 平台上类似的小工具其实还有很多，如果你有什么日常使用、想要推荐的实用小工具本文没有提及，也欢迎在评论区分享。</p> 
<p>原文链接：https://sspai.com/post/71216 </p> 
<p>作者：Mirtle </p> 
<p>责编：克莱德 </p> 
<p>题图来自 Unsplash：@abeso</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247530293&idx=1&sn=e158756b5bf9da125c25ca3ab352edbc&chksm=fdb3825fcac40b49a106a5442abf55849fb734f6f346e4b0614ae7c48e5649a589e0652576ea#rd">“少数派”（ID：sspaime）</a>，作者：321，36氪经授权发布。</p>  
</div>
            