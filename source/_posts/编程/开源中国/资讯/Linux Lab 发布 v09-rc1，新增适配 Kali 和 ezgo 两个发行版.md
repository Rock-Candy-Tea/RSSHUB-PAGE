
---
title: 'Linux Lab 发布 v0.9-rc1，新增适配 Kali 和 ezgo 两个发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic3.zhimg.com/80/v2-063226f8ec64f9cefda4ac352169dade_720w.jpg'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 09:29:00 GMT
thumbnail: 'https://pic3.zhimg.com/80/v2-063226f8ec64f9cefda4ac352169dade_720w.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0"><strong>简介</strong></h2> 
<p style="margin-left:0; margin-right:0">自 Linux Lab v0.8 正式版发布以来，社区计划在 v0.9 继续新增嵌入式图形系统 GuiLite 和 RISC-V 真实开发板支持，目前急需社区的同学踊跃报名参与，有一定基础并且乐于参与社区开发与贡献的同学，欢迎联系申请 RISC-V 开发板（数量有限，先到先得）。当然，也欢迎大家贡献更多其他的新功能。</p> 
<p><img src="https://pic3.zhimg.com/80/v2-063226f8ec64f9cefda4ac352169dade_720w.jpg" width="509" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">这段时间，应同学们的需求，社区为随身 Linux Lab Disk（即 Linux Lab 真盘）新增了面向 Security 的 Kali Linux 发行版支持（适合研究安全的同学使用），同时新增了面向儿童教育领域的 EZGO Linux 发行版支持（适合小朋友或者小朋友的家长们指导孩子使用），目前支持范围扩大到：Ubuntu 18.04/20.04/21.04, Deepin 20.2, Manjaro, Fedora 34, Kali Linux, EZGO 14，欢迎留言提出其他需求。</p> 
<p><img src="https://pic1.zhimg.com/80/v2-52c9306166776fc074980df44fce9b94_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">Linux Lab Disk 可以免安装、零配置、即插即用，插入我们的任意一台 X86 台式机或者笔记本后，1分钟内就能学习和使用 Linux 系统，还能直接做C语言、Python、Rust、操作系统等技术实验与开发。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-06e8a90279c4ba4635dc3c34342e3477_720w.jpg" width="1024" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">另外，为降低答疑、咨询和维护的开销，社区临时关闭了部分Linux Lab 虚拟开发板的访问权限，这部分虚拟开发板未来可能会转为付费服务，以便有足够的资源支持后续的维护和迭代，谢谢理解。</p> 
<p><img src="https://pic1.zhimg.com/80/v2-8f7c280278a9743a7197f007df1d2ad8_720w.jpg" width="687" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">以上表格未同步到最新，最新的大部分已支持到 v5.13。</p> 
<h2 style="margin-left:0; margin-right:0"><strong>Linux Lab v0.9-rc1</strong></h2> 
<p style="margin-left:0; margin-right:0">社区在 v0.9-rc1 为 Cloud Lab 升级了 Linux Lab 的镜像并新增了对 KDE konsole 终端的支持。与此同时，做了如下几处变更：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>大部分开发板的默认内核版本调整为 v5.13。</li> 
 <li>为 boot-test 新增缺失的 bsp 自动下载依赖。</li> 
 <li>升级 llvm 工具链到最新的 13</li> 
 <li>对 list-linux 结果按版本排序</li> 
 <li>为 kernel-cleanup 新增 kernel-cleansrc 别名并新增 kernel-cleanall，可触发 cleansrc 和 clean</li> 
 <li>更新 x86_64/pc 的编译器配置</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><strong>Linux Lab Disk</strong></h2> 
<p style="margin-left:0; margin-right:0">近期有不少同学在咨询 Linux Lab Disk 是否支持 Kali Linux，这款发行版主要是面向网络安全领域，在经过一番调研后，社区花了一周时间进行适配，目前已经完美支持，这款发行版的体验非常棒，控制台的提示符、主题风格都很有特色，另外，面向 Security 方面的工具也非常全面。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-c2bd03046f15ed315b68baa83a40e92f_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p><img src="https://pic1.zhimg.com/80/v2-b4369d1397f39430731bc8f7f015c7b8_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">与此同时，考虑到诸多小朋友和家长的需要，我们特别适配了一款专门面向儿童教育领域的名叫 EZGO 的 Linux 发行版，这款发行版由宝岛台湾那边的社区朋友们开发，集成了非常多的面向儿童教育领域的开源软件，非常适合小朋友和家长指导孩子们学习时使用，社区也将陆续新增包括 Scratch 在内的各类软件进去，方便大家在学习其他课程的同时学好信息学。</p> 
<p><img src="https://pic4.zhimg.com/80/v2-d625b1886dc584cf4307a532dec2ab5f_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<p><img src="https://pic1.zhimg.com/80/v2-8fbf2a90b75d46e4f2c7221e5131593c_720w.jpg" width="1080" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0"><strong>小结</strong></h2> 
<p style="margin-left:0; margin-right:0">为方便大家更快捷地体验到 Linux Lab，社区趁双十一制作好了数十枚 32G-128G 的免安装、即插即用版 Linux Lab Disk 和 Pocket Linux Disk（未预装 Linux Lab，其他同 Linux Lab Disk），可选系统已经进一步覆盖：Ubuntu 18.04/20.04/21.04, Deepin 20.2, Manjaro, Fedora 34, Kali Linux, EZGO 14。如有需要，大家可以在某宝检索 “Linux Lab真盘” 或 “Pocket Linux系统”。</p> 
<p style="margin-left:0; margin-right:0">新增的 ezgo 预装了很多开源的教育软件，适合带娃学习的家长朋友们，而 Kali Linux 集成了很多安全工具，适合培养 Geek。不用单独购买学习本，插到自用的或者闲置的笔记本或者台式机电脑就可以直接启动使用，既可以关机后独立开机使用，也可以在运行的 Windows 下自动启动。</p>
                                        </div>
                                      
</div>
            