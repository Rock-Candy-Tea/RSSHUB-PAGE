
---
title: 'Linux Lab 发布 v0.7-rc1，同步制作 200 枚固态 Linux Lab to go'
categories: 
 - 编程
 - 开源中国
 -  - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f1f2f1a16280adef46eb5218176f48f3b87.png'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 14:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f1f2f1a16280adef46eb5218176f48f3b87.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Flinux-lab" target="_blank">Linux Lab</a> 是一套用于 Linux 内核学习、开发和测试的即时实验室，可以极速搭建和使用，功能强大，用法简单！本次发布的 Linux Lab Disk (Linux Lab to go) 进一步降低使用门槛。</p> 
<p>以下为 Linux Lab Disk 使用效果图，具体请以实物为准。</p> 
<p><img alt="Linux Lab Logo" height="756" src="https://oscimg.oschina.net/oscnet/up-f1f2f1a16280adef46eb5218176f48f3b87.png" width="1024" referrerpolicy="no-referrer"></p> 
<p>可以用它来高效地学习处理器架构、Linux 内核、嵌入式 Linux 系统、C 语言编程、Linux 汇编、Shell 编程等。</p> 
<p><img alt="Linux Lab Boot example" src="https://oscimg.oschina.net/oscnet/up-b037301530df1be5a81c9a6fd44602ce421.JPEG" referrerpolicy="no-referrer"></p> 
<p>已经跃跃欲试了？！快来看看：</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Fpdfs%2Flinux-lab-v0.6-manual-zh.pdf" target="_blank">Linux Lab v0.6 中文手册</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Fpdfs%2Flinux-lab-v0.6-manual-en.pdf" target="_blank">Linux Lab v0.6 英文手册</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Fwhy-linux-lab%2F" target="_blank">Linux Lab：难以抗拒的十大理由 v1.0</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Fwhy-linux-lab-v2%2F" target="_blank">Linux Lab：难以抗拒的十大理由 v2.0</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Fpdfs%2Flinux-lab-loongson-manual-v0.2.pdf" target="_blank">Linux Lab 龙芯实验手册</a></p> </li> 
</ul> 
<p>如果想学习 Linux 0.11 内核和 Linux X86 汇编语言，也可以访问另外两套 Lab，即 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Flinux-0.11-lab" target="_blank">Linux 0.11 Lab</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Fcs630-qemu-lab" target="_blank">CS630 Qemu Lab</a>。</p> 
<p>本次发售的 Linux Lab Disk 内置了上述 3 套实验环境，免安装，上电开机后即可使用。</p> 
<p><strong>版本更新</strong></p> 
<p>Linux Lab 于 2 月初发布了 <a href="https://gitee.com/tinylab/linux-lab/tree/v0.6/">v0.6</a> 正式版本，同步发布了 Cloud Lab v0.4。</p> 
<p>经过近 2 个月的开发，本次发布 <a href="https://gitee.com/tinylab/linux-lab/tree/v0.7-rc1/">v0.7-rc1</a>，主要是新增了 Linux Lab Disk，一款可开机即用的 Linux Lab U盘，同时修复了 Windows 和 macOS 的 webvnc 登陆衰退问题。本次同步发布 Cloud Lab v0.5 rc1。</p> 
<p>Linux Lab Disk 进一步降低了 Linux Lab 的准入门槛：</p> 
<ul> 
 <li>完全做到免安装，上电开机即用，消除主机操作系统的兼容性和网络环境等的不确定性等因素</li> 
 <li>Linux Lab Disk 同时允许在 Windows 和 Linux 下通过虚拟机直接启动</li> 
 <li>另外，还新增了透明压缩和内存编译等提升容量和寿命的特性，预计 128G 可以写入 150-200G 左右，64G 可以写入 80G-100G 左右，具体情况因写入数据类型而异</li> 
</ul> 
<p>本次同步制作了 200 个高速固态版 Linux Lab Disk，128G 和 64G 各 100 个，来不及自己搭建 Linux Lab 的同学，可以上手体验了，购买入口在：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshop155917374.taobao.com%2F" target="_blank">泰晓科技自营店</a>。</p> 
<p>本次相比上一个版本，合计 61 笔变更：</p> 
<pre><code>// linux lab
$ git log --pretty=oneline v0.5..v0.6 | wc -l
9

// cloud lab
$ git log --pretty=oneline v0.3..v0.4 | wc -l
52
</code></pre> 
<p>本次主要更新如下：</p> 
<ul> 
 <li> <p>Linux Lab</p> 
  <ul> 
   <li> <p>更新 Arch/Manjaro 下的 Docker 安装文档</p> </li> 
   <li> <p>在其他目录下，禁用 Lab 的命令行补全功能</p> </li> 
   <li>新增内存编译功能和使用文档 
    <ul> 
     <li> <p>编译结果需明确保存，否则关机后会丢失</p> </li> 
     <li> <p>基本消除磁盘写操作，提升磁盘寿命</p> </li> 
     <li> <p>在机械硬盘等情况下编译速度会大大提升</p> </li> 
    </ul> </li> 
  </ul> </li> 
 <li> <p>Cloud Lab</p> 
  <ul> 
   <li> <p>完善 Lab 启动消息通知功能</p> </li> 
   <li> <p>新增桌面快捷方式对 Ubuntu 20.04 的支持</p> </li> 
   <li> <p>允许通过环境变量设置屏幕 Size</p> </li> 
   <li> <p>修复 Windows 和 macOS 系统上的 webvnc 连接异常</p> </li> 
   <li> <p>Lab 容器内新增音、视频播放支持</p> </li> 
   <li> <p>更新 Linux Lab 内的桌面快捷方式，新增公开课视频、在线中文手册等入口</p> </li> 
  </ul> </li> 
</ul> 
<p>Linux Lab Disk (Linux Lab to go) 相关资料如下：</p> 
<ul> 
 <li> <p>详细开发过程请参考：<a href="https://gitee.com/tinylab/linux-lab/issues/I31ZTK">Linux Lab 正在新增对 Linux Lab Disk 的支持</a>。</p> </li> 
 <li> <p>Demo 盘演示视频地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fzvideo%2F1341540839756070912" target="_blank">学 Linux 内核难吗？这款U盘把门槛降低到 5 分钟内</a></p> </li> 
</ul> 
<p><strong>环境准备</strong></p> 
<p>在非 Ubuntu 平台，请提前自行安装好 docker，可参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2Fdocker-for-mac%2F" target="_blank">Docker for Mac</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2Fdocker-for-windows%2F" target="_blank">Docker for Windows</a>。</p> 
<p>如果是老版本的 Windows，可以用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2Ftoolbox%2Foverview%2F" target="_blank">Docker Toolbox</a>，建议通过 Virtualbox 或 Vmware 自行安装 Ubuntu 后使用。</p> 
<p>国内的同学请<strong>务必</strong>使用国内的 Docker 镜像服务，否则无法正常下载镜像，推荐参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhelp.aliyun.com%2Fdocument_detail%2F60750.html" target="_blank">阿里云镜像配置文档</a>。</p> 
<p>下面的链接是大家成功运行过 Linux Lab 的主机环境，欢迎参考，安装完以后也欢迎登记上来。</p> 
<ul> 
 <li> <p><a href="https://gitee.com/tinylab/linux-lab/issues/I1FZBJ">成功运行过 Linux 的操作系统和 Docker 版本列表</a></p> </li> 
</ul> 
<p><strong>极速体验</strong></p> 
<p>该版本依赖最新的 Cloud Lab 和 docker 镜像：</p> 
<pre><code>$ git clone https://gitee.com/tinylab/cloud-lab.git
$ cd cloud-lab
$ tools/docker/pull linux-lab     # 确保更新 docker 镜像
$ tools/docker/run linux-lab
</code></pre> 
<p>已经下载过的，请更新到最新版本并重启 Linux Lab：</p> 
<pre><code>$ cd cloud-lab && git pull
$ pushd labs/linux-lab && git pull && popd
$ tools/docker/rerun linux-lab
</code></pre> 
<p>进去以后，打开控制台，敲入如下命令即可启动一个虚拟开发板（自动下载预编译的版本）：</p> 
<pre><code>$ make boot
</code></pre> 
<p>一键编译和启动（自动下载源码、检出版本、打补丁、配置、编译）：</p> 
<pre><code>$ make boot BUILD=kernel
</code></pre> 
<p>默认使用的是 <code>arm/vexpress-a9</code>，如果要使用真实开发板，在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshop155917374.taobao.com%2F" target="_blank">购买</a>并连接串口和网口到开发主机后，可以简单切换：</p> 
<pre><code>$ make BOARD=arm/ebf-imx6ull
$ make login
</code></pre> 
<p>真实开发板与虚拟开发板用法有细微差异，其详细用法请参考：<a href="https://gitee.com/tinylab/linux-lab/tree/master/boards/arm/ebf-imx6ull">boards/arm/ebf-imx6ull/README.md</a>。</p> 
<p><strong>关键特性</strong></p> 
<p>Linux Lab 具备如下特性：</p> 
<ol> 
 <li> <p>支持 3 大操作系统（Windows、MacOS、Linux），可以轻松在这三大操作系统下使用。</p> </li> 
 <li> <p>支持 7+ 大处理器架构（X86、ARM、MIPS、PPC、CSKY，RISC-V, LOONGSON），其中 LOONGSON 和 CSKY 为国产处理器。</p> </li> 
 <li> <p>支持 17+ 款开发板（i386/pc, x86_64/pc, arm/versatilepb, arm/vexpress-a9, ppc/g3beige, mips/malta, aarch64/virt, aarch64/raspi3, riscv32/virt, riscv64/virt, csky/virt, loongson/ls1b, loongson/ls2k, loongson/ls232, loongson/ls3a7a, arm/ebf-imx6ull）。</p> </li> 
 <li> <p>支持 5 种登陆方式（docker, ssh, vnc，webssh, webvnc），可以本地访问，也可以远程访问。</p> </li> 
 <li> <p>集成了 5 大组件（Qemu、U-boot、Buildroot、Linux、Toolchain），都有预编译版本。</p> </li> 
 <li> <p>内置了 5 大平台，32 位和 64 位共 10 个 Hello World 汇编语言例程，见 <code>examples/assembly</code>。</p> </li> 
 <li> <p>可以学习处理器指令集、Qemu、Shell、汇编、C、Linux 内核、嵌入式 Linux。</p> </li> 
 <li> <p>支持 Debugging 和 Testing。</p> </li> 
 <li> <p>host & guest 双侧免 root 使用。</p> </li> 
</ol> 
<p><strong>更多信息</strong>：</p> 
<ol> 
 <li> <p>项目首页</p> 
  <ul> 
   <li> <p>Homepage: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftinylab.org%2Flinux-lab" target="_blank">http://tinylab.org/linux-lab</a></p> </li> 
  </ul> </li> 
 <li> <p>项目社群</p> 
  <ul> 
   <li> <p>联系微信：tinylab</p> </li> 
   <li> <p>联系公号：泰晓科技</p> </li> 
   <li> <p>Linux Lab 用户交流群</p> </li> 
   <li> <p>Linux Lab 开发者</p> </li> 
  </ul> </li> 
 <li> <p>项目仓库</p> 
  <ul> 
   <li> <p>Gitee: <a href="https://gitee.com/tinylab/linux-lab">https://gitee.com/tinylab/linux-lab</a></p> </li> 
   <li> <p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftinyclub%2Flinux-lab" target="_blank">https://github.com/tinyclub/linux-lab</a></p> </li> 
  </ul> </li> 
 <li> <p>视频教程</p> 
  <ul> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV12K411P79C" target="_blank">Linux Lab 入门</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1xz4y1Z7ag" target="_blank">基于 Linux Lab 进行龙芯 Linux 内核开发</a></p> </li> 
  </ul> </li> 
 <li> <p>在线演示</p> 
  <ul> 
   <li> <p>基本用法：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F6fb264246580281d372c6" target="_blank">Linux 快速上手</a></p> </li> 
   <li> <p>学习汇编：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F0f0c2a6e754702a429269" target="_blank">AT&T 汇编上手</a></p> </li> 
   <li> <p>学习Uboot：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F11f5ae44b211b56a5d267" target="_blank">Uboot 快速上手</a></p> </li> 
   <li> <p>ARM 开发：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2Fc351abb6b1967859b7061" target="_blank">在 arm/vexpress-a9 上运行 Ubuntu 18.04 LTS</a></p> </li> 
   <li> <p>RISC-V开发：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F37ce75e5f067be2cc017f" target="_blank">使用 riscv32/virt 和 riscv64/virt 开发板</a></p> </li> 
   <li> <p>龙芯开发：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F1eca85a09775fd212d827" target="_blank">在 Linux Lab 上使用龙芯 ls2k 平台</a></p> </li> 
   <li> <p>特性开发：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F7edd2e51e291eeca59018" target="_blank">一条命令测试和体验某个内核特性</a></p> </li> 
   <li> <p>模块开发：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F26b78172aa926a316668d" target="_blank">一条命令配置、编译和测试内核模块</a></p> </li> 
   <li> <p>内核调试：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F0255c6a8b7d16dc116cbe" target="_blank">所有板子的调试功能自测视频</a></p> </li> 
   <li> <p>内核测试：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshowterm.io%2F8cd2babf19e0e4f90897e" target="_blank">所有当前预置板子的启动过程自测视频</a></p> </li> 
  </ul> </li> 
</ol> 
<p>该项目开源，以 GPL 2.0 协议发布，欢迎所有高校、企业、个人用户使用或者参与开发。</p> 
<p>欢迎通过微信号（tinylab）联系我们，联系后可以获邀进 <strong>Linux Lab 用户交流群</strong> 和 <strong>Linux Lab 开发者群</strong>，还将获赠 Linux Lab 安装文档和 Linux Lab 大会演讲幻灯片。</p>
                                        </div>
                                      
</div>
            