
---
title: '字节新一代解码器 BVC｜助力 H.266_VVC 标准商业落地'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47e5f6f50807478fba2b486f2d944bc8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 21:17:42 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47e5f6f50807478fba2b486f2d944bc8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>随着网络环境的优化和移动设备性能的提升，高清流畅的极致观影体验吸引着更多的终端用户。高分辨率视频资源也给压缩标准提出了新的要求。从 H.264/AVC 标准到 H.265/HEVC 标准，虽然压缩效率提升一倍，但依然无法满足高清视频的压缩需求。因此，拥有更高压缩效率的 H.266/VVC 标准诞生。诞生初期，由于 H.266/VVC 编码标准复杂，且缺少对应的终端设备硬解码，让商业落地显得遥不可及。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47e5f6f50807478fba2b486f2d944bc8~tplv-k3u1fbpfcp-watermark.image" alt="图片1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1d9575e6e2448e68a4c801a3caa3e31~tplv-k3u1fbpfcp-watermark.image" alt="图片2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>用户通过高清、超高清视频获得极致的观看体验</em></p>
<h2 data-id="heading-0"><strong>H.266/VVC</strong> <strong>标准的压缩效率比</strong> <strong>H.265/HEVC</strong> <strong>提升一倍</strong></h2>
<blockquote>
<p>多功能视频编码 (Versatile Video Coding，VVC，也称为 H.266)是联合视频专家组制定的最新一代视频编码标准，于2020年7月正式定稿。作为 HEVC 的继任者，H.266/VVC 能够在相同的质量下将压缩效率再提升一倍。H.266/VVC 标准的推动将能为未来视频内容的发展提供巨大的潜力。</p>
</blockquote>
<p>H.266/VVC的前一代标准是H.265/HEVC。随着近几年移动终端的蓬勃发展，H.265/HEVC已经得到广泛应用，但其压缩效率仍无法满足大量4K/1080P等高清视频资源的需求。过大的视频资源压缩文件，占据了存储空间并吞噬着网络带宽，导致用户观看视频时频繁卡顿。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54d4e4fd072d45569811c6fbfa635d49~tplv-k3u1fbpfcp-watermark.image" alt="图片3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而在相同的编码质量下，H.266/VVC 标准的压缩率可以比 H.265/HEVC 标准提升一倍。</p>
<p><em><strong>举个例子</strong></em>，使用 H.265/HEVC 编码标准，用户观看一部电影需要 1GB 的流量，换成H.266/VVC 编码标准后，仅需 500MB 的流量，并且在智能终端播放的时候，画质可以保持不变。H.266/VVC 标准，使高清在线视频不再是流量吞噬者。</p>
<p>尽管 H.266/VVC 标准的压缩性能非常优异，但其解码复杂度显著高于 H.265/HEVC 标准。终端设备解码过程中会出现设备发热、耗电增加以及视频卡顿的现象，影响用户观看体验。在硬件解码芯片尚未问世的背景下，如何设计并实现一款超高性能的 VVC 软件解码器成为我们的重要目标。</p>
<h2 data-id="heading-1"><strong>BVC</strong> <strong>解码器，打通</strong> <strong>H.266/VVC</strong> <strong>标准落地的最后一公里</strong></h2>
<p>BVC 是字节跳动自研的新一代解码器，已正式支持 H.266/VVC 标准。BVC 解码器可应用于 Android、iOS、Linux、MacOS 和 Windows 等多种平台。</p>
<p>针对移动端用户众多、设备性能参差不齐的问题，我们在 Android 和 iOS 的 Arm 平台上，对 BVC 解码器进行了特别的优化，在部分设备上的解码速度达到参考软件的数十倍。BVC 的高效解码，使 H.266/VVC 标准的商业落地不再遥不可及。</p>
<p><em><strong>看一组详细数据</strong></em>，根据国际会议提案 JEVT-V128，在搭载 A14 处理器的 iPhone 12上，对于 4K 分辨率标准测试码流，BVC 单线程平均解码速度达到了 22 fps；2 线程可以实现 4K 视频的实时解码。对于 1080p 分辨率标准测试码流，BVC 单线程平均解码速度是 86 fps，即单线程可实时解码 1080p 视频。因此，在高端手机上，BVC 解码器支持流畅播放高清甚至超高清视频。
 
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b98c9085fb45ccbf514b3720ed2008~tplv-k3u1fbpfcp-watermark.image" alt="图片4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图1 对比不同线程的 BVC 与 VTM-11.0 的解码速度</p>
<blockquote>
<p>图1展示了在 iPhone12 上，BVC 和参考软件 VTM-11.0 解码不同分辨率视频的速度对比。横轴依次代表解码 4K、1080p、480p 和 240p 分辨率的视频；纵轴表示使用 VTM-11.0 解码和 BVC 分别使用1、2、4、6线程解码的平均帧率，数值越大表明解码速度越快。虚线表示各分辨率视频实时播放的常用帧率。可以看出，BVC 仅单线程的解码速度相较于 VTM-11.0 就有着 6-10 倍的巨大优势。</p>
</blockquote>
<p><em><strong>除了上述标准测试码流外</strong></em>，我们还测试了使用 BVC 编码器生成的抖音视频码流，BVC解码器表现出了强大的解码性能。在性能逊于 iPhone 12 的小米6手机上，BVC 单线程即可完成 1080p 视频的实时解码；在其它中低端手机上，BVC 单线程即可完成对 720p 视频的实时解码。BVC 解码器的出现，使得在各种性能的设备上均可实现对 H.266/VVC 标准视频资源的解码，并为用户带来流畅的观看体验。</p>
<h2 data-id="heading-2"><strong>BVC</strong> <strong>解码器如何实现技术突破</strong></h2>
<p>为了有效降低 BVC 解码器的计算复杂度，加快解码速度，我们从并行性、代码框架、汇编指令和访存效率等方向进行了优化，性能改善显著。</p>
<p>• <strong>细粒度的并行算法</strong>：BVC 支持不同层次的并行算法，包括帧级并行、块级并行和模块级并行。帧级并行即同时解码多个视频帧，可以充分利用多核 CPU 的性能，并行程度最高；块级并行即同时解码多个解码块；模块级并行即利用 CPU 的剩余资源，同时处理多个较复杂的模块。块级与模块级相结合可以高效降低视频帧的输出时延，保障视频会议和直播等实时场景的流畅体验。</p>
<p>• <strong>对流水线友好的代码框架：</strong> BVC 有着非常轻量级的代码框架，更加迎合空间较小、性能较差的移动端设备。针对各个功能模块特性，BVC 有不同的算法实现，尽可能减少了分支跳转，提升了 CPU 流水线的饱和度。</p>
<p>• <strong>高吞吐量的汇编优化</strong>：我们采用高吞吐量的 SIMD 指令，针对像素帧内预测、帧间插值、量化、变换、重建和环路滤波等复杂模块做汇编优化，均达到了数倍的模块加速比，最大程度提升 CPU 的计算效率。</p>
<p>• <strong>高效的访存设计</strong>：移动设备内存和缓存空间较小，访存效率有限，这极大地制约了解码器的性能。为此，我们针对 BVC 解码器的访存进行了优化，包括减少内存读写次数、集中内存使用和提高缓存命中率。优化后，访存不再成为在移动设备上解码超高清视频的瓶颈。</p>
<h2 data-id="heading-3"><strong>详细性能数据</strong></h2>
<p>我们使用 VVC 官方参考软件 VTM-11.0 做了一组测试。在通用配置下，生成若干组8比特码流，打开标准测试条件下的全部工具，包括较复杂的 DMVR、BDOF 和 ALF 等。测试的序列为标准通用测试序列，包括 class A、B、C、D、F 五类。其中，class F 是屏幕内容场景，分辨率从 480p 到 1080p 不等；class A-D 为自然场景，视频的分辨率分别为 4K、1080p、480p 和 240p。</p>
<p>在 iPhone 12（A14 处理器）上，BVC 单线程解码 4K 分辨率、8 比特标准测试码流的速度平均达到了 22fps，是参考软件 VTM-11.0 解码速度的 10 倍；在使用全部 6 个线程后解码速度甚至可达 55 fps，最高达到 78fps。对于 1080p 分辨率、8 比特标准测试码流，BVC 解码器的单线程平均解码速度是 86 fps，达到参考软件的8.8倍。</p>
<p>表1 解码器速度对比详细数据</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cff8377b80f642068d8ffbd31b596c07~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG96.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4"><strong>总结</strong></h2>
<p>BVC 解码器可以实现超清、高质视频的实时快速解码，展现出在移动端上卓越的解码能力，对视频行业的发展和 H.266/VVC 标准的落地起到积极的推进作用。</p>
<p><em><strong>接下来</strong></em>，基于实际应用中的问题和挑战，我们的技术团队将持续发力，不断优化 BVC解码器的性能，旨在为新一代标准的落地做出更多贡献。</p>
<h2 data-id="heading-5"><strong>火山引擎多媒体实验室 团队介绍</strong></h2>
<p>多媒体实验室致力于研究、探索多媒体领域的前沿技术，参与国际、国内多媒体方向的标准化工作，为多媒体内容分析、处理、压缩、传输、创新交互等领域提供软硬件解决方案。目前多媒体实验室所提供的众多创新算法已经广泛应用在了抖音、西瓜视频等产品的点播、直播、实时通信、图片等多媒体业务，在成本、体验、能力几方面赋能业务，为其提供极致的视频技术和极致的产品体验</p></div>  
</div>
            