
---
title: 'OGRE 13 开源游戏引擎发布，将采用语义版本控制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0816/070226_68qN_4937141.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 07:03:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0816/070226_68qN_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>OGRE（Object-Oriented Graphics Rendering Engine，面向对象图形渲染引擎） 又叫做 OGRE 3D。OGRE 是面向场景、实时的三维图像引擎。OGRE 是跨平台软件，支持 Windows、macOS、Linux、iOS、Android 等平台。底层也有 DirectX 及 OpenGL 等等多种不同的实现。</p> 
<p>OGRE 13 正式发布，更新内容如：</p> 
<h2>变化：</h2> 
<p>OGRE 13 版的重点是为未来的发展准备代码库和修复架构问题。一些过时的部分被删除，还有一些 API 被调整为更通用。</p> 
<p>本次更新的重点内容包括：</p> 
<h3>语义版本管理</h3> 
<p>OGRE 现在使用像 MAJOR.MINOR.PATCH （例如：13.1.1）一样使用语义版本控制，其中向后不兼容的 API 更改需要增加 MAJOR 的数字。此前 Ogre 并不遵循这一规则 —— 否则 Ogre 1.2 的升级版会变成 Ogre 2.0。</p> 
<p>然而，现在 OGRE/OGRENext 的分裂已经发生，我们放弃 1.x 的前缀。语义版本方案是现在大多数用户所期望的。</p> 
<h3>改进的 API 稳定性</h3> 
<p>此前，OGRE 只使用公共和受保护的可见性。虽然这使得随意定制 OGRE 类变得很容易，但当涉及到承诺一个稳定的 API 时，它就不是那么好了。</p> 
<p>以前，你可以使用一个继承的类成员，而我们后来需要改变它，导致你的代码被破坏。虽然我们可以将所有受保护的成员排除在我们的 API 保证之外，但如果编译器能够检查你是否只使用稳定的 API，那就更好了。</p> 
<p>同时，我们还将 API 的稳定性扩展到着色器代码。由于我们在那里没有 public/private，我们使用 @public-api 注释来注释 API。值得注意的是，这也包括 OGREUninifiedShader.h。</p> 
<h3>RTSS 的补充</h3> 
<p>可重复使用的法线图阶段，现在可以与 GBuffer 渲染相结合。</p> 
<p>WBOIT：加权、混合、与次序无关的透明阶段，将相应的算法添加到 OGRE。</p> 
<h3>改进的字形放置</h3> 
<p>以前使用斜体字体可能会导致字形截断，因为 OGRE 没有考虑字形重叠。参见下图中的“j”和“T”：</p> 
<p><img alt height="525" src="https://static.oschina.net/uploads/space/2021/0816/070226_68qN_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="525" src="https://static.oschina.net/uploads/space/2021/0816/070238_SmE2_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>其他：</h3> 
<ul> 
 <li>零外部依赖</li> 
 <li>支持 Direct3D 11 上的全恒定缓冲区</li> 
 <li>GLSLang 插件</li> 
 <li>DotScene 导出支持</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ogre3d.org%2F" target="_blank">https://www.ogre3d.org/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            