
---
title: '​虚幻引擎正式迎来AMD FSR 2.0游戏开发插件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0625/0298ac025fd294e.jpg'
author: cnBeta
comments: false
date: Sat, 25 Jun 2022 03:49:17 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0625/0298ac025fd294e.jpg'
---

<div>   
<strong>在 FSR 1.0 推出一周年之际，AMD 这周又通过 GPUOpen 项目，宣布了 FSR 2.0 将向所有开发者免费开放。</strong>作为一个开源项目，开发者现可通过虚幻引擎（UE4 或 UE5）插件，轻松地将这项免费技术应用到他们游戏中。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0625/0298ac025fd294e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0625/0298ac025fd294e.jpg" alt="-1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://videocardz.com/newz/amd-fsr-2-0-plugin-for-unreal-engine-4-and-5-is-now-available" target="_self">VideoCardz</a>）</p><p>尽管上月只有四款游戏首发支持 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 的 FidelityFX Super-Resolution 2.0 技术，但随着虚幻引擎开发插件的正式到来，后续我们将迎来更多支持 FSR 2.0 的新老作品。</p><p><a href="https://static.cnbetacdn.com/article/2022/0625/9af16d6fbea9210.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0625/9af16d6fbea9210.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>【虚幻引擎 - FSR 2.0 插件 - 安装流程】找到 Engine / Plugins 路径，提取 FSR2.zip 压缩包里的文件内容，选择对应虚幻引擎版本的子文件夹。</p><p>将 FSR2 文件夹放到虚幻引擎的源代码树中，UE4 为 Engine/Plugins/Runtime/AMD、UE5 则是 Engine/Plugins/Marketplace 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/6475bc503586f23.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>此外可选将 FSR2MovieRenderPipeline 文件夹，放置在 Engine/Plugins/Runtime/AM 源代码树中（仅适用于 4.27.2 及更高版本）。</p><p>然后打开选定的虚幻引擎项目，导航至工具栏上的“编辑”（Edit）→ 插件（Plugin）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/872964ecf4f92e5.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p>在“插件”对话框中，请确保 —— 在左侧勾选了“全部”（All），在右上角的搜索框中输入“fsr”，于确认框中选择“启用”（Enable）、且可选 FSR2MovieRenderPipeline 插件。</p><p>若出现提示，点击“立即重启”（Restart Now）虚幻引擎，以应用相关更改。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/a1ef3895ac9e630.png" alt="0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：AMD GPU Open <a href="https://gpuopen.com/learn/ue-fsr2/" target="_self">网站</a>）</p><p>据悉，AMD FSR 2.0 采用了不同于 NVIDIA DLSS 的时序拉伸（Temporal Upscaling）解决方案，但是对于已经支持运动矢量和其它时序拉伸的游戏来说，FSR 2.0 落实起来将只需数天或数月。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/62b9131b2c46311.jpg" alt="4.jpg" referrerpolicy="no-referrer"></p><p>要在 UE4 或 UE5 上使用 FSR 2.0 插件，可先打开现有的虚幻引擎项目，然后移步至编辑器（Editor）→ 影片序列（Sequencerrr Cinematic）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/960a0d8cf62726f.jpg" alt="5.jpg" referrerpolicy="no-referrer"></p><p>在工具栏里选择“影片输出”（Movie Output），接着点击“未保存的配置”（Unsaved Config），以打开电影渲染队列（Movie Render Queue）的设置。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/aef7346a5b56640.jpg" alt="6.jpg" referrerpolicy="no-referrer"></p><p>选择 +Setting 项下的“启用 FSR 2.0 设置”，再点击列表中的新设置，以选择想要的渲染画质档位，最后点击“接受”并本地渲染。</p>   
</div>
            