
---
title: 'CodeWeavers团队致力于为Mac引入DirectX 12游戏兼容支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1224/4f8f9e36d9b9127.png'
author: cnBeta
comments: false
date: Fri, 24 Dec 2021 05:34:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1224/4f8f9e36d9b9127.png'
---

<div>   
当 Valve 携手 CodeWeavers 团队的部分成员以帮助构建 Proton 时，他们可能没料到后者取得现今如此巨大的成就。自 2016 年秘密开动以来，Steam 游戏库中的很大一部分，现在都可以在 Linux 平台上体验了。<strong>这些游戏的一个共通点，就是未搭配旨在检测其运行环境的 Windows 反作弊客户端，所以也没有成为与 DXVK / VKD3D 不完全兼容的 DirectX 调用的受害者。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1224/4f8f9e36d9b9127.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://github.com/ValveSoftware/Proton/tree/experimental_6.3" target="_self">CodeWeavers</a>）</p><p><a href="https://www.neowin.net/news/directx-12-is-coming-to-mac-but-the-road-is-long/" target="_self">Neowin</a> 指出，DXVK 是负责将 DirectX 即时转换为 Vulcan 的软件，而 VKD3D 也为 DirectX 12 提供了同样的支持。</p><p>当然，CodeWeavers 对 Proton 的衍生技术并不陌生。20 多年来，他们一直在 Wine（不是一套单纯的模拟器）上构建，积极为公共与私营部门提供商用解决方案。</p><p>2006 年，当<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>转投<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>芯片时，CodeWeavers 的消费级产品 Crossover <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 也获得了新生，促使其将 Linux / Xorg 上的原生应用程序移植到 BSD / Aqua 环境。</p><p><img src="https://static.cnbetacdn.com/article/2021/1224/aae1fa55a8e9fdf.png" referrerpolicy="no-referrer"></p><p>现在，CodeWeavers 团队正面临着与 DirectX 12 实现兼容的新挑战。尽管实验代码已合并到 Valve / Proton 中，以供 Linux 用户使用。然而 Mac 上的 VKD3D，仍面临着诸多必须克服的技术挑战和限制。</p><p>具体说来是，登陆 macOS 平台的最大障碍，是苹果家的 Metal 底层。与 Vulkan 等跨平台技术相比，DX12 可调用百万级的着色器资源视图（SRV），而 Metal 的 SRV 上限仅为它的一半。</p><blockquote><p>简而言之，Metal 以不同的方式进行细分，且缺少几何着色器与变换反馈，结果就是 DX12 / Metal 存在特定的资源限制问题。</p><p>通常游戏需要访问至少百万个着色器资源视图（SRV），访问这么多 SRV 需要在第 2 层级进行资源绑定。但 Metal 的每个参数缓冲区仅支持大约 50 万资源，因而无法做到 2 级资源绑定。</p><p>即使 Metal 的 50 万限制对于 Vulkan 描述符索引已足够，但这种情况并不适用于 D3D12 —— 意味着 CrossOver Mac 不支持 Tier 2 绑定，导致许多 DX12 游戏无法运行。</p></blockquote><p>好消息是，CodeWeavers 似乎有信心扫除这些障碍，并在即将推出的 CrossOver 23 中为 Mac 带来 DX12 兼容性（推向上游 <a href="https://github.com/ValveSoftware/Proton/tree/experimental_6.3" target="_self">Proton 实验</a>）。</p><p>当然，如果你不强求在 M1 硬件上玩 PC 游戏，那在 Steam Deck、SteamOS 3.0、以及广阔的 Linux 桌面环境中玩游戏的朋友，还是能够更快地获得这项体验的。</p><p>这对于那些想要在M1 硬件上玩 PC 游戏的人来说是个好消息。对于那些计划在 Steam Deck、Steam OS 3.0 或广阔 Linux 桌面环境中的任何其他地方玩游戏的人，您将能够更快地利用这些进步，因为它们被推向上游Proton 实验。</p>   
</div>
            