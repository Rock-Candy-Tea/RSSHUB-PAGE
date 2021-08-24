
---
title: 'Linux Lab 发布 v0.8-rc1，Linux Lab Disk 同步支持 Deepin 20.2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic2.zhimg.com/80/v2-5ab7297335840b13f04200214d044db5_720w.jpg'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 02:20:00 GMT
thumbnail: 'https://pic2.zhimg.com/80/v2-5ab7297335840b13f04200214d044db5_720w.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start"><strong>1. 近期回顾</strong></h2> 
<p style="text-align:start">前不久，社区研发的 Linux Lab 开源项目在码云平台<a href="https://gitee.com/tinylab/linux-lab">迎来了第 1000 枚 Star</a>，我们同期发布了首支 Pocket Linux Disk，相继支持了 Ubuntu 18.04, 20.04 和 21.04，容量覆盖 16G, 32G, 64G, 128G, 512G ...</p> 
<p><img src="https://pic2.zhimg.com/80/v2-5ab7297335840b13f04200214d044db5_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">最近一段时间，社区主要成果如下：</p> 
<ul> 
 <li>持续推进开源之夏项目的开发，包括 Rust for Linux、openEuler Kernel 支持等几个项目进展都较为顺利，预期能通过中期评审，见<a href="http://gitee.com/tinylab/cloud-lab/issues">相关进展</a>。</li> 
 <li>发布 Linux Lab v0.8 rc1，主要是一些问题修复、openEuler Kernel 开发的初步支持以及 Pocket Linux 的相关支持。见<a href="https://gitee.com/tinylab/linux-lab">相关记录</a>。</li> 
</ul> 
<h2 style="text-align:start">2. 关键进展</h2> 
<p style="text-align:start">另外一个比较关键的进展这里单独拎出来介绍一下，那就是为 Pocket Linux Disk 和 Linux Lab Disk 相继新增了 Deepin 支持，即连续开发了两款 Deepin 2 go，都继承和支持 Linux Lab Disk 原有的特性功能，包括智能启动（业内独家自研的 vmboot 技术，插入 Disk 后自动运行）、透明倍容、时区兼容等。</p> 
<p style="text-align:start">Deepin 的引入有非常重要的里程碑意义：</p> 
<ul> 
 <li>Linux Lab Disk 和 Pocket Linux Disk 首次支持的 Ubuntu 是国外主导的开源项目，Deepin 是国内主导的开源项目，也是国内唯一一个成功获得社区用户认可和广泛使用的 GNU/Linux 发行版，并且有诸多原创性的贡献，比较突出的贡献是基于 Wine 的 Windows 程序运行环境方面的改进。</li> 
 <li>继 Wine 之后，Deepin 在近期发布的 20.2.2 版本中首次加入了安卓运行环境，并藉由内置的应用中心提供了不少适配好的安卓应用程序。</li> 
 <li>Deepin 还有不少本地客制化的工作，比如对中文方面的支持、对国产应用软件的集成与支持方面，比如微信、有道翻译、网易云音乐等。</li> 
 <li>另外，Deepin 对国产芯片的适配工作也在持续推进和完善，对龙芯、飞腾、申威、兆芯都有不错的支持与适配，运行效果已经满足基本的办公与服务器需要，体验也变得越来越好。</li> 
</ul> 
<p style="text-align:start">引入 Deepin 之后，Linux Lab Disk 和 Pocket Linux Disk 在原有特性功能的基础上将获得更多的易用性和本地化支持，将进一步降低国内用户的使用门槛，提升使用体验。</p> 
<h2 style="text-align:start">3. 成果一览</h2> 
<p style="text-align:start">Pocket Linux Disk 首批实物图：</p> 
<p><img src="https://pic4.zhimg.com/80/v2-da4f5b2194fe0463ea221711eb34699b_720w.jpg" width="388" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">Pocket Linux Disk 系统展示(Deepin 版）：</p> 
<p><img src="https://pic4.zhimg.com/80/v2-9e686cf56353ee1e3753265a89998dab_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p><img src="https://pic1.zhimg.com/80/v2-54e67aa1a0fc89268bae8e7ada5a6730_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p><img src="https://pic1.zhimg.com/80/v2-f0cae5f11caf353cee6c8274192f8dfc_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p><img src="https://pic3.zhimg.com/80/v2-272ae6cf4c3eb9024c390c3ba2b88e16_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">Linux Lab Disk 实物图：</p> 
<p><img src="https://pic2.zhimg.com/80/v2-855b65000d335c684eeb6dc1b2f83c5d_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"> </p> 
<p><img src="https://pic4.zhimg.com/80/v2-07984f3b4593599bfcff25ecf60808ef_720w.jpg" width="1028" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"> </p> 
<p><img src="https://pic2.zhimg.com/80/v2-e281090585a18701f2af3baea9ff55ed_720w.jpg" width="1024" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"> </p> 
<p><img src="https://pic3.zhimg.com/80/v2-1be6f1b205c3e2634f55d707d832aa2a_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"> </p> 
<p style="text-align:start"> </p> 
<p style="text-align:start">Linux Lab Disk 系统展示(Deepin 版）：</p> 
<p><img src="https://pic2.zhimg.com/80/v2-ae7f749e6e7420054567d6ee4c877b39_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p><img src="https://pic4.zhimg.com/80/v2-1c5dd15f61a17d244dd082e6bff84fcf_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p><img src="https://pic1.zhimg.com/80/v2-563f86de2971bef8c560c8e00f5c0ef0_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">4. 如何体验</h2> 
<p style="text-align:start">好了，怎么体验呢？</p> 
<p style="text-align:start">在某宝检索 “Pocket Linux系统” 或 “Linux Lab真盘” 即可找到，从 16G 到 512G，高速主控与固态主控的都有，欢迎选购。</p> 
<p style="text-align:start">Linux Lab Disk 可以让普通开发者在 1 分钟内进入 Linux 内核开发环境，3 分钟内完成编译与启动。</p> 
<p style="text-align:start">Pocket Linux Disk 可以让普通用户在 1 分钟内用起来 Linux 操作系统。</p> 
<p style="text-align:start">关键特性补充介绍：</p> 
<ul> 
 <li>两款 Disk 都能独立开机上电启动，也能在运行的 Windows 或 Linux 下并行自动启动，都能做到即插即用。</li> 
 <li>两款 Disk 都支持透明倍容，不仅不少容量，而且可用容量翻倍。</li> 
 <li>两款 Disk 全部采用 USB 3.x 接口 + 高速或固态主控，保障读写性能体验。另外，除了 16G 的入门版本，其他所有容量的 Disk 存储颗粒采用 MLC 或 SLC，读写都不掉速，16G 版本的最低写速也能到 20M/s 左右。</li> 
 <li>两款 Disk 最低都能支持 16G，虽然两款系统的数据大小都分别到了 17G 和 14G，但是透明倍容技术让 16G 的 Disk 都有几个 G 的剩余容量。</li> 
</ul> 
<p style="text-align:start">采用 Deepin 以后，大家更是可以欢快的跑大量 Windows 和 安卓应用程序了。</p> 
<p style="text-align:start">欢迎选购体验，Star，收藏，赞赏，转发，分享给周边的朋友。</p> 
<p style="text-align:start">感谢所有读者和用户的支持，祝好~~</p>
                                        </div>
                                      
</div>
            