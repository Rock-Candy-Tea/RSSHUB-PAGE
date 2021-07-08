
---
title: '谷歌弃用 APK 格式，替代品 AAB 有何优势？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210708/v2_ebabb9895b9b4d0abc6d2dab4c530b53_img_000'
author: 36kr
comments: false
date: Thu, 08 Jul 2021 10:52:08 GMT
thumbnail: 'https://img.36krcdn.com/20210708/v2_ebabb9895b9b4d0abc6d2dab4c530b53_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/MINFYEOOJQGyvEhB94VtWQ">“CSDN”（ID:CSDNnews）</a>，整理：郑丽媛，36氪经授权发布。</p> 
<p>Android 用户想必对 APK 并不陌生。APK 是 Android Package 的缩写，即Android 安装包，基于 ZIP 压缩包格式，通过把 Android SDK 编译工程打包成一个 Android 系统支持的安装程序文件，几乎所有 Android 应用程序都以这种格式发布。</p> 
<p>但自下个月起，APK 格式要被<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>弃用了。</p> 
<p>近日，谷歌宣布：自 2021 年 8 月起，Google Play 将要求开发者以 Android App Bundle （以下简称 AAB）格式发布新应用，该格式将取代 APK 作为标准发布格式。</p> 
<h2 label="一级标题" style>为何要从 APK 转变为 AAB？</h2> 
<p>一直以来，Android 首选的应用程序包就是 APK，而一个 APK 中往往包含应用代码、图片、音频和开发者生成的应用签名密钥等大量资源。</p> 
<p>不仅如此，由于 Android 设备规格各异，开发人员还需根据设备的不同屏幕密度（320dpi、480dpi 等）、处理器（ARM、ARM64、x86）、用户所在的不同地区，在 Google Play 中构建和上传多个 APK，以此才能在用户点击“安装”时，在其设备上安装最适配的 APK。</p> 
<p>但在这种情况下，应用开发者便承受太多：不仅要开发应用，还要管理许多 APK 以支持大量设备。因此为了省时省力，大多数开发者通常都会选择构建一<a class="project-link" data-id="66837" data-name="个通" data-logo="https://img.36krcdn.com/20200729/v2_63b69181aa5a41369459fccdd8c272b3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/66837" target="_blank">个通</a>用 APK，即包含语言包、代码等在内的所有资源。不论用户身处何处、使用何种规格的设备，只需下载这个通用 APK 即可。</p> 
<p>说到这里，你或许发现了问题所在：包含所有资源的通用 APK 太大了。用户分明只需其中与自己设备相适配的资源，却要把整个 APK 都下载下来，不仅延长了安装时间，也占用了更多的带宽。</p> 
<p>为了解决这个问题，谷歌在 2018 年 Google I/O 大会上推出了 AAB 格式，希望以此减少开发者的负担，同时也有助于减少应用大小、安装时间和带宽消耗，提高用户体验。</p> 
<p><img src="https://img.36krcdn.com/20210708/v2_ebabb9895b9b4d0abc6d2dab4c530b53_img_000" data-img-size-val="1080,789" referrerpolicy="no-referrer"></p> 
<p>简单来说，AAB 格式其实并不是一个全新的应用安装包，你可以将它当做一个容器，里面包含着一个基本 APK 和多个用于特定配置的 APK。</p> 
<p>而谷歌在这之中则充当“筛选”的角色：一旦开发者选择使用 AAB 格式发布应用，谷歌就会根据用户的设备配置从中生成优化后的 APK 提供给用户。对用户而言，这样的 APK 体积小、安装快，对开发者来说也省事：不必再为各种设备管理一大堆 APK。</p> 
<p>因此，总体来看，谷歌要求下个月以 AAB 格式发布新应用的决定主要面向开发者，对用户而言影响不是太大，因为最终在设备上安装 Android 应用的打包格式还是 APK。</p> 
<h2 label="一级标题" style>AAB 的优势</h2> 
<p>相较于 APK，AAB 自然有其独一无二的优点。</p> 
<p>首先便是上文所提到的应用体积缩小。据谷歌官方介绍，使用 AAB 生成优化的 APK 体积平均会比一般的 APK 小 15%，而这一数据会根据应用大小有较大起伏。例如 Airbnb 在从 APK 切换到 AAB 格式后应用大小减少了 22%，而 Netflix 更是减少了 57%。</p> 
<p><img src="https://img.36krcdn.com/20210708/v2_ff71c1801625498fae930c447e59ba04_img_000" data-img-size-val="584,554" referrerpolicy="no-referrer"></p> 
<p>其次，AAB 的 Play Feature Delivery 功能可自定义将哪些功能模块交付给哪个设备，支持安装时交付、按条件交付和按需交付等三种模式。这也就是将应用的功能拆分开来，以此大幅缩短用户下载应用的时间，其中没用的功能用户可以不下载或等到以后需要时再下载。</p> 
<p>还有一个 Play Asset Delivery 功能，以动态方式交付大型资源可以减少用户等待时间，同时缩减交付成本。即使用 Play Asset Delivery 的游戏可通过纹理压缩格式作为交付条件，以便用户只获取适合其设备的资源，避免浪费空间或带宽。</p> 
<h2 label="一级标题" style>对于 AAB 的担忧</h2> 
<p>虽然从结果看来，以 AAB 格式分发新应用对开发者和用户都有益处，但还是有部分人对此有些担忧。</p> 
<p>有人担心从 APK 变为 AAB 格式会太复杂。但谷歌表示：“对于大多数应用而言，构建 AAB 文件来替代 APK 文件仅需要少量工作。”它指出 App Bundle 是一种受主流构建工具支持的开源格式，因此在 Play Core 原生 SDK、Play Core Java SDK 和 Play Core Kotlin SDK 的助力下，无论用户偏好哪种编码环境，都可以轻松开始使用可选的高级 App Bundle 功能。此外，AAB 的要求仅适用于新应用，现有应用及面向特定 Google Play 用户的私人应用目前无需遵从此要求。</p> 
<p>有人对与谷歌共享私人签名密钥表示担忧（签名密钥是验证 APK 完整性的重要信息，谷歌从 ABB 中生成优化的 APK，因此签名密钥也将包含在 ABB 中），对此谷歌表示，所有“签名密钥都将存储在谷歌用来存储自己的密钥的同一基础设施上” ，因此开发者的私人签名密钥都会受到严密的安全保护。</p> 
<p>还有人担心因为 AAB 不能在 Google Play 以外的地方下载，会对如亚马逊应用商店等第三方应用商店造成很大影响。但据了解谷歌已经开发了一个名为 bundletool 的开源工具，允许开发人员从 AAB 包中创建 APK，因此想在第三方商店中发布 Android 应用程序的开发人员可以手动导出其应用的 APK 版本。</p> 
<p>那么对于谷歌的这一决定，你有什么看法吗？</p> 
<h3 label="二级标题" style>参考链接</h3> 
<ul class=" list-paddingleft-2"> 
 <li><p>https://beebom.com/apk-vs-aab/</p></li> 
 <li><p>https://mp.weixin.qq.com/s?__biz=Mzk0NDIwMTExNw==&mid=2247493854&idx=1&sn=cfccb6ee2d3556fa6cd35ba3a4125df5&chksm=c32ae42cf45d6d3a014e2c148917072dce17fa0524274ee2d90cd7ca7a5a8710f1308a016a7a&mpshare=1&scene=1&srcid=0708jLyLA5vdqSK37gE3fhkj&sharer_sharetime=1625703670494&sharer_shareid=a9f601a40d19fefc258fa43968f938c3&version=3.1.8.3108&platform=win#rd</p></li> 
</ul>  
</div>
            