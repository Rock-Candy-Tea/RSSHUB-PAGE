
---
title: 'Linux 5.14 即将为英特尔独立显卡启用图形TTM内存管理初始位'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0613/505fd7b75a11ad1.jpg'
author: cnBeta
comments: false
date: Sun, 13 Jun 2021 11:27:23 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0613/505fd7b75a11ad1.jpg'
---

<div>   
十年前，只有集成显卡的开发任务需要完成的英特尔的开源Linux图形驱动工程师宣布不支持TTM，而是设计了图形执行管理器（GEM）来满足内核图形内存管理的需要，但现在英特尔开始推出独立显卡和专用显存存，这时候TTM内存管理的需求就显得迫切了起来。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0613/505fd7b75a11ad1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0613/505fd7b75a11ad1.jpg" title alt="opt-5e39355956e78intel-dg1-gpu-discrete-graphics-card-powered-by-xe-graphics-architecture-3.jpg" referrerpolicy="no-referrer"></a></p><p>在Linux 5.14中，当独立显卡拥有本地内存时，英特尔驱动程序将在那里使用TTM的初始位。</p><p>英特尔上个月就宣布正在为他们即将推出的独立显卡产品的独立显存存管理进行TTM集成，但是英特尔内核图形驱动程序现有的GEM内存管理代码仍然保留，并且没有改变现有硬件支持的代码路径。</p><p>用于处理独立显卡 "dGFX"上的本地内存 "LMEM"的TTM设备和内存管理器的初始启用是在周四作为drm-intel-gt-next的一部分送入Linux 5.14合并之前的DRM-Next的。同样，现有的英特尔图形支持并没有改变，但最终目的是为Xe独立显卡硬件产品提供支持。</p><p>本次拉动请求还对英特尔的GuC提交后端进行了改进，以准备在较新的平台上启用。该请求现在开始默认为Rocket Lake以及Tiger Lake之后的第12代平台启用HuC加载，即Alder Lake。</p><p>除了这些与内存管理有关的工作外，还有许多其他英特尔图形驱动的改进将在Linux 5.14中进行。</p><p>Linux 5.14合并周期将在本月底启动，而稳定版将在今年夏天晚些时候发布，并赶上秋季的Linux发行时间节点。</p><p><strong>了解更多：</strong></p><p><a href="https://lists.freedesktop.org/archives/intel-gfx/2021-June/268871.html" _src="https://lists.freedesktop.org/archives/intel-gfx/2021-June/268871.html" target="_blank">https://lists.freedesktop.org/archives/intel-gfx/2021-June/268871.html</a><br></p>   
</div>
            