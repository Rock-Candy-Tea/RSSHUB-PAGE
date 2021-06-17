
---
title: '3D AR特效如何在相机中无缝应用'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qWZFWguVSvXzIPnLkOk3.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 17 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qWZFWguVSvXzIPnLkOk3.jpg'
---

<div>   
<blockquote><p>编辑导语：设计没有思路，3D AR特效不会应用在相机中？作者分享了自己将3D AR特效应用在相机中的做法，我们一起来看下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4720624 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/qWZFWguVSvXzIPnLkOk3.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>为迎接牛年春节，给大家带来新年的祝福和欢乐，我们围绕关键词“牛”设计了一系列针对QQ相机业务相关的玩法滤镜，包括“牛转乾坤”、“牛气冲天”、“牛势已到”、“招财童子吐福字”等等，以创新的互动能力为QQ用户提供新奇的玩法体验和情感表达。</p>
<p>其中：</p>
<ul>
<li>“牛转乾坤”以3D变脸技术为基础，让用户能从普通人脸变成牛脸，酷炫的风格配上节奏感极强的音乐，给用户带来新奇感。</li>
<li>“牛气冲天”则是以互动游戏的形式，让玩家在游戏中通过收集各种氛围元素不断积攒牛气，获得更高的牛气值和更厉害的称号，享受不断刷分带来的乐趣。</li>
<li>“牛势已到”则尝试以脸部为驱动，配合脸部表情驱动模型产生变化以及左右摇摆带来的物理随动效果，配合一些春节氛围元素，趣味十足。</li>
<li>“招财童子吐祝福”则结合了中国传统民俗，以拜年送祝福的形式，福气又添财等等。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/TZjx58JH5Qqk7WMcDT8w.gif" alt referrerpolicy="no-referrer"></p>
<p>项目中攻克了不少问题难点，篇幅有限，本文仅以“牛势已到”的设计制作过程，和大家分享下设计背后的故事。抛砖引玉，希望和大家学习交流。</p>
<section></section>
<h2 id="toc-1">一、问题攻坚，剥开盲区</h2>
<p>对我们设计团队来说，这次的玩法设计中涉及到很多以前较少接触的技术领域，比如将3DMM、Blendshape、AR、多段3D动画合并与触发，面部识别等多能力复合应用的体验把握、效果和性能控制，这对我们设计团队来说是一次不小的挑战。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/2ciswgOetXumyZ1eYL8J.png" alt width="740" height="498" referrerpolicy="no-referrer"></p>
<p>本次的美术制作管线（Art Pipeline）需要结合不同DCC工具制作不同阶段的美术资源，然后还要在新版工具完成配置，这与常见的游戏制作流程有很大不同。</p>
<p>多能力复合应用不仅带来了新的摸索成本，在技术落地上也带来实际的困难，不少技术黑盒的存在使得在效果还原的过程中不断踩坑。</p>
<p>因为标准的不确定性，导致对于模型的面数，比例，贴图，动画长度等等存在很多的未知难点。</p>
<h2 id="toc-2">二、流程探索，高效落地</h2>
<p>虽然存在很多的不确定性，但有挑战才有突破的机会。我们尝试借鉴常见的3D游戏制作流程，边推进边调整。</p>
<h3>1. 玩法设定</h3>
<p>因为是基于QQ相机的AR玩法，所以我们将整体交互设定为以用户的脸为主体，当引擎识别出用户的脸后，可以将引擎中的模型脸与用户的脸相匹配，然后用户可以通过头的摇晃和面部表情驱动模型变化。</p>
<h3>2. 风格设定</h3>
<p>在这个玩法中，由于是以虚拟形象结合玩家的脸部作为游戏主角，所以关于主角的风格设定尤为关键。为找到想要的春节氛围，前期搜集了很多春节相关的参考，主要有2个方向。</p>
<p>方案A的方向是通用的春节的喜庆元素，关键词：财神、红包、福袋、春节、牛年、Q萌。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NvLTULJ8bUcsEDHsgZIw.png" alt width="824" height="464" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片来源于网络</p>
<p>方案B的方向是更加本土和有特色的文化，关键词：国潮、陕北外套、腰鼓、喜庆、牛年头套、春节。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/h4v4U9KyjQPeTHNBT5gk.png" alt width="839" height="483" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片来源于网络</p>
<p style="text-align: left;">从关键词和灵感图中，我们创作了2个版本的原画概念方案。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/lmIMcuoH36s6UkUGuPdv.jpeg" alt width="853" height="375" referrerpolicy="no-referrer"></p>
<p>经过讨论，确定以方案A为最终形象设定，原因是方案A更加符合用户对春节的期望：化身财神，小孩子的形象也比较有亲切感。因为头部到时候会替换用户的脸，所以这里不需要设计角色的脸部造型。</p>
<h3>3. 3D模型设计</h3>
<p>有了明确的2D形象设计后，接下来要做的工作就是把它转化成3D模型，最终的模型设计因为要平衡好性能和品质，相比于2D设计，3D设计流程显得复杂很多。这里的关键步骤有以下几点：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/UrJKh6cobSx8AnoX1fr3.png" alt width="740" height="479" referrerpolicy="no-referrer"></p>
<p><strong>（1）中模设计</strong></p>
<p>先根据原画设定做好中模设计，这一步主要是确认模型的基本造型，便于沟通和调整。</p>
<p>这个阶段可以先不考虑小细节，比如衣服褶皱那些可以在高模中雕刻。当然，也可以根据3D模型的具体情况在2D原画的基础上做一些适当设计发挥。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/HM0kKjIDMO4p4QtD5rGP.jpeg" alt width="736" height="326" referrerpolicy="no-referrer"></p>
<p><strong>（2）雕刻高模</strong></p>
<p>确定中模的结构后，接下来就需要完成高模的设计。有些人可能觉得好奇，最终用到模型资源是低模，那为什么还要做高模呢？</p>
<p>其实，高模的作用就是为低模而准备的。通过高模烘焙出法线贴图，AO贴图，金属度贴图等等纹理贴图，能够让低模也拥有高模的细节，这样做的原因主要是为了降低性能消耗。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/xkAR4QW60AVJ4V8VnrGJ.png" alt width="759" height="372" referrerpolicy="no-referrer"></p>
<p>精度要求不高的模型在非专业雕刻软件中，比如C4D中就能完成雕刻，而精细度更高的高模则需要到专业的雕刻软件，比如Zbrush中雕刻会更加方便。</p>
<p>雕刻要注意把细节雕刻的足够明显，甚至可以夸张一些，目的是为了在烘焙后能得到更多细节的贴图。</p>
<p>这样最终烘焙出来的贴图才能方便调整，比如效果太强可以适当减弱，但如果效果太弱是没法再增加细节的。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Vuv1XxbgfRgOhHTmzFrI.gif" alt width="748" height="595" referrerpolicy="no-referrer"></p>
<p><strong>（3）拓扑低模</strong></p>
<p>高模的面数一般会非常多，考虑性能问题，一般来说是不能最终使用的，这个时候还需要对模型进行拓扑，也就是重新布线。</p>
<p>拓扑的作用是优化布线，减少面数，而优化好的布线也更方便拆UV。这里面有2个需要注意的地方：</p>
<ul>
<li>保持面片，不通过挤压做出封闭厚度。需要做厚度的地方，用面片弯曲来实现。</li>
<li>用点多的高模来做（可以通过加细分来得到更多点的模型），精度更高的模型会更加方便吸附选择，这样最终得到的布线可以更加规则。</li>
</ul>
<p><strong>（4）拆UV</strong></p>
<p>这里一般建议用更加专业的拆UV工具来做，比如Uvlayout ，Maya等，不建议用C4D直接拆UV。</p>
<p>我这里由于是在C4D中做的模型，所以通过在C4D中整理好模型导出.fbx文件，导入Maya中进行拆分，然后再导出拆分好UV的.fbx文件来画贴图。</p>
<p>注意将单个部件拆分在一个完整区域中，会更方便定位。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tNVSC9ZRf2ucq6tNPxcU.png" alt width="788" height="471" referrerpolicy="no-referrer"></p>
<p><strong>（5）画贴图</strong></p>
<p>把拆分好的.fbx导入到SP，然后在SP中进行比较细致的纹理设计。</p>
<p>如果对这个软件不熟悉，也可以在C4D中简单画一些贴图大概范围，然后在Ps里细化贴图。</p>
<p>当然，用SP的好处就是可以烘焙出非常多的细节贴图，主要用到的贴图包括Diffuse、Normal、Metallic、Roughness方便后续使用。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/XljrE78lsHKbTbQokIzu.png" alt width="821" height="559" referrerpolicy="no-referrer"></p>
<p><strong>（6）烘焙</strong></p>
<p>确定好贴图后，通过SP可以将各种需要的贴图烘焙出来，用到最终的低模上。烘焙的时候需要注意，低模和高模中的Mesh命名要一一对应。</p>
<p>烘焙出来的贴图可能有问题，如出现破裂，可以用Ps的内容识别工具进行修复，主要修复法线贴图上过渡比较锐利的地方。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/jOkoU5zD1IL1VeSJzCvk.png" alt width="790" height="448" referrerpolicy="no-referrer"></p>
<p><strong>（7）确定最终模型效果</strong></p>
<p>贴图制作完成后，可以得到最终的静态渲染效果。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/eYnUqLz9i5p58cTKbhAP.jpeg" alt width="793" height="572" referrerpolicy="no-referrer"></p>
<h3>4. 骨骼绑定</h3>
<p>模型和UV确定后，接下来需要进行骨骼绑定和权重分配。</p>
<p>因为后续需要在引擎中加上物理随动效果，所以这里的绑定规范会跟常规的3D动画绑定要求有所不同，它要求哪里需要产生动画就要将骨骼顶点添加到Mesh的末端点，以获得更加精确的模型控制。</p>
<p>所以，在实时3D内容的设计中，仅靠权重控制不能做到足够灵敏。至于绑定的工具，用自己熟悉的软件即可，比如C4D，Maya ，Blender等等。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/plQUyzJKbX0yExIDJw0h.png" alt width="812" height="507" referrerpolicy="no-referrer"></p>
<h3>5. 动画设定</h3>
<p>在这次的项目中，需要做多达5段的动画，其难点在于，这套多段动画会分为循环动画、非循环动画，其中拆分开的循环动画，需要首尾完全相同，并又能准确衔接到下一个动画。</p>
<p>这又是与3D动画设计不同的地方，对动画节奏提出了更高的要求。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/DEBY1VyjomjdCimIPoUP.png" alt width="775" height="481" referrerpolicy="no-referrer"></p>
<p>为了提升沟通效率，向开发说明这里的动画逻辑，制作了一张动画时间线图。</p>
<p>最终把动画拆分成5段进行输出：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/yXtGPDe5RAsVTdMRqnTP.gif" alt width="794" height="238" referrerpolicy="no-referrer"></p>
<p>而为了实现这样一套复杂的动画内容，经过了反复的测试，我们使用Blender导出最终的多段动画，实现了复杂逻辑控制。</p>
<p>这里会选择使用Blender输出，主要原因是Blender的动画规则更符合引擎的读取需要，效果更加接近引擎中的实际效果，便于测试。</p>
<p>因为需要多DCC工具的配合，在不断导入导出的过程中出现了各种疑难杂症。这里面有几个点尤其需要注意：</p>
<p>（1） 要用正确的Blender版本进行动画合成输出，Blender版本问题会产生各种bug。这里建议用Blender 2.8 版本进行动画输出，兼容性更高，导出错误率较低。想要更方便导出.glb动画格式，也建议大家尝试用Maya+Babylon插件。</p>
<p>其中有个细节需要注意下，Blender2.9软件操作更加便捷，但输出动画时，skin值会丢失，导致动画运行不正常，暂时只能通过换到更低的2.8版本来解决。</p>
<p>（2）在导入Blender前，需要在C4D中把除了骨骼动画外的所有动画轨道全部删除清理，这样导入Blender中的动画轨道才是最干净好处理的。</p>
<h3>6. 氛围细节</h3>
<p>因为画面是以脸部运动为驱动的，所以模型会在整个屏幕产生移动，为了让画面更加合理，即人物不可能是没理由的漂浮在空中，所以给人物增加了站在云上面的设定。</p>
<p>为了强化春节氛围，还增加了元宝和春联的装饰元素。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/odrJ6T6xgRco4biyDbGg.png" alt width="769" height="515" referrerpolicy="no-referrer"></p>
<p>并结合用户的面部表情触发，设计了触发前后的状态变化给用户带来惊喜，提升可玩性。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/adCzrb464aMVm4z4EnnC.png" alt width="747" height="461" referrerpolicy="no-referrer"></p>
<h3>7. 背景音乐</h3>
<p>同时，增加了背景音乐，这里面有个小细节点是结合了人物面部表情对音乐进行卡点。当用户张嘴的时候，音乐也会同步变化，会模仿画面喊出“财神到！”，带动用户一起互动。</p>
<p>同时也用C4D+AE制作了完整的玩法Demo，便于开发做效果还原。</p>
<h3>8. 性能问题</h3>
<p>做3D内容设计相较于做3D动画设计，会有更多的技术性的思考，性能就是一个重点。</p>
<p>做动画设计时，怎么好看就可以怎么来，但对于实时交互的3D效果来说，因为最终是需要在手机QQ中上线，需要兼容到各种不同的机型，所以我们对于资源包要求非常苛刻，需要做很多美术效果的平衡。</p>
<p>整个的优化思路包括以下几点：</p>
<ul>
<li>当前期做完减面后，依然发现性能不符合要求需要减面时，可以利用Blender的减面修改器进行减面。利用这个修改器做减面对模型效果影响比较小，又能快速实现减面能力，非常方便。</li>
<li>经过测试发现整体性能消耗上，动画带来的顶点变换产生的性能开销最大，所以要平衡好动画元素。做性能优化时，可以考虑从小动画上入手，去掉一些不太能注意到的小骨骼动画，减少顶点变换量，从而提升性能。</li>
<li>优化贴图大小，合并贴图。贴图存储的不单是颜色，还包含了各种信息，例如各种黑白图，能改变粗糙度，金属度等等。所以可以将贴图利用不同通道的方式合并到一张图中，缩小贴图的文件大小。</li>
</ul>
<p>以最好机型为基础，做出性能允许的最佳资源，以这个标准效果向下兼容，打包出几个性能区段的素材包，包括：</p>
<ul>
<li>动画+物理随动，高端机型</li>
<li>只有少部分动画，中端机型</li>
<li>没动画，没物理随动，低端机型</li>
</ul>
<h3>9. 上线效果</h3>
<p>最后，经过复杂的引擎配置流程，材质调整，平衡了一部分效果后最终得以上线，这是最终上线后的效果，可以在QQ相机中进行体验。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/joEhISAIlsfD9RJ6puyE.gif" alt width="645" height="375" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、规范梳理，反思沉淀</h2>
<p>在这个项目中遇到很多的难题，为了让后续类似玩法能够更好的推进，也对整个项目中需要注意的事项和制作输出规范进行了沉淀，形成了规范文档。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/AIoeR9lU0EYkgx40rnwb.png" alt width="679" height="405" referrerpolicy="no-referrer"></p>
<p>项目上线后，我们也进行了反思，从3D动画设计到实时3D内容设计需要做一定的思维转换，比如一开始就需要评估清楚玩法和用户使用时的真实场景，不止步与静态渲染。</p>
<p>这个玩法主要是应用在用户自拍的过程中，那么用户拍摄的范围多半只能是上半身，想要让用户体验到完整的模型资源，在人物的比例上，可以优化为头身比为1:1，头套可以比身体稍大一些，会显得更加可爱。</p>
<p>拓扑可以做的更加精致一些，在主要部位上的面数可以适当多一些，非重要的元素，面数可以更少，减面也需要差异化处理。</p>
<p>当时留的时间比较紧张，没有做太细致得贴图。后续如果继续做好的话，模型上的重点展示区域贴图可以做的更加细致一些，提高品质的同时也提升了效率。</p>
<p>实时3D内容相比动画，也更注重互动性，比如拍摄比例，张嘴互动、骨骼反馈的灵敏度等等，这些都是与3D动画渲染所不同的地方。</p>
<p>在落地的过程中，还会有比较多技术项的思考，比如减面优化、适配降级、对接引擎过程中的各种疑难问题解决等等。</p>
<h2 id="toc-4">四、挑战与机遇，未来可期</h2>
<p>对于设计师来说，这次项目挑战不小，同时也收获颇丰。</p>
<p>从0-1的过程中，熟悉了非常多以前不常接触的技术流程，比如模型雕刻、贴图烘焙、骨骼绑定、权重分配、多段动画的合并、多DCC工具的配合等等。</p>
<p>这些技术点的学习，为后续的项目提供了经验支撑。有挑战才能有进步，跳出自己的舒适区，才能成长的更快。</p>
<p>对于未来，基于多动画，物理随动的玩法能力，也可以应用到更多的创意玩法中，比如与脸部驱动，身体随动之类玩法，都能以这次的项目探索作为经验沉淀而快速复用，值得期待。</p>
<p>最后，想体验文中所说的玩法，可以在QQ相机中找到这些滤镜，操作路径是：打开QQ聊天窗口——找到相机选择右下角的表情图标——选择最新选项——下滑找到“牛势已到”，点击即可玩起来。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/5dDVDaJBl5j2U6J4p20Y.jpeg" alt width="764" height="482" referrerpolicy="no-referrer"></p>
<p> </p>
<p>本文由 @腾讯ISUX 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4719764" data-author="818930" data-avatar="http://image.woshipm.com/wp-files/2019/11/wp2UyWymZgi2Ym8SVyQ2.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            