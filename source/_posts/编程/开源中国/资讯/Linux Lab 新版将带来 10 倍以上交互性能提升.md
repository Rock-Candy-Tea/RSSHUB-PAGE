
---
title: 'Linux Lab 新版将带来 10 倍以上交互性能提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic4.zhimg.com/80/v2-9255630f542e8d572d5c2b2ae1cf9e67_720w.jpg'
author: 开源中国
comments: false
date: Sun, 26 Dec 2021 19:55:00 GMT
thumbnail: 'https://pic4.zhimg.com/80/v2-9255630f542e8d572d5c2b2ae1cf9e67_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#121212; margin-left:0; margin-right:0; text-align:start">大家好，经过两周多超级紧张的研发，国产<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2Ftinylab%2Flinux-lab" target="_blank">Linux Lab</a><span> </span>开源项目迎来了重大功能和体验提升，不仅首次完整支持 Windows，而且各项性能提升数倍到数十倍，即将发布到 v0.9 正式版，做好了充分的准备去迎接来年的 v1.0。v0.9 正式版争取在农历新年之前发布。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">项目地址在此：</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2Ftinylab%2Flinux-lab" target="_blank">gitee.com/tinylab/linux-lab</a></p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">相关成果如下：</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">一、功能支持：首次完全兼容 Windows 平台</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Linux Lab 两年前就已经支持 Windows，鉴于早期缺少开发环境，所以一直未能提供完整支持。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">经过本次的紧张适配开发，现在已经完全兼容 Windows 平台下的 Docker toolbox 及 Docker Desktop with wsl2，minix 和 nfs 也完整导入，功能上已经与 Linux 版本的 Linux Lab 完全一致，各项性能指标也已经达到了可以欢快使用的状态。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">继上个版本支持 openeuler 内核开发后，本次新增了微软 wsl2 内核开发，可一条命令自动抓取最新的版本、完成编译并直接替换掉本地微软自带的 wsl2 内核，在 Windows 下开发 wsl2 内核变得超级简单。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-9255630f542e8d572d5c2b2ae1cf9e67_720w.jpg" width="1920" referrerpolicy="no-referrer"></p> 
<p>Linux Lab Disk、Linux Lab with Docker toolbox 与 Linux Lab with wsl2 based Docker Desktop 并存</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">二、启动速度提升 10 倍，6s 可启动</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">从桌面点击 Linux Lab 的启动速度提升了 10 倍，目前 Linux 下仅需 6秒（新版已经优化到 4 秒内），Windows 平台下也仅需 30-50s。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">为了解决 Windows 平台下的 I/O 性能问题（主要是 MSYS2），过去两周，早期的 Cloud Lab（Linux Lab 运行环境与工具）得到了大规模的重构，大量的 I/O 操作得以消除或优化，交互响应得到了相当程度的优化，目前使用非常顺畅。</p> 
<p><img src="https://pic1.zhimg.com/80/v2-9b36eaec09159deeadf03ed180b0104c_720w.jpg" width="798" referrerpolicy="no-referrer"></p> 
<p>Linux Lab for Linux 仅需 6s 就可启动，最新版仅需 4s</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">三、编译速度提升 10 倍以上，6 分钟可完成下载、编译并引导启动</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">全新增加了 Fast Fetch 和 Oneshot memory 编译模式，从下载全新内核源码、编译并启动新编译的内核，仅需 6 分钟（CPU: I7-8550U @1.9G HZ，Memory: 8G, Internet: 300M）。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">6 分钟为 Windows 下实测数据，Windows 平台优化到了与 Linux 平台相当，Linux 平台应该仅需 5 分钟左右。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Windows 原生 wsl2 的 I/O 性能极慢（wsl2 挂载进来的磁盘是通过本地网络访问的，Docker Toolbox 基于虚拟机的共享文件夹方式的 I/O 性能也一般），Linux Lab for Windows 通过 Fast Fetch 和 Oneshot memory 模式彻底消除了 wsl2 和 Docker toolbox 的 I/O 问题，包括性能以及其他文件系统的兼容性问题（符号链接、符号大小写等）也一并消除。相关功能对 Linux 和 MacOS 版本同样有效，欢迎 Linux 和 MacOS 的小伙伴抢先体验和反馈，切换到 next 分支即可抢鲜。</p> 
<p><img src="https://pic2.zhimg.com/80/v2-99b37c1ac6acc7b6f07925d1ef1fae2d_720w.jpg" width="985" referrerpolicy="no-referrer"></p> 
<p>在 Linux Lab for Windows+wsl2 上仅需 6m 中可完成一个全新内核的下载、编译和启动</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">四、指令响应提升 10-20 倍，从2000毫秒左右降低到100多毫秒</h3> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Linux Lab 本身内建的各种交互指令也得到了进一步的性能提升，经过数项优化，指令响应时间从 3-5s 直接优化到了 100 多毫秒，如下是其中一项优化，直接提升了 10 倍，综合各项优化，提升了数十倍，交互体验从略显卡慢到酣畅淋漓。</p> 
<p><img src="https://pic1.zhimg.com/80/v2-3902723a842873654e93c54783604288_720w.jpg" width="1016" referrerpolicy="no-referrer"></p> 
<p>Linux Lab for Linux 交互响应进入毫秒级时代，迎来酣畅淋漓的体验</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">这是 Linux Lab 开源项目的一小步，但很可能是国内 Linux 以及 OS 开发领域的“一大步”，相关成果进一步把底层计算机操作系统以及周边技术的开发与实践门槛降低到极致时间，将开放怀抱迎接更多的人才进入底层芯片与 OS 开发领域，提升国内的行业竞争力。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">另外，Linux Lab 开源项目上周获得了迄今为止第一笔来自个人用户的大额赞助，在这里特别感谢软件所吴伟老师的长期鼓励和支持，吴伟老师团队长期深耕难啃的编译器技术以及周边，目前聚焦 RISC-V 方向，欢迎大家关注他团队的 hellogcc 公众号。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">Linux Lab v0.9 正式版将在 README 等文档增加个人和企业赞助榜单，以感谢大家的热情支持。借这个机会特别感谢其他企业和机构对该开源项目的直接或间接支持，包括龙芯、统信、软件所、野火、平头哥与全志等。</p> 
<p style="color:#121212; margin-left:0; margin-right:0; text-align:start">最后，欢迎大家订阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Ft.zsxq.com%2FuB2vJyF" target="_blank">Linux 知识星球</a><span> </span>以便关注项目开发动态与相关性能提升的最佳优化实践。也可以直接在某宝检索 Linux Lab 选购免安装版随身款 Linux Lab Disk 快速上手。</p> 
<p><img src="https://pic3.zhimg.com/80/v2-de1854f2253ce6abafe94c6b926dc7be_720w.jpg" width="1920" referrerpolicy="no-referrer"></p> 
<p>Linux Lab Disk 内置 Linux Lab, Linux 0.11 Lab 等，免安装，支持：智能启动、透明倍容和时区兼容</p> 
<p><img src="https://pic1.zhimg.com/80/v2-af35d35ddbcd3a6bf9992365fe4d4d04_720w.jpg" width="1280" referrerpolicy="no-referrer"></p> 
<p>Linux Lab Disk 实际启动与使用效果 / kali Linux 版</p>
                                        </div>
                                      
</div>
            