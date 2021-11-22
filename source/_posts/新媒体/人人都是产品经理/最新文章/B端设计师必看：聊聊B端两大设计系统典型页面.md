
---
title: 'B端设计师必看：聊聊B端两大设计系统典型页面'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/YrsvhePAGe9hYaCzd66U.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 22 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/YrsvhePAGe9hYaCzd66U.jpg'
---

<div>   
<blockquote><p>编辑导语：有效地利用B端设计系统，产品设计师将可以更高效地做出更好的交互设计。那么前段时间发布的Arco Design设计系统，和已有的阿里Ant design系统，二者有什么区别呢？本文作者对两大设计系统典型页面发表了他的看法，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5225116 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/YrsvhePAGe9hYaCzd66U.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、简介</h2>
<p>前两周字节发布了自己的中后台设计系统 Arco Design，在仔细阅读官网文档了过后，想和大家聊聊我自己对于 Arco Design设计系统的与阿里的Ant design的一些对比和差异分析。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/9EaLSueo8uIfPKCegMiy.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/j6aJPjpZtRwtA90XRtY4.png" alt width="703" height="391" referrerpolicy="no-referrer"></p>
<p>ArcoDesign 是一套设计系统的简称，是基于字节跳动所有的中后台产品。ArcoDesign 主要服务于字节跳动旗下中后台产品的体验设计和技术实现，主要由UED设计和开发同学共同构建及维护。</p>
<p>Ant Design是阿里打磨出的一个服务于企业级产品的设计体系， 通过模块化解决方案，降低冗余的生产成本，让设计者专注于更好的用户体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/9NgxRw0EdlKla41J2m5i.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、总览</h2>
<p>Ant和Arco两者的前端框架都是基于React和Vue，设计价值观和设计原则也有所不同。Arco Design 基于<strong>「清晰」、「一致」、「韵律」和「开放」</strong>的设计价值观，试图建立务实而浪漫的工作方式。在「设计价值观」的坚持上，Ant Design 有四点与众不同：<strong>「自然」、「确定性」、「意义感」、「生长性」</strong>。</p>
<p>我的个人理解Arco Design是站在设计规范的基础出发点考虑，希望给用户传递出来的价值出发，让用户深刻感受到系统是「清晰」、「一致」、「韵律」和「开放」的，而Ant Design所传递出来的价值观似乎更加玄学或者说格局更高，上升到更高的思维境界，即大自然思想和社会责任。</p>
<p>当然这部分的内容相对比较虚，每个人侧重点想法都不同，大家可以自己去理解一下这部分内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/5fnCMuSCCe0QyQNUhPDh.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/xtqJDtFT7X0bHZ0zA9DB.png" alt width="707" height="393" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、B端典型页面分析</h2>
<p>接下来会从工作台、表格、表单几个典型高频的B端界面进行分析，看看两者的差别。</p>
<h3>1. 工作台</h3>
<p><strong>1）布局</strong></p>
<p>Arco的卡片列布局灵活，基于24栅格进行布局，将整个栅格区域2:2:1的比例进行分割，信息卡片的宽度根据栅格宽度进行自适应，这样的工作台页面既灵活也能够满足业务需求。</p>
<p>Ant的卡片列布局采用3:2比例进行布局，同样是基于24栅格。目前主流的B端页面都是以24栅格为基础进行设计。3:2还是2:2:1这两种卡片布局方式没有绝对的优劣，主要是根据我们<strong>页面的信息量以及行业属性</strong>去确定。如果工作台所展示的单个信息量较多可采用少列大宽度进行布局，满足信息展示的最优布局。</p>
<p>作为B端的工作台页面，核心诉求是能够清晰<strong>找到用户想要的信息</strong>，想要做的内容，所以我们设计师要优先保证用户能够快速定位到核心的信息，快速到达要到达的功能。</p>
<p><strong>2）信息展示</strong></p>
<p>Arco针对同系列的模块设计了两种尺寸的间距，例如欢迎问候信息与下方的数据信息之间是大间距，数据信息与下方的团队动态最近项目之间是小间距。</p>
<p><strong>格式塔心理学的接近原则指出：接近的事物会被认为是同一个整体，拥有相似的功能或特征。</strong>所以在这里设计师通过两种间距的留白对我们视觉进行暗示，<strong>强调信息之间的关联程度，便于区分信息层级</strong>。</p>
<p>Ant在卡片方面没有为卡片间距设置两种尺寸，从上下到左右都是一种尺寸，这样做的好处可以让视觉更加对齐，显得页面更加规整，不好的一点就是内容区域外间距与卡片之间的间距一样宽视觉上并没有聚焦，显得内容区域很散。标题方面没有进行加粗重色强调，将内容进行突出，使用户更加聚焦于内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/6AYp4MZsmT0HzJOnA2XA.png" alt width="704" height="391" referrerpolicy="no-referrer"></p>
<p><strong>3）导航方式</strong></p>
<p>两个系统默认都采用侧边栏导航方式，侧边导航在国内的 B 端产品当中最为常见的。将菜单栏放置在左侧，页面布局上基本为左右结构，将导航菜单放置左侧固定。侧边栏导航<strong>扩展性强、展示灵活、能够快速定位</strong>，缺点是<strong>不易阅读、阅读沉浸感低。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/fg6Be4rOWf2PB1DA8Wnk.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p>Arco导航区域与内容区域都使用同类浅色，采用线的方式进行分割，整体视觉比较清爽。Ant导航区域使用了传统的重色与内容区进行区分。</p>
<p>目前的设计趋势流行浅色导航，有几个产品的WEB端进行了一系列的大改，YouTube、Twitch、Twitter都进行了重新设计，他们不约而同地将块面去除，去掉多余的的灰色，通过留白和空间将页面拉开。这否是是下一个WEB端所要追寻的趋势，我还不得而知，但是对于导航层级多的侧边栏导航，我<strong>仍然建议使用深色背景区分导航栏</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/PNvUrVraUiFiagOxReK7.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/XYv0YqpkSb6POf5aYp6o.png" alt width="704" height="391" referrerpolicy="no-referrer"></p>
<p>有一个细节，在页面背景有一个以登录的用户名形成的一个背景水印，在B端的页面中，对信息的保密程度要求很高，这里是为了防止公司核心数据资料泄露，在截图的时候会有水印的存在，增强了信息的保密级别，这是一个很好的设计洞察点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/8l8huKtwrsLiyW7LfCKR.png" alt width="704" height="391" referrerpolicy="no-referrer"></p>
<h3>2. 表格</h3>
<p><strong>1）表格样式</strong></p>
<p>表格作为<strong>组织整理数据的手段</strong>，可以有效地向用户展示数据信息，是B端产品中出现<strong>最高频</strong>的模块之一。</p>
<p>用户主要通过表格浏览<strong>获取信息</strong>、对数据进行<strong>筛选</strong>、<strong>排序</strong>以及<strong>相关业务处理等</strong>更多复杂操作、对比数据的差异与变化（关联和区别）。好的表格信息展示设计，应当是能够<strong>辅助用户高效便捷地</strong>实现以上场景中的诉求。</p>
<p>Arco和Ant的表格设计样式与市面上多数产品都类似，采用表格列无分割线条、表头与内容左对齐、数字右对齐的方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/vF2W7BUfhyZnYnGmjOUl.png" alt width="707" height="393" referrerpolicy="no-referrer"></p>
<p>合格的表格设计要定义合理的表格行高，在具体设定表格行高时，由于表格中以文字信息为主，我认为可以<strong>参考文字排版的常用做法</strong>，将整个表格的行高分成<strong>文字行高、文字与分割线间距离</strong>，即上下间距两部分来考虑。</p>
<p><strong>文字行高可以设定为字号的1.2~1.8倍，文字与分割线间距离可以设定为字号的1~1.5倍。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/dqCCfFuyfy7oogttZZ5V.png" alt width="708" height="268" referrerpolicy="no-referrer"></p>
<p><strong>2）信息展示</strong></p>
<p>表格行高决定<strong>屏幕内能呈现的行数，即用户在一屏内能获取信息的数量</strong>，主要<strong>影响用户纵向对比数据的效率</strong>。</p>
<p>在B端用户使用场景中，数据量极大的表格的展示问题是体验优劣的关键因素。对于1920*1020（包含该分辨率）以上的大屏用户，对于一屏显示行数的感知不强，但对于1366×768、1280*720等这类小屏，显示行数有限，用户进行纵向数据对比的效率就会有所降低。在设计前，<strong>应当充分了解目标用户的行为诉求</strong>，了解目标用户设备屏幕分辨率的占比分布情况，有针对性的设置行高。</p>
<p>B端产品的特点之一是<strong>通用化，覆盖用户角色多样</strong>。然而用户个体对于表格信息呈现密度的诉求经常是有所差异的。产品为了让不同用户都能获得较好的体验，可以考虑把<strong>表格疏密度的设置开放给用户</strong>，建议不是完全开放给用户去调整尺寸，而是给出一定阶梯度的快速选项，例如舒适、标准、紧凑三种高度来满足用户需求。</p>
<p>Ant的表格功能很齐全，很多功能都是B端产品的痛点，例如表格可以通过调整单元格行高来调整密度，紧凑模式下可以显示更多的数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/f22hnEi6euvE6GI9wKRE.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p><strong>3）操作路径</strong></p>
<p>作为一个查询表格，我不是很理解为什么Arco将查询条件放置在表格右上角这么隐秘的位置，而将明显的左上角放一个添加按钮，如果存在多个查询条件是不是要从右往左放置呢？这里我不是很理解，大家也可以说一下自己的想法，相互探讨一下。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/fdIkpyXzmyLr0lyoISD4.png" alt width="707" height="393" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/rGPS4KAfCcf4Sy83xJ7m.png" alt width="709" height="394" referrerpolicy="no-referrer"></p>
<p>Ant的表格使用路径符合F型视觉动线布局，在B端的市场中这种表格的设计方式已经符合用户的操作习惯了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/lL57dHrTUJcrvXCyAc5s.png" alt width="708" height="473" referrerpolicy="no-referrer"></p>
<p>在2006年时候，尼尔森诺曼发表了一篇人们如何扫描和阅读网站习惯的分享，他们通过研究发现，用户倾向于一种F模式去查看网站。F模式，能很好地帮我们创建好的视觉层次结构设计，因为这是人们可以轻松扫描设计一种布局，它能让大多数用户感到舒适，因为我们用户一直从上到到下，从左到右阅读。</p>
<p>在设计之前，我们先要去确定哪些内容最重要，明确信息的优先级，只有清楚知道你希望用户看到什么，才能将它们放在用户视线热点中。</p>
<p>个人认为在表格设计的完整度和设计的合理性方面来看，阿里的Ant系统做得比字节的Arco更好。</p>
<h3>3. 表单</h3>
<p>表单在界面中主要负责数据采集的功能，任何一个表单都可以被拆解成三个最基本要素：</p>
<p>标签（标题）、输入框和按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/swkTqADtz8rIbNLWrD74.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/kGGBTrUl12dP9Db06PjJ.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p><strong>1）表单布局</strong></p>
<p>Arco的表单属于复杂表单，当表单条目数在7个以上，可归类到复杂表单，这时候就需要根据表单的复杂度、逻辑性、关联性进行判断，选择合适的分组方式，进行归纳简化，降低表单填写负荷。采用3列布局，便签与文本框上下左对齐，这样的对齐方式有利于用户浏览的效率、对齐的美观以及国际化拓展页面的对齐问题。</p>
<p>Ant的表单也是较为常规的布局方式，有一点差异就是文本框并没有右对齐，这里阿里自己也做出了解释：文本框是根据需要填写的字段进行长度展示的，需要填写内容比较长的文本框就会比较长。实际业务中，大部分 input 所需填写内容都存在理想长度，input 的宽度应该向用户暗示所需输入内容的长度来减轻判断负担。</p>
<p><strong>2）标签对齐方式</strong></p>
<p>Arco和Ant都使用了顶标签的形式对齐。</p>
<p>标签分为左标签、右标签、顶标签三种，不同的对齐方式，使用场景不同。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/fIlW8fmQCtWL1qhN5coK.png" alt width="710" height="332" referrerpolicy="no-referrer"></p>
<p>该如何选择呢？我们需要从3个方面进行考虑：操作效率、标签长度、屏效、视觉对齐。</p>
<p>① 操作效率</p>
<p>根据Matteo Penzo的研究总结得到的浏览时间表发现，标签移动到输入框的时间，顶部对齐最快只要50ms，其次是右对齐240ms，左对齐耗费时间最长500ms。</p>
<p>因此当<strong>以操作效率为主时，推荐使用顶对齐</strong>的方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/1arg4dLfnwCcaJQto3hr.png" alt width="707" height="393" referrerpolicy="no-referrer"></p>
<p>② 标签长度</p>
<p>当标签长度超过8个字，或者需要考虑中英文双版本时，推荐<strong>使用顶对齐</strong>的方式，其容纳的标签文字更多，拓展性更好，比如Ones的建任务的标签，就采用标签顶对齐的方式：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/HUhBU5hE9VsjzybOeZd5.png" alt width="707" height="393" referrerpolicy="no-referrer"></p>
<p>③ 屏效</p>
<p>如果只考虑屏效，那么标签左对齐右对齐均可，但是如果还考虑表单录入效率，那么推荐使用标签右对齐的方式，比如蜂鸟汇报：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/M82w9Az4khtC7HBayDeC.png" alt width="704" height="391" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、颜色主题配置</h2>
<p>Arco的颜色主题配置可以说是让人眼前一亮了，可调整的范围非常广非常牛逼。可以编辑的维度从基础的颜色、字体、阴影、 到组件的按钮、导航、分类、表格 一共有接近40款组件的样式，并且都是可以进行可视化编辑与实时预览的。</p>
<p>如果你用了 Arco 过后，或许不用苦苦地站在前端后面，让他帮忙调整页面，作为设计师自己就能够搞定，并且每一个组件可以调整的粒度是非常之细，包含各种宽度、图标大小、颜色、投影，等等…在这里可以编辑自己的主题，也可以在商城社区查看到别人发布的主题，真的是很方便啊。</p>
<p>真的有些amazing！假如你需要去设计一套官方的设计系统，完全可以通过 Arco 进行设计和预览、落地。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/yF2DDC9noKtic4QoHlVy.png" alt width="706" height="392" referrerpolicy="no-referrer"></p>
<p>Ant并没有做这方面的功能，颜色主题配置这一块确实是Arco很大的亮点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/cjdeItvcCqZO9nRl9l3R.png" alt width="709" height="394" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、总结</h2>
<p>无论是Arco Design还是Ant Design设计系统，都代表了字节跳动和阿里两家互联网巨头公司在B端领域的沉淀和竞争。对于B端交互设计师来说，两个设计系统都值得我们去研究和学习，建议大家都去看看设计规范里面的内容，对于我们认识和熟悉控件以及和开发对接都很有帮助。</p>
<p> </p>
<p>本文由 @晨屹 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5221864" data-author="265625" data-avatar="http://image.woshipm.com/wp-files/2021/10/QC7ndE6f9pjapW9Y0aWy.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            