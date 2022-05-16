
---
title: '中国移动 OneOS - V2.2.0 发布，新增 LoongArch 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5816'
author: 开源中国
comments: false
date: Mon, 16 May 2022 10:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5816'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>中国移动OneOS物联网操作系统V2.2.0版本已成功上线。新版本增加了对LoongArch</span></span></span><span><span><span>支持</span></span></span><span><span><span>等核心功能。</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>本次更新中支持的LoongArch，是龙芯中科研发的一套完全采用中国技术的指令集，该指令集融合了各国际主流指令系统的主要功能特性。此前龙芯中科与中移物联网联合推出了基于龙芯2K0500平台的国产嵌入式软件开发解决方案，此次OneOS-V2.2.0原生支持LoongArch指令集，将为打破国产软件生态发展受制于人的局面做出又一贡献。</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>除此之外，OneOS-V2.2.0版本在内核、驱动、组件方面还有许多的亮点之处。详细更新说明如下：</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>内核方面：</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>1、新增LoongArch支持</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>2、新增AC6编译器支持</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>3、新增ARMV5te（ARM9）架构支持</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>4、新增GCC编译器9.3版本支持</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>5、新增C++库适配</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>6、支持CPU使用率统计、内存内容监测、运行信息维测统计</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>驱动方面：</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>1</span></span></span><span><span><span>、新增驱动库适配AC6编译器</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>2</span></span></span><span><span><span>、新增CODESYS支持（相关开发板适配）</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>3</span></span></span><span><span><span>、新增USB驱动框架</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"> </p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>组件方面：</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>1、新增LWIP支持IPV6</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>2、新增FOTA解决方案(电信云模式、主从模式)</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>3、新增MOLINK蓝牙模组支持</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>4、新增蜂窝网络日志统计</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>5、新增电源管理能耗分析框架</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>6、新增COAP3支持</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>7、新增定位组件端侧RTK优化</span></span></span></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span><span><span><span>以上就是本次版本更新的介绍，OneOS-V2.2.0代码包已上线<a href="https://gitee.com/cmcc-oneos/OneOS">码云</a></span></span></span><span><span><span>，欢迎各位开发者前往下载使用。</span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            