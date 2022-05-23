
---
title: '日历APP概念设计的5个阶段'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/02/0Sa8DF2PwiuGoyHVojYq.png'
author: 人人都是产品经理
comments: false
date: Thu, 26 Dec 2019 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/02/0Sa8DF2PwiuGoyHVojYq.png'
---

<div>   
<blockquote><p>就像文中作者说的简单的东西往往需要精心设计而变得简单。这是一篇很详细、完整关于一个产品实现的过程，可以学到如何灵活应用设计方法论结合思考去做设计和产品。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/02/0Sa8DF2PwiuGoyHVojYq.png" referrerpolicy="no-referrer"></p>
<p>人们定期使用日历。每天有很大比例的人不止一次使用它们。</p>
<p>日历帮助你安排日常行程并且跟踪你的“待办事项”。另外，它还是一个很好的时间管理工具。</p>
<p>日历看上去可能是个很简单的应用，但当你开始重新研究它时，你会发现这个主题会变得相当的概括。</p>
<p>在使用日历时，我沿用去尝试改进用户体验的方法论是：<strong>双钻石</strong>(The Double Diamond: 是英国设计委员会于2005年开发的设计过程模型的名称。它表明设计过程应分为四个阶段：发现、定义、开发、交付)。我有一周的时间去研究，一周的时间去制作最终的原型。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/gMNnF12Q7MfwpYPo0J2w.jpeg" width="800" height="571" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“双钻石“示例图</p>
<h2 id="toc-1">01 探索阶段</h2>
<p>我决定从桌面研究 (Desk-Research) 开始进入这个主题。刚开始我用基准化分析法(Benchmarking) 来研究市场，发现潜在的竞品并且分析他们正在做些什么。比方我进入Google play后下载各种日历应用程序，使用他们然后对它们的使用表现、包含功能和UI界面美观等方面进行记录。</p>
<p>我还研究了移动端和网页日历之间的差异，来帮助我理解如何在不同平台之间综合信息。除了专注于研究日历相关应用，我还查找了其他工具，这些工具可能潜在一些功能点是可以借鉴在最后的产品里的。</p>
<p>这些具有激励意味的应用程序包括：BeWet, Drink Water Reminder 和 Water Drink Reminder；体育类应用程序例如：Runastic 和 Sportstracker，其他项目追踪类应用程序如：Ovuview。</p>
<p><strong>桌面研究</strong> (Desk-Research): 为市场调研术语，对已经存在并已为某种目的而收集起来的信息进行的调研活动，也就是对<strong>二手资料</strong>进行搜集、筛选，并据以判断他们的问题是否已局部或全部地解决。</p>
<p><strong>基准化分析法 </strong>(Benchmarking): 就是将本企业各项活动与从事该项活动最佳者进行比较，从而提出行动方法，以弥补自身的不足。</p>
<p>我做了一个小小的网络志 (Netnography) —— 直接从用户评论的部分收集有价值的发现内容。</p>
<p><strong>网络志</strong> (Netnography) : 从词的组合上来讲有两部分，即“网络”(net)和“志”(-nography)。网络(net)是指互联网(Internet),而志(- nography)是ethnography的缩写。是一种源于人类学的在线研究方法，被用于当代数字通信环境中的社交互动。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/E9eM6r1TV2MzvZIE4GL3.png" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“网络志“示例图</p>
<p>在所有的意见当中，我发现用户最关注的点是：</p>
<ul>
<li>可以选择他们想过的节日( 例如：你来自德国，但是你居住在意大利。所以你也想了解意大利的节日活动)。</li>
<li>非常容易同步和分享活动。</li>
<li>能够（针对某天）添加任务。</li>
<li>我选取了一些包含很多有趣的功能同时用户也非常喜欢的应用程序：小米日历 (OS系统) 、谷歌日历、Ovuview、Sportstracker和iOS系统日历。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/IEBsIwvQiaaVlXnScBau.png" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“用户喜欢日历应用程序“示例图</p>
<p>通过Lightning Demos的调研方法，我绘制了一些特别的、可以深入研究的功能草图。例如：谷歌日历的用户非常喜欢能够清晰区分不同任务的月概览设计。而小米日历具有独特的简约风格。</p>
<p>ios日历的用户认为根据他们设置的活动地点时间来获取通知是非常有用的。虽然一些功能没有包含在我的草图里，但在之后的设计里，我是希望能够包含像应用程序Ovuview一样对过去和未来的日期有着明显区分的功能。这也是其中一个为数不多的有差异的地方。</p>
<p>Lightning Demos: 是一种快速的设计调研方法，通过快速调研相关产品（半小时左右），列出三个启发灵感的产品或者服务功能, 通过文字或者图形的方式记录下来。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/u1NvV02evQQN8xhkGBdK.jpeg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“草图“示例图</p>
<p>在这初次的产品接触之后，我整理了一系列的研究问题，帮助我们挖掘有价值的内容，也为了便于之后访问用户：</p>
<ol>
<li>是否可以追踪到用户他/她的行为足迹？</li>
<li>是否可以追踪到用户她的生理日期？</li>
<li>是否有权限访问用户的月历？</li>
<li>是否可以同步用户其他的日历？</li>
<li>是否可以同步用户的电子邮件账户？</li>
<li>是否可以同步用户在不同地区的假期 (本国、马德里、卡斯蒂亚莱昂…)？</li>
<li>是否可以共享用户日程事件给他人？</li>
<li>用户是否可以设置不同类型的日程事件通知呢？</li>
<li>用户是否可以批量编辑日程事件？</li>
<li>用户是否可以自定义日历的风格？</li>
<li>用户是否可以通过分类来划分日程事件？</li>
<li>用户是否可以快速的更改日历？</li>
<li>是否用户无需无限地滚动就能在日历上搜索到特定的日期？</li>
<li>是否用户需要所有日历的汇总概览？</li>
<li>是否用户可以在一个地标上加入地图，来帮助他到时找到这个位置？</li>
<li>是否用户可以添加挑战的选项？</li>
<li>是否用户可以划掉已经完成的活动/日程事件？</li>
<li>是否能够在视觉上让用户清晰的区分过去、当前、未来的日期？</li>
<li>是否用户可以预先设置日历？</li>
<li>是否用户可以自定义添加日历呢？</li>
<li>是否用户可以看到他/她的目标事件进度条？</li>
</ol>
<p>我进行了一系列的用户访谈并且制定一份表格去了解其他人在他们使用日历过程中的看法和意见。我希望从一个局外人的角度来看待用户对当前市场上产品的看法，以及他们觉得自己缺少了什么。</p>
<p>为了让这个主题能够获取更多有价值的发现，我整理了一份表格发给大家。78.6%的受访人群几乎每天都使用日历，这是相当高的比例了！因此，我认为给予这种工具应用这么多重视是重要的，何况它本身就值得。</p>
<p>该表格显示，大多数用户喜欢用日历去管理工作和个人日程事件。我从这些表格中得到一个有趣的发现，50%的用户使用桌面操作系统日历，92%的用户使用手机操作系统日历。在这些用户当中，35.7%的人使用电子邮件提供的日历。这意味着，有相当多的用户没有找到更好的日历应用程序。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/HXgQBNIngUptTe0N9MTe.png" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p>“调研数据“示例图当被问及是否觉得缺少一个更完整的日历应用程序时，有7%的人回答：是的，28%的人回答：可能吧。</p>
<p>当被问及功能时，100%的用户赞同他们都想要划掉已经过去的事件或完成的任务。同时大家都希望有一个更好的事件总览页面，并且可以分享事件给其他用户。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/yes3IVSmIzmYWFyvQeex.png" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“调研数据“示例图</p>
<p>在完成这些工作之后，我创建了用户画像 (User Personas) ，来帮助我把所有的信息进行梳理，以便更好地理解用户需求。</p>
<p>尽管采访的用户中没有一个使用日历来追踪运动或饮食，但我还是决定在我的用户角色当中加入这项功能，因为我的目标是改变普通日历不包含此功能的现象，并在之后的设计提案当中加入这一功能。</p>
<p>用户画像 (User Personas）: 基于研究中实际用户的典型使用行为、动机和目标而建立起的一种合成人物模型。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/jCyXVfdZT66PThoSiqCg.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“用户人物模型“示例图</p>
<p><strong>从目前的研究中，我得到了以下的发现：</strong></p>
<p>用户想要：</p>
<ul>
<li>自定义活动。</li>
<li>添加任务和事件。</li>
<li>同步日历。</li>
<li>共享事件。</li>
</ul>
<p><strong>我收集了以下有建树的意见：</strong></p>
<ul>
<li>加强过去和未来日期的区分。</li>
<li>划掉任务和事件。</li>
<li>将活动与目标分开。</li>
<li>添加进度条。</li>
<li>目标跟踪的指标。</li>
</ul>
<h2 id="toc-2">02 定义功能</h2>
<p>为了定义未来解决方案的功能，我开始比较之前选择的日历应用，它们事件概览页面的不同之处。从整体上去深入研究用户他们喜欢的这些应用程序的功能。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/4wYykMVtXp6lPnO3JEXF.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“定义功能“示例图</p>
<p>我进行了启发式评估分析 (Heuristic Analysis) ，以便确定哪些功能是最突出的，哪些是可以被改进或简化的。需要指出最重要的一点就是谷歌日历的 “目标选择”，这是一个非常棒的功能，允许用户去追踪他们的目标。</p>
<p>谷歌日历目前区分了活动、目标和提醒。这也是我之后打算要实现的功能。通过试图简化过程、减少步骤的数量，来避免对用户的认知造成负担。这也是我想在这方面去保持一致和标准。</p>
<p><strong>启发式评估 </strong>(Heuristic Analysis) : 对计算机软件进行易用性检验的一种方法，旨在用户界面设计的过程中找到易用性方面的问题。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/9QBWELBJC8UtaUkJTHRQ.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“Heuristics“示例图</p>
<p>我把应用程序的反馈给标记下来，去看看我的设计当中需要添加什么。对我来说，真正重要的事情是探索UI界面的美观性和从极简主义中获得启发。因为有些日历看起来是非常的粗糙和拥挤的。当新增功能时，保持干净的设计是非常困难的。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/Te42Slh8ut44AcP1Ji7m.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“干净界面“示例图</p>
<p>在研究这个的时候，我进行了一次MoSCoW的调研，帮助我在应用程序中更加清晰地确定重要的功能。我根据用户需求，选择放在应用中的功能主要有：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/ioWpkk9YZ00ApAl2eWMB.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“MoSCoW“示例图</p>
<ul>
<li>导入</li>
<li>共享</li>
<li>同步</li>
<li>划除</li>
<li>分类</li>
<li>自定义通知</li>
</ul>
<p>同时，我认为如果可以定制化自己的日历去记录和挑战更高目标。这可能对用户来说，是非常有吸引力的 (例如多喝水)，或者生理记录 (例如女生的生理期)。</p>
<h2 id="toc-3">03 开发产品</h2>
<p>我通过一些草图来整理之后的设计解决方案，并且选择最佳的视觉形式去呈现。在这个过程中，最困难的事情是不超出负荷的设计下去添加功能。我根据草图绘制出了第一个线框图 (Wireframes)，从视觉上进行优先级排序，哪些界面是需要被设计的、哪些是不需要被设计的。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/rE1bSSMyBwn0VloRcI1P.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“线框图“示例图</p>
<p>我更加深入地研究了月日历下如何明确区分过去、现在和未来的日期。为此，我还创建了中等保真原型图 (Medium Fidelity Prototype) ，并进行了一些树测试 (Tree Testing) 去了解哪种解决方案会更符合用户的视觉感受。</p>
<p><strong>中等保真原型图</strong> (Medium Fidelity Prototype) : 功能有限但可单击区域的原型，可显示应用程序的交互作用和导航可能性。</p>
<p><strong>树测试</strong> (Tree Testing) : 一种用于评估网站主题可查找性的可用性技术。它也被称为反向卡片分类或基于卡片的分类。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/JjRIVCM4guUnyh5BP3Nn.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“日历视觉设计“示例图</p>
<p>我不得不考虑很多种方法来实现”划除“功能。我围绕这个特定的功能画了很多草图，以便从所有可用选项里选出最佳的方案。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/u7yyWFcjAlONSwVLOGOw.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“划掉功能“示例图</p>
<p>到最后我还为新的日历应用程序快速建立一套品牌系统 (Branding System)。创建的色板是为了找到柔和、中性的颜色，在选择颜色范围时要考虑的一件事就是远离经典的蓝色色板，这在数字化设计中是非常典型。</p>
<p><strong>品牌系统 (Branding System):</strong> 是元素的集合，这些元素共同创建统一，一致且灵活的品牌资产，从而将品牌价值有效地传达给目标受众。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/81fjeDMra5rj5hsnOwr4.jpeg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“品牌系统“示例图</p>
<p>该商标以一只山羊作为毅力的象征来传达品牌含义。“Chivo”这个名字在西班牙语中是“Cabra“，同为“山羊”的意思。因此，通过风格、组合的图像和字体构成了这样一个年轻、动态的商标。</p>
<p>该应用程序的字体选择的是Roboto字体的 Medium和Regular字形，主要是因为它在数字化格式上具有更好的拓展性，并且它很符合品牌的整体外观形象和感觉。</p>
<h2 id="toc-4">04 方案交付</h2>
<p>Chivo是一款全新的日历应用程序，它可以让你以一种简单的方式去记录你所关心的事情。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/wCkEmCQfoYeK7avzBvU0.jpg" width="605" height="487" referrerpolicy="no-referrer"></p>
<p>“Chivo应用程序“示例图你是否曾经发现自己的日程表安排得满满的，以至于很难记录下你所需要做的事情呢？</p>
<p>Chivo可以根据你的喜好去创建单独的日历。你仍然可以看到所有事件与目标的典型概览。但现在如果你想，你可以专注于其中的一个分类上。这意味着，如果你只想关注你的健身日历上，那么你就可以选择查看健身日历这分类。同样你也可以选择查看工作日历或者其他的日历，如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/yDYuW1B9mRELTXnIRrc2.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“Chivo应用程序“示例图</p>
<p>你可以在左上方的汉堡菜单上找到你所创建的日历。在与真实用户进行了一些交互上的实验之后，我创建了一个加速器，来鼓励用户通过向左或向右滑动来更改日历。</p>
<p>在大多数日历中，当你向左或向右滑动时，其实你是在改变月份。而在Chivo你是在进行日历的滚动切换。而通过垂直划动，用户可以进行月份切换。如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/79s2qsU1ZxdtvLPUQ4dV.gif" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“Chivo滚动效果“示例图</p>
<p>当创建新事件时，我在ios日历中添加了一个已经存在的选项，可以根据你的旅行时间来得到对应的通知。如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/4WquTaJW6ORMOEEMKKFB.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“创建新事件界面“示例图</p>
<p>我注意到启发式和创建反馈信息可以让用户了解在应用里将会发生什么。例如：如果你在健身日历上创建一个事件，但是它和工作日历上的一个事件是同一天或者是同一时间点，那么会出现一个弹窗来告知你。在这弹窗里，你可以选择以任何方式创建它或者取消和修改日期/时间。如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/YYNH0flJda8uvw999gpT.jpg" width="608" height="485" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“弹窗内容“示例图</p>
<p>Chivo还能区分事件和目标。事件是典型日历输入方式，而目标是一种可以推迟的灵活输入方式。Chivo从你的目标中收集信息，并向你展示数据图形，以便你继续追踪正在做的事情。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/3lKol7TKH5j0xp5xwXdH.png" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“添加事件/目标“示例图</p>
<p>如上所述，我简化了创建目标的过程。我通过创建遮罩来减少创建目标过程中步骤/界面的数量。这让用户回到他/她通用的目标或编辑界面，并且可以让他/她很清楚的了解到正在做的事情。如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/2LVRgE2P8VapUQQxZWXe.jpg" width="800" height="auto" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“创建新目标的界面“示例图</p>
<p>结合用户希望能够划掉事件和目标的需求，我在Chivo中实现了一个允许用户去标记逐渐完成事情的功能。该功能通过在日历中添加一个进度条，来帮助用户清楚参看日常任务完成的状态。如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/12/t91Rfkm1IYEv7LShSKDV.jpg" width="600" height="541" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">“标记逐渐完成事件的功能“示例图</p>
<h2 id="toc-5">05 未来规划</h2>
<p>由于时间的限制，我不得不省略了两个将来可能会非常有趣的功能：能够添加挑战之类的功能以及能够追踪女性生理期。</p>
<p>我从没有想过，创建一个日历应用程序会如此具有挑战性。但是我想，简单的东西之所以操作简单，真是因为他们经过精心设计的。</p>
<p> </p>
<p>原文作者：Carlota Anton</p>
<p>原文地址：https://uxplanet.org/rethinking-a-calendar-def7711c8b02</p>
<p>编译作者：不喜处，杭州UI设计师</p>
<p>评审指导：TCC委员团 胖鱼、呵呵、弹跳；编辑整理：三分设运营编辑 皮皮</p>
<p>本文由 @三分设 翻译发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="3198113" data-author="719867" data-avatar="http://image.woshipm.com/wp-files/2020/04/GJMm6mJS8RLrwBroDbkk.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            