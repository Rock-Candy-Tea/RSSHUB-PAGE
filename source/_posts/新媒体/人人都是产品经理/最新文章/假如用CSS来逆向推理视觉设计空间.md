
---
title: '假如用CSS来逆向推理视觉设计空间'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/2tGJGQUJGpdvtLYIlgBH.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 21 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/2tGJGQUJGpdvtLYIlgBH.jpg'
---

<div>   
<blockquote><p>编辑导读：每一个职场人都应该善于从工作中发现问题，并整理思路。本文作者经历了一个产品从0到1的设计过程，通过 CSS 对视觉空间有了一些新的想法，从中总结出了一些经验，和大家分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5259771 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/2tGJGQUJGpdvtLYIlgBH.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近几个月都在忙乎自己的产品，活生生体验了一把需求-设计-前端开发集成式累死狗的节奏；但，自从离开学校后基本没怎么敲代码的半吊子选手，通过这次的自力更生，仿佛在黑暗中找到了光明，变得大彻大悟，牛的一比哈哈哈哈~</p>
<p>简单交代下事发背景，我这款产品的研发人员构成：就俩人，除了我还有一个iOS工程师，那么按照常识我们都知道，一款产品的上线需要经过<strong>「1.确定方向」-「2.具体需求分析与产出」-「3.产品设计」-「4.产品研发」-「5.市场推广和渠道投放」</strong>这些个环节（我分的颗粒度比较粗），才算是勉勉强强的一个合格的流程；所以因为工种原因，我把这些环节做了些许整理分配给我们俩，大致情况如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/LPsMmgPNhx0T9kkbqm7x.png" referrerpolicy="no-referrer"></p>
<p>看上图能发现，其实我们在市场和渠道上需要大量的H5，比如：社群裂变landingpage / 官网 / 公众号SVG推文等等；<strong>但，问题来了，woc我们特么没有前端啊！万了！万了！芭比Q了个屁的了…</strong></p>
<p>在这种情况下，鄙人寻思了半天想出两个结局，要么冷启动阶段不做宣发，让这个襁褓中的产品自生自灭（这不行，舍不得）；要么自己coding，每晚拜四阿哥，祈求他干掉每一个bug！换的一方平安，顺利渡过冷启动阶段（就这个了！）；</p>
<p>背景就是这样，于是我开始自己写吧（边写边查边百度复制），打算重新跟CSS / JS交个朋友…令人万万没想到的事，就在这个拧巴的过程中我通过 CSS 对视觉空间有了一些新的想法：</p>
<h2 id="toc-1">一、盒子模型的三维化</h2>
<p>说个大家都懂但又绕不过去的概念，网页设计中常听的属性名：内容(content)、内边距(padding)、边框(border)、外边距(margin)，<strong>CSS都具备这些属性</strong>。这些属性我们可以用日常生活中的常见事物——盒子作一个比喻来理解，所以叫它<strong>盒子模型</strong>，CSS盒子模型就是在网页设计中经常用到的 CSS 技术所使用的一种思维模型：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/G95TxdAnfrm98XY7Vjme.png" referrerpolicy="no-referrer"></p>
<p>虽然所有HTML元素可以看作盒子，但在日常应用时，按照过往的认知，我们通常只对单一的某个元素赋予盒子，给ta添加相关属性，总体上这种做法确实可以让一个物体更充实丰富，也因为仅仅是对个体的属性，也就是说即使在xy轴的二维空间上玩出花来，也无法帮助整个画面里的所有元素形成相对舒适的关系。</p>
<p>举个例子🌰来说明下，方便理解，下图是我孵化的新产品产品欢迎页，当设计完成后，看了半天生出一种“平平无奇”的鸡肋感；坦诚的讲，这样的画面谈不上多好，中规中矩罢了，于是反复的观摩，逐渐发现了问题，造成这种高不成低不就的原因有二：<strong>缺点东西</strong>和<strong>少点层次</strong>…</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/h2vHgy7dNuf0Xqs90avl.png" referrerpolicy="no-referrer"></p>
<p>你会发现其实这些看似摸不着头脑的问题背后的本质是很直接和明了的，<strong>空间太单薄，设计出来的东西也立不住，会有一种缥缈的感觉，也对应的画面不够丰富饱满</strong>；因为主要问题出在空间上，所以也是基于此我从源头开始来了个重新推导，结合CSS盒子模型把视觉结构重新塑造了一番：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/U6FoJmk07IMvdWxvHWqQ.png" referrerpolicy="no-referrer"></p>
<p>然后，我随意画了几个长方形，看起来像碎纸屑的样子，再试着把页面的元素按照总结的方法套进去，效果如下（gif实在是太拉垮了）：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/sQxe8G32AugdGhLf8tmk.gif" referrerpolicy="no-referrer"></p>
<p>嗯，总体感觉舒服多了，该有的也有了，还不戳~如果你细品，就会发现这个理论构建了一个半自动的工作流，只需要把特定的几个元素替换下，调节部分属性参数，就可以复制出一系列的视觉方案；按照这个方法，我做了一系列的拓展方便未来做产品运营可以用的上：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/vzdBYFJMWb16wTfmQYPR.png" referrerpolicy="no-referrer"></p>
<p>要说明的是，解决层级问题的方法有很多，立体化的盒子是办法，通过改变材料或质地也是一种办法，比如我们现在及其流行的磨砂玻璃：</p>
<p>·要说明的是，解决层级问题的方法有很多，立体化的盒子是办法，通过改变材料或质地也是一种办法，比如我们现在及其流行的磨砂玻璃：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/0DR5f1FBPANg6IO5doVC.png" referrerpolicy="no-referrer"></p>
<p>他们的本质都是让画面各种元素关联起来，互相之间都有联系，从而凸显层级关系，三维盒子是这样，磨砂玻璃同样也是，这跟扁平的设计风格区别很大。说到这就不得不提一嘴历史，从过去到现在，我们反复在经历“写实”-“扁平”-“写实”-“扁平”的设计浪潮，2种风格在时代的冲击下不停迭代着，我们很难评价他们的好坏，但如果细琢磨也能发现两者的不同，从我的观点出发，<strong>写实是对现实的隐喻，ta强调关系（源于现实世界没有独立存在的个体），每一个物体都会处于某一个环境，形成一定的空间，产生一定的关系；扁平是对规则的抽象，ta强调约束，因为少了透视层级，所以需要在仅有的二维空间里尽可能的通过逻辑规则帮助画面统一和谐</strong>；可以预见的是，不管你是喜欢或讨厌，它们还是会此消彼长，永远循环着。</p>
<h2 id="toc-2">二、微妙的视觉冲力</h2>
<p>三维的盒子借助空间就很容易产生微妙的效果，比如下图这个例子，虽然终点是相同的画面，但起点不同使这个过程带了来大为不同的视觉冲力（gif实在是太拉垮了，again！）：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Y5fz2QmSO8OAlKqAYIdi.gif" referrerpolicy="no-referrer"></p>
<p>所以如果你恰巧在做动态设计或者视频剪辑等工作的话，那么别单纯的把这当做一个视觉问题，<strong>本质还是信息与视觉神经的交互问题</strong>，还是以上面两个例子来说，他们分别给了观者<strong>“扑面而来”</strong>和<strong>“穿脑而过”</strong>的感觉，如果细品你会发现：前者是压迫和震撼，后者是意外和出奇。</p>
<p>另外，在静态的设计上也同样如此，我翻了下最近收到的作品集，也发现很多朋友为了显得项目厚实写了很多推导，这导致画面臃肿不堪，在面试官和信息的交互上并没有起到很好地作用，甚至增添了获取信息的成本，所以，排版尽量简洁，这无关美丑，只是让信息提取过程高效且舒服就好。</p>
<h2 id="toc-3">三、参考/工具推荐</h2>
<p>最后推荐个参考和几个web工具：我自己是个重度3C爱好者，所以闲着没事我就会去看看各大手机（硬件/汽车主机厂）厂商的官网，特别是手机和新能源汽车行业卷到死，年度旗舰感觉一年都能搞个3-5款，更别提频率接近每个月的新品发布会了，所以<strong>这些网站就成了我摄取灵感的最佳基地</strong>；</p>
<p>这里面强如apple没毛病，华米OV（华为/小米/oppo/vivo）等手机厂商也不赖，还有蔚小理（蔚来/小鹏/理想）等等新能源厂商，他们的产品详情页基本走在了趋势的前沿，对技术和设计也都具备很高的水平，比如其中我最喜欢蔚来的这个：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/3DswZ5FJLy9uYA2z22cF.gif" referrerpolicy="no-referrer"></p>
<p>因为大小限制，截屏只是一小部分，建议铁子们去看一下完整版的页面，非常惊艳，也能更好的理解上文所说的“精神小盒”具体的含义，链接：<strong>https://www.nio.cn/ep9-experience</strong>，还有2款小工具提供给铁子们供大家使用：</p>
<h3>第一款，浏览器CSS overview</h3>
<p>这简直就是神器，可以在任意站点查看他们的<strong>颜色使用情况、字体使用情况</strong>，甚至能分析出是否符合wcag的可用性标准；我在最常用的两款浏览器上（Chrome / edge）都测试了一下，响应速度超快，通过自带的分析基本可以推导出每家企业的基础规划和应用，棒的一比~而且只需要非常简单的操作就可以解锁这神仙工具：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ns1XsOURGzckAvIFVMrJ.png" referrerpolicy="no-referrer"></p>
<h3>第二款，VisBug</h3>
<p>这款插件是Chrome开发者峰会上，Google推出的新开发工具，它简化了使用简单的点击式界面编辑网页的任务，更适合产品设计师使用，操作如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/KmZe3iewgIGtjawnefNg.png" referrerpolicy="no-referrer"></p>
<p>这款工具的应用意味着，页面初步开发完成之后，完全可以在一个简单的GUI完成所有的细节调整。开发者和设计师再也不用在浏览器和开发工具之间来回切换、调整、部署了。</p>
<h2 id="toc-4">四、总结一下</h2>
<p>不得不说，产品设计一直以来都是侧注重于规则和方法，比如设计组件、设计规范、转化方法、引流方法等等等等；但产品在视觉上因为无法使用方法，以至于权重或多或少的被降低了，这也涉及到一个概念——方法之所以称之为方法，具备一定的流程性和可复制性，所以这篇文章尽可能的把视觉总结归纳成现实可用的方法，希望对铁子们有那么一丁点的启发吧~</p>
<h3>#专栏作家#</h3>
<p>负能量补给站，微信公众号：负能量补给站，人人都是产品经理专栏作家。专注设计观点输出和资源共享。</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5258647" data-author="1170837" data-avatar="http://image.woshipm.com/wp-files/2020/11/icIZaKdzZY1dGyNMa1tP.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            