
---
title: 'FSR 2.1 发布，AMD 图像超采样技术'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8129'
author: 开源中国
comments: false
date: Sat, 10 Sep 2022 06:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8129'
---

<div>   
<div class="content">
                                                                                            <p>AMD FidelityFX Super Resolution 2 (FSR 2) 是一个开源的高质量解决方案，用于从低分辨率的输入产生高分辨率的帧。</p> 
<p>FSR 技术是一项允许游戏同时提高性能和视觉效果输出的技术。以往在电脑配置的限制下，游戏通常无法同时兼顾游戏性能和视觉效果，尤其是大型的 3A 游戏，玩家需要根据自己的偏好在两者之间相互权衡，而在 FSR 技术的加持下玩家可以两者兼得。</p> 
<p>近日 AMD 发布了 FSR 2.0 版本的第一个主要更新，FSR 2.1 包括对算法的某些部分的重大改变，使游戏能够进一步提高质量，并减少重影和闪光等伪影。</p> 
<h3>变化</h3> 
<ul> 
 <li>利用运动矢量散度来减少锁定像素，有助于缓解重影问题</li> 
 <li>遮蔽逻辑现在能够检测深度分离较小的区域中的遮蔽，有助于减轻重影并提高整体图像质量</li> 
 <li>一些以前的半精度算法现在是全精度的，提高了整体图像质量和时间稳定性</li> 
 <li>Reactive Mask 膨胀和数值范围改进，有助于减轻透明几何体上的重影</li> 
 <li>Composition 和 Transparency Mask 更新，以帮助减轻某些几何体上的重影</li> 
 <li>更新了动画纹理、火花粒子和烟雾粒子的示例</li> 
 <li>FSR 2.1 还包括许多小的错误修复，以及文档的修复和改进</li> 
 <li>应用端 FSR 2 API 没有变化，所以从 FSR 2.0 更新到 FSR 2.1 应该很简单</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FGPUOpen-Effects%2FFidelityFX-FSR2%2Freleases%2Ftag%2Fv2.1.0" target="_blank">https://github.com/GPUOpen-Effects/FidelityFX-FSR2/releases/tag/v2.1.0</a></p>
                                        </div>
                                      
</div>
            