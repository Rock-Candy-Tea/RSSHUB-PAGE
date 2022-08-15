
---
title: 'SaaS产品设计方法论'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/318211e96d3322465396a54dee6ef5aa-picture'
author: PMCAFF
comments: false
date: Sun, 17 Apr 2022 09:20:17 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/318211e96d3322465396a54dee6ef5aa-picture'
---

<div>   
<div><style>
#articleCont &#123;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  word-wrap: break-word;
&#125;
#articleCont :first-child &#123;
  margin-top: 0 !important;
&#125;
#articleCont h1,
#articleCont h2,
#articleCont h3,
#articleCont h4,
#articleCont h5,
#articleCont h6 &#123;
  margin: 40px 0 20px;
&#125;
#articleCont h1 &#123;
  font-size: 24px;
&#125;
#articleCont h2 &#123;
  font-size: 22px;
&#125;
#articleCont h3 &#123;
  font-size: 20px;
&#125;
#articleCont h4 &#123;
  font-size: 18px;
&#125;
#articleCont h5 &#123;
  font-size: 16px;
&#125;
#articleCont i &#123;
  font-style: italic;
&#125;
#articleCont p,
#articleCont div &#123;
  word-wrap: break-word;
  margin: 14px 0;
  text-align: justify;
&#125;
#articleCont blockquote &#123;
  border-left: 6px solid #ddd;
  padding: 5px 0 5px 10px;
&#125;
#articleCont blockquote p:last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont .simditor-body blockquote :last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont a &#123;
  color: #82b64a;
&#125;
#articleCont a:visited &#123;
  color: #82b64a;
&#125;
#articleCont a:hover &#123;
  color: #74a342;
&#125;
#articleCont img &#123;
  max-width: 100%;
  height: auto;
&#125;
#articleCont hr &#123;
  margin: 19px 0;
  border: none;
  border-top: solid 1px #ddd;
&#125;
#articleCont ol &#123;
  list-style-type: decimal;
&#125;
#articleCont ol li &#123;
  list-style-type: decimal;
&#125;
#articleCont ul &#123;
  list-style-type: disc;
  padding-left: 40px;
&#125;
#articleCont ul li &#123;
  list-style-type: disc;
&#125;
#articleCont table &#123;
  width: 100%;
  font-size: 12px;
  border-collapse: collapse;
  line-height: 1.7;
&#125;
#articleCont table thead &#123;
  background: #f9f9f9;
&#125;
#articleCont table th,
#articleCont table td &#123;
  border: solid 1px #ccc;
  text-align: left;
  vertical-align: top;
  padding: 2px 4px;
  height: 30px;
  min-width: 40px;
  box-sizing: border-box;
&#125;
#articleCont pre &#123;
  white-space: pre-wrap;
&#125;
</style><p><b><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/318211e96d3322465396a54dee6ef5aa-picture" alt="318211e96d3322465396a54dee6ef5aa-picture" coffee-w="750px" coffee-h="450px" coffee-format="png" referrerpolicy="no-referrer"><br></b></p><h3><b>写在前面</b><br></h3><p style="text-align:justify;"><font>有这样一个场景</font></p><p style="text-align:justify;"><font>⽼板</font>/<font>⽤户：我有⼀个特别棒的想法，优先级很⾼，你赶紧把⽅案产做出来。</font></p><p style="text-align:justify;"><font>产品经理：保证效率！我⻢上就开始画原型，然后内部评审，接着推进开发。</font></p><p style="text-align:justify;"><font>这时候</font><font>部分</font><font>产品经理急于表现，需要将需求快速落地，第⼀反应就是开始执⾏，所以经常会发⽣⼀种情况，产品经理很努⼒的去做，把需求或想法百分百的去还原，但结果⽼板或⽤户体验完之后发现，这并不是我想要的功能</font><font>。</font><font>出现这种情况的原因是<b>产品经理没有</b></font><font><b>了解到这个需求背后的动机和⽬的</b>，这是很多⼩伙伴容易出现的问题。而</font><b>SaaS<font>产品设计，</font><font>不仅仅只</font><font>关注设计，在此之前我们更要关注产品的定义。需要我们想清楚这个需求对应的场景是什么，场景中的需求价值是什么。之后才是结构化的框架把功能设计出来。</font></b></p><p style="text-align:justify;"><b>文章整体分为以下几个部分</b><br></p><blockquote><p style="text-align:justify;">1.SaaS产品设计痛点场景拆分</p><p style="text-align:justify;">2.SaaS产品不同维度的认知</p><p style="text-align:justify;"><font>3.我们通过什么方式去理解业务</font></p><p style="text-align:justify;"><font>4.我们如何梳理业务判断需求价值</font></p><p style="text-align:justify;"><font>5.我们如何设计产品架构与功能</font></p><p style="text-align:justify;">6.SaaS产品生命周期中的设计原则</p></blockquote><hr><p><font>以下，咱们一起进入正文~</font></p><h3><b><font>1.SaaS产品设计痛点场景拆分</font></b></h3><h4><b><font>1.1.</font></b><b>SaaS</b><b><font>产品经理的工作方式</font></b></h4><p style="text-align:justify;">SaaS<font>产品经理⼯作本质是从发散到收敛的⼀个过程。发散是指产品的定义，收敛是指产品的设计。但往往很多产品经理⼀上来就开始收敛了，开始画原型，好⼀点的产品经理可能先去思考这个功能影响的范围，影响的⾯</font><font>。</font><font>最后梳理出⼀个脑图，⽤这个脑图去跟</font><font>开</font><font>发去碰，<b>但是⼀个优秀的产品经理除了⼀上来就收敛之外，</b></font><b><font>其次</font><font>需要</font><font>我们思维</font><font>先发散，</font></b><font><b>最终产品定义这个场景对应的价值是什么</b>。</font></p><h4><b><font>1.2.</font></b><b>SaaS</b><b><font>产品理解业务是进⾏需求梳理与功能设计的前提</font></b></h4><p style="text-align:justify;"><font>在这⾥在跟⼤家分享</font><font>三</font><font>个场景</font><font>：</font></p><blockquote><p style="text-align:justify;"><font><b>场景一：</b></font><font>很多同学都是半路转⾏过来做</font>SaaS<font>产品经理，往往会遇到不知道如何去跟进⾏业的趋势，同时也不知道如何去做业务调研。⽽对于业务理解的⽋缺也直接影响到对应的产出，这时候根据</font><font>对</font><font>业务</font><font>理解而设计的产</font><font>品⽅案也会被吐槽，不懂业务。这种场景我相信很多</font>SaaS<font>产品经理都会有许多感触。</font><font>【理解业务难】</font></p><p style="text-align:justify;"><font><b>场景二：</b></font><font>很多产品经理由于之前经验习惯，专注思考单个场景下的⽤户价值，在这时候会导致在思考业务场景时经常出现遗漏，</font><font>从而</font><font>导致业务⽆法闭环，终端⽤户对产品感到满意，</font><font>却</font><font>没有直接转换成付费。</font><font>【需求梳理不清晰】</font></p><p style="text-align:justify;"><font><b>场景三：</b></font><font>产品经理</font><font>进⾏了全盘梳理，理清价值之后，全身⼼投⼊产品设计中去，然⽽业务出现了⼀堆个性化需求，产品经理硬着头⽪单点设计，最后演变成定制化设计，导致产品逻辑异常复杂，研发成本也不断升⾼，终端⽤户在前端界⾯也会吐槽越来越复杂，不知道怎么⼊⼿了。</font> <font>【功能设计复杂】</font></p></blockquote><p style="text-align:justify;"><font>出现上面三种场景</font><font>情况的原因是</font>SaaS<font>产品有⾮常强的业务壁垒，所以不同⾏业产品经理会出现隔⾏如隔⼭的情况，产品设计不清楚具体场景的痛点和难点。其次是</font><b>SaaS</b><font><b>产品业务流程是⽐较复杂的，看似简单的功能也会涉及多个⻆⾊</b>，所以需要通盘考虑。最后</font>SaaS<font>产品个性化需求⾮常多，需要满⾜不同个性化需求，所以导致设计⽅案复杂。</font></p><p style="text-align:justify;"><font>所以接下来的文章也会围绕这三个场景去跟大家分享对应的产品方法论。</font></p><hr><h3><font><b>2.</b></font><b>SaaS产品不同维度的认知</b></h3><h4><b>2.1.</b><b>SaaS</b><b>产品认知的歧义</b></h4><p style="text-align:justify;"><font>很多⼈</font><font>认为</font>SaaS<font>产品是</font>toB<font>产品，</font><font>但</font><font>从本身定义软件即服务来看，即没有说是</font>toB<font>也没有说是</font>toC<font>。</font><font>而</font><font>⼴义的</font>SaaS<font>定义是既有</font>toB<font>也有</font>toC<font>（</font><font>比如</font><font>印象笔记</font>/⽯墨⽂档）。从软件交付⽅式来讲，SaaS<font>本身作为</font><font>一种</font><font>交付模式，本身不存在</font>toB<font>或</font>toC<font>之分。从商业模式来</font><font>讲</font><font>，如果我们</font><font>把</font>toB<font>产品定义为基于互联⽹提供服务，⽤以提升企业效率，增加企业收⼊的产品，那么</font>SaaS<font>产品可以算是</font>B端产品的⼀个分⽀。</p><h4><b>2.2.SaaS</b><b>产品不同维度的认知</b></h4><p style="text-align:justify;">SaaS<font>模式的出现很⼤程度上是顺应⽤户对数据安全和低维护成本的需求⽽衍⽣的。</font></p><p style="text-align:justify;"><b>SaaS</b><font><b>产品划分：</b>业务垂直型（提供⾯向特定业务的</font>SaaS<font>解决⽅案</font> <font>⽐如：</font>crm erp等）、⾏业垂直型（提供⾯向特定⾏业的SaaS<font>解决⽅案⽐如零售电商、餐饮、医疗、制造业）⾏业和业务之间肯定有交叉的，⼀个</font>SaaS<font>产品既会有特定的业务，也会⾯向特定的⾏业。</font></p><p style="text-align:justify;"><b>SaaS<font>产品特点：</font></b></p><blockquote><p style="text-align:justify;"><font>云端架构：</font>SaaS<font>公司提供服务器、数据库等硬件，⽆需本地部署；</font></p><p style="text-align:justify;"><font>成本下降：⽆需客户承担基础设施成本、⽇常运维成本，付费灵活；</font></p><p style="text-align:justify;"><font>⽤户按⽉</font>/年⽀付费⽤，⽽⾮⼀次性购买，体验提升；</p><p style="text-align:justify;">后续升级维护由SaaS<font>公司负责，通过数据驱动迭代。</font></p></blockquote><p style="text-align:justify;"><b>SaaS</b><font><b>产品业务阶段：</b>整体划分为四个阶段，基础产品完善期、⾏业产品深⼊期、⽣态建设期、再创新。</font></p><p style="text-align:justify;"><img alt="鐢绘澘.jpg" src="https://img.pmcaff.com/FgKKhoijyryq-EcP4hHaSbCnD5xQ-picture" width="1200" height="1024" coffee-w="1920px" coffee-h="1024px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></p><hr><h3><b>3.我们通过什么方式去理解业务</b><br></h3><h4><b><font>3.1.业务理解</font></b><b>=</b><b><font>行业模式（宏观）</font></b><b>+</b><b><font>企业运作流程（微观）</font></b></h4><p style="text-align:justify;"><font>对业务的理解我们可以由抽象化转换为具象化，本质需要从⾏业模式和运作流程去了解。懂⾏业模式是要能够理解约定俗成的玩法和规则是什么。懂运作流程是⾏业中某个企业不同岗位</font>/⻆⾊如何各司其职的。运作流程是⾏业模式的直观体现，⾏业模式⼜为理解运作流程提供指南针。理解⾏业的限制，了解他的客观规律从⽽避免⾛弯路，理解运作流程从⽽能够还原场景，并设计功能满⾜需求。所以我们需要通过⾏业分析了解⾏业模式，通过业务调研了解某个企业的运作流程。</p><p style="text-align:justify;"><font><b>⾏业模式：</b>从宏观⻆度，我们了解⾏业内企业相应业务的玩法，从⽽抽象出通⽤的玩法和规则，这样我们才可以了解企业的核⼼痛点，其次也为SaaS<font>产品及</font></font><font>服务提供⽅向指南。</font></p><p style="text-align:justify;"><font><b>运作流程：</b>从微观⻆度，对于每个企业我们需要了解企业内部不同员⼯是如何操作的，最终实现公司业务运转，了解这些才能使我们产品设计更加落地。</font></p><p style="text-align:justify;"><font><img alt="4d15882789b5bafd1e11a623f871d96.jpg" src="https://img.pmcaff.com/FpRtByOhtq7JVmTJLIr4N00f2Ugc-picture" width="1200" height="1024" coffee-w="1920px" coffee-h="1024px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></font></p><h4><b><font>3.2.行业模式（宏观）</font></b><b><font>：如何快速了解一个行业</font></b></h4><p style="text-align:justify;">SaaS<font>产品经理算半个⾏业专家。</font></p><p style="text-align:justify;"><font>⽹上做⾏业分析的⽅法有很多，重要的是需要找对维度，不能只停留在⼤范围层⾯，⽽是需要聚焦于我们⾃身业务的边界。关于维度层⾯这边跟⼤家分享五个分析行业的维度，</font><font>分别是：</font><font>⾏业基础信息、外部经营环境、内部市场环境、标杆企业分析、</font>SaaS<font>竞品分析；</font></p><p style="text-align:justify;"><img alt="2780b259c25d0302cd513edb47c64f8.jpg" src="https://img.pmcaff.com/FlMuiKvr9f3kNyagw81EVl_malkS-picture" width="1200" height="700" coffee-w="1920px" coffee-h="700px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></p><p style="text-align:justify;"><font>通过上诉⼏个维度我们可以快速了解⼀个⾏业，但是往往实际</font><font>工作场景是</font><font>我们做出了⼀份分析报告，但不知道真正作⽤在哪⾥。这</font><font>种情况下</font><font>需要回归到本质</font><font>，</font><font>我们是为了了解⾏业通⽤规则和玩法，最终服务于⾃身</font>SaaS<font>业务</font><font>。</font></p><h4><b><font>3.3.企业运作流程（</font></b><b><font>微观</font></b><b><font>）</font></b><b><font>：如何进⾏业务调研</font></b></h4><p style="text-align:justify;"><font>先跟⼤家讲讲</font>C端产品的⽤户调研与SaaS<font>产品业务调研的区别，</font>C端⽤户调研只需要关注单点⽤户，SaaS<font>业务调研需要全盘考虑整个业务流程，这也是很多转⾏做</font>SaaS<font>产品经理会按照以前的调研⽅式，去做业务调研，容易导致产品流程上没有闭环。其次</font>C端⽤户调研需要以⽤户体验为中⼼，相对于来说SaaS<font>产品更关注需求，解决了什么业务问题。最后</font>C端产品⽤户需求层⾯相对于容易抽离共性，SaaS<font>天然存在⼤量个性化需求且极度分散。</font><font>而且</font>C端产品⼀般都是⽤户可以通过共情来挖掘潜在需求，SaaS<font>产品经理通常不是⽤户，需要通过理解业务来挖掘需求。</font></p><h4><b><font>3.4.运作流程要素与调研步骤</font></b></h4><p style="text-align:justify;"><font>业务调研最终是为了理解业务的运作流程，运作流程包括的元素有什么：企业（通过定义标杆企业描绘客户画像）、⻆⾊（通过查看组织架构和参考同类型企业来梳理⻆⾊特征）、流程（通过观察与调研了解核⼼业务的⼯作流）。</font></p><p style="text-align:justify;"><font>业务调研整体分三步：</font></p><p style="text-align:justify;"><font><img alt="鐢绘澘澶囦唤 3.jpg" src="https://img.pmcaff.com/Ft3eMld-NAnLcM9BX-iQHLkwX8rf-picture" width="1200" height="500" coffee-w="1920px" coffee-h="500px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></font></p><p style="text-align:justify;"><font><b><i>第⼀：定义并选择标杆企业。</i></b>在这⾥需要定义标杆企业的客户画像，以标杆企业的需求为核⼼。客户画像包含（客户</font>/企业规模、从属细分类⽬、业务范围），在这⾥为什么我们需要选择标杆企业的原因是在于标杆企业需求具有代表性，相对容易抽离。其次也是因为标杆企业的声⾳有影响⼒，后期能够引领其他客户。</p><p style="text-align:justify;"><font><b><i>第⼆：梳理业务链条的⻆⾊。</i></b>在这⼀步梳理好业务流程中的关键⻆⾊之后，我们需要定义⻆⾊的特征（主要负责什么、业务⽬标</font>/KPI是什么、职业特点是什么），怎么找到这些业务流程中的关键⻆⾊，第⼀可以从企业的组织架构中寻找，这是最便捷也是最直接快速的⽅法。在得不到组织架构的情况下，可以参考同类型企业的流程及⻆⾊（当然这⾥的企业也是属于标杆企业），在做整体⻆⾊梳理的时候我们必须要注意业务的闭环，如果忽略了业务链条不重要的⻆⾊，可能会导致业务⽆法闭环。</p><p style="text-align:justify;"><font><b><i>第三：观察与调研并⾏。</i></b>在梳理完业务流程之后我们需要通过观察与调研，理清⻆⾊的⼯作流（核⼼流程）。对于</font>SaaS<font>产品来说，观察⽐直接开放式调研更有效，这么说的原因是在于产品很难从根上去撼动绝⼤部分公司的业务模式，所以我们侧重在还原业务，⽽⾮创造业务，还有⼀个原因是调研过程中多少都会有主观成分在，所以需要通过观察还原业务。观察的⽅式我们可以通过驻场，深⼊业务需求⽅的⼯作场景，观察他们平时的⼯作⽅式。在观察的同时我们也需要得到这个⻆⾊的⼯作流是什么样⼦的？有没有标准化流程？在什么情况下，执⾏了那系列任务，完成了什么业务上的⽬标？还有⼀种⽅式轮岗机制，有机会的话能够直接上⼿体验业务⽅的⼯作是最好的。⽤户调研主要从流程维度和具体场景维度去设计调研问题。</font></p><p style="text-align:justify;"><font>在理解业务这个层⾯上我们需要循序渐进的，<b>理解业务没有太多的技巧，通过观察和调研交叉，了解⽤户</b></font><b>/⽤户需求，并通过产品设计满⾜需求，了解反馈，进⽽根据反馈持续满⾜需求----<font>通过不断地这样循</font><font>环深耕业务，才能不断深化对业务的理解。</font></b></p><hr><h3><b>4.SaaS产品如何梳理业务判断需求价值</b><br></h3><p style="text-align:justify;"><font>很多产品经理在做了⼀波业务调研之后，也对业务有了⼀定程度的理解，认为接下来就该到需求分析了。其实不是这样，除了对业务要有⼀个深度了解之外，还需要还原业务中遇到的场景是什么，</font><font>用户需求</font><font>价值是什么。如何去判断需求的价值，其实本质是我们需要在产品定义这个环节去梳理清晰。</font></p><p style="text-align:justify;"><b><i><font>产品定义分</font><font>两个部分</font><font>：第⼀回归场景（梳理并描述业务场景），第⼆理清价值（判断场景中需求的价值）。</font></i></b></p><h4><b><font>4.1.为什么要回归场景？</font></b></h4><p style="text-align:justify;"><font>在这个跟</font><font>⼤家描述两个我们常⻅的⼯作场景，很多时候产品经理在提出产品⽅案时，⼤家围绕实现细节开始讨论的时候容易出现，</font>‘我觉得’的⽅式来表达⾃⼰的观点，每个⼈都有⾃⼰的想法，⽆法达成统⼀的意⻅。还有⼀种情况是在没有理解场景的情况下直接开始画原型，这时候会出现我们产品上线之后总是不符合实际线下流程，还得推倒从来。</p><p style="text-align:justify;"><font>现在我们回想</font><font>上⾯两个场景</font><font>中</font><font>为什么出现这种情况，</font><font>本质是因为产品经理</font><font>对外（项⽬组其他⼈），完成⼀项任务肯定是需要多个部⻔多个⻆⾊频繁的传递⽤户需求，因此使⽤⼀套易理解，贴近实际的沟通的⽅式就很重要，⽽场景就是通⾏于不同⻆⾊之间解决产品问题的语⾔。</font></p><p style="text-align:justify;"><font>对内</font> <font>（⾃身思考）产品设计我们需要先发散后收敛，因此动⼿画原型，写⽂档之前我们需要做⼤量的思考，调研。逻辑基点是⽤户⾯临的实际情况到底是什么样的，即回归场景。</font></p><h4><b><font>4.2.单个场景与多个场景</font></b></h4><p style="text-align:justify;"><font>在单个场景上，</font>SaaS<font>产品不能创造，只能还原。这也是和</font>C端的区别点，C端因为⾃⼰就是⽤户，可以以发散的⽅式创造场景，从⽽引领⽤户需求。SaaS<font>业务天然存在壁垒，⽆法发散获取，只能还原场景，且颗粒度需要更细。在多个场景上，</font>SaaS<font>产品需要考虑业务的闭环。同样以</font>C端举例，c端产品相对简单，重点在于单点突破核⼼场景。SaaS<font>产品业务链⻓，缺少任何⼀个必备场景都可能⽆法闭环。所以回归场景我们需要先将单个场景描述清晰，进⽽梳理链条中的全场景。</font></p><h4><b><font>4.3.场景我们该如何去描述</font></b></h4><p style="text-align:justify;"><font>回归场景我们需要通过⼀种通⽤的场景描述⽅式，对内形成自己的思考基点，对外让⼤家形成共识。在这里跟⼤家分享⼀种场景描述⽅法，场景描述的</font>7要素（⽤户、环境、时机、⽬标、动作、截⽌、任务）SaaS<font>产品的场景是真实存在的，不是凭空捏造的。需要在真实业务中得到验证。场景描述⽅式本身不重要。重要的是对外能够形成统⼀的认知，对内思考能够还原⽤户实际情况才是关键。</font></p><p style="text-align:justify;"><font><img alt="鐢绘澘澶囦唤 4.jpg" src="https://img.pmcaff.com/FqGAuc2I-GOEwTpVZVlTuLN_jCEt-picture" width="1200" height="1080" coffee-w="1920px" coffee-h="1080px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></font></p><p style="text-align:justify;"><font>针对单⼀的场景我们可以通过单⼀场景描述⽅式去还原，针对多个场景时我们可以借助场景需求清单，场景需求清单是多个场景串联形成的结构化信息，他是⼀个业务链条下的场景拆分后的需求集合，场景需求清单可以帮助我们梳理业务链条下的场景关系，避免遗漏影响业务闭环的场景。基于之前的调研，找到关联步骤</font>/流程，根据流程还原每个流程下的代表性场景，并拆解出需求。<b>核⼼步骤提炼成三步：第⼀梳理出清晰地业务流程、第⼆将场景归类到流程中、第三基于场景拆分⽤户需求；需要注意的是每个流程下可以写多个具有代表性的分⽀场景，同时我们也可以把⻆⾊标注出来。</b></p><p style="text-align:justify;"><b>示例：场景需求清单</b></p><p style="text-align:justify;"><img alt="f096ca83797f71952658738318f73dc.png" src="https://img.pmcaff.com/FiKhlqOE38OiWfm4R7Q9C2_ADIOx-picture" width="831" height="153" coffee-w="831px" coffee-h="153px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:justify;"><font>当场景清单⾜够庞⼤时，我们需要对原有的场景需求清单进⾏抽离，抽离出最关键的类别</font>/流程，以及其中不可或缺的场景形成场景需求清单，这⼀步的核⼼在于如何抽离（需求理解业务），说到核⼼场景我们需要前⾯提到的业务闭环，业务闭环我们可以定义他为为了完成⽬标下的最⼩步骤的集合，核⼼场景即最⼩步骤的展开，对于最⼩步骤依赖于对业务的理解，需要站在业务员的角度，来看哪些是不可或缺的，同时我们需要考虑到意外情况下的分⽀场景，如果出现意外情况⽽导致业务⽆法进⾏，业务⽆法闭环，那么也会导致⽤户放弃使⽤产品。讲到这⾥我们发现核⼼场景也是MVP版本。</p><h4><b><font>4.4.宏观与微观的价值理清（理清价值）</font></b></h4><p style="text-align:justify;"><font>价值主张与需求对应的价值，两者之间产品的价值主张为判断需求的价值提供⽅向和原则，⽽不同需求价值的积累进⼀步巩固价值主张。</font></p><p style="text-align:justify;"><font><b>价值主张（宏观）：</b>为特定⽤户群体提供差异化价值，价值主张是进⾏需求判断的第⼀原则，</font>SaaS<font>产品应该尽可能满⾜每个客户的个性化需求，但不该包含与价值主张完全不⼀致的需求。如果在实际⼯作中遇到需求判断经常找不到⽅向，也许应该开始思考产品的价值主张。</font></p><p style="text-align:justify;"><font><b>需求价值（微观）：</b>需求的两种价值⼀是⽤户价值（给产品⽤户带来什么），另外⼀种是商业价值（给</font>SaaS<font>⼚商带来什么），针对⽤户（我们提供业务闭环类价值、效⽤类价值、体验类价值）、对于</font>SaaS<font>⼚商（收⼊价值、对⾃身是否能够采集到更多的业务数据价值）。在</font>SaaS<font>产品中⽤户价值中最常⻅的是效⽤价值。</font></p><p style="text-align:justify;"><font><img alt="鐢绘澘澶囦唤 6.jpg" src="https://img.pmcaff.com/FnXOpYlh7TcbIqD_NTlYhtCAr8kw-picture" width="1200" height="1080" coffee-w="1920px" coffee-h="1080px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></font></p><h4><b><font>4.5.如何找出场景中的需求价值</font></b></h4><p style="text-align:justify;"><font>找出价值我们需要做的三件事：第⼀需求的⽤户价值是否与产品价值主张相契合？第⼆⽤户的需求价值具体类型是什么，表现在哪⾥？第三需求是否存在商业价值，表现在哪⾥？</font></p><h4><b><font>4.5.如何判断场景中的需求价值</font></b></h4><p style="text-align:justify;"><font>需求来源于场景，满⾜需求则产⽣价值，⾯对扑⾯⽽来的需求</font>SaaS<font>产品经理更需要清晰理解并判断需求的价值。</font>SaaS<font>产品为什么更需要理解价值，原因在于</font>SaaS<font>场景都是真实存在的，客户就是上帝，不存在伪需求，所以需要对⼤量需求进⾏判断</font><font>。在需求判断中常规会出现三种场景分别是：</font></p><p style="text-align:justify;"><img alt="06b12017a6b4eb7f759709356307fd4.jpg" src="https://img.pmcaff.com/Fgg_xFktFJ9WjOfy7zXXm3nQCCEL-picture" width="1200" height="640" coffee-w="1920px" coffee-h="640px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p style="text-align:justify;"><b>示例：场景需求价值清单</b><br></p><p style="text-align:justify;"><img alt="618700a73ed703cc2ac639f961fe209.png" src="https://img.pmcaff.com/FlZFjA2NyhzOpfN9N3Gaz9H4EszH-picture" width="830" height="154" coffee-w="830px" coffee-h="154px" coffee-format="png" referrerpolicy="no-referrer"><br></p><hr><h3><b><font>5.我们如何设计业务架构与功能<br></font></b></h3><p style="text-align:justify;"><b><font>5.1.什么是业务架构</font></b></p><p style="text-align:justify;">对于SaaS<font>产品首先我们理解</font><font>场景七要素中的任何⼀个要素发⽣变化，都会导致场景不⼀样，从⽽产⽣不⼀样的需求。</font>SaaS<font>产品有⾮常强的业务属性，如果<b>缺乏框架性思考，单点设计功能将会让你精疲⼒尽，对内部来说不断堆砌功能，开发成本会越来越⾼</b>，对外部来说⽤户看到的信息繁杂，⽆法⾼效的完成任务，所以我们设计功能前需要理清架构，以⼀种</font><font>全局</font><font>的框架视⻆来思考。<b>业务</b></font><b><font>架构</font><font>是⼀套功能依据业务进⾏分类整合，形成抽象化的业务模型，架构可以帮我们理清每个业务模块</font>/功能间的边界，以及他们之间的关系</b>，在我们⾯对多个类似的需求时先梳理架构就可以基于场景迅速定位到对应的模块，在设计功能时我们需要重点考虑以⼀个功能满⾜多个类似的需求。</p><p style="text-align:justify;"><img alt="鐢绘澘澶囦唤 5.jpg" src="https://img.pmcaff.com/FkHdnxAijYhhM4hP1eY3b8T4KEXN-picture" width="1200" height="1080" coffee-w="1920px" coffee-h="1080px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></p><p style="text-align:justify;"><font>业务架构：架构的作⽤在于建⽴⼀套标准化的业务模型，搭建框架，最终是为了⾼效满⾜⽤户的不同需求。所以也就是我们常听说的<b><i>后端标准化，前端个性化</i></b>。理解业务是梳理功能架构的前提</font><font>。</font></p><p style="text-align:justify;"><font><b>示例：微信业务架构</b></font></p><p style="text-align:justify;"><font><img alt="61fea7782d0714893fb09a745973001.png" src="https://img.pmcaff.com/FnRpju0ldsD86NzoS5T5RCWcjmKd-picture" width="743" height="339" coffee-w="743px" coffee-h="339px" coffee-format="png" referrerpolicy="no-referrer"><br></font></p><h4><b><font>5.2.基于目前的场景和需求我们如何梳理架构</font></b></h4><p style="text-align:justify;"><font><b>梳理架构分成三步⾛：第⼀</b></font><font><b>将</b></font><font><b>场景需求清单拆解到功能、第⼆将功能按不同维度整合、第三梳理模块之间的逻辑关系；</b>在第⼆步将功能按不同模块分类整合时我们先拿出符合通⽤模块的功能，进⾏归类整合，切记重复造轮⼦。不符合通⽤模块的功能，根据业务重要程度和复杂性单独整合。如果有必要根据业务重要程度和复杂性，继续梳理⼦模块。在梳理模块之间的逻辑关系时我们<b>先梳理静态模块（不产⽣数据流），在梳理动态模块（产⽣数据流）</b>。整体表⾯上是梳理架构图，背后是对业务的深刻理解。</font></p><p style="text-align:justify;"><font>架构本质是后端业务逻辑的标准化；在完成后端标准化之后，随着产品的不断发展，我们需要通过可配置的⽅式在前端满⾜⼤量个性化需求，即前端个性化。因为</font>SaaS<font>产品本身特质，我们需要考虑到⼤量个性化需求。那么我们需要考虑如何设计⼀个功能满⾜绝⼤多数需求，核⼼我们需要运⽤可配置去解决前端个性化需求和后端业务归类。</font></p><h3><b><font>5.3.如何设计一个功能满足不同场景需求</font></b></h3><p style="text-align:justify;"><font>通过可配置化满⾜客户的个性化需求</font><font>。</font><font>⼀般会存在两种情况，第⼀是业务流程与现有⽅案差别较⼩，那我们可以从<b>功能层⾯进⾏配置</b>，第⼆是业务流程与现有⽅案差别⼤，那我们从<b>系统层⾯进⾏配置</b>。</font></p><p style="text-align:justify;"><font>在可配置层⾯⼀般来说包含界⾯布局，字段名、验证逻辑、计算规则、审批流配置，⻆⾊配置，⻆⾊功能权限配置，⽤户配置，⽤户数据权限配置等。在产品设计时需要规划好什么样的配置功能开放给客户，什么给到⾃⼰。原则上为了避免客户的复杂度，尽量开放⼩范围的配置功能给到客户⾃⼰使⽤。⾼配置往往会造成低易⽤性，配置项过多会带来⻚⾯不简洁，流程不⾼效；<b>本质上来说⽤户要的不是配置项，是低成本实现⽬标的功能。</b></font></p><p style="text-align:justify;"><font>在判断功能要不要做成配置时我们可以通过两个维度来做判断，<b>⼀个是模式切换频率，还</b></font><font><b>有⼀个则是需求的⻓尾程度（⽤户需求差异化程度）</b>，针对⼀些默认配置项判断标准我们需要回归到场景，在⼤量同⼀种类型的个性化场景中，找到最核⼼的场景，并根据场景下的功能设计设置为默认配置项。</font></p><hr><h3><b>6.SaaS产品生命周期中的设计原则</b></h3><p>通过前面的文章，我们知道了SaaS产品的方法论之后，我们也应该了解底层的设计原则，了解原则的好处有两点，通俗的来说一方面是可以驱动产品优化和产品经理本身的自我成长，另一外面则是可以消除外部给你带来的一些负面影响。</p><p><b>1.原则是自我改善的有利工具，可以在日常工作中验证我们自己的方法论，帮助自己成长；</b></p><p><b>2.有了原则，就能超脱情绪和环境的影响，自主判断选择最佳方案。</b></p><p><img alt="image.png" src="https://img.pmcaff.com/FoAO-YylmiozJ6RrcbWTxfYFxIsa-picture" width="836" height="286" coffee-w="836px" coffee-h="286px" coffee-format="png" referrerpolicy="no-referrer"><br></p><p style="text-align:justify;"> </p></div>
  
</div>
            