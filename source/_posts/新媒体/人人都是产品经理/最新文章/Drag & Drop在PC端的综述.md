
---
title: 'Drag & Drop在PC端的综述'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZqS0AGMBQLvjEUFn4tsu.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 08 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZqS0AGMBQLvjEUFn4tsu.jpg'
---

<div>   
<blockquote><p>编辑导读：拖放交互是PC端较为流行的交互形式，有直观、学习成本较低的特点，也有低效率、不精准、甚至容易造成身体上的疲劳。本文作者围绕拖放交互进行了分析，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5129552 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZqS0AGMBQLvjEUFn4tsu.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>对于拖放交互的研究，之前一直是较为模糊的。我一直认为其是较为基本的交互形式，虽然明白有很多的微交互，但是也没有系统的去研究过。所以我希望从底层的拖放交互入手进行一个完整的总结。而后，便有这篇文章，希望能为后面的工作打下基础。若有错误，欢迎纠错谢谢。</p>
<h2 id="toc-1">一、拖放交互的概述</h2>
<h3>1. 优缺点</h3>
<p>拖放交互是PC端较为流行的交互形式，因为符合真实世界的情况，所以非常符合用户的心理模型，有直观、学习成本较低的特点，但是反之也有低效率、不精准、甚至容易造成身体上的疲劳，例如进行长距离的拖放，用户需要一直点击着鼠标长距离移动，若失败了还需要重新开始。所以，针对于拖放的交互，需要保证其有代替的交互形式，例如删除的“delete”、或者是使用空格+键盘方向键的形式移动。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/FDLXKdxbbVanUZgL4ERl.jpeg" width="476" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">删除-mac</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/hFUuQ6c9k8cojbUjrl9Q.png" width="484" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">可以使用键盘移动的控件-salesforce</p>
<h3>2. 拖放的类型</h3>
<p>拖放的类型大致分为两种，第一种针对于物体的大小的改变，即窗口的大小的拉伸或者表格的宽度等；第二种是针对物体的移动，移动也分为应用内移动以及跨应用移动。应用内移动即在单一的应用内，例如修改菜单排序，改变物体分组等，反之，跨应用移动，就是多个应用之间的交互，例如将聊天软件的文本直接移动带文本编辑软件中。针对于被拖放的物体，也分为复制还是单纯移动。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/eJXcMPtRG0QuCVadLl1k.png" width="297" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Ai的物体大小移动改变</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/EsCwsuFZqbGV5svqElvB.jpeg" width="222" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">应用内的菜单移动</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/dI1fsNu868ji9bhxzAZ8.png" width="559" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">跨应用的拖放</p>
<h3>3. 拖放的过程</h3>
<p>针对于整一个拖放的交互流程我自己分为了6个节点：</p>
<ol>
<li>拖放前的识别</li>
<li>触发拖放的行为</li>
<li>开始拖放</li>
<li>遇到接受区域</li>
<li>取消拖放的方式</li>
<li>放下拖放</li>
</ol>
<p>后续对于拖放的交互介绍，我也会按照这六个节点进行阐释。</p>
<h2 id="toc-2">二、拖放前的识别</h2>
<h3>1. icon与文本提示</h3>
<p>拖放交互在各个系统中都较为常见，我们在系统软件中较为常见就是一些文本和图片等的形式，但是对于其他物件的拖动交互，我们需要让用户感知到此物件是可以拖动的。最明显方式是使用icon的进行提示，但是这些图标并没有想象中的那么统一和明确，以下是Norman Group找到的常用的icon。</p>
<p>其中左一的icon与更多的省略号相似，而右一的与汉堡菜单类似（hamburger menu）。最重要的是保证icon在平台内的统一性以及与其他icon的差异性。与icon较为类似的就是文本提示，直接在物体上进行提示，其中Trello的看板中，需要用户拖动链接去操作栏，用户点击send to Trello的链接时，其提示会变大以及变色。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/1eOCxKfvLMw6dXAW1HRY.png" width="465" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Norman Grounp展示的三种icon</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/90vX2D3Q6BAFTKPPjpTL.png" width="353" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Trello的拖放提示</p>
<h3>2. Hover展示</h3>
<p>Hover在日常交互中作为一个重要的反馈。hover的反馈也分为两种：</p>
<p>（1）第一种物体自身的反馈，例如增加阴影：material design中若产生卡片的拖放交互，其卡片一定会增加Z轴的高度，视觉上的反馈是就是增加阴影，使卡片在活动高度进行移动、tooltip：有时为了让用户快速了解到该区域可以拖动，用户首次hover到该物体时也会进行提示。</p>
<p>（2）第二种为光标pointer的提示，例如当光标hover到物体时，光标会改变从而作为一个视觉反馈，以代表其可以被拖放，MAC 常常会用到米奇手的形式，而window是会使用一个双向箭头代表其可以拖动。针对于pointer的反馈，切记保持统一，尽量使用系统自带的形式。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/0EZE9YKif1MZTTLmIhp8.png" width="409" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">卡片的hover，提升Z轴高度到4dp</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/rfFl92l1hFQUeEvLb3qF.png" width="447" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">mac：米奇手；win：双向箭头</p>
<h3>3. 动效引导</h3>
<p>该类交互常用于引导新手用户或展示新功能中使用。一般在游戏交互上使用较多，当用户进入游戏界面，可拖动的物体会有偏移并回弹的小动效；或用于移动端的横向滚动中，在同花顺新改版后，用户进入自选股页面会有一个向右滑动并回弹的小动效，示意可以拖动。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/H0TOAbSkFfHVkOlRX2Vp.jpeg" width="285" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">同花顺自选股</p>
<h3>4. 切勿滥用pointer反馈</h3>
<p>现应用中有很多的对象可以被拖放，所以如果乱用pointer反馈，会造成每当hover到能够拖动的物体时就出现反馈，会造成页面的快速变化从而导致用户的混乱，并且有时在应用中拖放是辅助功能。例如window桌面的文件其可以拖动，但用户主要还是双击打开。如果当光标hover到文件上就是拖动的pointer会让人造成误解。所以，这里建议还是不要滥用过pointer反馈，除非对于物体的主要操作就是拖放。</p>
<h2 id="toc-3">三、触发拖放行为</h2>
<h3>1. 鼠标点击和3像素阈值</h3>
<p>我们光标hover在了希望触发拖放交互的物体上时（源物体），会产生上述的反馈。通常，我们使用鼠标点击并移动，来触发拖放的交互行为（键盘中常用空格），在有些情况下pointer反馈（mac）的米奇手会从展开变为抓紧。但有些时候一个对象既可以点击又可以拖放移动，若用户只有点击行为，依然容易造成物体在应用内超短距离的移动，这样会造成界面物体的颤动。所以，我们需要解决这个问题就应该建立拖动的阈值，当鼠标移动超过此阈值才开始触发拖放行为。在MAC HIG和About face中都设定了3像素的阈值，当移动超过3像素，才开始触发拖放。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZbZ2jL20mRo9LGiTHSZ5.png" width="334" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">米奇手展开（左一）、抓紧（右一）</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/KnOnaw6A50yJLbHhSPkX.jpeg" width="484" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">《About Face》：3像素元素</p>
<h3>2. 触发时，保持窗口不变</h3>
<p>在跨应用的情况下，会存在前后窗口的关系。例如你已经在微信的聊天区域选中了你想要的文字，你回到了word进行了一些文字的编辑，这个时候你想将微信选中的文字拖放进来。这个时候word是你选中的活动窗口，而微信则变成了你的背景窗口。MAC HIG中建议，在背景窗口的选中物体同样能够触发拖放交互，并且触发以及拖放过程中不会改变窗口状态（即word 还是活动窗口，微信依旧是背景窗口）。这样的好处是在跨应用的拖放时，可以保证整体桌面各个窗口的位置、重合关系都不会发生改变，保证前后目标的完整，不会造成拖动的时候因为窗口改动而遮盖掉你预想接受的区域。较大层面上增加了跨应用拖放过程中的交互体验。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/TaniR8JDYN7toqqlzVG3.jpeg" width="372" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">从背景窗口触发拖放，不改变窗口状态</p>
<h2 id="toc-4">四、开始拖放</h2>
<h3>1. 实时与非实时</h3>
<p>在拖放过程中也会分为两种类型，实时与非实时的。实时是指：用户在拖放过程中源物体直接跟着鼠标进行了移动，常用于在某一个特定区域内，物体可以在这个区域内自由移动的情况，例如sketch画布中物体都是实时移动的。非事实移动是指：用户在拖放源物体时，源物体自身保持位置不变，会增加一个跟随鼠标移动的目标物体，例如：在桌面上移动文件夹到回收站中，源物体的自身位置是保持不变的，跟随鼠标的是一个具有透明度的目标物体。</p>
<p>实时拖放常用于像sketch这样的操作画布中，在某一个特定区域的使用，因为这样会将移动与复制区分的更加明显；非事实的情况，则常用于更多的跨区域以及跨应用中使用。因为实时的拖放有一种过程中不可撤回的感觉，所以在其他情况下尽可能少用。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/mOo7KRpUvpgQW1AkELIi.jpeg" width="268" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">非实时移动</p>
<h3>2. 非实时：源物体、目标物体、接受区域</h3>
<p>对于非实时的拖放，会有三个模块：源物体、目标物体以及接受区域。正如上文所述，源物体是被选中，被拖动的物体；而拖动过程中跟随鼠标的是目标物体；接受区域就是目标物体需要拖动到的具体位置，可能是一个区域也可能是一个功能按钮等，在后续我们会详细讲述。</p>
<p>在拖动过程中，源物体还是会保持点击后的状态，而针对于目标物体，Norman Group 提供了四种较为常见的形式：提供一个轮廓或对比色、增加投影、视觉偏移：缩小或者倾斜、半透明。这四种样式并不是互斥的，可以同时使用。其中半透明的形式较为重要，半透明可以保证目标物体的尺寸大于接受区域的时候不会进行遮盖。</p>
<p>而以上情况都是常用于单物体的移动，对于多个物体移动时，MAC 中会使用物体的堆叠图来展示，并且在堆叠图的左上角增加了红色badge的数字统计；Window也会有使用同样方式形成一个正方形的堆叠区域，并且在中心显示数字统计。</p>
<p>对于非实时的拖放，会有三个模块：源物体、目标物体以及接受区域。正如上文所述，源物体是被选中，被拖动的物体；而拖动过程中跟随鼠标的是目标物体；接受区域就是目标物体需要拖动到的具体位置，可能是一个区域也可能是一个功能按钮等，在后续我们会详细讲述。</p>
<p>在拖动过程中，源物体还是会保持点击后的状态，而针对于目标物体，Norman Group 提供了四种较为常见的形式：提供一个轮廓或对比色、增加投影、视觉偏移：缩小或者倾斜、半透明。这四种样式并不是互斥的，可以同时使用。其中半透明的形式较为重要，半透明可以保证目标物体的尺寸大于接受区域的时候不会进行遮盖。</p>
<p>而以上情况都是常用于单物体的移动，对于多个物体移动时，MAC 中会使用物体的堆叠图来展示，并且在堆叠图的左上角增加了红色badge的数字统计；Window也会有使用同样方式形成一个正方形的堆叠区域，并且在中心显示数字统计。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/7t0Jtfve6gqSQJx0IwVY.jpeg" width="541" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Clarity的设计师，对于目标物体增加紫色</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/7PdzbU2UXE3pXIFeQUi2.png" width="559" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">卡片的移动，提升Z轴高度到8dp</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/V4VFHJnWfODlnpuEw90M.jpeg" width="578" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Trello：目标物体有物理性质的倾斜</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/9XFgZTaa1xgKG8GGQPUC.jpeg" width="653" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">window：半透明的目标物体</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/eW4TGS5NVDloPjODp00e.jpeg" width="653" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MAC：堆叠图和badge的计数</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/cKtJGbQtjeEKNeA9zIgN.png" width="653" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Window：堆叠图和badge的计数</p>
<h3>3. pointer尽可能保持箭头</h3>
<p>在拖动过程中，鼠标的pointer尽可能保持箭头。有些场景下，物体在移动过程会保持米奇手的状态或者其他，但是，我们建议在拖动过程中，保持pointer为箭头的状态。</p>
<p>理由如下：</p>
<ul>
<li>箭头（arrow）作为系统默认提供的，其具有很好的扩展性，mac和window中会支持其他的相关于箭头的扩展类型，如Drag coyp的形式就是箭头增加“➕”号，代表复制的意思；</li>
<li>箭头作为鼠标这个精准操作仪器的默认状态，其箭头的含义非常明确，即箭头左上角的尖端位置便是应该触发的区域，其包含了精准的属性，而当使用其他pointer时，例如米奇手就很难界定其精准的区域。所以，针对拖放交互来说，其接受区域是需要被精准点击的，所以我们建议尽量保持箭头的状态。</li>
</ul>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/nneyUuQ8ab1x4EuiSVdt.png" width="222" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MAC：pointers类型</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/YYLFvE0froKOHU5ObSlQ.jpeg" width="206" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Win：复制移动的pointers类型</p>
<h2 id="toc-5">五、遇到接受区域</h2>
<h3>1. 提供接受区域的视觉反馈</h3>
<p>拖放的最终目标就是将目标物体移动到接受区域，对于接受区域也必须有明确的视觉反馈来提示用户移动的是否正确，此区域是否能够接受目标物体等。有时候接受区域是一个容器范围，例如一个文档；有时候接受区域可能是一个功能按钮（导出、打印等等）或者是一个文件夹等等，所以每一个接受区域都应该有自己的视觉反馈。如果页面内的模块、交互较为单一、明确，例如Visio的画布，用户非常明确可以将形状拖放到画布中，可不增加视觉反馈，以免过多反馈造成页面的快速闪动。</p>
<p>针对于接受区域的接受情况，我也分为三种：接受、不接受、部分接受。后续我也会按照这三个部分进行详细的阐述。</p>
<h3>2. 接受</h3>
<p>接受：即接受区域能够放下目标物体。同理最为重要的就是明确的视觉反馈。以下我罗列了6种反馈的形式：高亮、直观预览、横向插入指示器、纵向插入指示器、增加图片清晰度、增加pointer。</p>
<p><strong>1）高亮</strong></p>
<p>高亮的形式较为常见。常用于拖放到文件夹或者某按钮功能时使用，对于小范围的容器也可以尝试使用，例如chrome中将文本信息拖放到地址栏。当接受区域具有较大范围时，请注意谨慎使用，以免过多反馈造成页面快速闪动。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/CPcqajnac3ZfVWGGjQir.png" width="391" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MAC：应用成组时的高亮</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/yiBVX2UPfRvSgX0G19gg.png" width="865" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Chrome：小容器的高亮</p>
<p><strong>2）直接预览</strong></p>
<p>直接预览也是一个较为常见的反馈形式，常用于对于当前物体排序的一种反馈。mac中launch的软件排列就是一个做明显的例子。直接预览是一把双刃剑，其优点就是反馈直接、明确；其缺点就是直接的反馈会导致在拖放过程中页面结构产生快速的调整，造成用户分心混乱，所以，适时的添加delay以及触发反馈的方式是很重要的。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/lSDTNzPCo8dt9WG7OOeY.jpeg" width="372" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MAC：launch软件排序</p>
<p><strong>3）横向插入指示器</strong></p>
<p>横向插入指示器，算是直接预览的变体，其也适用于重新排序，更多用于插入的使用场景。在移动过程中，其不直接对于页面进行直接的重新排版，而是在已有的内容之间插入一条横向的指示器，以反馈其拖放后的位置。其既有较好的视觉反馈，又不会在拖放过程中影响当前的布局，是一个较好的反馈形式。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/d3KK4Mgo7IflAfXAhYYd.jpeg" width="222" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MAC：侧导航插入</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/uUBXbL2KK62NaUkkUgBg.png" width="194" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Window：桌面移动</p>
<p><strong>4）纵向插入指示器</strong></p>
<p>纵向的插入指示器，与横向类似，但其主要用于文本编辑器的场景，但是其本质还是在于容器默认排序的方式，文本编辑是从左至右排序，应该使用纵向的插入指示器，而window的桌面是从上至下的排布则默认应该是横向的指示器。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/801xTk2cdlqXbtZnGeoR.png" width="297" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">文本编辑：字段移动</p>
<h3>3. 不接受</h3>
<p>当接受区域，不接受所拖放的物体时，也必须要体现出适当的视觉反馈，而不是仅仅在可以接受的时候展示视觉提示。mac和windows的系统都会使用一个禁止符号来表示不可放置。在About face中提出，“光标（pointer）的反馈必须在视觉上表明源对象（物体）”，其希望将两者的视觉反馈分开，光标的视觉反馈都代表源物体、目标物体，而接受区域自身来展示是否接受的视觉反馈。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/12Isa4ma3Qpx1t5kIz0d.png" width="409" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">禁止拖放：mac（左）、Windows（右）</p>
<h3>4. 部分接受</h3>
<p>部分接受针对于多物件拖放。上文也提到了目标物体上会存在一个计数的badge，当接受区域仅能够接收部分的目标物体时，请实时更新计数以表示多少物体能够接受。</p>
<h3>5. 触发条件</h3>
<p>针对上述的各种接受区域的视觉反馈，其触发条件基本有三种情况，分别是：（1）光标触发、（2）目标物体触发、（3）增加触发区域</p>
<p><strong>1）光标触发</strong></p>
<p>光标触发，很好理解就是以光标为依据触发反馈。这个触发方式是最为常见的，光标是一个很好判定的标准，具有精确操作的属性（这也是为什么要保持箭头的原因），用户可以很好的利用光标箭头左上角的区域来判定现在所处于的位置，对接受区域较小的时候是很好的标准。在一些树状控件的拖放层级、文件拖放到文件夹等场景下都是较好的选择。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/uKmhTrIB6A3DQZbCVmoq.jpeg" width="758" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">光标触发：未触发（左一、中间），触发（右一）</p>
<p><strong>2）目标物体触发</strong></p>
<p>目标物体触发，一般使用于直接预览的反馈场景，常用的触发基准为物体的中线，Norman Group提到如果使用目标物体的边线来触发的话会导致反馈的过度敏感；如果使用光标来衡量，会导致响应过慢，特别针对长距离以及大物体移动的时候，会导致鼠标移动距离过大造成疲惫；使用物体的中线作为衡量标准，较为符合整体的自然交互形式。其中mac的launch移动就是按照应用的logo中线为衡量标准的。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Da9FMAeVLKnC1rxlLcYX.png" width="203" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">边线触发</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/DC5c5idkV21ZepKib89t.png" width="209" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">光标触发</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/tXlttHIUVM7XAcCU16ZO.png" width="210" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">中线触发</p>
<p><strong>3）增加触发区域</strong></p>
<p>增加触发区域：针对于小范围的接受区域，根据菲兹定律（Fitts law）我知道移动时间与接受区域的大小有关系，针对于小范围的接受区域，我们应该增加触发区域，一种方案是可以依靠增加触发区域从而触发接受区域的视觉反馈；另一种方案是利用增加的触发区域快速将鼠标移动到接受区域已提供一种自动吸附的功能。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/vzQP9vtUUYvOY3q0EpHw.png" width="615" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">增加触发区域以提供视觉反馈</p>
<h3>6. pointer的变化</h3>
<p>当目标物体悬浮在接受区域的时候，pointer会显示出默认状态下此接受区域对于目标物体是移动还是复制，若是移动的情况下，可以利用键盘的快捷键快速的切换成复制，常用是ctrl、option等不同软件、系统都有一定的区别。mac中都是以箭头扩展的形式，而window中的桌面文件拖放时，使用更加明确的文本提示。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/gAyGdSAnNBzACWqCNzqk.jpeg" width="315" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Windows：移动文件</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/kVotjgQ4Nrnrld9e5oeJ.jpeg" width="297" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Windows：复制文件</p>
<h3>7. 目标物体的变化</h3>
<p>目标物体应该展现出在接受区域拖放结束后的样子。当源物体在源区域的展现形式与接受区域的展现形式不同时候，应该更随着hover的区域而变化（需要有delay）。在HIG中讲到，图片被拖放到文本编辑中，目标物体应该在hover到编辑器时，展示出其在文本编辑器中的样子。mac在拖放文件时，目标物体在hover侧导航以及具体文件夹时，会根据当前的接受区域展示的样式而改变自身样式。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/lPxgh7jk72opp87o38NJ.jpeg" width="409" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片移动到文本编辑器</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/x6qXN68ArIeUqxLZgD0i.jpeg" width="409" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">文件移动到侧导航（上）、移动到具体文件夹（下）</p>
<h3>8. 接受区域的移动</h3>
<p>接受区域的移动：其适用于当前窗口仅显示了部分区域的情况，例如：滚动显示的文件夹、一个巨大的画布等，用户在移动目标物体的时候，如果当前接受区域的显示内容与用户的预期不符，我们应该提供在hover状态下能够同时移动接受区域的功能。常用的触发方式就是hover到接受区域的边缘，接受区域应该提供自动移动的功能。其中优化的方式还有，利用靠近边缘的距离来调整移动速度（越近越快）、利用停留在触发区域的时间（越久越快）等等。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/aPQCyfiDCVXcazY1gPse.jpeg" width="477" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">《About Face》：指出windows的文件夹区域的滚动</p>
<h3>9. 改变窗口次序与唤醒窗口</h3>
<p>改变窗口次序，用于跨应用拖放。上文提到在触发拖放的时候不应该调整窗口次序，但是一旦已经拖放到接受区域的时候，为了展示更加完整的接受区域以免被其他窗口遮挡，我们应该调整窗口次序，将接受区域所在窗口调整为活动窗口。但需要注意的是为了避免在拖放路径中改变非接受区域的窗口，所以触发窗口次序改变需要提供较长时间hover的delay。唤醒窗口，用于拖放的接受区域未显示的场景下，例如接受区域隐藏在程序坞中，或开一个文件等，同样的唤醒窗口的触发也需要提供较长时间hover的delay。</p>
<h3>10. 目标物体的精准移动</h3>
<p>目标物体的精准移动，用于需要精准对齐的应用。常用于图像编辑的应用中，《About Face》中提出鼠标的精确滚动，可以利用快捷键加鼠标的形式，让鼠标在移动过程中保持精准移动，例如：鼠标移动10个像素的位置，光标仅移动1像素，但是这样形式的精准滚动也会造成容易在释放过程中，造成少量像素的偏移，这里同样可以设置合理移动阈值所解决。精准移动的模式较为复杂，智能吸附、像素吸附、网格吸附、根据鼠标移动速度调整光标移动的像素等，本文不做展开，同时精准移动也可以利用方向键以及方向键+shift等形式替代。</p>
<h2 id="toc-6">六、取消拖放</h2>
<h3>1. 取消拖放的2种方式</h3>
<p>对于在拖放过程，当用户在没有抬起左键的时候，都有权利结束此次拖放行为（即使结束了也可以撤销），常用的有两种形式（1）键盘的Esc（2）合击（chord-clicking）</p>
<p><strong>1）键盘的Esc</strong></p>
<p>Esc是常规的退出按键，也比较符合用户的心理模型。按下Esc，应该能够保证本次拖放行为的结束，并恢复到原来的样子。</p>
<p><strong>2）合击（chord-clicking）</strong></p>
<p>即鼠标的左键右键同时按下，在拖放过程中，因为左键的按钮一直保持按下的状态，这时按下右键产生合击，从而结束拖放行为，这样的交互形式较为晦涩难懂。</p>
<h2 id="toc-7">七、放下目标物体</h2>
<h3>1. 更新选中态</h3>
<p>当拖放结束后，目标物体被放置在接受区域，应该保持目标物体的选中以表示此次交互结束，之前的源物体（若是复制即还存在）的选中状态应该保持消失。</p>
<p>在HIG中提及到，多容器拖放的事件：“When selected content is dragged to another container, it should become selected in the new location and any previous selection should be deselected.” 在多容器拖放后，应该保持接受区域的目标物体保持选中状态，并删除之前任何源物体的选中状态。但在实际的mac中的两个文件夹中的复制拖放，并没有遵循此规定。个人认为还是应该还是遵循此规定，应该把持目标物体的选中示意着拖放结束这一个完美的线形流程的完结，若想要进行下一次拖放则需要重新选择源对象进行拖放。</p>
<p><img data-action="zoom" class="content_image aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/j967uaS0R2gqMxGTcUqa.jpeg" width="374" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Mac：文件夹复制拖放结束后，并未选中目标对象</p>
<h3>2. 当拖放后启动流程，需提供额外反馈</h3>
<p>当拖放结束后，目标物体启动了新的流程，例如打印、上传、下载等，这时需要提供额外的反馈来表示其启动的进程。例如：百度识图，其在拖放图片结束后会产生识别的额外反馈。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/yxXRK7WaKCUpUnY5eCTH.png" width="728" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">百度识图：接受区域</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/9p2004IxvsJw7llOhVQN.png" width="728" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">百度识图：拖放后的额外反馈</p>
<h3>3. 提取可接收信息</h3>
<p>HIG提出：如果拖放的目标物体包含了多重信息，但是接受区域的仅能够接受部分信息，可以提取可接收信息放入到接受区域。例如将通讯录的个人信息拖放到邮件地址中，邮件仅能接受姓名以及邮件地址，其他的真实地址等信息就会被剔除。</p>
<h3>4. 拖放失败，提供动画反馈</h3>
<p>当目标对象移动到不可接受的区域并释放，其产生的结果应该与上述提到的取消拖放的结果相同，同时需要一个动画效果来反馈给用户拖放失败的信息：目标物体应该会移动回源目标。HIG中将这种动画成为“zoom back”。</p>
<h3>5. 确保操作可逆，若不可逆提供反馈</h3>
<p>当拖放操作完成后，确保整个流程是可逆的。提供撤回以及重做的功能，帮助用户解决错误。若因为业务原因无法进行撤销，在拖放结束后应该进行合理的提示。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/VYGDfi5m29wjHwRRfnxA.jpeg" width="634" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MAC：不可撤回的提示</p>
<h2 id="toc-8">八、总结：优化设计</h2>
<p>本次对拖放进行了一个详细的信息梳理形成一份类似于研究报告的综述文档。正如前言所说，本次拖放的总结一个是弥补了我对拖放整体的交互细节的空缺，另一个部分就是我希望能够基于这个总结，去针对业务的画布进行一个交互上的整体优化以及形成一个简单的规范。</p>
<p>而对于其他拖放场景的优化也可以参考本次的综述文档，例如在收集参考资料的时候也看到了saleforce提供的五种拖放控件（https://salesforce-ux.github.io/dnd-a11y-patterns/#/canvas?_k=nlllw7），其使用过程中会发现很明显的微交互上的缺陷，例如示意拖放的icon不统一性、移动过程中接受区域没有视觉反馈等等的问题，都可以进行优化。</p>
<p>感谢大家能够观看到这里，谢谢。</p>
<h2 id="toc-9">九、参考文档</h2>
<p>Apple Human Interface Guidelines</p>
<p>Microsoft Fluent Design System</p>
<p>《About Face 4：交互设计精髓》</p>
<p>Salesforce Lightening Design System</p>
<p>Google Material Design</p>
<p>https://www.nngroup.com/articles/drag-drop/</p>
<p>https://zhuanlan.zhihu.com/p/407548600</p>
<p>https://www.yuque.com/u2411630</p>
<p> </p>
<p>本文由 @Y.h 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5128157" data-author="868828" data-avatar="https://static.woshipm.com/WX_U_201904_20190417214622_6939.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            