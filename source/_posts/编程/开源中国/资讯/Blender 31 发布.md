
---
title: 'Blender 3.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0310/071211_tFk3_4937141.png'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 07:12:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0310/071211_tFk3_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Blender 是一个免费和开源的 3D 计算机图形软件工具集，用于创建动画电影、视觉效果、艺术、3D 打印模型、交互式 3D 应用、VR 和计算机游戏。</p> 
<p>近日，Blender 3.1 正式发布，该版本的更新内容如下：</p> 
<h3>Apple Metal</h3> 
<p>Blender 3.1 现在有一个 Metal GPU 后端，由苹果提供。目前支持 Metal GPU 渲染的设备有：</p> 
<ul> 
 <li>运行 macOS 12.2 或更新版本的苹果 M1 设备</li> 
 <li>运行 macOS 12.3 或更新版本，使用 AMD 显卡的苹果电脑</li> 
</ul> 
<p>该实现还处于早期状态。性能优化，以及对英特尔 GPU 的支持正在开发中。</p> 
<p><img alt height="345" src="https://static.oschina.net/uploads/space/2022/0310/071211_tFk3_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>使用 M1 处理器的 MacBook Air 的每个样本的渲染时间</p> 
<h3>光线追踪精度</h3> 
<p>渲染小的、大的和远的物体所产生的许多伪影已经被消除了。渲染重叠几何体时仍然可能存在伪影，在某些情况下比以前更严重。 这种重叠的几何图形应该被移除，或者在它们之间添加一个小的距离。</p> 
<h3>点云</h3> 
<p>现在支持将点云对象直接渲染为球体，与在每个点上实例化一个对象相比，这在内存使用和渲染时间上要高效得多。</p> 
<p>点云可以用几何节点生成或从其他软件导入。新的点信息着色器节点可以用来获得点的中心位置和半径，以及点的随机值。</p> 
<h3>其他</h3> 
<ul> 
 <li>相机：新的 Fisheye Lens Polynomial 模型</li> 
 <li>Map 范围节点现在可以直接作用于向量</li> 
 <li>让 Embree compact BVH 成为可选项。禁用它可以改善 CPU 渲染时间，但代价是更高的内存使用率</li> 
 <li>Python API 中的去噪算子现在支持 OptiX 的时间去噪。这需要启用去噪数据和矢量通道。目前该功能没有用户界面，只有一个 Python API</li> 
 <li>Python API 中的合并操作现在支持合并使用自适应采样的 OpenEXR 渲染器</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.blender.org%2Fdownload%2Freleases%2F3-1%2F" target="_blank">https://www.blender.org/download/releases/3-1/</a></p>
                                        </div>
                                      
</div>
            