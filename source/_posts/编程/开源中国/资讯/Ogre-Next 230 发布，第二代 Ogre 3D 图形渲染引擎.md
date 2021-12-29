
---
title: 'Ogre-Next 2.3.0 发布，第二代 Ogre 3D 图形渲染引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7805'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7805'
---

<div>   
<div class="content">
                                                                                            <p>Ogre-Next 是开源 3D 图形渲染引擎 Ogre 的第二代，相对于 Ogre 来说，Ogre-Next 更适用于<strong>在屏幕上</strong>拥有<strong>大量对象或渲染预算紧张的项目，例如 VR。</strong></p> 
<p>目前 Ogre-Next <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ogre3d.org%2F2021%2F12%2F24%2Fogre-next-2-3-0-deadalus-released-and-merry-christmas" target="_blank">发布了 2.3.0 版本</a>，此版本主要改进了设备丢失（Device Lost）问题的处理、使用了先进的阴影映射技术、稳定的 Vulkan ...详细改动内容如下：</p> 
<h3><strong>改进对设备丢失问题的处理</strong></h3> 
<p>游戏程序的设备丢失被视为严重故障且非常罕见，通常是由于硬件或软件故障，或者在游戏过程中进行 Windows 更新。无论如何，在这种情况下，游戏体验都已经中断了。</p> 
<p>而对于非游戏的应用程序，出现设备丢失问题的主要原因是以下两个：</p> 
<ul> 
 <li>显卡驱动升级</li> 
 <li>从省电模式切换到性能模式，反之亦然（主要在笔记本电脑或其他移动设备上）</li> 
</ul> 
<p>现在，Eugene 会尽可能地从丢失的设备中恢复丢失前的内容。</p> 
<h3 style="margin-left:0px">将 importV1 切换为 createByImportingV1</h3> 
<p>2.2 及更早版本有一个名为 <code>Mesh::importV1</code> 的函数，它会通过用来自 v1 网格的数据来填充 v2 网格，从而有效地导入它。</p> 
<p>在 2.3 中用户应该使用 <code>MeshManager::createByImportingV1</code> 代替 <code>Mesh::importV1</code>。此功能会“记住”通过转换过程创建了哪些网格，允许设备丢失处理重复此导入过程并重新创建资源。</p> 
<p>另外，两个函数的功能没啥区别，参数也基本一样。</p> 
<h3>先进的阴影映射技术</h3> 
<p>引入了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fissues%2F17260" target="_blank">Normal Offset Bias</a> 技术，能够极大程度改善自我遮蔽和阴影失真（Shadow Acne）的问题，投射阴影的步骤也比原来的 Inverted-culling 方法好用得多。</p> 
<p>随着 Normal Offset Bias 取代 Inverted-culling 方法，旧的函数 <code>HlmsManager::setShadowMappingUseBackFaces()</code> 已经被删除，取而代之的是 <code>ShadowTextureDefinition::normalOffsetBias</code> 和 <code>ShadowTextureDefinition::constantBiasScale</code> 。</p> 
<h3>稳定的 Vulkan</h3> 
<p>在 Ogre 2.3.0 中，Vulkan 已经进入稳定阶段。但要注意的是，在和 Qt 整合的时候存在一些问题，目前尚未深入研究。</p> 
<p>Ogre-Next 2.3.0 是一个历时一年的大型版本，还有更多详细更新项，在此不一一列举，感兴趣可移步<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOGRECave%2Fogre-next%2Freleases%2Ftag%2Fv2.3.0" target="_blank">更新公告</a>细阅。</p>
                                        </div>
                                      
</div>
            