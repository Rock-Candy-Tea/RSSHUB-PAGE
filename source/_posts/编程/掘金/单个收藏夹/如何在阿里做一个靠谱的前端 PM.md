
---
title: '如何在阿里做一个靠谱的前端 PM'
categories: 
    - 编程
    - 掘金
    - 单个收藏夹

author: 掘金
comments: false
date: Thu, 14 May 2020 04:34:04 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2020/5/14/172132c87e184bb0?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/5/14/172132c87e184bb0?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="853" referrerpolicy="no-referrer"><br></p><div><blockquote>
<p>本文来自飞猪前端@九屻同学（也叫狗哥），深入业务侧开发多年，在项目中有深厚PM的经验，给飞猪新同学梳理了这篇《前端PM手册》,借飞猪前端团队微信公众号分享给前端的开发同学，期待可以给大伙一些阿里项目开发管控过程中的一些输入，欢迎一起交流！</p>
</blockquote>
<h1 data-id="heading-0">前端PM防diss指南</h1>
<p>从开始做飞猪前端导购业务项目至今已有一年多时间，在大大小小的需求洗礼下自认为对前端需求的掌控度尚可，但是在接到个别需求时还是会有一些不在掌控、千头万绪的感觉，会怕遗漏一些应该做的对接或者评审，也会遇到一些状况外的问题，更是会遇到“模棱两可”的选择题，尤其是我这种比较纠结类型的人，比如：</p>
<ul>
<li><div>这种类似的场景见得太多了，看一下就直接跳过吧？</div></li><li><div>需求评审时已经说清楚了，需求也不大，技术评审还要做吗，是不是可以直接拉排期了？</div></li><li><div>技术评审某个同学没参加会议，我也不直接依赖他，是不是不来也没关系？</div></li><li><div>这个功能点到预定时间了还没完成，钉钉催下进度就好了？</div></li><li><div>要发项目周报吗，好像不发也可以？</div></li><li><div>......</div></li></ul>
<p>当因为生怕遗漏而焦虑时，是否有一个可以check的“应做事项list”？当遇到状况外的问题时，是否有“指南”可以学习？当面对上面的选择题时，是否有前人的经验可以帮助决策？哪些是不变的定论，又有哪些是需要因地制宜的思考，这个准绳是什么？其实目前现有的技术PM定义里面已经包含了答案：<br>
<br>• 技术：提供技术方案,解决产品可用性、易用性问题，同时确保技术上的健壮性和系统性，对用户体验和有效的实施过程负责。<br>• PM：确保成员对Task理解清晰，边界清楚，对工期预期一致，组织推动落地，调动资源，化解风险，对交付物质量负责<br>
<br>但是“定义”，一般都是抽象的，具象到现实的导购场景上时我们该怎么做，哪里能有一个清晰的答案，哪怕是经验？<br>为了防止自己后续再陷入这些问题，根据我以往做前端PM的经验和教训，基于现有阿里业务项目总结出一份《前端PM手册》，如果你是其他业务线的小伙伴，可将自己的业务以及工具代入阅读。希望这份手册能对我和其他同学在之后的工作中有一些帮助，也希望能对其他业务线的同学有些启发，欢迎大家批评指正。<br></p>
<h2 data-id="heading-1">需求评审</h2>
<h3 data-id="heading-2">评审前的准备</h3>
<h4 data-id="heading-3">能力准备</h4>
<ul>
<li><div>熟悉对应业务，对业务有自己的体感，清晰业务范围和边界</div></li><li><div>熟练业务常用工具：比如依赖的搭建平台、业务逻辑处理的工具（圈特定的人、选择合适的商品）、模版搭建工具；算法规则配置等等</div></li><li><div>熟悉项目日常工具：需求周期管理平台、数据埋点平台、ABTest工具、玩法活动平台等等</div></li></ul>
<h4 data-id="heading-4">和PD事先沟通产品意图（一般发起评审前会PD先找主要开发者沟通）</h4>
<ul>
<li><div>对不是通用能力解决的场景，态度明确的提出意见，建议PD重新审视需求和资源</div></li><li><div>对不熟悉当前业务运营工具、实现流程的，需要科普</div></li><li><div>对不熟悉项目历史（指已有项目做更新迭代）的PD，需要科普并提供自己的见解</div></li><li><div>对重复实验性改动（既之前做过类似改动但是效果并不理想）提出意见，尤其是背景和目标无太大区别时态度要坚决</div></li><li><div>要充分倾听PD的改动背景、设计思路、产品预期，能据此提出的意图给出自己的建议或意见（技术上或者业务上），能对PD和业务有一定的输入</div></li><li><div>对PD不熟悉需要涉及资源的情况，要及时给出负责人或者范围或者方向，让PD有大致的体感</div></li></ul>
<h4 data-id="heading-5">沟通后的工作</h4>
<ul>
<li><div>仔细阅读PRD，需要对每个模块用到哪些能力有清晰的体感</div></li><li><div>需求的业务目标必须清晰合理，投入产出过低、目标模糊的需要反馈给PD重新审视</div></li><li><div>涉及到自己不熟悉的领域要及时补足信息
<ul>
<li><div>例如：这个活动页面需要用到秒杀功能，秒杀功能对应的活动玩法体系自己是否了解？</div></li><li><div>例如：本次有招商的商品进入，招商的流程、招商商品和普通商品的差异自己是否了解？</div></li></ul>
</div></li><li><div>不涵盖在自己理解的业务范围内需求，要及时和老板沟通业务范围和边界，然后反馈给PD</div></li><li><div>功能改动涉及到开发人员不清楚的话，及时咨询，防止评审时漏人</div></li><li><div>有新技术、新工具挑战，要及时做好技术储备</div></li></ul>
<h4 data-id="heading-6">需求评审邀请</h4>
<ul>
<li><div>需求评审会议邀请由PD发出，PM需要检查与会人员是否涵盖所有必要人员以及必要人员是否能准时参加</div></li><li><div>PD没有项目钉钉群的，需要拉钉钉群，由PD负责阐述需求背景等，需求PRD地址需要放入群公告</div></li><li><div>PD没有提前沟通需求的，仔细阅读PRD后如果有疑问，根据对项目的影响决定是否立刻需要找PD沟通
<ul>
<li><div>对于业务边界、资源优先级等<b>直接影响项目开展的问题</b>，需要立刻找PD沟通，需要PD理清边界、协调资源</div></li><li><div><b>部分模块</b>技术上不可行、目前工具无法承接等问题，可以在评审时抛出讨论</div></li></ul>
</div></li></ul>
<h3 data-id="heading-7">评审</h3>
<h4 data-id="heading-8">需求评审会议</h4>
<ul>
<li><div>确认必要人员全部到场</div></li><li><div>需求的业务目标必须清晰合理，有量化可追踪
<ul>
<li><div>例如：本期重点关注的指标是点击率，需要明确点击率在多久内达到多少，对比哪个时期提升多少</div></li></ul>
</div></li><li><div><b>需求评审的重点是评审需求的合理性，以各需求相关方认可为准</b>，不必在技术细节上过多讨论，此类问题可记录后在技术评审上确定
<ul>
<li><div>例如：某个商品字段能否取到这种问题，只要不是本期特别关注的字段可以先记录下来，因为有可能交互稿也只是示意图，可以在UI评审时确认，技术评审时确定</div></li></ul>
</div></li><li><div><b>需求点必须做到完全清晰，不可想当然如此，必须要各方确定方案，并且要确认方案的可行性</b></div></li><li><div>需求使用交互稿评审的，需要关注前端的交互问题，在需求评审时就抛出，防止拖慢UED进度</div></li><li><div>**有讨论后确认的模块的需求，或者特殊的模块需求，需要有文字记录  **
<ul>
<li><div>例如：秒杀模块倒计时需求，是运营填写倒计时的时间点还是读取活动的接口，倒计时结束后模块更新成什么内容，异常兜底怎么处理。这种产品、运营、技术沟通后形成的共识，一定要记录下来</div></li></ul>
</div></li><li><div><b>对于需要会后确认的点，要记录清楚问题、指定到人以及要确定在什么时间可以确认好</b>，确认好之后要有反馈（在UI评审上或者群里给到回复）</div></li><li><div>确定后续UI评审的时间，资源不确定的情况下除外</div></li></ul>
<h4 data-id="heading-9">需求评审会议结束后</h4>
<ul>
<li><div>将记录的结论、问题以会议纪要的邮件形式发出同时同步到钉钉群和PRD的评论中，要求有疑问立马反馈。对于确定到某个人的某个时间点必须给出结论的事项，一定要标注清楚问题、人和时间</div></li><li><div><b>到了确定的deadline无进度回复的，需要联系问题的负责人确定进度，并将进度周知各方</b></div></li></ul>
<h2 data-id="heading-10">UI评审</h2>
<h3 data-id="heading-11">评审前的准备</h3>
<h4 data-id="heading-12">预览设计稿</h4>
<ul>
<li><div>预览一遍设计稿，设计稿主要关注常见的问题点
<ul>
<li><div>titlebar是常态的还是异形的，目前是否支持</div></li><li><div>当前技术栈下是否与特殊排版无法实现</div></li><li><div>每个卡片字段取值来源</div></li></ul>
</div></li><li><div>模块和需求设计相差较大的，需要记录并在评审时提出</div></li></ul>
<h4 data-id="heading-13">UI评审邀请</h4>
<ul>
<li><div>需求评审会议邀请由PD或UED发出，PM需要检查与会人员是否涵盖所有必要人员以及必要人员是否能准时参加</div></li><li><div>UI稿地址需要放入项目群公告</div></li></ul>
<h3 data-id="heading-14">评审</h3>
<h4 data-id="heading-15">UI评审会议</h4>
<ul>
<li><div>确认必要人员全部到场</div></li><li><div>需求评审待确认事项同步
<ul>
<li><div>所有关于需求的待定事项必须此时完成确认</div></li></ul>
</div></li><li><div>模块和需求设计相差较大的，需要和PD、相关方沟通确认并记录</div></li><li><div>设计稿交互、排版不合理或者无法实现，或者实现成本大但是业务收效低的需要提出沟通，并将最终结果记录下来</div></li><li><div><b>UI稿的评审要精确到商品或内容的字段，尤其是牵涉到不常见字段时一定要重点关注，需要和服务端同学一起在会上沟通确定能否拿到，不确定的需要将该问题跟进的负责人和时间点记录下来</b></div></li><li><div><b>需要能掌握每个模块对应的前后端、算法等开发者是谁</b>，开发者的依赖方不在场的需要记录下来，以确保技术评审无遗漏相关方</div></li><li><div>会上除了无法确认的纯交互、排版外，其他事项需要全部确定下来，单纯的UI问题需要具体到人到什么时间确认，确认时间需要在技术评审之前，将负责人和时间点记录下来</div></li></ul>
<h4 data-id="heading-16">UI评审会议结束后</h4>
<ul>
<li><div>将记录的结论、问题以会议纪要的邮件形式发出同时同步到钉钉群和PRD的评论中，要求有疑问立马反馈。对于确定到某个人的某个时间点必须给出结论的事项，一定要标注清楚问题、人和时间</div></li><li><div><b>到了确定的deadline无进度回复的，需要联系问题的负责人确定进度，并将进度周知各方</b></div></li></ul>
<h2 data-id="heading-17">技术评审</h2>
<h3 data-id="heading-18">评审前的准备</h3>
<h4 data-id="heading-19">心理准备</h4>
<ul>
<li><div>需要到场的相关方是否都已清楚、明确</div></li><li><div><b>PM必须清楚各位开发和业务方站位</b>
<ul>
<li><div>例如：一个典型的促销活动页面，商品池是谁提供（算法还是运营），商品字段由谁来补充（服务端取值还是算法计算产出），投放的方式是怎么样的（运营配置入口还是个性化算法），生产的方式是怎么样的（算法还是运营配置），入口有哪些case，每种入口展示需要哪些字段</div></li></ul>
</div></li><li><div>需求和UI是否已经了然于胸，每个模块需要沟通的功能点是否已经心中有腹稿</div></li><li><div>前期遗留的待定事项是否都已有确切结果</div></li><li><div>哪些是重点问题，哪些是一带而过的点，要分清主次
<ul>
<li><div>常见的功能点是次，新的功能点是主</div></li><li><div>简单的模块是次，复杂的模块是主</div></li><li><div>单个开发者自给自足的模块是次，多方合作实现的模块是主</div></li></ul>
</div></li><li><div><b>技术评审的主要目的不是为了拉排期，而是为了信息互通、确定技术方案、理清各开发者边界和合作方式</b></div></li></ul>
<h4 data-id="heading-20">技术评审邀请</h4>
<ul>
<li><div>需求评审会议邀请由技术PM发出，PM需要检查与会人员是否涵盖所有必要人员以及必要人员是否能准时参加</div></li></ul>
<h3 data-id="heading-21">评审</h3>
<ul>
<li><div><b>所有开发人员&测试人员&PD必须全部到场</b>，如果需要运营配合的，运营同学也必须到场</div></li><li><div>评审参照UI视觉稿逐模块进行</div></li><li><div>每个模块的每个字段由谁提供、怎么实现要沟通清楚
<ul>
<li><div>对于某些特殊字段，需要文案记录取值逻辑，谁来实现，怎么实现都要记清楚</div></li></ul>
</div></li><li><div>对于之前未接触过的功能点，需要文案记录技术方案</div></li><li><div>对于需要多方合作完成的模块
<ul>
<li><div>需要各方对技术方案达成共识，要探讨到具体的实现流程，不能有含糊的想当然
<ul>
<li><div>例如：某个数据谁来给数据依赖方，数据从哪里来又将通过什么方式给到依赖方，是事件通知、sql还是离线表，这个数据实时性的要求如何，稳定性的要求如何</div></li></ul>
</div></li><li><div>需要清晰到每个开发者负责哪些、提供哪些、上游下游是谁</div></li></ul>
</div></li><li><div>对于各方难以抉择的边界问题，及时拉上相关方主管确认边界划分</div></li><li><div>各个模块的方案沟通清楚后，协商排期
<ul>
<li><div>一般的需求，需要后端提供功能联调的，需要确认的时间点按照时间线正序：
<ul>
<li><div>Kickoff时间</div></li><li><div>前后端数据协议约定</div></li><li><div>后端mock数据提供</div></li><li><div>后端真实数据提供</div></li><li><div>前后端联调时间</div></li><li><div>提测时间</div></li><li><div>验收时间</div></li><li><div>上线时间</div></li></ul>
</div></li><li><div>一般的搭建需求，需要确认的时间点按照时间线正序：
<ul>
<li><div>Kickoff时间</div></li><li><div>前端创建完成模块时间</div></li><li><div>运营同学商品池创建完成时间</div></li><li><div>运营同学数据投放平台配置完成事件</div></li><li><div>提测时间</div></li><li><div>验收时间</div></li><li><div>上线时间</div></li></ul>
</div></li><li><div>后端也有依赖改动的，除一般需求的必须时间点外，需要清晰到各个被依赖方能提供出数据或能力的时间点，必须要满足依赖方的开发工期</div></li></ul>
</div></li><li><div>会议结束后需要有一个明确的开发排期</div></li></ul>
<h2 data-id="heading-22">项目进度跟踪</h2>
<h3 data-id="heading-23">项目启动</h3>
<h4 data-id="heading-24">是否需要Kickoff邮件</h4>
<ul>
<li><div>除日常迭代外所有项目均需要Kickoff邮件</div></li></ul>
<h4 data-id="heading-25">Kickoff邮件内容</h4>
<ul>
<li><div>基本要素：项目背景、项目目标、项目节奏、项目成员、项目资料</div></li><li><div>明确阐述项目范围和开发内容，后续开发范围以此为准，不在该范围内的变动均算需求变更</div></li><li><div>邮件接收人为全体项目成员，抄送主要相关方（PD、运营、UED、前后端、算法、测试）主管 + 自己所在团队项目成员，重要项目需要抄送到推进此事各团队或BU负责人</div></li></ul>
<h3 data-id="heading-26">项目周报、日报</h3>
<h4 data-id="heading-27">是否需要项目周报或日报</h4>
<ul>
<li><div>原则上鼓励项目周报</div></li><li><div>重要或特殊项目（如：涉及相关方多且跨团队甚至跨BU的项目；相关方多，信息难以同步的项目），必须有日报周知</div></li><li><div>开发工期在两周内的日常迭代项目，可以没有项目周报或者日报，但需要每天要关注各个开发者的进度</div></li><li><div>开发工期在两周内的日常迭代项目，因非资源问题开发进度受阻未按时提测的，需要有项目日报周知进度</div></li><li><div>除以上类型外的项目需要有项目周报
<a href="https://juejin.cn/post/undefined"></a></div></li></ul>
<h4 data-id="heading-28">项目周报、日报内容</h4>
<ul>
<li><div>本周/日工作进度：具体到每个事项以及事项对应的负责人</div></li><li><div>总体进度：明确进度百分比，概述目前完成的功能</div></li><li><div>问题&风险
<ul>
<li><div>问题：本周/日发现未解决但已有解决方案的</div></li><li><div>风险：有可能影响项目内容或进度的事项，需要标红警示</div></li><li><div>不可控风险：基本确定影响项目内容或进度的事项，置顶标红警示</div></li></ul>
</div></li><li><div>下周/明日工作安排：具体到每个事项以及事项对应的负责人</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-29">风险&延期</h3>
<ul>
<li><div><b>发现风险一定要第一时间同步PD</b></div></li><li><div>对于不可控风险，立刻拉动PD和相关开发者会议沟通解决方案</div></li><li><div>资源投入问题
<ul>
<li><div>投入产出较低的功能点，优先考虑是否有替代方案甚至去除该功能（例如：商品卡片的某个字段取值逻辑问题，按照既定逻辑需要涉及多方改动，是否可以使用现有的其他取值代替），需要和PD、开发、测试达成一致，发送需求改动通知报</div></li><li><div>能通过补充人力来解决的
<ul>
<li><div>PM动员协调项目成员，组织加班，加班需要有加班邮件，邮件内容如日报</div></li><li><div>如果相关开发人员团队有富余人力可由开发者在团队内沟通协调</div></li><li><div>无法协调的，由PD出面协调人力资源</div></li></ul>
</div></li><li><div>不能解决的，再考虑需求是否有替代方案，需要和PD、开发、测试达成一致，发送需求改动通知</div></li><li><div>可能因一个功能延期但是该功能优先级并不高的情况，考虑需求是否可以分拆到二期进行，需要和PD、开发、测试达成一致，发送需求改动通知</div></li><li><div>以上都不可行，考虑项目延期，延期需要和PD、开发、测试达成一致，发送项目延期通知</div></li></ul>
</div></li><li><div>功能实现问题
<ul>
<li><div>投入产出较低的功能点，优先考虑是否有替代方案甚至忽略该功能，需要和PD、开发、测试达成一致，发送需求改动通知</div></li><li><div>技术上有实现方案，不过需要既定成员外同学参与实现的，PM与PD一道协调人力或由PD指定子需求，PM和相关开发同学确认技术方案可行</div></li><li><div>不能解决的，再考虑需求是否有替代方案，需要和PD、开发、测试达成一致，发送需求改动通知</div></li><li><div>无替代方案且无法实现，考虑去除该功能，需要和PD、开发、测试达成一致，发送需求改动通知</div></li></ul>
</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-30">需求改动&延期通知</h3>
<ul>
<li><div>非重大项目需求改动：钉钉群周知并且在PRD中备注，项目周/日报中体现</div></li><li><div>重大项目需求改动 或者 任何项目延期：除钉钉群周知并且在PRD中备注，项目周/日报中体现外，需要邮件周知Kickoff邮件的收件人</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-31">提测规范</h2>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-32">是否需要提测邮件</h3>
<p><b>所有项目均需有提测邮件</b><br></p>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-33">提测邮件内容</h3>
<ul>
<li><div>基本要素：功能完成度、是否完成自测、测试包（如果需要）、离线包（如果需要）、页面地址、二维码、项目资料</div></li><li><div>中间有需求变更的，需要在提测邮件中着重提醒</div></li><li><div>对测试内容有特殊要求的，需要在提测邮件中表明</div></li><li><div>对测试方法有特殊要求的，需要在提测邮件中标明测试方法文档地址</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-34">发布</h2>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-35">发布前提</h3>
<ul>
<li><div><b>必须测试通过</b></div></li><li><div><b>必须业务方验收通过</b></div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-36">发布安排</h3>
<ul>
<li><div><b>发布严格遵循当时实行的变更红线，必须做到有灰度、有监控、可回滚</b></div></li><li><div>按照各方依赖顺序发布
<ul>
<li><div>一般被依赖方先发布</div></li><li><div>如果有影响线上的改动，不兼容旧版一方后发布</div></li></ul>
</div></li><li><div>发布后要立刻组织测试和业务方进行线上验收</div></li><li><div>测试和业务方验收通过后，发布正式完成</div></li><li><div>验收发现线上问题
<ul>
<li><div>用户无感知并可快速修复：修复并发布</div></li><li><div>用户无感知但无法快速修复：和PD沟通是否走日常迭代</div></li><li><div>用户有感知并可快速修复：先回滚再修复</div></li><li><div>用户有感知但无法快速修复：参考风险&延期中的指导</div></li></ul>
</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-37">发布后要做的事情</h2>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-38">问题记录</h3>
<ul>
<li><div>养成线上问题排查过程和分析记录的良好习惯</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-39">监控&性能</h3>
<ul>
<li><div>关注监控平台各项稳定性指标</div></li><li><div>关注是否有舆情反馈</div></li><li><div>采集性能数据，有新旧版本的需要对比前后性能变化</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-40">业务数据</h3>
<ul>
<li><div>关注线上业务数据表现，业务目标在预期时间内是否达成</div></li><li><div>分析业务数据：找出表现好和不好的数据维度并分析原因</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-41">是否需要Release邮件</h3>
<ul>
<li><div>有Kickoff的项目，都需要有Release</div></li></ul>
<p><a href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-42">Release邮件内容</h3>
<ul>
<li><div>业务目标完成情况，分析业务数据阐述自己的理解
<ul>
<li><div>例如：某个模块点击率提升显著，分析是曝光降低导致还是真实的点击率提升</div></li></ul>
</div></li><li><div>线上成果展示
<ul>
<li><div>线上页面展示</div></li><li><div>改版项目，对比新旧版本页面</div></li></ul>
</div></li><li><div>技术成果总结</div></li><li><div>邮件接收人为Kickoff邮件接收人</div></li></ul>
<h2 data-id="heading-43">Last but not least</h2>
<p>以上即《前端PM防diss指南》全部内容，也是飞猪这边项目开发过程中的一个缩影，如果没有说明白的地方，欢迎评论交流，也欢迎指出不对的地方~</p>
<p><b>飞猪正在招聘前端，目前我们在 Serverless 、微前端运营工作台、端渲染、互动营销、招选投搭、智能化、体验技术、数据度量有不少建设，欢迎有能力同学进来落地技术产生业务价值，想带人同学过来直接带一个方向也是可以的，欢迎关注微信公众号来联系！</b></p>
<div></div>
<div><img alt class="lazyload" src="https://user-gold-cdn.xitu.io/2020/5/14/172132badf4ccc6b?imageView2/0/w/1280/h/960/ignore-error/1" data-width="854" data-height="255" referrerpolicy="no-referrer"></div>
<p>本文使用 <a href="https://mdnice.com/">mdnice</a> 排版</p></div><p><br></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            