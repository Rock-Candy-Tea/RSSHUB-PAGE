
---
title: '工序升级！在 Cocos Creator 里画一个完美的矩形'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/15/140833l5fpzf390kouup9v.jpg'
author: GameRes 游资网
comments: false
date: Fri, 15 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/15/140833l5fpzf390kouup9v.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516762">
在认识了 WebGL 的基础工作原理，以及如何利用 WebGL 绘制后，接下来的几章就带大家了解一下这套流程如何应用到 Cocos Creator 3.x。<br><br>
之前我们利用 WebGL 绘制出了一个矩形，本章先来看看要如何在 Cocos Creator 3.x 绘制同样的矩形。<br><br><strong><font color="#de5650">流程概述</font></strong><br><br>
Cocos Creator 3.x 为了方便用户使用和定制，对内部功能做了多层封装，用户根据需求自行组装即可。因此，我们只需要组装相关的部分。根据矩形绘制流程，可以将内容很直接地拆分成以下几个部分：<br><br><strong>第一是数据准备部分，也就是提供顶点数据。</strong>在之前的案例里，我们是直接提供了固定数据。Cocos Creator 3.x 也有多个地方会提供顶点数据，例如：2D 的渲染组件（Sprite、Graphics 等），3D 的模型组件（MeshRenderer、SkinnedMeshRendere 等）等。当然，用户也可以自定义顶点数据，由于这部分涉及到渲染管线以及引擎底层，超出本章介绍范围，这里就不再过多赘述。<br><br><strong>第二是画布清除阶段，这部分跟相机有关。</strong>因为游戏场景往往是由很多对象构造而成，但是实际呈现的画面只有其中一小部分，呈现的部分就是相机照射的部分。由于我们的屏幕画布只有一块，因此，由相机决定是否要擦除之前的内容重新绘制，或者在原有内容的基础上继续绘制。<br><br><strong>第三是着色指令部分，这部分就类似于顶点/片元文本的编写。</strong>在 Cocos Creator 3.x 里通过 Cocos Effect 来实现。<br><br>
在这里我会用最基础绘图组件 Graphics 进行绘制，带大家了解一下这套流程。<br><br>
首先，新建场景，在层级管理器上创建 Canvas 节点，并在 Canvas 节点下创建一个 Graphics 节点。创建脚本 Draw 并挂载在 Graphics 节点身上并调用 Graphics 绘图相关接口。在这里，同样绘制一个矩形：<br><br>
import &#123; _decorator, Component, Node, Graphics &#125; from 'cc';<br><br>
const &#123; ccclass, property &#125; = _decorator;<br><br>
@ccclass('Draw')<br><br>
export class Draw extends Component &#123;<br><br>
start () &#123;<br><br>
const g = this.getComponent(Graphics);<br><br>
g.fillRect(0, 0, 200, 150);<br><br>
&#125;<br><br>
&#125;<br><br>
接着，运行预览，就可以看到绘制了一个纯白色的矩形。<br><br><div align="center">
<img id="aimg_1015116" aid="1015116" zoomfile="https://di.gameres.com/attachment/forum/202110/15/140833l5fpzf390kouup9v.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/140833l5fpzf390kouup9v.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/140833l5fpzf390kouup9v.jpg" referrerpolicy="no-referrer">
</div>
<br>
在这个过程中一共经历了以下几个阶段：<br><br><div align="center">
<img id="aimg_1015117" aid="1015117" zoomfile="https://di.gameres.com/attachment/forum/202110/15/140833lcbgopg13fbgzwf9.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/140833lcbgopg13fbgzwf9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/140833lcbgopg13fbgzwf9.jpg" referrerpolicy="no-referrer">
</div>
<br>
接下来说说开发者需要关心的几个部分。所有之前关于 gl.xxx 的部分，都在底层直接处理完了，所以并不需要我们手动去执行，除非整个流程我们都需要使用自定义的。<br><br><strong><font color="#de5650">顶点数据</font></strong><br><br>
在 Creator 中，顶点坐标起源于模型空间，最终需要转换到屏幕空间，这过程需要经历以下几个步骤：<br><br><div align="center">
<img id="aimg_1015118" aid="1015118" zoomfile="https://di.gameres.com/attachment/forum/202110/15/140833emakm13beff1zfei.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/140833emakm13beff1zfei.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/140833emakm13beff1zfei.jpg" referrerpolicy="no-referrer">
</div>
<br>
Local Space 局部坐标，也可以称之为模型坐标。可以理解为就是相对于父节点的坐标。<br><br>
World Space 世界坐标。世界坐标是一个很大的空间范围，相对于世界原点。通过模型坐标结合模型矩阵得出。<br><br>
View Space 观察坐标。可以理解为将世界坐标转换到相机空间的坐标，转换后的值是相对于相机原点。通过世界坐标结合观察矩阵得出。<br><br>
Clip Space 裁剪坐标。也就是将观察坐标处理到 -1.0 ～ 1.0 的范围，也就是我们在 WebGL 里提供的标准设备化坐标，最终剔除超出 -1 ～ 1 的坐标。通过观察坐标结合投影矩阵得出。<br><br>
Screen Space 屏幕坐标。这个过程其实就是将 -1.0 ～ 1.0 范围的坐标转换到 gl.viewport 所定义的坐标范围内。最后变换出来的坐标会送到光栅器，转换成片段。<br><br>
因此，根据数据类型，最终都需要转换成裁剪坐标提供。<strong>Graphics 提供的是模型坐标</strong>。喜欢探究的同学可以查看引擎底层 graphics.ts 里的 activeMode、_uploadData 和 graphics-assemler 部分，这里就处理了顶点数据缓存创建、绘制数据收集，绑定等步骤。<br><br>
这里顺带提一下<strong>标准设备化坐标和屏幕坐标之间的关系。</strong>标准化设备坐标是 x 轴向右，y 轴向上，x 和 y 的取值都是从 -1～1，在这个范围内的顶点可见，否则都不可见。屏幕坐标是 x 轴向右，y 轴向下，x 和 y 的取值范围都是从 0 对应到屏幕宽高，在矩阵变换的最后一步，就是将标准化设备坐标转换到屏幕坐标后上屏显示。<br><br><div align="center">
<img id="aimg_1015119" aid="1015119" zoomfile="https://di.gameres.com/attachment/forum/202110/15/140834mczzr75efh6sepri.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/140834mczzr75efh6sepri.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/140834mczzr75efh6sepri.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">Cocos Effect</font></strong><br><br>
有了顶点数据之后，对应的也需要编写 Shader 文本，在 3.x 里则对应 Cocos Effect。Cocos Effect 是一种基于 YAML 和 GLSL 的单源码嵌入式领域特定语言，YAML 部分声明流程控制清单，GLSL 部分声明实际的着色片段，这两部分内容上相互补充，共同构成了一个完整的渲染流程描述。引擎会根据这份描述执行相对应的渲染程序。<strong>Cocos Effect 无法单独使用，需要搭配材质使用。</strong><br><br>
> 注意：如果使用 VSCode 编辑自定义 Effect。推荐在 VSCode 上搜索安装 Cocos Effect 插件，以便获得代码高亮提示。<br><br>
我们可以通过在编辑器的资源管理器面板处右键，选择 Effect 创建 .effect 文件即可。<br><br><strong><font color="#de5650">YAML101</font></strong><br><br>
YAML 是一种序列化语言，也可以理解为是一种专注于写配置文件的语言。Cocos Creator 3.x 完全支持 YAML 1.2 标准的解析器。YAML 完全兼容 Json 语法，所以 Json 也可以看做是 YAML 的子集。<br><br>
YAML 是由 : 和空格分隔的键值组合。<br><br>
所有的引号和逗号都可以省略<br><br>
key1: 1<br><br>
key2: unquoted string<br><br>
// 注意：冒号后的空格不可省略<br><br>
行首的空格缩进数量代表数据的层级<br><br>
object1:<br><br>
key1: false<br><br>
object2:<br><br>
key2: 3.14<br><br>
key3: 0xdeadbeef<br><br>
nestedObject:<br><br>
key4: 'quoted string'<br><br>
以连字符 + 空格开头，表示数组元素<br><br>
- 42<br><br>
- "double-quoted string"<br><br>
// 最终解析效果如下：<br><br>
&#123;[42, "double-quoted string"]&#125;<br><br>
YAML 中可以通过 & 定锚点，* 来引用<br><br>
object1: &o1<br><br>
key1: value1<br><br>
object2:<br><br>
key2: value2<br><br>
key3: *o1<br><br>
// 最终解析出来效果如下：<br><br>
&#123;<br><br>
"object1": &#123;<br><br>
"key1": "value1"<br><br>
&#125;,<br><br>
"object2": &#123;<br><br>
"key2": "value2",<br><br>
"key3": &#123;<br><br>
"key1": "value1"<br><br>
&#125;<br><br>
&#125;<br><br>
&#125;<br><br>
<< 表示追加，类似继承<br><br>
object1: &o1<br><br>
key1: value1<br><br>
key2: value2<br><br>
object2:<br><br>
<<: *o1<br><br>
key3: value3<br><br>
// 最终解析效果如下：<br><br>
&#123;<br><br>
"object1": &#123;<br><br>
"key1": "value1",<br><br>
"key2": "value2"<br><br>
&#125;,<br><br>
"object2": &#123;<br><br>
"key1": "value1",<br><br>
"key2": "value2",<br><br>
"key3": "value3"<br><br>
&#125;<br><br>
&#125;<br><br>
以上部分仅罗列出 Cocos Effect 开发中常见的写法，更多写法请参考 YAML 官网。<br><br><strong><font color="#de5650">Cocos Effect 写法</font></strong><br><br>
Cocos Effect 主要由两部分构成：<br><br>
一个是由 CCEffect 包裹的用 YAML 格式编辑的渲染流程清单。这里罗列的内容主要涉及到与编辑器交互（供开发者在编辑器中进行数据调整）以及与 CCProgram 的数据交互。CCEffect 的核心是 Technique 渲染技术。<br><br>
◇ Technique 渲染技术代表完成一个最终效果的方案。一个方案可以由一个或者多个 Pass 融合完成。<br><br>
◇ 一个  Pass 就是一次 GPU 绘制，一般包括一次顶点着色器和片元着色器。<br><br>
◇ 每个顶点/片元着色器都要申明各自的入口函数并提供返回值，此处入口函数的返回值会提供给运行平台的入口函数。<br><br>
另一个是由 CCProgram 包裹的基于 GLSL 300es 格式的着色器（shader）片段。<br><br>
如果要绘制在文章开头的目标矩形，内容可以如下：<br><br>
CCEffect %&#123;<br><br>
techniques:<br><br>
- name: opaque<br><br>
passes:<br><br>
- vert: unlit-vs:vert #此处的 vert 对应 CCProgram 的 vert，指向渲染平台的入口函数。例如：WebGL 就是 main 函数。<br><br>
frag: unlit-fs:frag<br><br>
&#125;%<br><br>
CCProgram unlit-vs %&#123;<br><br>
precision highp float;<br><br>
in vec4 a_position;<br><br>
in vec4 a_color;<br><br>
out vec4 v_color;<br><br>
vec4 vert () &#123;<br><br>
v_color = a_color;<br><br>
return a_position;<br><br>
&#125;<br><br>
&#125;%<br><br>
CCProgram unlit-fs %&#123;<br><br>
precision highp float;<br><br>
in vec4 v_color;<br><br>
vec4 frag () &#123;<br><br>
return v_color;<br><br>
&#125;<br><br>
&#125;%<br><br>
>注意：Cocos Creator 采用的是 GLSL es300 格式来编写 Shader 片段。因此，后续所有的输入输出都使用 “in”、“out” 关键字而非旧版的 “attribute” 和 “varing”。当然，如果想继续使用，仍然兼容。<br><br>
Graphics 组件在绘图的时候，也采用了为自己量身定做的 Shader，这个在 Graphics.ts 内有迹可循。采用的是内置的 builtin-graphics。可以在 <strong>资源管理器面板->internal->effects </strong>下找到。它的内容如下：<br><br>
CCEffect %&#123;<br><br>
techniques:<br><br>
- passes:<br><br>
# 确定顶点和片元着色器。指向的是 CCProgram 定义的着色器。<br><br>
- vert: vs:vert<br><br>
frag: fs:frag<br><br>
# blendState、rasterizerState 和 depthStencilState 是与测试与混合有关，可以暂时忽略<br><br>
# 此处设置的原因是因为引擎内提供一套默认的测试与混合配置，但是在 2D 上由于当前设计暂时不需要深度，因此，需要手动修改相关配置<br><br>
blendState:<br><br>
targets:<br><br>
- blend: true<br><br>
blendSrc: one<br><br>
blendDst: one_minus_src_alpha<br><br>
blendSrcAlpha: one<br><br>
blendDstAlpha: one_minus_src_alpha<br><br>
rasterizerState:<br><br>
cullMode: none<br><br>
depthStencilState:<br><br>
depthTest: false<br><br>
depthWrite: false<br><br>
&#125;%<br><br>
CCProgram vs %&#123;<br><br>
// 顶点着色器内所有浮点数精度定义<br><br>
precision highp float;<br><br>
// 引入 Creator 3.x 提供的代码片段<br><br>
// cc-global 提供了投影矩阵和观察矩阵<br><br>
#include <cc-global><br><br>
// cc-local 提供了模型矩阵<br><br>
#include <cc-local><br><br>
// 定义需要输入的三个顶点属性数据 a_position，a_color 和 a_dist。其中，a_dist 是为了抗锯齿功能所需提供，可不用关心。<br><br>
in vec3 a_position;<br><br>
in vec4 a_color;<br><br>
out vec4 v_color;<br><br>
in float a_dist;<br><br>
out float v_dist;<br><br>
// 提供最终需要传给顶点着色器 main 函数的数据值<br><br>
vec4 vert () &#123;<br><br>
vec4 pos = vec4(a_position, 1);<br><br>
// 将模型坐标转换成裁剪坐标<br><br>
pos = cc_matViewProj * cc_matWorld * pos;<br><br>
v_color = a_color;<br><br>
v_dist = a_dist;<br><br>
return pos;<br><br>
&#125;<br><br>
&#125;%<br><br>
CCProgram fs %&#123;<br><br>
// 低版本处理方案，可不用关心。<br><br>
#pragma extension([GL_OES_standard_derivatives, __VERSION__ < 300])<br><br>
precision highp float;<br><br>
in vec4 v_color;<br><br>
in float v_dist;<br><br>
// 提供最终需要传给片元着色器 main 函数的数据值<br><br>
vec4 frag () &#123;<br><br>
vec4 o = v_color;<br><br>
// 此处也可不用关心<br><br>
#if __VERSION__ < 300<br><br>
#ifdef GL_OES_standard_derivatives<br><br>
float aa = fwidth(v_dist);<br><br>
#else<br><br>
float aa = 0.05;<br><br>
#endif<br><br>
#else<br><br>
float aa = fwidth(v_dist);<br><br>
#endif<br><br>
float alpha = 1. - smoothstep(-aa, 0., abs(v_dist) - 1.0);<br><br>
o.rgb *= o.a;<br><br>
o *= alpha;<br><br>
return o;<br><br>
&#125;<br><br>
&#125;%<br><br>
上下一对比，我们所需要的部分跟上方绘制矩形所需内容就差不多重合了。只是多了一层模型坐标到裁剪坐标的转换。<br><br>
最后，这里还差最后一部分内容，就是关于相机。当我们创建 Canvas 节点的时候，可以看到默认会创建出一个 Camera 节点，Camera 节点上的 Camera 组件持有 ClearFlags，ClearColor 以及 Rect 这三个属性，在 WebGL 就分别控制了 gl.viewport、gl.clear 和 gl.clearColor 部分。其中：<br><br>
ClearFlags 的 SOLID_COLOR 模式，要求每帧清除屏幕内容<br><br>
ClearColor 要求清除屏幕内容后默认填充什么颜色<br><br>
Rect 定义屏幕空间视口，xy 值限制在 -1～1，wh 值限制在 0～1<br><br>
到此为止，我们大致了解了一个基础绘图组件 Graphics 的顶点数据的获取途径以及它的 Shader 内容。<strong>下一章，我们来分析一下在基础绘图 Shader 基础上添加了纹理贴图处理的 2D 渲染组件 Sprite，并对它进行一些改造。</strong><br><br><strong><font color="#de5650">扩展知识</font></strong><br><br>
所有场景里的对象都必须在相机的可视区域内，才能被最终渲染出来。相机的可视条件分为两部分：<br><br>
条件一：相机的 Visibility 包含节点的 Layer 值。比如：2D 相机的 Visibility 包含 UI_3D 和 UI_2D，节点的 layer 为 DEFAULT，那么此节点就无法被 2D 相机渲染。<br><br>
条件二：在条件一满足的情况下，物体需要在相机照射的视距框内，物体才可被渲染。<br><br>
最终，所有的内容经过渲染管线的处理成为一个“拍扁”后的 2D 像素。此时不代表最终呈现的就是这样的 2D 像素，最后一个阶段是 viewport。假设，此时将相机 Rect 的 w 分量改为 0.5，可以看看前后渲染内容的对比：<br><br><div align="center">
<img id="aimg_1015120" aid="1015120" zoomfile="https://di.gameres.com/attachment/forum/202110/15/140834ke1xdy0gg8do0gx3.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/140834ke1xdy0gg8do0gx3.jpg" width="596" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/140834ke1xdy0gg8do0gx3.jpg" referrerpolicy="no-referrer">
</div>
<br>
可以清楚的看到由于视口的调整，只有左半边屏幕能够呈现内容，因此，只有以相机原点为中心所照射的一半内容被呈现了出来。<br><br><font size="2"></font><br><font size="2">来源：COCOS</font><br><font size="2">原文：https://mp.weixin.qq.com/s/K2jlmFgt1HLYN-B3jtroHA</font><br><br><br>
</td></tr></tbody></table>


  
</div>
            