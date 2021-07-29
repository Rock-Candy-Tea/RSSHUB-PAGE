
---
title: '【用户视角的B_G端PRD撰写】避坑指南'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AMX7dO8NvkAqLIx0jDQO.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 29 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AMX7dO8NvkAqLIx0jDQO.jpg'
---

<div>   
<blockquote><p>编辑导语：在写PRD需求时，我们总会遇到各种各样的坑，如何避免或者少踩一些坑呢？作者分享了从用户视角出发的自己经历过的奇葩问题与解决思路，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4955141 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AMX7dO8NvkAqLIx0jDQO.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、背景讲述</h2>
<p>接到公司任务，做《避坑36计》分享PRD撰写思路。</p>
<p>之前做的G端需求调研避坑分享，让我司百来号人，看到什么叫自杀式自黑总结，讲述遇过的各种奇葩问题和解决思路。这次决定换换这打脸不讨好的方式。</p>
<p>毕竟公司产品被强制参加，改变策略不讲个体遭遇，收集一波研发、设计的吐槽，再需求分析共同探讨。这决定了本期主题《用户视角的PRD撰写》。</p>
<p>决定记录下来，一方面是提炼总结和自我提醒；另一方面，是和同行共同交流避坑经验，交流互助，碰撞更好的解决方案。更好地满足PRD产品的用户需求。</p>
<p>注：总结来自创业属性公司，可能和大厂所遇问题不同，若有不同观点，也欢迎交流。</p>
<h2 id="toc-2">二、 现有声音收集</h2>
<p>为收集现有痛点和需求，于是乎，先去问了设计、研发们一个小问题：你觉得产品的PRD怎么样？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Yjev1Xdg7pkoHNsKGhCA.jpeg" alt width="488" height="223" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/QRGKw0UYjP2HZQqH9848.jpeg" alt width="489" height="230" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DRUGcFqT1PnwDxkY8Hir.jpeg" alt width="491" height="166" referrerpolicy="no-referrer"></p>
<p>得到的问题反馈，好气又好笑，含蓄又直接，八分的玩笑中透露出十分的认真，但每个反馈都值得被认真对待。确实是群有想法、有输出、能抗伤害的同事了。</p>
<p>虽然个人认为，PRD不一定要实现全部交互跳转，从全流程来看，在需求不明确的场景下，B端/G端产品存在较大的改动风险。交互不难实现，但维护成本太大，并存在被看漏的可能性。</p>
<p>拆解该研发槽点的底层需求，实际是觉得现有方式表达并不清晰，没能很好呈现页面的跳转关系，造成了团队沟通上的困难。而认为要有交互，只是他作为用户提出的解决方案。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bw2vg4B8ye3BrnRHBTNh.jpeg" alt width="510" height="148" referrerpolicy="no-referrer"></p>
<p>所有诉求问题，可总结为两点：</p>
<ol>
<li>可读性差</li>
<li>内容不详</li>
</ol>
<p>于是，我又去问了其他产品：<strong>你写PRD担心过什么？</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/XbKjAsNXfLJTfM0MMpPU.jpeg" alt width="518" height="291" referrerpolicy="no-referrer"></p>
<p>有些也是我初转产品时，曾担心过的问题。看到此处的读者，不知是否有过类似担忧？</p>
<h2 id="toc-3">三、PRD的用户视角分析</h2>
<p>用基础分析工具5W1H，拆解下PRD的用户需求。</p>
<h3>1. what：PRD是什么？</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/zBht9eh1JqKRc6T23y1d.jpeg" alt width="645" height="322" referrerpolicy="no-referrer"></p>
<p>首先，在定位上，PRD是产品经理的沟通工具。涉及最多的两种表现形式是Word+Axure，和Axure。两者各有优劣，其实不用局限于一种形式，可根据使用场景选择合适的表现形式。</p>
<h3>2. why：为什么要写PRD？</h3>
<p>这里引用他处定义，解释说明。</p>
<blockquote><p>产品原型的目的，是清楚表达产品设计理念和功能交互及执行逻辑，提高产品、研发、UI及业务部门之间的沟通效率，避免信息不对称和信息传达的遗漏和缺失而导致的整个项目进度延期问题。</p></blockquote>
<p>具个人经验，归纳为两点：</p>
<ol>
<li>减少沟通的认知偏差</li>
<li>保障质量的前提下提升效率</li>
</ol>
<p>说人话就是：减少扯皮，避免返工；能懒则懒，减少加班。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/FCI3IndGytVtga9Yuks4.jpeg" alt width="776" height="437" referrerpolicy="no-referrer"></p>
<h3>3. when：PRD在什么阶段写？</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Muvk2XhIG2jPoPpoDLDN.jpeg" alt width="785" height="437" referrerpolicy="no-referrer"></p>
<p>理论上，PRD作为产品需求文档，是继BRD、MRD后，从产品规划到产品设计的阶段性产出物。在中小型公司中，常缺失在规划阶段的商业论证和市场验证，需求来自领导对市场的敏感度，来决策做或不做，缺失的商业需求文档、市场需求分析。</p>
<p>后果是，在PRD梳理过程中，影响决策。导致后期部分功能需求摇摆不定，因为缺少此类信息输入，细化PRD后，才发现底层逻辑需求错误，导致大范围返工。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/9wNDR7l6p2Vap0T2zdkW.jpeg" alt width="809" height="464" referrerpolicy="no-referrer"></p>
<p>而在实践中，经常为了更快产出，会变成PRD通关全过程，缺少BRD、MRD的阶段和产出。</p>
<p>BRD：Business Requirement Document，产品向上沟通立项的工具。<strong><br>
</strong></p>
<p><strong>内容：说明产品卖给谁、成本和收入情况、为什么能赢利等关键问题。阐述为什么立项，为公司提供信息，从而决策该产品是否有投入资源的价值。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/LU2KfApHDILz4qxEu8uB.png" alt width="358" height="210" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">MRD：Market Requirement Document</p>
<p><strong>定义：</strong>向上沟通要做什么、怎么做的工具。</p>
<p><strong>内容：</strong>说明所处行业的市场情况、目标用户、竞品情况、自身策略等信息。阐述内外环境影响，向公司说明产品在市场中的定位和策略，核心是为该产品在同公司的众多产品线中，争取更多的研发、运营和市场资源倾斜。</p>
<p>where：PRD在哪儿写？</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/SBlNpVm7ZoQNTTgXx0kA.jpeg" alt width="787" height="425" referrerpolicy="no-referrer"></p>
<p>此处可划分为两大阶段，四个类型。两大阶段为需求评审、交互评审；四个类型为项目的大版本需求设计、项目的小迭代需求、新产品从0-1孵化、新产品迭代需求。在不同环节，关注的内容会有所不同。</p>
<h3>4. who：分辨PRD用户是谁</h3>
<p>在B端、G端产品中，PRD的用户在产品工作中的上下游环节，可分为公司外部相关方、内部成员。</p>
<p>1）内部成员：内部用户和C端基本一样。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/yBPTdJHBg9TneMSiAZQI.jpeg" alt referrerpolicy="no-referrer"></p>
<p><strong>a）需求评审阶段：</strong>主要面向领导、研发负责人、产品负责人、项目经理。希望获取的信息如下：</p>
<ul>
<li>需求价值</li>
<li>目标</li>
<li>用户故事（为谁在什么场景下解决什么问题）</li>
<li>方案可行性</li>
<li>成本（功能清单）</li>
<li>需求优先级</li>
<li>竞争力情况</li>
<li>产品架构（和其他模块的关系）</li>
</ul>
<p><strong>b）交互评审阶段：</strong>主要面向前端、后端、设计、测试、项目经理、协同产品。希望获取的信息如下：</p>
<ul>
<li>需求价值</li>
<li>目标</li>
<li>用户故事（为谁在什么场景下解决什么问题）</li>
<li>方案可行性</li>
<li>需求优先级</li>
<li>产品架构（和其他模块的关系）</li>
<li>页面交互</li>
<li>性能要求</li>
</ul>
<p>作为PRD文档，交互评审阶段为核心业务场景。详细拆解该阶段各类用户的核心关注点，如下：</p>
<p><strong>后端：</strong>关注数据从哪来，数据有什么，哪些需要存，如何建表存，这些数据是否需要支持增、删、改、查等功能，需要为产品提供哪些接口，评估方案可实施性。</p>
<p><strong>前端：</strong>关注后端接口如何与前端界面结合，调取后端哪个接口，并用怎样的方式为后端收集入参，在收集入参时前端是否要做额外的限制，以及后端返回的出参如何转化为前端的提示等，评估方案可实施性。</p>
<p><strong>设计师：</strong>关注信息布局和交互的合理性、用户体验、产品的界面调性。作为产品下游，他们往往是最关注PRD中原型内容的人。</p>
<p><strong>测试：</strong>关注产品的user story，因为QA需要模拟不同的使用场景设计测试case，大部分情况下QA会用Xmind等脑图设计工具来设计、覆盖可能出现的case，并进行遍历测试。</p>
<p><strong>协同产品：</strong>产品中有哪些通用概念，本次迭代与之前版本的功能迭代的关系，需求的紧急性和重要性。</p>
<p>2）外部相关方与C端不同在于，B端和G端的外部相关方，对产品有绝对性影响。可划分为高、中、基层甲方领导。</p>
<ul>
<li>甲方高层：很多不看，他们喜欢看PPT和上线系统，部分喜好抠“字眼”。</li>
<li>甲方中层：注重业务逻辑（解决了什么问题）、功能价值（可达到的效果）、用户场景（为谁在什么场景下解决什么问题）、使用体验，部分喜好抠字段、交互和视觉呈现。</li>
<li>甲方基层：注重功能使用场景（功能是否满足业务需求）、使用体验、字段。</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/gFRHX2QlLTgpCTd9OhC4.jpeg" alt width="752" height="349" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、how：PRD的内容要素</h2>
<p>PRD涉及的信息要素有版本记录、需求分析、需求设计、全局说明、原型设计四大内容。在不同阶段场景下，涉及的内容略有差别，具体内容如下图。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/h6NqgjmPsCkglwtuaXqD.jpeg" alt width="780" height="435" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/GB1dBKDVm0SQ9w4hw6UJ.jpeg" alt width="766" height="288" referrerpolicy="no-referrer"></p>
<p>此处进行总结罗列，不做内容拆解，等有时间精力梳理时，再进行总结分享。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/epAdcVbQ9umVGlsM6cxO.jpeg" alt width="754" height="555" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、PRD撰写的避坑总结</h2>
<h3>1. 避坑一：无版本记录、修订记录</h3>
<p>版本记录、修订记录不可少。在PRD里直接记录，每次修改时顺手完成，成本远远小于事后追溯。</p>
<p>版本记录：用于方便对应不同版本。内容包含系统名称、文档版本号、系统版本号、创建时间、产品经理、UI设计师、前端、后台人员信息。</p>
<p>修订记录：易于回溯和总结变更原因，保障下次的输出。内容包含修订日期、文档版本、所在页面、变更内容、修订情况、修订人员。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/NsnzD9iYXlCGhuvchFRN.png" alt width="789" height="233" referrerpolicy="no-referrer"></p>
<p>在这过程中，不但要补充内容，也要思考需要修改的原因是什么。是需求挖掘没有到位？没有找到关键的业务干系人？业务流程存在疏漏？还是外部商务因素干扰引发的需求反复？</p>
<p>要综合衡量每次修改的成本差异、实现效果。思考修改变动是否能解决用户核心问题，此次修改是不是项目中最需要坚持的核心功能流程，要注意把撕逼的机会留给守护核心功能流程上。</p>
<h3>2. 避坑二：需求背景描述不全面</h3>
<p>需求背景需全面，尽量还原业务场景。需求收集-分析的过程，是产品设计的输入，让产品经理能摸清问题的本源。沟通要在信息对等的前提下进行，需求场景表达越合理，越能让团队觉得自己所做事情是有价值的。</p>
<p>如果被质疑时，你只能说出“老板/领导要这么做”的话，说明你在需求调研和需求分析阶段偷了懒，没有负起责任，这也容易因为对需求理解不到位造成返工。</p>
<p>做功能只是手段、不是目的。不要只做传话者，变成了自己讨厌的人。</p>
<p>常见的需求来源有：</p>
<ol>
<li>业务需求/问题</li>
<li>现状数据分析</li>
<li>来自竞品（抄竞品）</li>
</ol>
<h3>3. 避坑三：需求评审阶段，未梳理系统依赖</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/OT2z5ZMRBpyESsb74EXn.jpeg" alt width="737" height="361" referrerpolicy="no-referrer"></p>
<p>B/G端系统，常依赖于其他系统数据，在需求评审阶段，就需梳理清楚所有所需数据来源、系统依赖。</p>
<p>一方面，是进行初步的可行性评估，明确所需条件是否具备；另一方面，可提前协调相关资源，预留字段和接口。若交互设计阶段，才进行相关梳理和确认，易造成决策返工，可能会发现前置条件并不满足。</p>
<h3>4. 避坑四：数据层分析缺失</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pV9FbLY7NtYeTWFksxa6.jpeg" alt width="753" height="443" referrerpolicy="no-referrer"></p>
<p>交互评审中，数据分析梳理不可缺。B/G端系统设计中，数据是核心。其中数据清单列表、实体关系图是每次需求都需梳理和更新的必要信息，数据流程图可根据需求的复杂程度决定是否分析。</p>
<h3>5. 避坑五：信息不清晰 布局不简洁</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/nIoWggAitpNqrUd7MMls.jpeg" alt width="732" height="430" referrerpolicy="no-referrer"></p>
<p>信息结构尽量清晰，布局尽量简洁。无论页面设计，还是PRD的排版布局，都要注意信息设计的合理性。并且内容越清晰，越能降低评审人员的理解门槛，提前讨论疑问点，让评审效率更高。形式的建议如下：</p>
<p><strong>1) 图文结构化布局</strong></p>
<p>页面元素与注释对应清晰，最好在元素边上就是注释。</p>
<p><strong>2) 文字排版简洁</strong></p>
<p>描述简洁精炼。避免大段文字，多分行。</p>
<p>信息要放得下。放不下又全要，就换个交互形式。</p>
<p>考虑信息主次。考虑信息的次序感，通过字体类型（粗细）和字号区分出信息层级和描述重点。</p>
<p><strong>3) 色彩简洁</strong></p>
<p>避免丰富的颜色。用黑白灰+主题色+强调色。</p>
<h3>6. 避坑六：忽略细节定义</h3>
<p>注意细节定义。以下几点，都是较为重要且易被忽略的。</p>
<ul>
<li>定义数据</li>
<li>定义地图交互</li>
<li>定义异常状态反馈</li>
<li>定义排序规则</li>
<li>定义状态机</li>
</ul>
<p>最后，其实还需结果导向，不要拘泥于形式表达，最终是希望能和上下游高效协同。</p>
<h2 id="toc-6">六、总结&思考</h2>
<p>前期设计环节考虑越充分，越能保障后续实现的质量。所以还是有必要梳理PRD规范。当生产中的每个环节都保证生产质量，从整条生产链来看，会节省了不少“补锅”成本，也就是“1-10-100”理论。</p>
<p>在设计阶段，花1块钱能解决的问题；留在制造阶段，要用至少10倍成本来纠错；如缺陷流出到顾客，则至少要花100倍成本来纠错。</p>
<p>但标准的制定和执行需要过程，需有序推进。这是关于产品质量和效率的权衡，值不值得我们花时间让它变得高质量，要聚焦目标和初心，是为了“60分”还是“100分”，优先处理最重要的事情，聚焦处理核心的需求。</p>
<p>在公司分享的最后环节，产品副总裁让大家挨个补充了所遇问题和感想，并针对每个槽点/问题，拆解了解决方案，让总结和分享并没有止步于会议。例如：</p>
<p>问题：评审没有“裁判”。</p>
<p>方案：定义关键要素的标准。增加打分标准。记录评审修改过程，进行评估，标准为评审次数、文档修改次数的有效归档、修改情况，利于复盘提升产品设计能力。</p>
<p>问题：评审没有“教练”。</p>
<p>方案：制定标准：原型中，写标准示例，建立知识库优秀案例</p>
<p>这样有自省能力和持续成长的组织，相信未来会更好。我也会继续努力，在此次总结后，梳理下出适合自身行业的PRD标准，持续优化自身和团队的输出质量及效率。望共勉之。</p>
<p> </p>
<p>本文由 @wenda 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4947285" data-author="95631" data-avatar="http://img.woshipm.com/WD_U_201606_20160617104414_3779.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            