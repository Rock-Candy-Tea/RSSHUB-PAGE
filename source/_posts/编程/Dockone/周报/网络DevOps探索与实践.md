
---
title: '网络DevOps探索与实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/6302e124e33d30d884937ab119d0db44.png'
author: Dockone
comments: false
date: 2021-04-06 00:27:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/6302e124e33d30d884937ab119d0db44.png'
---

<div>   
<br>【编者的话】在SDN及云网络大行其道的背景下，运营系统的开发工作面临着新的挑战。传统的运营定义需求、由专业开发端到端实现上线的模式已经难以为继。本文主要讲述如何利用DevOps的模式，打造一个可配置、Codeless的运营平台，实现上层业务应用由运营人员自行开发的目的。<br>
<br>DevOps作为一种重视软件开发人员与运维人员的沟通合作的文化及管理手段，已经在系统需求管理、开发构建、部署发布等场景显示出其便捷、可靠等优势。腾讯网络在基础架构海量运营中积累了不少经验，基于DevOps的理念重新设计了运营系统的软件架构。接下来，会介绍该系统在事务流程化、Codeless、开发生命周期管理、产品化等方面的实践经验。<br>
<h3>为什么要引入DevOps模式？</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/6302e124e33d30d884937ab119d0db44.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/6302e124e33d30d884937ab119d0db44.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
老的开发模式这样会出现多个问题：<br>
<ul><li>最常见的一个场景：开发这边的排期已经到2个月之后，运营这边觉得太晚了。但前面确实有那么多开发需求待实现。开发搞不过来了。</li><li>某些新的监控项目，运营通过具体的数据才能知道该功能的业务价值；开发的同学把功能上线后，就忙着下一个需求了，对后续的运营关注不多。经常会导致历史上积累了非常多的工具系统，但作用都很寥寥。</li><li>基础架构的运营系统，原来只针对自研业务做了大量的功能；后来到公有云，现在也有大量的私有云客户，服务的对象发生了变化。外部的客户对功能需要做二次开发，需要具备DevOps能力。</li></ul><br>
<br>为了解决以上这些问题，需要系统化的来进行解决。根本上来说，就是要以人为本，提升运营与开发的满意度，DevOps是一个切实可行的方案。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/828deb85b1322e7875056f56b4f85bbe.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/828deb85b1322e7875056f56b4f85bbe.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
DevOps没有发明任何新技术，他只是一种软件开发的模式。这里有个DevOps的分级模型，是国内业界的前辈制定了一个规范，最近也已经通过了ITU-T组织的审核。这里内容比较多，不逐一赘述。基础架构DevOps的实践过程，是借鉴其理念，让大家都在同一个简单易用的软件平台上进行合作开发，达到服务快速上线目的。其中最主要的一个关键点就是双方要进行融合，互相促进。<br>
<h3>腾讯网络运营DevOps系统的现状</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/27d5fe941ebb75cbdc86c21ba7ad4ecd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/27d5fe941ebb75cbdc86c21ba7ad4ecd.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
腾讯的网络运营先后经历人工操作、工具脚本、自动化等这几个阶段。运营团队，就是我们熟悉的网工，过去都有专业的开发人员来进行配套的工具系统开发。在过去几年，网工们的开发能力持续提升，在DevOps平台的加持下，已经掌握了通用的开发能力，一些运营过程中需要的功能，可以基于DevOps平台自行开发了。这样，传统的开发人员和网工，都可以基于这个统一平台来“吃自己的狗粮”。运营人员自行开发功能，上线后出现问题，反查自己设计的业务逻辑；开发人员主导开发功能发布后，出现了bug，也自己定位代码或者平台的问题。这样，发现问题后，都先从自身出发来排查，减少了互相埋怨，大家的关系也相对融洽起来。<br>
<h3>如何建设DevOps平台？</h3>我们把建设的过程分以下6个方面来介绍。<br>
<h4>1、上层规划 – 运营事务流程化</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/cd14727ff3aa5bce23e1f6620923027b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/cd14727ff3aa5bce23e1f6620923027b.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
无流程不运营。我们在内部先把这个意识先进行了统一，这个是DevOps开发的前提，也是DevOps任务可编排的前提。我们经常说可编排，编排完了之后，不就是由一个个编排后节点串接起来的流程吗？下面跟大家介绍下我们内部总结出来的流程成熟的模型。初步评估，腾讯基础架构运营处在level 3这个阶段。怎么解读呢？<br>
<ul><li>流程体系化，是指我们各个运营业务基本都有了对应的线上流程。几乎不存在线下操作的场景了。</li><li>部分的流程完成生命周期管理，这个是对流程控制端到端的一个需求。</li><li>较为完善的OLA/SLA管理，有了详细的OLA数据，我们就能对每个工单的实施过程都能详细的分析和管理。</li><li>工具系统敏捷迭代，系统工具除了能直接解决业务的需求，还要有二次开发的能力。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/a05a9f8c770d11157dbbc4082a031592.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/a05a9f8c770d11157dbbc4082a031592.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在系统架构顶层设计方面，我们使用DDD—领域驱动设计的模式，具体到DevOps平台，着重领域层的实践。把DevOps的整体功能模块分为四大块：<br>
<ul><li><strong>可视化编排平台</strong>：这个是运营事务流程化的具体落地方式。流程图让业务逻辑可以非常直观的展示出来。</li><li><strong>应用管理模块</strong>：方便用户参与开发。SDK的方式，是开源共建的基础，减少了大量重复代码；权限管理，有效避免了用户之间的互信影响。</li><li><strong>数据运营模块</strong>：数据化管理。流程及工单数据每天都会以非常大的量级增长，没有完善的任务超时告警及运营数据自动收集分析功能，后续的业务维护会非常耗时耗力。</li><li><strong>平台管理</strong>：是系统运维的重要窗口。让人人可运维成为可能。</li></ul><br>
<br><h4>2、业务逻辑 – 无代码化开发</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/8c85eb69403d1a07b753c3cefaa61112.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/8c85eb69403d1a07b753c3cefaa61112.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
无代码化开发，并不是指一行代码都没有。而是尽量减少编码的场景。在很多模块中，DevOps平台把设备命令模板层、业务函数、业务流程及触发规则等这四个层次，都用对应的模板或SDK封装起来，形成可复用的逻辑。这里列举的是命令模板这一层的封装。对于运营人员来说，在DevOps体系的驱动下，开发能力逐步提升。同时，通过配置化或少量的代码，可以用极低的成本，快速开发上线验证类的功能，不需要任何专业开发资源投入，大大较少试错的成本。<br>
<h4>3、DevOps的生命周期管理</h4>这里是从DevOps开发的新模式出发，把过程中需要配套的功能点逐一进行完善，从而完成了DevOps开发整个生命周期的管理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/24514e6a6f37e8f1452f491e21fddcae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/24514e6a6f37e8f1452f491e21fddcae.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><strong>需求管理</strong>。对需求进行建模，把功能点往各个预分配好的领域靠拢，避免功能碎片化。在腾讯内部，有TAPD工具对需求做详细跟踪，保证落地效果。</li><li><strong>开发环境</strong>。这个是参与DevOps开发同学最关心的地方，直接关系到开发效率。主要涉及环境统一配置、代码版本管理、测试覆盖及CI/CD等环节。</li><li><strong>流程管理</strong>。事务流程化后，会产生非常多的流程，流程图需要方便创建及修改；其次在工单建立后，会马上实例化，任务执行过程中的异常超时基础配置需要在OLA/SLA中进行配置。</li><li><strong>任务管理</strong>。具体事务的操作，更多的是调用第三方接口和对设备进行查询操作。需要全程对任务的执行过程进行跟踪，其次需要把可以复用的代码通过SDK有效管理起来，避免重复开发。</li><li><strong>运维管理</strong>。这块是整个DevOps平台的后腰，保证系统的正常运行，以及出现问题后快速恢复。</li></ul><br>
<br><h4>4、可维护 – 产品化的控制台</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/6a2cac9df607914ea3ef453262f9aff1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/6a2cac9df607914ea3ef453262f9aff1.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
提供便于DevOps应用开发和运维的Web控制台，旨在通过页面可视化以及页面可操作的手段，提升开发和运维效率。在过去，我们讲的D/O分离是指开发与系统运维的分工。在DevOps时代，运维工具不但面向专业开发人员，也需要面向业务开发人员，让大家在同一个控制台中发现问题、定位问题。在运维底层功能方面，我们把流程实例管理、任务管理及控制台的功能，按不同的角色进行开放。本着谁开发，谁负责的原则，大家一起共同把系统平台及业务功能模块的可用性维护起来。<br>
<h4>5、认证管理 – 建立岗前认证培训体系</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/10496adcdbe1fede2a7a791d9a25cb3d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/10496adcdbe1fede2a7a791d9a25cb3d.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
DevOps是一个以人为本，回归人性的一种开发运维文化，其效果体现更多的是在于人，在于从业人员能力的提升，更注重开发人员的感受。所以，在内部有一个DevOps的认证体系，经过这个体系的培训，可以让一个小白用户从零开始逐步上手。这个培训体系主要分为四个步骤：<br>
<ul><li>开发知识基础。主要是学习开发环境、代码管理及代码检查一些基础的知识。</li><li>DevOps功能开发。这个是按照基础架构运营功能的特点来展开的，主要的内容包括需求的提炼汇总，把运营需求用流程图的形式展示出来，然后进行任务节点的逻辑代码编写。</li><li>demo实战。经过以上两个阶段的学习，这里可以开始动手了。</li><li>经过一系列培训，通过考试后，对学员颁发证书。并根据不同的能力水平，证书也会区分一级、二级和三级。</li></ul><br>
<br><h4>6、最差实践 – 坑点</h4>我们的题目叫“最佳实践”，但这个过程并不是一帆风顺的，过程中经历了非常多的挫折与不理解。我们把这些因为考虑不完善而踩坑的地方总结了几个最差实践。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/35b8a68a8967461e7e8d45a274fb1f03.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/35b8a68a8967461e7e8d45a274fb1f03.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
第一方面就是主要功能点缺乏，用户使用满意度不高。<br>
<br><strong>1）尝试去优化某个具体的环节，而忽略了全局优化的可能</strong><br>
<br>前期缺少顶层设计，举个例子，我们之前一直以为画流程图是用户接触DevOps系统的第一个界面，是业务需求转化的第一步。就千方百计的把画流程图的界面进行优化。但用户在画完图了后，后面就很少会关注了。<br>
<br><strong>2）产品化不够，用户使用不够友好</strong><br>
<br>一个功能完备的DevOps平台就跟建设一座城市或一个小区一样，有太多的功能点需求开发。SDK的合入规则，云函数的调用方式等等。这些专业的开发技能，对于传统的开发同学来说，大家交流起来是很顺畅的。但对于运营同学，要跟大家解释就显得比较费劲。<br>
<br><strong>3）研发效能低下</strong><br>
<br>本地开发环境无法与线上环境保持一致，调试困难。还有业务代码逻辑的经常需要线上调试，测试的覆盖率长期偏低，功能稳定性无法保证。还有bug定位跟踪的方式比较单一，一个bug需要分析半天才能知道问题点在哪里。<br>
<br>第二方面是过度设计，没有使用户真正获益。对于Devops的深入程度，有一点我们必须牢记，那就是DevOps平台系统本身的成功并不是真正的成功，只能是业务的效率提升，<strong>使用DevOps的用户满意度提升了，才是检验成功的唯一标准。</strong><br>
<h3>网络运营DevOps系统的后续发展 - 打造生态</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210401/c3352a1cd900d13e8e6e2b940fe503f1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210401/c3352a1cd900d13e8e6e2b940fe503f1.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
罗马不是一天建成的，这个DevOps平台凝聚了腾讯基础架构运营多年的经验。之前我们谈的自动化及数据化运营，更多是端到端的传统开发方式。具体到DevOps，我们希望可以打造一个生态，可以跟众多的合作伙伴和外部的用户一起，一起在同一个平台上进行功能完善和迭代。<br>
<br>在接口对接方面，近期我们跟很多运营商及设备厂商一起努力，把报障、割接、还有case管理、备件管理等几个使用频率最高的场景进行了线上对接。在外部用户方面，我们通过腾讯云的窗口，把DevOps的能力对外进行的开放。使用的用户越多，发现越多的问题，DevOps平台的功能就可以越趋完善。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/OKLiDi78uB8ZkPG2kUVxvA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/OKLiDi78uB8ZkPG2kUVxvA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            