
---
title: '​openKylin 0.7 体验版本发布，支持 PC、平板双模式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.openkylin.top/upload/202207/1658483497707290.png'
author: 开源中国
comments: false
date: Sat, 23 Jul 2022 10:11:00 GMT
thumbnail: 'https://www.openkylin.top/upload/202207/1658483497707290.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#3d3d3d; text-align:justify">7月22日，桌面操作系统根社区openKylin（开放麒麟）首个体验版——openKylin 0.7发布。</p> 
<p style="color:#3d3d3d; text-align:justify">openKylin 0.7基于Linux 5.15内核和其他开源组件进行构建，向“每一行代码都自主创新”的目标迈进。同时，此版本默认搭载UKUI3.1桌面环境，自带“和印”、“寻光”两套系统主题，提供wayland支持和平板模式支持，并集成了一系列稳定版本的基础库、图形开发库和SDK，为用户带来良好使用体验。</p> 
<p style="color:#3d3d3d; text-align:center"> 
 <video controls height poster="https://www.openkylin.top/upload/202207/1658466412693863.png" src="https://www.openkylin.top/public/video/openkylin07.mp4" style="max-width:100%" width>
   
 </video> </p> 
<p style="color:#3d3d3d; text-align:center"><span style="color:#0070c0"><strong>openKylin 0.7版本特性大盘点</strong></span></p> 
<p style="color:#3d3d3d; text-align:justify"><strong>1、内核</strong></p> 
<p style="color:#3d3d3d; text-align:justify">openKylin 0.7内核以Linux 5.15内核为基础，在Linux 5.15内核原有的特性之上，进行了以下优化：</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="text-align:justify">进一步优化对Intel第 12 代 CPU 的支持；</p> </li> 
 <li> <p style="text-align:justify">增加对Intel近一两年推出的集显的支持；</p> </li> 
 <li> <p style="text-align:justify">改进RISC-V支持；</p> </li> 
 <li> <p style="text-align:justify">修复多款整机的兼容性问题。</p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><strong>2、基础组件库</strong></p> 
<ul style="list-style-type:disc"> 
 <li> <p style="text-align:justify">集成了一系列稳定版本的基础库，如glibc 2.31, GCC 9.3, Python 3.8.2 等；</p> </li> 
 <li> <p style="text-align:justify">集成了图形开发库Qt 5.15 LTS版本，支持3D图形抽象API、Qt Quick 3D、最新版 Qt Design Studio 1.5；同时，改进了qmllint工具，以及对客户端/自定义窗口装饰提供更好的支持；</p> </li> 
 <li> <p style="text-align:justify">集成了由麒麟软件研发的SDK，将应用层、基础层相关接口和系统层接口进行封装，为在openKylin桌面操作系统上进行应用开发提供多种工具与接口。同时，同一开发套件也可兼容多种系统架构，为开发者提供更多便利，降低开发成本，使开发更聚焦于实际业务，提升开发的质量与效率。</p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><strong>3、桌面环境</strong></p> 
<p style="color:#3d3d3d; text-align:justify">openKylin 0.7默认搭载最新UKUI 3.1桌面环境，主要特性如下：</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="text-align:justify">默认开启wayland支持，提供更流畅的渲染以及更好的HiDPI支持，充分利用EGL硬件加速，降低功耗，提升效率；</p> </li> 
 <li> <p style="text-align:justify">默认提供平板模式支持，通过状态管理服务、多端融合的窗口管理、手势管理、应用生命周期管理，从底层服务到上层应用初步形成一套PC、平板多模式融合的解决方案，大大提升了用户在触摸屏以及二合一平板等产品上的操作体验。</p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:justify"><strong>4、关键应用</strong></p> 
<p style="color:#3d3d3d; text-align:justify">openKylin 0.7 系统具有丰富的关键应用，从功能性和易用性方面提升用户体验,例如：</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="text-align:justify">支持多种格式的图片预览和打印；</p> </li> 
 <li> <p style="text-align:justify">支持音频裁剪后自定义输出，多种格式视频播放；</p> </li> 
 <li> <p style="text-align:justify">支持基于openKylin查看天气、日历，设置闹钟，制作启动盘等多种便捷操作；</p> </li> 
 <li> <p style="text-align:justify">支持触控手势；</p> </li> 
 <li> <p style="text-align:justify">支持多网卡切换；</p> </li> 
 <li> <p style="text-align:justify">支持 5G WI-FI，访问速度更快。</p> </li> 
</ul> 
<p style="color:#3d3d3d; text-align:center"><span style="color:#0070c0"><strong>每年发布一个操作系统版本，并不定期推送更新</strong></span></p> 
<p style="color:#3d3d3d; text-align:justify">openKylin自6月成立以来，便积极推进社区建设，目前已有46个企业加入社区，包括操作系统厂商、CPU厂商、GPU厂商、整机厂商、以及软件厂商等，并成立了14个SIG组。</p> 
<p style="color:#3d3d3d; text-align:center"><img alt="openKylin（开放麒麟）" src="https://www.openkylin.top/upload/202207/1658483497707290.png" referrerpolicy="no-referrer"></p> 
<p style="color:#3d3d3d; text-align:justify">目前，openKylin已构建开源基础设施全生命周期自动化平台，成员只需一键提交，可自动化执行代码检测、编译、构建全流程，极大的提升社区参与者的编码效率。</p> 
<p style="color:#3d3d3d; text-align:justify">同时，openKylin打造了一套从代码到镜像的一体化平台，从码云到OKBS（编译平台），再到OKIF（镜像构建平台），无缝支撑了从上游代码到生成镜像的整体流程，实现代码自主选型、软件包自主编译、镜像自主生成的全栈式需求。</p> 
<p style="color:#3d3d3d; text-align:justify">在版本发布周期规划上，openKylin社区计划每年发布一个操作系统版本，并不定期推送更新，以旺盛的生命力向上生长。</p> 
<p style="color:#3d3d3d; text-align:center"><span style="color:#0070c0"><strong>诚邀您参与openKylin社区共建</strong></span></p> 
<p style="color:#3d3d3d; text-align:justify">此外，<strong>openKylin社区将邀请广大企业和开发者参与社区，携手共建，基于openKylin 0.7版本，协助完成打包、适配和测试等工作，在openKylin操作系统建设历程中留下自己的足迹。</strong></p> 
<p style="color:#3d3d3d; text-align:justify">秉承着建设数字基础设施、“坚底强链”的初心，怀揣着推动中国桌面操作系统发展的使命，openKylin将携手社区力量和行业伙伴，共同打造具备软硬件协同内核设计、多生态应用兼容环境、跨平台编程框架和统一运行支持环境的新一代操作系统。</p> 
<p style="color:#3d3d3d; text-align:justify">openKylin官方下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenkylin.top%2Fdownloads%2Findex-cn.html" target="_blank">https://openkylin.top/downloads/index-cn.html</a></p> 
<p style="color:#3d3d3d; text-align:justify">openKylin已知问题列表：<a href="https://gitee.com/openkylin/qa/blob/master/%E5%B7%B2%E7%9F%A5%E9%97%AE%E9%A2%98" target="_blank">https://gitee.com/openkylin/qa/blob/master/已知问题</a></p>
                                        </div>
                                      
</div>
            