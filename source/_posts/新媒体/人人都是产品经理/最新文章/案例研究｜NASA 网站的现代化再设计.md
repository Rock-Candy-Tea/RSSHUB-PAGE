
---
title: '案例研究｜NASA 网站的现代化再设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/PLQ1Sbzw7nBZ9R0A9RvM.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 29 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/PLQ1Sbzw7nBZ9R0A9RvM.jpg'
---

<div>   
<blockquote><p>编辑导语：如何对网站进行设计，在保留原有品牌形象的同时，满足企业与用户双方需求，提升用户体验，让网站界面变得更富有吸引力？本篇文章里，作者结合自身经历，分享了他对NASA网站进行现代化再设计的经验，不妨来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5115094 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/PLQ1Sbzw7nBZ9R0A9RvM.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>前段时间，我应聘了 NASA SEWP（企业范围采购解决方案）的 UI 设计师职位，这是 NASA 的一个的分部门，他们与政府合作并为之提供 IT 相关的商品和服务。作为面试过程的一部分，我必须针对关于他们产品的两个案例问题提出解决方案：</p>
<p>1）鉴于 NASA SEWP 从未对其视觉识别（标志、排版、配色方案等）进行合理的设计，我们希望看到一些初步的草图，说明你将如何改进 SEWP 的品牌形象以使之符合现代美学，同时又不丢掉作为 SEWP 文化基础的俏皮精神（ 预期成果：大致的Logo、配色方案和排版方案）。</p>
<p>2）<strong>NASA SEWP 目前的网站更像是一个工具箱</strong>，<strong>并没有一个明确的使用逻辑能让新用户快速适应它</strong>。请根据你的 UX/UI 设计的经验，评估此网站并概述一些初步的建议，使用户流更直观，提供更好的用户体验（请提供粗略的草图和优秀的案例参考）。</p>
<p>请向我们展示如果这是你的第一个项目，你将如何开始解决这一问题，无需创建原型或任何高保真。</p>
<p>在上次的文章中，我介绍了关于第一个问题的解决方案，所以在这里我们将对SEWP的主页和供应商查询工具的页面布局进行一次尝试，并确定改进的机会。</p>
<p>如果你了解我，就知道我喜欢动漫。你可能也知道我认为《钢之炼金术师：Brotherhood 》是有史以来最棒的动漫。</p>
<p>你可能不知道（除非你看过那篇关于动漫与用户体验设计关系的文章），设计就像炼金术：它包括理解问题，解构问题以确定解决方案，并重建新的解决方案进行测试或执行。我将应用这个框架来解决这一问题，我们可以把这一问题陈述为：</p>
<p>我们如何重组 NASA SEWP 的主页和供应商查询工具页面，使其更具吸引力和更直观？</p>
<p>首先，让我们明确我们在寻找什么！</p>
<h2 id="toc-1">一、了解问题 Understanding the Problem（s）</h2>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/rtBwcZsMoh5RAa9xWCeH.png" alt="案例研究｜NASA 网站的现代化再设计" width="727" height="358" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">NASA SEWP 当前主页</p>
<p>首先是 NASA SEWP 的主页，很明显，在这上面杂乱地摆布着很多信息，没有一个清晰的流程或方向感，此外该网站也不是响应式的。在明确此页面所存在的问题时，有以下几点让我印象深刻：</p>
<ul>
<li>没有介绍部分；</li>
<li>链接和号召性用语太多，层次结构太少；</li>
<li>过度拥挤的导航栏；</li>
<li>文字太多，没有图片；</li>
<li>侧面元素可能会分散注意力；</li>
<li>灰色的外部背景和页脚；</li>
<li>页脚链接感觉太分散；</li>
<li>社交媒体图标的感觉和风格不一致。</li>
</ul>
<p>另一个需要优化的页面是供应商查询工具，该工具用于查找可以与政府机构签约的公司，以获得他们需要的任何服务或产品。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KjVdsFn08bF8EkSZdDrf.gif" alt="案例研究｜NASA 网站的现代化再设计" width="728" height="396" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">加载动画非常不合适，表格滚动了很长时间</p>
<p>该页面的问题我总结了以下几点：</p>
<ul>
<li>“LOADING” 覆盖后原图移位；</li>
<li>很难找到过滤器选项；</li>
<li>“返回顶部” 按钮居中，与表格重叠；</li>
<li>提供的特定供应商的信息很少；</li>
<li>非常长的滚动时间（感觉就像无限滚动）；</li>
<li>这更多是一个技术或后端问题，在浏览器中按下返回键后，理应从供应商回到表格，但实际情况下却会让你回到前一页而不是表格。</li>
</ul>
<p>现在我们了解并掌握了问题的背景，现在可以分析如何解决这些问题。<strong>在研究解决方案</strong><strong>之前</strong>，<strong>最好有一些灵感来源可供借鉴</strong>。让我们解构采购服务领域的一些案例，看看它们做得好的地方。</p>
<h2 id="toc-2">二、解构问题 Deconstructing Some Examples</h2>
<p>采购领域有两个优秀的网站可供我们学习，帮助我们实现更新 NASA SEWP 网站的创意，它们就是 IBM 的采购服务网站和 Carahsoft。</p>
<p>首先，这两个网站都是响应式的！<strong>在移动设备上有一个清晰的结构和流程</strong>，<strong>因此可以任意的扩展到更大宽度的屏幕</strong>。这两个网站也有一个浮动导航栏；当向下滚动网页时，用户随时可以访问其他页面或菜单。</p>
<p>首先我们分析一下 IBM 的网站，因为它在 SEWP 当前所存在问题的方面做得非常出色。</p>
<h3>1. IBM 网站</h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/GjTHUc2WEAatBae0XldT.png" alt="案例研究｜NASA 网站的现代化再设计" width="721" height="353" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">IBM Procurement Consulting Services 以简洁而吸引人的方式为用户提供了场景</p>
<p>IBM Procurement Services 的导航栏简单但也很完整。<strong>他们没有将所有内容都塞在一行中</strong>，<strong>而是将元素分成两行</strong>。</p>
<p>第一行包含 IBM 徽标（它会将您带到 IBM 的主页）、搜索和账户 icon 和一个包含导航链接的汉堡式菜单。同时还将移动端可访问性考虑在内，第二行在较大宽度的屏幕上会显现出来，里面包含了同样在汉堡菜单中的下拉元素，便于访问。</p>
<p><strong>还有一个提供背景图片以及主要和次要 CTA 按钮的主页横幅</strong>。在此部分下方是一组浮动链接，当您向下滚动时，这些链接会固定在页面顶部，对于较长的页面来说非常有用。</p>
<p>IBM 在构建良好的用户体验方面做得很好。视口右下角还有一个聊天功能，以防人们需要提问或与 IBM 的同事联系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/toREhusEq9qJLL91rXtk.png" alt="案例研究｜NASA 网站的现代化再设计" width="727" height="471" referrerpolicy="no-referrer"></p>
<p>关于页面可扩展性，<strong>从技术角度来看</strong>，<strong>IBM 似乎利用了 flexbox 或网格系统来对齐</strong>、<strong>定位和构建其内容</strong>。内容本身也很容易被用户理解，而且在必要时还使用了图像和图表来补充文本。</p>
<p>最后，页脚的设计很简单，没有太多链接，并且页脚中的内容（和正上方的 CTA 横幅）感觉更有条理和整齐。</p>
<h3>2. Carahsoft 网站</h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hngwijByKgpyxJlghxYe.png" alt="案例研究｜NASA 网站的现代化再设计" width="727" height="351" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Carahsoft 遵循与 IBM 类似的结构，因为它具有部分导航元素和内容</p>
<p>虽然 Carahsoft 的导航部分占用了更多空间，但它仍然很好地组织了它的元素。第一行包含公司本身的链接（职位招聘和介绍等）和一个搜索框，第二行是品牌 LOGO 和联系链接，占据了大部分空间，第三行公司的下拉菜单。</p>
<p><strong>尽管主页横幅较小</strong>，<strong>但它仍然存在</strong>，<strong>并以轮播的形式为提供了关于采购领域的信息</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/zj7jPbnCX70kFvuIrUMv.png" alt="案例研究｜NASA 网站的现代化再设计" width="727" height="471" referrerpolicy="no-referrer"></p>
<p><strong>Carahsoft 通过对信息或链接进行分组</strong>、<strong>分割和突出显示进行排版</strong>。该网站还包括实时聊天功能，但它确实会占用更多空间，并且在您单击关闭按钮时会完全消失。</p>
<p>最后，该网站的页脚包含了相当多的内容（比 SEWP 的页脚内容更多），由于其元素的结构是按列排布的，所以当缩小视口宽度时，这些列就会折叠成行。</p>
<p>现在我们分析了一些鼓舞人心的例子并总结出了它们优秀的地方，让我们将这些知识应用到重建 NASA SEWP 的主页中，同时考虑供应商查询工具页面的相关元素之间的排版。</p>
<h2 id="toc-3">三、重构解决方案 Reconstructing the Solution</h2>
<p>通过将学习到的优点应用到 NASA SEWP 的网页设计中，确定了如下的改进机会点。</p>
<h3>1. 主页</h3>
<p>我对主页提出了如下的改进机会点：</p>
<ul>
<li>包括一个主页横幅部分（带有 1-2 个 CTA 或轮播图的图片）；</li>
<li>合并和删除优先级较低的 CTA，使用颜色强调主要 CTA；</li>
<li>显示最重要的导航链接，并将其余的放在一个汉堡式菜单里；</li>
<li>将文字配以图像和图形（也可以考虑使用较短的文本）；</li>
<li>在主体或导航中包含这些元素；</li>
<li>白色是我们的朋友：保持一致的留白；</li>
<li>重新排列页脚元素以使其更具流动性和结构性；</li>
<li>使底部的社交 APP 图标保持一致的风格（例如从 Font Awesome 中提取）。</li>
</ul>
<p>根据这些要点，我绘制了主页概念图如下图所示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/GEDKMGVH2PD5khn4SLzY.png" alt="案例研究｜NASA 网站的现代化再设计" width="726" height="692" referrerpolicy="no-referrer"></p>
<p><strong>我尝试了不同的主页横幅结构以及供用户优先浏览的内容</strong>。最终决定当然取决于用户研究和测试，以及对 SEWP 来说 SEO 和转换的优先级。</p>
<p>为了适应当代社会现代化发展程度，尤其是考虑到现在超过一半的网络流量发生在移动设备上时，我绘制了一些移动 APP 概念图，以提高该网站的可访问性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WAj53ggKvHwSts6ZXPto.png" alt="案例研究｜NASA 网站的现代化再设计" width="718" height="1083" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（说明：我选择了第一版（V1），因为它占用的垂直空间较少，而且主要内容都包含在内）</p>
<h3>2. 供应商查询工具页面</h3>
<p>供应商查询工具本质上是一个表格搜索引擎，因此，用户如果不知道要搜索什么，或者在页面上得到太多反馈结果，可能会感到不知所措。</p>
<p>牢记这些要点，我提出了以下的改进机会点并将它们应用到我的草图中：</p>
<ul>
<li>将“加载”轮或图形构建到表格中；</li>
<li>加入过滤器选项（# 产品、字母、供应商类型、合同等）；</li>
<li>如果保留 “回到顶部”按钮，最好将其放在一边；</li>
<li>提供有关提供商的更多详细信息（联系方式、经常显示的地址、链接等）；</li>
<li>每页显示一定数量的搜索结果（也可以让用户控制每页的浏览量）；</li>
<li>加入一个后退箭头按钮，帮助用户可返回查找工具页。</li>
</ul>
<p>与主页一样，我也设计和思考了供应商查询工具页面的移动端版本，使用户在移动端也能够正常地访问供应商工具及其提供的内容。</p>
<h2 id="toc-4">四、写在最后 Closing Thoughts</h2>
<p>由于 NASA SEWP 从未有过正式的设计方向，因此承担完全改造 UI 以及扩展网站的 UX 的角色是一件非常有趣的事情。</p>
<p>团队惊喜地发现我在概述重新设计概念时考虑了响应式设计和移动端布局，并围绕是否需要在网站上实现实时聊天的功能进行了讨论。我主张在用户测试中将其考虑在内，以查看客户和访问者是否使用该功能或发现它的价值。与第一个针对品牌形象改造的测试相同，这个练习也为我提供了展示设计方案和促进与队友讨论的机会，谢谢阅读！</p>
<p>本文翻译已获得作者的正式授权（授权截图如下）</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜NASA 网站的现代化再设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Hco8ojD0h36nCvOPAL0u.png" alt="案例研究｜NASA 网站的现代化再设计" width="724" height="1060" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：Ahmed Ayoub</p>
<p>原文：https://bootcamp.uxdesign.cc/case-study-a-modernized-redesign-10cefa80e0dd</p>
<p>译者：陈熠璇；审核：吴鹏飞、李泽慧、张聿彤；编辑：孙淑雅</p>
<p>本文由@TCC翻译情报局 翻译发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5115060" data-author="1274336" data-avatar="http://image.woshipm.com/wp-files/2021/05/xCvopGF5HenULUrgReTS.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            