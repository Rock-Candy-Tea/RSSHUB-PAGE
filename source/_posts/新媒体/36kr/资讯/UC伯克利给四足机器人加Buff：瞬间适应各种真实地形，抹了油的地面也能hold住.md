
---
title: 'UC伯克利给四足机器人加Buff：瞬间适应各种真实地形，抹了油的地面也能hold住'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210712/v2_2deb4025de22408d89445a7e6b615f57_img_000'
author: 36kr
comments: false
date: Mon, 12 Jul 2021 09:41:09 GMT
thumbnail: 'https://img.36krcdn.com/20210712/v2_2deb4025de22408d89445a7e6b615f57_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/V3QrkUrYkRONvOXd_uS0-Q">“量子位”（ID:QbitAI）</a>，作者：丰色，36氪经授权发布。</p> 
<p>随着四足机器人的应用越来越成功，它们面对的场景也会越来越多：</p> 
<p>今天爬楼梯，明天过草地，后天又去坑坑洼洼的石子地……</p> 
<p>这么复杂多变的地形它们可hold不住，分分钟给你表演个人仰马翻。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_2deb4025de22408d89445a7e6b615f57_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p>不过现在，来自UC伯克利、卡内基梅隆大学以及Facebook AI的研究人员发明了一种新算法：</p> 
<p>不需要任何参考轨迹，无需微调直接部署在机器人身上——</p> 
<p>就能让它们在瞬间适应各种复杂的新地形，一步都不带“走神”地穿过乱石、沙滩、楼梯、长植被、人为搭建的活动板等环境。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_89890207cd3b4451859d09b9c773d2fe_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p><img src="https://img.36krcdn.com/20210712/v2_fbb66c93d8c84389a55dcb50cf31e8c0_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p><img src="https://img.36krcdn.com/20210712/v2_459ae4a0f31749f793f2287bfb9cd2b1_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p><img src="https://img.36krcdn.com/20210712/v2_7bf6949e767b4c27acd45f8003ae0cd9_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p>在滴了油的垫子上也是健步如飞、突然被负重5公斤也没事！</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_e2f7e15fd2764c2aa16bd5b2c523a335_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p>这个对于人类来说非常简单的技能，机器人现在也拥有了……</p> 
<p>就问你厉不厉害（怕不怕）？</p> 
<p>ps.眼尖的朋友应该能看出来，这个项目用的机器人就是咱国产的A1，来自杭州的Unitree。</p> 
<h2>如何做到的？</h2> 
<p>这个算法被命名为RMA（Rapid Motor Adaptation，快速电机自适应）。</p> 
<p>由两部分组成：基本策略模块 (base policy, π)和自适应模块 (adaptation module, ϕ)。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_2e6b38faeadf42359c2466d3d16c940c_img_000" data-img-size-val="1080,701" referrerpolicy="no-referrer"></p> 
<p>算法完全在仿真环境中训练，然后直接部署于现实世界。</p> 
<p>训练分为两个阶段。</p> 
<p>第一阶段，将机器人当前状态、先前的动作、环境因素作为输入，使用model-free的强化学习进行基本策略训练。</p> 
<p>第二阶段，采用on-policy数据的监督学习，训练自适应模块通过历史状态和动作来预测外部参数（extrinsics），也就是该怎么下脚。</p> 
<p>部署阶段，自适应模块生成外部参数，基本策略模块生成所需的关节位置，并使用A1机器人的PD控制器转换为扭矩。</p> 
<p>总的来说，基本策略模块探测环境，并实际控制机器人的步态。</p> 
<p>自适应模块负责分析基本策略给的数据，并加以分析，然后告诉基本模块如何调整步态。</p> 
<p>两者协同工作以便在多样化的环境中实现实时适应。</p> 
<p>需要注意的是，该算法没有视觉输入！环境因素由机器人运动部件“感觉到”的力收集而来。</p> 
<h2>室内和室外测试</h2> 
<p>又到了评估性能的时刻，室内测试中，将三者：RMA、A1机器人本身的控制器、没有自适应模块的RMA进行了比较。</p> 
<p>结果发现，RMA以100%的成功率走下15cm高度的台阶，并以80%的成功率走过可变形表面（记忆泡沫床垫和微微不平整的泡沫垫）。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_ca50377909134ba280d2922396043cae_img_000" data-img-size-val="630,352" referrerpolicy="no-referrer"></p> 
<p>它也能够成功爬上斜坡和台阶。</p> 
<p>在油性表面上行走的成功为90%。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_f5c46e27ce9348da9c2ff6dbe18dad37_img_000" data-img-size-val="1058,248" referrerpolicy="no-referrer"></p> 
<p>而A1的控制器在不平整的泡沫上就只有20%的成功率。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_77060d746d184f0ba6b4ab732a0c7e15_img_000" data-img-size-val="644,438" referrerpolicy="no-referrer"></p> 
<p>没有自适应模块的RMA就基本啥也不行了。</p> 
<p>最下面的三张图表还说明了三种方法的有效载荷限制：</p> 
<p>A1控制器的性能在8Kg载荷下开始下降。</p> 
<p>没有自适应模块的RMA承载超过8Kg后就没法移动，不过倒是不会跌倒。</p> 
<p>而RMA则在负重、保持平衡与行走距离上碾压前两者。</p> 
<p>A1机器人的本身重量为12Kg。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_e0497651e4144026882bb0bec41ea6b8_img_000" data-img-size-val="1022,688" referrerpolicy="no-referrer"></p> 
<p>而在室外：RMA在沙子、泥堆、高大植被上行走或穿越灌木的成功率为100%（不会被草缠脚）。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_e544c977f7964b358016093dfe3e57bc_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p><img src="https://img.36krcdn.com/20210712/v2_9ec7095948fb4b8bb017e225e847e4f1_img_000" data-img-size-val="638,352" referrerpolicy="no-referrer"></p> 
<p>而在乱石堆上行走时成功率为80%。</p> 
<p>在铺满了枯枝败叶的自然阶梯上的成功率为70%。</p> 
<p>最后，研究人员表示，要开发出真正可靠的地形自适应机器人，现在的这个“盲人”机器人的装备还远远不够，还需配上视觉传感器等工具。这也是他们未来工作的一个重要方向。</p> 
<p>论文地址：https://arxiv.org/abs/2107.04034</p> 
<p>看大量实验效果请戳：</p> 
<p>https://ashish-kmr.github.io/rma-legged-robots/</p>  
</div>
            