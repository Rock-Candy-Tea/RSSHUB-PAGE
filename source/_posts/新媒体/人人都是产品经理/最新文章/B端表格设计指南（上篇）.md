
---
title: 'B端表格设计指南（上篇）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/rry9yxxrscVkmIAqc3ZU.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 22 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/rry9yxxrscVkmIAqc3ZU.jpg'
---

<div>   
<blockquote><p>编辑导读：表格是展现数据最为清晰、高效的形式之一，它也是B端产品和设计师每天接触最多的组件，常和排序、搜索、筛选、分页等其他界面元素一起协同。本文作者总结了一套B端表格设计指南，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5327097 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/rry9yxxrscVkmIAqc3ZU.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>大家好，我是小鹿，周末来小小的充个电吧～今天为大家分享的是<strong>「B端典型页面-表格（上篇）」</strong>，文章将从概念和结构拆分为以下四个部分为大家进行全方位的解读复盘。</p>
<p>01 表格的概念</p>
<p>02 数据查看-显</p>
<p>03 数据筛选-查</p>
<p>04 数据操作-增删改</p>
<p>因篇幅较长，考虑到大家的阅读体验，本篇将从前两个部分<strong>「表格的概念」</strong>和<strong>「数据查看」</strong>结合实际案例进行分享。</p>
<h2 id="toc-1">一、表格的概念</h2>
<h3>1. 表格的特点</h3>
<p>表格是展现数据最为清晰、高效的形式之一，它也是B端产品和设计师每天接触最多的组件，常和排序、搜索、筛选、分页等其他界面元素一起协同。在企业级中后台中，常应用于：</p>
<p><strong>一次性浏览大量信息</strong>-很多图表类型无法展示数据特点，而表格是组织大量信息通用性最高的一种表达方式，既可陈列信息，又可以表达信息之间的关系；</p>
<p><strong>信息之间需对比</strong>-表格的归纳与分类，便于用户快速查询其中的差异与变化和关联；</p>
<p><strong>快速确定并执行多种复杂操作</strong>-如对信息进行搜索、筛选、增删改等。</p>
<h3>2. 表格页的构成</h3>
<p>通常表格的组成元素以及相关元素会有多个部分，根据不同粒度的用户目标将其解构为三部分：</p>
<ul>
<li><strong>数据查看</strong>：表格的核心-显，用户用来阅览、对比和分析数据</li>
<li><strong>数据过滤</strong>：辅助作用，承载表格的查功能，将数据过滤，方便用户快速查询定位数据，一般位于表格上方</li>
<li><strong>数据操作</strong>：辅助作用，承载表格的增删改的功能，比如常见的“新增”、“删除”、“编辑”按钮。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/85yuSElODjOorirkOraB.png" width="1197" referrerpolicy="no-referrer"></p>
<p>从用户目标来看，表格页的终极目标是查看，所以我们按照数据查看、数据过滤、数据操作的顺序来对表格页进行讲解。</p>
<h2 id="toc-2">二、数据查看-显</h2>
<p>数据查看区主要由表头、行、列、单元格五个部分组成。</p>
<p><strong>表头</strong>：说明数据的内容，可以包含筛选、排序等功能起到数据解释作用</p>
<p><strong>行和列</strong>：对本行/本列数据的描述，可以理解为是表格的骨架，是用户快速扫描并接收表格布局的关键要素</p>
<p><strong>单元格</strong>：表格的主体内容，承载用户的每一条数据，也是整个表格的核心</p>
<p><strong>分页器（不一定有）</strong>：分隔长列表的组件，每次只加载一个页面</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Y5veM0Ajm62noMRibYc4.png" width="1237.5" referrerpolicy="no-referrer"></p>
<p>对表格元素庖丁解牛后，小编将通过<strong>八个点</strong>：视觉风格、表格构成（表头、行、列、单元格、分页器）、基础交互和详情查看，<strong>三原则</strong>：信息降噪、呼吸适中、高效易读</p>
<p>来对表格设计一一拆解</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/rbu72qgbSlHix62ieg5I.png" width="1071" referrerpolicy="no-referrer"></p>
<h3>1. 视觉风格</h3>
<p>表格中所承载的数据信息才是主体，在进行表格设计时，尤其要注意去除所有非必要的视觉元素，让用户将注意力集中在数据信息上，而不是无关的边框、底色等。</p>
<p><strong>1.1 去掉不必要的分割线和斑马纹</strong></p>
<p><strong>去掉竖向分割线</strong>：水平分割线能显著减轻长表格在垂直方向的视觉重量，加快大量数值的对比工作。</p>
<p>而竖向分割线的作用是即使缩减元素之间的距离也能区分不同元素，但如果使用了合适的对齐方式分，竖直分隔线就会很多余的。即使要用，也要非常淡，不能妨碍快速浏览。</p>
<p><strong>不使用斑马线</strong>：数据量不大且易分辨的情况下，斑马线在很多时候也是没有必要的，因为它们是同一类数据，而且水平分割线就已经能够明显区隔。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/zuL2VT5ogjDGhj63iZ7h.png" width="1545" referrerpolicy="no-referrer"></p>
<p><strong>1.2 分割线样式轻盈</strong></p>
<p>分割线的样式尽量轻盈，无关的边框不要抢视觉，数据才是主体，突出内容。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/xPiCkuGE1Iz7jef85rbP.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>1.3 减少图形元素的使用</strong></p>
<p>去掉不必要的装饰和颜色，如icon、标签等，虽然能够帮助组织数据、更直观的传达信息，但物极必反，少即是多，要注意克制这些元素的使用。标签能用线性就不用面性，做到轻盈，否则表格中最重的就是标签。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/g5BaNgGvdakVWawse3He.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>1.4 字体降噪</strong></p>
<p>在产品的品牌设计中，字体是规范中的重要一环。然而在设计表格时，简约至上才是关键，尽量避免任何装饰性字体。虽然文本不能够建议你具体使用哪种字体，但数字<strong>建议使用Helvetica Neue、Helvetica等其他等宽字体</strong>，文本最好不要出现以下情况</p>
<p><strong>不要出现衬线字体</strong>：因为个性会产生阅读噪音，不利于用户对数据的理解和思考。</p>
<p><strong>不要出现全大写字体</strong>：因为它很难读，需要转化思维。</p>
<p><strong>不要出现使用斜体</strong>：易引起视线疲劳，影响阅读。</p>
<p><strong>不要出现多种字体</strong>：保持风格统一。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Q33aTVUHVW2if5Ejk33v.png" width="1071" referrerpolicy="no-referrer"></p>
<h3>2. 表头</h3>
<p>根据表头的复杂程度，可以分为以下三类类型：</p>
<ul>
<li><strong>纯文本表头</strong>：仅起到解释数据属性的作业</li>
<li><strong>多功能表头</strong>：含筛选、搜索或排序等相关操作</li>
<li><strong>分组表头</strong>：信息分类层级较多的情况下使用，表格需要采取带竖向分割线</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/aNsRMWsKGYEjjVb036yN.png" width="1665" referrerpolicy="no-referrer"></p>
<p>而在表头设计过程中，有以下3点需要注意：</p>
<p><strong>2.1 精简表头-少一字不可</strong></p>
<p>表头在能够概括的情况下，尽量简炼、准确，一般可根据上下文关系来进行减短简化，以达到节省表格头部空间和减轻视觉压力的作用。</p>
<p>一个简单的检验表头是否精简的方法是：少一个字不可，通俗易懂的说法就是字数再精简用户就不明白意思</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/knJwriMCE2YmEs3n2I6Q.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>2.2 定义专有名词</strong></p>
<p>对于比较复杂的表头，可以定义一个专有名词，鼠标hover上去对专业术语或用户不常见的名词给予该字段的详细解释，同时满足新手、普通、专家用户的需求。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ukt3zjN4Icb7t9EgapVa.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>2.3 情况允许时，去掉表头</strong></p>
<p>如果表格数据可以自我解释，表头就不是必须的。如电子邮件的表格，就不需要表头，因为发件人和邮主题的区分度比较高。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/L2KbJG9zvpNyPhAIzKdI.png" width="1439" referrerpolicy="no-referrer"></p>
<h3>3. 单元格</h3>
<p><strong>3.1单元格高度</strong></p>
<p>在开发同学的眼中，<strong>单元格高度=内容高度+上间距+下间距</strong>，在实现设计稿时，通常也是按照这个方式来写的，而不是像设计同学一样按照文字的尺寸来计算间距。其中，文字行高建议设为字号的1.5倍，上下间距设为字号的1.2倍。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ND2lGK48b5MdSS26NlE1.png" width="1272" referrerpolicy="no-referrer"></p>
<p>当然，在很多很多通用化产品中，存在多个设备屏幕分辨率的差异，为了让每一个分辨率下的产品都能够有较好的展示效果，可设置<strong>舒适、标准、紧凑</strong>三种高度来满足需求，提供切换按钮让用户自己控制显示密度。</p>
<p><strong>3.2 单元格截断规则</strong></p>
<p>工作中常常会遇到单元格数据过多的情况，常见的方法有两种：</p>
<ul>
<li>定义一个单元格长度或字数限制，<strong>超过该范围以”…”显示</strong>，鼠标悬停时出现气泡显示完整内容。</li>
<li><strong>折行</strong><strong>显示</strong>，这种方法让平铺直叙，让用户可以直接了当的看到所有信息，在B端使用层面上还是不错的，建议不要超过三行，超出可“…”显示。</li>
</ul>
<p>数据过多时，单元格长度如何定义？超过哪个范围“…”显示呢？</p>
<p>定义长度的依据：<strong>根据业务字段，防重复</strong>。保证用户在扫视的时候，对重要字段能快速区分、对比。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/QSnvDUuQUpCgHZBODi8Q.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>3.3 不留空白格</strong></p>
<p>当表格单元格中没有相应数据时，要避免直接留出空白单元格。空白格容易造成用户的困惑甚至误解，用户会搞不清楚到底是没有数据，还是根本没有值？</p>
<p>正确做法是，<strong>数据不存在</strong>（数据库中没有该字段）<strong>用“-”</strong>，<strong>没有数量</strong>（数据库中有该字段）<strong>用“0”</strong>，且小数点后位数、单位，都要与上下单元格保持一致。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/B3GEskF2480eieCGTymS.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>3.4 收起低频操作</strong></p>
<p>对于单条数据操作频繁的场景，当超过三个操作项时，操作低频折叠收起。这样做的优点是界面简洁明快，信息密度低，可以帮助页面突出更加重要的信息，减轻空间压力，减少干扰。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ljA9al9uHIjxyWNMlKsY.png" width="1272" referrerpolicy="no-referrer"></p>
<h3>4. 行的设计</h3>
<p><strong>4.1 对齐方式</strong></p>
<p>多行情况下，居中和顶部对齐都是可以的。不过小编建议采用顶部对齐，考虑到一行类不同的单元格会有行数不一致的情况，比如有个3行数据，有的只有一行，这个情况下居中对齐信息的阅读效率不如顶部对齐效率高</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/nIS4Ro8ZDHUAmo8Tf6bg.png" width="1797" referrerpolicy="no-referrer"></p>
<p><strong>4.2 默认行排序</strong></p>
<p>新增一条数据后，这条数据应该被放在表格的哪里呢？这是个和表格默认排序有关的问题。</p>
<p>表格数据应该默认按添加的时间排序，还是应该按某个字段的名称排序？</p>
<p>如果我们默认按某个字段排序，比方说岗位列表里增加一条“广深常温B2C 叉车员”的字段，而首字母G的数据在表格中极大概率不靠前。这时就会出现一个问题，用户要在茫茫数据中找到刚增加的那一条数据，或者用户根本不知道自己增加的数据已经被插入在了表格里了，这会让他们觉得自己的操作失败了。</p>
<p>解决这个问题的一个方法就是按照数据添加时间排序，<strong>默认最新创建的在最上面</strong>，体验上创建完反馈，马上就出现了变化，且针对最新数据的操作频率较高，方便用户发现与查找。同时也可以用带排序的表头，让用户自定义排序。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/GokvLhRqhvG2TWOrf4QF.png" width="1272" referrerpolicy="no-referrer"></p>
<h3>5. 列的设计</h3>
<p><strong>5.1 合适的列间距</strong></p>
<p>合适的填充和边距对于视觉设计至关重要，以保证易读性。定义列的间距时，我通常的做法是<strong>N1保持不变，将N2定义一个最小值，N2再根据表格的宽度自适应变化</strong>。</p>
<p>表格主要适配到这个最小宽度，这一步骤通常的设计系统的初期就要完成，一方面可根据自己项目目前情况，按照导航宽度等固定尺寸确定最小的表格宽度，这样在处理最小尺寸时，可以有一个明确的边界，同时能与开发同学进行理解沟通。<strong>当表格宽度大于页面宽度，固定首尾列，左右滑动</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/2j7CAo9TSIlQQ2LhVdRX.png" width="1276.5" referrerpolicy="no-referrer"></p>
<p><strong>5.2 控制列数</strong></p>
<p>基于对实际业务需求、目标用户诉求及其行为的理解，<strong>列数尽量控制在7±2</strong>，列举用户更为关注的数据，用户需要的非重点、辅助性信息可以在详情中展示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MfUj1LAIWEMV3YpFgOhL.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>5.3 自定义列</strong></p>
<p>如果不同用户想看到的信息侧重不同，可以让用户自定义列的展示。<strong>在默认情况下仅展示最常用、最重要的几个指标</strong>（如下图）。这样做的好处是：</p>
<p>首先，用户能在表格上方看到所有的指标名称，避免了原来需要横向拖拽才能浏览到所有指标的情况；</p>
<p>其次，用户可以根据自己的需要，自由的选择显示所需指标，隐藏不必要指标，减少干扰。但需注意<strong>系统应记住用户上一次的自定义列设置</strong>，减少用户重复操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Wmw6NezwTcLfQQtJBPxD.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>5.4 合适的对齐方式</strong></p>
<p>合适的对齐方式能够提升数据的浏览效率。表格内信息的纵向列对齐（符合格式塔心理学中相近原则）能够很好的形成视觉引导线。通过对齐，会让表格更加规范易理解，给用户视觉上的统一感，视线流动更顺畅，让用户快速的捕捉到所需内容。</p>
<ul>
<li><strong>文本左对齐</strong>：更高效的阅读浏览顺序，包括非比较型和固定长度的数字，如日期2020-12-04（补0是数字书写规范）、编号1948696等；</li>
<li><strong>数值右对齐</strong>：金额、长度、高度等，数字是从右往左读的，通过数值位数的长短即可对比数值的量级和大小，方便数值的比对。这是因为在对比数字时，首先看个位，然后十位、百位等；</li>
<li><strong>操作右对齐</strong>：操作即使没有纵向分割线也能很好的起到分隔的作用，视觉上看表格是一个方方正正的格子，比较整齐</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/4GpvN5o5vwtgEYR00fN2.png" width="1272" referrerpolicy="no-referrer"></p>
<h3>6. 分页器</h3>
<p>在Web端，数据量动辄上万条，容易出现浏览器响应太慢或者浏览器内存溢出的情况。使用分页器有哪些优点呢？</p>
<ul>
<li>分页可以<strong>缓解服务器的加载压力</strong>，每翻一页加载该页的页面，缩减单次加载的数据量来缩短等待加载的时间，从而达到少量多次的高效体验。这就是为什么哪怕是移动时代了，很多表格还是使用分页组件。</li>
<li>分页可以跳跃查看数据，灵活性更高、步骤更短。</li>
</ul>
<p>表格设计大原则是整张表不要超过一屏，每一页的默认行数：10行以上，减少翻页的次数。但考虑到每个用户的使用习惯，在给出默认行的数量后，可以让用户自定义每页的显示的数量，相比于跨屏翻页而言，向下滚屏会更便利。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TzVBNepTDrY8R4Frtxcq.png" width="718.5" referrerpolicy="no-referrer"></p>
<p>2个小tips：</p>
<ul>
<li>当表格数据无数据时，翻页控制按钮不可见。</li>
<li>当表格数据条数小于10条时，翻页控制按钮不可见</li>
</ul>
<h3>7. 详情查看</h3>
<p><strong>7.1 详情入口</strong></p>
<p>详情查看可以分为点击详情、跳转（显性和隐性）三种方式。</p>
<ul>
<li><strong>详情</strong>：在操作列中增加“详情”功能，点击查看详情。</li>
<li><strong>显性跳转</strong>：把 ID、名称等唯一性标志的字段加上超链接</li>
<li><strong>隐性跳转</strong>：默认不显示链接色，鼠标hover上去才显示链接色，点击可以查看或直接点击除操作外的单元格查看（如飞书管理后台）</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/D2lmGBXEEUG76PrbJZ1H.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>7.2 详情交互</strong></p>
<p>关于表格详情查看的展现形式，按可承载的信息量由少到多依次分为折叠展开、弹窗、抽屉、及新增页面四种类型。</p>
<p><strong>a. 折叠展开</strong></p>
<p>直接在表格里展开（可以是详情，也可以是二级表格），无需打开新页面即可查看附加信息，防止用户迷失。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/mrp2zHqvp0prKG905wZ1.png" width="1272" referrerpolicy="no-referrer"></p>
<p><strong>适用场景</strong>：信息量较少的情况</p>
<p><strong>b. 弹窗</strong></p>
<p>弹窗是一种中断用户当前操作并对其进行补充、或者对当前操作进行强制反馈的交互形式，需要用户进行强交互，它可以保留用户当前进程的情况下，指引用户完成一个特定的操作。主要分为模态弹窗与非模态弹窗两种形式：</p>
<p><strong>非模态弹窗：</strong></p>
<p>通常这类弹窗只会在屏幕上短暂停留，几秒就会消失，也因此用户感受不到他的存在。它的缺点也非常明显，展示时间较短，不适合展示重要信息、不能承载大量文案。在详情查看页面中并不适用，此处就不再进行拆解。</p>
<p><strong>模态弹窗：</strong></p>
<p>位于浏览器的主页面核心区域，需要用户对它做出相应交互，弹窗才会消失。</p>
<p><strong>优势</strong>：通过全局的半透明黑色能够让用户更加聚焦，集中精力去处理好当前事情，能够通过透明度展示背景，让用户了解到自己并没有离开当前页面</p>
<p>劣势：打扰用户，感到强烈的中断的感受</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/H80u9aq0AlNsYIyUtfbt.png" width="1000.5" referrerpolicy="no-referrer"></p>
<p><strong>适用场景</strong>：数据详情体量不大，页面内容较轻时。同时，不需要参照上级页面内容，有快速回退的诉求。</p>
<p><strong>c. 抽屉</strong></p>
<p>侧滑抽屉相比弹窗减少了页面层级和隔离感，有较强的连贯性，适合与原页面具有连贯结构的内容的展示。单击行链接将表格转换为左侧的列表项目和右侧的其他详细信息，这让用户能够解析大型数据集，而且在涉及到多个项目时不会丢失位置。可<strong>自定义上下左右四个方向，一般右侧滑出最为常见。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/y1Ne72rw5NjAtYsuCuoN.png" width="1000.5" referrerpolicy="no-referrer"></p>
<p><strong>适用场景</strong>：详情页的内容较多时，且有快速切换主体的诉求。</p>
<p><strong>d. 新增页面</strong></p>
<p>新增页面几乎是万能的，无论页面内容量是多少、页面间是否连贯、以及使用频率怎样，都可以使用。新增页面又分为：覆盖当前窗口以及新窗口跳转两种形式，在场景上可以根据两者差异进行选择。</p>
<p>在详情查看中，二级页面使用频率是非常高的，需要用户在A与B页面之间进行来回切换，这时候考虑页面反复出现是否流畅，是否有切换成本的产生，本着产品效率至上的原则，新增的页面建议新开一个窗口跳转而非覆盖，如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TyoRA88JM6gECAAPhVDS.png" width="1000.5" referrerpolicy="no-referrer"></p>
<p><strong>适用场景</strong>：当详情页承载内容过多且里面的操作相对复杂时，如详情页内有表格的嵌套和特别多的操作</p>
<h3>8. 基础交互</h3>
<p><strong>8.1 表格滚动</strong></p>
<p>表格滚动方式有表头固定和列固定两种，比较复杂的表格可同时采取表头和列都固定的情况</p>
<p><strong>表头固定</strong> ：适合列表滚动加载时，适合浏览场景</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/9u46NBK24HTl4ohMEi3u.png" width="1250" referrerpolicy="no-referrer"></p>
<p><strong>列固定</strong> ：适合列表项较多时 ，需要左右滑动时。比较常见的是首尾固定，当时也可以按照业务要求首列或者尾列固定，或者说表格前两列业务都需要看到，则可以固定前2列</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BqTFEOkU2P8cImiLuwh1.png" width="1250" referrerpolicy="no-referrer"></p>
<p><strong>8.2 加载</strong></p>
<p>表格中的复选框、折叠图标，操作按钮等遵循组件本身的加载规则。</p>
<p>加载机制根据实际业务中的数据量来决定是全量加载还是分页加载。</p>
<p>加载样式循序对应规则：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/twX9g9vfCFRREE5FPAaX.png" width="1250" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、最后</h2>
<p>以上就是<strong>「B端典型页面-表格」</strong>上篇的全部内容啦～～</p>
<p>后续会为大家分享<strong>数据筛选、数据操</strong><strong>作</strong>等一系列的设计知识点，希望能给正在从事或准备入局B端的的小伙伴带来启发和帮助。</p>
<p> </p>
<p>本文由 @且曼B端设计_刘美芳 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5323117" data-author="1164233" data-avatar="http://image.woshipm.com/wp-files/2022/02/sKAwxVYJStGf3iutjdn9.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            