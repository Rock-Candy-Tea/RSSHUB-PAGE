
---
title: 'OLED屏为了延长使用寿命牺牲了什么？一文看懂'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60ea756f8e9f096bf83d5918_1024.jpg'
author: ZAKER
comments: false
date: Sat, 10 Jul 2021 22:07:38 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60ea756f8e9f096bf83d5918_1024.jpg'
---

<div>   
<p>随着前段时间新品 SwitchOLED 的发布，舆论的风口再次集中到 OLED 屏幕上，尤其针对低分辨率 / 低像素密度情况下 OLED 屏幕的观感体验问题。</p><p>究竟同尺寸同分辨率 OLED 等于 70% 或三分之二 LCD 的结论从何而来，饱受诟病的模糊、彩边、颗粒感等等显示问题在像素级微观层面上又如何解释，这些问题都要从有机自发光材料的使用寿命说起。</p><p>OLED 屏固然有高色域、高对比度、快速响应时间、广可视角度、较好的能耗表现等等优点，不过也有使用寿命短、易烧屏、（相对）不清晰、显示文字效果差等问题，都是老生常谈的内容。</p><p>但你可知其实以上问题归根结底都来自 OLED 的技术根源——有机自发光材料的寿命问题，并且其中一些还是技术人员为了改善使用寿命而采用的新技术带来的负面影响，即子像素的排列方式问题。</p><p>早期 OLED 屏采用与 LCD 类似的标准 RGB 排列方式，但经过测试发现同样面积大小的红绿蓝三色子像素的使用寿命并不相同。</p><p>一旦其中的一种或两种子像素 ( 一般是红蓝 ) 发光性能快速损耗，就会使得正常的显示内容发生严重色偏，甚至由损耗区域组成某种图形，这就是烧屏现象。</p><p>由于 OLED 的原理，烧屏现象尚且不是能够完全解决的问题，只能靠各种软硬件优化缓解，延长其使用寿命。</p><p>软件优化方案例如像素抖动、动态屏保、定时熄屏等，都是为了确保不在一些固定的像素区域进行高强度、长时间的显示，或直接熄屏以此降低损耗；硬件优化方案就是对前文提到的子像素排列方案优化。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202107/60ea756f8e9f096bf83d5918_1024.jpg" data-height="229" data-width="493" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60ea756f8e9f096bf83d5918_1024.jpg" referrerpolicy="no-referrer"></div></div>既然在传统同面积方案下注意到红蓝色子像素的损耗更快，自然能想到增大这两种像素面积，通过这种方式平衡三色使用寿命，由此诞生了 RGBPentile 排列，简称 P 排。<p></p><p>这种排列方式对比标准 RGB 不光增大了红蓝子像素面积，而且相邻的每三个绿色子像素都会共用其间的两个较大的红蓝像素并以此类推，考虑到需要三色才能组成一个完整的像素点。</p><p>可以说同宽度的 Pentile 排列与标准 RGB 排列相比减少了三分之一的像素点，这就是三分之二说法的由来。</p><p>在同样的现象上深入下去，我们会发现 Pentile 排列的横向和 45 度倾斜边缘必然存在这种子像素不完全的问题，它要么仅有红色和蓝色，要么仅有一整列绿色，倾斜情况下则是红绿或蓝绿的组合。</p><p>表现在文字和图形边缘的宏观视觉效果上就是彩边问题。有一部分厂商另辟蹊径，在共用红蓝像素的基础上修改排列方式，开发出将 RGB 三色子像素三角形排列的 Delta 排列，京东方还以此发展出继续拆分绿色子像素的 2in1 排列。</p><p>这种 Delta 排列方式虽然一定程度上解决了侧边缘彩边问题，不过共用红蓝子像素的程度愈发提高，等效分辨率可以说进一步下降了。</p><p>这是许多消费者难以接受的，所以 Delta 排列及其衍生品向来有不太好的风评，连带着对一些手机的销量口碑产生负面影响。</p><p>我们可以看到在这张图中还有 Pearl ( 珍珠 ) 排列和 Diamond ( 钻石 ) 排列，这两种排列方式大同小异，同样从对 P 排的改进中诞生。</p><p>特点在于将原有排列方式整体倾斜 45 度，同时重新布置绿色子像素位置使其相互错开分散在红色与蓝色子像素之间，减少了各种角度的彩边问题。</p><p>同时达到相对一般 Pentile 排列和各种 Delta 排列更好的视觉等效分辨率，虽说依然无法达到标准 RGB 排列的水平，不过结合同步发展的单个像素面积缩小和分辨率提高，已经接近肉眼难以辨识的程度。</p><p>钻石排列和珍珠排列这两者是目前最佳的 OLED 子像素排列方案，专利分别归属于三星与 TCL 华星光电。</p><p>细节设计上，三星 Diamond 排列将子像素形状定为菱形，而 TCL 华星 Pearl 排列将子像素形状改为弧形，进一步提升子像素开口率，即像素的有效透光区域占比，提升了使用寿命。</p><p>可以看出，当下国内外显示设备厂商在 OLED 面板上的 " 折腾 " 主要都是为了提升其使用寿命，但都仅能治标不能治本，同时不同程度地导致了分辨率等显示效果的损失。</p><p>对于一种面向市场和大众的电子设备，即使其性能再怎么优越，使用寿命以及衍生出的性价比问题都不可小视。</p><p>这是来自有机自发光材料的原罪，希望各大厂商能坚持攻关研发。</p><p>在保留 OLED 既有的较强色彩表现，高亮度和对比度等优秀素质的基础上，不断探索多种技术手段继续提升使用寿命，降低成本，让使用 OLED 屏的电视能够成为走入千家万户的普及性产品。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202107/60ea756f8e9f096bf83d5919_1024.jpg" data-height="337" data-width="600" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60ea756f8e9f096bf83d5919_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            