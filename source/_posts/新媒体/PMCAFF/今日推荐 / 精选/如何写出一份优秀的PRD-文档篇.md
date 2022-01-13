
---
title: '如何写出一份优秀的PRD-文档篇'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://img.pmcaff.com/FpcRpRDcuBLobqHXsnzxKx0KJxLq-picture'
author: PMCAFF
comments: false
date: Mon, 27 Dec 2021 10:31:13 GMT
thumbnail: 'https://img.pmcaff.com/FpcRpRDcuBLobqHXsnzxKx0KJxLq-picture'
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
</style><p>没有看如何做写PRD准备的朋友，可以跳转：</p><p><a href="https://coffee.pmcaff.com/article/3193566787991680/pmcaff?utm_source=forum&newwindow=1" target="_blank" rel="noreferrer noopener">如何写出一份优秀的PRD-准备篇</a><br></p><p>上回讲到PRD撰写前的准备工作，包括摸清PRD的目标用户的习惯，深入了解本次用户的需求，根据INVEST和MVP原则、按照业务流程做功能拆分。</p><p>本次继续讲撰写PRD的具体技巧，如何能够写出一份自己和团队都能够读懂的PRD。</p><p><img alt="PRD.png" src="https://img.pmcaff.com/FpcRpRDcuBLobqHXsnzxKx0KJxLq-picture" width="1200" height="1200" coffee-w="2280px" coffee-h="1254px" coffee-format="png" referrerpolicy="no-referrer"><br></p><p><strong>1. 通用建议</strong></p><p>写PRD有一些通用的tips，可以让你的PRD更易于阅读。</p><p><strong>1.1 提供流程图</strong></p><p>除了上传自己在准备阶段梳理的整体业务流程图，如果某些Story的功能仍然比较复杂，那么也应当梳理出流程图，帮助阅读者对story有个全面的理解。</p><p><strong>1.2 使用专业、共识词汇</strong></p><p>专业词汇可以分为IT行业通用词汇和行业词汇，需要你在工作和团队沟通中不断积累。比如：</p><ul><li><p>IT行业通用：</p><ul><li><p>行业：流量、焦点小组、UGC、PGC、OGC、KOL等。</p></li><li><p>设计：banner、按钮、滑块、输入框、单/多选等。</p></li><li><p>前端开发：JS、CSS、HTML、WEB端、移动端、URL等。</p></li><li><p>后端开发：API、数据库、SQL、解耦合、并发、同步/异步等。</p></li><li><p>测试：冒烟测试、黑/白盒测试、bug、回归测试等。</p></li><li><p>数据分析：PV、UV、visits、点击、转化率、漏斗、用户画像等。</p></li></ul></li><li><p>行业词汇：因不同行业而异。比如电商、社交、在线教育等都有各自的专业词汇。</p></li></ul><p>共识词汇：指的是团队合作中大家常用的沟通用语。很多大厂的共识词汇甚至可能演变成行业通用词汇，即“互联网黑话”，比如赋能、拉通，组合拳、闭环、颗粒度等。个人不太喜欢这些词汇，有点过于滥用了。</p><p><strong>1.3 提供概念词典</strong></p><p>当你文档中出现一些不常见、复杂、有歧义的词汇时，建议列出你的概念并进行严谨的解释。放到“需求描述-业务规则”中最佳，方便阅读者在了解需求时对照查看。</p><p><strong>1.4 使用在线文档</strong></p><p>PRD最好写到在线文档中，与使用word等离线文档相比好处非常明显，更新之后开发、测试可以直接阅读最新的文档，不需要产品先发送文档，开发、测试再下载更新。</p><p>现在在线文档的种类非常多，并且功能越来越强大、体验也越来越好，并且很多提供了历史版本的功能，方便对比查看。</p><p><strong>2. PRD的结构</strong></p><p>日常迭代的PRD，内容我一般写的比较简单。包括：</p><ul><li><p>版本说明</p></li><li><p>需求背景</p></li><li><p>业务流程</p></li><li><p>需求列表</p></li><li><p>需求描述</p><ul><li><p>Story</p></li><li><p>流程图</p></li><li><p>界面描述</p></li><li><p>业务规则</p></li></ul></li></ul><p><strong>2.1 版本说明</strong></p><p>版本说明用于记录PRD的更新历史，方便开发、测试了解PRD都更新了哪些内容。</p><ul><li><p>版本号：记录更新的次数，1.0，2.0…即可。加一位小数是为了让开发团队看起来更亲切，哈哈。</p></li><li><p>日期：PRD更新的日期，让开发团队了解需求是什么时候更新的。</p></li><li><p>负责人：更新PRD的人，产生疑问时方便跟进。</p></li><li><p>版本内容：描述本次更新了哪些内容，包括那个Story的哪个具体功能、新的需求的概括。</p></li></ul><p>对于非常重要的更新，建议使用不同颜色字体，以引起开发团队的注意。注意，开发过程中的变更一定要经过开发团队的确认，产品不能擅自更改。</p><p><img src="http://img.pmcaff.com/dca741319ab0d1ea6f8e0849d340bbc0-picture" alt="dca741319ab0d1ea6f8e0849d340bbc0-picture" coffee-w="1080px" coffee-h="264px" coffee-format="png" referrerpolicy="no-referrer"></p><p><strong>2.2 需求背景</strong></p><p>目的是向设计师和开发团队解释清楚为什么要做本次需求。团队不了解用户需求，也能做设计和开发，但是基本做不出来优秀的产品。</p><p style="margin-left:32px;">设计师大多是有表达欲望的，尤其在更有发挥空间的色彩和图案层面。如果设计师不了解需求背景和用户，就只能根据自己的想象去做设计，做出的交互方式以及内容展示的重点很难满足业务和用户需求。比如你想突出产品特点，设计师做成了突出产品外观。</p><p style="margin-left:32px;">一个优秀的开发是需要能从业务和用户的角度思考的。拿到同样的需求，不同能力的开发交付的产品是不一样的。这种差别，不止体现在代码的可用性、兼容性、鲁棒性等技术层面，还会直接影响用户体验。比如了解用户的算法工程师，能够完成更符合用户需求的产品推荐；前端工程师能够开发出反馈更恰当、更及时、更丝滑的效果，让用户用起来更舒服。</p><p>需求背景描述应该使用<strong>5W1H的方法</strong>，即What、Where、When、Who、Why、How。根据需求的复杂程度从用户需求（必选）、业务需求（推荐）等方面描述。</p><p><strong>What：做什么功能。</strong></p><ul><li><p>用户需求：我们要做一个什么样的功能满足用户。例如：做一个商品搜索栏。</p></li><li><p>业务需求：我们要做一个什么样的功能满足业务。例如：做一个优先推荐利润高产品的搜索栏。</p></li></ul><p><strong>Where：使用场景是什么。</strong></p><ul><li><p>用户需求：用户在什么场景下使用。例如：在用户有明确购买目的场景下使用。</p></li><li><p>业务需求：业务对该功能的依赖场景是什么。例如：帮助商品初次触达用户的场景下需要。</p></li></ul><p><strong>When：一般什么时候使用。</strong></p><ul><li><p>用户需求：用户什么时间使用较多。例如：用户刚进入APP时最容易使用搜索栏。</p></li><li><p>业务需求：什么时候去实现业务需求。例如：用户使用搜索栏搜索时。</p></li></ul><p><strong>Who：谁的需求。</strong></p><ul><li><p>用户需求：哪些用户会使用该功能。例如：所有用户都会使用搜索栏。</p></li><li><p>业务需求：哪些业务对功能有依赖。例如：所有商品对搜索栏都有依赖，小品牌依赖度更高。</p></li></ul><p><strong>Why：为什么要做。</strong></p><ul><li><p>用户需求：用户为什么要使用该功能。例如：为了更快的找到想买的东西或品牌。</p></li><li><p>业务需求：业务为什么需要该功能。例如：除了能高效匹配用户和商品，还能通过结果排序盈利。</p></li></ul><p><strong>How：怎么做。</strong></p><ul><li><p>用户需求：如何做该功能以满足用户需求。例如：在首页增加搜索栏。</p></li><li><p>业务需求：如何做该功能以满足业务需求。例如：搜索栏能够搜索到全部商品并按照业务规则排序展示。</p></li></ul><p>在刚开始时，建议按照上述的格式自己列出来，再写成方便阅读的连贯文字。等到轻车熟路之后，就可以直接动笔，边写边梳理了。</p><p><strong>2.3 业务流程</strong></p><p>推荐以泳道流程图的形式展示，案例请看《如何写出一份优秀的PRD-准备篇》。想画好流程图其实也不难，掌握以下几个要点即可。</p><ul><li><p>横向列出功能相关的角色，例如用户、后台、运营等。</p></li><li><p>纵向列出功能相关的业务环节，例如挑选商品、下单购买、订单处理等。</p></li><li><p>按照业务（数据）流程推进，将对应的行为、处理写到对应角色下。</p></li><li><p>判断使用分支结构，务必使用多层二分法覆盖所有情况。</p></li><li><p>巧用循环结构，减低流程图复杂度。比如某个分支流程需要返回之前的流程，那么就可以使用循环结构。</p></li><li><p>所有的分支必须闭环，及指向结束。</p></li></ul><p><img src="http://img.pmcaff.com/1a1476b962b99cd12f7d37624738ea45-picture" alt="1a1476b962b99cd12f7d37624738ea45-picture" coffee-w="1080px" coffee-h="908px" coffee-format="png" referrerpolicy="no-referrer"></p><p><strong>2.4 需求列表</strong></p><p>按照需求的优先级，从高到低依次列出本次需要开发的功能。方便开发测试优先完成高优先级的需求，一旦发生延期风险，可以放弃开发后面的低优先级需求。</p><p><img src="http://img.pmcaff.com/7364e7a77d7f50cb9fbb62017fecf258-picture" alt="7364e7a77d7f50cb9fbb62017fecf258-picture" coffee-w="1080px" coffee-h="126px" coffee-format="png" referrerpolicy="no-referrer"></p><ul><li><p>需求名称：为需求起个简洁的名称，方便沟通。例如搜索栏。</p></li><li><p>模块/子模块/页面：方便开发团队理解该功能在那个页面实现。</p></li><li><p>Story：描述该需求的用户故事。要用“作为一个用户（As a user），我希望（I want）什么功能，以（so that）满足什么商业价值“的标准格式描述，以讲清楚该需求的目标用户、功能和价值。</p></li><li><p>需求来源：讲清楚需求的来源，方便后续跟进。</p></li><li><p>优先级：需求的优先级，优先级的评估同样可以参考准备篇。</p></li></ul><p><strong>2.5 需求描述</strong></p><p>下面就到了PRD的重头戏：需求描述（或功能描述）。一个功能设计是否合理，能否被设计和开发团队读懂，设计、开发出满足用户需求和业务需求的产品，都要依赖需求描述的合理性。</p><p><strong>Story</strong></p><p>再次重申Story，避免阅读者返回需求列表查看。</p><p><strong>流程图</strong></p><p>对于复杂的功能，建议详细的画出流程图。简单功能可以省略。</p><p><strong>界面描述</strong></p><p>在与设计团队对接时，推荐使用手绘原型图。因为懒得画了，就想到网上找一些。很多手绘原型图画的都很好看、很精细，但是我觉得不是很合适。</p><p>如果有专业的交互设计师，这反而是对他设计的一种限制，以你的不专业影响了他的专业。如果需要你自己做交互设计，那么也没必要在手绘上画这么多时间，直接用工具做反而更好。</p><p>我个人认为画到如下程度就可以了。</p><p><img src="http://img.pmcaff.com/a67d3b60d00fa5d79a43224cdba789dd-picture" alt="a67d3b60d00fa5d79a43224cdba789dd-picture" coffee-w="658px" coffee-h="292px" coffee-format="png" referrerpolicy="no-referrer"></p><p><strong>在评审前，记得把手绘原型图替换为带标注的UX。</strong>虽然你更新起来会比较麻烦，但是对开发团队来说，阅读十分方便。下图是我几年前做的一个后台系统的交互及标注，供参考。</p><p><img src="http://img.pmcaff.com/d1fcae8ee14a9b603976ebab5aea19a3-picture" alt="d1fcae8ee14a9b603976ebab5aea19a3-picture" coffee-w="1080px" coffee-h="927px" coffee-format="png" referrerpolicy="no-referrer"></p><p><strong>业务规则</strong></p><p>业务规则是PRD中最核心，也是最难描述的部分。功能的流程、页面的导航、界面设计、组件功能、提示文字、异常情况等都需要在业务规则中描述清楚。个人的一些描述习惯如下。</p><ul><li><p><strong>从主要流程到分支流程。</strong>比如订单处理，应该优先描述正常的订单流转流程，再描述特殊订单的处理流程。</p></li><li><p><strong>从主要页面到次要页面。</strong>一个流程中可能涉及多个页面，那么应该按照主线将主要页面描述清楚，再描述次要页面。比如订单列表、订单处理页为主要页面，订单流转等为次要页面。</p></li><li><p><strong>从一般页面状态到特殊页面状态。</strong>一个页面可能会分成多种状态，比如一般页面、空页面、报错页面等，那么应当优先描述清楚一般页面，再讲清楚特殊页面及其出现条件。</p></li><li><p><strong>从上到下描述页面功能。</strong>这样描述会比较符合前端开发的习惯，从上小到下逐个完成页面布局和功能的开发。比如从页头、标题、搜索栏、主要功能区、到底部导航栏等。</p></li><li><p><strong>描述清楚每个功能区。</strong>首先描述清楚每个功能区的作用是什么，然后是使用什么控件，接着交代清楚默认状态、功能逻辑、功能限制等，最后补充报错情况。比如描述一个用户留言框：</p><ul><li><p>让用户输入留言保存并展示；</p></li><li><p>默认为空，显示提示文案”请输入留言“；</p></li><li><p>≤100字，过长无效；</p></li><li><p>提交时校验是否为空，若为空则报错”留言不能为空“；否则校验是否有敏感词，若存在则报错”存在敏感词，请修正后再试“；否则提交并保存用户留言。</p></li></ul></li></ul><p>从以上描述可以看到虽然一个输入框很简单，但其实要包括前端的展示、报错，以及后端的提交和储存。只不过这个控件很常用，可以约定俗成的简单描述。比如有标准的交互规范，可以描述为”用户留言默认为空，≤100字，需要空内容和敏感词校验“。<br></p><p>对于具体的文字描述，同样有一些原则，整理如下：</p><ul><li><p><strong>要符合MECE原则</strong>，即 Mutually Exclusive Collectively Exhaustive，“相互独立，完全穷尽”。我们在描述需求的时候，一定要考虑所有的情况，并给出应对方案。为了避免遗漏，最好借助坐标轴、集合关系图、脑图等方法。</p></li></ul><p><img src="http://img.pmcaff.com/727d6364230d59a9052d8e1e0652c36d-picture" alt="727d6364230d59a9052d8e1e0652c36d-picture" coffee-w="600px" coffee-h="706px" coffee-format="png" referrerpolicy="no-referrer"></p><ul><li><p><strong>描述逻辑清晰。</strong>因为受个人思维习惯的影响，所以想讲清楚什么是逻辑清晰比较困难。大概就是符合大多数人的认知规律，能够按照时间先后、因果、主次、关联、整体与部分等关系，合理的将产品功能描述清楚。因此更多的需要把功夫花在平时对自己的训练上，多读一些科学、哲学相关的书籍。</p></li><li><p><strong>用语简洁。</strong>这个很好理解，没有人喜欢又臭又长的需求文档，要用尽量精简的语句，将产品功能描述清楚。比如：</p><ul><li><p>描述不必事无巨细，抓住重点描述。比如”当用户滑动并看到按钮时，可能用手点击按钮“，改为”当用户点击按钮时“。</p></li><li><p>尽量用短句，减少长句。比如”当用户点击输入框弹出键盘输入文字并显示“，改为”1.点击输入框，2.弹出键盘，3.显示输入文字“。</p></li><li><p>避免抽象词汇，选用具体词汇。比如”输入文字不能太多“，改为”输入文字≤100字“。</p></li><li><p>不必有客套话，直接描述。比如”请开发大大注意不能提交空内容，谢谢“，改为”检验是否为空“。</p></li><li><p>不必用华丽的辞藻修饰，要用精确的修饰。比如”页面切换时要如牛奶一般丝滑“，改为”页面切换要平滑“。</p></li><li><p>减少语义重复的语句。比如”按钮要大、明显、容易点击“，改为”按钮要方便点击“。</p></li></ul></li><li><p><strong>使用专业词语。</strong>文章开篇已经交代过。使用专业词汇除了方便阅读，同时也能极大精简语句。比如”内容过多时，输入框旁边要出现滑块，拖动滑块可以改变显示文章“，改为”输入框内容过长显示滚动条“。</p></li><li><p><strong>避免歧义。</strong>在写功能描述时，一定不要只考虑自己头脑中的概念，要考虑自己的措辞是否会造成误解。</p><ul><li><p>尽量使用数字、公式、图表。比如”输入不能多于100字“，那么输入100个字是否允许呢？最好描述为”输入≤100字“。</p></li><li><p>避免主体及对象模糊。比如”前端负责提示，后端负责提交数据。其还要负责埋点。“前后端都可以实现埋点，因此要注意指定清楚。</p></li><li><p>可以使用缩写，但是不能产生二异性。比如”后台“可能指程序后台，也可能指运营后台等。如果可能让人误解，就必须描述清楚。</p></li><li><p>其它的行文技巧。比如注意多音字、多义词、定语范围等。</p></li></ul></li></ul><p>最后是要有一个清晰的排版。每个人都有自己的排版技巧。在此就不跟大家介绍了。</p><p>关于如何书写PRD的分享就到这里，希望对你有帮助。也欢迎分享你撰写PRD的技巧。</p><p style="text-align:justify;"><span style="color:rgb(18,18,18);">个人公众号：apmdogy，优质文章提前几天看。</span></p></div>
  
</div>
            