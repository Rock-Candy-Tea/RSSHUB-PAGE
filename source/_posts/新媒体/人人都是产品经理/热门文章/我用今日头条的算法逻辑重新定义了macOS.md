
---
title: '我用今日头条的算法逻辑重新定义了macOS'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/0RoqlVblq5C9XAP8hjNE.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 18 Mar 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/0RoqlVblq5C9XAP8hjNE.jpg'
---

<div>   
<blockquote><p>编辑导读：今日头条作为“算法魔力”的代表，能让用户沉浸其中无法自拔。回到工作中，枯燥难用的系统很大程度上影响了我们办公的心情，那为什么办公系统不能像今日头条那样呢？本文作者从今日头条的算法逻辑出发，重新定义了macOS，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4416375 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/0RoqlVblq5C9XAP8hjNE.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>除了工作之外，我大部分时间会分为2个状态：一个是刷头条，另一个是坐在马桶上刷头条；几乎每天有3-4个小时是跟头条相伴，这算法的魔力真是可怕，总能知道我想看点啥，让我不自然的刷啊刷啊刷，时间就这么过去了，比起坐在电脑前对着一堆应用程序图标不知道该干啥爽多了。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/vckJzizBDtjqyI8nPswY.png" referrerpolicy="no-referrer"></p>
<p>每当这个时候我又想打开头条摸会儿鱼，唉唉唉！不对，不对，为什么头条能让我爽但电脑不能呢！为什么操作系统不可以帮我做我该做的事情呢！为什么我一个花季美少年要对着一堆应用图标发呆呢！！！一连串的灵魂拷问让我产生了一个大胆且优雅的想法：我要用今日头条的算法逻辑去重新定义了macOS！嗯，就这样！</p>
<p>作为一个七分熟的互联网产品从业者，重新做一款产品一定要讲究“方法”（上头了哈）。好，我们一起按照案件推理的逻辑一步一步捋一捋哈：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/tq13eyUgZns2ViJdSgaa.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、理不清，用不溜</h2>
<p>我是一个极度不讲究的人，用完的东西乱扔乱放，导致我的电脑桌面乱作一遭，之前也试图用所谓的整理术（日本收纳术也稍有涉及）去试着整理下目录结构，但抵不住丑陋的本性，还是放弃了，所以导致desktop如下图一样：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/NyYFJl192ajx71EcKavK.png" referrerpolicy="no-referrer"></p>
<p>不知道有没有人跟我一个德行，就是明明道理都懂，用起来一塌糊涂。即使有已经有自动分类但还是别别扭扭，导致找个东西找半天，效率极低。</p>
<h2 id="toc-2">二、目标和结果不直接</h2>
<p>在过往的操作中，我会发现其实想法和最终结果之间的距离要跨越不少“阻碍”，目标和结果之间要绕来绕去不直接。这么说吧，现在的macOS（也包括其他操作系统）的操作逻辑大致是：脑子里想要干一件事 → 判断能完成这件事的应用程序，并定位到某一款上 → 通过app图标入口进入 → 开始干。</p>
<p>举个例子来解释下：我想看《赘婿》（吉吉国王太搞笑了哈哈哈），对应上面的步骤依次为：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/mbyD9W3L6FHEi4MRyeQS.png" referrerpolicy="no-referrer"></p>
<p>一切都很顺畅吧？没什么不合理吧，但如果抛开惯性思维的前提下仔细琢磨琢磨你会发现任务逻辑的是有问题的，目前所有的操作系统是以应用程序为核心的操作逻辑，而不是以事件的终极目标为核心：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/lo5S2jorezlAThd44ELD.png" referrerpolicy="no-referrer"></p>
<p>说起来就像设备转换器一样，这个玩意的终极目标是要接入的设备正常运行，说白了就是电脑接口不满足设备。所以说使用这些个设备之前你势必会经历买个转换器这个环节，一定程度上转换器成了设备的分发渠道，用ta实属无奈，不用还不行。按照今天科技的发展，做到美观和实用共存应该也不是什么难事，那为什么电脑就不能做的直接一点，让设备可以直接连接电脑使用呢？</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/zBm5GnROCZZ7ae2rpdhW.png" referrerpolicy="no-referrer"></p>
<p>我试图倒回到源头来看，从1973年施乐发明的第一个图形化操作系统诞生到如今，已经经历了48年的操作系统，看起来对任务流逻辑的理解没有任何成长，依旧还处于诞生那一刻的那个心智上。唉，这不禁让我陷入了沉思。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/NwuszXCUA2H8HdoW2e5d.png" referrerpolicy="no-referrer"></p>
<p>所以写到这里，费了这么大的篇幅，我就想要强调“目标”和“结果”之间需要有一个直接触达，这个过程不需要拐弯抹角和遮遮掩掩，要的只是简单和粗暴。那么综上来看，看起来如果是通过内置算法模型去学习操作者的习惯和爱好也许是改变这个固化任务流最好的方式了。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/oENo8c0kld4AAiPXy2CG.png" referrerpolicy="no-referrer"></p>
<p>基于此，我去翻阅了今日头条算法架构师曹欢欢博士有关推荐系统原理的分享，其中主要介绍今日头条推荐系统的搭建以及内容分析、用户标签、评估分析，内容安全等原理；我试着摘取了些通俗的语言来简单介绍下推荐系统的核心因素以及算法函数模型：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/55rbb42VhYViL4XVzg0e.png" referrerpolicy="no-referrer"></p>
<p>有了这个模型的加持，我重新梳理和定义了我理想中的操作系统任务流逻辑，接下来分两部分介绍下：</p>
<h3>1. 核心理念</h3>
<p>我定义的操作系统其核心是无需让人们围绕App，而是可以对用户的意图分析做出了流畅的响应，从而减轻了所有多工具工作流所带来的间隙摩擦的不快。</p>
<h3>2. 任务流重塑</h3>
<p>以往的触达操作需要用户的重度操作，而我希望把这些操作转化成数据运算转化到后台自动化，也就是说你不需要关注怎么到的目的地，你只需要关注目的地是不是你希望的那个地方就可以了：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/Qvd2aniiJIjC1JtQtRO3.png" referrerpolicy="no-referrer"></p>
<p>再补充下，除了根据兴趣和习惯去计算操操作者的行为之外，时间和空间同样在算法模型中占据很重要的位置，ta会根据日期判断是否处于工作日和写字楼，或者是休息日和家，所以整个影响算法的关键因素大致有：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/PYJCq4sU3GiRL3dzUqvV.png" referrerpolicy="no-referrer"></p>
<p>通过对原理的分析和重构，我决定尝试着把我想象中的macOS设计出来。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/deTGC83viSa0ZsIjcuaY.png" referrerpolicy="no-referrer"></p>
<p>终于，在一些列的构思和尝试后，我把我理想中的 macOS 设计了出来，不废话，先看图：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/QnJNzhcJYqdMEaClonhb.png" referrerpolicy="no-referrer"></p>
<p>这就是我定义的全新 macOS 了，模块是ta的骨骼基础；所有的任务都是以模块化作为区分，从而更好的区别层次。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/JNXHmemsOv9k2ywjRjD8.png" referrerpolicy="no-referrer"></p>
<p>当我们进入到系统，清晰可见两大模块我把他们命名为：工作启动台（左侧大卡片）和场景化模组（右侧小卡片），拆分来看下框架逻辑：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/BQsiiTTQF28MQYhzIEW7.png" referrerpolicy="no-referrer"></p>
<p>接下来分别介绍下这4个feature：</p>
<p><strong>1）工作启动台</strong></p>
<p>如上图所述，工作启动台是基于机器学习和场景分析，从学术的角度上来说（并不严谨的学术）同时通过API接口跟第三方的应用程序数据互通，根据任务类型 / 时间和 POI 等综合维度来确认用户核心关注事件，一定程度上会帮助用户“预判”接下来可能会发生的事。</p>
<p>按照通俗的方式，打个比方解释下，有这么个场景，钉钉里需求方说：“明天咱们需要给老板汇报商业化项目进展”，那么OS会自动抓取“明天（时间）”“汇报商业化项目（事件）”这两个关键词，并结合习惯联想出“PPT（形式）”，自动为你创建一条工作：“商业化项目汇报.pptx”，同时反复提醒你时间节点，形成一条工作任务流：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/kn4A16DW6kJ6jPYFvGzf.png" referrerpolicy="no-referrer"></p>
<p>不得不说，在我30多年的人生路上，最讨厌的环节就是事无巨细的决策（除了中午吃啥这一个事很享受外），不过用了这款系统完全可以通过语言分析来大大提高生产力，不需要你做任何时间判断 / 工具选择 / 项目命名乃至排期上的决策，也能完美开工，太tm屌了哇哈哈哈哈哈～</p>
<p>不过，作为一个职场人，我们每天要处理大量的工作，没有一个人可以说他一天就处理一件重要的事，通常情况下我们是多线并行的状态，也就是说这个事很重要，那个事也挺重要，搞得最后一团糟，啥啥都做不好，交不了差。</p>
<p>现在好了，有了系统的这套算法，ta可以自主学习和分析你的状况，按照任务分类 / 时间和形式来帮助定义优先级和展现逻辑，这就让你在面对一堆任务的时候也不会无从下手：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/SmGOCK7gkqKHzqmqfScQ.png" referrerpolicy="no-referrer"></p>
<p>不过，我深知算法的能力永远做不到人那么智慧（可能跟人有情感有关），所以开放给了用户一些自定义的权限；也就是说假如算法出现了错误或者不那么称心如意的时候，选择自定义工作流也未尝不是一种解决方案：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/TCA6Kb9dAQNZKF8Dg9mr.png" referrerpolicy="no-referrer"></p>
<p><strong>2）场景化模组</strong></p>
<p>作为整个系统的另外一个重要组成部分，场景化模组主要承载的是工具类型的呈现，辅助主线工作的正常进行。举个例子来说，通常我们完成一个ppt汇报的工作涉及到的工具有：powerpoint（主要生产力工具）/photoshop（P个图片）/execl（找找数据）/QQ音乐（听歌找找感觉）等等。</p>
<p>所以当我们同一任务下多线程子任务并行的时候，工作启动台就不足以承载这种场景，而场景化模组刚好作为补充来弥补过度聚焦后带来的拓展不足。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/xbEZDnbvMPVrUCd8qS8e.png" referrerpolicy="no-referrer"></p>
<p>需要补充的是，模组的出现逻辑同样是通过算法模型的分析和学习依次呈现的，具体会根据“任务类别”“场景”“时间”和“位置”这四大维度判断展示顺序：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/8r32d5XzqmldrXIW8bTT.png" referrerpolicy="no-referrer"></p>
<p><strong>3）体感交互的全新升级</strong></p>
<p>另外作为一个产品体验设计师，我深感siri的鸡肋（鸡肋中的大鸡肋），因为在工作场景下，如果我对着我的搭载M1芯片8核中央处理器和16核神经网络引擎的macbook pro说话的话，身边的同事一定觉着我是个傻子（傻子中的大傻子）…所以改变Siri的交互形式这种事必须要做！！！</p>
<p>如果你是一个体感游戏玩家，那么我猜看到这里你应该也跟我想的一样，没错啊！新的Siri就是体感触控！类似于X-box的交互体验，早在2013年的时候我有幸受邀参加美国体感控制器Leap motion的发布会，深深的体会到了AR体感交互的魅力，只需要通过usb接入电脑，就可以像体感游戏机一样，通过无触碰手势干任何事情：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/g90UhGYv3fzPIQoqDVl2.png" referrerpolicy="no-referrer"></p>
<p>所以我结合了Siri的智能和Leap motion的AR，打造了独一无二的语音/体感的双线操作系统管家（实在想不出好名字了…就叫个管家吧）——Leap Siri：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/YGOsoThJHA12G9ruwTHB.png" referrerpolicy="no-referrer"></p>
<p>上述所有的文字都在强调工作场景，不过理论上来讲，一个好的系统要满足工作和生活娱乐双场景，在工作环境中好好工作，在娱乐环境中就用ta来刷刷剧和玩玩游戏；但生活中充斥着不太听话的小朋友，他们总是会反其道而行之，比如在工作场景刷剧和玩游戏（这特么可不就是我么），所以！为了我们伟大的摸鱼事业，我也为这群有理想的人设计了一个专属交互，我称这个交互为“feel fish”：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/ZvaYXxnwL2R8pYpshmTs.png" referrerpolicy="no-referrer"></p>
<p>棒极了哈哈哈哈，以后上班摸鱼再也没有后顾之忧了，全靠Feel Fish啦～</p>
<p><strong>4）概括一下</strong></p>
<p>总的来说，这款全新的操作系统一定程度上颠覆了以往按照app为核心的操作模式。换句话说这个redesign的版本取缔了“中介”这个概念，直接可以触达任务本身是ta的理念。</p>
<p>嗯，关于系统逻辑这一块想讲的也大概讲完了，至于具体的执行操作流程，我就不展开在这里讲了，与当下的情况也大同小异，等发现有什么难以忍受的痛点的时候再写一篇文章掰扯掰扯好啦。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/iA3SUyiC6s8aliD28LLv.png" referrerpolicy="no-referrer"></p>
<p>好了，一切都准备就绪了，最后的一步要给我这个全新的系统起个高大上的名字。就在我有这个想法的时候，脑子里闪过了无数的词汇，但让我最记忆深刻的就是钢铁侠的“贾维斯”了，如果你是一个漫威迷你对这个名字一定不会陌生：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/pmH8oh3WgB3ZxVmrnxg2.png" referrerpolicy="no-referrer"></p>
<p>贾维斯：钢铁侠专属的人工智能操作系统，为钢铁侠的战斗提供坚实的后盾。</p>
<p>贾维斯！多么有内涵的一个名字，既不绕口又颇具深意。所以我穷尽毕生所学，以贾维斯为原型，打造了一个划时代的系统代号，并为ta设计了独一无二的logo，激动之情涌上心头，不废话了，就让ta亮个相吧！小宝贝！</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/4TGJ5vfkOeXQy5WXjgaV.png" referrerpolicy="no-referrer"></p>
<p>张铁柱！绝了啊，完美对仗贾维斯，哇哈哈哈哈哈哈哈哈哈哈（希望Tim Cook看见这篇文章赶紧为我安排入职）～</p>
<h2 id="toc-3">三、总结一下</h2>
<p>如你所见，这篇文章纯属我个人对操作系统的不满和愤忿。这个世界每时每刻都在进步，但依旧有不少东西还在依赖惯性思维运转着，才有了整篇的论点，YY归YY，但不得不说算法真是个神奇的东西，几乎已经深入到我生活中的点点滴滴，期待未来算法可以帮我解决更多苦力劳动，释放生产力，省出来的时间去王者峡谷大杀四方他不香么～</p>
<p> </p>
<p>本文由 @负能量补给站 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4414771" data-author="1170837" data-avatar="http://image.woshipm.com/wp-files/2020/11/icIZaKdzZY1dGyNMa1tP.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            