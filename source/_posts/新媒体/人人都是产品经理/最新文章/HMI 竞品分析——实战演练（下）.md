
---
title: 'HMI 竞品分析——实战演练（下）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/CBpjhkCLnEsgs8Jhx2S0.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 08 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/CBpjhkCLnEsgs8Jhx2S0.jpg'
---

<div>   
<blockquote><p>编辑导语：当下市面上的HMI语音交互都做得怎么样？本篇文章里，作者就对市场上常见的HMI语音交互产品做了使用分析，并提出了自己在语音交互上的设计看法，不妨一起来看一下，也许会对你有所启发。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5346163 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/CBpjhkCLnEsgs8Jhx2S0.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、语音交互分析</h2>
<p>上一篇文章我们结束讲到了中控手势的分析，这一篇从语音交互开始讲解，如果上一篇还没有看的同学，可以看一下《<a href="http://www.woshipm.com/evaluating/5315730.html" target="_blank" rel="noopener">HMI 竞品分析——实战演练（上）</a>》。</p>
<h3>1. 特斯拉Model<strong> 3 </strong></h3>
<p>空调的语音交互，调节温度只能做到调整到原先设定好的默认值温度。</p>
<p>缺点：如需想要再次调节温度高低，只能通过对中控屏下方的dock栏调节温度区域进行滑动。</p>
<h3>2. 蔚来ES6</h3>
<p>在体验的过程中，基本的功能都能很好实现，比如加热座椅、通风座椅，还有就是空调的控制等等，这些常见的操作都能很好完成。值得一提的是，打断语音播报直接发出下一步指令，以及上下文语义衔接等功能也都是支持的。</p>
<p>缺点：但不支持局部功能的免唤醒操作，每次使用语音控制都得呼唤一遍“Hi，NOMI”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/8AnPXrV4n02xIMN4YOu4.png" alt width="854" height="547" referrerpolicy="no-referrer"></p>
<h3>3. 小鹏P7</h3>
<p>全场景语音控制也选择了与思必驰合作开发语音识别的部分，语义分析则是小鹏自己的团队进行研发的，正确识别率达到80%。</p>
<p>在对于空调的控制方面也是不错的，可以精准地说将温度调到多少度，如果想继续调整说：“好热啊、在帮我下降2度”，它也可以完成此项操作，如果你说将温度调整到35度，这个已经超出了P7最高温度32度，就怕语音形象给你来一句：“我怕你是有大病吧🤪 ”</p>
<p>暂时没啥缺点，就是识别率需要再提高一些，我体验下来觉得他们的TTS反馈还挺丰富的，车联网中的名词，T一般代表的就是to的意思，其中STT是语音转文字过程，而TTS只是文字转语言过程。</p>
<p>简单来说，你可以去看目前比较成熟的梧桐车联TINNOVE，能够支持40多种语言意图操控，并做出类人类的智能化反应，就是STT和TTS通力合作的一个结果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/6rqnvey8um4Oktiz69zT.png" alt width="854" height="525" referrerpolicy="no-referrer"></p>
<h3>4. 理想ONE</h3>
<p>语音控制温度我很是喜欢，比如你可以说，前排温度调整到23度，后排只要跟说“我也要”就可以同步进行调温度，这个就是他OTA2.2 升级的功能四音区锁定。</p>
<p>所谓的四音区锁定就是理想同学此前已经支持车内前后左右四个音区识别控制功能，但这也带来一个问题：熊孩子在后面乱指挥怎么办？</p>
<p>理想同学支持除主驾之外任意一个音区的识别关闭。家长只要在前面说「关闭后音区」、「不要听左后音区」就能关闭响应位置的语音识别，避免熊孩子捣乱，🤪让你皮。</p>
<p>缺点：对于方言的识别率还有待提高。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/iOl9ToIInVcOisoDWsl6.png" alt width="847" height="441" referrerpolicy="no-referrer"></p>
<h3>5. 总结一下</h3>
<p>个人倾向于 小鹏P7 和 理想ONE 的语音控制，他们体验的感觉很棒，另外从空调的语音控制来看，特斯拉Model 3、蔚来ES6 、小鹏P7、理想ONE都是支持语音控制空调的。</p>
<p>但是只有特斯拉Model 3只能设定最常用的温度和风量，其他三种车都可以设随意的说设定多少温度、调整风向和风量、还可以切换内外循环，识别率成功率都非常不错，可以不用操作中控屏幕，大大提高了安全驾驶性。</p>
<p>但现在很多人不习惯用语音来操作车机系统，所以单方面从中控的交互设计内容，可以偏向于理想ONE多参考一下，增大操作区域，减少交互手势，对于复杂的手势操作尽量避免不使用。方控控制空调这内容会连通方控整个模块一起讲，就不单独这边再开一小段了。</p>
<h2 id="toc-2">二、竞品方控分析</h2>
<h3>1. 特斯拉Model 3方控</h3>
<p>左侧功能为：控制音量 / 切换音乐 / 调节后视镜位置 / 调节大灯的角度 / 调整方向盘的位置。</p>
<ol>
<li>控制音量：直接按下滚轮可以静音或者取消静音。</li>
<li>切换音乐：向左拨动切换上一首歌曲，向右拨动切换下一首歌曲。</li>
<li>调节后视镜：进入车辆控制 ➡️ 快速控制 ➡️  后视镜 ，即可使用左侧滚轮调节后视镜。</li>
<li>调整方向盘位置：进入车辆控制 ➡️ 快速控制 ➡️  调整 ➡️ 方向盘 ，即可使用左侧滚轮调节方向盘，上下滚动滚轮来调整方向的高度 / 倾斜角度，左右滚动滚轮用来拉近或者远离方向盘。</li>
<li>调整大灯角度：进入车辆控制 ➡️ 维护 ➡️  调整大灯 ，即可使用左侧滚轮调整大灯角度。</li>
</ol>
<p>切记注意点，特斯拉的车子出场时就已经将大灯调整到最佳位置，建议不要随便地尝试调整，让们安全驾驶，远离事故。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/zfKBmYzxMqXZlM5wIfEv.png" alt width="858" height="590" referrerpolicy="no-referrer"></p>
<p>右侧功能就相对减少了：语音指令 / 调节设置速度 / 调节跟车距离。</p>
<ol>
<li>语音指令：按下右侧滚轮，就能启动语音控制，说出相对于的指令，例如：将温度调整为XX度（这个温度的值也是之前设定好的默认值，Model 3方控无法做到调节温度增减功能，特斯拉的设计理念是做减法，所以他在方控没有做过多复杂的一些操作）。</li>
<li>调节设定速度： 主动巡航情况下，上下调整车速；可以快速调整单位为5km/h ，慢速度调整单位为1km/h。</li>
<li>调整跟车距离：右侧滚轮左右调整时可以选择设置1-7范围的跟车距离。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/yj8dBqubgBwx9QkYPetO.png" alt width="852" height="586" referrerpolicy="no-referrer"></p>
<p>还有一个隐藏功能，我来悄咪咪地告诉你们。</p>
<p>在驻车状态下，长按方向盘两边的滚轮按钮，直到中控屏幕变黑，这样就完成了一次重新启动。</p>
<h3>2. 蔚来ES6方控</h3>
<p>蔚来ES6方向盘左侧的多功能按键，主要负责ACC自适应巡航功能，它的布局相对另外一个款车ES8有所简化按键也变得更多，和特斯拉的设计理念也基本吻合，尽量去做减法，去繁为简，增加按键的操作面积也是为了安全驾驶。</p>
<ul>
<li>左上角 ➡️ 增加巡航车速或恢复自适应巡航     /    左下角 ➡️ 减小巡航车速。</li>
<li>右上角 ➡️ 增加跟车距离   /   右下角 ➡️ 减小跟车距离   /   中间  ➡️  激活或退出自适应巡航。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/tdPuLg3QgZW08nH0kY6R.png" alt width="852" height="586" referrerpolicy="no-referrer"></p>
<p>蔚来ES6方向盘右侧的多功能按键，主要负责娱乐系统以及语音、电话功能的控制。其中上下按键负责音量，左右键为切歌。</p>
<ul>
<li>左上角 ➡️ 语音功能键     /    左下角 ➡️ 方向导航键。</li>
<li>右上角 ➡️ 菜单键   /   右下角 ➡️ 方向导航键   /   中间  ➡️  圆圈 ⭕️ 为确认键、两边左右侧为切歌。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/w3vzGaosIFcLOx3VGAS3.png" alt width="831" height="572" referrerpolicy="no-referrer"></p>
<h3>3. 小鹏P7方控</h3>
<p>小鹏P7方向盘左侧，上下按键为控制车辆空调温度增减， 左右是来调节空调的风量大小。</p>
<p>左下方为语音唤醒按键，按下去之后可以跟小P进行对话，右侧的小鹏logo按钮则为一个灯语的系统。</p>
<p>触摸左侧旋转来可以进行切换仪表盘左侧的显示内容，内容有车辆信息、音乐、胎压、行驶里程等。</p>
<p>右侧“上下”按键为音量的调节大小，左右按键为切歌，左边是返回按键，右边则是静音按键，</p>
<p>触摸右侧旋转来也可以进行切换仪表盘右侧的显示内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/Wm6jsdyXpX4LA4Im7fKg.png" alt width="861" height="592" referrerpolicy="no-referrer"></p>
<h3>4. 理想ONE方控</h3>
<p>我这边所讲的是理想ONE发布的最新款的车型。</p>
<ol>
<li>向上短按唤醒语音/结束对话。 向下短按接听电话、长按挂断电话；</li>
<li>长按进入仪表页面内容， 向上/向下滚动滚轮切换页面。退出仪表页面内容后，短按静音/取消静音；向上/乡下滚轮滚轮 增加/减少音量；</li>
<li>向上/向下短按 切换下一首/上一首。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/fK7QQhkfjg7pQrOYl4XP.png" alt width="847" height="582" referrerpolicy="no-referrer"></p>
<ol>
<li>自动泊车启动后，向上短按开始泊车/继续泊车 ； 自动泊车未启动，向上短按开始自动泊车；向下短按激活自定义键。</li>
<li>长按进入仪表屏页面内容，向上/向下滑动滚轮切换页面。退出仪表屏内容后，向上/向下滑动滚轮，巡航车速增加/减少1km/h ；短按设置巡航车速为道路限速。</li>
<li>向上短按执行NOA系统 推荐变道，向下短按取消NOA系统推荐变道。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/kQ6T2GWTkVDFwQxNRSMs.png" alt width="848" height="583" referrerpolicy="no-referrer"></p>
<h3>总结一下</h3>
<p>方控作为车内交互的重要硬件，现在市场上面还是多数车型以硬按键为主，将常用的功能移植到方向盘上面，比如快速调节音量大小、切歌等功能，也有调整驾驶模式跟车距离等等。</p>
<p>按照现在方向盘的进展没办法满足于智能化和数字化趋势的转变，很多车厂也在开始尝试制作出前瞻性的智能化和数字化的方向盘，如果将中控可移植到方向盘上功能变的越多，那随之而来就会减少驾驶员的注意力分散，从而可以提高安全驾驶的可能性。</p>
<p>PS：有可能在后面对于未来前瞻性的方向盘有文章安排计划。</p>
<h2 id="toc-3">三、竞品UI界面分析</h2>
<p>在热门车型UI界面中挑选对比，在分析完热门车型页面设计的内容后，我会呈现一些自己的idea，这些纯属个人想法，并未用到实际项目中。</p>
<p>下面我会从单个功能 ➡️ 对比体验，单个界面 ➡️ 从界面内容、交互操作、信息位置、信息数量、色彩使用、界面风格，多个界面从 ➡️ 功能的逻辑、用色统一、情绪引导出发阐述。</p>
<p>当有人质问你为什么要这么设计的时候，你得有理可循，没有理论支持的设计如同一盘散沙，一击就溃，这就是为什么我们设计师需要做很多的分析、调研等等一系列的准备工作。</p>
<h3>1. 主界面分析</h3>
<p>特斯拉Model 3 、蔚来 ES6 、小鹏 P7 的主界面以地图方式呈现，而理想 ONE 是有传统上主界面的。</p>
<p>我们来分析一下特斯拉Model 3的首页，既然取消掉仪表盘，取而代之的是占用中控左侧1/3区域作为仪表盘的功能页 + 右侧2/3区域则作为车机系统页面，将使用频率较高的导航作为主界面，顶部的状态栏基本都可以进行点击操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/9A8K5nMsivyBcQBlUJeb.png" alt width="853" height="480" referrerpolicy="no-referrer"></p>
<p>蔚来 ES6 也沿用将导航作为主界面和Model 3不同之处，是增加了两个卡片，靠近主驾驶是常用的音乐卡片，旁边则是车辆信息卡片。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/sci3gJlVRJxCNCefJc2f.png" alt width="855" height="628" referrerpolicy="no-referrer"></p>
<p>小鹏 P7 也是导航作为他们的主界面，和蔚来 ES6 不一样之处就在于小鹏 P7 的常用卡是放在中控左侧栏，卡片的功能有：导航、音乐、电话、消息中心，顶部的状态栏都可以进行点击操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/cfYBJUYeg9UeDVQWcxFe.png" alt width="857" height="411" referrerpolicy="no-referrer"></p>
<p>理想 ONE 采用的是横屏布局，它的主界面采用卡片式的功能页面设计，理想 ONE 中控屏左侧显示的是时间以及5大功能键，右侧是各个常用的功能卡片页。我们很多项目的主页也是采用这种卡片式设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/BTd8DxqpEe4deFoqLdHz.png" alt width="843" height="443" referrerpolicy="no-referrer"></p>
<p>延展一下小知识点，敲重点了，提高注意力听一下。</p>
<p><strong>对于汽车而言，卡片式设计有两大好处：</strong></p>
<ol>
<li>把学习成本降至最低；</li>
<li>增加的接触面积让驾驶的时候，误触率也降到最低，给到用户带来最为直观的体验就是简单易用。</li>
</ol>
<p><strong>总结一下：</strong></p>
<p>这边对照分析的4款车型首页的功能：车辆信息 + 导航（Model 3） /  卡片 + 导航（ES6 +P7）  /   卡片（理想one），卡片样式的设计，极大了提高对于功能的操作性，原本需要点击功能进入二级页面，再进行对其进行操作，现在首页可以直接利用（卡片 + 快捷按钮）样式便捷性操作该功能。还有多种首页的样式比如传统功能图标采用的是“陈列式”的设计（代表作：苹果carplay）。</p>
<p><strong>1）在用色方面</strong></p>
<p>车机系统用色方面大家都用了对比度较高的颜色，不会像移动端那样子，由于驾驶场景的特殊性，驾驶员没有过多的时间停留在屏幕上，因此如果用了对比较低的，那么会影响到驾驶者的安全驾驶。</p>
<p>在我第一篇文章中我也有提到，文本视觉呈现及文本图像至少要有 <strong>7:1</strong> 的对比度，针对大号文本以及大文本图像至少有 <strong>4.5:1</strong> 的对比度。</p>
<p><strong>2）自己理解 + 新的idea</strong></p>
<p>首先要提高屏幕的利用率，不能为了设计而设计，从而让费屏幕的使用率，要站在用户角度思考问题，帮助用户解决问题和痛点，而不是想当然天马行空的设计，为了好看为出发点，有这个想法的请给我立马打回去。</p>
<p>有的车厂设计方案为了好看将屏幕的利用率降低，3张功能卡 + 一个车模 + 车模下方控制车辆的3个功能按钮 + 底部的dock栏，输出的设计效果图还不错，但是这是在牺牲了功能为代价的基础上。</p>
<p>新的idea，首先要分场景，是辅助驾驶还是全自动驾驶，因为全自动驾驶的话就不需要考虑安全驾驶的因素了，这样设计方案可以做出很多种，交互方式也因此将改变。</p>
<p>安于现在的技术和道路复杂状况，自动驾驶发展的道路我觉得很长，对于前瞻性的设计还是要输出和探索。下面我们就开始说一下，介于现在的设计该如何优化首页，有哪些值得我们去探索的？</p>
<p>在首页中我们可以加入场景化相结合，比如天气有阴雨天 、晴天、下雪等，都会在中控屏幕中显示。</p>
<p>大家肯定会说这不会影响驾驶员嘛？现在的技术可以做到识别主驾驶眼球，当主驾驶用眼睛扫描屏幕的时候，这些场景化的内容会立即消失，而且在设计之初也会考虑到不会影响到驾驶和中控操作等，在不影响安全驾驶的情况下，我们可以将这个功能做到设置中开关切换状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/LuFb4opnIih6eXRY9u9I.png" alt width="853" height="480" referrerpolicy="no-referrer"></p>
<h3>2. Dock栏分析</h3>
<p>Model 3最高两级菜单，所以操作起来非常的方便，底部的dock栏包含了车辆设置、音乐、摄像头、雨刮器、座椅、风量、温度、前除霜、后除霜、音量。</p>
<p>更多功能  ➡️（通话、日历、摄像头、能量、充电、网络、娱乐、玩具箱子）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/vLw0aD2rqELo46PFNDl2.png" alt width="841" height="517" referrerpolicy="no-referrer"></p>
<p>这边就有人有疑问了，为什么dock栏图标下面没有文字，而折叠后就加文字了呢？</p>
<p>首先下面作为常用的功能，前期通过4S店员的讲解和查看使用手册，短期的高频率使用更容易让人能够记住它，所以在设计上只保留了icon去除了文字，相对于折叠的功能，它记忆性是呈现逐步递减的，因此需要添加文字作为说明。</p>
<p>蔚来 ES6 由于是竖屏所以底部的 dock 栏 相对 Model 3 减少很多，内容 ➡️ 车辆、内外循环、双区温度、风量调节、前除霜、后除霜，屏幕中是减少了很多，但中控下面的硬按键弥补了中控过少的缺陷，硬按键包括主页按键、设置按键、车辆驾驶模式设置按键以及音量旋钮。可以让用户更加快捷地进入到相应的设置页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/A15N7ZseRYxkBNHmo1bM.png" alt width="855" height="592" referrerpolicy="no-referrer"></p>
<p>小鹏 P7 的 dock 栏位置处于屏幕的最左侧，做在左边的优点大家肯定不谋而合地都会想到，他靠近左侧的驾驶员呀。</p>
<p>对的，确实是基于这个体验做的方案，小鹏P7的 dock 栏内容 ➡️ 应用中心、车辆设置、自动泊车、空调、音乐、电话等。与 Model 3 一样，P7 大屏顶部各个图标也均可打开，比如个人中心、电量管理中心、车辆中心等等，可以快速进入相应的控制页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/ZMMlR1dKncFeIIf98ikJ.png" alt width="857" height="482" referrerpolicy="no-referrer"></p>
<p>理想 ONE 中的 dock栏就和其他三种车型有这很大的区别，既不是放在最左边一竖排，也不是放在底部，由于1920×720分辨率的原因，不适合设计在底部区域，如果硬是放在底部的话，会占据很多可利用的空间，因此这种方案肯定不是最优的选择。</p>
<p>理想 ONE 的选择区域就是最左侧时间和音乐快捷控件的下方，虽然方式独特，但也算是适合的方案，dock栏的内容 ➡️ “主页”、“车辆”、“导航”、“音乐”、“360倒车”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/49kFwFWEVuYZzNcWz1Lc.png" alt width="861" height="408" referrerpolicy="no-referrer"></p>
<p><strong>总结一下：</strong></p>
<p>关于Dock栏的设计，每个车厂都有自己的定义，当中控屏幕为竖屏的时，dock几乎都设计在底部，因为设计在底部的话可以大大提高屏幕的利用率，如果做在侧边栏可想而知，将会减少屏幕的利用率，如下图：给大家展示一下效果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/kg02LYylzUrTO32J5SoI.png" alt width="853" height="524" referrerpolicy="no-referrer"></p>
<p>小鹏 P7 和特斯拉 Model 3 屏幕类型相对比较类似 高度相同，长度 P7 比 Model 3 多出 480px，所以我想这是导致他们在设计策略不同的主要原因吧。他们在对于dock定义，各有优缺点：</p>
<ul>
<li>优点：小鹏P7 dock栏在左侧 便于用户操作  /  特斯拉  Model 3 dock栏功能较多还有功能扩展设计。</li>
<li>缺点：小鹏P7 dock栏功能相对较少，在操作空调调温度体验很差  /  特斯拉  Model 3 dock栏 距离主驾驶较远的功能点击困难，因此他们在对于功能定义排序有着很好的策略，将常用的功能集中于靠近主驾驶左侧区域。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/AQFt7TUGJrhcHGtOkpY7.png" alt width="851" height="523" referrerpolicy="no-referrer"></p>
<p>理想one做的比较特别，一般车载系统的设计dock栏不是放在 左侧 or 底部 （PS：海外版本 有的国家主驾驶是在右侧的那么 放在左侧的dock栏设计要移到右侧区域中）。但是理想one的dock也是放在靠近主驾驶区域的位置。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/leHjDAEaESOsvtWscvSI.png" alt width="854" height="458" referrerpolicy="no-referrer"></p>
<p><strong>自己理解 + 新的idea：</strong></p>
<p>在对于dock做设计方案的时候，要考虑几个要素：</p>
<ol>
<li>在安全驾驶为前提下便于用户操作；</li>
<li>dock栏的内容要使用频率较高的功能；</li>
<li>dock栏的交互手势不要过于复杂，点击、左右、上下滑动即可，长按的操作千万别有。</li>
</ol>
<p>新的idea，根据用户习惯可进行对dock功能进行编辑，dock功能分为可编辑为不可编辑，比如返回主页页面设定为不可编辑，因为如果改动了这个，全局的交互都会因此改变，再出设计方案就要多出很多内容，所以需要可编辑为不可编辑，就像手机自带的功能没办法删除一个道理。</p>
<h2 id="toc-4">四、最后来个总结</h2>
<p>在做竞品分析的时候，不建议视觉设计和交互分的太明显，在一个产品的设计体验上，他们是互相辅佐的，是一个互补的关系，如果你想要很好的锻炼你自己一下，就要尝试一下交互和视觉一起来做分析，还是那句话：站在用户角度去为用户考虑设计。</p>
<p>文章中如有不足之处，欢迎补充交流，我们下期见。</p>
<p>下期文章预告：HMI——语音探索</p>
<p> </p>
<p>本文由@设计界的影帝 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议吗</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5345522" data-author="1144194" data-avatar="http://image.woshipm.com/wp-files/2021/02/7ff0E7qRVbu3wtH8GNE0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            