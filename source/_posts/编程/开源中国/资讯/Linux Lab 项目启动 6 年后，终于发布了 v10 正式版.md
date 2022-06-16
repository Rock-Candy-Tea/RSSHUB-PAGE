
---
title: 'Linux Lab 项目启动 6 年后，终于发布了 v1.0 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1666'
author: 开源中国
comments: false
date: Thu, 16 Jun 2022 17:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1666'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><span>简介</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">自 Linux Lab v0.9 发布以后，又经过了 5 个月的漫长迭代，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftinylab.org%2Flinux-lab" target="_blank">Linux Lab</a> 终于迎来了 v1.0 正式版，同时也迎来了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftinylab.org%2Fcloud-lab" target="_blank">Cloud Lab</a> v0.80-rc1 版本，两者需同步升级配合使用。</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0">发布仓库</p> 
  <ul style="list-style-type:square"> 
   <li> <p>Gitee: <a href="https://gitee.com/tinylab/linux-lab">https://gitee.com/tinylab/linux-lab</a></p> </li> 
   <li> <p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftinyclub%2Flinux-lab" target="_blank">https://github.com/tinyclub/linux-lab</a></p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">用户手册</p> 
  <ul style="list-style-type:square"> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftinylab.org%2Fpdfs%2Flinux-lab-v1.0-manual-zh.pdf" target="_blank">Linux Lab v1.0 中文手册</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftinylab.org%2Fpdfs%2Flinux-lab-v1.0-manual-en.pdf" target="_blank">Linux Lab v1.0 英文手册</a></p> </li> 
  </ul> </li> 
</ul> 
<h2><span>更新情况</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">Linux Lab v1.0 升级了部分内核版本到 v5.17，修复了多处内存编译 Bug，优化了 make 命令自动补全功能，并重点完善和新增了 examples，同时更新文档对齐到最新的功能。</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0">v1.0 rc3</p> 
  <ul style="list-style-type:square"> 
   <li> <p>全面整理 Assembly 实验案例</p> </li> 
   <li> <p>删除多余的 do target，由其他更简洁的用法替代</p> </li> 
   <li> <p>允许更简单编译内核目标文件，例如：<code>make kernel arch/riscv/kernel/sbi.o</code></p> </li> 
   <li> <p>修复 make 自动命令补全，允许通过 tab 按键快速补全常用命令</p> </li> 
   <li> <p>完善 make patch 命令</p> </li> 
   <li> <p>更新文档和 License 信息</p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">v1.0 rc2</p> 
  <ul style="list-style-type:square"> 
   <li> <p>升级 RISC-V 支持，qemu 升级到 v6.0.0，内核升级到 v5.17</p> </li> 
   <li> <p>升级 arm/vexpress-a9 的默认内核到 v5.17</p> </li> 
   <li> <p>规范 build 输出路径，跟 <code>boards/</code> 下的路径保持一致，方便更快找到目标文件</p> </li> 
   <li> <p>完善 docker 文件系统运行和导出支持</p> </li> 
   <li> <p>新增 Python 实验案例</p> </li> 
   <li> <p>完善 Assembly 和 Shell 实验案例</p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">v1.0 rc1</p> 
  <ul style="list-style-type:square"> 
   <li> <p>增强 test 功能，允许在 testcase 中执行多个命令</p> </li> 
   <li> <p>修复 test 中的内核参数传递问题，确保兼容 uboot 和 kernel</p> </li> 
   <li> <p>允许灵活增加 app 的子 make 目标，例如 <code>make root busybox-menuconfig</code></p> </li> 
   <li> <p>修复两笔内存编译的问题</p> </li> 
  </ul> </li> 
</ul> 
<h2><span>项目感想</span></h2> 
<h3><span>历史回顾</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">Linux Lab v1.0 是一个很重要的里程碑，不仅意味着其核心功能已经非常稳定和完善，也意味着我们的工作重心将发生调整。在 v1.0 之后，我们将把重点调整到 examples 的开发上，将通过 examples 帮助更多的同学更高效地学习、研究和开发操作系统以及周边的技术。</p> 
<p style="color:black; margin-left:0; margin-right:0">刚刚查看了第一笔提交记录：</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">Author: Wu Zhangjin <a href="https://www.oschina.net/action/GoToLink?url=mailto%3Awuzhangjin%40gmail.com" target="_blank">wuzhangjin@gmail.com</a><br> Date: Mon Jul 11 09:06:04 2016 +0800</p> 
 <p style="color:black; margin-left:0; margin-right:0">Init linux-lab</p> 
 <p style="color:black; margin-left:0; margin-right:0">Aims to build a Qemu-based Linux Lab to easier the Linux Learning and new features development.</p> 
 <p style="color:black; margin-left:0; margin-right:0">Signed-off-by: Wu Zhangjin <a href="https://www.oschina.net/action/GoToLink?url=mailto%3Awuzhangjin%40gmail.com" target="_blank">wuzhangjin@gmail.com</a></p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0">非常令人感慨，六年前肯定想不到，今天的 Linux Lab v1.0 已经支持了市面上所有的主流处理器架构，支持了 20 多款开发板，支持了从 v0.11 到 v5.x 的几乎所有 Linux 内核版本，加 Cloud Lab 在内，一共有 3294 笔变更，每一笔背后都是煞费苦心的设计和思考以及大量繁琐的验证和测试。</p> 
<pre><code>$ cd cloud-lab/labs/linux-lab
$ git log --oneline --root | wc -l
2152

$ cd ../../
$ git log --oneline --root | wc -l
1142
</code></pre> 
<p style="color:black; margin-left:0; margin-right:0">我想说，这份努力是值得的，作为计算机软件中偏底层最接近硬件最复杂的操作系统，向来是相对比较难上手的，最大的门槛是重复又依赖繁多的环境构建，但是有了 Linux Lab，继而有了 Linux Lab Disk，我们可以在 1 分钟内进入实验环境，在 10 分钟内编译并启动 Linux 内核，Linux 内核与嵌入式 Linux 开发从未像今天这般简单。</p> 
<p style="color:black; margin-left:0; margin-right:0">期待我们的工作对操作系统的人才培养、技术孵化、开发效率等方面都有所助力！</p> 
<h3><span>感谢致谢</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">感谢六年来，所有参与、支持和鼓励过这个项目的同学们！没有你们的支持，这个项目也许早就夭折了；没有你们的支持，我们不会有动力不厌其烦地去完善和迭代，那些 Bug Report，Patch，赞誉背后的支持让所有的开发不再孤立无援，而是温暖充盈。</p> 
<p style="color:black; margin-left:0; margin-right:0">也要特别感谢这个项目用到的所有开源项目，包括但是不限于：Ubuntu, Linux, Docker, Qemu, Buildroot, U-Boot, Busybox, Make, webvnc 等等，没有这些工作，就不可能有 Linux Lab。</p> 
<p style="color:black; margin-left:0; margin-right:0">同时感谢项目的托管平台：Github 和 Gitee，也要感谢曾经赞助过这个项目的企业、研究所和个人，包括购买过 Linux Lab Disk 以及社区所有其他付费服务的所有同学们！</p> 
<p style="color:black; margin-left:0; margin-right:0">另外，这六年来，家里的夫人和小伙伴也给了莫大的支持，这个项目牺牲了很多本应该陪伴他们的时间。随着 v1.0 版本的发布，希望后面能够有更多的时间陪伴他们。</p> 
<h3><span>商业化尝试</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">过去数年来，包括社区和项目在内，所有的开发和答疑都是公益性质的，是个人投入资金和时间在运营，虽然有获得了一些赞助，但是杯水车薪。</p> 
<p style="color:black; margin-left:0; margin-right:0">为了项目的持续健康发展，在经过艰难的考虑后，我们做了一些商业化尝试，希望大家能够多多支持。</p> 
<ul style="list-style-type:disc"> 
 <li> <p>Cloud Lab 和 Linux Lab 项目都采用双 Licenses，非商业用户采用 GPL v2 协议，商业用户需要获得商业授权。</p> </li> 
 <li> <p>之前维护的开发板和内核版本数量巨大，答疑和维护已经令人精疲力尽，所以开发板部分，后续仅默认开放 <code>arm/vexpress-a9</code>，其他开发板将暂停开放并可根据需要付费购买服务。也欢迎其他企业、机构或个人联系赞助某个开发板或处理器架构，获得相应的资源后，社区将考虑重新开放对应的开发板或处理器架构。</p> </li> 
 <li> <p>社区也研发了免安装即插即跑的 Linux Lab Disk，也叫泰晓 Linux 实验盘，插上即可开展 Linux 内核与嵌入式 Linux 开发，容量覆盖 32G-2T，支持智能启动、透明压缩、时区兼容、出厂恢复等新创特性，用户可根据需要选购。欢迎高校、企业和机构联系团购，泰晓 Linux 实验盘可用于高校计算机实验室、企业内部培训等。</p> </li> 
</ul> 
<h2><span>更多资料</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0">使用 Linux Lab 的好处</p> 
  <ul style="list-style-type:square"> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftinylab.org%2Fwhy-linux-lab" target="_blank">Linux Lab：难以抗拒的十大理由 V1.0</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftinylab.org%2Fwhy-linux-lab-v2" target="_blank">Linux Lab：难以抗拒的十大理由 V2.0</a></p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">Linux Lab 视频公开课：含用法介绍、使用案例分享、发布会视频回放、Linux Lab Disk功能演示等</p> 
  <ul style="list-style-type:square"> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cctalk.com%2Fm%2Fgroup%2F88948325" target="_blank">CCTALK</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspace.bilibili.com%2F687228362%2Fchannel%2Fdetail%3Fcid%3D152574" target="_blank">B 站</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fwuzhangjin" target="_blank">知乎</a></p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">采用 Linux Lab 作为实验环境的视频课程</p> 
  <ul style="list-style-type:square"> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cctalk.com%2Fm%2Fgroup%2F88089283" target="_blank">《360° 剖析 Linux ELF》</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcctalk.com%2Fm%2Fgroup%2F89507527" target="_blank">《Rust 语言快速上手》</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cctalk.com%2Fm%2Fgroup%2F89626746" target="_blank">《软件逆向工程初探》</a></p> </li> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cctalk.com%2Fm%2Fgroup%2F89715946" target="_blank">《Linux内核热补丁技术介绍与实战》</a></p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">采用 Linux Lab 或者 Linux Lab 正在支持的图书、课程等</p> 
  <ul style="list-style-type:square"> 
   <li> <p><a href="https://gitee.com/tinylab/linux-lab/issues/I49VV9">成功适配过 Linux Lab 的国内外图书、线上课程列表</a></p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">采用 Linux Lab 或者 Linux Lab 正在支持的真实硬件开发板</p> 
  <ul style="list-style-type:square"> 
   <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshop155917374.taobao.com%2F" target="_blank">ARM IMX6ULL</a>，野火电子</p> </li> 
   <li> <p>RISCV-64 D1, 平头哥</p> </li> 
  </ul> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">Linux Lab 社区正在开发的周边硬件</p> 
  <ul style="list-style-type:square"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshop155917374.taobao.com%2F" target="_blank">Linux Lab Disk</a>，免安装、即插即用 Linux Lab 开发环境 
    <ul style="list-style-type:square"> 
     <li> <p>支持 Ubuntu 18.04-21.04, Deepin 20.2+, Fedora 34+, Mint 20.2+, Ezgo 14.04+, Kali, Manjaro</p> </li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshop155917374.taobao.com%2F" target="_blank">Pocket Linux Disk</a>，免安装、即插即用 Linux 发行版 
    <ul style="list-style-type:square"> 
     <li> <p>支持 Ubuntu 18.04-21.04, Deepin 20.2+, Fedora 34+, Mint 20.2+, Ezgo 14.04+, Kali, Manjaro</p> </li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            