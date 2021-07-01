
---
title: '用机器_大脑_操纵活线虫运动，微型机器人新研究登Science子刊'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210701/v2_59b669a92881490598cf464ee60deae6_img_000'
author: 36kr
comments: false
date: Thu, 01 Jul 2021 07:11:59 GMT
thumbnail: 'https://img.36krcdn.com/20210701/v2_59b669a92881490598cf464ee60deae6_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/MaZwQDqOoaCHUShWh-wkWw">“智东西”（ID:zhidxcom）</a>，作者：ZeR0，编辑：漠影，36氪经授权发布。</p> 
<p>智东西7月1日报道，给一个活体生物躯体注入机器的“大脑”，然后人为控制该生物的行为，已经从科幻片走入现实世界。</p> 
<p>今日，国际机器人学术顶刊Science Robotics上最新发表的一篇新论文，描述了一种用机器视觉、运动控制和导航等算法取代线虫大脑、精密操控活体线虫运动的新方法，创造出一个不受束缚的、高度可控的微型软体机器人，并将其命名为RoboWorm。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,544" src="https://img.36krcdn.com/20210701/v2_59b669a92881490598cf464ee60deae6_img_000" referrerpolicy="no-referrer"></p> 
<p>论文链接：</p> 
<p>https://robotics.sciencemag.org/content/6/55/eabe3950</p> 
<p>该论文题目为《通过光遗传运动控制秀丽隐杆线虫，实现活的微型软体机器人》（Toward a living soft microrobot through optogenetic locomotion control of Caenorhabditis elegans），由加拿大多伦多大学机械与工业化学院与Lunenfeld-Tanenbaum研究所合作完成。</p> 
<p>“生物本身即最完<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>机器人。”论文第一作者董先科博士告诉智东西，从机器人学的角度，这一研究相当于做了一个<a class="project-link" data-id="32740" data-name="微米" data-logo="https://img.36krcdn.com/20200729/v2_b4bfc7107198481dbced94d15dd845c7_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/32740" target="_blank">微米</a>尺度的蛇形机器人，只不过用了生物本身的肌肉细胞作为执行器，这使得微型机器人变得更加灵巧，也更像真正意义上的机器人。</p> 
<h2>01.</h2> 
<h2>破解微型机器人的运动控制技术瓶颈</h2> 
<p>学习自然生物的运动是设计微型机器人最有效的策略之一。</p> 
<p>得益于数百万年的进化，生物们发展了复杂的身体结构、高效的能量流动和先进的运动控制系统，这些系统超过了任何人造机器。</p> 
<p>这些生物的特性，为各种微型机器人的设计提供了巨大的灵感。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,520" src="https://img.36krcdn.com/20210701/v2_6304dc63b85b474b97bd3927b4ab1651_img_000" referrerpolicy="no-referrer"></p> 
<p>微型机器人领域在MEMS技术以及光刻蚀技术的迭代之下，近十年来有长足的发展，并逐步在靶向给药、测量细胞器模量、辅助精子移动人工受孕等场景尝试应用。</p> 
<p>然而，与自然模型相比，生物启发的微型机器人的结构通常被大幅简化，以促进微型机器人的制造和驱动。因此，这种微型机器人的性能无法与生物体相提并论。</p> 
<p>人类若想真正制造尺寸在数百微米乃至数微米的受控微型机器人，目前条件下，仍然存在诸多技术瓶颈。</p> 
<p>比如在工艺方面，主要瓶颈在于如何制造装和配微型机器人，如何给这么小的机器人供能。</p> 
<p>在原理瓶颈方面，微米环境里粘滞力和摩擦力比重力大几个数量级，用什么结构驱动微型机器人运动，以完成既定任务。</p> 
<p>在控制方面，如何测量微型机器人的运动，构成闭环，如何对这么小的机器人实现精密控制等等，都是当前研究面临的挑战。</p> 
<p>现阶段学术界开发的微型机器人构造相对简单，多为简单的、能直接用光刻蚀技术加工的微结构体，如微纳米磁块、微米螺旋体、微米管等。操控性和功能大都比较有限。而如果结构过于复杂，在微米尺度下，它们即使能够加工出来也很难装配。</p> 
<p>针对这些瓶颈问题，此次在Science Robotics上发表的新论文，提出了一种相当有“脑洞”的解决方案：用机器视觉、运动控制和导航算法替代生物的大脑，重构生物的感官运动系统，人为控制活体生物的运动，直接将微米级生物开发为受控微型机器人，以完成微米环境下的特定任务。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,409" src="https://img.36krcdn.com/20210701/v2_643cbe6e0d114089aea24c288133a7f1_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲秀丽隐杆线虫受光驱动激活肌肉群</p> 
<h2>02.</h2> 
<h2>结合机器视觉算法，精密控制活体线虫</h2> 
<p>这项研究选择的生物对象是秀丽隐杆线虫。</p> 
<p>秀丽隐杆线虫是生物学中唯一一个神经元连接映射图被完全揭示的模型生物，身体透明，成年体长度约1毫米，宽度约80微米，身体里一共302个神经元。关于秀丽隐杆线虫的研究分别在2002、2006、2008年产生了三个诺贝尔奖。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,574" src="https://img.36krcdn.com/20210701/v2_87d2b83bd3004c9a8fff780c7710f83b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲秀丽隐杆线虫</p> 
<p>作为一种软体生物，线虫的身体每个地方都能弯曲，拥有无限自由度。近年来，随着人工神经网络的发展，人们对生物本体的神经系统信号传递处理的机理剖析有更迫切的需求。秀丽隐杆线虫也成为神经生物学甚至人工智能学科的研究热点之一。</p> 
<p>通过一系列生物化学以及工程手段，该研究将活的线虫变成了可以人为精密控制的微型机器人。</p> 
<p>首先，研究者用化学方法阻断了线虫的<a class="project-link" data-id="630922" data-name="运动神" data-logo="https://img.36krcdn.com/20201111/v2_ccb0835707164dd98ecdff2c97e319a8_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/630922" target="_blank">运动神</a>经元与肌肉细胞组的信息传递，将线虫的神经系统暂时麻醉，使得现场仍然是活的，但它的大脑无法向肌肉传达运动指令，即无法控制自身运动。</p> 
<p>然后，通过机器视觉算法实时分析线虫的形态和周围的环境，分析结果，在进一步建模和控制算法综合之后，用光遗传学的方法，操纵微米激<a class="project-link" data-id="520880" data-name="光束" data-logo="https://img.36krcdn.com/20201107/v2_6cd9bb3de3a242679c34dd60690b22ab_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/520880" target="_blank">光束</a>精密协调控制肌肉细胞组群的活动，实现线虫整体的闭环运动控制。从而用算法取代线虫的“大脑”，重构线虫感官运动系统对身体的控制。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,381" src="https://img.36krcdn.com/20210701/v2_89391d97d3ce4b92b9af222cfb0d9d15_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲线虫闭环控制之字形模型与控制系统架构</p> 
<p>具体而言，考虑到照明光强、显微镜聚焦状态、虫子大小等干扰因素，研究人员采集了几千张自然状态的虫子连续爬行的照片，在此基础上设计机器视觉算法。据董先科介绍，该算法在普通的笔记本电脑上也能实现50fps的速度，相关代码已公开。</p> 
<p>开源地址：https://github.com/BionDong/worm-locomotion-feature-analysis</p> 
<p>然后，控制算法会根据机器视觉算法测量的物理状态，计算当前时刻需要用多大的激光强度，来激活或抑制哪组肌肉细胞，从而操纵线虫向设定的位置移动。</p> 
<p>为了精密的协调控制肌肉收缩，需要激光束有细胞级的精度。为此，研究人员改装了一台倒置显微镜，并且在上面搭建了一个激光投影系统。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,549" src="https://img.36krcdn.com/20210701/v2_da1950c2060840faab93419dbfd1073e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲基于倒置显微镜的激光投影系统的硬件架构</p> 
<p>该系统用数字微型器件DMD反射473nm的蓝色激光束，搭建一些光学元件让激光束透过显微镜物镜缩小上百倍，然后聚焦在线虫身上，最后通过给DMD编程来控制激活或抑制哪些肌肉细胞。</p> 
<p>目前这个系统能够达到3微米的投影精度，基本可以实现对单个肌肉细胞的光遗传学操控。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,562" src="https://img.36krcdn.com/20210701/v2_f25851cd6fd54d12b6e0e49e60bd6261_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲不同激光强度下，线虫的肌肉弯曲反应</p> 
<p>研究者在这种人为改造的活体机器人上，设计算法实现了线虫在自然状态下被观察到的所有五种运动模式，并赋予了自然状态下线虫没有的“全局视觉”：通过运动控制和导航算法，精密操纵线虫机器人避障，一次性通过迷宫。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,562" src="https://img.36krcdn.com/20210701/v2_200b0152da9a44e188ff474ffb51c9a2_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲控制机器人线虫通过迷宫</p> 
<h2>03.</h2> 
<h2>为新型蛇形机器人研究提供新思路</h2> 
<p>论文第一作者董先科是一位90后青年学者，2012年在哈尔滨工业大学航天学院自动化专业完成本科学习，2014-2019年在加拿大麦吉尔大学机械工程系获得博士学位，主攻机器视觉、微型机器人，以及机器人精密操作研究方向。</p> 
<p>自2019年至今，董先科在加拿大多伦多一家科技公司任算法研发工程师，负责嵌入式高帧率目光跟踪系统的算法开发，以及在医疗AR和辅助驾驶场景的应用。此前他曾以第一作者身份获得机器人领域顶级学术会议ICRA 2015的最佳会议论文提名奖和最佳自动化论文提名奖。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,681" src="https://img.36krcdn.com/20210701/v2_21b721522530464383d03739ab52cba1_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲论文第一作者董先科</p> 
<p>他介绍道，微米环境下，由于物理定律的尺度缩小效应，粘滞力和摩擦力比重力要大几个数量级。因此微米环境下的自主运动模式，比如细菌的鞭毛运动、精子的游泳运动、线虫的蛇形运动等，与日常宏观运动模式有很大区别。</p> 
<p>生物拥有灵巧的身体和对环境的高度适应，具有可靠和高效的天然属性。将微米环境里生活的生物改造为微型机器人，是微型机器人领域的全新思路，也对日后人造微型机器人提供了前瞻性研究。</p> 
<p>目前广义蛇形机器人的开发往往将其等价为串联杆件模型，用拉格朗日方程进行刚体建模。但这种传统方法忽略了机器<a class="project-link" data-id="406849" data-name="人和环境" data-logo="https://img.36krcdn.com/20201021/v2_fe87b8c161c14e899112c3fafee8f845_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/406849" target="_blank">人和环境</a>复杂的力学交互，因此蛇形机器人运动速度和效率往往不高。</p> 
<p>本文通过建模仿真以及一系列实验，揭示了线虫在蛇形运动过程中肌肉的活性部位与身体的曲率之间存在相位差，并从理论和实验两方面验证了此相位差是驱动线虫蛇形爬行的运动模式的原因。该成果对新型蛇形机器人的设计建模与控制有重要的指导意义。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,758" src="https://img.36krcdn.com/20210701/v2_00c111a257fa4c92a4115d36007f8e61_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">▲线虫向前和向后爬行过程中的相位差异</p> 
<p>最后，本文示范了用微米激光束精密操控肌肉细胞活性的实验。此方法对其他生物瘫痪疾病的治疗也有启示意义。</p> 
<p>在这项研究中，研究团队做了很多基础的动力学研究，研究微米下的“蛇”如何爬动。也许将来某一天能以此为基础，做出人造的微米蛇形机器人，将之放到人的血管或者消化道里为人治病。</p> 
<p>董先科说，他接下来的研究计划是进一步设计尺寸稍大的人造蛇形机器人，然后用现在做出来的模型进行控制，因为更多地考虑到了机器人和环境的力学交互，预想可能提升很多方面的性能。</p> 
<p>另一方面，这个线虫机器人可以作为一个研究线虫神经学的极佳平台，比如研究这个只有302个神经元的模型生物有没有习惯性记忆，或者怎么构成习惯性记忆。据他透露，有一些与线虫生物学家合作的课题正在开展。</p> 
<h2>04.</h2> 
<h2>结语：或启发线虫神经学及</h2> 
<h2>微型机器人相关研究</h2> 
<p>由于生物神经系统的工程或重新设计具有挑战性，再加上缺乏准确描述生物行为的生物力学模型，大多数生物混合微型机器人的设计仅涉及简单的生物组件，不具备在运动期间协调这些驱动组件的身体级智能。</p> 
<p>总体来看，这项将活线虫转化为微型软体机器人的新研究，为秀丽隐杆线虫及其他线虫的神经学研究提供了一个极佳的平台，亦对微米尺度下机器人的开发亦提供了开创性的思路。结合肌肉活性的荧光成像，该研究还对微米尺度下蛇形运动的动力学研究有示范意义。</p>  
</div>
            