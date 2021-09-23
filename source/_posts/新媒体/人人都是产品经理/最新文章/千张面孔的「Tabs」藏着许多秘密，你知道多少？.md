
---
title: '千张面孔的「Tabs」藏着许多秘密，你知道多少？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/9jnl7AS22nM9Q84gbHKG.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 23 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/9jnl7AS22nM9Q84gbHKG.jpg'
---

<div>   
<blockquote><p>导读：「Tabs」作为界面设计当中诞生比较早的交互组件，一直在设计稿之中占举足轻重的地位，当他从桌面时代进化到移动端时代过程中也诞生了很多的变体，同时由于客观上存在复杂的用户场景，造成新手设计师使用起来会碰到很多问题花样百出。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5148242 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/9jnl7AS22nM9Q84gbHKG.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">01「Tabs」在现实世界的隐喻</h2>
<p>「Tabs」在现实世界当中可以看作是一个大抽屉，而不同标签页是对放在抽屉里不同文件夹的比喻，<strong>其中每个文件夹是有其特定内容，大体性质相互一致，</strong>但所有文件夹均属于同一个抽屉，文件夹上的标签可以让使用者对该文件夹进行命名或者进行标记。</p>
<h2 id="toc-2">02「Tabs」的交互含义</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/hGuOJRuFyVRLMNkdNQb7.png" referrerpolicy="no-referrer"></p>
<p>从现实世界映射到界面世界中，<strong>「Tabs」是一种可以在不同屏幕、不同数据集或者不同组织内容之间实现相互切换功能的交互组件，其本质为对屏幕的复用。</strong></p>
<h2 id="toc-3">03「Tabs」的结构</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/koXTQl535tGkRO0huv7n.png" referrerpolicy="no-referrer"></p>
<p>「Tabs」作为一种常用交互组件，设计师已经演化出许多不同的外观，这里小编直接引用Material Design里提到的外观进行解构。</p>
<p><strong>1.Container 容器</strong></p>
<p><strong>2.Active icon 选中图标(如果有选中文本标签，其可选)</strong></p>
<p><strong>3.Active text label 选中文本标签(如果有选中图标，其可选)</strong></p>
<p><strong>4.Active tab indicator 选中标签指示器（可选）</strong></p>
<p><strong>5.Inactive icon 非选中图标(如果有非选中文本标签，其可选)</strong></p>
<p><strong>6.Inactive text label 非选中文本标签(如果有非选中图标，其可选)</strong></p>
<p><strong>7.Tab item 标签项</strong></p>
<h2 id="toc-4">04 聊下「分段选择器」</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/6kGVcrh3p7VPisNotn9f.png" referrerpolicy="no-referrer"></p>
<p>「Segmented Controls」意为「分段选择器」，由于两者外形结构相似性很高，许多年轻设计师会把「tabs」与「Segmented Controls」混用，以为两者是同一样事物，其他它们本质大有不同，<strong>「Segmented Controls」是iOS原生控件之一，有他特定的使用场景。</strong></p>
<p>在苹果的人机交互指南当中对「Segmented Controls」的定义：<strong>分段选择器是一组分段（segment ）的线性集合，每段互斥对立，点击一段后使其触发，其他分段将变成未触发。</strong></p>
<p>所以苹果对「Segmented Controls」的定义其实是一种单选组件的变体，<strong>功能上更趋近于数据筛选而不是屏幕复用，</strong>这里提供人机交互指南对应网址。</p>
<p>https://developer.apple.com/design/human-interface-guidelines/ios/controls/segmented-controls/</p>
<h2 id="toc-5">05「Tabs」的使用小窍门</h2>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/aPIVbQVXTV9cLVkFF9QX.png" referrerpolicy="no-referrer"></p>
<h3>1. 突出选中标签，弱化未选中标签</h3>
<p>很多设计师在设计前都会记得这个基本点，但是使用中又往往会南辕北辙。<strong>通常使用的设计手法有拉开标签字体的大小、粗体，使用图标等一些视觉设计手法来提高区分度。</strong>下图所示，如果这个设计有三个标签项那么就没问题，但是在两个标签项的情况下用户就会很迷惑。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/lvC9Zgx3j6zJWMVWqD3a.png" referrerpolicy="no-referrer"></p>
<h3>2. 「tabs」在移动端支持手势交互</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Hemzrzh5VESR1Y2ejC82.gif" referrerpolicy="no-referrer"></p>
<p>使用时用户可以通过点击一个标签来进行内容之间的切换，<strong>同时在内容模块上也要支持执行滑动手势对「tabs」进行左右切换。</strong>但是如果在界面内也存在某些支持滑动的元素时，那么在设计「tabs」的滑动手势就需要特别注意了。</p>
<h3>3. 滚动型「tabs」 注意露出标签的位置</h3>
<p>由于在移动端「tabs」对于标签页数量没有卡的特别死，那么我们就可以通过滚动型「tabs」来扩展更多的数量。同时在使用滚动型「tabs」时部分标签是处在屏幕之外，<strong>那么在交接处的标签名我们需要露出部分在屏幕内，这样做可以暗示用户「tabs」可滑动，并且在屏幕外还存在信息。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/9ln3VJ3kZz9RfPEZvsZ3.png" referrerpolicy="no-referrer"></p>
<h3>4. 内容划分符合认识逻辑</h3>
<p><strong>对标签下的页面内容划分要符合当前的信息逻辑</strong>，这样做的好处是让用户可以轻松预测他们在选择下一个标签时的内容，<strong>如果设计师对于信息设计很难做到合适的划分角度，那么这时候使用「tabs」组件可能是一个错误的选择。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/QHcv5ZyB9pDuUuZgJ0Kn.png" referrerpolicy="no-referrer"></p>
<h3>5. 慎重对待默认项</h3>
<p>对于「tabs」来说默认项是第一个标签，但是在特定情况下也是可以对其进行自定义。<strong>但是对于数据（例如填写率，转化率等）来说个从左到右标必定衰减，那么我们在设计时就得考虑这一点。</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/sfDfuVbjuD2QLENQc41r.png" referrerpolicy="no-referrer"></p>
<h3>6. 信息对比不使用「tabs」</h3>
<p>小编见过很多设计师在设计一组对比信息时喜欢使用「tabs」来对信息进行分类，然后让用户在不断点击标签时进行信息对比。其实这种设计框架十分不可取。<strong>来回切换会给用户的短期记忆带来额外的负担，增加认知负荷和交互成本，并降低可用性。</strong></p>
<h2 id="toc-6">06 文末小节</h2>
<p>「Tabs」可能看起来像是用户界面设计中一个毫不起眼并且十分无趣的组件，但是设计师必须靠它与用户建立起良好的交互关系、同时它也包含着设计师对于界面编排的基本理解以及对页面框架结构的阐述。合理的「tabs」使用可以让用户迅速下降对于信息的接纳成本，提高使用体感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/gUVl2rk4LAEndkWPQEph.png" width="520" height="576" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：月亮与六便士；公众号：月亮体验设计坊</p>
<p>本文由 @月亮与六便士 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5145814" data-author="988175" data-avatar="http://image.woshipm.com/wp-files/2021/07/rrnx9WFpJbrvF2BwdXNs.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            