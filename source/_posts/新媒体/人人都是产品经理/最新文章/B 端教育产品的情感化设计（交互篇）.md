
---
title: 'B 端教育产品的情感化设计（交互篇）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5IocZOk3AlQDETGCtSw6.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 05 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5IocZOk3AlQDETGCtSw6.jpg'
---

<div>   
<blockquote><p>导读：B 端产品设计如何兼顾产品工具属性与情感化体验？如何通过设计让枯燥的学习过程变得有趣，把 “要我学” 变成 “我要学”，提升学员学习积极性？本文将通过我们在 B 端教育产品 「学习科学师训平台」小程序的设计经验，讲一讲如何做 B端教育产品的情感化设计。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4995552 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5IocZOk3AlQDETGCtSw6.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>一个教师的执教生涯中可能会经历上百次的教师培训，大到国家级培训、市级培训，小到区级培训、学校培训，既有线下集中培训，也有线上网课。国家为此投入了大量的人力物力财力，但由于部分网络培训课形式主义严重、教师培训内容“假大空”等原因，导致教师可能对培训有抵触心理。本应为教师带来专业知识的培训，却让老师身心俱疲。</p>
<p>因此，我们在本次师训产品设计过程中，充分考虑参加培训的教师心理，通过情感化的设计充分缓解老师的焦虑情绪，提升老师的参与度和积极性。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/BmwB2ynFLIihX3T5IHje.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">01 项目背景</h2>
<p>「学习科学师训平台」小程序（以下简称师训小程序）是我们为清华大学教师培训团队打造的一款用于培训青年教师的培训平台，其中认证培训板块是通过为期一个月的线上直播为主的培训课程，培养一批青年教师。让老师了解如何通过科学的心理学方法，理解和教育学生，提升老师的教学水平。</p>
<h2 id="toc-2">02 客户诉求&用户心理</h2>
<p>经过与客户的深入交流，总结其主要的设计诉求是，能够让参与培训的教师们在一种轻松、有趣的氛围中完成培训，同时加强教师与授课讲师的互动性。为什么客户会提出这样的需求呢？我们深入挖掘了教师参与线上培训时懈怠的原因，大致有以下几点：</p>
<ul>
<li>培训内容上，与自己想学的脱钩，或者内容太虚无法落地。</li>
<li>培训形式以线上视频为主，缺少参与感，有问题也得不到及时的交流和解答。</li>
<li>培训占用自己太多时间，平时备课上课已经非常忙碌，难以有精力和时间再上培训课程。</li>
</ul>
<p>综合考虑客户诉求及用户心理，我们认为应该为产品赋予更多情感化的元素，让参与培训的教师能够在轻松有趣的氛围下快乐学习，收获满满。</p>
<h2 id="toc-3">03 什么是情感化设计</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/qIOFGWPTLB0DKO0aFmyS.png" referrerpolicy="no-referrer"></p>
<p>美国认知心理学家 Donald A.Norman 在《情感化设计》一书中，分别从本能、行为、反思三个层次阐述了情感化设计的含义和作用。</p>
<p>其中，本能层次关注的是视觉及其他感官出于本能的直接反应，好看的外观是产品吸引人的第一步。</p>
<p>其次，行为层次关注的是使用的效率和乐趣，可通过满足用户的功能需求和提高易用性来实现。</p>
<p>最后，反思层次与用户的长期感受有关，需要建立品牌或产品的长期价值。只有在产品/服务和用户之间建立起情感纽带，通过互动影响产品在用户心中的形象、满意度、记忆等，才能形成用户对品牌的认知，培养用户对品牌的忠诚度。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/0eD9jB4bqY90EeE2CNSd.png" referrerpolicy="no-referrer"></p>
<p>结合产品的使用场景和客户、用户诉求，我们圈定了主要设计范围：</p>
<ul>
<li>本能层次：通过新的交互和视觉形式，塑造品牌形象，第一眼就能打动用户。</li>
<li>行为层次：打造一站式的高效学习工具，将零散分布在多个工具上的课程内容集成到师训平台，重点打磨核心的功能–直播和录播课的体验。</li>
<li>反思层次：给予用户成就感和荣誉感。引入激励机制，在认证培训的多个环节给予用户及时的正反馈，创造成就感，不断激励用户完成培训课程。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/wTWZJQvrOycnRGAA2rJ3.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">情感化设计的三个层次上的设计策略</p>
<h2 id="toc-4">04 什么是本能层次设计</h2>
<h3>4.1 本能层次的设计</h3>
<p>在本能层次上，我们希望传达给用户的感觉是轻松、愉悦，而不是传统、枯燥的培训体验。因此在交互形式和视觉表现上，我们做了轻量化的设计，并通过品牌的打造来提升品质感和加深印象。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xUchb0NW6SuIhcdaKaoS.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">本能层次上的设计策略</p>
<p><strong>4.1.1 新的交互视觉形式</strong></p>
<p>教育产品通常会把课程列表作为首页，让用户自己查找课程。这种形式足够安全稳定，却也相对刻板无趣。用户看到一个长长的课程列表，可能会产生压力感和焦虑感。</p>
<p>为了让用户第一眼就感受到轻松愉悦，我们将课表按轻重缓急做了样式上的区分，状态为“远未开始”和 “已结束”的课程不是用户最关心的，我们进行了弱化处理。重点突出“进行中”的课程，若无“进行中”的课程，则突出展示“即将开始”的课程。这样，用户只要关注当前最重要的课程即可。</p>
<p>课表以学习地图的形式串起来，根据课程完成进度依次点亮地图，营造过关斩将的快感。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/v8MQMfT9Ap1S90IIHyqx.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">对比列表形式及地图路径形式</p>
<p><strong>4.1.2 品牌影响力的建立</strong></p>
<p>在第一版学习地图设计中，客户并没有关注品牌设计，我们对客户的了解也有限，导致第一版小程序没有体现清华团队的特点和权威性。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/t6iCNQa3zMFNiz9r4qPT.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">第一版地图设计方案</p>
<p>因此，我们希望在第二版设计方案中，突出强调客户的识别性元素。经过与客户的深入沟通，我们了解到客户创业多年，已经有了许多品牌沉淀，包括老师的形象照、团队宣传视频、IP形象、学员感悟传播图片等。经过内部评估，我们决定采用老师形象和课程名句来打造品牌。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/3S5aTOFNop8EiCOhBoFe.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">客户品牌沉淀</p>
<p>最终，学习地图首页通过跳一跳的形式来展示每个课程节点，每次默认展示用户最近需要学习的课程，弱化其他课程。用户进入产品只需点击最大的课程卡片即可开始学习，减轻用户的心理负担，也可以通过上下滑动来查看其它课程。学过的课程节点和未学的课程节点通过颜色做区分，使用户能直观地感受到过五关斩六将的快感。</p>
<p>在课程卡片上呈现相关课程授课老师的形象照，突出清华老师的专业形象，加深学员对这些授课老师的印象，形成品牌认知。</p>
<h3>4.2 行为层次的设计</h3>
<p>在行为层次上，我们希望打造一个一站式高效学习工具，充分做好 B 端的工具体验。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vwdXiR9WWHTQdGtCnPeh.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">行为层次上的设计策略</p>
<p>整个认证培训的过程涉及直播课、录播课、微信互动课、线下课、线上考试等各种课程，类型多样，对应平台众多。客户原来的直播课程通过小鹅通来实现，录播课程要求学员到国家人事人才网学习，收集作业、问题答疑以及互动游戏则通过微信群来实现。</p>
<p>学员需要在多个平台上切换，极其影响培训体验。因此，我们希望通过师训小程序时，把这些零散的功能都整合到同一个平台，用户只要通过小程序，就能完成整个培训。</p>
<p><strong>4.2.1 一站式高效的学习工具</strong></p>
<p>根据客户当前的问题，我们进行了相应的功能设计，来打造一个高效的、沉浸式的学习工具。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/uq2kaxcL0wDBpingELbp.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">问题及解决方案</p>
<p>我们通过学习地图串起了所有散在各个平台的课程，用户可通过小程序访问线上课程、查看线下课地址以及直接跳转至人事人才网考试。</p>
<p>其中核心优化了直播和录播课的体验。</p>
<ul>
<li><strong>重点提升直播过程中的互动性，提升教师的参与感</strong>。重点关注问题收集和回答、点赞评论、上台连麦、作业评论环节，打磨核心上课体验。</li>
<li><strong>提升上课效率，减少对教师时间的占用</strong>。直播课提供短视频回放且可以选择倍速播放，每个问题回答自动剪辑为短视频，方便错过直播的教师回顾课程内容。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/JRn22oUEmKV2n0XHJXdc.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">直播互动和作业</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/PmBAOSqbeSmgpTBPKK33.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">直播答疑</p>
<h3>4.3 反思层次的设计</h3>
<p>反思层次的设计，在于更高层次地满足用户的精神需求，让用户获得自我成就的满足感。因此，我们搭建了一套激励系统，来激励教师持续学习。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/uvpKCgV0IueOxroTclFH.png" referrerpolicy="no-referrer"></p>
<p>首先我们来思考一个问题：</p>
<p>为什么你上课学习的时候总是走神，而玩游戏时总是停不下来？</p>
<p>我们可以从游戏设计中，学到很多让用户上瘾的方法。游戏设计的三大要素如下，我们将借鉴游戏的体验要素，应用到教育培训的产品设计中。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/OvapiCuntrSA4uld881N.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">游戏设计的三大要素</p>
<p><strong>4.3.1 即时、持续、随机的正反馈</strong></p>
<p>游戏和学习最大的区别在于，游戏能够及时、持续地给出玩家正像反馈，而学习则是延时反馈，学习效果要经过一段时间、积累到一定程度才能看到效果，坚持学习是件不容易的事。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/kkCs8IMJ49KWAUnPxYYo.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">不同反馈</p>
<p>我们将及时、持续、随机的正反馈引入到师训的设计中，通过梳理用户体验地图，在课程学习的各个节点设置不同的激励，提升学员学习的积极性。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/2BKWGGSPVDv3Z6FhBMa5.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">认证培训用户体验地图</p>
<p><strong>即时激励</strong>：对于完成课程、提交作业、互动留言给予能量值及时激励，用户能直观地感受到做这件事的快乐，形成正反馈，并加强这些行为。奖励用户的能量值可累积，用于排行榜的展示。奖励通过两种形式：大浮层和小toast。大浮层用来奖励完成课程和提交作业这两个主要行为。小toast用来奖励互动留言等社交行为。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Q06HlkX8j0FL1qPNX4qA.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">即时激励设计方案</p>
<p><strong>持续激励</strong>：整个培训围绕一个主要挑战目标展开，那就是登山看日出，同时也会设立常驻榜单来实时查看每个人的学习情况。学习地图首页展示少部分优秀学员头像，由授课讲师在后台手动配置。学习好的学员或积极主动的学员都有可能上榜。其他教师都可以看到光荣榜的成员，受到鼓舞，积极争取上榜。通过个人中心可查看排行榜，包含个人的和队伍的榜单，学员可直观地看到自己所处的位置，努力迎头赶上。排行榜前三名的头像带有装饰“1” “2” “3” 来标记学员前三名的身份，显示其尊贵性。且头像装饰会透传到互动区，强调前三名的荣誉感。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/o3ZttzYxTPci7hbXnsEh.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">持续激励设计方案</p>
<p><strong>随机激励</strong>：相比于固定的激励，随机激励更能强化用户的行为。我们在课程中间几个节点设置了随机抽奖，来缓解学员后期的懈怠和无聊感，提升教师的学习热情。在课程中插入的多个彩蛋节点可抽取奖品，奖品包括实物笔记本、虚拟兑课卡。只有当彩蛋节点前面的所有课程都已完成，用户才可以在彩蛋节点抽取奖品，以此来鼓励用户完成前面的所有课程。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/RXmj4c3C4Uuho7NERt7f.png" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">随机激励设计方案</p>
<p><strong>4.3.2 阶梯上升和社交互动</strong></p>
<p><strong>阶梯上升</strong>：我们将大目标拆解成一个个小目标，用每个地图节点承载。根据到达关卡的不同，地图前景不断丰富，直到最终太阳升起看日出，可以看到每个小目标完成后的成果。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/uc4QULqDqYaOjCF2WfWs.png" referrerpolicy="no-referrer"></p>
<p><strong>社交互动</strong>：在直播过程中加强答疑、连麦等互动形式，提升老师的参与感。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/3YJh2j15YRq76tLDf4QF.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">05 总结</h2>
<p>B端产品在合适的场景下，可以根据用户需求对产品进行情感化设计。富有情感的产品更有人情味，用户更愿意使用，也是产品的重要优势。</p>
<p>情感化可从三个层次考虑：本能层次、行为层次和反思层次。通过本能层次吸引用户注意，通过行为层次提升使用的愉悦性，通过反思层次让用户有所收获，回味无穷。设计师可以结合具体用户体验诉求和客户需求，做好每一个层次的设计。</p>
<p>最后用著名硅谷投资人 Fred Wilson 的话为结尾，世界需要更多有趣的产品。</p>
<p>“When choosing a product, humans only care about: Does it work, and is it interesting? The world already is full of things that do work, but most of them are boring.”</p>
<p><strong>参考资料：</strong></p>
<p>[1]. 田园. 教师培训有多大用？来听听156位一线教师的真心话 [EB/OL]. https://www.jiemodui.com/N/98692.html</p>
<p>[2]. [美] 唐纳德·诺曼. 情感化设计[M].</p>
<p>[3]. Jonas Kurzweg. How Emotion Design built a billion-dollar business [EB/OL]. https://medium.com/uxcam/how-emotion-design-will-build-you-a-billion-dollar-business-c79e84e9a6d8.</p>
<p>[4]. [美] 尼尔·埃亚尔, [美] 瑞安·胡佛. 上瘾[M].</p>
<p>[5]. 史玉柱. 史玉柱自述[M]. 第五章第二节, 玩家需求的八字方针.</p>
<p>[6]. Fred Wilson. Minimum Viable Personality [EB/OL]. https://avc.com/2011/09/minimum-viable-personality/</p>
<p> </p>
<p>作者：Baoling，微信公众号：BaolingUX</p>
<p>来源：https://mp.weixin.qq.com/s/BtwmZlHAdSNJpaa4jnUwNA</p>
<p>本文由 @BaolingUX 授权发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
                      
</div>
            