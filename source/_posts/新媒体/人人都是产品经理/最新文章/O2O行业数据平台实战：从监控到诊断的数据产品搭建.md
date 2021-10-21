
---
title: 'O2O行业数据平台实战：从监控到诊断的数据产品搭建'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/CkMszoFfjvMExoG0SYCc.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 21 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/CkMszoFfjvMExoG0SYCc.jpg'
---

<div>   
<blockquote><p>10月的第一场会员直播，我们邀请到了前滴滴高级数据产品@高远老师，她将基于多年的数据产品经验，深度解析O2O行业场景及痛点，从监控——分析——诊断三个层次拆解数据产品的构建思路。本文为直播内容整理，内容有删改。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5184756 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/CkMszoFfjvMExoG0SYCc.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>大家好，我叫高远，之前就职于出行行业的一家头部公司，担任高级数据产品。近5年专注于出行行业、内容行业、工业方向的数据产品领域，掌握上述领域的体系化搭建方法，创新性地打造出数据产品独有方法论，深度参与主流数据平台（滴滴网约车和字节内容方向）上述系统的规划和设计；并对应用型数据产品有着深刻认知，在企业内部研发数据驱动、数据增长相关课程，累计学员超过1w人。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4aMJUCx2zvqpU3BpaNSe.png" alt width="606" height="341" referrerpolicy="no-referrer"></p>
<p>本次分享主要包括两大部分：<strong>第一部分</strong>先给大家解析一下O2O行业业务管理的一些相关痛点；<strong>第二部分</strong>是关于数据产品整体落地的实践，从level 1的数据监控，到level2的数据分析，再到到level3的数据诊断。</p>
<h2 id="toc-1">一、O2O行业业务管理痛点解析</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/LTARkKU2W6hmuQW8ylLZ.png" alt width="609" height="343" referrerpolicy="no-referrer"></p>
<p>先进入到第一个部分——O2O行业业务管理痛点解析。</p>
<p>作为业务型的数据产品，我用十四个字概括其核心要务就是：<strong>比业务更懂业务，让产品更加落地。</strong></p>
<p>那大家就要考虑应该如何深入到业务中去，如何让产品更好地落地。其实做数据产品也罢，做产品经理也罢，各种产品类型都万变不离其宗，也就是要聚焦用户。所以我们要很清楚我们的用户到底是谁？我们服务于谁？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Z0LClxUIzzFa4819R5Lh.png" alt width="604" height="340" referrerpolicy="no-referrer"></p>
<p>就上述问题我做了一个总结。大家可以看一下这个表格，我们服务于业务方，无非是面对两类人群，第一类是区域负责人和部门leader等管理人员，第二类是运营、策略、市场等业务人员。</p>
<p>首先来看一下管理人员最关注什么。管理人员需要第一时间产出相关数据，因为他需要通过这些数据去及时发现问题，并及时进行业务调整，所以数据监控对管理人员而言是非常重要的。另外，管理人员也想知道问题大概出在哪个环节。还有就是他们要做一些降本增效工作，所以需要知道如何去发挥人力最大的价值。</p>
<p>这些其实就是关于管理者的一些场景。那我们从需求层面来去抽象这些场景的话，可以概括为三点：</p>
<ul>
<li>第一，需要多种时间粒度去监控业务的发展情况，更好地去发现业务问题。</li>
<li>第二，需要快速知道关键指标异动背后的原因，及时进行策略方向的调整。</li>
<li>第三，也是管理人员的终极目标，即如何通过一套科学的产品去提高人效和钱效。比如说以前可能需要五个人负责一个城市，现在可能通过数据的助力一个人就可以负责五个城市。</li>
</ul>
<p>针对管理人员的这些需求，我们的解决方案里包含了L1阶段的数据监控，和L3阶段的数据诊断。这部分后续再给大家详细讲解。</p>
<p>接下来就是关于业务人员。业务人员经常会面临的场景可以总结为四类。</p>
<ul>
<li>第一，每次进行业务分析都耗时耗力，尤其是对于一些分析理论掌握得不够扎实的业务人员而言，他们的方法通常比较粗犷，没有办法很好地进行精细化运营。</li>
<li>第二，在O2O行业最重要的是供需，而长期供需是通过定价手段去调控的，那如何去证明这一次的调价策略是正确的，对城市是有益的，这需要业务去衡量。</li>
<li>第三，对于业务而言，如何分析和量化单点的、外部的、特殊的事件对整体业务的影响也是经常需要面对的工作，单点事件包括一些极端天气、节假日等。</li>
<li>第四，对于常见的业务问题怎样可以一站式解决，提升人效和钱效。</li>
</ul>
<p>同样地，根据这几个场景，对应可以提炼出业务人员的主要需求：</p>
<p><strong>一是</strong>B&C端需要一套可行可落地的方法进行精心化运营。<strong>二是</strong>通过数据产品更好地去评估定价。<strong>三是</strong>将单点事件对业务的影响量化出来。<strong>四是</strong>追求一个更高的水平，就是把数据产品做得更加智能化，能够一站式解决常见的业务问题，不再需要一个一个环节去定位。</p>
<p>在解决方案上，业务人员最关注的是数据分析，也就是L2的产品；其次是L3数据诊断方面的产品；最后也还会关注L1数据监控，但毕竟是业务人员，他们更关注的还是如何解决问题，所以数据监控只是作为辅助。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/HjiF6Dq5gJOvlLmGK0X0.png" alt width="596" height="335" referrerpolicy="no-referrer"></p>
<p>那刚刚我们说到的L1、L2、L3对应的数据监控、数据分析、数据诊断，这些究竟是怎样的概念？在整体的产品框架中起到怎样的作用？</p>
<p>大家可以看一下这个图。我们所有的产品都是在一些基础平台的模式上去建设的，具体可以分为对内和对外两大部分。</p>
<p>这次就重点给大家分析数据产品的对内建设，即红色虚线框内的内容。</p>
<p><strong>首先</strong>是关于L1数据监控方面是如何去落地到产品的；<strong>其次</strong>是分析层面的L2阶段，比如核心分析、定价分析及事件分析如何落地这些产品、推动业务的；那<strong>最高级别</strong>，也就是L3诊断层的话，主要是关于如何通过指标的诊断一站式解决问题。</p>
<p>接下来我将会把之前实际落地操作过的一些产品拆解到每个小点里给大家做详细讲述。此外，由于我之前做的是O2O的出行行业，所以会以出行行业为例给大家分享如何落地这三个方向的产品。</p>
<h2 id="toc-2">二、数据产品的落地实践：监控——分析——诊断</h2>
<p>接下来进入到第二个环节，也是本次课程的核心部分——数据产品的落地实践：从监控到分析到诊断。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/RAR0pPOaie7kb3chvi9b.png" alt width="606" height="341" referrerpolicy="no-referrer"></p>
<p>数据产品有三个层级。</p>
<p><strong>第一层L1叫数据监控</strong>，它可能是最基础的一层，就是必须具备的。如果用一个词去解释的话就是需要去<strong>“看数”</strong>，从繁杂的数据中提炼出最核心的指标进行监控。</p>
<p>在这个基础之上晋升一个层级到<strong>L2的数据分析</strong>，这个阶段要能够“<strong>用数”</strong>，专项问题专门解决，用统一的方法去解决专项问题，到这一步开始有一些思路和一些方向引导，去定位具体的问题。</p>
<p>第三层相对而言就比较难了，它是建立在L1和L2上的<strong>数据诊断</strong>产品，总结来说可以称之为<strong>“智数”</strong>，也就是从发现问题到分析问题再到一站式解决问题，通过人机结合的方式帮助运营完成这个过程。</p>
<p>接下来我们就分别讲解这三个层级该怎么搭建。</p>
<h3>1. 如何提取核心数据指标体系，高效把控业务表现</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/sNfgrXkdT36mOdxnta3s.png" alt width="600" height="338" referrerpolicy="no-referrer"></p>
<p>首先是数据监控这个环节。这个环节分四步走，<strong>第一步</strong>要去了解清楚盈利模式，<strong>第二步</strong>要根据盈利模式建构业务模型，<strong>第三步</strong>是在业务模型的基础之上抽象出一些指标分类，那由指标分类以及现在业务的一些痛点诉求最终就可以进入<strong>第四步</strong>——监控产品的搭建。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/xveCNcqG1rGu0UVl1DBh.png" alt width="602" height="338" referrerpolicy="no-referrer"></p>
<p>在盈利模式这块，抛开O2O这个行业来说，所有市面上的行业都可以用这一套理论去解决它的盈利模式。</p>
<p><strong>这个模式分为两个维度，维度一：是否省时间，维度二：是否直接提供价值。进而分为四个象限，其实每一种业务都可以映射到这个模式里。</strong></p>
<p>比如<strong>第一象限的省时间且直接提供价值就可以对应工具类业务，</strong>像拍照工具、支付工具等，这些都是可以以免费模式去提供给用户的，当然可能会有一些增值服务去收取额外的一些费用，这部分其实就是这类业务的盈利模式。</p>
<p>然后<strong>第二象限对应的就是内容类业务，</strong>再细分的话可以分为两种，第一种是自研模式，比如以售卖课程为主的业务；还有一种是流量模式，像短视频领域。</p>
<p>那<strong>第三个象限的话是一些社交类业务，</strong>比如聊天软件等，这走的也是流量模式。</p>
<p><strong>最后一个象限对应的是我们今天要重点讲解的交易类业务。</strong>就比如O2O行业，走的是佣金模式，因为O2O是融合线上线下的一个模型，这个模型本质是为了撮合B、C两端的交易，我们就通过撮合这样的交易从中获取佣金，这就是O2O行业的盈利方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/i7ZcWim21cyTCw2fZoyW.png" alt width="599" height="337" referrerpolicy="no-referrer"></p>
<p><strong>关于O2O行业使用的佣金模式，它的利润公式是这样的：利润=单笔应收金额*（1-分账比例）*单量</strong></p>
<p>举个简单的例子，比如在出行行业，用户今天上班打了一次车，然后我们收了一百块钱，那这一百块钱就是对应公式里的“单笔应收金额”；“分账比例”则是给司机的那一部分，剩下的就是给我们平台中心；“单量”其实就是数量。</p>
<p>在实际过程中，除了分账比例外有时候还需要扣除一些额外费用，比如补贴率，因为有些地方可能缺需求，那我们可能就会通过一些活动去补贴乘客；以及可能还有一些管理费用，所以要把所有成本都减掉。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/MFFXHI1PziAFTFj4N6V2.png" alt width="607" height="342" referrerpolicy="no-referrer"></p>
<p><strong>出行行业的利润是通过促成B&C端的交易来获取的，那么根据刚刚的利润公式，要达到利润最大化，无非就是提高单笔预售金额，降低分账比例，提升单量。</strong></p>
<p>当然，对于B端和C端又有不同的处理方式。假设我们平台想通过提升单量来实现利润最大化，需要思考的是如何帮助业务去刺激更多需求，也就是让更多人去打车；而对于司机端，只有降低分账比例才能提高我方利润。这样就会导致平台和司机的利润矛盾，所以你<strong>需要去寻求平衡点——一个让平台和司机都相对满意的最优值，</strong>比如看看能不能让司机获得一些额外收入。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/jcGKNU7EnzDcvDWbU14G.png" alt width="601" height="338" referrerpolicy="no-referrer"></p>
<p>在刚刚的基础上再做一些拆解，把相关指标分类提取出来，从而得到一张业务流程图。</p>
<p>平台的目标是提高利润，那我们就通过流程拆解分析当前进度、差距以及挖掘增长洼地。</p>
<p><strong>对于O2O平台而言，万变不离其宗，最重要的就是供需，关键就是去提升总量、调整结构。乘客端和司机端就像是翘翘板的两端，需要平台去平衡。</strong>无论是是刺激乘客还是激励司机，都需要通过一定的策略去实现，比如采取补贴活动。但是活动的效果有时候可能并不好，说我们补贴的一些活动，进而评估活动效果和ROI。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/JYFPkOs1CyerhhBaYuzK.png" alt width="608" height="342" referrerpolicy="no-referrer"></p>
<p>在这个基础上继续拆解得到这张图，实际上就是将刚才的利润公式进一步细化，并且分别对应B端和C端。</p>
<p>像应收金额=C端的需求订单量*（B端的需求应答率*订单完成率），因为一份订单并不是直接就能达到完单的效果，还要看转化率。</p>
<p>按照这样把利润公式里的指标进行一层一层细拆下来的话，可以分为六类指标。</p>
<p><strong>第一类是财务指标，</strong>比如利润、补贴等；<strong>第二类是C端相关指标，</strong>在O2O行业的话就是乘客相关指标，比如需求订单量、C端补贴等；<strong>第三类是B端相关指标，</strong>包括需求应答率、订单完成率、司机在线时长、B端补贴等。这三类属于<strong>纵向指标。</strong></p>
<p><strong>横向指标</strong>分类也包括三大类，<strong>第一类是订单相关指标，</strong>比如订单的转化如何，是否存在漏洞，整体完成效果怎么样；<strong>第二类是体验相关指标，</strong>比如司机的差评率，或者司机是否有投诉乘客等，虽然体验这块占比会比较小，但对于平台的伤害却是比较大的，比如用户打车觉得坐车环境比较差、有气味儿之类的，可能下次就不会选这个司机了；<strong>第三类是策略相关指标，</strong>比如做活动花了多少钱等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/zzUSbGkIoRnw36ZUXpjp.png" alt width="608" height="342" referrerpolicy="no-referrer"></p>
<p>指标分类梳理清楚了之后就到了数据监控产品的落地环节。</p>
<p>有人就会说，做监控可以用excel 报表或者一些通用看板，为什么要定制化看板，这样不是更加耗时耗力吗？</p>
<p>根据我之前的经验，每一种方式都各有利弊。<strong>首先是Excel报表的方式，</strong>这种方式的优势就是数据获取灵活，自由度高，上手比较容易。但是缺点也多，比如自写sql难度会比较高，因为写sql的链路非常长；还有就是数据口径难以保证、可视化效果差等，所以这种方式其实不适用于长周期数据，比如在出行行业，当你拿到某条业务线全年的数据，这个Excel 报表可能得有几百兆，根本打不开。</p>
<p><strong>其次是通用报表，</strong>很多企业会购买市面上一些比较成熟的报表比如Tableau、FineBI，这些通用报表其实也非常强大，数据非常全面，使用也比较简单，都根据行业上一些标准方案去做的。同样地，这种方式也存在一定的缺点，比如对于业务而言功能相对单一，查询性能也比较有限，还无法添加个性化功能。就比如说我想快速看一下日均数据、周均数据，或者需要可视化表达比较好的方式去展现同环比等，这类个性化功能比较难以实现，所以无法灵活地进行业务扩展。</p>
<p><strong>因此，定制化开发的数据监控产品就应运而生了。</strong>那它的优点还是比较多的，首先是数据全面；其次是功能强大、贴近业务，因为一切都是定制化的，你可以根据现在的业务特点去增加一些数据功能；另外，这种方式还可以支持多种时间粒度，就比如日均、周均、月均这些数据，各种丰富维度都可以实现；最后可视化效果也比较好，最重要的是数据产出非常稳定。但唯一一个缺点就是需要进行定制开发。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/6IRuvTl8aU7VWHdYTwSH.png" alt width="597" height="336" referrerpolicy="no-referrer"></p>
<p><strong>总结而言，数据监控就是去解决管理者日常进行数据监控要面临的场景，着重服务于管理者。</strong></p>
<h3>2. 以B端为例，通过运营、定价等分析落地数据产品</h3>
<ul>
<li>数据分析之核心分析</li>
<li>数据分析之定价分析</li>
<li>数据分析之事件分析</li>
</ul>
<h3>3. 数据驱动产品，数据诊断建设三步走</h3>
<ul>
<li>数据诊断之整体结论</li>
<li>数据诊断之原因分析</li>
<li>数据诊断之专属策略</li>
</ul>
<p>囿于篇幅有限，想要观看完整视频的朋友可扫描下方海报的二维码添加会员学习顾问@小熙老师的微信（微信号：qdxyx520）并备注“高远”，即可获得观看链接。</p>
<h2 id="toc-3">三、本月直播回顾</h2>
<p>本次会员直播课程，高远老师为大家详细拆解了数据产品的构建思路，希望大家都能学以致用，以数据驱动业务发展！</p>
<p>每周三/四晚上8点，起点学院会员平台都会邀请一线的互联网产品、运营实战派专家，与大家分享最新的产品行业动态、运营玩法和干货知识。</p>
<p>每个月的会员直播都有月度主题，每周直播围绕月度主题展开。本月主题如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/cbS9YJOI3CpYasksHEiK.jpg" alt width="546" height="894" referrerpolicy="no-referrer"></p>
<p>扫描上方海报的二维码添加会员学习顾问@小熙老师的微信（微信号：qdxyx520）并备注“高远”，即可获取完整课程的链接。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5183164" data-author="793690" data-avatar="http://image.woshipm.com/wp-files/2019/06/uG3dh92gIrgmElEfyaWm.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            