
---
title: '学习 VR 开发之前，这 7 个容易混淆的概念一定要理清'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202105/10/112044cg7bmr5759ooogbz.jpg'
author: GameRes 游资网
comments: false
date: Mon, 10 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/10/112044cg7bmr5759ooogbz.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2496122">
U 酱陆续为大家推荐了动画制作、实时光追、Shader Graph、FPS 游戏制作的精品课程，掐指一算，当下热门的 VR 制作怎么能漏掉呢？<br>
<br>
在 Unity VR 应用程序开发的过程中，有几个容易混淆的概念，我们先来给大家做一下区分，它们是 OpenVR、OpenVR Desktop、OpenVR XR Plugin、SteamVR、SteamVR Plugin、OpenXR 以及 OpenXR Plugin。<br>
<br>
以下内容均出自本次推荐的 VR 课程，心急的朋友可以直接拉至文末了解课程详情。<br>
<br>
<strong><font color="#de5650">OpenVR</font></strong><br>
<br>
OpenVR 是 Valve 公司开发的一套包含一系列 SDK 和 API 的工具集，旨在从驱动层级为硬件厂商提供软硬件开发支持。硬件设备制造商可以为设备开发 OpenVR 驱动程序，以使设备能够运行在 SteamVR 平台上。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112044cg7bmr5759ooogbz.jpg" alt="微信图片_20210510111959.jpg" title="微信图片_20210510111959.jpg" referrerpolicy="no-referrer">
</div><br>
虽然 OpenVR 是 HTC Vive 默认使用的驱动程序，但它的开发目的是为了得到更多厂商的支持，例如，开发者也可以为 Oculus Rift 或 Windows MR 设备开发基于 OpenVR 的软件应用。<br>
<br>
需要注意的是，OpenVR 虽然也提供了一套开发标准，但是相较于 OpenXR，其覆盖范围相对较小，另外，Valve 从 SteamVR 客户端 1.16 开始，已经对 OpenXR 标准进行了全面的支持。<br>
<br>
作为 Unity 开发者来说，并不需要太多关心 OpenVR 及其 SDK，因为这更多的是面向 VR 硬件平台和游戏引擎开发商来进行使用的。<br>
<br>
<strong><font color="#de5650">OpenVR Desktop</font></strong><br>
<br>
Unity 需要各 VR 硬件平台提供与对应底层驱动程序通信的工具包来完成 VR 应用程序的渲染等工作，OpenVR Desktop 则是 OpenVR 提供给 Unity 使用的一系列组件，用于访问 OpenVR 的 SDK。该工具包可以通过 Package Mananger 进行安装，但仅存在于 Unity 2019.4 LTS 及其以前版本，在 Unity 2020 中被废弃，转而使用 OpenVR XR Plugin 代替，如下图所示：<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112044ppxkm2h26hhhzqph.jpg" alt="微信图片_20210510112004.jpg" title="微信图片_20210510112004.jpg" referrerpolicy="no-referrer">
</div><br>
要使用 OpenVR Desktop，在将工具包安装完毕以后，需要在 Build Settings 中开启 VR 支持并选择 OpenVR SDK。在 Build Settings 中开启 VR 支持的方式，仅适用于 Unity 2019 及其以前的版本，而在 Unity 2020 及其以后的版本中，此方法也将被废弃，转而使用 XR Plug-in Management 进行管理。<br>
<br>
<strong><font color="#de5650">OpenVR XR Plugin</font></strong><br>
<br>
OpenVR XR Plugin 与 OpenVR Desktop 的作用和地位相同，推出的目的是为了配合 Unity 2020 在 XR Plug-in Management 中管理 VR 平台提供的工具包。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112045ym9vuverev9zmv9v.jpg" alt="微信图片_20210510112005.jpg" title="微信图片_20210510112005.jpg" referrerpolicy="no-referrer">
</div><br>
OpenVR XR Plugin 目前需要手动从本地磁盘进行安装，开发者可访问网址：github.com/ValveSoftwar，下载该工具包的 .tgz 格式文件，然后在 Package Manager 中选择"Add package from tarball..."命令进行安装。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112045uizxk66cgkdi3kne.png" alt="微信图片_20210510112006.png" title="微信图片_20210510112006.png" referrerpolicy="no-referrer">
</div><br>
另外，如果开发者使用 SteamVR Plugin 2.7.x 进行 VR 应用程序开发，则在插件中已经包含了 OpenVR XR Plugin 工具包，可使用以上方式进行安装而不用从网络重复下载，如下图所示：<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112045xxvqix80x5xzi4b0.jpg" alt="微信图片_20210510112007.jpg" title="微信图片_20210510112007.jpg" referrerpolicy="no-referrer">
</div><br>
安装完毕后，可以在 XR Plug-in Manager 中启用并进行相关设置，如下图所示：<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112046afxbsfww3c7fbxs3.jpg" alt="微信图片_20210510112008.jpg" title="微信图片_20210510112008.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">SteamVR</font></strong><br>
<br>
SteamVR 是 Valve 基于 OpenVR 推出的一套 VR 体验解决方案，以软件客户端形式存在，面向终端用户，故也常被称为 SteamVR 客户端。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112046clffllf6hd49ghxl.jpg" alt="微信图片_20210510112009.jpg" title="微信图片_20210510112009.jpg" referrerpolicy="no-referrer">
</div><br>
当运行或测试 SteamVR 平台支持的应用程序时，SteamVR 客户端会自动开启，为应用程序提供运行时环境。<br>
<br>
除此之外，SteamVR 客户端还提供 VR 控制器的配对、驱动更新、性能分析等功能。初次连接 VR 设备以后，需要通过 SteamVR 客户端进行设备校准，即所谓的房型设置。在客户端界面底部，列出了当前已经连接到系统中的设备，包括头显、手柄控制器、基站、其它可跟踪设备如 Vive Trakcer 等。<br>
<br>
SteamVR 可以通过 Steam 客户端进行安装，还可通过设备供应商提供的安装程序进行安装。以 HTC VIVE 为例，购买后可访问网址：https://www.vive.com/cn/setup/，选择下载 VIVE 安装程序，该程序将引导用户进行设备连接，完成相应驱动程序和 SteamVR 的安装，对于初学者来说相对友好。两种渠道安装的 SteamVR 客户端均能保证 VR 应用程序的运行，选择其中一种即可，两者亦可同时存在。<br>
<br>
对于终端用户，当前支持 SteamVR 的硬件包括但不仅限于以下设备：<br>
<br>
<ul><li>Valve Index</li><li>HTC VIVE/Cosmos</li><li>Windows Mixed Reality</li><li>HP Reverb G2<br>
</li></ul><br>
SteamVR 客户端作为桥梁，介于 OpenVR 底层驱动与用户之间工作—— SteamVR 获取到用户的输入，如控制器按键的按下、头显在空间中移动等，将这些数据信息传递给 OpenVR 进行处理，OpenVR 将处理后的数据通过 SteamVR 呈现给用户。<br>
<br>
<strong><font color="#de5650">SteamVR Plugin</font></strong><br>
<br>
SteamVR Plugin 是  Valve 公司提供给 Unity 开发者的开发工具，以 .unitypackage 文件的形式存在，在使用方面符合一般的 Unity 插件导入流程，开发者可使用该插件开发面向 SteamVR 平台的 VR 应用程序。SteamVR Plugin 可由 Unity Asset Store 和 Github 下载安装，所不同的是，Asset Store 中总是提供最新且稳定的 SteamVR 插件版本，而在 Github 中，可以下载该插件的所有过往版本及预览版。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112046rhzenh6qxehuuump.jpg" alt="微信图片_20210510112013.jpg" title="微信图片_20210510112013.jpg" referrerpolicy="no-referrer">
</div><br>
SteamVR Plugin 能够与 SteamVR 客户端进行交互，主要帮助开发者实现三项主要功能：为 VR 控制器加载呈现相对应的 3D 模型、处理控制器的输入、根据用户实际手部动作估算骨骼数据并通过这些数据在虚拟世界中呈现相对应的手部姿态。除此之外，SteamVR Plugin 还提供了一套便捷的交互系统（Interaction System），帮助开发者快速开发出常见的 VR 交互功能，该交互系统脱胎于 Valve 开发的《The Lab》VR 体验应用。<br>
<br>
<strong><font color="#de5650">OpenXR</font></strong><br>
<br>
随着行业的发展，越来越多的 VR/AR 设备被推向市场。这对于开发者来说，面临的重要议题之一便是针对不同的 VR/AR 硬件平台进行应用程序的适配，这将带来一部分额外且不必要的工作量；对于硬件平台厂商来说，新上市的产品面临着内容严重不足、生态急需健全的问题。<br>
<br>
OpenXR 是一套由 Khronos Group 发起，联合多家行业头部公司一起制定的开放标准，旨在解决 XR 平台碎片化的问题，同时简化 AR/VR 软件的开发。对于开发者来说，基于此标准进行 XR 应用程序的开发，能够使应用程序覆盖更广泛的硬件平台，同时无需移植或重新编写代码；而对于支持 OpenXR 的硬件平台厂商来说，能够在产品发布时即可拥有可运行在其上的大量内容。<br>
<br>
下图左侧为引入 OpenXR 标准之前的行业现状—— VR/AR 应用程序和引擎必须使用每个平台独有的 SDK 和 API，新的设备同样需要特定的驱动程序。而在引入 OpenXR 标准以后，将统一由 OpenXR 提供的跨平台高性能的应用程序接口与众多 XR 硬件平台进行交互，如下图右侧所示。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112047qti9ch611xviwbsv.jpg" alt="微信图片_20210510112014.jpg" title="微信图片_20210510112014.jpg" referrerpolicy="no-referrer">
</div><br>
OpenXR 1.0 标准于 2019 年公布，各大 XR 平台开始逐步加入到支持 OpenXR 标准的行列，包括 Oculus Quest/Rift、Windows Mixed Reality、Unity、Unreal Engine、SteamVR 等目前主流的 VR 平台和游戏引擎。这就意味着，开发者将专注于应用程序的开发而不是各平台的交互适配问题。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112047pdem99ahamojxeo9.jpg" alt="微信图片_20210510112015.jpg" title="微信图片_20210510112015.jpg" referrerpolicy="no-referrer">
</div><br>
由上图可见，OpenXR 集合了行业众多头部公司和组织参与制定标准，覆盖了从 VR 到 AR、从软件到硬件的广阔范围。<br>
<br>
<strong><font color="#de5650">OpenXR Plugin</font></strong><br>
<br>
OpenXR Plugin 是 Unity 开发的符合 OpenXR 标准的工具包，旨在让 Unity 开发者尽可能高效地将内容部署到更加广泛的 XR 目标平台上。开发者在 Unity 2020 中通过 Package Manager 搜索"openxr"即可找到该工具包并进行安装。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112047r5f1ilehc4cnchk5.jpg" alt="微信图片_20210510112016.jpg" title="微信图片_20210510112016.jpg" referrerpolicy="no-referrer">
</div><br>
由于处于版本发布的早期，所以目前通过广泛测试的硬件平台有限，Unity 声称目前无法测试或保证所有支持 OpenXR 的配置都能以最佳状态运行，该工具包也在不断完善中，后续会逐步增加支持的平台。以下是截至当前经过全方位测试并被官方支持的平台。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112048i8n66omn4okzco54.jpg" alt="微信图片_20210510112018.jpg" title="微信图片_20210510112018.jpg" referrerpolicy="no-referrer">
</div><br>
由于 OpenXR 只支持基于动作的输入（action-based input），所以 OpenXR Plugin 可以直接使用 Unity 的 Input System 处理输入和交互。如果开发者的项目正在使用特定平台的工具包（如 MRTK、Oculus ），Unity 不建议启用 OpenXR，因为许多厂商仍在为 OpenXR 添加支持。<br>
<br>
以上内容完全来自于 Unity 社区博主邵伟，今天 U 酱要推荐的课程，正是该作者的《SteamVR 2.x 交互开发指南》。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112048uvj398oxx5o3szlc.jpg" alt="微信图片_20210510112019.jpg" title="微信图片_20210510112019.jpg" referrerpolicy="no-referrer">
</div><br>
SteamVR Unity Plugin（以下简称 SteamVR）在 2.0 及其以后的版本（2.x）中进行了完全的框架重构，原来使用 1.x 版本开发的项目将不能继续适配。相较于 1.x 版本，2.x 引入了动作（Action）的概念，使用新的输入系统来响应用户的交互，目的是解决 VR 硬件碎片化的问题——开发者只需要进行一次开发，即可部署到适用于所有基于 SteamVR 的硬件平台上。<br>
<br>
新版本的难点在于动作（Action）的使用，重点在 Interaction System，通过该交互系统，能够实现常用的 VR 交互。本套课程将通过 30+ 个课时，近 9 小时内容，深入讲述 SteamVR 插件中高频组件的使用方法，结合实例实现常见的 VR 交互方式，同时，我们也将基于项目实战经验，介绍该插件的一些特性，如场景跳转时的 Player 管理、与通用渲染管线（URP）的适配、如何集成 VRTK4 等。<br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112049y2awuk5vuq88nazx.jpg" alt="微信图片_20210510112021.jpg" title="微信图片_20210510112021.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112049yqcc27cw5nhg2i41.jpg" alt="微信图片_20210510112022.jpg" title="微信图片_20210510112022.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112050e4fevn7gvf3f5c66.jpg" alt="微信图片_20210510112023.jpg" title="微信图片_20210510112023.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">图片来源于课程</font></font></div><br>
本课程硬件系统基于 HTCVIVE（亦适用于 Cosmos 精英套装），软件版本使用 SteamVR Unity Plugin 2.5、2.6.1、2.7.2，Unity 编辑器使用 2019.4 LTS 版本，少量内容使用 VRTK4，提供课程中涉及到的所有素材和项目源文件。<br>
<br>
<strong>适用对象</strong><br>
<br>
<ul><li>高校师生</li><li>VR 开发初学者</li><li>新晋 VR 开发团队</li><li>希望将项目升级使用 SteamVR 2.x 的开发者<br>
</li></ul><br>
<strong><font color="#de5650">关于讲师</font></strong><br>
<br>
<div align="center">
<img src="https://di.gameres.com/attachment/forum/202105/10/112050tpnbznyz0ssn1nyp.jpg" alt="微信图片_20210510112026.jpg" title="微信图片_20210510112026.jpg" referrerpolicy="no-referrer">
</div><br>
邵伟，Unity 价值专家（UVP），公众号『XR 技术研习社』主理人，两届高通 Qualcomm XR 创新应用挑战赛评委和技术导师，出版作品《Unity VR 虚拟现实完全自学教程》与《Unity 2017 虚拟现实开发标准教程》，著有多部 VR 开发相关视频教程，累计录制课时时长超 5000 分钟，目前专注于 XR 技术教育培训工作。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：Unity官方平台</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/AVGTHxFWe6tfoHxlE9Mvug</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            