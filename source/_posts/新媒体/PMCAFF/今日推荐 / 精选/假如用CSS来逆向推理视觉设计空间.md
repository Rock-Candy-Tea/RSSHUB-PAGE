
---
title: '假如用CSS来逆向推理视觉设计空间'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/7db2fa03e8b3a38aa46e7feaf5188093-picture'
author: PMCAFF
comments: false
date: Mon, 20 Dec 2021 18:31:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/7db2fa03e8b3a38aa46e7feaf5188093-picture'
---

<div>   
<div><style>
#articleCont &#123;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  word-wrap: break-word;
&#125;
#articleCont :first-child &#123;
  margin-top: 0 !important;
&#125;
#articleCont h1,
#articleCont h2,
#articleCont h3,
#articleCont h4,
#articleCont h5,
#articleCont h6 &#123;
  margin: 40px 0 20px;
&#125;
#articleCont h1 &#123;
  font-size: 24px;
&#125;
#articleCont h2 &#123;
  font-size: 22px;
&#125;
#articleCont h3 &#123;
  font-size: 20px;
&#125;
#articleCont h4 &#123;
  font-size: 18px;
&#125;
#articleCont h5 &#123;
  font-size: 16px;
&#125;
#articleCont i &#123;
  font-style: italic;
&#125;
#articleCont p,
#articleCont div &#123;
  word-wrap: break-word;
  margin: 14px 0;
  text-align: justify;
&#125;
#articleCont blockquote &#123;
  border-left: 6px solid #ddd;
  padding: 5px 0 5px 10px;
&#125;
#articleCont blockquote p:last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont .simditor-body blockquote :last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont a &#123;
  color: #82b64a;
&#125;
#articleCont a:visited &#123;
  color: #82b64a;
&#125;
#articleCont a:hover &#123;
  color: #74a342;
&#125;
#articleCont img &#123;
  max-width: 100%;
  height: auto;
&#125;
#articleCont hr &#123;
  margin: 19px 0;
  border: none;
  border-top: solid 1px #ddd;
&#125;
#articleCont ol &#123;
  list-style-type: decimal;
&#125;
#articleCont ol li &#123;
  list-style-type: decimal;
&#125;
#articleCont ul &#123;
  list-style-type: disc;
  padding-left: 40px;
&#125;
#articleCont ul li &#123;
  list-style-type: disc;
&#125;
#articleCont table &#123;
  width: 100%;
  font-size: 12px;
  border-collapse: collapse;
  line-height: 1.7;
&#125;
#articleCont table thead &#123;
  background: #f9f9f9;
&#125;
#articleCont table th,
#articleCont table td &#123;
  border: solid 1px #ccc;
  text-align: left;
  vertical-align: top;
  padding: 2px 4px;
  height: 30px;
  min-width: 40px;
  box-sizing: border-box;
&#125;
#articleCont pre &#123;
  white-space: pre-wrap;
&#125;
</style><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/7db2fa03e8b3a38aa46e7feaf5188093-picture" alt="7db2fa03e8b3a38aa46e7feaf5188093-picture" coffee-w="1880px" coffee-h="848px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">最近几个月都在忙乎自己的产品，活生生体验了一把需求-设计-前端开发集成式累成狗的节奏；但，作为自从离开学校后基本没怎么敲代码的半吊子选手，通过这次的自力更生，仿佛在coding的黑暗中找到了design的光明，变得大彻大悟，牛的一比哈哈哈哈~</p><p style="text-align:justify;">简单交代下事发背景，我这款产品的研发人员构成：就俩人，除了我还有一个iOS工程师，那么按照常识我们都知道，一款产品的上线需要经过「1.确定方向」-「2.具体需求分析与产出」-「3.产品设计」-「4.产品研发」-「5.市场推广和渠道投放」这些个环节（我分的颗粒度比较粗），才算是勉勉强强的一个合格的流程；所以因为工种原因，我把这些环节做了些许整理分配给我们俩，大致情况如下：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/e107d5a2eaa66cebc3770ce7b3fa94f2-picture" alt="e107d5a2eaa66cebc3770ce7b3fa94f2-picture" coffee-w="1880px" coffee-h="1720px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">看上图能发现，其实我们在市场和渠道上需要大量的H5（社群裂变landingpage / 官网 / 公众号SVG推文等等）；但，问题来了，woc我们特么没有前端啊！万了！万了！芭比Q了个屁的了…</p><p style="text-align:justify;">在这种情况下，鄙人寻思了半天想出两个结局，要么冷启动阶段不做宣发，让这个襁褓中的产品自生自灭（这不行，舍不得）；要么自己coding，每晚拜四阿哥，祈求他干掉每一个bug！换的一方平安，顺利渡过冷启动阶段（就这个了！）；</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/5e0630f1b7f32c9bb506832d307d7b81-picture" alt="5e0630f1b7f32c9bb506832d307d7b81-picture" coffee-w="1880px" coffee-h="952px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">背景就是这样，于是我开始自己写网页（边写边查边百度复制），重新跟CSS / JS交个朋友…起初我只是把这件事当做一个任务来完成，但意料之外的是，我通过一段时间的coding，在CSS和之前一直秉持的视觉空间观点中找到了一些通性，也提炼了些即时可用的方法，基于此我试着分享给铁子们：</p><h1><strong>1.三维化的盒子模型</strong></h1><p style="text-align:justify;">说个大家都懂但又绕不过去的概念，网页设计中常听的属性名：内容(content)、内边距(padding)、边框(border)、外边距(margin)， CSS盒子模型都具备这些属性。这些属性我们可以用日常生活中的常见事物——盒子作一个比喻来理解，所以叫它盒子模型，CSS盒子模型就是在网页设计中经常用到的CSS技术所使用的一种思维模型：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/8f855c56877d0f5cbe0de4b021e76151-picture" alt="8f855c56877d0f5cbe0de4b021e76151-picture" coffee-w="1880px" coffee-h="1000px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">虽然所有HTML元素可以看作盒子，但在日常应用时，按照过往的认知，我们通常只对单一的某个元素赋予盒子，给ta添加相关属性，总体上这种做法确实可以让一个物体更充实丰富，也因为仅仅是对个体的属性，也就是说即使在xy轴的二维空间上玩出花来，也无法帮助整个画面里的所有元素形成相对舒适的关系。</p><p style="text-align:justify;">举个例子说明更方便理解，下图是我孵化新产品的产品欢迎页，当画面完成的那一刻，看了半天还是生出一种“平平无奇”的鸡肋感；坦诚的讲，这样的画面谈不上多好，中规中矩罢了，于是反复的观摩，逐渐发现了问题，造成这种高不成低不就的原因有二：缺点东西和少点层次…</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/a8f54cc26cc009675b7e306a30be9aa6-picture" alt="a8f54cc26cc009675b7e306a30be9aa6-picture" coffee-w="1880px" coffee-h="3388px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">你会发现其实这些看似摸不着头脑的问题背后的本质是很直接和明了的，空间太单薄，设计出来的东西也立不住，会有一种缥缈的感觉，也对应的画面不够丰富饱满；因为主要问题出在空间上，所以也是基于此我从源头开始来了个重新推导，结合CSS盒子模型把视觉结构重新塑造了一番：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/14cef33ec52261bae0af8d46a6995f22-picture" alt="14cef33ec52261bae0af8d46a6995f22-picture" coffee-w="940px" coffee-h="4332px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">然后，我随意画了几个长方形，看起来像碎纸屑的样子，再试着把页面的元素按照总结的方法套进去，效果如下（gif实在是太拉垮了）：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/7d114f256632b5060aacd2ff1904084a-picture" alt="7d114f256632b5060aacd2ff1904084a-picture" coffee-w="1200px" coffee-h="2575px" coffee-format="gif" referrerpolicy="no-referrer"></p><p style="text-align:justify;">嗯，总体感觉舒服多了，该有的也有了，属实不戳~如果你细品，就会发现这个理论构建了一个半自动的工作流，只需要把特定的几个元素替换下，紧接着调节部分属性参数，就可以复制出一系列的视觉方案；按照这个方法，我做了一系列的拓展方便未来做产品运营可以用的上：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/7fa01248ab956861b70eeab1e1e9461b-picture" alt="7fa01248ab956861b70eeab1e1e9461b-picture" coffee-w="940px" coffee-h="4340px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">要说明的是，解决层级问题的方法有很多，立体化的盒子是一个办法，通过改变材料或质地也是一种办法，比如我们现在及其流行的磨砂玻璃：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/c07ff042abf1393743ed046247afcbb6-picture" alt="c07ff042abf1393743ed046247afcbb6-picture" coffee-w="1880px" coffee-h="1066px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">他们的本质都是让画面各种元素关联起来，互相之间都有联系，从而凸显层级关系，三维盒子是这样，磨砂玻璃同样也是，这跟扁平的设计风格区别很大。说到这就不得不提一嘴历史，从过去到现在，我们反复在经历“写实”-“扁平”-“写实”-“扁平”的设计浪潮，2种风格在时代的冲击下不停迭代着，我们很难评价他们的好坏，但如果细琢磨也能发现两者的不同，从我的观点出发，写实是对现实的隐喻，ta强调关系（源于现实世界没有独立存在的个体），每一个物体都会处于某一个环境，形成一定的空间，产生一定的关系；扁平是对规则的抽象，ta强调约束，因为少了透视层级，所以需要在仅有的二维空间里尽可能的通过逻辑规则帮助画面统一和谐；可以预见的是，不管你是喜欢或讨厌，它们还是会此消彼长，永远循环着。</p><h1><strong>2.微妙的视觉冲力</strong></h1><p style="text-align:justify;">三维的盒子借助空间就很容易产生微妙的效果，比如下图这个例子，虽然终点是相同的画面，但起点不同这个过程带了来大为不同的视觉冲力：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/4dd8035ea62e36b33625601249078d5d-picture" alt="4dd8035ea62e36b33625601249078d5d-picture" coffee-w="nullpx" coffee-h="nullpx" coffee-format referrerpolicy="no-referrer"><img alt="640.gif" src="https://img.pmcaff.com/Fi1rTZu5xm2SgF_-rWGY4yRZZY3T" width="940" height="1200" coffee-w="940px" coffee-h="3320px" coffee-format="gif" referrerpolicy="no-referrer"></p><p style="text-align:justify;">所以如果你恰巧在做动态设计或者视频剪辑等工作的话，那么别单纯的把这当做一个视觉问题，本质还是信息与视觉神经的交互问题，还是以上面两个例子来说，他们分别给了观者“扑面而来”和“穿脑而过”的感觉，如果细品你会发现：前者是压迫和震撼，后者是意外和出奇。另外，在静态的设计上也同样如此，我翻了下最近收到的作品集，也发现很多朋友为了显得项目厚实写了很多推导，这导致画面臃肿不堪，在面试官和信息的交互上并没有起到很好地作用，甚至增添了获取信息的成本，所以，排版尽量简洁，这无关美丑，只是让信息提取过程高效且舒服就好。</p><h1><strong>3.参考与工具推荐</strong></h1><p style="text-align:justify;">我自己是个重度3C爱好者，所以闲着没事我就会去看看各大手机（硬件/汽车主机厂）厂商的官网，特别是手机和新能源汽车行业卷到死，年度旗舰感觉一年都能搞个3-5款，更别提频率接近每个月的新品发布会了，所以这些网站就成了我摄取灵感的最佳基地；</p><p style="text-align:justify;">这里面强如apple没毛病，华米OV（华为/小米/oppo/vivo）等手机厂商也不赖，还有蔚小理（蔚来/小鹏/理想）等等新能源厂商，他们的产品详情页基本走在了趋势的前沿，对技术和设计也都具备很高的水平，比如其中我最喜欢蔚来的这个：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/2fe3393c8dd43df26cc279f423a124d0-picture" alt="2fe3393c8dd43df26cc279f423a124d0-picture" coffee-w="2552px" coffee-h="1628px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">因为大小限制，截屏只是一小部分，建议铁子们去看一下完整版的页面，非常惊艳，也能更好的理解上文所说的“精神小盒”具体的含义（蔚来ep9的网页)；另外，还有几款小工具提供给铁子们供大家使用；</p><h2>第一款，浏览器自带的CSS overview</h2><p style="text-align:justify;">这简直就是神器，你可以在任意站点查看他们的颜色使用情况、字体使用情况，甚至能分析出是否符合wcag的可用性标准；我在最常用的两款浏览器上（Chrome / edge）都测试了一下，响应速度非常快，通过自带的分析你基本可以推导出每家企业的基础规划和应用，棒的一比~而且只需要非常简单的操作就可以解锁这神仙工具：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/6fc821b96b25b14b126e5a92d6414fa4-picture" alt="6fc821b96b25b14b126e5a92d6414fa4-picture" coffee-w="940px" coffee-h="4970px" coffee-format="png" referrerpolicy="no-referrer"></p><h2>第二款，VisBug</h2><p style="text-align:justify;">这款插件是Chrome开发者峰会上，Google推出的新开发工具，它简化了使用简单的点击式界面编辑网页的任务，更适合产品设计师使用，操作如下：</p><p style="text-align:justify;"><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/7b3baf2624cbec9fdd74228a2d8108e9-picture" alt="7b3baf2624cbec9fdd74228a2d8108e9-picture" coffee-w="1880px" coffee-h="2992px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;">这款工具的应用意味着，页面初步开发完成之后，完全可以在一个简单的GUI完成所有的细节调整。开发者和设计师再在不用在浏览器和开发工具之间来回切换、调整、部署了。</p><h1><strong>总结一下</strong></h1><p style="text-align:justify;">不得不说，产品设计一直以来都是侧注重于规则和方法，比如设计组件、设计规范、转化方法、引流方法等等等等；但产品在视觉上因为无法使用方法，以至于权重或多或少的被降低了，这也涉及到一个概念——方法之所以称之为方法，具备一定的流程性和可复制性，所以这篇文章尽可能的把视觉总结归纳成现实可用的方法，希望对铁子们有那么一丁点的启发吧~</p></div>
  
</div>
            