
---
title: '一文读懂如何打造B端导航设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/POh2MdOoworg8bMQPDMw.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 26 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/POh2MdOoworg8bMQPDMw.jpg'
---

<div>   
<blockquote><p>编辑导语：B端产品对于导航界面的结构设计比较注重，用户在进入页面的第一时间就对整个页面有一个大概的初印象，而且B端产品的功能性较强，所以对于设计方面要格外注意；本文作者分享了关于打造B端导航设计的思考，我们一起来了解一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4495217" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/POh2MdOoworg8bMQPDMw.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>导航作为网站或者平台的骨架，是产品设计中不容忽视的一环。</p>
<p>最近有幸接触到关于B端专题分享，课程中学到了很多关于导航的知识，于是结合自身对导航设计的理解，并综合当下导航设计相关的资料书籍，对B端导航设计作如下阐述；从多角度深入细节去解析导航，总结的一些方法和思考分享给小伙伴们，也希望大家从更多的角度跟我一起探讨。</p>
<p>本文主要从导航的结构层面出发去分析系统导航控件的组成与样式，而不是仅仅停留在导航的外观和形式上。</p>
<h2 id="toc-1">一、认识导航</h2>
<h3>1. 导航的定义</h3>
<p>我们先来圈定一下导航的范围，我们研究的是B端的导航设计，那到底啥是导航？</p>
<p>假设：同事约我们到一个陌生的大型商场吃饭，当我们到商场后，我们会通过什么找到约定的餐厅？</p>
<p>一般情况，我们都会通过商场楼层索引找到餐厅所在楼层和区域吧。如果商场里索引指示清楚的话，我们就能快速找到约定的饭店，不然，我们会感到困扰，自己瞎找，走了很多冤枉路还不一定找到，最后只能寻求朋友或商场工作人员帮助，难免会有不满。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/vX5aCkVJbOekBTCL0iNf.png" alt="一文读懂如何打造B端导航设计" width="400" referrerpolicy="no-referrer"></p>
<p>其实商场楼层索引与B端导航作用很像，都是为了告诉我们，这里有什么、我可以做什么、我在什么位置？导航就是一种对信息的分类，帮助用户找到想要的信息，完成预期的任务，告诉用户从哪里来？用户在哪里？用户可以去哪儿？</p>
<p>很多同学会将它和菜单弄混淆，菜单是一种对动作的分类和集合，点击菜单之后，会立马产生相应的动作，而导航点击后，你看到的是信息分类的合集。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/nD9pntq1speYP2col7Kp.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<p>而且在B端系统中的后台系统是根据具体业务设计的，作为一个后台系统设计师，知道如何在狭小的屏幕空间选择合理的导航形式表达业务内容是很重要的。</p>
<h3>2. 导航的作用</h3>
<ul>
<li>告诉用户这里有些什么。导航通过让层次结构可视化，从而告诉用户网站上有些什么，有效地体现站点内容。</li>
<li>告诉用户如何使用网站。好的导航能够帮助用户规划行程，含蓄地告诉用户该从哪里开始，能进行哪些选择，帮用户快速找到所需内容。</li>
<li>确定用户的位置。当用户到达某一个地方，好的导航会告诉用户“你在哪里”让他们知道所在位置，避免迷路。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/etiNNyBb8EOiYUdhlgCg.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、导航的分类</h2>
<p>可能提到导航分类就会想到：顶栏菜单、侧栏菜单、折叠菜单、下拉菜单、面包屑、分页、步骤条、时间轴、tab标签页、胶囊菜单、徽标数等；但是这些都不是今天我们要讨论的重点，这些都只是导航不同的外观形式的区分，哪有人就有疑问了：那导航和导航条是一致的吗？</p>
<p>导航条也仅是导航的一种外观。今天我们要说的是从结构和交互层面出发，针对对象去解析我们的导航。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/0p5ZY4febwUmj6SBzAjt.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>1. 全局导航 Global Navigation</h3>
<p>特点：</p>
<ul>
<li>可以覆盖整个产品的通路，往往是产品的一级信息分类，是用户操作上贯穿始终的导航；</li>
<li>不一定包含全局信息，但是一定可以去到关键节点。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/DledaHO8AK3XPQ36LcZ7.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>2. 局部导航 Local Navigation</h3>
<p>特点：</p>
<ul>
<li>在同一个架构中，可以到这个节点的上下一级的通路；</li>
<li>有严格的父子级关系，局部导航与全局导航有层级关系，局部导航帮助用户进入更加特定的页面。</li>
</ul>
<p>通常情况下，一个通路代表一个界面（这里的通路是交互上的概念），一般局部导航为二级导航。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/UGnLDPRXF1UPKSY7px20.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>3. 辅助导航 Supplementary Navition</h3>
<p>特点：</p>
<ul>
<li>提供用户在全局/局部导航不可到达的相关内容的快捷途径；</li>
<li>这个快捷途径是在本产品内的。</li>
</ul>
<p>例如在我们站酷的收藏文件夹页面，想要快速到达编辑作品收藏夹，这时候我们使用辅助导航，它可以帮助解决用户下一步去哪里，还能提供什么帮助等问题，优秀的设计是让用户可能多的使用关联导航，而不是全局和局部导航。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/XbPL0iRFwEShVVMyhSKN.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>4. 内嵌导航</h3>
<p>特点：</p>
<ul>
<li>也叫上下文导航，嵌入页面自身内容的导航；</li>
<li>通常同在上下文超级链接，引导搜索等。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/fyXuHkFbjeku8eKXrB2P.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>5. 友好导航</h3>
<p>特点：</p>
<p>给用户提供一个便利的前进途径，在需要的时候能找到信息入口，帮助提升网站可用性的功能，并不是主要功能，但却不能缺少，通常摆放位置在界面右上角。</p>
<p>通常置于网站右上角关于用户、消息、登录、帮助等导航，比如站酷右上角消息中心、我的个人服务等。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/YtyulK9heFvSh8oJ8kdB.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>6. 远程导航</h3>
<p>特点：</p>
<ul>
<li>不包含在产品结构中，以独立的方式独立存在于产品内。</li>
<li>通常是网站地图、索引表（地址选择、品牌选择）等。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/o8tgZy9niPYHUj7b30rw.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、导航的外观</h2>
<h3>1. 导航的外观</h3>
<p>导航的类型有很多种，同样结构的导航可以使用不同的外形，常用的比如顶栏菜单、侧栏菜单、折叠菜单、下拉菜单、面包屑、分页、步骤条、时间轴、tab标签页、胶囊菜单、徽标数等。</p>
<p>各类导航中的字体大小可根据组件库进行统一设定。</p>
<p>顶栏菜单多为一级菜单，点击切换页面，或作为下拉菜单的父级，将子级菜单合理分类。</p>
<p>侧栏菜单为垂直导航菜单，可以内嵌子菜单。</p>
<p>下拉菜单的触发方式一般有鼠标悬停和鼠标点击两种。</p>
<p>步骤条引导用户按照流程来完成任务，一般步骤不得少于两步。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/yzoIPeJsiznV6dRYa1Qd.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、导航的贴士</h2>
<h3>1. 导航尽量扁平，保持稳定就算要多一次点击</h3>
<p>三次点击已被证实无效，保证稳定的结构，多一次点击也未必是坏事。</p>
<p>在B端界面中我们尽量不要修改它的操作路径，如果跟C端一样频繁的去改变它的路径，去改变他的结构 ，用户就会产生负面情绪，理想状态下，用户需要点击的导航层级越少，那么用户到达他们的目标页面也就越快越清晰，信息层级越深，则用户越容易被误导，但是B端用户对点击次数多少是不太关注的，反而会因为修改了操作路径产生厌恶感。</p>
<p>网站导航的目标是为了让用户快速找到自己所需的内容，不能一味的追求扁平的导航结构，使得整个网站的信息分类混乱；所以，要根据情况综合考虑信息分类的广度与深度，对于信息的分类，常见的可以通过卡片分类法来进行划分。</p>
<p>比如小鹅通的后台导入用户藏的很深，通过用户管理到用户列表，再到导入用户。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/qsRzdYil7Q3eOh6Iw4be.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<p>再比如，我们平时使用微信的朋友圈流量非常大，按照一般的交互优化是要提升朋友圈的权重，将它放在下面的Tab栏，而微信一直保存它原来的入口方式：打开微信——发现——朋友圈，是因为只有这样才能尊重用户的使用路径。</p>
<p>所以在B端过程中，为了保持稳定多一次点击。</p>
<h3>2. 最好便于拓展</h3>
<p>保证导航不会由于产品的变化，发生很大的变化。</p>
<p>竖向导航拓展性比较强，一级导航的数目可以展示更多，而且层次清晰，一二三导航都可以流畅展示。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/T7qsXkTi0ZvETbZDllJl.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>3. 清晰可见，操作易懂</h3>
<p>导航大小足够、位置是用户熟悉的，要有积极的响应、与内容区要有对比。</p>
<p>积极响应的意思：一个页面够不够积极，取决于它给我的反馈够不够积极，比如鼠标hover上去会不会变色、变大、往上移一个像素等。这个是一个页面积极响应的态度清晰可见、操作易懂。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/jqiqi2GJxrbX91LCKTb2.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>4. 导航项可以重复</h3>
<p>导航可以重复，导航项也可以重复，它没有严格的层级结构，它是可以重复的，也就是一个界面中，允许存在两个主导航，同一个主导航中允许存在两个重复的项。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/AyiLoavnLSttS5REgOji.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>5. 不要让用户有惊喜</h3>
<p>避免因为有趣所以设计，要符合用户预期，这对B端设计非常重要，可能在C端设计没有任何问题，它需要一定的小惊喜，但是toB 一定不要，并且符合用户预期，避免因为有趣去设计。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/JF33Z85Uuzai1UACAtfd.png" alt="一文读懂如何打造B端导航设计" width="500" referrerpolicy="no-referrer"></p>
<h3>6. 导航的反馈需要保持一致</h3>
<p>文字链和带“跳转”的文字链，他代表的隐喻是不一样的。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/KLEiUk6thzXtZa9XsPkE.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>7. 导航不一定要有层级关系</h3>
<p>他只要做好信息分类，让用户完成任务，尽到导航的本职。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7TvOHiTSFbcTFxe8omN0.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、导航的布局</h2>
<h3>1. 全局导航样式与分析</h3>
<p>因B端用户在进入一个系统时，通常情况下都是抱有明确目的性，所以此处聚焦分析“结构导航中的全局导航”</p>
<p>常用的B端全局导航样式有三种，分别为：顶部水平导航、侧边垂直导航、混合导航，这里我们可以参考我的上篇讲B端组件库的文章里的<a href="http://www.woshipm.com/pd/4408159.html" target="_blank" rel="noopener">导航组件部分</a>，里面有详解讲解三款样式的适用场景以及它们的优缺点。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Ng0CHaecIVhbLmgE2YDc.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<p>所以我们做设计并不是坐在工位上想想，它是有一定方法的，搞清楚结构、定义、外观，然后做组合，我们就能更好的规范我们的导航。</p>
<h2 id="toc-6">六、6步导航设计法</h2>
<p>基于以上的结构、定义、外观，我们该如何把理论落地到我们的业务线呢？下面我们用一个具体案例来对导航的交互层面设计进行一个深度体验，这里我还是以小鹅通作为我们的案例，总共分为六步。</p>
<h3>1. 搞清楚每一个导航项的定义</h3>
<p>导航项决定了你的目标目标界面，帮助用户找到想要的信息，完成预期的任务。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/syR6gNJWqDQIw5Oa8JQe.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<p>我们会发现小鹅通导航的分类是从引流到促活的路径，但是我们在这里也会遇到很多问题：为什么会出现这类无用导航？为什么导航分类和导航项名字一样，但是内容不一样？为什么这个</p>
<h3>2. 搞明白用户的操作路径</h3>
<p>我们只有很好的搞明白用户的操作路径，才可以给任务类产品做一级分类，带着上面的问题，基于不同角色的产品用户体验地图可以得到用户的操作路径，这样我们就不难理解现在小鹅通的一级侧边导航了。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/65NVDW9BbCGFCdI30vpE.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>3. 区分一下权限</h3>
<p>针对B端来说，不同的用户看到内容是不一样的，可以考虑根据用户角色的不同，给用户不同的权限，这又是一个崭新的话题，一个角色可能有多个账号，可能有多个用户。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IIWitADnWvb1sUBfUowM.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<p>因此我们可以很好的得出，针对不同的角色，可以展示不同的内容，虽然我们划分了不同的角色，比如运营人员和管理员，但是我们还可以把他们划分到二级项里面去，因为我们是允许耦合的情况发生的。</p>
<h3>4. 划分一下界面数据的本质</h3>
<p>区分界面数据的性质，相同的数据来源，可以帮助我们区分界面性质，而且通常有一组相同的界面来围绕。</p>
<p>补充：</p>
<ul>
<li>元数据：数据属性的信息,用来支持如指示存储位置、历史数据、资源查找、文件记录等功能，例如一件商品、一个客户；</li>
<li>记录集：指定数据库中检索到的数据的集合，例如订单列表、发货列表；</li>
<li>关系列表：用来描述对象和对象的关系，比如你和我是好友、你和我在同一个企业微信群。</li>
</ul>
<p>我们按照上面的界面数据的性质，给小鹅通区分界面性质。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/8dlV0TiL0NaIs6PFkk1m.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<p>我们标出相同的数据类型，发现相同关系的貌似可以归类在一起。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/1DKgWa7Mkvkj1iNbttAj.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>5. 搞明白用户的使用频次</h3>
<p>高频次的可以高优展示，低频次的可以降低权重，甚至隐藏，这里我们想要搞清楚用户的使用频次，有两个方法：用户调研、数据埋点，这样我们得到一个新的一列使用频次，结合我们整理好的一级导航和二级导航，按照我们使用频次的排序，但是我们不用十分严谨的按照频次排序，而是结合具体情况去综合考虑。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/BSCxnV4T7nhwuEZH3hAc.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>6. 设计合适的导航布局</h3>
<p>这一步就是涉及到布局和外观面了，这里我们的可以回顾下上面的全局导航的布局，反正记住一点就是可用性永远大于体验。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/tsrNmyraCJEp6r1mlWDi.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h3>7. 补充贴士</h3>
<p>当二级项导航内容过多时，可以再做一个分类的命名。</p>
<p><img data-action="zoom" class=" aligncenter" title="一文读懂如何打造B端导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OjMLrloPGgLHrCQqt1Wn.png" alt="一文读懂如何打造B端导航设计" width="960" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、最后</h2>
<p>以上就是本文对B端导航的全面解析啦，相信大家应该知道了解到了如何打造一个比较好的B端导航，关于这方面个人建议需要关注如下几个方面：</p>
<p>严谨的信息架构搭建是一切的前提：信息架构的搭建是网站的基础，可尝试采用卡片分类法对导航进行分类筛选；而对于导航设计目前已经形成的规范，个人还是建议不要走花路，改变用户行为总是要付出代价的。</p>
<p>注重可视化语义表达：可采用颜色、icon等元素提高导航可视性，根据NNGstudy的研究：当用户在网页检索信息时，相比于只有文案，通过颜色和icon的差异化设计的视觉指引能让用户快37%。</p>
<p>注重交互细节和触点交互反馈：好的网页是要能够给到用户积极反馈的，设计师需要加强触点交互反馈；对同一级导航制定统一的交互行为规则、反馈及循环模式等，例如鼠标每次悬浮，菜单背景灰色显示，文字由深灰变为蓝色；另外需注意，对不同层级的导航可进行差异化处理，凸显导航层级。</p>
<p>在导航设计上面，设计师还是有很多突破的，但是改变用户的习惯是要成本的，刚接触后台产品的时候，最希望能把产品做的美观，工作中慢慢地发现项目的背后思考更为重要，产出的设计成果也应该有理有据、支撑整个设计体系。</p>
<p>在后台产品的设计过程中，更应该把宝贵的时间用在更值得关注的事物上，让设计师能够辅助业务挖掘，从趋于相同的表象中找到产品独有的闪光点，从而切实解决问题和实现价值。</p>
<p>大家一起加油吧！！</p>
<p>参考资料：</p>
<p>CCTalk夏叙老师《关于导航栏的解构和分析》</p>
<p>后台系统的导航设计：组成与呈现：http://www.woshipm.com/pd/1051921.html</p>
<p>浅谈web端导航设计 @UED频道：https://zhuanlan.zhihu.com/p/40405686</p>
<p>UI进阶干货-详解B端产品&C端产品：https://zhuanlan.zhihu.com/p/70713465</p>
<p> </p>
<p>本文由@佩奇一只居 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4494958" data-author="879352" data-avatar="http://image.woshipm.com/wp-files/2021/03/RW1YGIiIIfgQ3YJCaZ8r.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            