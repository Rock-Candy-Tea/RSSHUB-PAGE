
---
title: 'RT-Thread Studio V2.1.0 发布，支持用户自制开发板支持包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b940b4241a1b8c4edba618c87f02d4b084e.png'
author: 开源中国
comments: false
date: Wed, 31 Mar 2021 09:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b940b4241a1b8c4edba618c87f02d4b084e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RT-Thread Studio V2.1.0 已发布。</p> 
<p>主要变化：</p> 
<ul> 
 <li>新增开发板支持包制作工具功能和详细教程，大大降低开发板支持包制作和上线的难度。</li> 
 <li>支持了 MDK 协同开发，将 MDK 工程导入到 Studio 后可以双向无缝同步开发，极大地方便了工程转移和多工具间协同开发。</li> 
 <li>支持 cubemx 协同开发，无缝调用 cubemx 并将代码生成回 Studio 工程，提高了工具间协同的便利性。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b940b4241a1b8c4edba618c87f02d4b084e.png" referrerpolicy="no-referrer"></p> 
<h1>1、支持用户自制开发板支持包</h1> 
<p>现在可以直接通过可视化的 Studio 的开发板支持包制作工具和教程，轻松地制作开发板支持包并且上线到 SDK Manager。</p> 
<p>在开发板支持包制作工具中，大家可以图形化地配置开发板、文档、工程的信息，所有配置项都有清晰易懂的提示以供参考，在配置结束后，支持预览来查看配置的所有内容。制作教程在 Studio 文档中心，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rt-thread.org%2Fdocument%2Fsite%2Frtthread-studio%2Fum%2Fstudio-user-manual%2F%23_73" target="_blank">链接地址点此访问</a>。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0331/085801_meaY_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>2、新增上线 40 多个开发板支持包</h1> 
<p>目前已通过 Studio 的开发板支持包制作功能，制作上线了 40 多个开发板支持包，目前开发板支持包总计 70 多个，涵盖了 8 个不同厂商，例如 Allwinner，AlphaScale，ArteryTek，Bluetrum，GigaDevice，MicroChip，MindMotion，NXP，ST，TI，Synwit。此外，本次新增上线了 RT-Thread V4.0.3 新版本源码资源包。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0331/085916_KtTH_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>3、支持 MDK 开发</h1> 
<p>Studio 现在支持和 MDK 工程双向同步协同开发。大家可以将现有的 RT-Thread MDK 工程直接导入到 Studio 中，MDK 的配置会自动同步到 RT-Thread Studio 工程。</p> 
<p>Studio 提供了双向同步的机制，可以在 MDK 工程和 Studio 工程之间随时切换，并且提供了 MDK 的配置功能，可以执行 C/C++、 ASM、 Linker 等配置项，配置结束后，会自动同步到 MDK 工程。如果大家在 MDK 上修改了一些配置，也可以在 Studio 手动触发同步功能，会将修改后的配置同步到 Studio 工程。</p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rt-thread.org%2Fdocument%2Fsite%2Frtthread-studio%2Fum%2Fstudio-user-manual%2F%23mdk" target="_blank">更多教程请访问文档中心</a>。</strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0331/090020_RmzX_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>4、支持 CubeMX 开发</h1> 
<p>Studio 已经支持和 STM32CubeMX 协同开发，大家可以在 Studio 工程中直接打开 CubeMX Settings，然后进行配置，配置结束后，点击 GENERATE CODE， CubeMX 生成的代码会自动存放在 Studio 工程目录下，无需再做任何修改，并自动加入编译，大家只需要正常地编译、下载、调试即可。</p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rt-thread.org%2Fdocument%2Fsite%2Frtthread-studio%2Fum%2Fstudio-user-manual%2F%23cubemx" target="_blank">更多教程请访问文档中心</a>。</strong></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0331/090103_EMhs_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>5、完善和添加新QEMU模拟器</h1> 
<p>QEMU这次新增了两个模拟器：stm32f401 和 stm32f410 系列，大家可以在 SDK Manager 中下载最新版。配置 QEMU 时，在 Emulator 配置栏的下拉框中选择模拟器。另外，配置界面也做了一些更新，解决了一些用户反馈的问题。首先，新增了串口的配置，选择不同串口时，stdio 也会定位到对应的串口上；其次 SD Card Memory 改成了可选项，兼容不需要 SD 卡的情况；最重要的一点，将 -show-cursor 等命令移动到了 Extra Command 中，大家可以自定义这些命令的参数，让 QEMU 使用上更具灵活性。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0331/090152_KVHv_2720166.png" referrerpolicy="no-referrer"></p> 
<p>除了上述新增的功能亮点外，本次更新还修复了一些遗留问题，比如 workspace 不能切换的问题，现在已经可以正常切换了，对于构建时命令行过长超出 windows 命令行长度限制的问题也得到了有效解决。很多其它细节完善就不再详细讲述了，希望大家能亲自上手体验和发现。</p> 
<p>顺便告诉大家一个“彩蛋”，大家可以在 RT-Thread 文档中心网页右上角，看到 RT-Thread 官方的吉祥物，点击可以跳转到新版文档中心页，支持在线编辑，大家可以试试，以后发现文档中心有问题，可以直接在线修改了。</p> 
<p>已经安装过 Studio 的，打开 Studio 就可自动检测并升级到 V2.1.0 版本，没有安装的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rt-thread.org%2Fpage%2Fdownload.html%23studio" target="_blank">可以点此</a>下载安装 V2.1.0 完整安装包<strong>(建议不要覆盖安装</strong><strong>)</strong>。</p>
                                        </div>
                                      
</div>
            