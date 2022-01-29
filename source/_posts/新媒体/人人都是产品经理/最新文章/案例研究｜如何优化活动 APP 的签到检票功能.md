
---
title: '案例研究｜如何优化活动 APP 的签到检票功能'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/01/S2bLF7dwsnJvZ97d4nej.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 29 Jan 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/01/S2bLF7dwsnJvZ97d4nej.jpg'
---

<div>   
<blockquote><p>编辑导语：有些 APP 可以让用户自由的策划活动并进行线上线下售票检票，作者以 Ticektleap的移动端 APP 为例，介绍她如何抓住 Ticketleap 移动端检票困难的痛点，并对此重新设计使用流程。本文说明了她对于整个 APP 的改版思路过程，从用户群定义、问题分析、详细设计、到最后的思考。推荐对APP改版感兴趣的用户阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5161867 aligncenter" src="https://image.yunyingpai.com/wp/2022/01/S2bLF7dwsnJvZ97d4nej.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>一场音乐现场演出的成功举办需要很多人的努力，从音响检查到开门检票，每一个节点都需要合理的人员安排。</p>
<p>在我们放热情的观众入场前，这些活动工作安排都需要定下来：评估调查舞台设备、各项条款与巡回经理达成一致、向 AV 技术人员传达指示、监督接待演出艺人等。</p>
<p><strong>最后一件我们需要去处理的技术问题是如何让观众进入</strong>。</p>
<p>Jazz Grooves 公司一直以来使用 Tickeleap 作为销售、营销、签到音乐会门票的首选平台。</p>
<p>尽管该公司的 Web 界面有很高的易用性，但我们在使用其手机端 APP 操作时遇到了许多问题，因此，我决定对它进行重新设计。</p>
<h2 id="toc-1">一、总览</h2>
<p><strong>Ticketleap 是一个设计用来提供活动门票的平台</strong>。</p>
<p>其移动端 APP 支持活动创建者在活动现场出售门票，并通过 QR 码或姓名让活动参与者检票入场。</p>
<p>但是，Ticketleap 的移动端产品几乎没有更新过，因此很遗憾地比竞品落后（例如 Ticketmaster 和 Eventbrite ）。</p>
<h2 id="toc-2">二、谁是 Ticketleap 的用户群体</h2>
<p>我将 Ticketleap 的用户群体分为两个主要组：<strong>活动策划者 </strong>和<strong> 活动参与者</strong>，本次优化主要关注 Ticketleap 的活动策划者用户群。</p>
<p>在阅读了很多有关 Ticketleap 的定价模型和产品分析文章后，我对 Ticketleap 的整体用户群有了更深入的了解。</p>
<p>该产品自豪于能够满足经验不足 / 个体的活动策划者的需求，让他们能自己动手、进行活动策划和落地：</p>
<ol>
<li>用户能够以非常低的成本建立完整的活动管理系统（售票、跟踪销售、促销活动），没有启动费或者合同。</li>
<li>即时性的付款功能，可以实现网络交易和现场交易。</li>
<li>因为平台低廉的票价手续费，门票销售规模可以和活动策划者想要的一样，小型和大型活动都能满足。</li>
</ol>
<p>考虑到这些，我整理出三种主要的用户画像：</p>
<p><img data-action="zoom" class=" aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/70V1owCdtMQUqWMy3CMp.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="675" height="283" referrerpolicy="no-referrer"></p>
<p>凯瑟琳（Catherine），亚历克斯（Alex）和简（Jane）都拥有一个共同的目标，那就是<strong>在没有太多</strong><strong>障碍的情况下去快速发布和宣传他们的活动</strong>。</p>
<p>他们的活动规模不同，导致了他们的检票过程不一样。</p>
<p>对于像凯瑟琳这样的人来说，她只打算卖几张工作坊的门票，那么检票 APP 的交互操作对她可能根本不重要。</p>
<p>像亚历克斯和简这样的大型活动策划者需要安排工作人员进行以下工作：</p>
<ul>
<li>在门口扫描门票，让活动参加者进入会场</li>
<li>为等待进入的用户提供其他形式的服务</li>
</ul>
<h2 id="toc-3">三、用户检票入场时会遇到什么问题</h2>
<p>大多数活动参加者会提前购票，这样可以直接扫码核销门票，当然，也会有一部分人希望在现场买票。</p>
<p>活动现场也会出现一些特殊情况，参加者丢失了门票的电子邮件，或是一些散客试图无票闯入。</p>
<p>Ticketleap APP 当前的设计给活动策划者带来了很大的压力，需要参与签到的工作人员处理多项任务。</p>
<p>这使参加者在排队的时候需要等待更长时间，才能进入场地。</p>
<h3>1. 为什么这个问题值得探索</h3>
<ol>
<li>活动策划者通过准确计算已售门票数量来维护参与活动的人数合理。计算错误 / 超过负荷会引发现场安全问题；</li>
<li>活动策划者希望让活动参加者保持愉悦的心情，这意味者要提高参加者的入场效率；</li>
<li>避免检票工作人员感到疯狂和不知所措，让他们能正常完成工作。</li>
</ol>
<p>针对活动策划者使用 Ticketleap APP 在检票时遇到的困难，我不禁想知道，Ticketleap APP 是否可以帮助活动策划者更轻松地提高检票的效率？</p>
<h2 id="toc-4">四、用户痛点</h2>
<h3>1. 导航</h3>
<p>在原始设计中，扫码核销页面汇聚了过多高频使用的核心功能，分散在页面的各个部位，影响操作效率。</p>
<p>同时，工作人员帮助活动参与者扫码检票时，如果需要进行其他操作 / 查看购票信息，只能打断操作，进行切换。</p>
<p><img data-action="zoom" class=" wp-image-742696 aligncenter" src="https://image.yunyingpai.com/wp/2022/01/Bo2u45OZolokU9HrZmKr.jpg" alt width="348" height="427" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="wp-image-742697 aligncenter" src="https://image.yunyingpai.com/wp/2022/01/oZJLlzjyFlDgFxwWyEji.jpg" alt width="587" height="342" referrerpolicy="no-referrer"></p>
<h3>2. 区分不同类的门票</h3>
<p>Ticketleap 的网页端应用程序能让活动策划者自定义活动页面，包括出售的门票类型。</p>
<p>这非常有用：例如，亚历克斯想要为队里球员的家人们保留座位，或者简想要为她的电影工作人员保留电影院的前排座位。</p>
<p><img data-action="zoom" class=" aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/GAktTyoFEj6xwb6Ida1s.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="562" height="327" referrerpolicy="no-referrer"></p>
<p><strong>但是随着选择的增多，就需要更多的配置和信息</strong>。</p>
<p>Ticketleap APP 很难去区分不同的选择。</p>
<p>信息，例如不同的门票种类，要么隐藏了，要么太小了，让检票人员很难迅速采取行动去满足活动参加者的需求。</p>
<p><img data-action="zoom" class=" aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/woFkKpqdPuYCwrs3u7Rc.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="526" height="306" referrerpolicy="no-referrer"></p>
<h3>3. 销售门票</h3>
<p>门票销售的流程很长，购买过程困难，而且不能撤销（没有办法在购物车里减少门票数量或者取消订单，除非用户离开当前页面）。</p>
<p>活动参加者在门口进行乏味冗长的购票流程，让他们等待入场的时间更长，也让排在他们后面的人等的时间更久。</p>
<p><img data-action="zoom" class="wp-image-742698 aligncenter" src="https://image.yunyingpai.com/wp/2022/01/hUUl4iTiL7V54DX5bhrs.jpg" alt width="547" height="221" referrerpolicy="no-referrer"></p>
<h3>4. 不一致的反馈信息</h3>
<p><strong>检票提醒和通知不一致</strong>。</p>
<p>Ticketleap APP 允许三种方式让活动参加者检票进入：</p>
<ol>
<li><strong>扫描门票；</strong></li>
<li><strong>查找姓名；</strong></li>
<li><strong>现场售票</strong>。</li>
</ol>
<p>但它也为活动参加者进行检票后提供了 3 种不同类型的反馈，反馈需要标准化以保持清楚和一致。</p>
<p><img data-action="zoom" class=" aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/AfuJEdMJ95z4R2yxf3HG.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="529" height="308" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、我的解决方案</h2>
<h3>1. 导航</h3>
<p>下图中你可以看到检票工作人员是怎么扫描门票的。</p>
<p>如果排队的人想买张票，你需要确保有足够的门票可以出售。</p>
<p>下图为原始设计和重新设计的对比，展示了如何查看剩余门票数。</p>
<p>注意新设计是如何减少了一步操作，同时使已检票的数字变得更加清楚。</p>
<p><img data-action="zoom" class="wp-image-742699 aligncenter" src="https://image.yunyingpai.com/wp/2022/01/LLetoneRxk5xfKBc9KqY.jpg" alt width="581" height="497" referrerpolicy="no-referrer"></p>
<p>在原始设计中，扫描后的参加者信息会全部展示出来，不管是重复的还是不必要的信息。</p>
<p>新设计清楚地展示了检票工作人员需要立即了解的数据：</p>
<ul>
<li><strong>检票状态</strong></li>
<li><strong>参加者的门票类型</strong></li>
<li><strong>检票入场时间</strong></li>
<li><strong>参加者姓名</strong></li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/FG7hWUvuKVzThoQffdhV.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="551" height="675" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/H57f9pTUeU62S6iCmPWk.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="557" height="683" referrerpolicy="no-referrer"></p>
<h3>2. 区分不同类的门票</h3>
<p>如果用户是和亚历克斯和简一样，需要自定义一些特殊票种，那么最重要的是帮助他们在检票时快速识别持有这些门票的参加者。</p>
<p>在下图的原始设计中，很难看到 Shelby 的门票类型以及她名下有多少张门票。</p>
<p>在新设计中，用户可以快速确定 Shelby 持用的门票类型，并只用检票一次，就能为 Shelby 团体中的每个人提供帮助。</p>
<p>使用这样的方式，如果 Shelby 的团体没有整体都到，可以稍后检票入场，而不需要让 Shelby 站在门口等他们。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/7x9WPDd9pZ47ykJghNGI.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="560" height="686" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/0LuHh2HfALG3NJIR6alq.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="550" height="674" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/Oac0ZEQC7r8U3O5V4IpM.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="578" height="118" referrerpolicy="no-referrer"></p>
<p>在检票确认通知中，<strong>新设计将门票类型确定为最大且最重要的信息</strong>。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/cazJgX6Q36K2UdidZaGB.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="575" height="705" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/M0MmiHysXZ8bDVVeThsj.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="565" height="692" referrerpolicy="no-referrer"></p>
<h3>3. 销售门票</h3>
<p>我极大地缩短了结账流程，并给用户留出了更多的容错空间。<strong>新设计的结账流程可以让检票工作人员轻松地进入和退出销售模式</strong>。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/4FdRMo4nXGmiHEyGpeBS.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="604" height="244" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/vvhXh5vrkD85dXwojlLw.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="611" height="382" referrerpolicy="no-referrer"></p>
<h3>4. 不一致的反馈信息</h3>
<p>同样，<strong>反馈的一致性对于用户在压力下迅速行动至关重要</strong>。</p>
<p>在新设计中，检票确认和上述的一样进行了优化。另外，<strong>请注意要保持反馈信息的一致性</strong>。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/ssObpW62NWtwbTzRgsco.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="618" height="604" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="案例研究｜如何优化活动 APP 的签到检票功能" src="https://image.yunyingpai.com/wp/2022/01/BU0TiIDzNnNuFSiOKl4T.png" alt="案例研究｜如何优化活动 APP 的签到检票功能" width="616" height="415" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、最后的一些思考</h2>
<p><strong>协助活动策划者自助完成整场活动的落地</strong>，<strong>需要平台能够包容用户的多样性需求</strong>。</p>
<p>尽管Ticketleap 在网页端表现良好，但其移动端 APP 仍需改进，它让经验不足的活动策划者在同时处理这两件事上非常困难：<strong>分辩多样的票种</strong> 和 <strong>保持高效的检票</strong>。</p>
<p>在这次的实践中我学到了，通过实际操作可以找到流程中需要改进的部分。</p>
<p>看到项目成员在看似简单的任务上挣扎了 20 秒后，我理解了问题出在哪里，以及我们该如何改善检票入场流程。</p>
<p>但是，如果无法到 Ticketleap 的公司内部进行研究，我不能确定他们当前是否发现了这些问题并进行优化，也无法了解内部真实遇到的问题。</p>
<p>因此，这个重新设计是基于我自己的研究和理解而推进的。</p>
<p> </p>
<p>原文：https://bootcamp.uxdesign.cc/operating-event-doors-with-ease-a-ticketleap-redesign-f49d0e884d6b</p>
<p>作者：Katie Shia</p>
<p>译者：陈羽姿；审核：李泽慧、张聿彤；编辑：孙淑雅</p>
<p>本文由@TCC翻译情报局 翻译发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5296575" data-author="1274336" data-avatar="http://image.woshipm.com/wp-files/2021/05/xCvopGF5HenULUrgReTS.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            