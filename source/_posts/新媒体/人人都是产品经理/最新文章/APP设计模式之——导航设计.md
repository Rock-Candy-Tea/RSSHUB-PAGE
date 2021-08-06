
---
title: 'APP设计模式之——导航设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/j7QAd5dZdJJeapbhcMCV.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 06 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/j7QAd5dZdJJeapbhcMCV.jpg'
---

<div>   
<blockquote><p>编辑导语：清晰的导航设计可以帮助用户快速获取所需信息，让用户的注意力实现有效聚焦。不过，导航设计需要针对不同的场景和目的来进行规划。本篇文章里，作者对APP设计模式之一——导航设计进行了详细的总结和分析，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4995628 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/j7QAd5dZdJJeapbhcMCV.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、一级导航/主导航</h2>
<h3>1. 标签式导航</h3>
<p>标签式导航又叫Tab式导航，是目前移动端市场上最为广泛的导航设计。标签导航通常分为底部，顶部，顶、底混合使用这三种模式。</p>
<p><b>1）底部导航</b></p>
<p>采用文字加图标的方式展现。一般有3~5个标签，适合在相关的几类信息中间频繁地切换使用。这类信息优先级较高、用户使用频繁，彼此之间相互独立，通过标签式导航的引导，用户可以迅速地实现页面之间的切换且不会迷失方向，简单而高效。</p>
<p>它的缺点是会占用一定高度的空间，如果用户是小屏幕手机，则视觉体验不太好。</p>
<p>下图应用分别为<b>微信</b>、<b>Facebook</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/68FZfkVz8AATQpCEL4iY.png" alt="APP设计模式之——导航设计" width="685" referrerpolicy="no-referrer"><b></b></p>
<p><b>2）顶部导航</b></p>
<p>当内容分类比较多，用户对不同内容的打开率相差不是很大，需要快速切换/调出的时候，经常会采用顶部导航设计模式，常见于工具类APP中，如<b>Wave Analytics</b>、<b>滴滴打车</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oLA65rtfR6GjY45uurz4.png" alt="APP设计模式之——导航设计" width="685" referrerpolicy="no-referrer"><b style="font-family: inherit; font-style: inherit;"></b></p>
<p><b style="font-family: inherit; font-style: inherit;">3）顶部、底部双Tab导航</b></p>
<p>标签式导航除了设在顶部和底部，另外有些内容比较多的产品会采用顶部、底部混合使用标签式导航，如<b>简书</b>、<b>网易云阅读</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/6AMCYGsZtpZlAzbcod0W.png" alt="APP设计模式之——导航设计" width="684" referrerpolicy="no-referrer"></p>
<h3>2. 抽屉式导航</h3>
<p>抽屉导航指的是一些功能菜单按钮隐藏在当前页面后，点击入口或侧滑即可像拉抽屉一样拉出菜单。</p>
<p>这种导航设计比较适合于那么不需要频繁切换的次要功能，例如对设置、关于、会员、皮肤设置等功能的隐藏。下图分别是<b>Wave Analytics</b>、<b>Gadgets News</b>、<b>My Rolls</b>和<b>Perisfind</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/XbEjViOy1CnwQIjAGuUC.png" alt="APP设计模式之——导航设计" width="684" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/zu9SafpHLBmmjeei6dXv.png" alt="APP设计模式之——导航设计" width="685" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">抽屉式导航的优点在于节省页面展示空间，使主页面更加简洁美观，让用户将更多的注意力聚焦到当前页面。</span></p>
<p>缺点在于次功能入口比较隐蔽，用户不容易发现；使用次功能需要二次点击，增加用户使用成本。</p>
<h3>3. 桌面式导航</h3>
<p>桌面式导航类似于操作系统或启动控制面板，其特色是主页由多个按钮组成。均衡布局时，按钮通常大小一致，以3*3、2*3、2*2和1*2等形式排布于桌面。点击按钮时，跳转至其他内部子系统/子模块。</p>
<p>如图，<b>Strides</b>和<b>Finance</b>采用了基于圆形按钮的均衡布局：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/aR3ukUJlq1vNYAH0Ecbw.png" alt="APP设计模式之——导航设计" width="686" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">而</span><b style="font-family: inherit; font-style: inherit;">360</b><span style="font-size: 16px;">和</span><b style="font-family: inherit; font-style: inherit;">日语五十音图</b><span style="font-size: 16px;">则采用了基于圆角矩形按钮的均衡布局：</span></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/NhCfBjwlgy4IlnaFrpf3.png" alt="APP设计模式之——导航设计" width="685" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">注：当圆角矩形弧度越来越小，甚至消失不见成为正方形的时候，往往用方形格子隔开各个按钮，使得视觉效果最好，这种模式见于下一节的“宫格式导航”中。</span></p>
<p>市面上还存在着一些极少数应用，它们内部生态繁杂，提供（自己的或者来自第三方服务）眼花缭乱、不胜枚举的服务项目，有些服务项目单独拎出来，做成一款应用，都可以匹敌一家小型互联网公司，甚至是中型互联网公司。</p>
<p>但是出于业务整合、平台搭建、体系构建、服务扁平化，它们会被塞到一个“壳子”里，形成“超级服务平台类”APP，比如阿里系的<b>支付宝</b>和<b>千牛工作台</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/9Sx4DE8Ld58lPMVhMXTL.png" alt="APP设计模式之——导航设计" width="680" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">支付宝首页的服务项目，可以在“全部”页面中进行个性化配置；千牛工作台首页的三方服务，可以在“设置”页面中进行个性化配置。两个APP都支持用户根据自己实际需求和使用频度，优化服务项目的显示顺序，进行入口优化。</span></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/k76fDxLlKPf3piPUUEY2.png" alt="APP设计模式之——导航设计" width="681" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">这种“超级服务平台类”APP，目前我仅在阿里系的产品中看到过，其特点是：</span></p>
<ol>
<li><span style="font-size: 16px;">高频/超高频使用，用户粘性极高，应用处于市场垄断地位，几乎无可替代产品（生态庞大带来的优势）；</span></li>
<li><span style="font-size: 16px;">应用服务种类多且扁平化（使得并列式的桌面布局模式成为必选项）；</span></li>
<li><span style="font-size: 16px;">可以当做企业移动后台来使用（支付宝的服务包括衣食住行，可认为是企业个人），我称之为“行走的ERP”；</span></li>
<li><span style="font-size: 16px;">商业氛围浓厚。</span></li>
</ol>
<p>最佳实践：菜单无主次之分，每个菜单所占空间大小一致。菜单有主次之分，主要的占空间较大，其余的占空间较小。在使用桌面式导航布局时，要充分考虑到给客户提供个性化和定制化功能。</p>
<h3>4. 宫格式导航</h3>
<p>宫格导航是将主要入口全部聚合在主页面中（因其布局比较像传统PC桌面上的图标排列，又被称为“桌面式导航”），每个宫格相互独立，它们的信息间也没有任何交集，无法跳转互通。</p>
<p>因为这种特质，宫格式导航被广泛应用于各平台系统的中心页面。这样的组织方式无法让用户在第一时间看到内容，选择压力较大，因此现在采用这种导航的APP已经越来越少，往往用在二级页作为内容列表的一种图形化形式呈现，或是作为一系列工具入口的聚合。下图应用分别是<b>钉钉</b>和<b>epocrates</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/IF4RWrXQXHWPBNEK8BRN.png" alt="APP设计模式之——导航设计" width="686" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">作为二级导航的宫格式导航：</span></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oHP9uUkpdKq3rWze3VHV.png" alt="APP设计模式之——导航设计" width="683" referrerpolicy="no-referrer"></p>
<h3>5. 舵式导航</h3>
<p>在有些情况下，简单的底部tab式导航难以满足更多的操作功能，这个时候我们就需要一些扩展形式来满足需求 ，新浪微博、lofter、闲鱼底部采用的就是舵式导航，舵式导航（之前看到别人这么叫所以我也就这么称呼吧）。</p>
<p>跟标签式导航相比，区别在于舵式导航把类似生产内容的主功能按钮放在中间，标签更加突出醒目，同时该主功能标签做了功能扩展，也因此给设计增加了一些个性化的亮点。如<b>新浪微博</b>和<b>育学园</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/98VqFW8Ma8WtOKVgi0IP.png" alt="APP设计模式之——导航设计" width="682" referrerpolicy="no-referrer"></p>
<h3>6. 隐喻式导航</h3>
<p>这种模式的特点是用一个页面来体现整个应用程序。常用于游戏app，如<b>Air Supremacy</b>和<b>2020:My country</b>。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/0F6zuADUE1PRnYYwNAhT.png" alt="APP设计模式之——导航设计" width="682" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">此外，在分类物品（如各类笔记、书籍、酒品）应用，和其他单一功能应用中也能经常看到隐喻式Tab。如</span><b style="font-family: inherit; font-style: inherit;">DAKA</b><span style="font-size: 16px;">、</span><b style="font-family: inherit; font-style: inherit;">石墨文档</b><span style="font-size: 16px;">、</span><b style="font-family: inherit; font-style: inherit;">拼图酱</b><span style="font-size: 16px;">和</span><b style="font-family: inherit; font-style: inherit;">Moment：</b></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZoK1KkeN4YQ4koxdGXhQ.png" alt="APP设计模式之——导航设计" width="690" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5X8uPb8qg1E8pQIKf2Ms.png" alt="APP设计模式之——导航设计" width="685" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">最佳实践：使用隐喻式要慎重，一个执行起来不明确的隐喻，反而会起到反作用。</span></p>
<h2 id="toc-2">二、二级导航</h2>
<p>二级导航用于在页面及模块中进行导航，因此这种应用通常来讲至少有3层信息结构，最常见的就是国内绝大多数APP都有的“我的”功能菜单。</p>
<h3>1. 列表式导航</h3>
<p>列表式导航作为信息组织框架，是我们在产品设计中必不可少的一个信息承载模式。</p>
<p>列表导航与宫格导航类似，常用于二级页面，不会默认展示任何实质内容，所以通常app不会在首页使用它。这种导航结构清晰，易于用户理解，能够帮助用户快速的定位去到对应的页面。下图应用分别是<b>微信</b>和<b>Strides</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nPNv4wuzdNMvipWP2KGZ.png" alt="APP设计模式之——导航设计" width="683" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">列表菜单导航的每个列表均指向相应的功能/内容选项，它有许多衍生形态，包括个性化菜单列表、分组菜单列表和增强型菜单列表。增强型菜单列表是指在简单列表的基础上，带有额外的搜索、浏览及过滤功能。</span></p>
<p>下图应用分别是：<b>QQ</b>、<b>有道云笔记</b>、<b>Retrica</b>和<b>Strides：</b></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nEZlZljRdssLPC05CqLq.png" alt="APP设计模式之——导航设计" width="682" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ODTLqUUqNxMnJ9meD8Pd.png" alt="APP设计模式之——导航设计" width="684" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">最佳实践：列表菜单导航适合长标题或者有副标题说明，使用类表菜单导航应该提供一个从子页面返回类表页面的方式，通常在标题栏添加一个带有菜单字样的按钮作为返回按钮。</span></p>
<h3>2. 选项卡式</h3>
<p>底部选项卡现在几乎成了IOS和Android两大系统（黑莓和webOS也比较广泛，但因为已经不是主流系统，因此暂不讨论）阵营中，绝大多数应用的标配。如<b>Facebook</b>、<b>Twitter</b>、<b>微信</b>和<b>新浪微博</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/BfbO9aZmeq2JvvngW9IG.png" alt="APP设计模式之——导航设计" width="693" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oyUi7HzRUOLqEeHfvkzM.png" alt="APP设计模式之——导航设计" width="681" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">也有非常多的应用，将Tab标签设置再了导航栏下，即顶部导航，有点类似于传统网站导航，如</span><b style="font-family: inherit; font-style: inherit;">360云盘</b><span style="font-size: 16px;">、</span><b style="font-family: inherit; font-style: inherit;">扇贝单词、豆瓣</b><span style="font-size: 16px;">和</span><b style="font-family: inherit; font-style: inherit;">Facebook</b><span style="font-size: 16px;">等。</span></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ze7CSjhDGsrx28FfRxai.png" alt="APP设计模式之——导航设计" width="692" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/kT1tYngObL18NII9g93E.png" alt="APP设计模式之——导航设计" width="682" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">最佳实践：使用选项卡导航要注意视觉上对已选择和未选择的选项进行有效区分。</span></p>
<h3>3. 图库式</h3>
<p>图库式界面被分割成用于导航的各个内容区块。内容区通常载有单独的文章、标题、照片、产品和其他能够放置在内容区、网格或幻灯片里展示的内容。如TED、BBC NEWS、Bilibili、搜狐视频等。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/FsdC1aRjw7KoexNHQnPE.png" alt="APP设计模式之——导航设计" width="693" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/0wjYBvpRDd9SYODkGwh3.png" alt="APP设计模式之——导航设计" width="681" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">有时候如果内容区是以分组形式布局，分组的内容应设计得容易被用户浏览到，如使用侧Tab形式（也称抽屉式导航）去管理分组内容，让用户能够在Tab中切换，查看不同分组，下图应用分别是</span><b style="font-family: inherit; font-style: inherit;">My Rolls</b><span style="font-size: 16px;">和</span><b style="font-family: inherit; font-style: inherit;">Perisfind</b><span style="font-size: 16px;">：</span></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/pWFSCcoKAWpcdJ6mY2iU.png" alt="APP设计模式之——导航设计" width="680" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">最佳实践：图库式界面的设计模式适用于用户想要浏览的、经常更新的内容。</span></p>
<h3>4. 页面旋转式</h3>
<p>页面旋转常见模式是使用左右滑动手势在页面间快速切换，用户滑动时将显示下一个页面。页面指示器（IOS系统下面的小点）显示一共有多少页可供切换。下图应用分别是<b>tapas</b>和<b>ConnectID</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DxzVA3tUOH5rW9zVtPwG.png" alt="APP设计模式之——导航设计" width="692" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Kzupwl0GVia9HqIkykLd.png" alt="APP设计模式之——导航设计" width="682" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">页面旋转导航模式有一定的局限性，当页面超过8个时，要考虑使用列表导航。</span></p>
<p>最佳实践：</p>
<ol>
<li>页面旋转导航适用于页面数量较少的情况；</li>
<li>使用指示器反应页面数量和当前页面；</li>
<li>左右滑动手势是最常见的旋转导航手势。</li>
</ol>
<h3>5. 图片旋转式</h3>
<p>图片旋转式的常见形态，是类似于2D旋转木马形式，图片可以左右滑动，且沿任意方向一直滑动可重新回到初始图片处。下图分别来自应用<b>TED</b>、<b>BBC NEWS</b>、<b>IMOB</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xzwyOV0GZyWSjQegpsua.png" alt="APP设计模式之——导航设计" width="690" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/qE4u2M82qxIhpXxmBXnb.png" alt="APP设计模式之——导航设计" width="682" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、其他类型</h2>
<h3>仪表盘式</h3>
<p>仪表盘汇总展示了一些关键指标。进入每一种度量方式后，都可以了解更多额外信息。这种主导航模式常用于金融应用程序、分析工具、销售和营销应用程序，如<b>友盟统计</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——导航设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/0IeGKLa8kUXFIcVV3Dsx.png" alt="APP设计模式之——导航设计" width="684" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">最佳实践：仪表盘只需要载入被研究确认过的关键数据即可，不需要过多内容。</span></p>
<p> </p>
<p>作者：银发的芝加哥</p>
<p>原文链接：https://zhuanlan.zhihu.com/p/27382083</p>
<p>本文由@银发的芝加哥 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
                      
</div>
            