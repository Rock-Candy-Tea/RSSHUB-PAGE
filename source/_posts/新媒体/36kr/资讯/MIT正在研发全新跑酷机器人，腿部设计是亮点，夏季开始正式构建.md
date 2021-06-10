
---
title: 'MIT正在研发全新跑酷机器人，腿部设计是亮点，夏季开始正式构建'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210610/v2_82ac792eaaba4989872e325276031c7f_img_000'
author: 36kr
comments: false
date: Thu, 10 Jun 2021 05:23:38 GMT
thumbnail: 'https://img.36krcdn.com/20210610/v2_82ac792eaaba4989872e325276031c7f_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/XgdUJgpMKNIvisz6T_-PSQ">“大数据文摘”（ID:BigDataDigest）</a>，36氪经授权发布。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,604" src="https://img.36krcdn.com/20210610/v2_82ac792eaaba4989872e325276031c7f_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">来源：IEEE</p> 
<p>过去很长一段时间以来，科学家们执着于开发出一个能在平坦的表面上行走而不会摔倒的双足机器人。</p> 
<p>如今，随着Agility Robotics和Boston Dynamics等公司的努力，我们甚至可以期望双足机器人在某些动态任务上能达到或超过人类的表现。</p> 
<p>那下一步呢？</p> 
<p>人类在进步，机器人同样。双足机器人的下一歌目标似乎是要突破人类表演的极限，也就是杂技。</p> 
<p>我们知道，IHMC一直在开发一款名为Nadia的儿童大小的杂技人形机器人，现在，MIT的Sangbae Kim实验室也加入了进来，研究人员表示，他们正在研究新型杂技机器人。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,658" src="https://img.36krcdn.com/20210610/v2_aefee2881ea7463aa3f9f470bb650f08_img_000" referrerpolicy="no-referrer"></p> 
<p>麻省理工学院仿生机器人实验室已经研发出了各种机器人，包括Cheetah和HERMES。最近，他们一直在用Cheetah进行了各种研究，比如步态探索和一些简单的四足杂技。</p> 
<p>在最近发表在arXiv上的一篇论文中，Matthew Chignoli、Donghyun Kim、Elijah Stanger-Jones和Sangbae Kim描述了“一种新的人形机器人，一种可感知执行器的运动规划器，和着陆控制器，作为用于人形机器人高动态运动控制的实用系统设计的一部分”。</p> 
<p>不仅仅是机器人本身，还有所有必要的软件基础设施，以使其按照他们的意愿行事。</p> 
<p class="image-wrapper"><img data-img-size-val="960,966" src="https://img.36krcdn.com/20210610/v2_bbc9ea882d4341a18cdee3752d7f83a8_img_000" referrerpolicy="no-referrer"></p> 
<p>首先让我们谈谈硬件，这是MIT的人形机器人是通过模拟实现的。麻省理工学院的Matt Chignoli说，它的外观看上去有点像Cheetah的直立版，但这其实是不正确的。虽然机器人的躯干和手臂与Cheetah非常相似，但腿部设计是全新的，并具有重新设计的执行器，具有更高的功率和更好的扭矩密度。</p> 
<p>Chignoli在一封电子邮件中写到：“腿部设计的主要重点是，实现人类步行和跑步时的那种平滑动态的‘脚跟到脚趾’动作，同时保持低惯性以与地面接触进行顺畅的交互。”“动态脚踝动作在类人机器人中很少见。我们希望开发出能够模仿人类腿部动作的健壮、低惯性和强大的腿部。”</p> 
<blockquote> 
 <p>设计策略很重要，因为在类人机器人领域，目前由液压驱动机器人和具有串联弹性致动器的机器人主导。随着我们继续提高本体感受执行器技术的性能，我们的目标是，证明高扭矩密度、高带宽力控制和减轻冲击能力的独特组合是高动态的最佳选择，对于任何有腿机器人来说都是如此。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,488" src="https://img.36krcdn.com/20210610/v2_fa19c588368e458e93ef1ec2053e678b_img_000" referrerpolicy="no-referrer"></p> 
<p>这项工作看上去似乎很容易，但那只是模拟，你可以在模拟中<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>任何东西。研究人员正在投入大量工作来准确地模拟动作，尤其是机器人在执行动态<a class="project-link" data-id="33557" data-name="运动时" data-logo="https://img.36krcdn.com/20200729/v2_0ef362a802ce420296a14241d13feb79_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/33557" target="_blank">运动时</a>运行的详细物理约束的建模，这样就能让规划者考虑到这些限制，从而使最终的实际运动与模拟得以准确匹配。</p> 
<p>“当谈到机器人的能力时，我们在模拟中展示的任何东西都应该在机器人上可行，”Chignoli说，“我们模拟了包括机器人执行器和电池的详细模型，这些模型已经过实验验证。这种详细的模型并不经常包含在机器人的动态模拟中”。</p> 
<p>“尽管我们相信我们的模拟器能够以高保真度准确模拟我们机器人的物理能力，但其仍有一些不确定性，因为我们的目标是将特技动作部署到硬件上，”Chignoli解释道，“主要的困难是状态估计，我们一直在利用与无人机状态估计相关的研究，该研究利用了视觉里程计。但是，如果没有组装的机器人来测试这些新的估计策略，就很难判断模拟是否为这些类型的事物的真实转移”。</p> 
<p>如今，MIT Humanoid的设计已经完成，预计在夏天开始进行建造，最终目标是让机器人能在具有挑战性的地形上跑酷。根据Chignoli的说法，真正重要的贡献是框架而不是机器人本身：</p> 
<blockquote> 
 <p>我们在人形机器人上展示的杂技动作与实际杂技无关，更多地是关于完成此类动作的能力对硬件和控制框架意味着什么。就机器人的能力而言，运动很重要，因为我们证明，至少在模拟中，我们可以使用完全不同的驱动方案复制波士顿动力ATLAS的动态特性。</p> 
 <p>当人们考虑如何设计下一代动态人形机器人时，验证本体感受器可以实现执行此类运动所需的扭矩密度，同时保留低机械阻抗和高带宽扭矩控制的优势非常重要。</p> 
</blockquote> 
<p>相关报道：</p> 
<p>https://spectrum.ieee.org/automaton/robotics/humanoids/mit-dynamic-acrobatic-humanoid-robot</p>  
</div>
            