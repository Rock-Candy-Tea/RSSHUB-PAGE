
---
title: '企业自研CRM系统，如何实现从0到1开发落地？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/SElzWj8bbSvRs8Lau58h.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 23 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/SElzWj8bbSvRs8Lau58h.jpg'
---

<div>   
<blockquote><p>本次直播我们邀请到了有着多年B端产品经验的@罗文老师，曾主导重构公司CRM系统，从0到1设计产品架构，推进研发并实施落地；数据系统负责经验，重构BI系统，建立数据中台，掌握数据赋能业务，曾获神策行业领军人物奖项；负责大型商超企业中经营分析平台的方案搭建，指标梳理与指标平台接入。本文为直播内容整理，内容有删改。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5452030 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/SElzWj8bbSvRs8Lau58h.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>大家好，我是罗文，之前在一家职业教育公司主导过CRM系统从0到1的产品架构设计以及推进研发的实施落地等，现在任上海一家游戏公司数据产品经理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/eo5hHAM35CNtjwuRzERt.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p>本次分享主要分三部分：第一部分是自研CRM从需求诞生到产品落地的实现流程；第二部分是基于流程和背景拆解需求，以及如何应对具体问题形成较固化的标准；第三部分是避坑指南。</p>
<h2 id="toc-1">一、自研CRM从需求诞生到产品落地实现流程</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/qu5KhTazsUoT5JpBm2fZ.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p><strong>自研CRM和SaaS型CRM的区别：</strong></p>
<p>在工作中CRM主要分自研和SaaS型两种方向，SaaS属于B端行业较流行的软件部署方式，因其成本较低便于扩张，所以在领域传播的应用较广泛，但公司开发时大多属于自研，很少采购。</p>
<p>两者共同点是行业性强，行业特性决定系统内的流程设计思路，比如零售CRM和在线教育CRM差别很大，模块和流程都是不一样的；在线教育内部也会分K12和职教，比如K12的用户群体时间较固定，具有排课功能，而职业教育因其时间无法固定，没有排课功能。</p>
<p>自研CRM的定制化程度高，解构度与工具化相对较低，更追求开发速度和高人效，即花更少时间实现更多功能；SaaS型CRM为适应行业内更多大型客户，定制化程度较低，追求通用和适配，设计时强调单功能解耦与插件化，比如把某功能设计成插件化，针对不同公司开放。</p>
<p>在自研时，可借鉴SaaS的插件化思路，提高灵活性，但需要衡量插件化开发成本小于或等于（直接开发成本+后期维护成本）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/zZWrV2EsuUzY7m8xOHmp.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<h3>需求背景</h3>
<p>自研CRM的前提背景是基于三个Boss需求，这些需求在大多数公司都会用到：</p>
<p>第一个需求是解决线索囤积问题，当线索已经囤积很多却无法循环时，老板想要提高数据利用效率，强制循环。</p>
<p>在实际业务场景主要体现在销售手里掌握成百上千个线索，但因电话打不过来，成单率较低，但依旧希望把线索掌握在自己手里养着，不会放到公海，别人也接不到。这种现象在B端获客场景很正常，因为B端客户较少，需要进行长期的关系维护，但C端老板会尽量避免该情况出现；</p>
<p>第二个需求是尽可能实现销管销控自动化，可人为干预。是指期望用预设规则提高自动化，减少人为的干预，希望像“工业化流水线”一样让线索“自动”转化，有人专门负责首购，有人专门负责复购的成单方式，各司其职，充分发挥人效；</p>
<p>第三个需求是满足团队无限扩张时，数据和利益的清晰分配。比如公司想成立上海和武汉两个分部，如何让资源不争抢且平均，必须要划分资源的自动规则，并可以根据客户情况调整结算规则。</p>
<h2 id="toc-2">二、CRM系统的结构框架拆解与落地案例难点解析</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Cr8Zc7ZFH1QZ36CuBLZN.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p>当接到需求后，首先是需求的调研落地流程，该流程属于较粗粒度，因为粗粒度才能得出规律，如果细粒度则每个公司都不一样：</p>
<p>首先是Boss提出想法，产品采集需求；当接到需求后，内部需要进行调研盘点，基于内部现状跟业务人员进行调研，主要分两层：一是领导层调研，二是基层调研；然后把调研结果的现状和老板期望，进行现状盘点和整体设计；设计完后出版方案，之后跟老板进行初步评审。</p>
<p>跟老板评审后还有业务评审工作，主要涉及两轮工作，因为老板跟业务的想法出入性肯定会很大，需要有磨合过程；在业务评审会后进行最终的产品定版，并进行公司的内部研发流程；最后是系统切换和实施环节。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0Nctgxfh0SelUV1uVkAy.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<h3>1. 需求调研和梳理</h3>
<p>上图是有关调研的两方面，一是内部调研，需要先摸清楚系统的如下属性：</p>
<ol>
<li>系统服务谁？业务特点如何？</li>
<li>系统有多少业务流程？</li>
<li>内部功能模块有多少？模块间的关系是什么？</li>
<li>功能和模块间功能相似性和矛盾点，比如相似的功能为什么不合并？矛盾的功能是否真的矛盾？</li>
</ol>
<p>在调研时还有一种极端情况，即如果遇到没有文档或相关知情人员的情况下，建议跟研发一起摸索，比如数据库表、模块等，或者与业务人员沟通，体验一天业务现场工作，比如实际操作系统的功能页面等。</p>
<p>二是当清楚内部情况后，需要对外部竞品进行调研，基于内部的上述系统属性，在市面寻找对应的产品进行调研。这里分享一个技巧，即调研时可以结合行业搜索相关竞品，比如在线教育+排课功能+CRM三个关键词，就可搜到相关竞品。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Pipcs0ObfqhcPrU8G74r.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p>在跟业务人员进行调研时需注意两点：一是在调研流程中保持中立，让被调研对象打开话匣子，防止其隐藏信息，在此基础上再根据业务属性逐个了解并详细记录；二是调研要点时要分别调研领导和基层，防止隐藏信息，也方便找到心口不一的地方，领导方主要看如何管理、带领队伍和提绩效，管理思路如何落地到产品上，基层方则是如何使用、提高操作效率和应对绩效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Zqla92UJOuQ5RlvE3WkJ.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p>大规模调研完成后，需要进行阶段性产出，该环节属于整个系统设计的地基部分，主要分为三部分：</p>
<p>第一部分是基于需求调研，产出用户故事地图，属于纯梳理调研。</p>
<p>第二部分是基于Boss想法，结合第一部分的用户故事地图，调研与产品设计结合，产出业务宏观流程图和细节流程图，可以概括为不仅仅是现状，还要加入老板期望。</p>
<p>第三部分是基于已经梳理的流程图，结合Boss需求，开始具象化，设计业务架构图。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/D2D3NPupDlDkKJdyUESd.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<h3>2. 调研产出</h3>
<p>首先是产出用户故事地图，如上图所示，用户故事地图主要分为四部分：业务阶段、子流程、具体场景和功能需求。</p>
<p>比如在整个CRM的业务组成上，第一个大环节是获取流量，主要有网站运营部、直播社群部、SEM投放部和市场部等参与到打造流量的过程中；流量打造时，每个部门都有各自的业务流程，比如网站运营部有对应的获取流量流程，该流程对应增加流量渠道和统计名片绩效等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/z3pD5dFoEUxiQsPJZdXS.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p>其次是产出业务流程图，主要分为两种，一是业务视角的流程图，二是系统视角的流程图。</p>
<p>从业务视角出发，业务有品宣和广告环节，在投放品牌广告后，会有流量线索获取环节，即线索通过在线聊天窗口、表单收集页面、短信授权页面、免费引流课等渠道进来；引流完后是商机收集环节，主要分两种：一是广告后台直接把数据传回来，二是通过自建站页面直接把数据传回来，数据传回来后，商机就进入到CRM系统。</p>
<p>然后进行线索培育，主要分为两种，一是人工强干预，比如社群和电销，先进行第一波成单；二是自然弱干预，比如促销短信、直播课和价值页面引流等，进行长期影响，如果影响不了，用户就会流失进入到下一波循环。</p>
<p>在第一波数据触达完后，会进入到成单环节，成单后是产品的交付服务，再之后是用户复购。以上每个环节都可以拆成一个单独模块或小组，进行业务上的承载，在实际产品工作中，需要先把大的业务梳理清楚，然后再去梳理小的业务。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ZMPnErLX9Nw779wzqKZ4.png" alt width="720" height="405" referrerpolicy="no-referrer"></p>
<p>从系统视角出发，在业务某个环节涉及到自建站或第三方平台等都是需要系统承载的，比如营销广告平台、投放插码平台、数据统计平台等，如果意识不到有营销广告等平台的存在，就会面临数据不知道怎么回传或需求无法实现的情况。</p>
<h3>3. 产品设计</h3>
<h2 id="toc-3">三、避坑指南：常见问题和经验总结</h2>
<p>在接下来的部分，罗文老师详细讲解了<strong>自研CRM中的产品设计环节</strong>以及根据自己的经验分享了<strong>常见问题和避坑指南。 </strong></p>
<p>囿于篇幅有限，想要观看完整视频的朋友可扫描下方二维码添加会员学习顾问@betty老师的微信，并备注“罗文”，即可获得观看链接。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wzTkbBp56k0U4oCWU1rh.png" alt width="253" height="253" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、4月直播回顾</h2>
<p>本次会员直播课程，罗文老师为大家详细讲解了企业自研CRM系统时，如何实现从0到1的开发落地，希望大家都能有所收获~</p>
<p>每周三/四晚上8点，起点课堂会员平台都会邀请一线的互联网产品、运营实战派专家，与大家分享最新的产品行业动态、运营玩法和干货知识。</p>
<p>每个月的会员直播都有月度主题，每周直播围绕月度主题展开。本月主题如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/2QwN6cm1HPRIkXudG5sd.jpg" alt width="572" height="1017" referrerpolicy="no-referrer"></p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5449620" data-author="793690" data-avatar="http://image.woshipm.com/wp-files/2019/06/uG3dh92gIrgmElEfyaWm.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            