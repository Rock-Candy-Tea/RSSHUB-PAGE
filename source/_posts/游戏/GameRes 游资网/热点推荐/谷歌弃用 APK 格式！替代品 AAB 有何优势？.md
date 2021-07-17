
---
title: '谷歌弃用 APK 格式！替代品 AAB 有何优势？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/09/140103keizeazenzuazeiq.jpg'
author: GameRes 游资网
comments: false
date: Fri, 09 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/09/140103keizeazenzuazeiq.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2503889">
Android 用户想必对 APK 并不陌生。APK 是 Android Package 的缩写，即Android 安装包，基于 ZIP 压缩包格式，通过把 Android SDK 编译工程打包成一个 Android 系统支持的安装程序文件，几乎所有 Android 应用程序都以这种格式发布。<br>
<br>
但自下个月起，APK 格式要被谷歌弃用了。<br>
<br>
近日，谷歌宣布：自 2021 年 8 月起，Google Play 将要求开发者以 Android App Bundle （以下简称 AAB）格式发布新应用，该格式将取代 APK 作为标准发布格式。<br>
<br>
<div align="center">
<img id="aimg_991534" aid="991534" zoomfile="https://di.gameres.com/attachment/forum/202107/09/140103keizeazenzuazeiq.jpg" data-original="https://di.gameres.com/attachment/forum/202107/09/140103keizeazenzuazeiq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/09/140103keizeazenzuazeiq.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">1、为何要从 APK 转变为 AAB？</font></strong><br>
<br>
一直以来，Android 首选的应用程序包就是 APK，而一个 APK 中往往包含应用代码、图片、音频和开发者生成的应用签名密钥等大量资源。<br>
<br>
不仅如此，由于 Android 设备规格各异，开发人员还需根据设备的不同屏幕密度（320dpi、480dpi 等）、处理器（ARM、ARM64、x86）、用户所在的不同地区，在 Google Play 中构建和上传多个 APK，以此才能在用户点击“安装”时，在其设备上安装最适配的 APK。<br>
<br>
但在这种情况下，应用开发者便承受太多：不仅要开发应用，还要管理许多 APK 以支持大量设备。因此为了省时省力，大多数开发者通常都会选择构建一个通用 APK，即包含语言包、代码等在内的所有资源。不论用户身处何处、使用何种规格的设备，只需下载这个通用 APK 即可。<br>
<br>
说到这里，你或许发现了问题所在：包含所有资源的通用 APK 太大了。用户分明只需其中与自己设备相适配的资源，却要把整个 APK 都下载下来，不仅延长了安装时间，也占用了更多的带宽。<br>
<br>
为了解决这个问题，谷歌在 2018 年 Google I/O 大会上推出了 AAB 格式，希望以此减少开发者的负担，同时也有助于减少应用大小、安装时间和带宽消耗，提高用户体验。<br>
<br>
<div align="center">
<img id="aimg_991535" aid="991535" zoomfile="https://di.gameres.com/attachment/forum/202107/09/140107vfpgwgq7w7m2pqpj.jpg" data-original="https://di.gameres.com/attachment/forum/202107/09/140107vfpgwgq7w7m2pqpj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/09/140107vfpgwgq7w7m2pqpj.jpg" referrerpolicy="no-referrer">
</div><br>
简单来说，AAB 格式其实并不是一个全新的应用安装包，你可以将它当做一个容器，里面包含着一个基本 APK 和多个用于特定配置的 APK。<br>
<br>
而谷歌在这之中则充当“筛选”的角色：一旦开发者选择使用 AAB 格式发布应用，谷歌就会根据用户的设备配置从中生成优化后的 APK 提供给用户。对用户而言，这样的 APK 体积小、安装快，对开发者来说也省事：不必再为各种设备管理一大堆 APK。<br>
<br>
因此，总体来看，谷歌要求下个月以 AAB 格式发布新应用的决定主要面向开发者，对用户而言影响不是太大，因为最终在设备上安装 Android 应用的打包格式还是 APK。<br>
<br>
<strong><font color="#de5650">2、AAB 的优势</font></strong><br>
<br>
相较于 APK，AAB 自然有其独一无二的优点。<br>
<br>
首先便是上文所提到的应用体积缩小。据谷歌官方介绍，使用 AAB 生成优化的 APK 体积平均会比一般的 APK 小 15%，而这一数据会根据应用大小有较大起伏。例如 Airbnb 在从 APK 切换到 AAB 格式后应用大小减少了 22%，而 Netflix 更是减少了 57%。<br>
<br>
<div align="center">
<img id="aimg_991536" aid="991536" zoomfile="https://di.gameres.com/attachment/forum/202107/09/140125z0zle3ez5b4gl5xu.png" data-original="https://di.gameres.com/attachment/forum/202107/09/140125z0zle3ez5b4gl5xu.png" width="584" inpost="1" src="https://di.gameres.com/attachment/forum/202107/09/140125z0zle3ez5b4gl5xu.png" referrerpolicy="no-referrer">
</div><br>
其次，AAB 的 Play Feature Delivery 功能可自定义将哪些功能模块交付给哪个设备，支持安装时交付、按条件交付和按需交付等三种模式。这也就是将应用的功能拆分开来，以此大幅缩短用户下载应用的时间，其中没用的功能用户可以不下载或等到以后需要时再下载。<br>
<br>
还有一个 Play Asset Delivery 功能，以动态方式交付大型资源可以减少用户等待时间，同时缩减交付成本。即使用 Play Asset Delivery 的游戏可通过纹理压缩格式作为交付条件，以便用户只获取适合其设备的资源，避免浪费空间或带宽。<br>
<br>
<strong><font color="#de5650">3、对于 AAB 的担忧</font></strong><br>
<br>
虽然从结果看来，以 AAB 格式分发新应用对开发者和用户都有益处，但还是有部分人对此有些担忧。<br>
<br>
有人担心从 APK 变为 AAB 格式会太复杂。但谷歌表示：“对于大多数应用而言，构建 AAB 文件来替代 APK 文件仅需要少量工作。”它指出 App Bundle 是一种受主流构建工具支持的开源格式，因此在 Play Core 原生 SDK、Play Core Java SDK 和 Play Core Kotlin SDK 的助力下，无论用户偏好哪种编码环境，都可以轻松开始使用可选的高级 App Bundle 功能。此外，AAB 的要求仅适用于新应用，现有应用及面向特定 Google Play 用户的私人应用目前无需遵从此要求。<br>
<br>
有人对与谷歌共享私人签名密钥表示担忧（签名密钥是验证 APK 完整性的重要信息，谷歌从 ABB 中生成优化的 APK，因此签名密钥也将包含在 ABB 中），对此谷歌表示，所有“签名密钥都将存储在谷歌用来存储自己的密钥的同一基础设施上” ，因此开发者的私人签名密钥都会受到严密的安全保护。<br>
<br>
还有人担心因为 AAB 不能在 Google Play 以外的地方下载，会对如亚马逊应用商店等第三方应用商店造成很大影响。但据了解谷歌已经开发了一个名为 bundletool 的开源工具，允许开发人员从 AAB 包中创建 APK，因此想在第三方商店中发布 Android 应用程序的开发人员可以手动导出其应用的 APK 版本。<br>
<br>
那么对于谷歌的这一决定，你有什么看法吗？<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：CSDN</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/MINFYEOOJQGyvEhB94VtWQ</font></font><br>
</td></tr></tbody></table>



  
</div>
            