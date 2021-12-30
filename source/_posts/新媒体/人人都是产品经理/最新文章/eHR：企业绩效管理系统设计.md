
---
title: 'eHR：企业绩效管理系统设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/R8WFgP3xXqu0PL6AwSqt.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 30 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/R8WFgP3xXqu0PL6AwSqt.jpg'
---

<div>   
<blockquote><p>编辑导语：作为eHR的核心模块之一，绩效管理系统的重要性可谓不言而喻。而企业利用绩效管理系统，可以更好地进行员工管理，推动后续业务发展。那么，你知道如何进行绩效管理系统设计吗？本文作者做了相应总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5270840 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/R8WFgP3xXqu0PL6AwSqt.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>eHR系统包含核心人力、人员管理、薪酬管理、绩效管理、招聘管理、培训管理等模块，而绩效管理系统是eHR的核心模块之一，接下来我们将探讨如何搭建企业绩效管理系统。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/NRPzAy4k9yRj8cBRfSlD.png" alt="eHR-绩效管理系统" width="669" height="460" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">绩效系统业务架构图</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/PX33oL4ul0jEPNuxIpZx.png" alt="eHR-绩效管理系统" width="672" height="449" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">绩效系统产品架构图</p>
<h2 id="toc-1">一、什么是绩效管理</h2>
<p>所谓绩效管理，是指各级管理者和员工为了达到组织目标，共同参与的绩效计划制定、绩效辅导沟通、绩效考核评价、绩效结果应用、绩效目标提升的持续循环过程。</p>
<p>绩效管理的目的是持续提升个人、部门和组织的绩效。绩效管理系统（Performance Management System）就是管理组织和员工绩效的系统。系统就如同为企业的各种管理系统搭建了一个管理平台。</p>
<h2 id="toc-2">二、绩效管理方法</h2>
<p>绩效管理的方法有很多种，常用的管理模型有MBO、KPI、OKR、360、BSC等。这些方法各有特点，企业需要根据自身的发展阶段和管理需要，选择最适合的绩效管理工具，因此要求绩效管理系统具备多种管理工具的能力。</p>
<h3>1. MBO</h3>
<p>目标管理（management by objective，MBO）最早是由管理大师彼得·德鲁克（PeterF．Drucker）提出的。当组织目标确定后，各级管理者必须将其有效分解，转变成每个部门和岗位的子目标。目标管理强调的是通过目标任务来管理组织，要求目标必须清晰可分解，特点组要有四个：</p>
<ol>
<li>具备明确的目标（SMART原则）</li>
<li>各层级参与决策（上下共同参与）</li>
<li>规定出具体时限</li>
<li>反馈目标的结果</li>
</ol>
<h3>2. KPI</h3>
<p>关键绩效指标（key performance indicator，KPI），通常用来衡量不同部门或者岗位人员绩效表现的量化指标，是组织实现战略目标需要关键要素的量化和提取。重点在于对关键要素的抽样、量化、计算。</p>
<h3>3. OKR</h3>
<p>目标与关键成果法（objectives and key results，OKR），创始人是英特尔公司前CEO安迪·格鲁夫。</p>
<p>其特点主要有两个，一是每个岗位有明确的重心工作，而不是大量KPI。二是强调绩效的透明与沟通，避免过程偏移方向。</p>
<p>OKR在互联网企业应用广泛，能更好地适应企业快速变化的业务需求。相对于KPI绩效管理模式，OKR的指标一般比KPI少，最大的区别是，KPI指标通常是从企业战略顶层出发，自上而下制定任务指标，而OKR则是自下而上或者同时开始制定。</p>
<h3>4. 360</h3>
<p>360度评估（360°feedback），最早也是由英特尔公司提出并实施的。它是将员工的直接上级、直接下级、关联方、顾客以及员工本人全方位对自己的绩效进行评估。</p>
<p>使用多方参与的形式，360度评估的优点是更加强调对内、外部客户的服务，提升组织的运行效率。对员工的能力素质进行更全面的考核，使员工的参与感更强，能够提高考核的全面性和公正性。缺点是考核的成本较高；若管理不善，打分容易流于形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/nA10r2r0o6So3fgCcJhQ.png" alt="eHR-绩效管理系统" width="674" height="465" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">360绩效评估方法</p>
<h3>5. BSC</h3>
<p>平衡计分卡（the balanced scorecards，BSC），是由美国哈佛商学院的教授罗伯特·卡普兰和诺朗诺顿研究所所长、美国复兴全球战略集团创始人兼总裁戴维·诺顿共同创建的。</p>
<p>BSC共有四个指标，分别是<strong>财务、客户、内部经营过程、学习与成长</strong>。</p>
<p>平衡计分卡多数用于组织目标或管理层的绩效管理中，相比于其他绩效管理的特点是可以充分调动员工的积极性，把员工的工作与部门的目标联系起来。员工需要用企业的视角来审视自身的工作成果，把员工的被动变为主动，让员工能够充分参与进来。</p>
<h2 id="toc-3">三、绩效管理的业务流程</h2>
<p>确定了企业的绩效管理方法后，如何使管理方法发挥管理效能，还需要有效的绩效管理业务流程。通常绩效管理流程分为4个步骤，分别是<strong>绩效计划、跟踪辅导、绩效考核、结果应用</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/0NR63NJApydLGuuq02EP.png" alt="eHR-绩效管理系统" width="559" height="583" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">绩效管理流程</p>
<p><strong>绩效计划</strong>，是各级根据公司目标，确定自身工作计划，并不断地上下交流沟通、争取达成一致、形成最终计划方案的过程。</p>
<p><strong>绩效辅导</strong>，是在一定的考核周期内，对目标进行回测、跟踪，对目标的完成情况进行分析，并制定改善方案或修订目标的动作。</p>
<p><strong>绩效考核</strong>，是在考核周期内，对目标的完成情况进行考核评估，企业还会根据员工考核情况进行等级排名以及考核反馈工作。</p>
<p><strong>结果应用</strong>，是根据考核结果，进行相应的奖惩，比如调薪调级，生成绩效画像等。</p>
<h2 id="toc-4">四、培训管理的业务架构图</h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/R7AlJPylPAin6Mq75Xla.png" alt="eHR-绩效管理系统" width="633" height="437" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、绩效管理的业务场景</h2>
<p>以某大型集团企业为例，其绩效管理工作会贯穿全年，并分成计划、追踪、总结、应用四个阶段工作，需要全集团人员参与。</p>
<h3>1. 计划阶段</h3>
<p>年初集团战略企划部门确认各个子公司、部门的年度目标，并下达到各层级组织。在组织层面，集团自上而下地制定了各个层级的年度KPI。在员工层面，由COE发起绩效计划制定工作，从总经理到基层员工，逐级完成KPI的任务分解。</p>
<h3>2. 追踪阶段</h3>
<p>企业员工每月进行月度汇报，各层级的直线领导对员工的工作进展进行评分，形成月度追踪报告。根据实际情况对下属工作进行辅导，提升其工作能力，及时调整员工的目标计划，适应市场变化。</p>
<p>总结阶段年底由人力部门发起全集团的绩效总结工作，并根据每月绩效评分，及最终达成情况，计算得到年底总结分数，由各个部门负责人进行排名总结，完成本年度总结工作。</p>
<h3>3. 应用阶段</h3>
<p>每年绩效排名前5%的员工，按绩效管理规定，发起涨薪流程，连续2年排名前5%的员工，可发起晋升流程。</p>
<p>上述企业的绩效管理工作贯穿全年，参与的角色有公司管理层、绩效HR、直线领导、员工，还有企划部门管理员。企业需要通过绩效管理系统，有效提升管理效能，从而提高企业竞争力。</p>
<h2 id="toc-6">六、绩效管理的系统关系</h2>
<p>绩效管理是企业管理工作的重中之重，对上要承接企业战略目标，对下需要管理和提升员工能力，因此许多企业都会将绩效管理放在核心位置。</p>
<p>从上述例子可以看出，绩效系统不仅跟e-HR系统内的模块关联，还与外部经营管理系统产生关联，其中包括：</p>
<ul>
<li>核心人力系统</li>
<li>培训管理系统</li>
<li>员工画像系统</li>
<li>薪酬管理系统</li>
<li>招聘管理系统</li>
<li>员工服务系统</li>
<li>经营管理系统</li>
</ul>
<p>核心人力系统为绩效管理系统提供人员架构和岗位等底层人力数据。培训管理系统、员工画像系统、招聘管理系统都是依据员工绩效数据来开展业务，比如绩效优秀者调薪，绩效较差的员工开展专项培训等业务场景。一些大型企业会接入企业经营管理系统，将经营数据直接关联绩效指标，自动计算绩效等级。</p>
<h2 id="toc-7">七、绩效管理系统产品架构图</h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/CX6lizGfqPapMVWcm3or.png" alt="eHR-绩效管理系统" width="645" height="453" referrerpolicy="no-referrer"></p>
<p>绩效产品的应用模块，主要是根据业务流程分成4个功能模块：</p>
<ol>
<li>绩效计划模块</li>
<li>过程辅导模块</li>
<li>考核评估模块</li>
<li>结果应用模块</li>
</ol>
<h3>1. 绩效计划模块</h3>
<p>从功能上可以分成计划的制定、计划审批、计划参考功能，单从系统角度来看功能并不复杂，<strong>如何提升系统的业务价值，支撑企业的战略计划，成为这个模块产品设计的难点</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/8JR1j3kBGffy5zPsbQOj.png" alt="eHR-绩效管理系统" width="642" height="500" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">企业的战略分解</p>
<p>企业由战略部门制定企业战略目标，各级员工再根据战略目标制定个人计划。一些企业则使用经营管理系统建立量化的KPI指标，通过人力系统将KPI目标导入到个人绩效中。</p>
<p>此时应该考虑如何处理企业的战略计划和个人计划之间的关系？实际在项目上的处理方式是将企业战略目标作为一个数据表，将个人绩效作为另外一个数据表，两者建立承接关系。下图左侧是组织绩效，右侧是个人绩效，通过绩效系统建立关联，并不断向下一层级分解。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/0Vhkag5y4nRfzHpSptgA.png" alt="eHR-绩效管理系统" width="652" height="381" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">组织绩效与个人绩效的关系</p>
<p>但事实上很多公司的组织绩效与个人绩效是分离的，管人和管事并不在一个系统里。其实e-HR系统远不止简单地管理“人”，<strong>通过接入经营数据为企业管理者提供“人”、“业”一体的管理能力，解决经营系统与人力资源系统的信息孤岛问题，真正帮助企业通过战略计划驱动业务发展</strong>。</p>
<h3>2. 过程辅导模块</h3>
<p>该功能模块主要满足绩效过程追踪及辅导的业务需求，包含以下功能：</p>
<ul>
<li>过程汇报</li>
<li>过程评价</li>
<li>评价征询</li>
<li>追踪预警</li>
<li>任务督办</li>
<li>汇报模板</li>
</ul>
<p>企业在发展过程中，需要断调整其目标方向及管理方式，绩效管理也是一样，在过程中可能需要不断调整和切换目标计划。过程辅导的设计难点在于<strong>如何满足多线任务、多角色辅导的需求</strong>。</p>
<p>举个例子，年初Q1阶段，员工根据部门组织目标制定了个人年度计划，并每月根据年度计划任务的过程执行情况，向自己的直线领导汇报工作。在Q2阶段，参与项目A，还需要按每周一次的频率，向项目负责人另外做汇报，形成了两条汇报线。在Q4的时候，需要根据自己的全部工作，包括项目A，一并进行年度总结向公司领导汇报。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/XzdPszSRulLN29Fi05ny.png" alt="eHR-绩效管理系统" referrerpolicy="no-referrer"></p>
<p>系统需要满足企业多种绩效考核模式，支持多线程过程辅导工作，要考虑到计划任务在不同时间节点进行任务的增删改，同时按照多角色、多线程管理目标任务的方式开展任务。</p>
<h3>3. 考核评估模块</h3>
<p>包含绩效总结、总结审批、总结征询、综合评估、绩效排名、考核配置等功能。大型企业的业务模式会比较复杂，需要考虑如何支持以下考核场景：</p>
<ul>
<li>多个角色参与</li>
<li>多种考核工具</li>
<li>多个考核周期</li>
</ul>
<p>下图就是较常见的考核场景，员工的年度考核包含了3项任务，职能性的工作由直线主管考核，项目性的工作由项目经理进行考核。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-绩效管理系统" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/lLxFpQXfvhApZo0MYXDx.png" alt="eHR-绩效管理系统" referrerpolicy="no-referrer"></p>
<p>这3项任务由不同的角色评分，并且采用不同的评分方式。职能工作由直线领导和业务同事进行360考核。项目A由项目负责人进行考核评分。项目B因为是跟销售业绩挂钩，业务系统根据销售业绩，直接计算评分，由项目负责人确认分数。最终得分则由直线主管或者部门长作确认并进行绩效排名。</p>
<p>系统功能上，支持多线考核任务的场景，各方角色围绕被考核对象进行考核任务处理。除此之外， 评分、排名、面谈工作是否需要进行流程上的拆分，还需要根据企业的具体管理制度而定。</p>
<h3>4. 结果应用模块</h3>
<p>主要包含以下功能：</p>
<ul>
<li>个人绩效画像</li>
<li>团队绩效画像</li>
<li>绩效全景图</li>
<li>调薪应用规则</li>
<li>晋升应用规则</li>
</ul>
<p>结果应用将员工绩效结果生成画像，根据业务规则应用到各个业务模块。</p>
<h2 id="toc-8">八、一点经验之谈</h2>
<p>绩效系统在企业管理系统中占有重要地位，但产品经理要衡量灵活性和研发成本，确定好产品的能力边界，避免过度设计，导致绩效系统功能过于繁杂。</p>
<p><strong>毕竟绩效管理的目标是提升和激励员工，如果系统有过多的汇报环节和冗长的考核过程，最终会大大降低员工的积极性，适得其反。</strong></p>
<p> </p>
<p>作者：产品老黄人，入坑6年的B端产品，在某行业头部企业任职资深产品经理，专注eHR\OA\CRM系统。公众号：产品老黄人。</p>
<p>本文由 @产品老黄人 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5269313" data-author="322454" data-avatar="http://image.woshipm.com/wp-files/2021/12/RHMGnoubsfFVFa614pLs.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            