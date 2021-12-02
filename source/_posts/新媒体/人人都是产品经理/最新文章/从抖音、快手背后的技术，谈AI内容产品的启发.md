
---
title: '从抖音、快手背后的技术，谈AI内容产品的启发'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/vcksCKhIDkDgLUNLjqxt.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 02 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/vcksCKhIDkDgLUNLjqxt.jpg'
---

<div>   
<blockquote><p>#本文为人人都是产品经理《原创激励计划》出品。</p>
<p>不知不觉中，AI技术已经渗透了我们的生活，比如短视频平台就有AI/AR道具，创作者可以利用这一类道具来创造更有趣的内容。具体而言，有哪些AI技术可以应用在内容类型产品中、增加创作的多样性？不妨来看看作者的总结。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5235938 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/vcksCKhIDkDgLUNLjqxt.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近因为工作原因接触到了快手的AI技术（主要是CV方向的），也跟快手的技术团队做了一些访谈。不由得感叹其实快手的技术还是非常领先的，甚至很多场景做得比抖音还要早，技术单拎出来比字节的技术更加能打、更加领先。</p>
<p>但是为什么AI技术如此出众的快手却在大众市场上或者是我们谈的商业市场上不如抖音呢？互联网的竞争如此激烈，原则上在占用用户时间的维度上大家都是竞品，人们知道字节的轻颜、剪映、醒图，但是很少人知道快手也有对标的一甜、快影和原片。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/fQIX7dXB6vAyBq04HU3V.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" width="627" height="382" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图1 快手头条有一系列对标的竞品</p>
<p>首先需要澄清的一点是，AI技术并不是万能的。很多商业上的成功，并不代表这家公司只是因为技术很厉害、算法很牛逼，商业上就一定很成功，这个不是充分必要条件，技术很牛逼最多只是一个充分条件。</p>
<p>商业上的成功，或者是我们世俗定义的成功，更多还包括组织上的成功（人才的管理、激励，组织协同工作、效能最大化）、产品的成功、对于人性的洞察与应用，对于商业模式的理解等等，这些全部要素才能最终使得一款产品真正地走向成功并且生命周期足够长。</p>
<p>比如说微信就是一个很典型的例子，微信有AI技术么？当然，但这些都是润物细无声的存在，微信并不会为了AI而AI，比如微信扫一扫入口识图、识街景、识商品/长按翻译/语音转文字等，这些都是AI技术能力产品化，但是这些并不是微信这个产品的全部，或者说，这些技术只是帮助微信更好地向用户提供一个交流沟通的工具，让人们更加无障碍地交流互动。</p>
<p>问一个问题，对于抖音或者快手来讲，大部分人是刷视频还是调用摄像头主动拍摄视频呢？</p>
<p>相信大家的答案应该是一致的，大部分人用抖音快手还是用来浏览，kill time。真正使用抖音里面的各种AI/AR道具UGC创作内容的还是少数，大部分用户如果使用道具可能是尝鲜，比如一些拍同款；对于专业的内容创作者，主要是通过内容本身的编排设定来吸引观众，也不太依赖于AI的模板或者是各种道具。即使需要使用AI的各种剪辑等特效技术，可能也是在视频创作过程中使用，即作一个AI赋能的视频编辑工具，比如类似剪映。</p>
<p>但是问题又回到了起点，为什么快手很多的gan（对抗生成网络）等AI生成技术比抖音好很多呢？头条不是算法起家嘛？通过近一周多时间仔细分析两家公司的背景，尝试得出的原因总结如下：</p>
<p><strong>1）基因使然</strong></p>
<p>快手最早是从动图gif剪辑工具起家，本身就是一家技术驱动型的公司，且创始人宿华和程一笑也都是技术出身，因此营造工程师的乐园，重点在CV等技术上加大投入，用技术来驱动产品，通过一些AI加持的爆款特效+专题运营来激发用户活跃度；这个是快手这家公司的底层逻辑。</p>
<p><strong>2）老铁需求</strong></p>
<p>快手本身的平台特质跟抖音就有很大区别，抖音是符合马太效应的，即主要的80%流量都导向头部的20%网红，而网红生产的内容是通过抖音大数据平台算法得出的。</p>
<p>快手则相反，致力于构建一个公平的平台机制，如果流量太高反而会被限流，更多的鼓励是平民生产内容，构建同城或者是你身边跟你很相似的人的故事。这些人可能就与你我一样是个普通人，背后没有MCN机构、没有巧妙构思的脚本、专业的剪辑，因此这些“平民”需要AI加持、需要一些工具来低成本地创造内容，记录自己的生活。</p>
<p>从这个角度来讲，快手更需要更加强大的内容创作生成技术来帮助普通人实现明星梦，或者是拍同款。</p>
<p>虽然AI技术不是万能的，短视频的核心还是内容为王、围绕内容构建各式各样的玩法；但是通过AI技术加持，帮助大家高效地生产内容、创造有趣的、好玩的内容，所以接下来想谈谈，具体有哪些AI技术是可以应用在内容类型产品中的。</p>
<h2 id="toc-1">一、物体/动作检测技术</h2>
<p>这一类应该是最早应用在短视频内容创作上的，包括很多自拍相机也有类似的功能。比如眨眼睛、吐舌头、比各种手势来触发一些特效，这些是基于人脸的。同理，基于一些生活中的图标、物体检测来触发一些特效。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/66fRSzmFJSEXvemjc66U.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2 比心特效</p>
<h2 id="toc-2">二、美颜、美妆、美体、美牙等人像美化功能</h2>
<p>这些其实都是基于关键点技术，无论是人脸的关键点检测还是人体的关键点检测技术，不论是5点、21点还是137、200+、1000+的点，又从2D的关键点到3D的关键点，这里都是为了帮助机器确认人脸的五官位置以及面部轮廓来进行的比例调整，比如大眼、瘦脸、瘦腰、拉腿等等。</p>
<p>这些比较基础，对于关键数量依赖比较少。如果想要做得更加精细，比如美妆里面需要进行眼妆（睫毛、眼影、眼线、眼睑下至、卧蚕）等等小部位的刻画，这就需要关键点数量的增加，甚至如果想要做丰额头、高鼻梁、低颧骨、丰苹果肌等效果，就需要一些3D mesh（从原来的点形成网状结构）的辅助。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/nEpuNxm4g8KU9FGujOGO.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" width="628" height="308" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图3 2D人脸关键点和3D关键点，人像美化的最基础技术</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/eK9ix4jwkJZHLy1PGpIH.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" width="628" height="405" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图4 人体关键点技术</p>
<p>又或者是如果在美体这个用户体验做到既可以拉腿、细腰、丰胸，同时又不让背景畸变，就需要引入matting和inpAInting的技术了（既抠图和补全），有些场景下也可以使用3D人体重建的技术。比如说剪映软件里的换背景功能也依赖于抠图能力。</p>
<p>牙齿美白、口红依赖于分割技术，比如我最近在使用剪映牙齿美白功能的时候，嘴巴前面有一个遮挡物时，就会在遮挡物上就浮现了一个白色的月牙状不明物体，这是因为牙齿没有像嘴巴一样做遮挡状态的判断，呈现了一种俗称“穿帮”的画面，非常尴尬。</p>
<h2 id="toc-3">三、AR类（人和环境）</h2>
<p>所谓AR类的，我们统一都定义为在已有的现实空间中叠加3D渲染的CG素材，不论是叠加在人脸上的、还是叠加在环境中的。</p>
<p>这些底层技术一部分依赖于3D的人脸关键点的定位技术，另一部分依赖于对于空间的3D定位技术，如何在不同的用户手机姿态运动下、用户本身做各种动作的情况下，能保证叠加3D素材的绝对位置的固定（因为现实生活中的物体都是绝对静止的、不会随着手机的运动而动来动去），这个是对于技术考验最大的部分。</p>
<p>当然3D素材的精致程度，很大程度也依赖于CG的生成效果。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/fwMSdzL5mqpVa6XNZIcv.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" width="629" height="354" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图5 google基于Android像开发者提供的ARcore能力，对标的苹果有ARkit</p>
<p>同时，这类型的技术还非常适合跟广告主结合，广告主通过某个主题的风格或者元素，平台推出、大V优先使用引发网友参与最后形成二次传播，使得品牌的产品及形象在网友中引发广大的讨论。</p>
<p>比如在ins上，Gucci、LV、Dior就订制了很多富含自己品牌元素的AR贴纸套装供用户使用，用户在拍照录视频玩的同时，也可以体验产品虚拟试穿、试戴的效果，进一步促进购买转化。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/7u73QKiajqytc42DK6Zl.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" width="371" height="660" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图6 ins上的gucci lens（特效）</p>
<h2 id="toc-4">四、生成类网络（GAN）</h2>
<p>随着蚂蚁呀嘿的一夜爆火，zao等AI换脸引发社会广泛伦理道德的讨论，社会对于GAN生成类的特效一直有很高的热度，比如说“变三岁”、当你老了、迪士尼风、国漫风、手绘小姐姐等等。</p>
<p>由于GAN本身网络的特性就十分适合短视频这类、以内容生产作为主要驱动力的产品定位，通过使网络学习大量的目标图片的风格，AI技术结合一些短视频类的模板就可以非常快速地帮助用户生成非常搞笑的、可爱的、炫酷的短视频内容，也非常适合结合短视频平台的各种节日运营活动展开，比如万圣节生成鬼怪妆容、儿童节生成儿童脸，520/情人节“变男友”等等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="从抖音、快手背后的技术谈AI内容产品的启发" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/HXZRYKM9K1D6o46NmKm1.jpeg" alt="从抖音、快手背后的技术谈AI内容产品的启发" width="627" height="301" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图7 快手平台520活动变男友，应用的就是GAN网络生成有夫妻相的男友</p>
<p>虽然在任何时代，内容为王此话不假，但是在所有UGC的平台都已经被AI深度渗透、成为不可或缺的一部分的时候，你的产品没有反而无法留住用户。此时的AI技术在Kano模型当中已经从一个魅力需求变成了一个基础需求。</p>
<p>据内部消息，小红书已经大规模高薪聘请CV算法工程师来帮助提升其平台内容的AI多样性，你认为这必要么？</p>
<p> </p>
<p>作者：大仙河，7年AI产品相关经验；微信号 ：大仙河知识学堂</p>
<p>本文由@大仙河 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>本文为人人都是产品经理《原创激励计划》出品。</p>
<p>题图来自 Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5234430" data-author="1284679" data-avatar="http://image.woshipm.com/wp-files/2021/10/krXUMQygcxKDrCDn4avA.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            