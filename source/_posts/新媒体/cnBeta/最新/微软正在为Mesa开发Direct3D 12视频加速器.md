
---
title: '微软正在为Mesa开发Direct3D 12视频加速器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1122/659ccf405b17c50.jpg'
author: cnBeta
comments: false
date: Mon, 22 Nov 2021 12:49:55 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1122/659ccf405b17c50.jpg'
---

<div>   
作为微软围绕支持GUI应用程序与Windows Subsystem for
Linux（WSL2）以及在Windows上将Vulkan/OpenGL/OpenCL映射到Direct3D的持续工作的一部分，微软工程师现在正努力为Mesa添加Direct3D
12视频加速支持。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1122/659ccf405b17c50.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1122/659ccf405b17c50.jpg" title alt="cold12.jpg" referrerpolicy="no-referrer"></a></p><p>微软不仅在努力为他们的Gallium3D Direct3D 12驱动添加D3D12视频加速，而且还希望能够实现它，以便其他Mesa视频前端能够在这个D3D12视频加速代码路径上工作。理论上，这将允许Mesa的VA-API和VDPAU实现能够在这样的环境中运行D3D12视频硬件加速。</p><p>微软的D3D12开源视频驱动目前正在通过这个Gitlab分支进行工作：</p><p><a href="https://gitlab.freedesktop.org/sivileri/mesa/-/commits/user/sivileri/mesa_d3d12_video_driver_1" _src="https://gitlab.freedesktop.org/sivileri/mesa/-/commits/user/sivileri/mesa_d3d12_video_driver_1" target="_blank">https://gitlab.freedesktop.org/sivileri/mesa/-/commits/user/sivileri/mesa_d3d12_video_driver_1</a><br></p><p>Mesa Direct3D 12视频支持工作是由微软在邮件列表中提出的：</p><p><a href="https://lists.freedesktop.org/archives/mesa-dev/2021-November/225575.html" _src="https://lists.freedesktop.org/archives/mesa-dev/2021-November/225575.html" target="_blank">https://lists.freedesktop.org/archives/mesa-dev/2021-November/225575.html</a><br></p><p>因为围绕Wayland集成的一些开放性问题。这段代码仍在变化中，在为终端用户准备好之前还有更多的工作要做，但还是很有趣，者是微软对Mesa的又一次推动。</p>   
</div>
            