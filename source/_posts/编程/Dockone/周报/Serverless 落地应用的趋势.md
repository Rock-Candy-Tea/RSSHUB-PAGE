
---
title: 'Serverless 落地应用的趋势'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/b90d3b46748bc72a0c250452fc819486.png'
author: Dockone
comments: false
date: 2021-11-07 00:26:22
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/b90d3b46748bc72a0c250452fc819486.png'
---

<div>   
<br>【编者的话】Serverless 近年来炙手可热，在传统的 IT 架构已不适应当今快速发展的数字经济环境的背景下，Serverless 和 FaaS 是不是解决问题的银弹？在实际应用中，Serverless 的表现又是如何？本次演讲将分享 Serverless 的落地场景、问题与优势，探讨如何利用 Serverless 助力业务发展。<br>
<h3>架构设计的过程就是挖坑与填坑</h3>我是做OTA的，我们产品就是机票、火车票、酒店等等，最近有一个机票盲盒挺热的，那个是我们原创的，也是在 Serverless 上做的。今天主要讲 Serverless 的原因是，五年前我们做了自己的 Serverless，为什么做呢？我们当时也没发现这个有多高大上，是因为被业务逼的：一是能不能以最快的速度上线？最好早上想出一个绝妙的 idea，下午就上线。我们说不行，得加个设计、服务器部署……业务说，什么意思，不就写行代码吗？于是，我们被逼得不行了，KPI被压得很紧，我们这时候想到，如果我们去做不用关心服务器、不用关心部署和框架，甚至不用关心开发过程的办法，于是就去做了 Serverless。<br>
<br>五年前因为各种原因，也没有真正可以生产的 Serverless，于是我们自己开始从零做起，但自己做是比较简单的，因为我们不需要对外销售或者对外服务，我们只服务自己，不通的地方用行政命令就能解决；但对外，这件事就做不到了。落地趋势上来说，这五年我们一直把应用放上去，也有很多应用拿了出来，在分享的开始，我们一起来想这么几个问题：我们为什么要用 Serverless，只是为了让我们的架构设计好看一点吗？我们的架构师喜欢“追星”，怕落伍于时代？还是说我们真正要解决什么问题？第二是，Serverless 到底解决什么问题？一开始大家想到它可以弹性计算，弹性计算省的前真的比业务更重要吗？有些问题把它想到极致点的时候，可能更加容易解决，并不一定非得用一个技术去解决。另外，Serverless 怎么助力业务？难道只是为了更快的需求变现吗？那我们多招些程序员不是更快吗，如果HR同学足够努力，那 Serverless 就不用做了，因为有足够的工程师帮助变现。<br>
<br>带着这些问题我们再去想用 Serverless 做什么？来看架构设计的过程，<strong>其实架构设计的过程本身，我认为就是一个填坑与挖坑的过程</strong>。我们觉得单体应用不好，所以从单体的坑里爬出来，去旁边挖了一个微服务的坑，用挖出的土把单体的坑填了。当我们觉得微服务很难治理的时候，在旁边挖了一个service mesh的坑，又把这些土填回微服务的坑。后来我们又觉得 Serverless 很火，于是又挖了一个坑，挖到一半突然觉得隔壁单体的坑看起来不错，因为这么多微服务拉不起来，而单体就一个，我们是不是应该回归单体呢？于是就出来这么多填坑和挖坑的故事，也正好是刚才我们提到的，我们为什么去想 Serverless？因为在填坑和挖坑背景之下就是我们要解决业务应用难题的时候，在每一个时代，整个基础设施是不一样的，所以我们在那个时代填那个时代的坑的时候，发现因为基础设施落后，我们在架构上想了很多办法；当基础设施在提高的时候，于是我们架构设计又开始回归，这是不停循环的过程。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/b90d3b46748bc72a0c250452fc819486.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/b90d3b46748bc72a0c250452fc819486.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
回到原点，最早的时候应用怎么做？其实很简单，只需应用+数据库，最多在数据库上再放点缓存，运维也很简单，只需要看生死。但随着坑越挖越大，业务需求越来越多，系统规模越来越大，麻烦出现了。最早我们把前后拆开来，把一些服务单独部署出来，服务化、总线开始出现，这个时候架构本身意义上来说，它并没有大的变化，只是把原来完整的整体切分出多个个体。这个情况很多新的程序员还没有切身感受——什么是单体应用？现在的其实跟当年真正的单体应用差很多，我毕业时，一个单体运转起来上百G的内存就没了，非常依赖CPU的性能，成千上万的应用卡在代码里，根本分不清。但是到我们服务化之后，又出现问题，简单的服务化可能带来的是什么？更多的被部署，调用了无序，各种麻烦出来了，我们的问题是看到这么一张图（见下图），我们的运维、架构师看到所有应用的时候，就像看到那几个小孩把东西弄得杂乱无章，为什么？<strong>因为应用从1到10很简单，但拆成上万个应用的时候，可以想象刚才那种模式的大缺点是互相没有关系、不知道互相做了什么，这就带来大量重复的劳动</strong>，然后链路上到底哪一块是我们真正的压力？再下来，原来很简单的一句SQL，是否现在没法用了？一系列的问题带来了刚才架构的凌乱。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/9892bfa2332ca94ac1324e9173c00dc1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/9892bfa2332ca94ac1324e9173c00dc1.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
那为什么被如此吐槽的单体应用在今天还有大量的新增呢？甚至很多创业公司就是单体起家的，因为它能实现快速迭代。<strong>我们需要的并不是庞大而复杂的技术架构或者业务架构，我们真正要服务的是整个业务的快速变现和快速试错</strong>。这样的过程中，在量独大的情况下，这个场景下单体非常适合。但单体变大又带来很多麻烦，怎么办？微服务治理真能把它治理好吗？看起来这样的微服务架构是很好，但是很复杂，复杂到可能几个程序员都搞不定，或者随着时间推移一样会带来下一件事情——你的微服务越来越大，越来越像原来你所讨厌的那个单体的形象——很大，跑不动，所有的都在一起。但微服务里依然在发生，为什么？因为没有真正的方法论去控制微服务有多“微”，或者有多小，或者什么时候该再起一个服务？举个例子，我见过很多奇怪的服务，比如在正常的情况下，出现订单服务，突然在某一天有紧急需求，在没有控制、迫不得已的情况下，新做了个列表，改名为新订单查询接口，下单接口也同理，也许会出现新下单接口、新新下单接口、新新新下单接口……也许还会出现“老下单接口”、临时下单接口等等。我们有十年左右的微服务积累，发现了很大的问题，我们积累了很多微服务，最早的到现在都没有下线，因为不知道哪个老旧项目是否还需要。公司的运维都说：你们的微服务只有上线，没有下线。它们不停膨胀，名字乱七八糟，这样的微服务又比单体好到哪里？单体是在一个代码加，部署在一个实例里，现在只是部署在不同的服务器上，让不同服务器膨胀而已，最后的结果对于我们快速的变现、很好的运维、质量保障，对整个体系没有任何好处。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/36349065547211cd61c6790a0080a7b7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/36349065547211cd61c6790a0080a7b7.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
微服务带来的是虚假的繁荣景象，链路、扩容都有问题，其实在真实业务情况下，扩容从来不是因为某一个服务器，或者某一个部署不够，拉起不够，最大的问题永远来自于链路无法更新、链路上有很多单节点问题，或者有些点就是无法扩容的。再好的微服务与基础设施一样无法扩容。这样的麻烦点带来一个问题，在现有的微服务体系或单体体系，如何更高速地让你的应用成长、业务变现更快？这个情况下，我们的架构到底出了什么样的问题，所以导致我们现在不管怎么做，都快不起来？<br>
<br>总结一下，第一个是我们可不可能用一两个小时写个服务并上线？为什么不能呢？因为受制于开发过程，或受制于服务基础设施对开发过程的支持问题。第二个是研发是否需要关注每个服务器？代码同学可能不愿意想，但整个轮子是自己造的，一系列的事情都要被考虑，在DevOps里是一个很大的问题。因为这两点，整个需求的前置条件就越来越多。再下来，开发人员可以像操作IDE那样完成他不熟悉的技能吗？如果一直用同一种编程语言可能没问题，但如果没有很好的培训体系，或没有单一的技术架构体系下，这也是一个麻烦点，我们真的有那么多全栈工程师吗？接着是运维智能化，今天我们看到的运维都是人在运维，是真的“人工”智能。这些加起来，尤其是第一第二点，是我们最大的“坑点”所在。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/7db7063f45b6c84545a6e10af1cff5dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/7db7063f45b6c84545a6e10af1cff5dc.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
程序员可以安静地写代码吗？今天的程序员真正写程序的时候，真的很痛苦。左边的框架是JAVA的，有一系列的问题，正好是在阻止程序员的变现速度，在写每一行代码的时候需要考虑的太多了：各种组件怎么用，各种规则怎么办，各种配置在哪里，各种工程结构在哪里？其实很多业务代码很少，但根本没有办法快速上线。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/f033614fe9958bd7477923daf5bef211.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/f033614fe9958bd7477923daf5bef211.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
那我们程序员真的幸福吗？其实很多情况下，我们程序员叫重构，每个程序员在工作时，听到最多的一句话就是我们需要再迭代一下，迭代一下就是代码需要重做一下，或者重写了。为什么会出现这样的问题？因为我们的业务逻辑不够纯粹，或者业务逻辑纯粹之后独立部署的比较少，都是互相关联的状态。当业务逻辑不够独立或者设计不太完美的情况下，我们试图做成完美服务体系的时候，一个业务点发生变化会带来一系列变化，导致的问题是大量重构和重写。我想在这里引出 Serverless 的一个点，<strong>既然我们避免不了重构，也避免不了业务变化，业务确实一直在变化，重构一直在发生，不如让我们更加开心地、更爽地去重构、去变化</strong>。既然我们的代码用了一段时间一定会变成没用的，那就让它自然死亡，不要变成僵尸，这也是触发我们去做 Serverless 的一个点，让我们代码转换速度变得更快，让我们废弃代码或者重新做成代码成本越来越低，我重新做它的时候并没有让整个工程都去重构，这样的事情实现的时候，也让我们的代码业务逻辑片断不停地被重新迭代。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/5ff683c8d0782a5e6cae4fa6e5454fae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/5ff683c8d0782a5e6cae4fa6e5454fae.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>为什么要做 Serverless 架构？</h3>剩下的就是刚才说的<strong>各种环境依赖，这也是我们做 Serverless 很大的点</strong>。整个环境依赖状态下，我们一直忽略了生产中一个很大的问题——整个开发过程。这件事情其实被我们所有架构师忽略，或者大部分技术分享的时候也很少提及。大部分时间下，我们一直在集中生产，怎么让生产更稳定，怎么做故障的转移、自愈，怎么做弹性、扩容，却很少想到我们怎么更舒服地开发、写代码。因为任何一个架构做出来，一定要从写代码、调试、测试开始，但我们回头看看今天的开发测试过程，如果把整个框架的可扩展性、整个架构可扩展性排除外，今天开发过程是不如单体状态下的，因为太麻烦了。本来我自己本地就可以跑起来的代码不得不依赖一个开发环境，本来很容易做的测试的状态不得不依赖测试环境，而测试环境又互相依赖和冲突，以至于测试没有办法真正把环境更好地测试。如果把这些都隔离出来，每个程序员、每个开发、每个测试都有完整独立的环境，可以解决这个环境，但是可以想象这个成本会有多大，而且要保证这个环境的代码是同步的？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/df497ea58271a175e244ed94c6c78285.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/df497ea58271a175e244ed94c6c78285.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
紧接着的运维部署也极其恐怖，现在很多公司一直在说DevOps，但真正情况下我们运维和开发是分离的，这个分离不是人的分离，<strong>人在哪个组织架构并不重要，重要的是人看事物的角度是否一致</strong>，很多情况下运维和研发是不一致的角度，运维看到的是一个个铁壳服务器，研发同学看到的是一行行代码，两者之间没有很好的共同的视角，导致很多问题是Dev和Ops分开的状态。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/f3700b174dfb35e1910b2a105167a384.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/f3700b174dfb35e1910b2a105167a384.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这件事情在 Serverless 角度也是这个状态。在 Serverless 眼中，就是硬币的两个面，如果我们把基础研发和业务系的研发看成两个面，代表了不同的角度。我们先来看基础系的同学，今天很多 Serverless 框架或者 Serverless 工具都是基于相同的理念做出来的，大量的工程师是基础架构研发团队出身，我也是这样，三年前一直在从事基础架构，从基础架构程序员到架构师再到CTO，所以在基础架构同学眼里，永恒的一件事情是什么？我做的这个东西在没有出问题的时候，在向别人介绍的时候，都是银弹，你用我的能解决所有问题，包治百病！等到故障出现的时候就说你们用错了，我不是银弹！从基础架构同学眼里看业务同学，永远是CRUD，“云程序弹性工作我已经完成了，不是可以快速拉起吗？”如果转化到业务的视角，个人经历来说，正好这三年我做业务去了，我刚到业务团队时想：这不是很简单吗？指挥几百个基础架构的人都这么轻松，指挥上千个业务同学更简单。其实不是这样的，业务更注重的是模型。<strong>业务模型的变化带来程序的变化，也就是，让自己试图变成运营和产品</strong>。再下来业务逻辑代码是不是一定的？如果找不到对应代码，未来维护非常麻烦，某个业务点的改动一定会针对代码，中间出现断层就麻烦了。工程进度也越快越好，因为所有人都催你赶紧上线。一条 SQL 到一个服务的距离到底有多远？一个代码脚本能不能就是一个微服务？如果重构是天性，能不能让重构变得廉价？<strong>今天 Serverless 就在完成这几件事，更轻地做服务，让重构变得更廉价</strong>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/ffc80bacc7f1f5b5dd90af508795e708.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/ffc80bacc7f1f5b5dd90af508795e708.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果基于 Serverless 架构，从研发人员的角度看，整个编码过程到线上过程其实是比较完整的闭环状态。这是我们当年自己做平台的时候，梳理出的每一个脚本联系的关系。还有整个编程过程，SDK 是不是可以做得更好，面向无服务状态？比如我们去数据库拉下数据也好，是不是能把类似于 SQL 的传统写法去掉？既然是无服务器架构，开发过程为什么还要面向服务器，还要问“我的 DB 服务器在哪里”，完全可以把它变成一个对象。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/804d1c2a7472f7aaa9c17187b0f5606e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/804d1c2a7472f7aaa9c17187b0f5606e.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后还有整个 Gateway 弹性扩容的能力和云化 IDE。这些事情是我们当时第一个就去做的，甚至比框架还要早，我们想解决的是开发效率的问题，云化IDE让大家通过浏览器就可以编程。这件事其实一开始是极其失败的，所有编程的同学都说，工具在你这里都变成私有的状态了。但我们尝试至今，整个 Serverless 还是不错的，它最好的状态是节省了大量开发的效率问题，当然真正的开发过程没有那么多，还要写代码，但开发周边的事都被省下来了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/a23f4f97d4129669e447183d4bd65209.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/a23f4f97d4129669e447183d4bd65209.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们是比较多栈的，现在前端所有东西的中间层全部在 Serverless 上；另外还有很轻的服务，在服务过程中很多情况下会面临一个问题，当服务很轻的时候，几百上千行代码就能解决，这些我们都放在 Serverless 平台上处理，可以快速增删；还有弹性极致的问题，每次实时计算的节点会有很多，每个人搜索的时候计算的数据量都是不一样的，我们就用了大量计算脚本跑在 Serverless 平台上。这是我们整个 Serverless 平台的结构，不可变的、重的沉淀在微服务体系，在这个基础上再通过事件触发，联动整个 Serverless 平台的脚本，我们低代码平台也是这样的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/27960c19cfc401c628ed2152a6da06f8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/27960c19cfc401c628ed2152a6da06f8.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后，<strong>Serverless 核心的价值一定不是省下那几台服务器的钱，更多是整个变现速度的提升</strong>。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/9y3g4PQYSjlnRPJWYFbyjg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/9y3g4PQYSjlnRPJWYFbyjg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            