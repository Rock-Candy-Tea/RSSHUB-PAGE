
---
title: '解锁B端工作台设计之客服系统重构'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/W1N4ijNIv7hEXK1hqGo3.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 21 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/W1N4ijNIv7hEXK1hqGo3.jpg'
---

<div>   
<blockquote><p>编辑导语：结合客服系统，企业可以提升用户服务效率与用户端的服务质量。然而在B端产品设计中，客服系统设计仍然存在标准化程度低等问题，若想解决这些问题，可以从哪些方面入手呢？本篇文章里，作者结合实际案例，对B端工作台的客服系统设计策略做了梳理，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5223077 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/W1N4ijNIv7hEXK1hqGo3.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<p>在B端产品设计中，工作台是非常重要的功能，一个好的工作台可以极大地提升用户工作效率和体验。</p>
<p>随着集团产业化如火如荼的进行，营销和服务领域也在进行重大转型升级。客服系统重构助力集团产业化进程，意在串联业务，提升客户的服务质量和应答效率。下面以客服系统（CSC）重构项目举例进行说明，如何设计系统工作台。</p>
<h2 id="toc-2">二、背景</h2>
<p>客服系统（CSC）属于综合客服体系，其核心价值在于提升企业的核心竞争力与品牌形象。服务已签约客户，进行客户售后服务、提消耗、会员续费等增值服务。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/cxHN0Ye6xObBBvEptwiX.png" alt="解锁B端工作台设计之客服系统重构" width="673" height="400" referrerpolicy="no-referrer"></p>
<p><strong>痛点：</strong>目前客服工作流自主而无序，业务动作难以标准化，目标任务完成率低，同时与业务线的结合程度有限，支持方案不足等问题严重影响客服效率和质量。</p>
<h2 id="toc-3">三、工作台说明</h2>
<p>工作台是支撑用户完成职能角色定义下的工作内容的数字系统，是业务系统中的重要模块。在客服系统中主要有两大类角色，分别是：</p>
<ul>
<li><strong>执行者（客服）</strong>：核心需求是能够高效地完成任务。</li>
<li><strong>管理者（客服主管）</strong>：核心需求是对业务情况进行把控。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/ZkR9pZ9Cmtefdhr0EMlw.png" alt="解锁B端工作台设计之客服系统重构" width="674" height="332" referrerpolicy="no-referrer"></p>
<p><strong>以执行者为</strong><strong>例</strong>，一个一线的客服人员每天需要做的事情有哪些呢？首先上班之后应该会看看今天要做哪些任务，然后按照规划开始工作，下班之前再看看任务的完成度等。可以看出客服人员一天的工作都是围绕着任务展开的。假如没有工作台，任务分散在系统各个位置与模块，会导致业务人员浪费很多时间在找任务，同时也可能会遗漏任务。</p>
<p>那么<strong>对于管理者而言</strong>呢？管理者需要掌握业务全景以及客服人员的任务完成情况，如果没有单独的数据报表和工作台，管理者只能手动搜寻数据进行统计。效率低下的同时管理也会存在滞后的情况。</p>
<p><strong>由于客服系统的核心是“任务”，理论上来说没有工作台，业务也可以正常运转，但是一个好的工作台，能极大地提升用户的工作效率和使用体验。</strong></p>
<h2 id="toc-4">四、如何设计？</h2>
<p>客服工作台是客服登入系统的第一个页面，承载着客服最关心、最紧急、最重要的事项和信息，核心作用是让客服以最快的速度看到想看的信息，处理最急需处理的事项，从而达到“增效”的目的。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/5dmmQiFfJgiUFPRix3lv.png" alt="解锁B端工作台设计之客服系统重构" width="672" height="331" referrerpolicy="no-referrer"></p>
<p>所以做好工作台的第一步就是了解用户最关心的是什么？围绕关键角色“客服”“客服主管”，整合与之对应的工作流信息，不同的角色展示不同的任务工作台信息。</p>
<h3>1. 内容获取</h3>
<p>客服工作台的内容是根据用户的实际需求来确定的。</p>
<p><strong>1）获取方法</strong></p>
<p>常用获取需求的方法有：用户访谈、调研问卷、用户反馈、竞品分析、头脑风暴等。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/gQ591bPJJx8vvEMDm57D.png" alt="解锁B端工作台设计之客服系统重构" width="675" height="350" referrerpolicy="no-referrer"></p>
<p>需求调研以定性调研为主，主要因为我们的客服系统需求具有集体性，只要调研清楚一个角色中的一两个用户的需求，就足以涵盖这个角色中用户的绝大部份需求。本次重构使用了用户访谈+用户反馈的方法进行内容需求收集。</p>
<p><strong>2）重构目标</strong></p>
<p>本次重构目标为标准化工作流，实现管理策略到目标任务的转化，提升管理过程目标完成率。为了让用户更直接，及时地了解业务情况，可以根据客服任务的实际需要，展示几个主要的关键指标、如：当月现金消耗、现金消耗完成率、客户数、客户数完成率、覆盖率、总KPI完成率等数据，这些数据可以让客服人员一目了然了解自己当前的业务完成情况。</p>
<p><strong>3）具体内容</strong></p>
<p>以一线客服为例，最终确定了业绩展示、日程管理预约、提醒、每日待办事项、常用工具等为工作台核心内容。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/SDRxW1zk6zg4ZLrT9ddm.png" alt="解锁B端工作台设计之客服系统重构" width="674" height="342" referrerpolicy="no-referrer"></p>
<h3>2. 框架结构</h3>
<p>客服工作台的设计包括导航设计和页面布局设计。</p>
<p><strong>1）导航设计</strong></p>
<p>由于本次系统重构是以标准化任务流为核心，根据调研得知客服的使用场景是多任务多页面并行，内容繁杂，所以本系统去导航设计，引入系统内多页面打开的方式，减少系统跳出频率，增加任务完成效率。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/EAUtc4bBUPvD64Sr7WR4.png" alt="解锁B端工作台设计之客服系统重构" width="671" height="91" referrerpolicy="no-referrer"></p>
<p><strong>2）页面布局设计</strong></p>
<p>主要依据信息的重要程度、进行不同程度的视觉引导，由核心目标得出以数据导向、任务流程导向为指导原则进行页面布局，划分清楚具体模块职能，提升用户浏览效率和具体操作效率。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/8klb9kK0ctpis9KaiQMp.png" alt="解锁B端工作台设计之客服系统重构" width="674" height="354" referrerpolicy="no-referrer"></p>
<h3>3. 系统拓展</h3>
<p>由于我们是多业务线多场景使用的系统，为满足多场景需求和应对未来可能遇到的问题，降低产品变动的频率和开发成本，同时考虑到团队、个体、研发效能的可持续性和可拓展性，高灵活性让系统可以面向角色和场景进行任意的组合搭配。</p>
<ul>
<li><strong>UI层面：</strong>进行整体内容结构的分拆，减少元素和模块之间的耦合性。</li>
<li><strong>代码层面：</strong>根据UI拆解的不同单元进行有序页面聚合重构，满足多角色多场景需求。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/tyZGXqvbMkAFgp1a4Pru.png" alt="解锁B端工作台设计之客服系统重构" width="675" height="251" referrerpolicy="no-referrer"></p>
<h3>4. 视觉传达</h3>
<p>视觉传达的核心是让系统和用户产生连接感，从而让系统更贴心的服务用户，连接感的两个重要来源分别为“<strong>机因”</strong>和“<strong>人因”。</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/AawfaSIcMVx5UGsmnuBj.png" alt="解锁B端工作台设计之客服系统重构" width="678" height="252" referrerpolicy="no-referrer"></p>
<p><strong>1）机因</strong></p>
<p>据统计客服人员使用的屏幕主流分辨率是1366*768、1600*900。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Ru6JOzTeutAbweXlkIFf.png" alt="解锁B端工作台设计之客服系统重构" width="672" height="259" referrerpolicy="no-referrer"></p>
<p>大部分机型分辨率为1366*768，单屏幕可视范围区域较小，同时由于我们业务本身的特殊性，需要单屏幕看到更多的内容。经过综合评估，最终选了我们组件库中最小的组件尺寸，基础文字大小从14号变成了12号，这样可以兼顾多内容展示且留有一定的阅读空间，增加整体的业务浏览效率。</p>
<p><strong>2）人因</strong></p>
<p>本次重构重点增加了情感化设计，C端产品早就将情感化纳入基础的设计体系，而B端产品的情感化设计却远未达到标准。由于大家都认为B端产品设计存在太多的客观因素影响，情感化可能不必要。那我们为什么要情感化设计呢？</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/zbyR6VhTUCaCCnIZbIRu.png" alt="解锁B端工作台设计之客服系统重构" width="674" height="271" referrerpolicy="no-referrer"></p>
<p><strong>A：补充和协调</strong></p>
<p>客服系统因其自身特征（逻辑结构复杂）集中于解决其是否可用和是否稳定的问题，而忽略了情感化部分的设计。正是因为它的产品特征与工作环境，客服系统更需要情感化设计的补充和协调。</p>
<p><strong>B：良性的情感关系建立</strong></p>
<p>心理学家表明人类具有情感诉求，当诉求得以满足后，便会产生一系列的美好情绪，而这些情绪具有改变人脑解决问题方式并帮助大脑决策的能力，而情感系统则会改变认知系统的运行过程。因此，建立良性的用户和产品关系，可以帮助用户在使用产品的过程中变得更富创造性、积极性和对产品错误的容忍性。</p>
<p><strong>C：客服需要</strong></p>
<p>客服工作本身的特点为繁杂、枯燥、重复性高、高时长、高任务量，情感化的满足可以为高强度工作增加一些调味剂，以此舒缓工作压力。增加工作愉悦性的同时提升服务效率和质量。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/5VhtCAH89Kh2w6XiTXKe.png" alt="解锁B端工作台设计之客服系统重构" width="671" height="270" referrerpolicy="no-referrer"></p>
<p>结合客服系统B端产品的基础特点“重功能、轻体验”，视觉传达层面在不影响产品功能的基础上，增加了换肤、插画运用，优化了心灵鸡汤的展现形式和内容，以此拉近客服系统与客服人员的距离。</p>
<p><strong>插画运用：</strong>为打破枯燥的工作环境，在主工作台、系统登入登出页面中加入了插画元素。</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/AqHPSvvwxUcLaznam83g.png" alt="解锁B端工作台设计之客服系统重构" width="674" height="221" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/gPqj9FY8e5Mt8lmNtVjF.png" alt="解锁B端工作台设计之客服系统重构" width="674" height="403" referrerpolicy="no-referrer"></p>
<p><strong>换肤：</strong>系统颜色的不同会给让人产生最直观的感官体验，目前系统提供换肤功能，为用户个性化定制让系统更贴心。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/eyY30FwUKh2RqlvBnMn8.gif" alt="解锁B端工作台设计之客服系统重构" width="673" height="487" referrerpolicy="no-referrer"></p>
<p>以上页面数据已做脱敏处理均为虚构数据<strong>心灵鸡汤：</strong>插画与心灵鸡汤相互结合，增加互动真实感，深度洗涤心灵哈～</p>
<p><img data-action="zoom" class=" aligncenter" title="解锁B端工作台设计之客服系统重构" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/3WiWBQPTqySNZxlbRJ0d.png" alt="解锁B端工作台设计之客服系统重构" width="671" height="91" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、总结</h2>
<p>工作台的设计整体来看无非就是围绕任务、人、场景而来，看起来比较简单，但因其服务的业务不同而发挥不同的价值，只有深入了解业务和用户的真实需求，才能让其发挥更大的价值。小小的工作台也有大大的能量～</p>
<p>以上内容结合自身工作经验，以及部分资料文章参考。如有思考不全的地方，欢迎评论区进行交流学习。</p>
<p> </p>
<p>作者：刘静颐；微信公众号：58UXD</p>
<p>本文来源于人人都是产品经理合作媒体@58用户体验设计中心</p>
<p>题图来自Pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5223054" data-author="237551" data-avatar="http://image.woshipm.com/wp-files/2017/05/xh21CT01uRslo5Qe600c.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            