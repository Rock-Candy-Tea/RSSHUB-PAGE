
---
title: '3D to H5工作流应用手册——理论篇'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/bo0saCX6jekyL2bsJBQ8.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 04 Jan 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/bo0saCX6jekyL2bsJBQ8.jpg'
---

<div>   
<blockquote><p>编辑导语：作为产品设计师，你知道计算机是如何理解和实时渲染3D项目的吗？相信你也曾为这个问题而困扰，本篇文章里，作者总结了相应的理论问题，也许可以帮你打通3D和H5之间的障碍。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5275393 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/bo0saCX6jekyL2bsJBQ8.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h3>前言</h3>
<p>设计师需求中3D视觉平移到互动H5中的项目越来越多，three.js和PBR工作流的结合却一直没有被系统化地整理。</p>
<p>和各位前端神仙一起做项目，也一起磕磕碰碰出了爱与痛的领悟。小小总结，希望3D去往H5的道路天堑变通途。</p>
<p>本手册主要分为两大部分：</p>
<p><strong>Part 1 理论篇：</strong>主要让设计师了解计算机到底是如何理解和实时渲染我们设计的3D项目，以及three.js材质和预期材质的对应关系。</p>
<p><strong>Part 2 实践篇：</strong>基于three.js的实现性，提供场景、材质贴图的制作思路、以及gltf工作流，并动态讨论项目常常遇到的还原问题。</p>
<p>本文主要for刚接触3D图形学的设计师，仅截取了最常用的理论知识和大家一起学习。</p>
<p>部分涉及技术美术或计算机图形学的描述可能不甚严谨，希望大家多多交流讨论哈。</p>
<p>其实无论H5开发用到的是哪种webGL，设计相关的材质制作基本还是基于PBR思路进行的，所以这边建议各位亲可以先去阅读一下Substance官方宝册《The PBR Guide》。</p>
<h2 id="toc-1">理论篇</h2>
<p>设计师在还原3D类型的互动H5项目的时候一定想过这个宇宙终极问题：<strong>为什么H5/Web实现的3D效果和C4D里渲染出来的差异那么大？</strong></p>
<p>其实这是我们对实时渲染引擎（UE、Unity、three.js等）和离线渲染工具（Redshift、Octane、Vray等）的差异存在误解：一是离线渲染工具是基于真实光照环境来计算每颗像素的着色，实时渲染如果要实现这种效果需要耗费更多硬件基础和算力去模拟光照（没个好显卡都开不动光追）。</p>
<p>虽然UE5的实时渲染技术和硬件兼容性已经让大家大吃一惊，但在实际项目，尤其是需要兼容低端设备的H5来说，渲染能力还是相对有限的。二是对于游戏或H5互动网站实际应用来说，流畅的互动体验优先级往往高于画面精细度，所以牺牲视觉保性能也是常见情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/pE4dhdNO6yESF6tFlPd1.jpeg" alt="3D to H5工作流应用手册 [理论篇]" width="692" height="779" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Octane离线渲染效果 VS three.js 实时渲染效果</p>
<p style="text-align: center;">材质细节、全局光照及投影、以及抗锯齿表现差距明显</p>
<p>当实时渲染效果与设计预期差距过大时，设计师能多了解一些基础的计算机图形学，也许就能更好地和开发同学商讨性价比更高的视觉实现和资源优化方案（以及更多Battle的筹码）。</p>
<h3>1. 着色器与着色算法差异（靴靴微硬核预警）</h3>
<p>首先我们要知道计算机之所以能在2D屏幕上画出3D的图像，是因为有着色器（Shader）在绘制，它将我们三维空间里的模型与光照信息进行转换，并光栅化为二维图像。在计算机图形学中，着色器是用于对图像的材质（光照、亮度、颜色）进行处理的程式。</p>
<p>常用的着色器分为四种：像素/片元着色器（Pixel/Fragment Shader）、顶点着色器（Vertex Shader）、几何着色器（Geometry Shader）、细分曲面着色器（Tessellation Shader）。</p>
<p>像素/片元着色器与顶点着色器（Vertex Shader）在webGL处理过程中都有使用，顶点着色器先将模型中每个顶点的位置、纹理坐标、颜色等信息进行转换装配，再由片元着色器对3D信息光栅化并转换成2D屏幕信息。（关于着色器差异，感兴趣的同学可以直接跳到附录查看。）</p>
<p>着色器是怎么把顶点中所带有光照、纹理等信息转换并重建在二维图像的像素中呢？GPU中是透过不同的着色算法来实现的。</p>
<p>一种是获取每个三角形的插值（Interpolate）来实现，这种方法称作Per Vertex Lighting，但是当三角型很大的时候，插值往往不够精准。此时还可以引用另一种方法Per Pixel Lighting，计算每个像素的光照信息，获得更好的渲染效果，但是往往也带来更大的计算量。</p>
<p>一般常见计算机图形着色算法有三类：Flat Shading、Gouraud Shading、Phong Shading。这些算法虽然看起来和我们设计师没啥关系，但事实上在后面了解three.js材质时，就会发现他们在呈现时的差异。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/UncFN2ixoKVw4MH9pONa.png" alt="3D to H5工作流应用手册 [理论篇]" width="698" height="313" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Flat、Gouraud、Blinn-Phong着色法比较 [ F1, ©️Stefano Scheggi ]</p>
<p><strong>1）平直着色法 Flat Shading</strong></p>
<p>这种着色法认为模型中所有面都是平的，同一个多边形的上任意点的法线方向都相同。着色时，会优先选择多边形的第一个顶点或三角形的几何中心计算颜色。这种着色法实践上的效果很像低面模型，也比较适合使用在高速渲染的场景。值得注意的是，这种着色法难以做出平滑高光效果。</p>
<p><strong>2）高洛德平滑着色法 Gouraud Shading</strong></p>
<p>这是一种平滑的着色方法，在着色时会先计算三角形每个顶点的光照特性，利用双线插值去补齐三角形区域内其他像素的颜色。这个着色法的比起平直着色法增加了插值的细节，而且也比Phong着色法渲染单个像素的光照特性的性能要高。</p>
<p>但是在渲染高光时，可能会因为无法获取精确的光照值而出现一些不自然的过渡（或T型连接容易被错误绘制），此时可以考虑对模型进行细分或使用漫反射材质。</p>
<p><strong>3）Phong平滑着色法 Phong Shading</strong></p>
<p>与Gouraud Shading不同的是，它会对顶点的法线进行插值，并透过每个像素的法向量计算光照特性。这种做法能绘制出精致、精准的曲面，但是计算量较大。Blinn-Phong是Phong的进阶版，着色性能更好，且高光弥散更自然。</p>
<h3>2. 基本光照模型 Illumination Model</h3>
<p>简单了解计算机如何绘制3D图形后，再来看看它要如何具体理解我们所设计的3D场景。</p>
<p>3D转换成2D，也就是3D栅格化的过程中，每一个像素的颜色是需要基于它所在的环境计算出来，而基于被渲染物体表面某个点的光强度计算模型就被称为光照明模型（Illumination Model）或光照模型（Light Model），透过计算光照模型所得到表面位置对应像素颜色的过程被称为表面绘制（Surface Render）。</p>
<p>*请注意这里说的光照模型并不是指设计师理解的3D立体模型，而是指模型对象表面光照效果的数学计算模型。</p>
<p>影响光照模型的因素有两大方面，一是本身给渲染物体材质设置的各种光学特性（颜色反射系数、表面纹理、透明度等），二是场景中光源光及环境光（场景中各个被照明对象的反射光）。</p>
<p>传统光照模型都是对漫反射和镜面反射的理想化模拟，如果要还原基于真实物理世界的效果，光照模型需要遵循能量守恒定律：一个物体能反射的光必然少于它接受的光。在实践层面则表现为，一个漫反射更强且更粗糙的物体会反射更暗且范围更大的高光，反之亦反。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/1IQgF3XFz3bklXKP03dS.png" alt="3D to H5工作流应用手册 [理论篇]" width="697" height="131" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">基于PBR的光照模型需要遵循能量守恒定律 [ F2, ©️Joe Wilson ]</p>
<p>光照模型与着色组合在不同的渲染需求下也会有不同的应用：</p>
<ul>
<li>真实感渲染（Photorealistic Rendering）：目的是基于真实物理世界对3D场景进行仿真还原。</li>
<li>非真实感渲染（Unphotorealistic Rendering）：也被成为风格化渲染（Stylistic Rendering），会更抽象化地对模型进行重绘。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/Hp5HsgSVjaKspBRTWnGL.png" alt="3D to H5工作流应用手册 [理论篇]" width="694" height="268" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">真实感渲染及非真实感渲染对比 [ F3, ©️Autodesk ]</p>
<p><strong>1）真实感渲染 Photorealistic Rendering</strong></p>
<p>考虑到真实感渲染对硬件的依赖，目前webGL中使用的一般以简单的局部光照模型为主（只计算光源对物体的光照效果，不计算物体间的相互影响，我们看到的“假反射”通常透过贴图来进行模拟），根据反射形态，经典的光照模型有下列几种：</p>
<p><strong>Lambert 漫反射模型：</strong></p>
<p>这种模型的粗糙表面（如塑料、石材等）会将反射光从各个方向反射出去，而这种光反射也称为漫反射。理想的漫反射体我们通常称作郎伯反射体（Lambertian Reflectors），也就是我们熟悉的橡胶材质。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/Xyh8ErPZRL9LjEiIYEzo.png" alt="3D to H5工作流应用手册 [理论篇]" width="694" height="158" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">漫反射模型与其他光照模型对比 [ F4, ©️ViroCore ]</p>
<p><strong>Phong 镜面反射模型：</strong></p>
<p>这是一种以实验及观察为合成基础的非物理模型。它的表面反射同时结合了粗糙表面漫反射和光滑表面镜面反射，但Phong模型在高光处的表现有过渡瑕疵。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/MW1n8iJORQ4fVovvbtQ5.png" alt="3D to H5工作流应用手册 [理论篇]" width="695" height="193" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Phong镜面反射模型视觉构成 [ F5 ]</p>
<p><strong>Blinn–Phong 模型：</strong></p>
<p>是在OpenGL和Direct3D里默认的着色模型，一种调优后的非物理的Phong模型，顶点间的像素插值使用Gouraud着色算法，比Phong着色算法性能更好，而且高光效果也更平滑。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/yTtZvqtiMuSxxrjkgJWd.png" alt="3D to H5工作流应用手册 [理论篇]" width="698" height="194" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Phong及Blinn-Phong镜面反射模型对比 [ F6 ]</p>
<p><strong>Cook-Torrance/GGX 光照模型：</strong></p>
<p>如果你用过C4D的默认渲染器，那么一定在材质的反射通道设置中见过它俩。</p>
<p>这是相对高级的光照模型，不同于Phong和Blinn-Phong模型仅仅对漫反射及镜面反射进行理想化模拟，这两个光照模型基于不同物理材质加入了微表面（Microfacet）的概念，并考虑到表面粗糙度对反射的影响，对镜面反射进行了调优，使得高光的长尾弥散更加自然，也是目前PBR渲染管线（Unity、UE）中较常用的光照模型。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/5tFzto69nQ86IR1sGmgi.png" alt="3D to H5工作流应用手册 [理论篇]" width="695" height="235" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Phong、Blinn-Phong与GGX镜面反射模型对比 [ F7, ©️ridgestd ]</p>
<p><strong>次表面散射模型 </strong><strong>Subsurface scattering/SSS：</strong></p>
<p>终于有一个设计师们常见的概念了。次表面散射是指光穿透不透明物体时（皮肤、液体、毛玻璃等）的散射现象。现实生活中，大部分物体都是半透明的，光会先穿透物体表面，继而在物体内被吸收、多次反射、然后在不同的点穿出物体。以皮肤为例，只有大概6%的反射是直接反射，而94%的反射都是次表面散射。</p>
<p>BSSRDF（双向次表面反射分布函数）是用于描述入射光在介质内部的光照模型，目前也被应用在最新的虚拟角色皮肤实时渲染中；但由于SSS材质的计算需要依赖深度/厚度数据，所以webGL对这种高级光照效果的还原程度还是相对有限的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/YGvB1evdJqmlm8ipAVN5.png" alt="3D to H5工作流应用手册 [理论篇]" width="690" height="392" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Unity中模拟次表面散射光照模型效果 [ F8, ©️Alan Zucconi ]</p>
<p><strong>2）非真实感渲染 Non-Photorealistic Rendering-NPR</strong></p>
<p>也就是我们常说的3渲2，非写实渲染风格也是从人们对3D场景套以2D绘画或自然媒体材质需求而演化过来的。因此非写实渲染技术实际上是不同光照模型+不同着色处理共同作用的风格化输出，目前也被大量应用在动画及游戏中，像《英雄联盟：双城之战》《蜘蛛侠：平行宇宙》都是顶级三渲二大作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/GG67zEubqWuSYn2wgacV.jpeg" alt="3D to H5工作流应用手册 [理论篇]" width="696" height="392" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">在不同通道中混合应用真实感渲染及非真实感渲染效果 [ F9, ©️Polygon Runway]</p>
<p><strong>Cel Shading/Toon Shading：</strong></p>
<p>卡通着色，一种最常见的以3D技术模拟扁平风格的着色形式，通常以极简的颜色、渐变及明确的外框线等漫画元素作为风格特征。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/IpXiBbKxO56qJYRZtBhi.png" alt="3D to H5工作流应用手册 [理论篇]" width="699" height="277" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Blender中不同类型的Toon Shader效果 [ F10, ©️Blendernpr]</p>
<p>日本创意编程师Misaki Nakano制作了一个非常有趣的Toon Shading H5互动页面，大家可以体验一下不同着色形态下非常模型的视觉表现。搜索体验：https://mnmxmx.github.io/toon-shading/dst/index.html</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/alOwrty1PDU5dWdKSNP2.gif" alt="3D to H5工作流应用手册 [理论篇]" width="697" height="395" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Misaki Nakano的Toon Shader互动网站 [ F11, ©️Misaki Nakano]</p>
<p><strong>Customized Shading：</strong></p>
<p>目前越来越多渲染器可支持设计师及工程师根据项目需求对着色进行定制化处理，以产出更具风格化和艺术化的着色效果。例如工业界插画常用的冷暖着色（Gooch Shading），以及更具绘画质感的素描着色（Hatching）及油画水墨画等自然媒体着色，都已经深入到了我们日常的创作之中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/4kkOw23zoTvZcmRqACAi.png" alt="3D to H5工作流应用手册 [理论篇]" width="695" height="202" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">在Unity中，基于真实感渲染的贴图效果与NPR水墨风格化着色效果对比 [ F11, ©️邓佳迪]</p>
<h3>3. Three.js 材质着色对比</h3>
<p>说完真实感与非真实感渲染差异后，我们再来看看Three.js中的材质。</p>
<p>和许多渲染引擎一样，除了原生材质外，webGL的材质和着色都是可以根据需求进行定制的，但这往往会也带来较高的开发成本及兼容性风险。考虑到H5项目的实际应用场景，下表罗列了Three.js原生材质的对比，包含了材质特性优势、贴图差异及适用场景，大家可以基于项目需求快速选择并混合使用：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/T8yTK6lEeo75RCwtgAZt.jpeg" alt="3D to H5工作流应用手册 [理论篇]" width="691" height="1420" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">three.js材质对比表</p>
<h3>4. 色彩描述与管理 Color Space</h3>
<p>虽然着色、光照模型以及材质渲染对3D表现有着最为直观的影响，但3D工作流仍有一个隐秘而关键的环节——色彩管理。</p>
<p>真实世界中按照物理定律，如果光的强度增加一倍，那么亮度也会增加一倍，这是线性的关系。理想状态下，像素在显示屏上的亮度也应为线性关系，才能符合人眼对真实世界的观察效果（如图b：横坐标为像素的物理亮度，纵坐标为像素显示时的实际亮度）。</p>
<p>但是显示器的成像由于电压的影响，导致输出亮度与电压的关系是一个亮度等于电压的1.7-2.3次幂的非线性关系，这就导致了当电压线性变化时，亮度的变化在暗处转换时变慢，如果显示器不经过矫正，暗部成色也会整体偏暗（如图c）。目前大多数显示器的Gamma值约为2.2，所以也可以理解Gamma2.2是所有显示器自带的一个遗传病。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/BlVNbn5Uv5SOpyteldSN.png" alt="3D to H5工作流应用手册 [理论篇]" width="698" height="258" referrerpolicy="no-referrer"></p>
<ul>
<li>红色上曲线=Gamma0.45=sRGB Space</li>
<li>绿色下曲线=Gamma2.2=显示器真实成像缺陷</li>
<li>蓝色斜线=Gamma1.0=Linear Space 真实物理世界线性关系</li>
</ul>
<p>为了矫正显示器的非线性问题（从图c校正回图b），我们需要对它进行一个2.2次幂的逆运算（如图a），在数学上，这是一个约0.45的幂运算（Gamma0.45）。经过0.45幂运算，再由显示器经过2.2次幂输出，最后的颜色就和实际物理空间的一致了，这套校正的操作就是伽马校正（Gamma Correction）。</p>
<p>而我们常见的sRGB就是Gamma0.45所在的色彩空间，是1996由微软与惠普共同开发的标准色彩空间。当照片素材一开始储存成sRGB空间，相当于自带一个Gamma0.45的遗传病抗体，当它被显示器显示时，就自动中和了显示器Gamma2.2的缺陷，从而显示出与物理世界相符的亮度。</p>
<p>另一个校正原因是因为人眼在接受光线时的敏感度也不是线性的，人对于暗部的感知更敏感，对高亮区域感知较弱，而且人眼感知光强度与光的物理强度也刚好是对数关系。为了在暗部呈现更多人眼可感知的细节，Gamma0.45的色彩空间中（如图a），像素的实际亮度也会高于它的物理亮度。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/ex15ElnPBcjYECDank0u.png" alt="3D to H5工作流应用手册 [理论篇]" width="693" height="199" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">人眼感知光强度与发射光真实物理强度对比</p>
<p>上面那一大段确实有点绕，但也就说回来为什么建议渲染时使用线性空间（Linear Space）了。因为在计算机图形中，着色器的运算基本上都是基于物理世界的光照模型来保证渲染真实性的，如果模型的纹理输入值是非线性的（sRGB），那么运算的前提就不统一，输出的结果自然就不那么真实了。</p>
<p>而在大多数工作流及渲染软件中，大部分贴图资源都是默认输出sRGB的（设计师作图环境一般也在sRGB，所见即所得），而法线贴图、光线贴图等纹理（纯数值类纹理，只用于计算）又是Linear的，这个部分就需要我们根据渲染引擎本身的特性，来判断是否需要对不同的贴图进行不同的”去Gamma化”处理了（WebGL、Unity、Octane等）。</p>
<p>将所有贴图进行去Gamma化，统一为Linear空间后，再在渲染输出时由引擎统一进行Gamma校正，这个时候在显示屏里显示的就是接近真实世界的效果了。</p>
<p>更多色彩空间的实际效果比较，大家可以看下Unity的文档：《Linear/Gamma渲染比较》：</p>
<p>https://docs.unity3d.com/Manual/LinearRendering-LinearOrGammaWorkflow.html</p>
<p>回到H5所用的Three.js，它的着色器计算也是默认在Linear空间，如果最终渲染时不转化为sRGB，在设备显示时可能会造成色彩失真。在three.js中色彩管理的工作流会根据导入模型Asset的差异而有所不同，如果贴图与模型是分别导入场景，则建议可尝试以下流程：</p>
<p>1）输入贴图数据 sRGB to Linear: 含色彩的贴图（基础材质、环境、发光）设编码为sRGB（texture.encoding = sRGBEncoding），或将渲染设置renderer.gammaInput设为True，可将原为sRGB的贴图转换为Linear，而原纯数值类贴图（法线、凹凸等）仍旧保持Linear；这一操作可保证贴图输入数据的正确性与统一性。</p>
<p>2）刷新材质：当材质编码类型被修改后，需要设置Material.needsUpdate为True，以重新编译材质。</p>
<p>3）输出渲染 Linear to sRGB: 校正渲染输出值的Gamma：renderer.gammaOutput = true; renderer.gammaFactor = 2.2；以供显示屏正确显色。</p>
<p>《Part1-理论篇》就先告一段落啦，如果你偶发失眠，建议可以反复咀嚼延伸阅读的内容。</p>
<p>《Part2-实践篇》会继续完善three.js场景、材质贴图的制作思路、以及gltf工作流，并动态讨论项目常常遇到的还原问题。</p>
<p>2022，咱们需求再见。</p>
<h3>附录</h3>
<p><strong>1）着色器差异</strong></p>
<p><strong>① 像素着色器 Pixel Shader</strong></p>
<p>也称为片元/片段着色器（Fragment Shader）, 为二维着色器。它记录了每一个像素的颜色、深度、透明度信息。最简单的像素着色器可用于记录颜色，像素着色器通常使用相同的色阶来表示光照属性，以实现凹凸、阴影、高光、透明度等贴图。同时，他们也可以用来修改每个像素的深度（Z-buffering）。</p>
<p>但是在3D图像中，像素着色器可能无法实现一些复杂的效果，因为它只能控制独立的像素而并不含有场景中模型的顶点信息。不过，像素着色器拥有屏幕的坐标信息，可以依据屏幕或邻近像素的的材质进行采样并增强，例如，Cel Shader的边缘强化或一些后期的模糊效果。</p>
<p><strong>② 顶点着色器 Vextex Shader</strong></p>
<p>是最常见的3D着色器，他记录了模型每个顶点的位置、纹理坐标、颜色等信息。它将每个顶点的3D位置信息转换成2D屏幕坐标。顶点着色器可以处理位置、颜色、纹理的坐标，但是无法增加新的顶点。</p>
<p><strong>③ 几何着色器 Geometry Shader</strong></p>
<p>是最近新兴的着色器，在Direct3D 10 和Open GL3.2中被引用。这种着色器可以在图元外生成新的顶点，从而转换成新的图元（例如点、线、三角等），而优势也是在于可以直接在着色中增加模型细节，减低CPU负担。集合着色器的常用场景包括点精灵（Point Sprite）生成（粒子动画），细分曲面，体积阴影等。</p>
<p><strong>④ 细分曲面着色器 Tessellation Shader</strong></p>
<p>在OpenGL4.0和 Direct3D 11中出现，它可以在图元内镶嵌更多三角体。为传统模型新增了两个着色步骤（一是细分控制着色，又称为Hull Shader，二是细分评估着色，又称为Domain Shader），两者结合可以让简单的模型快速获得细分曲面。（例如，含细分曲面效果的模型加上置换贴图就可以获得极其逼真细腻的模型）</p>
<p><strong>2）一些术语的简单理解</strong></p>
<p><strong>GL：</strong>Graphics Library, 图形函数库。</p>
<p><strong>webGL：</strong>Web Graphics Library，Html 5可接入的3D绘图协议/函数库，可以为H5 Canvas提供3D渲染的各类API。</p>
<p><strong>Z-Buffering：</strong></p>
<p>深度缓冲，3D图像在渲物体的时候，每一个生成的像素的深度会存储在缓冲区中。如果另一个物体也在同一个像素中产生渲染结果，那么GPU会比较两个物体的深度，优先渲染距离更近的物体，这个过程叫做Z-Culling。当两个物体靠很近的时候（16-bit），可能会出现Z-Fighting，也就是交叠闪烁的现象，使用24或32bit的Buffer可以有效缓解。</p>
<p><strong>Rendering Pipeline：</strong></p>
<p>渲染管线/渲染流水线/像素流水线，为GPU的处理工作流，是GPU负责给图形配上颜色的专门通道。管线越多，画面越流畅精美。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3D to H5工作流应用手册 [理论篇]" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/UeFutqJfTqCTjLYb71Hk.png" alt="3D to H5工作流应用手册 [理论篇]" width="690" height="156" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">渲染管道细节工作流 [ F12 ]</p>
<p><strong>Rasterization：</strong></p>
<p>光栅化/点阵化/栅格化，就是将管线处理完的图元转换成一系列屏幕可视的像素，过程包括：图元拼装（Primitive assembly）-三角形遍历（Triangle Traversal）- Pixel Processing-Merging。</p>
<p><strong>3）参考文献+延伸阅读</strong></p>
<p>[1]Hearn, D. and Baker, M.P., 2004. Computer graphics with OpenGL, 计算机图形学第四版 . Upper Saddle River, NJ: Pearson Prentice Hall,.</p>
<p>[2]Akenine-Möller, T., Haines, E. and Hoffman, N., 2019.Real-time rendering. Crc Press.</p>
<p>[3]锐萌瑞, 经典光照模型（illumination model）</p>
<p>https://blog.csdn.net/qq_34552886/article/details/79089418</p>
<p>[4]Krishnaswamy, A; Baronoski, GVG (2004). “A Biophysically-based Spectral Model of Light Interaction with Human Skin” (PDF).</p>
<p>[5] List of Common Shading Algorithm：</p>
<p>https://en.wikipedia.org/wiki/List_of_common_shading_algorithms</p>
<p>[6] 0向往0, 剖析Unreal Engine超真实人类的渲染技术Part 1 – 概述和皮肤渲染</p>
<p>https://www.cnblogs.com/timlly/p/11098212.html</p>
<p>[7] 毛星云, 【《Real-Time Rendering 3rd》 提炼总结】(十) 第十一章 · 非真实感渲染(NPR)相关技术总结</p>
<p>https://zhuanlan.zhihu.com/p/31194204</p>
<p>[8] 卜噪大仙，局部光照模型杂记【Lambert/Phong/Blin-Phong/BRDF/BSSRDF/Cook-Torrance】</p>
<p>https://www.jianshu.com/p/96ca495669d6</p>
<p>[9] puppet_masterm, Unity Shader-Matcap（材质捕获）</p>
<p>https://blog.csdn.net/puppet_master/article/details/83582477</p>
<p>[10] WestLangley, documentation on gamma correction incorrect? #11110</p>
<p>https://github.com/mrdoob/three.js/issues/11110</p>
<p>[11] donmccurdy, Best practise for color management</p>
<p>https://github.com/aframevr/aframe/issues/3509</p>
<p>https://github.com/mrdoob/three.js/issues/11337#issuecomment-440795075</p>
<p>[12] alteredq, Questions about the use of Gamma Correction in the WebGL Renderer #1488</p>
<p>https://github.com/mrdoob/three.js/issues/1488</p>
<p>[13] Friksel, What’s this about gammaFactor?</p>
<p>https://discourse.threejs.org/t/whats-this-about-gammafactor/4264/3</p>
<p>[14] PZZZB，Linear Space Lightning、Gamma、sRGB详情讲解：</p>
<p>https://zhuanlan.zhihu.com/p/66558476</p>
<p>[15] Learn OpenGL, Gamma Correction</p>
<p>https://learnopengl.com/Advanced-Lighting/Gamma-Correction</p>
<p>[16] 柯灵杰，3D图形学基础：</p>
<p>https://zhuanlan.zhihu.com/p/27846162?source=post_page—–b1cde1f23adf———————-</p>
<p>[17] Klayge游戏引擎，关于D3D11你必须了解的几件事情（三）</p>
<p>http://www.klayge.org/?p=1404</p>
<p>[18] 拓荒犬, GPU渲染流水线简介</p>
<p>https://zhuanlan.zhihu.com/p/61949898</p>
<p>[19] Steve Baker, Learning to Love your Z-buffer.</p>
<p>https://www.sjbaker.org/steve/omniv/love_your_z_buffer.html</p>
<p>[20] Steve Baker, Alpha-blending and the Z-buffer.</p>
<p>https://www.sjbaker.org/steve/omniv/alpha_sorting.html</p>
<p>[21] Microsoft, Direct3D 11 Graphics-Tessellation Stages</p>
<p>https://docs.microsoft.com/en-us/windows/win32/direct3d11/direct3d-11-advanced-stages-tessellation#domain-shader-stage</p>
<p>[F1] Stefano Scheggi, Flat shading vs. Gouraud shading vs. Blinn-Phong shading</p>
<p>https://www.youtube.com/watch?v=VRw3GuVdldo</p>
<p>[F2] Joe Wilson, Physically-Based Rendering, And You Can Too!</p>
<p>https://marmoset.co/posts/basic-theory-of-physically-based-rendering/</p>
<p>[F3] Autodesk, Apply Visual Effects</p>
<p>https://download.autodesk.com/us/mudbox/help2011_5/index.html?url=./files/WS1a9193826455f5ff5cf1d02511b1d000978-6b44.htm,topicNumber=d0e8759</p>
<p>[F4] Virocore, Lighting and Materials</p>
<p>https://virocore.viromedia.com/v1.0.0/docs/3d-scene-lighting</p>
<p>[F5] Wikipedia, Phong Reflection Model</p>
<p>https://en.wikipedia.org/wiki/Phong_reflection_model</p>
<p>[F6] Wikipedia, Blinn–Phong reflection model</p>
<p>https://en.wikipedia.org/wiki/Blinn%E2%80%93Phong_reflection_model#cite_note-4</p>
<p>[F7] Ridgestd，从Microfacet到GGX反射模型</p>
<p>http://ridgestd.github.io/2019/03/18/ggx-shader/</p>
<p>[F8] Alan Zucconi, Fast Subsurface Scattering in Unity (Part 2)</p>
<p>https://www.alanzucconi.com/tag/sss/</p>
<p>[F9] Polygon Runway, Toon Shading Tutorial for Blender 2.8 with Commentary</p>
<p>https://www.youtube.com/watch?v=kriKwtzZWFg</p>
<p>[F10] Blendernpr, Basic Toon Shaders with Blender</p>
<p>]http://blendernpr.org/basic-toon-shaders-with-blender-internal/</p>
<p>[F11] 邓佳笛，在Unity进行水墨风3D渲染的尝试</p>
<p>https://zhuanlan.zhihu.com/p/25346977</p>
<p>[F12] Wikipedia, Graphics_pipeline</p>
<p>https://en.wikipedia.org/wiki/Graphics_pipeline</p>
<p> </p>
<p>本文由 @腾讯ISUX 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5275318" data-author="818930" data-avatar="http://image.woshipm.com/wp-files/2019/11/wp2UyWymZgi2Ym8SVyQ2.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            