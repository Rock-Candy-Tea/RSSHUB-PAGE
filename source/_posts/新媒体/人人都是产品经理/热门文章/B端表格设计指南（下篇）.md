
---
title: 'B端表格设计指南（下篇）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/SSLtrsl5zmO6nBdIiQIn.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 23 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/SSLtrsl5zmO6nBdIiQIn.jpg'
---

<div>   
<blockquote><p>编辑导读：表格是展现数据最为清晰、高效的形式之一，它也是B端产品和设计师每天接触最多的组件，常和排序、搜索、筛选、分页等其他界面元素一起协同。本文作者总结了一套B端表格设计指南，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5327867 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/SSLtrsl5zmO6nBdIiQIn.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>大家好，我是小鹿，今天为大家分享的是<strong>「表格设计指南下篇」</strong></p>
<p>在之前的文章中小编已经分享过上篇，里面介绍了表格的概念和数据查看的知识点，没有看过的小伙伴可以快速回看➡️➡️<a href="http://www.woshipm.com/pd/5323117.html" target="_blank" rel="noopener"><strong>《B端表格设计指南（上篇）》</strong></a></p>
<p>本篇文章就来聊聊数据筛选和数据操作。</p>
<h2 id="toc-1">一、数据筛选-查</h2>
<p>数据筛选区可以看作表格的导航，按预定目标过滤出某种具有特定性质的数据，将操作者所关注的数据展示到前面，便于<strong>快速查看、对比、分析信息的操作过程</strong>。</p>
<p>从用户角度出发，<strong>按不同粒度的数据检索方式分为3种方式</strong>，分别对应不同程度的用户。</p>
<ul>
<li><strong>搜索</strong>：当用户有相对明确的选择目标时，需定点查看，数据多且杂乱无规律；</li>
<li><strong>筛选</strong>：用户目标相对比较模糊，游离于一个大概的范围时，通常用于一些有清晰分类的数据；</li>
<li><strong>标签</strong>：查看无交集的数据内容，通常伴随时间、状态的流转。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/HEcoXFouFgb0oaODSdQw.png" width="1518" referrerpolicy="no-referrer"></p>
<h3>1. 搜索</h3>
<p>搜索可以帮助用户在巨大的信息池中缩小目标范围，快速而准确的定位到目标数据，并速获取需要的信息。<strong>由于考虑到用户需要手动输入，很难保证精准搜索，原则上所有搜索均为模糊搜索，必要精准搜索的地方使用筛选功能</strong>，给用户提供筛选选项。通常上端搜索栏不被限定搜索范围，可以全部搜索。</p>
<p><strong>1.1 模糊搜索</strong></p>
<p>优点：减少精准搜索带来的记忆负担</p>
<p>缺点：容易把不相关的信息带出来，如搜索手机号131，把ID含131数字的信息也带出来了</p>
<p><strong>1.2 带标签的搜索</strong></p>
<p>优点：搜索匹配精准度高</p>
<p>缺点：不方便，每次只能对单一条件进行搜索</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/hYwfj3PxbU7UZUwuolaO.png" width="1393.5" referrerpolicy="no-referrer"></p>
<h3>2. 筛选</h3>
<p>筛选可以帮助用户缩小数据范围，逐步找到想要的内容。或者当用户的目标就是查看某一范围的数据时，筛选将是一种十分快捷的方式。</p>
<p><strong>2.1 下拉筛选</strong></p>
<p>优点：空间利用率高，起到了很好的收纳作用</p>
<p>缺点：无法直观看到所有筛选项</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/LD2lWCpncsLdyma7plns.png" width="1050" referrerpolicy="no-referrer"></p>
<p><strong>2.2 平铺筛选</strong></p>
<p>优点：操作效率高，筛选项一目了然，支持输入更多筛选条件</p>
<p>缺点：空间利用率低，不适合选项太多的情况</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/lBDP1MUWsR6hgO0ivkl2.png" width="1050" referrerpolicy="no-referrer"></p>
<p><strong>2.3 表头筛选</strong></p>
<p>优点：筛选当前列，更直观，一般情况下表单左侧数据筛选频次越高</p>
<p>缺点：筛选的内容仅限于特定、单次列的筛选，对于首次使用者来说陌生，交互形式需要学习</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/k6uaiuRO5GmlsNVz2b1O.gif" width="814" referrerpolicy="no-referrer"></p>
<p><strong>2.4 tab标签</strong></p>
<p>使用场景：<strong>标签切换一般用于和时间、状态的流转有关，且没有交集的数据内容</strong>（可以是同性质，也可以是不同性质）。主要样式有基础、卡片、胶囊等。</p>
<p>优点：根据标签，可以很清楚知道划分，切换tab就可以筛选内容。</p>
<p>缺点：分类需覆盖选项，并且保证每一项没有交集，分类不能过多，超过7±2个选项可选择下拉筛选。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/43Ek9TMLl3RFnTMMrCsX.png" width="1050" referrerpolicy="no-referrer"></p>
<p>提升用户体验的一个小细节：<strong>默认用户最关注的选项，而非全部</strong>，这样可以缩短查询路径，同时给出条目，让用户清晰明了每个选项的数量，便于操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TBbT4e5pLLTI4UvHJTcs.png" width="1050" referrerpolicy="no-referrer"></p>
<h3>3. 组合筛选</h3>
<p>在企业级中后台中，用户查看的数据往往属性较多且不唯一，通过简单的检索方式很难精确定位到目标数据，所以，在<strong>实际使用时，常会将大量非交叉关系的属性进行罗列，搜索、筛选、标签切换组合出现，形成多属性组合检索</strong>。</p>
<p>而筛选项互相组合，其展示方式分为平铺和折叠两种。</p>
<p><strong>3.1 平铺显示</strong></p>
<p>选用对用户决策有意义、操作频次高的属性作为直接展示的组合检索条件，建议数量<strong>最好不超过5个</strong>（7±2法则）。</p>
<p>优点：大而全能最大限度避免检索条件疏漏的可用性问题</p>
<p>缺点：易用性不高。大而全可能为用户带来繁杂的第一印象，都是重点等于没有重点，增加用户的决策时间。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ThErIp00crlTMMxakOvr.png" width="1069.5" referrerpolicy="no-referrer"></p>
<p><strong>3.2 折叠展示</strong></p>
<p>如果多属性组合检索中的一部分检索条件不是高频率使用的，但又是必须存在的，</p>
<p>可通过折叠的方式将这部分检索条件隐藏起来，将高频率使用的、数据覆盖面广的1-3个属性直接展示出来。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/vStl3N4vsL97OJcCYsBr.png" width="1069.5" referrerpolicy="no-referrer"></p>
<p><strong>总结思考</strong></p>
<p>在设置组合检索项时，应考虑每一项检索甚至是多属性组合检索是否有必要。需从实际场景出发，<strong>根据用户对各个检索项的使用频率及组合检索项的数量，来决定组合检索项是直接展示还是折叠展示</strong>；以及哪些属性直接展示，哪些属性折叠展示，为各检索项安排合理的展示方式。</p>
<h3>案例一：不同筛选数据位置的摆放</h3>
<p>案例讲解前先开动大家聪明的小脑瓜思考🤔两个小问题：</p>
<p><strong>问题1:</strong></p>
<p>报表管理里面有一个吞吐量统计、舰次（舰是船的意思）和箱量的统计，一个是放在左图中筛选的最上方用我们带小横线的这个标签页默认样式，一个是用胶囊的样式放在筛选最下方表格的上方。这两个哪个的用法是正确呢？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bgzsVfLXsbN08K74G0WS.png" referrerpolicy="no-referrer"></p>
<p>5、4、3、2、1…</p>
<p>先来说下结论吧：<strong>左图是正确的</strong></p>
<p><strong>原因</strong>：首先分析下吞吐量、舰次、箱量三者的关系，很明显，他们和状态、时间的流转是没有关系的，它是不同类型的数据，三个tab的切换有可能就会影响到下面筛选项和表格的字段。所以他的层级是最高的，左图的位置正确</p>
<p><strong>问题2：</strong></p>
<p>如果还有在场箱、已出闸、已在船三个类别，那这三个tab标签是放在左图还是右图合适？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/9sJOc8Isi0O3VkhxXax9.png" width="949" referrerpolicy="no-referrer"></p>
<p>答案是：<strong>右图是正确的</strong></p>
<p>原因：这三个tab是状态和过程的流转有关系，他们是同类型的的数据集，和上面日期、港区的选择是同一个层级的，不会互相影响，之所以把它拿出来呢，是因为它这个筛选比较常用，本质上也是把这个选项给平铺出来了，方便用户查找。</p>
<p>我们再来总结一下案例中tab的用法。<strong>不同性质的数据集分类放在表格的顶部</strong>，下面的筛选和表格都是它的子维度。<strong>同性质，不同状态流程的筛选条件</strong>如果比较高频，可以从细分纬度的筛选条件中拿出来，<strong>紧挨在表格上方</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/hEGCukjf3xzDLNgisvEQ.png" width="1025" referrerpolicy="no-referrer"></p>
<h3>案例二：会员筛选优化</h3>
<p>比如说这我们以一个会员的这个筛选为例，我们的产品经理在做需求的时候，特别喜欢<strong>按照业务逻辑来做一个去梳理</strong>。</p>
<p>对会员的筛选，首页是这个人是不是会员，初始的注册时间，然后会员的来源、性别营销顾问等等，然后她的标签是什么，都有什么卡，然后再往后面耗费次数怎么样呢？积分怎么样？做这样的一个逻辑。</p>
<p>那可以思考下这样的逻辑是对的吗？<strong>这样的排序逻辑是对的吗？</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/lVdydIG20CZ3Vl1quIHE.png" width="1322" referrerpolicy="no-referrer"></p>
<p><strong>答案当然是不对</strong>的，首先应该明确一点，<strong>用户目标高于业务逻辑</strong></p>
<p>但这个时候还需要考虑<strong>2个关键问题：用户场景、目标有哪些？查询路径是什么？哪些检索频次高？</strong>依据从何而来呢？通常有两种方式：</p>
<ul>
<li>依据一：<strong>用户调研</strong>，通过【问卷投放】或【用户访谈】，深入理解用户真实使用场景以及与业务之间的关系。</li>
<li>依据二：<strong>数据埋点</strong>，每个操作埋个PV（点击量）,一个月后再看每个操作的数据量；</li>
</ul>
<p><strong>Step 1：信息排序</strong></p>
<p>会员全生命周期的业务逻辑应该按照的是你的这个用户的实际的这个操作频次性来去排序是更合理的，访谈中我们已经得到了用户对各个检索项的使用频率，那信息排序的原则是：<strong>按使用频率，用户目标高于业务逻辑。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/irjg3YOsPCcfDNZ50lTD.png" width="1322" referrerpolicy="no-referrer"></p>
<p><strong>Step 2：组织及隐藏</strong></p>
<p>同时我们为了保险起见，调研后只调整了信息的排序，同时我们针对后台数据做了一个点击埋点，一个月后的搜索点击次数如下图所示（注：数据已脱敏，大家了解思路即可）<img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/eqk9xTPWoML3eqiQMSLs.png" width="1322" referrerpolicy="no-referrer"></p>
<p>一个月后，我们发现<strong>搜索点击这里是 69,873 次，点击会员等级的是 19,876 次</strong>。对不对？而客户性别只有是 23 次，这种数据你们要怎么去做呢？默认折叠低频选项</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/opxvTZFZkV3kMmu9mrOH.png" width="1130" referrerpolicy="no-referrer"></p>
<p>🤔<strong>如果数据不是上图所示，每个筛选项都很低频呢？</strong></p>
<p>这个时候我们是不是就可以用高级筛选，把筛选都下钻到里面，以弹窗的形式呈现</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/LJVMW5FPqmY5EKHilDkg.png" width="1322" referrerpolicy="no-referrer"></p>
<p>这个时候可能又有小伙伴遇到另外一种场景了，产品涉及了多个角色，每个角色的诉求还不一样。客户粑粑是上帝，没有办法，上帝的需求都得满足。那这个时候自定义就可以出场了🤣</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/nKWeZUFEHpzXTwWlaeDB.png" width="1322" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、数据操作-增删改</h2>
<p>数据操作主要是针对表格数据的增、删、改。可以从控制范围和操作属性来区分：</p>
<p><strong>控制范围</strong>：单行操作、批量操作、全局操作</p>
<p><strong>操作属性</strong>：新增数据、编辑数据、删除数据、业务处理</p>
<p>本文主要从控制范围来对数据操作进行拆解。</p>
<h3>1. 单行操作</h3>
<p>单行操作也称行内操作，常见的显性与隐性两种方式。显性操作，操作项显示在行内，直观明了；隐性操作，鼠标悬停时才显示操作项，界面简洁，留更多的空间给需要查看的数据内容，减轻空间压力，减少干扰</p>
<p><strong>显性操作</strong>：文字按钮操作项一般不多于三个，图标按钮不多于四个时，操作项跟在行条目后面；当超过时，建议将相对低频操作选项折叠收起，点击”更多”或“…”下拉显示。操作按钮致灰时，鼠标选中可显示原因。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/78CiUVHUhOZCVSVbZDih.png" width="1141.5" referrerpolicy="no-referrer"></p>
<p><strong>隐性操作</strong>：如果行操作不那么重要，或者说行操作过于啰嗦影响用户阅读时，可将所有的操作进行隐藏，当用户鼠标悬停时进行展开所有操作。这种方式能最大程度上满足用户快速查看与编辑的需求，但是在实际使用中，用户的初次使用门槛较高，需要有一定的学习成本。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/CoGn5nBPFZ64r0vjE4dI.png" width="1090.5" referrerpolicy="no-referrer"></p>
<h3>2. 批量操作</h3>
<p>适用于数据量较大的表格，通常把操作放在表外部上方，这样操作更便捷，同时便于批处理和单个操作。批处理操作模式允许用户对一行或多行对象执行操作，通常与复选框操作配合使用，并在选中复选框后激活表上方操作按钮，如删除、批准、拒绝、复制之类的操作，这将节省用户时间，避免重复对多行进行相同操作。通常也分显隐性两种操作</p>
<p><strong>显性批量操作</strong>：较为常用，外漏操作简单易懂。</p>
<p>如有赞的批量操作，表格左上角和左下角都有，这样不管用户从上往下选还是从下往上选的场景都能覆盖；飞书的批量操作外漏在表格表格的右上角，虽然按钮放在右侧符合用户右手操作鼠标的习惯，而且考虑到适配问题，但是批量操作的路径不符合用户的操作动线，路径变长，大家可自行抉择</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/V3PkoVYrbwUcrI5afsG6.png" width="1235" referrerpolicy="no-referrer"></p>
<p><strong>隐性批量操作</strong>：容易造成记忆负担，增加学习成本，适合批量操作较低频的操作，产品没有那么复杂的产品。如飞书文档</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/m5HFUasPPpNvaFiNuP6z.png" width="681" referrerpolicy="no-referrer"></p>
<h3>3. 全局操作</h3>
<p>统揽全局，无需选择数据内容即可进行的操作，常见的【新增】、【导入】操作。</p>
<p>三种操作：两个在表格外，一个在表格内，那么很自然的我们会遇到一个问题，一个功能该放在哪呢？下面我通过一个案例来说明。</p>
<h3>4. 案例-数据操作优化</h3>
<p>产品现状：在HRM系统中，不同的权限使每行的数据拥有不同的操作项，而且这些操作因为视觉特征比较显眼，容易分散用户的注意力，且因表格空间有限，操作区的各操作项过于接近，误操作率相对较高。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/aNu0ylQpdP1JFEigWCrv.png" width="1131" referrerpolicy="no-referrer"></p>
<p><strong>设计优化方向：</strong></p>
<ul>
<li><strong>业务目标</strong>-提升数据操作效率；</li>
<li><strong>设计目标</strong>-降低误操作率，让用户聚焦内容；</li>
<li><strong>设计策略</strong>-控制操作项的显示数量，将操作项分类</li>
</ul>
<p><strong>Step 1：分析操作控制范围</strong></p>
<p>习惯上我们会认为一行数据是对某一个对象实例的描述，比如在上图表格中，一行数据是对某个待入职员工的描述，包括他的姓名、工号、在职状态等等。所以表格内的操作也是针对这个对象的。</p>
<p><strong>一般我会把一次只能针对一个对象操作的功能放在表格内</strong>，比如【详情】和【编辑】，因为查看详情不太可能一次查看多个对象，编辑修改信息也是。那么反过来，<strong>不属于任何一个对象实例的功能就需要放在表格外的操作栏</strong>，比如说【新增】。另外一种需要放在表格外的功能是批量操作，因为批量操作需要对多行数据进行同时操作，也不是属于单个对象实例的。以此为依据将图中操作分类如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/i4tBExykivBgxDAwJSBk.png" width="1266" referrerpolicy="no-referrer"></p>
<p>大家应该也有遇到过按钮像案例中【删除】、【入职生效】既可以作为行内操作，也可以作为批量操作的问题。<strong>作为行内操作，优点是更便捷，；表外作为是批量操作，这样更方便的同时操作多个数据</strong>，但如果只是操作单个数据时就会增加用户的操作步骤。或者两种方式都提供，虽然更灵活但是会让页面比较冗余。</p>
<p><strong>其实怎么选择还是要根据具体业务场景来决定，首先判断这俩操作是不是高频功能</strong>。在我们的业务功能中，已入职和离职的员工在该页面不能操作删除，且【删除】是相对低频地，完全可以只提供单个删除功能。【入职生效】作为高频功能，与产品经理讨论后提供行内操作和批量操作，选择这个方案的原因是，该功能作为行内操作已上线运营了1年时间，移除会产生学习成本。</p>
<p><strong>Step 2：判断摆放位置</strong></p>
<p>批量操作常见的摆放位置有三种形式。</p>
<p><strong>方案一：和全局操作一起置于表左上方或右上方</strong></p>
<p>因批量操作需要勾选左边复选框，放置在表右上方不符合操作动效，本着效率至上的原则，此处不考虑放在右上方。</p>
<p>优点：操作项信息前置能清楚的知道有哪些功能，无需用户记忆</p>
<p>缺点：但当批量操作较多时，会挤占页面空间，导致操作按钮很多，不易查找</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/j65LRISg7UHIPRKkCUsz.png" width="1069.5" referrerpolicy="no-referrer"></p>
<p><strong>方案二：默认不显示，勾选激活后显示于表左上方</strong></p>
<p>优点：减少了相应的视觉噪音，业务拓展性强</p>
<p>缺点：有一定的学习成本，没有勾选时不知道有该操作项</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/NlEKdJTAJGZo1GlE5XI7.png" width="1069.5" referrerpolicy="no-referrer"></p>
<p><strong>方案三：直接显示于表左下方，但需勾选激活后操作</strong></p>
<p>优点：上内容下操作，符合操作动线</p>
<p>缺点：和分页放置一起不易于业务拓展</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/HIAMs6vsHgoKkc9TdFq5.png" width="1069.5" referrerpolicy="no-referrer"></p>
<p>根据我司业务，最复杂的批量操作不超过3个，是可以满足业务场景的，即使后续再有新增的批量，也可以和下钻到「更多」，<strong>综合考虑后选择方案三，放置于表的左下方。</strong></p>
<p><strong>Step 3：优化信息层级</strong></p>
<p>单行操作根据操作频率优先级为入职生效>详情>删除>编辑，其中编辑和删除属于低频操作，可折叠隐藏。批量操作-导出也是低频操作。最后定稿方案如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ooynp4T6KcDIcq3BgJu6.png" width="1131" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、结语</h2>
<p>全篇的表格文章到这就结束啦～</p>
<p>本文提供了一个表格设计基本指南，在具体项目中，你可能需要根据产品特性和用户需求进行调整，但是表格设计的原则是通用的：</p>
<ul>
<li>从用户阅读表格的目标出发设计表格的内容和布局</li>
<li>从提高用户阅读速度的功能角度出发进行表格的视觉设计，避免过度设计</li>
<li>当表格指标、数据过多时，提供一些自定义的工具帮助用户自助选择出最需要的数据条目</li>
</ul>
<p> </p>
<p>本文由 @且曼B端设计_刘美芳 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5327476" data-author="1164233" data-avatar="http://image.woshipm.com/wp-files/2022/02/sKAwxVYJStGf3iutjdn9.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            