
---
title: 'Part 2 如何进行埋点（内附埋点文档模板）'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/6e2c7129eefdb1f648ee2e7fadabf737-picture'
author: PMCAFF
comments: false
date: Tue, 15 Jun 2021 15:04:29 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/6e2c7129eefdb1f648ee2e7fadabf737-picture'
---

<div>   
<pre><style>
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
</style><p>在上一篇文章，我们已经介绍了什么是埋点，以及如何选择具体埋点方式、位置。具体可点击查看 《<a href="https://coffee.pmcaff.com/article/2892981602240640/pmcaff?utm_source=forum&newwindow=1" target="_blank" rel="noreferrer noopener">什么是埋点？</a>》</p><p>埋点的前期知识背景了解的差不多了，接下来需要怎么拆解出埋点的需求，输出可行性方案给到开发呢？这篇文章，将会拆解6个步骤给到大家参考，还是那句话，具体的实施需要根据实际情况进行调整。这里说的不一定全对，但思路是可以参考的。废话不多说，请继续接着往下看吧。</p><h1>第一步：需求收集分析</h1><p>做埋点需求的第一步，是要理解埋点的具体价值和需求场景。我们要对需求进行梳理。首先要明确我们要分析什么样的场景，解决什么业务问题，要解决这个业务问题，要看什么样的数据，所以明确清晰产品的脉络和架构是关键。这里需要输出【产品信息结构图】【产品功能结构图】</p><p>有了基础的梳理后，我们需要再将核心业务流程或页面流程梳理出来。将用户与系统的交互故事完整的梳理出来。这些都是决定了用户在使用产品时的任务路径，借助它，可以知道流程中的潜在地雷是什么，哪里的效率比较低，有助于全局化思考。后续我们就可以在每个流程步骤，考虑好用户的目的、场景，提炼出重要指标。这里需要输出【核心业务流程图】</p><p>其实这里说的几个流程图，我们前期做别的需求分析时候可能梳理过了，也可以复盘一下即可。这里主要目的是了解需求背景目的，方便接下来的指标拆解。</p><p>【案例分享】</p><p>背景：</p><p>我们做的产品是在线旅游产品预订平台，目前公司在组织架构调整的大背景下，为了跟公司其他业务部门整合，我们不再侧重点在app上，改为H5端，所以之前的业务需要迁移到H5上面，埋点需要重新埋。</p><p>根据步骤一，我们拆解出【产品信息结构图】【产品功能结构图】【核心业务流程图】</p><p>1.1【产品功能结构图】</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/6e2c7129eefdb1f648ee2e7fadabf737-picture" alt="6e2c7129eefdb1f648ee2e7fadabf737-picture" coffee-w="1080px" coffee-h="779px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>1.2【产品信息结构图】</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/9fc01de817b2ae68d5c4cb2c4368126e-picture" alt="9fc01de817b2ae68d5c4cb2c4368126e-picture" coffee-w="1080px" coffee-h="564px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>1.3【核心业务流程图】</p><p>我们的核心业务流程，就是酒店的预订流程：</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/c50fb7a2d2fd7e43e211f0c81e1be90a-picture" alt="c50fb7a2d2fd7e43e211f0c81e1be90a-picture" coffee-w="919px" coffee-h="3405px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><h1>第二步：设计指标</h1><p>不同的业务角色关注不同的数据指标。例如产品、运营关心的指标是不一样的。在设计指标的时候，我们可以从两方面入手，一来需要关注这些不同角色的不同角度指标。二来可以根据产品流程设计指标。</p><p>【根据不同角色设计指标】</p><p>产品关注的指标场景：</p><p>功能优化前，需要参考每个功能的使用情况，用户偏好，用户来到了你的产品，第一件事情是做什么，然后还会做什么，还有哪些更深层次的需求。</p><p>新功能上线后，新功能是否得到用户的使用与认可？有没有因为交互体验功能按钮的设计而导致无效点击增多？产品是否更加聚焦的解决了用户的痛点？用户在哪个关键节点发生了流失？</p><p>运营关注的指标场景：</p><p>分用户运营、活动运营、策略运营、商家运营等类型，关注的数据各有侧重点，以活动运营为例，一次完整的活动运营，在工作的前中后阶段，对数据的需求情况。</p><p>例如活动运营的需求场景：</p><p>活动前，需要了解面向用户群体，确定活动入口的引导、布局以及内容。</p><p>活动中，对数据的时效性要求更高，需要了解活动进行的效果如何，必要的时候根据数据反馈及时调整问题和优化。</p><p>活动后，更加注重反馈和总结，对活动的复盘；本次活动的带来了多少的访问流量，转化率如何，不同渠道过来的用户表现如何，最终这些用户转化成活跃用户的又有多少？</p><p>那么根据场景拆解下来关注的指标有：</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/d46e3f585cfb28624ff2f80f8112ace7-picture" alt="d46e3f585cfb28624ff2f80f8112ace7-picture" coffee-w="1080px" coffee-h="524px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>【根据产品流程设计指标】</p><p>我们还可以根据产品的功能流程或者页面结构，定义好分析的目的，剥离关键流程，提炼关键指标。</p><p>【案例分享】</p><p>根据上述的步骤，以酒店预订转化率这个指标来作为我们最终想要看到的数据，根据产品流程设计指标角度来看。我们可以从预订酒店业务上的关键流程入手。具体如下：</p><p>酒店详情>立即预订>确认订单>支付>支付结果</p><p>在这个过程中，需要采集到从酒店详情页到提交订单页的转化，从订单提交页到订单支付的转化，支付页到支付结果之间的转化情况，也就是页面转化率。</p><p>那么对应的可以拆解成指标事件为详情页UV、订单预订事件、订单确认提交事件、支付事件、支付成功反馈事件。</p><h1>第三步：定义事件</h1><p>知道了要看什么指标，接下来就是定义事件。那什么是事件呢？例如：在登录中，填写完信息后，点击一下“登录”按钮，或者点酒店的“预订”按钮，页面流程的“下一步”按钮，获取到“登录成功”，访问某个页面，这些触发的行为都可以理解为一个事件。</p><p>这里简单说几个名词的定义：</p><p>事件指的是可以被记录到的操作和行为</p><p>属性就是对于一个对象进行刻画的维度</p><p>属性值是定义属性的特征或参数</p><p>举个例子：买一件衬衫，这是一个事件，那么属性的化，就是衬衫的大小、衬衫的颜色；属性值就是：SML、红黑白。</p><p>上面是简单的描述一个事件、属性、属性值的含义。那么我们真正定义一个埋点的事件，可以从4W1H维度考虑：包括Who、When、Where、How、What，</p><p>即：某个用户在某个时间点、某个地方以某种方式完成了某个具体的事情。</p><p>【案例分享】</p><p>以下是根据订单预订事件、订单确认提交事件罗列的事件、属性、属性值</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/95a259efb679c32538e42a80368449cc-picture" alt="95a259efb679c32538e42a80368449cc-picture" coffee-w="1080px" coffee-h="463px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><h1>第四步：撰写文档</h1><p>接下来就是编写文档了，其实就是把上面的事件、属性、属性值等维护。</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/54108295491b2138ae22ebd76bae1301-picture" alt="54108295491b2138ae22ebd76bae1301-picture" coffee-w="1080px" coffee-h="51px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/1c9f2e31339adf359fa91d08c307afee-picture" alt="1c9f2e31339adf359fa91d08c307afee-picture" coffee-w="410px" coffee-h="98px" coffee-format="jpeg" referrerpolicy="no-referrer"></p><p>其中状态是为了后续可以维护表格</p><p>正常===正常统计中</p><p>停用===最新版本无对应埋点</p><p>增加===最新版本新增埋点</p><p>变动===最新版本 UI 变动，但埋点统计维持不变；或改动了参数</p><h1>第五步：开发沟通，维护表格</h1><p>在整理完以上的表格之后，需要和其他产品、运营、开发对一下这份文档，看看是否有其他遗漏，同时，再进对应的事件参数等，对应到产品结构和流程中，看是否跑得通。</p><p>以后在维护需求文档的时候，当产品发生变化的时候，可以在状态等这些字段上管理这份表格的内容，这样一来，开发人员就会知道了。</p><p>但是记得最重要的一点，还是得跟开发沟通，正确地描述我们埋点的意义和背景。有时候开发人员也会补充和完善你的埋点需求。</p><h1>第六步：测试并验证上线</h1><p>当埋点开发完成后，需要测试看埋后想看的数据，是否可以看，是否有遗漏等，这个环节比较容易被忽视，但是这个是非常重要的环节。避免辛辛苦苦埋下的点，等到上线后，产生了一堆无效的数据，甚至会影响后续对产品的判断。测试没问题后，就可以发布上线验证了。</p><h1>结语</h1><p>到这里，我们的埋点工作基本就结束了。但是这仅仅是一个新的开始。埋点后，我们需要根据埋点统计出的数据，挖掘出价值，这才是难的。路漫漫兮其修远兮，一起加油吧。下一篇，将会介绍埋点后看什么样的数据，结合GA上面的数据进行简单的分析。</p></pre>
  
</div>
            