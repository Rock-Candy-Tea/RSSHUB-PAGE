
---
title: '手把手带你重新认识Radio Button'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/L2fdJ8rjXs9QoeHNjlNP.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 13 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/L2fdJ8rjXs9QoeHNjlNP.jpg'
---

<div>   
<blockquote><p>编辑导读：「Radio Button」是构成表单功能的基础元素之一，合适巧妙的设计它可以让用户对表单完成有个很好的心理预期，对提高用户体验至关重要。本文作者围绕Radio Button进行了分析，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5037770 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/L2fdJ8rjXs9QoeHNjlNP.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>今天在群里有个小伙伴截了两个boss直聘当中有关单选任务的设计问题，不研究不知道，一探究其根本发现「Radio button」这个表单设计当中最基本的元素可讲的点还是挺多的。今天我们就手把手从基本的组件层面来聊下「Radio button」。</p>
<h2 id="toc-1">一、「Radio button」的含义</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/87zfF4szjSTrclADCz9q.png" referrerpolicy="no-referrer"></p>
<h3>1. 「选择」的概念</h3>
<p>从社会学角度给出的定义：意思是挑选，选取，指从一些人或事物中选出合乎要求的目标 。</p>
<h3>2. 「Radio button」的隐喻</h3>
<p>「Radio button」顾名思义直译成中文就是「收音机按钮」，其物理原型是老式电台收音机。老式收音机使用物理按钮，并且默认打开就会接收到一个电台频率，按下一个按钮后，其他所有按钮都会弹出。</p>
<h2 id="toc-2">二、「Radio button」的定义与特征</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/PgN5SAr4FH39edFpHqOs.png" referrerpolicy="no-referrer"></p>
<p>那么结合刚才聊到的“选择”概念与“raddio button”隐喻，我们就可以给出“radio button”的定义与特征：</p>
<p>「Radio button」的定义：从若干个后选项当中，完成单选任务的组件。</p>
<p>「Radio button」的特征：</p>
<ul>
<li>后选项必然大于等于两个。</li>
<li>后选项的集合之间天然互斥。</li>
<li>默认情况之下，必然有一个选项是选中状态。</li>
<li>每次只能选中一个后选项。</li>
</ul>
<p>为了说明观点补充的下W3School的截图：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hHj4yHbDCVthRJYUoTmb.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、打爆大厂的狗头</h2>
<h5>讲了这么多以后终于可以打爆antdeisgn的狗头了，可能当中有些我们不知道的考量，但是antdesign给出最基本最简单用法是值得商榷的。仅仅只有一个后选项，那么选与不选有什么差别，也并没有给出默认选中的状态。只能说这种改造方式，违背原生控件的意图，也有违用户对于“选择”动作的基本认知了。所以在使用大厂设计时我们也要时刻提高警惕，不可迷信也不可全信。</h5>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/giFvGkihDfzbl4MJJwgy.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、「Radio button」的基本状态</h2>
<p>「Radio button」的交互状态比较简单，分别是「选中」，「未选中」、「不可选」三种。这里特别提醒一点，「Radio button」并不像「check box」有「不确定」状态。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hAVfSPbAn1QkTyWxcHb0.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、「Radio button」的设计窍门</h2>
<h3>1. 选项的逻辑顺序</h3>
<p>「Radio button」的选项应该按某种逻辑顺序排列，例如从最简单的操作到最复杂的操作，或者从最低风险到最高风险。让用户心理状态符合某种预期，更好的理解表单。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/QZ8KaL7so3Pp6CIFvLmq.png" referrerpolicy="no-referrer"></p>
<h3>2. 选项应该是全面和清晰的</h3>
<p>「Radio button」的控件内容比较少，用户对于它的理解来源于标签（Label）的释意与选项的描述，那么清晰准确的语义表达对于用户来说至关重要，合适的上下文联系可以让用户容易理解设计者的意图。</p>
<h3>3. 提供默认选择</h3>
<p>由「Radio button」的隐喻造成其默认情况下必定有一选中选项，那么将“最安全”或者“用户最希望的选项”作为默认值变的很关键。适合的默认值会增强用户信心，提高表单完成率。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/XsWYgCL34Y6lFCQiBZE2.png" referrerpolicy="no-referrer"></p>
<p>如果用户需要跳过该项选择，那就该在选项中提供一个为“无”的候选项。因为为用户提供明确的选择选项比强迫用户从选项中选择体验要好得多。</p>
<h3>4. 尽量垂直排列选项</h3>
<p>当页面布局在合理范围之内，后选项自上而下设计是一种比较优雅的设计方式。即节约横向设计空间，也让用户信息获取难易度降到最低。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/9dyIhnReyZIHyUFkzkyi.png" referrerpolicy="no-referrer"></p>
<p>当后选相水平放置时，用户在扫描选项时可能会遇到问题，很难分辨哪个标签对应哪个选项，所以「Radio button」的后选项横向排列不利于用户扫视信息。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xqM0zhY37wtzOyZjKe8Q.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">不优雅的设计</p>
<p>如果真的无法避免水平放置，那么选项之间合适的间距设计会变得十分重要，或者通过外观的设计从视觉上让用户得到更好的体验。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/m0MIjdhVtZPzvnxNlJY2.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">优雅的设计</p>
<h3>5. 较大的点击区域</h3>
<p>在衡量交互成本时，目标的大小起着重要作用。单选按钮本质上很小，很难点击到它们。尝试增加目标区域，以便更容易地选择选项。让用户不仅可以通过单击圆圈来选择选项，还可以通过单击文字来选择。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5NDjKafxqUtT1qAOJlU4.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">左：有限的区域可供点击 右：较大的可点击区域。</p>
<h3>6. 使用「Radio Button」而不是「下拉框」</h3>
<p>同样是用户完成单选任务的基本组件，「Radio Button」和「下拉框」使用场景略有区别。</p>
<p>在web端场景下，2≤选项≤5时，从操作路径，用户获取信息效率等几个方面综合考虑，使用「Radio Button」好过使用「下拉框」。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yH99ZCeoH76AliwBwlwC.png" referrerpolicy="no-referrer"></p>
<h3>7. 「Radio Button」在移动场景的样式变体</h3>
<p>移动设备屏幕横向空间受限，原生形态的「Radio Button」样式不利于节约空间，所以众多设计师创造出很多同构异型的组件样式，这里小编不一一枚举。但是有一种样式特别说明下（如图所示），以按钮group的样式来完成用户单选任务，这里不推荐Antdesign这种选项与选项之间无缝连接的设计方式。因为这么设计会让用户产生疑惑：这到底是tab类组件还是单选组件？建议的做法还是选项之间留有适当的空间，让其有别于tab类组件。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/sJqrvlP1Xnl0NIt53yCY.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、关于「Radio Button」的小结</h2>
<p>「Radio Button」是构成表单功能的基础元素之一，合适巧妙的设计它可以让用户对表单完成有个很好的心理预期，对提高用户体验至关重要。并且在平常的工作设计中，对大厂产品的设计也需要有怀疑精神，并不是所有都是正确优雅的设计。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/lQMVJQJOId9iYStvOjss.png" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：月亮月六便士；公众号：月亮体验设计坊</p>
<p>本文由 @月亮与六便士 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5031747" data-author="988175" data-avatar="http://image.woshipm.com/wp-files/2021/07/rrnx9WFpJbrvF2BwdXNs.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            