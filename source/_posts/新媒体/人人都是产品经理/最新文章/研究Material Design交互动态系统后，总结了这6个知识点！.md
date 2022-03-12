
---
title: '研究Material Design交互动态系统后，总结了这6个知识点！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/ZJWcmJwSpBZjuh4pmO9j.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 12 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/ZJWcmJwSpBZjuh4pmO9j.jpg'
---

<div>   
<blockquote><p>编辑导语：交互动效如果做得好，可以为产品赋能。这篇文章结合案例，系统梳理了交互动效设计的知识点，介绍了动效的作用和设计原则等，可以帮助大家更有说服力地和产品沟通，不妨来看看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-768248 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/ZJWcmJwSpBZjuh4pmO9j.jpg" alt referrerpolicy="no-referrer"></p>
<p>从设计的维度，动态设计可以分为交互动效和 Ae 动效，在这两方面个人都有相关落地项目。但是自己感觉学得不够系统，只是能做需求，做得还不够好，所以最近几天我都在学习研究 Material Design 交互动态系统规范。</p>
<p>从整体框架和细节入手，我结合日常业务设计思考总结了几点，输出了一套动效标注模板，希望对大家有帮助。</p>
<p>这次总结主要是分享交互动效的相关干货，方便自己沉淀设计经验，大纲如下：</p>
<ol>
<li>动效的作用</li>
<li>设计原则</li>
<li>持续时间</li>
<li>缓动曲线</li>
<li>动效风格</li>
<li>动效标注</li>
</ol>
<h2 id="toc-1"><span id="menu_0" class="auto_menu">一、动效的作用</span></h2>
<p>相信很多设计师在日常业务中都会主动挖掘机会点，来为产品增值赋能。机会点可以是交互动效，但是我们该怎样和产品同学沟通推动才更有说服力呢？如果只是说提升用户体验，说服力是很弱的。因此，我深度学习了 Material Design 动态系统规范，结合界面案例总结了几点作用：</p>
<h3>1. 使用更愉悦，微体验更好</h3>
<p>比如标签栏 tab 切换、下拉菜单出现，加入动效，符合现实场景动态，界面更加生动，还能缓解用户对内容的枯燥感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/NXon6f2pnfcMxSZcpCfl.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="300" height="300" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/Axi7kzRagjtVEXtsDXPT.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="300" height="300" referrerpolicy="no-referrer"></p>
<h3>2. 让不同界面的元素更具有关联性，易于理解层级</h3>
<p>比如收件箱消息列表和消息详情的转换，过渡流畅。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/IcL03ldo2ikh0pQnFvIX.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="600" height="379" referrerpolicy="no-referrer"></p>
<h3>3. 提供强提示的反馈和展示当前界面状态</h3>
<p>比如键盘输出完成，动画显示操作是否成功；列表占位符，加入动画表示正在加载中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/5gUUHyscaumQDlniWsDC.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="441" referrerpolicy="no-referrer"></p>
<h3>4. 教育用户，帮助用户了解如何操作</h3>
<p>比如滑动打开的手势动画，使操作行为易于理解。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/FJtuSmHXdnH3kUltGWyf.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="600" height="442" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、动效原则</h2>
<p>好的交互动效，会给人愉悦的心理感受。设计过程应当遵循以下几点原则：</p>
<p>（1）自然：在现实世界中，物体的速度会受到自身重量和摩擦力影响，不会突然运动，也不会突然停止，因此要使用缓动曲线，平稳过渡。</p>
<p>（2）及时反馈：动画持续时间适当，响应迅速，有助于用户了解UI变化。不宜太快，人的大脑容易反应不过来，处于很懵的状态。也不宜太慢，用户一直在等待，会产生枯燥不耐烦的心理感受。</p>
<p>（3）简单明了：动画过渡要简单明了，保持连贯，避免多个元素交叉重叠，显得混乱。</p>
<p>（4）一致性：遵循尼尔森十大交互原则中的一致性原则。整个产品应当使用统一的动效标准，比如运动速度、缓动曲线统一，使用户体验一致。</p>
<h2 id="toc-3">三、持续时间</h2>
<p>在及时反馈原则上，Material Design规范对于手机端的动画持续时间，提供了三个层级建议：</p>
<p>（1）小范围过渡的元素，建议时间是100ms，比如开关按钮动画。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/EYujFK88Yqz5l0V2BbvG.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="252" referrerpolicy="no-referrer"></p>
<p>（2）中范围过渡的元素，建议时间是250ms，比如半屏面板展开。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/taySVvPnExqplrMvdruT.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="252" referrerpolicy="no-referrer"></p>
<p>（3）大范围过渡的元素，建议时间是300ms，比如悬浮按钮转化为全屏面板。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/rHzgUaptDEMBx20lEyVj.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="600" height="442" referrerpolicy="no-referrer"></p>
<p>这个时间我们只能参考，具体动画时间还是要看界面效果来确定。</p>
<h2 id="toc-4">四、缓动曲线</h2>
<p>缓动曲线，调整过渡元素的速度，按物理规律自然地加速或减速，这样动画才会显得自然愉悦。在不同的平台或软件，缓动曲线可能会有不同的命名，MaterialDesign规范定义了四种：</p>
<h3>1. 标准曲线</h3>
<p>标准曲线（也称为EaseInOut）是最常用的缓动曲线，元素从静止开始快速加速，缓慢减速到结束。这种缓动曲线适合屏幕内的元素在屏幕内的运动，过渡自然，可以用在悬浮按钮转化为面板的动画。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/uHOcFarLKV7rQQdRWxDu.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="599" height="276" referrerpolicy="no-referrer"></p>
<h3>2. 强调曲线</h3>
<p>强调曲线（也称为EaseInOut）是标准曲线的拓展，元素加速时间减短，减速时间加长，强调过渡的结束。这种动画效果会稍微俏皮一些，对于办公产品要慎用，也避免曲线样式太多设计师无法清晰地区分使用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/tyxER3kcAhOE54gdZV97.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="599" height="276" referrerpolicy="no-referrer"></p>
<h3>3. 减速曲线</h3>
<p>减速曲线（也称为EaseOut），元素从屏幕外快速进入并逐渐减速，在静止时结束。这种缓动曲线可以用在半屏面板出现的动画。快速进入，可以迅速响应用户的操作行为；当用户大脑收到即时反馈后，为了避免高速移动带来的紧迫感，元素需要缓慢减速到静止。</p>
<p>同时，让用户在等待过程中可以提前识别和接收内容信息，动画结束后可以第一时间操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/QFRNVwvfQbj8dYOve1Dz.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="599" height="276" referrerpolicy="no-referrer"></p>
<h3>4. 加速曲线</h3>
<p>加速曲线（也称为EaseIn），元素在屏幕内静止，逐渐加速离开屏幕。这种缓动曲线可以用在半屏面板消失的动画。用户操作关闭面板，表示已经不关注面板内容，这时动画就需要快速响应，加速移动屏幕，避免用户出现等待的焦虑感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/hCqjZTAnySkQorx012uN.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="599" height="276" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、动效风格</h2>
<p>设计师了解完动效原则、持续时间、缓动曲线后，当业务需要定制一套动效标准时，我们需要结合产品调性制定动效风格。工具类产品专注内容，可以使用直接、简洁的风格；娱乐类产品，可以使用俏皮、活泼的风格。</p>
<p>影响动效风格主要有几点：速度、运动路径、缓动曲线、海拔高度，我们可以看下对比效果。</p>
<p>（1）持续时间300ms的标准缓动和650ms的强调缓动的对比。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/yAx3YqbezmVlOOePKfUU.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="441" referrerpolicy="no-referrer"></p>
<p>（2）如果元素沿对角线移动，运动路径可以是直线或弧形，看下对比。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/a2hxCveS9YbBkfgw5m9l.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="440" referrerpolicy="no-referrer"></p>
<p>（3）默认过渡和弹跳过渡的对比。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/14N1kdrrD2Rq5kZYLlez.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="440" referrerpolicy="no-referrer"></p>
<p>（4）默认情况下，背景内容在动画过程是静止的。为了动画更生动活泼，可以调整背景内容比例来强调海拔高度。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/FtxnPhw9vLUOebiMeIKW.gif" alt="研究Material Design交互动态系统后，我总结了几点！" width="600" height="442" referrerpolicy="no-referrer"></p>
<p>从对比效果来看，持续时间较短、斜向移动的直线路径、默认过渡、默认海拔高度的动画风格直接、简洁，及时反馈，专注内容；持续时间较长、斜向移动的弧形路径、弹跳过渡、变化的海拔高度的动画风格强调动画的过程，俏皮、活泼、生动有趣。</p>
<p>如果是办公产品，需要克制，不要盲目强调动画。</p>
<h2 id="toc-6">六、动效标注</h2>
<p>设计师完成交互动效Demo后，就要输出一份动效标注交付开发实现。</p>
<p>在实际项目中，我有遇到过一些问题：有些设计师反馈文字表格不直观、不易编辑；有些开发同学反馈动画曲线看不懂。</p>
<p>为了解决这些协作问题，我结合动效标注的项目经验，参考Material design规范动画曲线和咨询开发同学的意见，最终搭建了一个Sketch动效标注模板，组件化搭建编辑，比较方便。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="研究Material Design交互动态系统后，我总结了几点！" src="https://image.yunyingpai.com/wp/2022/03/VJtHlk5YqX5WpzdYIYFY.png" alt="研究Material Design交互动态系统后，我总结了几点！" width="598" height="726" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">总结</h2>
<p>以上就是我对Material Design交互动态系统的学习总结。理解交互动效的具体作用，我们才能更有说服力地和产品沟通，推动落地。在设计过程中，我们应当遵循自然、及时反馈、简单明了、一致性的原则，结合产品调性打磨出一套自然愉悦的动效标准。还需要注意一点，要恰当地使用持续时间和缓动曲线。</p>
<p> </p>
<p>作者：<span id="profileBt" class="rich_media_meta rich_media_meta_nickname">ALEI</span>，微信公众号：<span id="profileBt" class="rich_media_meta rich_media_meta_nickname">ALEI的设计思考</span></p>
<p>原文链接：https://mp.weixin.qq.com/s/JckY0VQJYEU2nXje2NINGA</p>
<p>本文由 @<span id="profileBt" class="rich_media_meta rich_media_meta_nickname">ALEI</span> 授权发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
                      
</div>
            