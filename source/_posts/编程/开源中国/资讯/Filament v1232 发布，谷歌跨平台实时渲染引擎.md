
---
title: 'Filament v1.23.2 发布，谷歌跨平台实时渲染引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8322'
author: 开源中国
comments: false
date: Fri, 17 Jun 2022 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8322'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px"><span style="color:#333333">Filament 是 Google 开发的轻量级跨平台实时渲染引擎，支持 PBR 材质，可用于开发游戏渲染引擎或构建音视频编辑工程。当开发者需要处理 3D 渲染效果，又不想引入庞大的游戏引擎时，可以考虑使用它（尤其是 Android 平台），因为它特别针对 Android 平台进行了优化。</span></p> 
<p style="margin-left:0px">目前，<span style="color:#333333">Filament 发布了 1.23.2 版本，带来如下变更：</span></p> 
<ul> 
 <li>gltfio：修复未打包访问器的变形问题。</li> 
 <li>gltfio：Ubershaders 被打包到灵活的档案中。</li> 
 <li>gltfio：去除维护不佳的 lite 模块。</li> 
 <li>引擎：在渲染阴影贴图时禁用用户剪刀。</li> 
 <li>引擎：将相同的后端 <code>RenderPrimitives</code> 合并在一起。</li> 
 <li>引擎：通过保留 128 个缓存条目来提高 <code>ResourceAllocator</code> 性能。</li> 
 <li>utils：删除 <code>std::hash<T></code> 类型的 <code>libutils</code> 定义，改为显式 <code>T::Hasher</code> 使用 。[<strong>包含 API变更</strong>]</li> 
 <li>后端：修复 WGL 上下文属性。</li> 
 <li>Metal：修复在 Ubershader 模式下使用 gltfio 时潜在的无效着色器。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Ffilament%2Freleases%2Ftag%2Fv1.23.2" target="_blank">https://github.com/google/filament/releases/tag/v1.23.2</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            