
---
title: '有人告诉你「Popover气泡卡片」这么好用吗'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/TbtOwBxTv2NCBtHHRi8t.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 07 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/TbtOwBxTv2NCBtHHRi8t.jpg'
---

<div>   
<blockquote><p>编辑导语：气泡卡片是一个由矩形和三角箭头组成的弹出窗口，可用来做提示引导，或者实现一些页面的耦合，等等。不过任何一种交互组件的使用都有限度，气泡卡片也不例外。本篇文章里，作者对气泡卡片的交互含义、以及设计时的注意事项做了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5126970 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/TbtOwBxTv2NCBtHHRi8t.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>前几篇短文小编介绍了「radio button」「check box」等一系列与表单相关等交互组件，相信观众老爷们对表单的页面编排已经有基本的概念。现在我们开启「popover」的世界，简单聊一聊气泡卡片的交互性质是怎么样的。</p>
<h2 id="toc-1">一、「Popover气泡卡片」的交互含义</h2>
<p><strong>「Popover」又称”气泡卡片/气泡弹出框/弹出式气泡/气泡”，是由一个矩形和三角箭头组成的弹出窗口，箭头指向的地方通常是导致气泡卡片弹出的控件或区域。</strong>通过点击气泡卡片内的按钮或非气泡卡片的屏幕其他区域可关闭气泡卡片。</p>
<h3>1. 「Popover气泡卡片」的交互结构</h3>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/XnFBdcktGbw12YvrBrxE.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="587" height="270" referrerpolicy="no-referrer"></p>
<p><strong>1）箭头（Arrow）</strong></p>
<p>箭头：「气泡卡片」内承担方向指示作用，位置不固定，随着需要指向的内容方向而改变。</p>
<p><strong>2）容器（Container）</strong></p>
<p>容器：文字信息或者操作信息的承载物。</p>
<p><strong>3）内容（Content）</strong></p>
<p>内容：「气泡卡片」内最重要的部分，可以是说明信息也可以是操作功能。</p>
<p>这里要强调一点，通常我们使用「气泡卡片」会用一些视觉手法强调其是浮于原操作界面之上，例如：描边、投影等。<strong>介于「气泡卡片」指向好、善于吸引注意力、操作效率高、可承载信息量大的特点，一般使用在以下三种场景</strong><strong>比较多：「快捷导航」「提示引导」「界面解耦」。</strong></p>
<h3>2. 快捷导航</h3>
<p>由于移动端局限于物理尺寸，<strong>设计师不得不将大量的低频但又重要的功能操作塞入「气泡卡片」内，通过“更多”、“···”、“+”的方式呼出「气泡卡片」。</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/RkZNcyWUeq9oKOIiWxEj.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="585" height="245" referrerpolicy="no-referrer"></p>
<h3>3. 提示引导</h3>
<p>基于「气泡卡片」自带箭头这一方向性特质，我们在可以把它使用在一些需要引导的功能设计上面，比如版本迭代后的新功能提示，<strong>这样做可以让用户非常明确地知道针对对页面中某项新功能产品方更新了哪些东西。降低用户认知成本。</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/dqFHisoaJszUudPUfhEZ.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="587" height="229" referrerpolicy="no-referrer"></p>
<h3>4. 界面解耦</h3>
<p>当不想破坏原界面用户使用节奏与信息密度的情况下，<strong>可以利用「气泡卡片」信息承载量大的特点来进行一些页面的解耦，达到屏幕空间复用的目的</strong>（此做法适用于大尺寸界面 ）。</p>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/QrsptY9bVPm3GXsly9la.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="584" height="292" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、「Popover气泡卡片」的注意点</h2>
<h3>1. 注意与「Edit Menus 编辑菜单」的区别</h3>
<p>在iOS规范当中明确把「Edit Menus 编辑菜单」与「Popover气泡卡片」分为两种不同的交互组件，使用场景也存在不小差异。</p>
<p><strong>「Edit Menus 编辑菜单」用在对文本信息、视图信息等内容编辑功能的承载，如复制和粘贴，其交互动作通常为长按或者双击。</strong></p>
<p><strong>https://developer.apple.com/design/human-interface-guidelines/ios/controls/edit-menus/</strong></p>
<p><strong>「Popover气泡卡片」在iPhone上苹果并不推荐使用，而是让它用在屏幕尺寸更大的iPad上。</strong></p>
<p>https://developer.apple.com/design/human-interface-guidelines/ios/views/popovers/</p>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Xlacnoi1lZ5PHU5QVUr1.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="397" height="376" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/wA7Y5LDXVoWYQkz55j2Z.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="588" height="390" referrerpolicy="no-referrer"></p>
<h3>2. 避免使用时面积过大</h3>
<p>不应该把气泡卡片面积做得过大，更不应该占据整个屏幕，这样会造成对原本信息的遮盖。<strong>说到底气泡卡片还是一种中等提醒的形式，设计师不应该贪心，设计时应对承载信息做减法，并且要注意不同屏幕下的适配问题。</strong></p>
<h3>3. 谨慎考虑弹出位置</h3>
<p>气泡卡片的箭头应尽可能直接指向目标的元素。由于无法在屏幕上拖动气泡卡片，因此气泡卡片不应覆盖重要信息。<strong>需要注意的是，在屏幕边缘需要转换气泡卡片的方向，例如在屏幕顶部，<strong>气泡卡片</strong>应当显示在触发位置的下方，否则气泡卡片会超出屏幕导致显示不完整。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/j0U5aSpcMvwaKd6ATh36.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="585" height="530" referrerpolicy="no-referrer"></p>
<h3>4. 请考虑实时保存</h3>
<p>基于它的关闭原理“通过点击气泡卡片内的按钮或非气泡卡片的屏幕其他区域可关闭气泡卡片”，造成它极其容易被误触关闭，<strong>所以在它内部进行操作时建议采用实时保存的机制，可以有效地给用户进行防错。</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/jETx4uDzkG2XUYs83miI.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="587" height="452" referrerpolicy="no-referrer"></p>
<h3>5. 每次只使用一个气泡卡片</h3>
<p>在同个窗体当中每次只能出现一个气泡卡片，当出现第二个的时候前一个必须关闭。因为从初衷来看气泡卡片就是想让用户进行内容聚焦，暂时屏蔽一些信息，如果多个同时使用的话就变的自相矛盾。<strong>并且除了弹窗之外，气泡卡片层之上不该有任何其他元素。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="有人告诉你「Popover气泡卡片」这么好用吗" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/GsXvIg1p7pEkXC0nDuGt.png" alt="有人告诉你「Popover气泡卡片」这么好用吗" width="386" height="352" referrerpolicy="no-referrer"></p>
<h3>6. 注意存在时间</h3>
<p>气泡卡片是一个中等量级的提醒组件，它不像「toast」自动出现自动消失，也不像弹窗绝对的模态强提醒，切换用户当下操作。<strong>它的出现时间与模态与非模态是可以由设计师根据业务属性自行把控，所以与前端开发进行沟通时需要把设计需求传递到位。</strong></p>
<h2 id="toc-3">三、文末小结</h2>
<p>早在移动互联网诞生之前，气泡卡片作为快捷导航或者提示引导就在PC和Web里被广泛运用。</p>
<p>在某些设计规范当中（比如iOS的移动端）并不提倡使用气泡卡片，<strong>但在移动互联网发展多年的当下，用户使用习惯已经培养完毕，只要把握好气泡卡片的特性，跨平台使用现在也挺常见。</strong>同时基于气泡卡片承载信息灵活的特点，在平常的设计工作当中饱受欢迎。</p>
<p> </p>
<p>作者：月亮与六便士；公众号：月亮体验设计坊</p>
<p>本文由 @月亮与六便士 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5125002" data-author="988175" data-avatar="http://image.woshipm.com/wp-files/2021/07/rrnx9WFpJbrvF2BwdXNs.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            