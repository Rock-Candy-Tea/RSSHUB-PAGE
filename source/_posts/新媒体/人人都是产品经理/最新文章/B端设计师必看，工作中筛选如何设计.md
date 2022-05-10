
---
title: 'B端设计师必看，工作中筛选如何设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/CQeZuTQhfolAkYeRotCy.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 10 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/CQeZuTQhfolAkYeRotCy.jpg'
---

<div>   
<blockquote><p>编辑导读：筛选作为一个常用的功能，在B端产品设计中，筛选区的设置便于用户进行数据查询和数据定位，可以快速按照需要对数据进行查询和筛选。本文作者围绕筛选这个话题展开了分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5432147 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/CQeZuTQhfolAkYeRotCy.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>今天和大家分享的是项目改版中筛选区的功能设计。</p>
<h2 id="toc-1">一、那么什么是筛选？</h2>
<p>筛选，也可以称作过滤器，它属于搜索框架的一部分主要用于内容提取，将一类数据展示，同时一类数据隐藏，可以整合很多的组件。</p>
<p>在B端产品设计中，筛选区的设置便于用户进行数据查询和数据定位，可以快速的按照需要对数据进行查询和筛选。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/N8Sql335Ay6QSGzF4KzT.png" width="1920" referrerpolicy="no-referrer"></p>
<p>在B端产品设计中，筛选的存在对于整个表单来说是非常重要的，它可以帮助用户在表单茫茫多的数据当中进行快速的数据定位；可以对表单进行快速数据按照自己想要的方式进行划分，缩短用户对于数据的寻找时间。</p>
<h2 id="toc-2">二、筛选区有哪些展现形式？</h2>
<p>筛选区常见到的有搜索、条件筛选这二类控件。搜索和筛选虽然同在筛选区，但是二者还是有所差异的。</p>
<p>通过百度百科我们可以了解到：</p>
<p>搜索，意思指仔细查找，搜寻。</p>
<p>筛选，筛选是利用筛子使物料中小于筛孔的细粒物料透过筛面，而大于筛孔的粗粒物料滞留在筛面上，从而完成粗、细料分离的过程。该分离过程可看作是物料分层和细粒透筛两个阶段组成的。物料分层是完成分离的条件，细粒适筛是分离的目的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/U3ke4ktCpW1gKYIVZBCG.png" width="960" referrerpolicy="no-referrer"></p>
<p>在B端系统界面设计中，搜索是通过指定任意条件，系统对此条件进行的检索后，展示相对应内容，功能偏主动性；筛选是系统提供指定各种条件缩小范围，可以选择查找不同条件的内容，功能偏被动性。</p>
<p>无论被动性还是主动性，搜索和筛选这俩个功能都是让用户使用某个条件对内容进行区分，从而找到用户想要的内容。二者在功能上相辅相成，在B端系统的页面中仅靠搜索或者筛选作为内容筛选都是不够的，这就需要组合筛选区了。</p>
<h3>1. 搜索筛选</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/9lOqh8Wwje7TQVJaJYJQ.png" width="960" referrerpolicy="no-referrer"></p>
<p><strong>精确搜索：</strong></p>
<p>优点：搜索准确率高，所要即所得。</p>
<p>缺点：需要用户自己输入，然后进行查询。需要记忆搜索详细信息。输入框需要有提示输入的内容，方便用户填写，以及确认输入的类别或格式。</p>
<p>适用场景：适用于用户有清晰的目标，同时需要有查询/搜索按钮，来执行筛选。搜索需要配合筛选固有类一起使用。</p>
<p><strong>模糊搜索：</strong></p>
<p>优点：模糊搜索可以用于搜索关键字的同义词，提高搜索的精确性。字段匹配推荐搜索结果，减少记忆负担，适用于不明确的信息筛选。</p>
<p>缺点：筛选出很多类似相关的内容，需要查找鉴别所要内容，不便捷。</p>
<p>适用场景：用户对目标模糊，模糊是指不用关心输入了什么格式，哪怕错了，系统也会推荐给用户相对正确的；用户需要浏览操作过滤器提供的信息来辅助筛选达到目标。搜索需要配合筛选固有类一起使用。</p>
<p><strong>搜索的设计原则：</strong></p>
<p>关于搜索，几乎没有人不知道，哪怕是不从事设计、产品的人，他们也知道。同时每一个产品，随着规模变大，搜索一定必不可少。那么如何设计好搜索呢？有哪些原则可以借鉴，总结了以下4个方面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/BWHdibFiYeaaPhlfemXy.png" width="960" referrerpolicy="no-referrer"></p>
<p><strong>渐进呈现：</strong></p>
<p>在我们设计搜索时，可以考虑渐进呈现的方式。这是指搜索结果不要一股脑儿都塞给用户，而是使用逐步扩大的方式，让用户慢慢进入目标。但这里要注意，渐进的层级不要太深，渐进的内容要做到足够为用户着想。</p>
<p><strong>结构化：</strong></p>
<p>结构化是指搜索结果呈现的形式要有归纳和整理的意图，不能反馈给用户的是没有层次的内容。简单来说，分类就是结构化呈现的体现，内容结构化后用户查找和定位才会更快速。</p>
<p><strong>可操作：</strong></p>
<p>对于搜索结果，我们可以给予操作选择，例如收藏、分享等，这将会大大提升用户与搜索结果之间的后续联系。</p>
<p>可操作性是最佳优先的好伙伴。同时给搜索结果添加使用类操作，这会让用户专注于目标。</p>
<p><strong>可保存：</strong></p>
<p>无论搜索任何内容，用户都有权保存自己常用的搜索结果，保证用户后续无需重复搜索。这点上已经有很多C端产品做的很好了，我们在B端产品上也可以考虑起来。</p>
<h3>2. 条件筛选</h3>
<p>下拉筛选：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0B1PY7pCQb8BU3azMbgQ.png" width="960" referrerpolicy="no-referrer"></p>
<p>优点：页面的空间利用率高，同时下拉起到了很好的收纳作用，不占据页面空间。</p>
<p>缺点：由于下拉的局限性无法观看到所有的筛选字段，需要操作点击查看。</p>
<p>适用场景：下拉的筛选字段选项有限，可以明确的总结分类时，一般采用固定选项类。这种操作起来便捷，降低用户的操作难度。一般情况下需要“搜索/查询”按钮，但是也有的产品是勾选即执行的。主要需要结合具体的使用场景去判定。</p>
<p>矩阵(平铺)筛选：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/bMw1vO4Tz1ScVmWURTEO.png" width="960" referrerpolicy="no-referrer"></p>
<p>优点：用户可以直接看到筛选内容，支持输入更多筛选条件，减少操作步骤提高了用户筛选的效率。</p>
<p>缺点：平铺的筛选类目占据页面空间较大，空间利用率低，信息量过多都是重点等于没有重点，增加用户的决策时间，不适合选项太多的情况。</p>
<p>适用场景：平铺筛选控件的普适性为最强，当没有其他更好想法时，用平铺总是一个好的选择。需要注意的是，筛选条件不要过多（遵循7±2 法则）。</p>
<p>当确实需要支持大量的筛选条件时，有两种解决方案可供参考：</p>
<ol>
<li>用户自行配置筛选条件：对用户来说，单次筛选会用到的条件是有限的；通过可配置的筛选条件，实现检索效率和信息噪音的平衡，对于用户自定义项的体验与应用都有更好的支持。</li>
<li>隐藏低频的筛选条件：这种方法需要对用户需求有明确的把握，哪些筛选条件是高频、哪些是低频需要有明确的分界，优点是第一次使用时用户能更快上手。</li>
</ol>
<p>表头筛选：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/NSaYcRyw2qnzt0HJaeeP.png" width="960" referrerpolicy="no-referrer"></p>
<p>优点：通过表头的点击，简洁、直观的筛选当前表格列。</p>
<p>缺点：只能筛选当前列的内容，筛选字段比较少，筛选形式比较单一。每个表头都会有筛选的icon，影响用户对于表头的识别。表头筛选学习成本最高，且和表头排序容易冲突，筛选值展示也不够直观。</p>
<p>适用场景：表头筛选类似Excel表格的操作，是一种相对高级的交互，适合表格列比较单一内容的筛选。</p>
<p>一般来说不推荐使用，仅建议在以下几种情况考虑使用：</p>
<ul>
<li>空间是在有限或者表格非常灵活；</li>
<li>用户可能对每一列都有筛选需求（如数据报表、Excel）；</li>
<li>产品规划时对于用户筛选需求不够明确，也可通过这种模式先采集数据，分析其使用频次，对后期的界面优化进行指导。</li>
</ul>
<p>TAB标签：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/QRtYdSOpIz3ulrYBlbjq.png" width="960" referrerpolicy="no-referrer"></p>
<p>优点：筛选条件一目了然，交互步骤少，一个Tab标签代表一个纬度，平铺展示筛选内容方便识别，学习成本低。</p>
<p>缺点：Tab标签筛选字段数量有限制，不宜过多，分类需覆盖选项，并且保证每一项没有交集，空间占用多、不够灵活，对用户自定义项支持较差。</p>
<p>适用场景：Tab标签切换一般用于和时间、状态的流转有关，且没有交集的数据内容（可以是同性质，也可以是不同性质）。权重高，选项值不超过5个。</p>
<h3>3. 组合筛选</h3>
<p>在B端系统表格类页面中，字段属性很多，简单的检索方式很难准确定位到目标数据，所以在实际使用当中，常会将大量非交叉关系的属性进行罗列，搜索、筛选、TAB标签切换组合出现，形成多属性的组合检索。而筛选项互相组合，其展示方式有如下几种：</p>
<p>平铺式：</p>
<p>平铺式是将所有筛选项罗列出来平铺在页面上，可以兼容多种数据格式比如数字、文本、标签、枚举值、布尔值等，包含但不限于日期选择期、标签切换、单选框、复选框等多种控件</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ylYIQ8DiKYQJIWd76qOb.png" width="960" referrerpolicy="no-referrer"></p>
<p>优点：用户能直接看到选项内容，方便用户识别选项，且提高了用户筛选的效率（节省了筛选操作），大而全的筛选字段最大限度避免筛选条件遗漏的问题。缺点：筛选项多会占据大量页面空间，信息量过多都是重点等于没有重点，增加用户的决策时间，不利于表格数据的直观展示，此类型一般配合“勾选即执行”使用。</p>
<p>适用场景：普适性为最强，当没有其他更好想法时，用平铺总是一个好的选择。适用于从各个纬度筛选的场景，多维度筛选对信息筛选的颗粒度需求不一致，同时希望备选项被选中。</p>
<p>折叠式：</p>
<p>折叠式筛选是平铺式筛选的改进，一种简单直接的筛选形式，对平铺的筛选项进行收纳，如果多属性组合检索中的一部分检索条件不是高频率使用的，但又是必须存在的，可以通过折叠的方式将这部分筛选字段隐藏起来，高频筛选字段外露。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Y63LuhgVwNNv7A4WNZ0k.png" width="960" referrerpolicy="no-referrer"></p>
<p>优点：高频筛条件可优先快速筛选、一定程度上减少用户的认知负荷，同时占用空间较小。缺点：不好划分不同用户的高频筛选项，当高频筛选项过多时，页面同样会出现信息冗杂、空间占比大等问题。</p>
<p>适用场景：折叠低频筛选，显示高频筛选，能满足大多场景下不占用太多空间。针对有更多筛选需求的用户也有更好的引导性。</p>
<h3>4. 筛选区的布局有哪些？</h3>
<p>从位置上来说，组合筛选一般有如下几种常见类型：上下布局水平筛选区、左右布局的垂直侧边筛选区、 内嵌的的表头筛选区。</p>
<p>上下布局水平筛选区：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/4YZhON1HHQhIV2K8mNf2.png" width="960" referrerpolicy="no-referrer"></p>
<p>最常用的上下布局，筛选区放置在表格页面的上方，方便用户识别选项，提高了用户筛选的效率，明确哪些数据是用户所需的。上下布局的筛选区也方便用户进行阅读，对于那些由不同数据结构组成的页面，是一个很好的选择。</p>
<p>上下布局的筛选区的可扩展性差，当筛选项目少于五个的情况下，最常使用的就是上下布局，而当筛选项目多的时候，会占据大量页面空间，内容在较多时，推荐增加收起功能，这样保证筛选整体面积不会很大，提升屏效比。</p>
<p>左右布局的垂直侧边筛选区：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/38BznNsAgYmVv3f5d2mH.png" width="960" referrerpolicy="no-referrer"></p>
<p>左右布局的筛选区一般是以字段选择进行筛选，筛选区的位置较固定，不会因为筛选项过多而影响页面中主要内容的位置，可扩展性强，可在收起部分嵌套更多的字段值。</p>
<p>左右布局的好处就是能够将筛选的所有条件都直接的展示出来，可以适应很多场景，但是这种类型筛选器可以影响整个页面。我们需要确保页面上的每个元素都有效地受到筛选的影响，避免造成混乱。</p>
<p>内嵌的表头筛选区：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ugvWvJN1JU3vycjhFcZr.png" width="960" referrerpolicy="no-referrer"></p>
<p>表头筛选是一种复杂的筛选形式，常见于列表中，是一种列表内置筛选形式，适合表格列比较单一内容的筛选，其最开始是源于Excel的筛选形式，点击表单的筛选按钮，可以将表头的筛选字段直接带入，方便用户。</p>
<h3>5. 筛选区的反馈</h3>
<p>筛选区有两种不同的反馈模式：数据实时更新反馈和数据手动更新反馈。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/owCzQHwkBN5oaYCnG47o.png" width="960" referrerpolicy="no-referrer"></p>
<p>数据实时更新反馈：</p>
<p>界面将与所有设置的筛选相匹配并对结果进行实时更新。</p>
<p>这种模式的优点是在执行筛选时为用户提供了一种方便简单的体验，可以在每次点击后立即看到结果。适用于较低风险的交互，一旦处理多选过滤器或更复杂的输入时可能会造成混乱。当然还需要考虑处理数据的多少，如果应用中数据量巨大，每次更新时间较长，反而会降低用户的使用效率。</p>
<p>手动更新反馈：</p>
<p>在手动更新反馈模式下，过滤结果只有在用户点击查询时才会更新。如果用户想在每次更改后查看结果，必须单击查询按钮。</p>
<p>这种模式适合多纬度复杂的筛选，所有筛选字段设置完毕之后，统一执行操作，和实时反馈结果相比降低筛选等待时间，尤其是在大量数据进行筛选中，优化了用户体验。</p>
<h3>6. 筛选需要注意哪些问题</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ZvgYWucxDChB43YiwWDN.png" width="960" referrerpolicy="no-referrer"></p>
<p><strong>什么情况不适合用筛选？</strong></p>
<p>选用筛选组件的前提是信息能被清晰分类。如用户ID/电话号码，注册用户邮箱这种无明显规则的就不适合用筛选组件去查找，用搜索会更好。</p>
<p>筛选分类条件有什么要求？</p>
<p>一是分类需符合大众认知的条件。如：按照年月日的认知来选择，地理位置按照省市区街道…</p>
<p>二是要求筛选类目的分类要合理、避免晦涩难懂的文案。这决定了用户使用筛选功能的时候是否清晰无困惑。</p>
<p>高频筛选操作怎么样方便用户操作？</p>
<p>首先高频筛选操作不是产研团队自己主观臆断出来的，需要有数据支撑。很多产品为了满足用户快捷操作，会在筛选区帮用户集成常用的快捷操作入口。比如很多电商产品的新品、包邮等快捷筛选。根据不同产品用户习惯下操作整理出快捷操作入口能提高用户体验方便度。</p>
<p>筛选和搜索的区别？</p>
<p>主要区别在于用户对目标的清晰度不同，需要选用不同组件功能来达到其目的。</p>
<p>在B端系统界面设计中，搜索是通过指定任意条件，系统对此条件进行的检索后，展示相对应内容；筛选是系统提供指定各种条件缩小范围，可以选择查找不同条件的内容。</p>
<p>搜索和筛选都是让用户使用某个条件对内容进行区分，从而找到用户想要的内容。</p>
<h2 id="toc-3">三、工作中的设计思考</h2>
<p>在设计组合筛选的时候，筛选区的设计需要根据业务实际情况进行设计，考虑每个筛选字段和业务场景，来安排合理的筛选展示方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/HessjwLYkb9lziXL5BvD.png" width="960" referrerpolicy="no-referrer"></p>
<p>那么到底什么情况下使用何种筛选模式？我们在设计筛选的时候可以如何思考？显然，使用频率和界面空间是两个非常重要的评判维度。除此之外，我们还可以以可见性、系统性能和用户认知等维度去深入思考，下面将逐一分析。</p>
<p>频率：</p>
<p>使用频率是界面设计的一个重要考量因素，我们通常都会把高频使用的功能放在显眼且容易操作的位置。同理，对于筛选模式，我们也会依据筛选条件的高低频进行设计。频率除了影响使用什么模式外，还会影响筛选条件及筛选项的排列顺序，这里就不多叙述了。</p>
<p>界面空间：</p>
<p>一些界面模式的出现就为了应对界面空间不足的情况。而我们基于有限的界面空间选择合适的筛选模式是件再正常不过的事。</p>
<p>可见性太弱，当筛选条件都被收纳在一个个小小的入口按钮时，它的可见性也会随之降低，尤其在PC端，一个大屏幕下更难发现。</p>
<p>可见性：</p>
<p>既然说到可见性，不妨展开讲讲。可见性是一项重要的设计原则之一。一个明显的道理是，可见总比不可见好，但由于界面空间限制，我们不得不取舍。那么如何取舍才能保证可用性仍然友好？</p>
<p>针对筛选模式的可见性，我们可以分三个要点去考虑：</p>
<p><strong>1）筛选条件本身的可见性</strong></p>
<p>用户越难发现，即可见性越低。通常，我们都可以以使用频率来决定筛选条件的可见程度。但有时候也会失效，因为正如上文所提及，到了筛选这一步通常是颗粒度比较细的分类，否则我们可以用导航解决。但颗粒度越细，用户对信息的需求就越不一致。比如，挑一件衣服，有人希望按品牌筛选，有人希望按价格，有人希望按颜色，我们很难判断哪个频率更高。面对这种情况，只能将所有的筛选条件平铺出来供用户选择。例如，淘宝天猫等电商产品往往会使用矩阵式的筛选，而一些数据格式更多样的B端产品则直接使用输入式的筛选。</p>
<p><strong>2）筛选项的可见性</strong></p>
<p>筛选项的可见性同样影响模式的选择。页签式和矩阵式筛选的可见性比下拉式更高，因为用户可以直接看到筛选项。但筛选项一定要让用户看见吗？对于这个问题，可直接以筛选项的多少去决策（少则可见，多则不可见），比如一些B端产品，如果将备选项都全平铺出来可能一个屏幕都放不下，所以只能将所有筛选项收起。但这是一种极端的情况，缺乏说服力。</p>
<p>用户对备选项是否足够熟悉？比如对于一个尺码的下拉框，我很清楚自己能选择什么，但对于一个衣服风格的下拉框，由于我对风格不熟悉，不能预判这个筛选条件能起什么作用，很可能会将其忽略。</p>
<p><strong>3）选中项的可见性</strong></p>
<p>选中项的可见性，即当我选中某几项后再次查看选中项的难易程度。</p>
<p>性能：</p>
<p>数据量大才需要筛选，而数据量大必然会有性能问题。在不同场景下，用户会发生不同的行为，对性能的要求也会不一样。我们能经常发现一些筛选模式会带有“确认”按钮，当用户设置完筛选条件后不会即时刷新，而需点击按钮才能触发。而有的筛选模式则没有“确认”按钮。这分别对应着两种不同的场景。</p>
<p>第一种场景，如B端产品中的查询报表场景。我需要找出符合条件A、B、C的所有信息，并进行对比分析，那么我就会设置筛选条件A、B、C后一并筛选出来，这种情况是一步到位的，我不需要再额外添加条件D或E，所以有“确认”按钮的筛选模式更符合此场景。反而即时刷新会在我设置筛选条件时造成干扰。</p>
<p>另外一种场景，常见于B端产品中的查询列表场景。如果我想找到信息α，通过筛选A后得出10个信息，那么凭肉眼即可找出信息α，任务结束，但如果筛选A后得出1000个信息，我可能会再添加筛选条件B、C或D，直到筛出的信息能让我一眼分辨出信息α。换句话说，这时候我的心理模式是即时满足的，只要信息缩窄到一定范围我就会停止添加筛选条件，否则我会继续添加筛选条件。所以即时刷新能更符合此场景，但与此同时就需要考虑到性能问题。</p>
<p>另外，我们也可从变更频次和变更概率这两个维度进行思考。</p>
<p>变更频次是指用户反复使用筛选的次数，变更概率是指用户使用筛选的可能性，一般来说，高频次必然大概率，但大概率不一定高频次。而这两种情况对性能的要求是不同的。还是以报表和列表为例，在列表中，虽然很大概率会使用筛选来寻找信息，但由于用户是即时满足的，而且满足即可，所以不会重复变更筛选条件。而在报表中，虽然用户会一次性设置筛选条件，但需要分析的数据不只一种，所以会高频更换筛选项，回想一下我们去分析自己产品或竞品的日活月活等数据时，是不是会高频地切换数据来分析比对？所以，高频次的筛选就会对性能有更强的要求，而为了避免性能问题，往往也会加上“确认”按钮。</p>
<p>用户认知：</p>
<p>最难解决的其实是用户的认知问题，尤其在模式相对固定的当下，让用户适应并习惯新的模式并非易事。我们想出一些创新性的筛选模式时，不要忽略用户的认知。</p>
<h3>案例1：筛选区内容样式进化-高级筛选</h3>
<p>最近公司的系统正在进行整体迭代改版，其中涉及到很多筛选页面的改造，筛选需要适用于不同用户角色从各个维度筛选的场景，应对各种复杂的筛选情况。</p>
<p>现有的筛选形式都不完全满足于需要，从现有业务出发，筛选功能的做法，需要考虑可扩展性，满足不同用户角色不同的筛选场景需求；其中影响筛选控件最重要的是用户的使用频率，因为用户的使用频率和使用方式，直接影响到筛选的形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/kjWP2ZRAm19fWoBGQwY3.png" width="960" referrerpolicy="no-referrer"></p>
<p>如何解决不同角色不同筛选场景的需求？</p>
<p>对于不同角色不同筛选场景，我们从个性化入手，通过配置筛选来解决用户想要的筛选，是否可以根据B端系统中的角色、权限来配置？</p>
<p>这种方式可以，通过B端系统的用户角色权限，绑定筛选字段分类；这种方式看上去很美好，但是应用起来却比较麻烦，首先对于每个用户角色所需的筛选字段需要做大量的调研，做到筛选字段适用于用户，其中无法避免筛选字段与用户角色不搭配的问题。</p>
<p>其次在用户角色分配权限上，系统管理员需要配置大量的筛选权限信息，操作比较繁琐，尤其是中、大型B端系统、后台类会更加繁琐耗时，这些都不符合B端降本增效的本质。</p>
<p>既然通过角色、权限配置不可取，那么我们顺着筛选可配置的思路来考虑……</p>
<p>那么是否可以在筛选区进行个性化配置？</p>
<p>我们尝试下，在筛选区增加设置功能，放个设置按钮。</p>
<p>设置按钮已经放置了，可以设置筛选字段的排序、可以开启、关闭筛选字段。不同的用户可以根据自己的需要设置个性化的筛选区，这就是高级筛选，解决了不同角色不同筛选场景的需求。</p>
<h2 id="toc-4">四、总结</h2>
<p>关于筛选区的文章到这就结束啦～</p>
<p>本文介绍了关于筛选区的一些内容，在具体项目中，你可能需要根据产品特性和用户需求进行调整。我也只是将自己的一段时间的工作进行总结，说的不正确，欢迎大家指正。</p>
<p>正文结束。</p>
<p>推荐：</p>
<p>B端产品垂直性比较强，这里推荐一些B端设计师和页面设计推荐，多看多积累。</p>
<p>1、🔍 Filters-Fintoryhttps://dribbble.com/shots/16154972–Filters</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/DONDa3LCBLVHydySA9KG.png" width="750" referrerpolicy="no-referrer"></p>
<p>2、Advanced Search & Filters for Mylagro-Gapsy Studiohttps://dribbble.com/shots/15232468-Advanced-Search-Filters-for-Mylagro</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/9EAI5kayU5HKD2FikI65.png" width="750" referrerpolicy="no-referrer"></p>
<p>3、Advanced Filters-UXDNhttps://dribbble.com/shots/14585643-Advanced-Filters</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ckjdU36YjpBp7WdIZ0ji.png" width="750" referrerpolicy="no-referrer"></p>
<p>4、Advanced Filtering-Jon Moorehttps://dribbble.com/shots/15656463-Advanced-Filtering</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/lPZOZOeKJL1oGRa5PY2O.png" width="750" referrerpolicy="no-referrer"></p>
<p>5、Filters-Eugen Eşanuhttps://dribbble.com/shots/14953107-Filters</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/HB6Pg2IC0DkSvzb2EXfa.png" width="750" referrerpolicy="no-referrer"></p>
<p>6、himalayas.app — filtering 2.0 🏔-Jordan Hugheshttps://dribbble.com/shots/16032266-himalayas-app-filtering-2-0</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/0nNEUR2d04OdBphRTvKk.png" width="750" referrerpolicy="no-referrer"></p>
<p>7、Filtering Component + Table Exploration-Micah Carrollhttps://dribbble.com/shots/15899953-Filtering-Component-Table-Exploration</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/zYqDn7lBm7L0xNVrVypS.png" width="750" referrerpolicy="no-referrer"></p>
<p>8、Folders and Filters-Liam Boltonhttps://dribbble.com/shots/15193780-Folders-and-Filters</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/nCVczZlT6YQ3yVmESXsv.png" width="750" referrerpolicy="no-referrer"></p>
<p>9、Material X design system UI kit – Figma Multiselect-Setproducthttps://dribbble.com/shots/14424197-Material-X-design-system-UI-kit-Figma-Multiselect</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/QQm831bOjWrP7FvhEN7E.png" width="750" referrerpolicy="no-referrer"></p>
<p>10、Manage Custom Filter-Eugen Eşanuhttps://dribbble.com/shots/15481814-Manage-Custom-Filter</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/AD1ZCQGlPewtPIEIu239.png" width="750" referrerpolicy="no-referrer"></p>
<p><strong>参考链接：</strong></p>
<p>CE青年《B端设计指南01-是啊选》https://www.zcool.com.cn/article/ZMTA1NjAzMg==.html</p>
<p>Hi_Nick《数据表格设计》https://www.zcool.com.cn/article/ZMTIwMjg4NA==.html</p>
<p>小鹿lp《B端体验设计主题-表格篇》https://www.zcool.com.cn/article/ZMTIwNzUxMg==.html</p>
<div>本文由郝小七指导<a href="http://www.woshipm.com/u/917803" target="_blank" rel="noopener noreferrer">http://www.woshipm.com/u/917803</a></div>
<div></div>
<div>
<p> </p>
<p>本文由 @Color可乐 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
</div>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5431711" data-author="786642" data-avatar="http://image.woshipm.com/wp-files/2018/11/HRhabM6ZW7TSLWfW3Drk.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            