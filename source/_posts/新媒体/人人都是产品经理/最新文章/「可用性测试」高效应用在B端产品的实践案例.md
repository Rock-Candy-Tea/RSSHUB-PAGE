
---
title: '「可用性测试」高效应用在B端产品的实践案例'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/06/xHJeZB3ZIRhBHlXE1WRL.png'
author: 人人都是产品经理
comments: false
date: Wed, 22 Jun 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/06/xHJeZB3ZIRhBHlXE1WRL.png'
---

<div>   
<blockquote><p>编辑导语：在做B端产品时，是否经常会遇到一些困扰，和技术部门、客服等等所持的意见不一致，无法从根本上解决问题。本文作者就分享了在可用性测试的应用实践经验，一起来看看吧，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-827096 aligncenter" src="https://image.yunyingpai.com/wp/2022/06/xHJeZB3ZIRhBHlXE1WRL.png" alt referrerpolicy="no-referrer"></p>
<p>在产品设计和研发过程中，你会不会时常遇到以下困扰：</p>
<ul>
<li>产品新功能上线后，收集到的用户反馈意见不一致，比如“有人觉的直接展开操作更方便，有人觉得滑动操作更好用”，“有人觉得页面蓝色风格不好看”，“排版设计吐槽不好看，信息太密集，抓不到重点”…</li>
<li>在设计方案的过程中，针对某个功能有多个设计方案，无法判断哪个方案更优；</li>
<li>产品已经开发完成，想在上线面客前检验下是否满足用户的使用需求？满意度如何？</li>
</ul>
<p>业务和客服人员往往需要花费大量的时间和精力去收集、处理用户的投诉反馈。但是因为面对用户的投诉或者反馈建议五花八门，都有各自的立场，无法明确分析出问题在哪里。</p>
<p>面对这类问题，技术部门通常都是通过版本回退等方式临时解决用户的投诉反馈，无法从根本上有效的解决用户的问题。</p>
<p>那么有没有其他更科学高效的解决问题的方法呢？</p>
<p>这里为大家分享一下我们在可用性测试的使用上的一些实践经验，把我们在B端产品上面对这些场景的时候做的一些工作分享给你，期望能给你带来一些直接的帮助。</p>
<p><strong>目录：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/132a2uRRJ8TH5uVRteTz.png" alt width="1842" height="747" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、可用性测试基本概念</h2>
<p>我们先看看国外体验设计专家Jeffrey Rubin和Dana Chisnell在《Handbook of Usability Testing》书中关于<strong>可用性测试（Usability testing）</strong>的定义：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/kB1w8TZLOEmCSnLEcDBJ.png" alt width="1842" height="660" referrerpolicy="no-referrer"></p>
<p>说明：典型用户即是指真正使⽤产品的⽤户、潜在⽤户或者意向⽤户等。产品设计开发出来是给典型用户使用的，只有通过典型用户的可用性测试收集到的数据和信息才是有意义的。</p>
<p>在ISO 9241-11:2018针对可用性的概念是指：</p>
<p><strong>“特定的用户在特定的使用场景下，为了达到特定的目的而使用某些产品时，所感受到的有效性、效率及满意度。”</strong>因此可用性测试也是通过测试来找出产品在有效性、效率性以及满意度三方面存在的问题，并针对性进行改善，以此来提高产品的体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/FJUuAUwzW7snYcvtTq5v.png" alt width="1842" height="993" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、可用性测试的价值</h2>
<p>可用性测试是改善产品的比较科学有效的方法之一。</p>
<p>有时，我们并不是产品的目标用户，很多需求和设计方案是产品及设计人员自己想出来的。虽然我们在设计时会依据一些经验与设计法则，但这些都只是未经验证的主观猜测，无法准确的评估设计方案的优劣。</p>
<p>所以为了真正的了解用户，我们需要找到我们的目标用户并向他们学习，这样才能使产品各关联方尽快对设计方案达成一致并积极改善产品体验。</p>
<p>可用性测试的价值可以概括为以下几方面：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/peS9D8zgq9Y2FD9DF2MK.png" alt width="1842" height="1230" referrerpolicy="no-referrer"></p>
<p>通过可用性测试，我们最终要达到的目的：<strong>提升产品用户体验和满意度，助力业务目标达成</strong>。</p>
<h2 id="toc-3">三、可用性测试的类型</h2>
<h3>1. 可用性测试适用场景</h3>
<p>可用性测试可以在产品的任何阶段进行，不同场景下可用性测试的侧重点不同。我们一般在产品上线前侧重方案验证；在上线后侧重找出问题，进行迭代优化；同时也会日常定期开展可用性测试，针对重点或者高频功能进行体验跟踪，持续优化体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/kuF6kfzDHtOxXKVqkTUW.png" alt width="1842" height="858" referrerpolicy="no-referrer"></p>
<h3>2. 可用性测试分类</h3>
<p>可用性测试的类型主要分为分析法（偏定性）和实验法（偏定量），区别在于是否有用户参与。以下为两种测试类型主要对比：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/zQMHllAtpAQ2jr6BzbBX.png" alt width="1842" height="999" referrerpolicy="no-referrer"></p>
<p>从某种程度而言，分析法和实验法是一种互补的关系，不同的测试方法适用的场景不一样，需要根据<strong>测试目标、问题场景、产品所处的阶段、经费预算、时间周期</strong>等因素选择适合的测试方法，以最优的方式来达成可用性测试的目标。</p>
<p>接下来我们通过一个过往的案例，来跟你分享一下我们是怎样结合目标来选择测试方法的。</p>
<p><strong>1）案例场景</strong></p>
<p>某产品有两个入口，分别为产品列表的入口和首页banner入口。 我们通过用户点击数据发现首页banner点击率比较低，多数用户还是通过产品列表的入口进入。我们希望分析找出banner入口点击率较低的原因，提升banner入口的点击率。</p>
<p><strong>2）原因分析</strong></p>
<p>从产品、设计及体验角度分析：banner样式、是否有动效、banner的大小、banner的位置、banner显示的文案等因素都会影响到最终的点击率。</p>
<p><strong>3）可用性测试方法策略</strong></p>
<ol>
<li>先用专家评审、启发式评估的方式分析了现有的问题，针对问题输出2个不同的方案；</li>
<li>采用A/B Test的方式，在小范围内对2个方案进小范围线上投放，结合投放数据选出转化率最高的banner正式上线。</li>
</ol>
<h2 id="toc-4">四、如何组织一场更有效的可用性测试</h2>
<p>结合我们的实践经验，我们把可用性测试分成7个阶段：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/k3Cntp6I3Gz2azK7c05O.png" alt width="1842" height="1587" referrerpolicy="no-referrer"></p>
<p>接下来我们会结合在小企业融资贷款产品领域的可用性测试实践，来具体分享如何组织一场可用性测试。</p>
<p><strong>背景说明：</strong>面向中小微企业的融资贷款产品，针对企业主和企业用户提供贷款资金进行经营周转。申请人可以通过线上进行贷款申请、合同签署、提款、还款等操作。</p>
<p><strong>业务诉求：</strong>由于历史原因，现有的功能框架陈旧，日常客户贷款申请及使用过程中反馈的问题较多；同时客户申请转化率不高，申请环节流失率较高。业务部门希望了解产品功能和流程中存在哪些体验问题？如何提高客户申请转化率，实现业务增长？</p>
<p>基于以上背景，我们决定针对小企业融资贷款产品进行一次可用性测试，帮助业务解决遇到的问题。</p>
<h3>1. 需求收集</h3>
<p>可用性测试通常是由设计师发起的，但是需求并非仅来源于设计师，可以是用户、业务、产品、技术等角色的反馈。比如用户反馈的问题、异常数据、阶段性的业务目标、版本迭代优化、常规的用户行为数据监测、创新产品方案设计等都可以作为可用性测试的需求来源。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Blil9GcnVZ0vfETbRUFF.png" alt width="1845" height="867" referrerpolicy="no-referrer"></p>
<p>我们通过建立可用性测试需求清单，统一收集各方提出的可用性测试需求，然后对需求进行统一合并、筛选、确认优先级等，纳入到可用性测试计划排期，然后协同各方一起推动可用性测试计划的执行。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/kYucrysFrkmjhoOim32X.png" alt width="1842" height="630" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：可用性测试需求收集清单模板</p>
<h3>2. 编写测试方案</h3>
<p>在收到可用性测试需求后，我们需要根据需求制定可用性测试方案。一份完整的可用性测试方案由以下几块组成：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/0Qp7LwmqLNjN9nZE5mNi.png" alt width="1842" height="1320" referrerpolicy="no-referrer"></p>
<p>以下为针对小企业融资贷款产品可用性编写的测试方案示例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/7ieuMQyUtJHjJvOISn5x.png" alt width="994" height="611" referrerpolicy="no-referrer"></p>
<p><strong>1）明确测试目的和范围</strong></p>
<p>在测试前，需要与需求提出方进行沟通，确定需要测试的产品是什么，想要验证什么样的结论或者达到怎样的预期，是为了发现产品或原型中可用性的问题，还是借此与竞品进行有效性、效率、满意度的比较，或是对某些功能点进行测试等。明确本次测试的产品及范围，以便后续测试工作的高效进行。</p>
<p><strong>2）确定测试任务</strong></p>
<p>可用性测试任务是指导测试进行的操作指引，我们通常会根据测试的需求和目标，把任务进行场景化设定，以任务脚本的形式引导用户进行测试。测试任务脚本内容包括：<strong>开场引导、任务设定、满意度评估、结束后访谈等</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/gHFcN1ZnQ6Ca4XrCHWF3.png" alt width="1842" height="798" referrerpolicy="no-referrer"></p>
<p>可用性测试一般情况下需要多人协同配合进行，由于涉及内容较多，对被测用户进行的活动任务也比较复杂且环环相扣，所以为了保障测试任务更好的实施，一般情况下会准备一份较为完整的测试脚本以供测试人员更好的配合。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/IeqzTWx2l9ZqAPs3upj4.png" alt width="603" height="364" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：xxx贷款产品可用性测试脚本模板</p>
<p><strong>① 开场引导</strong></p>
<p>向被测者介绍测试的目的，需要注意的事项等，测试前也可以做一个聊天式的沟通，了解用户对产品的使用情况，帮助用户将注意力转移到产品上，为测试做铺垫。</p>
<p><strong>② 任务设定</strong></p>
<p>设计测试任务就是“谁在什么情况下要做什么事”，紧抓“人”、“场景”、“目标”三个要素。任务设计的几条核心原则：</p>
<p>a) 根据测试目的列出任务清单，<strong>任务不宜过多</strong>，必须是<strong>紧贴核心测试任务</strong>的。</p>
<p>比如针对贷款产品，用户的核心任务就是申请、签约、提款和还款。因此我们的任务设定就需要围绕这几个主流程进行。</p>
<p>b) 将任务<strong>赋予真实场景</strong>，毕竟用户使用产品都是有真实场景的。</p>
<p>比如贷款产品申请，模拟用户在资金链紧张的场景下，如何找到并完成贷款产品的申请流程。</p>
<p>c) 明确测试任务<strong>起点和终点</strong>，判断用户是否完成了任务的主要依据就是，用户是否从起点（页面A）到达了终点（页面B）。起点未必一定要是首页，起点位置应根据具体场景来确定，毕竟并不是每个任务都是从首页开始的。</p>
<p>比如贷款申请，任务的起点是贷款产品的申请入口，任务的终点是完成贷款申请提交。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/SksMOwIy4eYKUMlvekBX.png" alt width="1046" height="373" referrerpolicy="no-referrer"></p>
<p><strong>③ 满意度评估</strong></p>
<p>在每一次任务完成后，可以让用户对任务进行评分，注意评分要有相同的维度，否则无法进行统计。比如可以从<strong>产品功能的满意度、操作的便捷性满意度</strong>进行评分，评分可以采取5分制。最后计算平均值得出每个任务的平均满意度分值。所有的任务平均分值再计算平均得出整个产品的综合满意度评分。</p>
<p>评估量表可以考虑比如SUS量表、ASQ量表等。具体选择哪种量表需要根据测试的场景、目标等选择合适的即可。以下为关于SUS量表的基本介绍信息：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/MV2rCC6qt9UglG397WpE.png" alt width="1338" height="514" referrerpolicy="no-referrer"></p>
<p>以下为我们在某次可用性测试用使用的SUS量表示例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/2nJMzioiLLfWeV24tJ3L.png" alt width="470" height="684" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：针对某款贷款产品可用性测试SUS评估量表模板</p>
<p><strong>④ 结束后访谈</strong></p>
<p>在完成测试任务后，可以对用户进行访谈，访谈目的是收集用户对产品的其他反馈意见，同时也可以对测试记录过程中有遗漏的地方进行回顾确认。</p>
<p><strong>3）明确用户招募</strong></p>
<p>我们需要根据测试选用的具体的可用性测试方法，在方案中明确用户招募的内容。一般用户招募需要从以下几方面进行考虑：</p>
<p><strong>① 招募的类型</strong></p>
<p>通常招募的用户类型分为：小白用户、专家用户。在招募时为了结果数据真实可靠，应避免该产品相关人员的参与。通常优先选择有代表性的用户，其中真实的产品目标用户为最佳。</p>
<p><strong>② 招募的来源</strong></p>
<p>招募的来源一般分为内部招募和外部招募。我们需要根据实际情况进行选择招募的渠道，以便在招募阶段按照确定的招募渠道来进行用户招募。</p>
<p><strong>③ 招募的数量</strong></p>
<p>测试者不宜过多，一般5名左右就够了。</p>
<p>根据尼尔森博士相关理论：有5个人参加的用户测试，就可以发现85%左右的产品可用性问题。因此招募的用户数量不是越多越好。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Dw3SMNI61b8ARpfpeO9l.jpg" alt width="699" height="417" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：尼尔森用户招募与问题关系图</p>
<p><strong>4）确定测试的关联资源</strong></p>
<p>可用性测试通常都是线下进行的，就需要提前准备相关的资源等，以便测试执行阶段正常开展测试。一般需要确定的关联资源包括：<strong>场地安排、测试设备、测试环境数据（软件安装包/版本等）、辅助测试人员、测试结束后赠送的礼物（如有）等</strong>。</p>
<p>在测试方案里我们需要根据不同的事项进行分工，根据不同的资源准备事项落实到对应的责任人，以便更好的完成测试的准备工作和进度跟踪。</p>
<p><strong>5）确定各节点时间排期</strong></p>
<p>在制定可用性测试方案的时候，很重要的一点就是我们需要根据整体的测试时间安排，确定各阶段节点的具体时间排期，需要在节点时间内完成该任务事项。同时与各关联方达成一致后，大家都按照这个时间排期计划往前推进。同时在临近时间节点的时候，需要提前确认该任务事项完成进度情况，做到整体进度可控。</p>
<p>同时需要考虑突发情况下，可能存在事项延期或者未能如期完成的情况。如果出现意外情况的时候，我们的对策是什么等等。</p>
<h3>3. 用户招募</h3>
<p>在确定可用性测试方案后，我们就要开始进行招募用户了。</p>
<p>用户招募的关键之处在于所招募的用户要具有代表性，可以根据产品后台的使用数据，了解用户的群体特征是怎样的，比如性别、年龄、婚姻状况、职业、居住条件等等特征分布，通过这些条件筛选，有助于更好的招募到典型的目标用户。</p>
<p>结合小企业融资贷款产品可用性测试，在招募用户的时候，我们通过后台大数据分析平台，了解小企业贷款用户的群体特征是怎样的，比如申请身份、职业角色、性别比例、年龄分布等，为招募用户提供基础参考数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/jaIv7gEZi2yfjjtGqLXx.png" alt width="1842" height="828" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：xxx贷款产品可用性测试用户招募</p>
<h3>4. 测试物料准备</h3>
<p>测试物料是在正式测试之前需要提前准备的事项，需要在执行测试前进一步明确清楚是否已准备妥当。一般需要准备的测试物料内容包括：<strong>场地安排、测试设备、测试环境数据、安排工作人员、明确用户排期、发送测试邀请函及测试结束后赠送的礼物（如有）等</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/ozSQNUqrarkNpvytwbwu.png" alt width="1842" height="1458" referrerpolicy="no-referrer"></p>
<h3>5. 测试执行阶段</h3>
<p>在正式测试执行阶段，主要分为以下流程环节：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/20WaOxTeMZUbhtXT2TIr.png" alt width="1842" height="1134" referrerpolicy="no-referrer"></p>
<p>测试执行是整个可用性测试的关键环节，操作执行的好坏直接影响到整个可用性测试的结果。我们需要按照之前的测试方案中的测试任务脚本，引导用户按照脚本执行测试任务， 同时在测试中要随时观察记录用户的操作遇到的问题以及用户的情绪表现等。在每次任务结束后及时进行任务满意度评分。评分过程保持客观独立评价，不要干扰用户评分。</p>
<p>如果测试用户遇到测试相关的问题，不要直接告诉用户应该怎么做。为了保证测试顺利的执行，我们需要注意以下几点：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/5HlFfe49MycbSd3R7MOF.png" alt width="1684" height="382" referrerpolicy="no-referrer"></p>
<h3>6. 测试结果整理分析</h3>
<p><strong>1）原始数据的整理记录</strong></p>
<p>测试完成后需要尽快针对原始数据进行整理，数据和问题的整理应尽可能详细，方便后续核对和查阅。针对可用性测试，一般需要整理的材料包括：测试观察问题记录表、任务完成效率统计表、任务完成有效性统计表、测试问题截图或者录屏文件整理。通过原始数据和材料的整理记录，可以确保结果分析的数据的真实性和准确性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/d913d2VDP75qGGLYUxeU.png" alt width="1916" height="626" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：单个任务完成效率的统计</p>
<p><strong>2）测试问题汇总整理</strong></p>
<p>针对记录的问题，需要详细记录问题。一般会提前制定一份可用性测试问题记录表，记录表需要明确记录问题出现的模块、功能页面、版本、手机类型、问题描述、问题截图、用户情绪反馈、测试记录人、记录日期等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/pdhfoIeQ1QKxCWVgD3ke.png" alt width="479" height="591" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：测试问题汇总统计表</p>
<p><strong>3）数据分析整理</strong></p>
<p>结果分析整理可以从定量和定性结果两方面进行，定量的结果可以分析任务的完成情况、任务的满意度等，并借助可视化的图表进行展现，比如：</p>
<p><strong>① 统计任务的满意度评分情况</strong></p>
<p>我们会统计并计算单个任务的满意度评分，并与总均值进行比较，对于评分比较低的任务功能则需要引起注意。后续需要重点分析满意度低的问题在哪里。</p>
<p>比如小企业融资贷款产品完成情况整理结果如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/NtZ5AeWlAKjJnhqf44pf.png" alt width="559" height="225" referrerpolicy="no-referrer"></p>
<p><strong>② 统计任务的完成情况</strong></p>
<p>任务完成一般可以分为完成、求助后完成、未完成三种情况，不同的完成情况用不同的色块表示，然后统计完成率情况。</p>
<p>比如小企业融资贷款产品完成情况整理结果如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/HKuTGlROB2iqOkZxGMhk.png" alt width="772" height="215" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：单个任务完成情况的统计</p>
<p><strong>③ 定性结果的整理</strong></p>
<p>根据记录的用户测试中的问题，分析具体的问题类型，划分为不同的类型进行统计，可以进行概括总结，归纳问题点集中表现在哪些方面，比如功能问题、性能问题、交互问题、视觉问题等，通过问题类型分布图可以清晰明确的看出问题集中在哪几个维度。</p>
<p>比如小企业融资贷款产品问题类型分布图如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/vafTcATunOu9sSPDI4V4.png" alt width="347" height="331" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图例：问题类型分布雷达图</p>
<h3>7. 测试分析报告编写</h3>
<p>在完成测试结果整理分析后，就可以开始分析报告的编写。报告内容一般分为以下几块：</p>
<p><strong>测试结果汇总、任务方案概览、测试问题分析、竞品分析、优化解决方案及后续的优化计划</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/nyWqvQOzqKzenDwrznYn.png" alt width="1842" height="1134" referrerpolicy="no-referrer"></p>
<p>可用性测试分析报告作为总结性的材料，不仅仅是对可用性测试过程的复盘，同时也是对各关联方具有重要的价值。体现在以下三方面：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/OaqWgNeyFQBdAnwLzggp.png" alt width="1842" height="852" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、如何驱动用户体验提升</h2>
<p>可用性测试可以帮助我们发现产品中存在的体验问题，在完成可用性测试报告后，并不意味着工作的结束。我们需要将可用性测试发现的问题、解决方案等与各相关方进行沟通，推动问题与优化方案纳入版本迭代优化，做好优化效果的验证及追踪。不断持续的通过可用性测试，打磨优化产品的用户体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Uu3I6VXrmFRkXwDAAd0j.png" alt width="1842" height="1134" referrerpolicy="no-referrer"></p>
<p>以上就是我们在B端产品可用性测试的实践经验。不同的产品使用的可用性测试的方法是和我们的服务的产品和具体的测试的需求是有较强关联的，不同的测试需求需要考虑测试的目标场景和是否有限定因素等，不能简单直接复用。大家可以根据具体的情况使用可用性测试这套工具和方法。</p>
<p>我们的可用性测试大多情况下都是线下进行的，希望大家能为自己争取机会，多尝试和用户沟通，你会发现很多之前想不到的问题，你对用户的行为习惯了解越多，设计的时候就越能避免产生体验的问题。这样才能有助于提升产品的用户体验，更好的帮助业务达成目标。</p>
<p> </p>
<p>作者：WOWdesign，研究设计价值最大化，涉及用户体验、品牌体验、空间体验。</p>
<p>本文由 @WOWdesign 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5495587" data-author="90253" data-avatar="http://image.woshipm.com/wp-files/2020/11/P6rhcSTeLPnz96Jt9FXH.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            