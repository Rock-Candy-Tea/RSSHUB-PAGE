
---
title: 'Khronos的ANARI分析性渲染界面获得AMD Radeon ProRender支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0510/3764e41041bda66.webp'
author: cnBeta
comments: false
date: Tue, 10 May 2022 07:58:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0510/3764e41041bda66.webp'
---

<div>   
<strong>Khronos 集团的 ANARI 分析性渲染界面已获得 AMD Radeon ProRender 的支持。</strong>Khronos ANARI 界面用于
3D 数据的可视化。Radeon ProRender
是一款基于物理特性的强大渲染引擎，助力创意专业人士制作出令人惊艳、达到照片级真实感的图像。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0510/3764e41041bda66.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0510/8fd805d4f2f88bd.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Khronos ANARI分析性渲染界面被添加到利用<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon ProRender的支持应用列表中。ANARI 限制了几个寻找功能丰富的数据可视化应用的商户的不同 API 的分散性。</p><p style="text-align: left;">2021 年，Khronos 集团发布了 ANARI 1.0 临时规范初稿，以创建一个专注于定制 3D 数据可视化的行业标准。该组织打算让分析性渲染界面成为 AMD Radeon ProRender 使用的黄金规则规范，并被几个 CPU 和 GPU 库所利用。</p><p style="text-align: left;">启用的消息今天上午在 AMD 的 <a href="https://gpuopen.com/radeon-prorender-now-supports-khronos-anari/" target="_blank">GPUOpen</a> 网站上公布，简要解释了 Kronos ANARI 1.0 支持的新整合。该应用在 Apache 2.0 许可下被认为是开源的，可以从 <a href="https://github.com/GPUOpen-LibrariesAndSDKs/RadeonProRenderANARI" target="_blank">GitHub</a> 下载。</p><p style="text-align: left;">实施细节如下：</p><blockquote style="text-align: left;"><p style="text-align: left;"><strong>相机</strong></p><p style="text-align: left;">● 支持的类型：透视和正视</p><p style="text-align: left;">● transform 参数覆盖了位置、方向和向上参数</p><p style="text-align: left;">● 现在不支持imageRegion参数</p><p style="text-align: left;">● 只有透视相机支持focusDistance和apertureRadius参数。</p><p style="text-align: left;">● 两种相机都有一个额外的参数sensorHeight。传感器的宽度将使用长宽参数计算。默认的传感器高度是24毫米。</p><p style="text-align: left;">● 正视相机有一个额外的参数 orthoHeight。它决定了正射影像机的投影将覆盖的区域。宽度将使用长宽参数计算。默认值为1</p><p style="text-align: left;"><strong>几何图形：</strong></p><p style="text-align: left;">● 现在不支持曲线几何类型</p><p style="text-align: left;">● 不支持常规参数（primitive.color, primitive.attribute, primitive.id）。</p><p style="text-align: left;">● vertex.color 只能接受float32类型（FLOAT32, FLOAT32_VEC2, FLOAT32_VEC3, FLOAT32_VEC4)</p><p style="text-align: left;">● vertex.normal 只能接受 FLOAT32 值</p><p style="text-align: left;">● primitive.index只能接受uint32值和向量。</p><p style="text-align: left;"><strong>体积</strong></p><p style="text-align: left;">● 空间领域的数据只能是float32格式（FLOAT32的ARRAY3D）。</p><p style="text-align: left;">● color只能接受float32类型（FLOAT32, FLOAT32_VEC2, FLOAT32_VEC3, FLOAT32_VEC4)</p><p style="text-align: left;">● 不支持color.position和opacity.position参数。</p><p style="text-align: left;"><strong>尚未实现的功能</strong></p><p style="text-align: left;">●  object introspection</p><p style="text-align: left;">● 摄像机的立体模式</p><p style="text-align: left;">● 深度帧缓冲器</p><p style="text-align: left;">● 曲线几何</p><p style="text-align: left;">● khr_auxiliary_buffers</p><p style="text-align: left;">● anari_khr_transformation_motion_blur</p></blockquote>   
</div>
            