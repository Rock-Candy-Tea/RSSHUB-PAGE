
---
title: '为什么一次会议的成本比一台MacBook Pro还高——减少会议中的开发人员的商业案例'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220508/3dc64cc060bfe061f6b279a4eab5a339.jpeg'
author: Dockone
comments: false
date: 2022-05-21 06:13:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220508/3dc64cc060bfe061f6b279a4eab5a339.jpeg'
---

<div>   
<br>开发人员以不屑于开会而闻名。会议迫使我们进行上下文切换，扼杀我们的工作流程，并长期削弱我们的工作满意度。然而，经理和Scrum主管似乎对会议爱不释手，由此产生的紧张关系遍布我们的日程表。Paul Graham在他的著名文章《<a href="http://www.paulgraham.com/makersschedule.html">Maker's Schedule, Manager's schedule</a>》中记录了这种现象。<br>
<br>大型组织尤其以用无意义的会议塞满开发人员的日程表而闻名——至少对开发人员来说是无意义的。而当一个Scrum主管变得无赖的时候，开发人员可能会有好几天在回顾、冲刺计划、演示和流程调整之间来回转换，而没有能够产出任何的实际价值。<br>
<br>前几周，我坐在一个特别无用的会议上，会议屏幕上全是其他开发人员——奇怪的是，这是由不同团队的技术负责人发起的。在无聊的时候，我开始想：<br>
<ul><li>我们如何为减少日程表上无意义的会议做一个商业案例？</li><li>我们怎样才能为我们参加的会议增加更多的价值？</li><li>我们怎样才能减少无意义的会议，而增加有价值的会议？</li></ul><br>
<br><h3>机会成本</h3>我之前曾经是一名会计，所以我想给一次会议的具体成本算个数。下面是我对一次会议对公司的机会成本的大致计算，不管它是否毫无意义。<br>
<br>以下是我的假设：这些是以美国为中心的，你可以根据当地的市场情况进行调整。<br>
<ul><li>会议时间为<em>1小时</em>，涉及一名项目经理和一个由<em>4名开发人员</em>组成的团队；</li><li>开发人员的平均总薪酬为20万美元，有2周的休假时间；</li><li>平均来说，一个员工要花费雇主<em>1.5倍于其报酬</em>的其他福利；</li><li>一个普通的开发人员平均每天有4-6个小时处于最大的生产状态（根据心理学的心流理论，我们也成为沉浸状态），我们使用<em>5小时</em>来计算；</li><li>根据<a href="https://en.wikipedia.org/wiki/Pareto_principle">帕累托原则</a>，每个开发人员产生的业务增值的80%来自<a href="https://zh.wikipedia.org/wiki/%E5%BF%83%E6%B5%81%E7%90%86%E8%AB%96">沉浸状态</a>，20%来自非沉浸状态；</li><li>在一个已经有太多会议的组织中，这是一个糟糕的会议安排——削减了流动状态的时间。每个开发人员在会议前后平均浪费了30分钟的时间来进行上下文切换，而这些时间是不增值的。（关于上下文切换的成本，见<a href="https://www.researchgate.net/publication/317989659_Impact_of_task_switching_and_work_interruptions_on_software_development_processes#pf2">本研究</a>）。</li></ul><br>
<br>使用这些假设，我们看到每个开发者每小时的处于沉浸状态对公司的成本是(200,000美元 * 1.5 * 0.8)/((52-2) *5 *5)=192美元/“沉浸小时”。<br>
<br>以每个开发人员2小时的“沉浸时间”为代价，4个开发人员参加这次会议，会议的开发人员的机会成本是<strong>1536美元</strong>。这个会议的机会成本高于一个全新的M1 MacBook Pro的价格。如果这个会议毫无意义，还不如取消它，让其中一个开发人员飞到巴厘岛。<br>
<br>根据我的经验，拥有最多会议的公司往往在开发设备和教育/培训费用方面也是最吝啬的——这是一个典型的聪明反被聪明误的例子。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220508/3dc64cc060bfe061f6b279a4eab5a339.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220508/3dc64cc060bfe061f6b279a4eab5a339.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
这或许是你正在可以看的景象，而不是你的PM的屏幕与他最喜欢的PPT。<br>
<h3>会议增值</h3>由于我会计的职业本能，也因为我曾经是一名自由职业者，我尽力确保我在每次会议上都能增加足够的商业价值，以证明我的存在。撇开政治不谈，仅仅是旁听一次会议其实让我感觉有点不好。我讨厌浪费我的时间。<br>
<br>会议增值有很多各种各样不同的方法，从提供实际的技术观点和专业知识到简单地保证所有人都能紧密关注会议的议程。在一个8人的开发者会议上减少15分钟的弯路，就足以证明参加会议的价值。当然，如果你在会议没有进展的时候缩短会议时间，或者建议取消会议，那就更好了。<br>
<br>从会议中获得价值的一个更好的方法，特别是对于高级开发人员和技术领导，是为团队的其他成员参加，并写一份一页的总结，让团队的其他成员在闲暇时可以阅读。<br>
<br>以上一节的会议为例。一位高级开发人员与项目管理人员一对一地解决了这个问题，并在会后花了30分钟总结所学到的关键点和做出的决定。这位高级开发人员在一个半小时的工作中增加了1500美元的商业价值——一个真正的力量倍增器。<br>
<h3>更好地开会</h3>我绝不是一个会议专家（我也不希望成为一个专家），但以下是一些对我来说很有效的会议技巧。<br>
<ul><li><strong>批次开会</strong>：在可能的情况下，把会议安排在团队每天站立会议的前后，或者选在一天即将结束，准备进行精神上休息的时候。我尽量保持每天上午11点到下午4点这段时间的自由。加分项：批次会议的最好方法是跳过它们。</li><li><strong>准备议程</strong>：这是会议的基本原则，但它常常被忽视。提前准备好会议的各种动作和预期的会议结果，这可以让你在做出决定后缩短会议时间。加分项：成为那个说“听起来我们已经完成了议程上的所有内容，我们可以结束了吗？”的人。</li><li><strong>将异步和同步分开</strong>：你不会用可以异步解决的函数阻塞JS主线程，那么为什么要阻塞一个同步会议，来讨论可以通过电子邮件提供并随时阅读的信息？加分项：有时候，把上下文写下来会把一个潜在的会议变成电子邮件或Slack投票。</li></ul><br>
<br><h3>写在最后</h3>跳过更多的会议，提出股东们并没有付给你每小时数百美元来旁边会议。如果你喜欢开会，你可以去参加MBA。<br>
<br>管理你的会议，并努力地融入你选择参加的会议。成为一个力量倍增器，你的团队会感谢你的领导。<br>
<br>如果你觉得这篇文章有帮助，请与他人分享。您可能还有兴趣了解<a href="https://blog.shimin.io/are-code-reviews-crippling-your-delivery-process-how-categorizing-your-code-review-comments-can-speed-things-up/">MR评论等级制度如何加速交付</a>或<a href="https://blog.shimin.io/afraid-your-technical-discussion-is-hurting-team-morale-heres-a-principle-to-keep-in-mind-during-technical-disagreements/">使用“意见分歧和承诺”来解决技术分歧</a>。<br>
<br><strong>原文链接：<a href="https://blog.shimin.io/the-business-case-for-fewer-developer-meetings/">Why a Meeting Costs More than a MacBook Pro – the Business Case for Fewer Developers in Meetings</a>（翻译：小灰灰）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            