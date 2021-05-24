
---
title: '深度解析B端导航设计：交互篇'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/BbQZ24JDLgj4QabmT8Lx.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 24 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/BbQZ24JDLgj4QabmT8Lx.jpg'
---

<div>   
<blockquote><p>编辑导语：导航设计与产品的信息架构有关，合理、有效的B端导航设计有助于引导用户、帮助用户快速方便地获取信息。本篇文章里，作者从产品设计交互的角度，针对B端导航设计做了详细的介绍，让我们一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4598848 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/BbQZ24JDLgj4QabmT8Lx.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/3n6qbRfwHAVe3V2Cwd8q.png" alt width="701" height="467" referrerpolicy="no-referrer"></p>
<p>hello各位在B端奋斗的小伙伴们，你是否会时常因为面对导航多种多样的形式从而面对需求时无从下手，你又是否因为虽然见过了很多的案例仍然不得导航设计的要领和精髓？</p>
<p>没关系，今天我们就一起来解决这个在B端设计中困扰我们多时的难题，从交互的角度结合案例对导航进行一个立体的剖析。</p>
<p>如果你准备好了那么就请系上安全带现在就发车。</p>
<p>要探讨一个概念那么首先需要知道其精准的定义，才能展开研究，而所谓的导航（Navigation）的精准定义可以阐述为：<b>是一种对信息的分类，帮助用户找到想要的信息，完成预期的任务。</b></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/q988syBoV916pxSmLA1c.png" alt width="703" height="468" referrerpolicy="no-referrer"></p>
<p>如果你觉得这个定义很抽象，那么不妨从这个角度去理解。如果说任何界面上的功能都能够找到在我们物理世界的隐喻的话，那么导航映射的就是我们物理世界中的路牌、导览、线路示意图等，因为立足于其功能而言，导航的作用用一种大白话的说法就是：告诉用户你从哪里来、你在哪里、你可以去哪里。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/1PYGyrA8esq1kzI1emn8.png" alt width="702" height="468" referrerpolicy="no-referrer"></p>
<p>由此我们对导航有了一个较为准确的把控，那么请在座的各位快速回答我一个问题，你能够告诉我以上6个内容那些不是导航吗？</p>
<p>3</p>
<p>2</p>
<p>1</p>
<p>OK公布答案，如果你的答案是2和6那么恭喜你，你对导航的理解是较为优秀的。2和6的名称大家想必也不陌生那就是：菜单。但是不夸张地说日常的工作中仍旧有不小数目的一波同学搞不清楚这二者的区别，那么如何对二者进行一个有效的区分呢？</p>
<p>同样是从定义来入手，参照前面我们给导航进行的定义方式，菜单就是：<b>是一种对动作的分类和集合，</b><b>帮助用户快速达到某个功能。</b>也就是说当你对菜单的某一个栏目进行点击时会立马生成一个具体的动作，而导航则是对信息的分类与合集。</p>
<h2 id="toc-1">一、导航的分类</h2>
<p>那么明白了这点我们就可以对导航进行分类了。</p>
<p>提到导航的分类大家一定会脱口而出一堆词汇如：顶部导航、底部导航、左侧导航、舵式导航、标签导航、菜单导航……没错这的确是一种分类，但这只是导航在外观这个维度的分类，并不是我们今天从交互、结构层去讨论的重点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/DdQt1jWAXgkmySPa2tpM.png" alt width="702" height="468" referrerpolicy="no-referrer"></p>
<p>而立足于结构来对导航进行分类又将是如何呢？较为科学的来说是以下几类：</p>
<ul>
<li>全局导航；</li>
<li>局部导航；</li>
<li>辅助导航；</li>
<li>内嵌导航；</li>
<li>友好导航；</li>
<li>远程导航。</li>
</ul>
<p>下面我们来对这6类导航进行一步一步的具体分析。</p>
<h3>1. 全局导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/CC9XJiYEFzwwpVoNKYAJ.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>所谓全局导航是指它可以覆盖整个产品的通路，往往表现为产品的一级分类（而且大部分情况都是一级分类），它不一定包含全局信息，但是一定可以让用户可以去到其目标的关键节点。</p>
<h3>2. 局部导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/30uYdwJOi4RyUjqfUyMw.png" alt width="702" height="468" referrerpolicy="no-referrer"></p>
<p>所谓局部导航是指在同一个框架中，可以到这个节点上的上下级通路，它一定存在于严格的父子级关系中。</p>
<h3>3. 辅助导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/DRSVPWWnzWq02vkdadQT.png" alt width="710" height="473" referrerpolicy="no-referrer"></p>
<p>所谓辅助导航就是提供用户在全局/局部导航不可达到相关内容的快捷途径（这个快捷途径在本产品内）。</p>
<h3>4. 内嵌导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/NKRSD4NB4E6xJIt2Pnwj.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>所谓内嵌导航也叫上下文导航，是指嵌入页面自身内容的导航，通常同在上下文超链接、引导搜索等。</p>
<h3>5. 友好导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/XRusdxZtm0vQqVpdT4qk.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>所谓友好导航是指它可以为用户提供一个便利的前进途径，在需要的时候能够找到入口信息，通常在不需要的时候成隐藏状态。</p>
<h3>6. 远程导航</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/VnOIoaYPSyTS6NDFZe4r.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>所谓远程导航是指不包含在产品结构中，以独立的方式存在产品内，通常表现为网站地图、索引表（地址选择、品牌选择）等。</p>
<h3>7. 导航的常用UI表现形式</h3>
<p>在从结构的层面了解了导航的基本类型之后，顺便给大家提一提导航的外观。这里并不展开说，大家需要知道的是导航的外观使用遵循的是“同构异型”的准则，什么意思呢？</p>
<p>同样的结构（比如同一组数据集：商品、商品名称、商品价格）可以嵌套进入不同的外观如：卡片式、列表、详情……这个视具体的业务情况、使用场景而定。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/cvAfRm1CqOGbEYwKmCit.png" alt width="708" height="472" referrerpolicy="no-referrer"></p>
<p>常用的导航外观基本分为以上七种外观即：菜单栏、树状表、顶栏、选项卡、面包屑、文字链接、步骤。</p>
<h2 id="toc-2">二、导航小贴士</h2>
<p>知道了导航的结构分类和使用场景，那么不妨来给大家一些关于导航本身的小贴士作为原则参考，解决大家在实战中的一些问题。</p>
<h3>1. 导航尽量扁平、保持稳定就算要多一次点击</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/sfVQhyrlDrY5XYSLer5w.png" alt width="704" height="469" referrerpolicy="no-referrer"></p>
<p>对于B端产品来说稳定相当重要！因为B端产品对于用户来说使用和学习成本、门槛较大，如果你很频繁地对其路径进行修改调整，用户就会因为产品不符合操作的习惯、心智模型对产品很容易滋生负面情绪，对于产品本身来说这样的伤害是需要尽量避免的。</p>
<h3>2. 最好便于拓展</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/M7Sw66p4NEZFZxh4PpMn.png" alt width="707" height="471" referrerpolicy="no-referrer"></p>
<p>还是从稳定的方面来说，我们需要保证的是导航的变化不会因为产品的变化而发生很大的变化。</p>
<p>举个很简单的例子，当我们的产品的功能增多时，尤其是二级导航的项目增多，导致原来如果是横向布局的导航不得不改成纵向布局的导航，这就是所谓的因为产品的变化发生很大的变化。所以在选择导航布局的时候就需要打下一个很好的基础便于日后的拓展。</p>
<h3>3. 清晰可见，操作易懂</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/bvUcYkwrjkfTXHqVknIs.png" alt width="704" height="469" referrerpolicy="no-referrer"></p>
<p>这是站在一个外观和交互共同的层面去看，导航的大小一定要足够，而且其位置一定要是用户认为足够清晰的，确保在视觉反馈的的层面对于用户来说是友好的。</p>
<p>其次就是所有的可交互区域需要有积极的响应，与内容区要有对比，可以将其称为界面的热情度，这也是一个优秀界面的自我修养。</p>
<h3>4. 导航项可以重复</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Ps6D2ykoPaYod3dxSVTR.png" alt width="707" height="471" referrerpolicy="no-referrer"></p>
<p>一个页面中允许出现两个主导航，同一个界面中允许出现两个同样的导航项，并不是说一个项在导航中只能够出现一次，并没有那么死板。</p>
<h3>5. 不要让用户有惊喜</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/qpQdJVAXy8x0Ggr2pyu1.png" alt width="699" height="466" referrerpolicy="no-referrer"></p>
<p>这对于To B 的设计来说十分重要，不同于To C的产品，B端产品的一个重点就是要符合用户的预期，所以我们一定要避免“因为有趣所以这设计”这个思路。</p>
<h3>6. 导航的反馈需要保持一致</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/3IDlCacBsT8miSKMSVK6.png" alt width="708" height="472" referrerpolicy="no-referrer"></p>
<p>界面上面所有的界面编排，所有的组件、所有的控件、所有的模式都是可以找到隐喻的。比如文字链和带“跳转”的文字链，它代表的隐喻是不一样的，所以我们就需要赋予其不同的外观和交互响应对应户进行反馈。</p>
<h3>7. 导航不一定是有层级关系的</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/8eBSisBd97KNZl1o0jaB.png" alt width="701" height="467" referrerpolicy="no-referrer"></p>
<p>回到最初导航的定义，它的本质是对信息进行分类，让用户快速完成任务，这也是导航的本职工作。</p>
<p>很多时候不一定要拘泥于这个项目它应该严格存在于哪个层级之中这样的思路进行设计，而是根据用户的需求，如何将这个项目合理的分类于最适合的集合之中。</p>
<h3>8. 按权重布局的三种导航样式</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/mAIPfmlIOOB6Cc0gPxdH.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>这是一个立足于外观的点，根据大量的案例分析和眼动测试，目前市面上最为常见的按照信息权重布局的导航可分为：横向式、纵向式、纵横式。由于这部分我们不展开说，所以直接在上图整理了每种布局的特征、优劣势和应用场景。</p>
<h2 id="toc-3">三、六步导航设计法</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/iwW7evawxCKSc4mqI5pp.png" alt width="707" height="471" referrerpolicy="no-referrer"></p>
<p>知道了上面的分类和注意事项之后，下面我们用一个具体案例来对导航的交互层面设计进行一个深度体验（因为此内容十分精彩也涉及到机密，所以不在这里做具体展示，以示意的方式来叙述），总共分为六步，看看这是否也是你工作场景中比较头疼的呢。</p>
<h3>1. 搞清楚每一个导航项的定义</h3>
<p>需要搞清楚导航项的定义是因为导航项的定义决定了你的目标界面是什么，所谓的目标界面就是导航所引导你到的哪一个分类的信息处。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/0bDaAsVj1xvwJYZUv3ZK.png" alt width="708" height="472" referrerpolicy="no-referrer"></p>
<p>所以我们首先来整理一下导航中每个导航项的界面定义，这也是我们日常工作中对导航梳理十分重要的一步。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/eHGyLZHtHjUfXYKkAXtu.png" alt width="704" height="469" referrerpolicy="no-referrer"></p>
<p>当问题被罗列出来之后我们就会自然而然的产生各种各样的疑问，比如导航分类之间存在有的存在流程上的关系，但是有的分类却并不属于流程，这是为什么呢？</p>
<p>再比如有的导航分类和导航项之间名字一样，但内容却不一样，这又是为什么呢（想一想这是不是我们工作中也经常遇到的疑问呢）？这都是后面我们需要去优化的地方。</p>
<h3>2. 搞明白用户的使用路径</h3>
<p>保留住上面的问题，我们来做第二步，这一步我们需要搞明白用户的使用路径，因为这样我们可以很好地给任务类产品做一级分类。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/LhT213OLnW0qiC5a00ob.png" alt width="702" height="468" referrerpolicy="no-referrer"></p>
<p>通过基于不同角色的用户体验地图我们可以得出不同的用户操作路径，于是便可以很顺畅地得出这一套操作流程的大框架。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/4YMF3lZGtZcswDqGaLdJ.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>基于业务中的任务链路推导出每一步的操作路径，于是我们就可以将用户的操作路径就可以提炼为一级导航。</p>
<h3>3. 区分一下权限</h3>
<p>得出了一级导航，下面我需要角色的权限进行一下区分，这也是B端产品的必备属性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/FlGEBTcsB944fRxwiSrE.png" alt width="707" height="471" referrerpolicy="no-referrer"></p>
<p>于是我们为每一个导航项进行了角色权限的梳理对应，那么一级导航中每个导航分类所对应的角色也瞬间一目了然。</p>
<p>这里面多说一句，<b>当用户用不同权限的账号登录产品时，能看到不同的内容这才是一个优秀的拥有权限设计的导航。</b></p>
<h3>4. 区分一下界面数据性质</h3>
<p>到了这一部分对于一些完全没有接触过数据的同学来说理解起来可能会一些难度，我们首先需要知道的是：“<b>相同的数据来源，可以帮我们区分界面性质，而且相同的数据来源，往往会有一组相同的界面来围绕。</b>”</p>
<p>在此需要记住三个概念：</p>
<ol>
<li>元数据：数据属性的信息，用来支持如指示存储位置、历史数据、资源查找、文件记录等功能，例如一件商品、一个客户；</li>
<li>记录集：指定数据库中检索到的数据集合，例如订单列表、发货列表；</li>
<li>关系列表：对来描述对象和对象的关系，比如你和我是好友，你和我在同一个企业微信群。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/GtehV7qUxWRsXW2Ku9eT.png" alt width="705" height="470" referrerpolicy="no-referrer"></p>
<p>于是我们为导航项进行数据性质的区分归类，也就是说相同数据类型的实体往往围绕着某个元数据并且包含系列的界面。当我们这里整理完后发现，相同数据性质的实体（这里可以理解为导航项）貌似可以归类在一起，这是我们作为分类的一个依据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/0t3FgbqJYdUJzSuHadsh.png" alt width="701" height="467" referrerpolicy="no-referrer"></p>
<p>根据相同的数据性质将导航项归入应该归入的二级导航中，此时不妨和最初的版本进行对比，我们的一级二级导航相对而言已经通过改版清晰了很多。</p>
<h3>5. 搞明白用户的使用频次</h3>
<p>这一步其实是比较好理解的，很简单的法则：“<b>高频次高优展示，低频次降低权重甚至隐藏</b>”。这是针对于二级导航中每个导航项的排布进行的设计。</p>
<p>这里不妨把频次由高到低量化成为：实时关注、每天关注、每月关注、很少使用、极少使用这个几个概念，分别用五角星、三角形、矩形、圆形、菱形进行代表。</p>
<p>而关于使用频次的高低甄别一般我们可以通过用户调研和数据埋点的两种常用方式来进行，这里并不展开讲。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/jWux88MY8lBCnoDKUROs.png" alt width="708" height="472" referrerpolicy="no-referrer"></p>
<p>于是我们可以将使用频次作为一列新的参考放入导航项的表格中，瞬间清晰明了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/4o0fPZjvIEY0abkuNpDs.png" alt width="706" height="470" referrerpolicy="no-referrer"></p>
<p>根据使用频次调整每个导航项的顺序。</p>
<h3>6. 设计合适的导航布局</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/l8uRXWiRAe7EpW9Md2rs.png" alt width="704" height="469" referrerpolicy="no-referrer"></p>
<p>这一步涉及的就是外观了，不妨回顾一下之前对于导航的三种常见布局，根据产品的操作复杂程度等综合需求，我们选择了第二种形式成为最终形式。</p>
<h2 id="toc-4">四、结语</h2>
<p>以上就是本期从交互的层面对导航进行的分析拆解。很高兴你能看到最后，以上内容可以作为一种思维模版放在你日常的设计分析中，希望能对你有所启发有所帮助，一起加油在B端奋斗的小伙伴们，我们下期见！</p>
<p> </p>
<p>本文由 @核糖 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4471027" data-author="1102151" data-avatar="http://image.woshipm.com/wp-files/2020/08/EgoFpBLrFpWswRTd7n8C.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            