
---
title: 'Coreboot 4.16 发布，替代 BIOS 和 UEFI 的开源项目'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6060'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6060'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Coreboot 原名 LinuxBIOS，是一个旨在取代计算机中专有固件（BIOS 或 UEFI）的软件项目，它采用轻量级固件设计，只执行加载和运行现代 32 位或 64 位操作系统所需的最少量任务。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">由于 coreboot 要初始化硬件，所以必须为所要支持的每个芯片组和主板移植。因此而言，coreboot 只适用于有限的硬件平台和主板型号。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">近日，coreboot 4.16 正式发布，自 4.15 版本以来，有 170 名开发者提交了 1770 个新文件。其中，有超过 35 人是第一次为 coreboot 做出贡献。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">新的主板：</span></p> 
<ul> 
 <li>Acer Aspire VN7-572G</li> 
 <li>AMD Chausie</li> 
 <li>ASROCK H77 Pro4-M</li> 
 <li>ASUS P8Z77-M</li> 
 <li>Emulation QEMU power9</li> 
 <li>Google Agah</li> 
 <li>Google Anahera4ES</li> 
 <li>Google Banshee</li> 
 <li>Google Beadrix</li> 
 <li>Google Brya4ES</li> 
 <li>Google Crota</li> 
 <li>Google Dojo</li> 
 <li>Google Gimble4ES</li> 
 <li>Google Herobrine_Rev0</li> 
 <li>Google Kingler</li> 
 <li>Google Kinox</li> 
 <li>Google Krabby</li> 
 <li>Google Moli</li> 
 <li>Google Nereid</li> 
 <li>Google Nivviks</li> 
 <li>Google Primus4ES</li> 
 <li>Google Redrix4ES</li> 
 <li>Google Skyrim</li> 
 <li>Google Taeko4ES</li> 
 <li>Google Taniks</li> 
 <li>Google Vell</li> 
 <li>Google Volmar</li> 
 <li>Intel Alderlake-N RVP</li> 
 <li>Prodrive Atlas</li> 
 <li>Star Labs Star Labs StarBook Mk V (i3-1115G4 and i7-1165G7)</li> 
 <li>System76 gaze16 3050</li> 
 <li>System76 gaze16 3060</li> 
 <li>System76 gaze16 3060-b</li> 
</ul> 
<p> 移除的主板：</p> 
<ul> 
 <li>Google ->  Corsola</li> 
 <li>Google ->  Nasher</li> 
 <li>Google ->  Stryke</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span><span style="background-color:rgba(0, 0, 0, 0.01)"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span>添加的处理器：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>src/cpu/power9</li> 
 <li><span><span><span><span><span><span><span><span><span style="background-color:rgba(0, 0, 0, 0.01)"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span>src/soc/amd/sabrina</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start">子模块更新</p> 
<ul> 
 <li>/3rdparty/amd_blobs (6 commits)</li> 
 <li>/3rdparty/arm-trusted-firmware (965 commits)</li> 
 <li>/3rdparty/blobs (30 commits)</li> 
 <li>/3rdparty/chromeec (2212 commits)</li> 
 <li>/3rdparty/intel-microcode (1 commits)</li> 
 <li>/3rdparty/qc_blobs (13 commits)</li> 
 <li>/3rdparty/vboot (44 commits)</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:rgba(0, 0, 0, 0.01)">官方表示，</span><span><span><span><span><span><span><span><span><span style="background-color:rgba(0, 0, 0, 0.01)"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span>2022 年 11 月 4.18 版本发布后，其</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:rgba(0, 0, 0, 0.01)">计划将转移对任何仍然需要 RESOURCE_ALLOCATOR_V3 的 boards 的支持到 4.18 分支。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:rgba(0, 0, 0, 0.01)">并</span><span><span><span><span><span><span><span><span><span style="background-color:rgba(0, 0, 0, 0.01)"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span>计划从 4.18 版开始弃用 LEGACY_SMP_INIT；</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>还包括 SMM_ASEG 的代码路径。此代码用于启动 AP 并在每个 AP 上进行一些功能编程，还用于设置 SMM。这在很大程度上已被 PARALLEL_MP 所取代，它应该能够涵盖 LEGACY_SMP_INIT 的所有用例，只需很少的代码更改。弃用的原因在于拥有 2 个代码路径来执行几乎相同的操作会大大增加社区的维护负担，同时也相当混乱。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#333333">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.coreboot.org%2Fblog%2F2022%2F02%2F26%2Fannouncing-coreboot-4-16%2F" target="_blank">查看官方博客</a>。</span></p>
                                        </div>
                                      
</div>
            