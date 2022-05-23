
---
title: '借助设计B端产品导航的机会，我对导航进行了一次彻底的分析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/avYTQy4urK7xXd2hO5zt.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 23 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/avYTQy4urK7xXd2hO5zt.jpg'
---

<div>   
<blockquote><p>编辑导读：导航栏是用户对产品架构了解的第一途径，是作为产品各个功能之间的桥梁，能够对产品功能进行分发、引导。本文作者以B端产品的导航栏为例，对其进行分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5452642 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/avYTQy4urK7xXd2hO5zt.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、定义</h2>
<p>B 端导航栏，是 B 端产品最重要的模块，对于大多数用户来说，使用B端产品主要是对具体功能进行操作，而导航栏作为产品各个功能的桥梁，他的作用是对产品功能进行分发、引导，让用户可以高效、准确的在各模块间穿梭。</p>
<p>导航栏的作用可以归纳为以下4点：</p>
<ul>
<li><b>作用一：这里有什么</b>，告诉用户这里有些什么，导航栏通过将功能结构可视化的方法，告知用户产品有哪些功能；</li>
<li><b>作用二：我在哪里</b>，确定用户的位置，好的导航会告诉用户当前所处位置，避免迷路；</li>
<li><b>作用三：怎么去</b>，告诉用户如何使用，好的导航能够帮助用户规划行程，执行完这一步操作后，下一步该去哪操作，帮用户快速找到所需内容；</li>
<li><b>作用四：怎么回</b>，告诉用户怎么返回，逆向导航，告知用户路径或者规划好用户的返回路径，让用户可以无感回到起始页面。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/vPx6w6sCgnod2BuYuEx3.png" alt width="2014" height="512" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、菜单</h2>
<p>B端产品设计中，<b>导航栏是功能菜单的载体，核心是功能</b>。因此在进行导航栏设计时，一个非常重要的前提就是要对菜单进行规划，整理。</p>
<h3>2.1 菜单的历史变迁</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/NFXxg0AycGVlSqyN4aNe.png" alt width="2522" height="1256" referrerpolicy="no-referrer"></p>
<h3>2.2 整理菜单</h3>
<p><b> 导航栏设计，必然要满足 “导航” 这个核心目标，组件的样式、交互必须为功能服务</b>。通常情况下，导航是反映产品功能模块的入口，产品中包含多少模块、子模块，就需要有序的布置到导航里面。我们可以通过思维导图的将菜单罗列出来，思维导图能解释不同功能层级的结构和从属关系，尤其是当菜单数量多，且层级超过两级的时候，思维导图就显得很有必要了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/DT4B6ZOEVXGPQZjGjAke.png" alt width="1062" height="1936" referrerpolicy="no-referrer"></p>
<p><b>理想状态下，导航菜单建议最多不要超过 9 个，最少不要低于5个。</b></p>
<p>根据“7±2原则”描述明确到：在导航菜单当中，超过 9 个会给用户查找时带来困难，低于 5 个说明导航菜单的分配效率不够高效。但在实际业务中，很多时候会超过9个菜单，这时需要对菜单进行分组，因为导航过多，用户寻找会十分迷茫，通过分组的方式，能够对菜单进行再次分类，提高查找效率。</p>
<blockquote><p>7±2原则解释：1956 年乔治米勒对短时记忆能力进行了定量研究，他发现人类头脑最好的状态能记忆含有7（±2）项信息块，在记忆了 5-9 项信息后人类的头脑就开始出错。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/l5nc44kbJC6zsOJ7VKri.png" alt width="1264" height="1520" referrerpolicy="no-referrer"></p>
<h3>2.3 菜单的深度和广度</h3>
<p>当菜单广度过大，我们也能够通过设计的方法来优化导航菜单，</p>
<ul>
<li>方法一：增加搜索栏，筛选菜单；</li>
<li>方法二：千人千面，据用户角色的不同，展示不同的菜单，大部分 B 端用户并不需要使用到全部功能菜单，管理员可以根据自身公司的业务不同，给用户配置出不同的角色权限予以满足用户的导航需求，这样在设计层面上能够减少很多不必要的麻烦。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hbA7r8uL6v0hi1KTQLpx.png" alt width="1280" height="663" referrerpolicy="no-referrer"></p>
<blockquote><p>某云目前拥有大概100+功能，这些都需要在导航菜单上显示，因此在导航设计上，它的模式是：全部菜单导航+搜索菜单</p></blockquote>
<h3>2.4 导航菜单不能隐藏超过两级</h3>
<p>导航菜单隐藏超过两级时，代表着产品在用户的使用规划中，没有深入思考整个用户体验，导航菜单层级越多，用户查找就会越慢，有一些三级导航的菜单，会通过设计优化来实现隐藏导航的合并，从而减少用户操作负担。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/BtgLhut05HMMZqkJX3Of.png" alt width="1280" height="549" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、导航</h2>
<h3>3.1 导航栏-PC</h3>
<p><b> 多种导航栏类型，该如何选择？</b>功能型产品适合侧边导航，侧边导航效率高、迟疑和错误更少，用户也普遍比较喜欢，信息型产品适合顶部导航，比如门户网站。</p>
<blockquote><p>Jennifer Rose Kingsburg 曾经对网页的三级菜单导航进行过一份研究，结论是左侧导航相对顶部导航优点更多些</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/9jFGp5UoKQ7XxtyMgz8E.png" alt width="1280" height="579" referrerpolicy="no-referrer"></p>
<p><strong>3.1.1 侧边导航栏</strong></p>
<p>将菜单栏放置在左侧，页面布局上基本为左右结构，侧边导航在国内产品中最为常见，国内厂商对于侧边栏导航的尤为偏爱，也就造成了现在 B 端产品的发展也逐渐趋同。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/TjCvjMDK8ygYA7JVmrDj.png" alt width="1280" height="367" referrerpolicy="no-referrer"></p>
<p>那么为什么国内B端为什么大多数是侧边导航栏呢？我把这种现象归纳为以下3个原因：</p>
<ul>
<li>原因一：中文文字宽度较短，侧边导航能最大发挥出他的优势，能最大限度减少空间的使用率；</li>
<li>原因二：国内的业务复杂，以及对于扩展性的要求较高，每个企业都想做一个又大又全的产品，因此侧边导航栏更加适合国内的实际需求；</li>
<li>原因三：一级导航在左侧时，效率高、迟疑和错误更少，用户追求的是使用产品完成目标任务，注重的是功能完整性和操作便捷性。</li>
</ul>
<p><strong>3.1.2 顶部导航栏</strong></p>
<p>将菜单栏放置在顶部，页面布局上基本为上下结构，顶部导航早期出现于各类门户网站，比如企业官网，各种咨询类的网站经常会采取这样的导航形式。顶部导航通常在B端产品中也是十分常见的，但还是以国外产品最为集中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/pRbtpLlAbpKJVGAXkbuF.png" alt width="1280" height="466" referrerpolicy="no-referrer"></p>
<p><strong>3.1.3 混合导航栏</strong></p>
<p>将顶部导航与侧边导航进行结合。通常将一级导航菜单放置顶部，通过一级菜单的点击后，展示侧边的二、三级菜单。在一些产品拥有复杂的逻辑关系，菜单之间关系分明的产品中，混合导航也是一个不错的选择。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/mSHRutp3zZf889XYVIan.png" alt width="1280" height="482" referrerpolicy="no-referrer"></p>
<h3>3.2 导航栏-APP</h3>
<p><strong>3.2.1 拇指热区</strong></p>
<p>移动端的交互都在手掌上完成，因此，在对移动端产品进行设计时，手势是不可忽略的一部分。</p>
<blockquote><p>拇指热区概念来源于交互大神 Steve Hoober 的一个观察实验，他发现在手机大屏时代，大部分的用户是以下图的方式抓握手机：以拇指的底部为支点，抵在手机的右下角。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/DegjIg7HNN1HnPaPKyld.png" alt width="1280" height="516" referrerpolicy="no-referrer"></p>
<p>设计导航系统的时候，也会遵循拇指热区的原则，把主要功能放在绿色区域，辅助功能放在黄色或者红色区域。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0G5O7Zf897rq6ndncPbX.png" alt width="1280" height="773" referrerpolicy="no-referrer"></p>
<p><strong>3.2.2 底部导航栏</strong></p>
<p>APP最常使用的导航模式，用于一级目录的导航，位于页面底部，无论用户单手还是双手操作都能轻松点击，能告诉用户当前位置及用户切换统一层级之间的不同模块。底部Tab栏具有很强的包容性，可以形成最基本的信息框架，然后用其他的导航模式来承载具体的功能和内容。展现形式有文字 + icon，也有纯icon形式，大部分是文字+icon，可能是减少用户记忆负担。</p>
<p><strong>优点：</strong>可以在第一时间让用户了解使用频率最高、最重要的功能和信息，同时能够支持用户在不同模块之间的快速切换。</p>
<p><strong>缺点：</strong>底部导航栏超过5个就容易引起误点操作，同时在底部会占据一定的屏幕空间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/RyFYg6WgUpCvRsHSkpVH.png" alt width="1261" height="1280" referrerpolicy="no-referrer"></p>
<p><strong>3.2.3 底部（舵式）拓展栏</strong></p>
<p>为了突出中间的功能，把Tab做的比较突出，鼓励用户更多使用该功能。常见的APP如某鱼、某乎等使用了这种导航栏，把第三个Tab标签做的更加突出，放进了一些常用的功能。</p>
<p><strong>优点：</strong>可以提高导航栏趣味性，让用户贡献更多的内容。</p>
<p><strong>缺点：</strong>此类导航也是一种二级导航，既然是重要功能为什么会放在二级导航呢？把重要功能放在二级界面，会增加用户的记忆负担以及操作负担。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/8bBBmTfP7s0vSBdwAaKf.png" alt width="1258" height="1280" referrerpolicy="no-referrer"></p>
<p><strong>3.2.4 顶部Tab栏</strong></p>
<p>用于展示同一模块下不同类别的信息或者筛选不用模块的信息，一般二级导航且支持左右滑动。</p>
<p><strong>优点：</strong>可以很好地扁平化信息层级，让用户可以迅速实现同一模块下不同类别信息之间的切换并且不会迷失方向。</p>
<p><strong>缺点：</strong>位于顶部切换起来不是很方便，同时占据空间，导致屏幕可展现区域变少。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/MGhW0J4ywFFsMcr29qj3.png" alt width="1280" height="1233" referrerpolicy="no-referrer"></p>
<p><strong>3.2.5 侧边（矩式）导航栏</strong></p>
<p>通常针对产品偏沉浸式阅读的情况下使用，主导航模块切换频率低，放入其中的模块使用频率低。常与底部标签式导航组合使用，将一级页面内的信息再细分，给人以清晰的呈现方式。通过把非核心功能的低频操作都放到一个抽屉里，使得用户获得沉浸式的体验，而且能够集中用户的注意力，让用户去更好地完成核心功能，不被打扰。</p>
<p><strong>优点：</strong>用户可以将注意力放在首页，减少其他类型的导航带来分散用户注意力的情况，给用户更沉浸式的操作感和阅读感，同时可以最大限度利用屏幕空间。</p>
<p><strong>缺点：</strong>侧边导航属于二级导航，用户使用的频率会降低，不利于产品页面流量的最大化，越放在下面的功能点击率越低，如果产品框架比较大，有很多功能需要推广时，一般不用此类导航。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/uYVbtmMDerAd5yCyiQai.png" alt width="984" height="1012" referrerpolicy="no-referrer"></p>
<p><strong>3.2.6 列表式导航栏</strong></p>
<p>通常用来展示某个具体模块内容的信息进行分类，以列表的形式呈现大量的条目。多用于辅助主导航来展现信息甚至更多层次的内容，有时候需要一些提示信息。</p>
<p><strong>优点：</strong></p>
<ul>
<li>列表式结构具有很强的延展性，调整的弹性高，菜单的排序更符合人的阅读习惯，它的导航效率高；</li>
<li>可以引入字母索引，在菜单很多时对菜单进行二次分类。</li>
</ul>
<p><strong>缺点：</strong>承载的信息种类比较单一，容易引起用户的单调感，很难让用户长时间停留，如果列表中蕴含的信息量比较庞大，往往需要加入搜索功能或者索引，否则用户会遇到寻找信息的困难。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Gc3ZWDH87RBrEb2M3FH3.png" alt width="1088" height="1116" referrerpolicy="no-referrer"></p>
<p><strong>3.2.7 宫格式导航栏</strong></p>
<p>一般作为信息或平台的入口，为产品或项目信息提供聚合的载体，适合承载订阅类产品或众多属性差异非常明显的分类信息，此类导航信息的呈现内容比较少，但是每个项目选取的效率比较高。</p>
<p><strong>优点：</strong></p>
<ul>
<li>可以通过入口来进行流量的分发，具有较强的延展性，可以无限扩展内容；</li>
<li>可以划分多个内容、多个模式，由不同团队独立开发每个模块再聚合。</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>宫格式结构是信息或平台的入口，所以具体的信息往往隐藏在下一级界面，用户无法第一时间看到信息，会增加用户的认知成本；</li>
<li>同时多个入口的情况下用户选择压力大，不同入口之间缺乏联动性，有可能会增加用户的操作。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/D44M5cCzgf44eUZM2U1g.png" alt width="1064" height="1098" referrerpolicy="no-referrer"></p>
<p><strong>3.2.8 卡片式导航栏</strong></p>
<p>宫格式导航的一种延展形式，通过增加内容的可视化程度让每个条目呈现更多的信息。它能根据页面内容的变化及时更新图片，适合以图片为主的内容，像新闻、美食、旅行、视频图片等经常使用，常作为二级导航。</p>
<p><strong>优点：</strong>对运营量的要求比较低，而且单个条目的转化率会相应的提高。</p>
<p><strong>缺点：</strong>当运营量较大的时候，这种结构会降低用户寻找信息的效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/DmhwgNFVgnnLzZHM7lTM.png" alt width="1050" height="1100" referrerpolicy="no-referrer"></p>
<p><strong>3.2.9 轮播（平铺）式导航</strong></p>
<p>适用于足够扁平化的内容和随意浏览的阅读模式，将所有信息平铺在一个页面，很容易带来高大上的视觉体验。</p>
<p><strong>优点：</strong>最大程度的保证了页面的简洁性和内容的完整性，且一般都会结合滑动切换的手势，操作起来也非常方便。</p>
<p><strong>缺点：</strong>用户只能切换的相邻页面，很难跳转到非相邻的页面，容易迷失位置。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/RuKYxJbOHuIgYAW0W8zC.png" alt width="1060" height="1090" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、设计落地-以PC端为例</h2>
<h3>4.1 第一步：整理层级框架</h3>
<p>制定出一个能满足层级显示和操作的交互结构出来，值得注意的是，导航选项中，并不是所有的选项都是用来跳转的，有的菜单是用来辅助区分内容和用来展开的，我们可以在菜单上标注说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/GAlOOEGZD0VF9VRysIUu.png" alt width="1280" height="1106" referrerpolicy="no-referrer"></p>
<h3>4.2 第二步：思维导图提取信息</h3>
<blockquote><p>现状：一级菜单11个，二级菜单37个，最多有三级，产品经理反馈二期会有新增功能</p></blockquote>
<p>分析：一级菜单目前11个已经超过顶部导航的显示范围，且后续会不定数量新增，考虑到导航的扩展性及容纳性，侧边导航可能更适合产品本身</p>
<h3>4.3 第三步：设计导航栏</h3>
<p>整理好上方的内容层级，到具体设计步骤里，首先要做的，就是制定出一个能满足层级显示和操作的交互结构出来。</p>
<p>再整理一遍，侧边栏的内容包含：</p>
<ul>
<li>不可点击的分类标题</li>
<li>可以展开的一级分类</li>
<li>可以实现跳转的一级分类</li>
<li>可以点击的二级分类</li>
</ul>
<p>而可交互的元素，对应的交互状态就包括：</p>
<ul>
<li>鼠标悬浮一级菜单样式</li>
<li>鼠标悬浮二级菜单样式</li>
<li>选中一级分类，一级分类高亮</li>
<li>展开一级并选中二级分类，二级分类高亮</li>
</ul>
<p>先用原型做个示意，它的状态包含了默认、选中一级、选中二级三种情况：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/FcONshR20pb1CwD4uyIN.png" alt width="1280" height="852" referrerpolicy="no-referrer"></p>
<h3>4.4 第四步：导航栏的选中样式</h3>
<p>菜单的选中样式是指示用户当前所处位置的重要因素</p>
<p>设计时要注意：</p>
<ul>
<li>子级和父级之间的区分</li>
<li>悬停状态与选中状态的区分</li>
<li>如果有悬停展开的子级，就要注意，显示悬停菜单时，一级菜单尽量不出现背景填充的样式。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/nNkfVoUIOtbP05wFFPUN.png" alt width="1280" height="988" referrerpolicy="no-referrer"></p>
<h3>4.5 第五步：功能拓展</h3>
<p>前面提到，产品二期会有新功能上线，后面还会有三期、四期…需要考虑导航栏的可拓展性，功能太多该怎么调整？</p>
<p><b>思考方向：侧栏如何容纳超过一屏的菜单？如何快速找到我想要的功能？</b></p>
<p><strong>解决方案1：</strong>单一用户或角色所需要使用的功能菜单一般只有几个，管理员可以针对角色或用户进行权限配置，特定角色展示特定菜单；</p>
<p><strong>解决方案2：</strong>可以增加搜索栏，对菜单进行快速查找。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/cyV3UCkxi8p231iCHkbR.png" alt width="1280" height="696" referrerpolicy="no-referrer"></p>
<h3>4.6 最后落地</h3>
<p>通过上述的分析与整理，便得出能满足我们现有功能的导航栏。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/eVqy6a8AsCyP4WEJ6YIE.png" alt width="588" height="1280" referrerpolicy="no-referrer"></p>
<p><b>注意踩坑</b>：如果一种导航模式用起来不够好用，是否需要在重构时切换到另外一种模式呢？根据 Jira 的用户测试，95% 的老用户对于这种情况会感到非常迷惑，即使是再小的导航功能修改都可能直接影响到大量用户的日常使用，因此不管哪种导航模式，一旦选定，尽量不要改变，所以在选择使用何种导航时，一定要结合产品的特性来谨慎选择。</p>
<p><strong>Jira的用户测试：</strong>https://link.uisdc.com/?redirect=https://community.atlassian.com/t5/Jira-articles/A-better-navigation-for-Jira-Cloud-is-coming-soon-available-now/ba-p/1216077</p>
<h2 id="toc-5">五、逆向导航</h2>
<p>横向导航和前进导航分别指引用户操作的水平渐进和层级渐进，逆向导航则负责对反向轨迹进行定义和实施，三者结合，实现对页面的全局操控。</p>
<p>PC产品，通过页面常驻的导航栏+面包屑+浏览器的返回键，用户可以很轻易地返回或者向上跳转。相较之下，移动端的逆向导航需要进行更多的设计。后面的讨论以移动端为例。</p>
<blockquote><p>逆向导航的概念官方定义出自Material Design：从用户行为维度，分成三类：Lateral navigation（横向导航）、Forward navigation（前进导航）以及Reverse navigation（逆向导航）</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/fdmIWDlkXBCebWGOz9O0.png" alt width="1280" height="775" referrerpolicy="no-referrer"></p>
<h3>5.1 什么时候需要逆向导航？</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/nx6w5XPoc4EOOPLyEHfR.png" alt width="1280" height="467" referrerpolicy="no-referrer"></p>
<h3>5.2 反向导航的设计要点</h3>
<p><strong>1. 逻辑：操作闭环</strong></p>
<p>不管是由用户还是系统触发，都必须保留回退的通路。使用过程中不能给用户留下死胡同、断头路。</p>
<p><strong>2. 体验：满足预期</strong></p>
<p>在完成第一步的基础上，需要对反向导航做更多的思考。</p>
<ul>
<li>当用户进入比较深的页面，并不一定希望按照顺序依次返回。</li>
<li>当任务流结束的时候，用户更期待返回“首页”,而不是“上一页”。</li>
</ul>
<p>90%的情况下，我们可以用 “从哪来回哪去“的方式满足需求。但是在B端产品中，容易出现链条很长的任务流，用户一个页面一个页面地操作，最后完成提交或者保存。这时候用户进入层级太深，“逐层返回“的方式就不太合适了，回到首页更符合用户的预期。</p>
<h2 id="toc-6">六、结束语</h2>
<p>工作中还有很多可以进行深入研究的地方，这里就说到这，文中如有不当的地方，欢迎大家一起交流。</p>
<p> </p>
<p>作者：WOWdesign，研究设计价值最大化，涉及用户体验、品牌体验、空间体验。</p>
<p>本文由 @WOWdesign 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5451845" data-author="90253" data-avatar="http://image.woshipm.com/wp-files/2020/11/P6rhcSTeLPnz96Jt9FXH.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            