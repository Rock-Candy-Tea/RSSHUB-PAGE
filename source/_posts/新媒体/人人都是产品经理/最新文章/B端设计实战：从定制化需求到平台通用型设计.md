
---
title: 'B端设计实战：从定制化需求到平台通用型设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/WSiVfJm0DOhXqgeRaMnB.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 10 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/WSiVfJm0DOhXqgeRaMnB.jpg'
---

<div>   
<blockquote><p>编辑导语：随着平台业务的逐渐增多，需要对其进行定制化的需求设计，业务需求多样性与平台能力统一性的矛盾该如何解决？本文就该矛盾展开分析，并提出解决的相应措施，确保平台实现了通用一致的设计目的，一起来看下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5131331 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/WSiVfJm0DOhXqgeRaMnB.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、平台提效设计的矛盾点</h2>
<p>在开始阐述本次专题之前，我想先简单介绍下我们的平台业务背景，随着字节教育前台业务的不断增多，前台业务对题目、图片、试卷等资源的需求量也越来越大，为了避免重复生产造成的资源浪费，题库中台生产能力应运而生，我们通过招募Freelancer或签约供应商，来为各业务线提供教育资源的生产服务，因此对内部我们也通常称呼为生产平台。</p>
<p>下图是我们的任务广场页，我们可以看到界面内罗列展示着各种各样的任务，这些任务通常会由不同业务根据需求进行投放展示，从而供生产员们自由领取进行生产。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/3cxfdqsaaOlfeEU8fi6y.png" alt width="600" height="1080" referrerpolicy="no-referrer"></p>
<p>作为一个B端生产平台，平台定位决定我们要服务多业务，多业务必然会产生复杂多变的业务场景，从而衍生出多样化的定制需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/sMykUCg0Wz2x2ig5wtMv.png" alt width="600" height="1080" referrerpolicy="no-referrer"></p>
<p>随着接入生产平台的业务不断增多，我们发现了一个日趋显著的问题，以同一个补答案的任务能力为例，我们会接收到3个存在差异的业务定制需求：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/zSaTISOugfmFK7LoZKrQ.png" alt width="600" height="861" referrerpolicy="no-referrer"></p>
<p>德国哲学家莱布尼茨曾说过：“世上没有两片完全相同的树叶。”</p>
<p>我今天也想说：“中台没有两个可直接复用的业务需求。”</p>
<p>从上面的业务需求例子中，我们可以发现不同业务对平台能力的特性存在显著差异化的诉求，而每次业务需求一旦出现新的定制点，就意味着要重新走一遍研发排期流程，即便走最敏捷的研发测试流程也需要1周时间，这对业务而言非常的不友善，下游的设计、前端、后端、测试也不得不在各个业务的定制需求中疲于奔命，逐渐背离了平台快捷高效的初衷。</p>
<p>为了解决这个问题，平台项目组内部进行反复探讨，我们回归到了一种经典的哲学思辨：</p>
<p>业务需求多样性与平台能力统一性的矛盾该如何解决？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/2bzhCzIhvpLNPZWBeP4M.png" alt width="600" height="1080" referrerpolicy="no-referrer"></p>
<p>为了解决这个矛盾，我们尝试过一些不靠谱的方法：</p>
<ul>
<li>我们对业务妥协过，通过拉代码分支的方式为业务支持各类定制逻辑，让平台能力变得冗杂且不通用，最终导致平台的维护成本急剧上升；</li>
<li>我们对业务强硬过，希望通过说明书或培训让业务先了解我们的平台能力规则，再提出符合规则的需求，但收效甚微，也让业务开始质疑平台的服务能力。</li>
</ul>
<p>通过各种踩坑后，最终我们达成了一个共识：</p>
<ul>
<li>首先，业务需求一定是多样化的，这是业务背景差异性所决定的客观现实；</li>
<li>其次，平台能力必须是统一的，这是基本原则，否则平台将不再是平台；</li>
<li>最后，二者看似冲突但并非不可调和，辩证哲学针对这个话题已经给出了解答，只要我们能够抓住业务需求多样性的共性特征，我们就找到通用化设计的钥匙。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/6VaqBM1nThvjyY06lfn3.png" alt width="600" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、从矛盾到通用的切入点</h2>
<p>在开展设计前，我们需要明确下当前的设计现状和设计原则：</p>
<p>作为B端生产平台的设计师，我们需要：</p>
<ol>
<li>为解决多业务的生产问题而设计；</li>
<li>为维持平台能力的通用性而设计；</li>
<li>面临复杂的业务场景和平台逻辑，必须关注能力抽象、角色、权限等问题。</li>
</ol>
<p>为此我们的设计方案，需要契合以下2点原则：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/XIhST2D1nzHf0KHQwlB7.png" alt width="600" height="681" referrerpolicy="no-referrer"></p>
<h3>1. 基于通用场景抽象共性特征</h3>
<p>为了确保设计能够通用一致，我们首先基于多个业务针对平台任务提出的定制需求，归纳了一个通用需求场景：</p>
<p>关键目的是契合业务特点，表现诉求是对平台任务进行定制。</p>
<p>基于以上假设，我们重新梳理关键目的（业务特点），发现不同的业务背景间包含多个同类的业务属性，我们可以将其抽象归纳为关键目的的共性特征。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/F9Vwe1wpqx5qIf1rICB6.png" alt width="636" height="260" referrerpolicy="no-referrer"></p>
<p>我们继续梳理表现诉求（定制任务），发现不同的业务定制需求中包含多个同类的任务特性，我们可以将其抽象归纳为表现诉求的共性特征。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/2NqyNCgL93plr2z59h0N.png" alt width="718" height="305" referrerpolicy="no-referrer"></p>
<p>通过抽象共性特性，我们可以将通用场景转化为明确的设计机会点，业务属性成为通用条件，任务特性成为通用结果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/fUu1hA9UrYPhOFCh6WQX.png" alt width="600" height="997" referrerpolicy="no-referrer"></p>
<h3>2. 将共性特征转化为平台能力</h3>
<p>将通用业务属性录入至平台内，并为其内置常用的变量值，形成平台配置能力的基础条件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Ttt9KaYiMKYJz4tb95Ic.png" alt width="600" height="830" referrerpolicy="no-referrer"></p>
<p>如果业务认为我们抽象的业务属性不够或过多，我们依然支持业务在项目权限内对业务属性和变量值进行增删修改，而我们提前基于业务权限做了项目数据分隔，所有变更仅在单一业务数据内生效，不会影响到其他业务的属性及变量值数据。</p>
<p>这些业务属性将成为平台的通用能力，用于服务更多的业务需求，达到通过配置设计实现定制效果的目的。</p>
<h3>3. 用平台配置设计实现定制</h3>
<p>根据“不同业务属性，定制不同任务特性”的场景思考进行配置设计，我们将基于业务增删修改后的业务属性作为任务配置的通用条件，任务特性则成为任务配置的通用配置项。</p>
<p>通过切换业务属性条件实现匹配业务背景的对应目的，基于业务属性条件可以实现配置更多定制的任务特性，而每次的规则配置将不再需要重复走研发流程，极大的提升了业务体验，同时也帮助设计产研从重复性劳作中释放，给予我们更多时间来进一步丰富和优化平台体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/YR5SE4xwCOsamIdHUdYD.png" alt width="600" height="880" referrerpolicy="no-referrer"></p>
<p>整个配置设计对业务而言，默认条件对应业务背景的关键目的，而配置项则对应业务的表现诉求，从心理模型上匹配了业务的需求逻辑，实现了清晰高效的设计目标；</p>
<p>对平台而言，将定制点中的共性特性进平台能力通用化，确保平台配置的最大兼容性和复用性，实现了通用一致的设计目的。</p>
<p>通过以上方法，我们将业务配置流程平均耗时从研发流程10天降低至手动配置1天，整体流程提效90%以上。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/ZqEaWGHiwETwByQEFzYZ.png" alt width="600" height="556" referrerpolicy="no-referrer"></p>
<h3>#专栏作家#</h3>
<p>愚者秦，微信公众号：feather-wit，人人都是产品经理专栏作家。先后任职于爱奇艺、字节跳动的一枚体验设计师，同时是兼职写小说的斜杠青年，善于总结和抽象设计方法，热衷于探索不同用户场景下的产品策略。</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5128685" data-author="86856" data-avatar="http://image.woshipm.com/wp-files/2018/10/kvMfyGYHdrCviAUcOssl.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            