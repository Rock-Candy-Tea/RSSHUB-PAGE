
---
title: 'CPU 为什么很少会坏？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-03-06 14:08:20
thumbnail: 'https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">温戈，</span><span class="bio">想当作家的 数字芯片设计工程师 公众号：OpenIC</span>
<a href="https://www.zhihu.com/question/20943539/answer/2365920874" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>在计算机的一生中，CPU 坏的概率极小。正常使用的情况下，就算其他主要的电脑配件都坏了，CPU 都不会坏。</p>
<p><strong>CPU 出现损坏的情况，多数都是外界原因。最主要的就是长期在超频下工作，且散热性差，引起电子热迁移导致的损坏。</strong></p>
<p>现在的个人电脑的更新换代基本不是由于 CPU 损坏才换的，主要是因为软件不断的升级、越来越大，造作系统的垃圾越来越多导致卡顿，让你无法忍受，才换电脑的。</p>
<p>CPU 在出厂之前，是经过非常严格的测试的，甚至在设计之初，就要考虑测试的问题。可以从 pre-silicon、post-silicon 和硅的物理性质等方面来解释这个问题。</p>
<p><strong>1、CPU 被做成产品之前被检出缺陷</strong></p>
<p>这一个阶段也就是芯片 tape out 之后，应用到系统或者产品之前。</p>
<p>事实上，在现在的芯片设计中，在设计之初就已经为芯片的制造，测试，以及良率做考虑了。保证这一步能检测出芯片的缺陷，主要是 DFT+ATE 来保证。当然也有一些公司会做 DFD 和 DFM。</p>
<p><em>DFT = Design For Test</em></p>
<p><em>DFD = Design For Debug</em></p>
<p><em>DFM = Design for manufacture</em></p>
<blockquote><strong>DFT 指的是在芯片的设计阶段即插入各种用于提高芯片可测试性（包括可控制性和可观测性）的硬件电路，通过这部分逻辑，生成测试向量，使测试大规模芯片变得容易的同时，尽量减少时间以节约成本。</strong></blockquote>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-65e4d53411d0d979d58e4bffa4948070_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>图片来源于网络</figcaption></figure>
<p><strong>DFT--</strong>可测性设计<strong>，按流程划分，依然属于设计阶段（pre-silicon），只不过是为测试服务的。</strong></p>
<p><strong>而 ATE（Auto Test Equipment ）则是在流片之后，也就是 post-silicon 阶段。</strong></p>
<p>ATE 测试就是为了检查制造缺陷过程中的缺陷。芯片测试分两个阶段，一个是 CP（Chip Probing）测试，也就是晶圆（Wafer）测试。另外一个是 FT（Final Test）测试，也就是把芯片封装好再进行的测试。</p>
<p>CP 测试的目的就是在封装前就把坏的芯片筛选出来，以节省封装的成本。同时可以更直接的知道 Wafer 的良率。CP 测试可检查 fab 厂制造的工艺水平。现在对于一般的 wafer 成熟工艺，很多公司多把 CP 给省了，以减少 CP 测试成本。具体做不做 CP 测试，就是封装成本和 CP 测试成本综合考量的结果。</p>
<p><strong>一片晶圆越靠近边缘，die（一个小方格，也就是一个未封装的芯片）出问题的概率越大。测出坏的芯片根据不同坏的情况不同，也会分 bin，最终用作不同的用途。</strong></p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-9cf50f70930b8cbf0e45b9c0a00c5062_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>图片来源于网络</figcaption></figure>
<p>所以在芯片被做成成品之前，每一片芯片都是经过量产测试才发货给客户的。</p>
<p><strong>2、做成成品出厂以后，在使用过程中坏掉了</strong></p>
<p>就单个晶体管来看，在正常使用过程中，真的那么容易坏掉吗？其实不然。</p>
<p><strong>硅由于物理性质稳定，禁带宽度高（1.12ev）,而且用作芯片的硅是单晶硅，也很难发生化学反应，在非外力因素下，晶体管出问题的概率几乎为零。</strong></p>
<p>即使如此，芯片在出场前，还要经过一项测试，叫“老化测试”，是在高 / 低温的炉里经过 135/25/-45 摄氏度不同温度以及时间的测试，以保证其稳定性和可靠性。</p>
<p>根据芯片的使用寿命根据<strong>浴盆曲线</strong>（Bathtub Curve），分为三个阶段，第一阶段是初期失效： 一个高的失效率。由制造，设计等原因造成。第二阶段是本征失效： 非常低的失效率，由器件的本征失效机制产生。第三个阶段： 击穿失效，一个高的失效率。而在计算机正常使用的时候，是处在第二阶段，失效的概率非常小。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-f7092207f3c1f017acce84028232b96c_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>图片来源于网络</figcaption></figure>
<p><strong>但是，耐不住有上百亿个晶体管啊...... 所以，还是有坏的概率的。</strong></p>
<p>就算是某个晶体管坏了，芯片设计中会引入容错性设计，容错性设计又可以从<strong>软件和硬件</strong>两个方面来实施。</p>
<p>比如多核 CPU 可以通过软件屏蔽掉某个坏的核心，ATE 测试后根据不同缺陷分 bin 的芯片，也会用在不同的产品上，毕竟流片是十分昂贵的。比如 Intel 的 i3，i5，i7 等。当然，也不是所有的 i3 都是 i5、i7 检测出来的坏片。</p>
<p>再比如存储器中一般存在冗余的信号线和单元，通过检查发现有问题的单元，从而用冗余的模块替换有缺陷的模块，保证存储的正常使用。</p>
<p>比如下面橙色的为冗余的 memory，红色的是坏的 memory，我们便可以通过算法把红色 memory 的地址映射到橙色备用的一个 memory 上。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-8db76c2a276524f001f7ae7a908f997e_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>芯片测试是极其重要的一环，有缺陷的芯片能发现的越早越好。如果把坏的芯片发给客户，不仅损失巨大，对公司的声誉也会造成负面的影响。</p>
<p><strong>在芯片领域有个十倍定律，从设计 -->制造 -->封装测试 -->系统级应用，每晚发现一个环节，芯片公司付出的成本将增加十倍！！！</strong></p>
<p>高质量的测试是由 DFT，ATE，diagnosis，EDA 等多方面协作完成的，尤其在超大规模集成电路时代，测试变得越来越难，越来越重要，其开销在整个芯片流程中也占有很大的比重。芯片作为工业皇冠上的明珠，所有电子系统的大脑，是万万不能出问题的！</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-5d5d68939fd4df750543317ff5fb4820_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/20943539">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            