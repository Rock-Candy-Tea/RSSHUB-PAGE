
---
title: 'Bevy 0.8 发布，Rust 构建的游戏引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4683'
author: 开源中国
comments: false
date: Mon, 01 Aug 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4683'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Bevy 是一个用 Rust 构建的数据驱动游戏引擎，Bevy 永远免费和开源，开发者可以查看 Bevy Assets，这是社区开发的插件、游戏和学习资源的集合。</p> 
<p>经过 130 位贡献者共 461 个拉取请求，时隔 3 个月，Bevy 0.8 版本正式发布。这个版本增加了大量的新功能、错误修复和调整，以下是其中的一些亮点：</p> 
<ul> 
 <li>新的材料系统：由于有了新的材质特性和 AsBindGroup 衍生功能，自定义着色器现在更容易定义。</li> 
 <li>摄像机驱动的渲染：每个摄像机现在都可以配置它所渲染的内容以及它的渲染方式。只需几行代码就可以轻松地将相机渲染分层，进行分屏，或渲染到纹理。</li> 
 <li>内置着色器模块化：许多内置的着色器类型和功能现在都可以导入。值得注意的是，自定义着色器现在可以导入 PBR 着色器逻辑。</li> 
 <li>聚光灯：一种新的灯光类型，可以从一个固定的点以圆锥体的形式发射光线。</li> 
 <li>可见性继承：隐藏一个实体现在也会隐藏它在层次结构中的所有子代</li> 
 <li>升级到 wgpu 0.13：使用新的 WGSL 着色器语法</li> 
 <li>ECS 内部重构：对 Bevy ECS 内部进行了全面的修改，使其更简单、更安全、更容易维护</li> 
 <li>反射的改进：支持更多类型的反射</li> 
 <li>层次结构命令：层次结构的更新现在使用 "事务性命令"，以确保层次结构在任何时候都保持一致</li> 
 <li>Bevy UI 现在使用 Taffy：已经换成了（并帮助维护）现已废弃的 Stretch UI 布局的合作分支</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbevyengine.org%2Fnews%2Fbevy-0-8%2F" target="_blank">https://bevyengine.org/news/bevy-0-8/</a></p>
                                        </div>
                                      
</div>
            