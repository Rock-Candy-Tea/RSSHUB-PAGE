
---
title: 'VR视觉显示大提升，NVIDIA VRSS 2全解析'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210415/v2_35541f76e1d142d784d4c8cb8a2cf6b8_img_000'
author: 36kr
comments: false
date: Thu, 15 Apr 2021 11:56:41 GMT
thumbnail: 'https://img.36krcdn.com/20210415/v2_35541f76e1d142d784d4c8cb8a2cf6b8_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/UbCJdaSJ99MJpYnmiPTR3g">“青亭网”（ID:qingtinwang）</a>，作者：前沿科技新媒体，编辑：hi188，36氪经授权发布。</p> 
<p>NVIDIA近两年真的是有点科技大爆炸的意思，显卡性能不断提高，对应在软件和AI整合方面同步在加速。尤其是以：光线追踪、DLSS、VRS和VRSS，大幅在提升画面质量，而且VRSS就是面向VR/AR领域。</p> 
<p>今年的GTC大会，NVIDIA宣布了升级版的VRSS 2，特点就是融合眼球追踪数据，真正实现动态注视区超采样渲染，实现了更符合人类视觉效果、高质量画面。而去年VRSS时仅支持固定中心区域超采样，虽然能满足大部分当下VR头显运行需求，没有眼球追踪数据的VRSS是没有灵魂的，VRSS 2就这么来了。</p> 
<h2>1，VRS是什么</h2> 
<p>VRSS（Variable Rate Supersampling，可变速率超级采样）是NVIDIA在自家显卡AI软件能力的其中之一，其基于VRS（Variable Rate Shading，可变着色率）技术。</p> 
<p>VRS是<a class="project-link" data-id="577369" data-name="图灵" data-logo="https://img.36krcdn.com/20210409/v2_11e43e11c55a435487a730ae43e4cafc_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4781700122" target="_blank">图灵</a>架构引入的新技术，它的目标是的通过更低的功耗实现同等画面效果，或通过同等功耗实现更好的画面效果。</p> 
<p>它的原理是，将着色率和单像素区分开，VRS下可对一大块像素统一进行着色。例如下图，原来是1×1的像素着色，现在可以进行2×2，4×4，2×1，1×2，2×4，4×2，共7种着色方式，这样就可以将原本16次的着色降低为1次，大幅降低GPU算力。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_35541f76e1d142d784d4c8cb8a2cf6b8_img_000" data-img-size-val="800,289" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>VRS原理示意图</p> 
<p>具体来说，应用到游戏中可以将一副画面的不同区域进行划分区域的着色，就像上图中赛车游戏整体画面进行分割。将中间蓝色区域进行1×1渲染，两侧绿色区域进行2×2渲染，红色次要区域进行4×4渲染，不同画面区域灵活的选择渲染方式。</p> 
<p>因为VRS仅适用于Turing架构的显卡，因此VRSS也同样如此，仅适用于RTX系列显卡。</p> 
<h2>2，VRSS又是什么</h2> 
<p>了解了VRS特性之后，相信很多小伙伴都会发现，VRS非常适合于人眼的自然特征，将人眼目光注视区域重点渲染，周围区域次要渲染。</p> 
<p>为此，专注为VR提供更佳显示能力的VRSS技术诞生，它基于VRS，特点是：拥有最高8倍的超采样方案，从而提供更好的视觉效果。同时，还提供划分区域的动态渲染的VRS功能。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_478526e50fc84c289b186bd011743080_img_000" data-img-size-val="800,449" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>2020年VRSS，固定中心区域超采样示意图</p> 
<p>在去年初CES上，VRSS首次发布时其仅支持固定中心区域的超采样显示，原因很简单，因为这是人们使用VR的主要视觉区域，这样也考虑到硬件性能，因为还需要保证给VR提供90帧的稳定画面。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_5038e60d27fb41659d746cbf7a8a871e_img_000" data-img-size-val="800,571" referrerpolicy="no-referrer"></p> 
<p>当时NVIDIA测试数据时，在《Boneworks中》游戏中，基于RTX 2080 Ti显卡，结合VRSS可以稳定在90帧，但如果不开启VRSS使用全屏4倍超采样，画面根据图中来看也就是75帧左右的水平。</p> 
<p>可见，VRSS技术可以为PC VR游戏提供更好的观感，让画面细节更丰富，例如在阅读场景。</p> 
<p>另一个重要的因素是，考虑到很多开发者在VRS API中遇到各种各样的问题。VRSS无需依赖API，只需在NVIDIA驱动中就能打开，这对开发者和玩家来说也更加便利。</p> 
<h2>3，VRSS 2提升在哪</h2> 
<p>前面提到，VRSS特点是只能提供固定的中心区域8倍超采样，虽然这足够满足目前绝大多数VR头显，甚至Quest 2这类移动设备也在采用类似的技术方案来平衡功耗。考虑到眼球追踪技术在VR中的加速，尤其是下一代Quest、或苹果的MR头显，很可能将眼球追踪作为重要的交互技术。</p> 
<p>实际上，很多的商用PC VR已经配备眼球追踪技术，例如Varjo、HTC Vive Pro Eye、刚刚发布的<a class="project-link" data-id="139938" data-name="惠普" data-logo="https://img.36krcdn.com/20200729/v2_fa9f5d981bf94a7782774ab7e73a6749_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/139938" target="_blank">惠普</a>Reverb G2 Omnicept等等。</p> 
<p>因此，VRSS 2的目标是深入结合眼球追踪技术。据<a class="project-link" data-id="82712" data-name="青亭网" data-logo="https://img.36krcdn.com/20210409/v2_e5f9feddd0684609a3453e04d5de1e2f_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4589001214" target="_blank">青亭网</a>了解，VRSS 2中的眼球追踪技术，是NVIDIA和Tobii联合研发，并且结合动态注<a class="project-link" data-id="32556" data-name="视点" data-logo="https://img.36krcdn.com/20200729/v2_89076d3e435d4aae9552d8e3e9c30593_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/32556" target="_blank">视点</a>渲染，从而在充分利用硬件的同时还提供更逼真的视觉观感。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_ba6236ffd1d647dc8899713a1c53110e_img_000" data-img-size-val="400,263" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>VRSS 2眼球追踪超采样示意图</p> 
<p>这样一来，VRSS 1中的中间固定8倍渲染则变成了动态眼球注视区域的8倍渲染，如上图蓝色区域。</p> 
<p>VRSS 2虽好，但是也有一些限制，硬件上目前仅支持Tobii的眼球追踪VR设备，似乎将其它眼球追踪方案商产品一棒子打死。据悉，首款支持NVIDIA VRSS 2的是惠普G2 Omnicept，后续可能会支持更多VR头显。</p> 
<p>在NVIDIA驱动中VRSS选项共有两个，自适应模式和始终开启模式。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_e81051e16f694a56b6e6102e7cee6553_img_000" data-img-size-val="300,178" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>VRSS 2自适应模式</p> 
<p>自适应模式：该模式会结合硬件性能，在不影响VR体验前提下将超采样区域最大化，也就是将超采样区域和周围区域的GPU利用率进行动态平衡，如上图绿色区域。</p> 
<p>始终开启模式：不考虑硬件性能，直接以设定好的范围进行8倍超采样，提供最大化的视觉效果。同时，该模式下可能会带来丢帧等情况。</p> 
<p>对于开发者来说，每款支持VRSS的应用需要向NVIDIA提交进行验证，批准后才会在NVIDIA驱动中显示出来。目前，经过验证的VRSS应用共计30款，不乏热门的《Pavlov VR》《VRChat》《 Boneworks》《Onward VR》等。</p> 
<p>当然，NVIDIA在AI技术方面还有DLSS技术，如果将VRSS与DLSS结合，那么在在视觉观感上<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>大幅升级，尤其是在未来超高分辨率的VR头显趋势下。</p> 
<p>参考：</p> 
<p>https://developer.nvidia.com/blog/delivering-dynamic-foveated-rendering-with-nvidia-vrss-2/</p>  
</div>
            