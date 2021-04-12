
---
title: '2D+1D _ vivo官网Web 3D应用开发与实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59429d3dfcaf4162aacfcbc285e560b6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 18:53:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59429d3dfcaf4162aacfcbc285e560b6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、 前言</h2>
<h3 data-id="heading-1">1.1 前端工程师，不写网页，还能做什么？</h3>
<p>在近20年的前端发展史中，前端经历了铁器时代（小前端），信息时代（大前端）以至现在的全能前端时代。经历了几个时代的沉淀之后，前端领域开始更加细分。</p>
<p>目前业界普遍认为前端细分领域的垂直方向有：助力于前后端分离和工程完善的NodeJS，关注用户界面展示的小前台，提供一站式解决方案的中后台，丰富数据展示能力的数据可视化(2D、3D)，以及面向未来的用户富交互体验的互动内容--AR、VR、3D等...</p>
<p>随着前端领域细分，前端工程师已不只是简单的负责堆砌网页、实现一些的交互，更可以在可视化领域实现一些很炫酷的效果。下图是vivo官网在3D数据可视化方面的实战展示。<a href="https://www.vivo.com.cn/vivo/3D/x50proplus" target="_blank" rel="nofollow noopener noreferrer">在线体验地址</a></p>
<p><img alt="vivo官网3D数据可视化实战图例" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59429d3dfcaf4162aacfcbc285e560b6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>数据可视化：</strong> 顾名思义，就是将数据以可视化图形图表等方式呈现给用户，使数据更加直观，客观，说服力更强。上图例就是利用渲染引擎对模型数据进行解析、渲染，最终呈现到移动设备。因其展现出的图像更加立体更具可交互性，属于3D数据可视化范畴。</p>
<p>今天我们就一起来了解一下前端的一个细化分支--3D数据可视化。本篇文章主要分为：</p>
<ul>
<li>
<p>前言</p>
</li>
<li>
<p>2D数据可视化</p>
</li>
<li>
<p>3D(2D+1D)数据可视化</p>
</li>
<li>
<p>vivo官网3D应用实战</p>
</li>
<li>
<p>总结</p>
</li>
</ul>
<p>希望通过五个章节的介绍和探讨，能够可以让大家对数据可视化以及3D数据可视化有一个较为清晰的了解。</p>
<h2 data-id="heading-2">二、 2D数据可视化</h2>
<h3 data-id="heading-3">2.1 什么是2D数据可视化？</h3>
<p><strong>2D数据可视化</strong>是指利用二维平面图表对数据进行组织处理、呈现的一种方式。讲到图表，大家首先想到的可能是我们日常用过柱状图，折线图等展示形式的图表图形。比如下面这种：</p>
<p><img alt="注：图片来自网络（谷歌图片搜索）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949aef7c260b4aae8d519f84825e8c42~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其实除了上面几种形式，还有一些比较炫酷的图表展示形式如：气泡图、面积图、省份地图、词云、瀑布图、漏斗图、热力图、GIS地图等。</p>
<h3 data-id="heading-4">2.2 2D数据可视化应用场景</h3>
<p>2D数据可视化在工作生活中的应用非常广泛。最简单的像Excel数据图表，XMind、Visio属于数据可视化的具体应用场景。也有一些稍微复杂的，比如数据可视化大屏，后台数据报表，地图等。</p>
<p><img alt="注：图片来自网络（谷歌图片搜索）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd4add529ca4a38ab25618fc0ab328c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>随着数据可视化的应用场景越来越广泛，数据可以呈现为更多丰富的可视化形式，使用户能够更加轻易、便捷的获取并理解数据传达的信息。</p>
<h2 data-id="heading-5">三、3D(2D+1D)数据可视化</h2>
<h3 data-id="heading-6">3.1 什么是3D数据可视化？</h3>
<p>3D数据可视化可以理解为在2D数据可视化的基础上增加了Z轴的维度，使数据呈现从二维平面扩展到三维立体结构。是一种新的管理、分析和交互数据的方式，并且能实现实时反射、实时折射、动态阴影等高品质，逼真实时渲染3D图像。</p>
<p>3D数据可视化与2D数据可视化(一般数据可视化)主要区别就是更立体，更真实，更有沉浸感。来张图感受一下：</p>
<p><img alt="注：图片来自网络（https://www.hightopo.com）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d874e6815104631812e4983165bd87e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.2 3D数据可视化应用场景</h3>
<p>3D数据可视化因其知识传输速度快、数据信息展示更直观、信息传达更容易，所以更加容易让使用者进行数据的理解和空间知识的呈现。</p>
<p>目前可见的3D数据可视化应用领域有智慧城市、汽车、手机模型展示等。</p>
<p><img alt="注：图片来自网络（https://www.hightopo.com）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7622b0b508e7418fa7090899e7cb074f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>相信随着浏览器对WebGL的支持度越来越广，以及5G的普及，前端3D可视化的应用领域会越来越广泛。</p>
<h3 data-id="heading-8">3.3 3D数据可视化解决方案</h3>
<p>了解了3D数据可视化的概念和应用场景，我们再来了解下目前业界3D数据可视化主流解决方案：WebGL。</p>
<p>下图为WebGL的渲染过程图：</p>
<p><img alt="注：图片来自vivo官网前端团队" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a51c26c13bf4577ab0171dac7aa81af~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>WebGL（Web Graphics Library） 是基于 OpenGL ES 规范的浏览器实现，上图的WebGL渲染过程可以理解为：</p>
<blockquote>
<p>1）<strong>JavaScript：</strong>  处理着色器需要的顶点坐标、法向量、颜色、纹理等信息，并为顶点着色器提供这些数据</p>
<p>2）<strong>顶点着色器：</strong> 接收 JavaScript 传递过来的顶点信息，将顶点绘制到对应坐标</p>
<p>3）<strong>光栅化阶段：</strong> 将图形内部区域用空像素进行填充</p>
<p>4）<strong>片元着色器：</strong> 为图形内部的像素填充颜色信息</p>
<p>5）<strong>渲染：</strong> 渲染到Canvas对象</p>
</blockquote>
<p>WebGL既可以绘制2D数据可视化图形图表，更是一种 3D 绘图标准，这种绘图技术标准将JavaScript 和 OpenGL ES 2.0 结合在一起，通过绑定， WebGL可以为 HTML5 Canvas 提供硬件 3D 加速渲染，这样 我们就可以借助系统显卡来在浏览器里更流畅地展示 3D 场景和模型。</p>
<h2 data-id="heading-9">四、vivo官网3D应用实战</h2>
<p>对用户来讲，网上购物最大的痛点就是不能所见即所得，目前主流的网上商城一般都是通过图片或者视频展示产品的特点，而这些二维的信息展示方式无法让用户很好的去了解产品的信息。有了3D展示场景之后，用户通过手机模型的3D展示可以更加直观清楚的了解手机的产品细节及特点，从而提升用户的购买欲望。</p>
<p>下面我们一起来了解下vivo官网在实现3D展示时的技术选型及实现方案。</p>
<h3 data-id="heading-10">4.1 可视化工具介绍及技术选型</h3>
<p>目前，业界已经有很多好用的3D可视化开发工具，方便我们进行3D可视化需求的开发。3D数据可视化主要包含渲染库和模型两方面，下面我们从3D渲染库和模型分别了解下3D可视化领域工具及官网的技术选型。</p>
<h4 data-id="heading-11">4.1.1 渲染库选型</h4>
<p>目前实现3D数据可视化的主流解决方案是基于WebGL，那既然有了WebGL，我们为什么还需要渲染库？</p>
<p>这是因为WebGL门槛相对较高，需要理解掌握相对较多的数学知识。虽然WebGL提供的是面向前端的API，但本质上WebGL跟前端开发完全是两个不同的方向，知识的重叠很少。</p>
<p>利用渲染库进行模型的渲染实现可以大大降低我们的学习成本，并且能够完成WebGL所能实现的几乎一切功能。常用的一些3D渲染库有：<strong>ThreeJs、BabylonJS、SceneJS</strong>以及<strong>CesiumJs；</strong></p>
<p><strong>几种不同3D渲染库对比：</strong></p>
<p><img alt="注：图片来自vivo官网前端团队" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2911f850004744cf8f653cf09e1a9c17~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过对比我们可以发现，上述几种渲染库各有优点。但是在做手机模型的3D渲染时，对于光照和阴影以及反射的侧重点比较高，并不需要碰撞检测等特性。所以，基于以上的对比，我们选取ThreeJs作为我们3D渲染的底层库去实现手机模型的3D渲染。</p>
<h4 data-id="heading-12">4.1.2 模型选型</h4>
<p>了解了渲染库，我们再来聊一聊常用的3D模型格式：OBJ、FBX、GLTF。</p>
<p>模型文件其实是一个包含了顶点坐标、索引(index)、UV、法线、节点关系、材质、贴图、动画等信息的数据集合。不论模型格式如何，但是其本质就是对上述信息的编排和组织。各种模型之间的区别无非是组织的方式不同，有些用纯文本（OBJ），有些用json（GLTF），有些用二进制（FBX）。</p>
<p><strong>几种不同模型文件对比：</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c11b2e692ddb474d8a9427b4e1062047~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb2f000fd444f1797f5f1caad5bb7a0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="注：图片来自vivo官网前端团队" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd561c64a640466f8ff94ff7f283864b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过对比我们发现几种模型格式分别适用于不同的场景：</p>
<blockquote>
<p>1）<strong>OBJ</strong>模型对于动画的支持不是特别友好，而手机在做3D展示时需要进行一些模型的拆解动画展示。</p>
<p>2）<strong>FBX</strong> 由于不同引擎解析的规范不同，导致不同引擎渲染出的效果差别较大</p>
<p>3）<strong>GLTF</strong>(GLB) 模型格式扩展性较高，ThreeJs、Babylonjs等WebGL渲染引擎的支持性较好</p>
</blockquote>
<h3 data-id="heading-13">4.2 3D场景搭建及方案实施</h3>
<p>我们发现，如果想要将3D场景中的物体展示的足够逼真，相机和光照是必不可少的两个基本要素。实际业务场景中还有模型颜色切换、模型旋转、缩放、全景场景等逻辑需要我们去处理。</p>
<h4 data-id="heading-14">4.2.1 场景相机</h4>
<p>首先，我们来了解一下相机。3D场景中的相机类似于现实生活中的人眼的功能。相机拍摄一个物体的时候相机的位置和角度需要设置，虚拟的相机还需要设置投影方式。位置和角度我们比较好理解，下面我们来介绍下投影方式：投影有两种方式，分别是正投影与透视投影：</p>
<h5 data-id="heading-15">4.2.1.1 正投影</h5>
<p><strong>正投影：</strong> 正射投影，又叫平行投影。这种投影的视景体是一个矩形的平行管道，也就是一个长方体，如图所示。正射投影的最大一个特点是无论物体距离相机多远，投影后的物体大小尺寸不变。</p>
<p><img alt="注：图片来自网络（http://m.dingjisc.com）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/615d22f1ac2a45d29ab233d7910bc6c8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>正投影通常用在建筑蓝图绘制和计算机辅助设计等平面图形方面，这些行业要求投影后的物体尺寸及相互间的角度不变，以便施工或制造时物体比例大小正确。</p>
<h5 data-id="heading-16">4.2.1.2 透视投影</h5>
<p><strong>透视投影：</strong> 透视投影符合人们心理习惯，即离视点近的物体大，离视点远的物体小，远到极点即为消失，成为灭点。它的视景体类似于一个顶部和底部都被切除掉的棱椎，也就是棱台。</p>
<p><img alt="注：图片来自网络（https://blog.csdn.net）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4626371a64f499dbb92fe462c012b04~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>透视投影通常用于动画、视觉仿真以及其它许多具有真实性反映的方面。相比较来讲，透视投影则更接近我们的视觉感知。所以在官网的手机模型3D展示中，我们选择透视投影来计算相机的投影矩阵。</p>
<p><strong>4.2.2 场景光照</strong></p>
<p>要想让我们渲染出的 3D 物体看起来更自然、逼真，很重要的一点就是模拟各种光照的效果。</p>
<p>3D场景中物体的光照由光源、介质（物体的材质）和反射类型决定的，而反射类型又由物体的材质特点决定。根据不同的光源特点，我们可以将光源分为 4 种不同的类型。</p>
<p>分别是<strong>环境光（Ambient Light）、平行光（Directional Light）、点光源（Positional Light）。</strong></p>
<p>我们分别来了解下环境光（Ambient Light）、平行光（Directional Light）、点光源（Positional Light）。</p>
<p><img alt="注：图片来自网络（https://blog.csdn.net）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f054c7743e457bbe3702163d750f4e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从图中我们可以看出：</p>
<p><strong>平行光</strong>是朝着某个方向照射的光，光线中的每一个光子与其它光子都是平行运动的。举个例子，阳光就可以认为是平行光，平行光只能照亮物体的一部分表面。</p>
<p>平行光除了颜色之外，同时具有方向属性，属于有向光。有向光和物体发生作用时根据物体的材质不同，会产生漫反射和镜面反射两种反射效果。3D场景中最终的反射效果是由环境光、平行光，漫反射以及镜面反射叠加在一起的效果。</p>
<p><strong>点光源</strong>是指光线是从一个点发射出来的，是向着四面八方发射的。这种光在我们的现实生活中是最常被用到的。举个例子，电灯泡就是向各个方向发射光线的，它就可以被认作是点光源。</p>
<p>点光源不仅有方向属性，还有位置属性。因此计算点光源的光照，我们要先根据光源位置和物体表面相对位置来确定方向，然后再和平行光一样，计算光的方向和物体表面法向的夹角。</p>
<p><strong>环境光</strong>就是指物体所在的三维空间中天然的光，它充满整个空间，在每一处的光照强度都一样。环境光没有方向，所以，物体表面反射环境光的效果，只和环境光本身以及材质的反射率有关。</p>
<h4 data-id="heading-17">4.2.3 模型旋转实现</h4>
<p>有了相机和光照就能够比较逼真的将模型呈现给用户了，但是还需要处理模型本身的一些交互操作，比如<strong>模型旋转、颜色切换</strong>等。</p>
<p>实现3D场景中的模型旋转有两种实现方式：</p>
<p>（1）3D场景中的相机不动，旋转3D实体即3D模型</p>
<p><img alt="注：图片来自网络（https://webglfundamentals.org）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bf8861fb8274e25ad536baa3d301f47~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>（2）旋转相机，即3D模型不动，相机围绕模型进行旋转</p>
<p><img alt="注：图片来自网络（https://webglfundamentals.org）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c94bd1ea82e44469fc529cbc7b0e304~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在现实生活中，将物体移动到视场中并不是正确的方法，因为在实际生活中通常是移动相机去拍摄建物体。所以我们选择移动相机 <strong>即实现方式</strong>(1) 去实现3D实体的旋转交互。</p>
<p><strong>4.2.4 模型颜色切换</strong></p>
<p>模型格式采用的是GLB模型（方便后期固化上传），所以每一种颜色对应一个新的GLB文件。</p>
<p>每一次切换模型需要重新对文件进行解析，但是由于不同颜色模型间贴图等材质可以共用，所以即使切换颜色时重新加载模型并解析也会比初始加载时的速度提升很多。所以考虑到后期的固化成本与复用性，切换颜色重新加载模型文件，不失为一种相对比较优雅的处理方式。</p>
<p><img alt="注：图片来自vivo官网前端团队" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c36971805874a05a6d9e69fc511ba78~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>4.2.5 全景场景搭建</strong></p>
<p>为了让用户在浏览产品的3D页面时有更强的沉浸体验。我们采用了全景模式。用户在全景模式下旋转缩放手机时，对应的背景元素同样会跟随相机的旋转和缩放进行旋转缩放。这样用户在进行浏览查看时，交互的体验感更强。</p>
<p>在ThreeJs中全景模式可以通过加载纹理贴图的方式实现：</p>
<pre><code class="hljs language-java copyable" lang="java">let texture = await Loader.loadImg(panoramicImg)
texture.encoding = THREE.sRGBEncoding

let sphereGeometry = <span class="hljs-keyword">new</span> THREE.SphereGeometry(<span class="hljs-number">3000</span>, <span class="hljs-number">160</span>, <span class="hljs-number">160</span>)
sphereGeometry.scale(-<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>)

let sphereMaterial = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123; map: texture &#125;)
let sphere = <span class="hljs-keyword">new</span> THREE.Mesh(sphereGeometry, sphereMaterial)

<span class="hljs-comment">// 设置材质对象的纹理贴图</span>
<span class="hljs-keyword">this</span>.bgMap = sphere
<span class="hljs-keyword">this</span>.stage.scene.add(<span class="hljs-keyword">this</span>.bgMap)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码首先创建一个球形几何SphereGeometry，将创建后的球形几何网格进行x轴反转：sphereGeometry.scale(-1, 1, 1)，使所有的面点向内。然后加载图片数据创建材质并加入map：new THREE.MeshBasicMaterial(&#123;map:texture&#125;)；new THREE.Mesh(sphereGeometry, sphereMaterial) 最终实现全景图效果。</p>
<h3 data-id="heading-18">4.3 性能优化</h3>
<h4 data-id="heading-19">4.3.1 模型压缩</h4>
<p>为了提升页面初始化的加载速度以及切换颜色模型时的解析速度，我们在制作完成模型后，需要对模型进行压缩以降低模型的体积量。</p>
<p>谷歌针对GLB模型有一个压缩库<a href="https://google.github.io/draco/" target="_blank" rel="nofollow noopener noreferrer">Draco 3D</a>，可以在不影响模型展示效果的情况下，对模型的体积进行压缩。可以利用GLTF Pipeline命令行对GLTF模型进行压缩。</p>
<p><strong>压缩的步骤：</strong></p>
<p>1、安装gltf-pipeline</p>
<pre><code class="hljs language-java copyable" lang="java">npm install -g gltf-pipeline
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、转换gltf至glb文件</p>
<pre><code class="hljs language-java copyable" lang="java">Converting a glTF to glb
gltf-pipeline -i model.gltf -o model.glb

gltf-pipeline -i model.gltf -b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>压缩之后，glb文件的体积会减少80%左右，所以在加载速度和效果呈现上会比原始的GLTF文件更快。</p>
<p><img alt="注：图片来自网络（https://cesium.com）" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/063b89b015a449c5820bfb6392073d68~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>4.3.2 模型解压缩</strong></p>
<p>ThreeJs有针对压缩模型的解压缩方案:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// Instantiate a loader</span>
<span class="hljs-keyword">const</span> loader = <span class="hljs-keyword">new</span> GLTFLoader();

<span class="hljs-comment">// Optional: Provide a DRACOLoader instance to decode compressed mesh data</span>
<span class="hljs-keyword">const</span> dracoLoader = <span class="hljs-keyword">new</span> DRACOLoader();
dracoLoader.setDecoderPath( <span class="hljs-string">'/examples/js/libs/draco/'</span> );
loader.setDRACOLoader( dracoLoader );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先构建一个GLTFLoader对象，然后在进行模型加载过程中，设置dracoLoader解析文件的路径，dracoLoader对压缩后的模型文件进行解析。最后将解析后的文件返回至脚本进行渲染呈现。</p>
<h2 data-id="heading-20">五、总结</h2>
<p>本篇文章首先介绍了2D数据可视化，通过将平面图表数据可视化形式拉伸到三维立体结构，衍生出了3D数据可视化相关内容，以及官网基于ThreeJs的3D应用开发实战。</p>
<p>但是WebGL关于3D渲染相关的知识远不止这些。这里只是列举出了比较常用的几种3D模型的渲染要素，比如灯光，相机等。实际还有关于物体材质的光的反射类型：漫反射、镜面反射，相机也有其他类型的相机模型：例如：正交相机、立方相机、立体相机等，由于篇幅原因我们不再做详细的介绍，感兴趣的同学可以去<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL_API" target="_blank" rel="nofollow noopener noreferrer">WebGL</a>官网去查看并学习相关内容。</p>
<blockquote>
<p>作者：vivo 官网商城前端团队-Ni Huaifa</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            