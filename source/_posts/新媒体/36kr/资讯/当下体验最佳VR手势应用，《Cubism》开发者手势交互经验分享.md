
---
title: '当下体验最佳VR手势应用，《Cubism》开发者手势交互经验分享'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210429/v2_ee41a17a3540474fbb66433ec2b8be58_img_000'
author: 36kr
comments: false
date: Thu, 29 Apr 2021 11:26:56 GMT
thumbnail: 'https://img.36krcdn.com/20210429/v2_ee41a17a3540474fbb66433ec2b8be58_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/vv1sf0eLDHj6TElUG9T-Bg">“青亭网”（ID:qingtinwang）</a>，编辑：Esther，36氪经授权发布。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_ee41a17a3540474fbb66433ec2b8be58_img_000" data-img-size-val="1021,580" referrerpolicy="no-referrer"></p> 
<p>Oculus在2019年底首次在Quest上推出手势识别功能，不久后许多开发者便在SideQuest等平台上发布了一些手势VR游戏demo，并且不断在测试VR手势的多种应用方向。比如，比利时独立开发者Thomas Van Bouwel就开发了一款用手玩3D虚拟积木的VR游戏，游戏画风和色彩十分卡通，玩法很简单，有点像是3D俄罗斯方块的感觉。</p> 
<p>Bouwel表示：出于对手势追踪这种全新输入方式的热情，在Quest开始支持手势识别几天后，我便发布了《Cubism》。不过，早期的《Cubism》在交互等方面还存在一些不足，没有考虑到手势技术的局限。因此在该作正式登陆Oculus商店初期，并不支持手势识别。</p> 
<p>后来经过数月学习和研发后，《Cubism》终于在3月16日重新加入手势玩法。据悉，在这个过程中Bouwel参考了《The Curious Tale of the Stolen Pets》、《度假模拟器》等支持手势识别的VR游戏，以及Luca Mefisto、Denny Kuhnert等开发者的作品，并总结了一些心得。</p> 
<p>那么，《Cubism》手势识别功能的开发背后，究竟有哪些故事？Bowel为这个功能做出了哪些调整？近期，Bowel在一篇文章中公布了该作在交互等方面的大量细节，感兴趣就<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210422/v2_9d94d5f89e394f8082c3b500e50c340d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>来看一下吧。</p> 
<h2 label="一级标题" style>提升手势识别准确性</h2> 
<p>《Cubism》的玩法足够简单，你只需要将散落在空间中的虚拟积木组合成每个关卡设定的目标结构即可完成任务。如果用VR手柄操作，准确性和体验感足够稳定，但这种交互对于手势识别的要求比较高，尤其是抓取和放置这两种交互。此前SideQuest版《Cubism》的体验感实际并不好，经常会因为难以区分抓取和松开的动作，而导致积木被虚拟手粘走，难以通关。</p> 
<p>因此，如何优化用手抓取和放置的准确性，决定了《Cubism》手势识别功能的大部分设计，比如：</p> 
<p><strong>1）幽灵手：</strong></p> 
<p>出于对手势识别技术局限的考量，Bouwel决定不采用基于物理模拟的手势交互，而是将虚拟手设计为幽灵感的透明样式。这样做的好处是，虚拟手可穿过积木去进行抓取，这样效果更准确，而且也更容易从组合在一起的积木中抓取其中一个，不破坏其他组合好的积木。而如果是模拟正常的物理规律，虚拟手在碰到积木后可能会产生推力，不小心推散已经组好的结构，抓取特定的积木也比较难。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_c80bb2df0abd4cdd8b91cddb75925165_img_000" data-img-size-val="640,360" referrerpolicy="no-referrer"></p> 
<p><strong>2）接触式抓取：</strong></p> 
<p>识别抓取和放开的手势意图有多种方式，比如：识别手指捏合动作，或者识别全指关节旋转同时检测手掌的一般交互范围。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_e299cd62fde84a458b021952c02002ca_img_000" data-img-size-val="460,259" referrerpolicy="no-referrer"></p> 
<p>对于《Cubism》来讲，由于可交互的积木形状并不规则，而且体积较小，于是Bouwel决定采用接触式的交互方案，来提升准确性。也就是说，当虚拟手的大拇指和食指距离靠近，并同时接触同一个积木时，即可识别为抓取动作。不需要用力完整的捏合手指，即可快速、自然的抓取。</p> 
<p>接下来，Bouwel借鉴了《The Curious Tale of the Stolen Pets》的手势交互，虚拟手指从抓取到放开这一过程之间，其位置和形状是锁定不变，目的是为了进一步向玩家确认正在抓取积木。此外，积木被抓取后，会与虚拟手的手腕定位同步，目的是让抓取动作更稳固，保证积木与锁定的手指保持一致位置。换句话说，就是积木可以准确的跟随手腕一起转动。</p> 
<p>当抓取，以及食指拇指之间的距离识别后，游戏系统会计算出触发放开动作的极限距离，当食指和拇指间距突破这个距离时，将被识别为放开。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_5b6cf531fc9a4b888f4ceb52080a19f3_img_000" data-img-size-val="640,360" referrerpolicy="no-referrer"></p> 
<p>除此之外，为了避免意外放手，Bouwel在游戏中还设计了多种保护措施，比如：当手势识别准确性低于一定阈值时，不会识别放开动作；当手势识别准确性稳定后，也会等一会再去识别放开动作；最后，在拇指和食指距离突破极限距离后，也需要短暂等待才开始触发放开动作。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_7537d11d47404c2291a6b0c381e29659_img_000" data-img-size-val="640,360" referrerpolicy="no-referrer"></p> 
<p>Bouwel表示：《Cubism》还借鉴了《度假模拟器》对过度抓取手势采取的策略，也就是设定一个标准抓取手势的阈值，当拇指和食指间距小于这个阈值时，系统会缩减识别放手动作的距离标准。换句话说，当你的拇指和食指过于靠近时，你不需要大幅度松手也能放开积木。这样做的好处是，对放开动作的识别更灵敏，避免动作滞后。不过触发的时机比较关键，需要仔细调试。</p> 
<p>根据玩家实际手势动作来调整识别的灵敏度，也是出于对手势识别缺乏体感反馈的考虑，如果你是抓取和放开实际的物体，其实可以通过触觉快<a class="project-link" data-id="587177" data-name="速得" data-logo="https://img.36krcdn.com/20201015/v2_3bc7bdb09cd842248c484bf9308cf954_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/587177" target="_blank">速得</a>到确认。相比之下，用隔空手势抓取虚拟物体可能会因为难以确定物体体积，而过度抓取。</p> 
<p>不过，《Cubism》并不能识别用拇指和除食指外的其他手指抓取的动作，因为系统可能会难以识别你哪根手指跟拇指在抓取哪个积木，容易混淆。而如果通过识别两根手指完全捏合的动作来判定抓取，却又容易打破自然感、沉浸感。</p> 
<p><strong>3）中心点识别：</strong></p> 
<p>据悉，《Cubism》除了通过识别拇指和食指动作外，还会额外识别这两根手指之间的中心点，这个中心点在哪个积木上，就会优先考虑抓取它，从而进一步避免错误抓取。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_ae2aa2d7ee9947c79be39ac141920d69_img_000" data-img-size-val="681,383" referrerpolicy="no-referrer"></p> 
<p><strong>4）抓取拼好的积木：</strong></p> 
<p>抓取拼好的积木与直接抓取单个积木方法相似，区别是你需要将食指和拇指放在抓取框架内，并捏合在一起。这里的抓取框架指的是可识别抓取的范围，通常在拼好的积木结构外层。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_bf908147d45a4a9c8120d3b0d9d01798_img_000" data-img-size-val="340,191" referrerpolicy="no-referrer"></p> 
<p>实际上，这个抓取框架的大小也有学问。它会根据你使用手势或手柄来动态调节大小，当你直接用手抓取的时候，框架范围会更大，方便你快速抓取，同时也避免你不小心抓取到其中单个的积木。</p> 
<p><strong>5）动态平滑手势：</strong></p> 
<p>Bouwel表示：Quest追踪到的手势识别数据目前还存在一些抖动，即使是在准确性高的时候，而这将对游戏体验有较大影响。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_39a2f30a422348df9ffaa86a6a15b8b2_img_000" data-img-size-val="360,203" referrerpolicy="no-referrer"></p> 
<p>当你用手抓取积木边缘时，这种抖动会更加明显，因此对积木进行精准摆放比较困难。因此，将手势数据平滑处理则有助于提升抓取的稳定性，让你更容易将积木放在目标位置。不过平滑的程度需要适量，否则可能会造成延迟的感觉。为了控制平滑手势的体验感，《Cubism》的手势识别系统会根据你手里有没有东西而动态调整。</p> 
<p><strong>6）按按钮动作：</strong></p> 
<p>在此前推出的《Cubism》Demo版中，有一个按钮，大多数人都想去按，但发现没反应。于是在正式版中，我将这个按钮设置为可按。不过，触发按钮需要满足两个条件：你的手需要悬在按钮上方，然后食指发射的射线对准并与按钮底部的触发机制相交。两个条件缺一不可，目的是为了避免误触。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_bd82a292a6c24beabb57ab114c78bff5_img_000" data-img-size-val="320,180" referrerpolicy="no-referrer"></p> 
<p>为了进一步避免误触，当你的手指不对着按钮时射线会消失，甚至当你按按钮时眼睛没看手指，也无法触发按钮。</p> 
<h2 label="一级标题" style>优化交互</h2> 
<p>为了开发更人性化的手势交互体验，Bouwel还在多组不同的人群进行测试，并收集反馈。根据这些反馈，他在《Cubism》上加入了交互信号，并为更多不同类型的人提供交互上的优化。</p> 
<p><strong>1）交互信号</strong></p> 
<p>为了帮助玩家确认抓取指令，《Cubism》采用了多种视觉信号，比如：当你的拇指和食指靠近积木时，指尖会变成和积木同色，暗示你可以抓取这个颜色的积木，同时也提示你哪根手指可以抓取（灵感来自于Luca Mefesto、Barrett Fox、Martin Schubert开发的VR作品）。与此同时，积木边缘也会变亮，强调它可以被抓取。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_9485c80bde37402e88a5fa4136b7fb99_img_000" data-img-size-val="580,326" referrerpolicy="no-referrer"></p> 
<p>此外，当你抓取成功后，食指和拇指的位置便会固定，同时积木的边缘会闪烁一次，你也会听到剪短的提示音。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_bd82a292a6c24beabb57ab114c78bff5_img_000" data-img-size-val="320,180" referrerpolicy="no-referrer"></p> 
<p>按钮方面，当你的食指靠近按钮附近时，指尖会变亮，意味着你可以用食指去按这个按钮。还有一个有趣的特点是，食指靠近某个按钮时，它会突出来，提示你可按。在食指触摸按钮后，按钮会跟随食指指尖向下移动，直到触底，这时候你也会听到确认性的提示音。</p> 
<p><strong>2）额外的交互优化</strong></p> 
<p>对于刚接触《Cubism》的一些新玩家来说，一些人可能会无意识的做出一些手势，因此Bouwel也将这些情况考虑在内，除了通过交互信号指引他们做出正确的手势外，也可以避免一开始不适应的体验。</p> 
<p>比如，有的人在抓取积木的时候习惯握拳，而不是只使用食指和拇指。因此，将可触发抓取的范围扩大，包含整个手指，让抓取手势的识别率更高。不过，目前这种方案还有待优化，比如排除意外抓取、抓错等情况。未来，或许可以通过识别完整的手指旋转动作来推算抓取。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_6d668f9b38fe4d49b9b2331381724060_img_000" data-img-size-val="713,420" referrerpolicy="no-referrer"></p> 
<p>有趣的是，有的玩家看到按钮后会使用捏合手势，而不是自然的去推按。因此，《Cubism》中的按钮也可以通过靠近，加上捏合手势来触发。当然，Bouwel还是希望玩家能够在发亮的食指尖或阴影提示的引导下去按按钮。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_7c3698ac16e14b3abd60167fb9c49a83_img_000" data-img-size-val="480,270" referrerpolicy="no-referrer"></p> 
<p>实际上，你在《Cubism》中遇到的第一个按钮将会写着“按钮后开启”，目的是告诉你按钮需要使用按的手势。</p> 
<h2 label="一级标题" style>提示手势追踪限制</h2> 
<p>近年来，Quest的手势识别性能在不断优化，不过依然存在局限。为了在不破坏体验的情况下让玩家了解手势追踪的局限，《Cubism》也采用了一些巧妙的设计，比如：通过弹出菜单来提示“避免双手交叉”等注意事项，看完后你还需要按下按钮确认。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_3421fdd2a99b40749e917fbf31f50348_img_000" data-img-size-val="681,372" referrerpolicy="no-referrer"></p> 
<p>此外，当手势追踪丢失时，你的虚拟手会从乳白色变成红色。又或者当你只用一只手玩，另一只手放在腿上时，追踪会消失，放置的手会呈现静止状态。为了向你解释为什么一只手静止不动了，《Cubism》会在手边提示是因为追踪丢失的原因。而当你因为双手交叉而丢失追踪信号时，游戏中也会有文字提示。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_0eca6fbc594044b7873753ae2ce6568f_img_000" data-img-size-val="681,383" referrerpolicy="no-referrer"></p> 
<p>对于老玩家来说，他们可以将一只不常用的虚拟手设置为无追踪时消失，避免造成误会。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_cbed1c03366c4efc840e2cd0cdce3580_img_000" data-img-size-val="380,214" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>未来的开发方向</h2> 
<p>Bouwel表示：Quest手势识别依然存在局限，同时尽管《Cubism》已经更新两版，却依然还有提升空间。接下来，将继续探索和支持手势这种全新的输入方式。</p> 
<p><img src="https://img.36krcdn.com/20210429/v2_8cda2374d5c241eb96cf50ca35c47708_img_000" data-img-size-val="280,158" referrerpolicy="no-referrer"></p> 
<p>总之，从短期来看手势识别有望降低VR使用门槛，让更多人可以分享。而长期来看，手势识别很可能会成为未来AR眼镜常用的输入方式，因此通过在《Cubism》VR游戏上探索手势识别，也是在为未来更长远的AR版《Cubism》做准备。</p> 
<p>从Bouwel分享的上述细节来看，他的确在《Cubism》对手势交互进行了多方面优化，解决了demo版本中经常遇到的问题，因此也十分期待有机会能亲自感受一下正式版与demo版的体验有哪些不同。</p> 
<p>参考：</p> 
<p>https://www.roadtovr.com/cubism-hand-tracking-case-study</p>  
</div>
            