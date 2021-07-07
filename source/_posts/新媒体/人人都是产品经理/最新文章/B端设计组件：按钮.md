
---
title: 'B端设计组件：按钮'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6Y8gePzr08qlHNR67nCw.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 07 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6Y8gePzr08qlHNR67nCw.jpg'
---

<div>   
<blockquote><p>导读：按钮是界面中最基础的元素之一，一个个按钮承载着一个个操作指令，响应用户各类操作行为，传达用户的种种业务诉求。B端业务庞大而复杂，不同的场景使用的按钮不同，同一流程不同状态下的按钮也不同，甚至同一模块在不同显示设备上按钮也有所差异。下面是在实际工作中的关于按钮的一些总结和思考，也希望能够给读者带来一些新的思考。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4829979 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6Y8gePzr08qlHNR67nCw.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、按钮类型</h2>
<p>依据按钮呈现的视觉重量差异，我们可以通过改变样式将按钮分为主按钮、次按钮、虚线按钮、文字按钮、图标按钮5类。</p>
<h3>1.1 主按钮</h3>
<p>在日常场景中，主按钮是页面中按钮区最为核心的操作按钮，通过使用主题色填充容器吸引用户视线聚焦，引导用户去关注、操作主流程，强调性较高。</p>
<p>常见有纯文字、图标+文字两种类型，5种不同状态</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/be8EZQQMjB5uZjyJavGk.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>1.2 次按钮</h3>
<p>次按钮是在日常场景中运用最广泛的的一种按钮，由此也被称为默认按钮，视觉呈现上相较于主按钮较“弱”。通常有描边和文字组成的字线型、背景填充（中性色或较浅的主题色）和文字组成的字面型两种，用于按钮区没有主次之分的平级按钮，强调性中等。</p>
<p>常见有纯文字、图标+文字两种类型，5种不同状态</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/OBQ6rw4fT14NmuK0Z3Y5.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ukf6rEZH9HV7fGt7Y3dX.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>1.3 虚线按钮</h3>
<p>虚线按钮在日常场景中属于低频操作按钮，容器内只有简单的虚线边框，视觉上弱于次按钮，常用于场景中的添加操作，强调性较低。</p>
<p>常见有纯文字、图标+文字两种类型，5种不同状态</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qwsvCJ1pjqiaIhtwNrs0.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>1.4 文字按钮</h3>
<p>文字按钮在日常场景中的使用频次也较高，文字按钮常见也分为两种：一种是各种状态下容器边界都是隐藏的，一种是在hover、press、active状态下容器有背景色填充（较浅中性色）的。不管哪一种形式视觉感受都较弱，通常用于不太明显的操作，强调性较低。</p>
<p>常见有纯文字、图标+文字两种类型，5种不同状态</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/F3KurfWCQk6jWkejqxF7.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/R7JitySFGJNDukvsUl5N.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>文字按钮和链接的在默认外观上基本一致，甚至在有的项目中各种交互状态也一致，比较难区分文字按钮和链接。</p>
<p>在我们的团队项目中，文字按钮和链接也做了不同的定义，链接在hover、press、active状态下都有显示下划线，来告知用户这是一个外部的链接；文字按钮则在hover、press、active状态下容器都会填充背景色。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/blbh9ArCYcAsqzm9wZvx.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>1.5 图标按钮</h3>
<p>图标按钮在日常场景中的使用频次较高、也颇为高效，图标按钮默认状态下容器在不可见，视觉感受也较弱，由于没有文字，一些语义性不强的图标容易导致用户理解的偏差，一般用在图标hover状态下会出现Tooltip提示来解决此问题，图标按钮的强调性也较低。</p>
<p>常见只有图标，5种不同状态</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/fzVCSoCwtVvjlEY9jqHT.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>综上所述就是在B端项目中十分常见的五种按钮，不同团队、不同项目都会根据自身的实际项目去定义和使用不同按钮。</p>
<p>在我们团队的实际项目中，依据按钮视觉重量的不同，将按钮分为一级按钮（主按钮）、二级按钮（次按钮、虚线按钮）、三级按钮（文字按钮）、四级按钮（图标按钮），在强调属性的重要程度上随级别增加递减。在实际的项目场景中，根据不同需求的强调程度去选择相应级别的按钮，有了这个准则作为指导参考，大大降低了团队在选择按钮时的时间成本。</p>
<h2 id="toc-2">二、按钮应用细节</h2>
<h3>2.1 按钮拆解</h3>
<p>通过对一个按钮的拆解，可以将按钮分为容器、背景、图标、文本、描边、圆角等基本元素，每种元素的视觉呈现都会反过来影响按钮的外观。不同风格、不同气质的产品，需要相应的处理的影响按钮视觉呈现的各个元素。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Xh7FGUl2ncrCT9cw4WgN.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>2.2 按钮圆角</h3>
<p>圆角按钮所带来的不仅仅是圆角大小的视觉表现，更多是影响着用户对整个产品整体认知，以及用户在使用产品过程中的具体感受。合理科学、适合产品气质特征、符合用户预期和认知的圆角元素，对整个产品使用体验的提升是有很大的帮助的。</p>
<p>这里的圆角不仅仅局限于按钮，推而广之适用产品中的每个元素，提前合理的规划各种元素圆角，更会对整个产品的一致性大有裨益。</p>
<p>直角按钮：棱角分明，四角垂直过渡，呈向外扩张之势，给人以尖锐、强烈，不易接近之感。</p>
<p>圆角按钮：与直角相比，四角过渡较舒缓，呈向内聚拢之势，多给人以柔和、亲近，平易好接触之感。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7UJMdjEn8E4xtBqgunA6.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>多个直角按钮近距离排列，由于直角的张力的存在，相邻直角按钮的间隔在视觉感受上被弱化，不像圆角按钮那样能更容易的区分、甄别每个按钮。满足产品需求的情况下，适当的圆角按钮较直角按钮更合适。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ehqm8Os18zCRTTfVIBi4.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>当然圆角也不是越大越好，相同尺寸的按钮，圆角越大对在页面中的视觉占比越小，操作的容易性越低。尤其在B端与下拉菜单进行联动时，也会受到大圆角（全圆角）的局限，使下拉菜单和按钮的组合适配显得比较突兀。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/WFxrZ6V7v7Vo9Tte5Pcq.png" alt width="1080" height="706" referrerpolicy="no-referrer"></p>
<h3>2.3 按钮loading状态</h3>
<p>按钮loading状态算是一种较为特殊的状态，指的是户操作按钮后在得到反馈前的一种临时按钮状态，常与按钮组合在一块作为多态按钮使用。</p>
<p>由于数据量大或者网速不稳定页面造成数据反馈会有一定的响应加载时间，当这个加载时间让用户有明显的等待感知时，就需要一种反馈来告知用户当前正在进行的状态，防止用户在不知情的情况下犯错误操作，一般会使用loading动画来做这种反馈，不仅向用户反映了系统的当前状态，适当的动画效果还能转移用户注意力，起到给用户情绪降躁的效果。</p>
<p>按钮的loading状态则可以代替loading动画，既起到了原来loading动画的效果，又不会因页面变动过大给用户带来不适。在越发重视用户体验的今天，按钮的loading状态也越来越多的运用在产品的各种场景中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/1KOXcZ0Jk42Edd3dvojy.png" alt width="1080" height="410" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、按钮应用技巧</h2>
<p>通过以上对按钮了解，应该对按钮有个大概的认识，接下来就去看看在实际工作中是怎么制作按钮。</p>
<h3>3.1 按钮宽度尺寸</h3>
<p>在实际项目中应用中，我们发现按钮中的文本字数≤4能够满足大多数场景。为保证大多数按钮的长度一致，就需要在定制按钮组件时给按钮中的文字区域一个基准宽度，当文字的实际宽度大于基准宽度时，按钮的宽度随着文字的实际宽度增加而增加；当文字的实际宽度不大于基准宽度时，按钮的宽度就是文字的基准宽度+左右padding值。</p>
<p>我们项目的网格基数是4px，基准正常按钮为96*32</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Yl5Of5Px7WOJYFwidbNz.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>3.2 按钮大小</h3>
<p>实际项目需求中，不同场景用到的按钮大小（按钮的高度）也会有所不同。在我们的项目中我们将通用按钮划分为大（large）、正常（normal）、小（small）、超小（extra small），按钮高度分别对应着36px、32px、24px、20px。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6ovGpU92BcHrQ906FURn.png" alt width="1080" height="648" referrerpolicy="no-referrer"></p>
<h3>3.3 按钮颜色</h3>
<p>若品牌色定义了从浅到深不同层级的色阶，可使用正常基准色作为按钮的normal颜色，相邻的浅色阶作为hover状态下对应的颜色，相邻深色阶作为press状态下对应的颜色。</p>
<p>我们项目中把“disabled”状态的定义为了一个中性色，用“置灰”的形式来告诉用户当前状态不可操作，而没有选择色阶中的浅色。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/uaTVnIn7ND67XiCREzmI.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>如果没有定义从浅到深的色阶，在原来主题色的基础上，则可以给hover状态添加一个透明度为16%（#fff），给press状态添加一个透明度16%（#000），给用户以实时操作反馈。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/4qPMNf01OdPYXn5M5otJ.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>3.4 按钮区</h3>
<p>按钮区是指用于放置按钮的区域，一个按钮区内可以有多个按钮，按钮区的位置应该位于什么页面的什么位置？参考众多设计语言，我们认为按钮应置于用户的视觉浏览路径中，便于被用户发现，并且应尽量靠近其所控制的对象。</p>
<p>结合经典的“F”、“Z”网页浏览模式作为基础指导。我们将一个相对复杂模块分为header、body、footer三个区域：header区域的按钮区放置影响模块全局的操作；body区域的按钮区放置影响跟随内容的操作；footer区域的按钮区放置具有“完结流程”意义的操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/yxak4jhoNQ1CNm3o3Pbr.png" alt width="1080" height="662" referrerpolicy="no-referrer"></p>
<h3>3.5 一个按钮区一个主按钮</h3>
<p>一个模块的按钮区最好只有一个主按钮，否则会对用户造成疑惑，“到底哪一个是主要流程？”，对模块主流程功能造成干扰。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/0FsbbexY1UQb5Ba1YJnh.png" alt width="1080" height="630" referrerpolicy="no-referrer"></p>
<p>一个模块的按钮区可以没有主按钮，在日常场景中，经常会遇到一个模块中几个分支流程重要程度都是平级的，此时则不需要主按钮。若非要安排一个主按钮则会让使用者产生困惑，造成流程层级混乱。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rgu8MJPUeZDuOrZ8XmnM.png" alt width="1080" height="630" referrerpolicy="no-referrer"></p>
<h3>3.6 按钮的排列</h3>
<p>最常见且疑问当属“取消按钮在左边还是右边”，Micrisoft、Apple、Google三家操作系统巨头给出的方案各不相同，可见不管哪种方案，只要能在系统中保证统一性，都是可以被用户所接受的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/26cPUGfzEwjMbGnkAxiE.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>在我们团队的项目中定义了这样一个“靠边原则”，既按钮区在左侧时，优先级别高的按钮落在左侧；按钮区在右侧时，优先级别高的按钮落在右侧。按钮位于中间位置时，引导操作的按钮统一在右侧。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qZVQ5Uez5A52e0j9uDKl.png" alt width="1080" height="614" referrerpolicy="no-referrer"></p>
<h3>3.7 按钮响应式规则</h3>
<p>按钮区的按钮较多且页面空间有限时，就需要“折叠”部分按钮，来优雅的展示按钮区效果。当模块宽度变窄，空间不足于完全放得下全部按钮式，此时统一采用靠右“折叠”，部分按钮隐藏在“…”按钮中，鼠标交互时再展示出来，用交互换得更大空间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bqmSpsgvmhOOJbKGRfRX.png" alt width="1080" height="614" referrerpolicy="no-referrer"></p>
<p>参考链接：</p>
<p>https://www.zcool.com.cn/article/ZMTEyNzczMg==.html</p>
<p>https://www.zcool.com.cn/article/ZMTA2NDY2OA==.html</p>
<p>https://www.zcool.com.cn/article/ZMTI2MzUwMA==.html</p>
<p> </p>
<p>本文由@小梗果 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4824922" data-author="1267161" data-avatar="http://image.woshipm.com/wp-files/2021/07/2SCGqUTk8KWcIGQoqCYa.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            