
---
title: '波士顿动力Atlas的后空翻怎么实现的？这篇论文给出了方案'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210527/v2_3d78bbc2b1c241a0be07a0d9b49d17e3_img_000'
author: 36kr
comments: false
date: Thu, 27 May 2021 08:00:23 GMT
thumbnail: 'https://img.36krcdn.com/20210527/v2_3d78bbc2b1c241a0be07a0d9b49d17e3_img_000'
---

<div>   
<p>编者按：本文来自微信公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/8jWxFIUbgh8ta4YkzThqAA">“新智元”（ID:AI_era）</a>，作者：新智元，编辑：LQ，36氪经授权发布。</p> 
<blockquote> 
 <p>波士顿动力的人形机器人Atlas表演的后空翻让人印象深刻，可是这类高难度的动作如何实现？近期MIT团队的成果给出了一个解决方案。</p> 
</blockquote> 
<p>几个月前，波士顿动力的人形机器人Atlas展示了一些新的技巧动作：毫不费力地单脚站立，扭摆身体、鬼步舞也不在话下，大有称霸舞池的架势。</p> 
<p class="image-wrapper"><img data-img-size-val="640,332" src="https://img.36krcdn.com/20210527/v2_3d78bbc2b1c241a0be07a0d9b49d17e3_img_000" referrerpolicy="no-referrer"></p> 
<p>不仅如此，Atlas还会后空翻，大大刷新了大家对人形机器人的印象。</p> 
<p>不过，Atlas发布三年以来，关于设计方法、面临的挑战，如何复刻其方法等问题并没有补充说明。</p> 
<p>对于执行其他高难度动作，只能推测是由精心设计的规划和复杂算法完成的。</p> 
<p>近日，MIT和马萨诸塞大学阿默斯特分校的研究人员给出了一种解决方案，展示了像空翻或旋转跳跃这类特技动作，相关论文已经发在arXiv上。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,128" src="https://img.36krcdn.com/20210527/v2_c84e30ce9e764b3da668fea6c67735f6_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">△ 论文 https://arxiv.org/abs/2104.09025</p> 
<p>他们设计了一种新的人形机器人，可以完成后空翻和其他杂技动作，该机器人由感知驱动器的动态运动规划器和着陆控制器支持。</p> 
<p class="image-wrapper"><img data-img-size-val="480,483" src="https://img.36krcdn.com/20210527/v2_4d2bbbb0066945e0b56877907467ced1_img_000" referrerpolicy="no-referrer"></p> 
<p>根据负责软件和控制器开发的研究人员Donghyun Kim介绍，「在这项工作中，我们试图提出一个真实的控制算法，使人形机器人做特技动作，如后/前/侧翻，旋转跳跃，并越过障碍，为了做到这一点，我们首先通过实验确定了驱动器的性能，然后在运动规划器中确定了主要的限制。」</p> 
<p class="image-wrapper"><img data-img-size-val="537,248" src="https://img.36krcdn.com/20210527/v2_ace3019cb5e84bedad2b7c6be94ca656_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">△ 该项目的人形机器人从0.4米的平台上进行后空翻的动作</p> 
<h2>关键在驱动器</h2> 
<p>为了执行高度动态的动作，机器人驱动器很关键。</p> 
<p>大多数现有的机器人设计并没有完全解决硬件相关的挑战，例如在高扭矩/高速<a class="project-link" data-id="33557" data-name="运动时" data-logo="https://img.36krcdn.com/20200729/v2_0ef362a802ce420296a14241d13feb79_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/33557" target="_blank">运动时</a>可能发生的电压下降。</p> 
<p>Donghyun Kim和同事开发了一种新的方法，可以处理在运动规划和控制过程中与高度动态机器人行为相关的限制。结合他们提出的人形机器人设计，这种方法可以实现更多的动态动作，如杂技。</p> 
<p>根据Donghyun Kim的介绍，「我们开发的新型人形机器人与过去开发的其他人形机器人最显著的区别在于驱动器，驱动器<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了极大的改进，我们已经在四足机器人、 MIT Cheetah 1, 2, 3和mini-cheetah机器人上进行了展示。同样的驱动器技术，高度后向驱动，快速和准确的扭矩控制，紧凑和强健的形状因素都将用于新的人形机器人。」</p> 
<p class="image-wrapper"><img data-img-size-val="1008,756" src="https://img.36krcdn.com/20210527/v2_f127e2fd18d74330be216d4c5ab59168_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">△ Cheetah 3</p> 
<p>与过去开发的其他人形机器人相比，该团队的研究人员Sangbae Kim设计的新机器人极具活力且非常高效。这将使它能够完成更高要求和更复杂的任务。</p> 
<p>「执行动态动作对于机器人来说是具有挑战性的，因为他们的操作者必须首先了解硬件和软件之间的相互关系，在这项工作中，我们试图在此前经验基础上，解决控制算法中动态动作的关键硬件限制。」Donghyun Kim 说。</p> 
<p class="image-wrapper"><img data-img-size-val="446,277" src="https://img.36krcdn.com/20210527/v2_84fd6235cfc045c9b9aa687ce1e32fc5_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc"> 上：180°旋转跳 下：站立前空翻</p> 
<p>Kim和他的同事们已经对他们的机器人设计、运动规划器和着陆控制器进行了现实环境模拟测试。测试结果表明他们的机器人应该能够做各种杂技动作，包括后空翻、前空翻和旋转跳跃，非常有前景。</p> 
<p>接下来，这个人形机器人有望高效完成很多复杂任务。同时，研究人员也计划在现实场景中测试他们的设计、运动规划器和控制算法，继续推进腿式机器人的动态能力，还计划在控制算法中加入一个感知系统，使机器人能够更好地回应外部环境的变化。</p> 
<h3>参考资料</h3> 
<p>https://dhkim0821.github.io/</p>  
</div>
            