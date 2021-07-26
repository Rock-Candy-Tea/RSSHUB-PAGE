
---
title: 'B端产品设计细节分析：数据筛选'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/9jNsCmhAE5QcX7Pz3tGl.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 26 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/9jNsCmhAE5QcX7Pz3tGl.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端产品设计中，数据的筛选是其中必不可少的一个步骤。数据的筛选并不仅仅是一个简单的步骤，它包含了很多设计的细节，我们一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4936268 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/9jNsCmhAE5QcX7Pz3tGl.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是筛选</h2>
<p>筛选（Filter）也叫做过滤器，是搜索框架中的一部分，用于数据抓取。</p>
<p>可以通过添加不同的属性来创建筛选组件，用户选择其中某个属性并定义其值。一个属性可以有一组可供选择的值，例如设备平台可以分为PC、IOS、Android等。</p>
<p>用户可以根据需要，对数据进行有规律的抓取，快速查找出特定内容，准确缩小数据的展示范围。并且可以定义并保存筛选以备后用。执行筛选后，用户也可以查看结果并进一步缩小结果的范围。</p>
<p>大多数B端产品数据复杂，数据内容通常都是由用户添加生成的，经常会有项目标题过长、自定义字段无规律、数值复杂的情况，筛选就显得尤为重要了。</p>
<h3>1. 使用场景</h3>
<p id="u4ee9ce49">只要用户有需要找到屏幕中任何相同元素的需求，都可以用到筛选，常见的使用情况有：</p>
<ul>
<li id="ue56158f6">数据列表、卡片列表等任何列表类型的页面，用于筛选可见项目的数量。</li>
<li id="u64188211">分析类型的屏幕和仪表板，用于筛选图表中包含数据的范围或类型（时间范围、受众类型、显示的指标、价值范围等）。</li>
</ul>
<p id="u0045bb9b">不管使用场景如何，其目的都是让用户对数据进行区分，找到想要的内容。流畅的筛选功能交互，可以减少用户的负担，使其将更多精力放到处理筛选后的数据中。同时，筛选属性还可以用于向用户介绍整个系统可以提供的内容。</p>
<h2 id="B1LXc">二、筛选项的类型</h2>
<p id="u71b37433">在构建筛选时，需要非常了解产品的数据结构。哪些字段与时间或日期有关？哪些是定量值、哪些是定性值？不同类型的数据需要不同类型的选择输入，所有数据点都可以反映在筛选器中。</p>
<h3 id="KK0sg">1. 日期</h3>
<p id="u659f2212">日期是B端产品中常见的筛选类型，一个场景事件的触发离不开时间选择。</p>
<p id="ua64df285">日期选择器是让用户在程序中选择日期或时间段的一类控件，其作用是查询过往时间发生的事情。通常根据用户习惯设置一个默认时间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BASZXBrYGjwhkbRZivEW.png" alt width="858" height="367" referrerpolicy="no-referrer"></p>
<p id="u2eb183f8">一个好的日期选择器，需要注意：</p>
<ul>
<li>确保开始日期和结束日期按顺序排列。</li>
<li>所选内容必须可见，对于已选的时间段需要有明显的样式区分。</li>
<li>通常根据用户习惯设置一个默认时间，如今天。</li>
<li>添加快捷选项和自定义选择。选择时间范围时，快捷选项是非常有用的。根据场景特征，增加昨天、最近7天、最近30天等快捷项。但是，如果用户寻找的内容快捷选项未涵盖，则允许他们设置自定义选择。</li>
</ul>
<h3 id="guoHr">2. 状态</h3>
<p id="u56556033">B端业务复杂，操作人员角色分工各不尽相同，根据实际的业务流程，同一条数据可能会产生多个状态节点。操作关联到系统的数据时，会触发状态的变更。状态字段常用于列表中，可以让用户追踪定责到具体环节，方便任务的交接。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/CH2uFHrrPDJ8CdlMvaHQ.png" alt width="823" height="387" referrerpolicy="no-referrer"></p>
<h3 id="tEI9B">3. 字典</h3>
<p id="ud7c60532">用户通过选择的方式录入系统预先配置筛选项信息时，可以使用字典格式。例如，标签类字段：性别男、女，架构类字段：省、市、区等。</p>
<p id="ua8177660">字典类字段的值较固定，涵盖范围广，用户可以通过确定性内容选择范围，提高筛选效率。</p>
<h3 id="yvf0o">4. 多条件</h3>
<p id="u6bf583c0">列表中最常见的两种字段内容是文本类和数值类字段，若想要精确的筛选这一类字段内容，需要提供含有运算符的筛选操作，常见的筛选操作有：等于、不等于、大于、小于、区间、有值、没值等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/p256vPTDl5JSGSfiw6UR.png" alt width="794" height="412" referrerpolicy="no-referrer"></p>
<h3 id="xFxLN">5. 联动</h3>
<p id="ubdbd5b4d">联动主要是指界面上的控件之间发生互相关联的变化，比如选择了某个值后，其他筛选项随之发生变化。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/RdI7kZNXcsAEEJSAvRQf.png" alt width="836" height="661" referrerpolicy="no-referrer"></p>
<h3 id="YlzyA">6. 高级筛选</h3>
<p id="ub274cbea">高级筛选是把筛选变成附加公式，而不是简单地一个值。</p>
<p id="ub88d9f73">在这种情况下，不仅可以让用户控制相对关系，还可以允许他们通过添加或排除条件来创建复杂的公式。通常有并级“且”、交级“或”两种关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/iHNs20DFUv4SQyXST5Qo.png" alt width="845" height="309" referrerpolicy="no-referrer"></p>
<h3 id="gyBtD">7. 筛选项优先级排序</h3>
<p>通常在用户眼中，不是所有字段都具有相同的可用性价值，不同的字段在不同使用场景中的重要程度也不一样。我们需要为高使用频率属性值在筛选组件中更快被访问。</p>
<p>所以在得到可能成为筛选的属性后，需要根据业务需求的重要程度，对所有可成为筛选项的属性做优先级排序。评估出需要实现哪些筛选项，排除哪些筛选项，哪些优先实现，哪些靠后实现等。</p>
<p>除此以外，还可以根据业务需求，对筛选进行分类。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/8zfOgVlKEXpPuoaWpqwH.png" alt width="845" height="299" referrerpolicy="no-referrer"></p>
<h2 id="pNfRZ">三、筛选的设计</h2>
<h3 id="j9rhz">1. 位置</h3>
<p id="u52c87875">筛选器组件的位置有三种常见的类型。一是左侧的垂直侧边栏形式，二是水平的筛选栏，三是嵌入到某个数据卡片或表头的并列形式。选择哪种类型取决于筛选对上下文的影响和产品的扩展性要求。</p>
<p><strong>（1）侧边栏</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bjWDoTwa3kMoDlXlrcwZ.png" alt width="851" height="612" referrerpolicy="no-referrer"></p>
<ul>
<li>全局影响：整个页面</li>
<li>可扩展性：高</li>
</ul>
<p>左侧边栏位置较固定，不会因为筛选项过多而影响页面中主要内容的位置，可扩展性强，可在收起部分嵌套更多的值。</p>
<p>但是这种类型筛选器可以影响整个页面。我们需要确保页面上的每个元素都有效地受到筛选的影响，避免造成混乱。</p>
<p><strong>（2）水平栏</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xSHnoVck4IjRsJldVeB2.png" alt width="832" height="771" referrerpolicy="no-referrer"></p>
<ul>
<li id="udbbb8b55">全局影响：可能影响整个页面，也可能影响页面中的某一部分</li>
<li>可扩展性：一般</li>
</ul>
<p id="uf99c0454">筛选栏可以放置在页面的特定部分的上方，明确表示只有那些项目才会受控。对于那些由不同数据结构组成的页面，是一个很好的选择。</p>
<p id="u5cf0f248">水平栏选项的可扩展性稍差，因为它局限于页面宽度。筛选内容较多时，最好有收起功能，提升屏效。</p>
<p><strong>（3）并列</strong></p>
<p id="u509e9456"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/fMn3wGEq3i9X73ChfxLv.png" alt width="835" height="585" referrerpolicy="no-referrer"></p>
<ul>
<li>全局影响：只影响某个部分</li>
<li>可扩展性：低</li>
</ul>
<p>并列形式常见于列表中，是一种列表内置筛选形式，类似Excel表格的操作。点击表头筛选按钮进行筛选，可以将筛选字段直接带入表头标题中。</p>
<p id="ube40e3a1">如果产品数据结构不一致（如各种图表、图形组成的仪表板），需要谨慎使用全局筛选，这个并列的形式可能更合适。可以在页面级别保留一些全局筛选，但也需要提供较小规模的筛选机制。</p>
<p id="uade40222">这种类型为用户提供了快速进入筛选的通道，但是筛选的图标各平台不一，会影响用户对表头的识别。</p>
<h3>2. 初始状态</h3>
<p><strong>（1）展开/折叠</strong></p>
<p>筛选较多的页面，考虑到屏效性，可以使用折叠/展开的形式，避免页面滚动影响用户操作效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/LUZgRxFMXOW8stl5abO8.png" alt width="716" height="1005" referrerpolicy="no-referrer"></p>
<p>如果界面筛选中没有默认的值，用户必须通过设置一个筛选以获取表的第一个结果集，则默认展开筛选栏。</p>
<p>如果界面在加载时执行的默认值，图表内容已预先填充内容，并且用户很少更改筛选栏，则界面可以默认折叠筛选栏。而如果筛选功能的使用频次不高，可将他它隐藏在下一个层级中，为关键信息预留更多位置。</p>
<p><strong>（2）平铺/弹出</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/TKQLIeGBHPyxFLfpJwLX.png" alt width="827" height="859" referrerpolicy="no-referrer"></p>
<p id="ud40c27fb">平铺筛选在B端产品中较为少见，它将筛选项全部罗列在当前页面内，用户可以直观对比各个选项，操作便捷，但是也有一定限制。这种类型展现条目本身必须可以标签化，条目的字节数受限，不可过长。如果筛选条目数量太多，甚至多到一屏放不下，需要考虑弹出式筛选。</p>
<p id="u39036c4a">弹出式的典型样式是下拉列表，当筛选条目数量较多时，给出一个额外的空间更有利于操作。对于多层级的信息（如省、市、区）弹出式也更为友好。</p>
<h3>3. 执行时间</h3>
<p id="u7aa11a9d">过滤器栏有两种不同的模式：实时更新模式和手动更新模式。</p>
<p><strong>（1）实时更新</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/KJp6Vu7gEMkoG0cY5BVR.png" alt width="889" height="161" referrerpolicy="no-referrer"></p>
<p id="ub6359d4e">在实时更新模式下，筛选栏会立即对每个输入更改做出反应。一旦用户做出选择，数据就会刷新并显示筛选结果，因此不需要查询按钮。界面将与所有设置的筛选相匹配并对结果进行实时更新。</p>
<p>这种模式的优点是在执行筛选时为用户提供了一种方便简单的体验，可以在每次点击后立即看到结果。适用于较低风险的交互，一旦处理多选过滤器或更复杂的输入时可能会造成混乱。当然还需要考虑处理数据的多少，如果应用中数据量巨大，每次更新时间较长，反而会降低用户的使用效率。</p>
<p><strong>（2）手动更新</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/c1zXra16IVGynFqekI7f.png" alt width="1029" height="212" referrerpolicy="no-referrer"></p>
<p id="u45ca03b8">在手动更新模式下，过滤结果只有在用户点击查询时才会更新。如果用户想在每次更改后查看结果，必须单击查询按钮。</p>
<p id="uaa26303f">这种模式最适用于非常繁重的数据集或低性能的应用程序。</p>
<p><strong>（3）使用哪种模式</strong></p>
<p id="uf1288b94">实时更新模式对用户更方便，但是，如果用户必须配置多个筛选器才能获得有用的结果集、或者预期产生的数据量过大，请考虑改用手动更新模式。</p>
<p id="uba4d564b">选择哪种模式需要考虑：数据量、系统性能以及用户期望。</p>
<h3>4. 显示结果</h3>
<p><strong>（1）筛选进度</strong></p>
<p id="u23bf7a8a">筛选操作需要一些时间才能显示结果。在此等待状态期间，需要给出进度的反馈。加载图标是常见加载方法。如果加载结果时出现问题，应以适当的形式将结果传达给用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/8MBkiNH44HRCAN7Nvd0m.png" alt width="757" height="694" referrerpolicy="no-referrer"></p>
<p><strong>（2）突出筛选结果</strong></p>
<p id="u58f1ff1f">应用筛选后，选项可能会隐藏在其下拉菜单或可扩展部分中。这时候需要突出执行过哪些筛选值。否则，用户很容易忘记操作内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/HIqI1iZM3USEI4sUCxTY.png" alt width="794" height="1146" referrerpolicy="no-referrer"></p>
<p id="u5e81592a">需要注意：</p>
<ul>
<li id="u84b04365">保持筛选条件在其内容上下文中可见。</li>
<li id="u8c243689">对于筛选结果应给出明确的指示（数字标记、粗体文本、背景颜色等）</li>
<li id="ud3e2034d">在专门的筛选条件概述/摘要部分集中显示它们。</li>
</ul>
<p id="u75b18c6d">如果多选并且没有足够的空间将它们全部列出时，需要给出明确数字提示用户选择的个数。标签内容可给出最大字符限制，超过部分用 … 代替。如果用户需要再次查看他们的选择，可以指明让用户再次打开下拉菜单查看。</p>
<p><strong>（3）结果计数</strong></p>
<p id="ue7c50efb">传达反馈的另一个关键要素是显示结果的数量。常见的结果计数通常与翻页功能配合使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BPC7wbcnlLIugWZl96xG.png" alt width="797" height="30" referrerpolicy="no-referrer"></p>
<p><strong>（4）空结果</strong></p>
<p id="ubdb6e06b">如果搜索结果不包含任何数据，需要给出空结果消息提示。最好能给用户一些建议以响应空结果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZrtkysSzZwWFLM4k6GMJ.png" alt width="679" height="729" referrerpolicy="no-referrer"></p>
<p><strong>（5）在结果中过滤和搜索</strong></p>
<p id="u635c20e8">筛选结果通常包含大量用户信息，最好提供一些用户可以应用于结果的逻辑筛选器。这可用于进一步限制结果的数量。</p>
<p id="u549179e7">排序功能可帮助用户按所需顺序对结果进行排序。</p>
<p><img data-action="zoom" class="aligncenter" style="color: #666666;" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/N3rsnjoIiS48hvDhPNnW.png" alt width="707" height="372" referrerpolicy="no-referrer"></p>
<p id="u7186ddfc">此外，还可以让用户更改视图以在最佳布局中查看结果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/KpqlALs0pRZeqZNNB2tG.png" alt width="824" height="335" referrerpolicy="no-referrer"></p>
<p><strong>（6）结果清除/结果重置</strong></p>
<p id="udfb70e7e">无论用哪种模式，都不要忘记添加一个易于访问的“全部清除”按钮。这为用户提供了退出筛选、返回初始结果的通道。如果初始筛选栏中有系统默认值，可以添加“重置”按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ySweDxme7fXWdq0oG7jC.png" alt width="762" height="542" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、小结</h2>
<p><strong>筛选的定义：</strong>根据用户需要，对数据进行有规律的抓取，快速查找出特定内容，准确缩小数据的展示范围<strong>。</strong></p>
<p><strong>筛选项的类型：</strong>日期、状态、字典、多条件、联动、高级筛选。</p>
<p><strong>筛选的设计：</strong>位置（侧边栏、水平栏、并列）、初始状态（展开/折叠、平铺/弹出）、执行时间（实时更新、手动更新）、显示结果（筛选进度、突出筛选结果、结果计数、空结果、在结果中过滤和搜索、结果清除/结果重置）。</p>
<h3>参考：</h3>
<ul>
<li>https://pencilandpaper.io/articles/user-experience/ux-pattern-analysis-enterprise-filtering/</li>
<li>https://experience.sap.com/fiori-design-web/filter-bar/</li>
<li>http://www.woshipm.com/pd/4609527.html</li>
<li>http://www.woshipm.com/pd/3622313.html</li>
<li>http://www.woshipm.com/pd/1947124.html</li>
</ul>
<p> </p>
<p>本文由 @LIZ酱 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4884403" data-author="1054439" data-avatar="http://image.woshipm.com/wp-files/2021/01/iH2zkLvy6O5tVZXjclsT.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            