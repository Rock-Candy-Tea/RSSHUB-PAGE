
---
title: 'OpenHarmony 2.2 Beta2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cdd943ec052aa0a1ea9286c7dcb37ae1293.png'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 07:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cdd943ec052aa0a1ea9286c7dcb37ae1293.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>8 月 4 日，开放原子开源基金会 (OpenAtom Foundation) 正式发布 OpenAtom OpenHarmony（以下简称“OpenHarmony”）2.2 Beta2 版本。</p> 
<p><strong>全球开发者可通过 Gitee 和镜像站点下载完整代码：<a href="https://gitee.com/openharmony" target="_blank">https://gitee.com/openharmony</a></strong></p> 
<p>据介绍，6 月 1 日，开放原子开源基金会发布了 <a href="https://www.oschina.net/news/144144/openharmony-2-0-canary-released" target="_blank">OpenHarmony 2.0 Canary </a>版本，自主研发，不兼容安卓；8 月 4 日发布的 OpenHarmony 2.2 Beta2 版本，具备了典型的分布式能力和媒体类产品开发能力，也包含了部分支持功能机开发目标的 OS 能力。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cdd943ec052aa0a1ea9286c7dcb37ae1293.png" referrerpolicy="no-referrer"></p> 
<p>▲ 版本路标</p> 
<p><a href="https://gitee.com/openharmony/release-management/blob/master/OpenHarmony-RoadMap.md" target="_blank">详细版本路标点此查看</a><strong>。</strong></p> 
<p><a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/release-notes/OpenHarmony-v2.2-beta2.md" target="_blank">根据 release note 的描述</a>，当前版本在 OpenHarmony 2.0 Canary 的基础上，针对轻量系统、小型系统和标准系统都有增加新的特性。</p> 
<p>标准系统新增特性功能如下：</p> 
<ul> 
 <li>新增分布式远程拉起能力端到端的构建。</li> 
 <li>新增系统基础应用的拖拽能力和新增若干 Sample 应用。</li> 
 <li>新增媒体三大服务能力，提供更好的媒体系统功能。</li> 
</ul> 
<p>轻量和小型系统新增特性功能如下：</p> 
<ul> 
 <li>新增轻量级 Linux 版本构建能力。</li> 
 <li>新增轻量级内核能力增强，包括文件系统增强、内核调试工具增强支持、内核模块支持可配置、三方芯片适配支持、支持 ARM9 架构等。</li> 
 <li>轻量级图形能力增强支持，包括支持多语言字体对齐、支持显示控件轮廓、支持点阵字体、供统一多后端框架支持多芯片平台等。</li> 
 <li>DFX 能力增强支持，包括 HiLog 功能增强、HiEvent 功能增强，提供轻量级系统信息 dump 工具、提供重启维侧框架等。</li> 
 <li>AI 能力增强支持，包括新增 Linux 内核适配支持、AI 引擎支持基于共享内存的数据传输。</li> 
</ul> 
<p>OpenHarmony 2.2 Beta2 关键特性：</p> 
<p><strong>1、支持分布式框架能力</strong></p> 
<ul> 
 <li>分布式软总线：支持基于 WIFI 的主动发现和设备间自组网，业务方通过使用分布式软总线实现设备间高速通信，不用关心通信细节。</li> 
 <li>分布式数据管理：支持富设备之间的数据同步，和加密型数据库。</li> 
 <li>分布式任务调度：见分布式跨设备 Ability 流转。</li> 
</ul> 
<p><strong>2、支持分布式跨设备</strong><strong> </strong><strong>Ability</strong><strong> </strong><strong>流转</strong></p> 
<p>OpenHarmony 支持应用以 Ability 为单位进行部署，应用“跨设备流转”的基础粒度也是 Ability。具备打破设备界限，多设备联动能力，使应用程序可分可合、可流转。基于 OpenHarmony 的分布式导航、多设备协同健身等设备的开发所需具备的核心要素已经就绪。</p> 
<p><strong>3、LiteOS-A</strong><strong> </strong><strong>高效实时调度算法</strong></p> 
<p>OpenHarmony Liteos-A 调度精确动态化：高优先级优先+同优先级时间片轮转的调度算法，结合优先级多队列、tick 精确动态化、时间片动态计算等技术，实现系统中线程的高效实时调度。</p> 
<p><strong>4、轻量系统图形硬件加速渲染</strong></p> 
<ul> 
 <li>提供基础的 UI 组件和独立的图形引擎，适用于基于 ARM Cortex-M 的 MCU 和低内存资源的 ARM Cortex-A 的芯片。</li> 
 <li>在 ARM Cortex-M 120MHz 级别的 CPU 下，纯软绘制可达 30FPS，对接硬件能力可达 60FPS。</li> 
 <li>ARM Cortex-M 下，UI 框架支持按需裁剪，可在 ROM<150KB 且 RAM<30KB 硬件条件下运行。</li> 
 <li>同时支持 OpenHarmony 自研 2D 绘制和扩展兼容其他三方绘制库，支持 34 个控件。</li> 
</ul> 
<hr> 
<p>OpenHarmony 是由开放原子开源基金会孵化及运营的开源项目，由开放原子开源基金会的 OpenHarmony 项目群工作委员会负责运作，遵循 Apache 2.0 等开源协议。由华为捐赠智能终端操作系统基础能力相关代码，博泰、华为、京东、润和、亿咖通、中科院软件所、中软国际等七家单位（按各单位简称首字母排序）及全球开发者共建的开源分布式操作系统。具备面向全场景、分布式、组件化等特点，是一款面向未来的根操作系统。</p>
                                        </div>
                                      
</div>
            