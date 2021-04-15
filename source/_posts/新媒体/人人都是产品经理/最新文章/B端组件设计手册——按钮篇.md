
---
title: 'B端组件设计手册——按钮篇'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/RxGLNzf9g9diYLF4EaB6.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 15 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/RxGLNzf9g9diYLF4EaB6.jpg'
---

<div>   
<blockquote><p>编辑导语：按钮设计在产品中是非常重要的组件之一，并且也是跟用户触发按钮的关键操作，所以设计师在对于按钮的设计时需要注意多种细节和规范，确保用户体验；本文作者分享了关于B端组件设计中的按钮，我们一起来了解一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4468843" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/RxGLNzf9g9diYLF4EaB6.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>我们在工作中经常会遇到各种各样的问题，遇到问题并不可怕，毕竟解决问题也是设计师不可或缺的能力之一，包豪斯“以解决问题为中心”的设计理念也深深影响着现代设计，所以定期的复盘和整理以及寻找解决办法是我们设计道路非常重要的环节，此篇即为设计师遇事不求人自己找答案系列的按钮篇；</p>
<p>回到本文，我们在日常的设计工作中，按钮是比较常见的组件，也是各个终端必不可少的组件之一。本文主要整理B端Web端的按钮的使用，Web常用的组件主要有反馈类组件、表单类组件、基础组件即按钮、数据展示类组件、导航类组件以及业务类组件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/tL2BI7gBMVTZS6cS4iPQ.png" alt width="1920" height="795" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、按钮的概述</h2>
<h3>1. 概述</h3>
<p>按钮是界面设计中比较重要的组件之一，是用户引流和行动触发的关键，用于提示用户按下按钮后将进行的操作，主要由文字和图标组成，可理解为一个操作的触发器。</p>
<p>来看看几个网站的解释：</p>
<ul>
<li>Ant Design：按钮用于开始一个即时操作。</li>
<li>Material io：Buttons allow users to take actions, and make choices, with a single tap；通过按钮，用户只需单击一下即可执行操作并做出选择。</li>
<li>Vant：按钮用于触发一个操作，如提交表单。</li>
<li>View UI：基础组件，触发业务逻辑时使用。</li>
</ul>
<h3>2. 按钮的起源</h3>
<p>按钮的前身是物理按钮，是连接人类与工业产品的桥梁，极大程度降低了人与机器互动的门槛，为人们提供了很大的便利。</p>
<p>1988年柯达公司发明了第一台可拍摄100张照片的柯达相机布朗尼，同时它的创始人伊士曼设计了流芳百世的广告词：“您只需按一下按钮，剩余的我们来做”，广告词言简意赅，并迅速传播开来，可谓开创了摄影文化及物理按钮的先河。</p>
<p>150年后，当今的布朗尼诞生了，也就是苹果iPhone，自07年iPhone初代发布以来，触摸屏逐渐取代了物理按钮成为人机交互的主流形态。</p>
<p>17年iPhoneX发布，手势交互成为大势所趋，虚拟按钮已经逐渐取代了物理按钮；布朗尼也许不是第一款便携相机，iPhone也不是第一款触摸屏手机，但是它们的成就都超越了技术，为各自时代的变革做出了贡献。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/e8VnxH5VYDKwOuNnSxIJ.png" alt width="1920" height="1350" referrerpolicy="no-referrer"></p>
<p>即使到现代，按钮仍是吸引用户点击的组件。触摸或点击按钮即可触发操作。很多家用电器和其他设备的物理按钮变为触摸屏控件，它们形成的行为习惯会继续延续按钮设计的初衷：直观性和易用性。</p>
<h2 id="toc-2">二、按钮的组成和分类</h2>
<h3>1. 按钮的适用范围</h3>
<p>首先我们在设计产品中的按钮时，肯定会遵循或制定设计规范，设计规范就是产品的标准使用说明；统一的设计规范可以帮助设计师提高效率，也可以帮助产品开发测试甚至用户有更好的体验，并降低学习成本。</p>
<p>而企业的规范也会有不同的适用范围，我们做设计时也要根据不同的范围去定义设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/LYQCIkBouhEoCj1vRWmt.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>首先企业级的设计规范，是针对企业整体的品牌调性，是所有产品设计规范的基石；其次某个产品线的设计规范，是在遵循企业级设计规范的基础上，对该产品线上所有产品定制的专属设计语言规范，如品牌形象、设计语言、用户体验等；具体产品规范则指针对具体某个产品，根据该产品的产品特性定制化设计语言；</p>
<h3>2. 按钮的分类</h3>
<p>1）按使用平台分类</p>
<p>日常设计工作中，移动端常见的按钮主要有悬浮响应按钮、浮动按钮及扁平按钮；web端常见的是面性按钮、线性按钮、图标按钮、文字按钮；本文主要以Web端为主，所以移动端不占过多篇幅讲解。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/beob8PfxOJ2JNMiMLSMI.png" alt width="1920" height="645" referrerpolicy="no-referrer"></p>
<p>2）按结构分类</p>
<p>Web端按钮主要用来作为执行下一个操作的入口，一般在执行对象为一个流程对象或者作为操作按钮时使用；Web端按钮样式主要有面性、线性、图标及文字四种；面性按钮一般用在比较重要的场景；线性按钮则用在次重要的操作场景；在使用纯图标按钮时候，一般会在鼠标停留时出现提示；文字按钮一般使用颜色来表示该文字可通过点击链接到下一个操作，且多使用主题色，视觉效果弱于面性按钮和线性按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/vdDpnLxNAkVrHL17quHq.png" alt width="1920" height="983" referrerpolicy="no-referrer"></p>
<p>① 图标文字按钮</p>
<p>图标文字按钮也是较常使用的按钮形式，为确保按钮的语义更加明确，通常会加上文本来注释图标语义；</p>
<p>如何来处理图标和文字的关系呢？</p>
<ul>
<li>图标和文字字体的顶线上下对齐；</li>
<li>图标和文字的杭高上下对齐，另外还要注意图标和文字的视觉重量，适当调整以确保视觉平衡；</li>
</ul>
<p>② 图标文字按钮</p>
<p>顾名思义，面性按钮即为填充底色的按钮，一般用作主按钮。</p>
<p>线性文字按钮和幽灵按钮：幽灵按钮（Ghost Buttons）最大的特点就是透和薄，没有填充底色和纹理，只有边框，既保留了作为按钮的功能性，又具备一定的简约视觉美感。一般用于网站首页，而线性按钮用途则十分广泛。</p>
<p>文字按钮：文本按钮一般用在列表中，常见的样式是加颜色或下划线的链接文本；</p>
<p>图标按钮：图标按钮相比于一般按钮，节省了很大的空间，可以与其他图标按钮一起排列，但是语义不明确的时候，容易造成用户理解偏差。</p>
<p>一般会用下面两种处理方式：</p>
<ul>
<li>图标按钮一般会在鼠标移动到图标上时通过鼠标hover效果展示提示信息；</li>
<li>在为认知度较低的人群设计产品时，建议使用图标文字按钮。</li>
</ul>
<p>悬浮按钮：一般用于移动端，Google Material Design更为常见，看起来像图标按钮，其实是页面中的主要操作按钮；网站也有使用，如飞书。</p>
<p>3）按优先级分类</p>
<p>根据优先级和对应样式分为，主要按钮，次要按钮，辅助按钮，一个页面中应包含有一个主要按钮；当页面总有多个按钮的时候，通常主要按钮和次要按钮搭配使用，B端页面中，由于业务功能比较复杂，有时还会出现多个同等重要的主要按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/6s4q5IUCWmrm4BuPTid1.png" alt width="1920" height="850" referrerpolicy="no-referrer"></p>
<p>4）按作用分类</p>
<p>行动按钮 CTA（Call To Action）行为召唤按钮。</p>
<p>在日常生活中，常见的CTA有商场里的产品销售模式，比如宜家的“请躺下试试”、“打开抽屉看看”，迪卡侬使用了“请试穿 Try Me”等来召唤邀请用户，而用户只有在试用体验后才有可能转化为真正的用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/2jtHJ2Z4nm71sKrQeCvn.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>在互联网行业，CTA同样有很多的应用，如在按钮、文案、图标等很多组件元素中，正确合理的使用行为召唤，可以为产品带来更高的转化率和收益。</p>
<p>行动按钮是连接用户和产品的交互点，在产品设计中扮演重要的角色，可以有效引导用户进行下一步操作，提高交互效率，提升交互体验及产品转化率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/NHwQNhOVoIwyBWCqxKjm.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>功能按钮：例如加减折叠等，主要用于交互场景。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/yrVYl0UXCvT7XO13A02D.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>基础功能按钮：主要指在各个系统中都通用的基础操作，如打开、关闭、读取数据、计算、复制、保存、删除等基础性操作。</p>
<p>管控按钮：主要指除去基础功能之外的功能，如对业务标准、管理规则等等进行检查，将业务处理的结果与设定的规则进行比对，如与规则不符，则给出相应的处理，如：询问、提示、警告、终止、通知等操作。</p>
<p>常见功能性按钮：</p>
<ul>
<li>新增——界面上新增一条数据的功能；</li>
<li>查询——查询历史数据的功能；</li>
<li>修改——修改已有数据的功能；</li>
<li>保存——将输入的数据保存到数据库的功能；</li>
<li>提交——完成业务处理后发出通知（包括走审批、转向下个流程节点）。</li>
</ul>
<p>两者关系：不同的按钮，功能也不尽相同，对应的要处理的业务也都不一样，将规则与按钮绑定后，可以在不同的业务处理阶段的结果进行相应的管理操作，点击按钮亦是激活管理规则。</p>
<h3>3. 按钮的组成</h3>
<p>1）按钮的组成</p>
<p>按钮用于提示用户按下按钮后进行操作，主要有三个部分组成：按钮容器，图标和文字，其中容器又包含了容器的大小，填充/描边颜色，以及圆角，如图所示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/nXcFVc043i3CAxG3VU67.png" alt width="1920" height="616" referrerpolicy="no-referrer"></p>
<p>2）影响按钮的视觉元素</p>
<p>设计按钮要有主次区分，根据信息传递的优先级，利用视觉元素（大小、颜色、填充、描边、饱和度等）来表现按钮的等级。</p>
<p>① 容器圆角</p>
<p>通常选用全圆角或者小圆角，小圆角一般为高度的1/4以内。圆角传达了一种简单、乐观、开放的感觉；它始于移动端，后面逐渐应用于Web端；很多设计系统都在使用圆角，并在图标、按钮、插画中广泛使用应用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/yj77J2FLHlwf1QBOzvSg.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>全圆角按钮在界面中会更突显，更容易引导用户注意进而点击按钮操作。例如音乐界面中的全部播放和暂停按钮；</p>
<p>② 容器填充或描边</p>
<p>通常大部分的按钮会使用品牌色，并使用一些辅助色来形成差异化，但是红色和橙色具有刺激行为的作用，不适合在非品牌色时滥用。浅灰色和低饱和度的颜色会给人一种按钮不可用或者禁用失效的感觉，需酌情使用。</p>
<p>颜色可用性：</p>
<ul>
<li>我们在设计产品时，要考虑颜色的可用性，以确保又视觉障碍的人群可以使用我们的产品，可使用accessible-colors查看对比度，确保按钮可读性；</li>
<li>另外设计按钮时，要考虑状态色和主题色的区分，比如红色橙色黄色等用于警示的颜色；</li>
</ul>
<p>③ 容器阴影</p>
<p>投影颜色一般选择与按钮同色系，这样看起来会更通透，不显脏。</p>
<p>投影虽然会使按钮看起来更有层次感，但是一些浅色按钮使用投影后，反而会降低投影的辨识度，看起来不够干净清爽。</p>
<p>④ 容器形状</p>
<p>按钮的存在是为了引导用户操作，如果只是为了凸显设计使用异形按钮，打破用户习惯；反而会让用户对下一步的行为产生困惑，这个形状到底它到底是个啥，是不是按钮，能不能点击，如果点击了会有什么后果。</p>
<p>⑤ 容器尺寸</p>
<p>按钮大小要便于用户进行点击操作，对于大多数平台，无论屏幕大小，触摸区域至少达到48X48dp，物理尺寸约为9mm，不同热区之间的间距应为8dp，一般如果按钮文字大小不小于极限值，按钮的交互热区都会满足点击需求。</p>
<p>如果是只有图标的按钮，不仅要确保按钮大小合适，也要确保交互热区满足点击要求。</p>
<p>麻省理工触摸实验表明，在使用触摸屏时人的手指部分尺寸时8-10mm，如果希望避免用户触摸错误，最小按钮尺寸应大于或等于10mm，而鼠标光标比手指接触触摸屏时的接触面积小很多，因此web端按钮可以偏小一些。</p>
<p>点击按钮是一个简单的任务，如果用户不能成功点击按钮或误触相邻按钮，会给用户带来负面体验并浪费更多的时间。</p>
<p>对于图标按钮，需确保触摸区域大于元素的本身大小，不仅在移动端或平板上如此，在web端也应如此。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/mmIzwSdrhw3XumoQAQxd.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>设计按钮的时候不应对按钮的尺寸做限制，按钮是产品系统中的一部分，按钮的大小对界面的可访问性会有一定的影响，因此我们在设计按钮的时候，宽度和高度都应有一定的标准。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/RiUP3SbzhEuO1YFmXShf.png" alt width="1920" height="945" referrerpolicy="no-referrer"></p>
<p>高度上应根据字体的行高，再添加标准单位的倍数间距，一般最小单位为4px，原因有两个：</p>
<ul>
<li>有视觉障碍的人可能会放大浏览器的页面，这时页面字体会变大，如果按钮尺寸定死，按钮文字就会超出按钮容器；</li>
<li>前端在创建按钮的时候，会在div容器中添加内间距，而不是固定高度；</li>
</ul>
<p>水平内间距，有两种方法：</p>
<ul>
<li>使按钮的宽度和网格对齐，这样所有的按钮长度都可以保持一致，但是它对按钮文字有一定限制；</li>
<li>两侧固定内间距，并设定按钮的最小宽度，这样可以在一定程度上避免过窄的按钮出现，但是不同字段按钮的长度也不同，当很多按钮在一起的时候，看起来会有些不均匀；</li>
</ul>
<p>还有一种方法是使用大写字母W（字号同按钮文字）来确定边距，垂直水平内间距都至少为1W，为了提高可读性，水平内间距一般为2W；</p>
<p>⑥ 图标</p>
<p>按钮中图标需要统一设计并保持一致，图标的线条粗细尽量和文字的笔画粗细保持一致，更显细节。</p>
<p>虽然纯图标按钮显得干净简洁，但是还需要考虑图形能否准确表达含义、传递信息，是否会引起用户误解或者认知错误。</p>
<p>⑦ 文本</p>
<p>按钮文字：</p>
<p>一定的留白会使按钮看起来更有呼吸感。可以分析一些按钮的负空间，看看按钮文字与按钮容器中负空间之间是否存在一些比例关系，并将这些关系运用到按钮设计中，这样我们的设计也许会更加的理性和有理有据。</p>
<p>一致性：</p>
<p>我们在产品设计前期，需要制定按钮标签的规范，以免后期花费更多的时间去修改所有的按钮；大多数按钮都包含指示文字告知用户下一步将执行什么操作，一般建议使用“动词+名词”结构，如：保存文章，而不是保存，这样按钮文本会更具有规范性以及语义明确。</p>
<p>按钮文本言简意赅：</p>
<ul>
<li>尽量不要换行，一行之内显示；</li>
<li>好的文案会引导用户进行操作；</li>
<li>按钮上的文案与样式一样重要，错误的文案会使用户感到困惑，甚至会导致错误操作；</li>
<li>好的文案会引导用户操作，并且最好包含动词，以及准确的表达操作目的，避免使用是、否或通用词语。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ig51cazIlloWj53mBFa3.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>⑧ 一致性</p>
<p>为了降低用户在操作过程中的理解成本，设计按钮的时候也要注意一致性，比如同一板块的按钮尽量大小和风格一致（比如圆角的大小，按钮形状的大小）。</p>
<p>非按钮文字，比如标题不要设计成按钮的样式，以免对用户错误的引导，产生误操作。</p>
<p>⑨ 主次分明</p>
<p>通过视觉效果凸显主要按钮，弱化次要按钮和辅助按钮，以引导用户操作。</p>
<h2 id="toc-3">三、按钮的状态</h2>
<h3>1. 按钮的不同状态</h3>
<p>按钮不同的状态可以给予用户不同的反馈，可以让用户了解产品按钮是否可以点击，已经点击或者已经成功点击。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/LbJ0JSBUDOz9ZH2OmIee.png" alt width="1920" height="948" referrerpolicy="no-referrer"></p>
<ul>
<li>正常-表示该组件是可交互的，也就是正常页面总的显示效果；</li>
<li>焦点-当用户使用选项卡时，需要有一个“焦点”状态告知用户按钮是可点击或者未点击状态，使用键盘或其他输入法传达用户已突出显示元素的信息</li>
<li>悬停-当用户将鼠标置于按钮上方时显示的状态，移动设备和平板电脑不会出现悬停状态；</li>
<li>活动-按下状态pressed，表示用户已使用鼠标或手指轻按按钮时的状态，当用户释放鼠标或者手指时，按钮会出现已点击状态。处理方式：增加10%的暗度；</li>
<li>进度/加载-在不立即执行操作并通知组件正在完成操作的过程中使用。</li>
<li>已禁用-表示该组件当前处于非交互状态，但将来可以启用；一般用于信息未填写完整，或者未达到使用条件时会出禁用状态；颜色使用建议：一般使用灰色或者降低不透明度，把正常状态做弱，提醒用户避免做无效点击；</li>
</ul>
<p>相信每个人都遇到过这种情况，对当前进度产生困惑，花费了一些时间去思考，为什么操作进度被禁用按钮阻止了， 我们需要做什么才能恢复原来的可交互状态。</p>
<p>建议尽可能避免使用禁用按钮，如果用户未提供必填信息，只需突出显示未填信息或者显示消息提示通知。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/4EUm2X7Q0GNZXXwrZe7l.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>使用场景：</p>
<ul>
<li>界面内容已通过审核，不可再编辑；</li>
<li>操作用户没有编辑权限；</li>
</ul>
<h2 id="toc-4">四、如何选择正确的按钮</h2>
<h3>1. 关于按钮的使用规则</h3>
<p>1）并不是所有时候都有默认按钮</p>
<p>我们通常会将最常用按钮设置为默认按钮（主按钮样式），并置于焦点状态；以便引导用户更快的完成任务。</p>
<p>但是，当所有按钮的重要程度都相同时，或者是危险操作时，这种情况下需要用户慎重选择，而不是做区分导致用户误操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/wpms3hxcG6oLNo8w2be3.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>如果可交互元素和不可交互元素使用来相同的样式，用户就会疑惑，不知道哪里可以点击，哪里不可以点击。</p>
<p>2）不要让我思考</p>
<p>界面对用户来说应该是清晰明了的，而不是让人困惑的，经过多年的各种设备和产品的训练，用户对按钮的认知已经有了一定的认知，如果偏差较大，会让用户产生困惑从而花更多的时间来思考。</p>
<p>3）一致性有助于提高效率和准确性</p>
<blockquote><p>“一致性是最强大的可用性原则之一：当事物始终表现相同时，用户不必担心会发生什么。”——雅各布·尼尔森（Jakob Nielsen）</p></blockquote>
<p>使用一致性，有助于用户高效并且准确的在产品中实现其目标；我们在做设计按钮的主要、次要和第三种样式的时候，尽量使用一些常见的样式，不仅要在设计系统内保持一致，也要考虑到整个平台的一致性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MuzrNPcGV70XHWnjrsZK.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>4）无障碍设计</p>
<p>影响可访问性的因素有很多，比如热区大小，字体 大小、颜色和对比度等，有很多工具可以用来检查组件设计的性能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/66AYlifKmLH5efZa4i3h.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<h3>2. 适配不同的场景</h3>
<p>1）不同设备</p>
<p>不同的机型，要考虑按钮的上下衔接，以便给用户带来更好的体验。</p>
<p>2）不同主题模式</p>
<p>确保按钮的可读性，需要考虑在不同环境下的适应度，现在很多产品都适配了深色主题模式，按钮的配色不能只考虑白色或浅色背景下的运用，还需考虑深色模式，确保按钮与背景的对比度和可读性。</p>
<p>3）主按钮的左右位置</p>
<p>不管是什么选择，都有相应的理论依据支撑，并且不管选择哪一种，都不会出现严重的可用性问题，所以，不管最终作何选择，相信我们都会有自己的理由。</p>
<p>Windows系统系统将确认按钮放在左边，Mac OS系统习惯将确认按钮放在右边，用户使用不同的系统，行为习惯也会有所不同。移动端倾向于将引导用户操作的按钮放在右边，吸引用户点击。</p>
<p>用户对弹窗中行动按钮的认知一般为左退右进；平台上iOS和mac OS一般均为左退右进，而Windows和Android为左进右退，Android4.0发布以后也改为退右进模式，更贴合用户心智模型。</p>
<p>为了防止用户误操作，通常会将确认按钮放在左边，通过助力设计让用户再次确认；我们在做设计的时候既要考虑操作不同系统的使用习惯，也要结合用户的习惯，将按钮放在合适的位置以便用户操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/NMa4Tk0rQIo1inNyE5tJ.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<p>针对按钮位置左的A/B测试结论：</p>
<p>Walker 和 Stanley 的两人针对这个问题做了对比研究实验，实验结果告诉我们，不要违背用户使用习惯；因为曾经有人做过实验，在操作性条件学习的初期，行为是具有目标导向的，会根据行为结果灵活调整；而在过度学习后，行为转变成习惯行为，模式固定，不易改变。</p>
<p>习惯行为是一种经过长期重复形成固定动作，不需经大脑思考，自动执行。</p>
<p>首先用户的习惯是点击右侧按钮，当主要按钮在右侧的时候，会更加引导用户习惯性的点击，当处于A选项时，主按钮位置与用户心理预期位置不符，用户会稍微停留一下，思考主按钮和次要按钮的文案内容，再去点击。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/XxFhiPbH4OkBRo5pANhO.png" alt width="1920" height="705" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、总结</h2>
<p>按钮是界面设计中比较重要的组件之一，是用户引流和行动触发的关键，用于提示用户按下按钮后将进行的操作。</p>
<p>本篇文章整理有不够详尽之处，后面会继续更新补改；另外带着问题和目的找答案，并将答案整理归纳，才能尽可能将我们见到的知识内化为自己掌握的本领。</p>
<h3>参考文章：</h3>
<p>https://www.iyunying.org/ue/2816.html#group=nogroup&photo=1</p>
<p>https://material.io/design/environment/elevation.html#depicting-elevation</p>
<p>https://uxdesign.cc/is-it-ok-to-grey-out-disabled-buttons-8afa74a0fae</p>
<p>https://uxdesign.cc/button-design-user-interface-components-series-85243b6736c7</p>
<p>http://www.woshipm.com/pd/4175418.html</p>
<p> </p>
<p>本文由 @婷婷与li 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4461816" data-author="700894" data-avatar="http://image.woshipm.com/wp-files/2021/04/6kj6n0O6GtqUwV9oJjNr.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            