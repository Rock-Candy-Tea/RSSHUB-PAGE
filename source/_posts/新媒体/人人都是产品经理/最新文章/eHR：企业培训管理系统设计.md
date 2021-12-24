
---
title: 'eHR：企业培训管理系统设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/LEE612hv5MLwPPHOfovh.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 23 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/LEE612hv5MLwPPHOfovh.jpg'
---

<div>   
<blockquote><p>编辑导语：企业培训管理系统应该怎么设计，才能提高企业内部的培训效率，进而推动业务进行？也许，你需要对企业培训先进行一个全面的了解，之后才能更好地进行系统设计。本篇文章里，作者结合实际经验，对企业培训管理系统的设计策略做了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5262624 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/LEE612hv5MLwPPHOfovh.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>eHR系统包含核心人力、人员管理、薪酬管理、绩效管理、招聘管理、培训管理等模块，而培训管理系统是eHR的基础模块之一，属于人力资源业务主要功能模块。培训管理系统可实现培训资源的整合，从而提高培训效率、增强培训效果、降低培训成本、扩大培训范围。</p>
<p>我结合近期所负责的培训管理系统项目，一起探讨如何搭建企业培训管理系统，培训系统的整体业务架构图及产品架构图如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/0HxYAK4WUvw9DAM6rmqR.png" alt="eHR-企业培训管理系统设计" width="618" height="378" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/J4XpzBKow14FL5xr1maX.png" alt="eHR-企业培训管理系统设计" width="617" height="361" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是企业培训</h2>
<p>在开始设计企业培训系统前，首先要了解什么是企业培训。</p>
<p>百科对企业培训的定义：企业培训是指企业或针对企业开展的一种提高人员素质、能力、工作绩效和对组织的贡献，而实施的有计划、有系统的培养和训练活动。企业组织培训，目标是提高员工能力，促进企业发展，培训管理是企业必不可少的管理工作。</p>
<h2 id="toc-2">二、企业培训的业务价值</h2>
<p>企业培训最直接的业务价值是提高个人和组织的业绩，推动组织和个人的不断进步，实现组织和个人的双重发展。</p>
<h2 id="toc-3">三、企业培训场景</h2>
<p>企业培训角色有企业的管理者、培训讲师、学员、培训HR，他们是培训系统的价值受益者。我们对不同角色的培训场景进行了详细调研，这里列举几个培训场景：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/TaMRoMNE4KH6Dr54QPPs.png" alt="eHR-企业培训管理系统设计" width="624" height="133" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>企业管理者：</strong>年初，企业战略会议决议通过本年度培训计划及培训预算，并落实分配到各个部门；</li>
<li><strong>培训HR：</strong>根据所负责部门的培训计划，每月组织开展培训活动，并对培训活动进行总结，向HRBP汇报；</li>
<li><strong>讲师：</strong>疫情防控期间，企业讲师通过办公网络，用手机在线上进行直播授课；</li>
<li><strong>学员：</strong>在手机app进行业务课程学习，完成组织安排的学习任务。</li>
</ul>
<h2 id="toc-4">四、企业培训业务流程</h2>
<p>企业培训的业务流程可以大致分为四个环节步骤，培训计划、培训实施、培训运营、总结分析。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/tIJzQd3BfrdUVMJmC8ja.png" alt="eHR-企业培训管理系统设计" width="621" height="54" referrerpolicy="no-referrer"></p>
<h3>1. 培训计划</h3>
<p>根据企业的培训资源，分析企业的培训需求，从而制定企业的培训计划，通过培训管理系统建立培训体系。</p>
<h3>2. 培训实施</h3>
<p>根据培训计划，开展培训工作，通常由负责培训管理的HR进行实施工作。</p>
<h3>3. 培训运营</h3>
<p>为了使培训达到更好的效果，在培训的过程中，管理员会通过相关的运营活动，使讲师、学员更加积极地参与培训，因此培训运营是相对于其他人力资源模块，更注重用户运营，产品经理在设计系统产品时，也需要更关注用户体验。</p>
<h3>4. 总结分析</h3>
<p>培训活动完成后，HR及企业管理层需要对培训效果进行评估，对培训成本、投入产出比进行测算，为后续的培训计划提供依据。</p>
<h2 id="toc-5">五、企业培训系统的业务架构</h2>
<p>通过对培训业务的梳理，可以初步形成培训系统的业务架构图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/1wH4y9yxW8VR6LMEuWK2.png" alt="eHR-企业培训管理系统设计" width="619" height="379" referrerpolicy="no-referrer"></p>
<p>通过业务架构图，我们可以看清楚企业培训业务的全貌。</p>
<h3>1. 企业培训的业务价值链</h3>
<p>对于企业而言，培训管理有助于提升企业整体竞争力，促进业务发展；对于企业的管理者而言，培训管理可培养和发展人才；对于员工而言，企业培训可提高个人能力，并通过员工之间的知识分享实现共同提高。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/hFdvMWpUAt1gMprRpzzT.png" alt="eHR-企业培训管理系统设计" width="625" height="92" referrerpolicy="no-referrer"></p>
<h3>2. 与其他模块系统关系</h3>
<p>培训系统作为应用HR信息系统的重要模块，与核心人力、绩效管理、员工画像等多个模块上都有业务关联。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/E8QrRehRffz8wp6tJpPc.png" alt="eHR-企业培训管理系统设计" width="296" height="335" referrerpolicy="no-referrer"></p>
<p>比如在进行岗位培训业务时，需要核心人力模块提供对应的岗位数据、组织架构数据及人员信息，根据业务要求开展培训工作。而绩效系统与培训系统两者关联也比较大，因为评估培训效果直接体现在员工的绩效上，同时绩效不好的员工需要加强业务上的培训。因此在进行系统设计时，同时需要考虑到模块间的业务支持，抽象出对应的系统功能。</p>
<h3>3. 培训业务产品能力</h3>
<p>根据培训管理的业务场景和业务流程，我们将培训系统的能力分成四个主要功能模块：</p>
<ol>
<li>培训资源管理；</li>
<li>培训运营管理；</li>
<li>培训学习应用；</li>
<li>培训数据分析。</li>
</ol>
<h2 id="toc-6">六、企业培训系统的系统架构</h2>
<p>初步梳理的培训系统的产品架构：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Kxm7A04pmcnnu2mRSsEi.png" alt="eHR-企业培训管理系统设计" width="620" height="363" referrerpolicy="no-referrer"></p>
<h3>1. 表现层</h3>
<p>该项目属于内部系统，共有PCAPP小程序三个端，PC端主要提供培训业务中台的管理能力，app端及小程序主要为学员提供培训应用功能，以及为讲师提供在线授课等功能。</p>
<h3>2. 应用层</h3>
<p>按照业务架构中产品的四个能力，即培训资源管理、培训运营管理、培训学习应用、培训数据分析进行功能规划。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/TscSI0K7C5JplTCpp7Co.png" alt="eHR-企业培训管理系统设计" width="618" height="171" referrerpolicy="no-referrer"></p>
<p><strong>1）培训资源管理</strong></p>
<p>对企业培训相关的资源进行统一管理，培训资源分为：</p>
<ul>
<li>内容资源；</li>
<li>人力资源。</li>
</ul>
<p>内容资源即培训物料、课程、题库，人力资源即讲师资源及学员管理。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/zYRWnzL28nfxHY1g4ElV.png" alt="eHR-企业培训管理系统设计" referrerpolicy="no-referrer"></p>
<p>在课程内容方面，系统支持课程内容的创建，同时还支持使用外部供应商内容，满足企业不同的培训需求。而讲师资源管理，涉及到内部讲师，外部讲师管理等功能。</p>
<p><strong>2）培训运营管理</strong></p>
<p>通过运营管理模块完成培训的业务闭环。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/eIgOfb06t6NtEJOwnSwf.png" alt="eHR-企业培训管理系统设计" referrerpolicy="no-referrer"></p>
<p>主要功能划分如下：</p>
<ul>
<li>培训计划；</li>
<li>培训实施；</li>
<li>培训运营；</li>
<li>培训评估。</li>
</ul>
<p>在培训计划环节，系统提供了培训需求分析、培训成本分析的能力。</p>
<p>在培训的实施环节，系统提供项目管理能力，帮助培训管理者将培训计划实施落地。</p>
<p>在培训运营环节，系统提供包含了证书管理、活动管理、学习任务、积分系统等功能。</p>
<p><strong>3）培训学习应用</strong></p>
<p>学习应用主要是满足学员端多种培训场景。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/rmjbGlg8ann4p1Y0awKg.png" alt="eHR-企业培训管理系统设计" referrerpolicy="no-referrer"></p>
<p>主要有以下功能：</p>
<ul>
<li>自学中心；</li>
<li>学习社区；</li>
<li>学习地图；</li>
<li>自制课程；</li>
<li>考试任务；</li>
<li>评分评价；</li>
<li>积分商场；</li>
<li>学习分队。</li>
</ul>
<p><strong>4）培训数据分析</strong></p>
<p>从个维度进行数据分析，支持从项目的维度进行数据分析，及从课程内容的维度、学员个体的维度进行数据分析，全方位全流程地评估培训效果。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="eHR-企业培训管理系统设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ADpBEpvwow2zoXosbBgF.png" alt="eHR-企业培训管理系统设计" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">支撑层</p>
<p>培训管理系统跟其他应用模块一样，在支撑层使用到共用的中台技术支撑、底层的基础服务支撑等，这里不多赘述。</p>
<h2 id="toc-7">七、产品设计过程中的一些经验分享</h2>
<p>在这里也跟大家分享一下产品设计过程中的一些经验。</p>
<h3>1. 培训系统需要结合C端产品运营设计思路</h3>
<p>培训系统在eHR系统中，应该算是最为重视用户运营的模块之一。</p>
<p>一个原因是培训业务运营的好坏，最终会影响到员工的绩效，从而影响到企业整体的收益。</p>
<p>二是因为企业的培训是长期训练的过程，而不是补针效应，需要HR、讲师、学员各方积极配合参与，才能达到良好的培训效益。</p>
<p>我们需要思考培训系统如何能提交培训效果，真正为企业带来业务价值？我们在产品的设计过程中，结合了C端产品运营思路，将<strong>用户运营、内容运营、活动运营、数据运营</strong>的设计应用到系统中。</p>
<p><strong>1）内容运营的功能设计</strong></p>
<p>优质培训内容资源是开展培训的前题条件，培训资源需要结合用户端的培训需求、企业端培训需求，提供大量优质的培训内容，这跟一些商业产品的运营思路相类似。</p>
<p>在内容资源管理上，系统着重加强两种课程内容的运营能力</p>
<ol>
<li>UGC内容，即员工自制课程；</li>
<li>PGC内容，即企业制作课程。</li>
</ol>
<p>通常企业会鼓励员工制作学习课程(UGC)，并选拔内部优秀员工作为讲师进行授课，这是常见的培训方式，这也是企业驱动用户生产UGC内容的方式。</p>
<p>而企业制作课程（PGC）则由讲师进行编辑制作的专业课程，以及供应商课程，比如喜马拉雅、得到等大型知识平台，作为课程学习资源，供企业员工进行学习。</p>
<p>针对课程内容，系统都会设置评分评价体系，通过评分机制，提高内容质量，在运营过程中，管理员还可以组合活动运营、用户运营工具提高用户的课程内容产出。</p>
<p><strong>2）用户运营的功能设计</strong></p>
<p>在进行培训系统设计时，既要考虑到如何提高培训内容的质量，还要考虑提高培训人员的参与度及培训效果。为了提高用户的活跃度，培训系统使用的用户运营工具：</p>
<ul>
<li>积分体系；</li>
<li>等级体系；</li>
<li>游戏运营。</li>
</ul>
<p>积分体系方面，系统可以针对学员设计不同的积分获取规则，通过学习、分享课程获取积分，而积分可用于兑换新课程、礼品等等，从而促进学员活跃度。</p>
<p>在讲师端，积分也可跟讲师等级体系挂钩，通过积分提升等级，鼓励讲师制作、讲授课程。</p>
<p>等级体系方面，学员和讲师分别设有相应等级，无论是学员还是讲师，等级体系都是用于激励用户更好地参与到培训中。</p>
<p>而用户运营另外一个重要工具是游戏化运营，做得比较多的是学习任务地图、游戏关卡等功能，将学习任务游戏化，提高学习的趣味性。</p>
<p>通过“闯关”、“经验值”、“打卡”等玩法来提升学习积极性。</p>
<p><strong>3）活动运营功能方面</strong>，通常需要结合专题课程功能、资讯频道、学习社区等功能实现活动运营，提高学员的活跃程度。</p>
<p><strong>4）数据运营功能方面</strong>，在系统从多种维度进行数据分析，为企业培训的计划、预算、效果提供依据。</p>
<h3>2. 其他可能遇到的问题</h3>
<p><strong>1）课程内容的权限问题</strong></p>
<p>上面有提到培训课程内容有多种来源方式，有自制课程、讲师课程、供应商课程等。</p>
<p>一些大型企业对知识库、培训内容会有不同的管理要求，特别是涉及商业机密的培训内容要特殊管控。</p>
<p>因此课程内容资源需要将管理权限、使用权限、查看权限进行单独处理，灵活管控避免泄密问题出现。</p>
<p><strong>2）学习任务推送场景问题</strong></p>
<p>企业培训的业务场景比较多，有管理员手动推送任务、系统规则推送任务、岗位学习任务推送、自定义推送任务等等，需要考虑到学习任务的内容异常场景、人员的入转调离场景、任务回撤场景等问题。</p>
<p> </p>
<p>作者：产品老黄人，入坑6年的B端产品，在某行业头部企业任职资深产品经理，专注eHR\OA\CRM系统。公众号：产品老黄人。</p>
<p>本文由 @产品老黄人 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5261274" data-author="322454" data-avatar="http://image.woshipm.com/wp-files/2021/12/RHMGnoubsfFVFa614pLs.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            