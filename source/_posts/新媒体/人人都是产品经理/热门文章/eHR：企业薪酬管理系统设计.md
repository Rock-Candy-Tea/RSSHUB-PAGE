
---
title: 'eHR：企业薪酬管理系统设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/4ihucrzmJtiHRTAa4obq.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 10 Jan 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/4ihucrzmJtiHRTAa4obq.jpg'
---

<div>   
<blockquote><p>编辑导语：薪酬管理系统是每个企业必备的一个系统，系统设计得合规，能够减轻财务人员的负担，提供工作效率。eHR系统提供了多项人力管理的业务，薪酬管理属于其中的一个核心模块之一。本文与大家探讨如何搭建企业薪酬管理系统，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5281098 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/4ihucrzmJtiHRTAa4obq.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>eHR系统包含核心人力、人员管理、薪酬管理、绩效管理、招聘管理、培训管理等模块，而薪酬管理是eHR的核心模块之一，本文将跟大家探讨如何搭建企业薪酬管理系统。</p>
<p>薪酬管理系统的整体业务架构图及产品架构图如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/UuMX46ondhfNWymrca6n.png" alt="eHR-薪酬管理系统设计" width="654" height="465" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">薪酬系统业务架构图</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/gtoCTf1CtcOQ1YLlAamY.png" alt="eHR-薪酬管理系统设计" width="613" height="431" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">薪酬系统产品架构图</p>
<h2 id="toc-1">一、薪酬的构成</h2>
<p>当前企业薪酬支付形式日益多样化，各种显性和隐性的薪酬形式层出不穷，福利、股权占薪酬的比重也越来越大，通常业务上所谓的薪酬，是指整体薪酬。</p>
<p>整体薪酬包括外在薪酬和内在薪酬，外在薪酬又包括基本工资、加班工资、绩效奖金、利润分配、股票期权、保险、住房补贴、薪资福利等。</p>
<p>内在薪酬，包括个人成长、升值空间、平台视野这些无形的薪酬，则不是系统所关注的重点。</p>
<p>而外在薪酬通常都可以用货币形式发放，这部分也就是通过薪酬管理系统和eHR系统管理的薪酬项目。</p>
<h2 id="toc-2">二、企业常用的薪酬模式</h2>
<p>用人单位会根据岗位的不同，采用多种薪酬模式。</p>
<p>设计薪酬管理系统时，要考虑满足当前市场上大多数薪酬管理模式。</p>
<p>具体包括以下几种：</p>
<ul>
<li>宽带薪酬模式</li>
<li>岗位薪酬模式</li>
<li>技能薪酬模式</li>
<li>其他薪酬模式</li>
</ul>
<p>宽带薪酬适用于扁平化组织，是目前最流行的薪酬管理模式，是我们要重点了解的薪酬模式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/uZ4F20TXhsOUwTW5miw7.jpeg" alt="eHR-薪酬管理系统设计" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">宽带薪酬与窄带薪酬的区别</p>
<p>宽带薪酬是用相对较少的薪酬等级以及相应较宽的薪酬变动范围，将企业原来数十个薪酬等级压缩成几个级别，工资浮动范围比较大，主要表现形式是固定薪酬+绩效薪酬。</p>
<p>岗位薪酬模式，以岗位来分配薪酬，它强调劳动价值和岗位价值的等价作用，一些国企和事业单位使用比较多。</p>
<p>技能薪酬模式，以员工能力或者技能作为支付方式，形式上有计件式、佣金式、年薪式等形式，这个模式通常会将绩效跟薪酬挂钩，在劳动密集型、销售型企业用的比较多。</p>
<p>其他薪酬模式还包括传统薪酬模式、年功薪酬模式等等。</p>
<p>产品经理在设计薪酬管理的功能时，要考虑使系统具备灵活的计算能力，支持不同的薪酬方案。</p>
<h2 id="toc-3">三、薪酬管理业务架构</h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/tnyzYslTl6ShdbXVrlts.png" alt="eHR-薪酬管理系统设计" width="607" height="431" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、薪酬管理的业务角色</h2>
<p>从系统的实际出发，薪酬管理涉及到以下角色：</p>
<ul>
<li>公司管理者</li>
<li>财务人员</li>
<li>薪酬HR</li>
<li>相关模块HR</li>
<li>系统管理员</li>
<li>业务部门参与者</li>
</ul>
<p>财务部：负责薪酬总额测算、计算公式调整、薪酬录入、核算、计税和发放。</p>
<p>公司管理者：进行薪酬总额测算、薪酬总额分配、计薪人员管理、定级定薪管理、计薪人员管理等工作。</p>
<p>薪酬HR：是薪酬管理主要参与者，负责总额计算、定薪定级、薪酬录入、核算等工作。</p>
<p>相关模块HR、业务部门参与者，根据薪酬管理的业务流程，参与到薪酬计算核算流程中。</p>
<p>根据不同的企业管理制度要求，还会将薪酬管理工作进行细分，比如有专门负责定岗定薪的HR、算薪管理HR、绩效管理HR。</p>
<p>集团型薪酬管理系统或者通用型的薪酬管理系统时，要重点考虑不同角色的权限问题，可以设置类似于绩效系统的考核组的方式，为不同部门组织设置对应的算薪组，通过管理算薪组，灵活开展薪酬业务，提高系统的灵活性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/xDXBysAsnTq6MdprIoet.png" alt="eHR-薪酬管理系统设计" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">系统角色用例</p>
<h2 id="toc-5">五、薪酬管理的业务场景</h2>
<p>薪酬管理涉及到公司战略、财务、管理制度等多方面需求，业务场景相对人力资源其他管理模块较为复杂，从企业管理角度看，我们将薪酬管理的业务抽象成4个业务场景：</p>
<ol>
<li>建立薪酬体系</li>
<li>确定执行方案</li>
<li>计算发放薪酬</li>
<li>查询薪酬数据</li>
</ol>
<p>建立薪酬体系：是从公司的战略角度出发，建立推动企业稳定发展的薪酬体系，其目的在于通过保障企业和岗位员工两个方面的利益，共同发展。</p>
<p>确定执行方案：是根据公司的薪酬体系，针对不同部门、岗位制定可执行的薪酬方案，落实到每位员工。</p>
<p>计算发放薪酬：是在固定的薪酬期间进行薪酬计算，通过财务部门向员工发放薪酬。</p>
<p>查询薪酬数据：有HR查询数据、员工个人查询数据等业务场景。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/UHNbBSqYIXOsDbJDwhod.png" alt="eHR-薪酬管理系统设计" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">薪酬系统业务场景</p>
<h2 id="toc-6">六、薪酬管理系统间关系</h2>
<p>薪酬与绩效系统关系：员工的绩效数据直接关系到薪酬的计算结果，甚至许多企业eHR将绩效和薪酬合并成一个模块进行管理。</p>
<p>薪酬与核心人力系统关系：岗位和职级等数据，是确定薪酬的基本，因此薪酬系统需要根据人力的核心数据定岗定薪。</p>
<p>薪酬与招聘系统关系：人员招聘入职时，需要走定岗定薪流程，涉及到薪酬部分数据的参数调用。</p>
<p>薪酬与员工管理系统关系：员工的职务调动、岗位调整、员工考勤、自主查询等服务功能，需要与薪酬管理模块产生数据关联。</p>
<h2 id="toc-7">七、薪酬管理系统架构</h2>
<p>根据业务场景，将薪酬管理系统分成4个大的功能模块：</p>
<ol>
<li>薪酬体系管理</li>
<li>薪酬执行管理</li>
<li>算薪发薪管理</li>
<li>数据报表</li>
</ol>
<p>薪酬体系管理：帮助管理者制定公司整体薪酬方案，从人力和财务维度进行管理。</p>
<p>功能包含薪酬总额预算管理、人员编制管理、成本中心等模块功能。</p>
<p>薪酬执行管理：主要根据管理者制定的薪酬体系，制定执行薪酬方案的功能。</p>
<p>定调薪管理、奖金管理、社保公积金管理、计薪规则管理、考勤规则、个税政策、薪资试算、薪酬审核等功能。</p>
<p>算薪发薪管理：包含数据维护，算薪人员维护，任务管理等功能。</p>
<p>数据报表：为员工、管理员提供数据报表及相关查询功能。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/CgGSk2el9W5zrMMKjMeB.png" alt="eHR-薪酬管理系统设计" width="790" height="305" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">薪酬系统功能模块</p>
<h3>1. 算发薪模块功能</h3>
<p>一般在薪酬管理系统中，个体薪酬管理中算发薪模块属于最小MVP的功能模块，是薪酬管理系统必不可少的能力。</p>
<p>我们可以把算发薪流程细化出来，分为3个步骤：</p>
<ol>
<li>数据维护</li>
<li>计算薪酬</li>
<li>发放薪酬</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-薪酬管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/mzpn08UYeBTDsrGmNNDc.png" alt="eHR-薪酬管理系统设计" width="645" height="508" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">算发薪的基本流程图</p>
<p>算薪数据维护，是计算薪酬的初始步骤，涉及到多个模块的数据，HR需要在系统上维护相关的数据，比如员工的工作性质、岗位调动、考勤数据等等，数据准备完成后执行计算任务。</p>
<p>薪酬的相关数据配置、计算方法配置，通常会在系统配置阶段完成，减少了HR在算薪阶段的工作量。</p>
<p>执行算薪任务后，对当期的所有数据进行校验，需要将算薪涉及的数据推送给对应的负责人审核。</p>
<p>比如，绩效考核数据在绩效系统中数据未同步，由绩效HR确认员工的绩效成绩。</p>
<p>以往这些工作可能是通过线下进行操作，在eHR各个模块打通后，确认流程线上化，大大节省了HR的效率。</p>
<p>计算薪酬完成后，由负责薪酬计算的管理员审批，系统将生成报盘文件，交由财务部门执行发薪流程，完成薪酬发放任务。</p>
<h2 id="toc-8">八、设计薪酬系统的经验分享</h2>
<h3>1. 系统设计</h3>
<p>系统设计的重点是数据分析和决策支持能力。</p>
<p>与其他eHR模块不同，薪酬系统不仅涉及到人的管理，还涉及资金的管理，直接关乎公司经济利益。</p>
<p>好的薪酬系统是建立在公司战略层面上，为公司管理层提供决策支持，因为公司领导关注人力资源的同时，更多的是关注公司盈利状况和未来发展。</p>
<p>在薪酬业务领域里，普通的薪酬HR只需要根据公司薪酬方案执行算发薪任务即可，这部分用户只会使用到系统的初级能力。</p>
<p>高级薪酬HR、总监，则是通过薪酬战略为公司招揽人才，通过薪酬策略，降低用人成本，直接为公司获取经济效益，这部分需求却是薪酬系统的核心能力。</p>
<h3>2. 产品经理能力</h3>
<p>产品经理重点能力是业务知识储备和商业视野。</p>
<p>作为B端产品经理，天然地需要深入了解业务，而薪酬系统要求产品经理不仅仅了解人力资源方面的业务，还要了解财务方面的业务。</p>
<p>比如说薪酬数据，需要先弄清楚相关的财务科目，因为薪酬科目就是从财务借用过来的术语，做财务报表，就涉及会计科目。</p>
<p> </p>
<p>作者：产品老黄人，入坑6年的B端产品，在某行业头部企业任职资深产品经理，专注eHR\OA\CRM系统。公众号：产品老黄人。</p>
<p>本文由 @产品老黄人 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5280723" data-author="322454" data-avatar="http://image.woshipm.com/wp-files/2021/12/RHMGnoubsfFVFa614pLs.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">3人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175124_8676.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602180747_3259.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183424_5190.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            