
---
title: '图形 API 规范 Vulkan 1.3 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8d7d37865220fe7e2aab105432e2d2a3be0.png'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 07:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8d7d37865220fe7e2aab105432e2d2a3be0.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvideocardz.com%2Fpress-release%2Fkhronos-announces-vulkan-1-3-graphics-api-specificaitons" target="_blank">Vulkan 1.3 规范已正式发布</a>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8d7d37865220fe7e2aab105432e2d2a3be0.png" referrerpolicy="no-referrer"></p> 
<p>Khronos Group 是一个由创建高级互操作性标准的行业领先公司组成的开放联盟，昨日<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvideocardz.com%2Fpress-release%2Fkhronos-announces-vulkan-1-3-graphics-api-specificaitons" target="_blank">宣布</a>了跨平台 3D 图形 API 及其生态系统 Vulkan 的最新更新：</p> 
<ul> 
 <li>Vulkan 1.3 规范已正式发布，纳入并强制执行了经过验证、由开发者要求的扩展集，使功能在所有支持的平台上一致可用</li> 
 <li>Vulkan 工作组正在制定一个公开路线图 (Public Roadmap)，为支持更高级的 Vulkan 功能提供计划和指导。针对中高端硬件的 Vulkan Roadmap 2022 定义了 Vulkan 1.3 以外的功能，这些功能将于今年开始提供</li> 
 <li>2022 年 2 月的 Vulkan 1.3 SDK 将引入 Vulkan 配置文件和工具，以便精确指定、管理和使用 API 功能集。配置文件将用于传达路线图、市场、平台以及硬件和软件开发人员的功能要求</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-45343a45040e9f220ca32259b6759af076b.png" referrerpolicy="no-referrer"></p> 
<p><strong>Vulkan 1.3 和 Vulkan 路线图 (Vulkan Roadmap 2022)</strong></p> 
<p><span style="background-color:#ffffff; color:#444444">Vulkan 1.3 将开发者社区要求的一些精心挑选的扩展整合到规范的新核心版本中，其中包括动态渲染、额外的动态状态、经过改进的 </span>synchronization API <span style="background-color:#ffffff; color:#444444">以及一系列其他功能（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.khronos.org%2Fblog%2Fvulkan-1.3-and-roadmap-2022" target="_blank">详情查看 Vulkan 1.3 and Roadmap 2022</a>）。更<span style="background-color:#ffffff; color:#444444">重要的是，与以前的版本不同，Vulkan 1.3 中添加的</span><strong style="color:#444444">任何功能都不是可选的</strong><span style="background-color:#ffffff; color:#444444">，从而确保它们在这个新 API 版本的所有实现中具有一致的可用性。</span><br> <br> <span style="background-color:#ffffff; color:#444444">与该规范的先前版本一样，Vulkan 1.3 仍希望为 </span>OpenGL ES 3.1-class 级别的<span style="background-color:#ffffff; color:#444444">硬件提供加速，使核心 API 能够在广泛的设备和市场中得到支持。</span>许多 Vulkan 设备通过可选扩展支持核心规格之外的功能，各个硬件供应商可以选择支持这些扩展，也可以不支持这些扩展。Vulkan 路线图旨在巩固对选定扩展的支持，以在关键市场中提供通用的功能基准。</p> 
<p>Vulkan Roadmap 2022 是一个标志性里程碑，<span style="background-color:#ffffff; color:#444444">所有积极开发用于智能手机、平板电脑、笔记本电脑、游戏机和台式机平台的中高端设备的 Vulkan 工作组硬件供应商都致力于支持这一里程碑，</span>从 2022 年推出的几款产品开始，这一里程碑需要支持 Vulkan 1.3 以及加上工作组认为对目标市场至关重要的一些扩展，<span style="background-color:#ffffff; color:#444444">包括描述符索引、片段着色器存储和原子、片段着色器中的子组支持、独立混合、样本着色、各向异性过滤、YCbCr 采样以及缓冲区资源的标量块布局。</span>Vulkan Roadmap 2022 <span style="background-color:#ffffff; color:#444444">还提高了许多硬件限制的最小值，包括最大图像和图像阵列尺寸、最大子组大小以及对每个着色器阶段可以访问的资源数的各种限制。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6904eef58a345acc83f60b25dabf30d5914.png" referrerpolicy="no-referrer"></p> 
<p><strong>Vulkan 配置文件 (Vulkan Profiles)</strong></p> 
<p><span style="background-color:#ffffff; color:#444444">新的 Vulkan 配置文件机制可实现 API 功能集的精确规范和管理。每个配置文件都指定了 Vulkan 的核心版本以及一组必需的扩展，并具有支持的限制、功能和格式。配置文件提供了一种在 Vulkan 生态系统中的参与者之间精确传达功能要求和设备功能的方法，以简化便携式应用程序的开发和部署。</span></p> 
<p><span style="background-color:#ffffff; color:#444444">Google 开发并发布了 Android Baseline 2021 Profile，用于宣传 Vulkan 1.0 以外的一系列功能，这些功能受 Android 生态系统中绝大多数活动设备的支持，包括不受支持以及不定期接收驱动程序更新的设备。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-741b4a13334be7c52173de1da103b8e1e11.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#444444">Vulkan Roadmap 2022 配置文件将对 Vulkan 路线图的第一个里程碑进行编码，该里程碑目前被记录在 Vulkan 1.3 规范中，将于 2 月中旬随 Vulkan SDK 一起发布。</span></p> 
<p><span style="background-color:#ffffff; color:#444444">Khronos 工具将使开发者能够生成自己的特定于应用程序的功能配置文件，轻松确定设备是否支持给定的配置文件，并在应用程序启动时启用配置文件中的功能/扩展。该工具的测试版将于 2 月中旬作为 Vulkan 1.3 SDK 的一部分发布，并将包括用于配置文件定义的机器可读文件格式，定义迄今为止发布的配置文件的文件、</span>header-only 库<span style="background-color:#ffffff; color:#444444">以及通过新的 VK_KHRONOS_LAYER_profiles 层的配置文件模拟支持。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvideocardz.com%2Fpress-release%2Fkhronos-announces-vulkan-1-3-graphics-api-specificaitons" target="_blank">详细更新说明查看发布公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            