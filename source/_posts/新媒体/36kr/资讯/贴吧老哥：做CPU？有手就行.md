
---
title: '贴吧老哥：做CPU？有手就行'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210727/v2_863a9f68f720415cad81664a7ab0034f_img_000'
author: 36kr
comments: false
date: Wed, 28 Jul 2021 00:58:25 GMT
thumbnail: 'https://img.36krcdn.com/20210727/v2_863a9f68f720415cad81664a7ab0034f_img_000'
---

<div>   
<p>如果有人和你说要“手搓”一颗CPU，我想大多数对于CPU行业有所了解的朋友第一反应都是“你在做什么梦？”。因为就算是目前成本最低的芯片，至少都采用<a class="project-link" data-id="32740" data-name="微米" data-logo="https://img.36krcdn.com/20200729/v2_b4bfc7107198481dbced94d15dd845c7_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/32740" target="_blank">微米</a>级工艺，不管是设计还是制作都需要专业机器的辅助，靠原始工具来制造几乎不可能成功。</p> 
<p>不过，如果是古董级别的CPU，那么人工自制的成功可能性还是有的，毕竟人类第一台计算机就是由一群工程师和科学家徒手打造的，最多就是用上了诸如焊枪等工具。如果说几十年前的人可以完成，那么在现代更发达的微电子工程学的指导下，制作一颗古董级处理器并不是一件困难的事情。</p> 
<p><strong>比如一位贴吧大神就自制了一颗CPU，并且成功运行了自己手写的二进制程序，被网友称为“肝上长了个人”“焊武帝”，</strong>如果你好奇他是怎么自制CPU的，小雷今天就带你<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>看看吧。</p> 
<h2><strong>如何手搓一颗CPU？</strong></h2> 
<p>手搓CPU之前，首先要了解CPU的基本构造，虽然经过数十年的发展，现代CPU在工艺上已经与最早的CPU有了很大区别，但是在基本构造上还是大致相同的。<strong>比如用于逻辑计算的运算逻辑部件，用于暂存指令、数据和地址的寄存器部件以及用于控制和分析指令的控制部件，小到普通的灯控芯片，大到超级计算器的处理器核心，基本上都遵循这个设计。</strong></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_863a9f68f720415cad81664a7ab0034f_img_000" referrerpolicy="no-referrer"></p> 
<p>在弄清楚了CPU的主要构造后，挡在面前的第一道拦路虎是电路设计，否则就连如何接线，接在哪里都会成为问题，更谈不上打造一颗处理器。可以用于CPU设计的软件有不少，这位手搓CPU的肝帝使用的Quartus就是一款由<a class="project-link" data-id="3968654" data-name="英特尔" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968654" target="_blank">英特尔</a>推出的设计软件，拥有强大的辅助功能。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_456664c98c6445978bd6f269ac5e56e0_img_000" referrerpolicy="no-referrer"></p> 
<p>在翻出<a class="project-link" data-id="4260438" data-name="了数" data-logo="https://img.36krcdn.com/20210422/v2_8e636ec7be434dd5bf7deebc8bed2b62_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/4260438" target="_blank">了数</a>年前用Quartus设计的原理图后，naiweide（贴吧手搓CPU的大神ID）开始打造移位寄存器，也就是我们上面提到的CPU关键部件之一。输入的数据会在经过并被分配到该去的位置，按照naiweide的描述“就像是现在马路中间的交警，指挥着数据什么时候该往哪里走”。</p> 
<p>可以说，如果移位寄存器出现问题，那么数据就会无法输入到正确的位置，导致无法正确执行指令，就像是出了“车祸”一样，无法通行。</p> 
<p>大家可以感受一下这个移位寄存器的大小。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_73bc6b910cea494fb7325c85b3eafc24_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_5dc4a3330e4a45ab99a04759671c0478_img_000" referrerpolicy="no-referrer"></p> 
<p>基本上用到的零件主要是二极管、三极管和电阻，此外还有作为地基的门电路，实际上后续的几个部件基本上也只需要这些零件即可，只不过是数量多寡的区别。</p> 
<p>在完成了寄存器的制作后，naiweide开始制作程序计数器，也就是上面提到的运算逻辑部件，这个模块可以说整个第一阶段最困难的，某种程度上来说也是最“劝退”的一个阶段（naiweide自称为此耗费了半个脑袋的头发，为他的头发默哀一下）。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_6e1164a976274577ad033d07ae89936b_img_000" referrerpolicy="no-referrer"></p> 
<p>程序计数器涉及到的零件数量远超寄存器，只要其中一个零件出现问题那么就会影响整个系统，而且缺乏有效的debug机制，想要找到故障位置也是相当困难。而在实际的焊接过程中，受焊锡量、焊接时间等因素的影响，看似正常的各个零件在实际运行时都可能出现意想不到的问题。</p> 
<p>比如在一次成功运行后，虽然肉眼之下一切正常，但是当naiweide用手机记录并慢放视频后，很快就发现程序计数器的执行速度忽快忽慢，而在正常情况下执行速度应该是恒定的，忽快忽慢就说明其中有一个硬件出现了问题。</p> 
<p>在经过一个星期的debug后，终于在硬件深处找到了一个焊接反了的二极管，再加上处理其他各种问题的时间，程序计数器花了超过一个月的时间才终于制作成功，而这还只是第一步，在将其与寄存器组合在一起后，能否正常运行还是一个未知数。</p> 
<p>为了更直观的给大家展示一下程序计数器的复杂程度，可以看一看naiweide拍摄的局部细节图。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_70877d3974954a36b61442a5b8914801_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_e084a04f92de4a488b11ccbdfaf7f4e8_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_0ad0a3455fc444e69d2d98dfbb1045f4_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_75e2b69f7def4d25b1384aca971ca39e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">最终完成版</p> 
<p>而且，在打造程序计数器的过程中，naiweide还发现自己的原理图存在严重问题，无法正确控制和分析指令，最终只能够一边debug一边对电<a class="project-link" data-id="3486" data-name="路图" data-logo="https://img.36krcdn.com/20210219/v2_29827f87c0294c679083236bab657724_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/3486" target="_blank">路图</a>进行修改，功夫不负有心人，最终成功点亮所有指示灯，<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了正常运行的回馈。</p> 
<p>在寄存器和程序计数器均完成后，接下来还要打造一个<a class="project-link" data-id="6632" data-name="指令集" data-logo="https://img.36krcdn.com/20210714/v2_949add4087f54678a4a1cb6db9763398_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4854500224" target="_blank">指令集</a>，用于解析和执行输入的指令，也就是控制部件。某种程度上，指令集的先进程度会直接影响到CPU的性能，但是对于naiweide打造的这个古董级CPU来说，能够正常运行就是成功的。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_c85d03d92f664fbeb7ae529633ebdecc_img_000" referrerpolicy="no-referrer"></p> 
<p>相较于程序计数器，指令集部分的设计和制作并不算难，但是同样会遇到许多问题，因为到了这一步已经需要将三大部件组合在一起进行测试，只要其中一环出现冲突，那么就会反馈出错误的信息和结果。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_833fbf33d2264c648b33129600a5e8f3_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_04a83869578b434a88c9dfd11662669f_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>在焊接上对应的硬件后，naiweide成功让这个古董级CPU成功运行了00H和01H两个指令，严格上来说，他已经成功打造了一颗真正的CPU，接下来的目标是使用这颗CPU实现流水灯效。</strong></p> 
<p>甚至在此之前，程序计数器部分又一次损坏，在经过详细检查后发现一颗二极管在运行过程中被电流击穿，完全损坏，在更换后才终于正常启动。</p> 
<h2><strong>真·写代码</strong></h2> 
<p>流水灯效，简单来说就是灯光依次亮起熄灭，是我们日常生活中最常见的灯效之一，在一般情况下，只需要一个小指甲盖大小的芯片就可以实现包括流水灯效在内的多种灯效控制。</p> 
<p>这么看来，似乎不难？毕竟只是灯光控制罢了，随便一个玩具都可能具备这个功能。但是，不要忘了这颗CPU是完全手工打造的，相当于完全自主研发的指令集和架构，所以没有办法从现有的资料中获得帮助，甚至连配套的编程语言都欠缺。</p> 
<p>那么，naiweide是如何解决编程问题的？<strong>很简单，使用最原始的机械语言——二进制，也就是由0和1组成的一长串数字代码。</strong>对于一般人来说，也许光是看着那一大串代码就已经头晕，并且觉得人类真的可以理解吗？实际上想要对其进行编译也不是什么异想天开的事情，一些常用的代码还是可以比较轻松记忆下来的。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_f37e6cbf2625443287a2555476965052_img_000" referrerpolicy="no-referrer"></p> 
<p>如果是利用现有的一些编程软件，其实也可以轻松的写下这段代码，不过naiweide还是使用了最原始的手写代码方式，来打造这颗CPU的第一个完整程序。至于输入程序的方式也是相当硬核，“扣”按键，在一块8位指令输入板上按照二进制代码的顺序依次扣动对应按键，输入完成后再进行第二条代码的输入。</p> 
<p>在完成指令输入后，naiweide发现程序并没有正常运行，在随后的检查中发现有地方的连接因为意外断开，而且程序设计上也有一些问题，最终重新编程后才成功运行了一套完整的流水灯效。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210727/v2_6e5098381a3947ad8c3100a28776c463_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>手搓CPU有意义吗？</strong></h2> 
<p>naiweide制作的这颗CPU，从性能和功能上来说可能还不如淘宝几块钱买的一颗处理器。根据作者描述，在最初启动的时候，主频只有可怜的1Hz，而在经过多次改进后，也仅仅提升到了100kHz。</p> 
<p>作为对比，淘宝售价5元的G620处理器主频为2.6GHz，也就是2600MHz，等于2600000KHz，也就是自制CPU的两万六千倍，考虑到更丰富完善的指令集和架构，实际差距还会更大。至于大家谈论CPU时常提的制程，该CPU大概是2.54mm制程，是目前的5nm先进制程的数十万倍。</p> 
<p>当然，单看性能什么的，肯定是没有意义的，naiweide制作CPU的初衷主要是想亲自验证一下二进制代码的执行过程，以及从零开始摸清楚CPU的运行逻辑，实践出真知，只有实际做过了，在随后的工作中才能更好的了解整个系统和硬件的运行过程。</p> 
<p>所以，从实用上看，确实没有多大意义，但是对于naiweide来说却是一个很好的学习及积累经验的过程。</p> 
<p>虽然不少评论都说只需要大学级别的知识就能制作出相同的作品，但是其中的毅力、耐心却很少有人具备，而这些恰恰是成功所具备的前置条件，所以小雷十分期待这位UP日后能够在这个领域做出更大的贡献。</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MjM5MTg5NTU0MQ==&mid=2653899886&idx=2&sn=3f15fc8589268c8291cedf8a4d8d66c4&chksm=bd7576f48a02ffe25aa93d1681a5f805cae90c9b7730e95f0b6d4fb316e378a69b8223c92daf&scene=27#wechat_redirect">“雷科技”（ID：leitech）</a>，作者：<a class="project-link" data-id="41584" data-name="雷科技" data-logo="https://img.36krcdn.com/20200729/v2_f2fd91dc27a341fd82b185abd25c5ae1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/41584" target="_blank">雷科技</a>互联网组，编辑：TSknight ，36氪经授权发布。</p>  
</div>
            