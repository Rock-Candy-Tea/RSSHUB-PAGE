
---
title: 'Axure打造最强DRD交互文档（含案例）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/I0B5ijYzhTDOaClTZhh0.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 22 Feb 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/I0B5ijYzhTDOaClTZhh0.jpg'
---

<div>   
<blockquote><p>编辑导读：交互设计说明文档，即DRD是指用来承载交互设计说明，并交付给前端、测试以及开发工程师参考的文档，是一项基本功。本文作者用Axure来完成了一份交互文档，并且通过案例，更切实地帮助理解交互文档的细节，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4382393 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/I0B5ijYzhTDOaClTZhh0.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>当我在网上搜寻交互文档规范时，可以搜到很多关于交互文档的结构搭建的文章，但始终没有一份较为完整的案例Demo展示，主要是因为大多数商业项目的交互文档是涉密的，无法进行分享。</p>
<p>相信大家和我一样想要一睹交互文档实战案例的芳容，我本着在交互行业学习的精神，研究了飞书、钉钉、腾讯会议，最终构建了这个《UEDART云办公APP交互案例》的虚拟项目，最终输出在交互文档中可以快速复用的框架与模块。旨在通过符合实际的项目来进行交互文档整体构建的阐述，让大家通过案例的浏览，更为切实的了解到交互文档的细节，从中得到一些有效的帮助。</p>
<p>以下预览的整个交互文档全部由Axure制作完成。</p>
<p><strong>UEDART云办公APP交互案例</strong><strong>预览：</strong><a href="https://vip.uedart.com/works/CloudOffice/Complete/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/Complete/index.html</a></p>
<p>关于整个云办公APP项目的需求分析、设计思路、业务流程图、页面流程图、原型图制作内容已经在《UEDART云办公APP交互案例》文档中体现了，本文就不再做过多赘述。接下来主要讲一讲，通过本次交互案例的展示，如何利用Axure快速构建DRD交互文档，为我们后续的工作提供更加有效的帮助。</p>
<p>通过本文的阐述再结合《UEDART云办公APP交互案例》，双管齐下，能够让大家更好地了解到整个交互文档框架与实战交互案例的全貌，深入各个环节挖掘细节知识。这样会比单独从一个角度切入更为的直观和有效。与此同时，大家可以初步了解到如何从项目实践中抽离共通性，有意识地将共通性进行模块化是提高效率的好方法。</p>
<p>希望本文能够给大家传播一些知识，也希望在和大家交流的过程中，我也能不断地修正错误汲取新知识，和大家一起成长。</p>
<h2 id="D9iAc">一、明确用户对象</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/lGy7XzZ5gj6ESWfL8aMb.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p><strong>交互文档给谁看，定义文档的用户对象很关键。</strong></p>
<p>根据文档的用户对象不同，制作的方式与精细度也会有不同的要求。</p>
<p>本次制作的交互文档主要是针对工作环节中，用于落地开发实现，辅助工作环节中的各个成员：产品经理、视觉设计、开发人员以及测试人员，了解产品交互的功能与流程细节需求，便于开发对需求的理解与实现。</p>
<h2 id="rFRV5">二、文档制作场景化</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/lni2KLApltawp54aDcbz.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<h3>2.1 我们产品设计中的几个常见场景</h3>
<p><strong>0-1的产品设计：</strong>完全0-1的产品，从头梳理产品业务、场景与业务，对应的业务与模块需求特别多</p>
<p><strong>全新业务线：</strong>已有基础流程与业务的沉淀，需要迭代全新业务线或大模块，对应的业务流程和功能多</p>
<p><strong>大版本迭代产品功能：</strong>涉及多平台、流程较多，对应的迭代功能比较多</p>
<p><strong>小版本迭代产品功能：</strong>涉及流程少，迭代功能少，对应的要求是快速响应上线</p>
<h3 id="mNKup">2.2 如何让整个文档框架更为的灵活呢？</h3>
<p>针对以上场景我将交互文档框架拆分为：大、中、小三种形式，分别对应产品设计的几个常见场景</p>
<p><strong>大型：0-1的产品设计，迭代全新业务线</strong></p>
<p>此会用1个完整的UEDART云办公APP交互文档案例来展示</p>
<p><strong>UEDART云办公APP交互案例</strong><strong>预览：</strong><a href="https://vip.uedart.com/works/CloudOffice/Complete/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/Complete/index.html</a></p>
<p><strong>中型：大版本迭代产品功能</strong></p>
<p>此大体结构和“大型”差别不大，主要是删减了一些基础信息的内容，流程和子业务的数量上的差异性</p>
<p><strong>交互说明框架(中型)预览：</strong><a href="https://vip.uedart.com/works/CloudOffice/mid/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/mid/index.html</a></p>
<p><strong>小型：小版本迭代产品功能</strong></p>
<p>小版本，时间紧，功能较少，于是这边简化为“页面流”和原型图展示</p>
<p><strong>交互说明框架</strong><strong>(小型)</strong><strong>预览</strong><strong>：</strong><a href="https://vip.uedart.com/works/CloudOffice/little/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/little/index.html</a></p>
<h2 id="QMIQw">三、提炼交互文档特性</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/NskVTdsOOGaGnF2ryIKg.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>结合用户对象和使用场景，提炼交互文档的几个特性。</p>
<ul>
<li><strong>易于阅读：</strong>方便流程中的各个对象的阅读与理解，方便浏览与阅读</li>
<li><strong>灵活应用：</strong>适配于各个产品设计的场景，提升效率</li>
<li><strong>调整修改：</strong>在产品开发进程中进行错误点的调整或需求变更的标记与注释</li>
<li><strong>版本迭代：</strong>要做好版本管理，方便更新迭代，不只是项目的迭代，整体交互文档框架也需要不断更新迭代使其更加符合我们实际的工作所需</li>
</ul>
<p><strong>为什么要提炼特性？</strong>——主要是让制作有方向性，这一点很重要。</p>
<p>做一件事一定要明确为什么做，在项目之初已经定义了本次项目的主要目的。在明确为什么做的基础上，如何更有效地实现目标，方向性很重要，它为接下去的项目制作提供了关键着陆点，在一系列的发问与思考中不断完善靠近最终目标。接下来的制作思路将基于此特性，进行制作方法的选型与整体交互文档构建的架构。</p>
<h2 id="WqKFM">四、制作思路</h2>
<p>最初定义《UEDART云办公APP交互案例》的输出为主，此案例按照大型的交互文档框架进行打造，让大家能够了解到交互文档的全流程制作的全过程。</p>
<h3 id="cebUA">4.1 制作准备与产出物</h3>
<p><strong>4.1.1 制作方法论</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/YAkfDHWslnOtWoSE8m2t.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>我称之为五环制作法：提炼原则，确定方法，统一规范、拆分模块、提升效率。</p>
<ol>
<li><strong>原则：</strong>基于交互文档的四个特性，易于阅读、灵活应用、调整修改、版本迭代。</li>
<li><strong>方法：</strong>利用Axure+oss原型托管的方式来实现整体文档的架构与部署。方便不同制作场景下的应用、各成员的浏览阅读、修改调整、版本迭代控制。</li>
<li><strong>规范：</strong>基于统一的规则，方便保持元素的一致性，提升文档细节美观度和阅读感。</li>
<li><strong>模块：</strong>文档内部形成标准件模块化、流程模块化、页面模块化、组件模块化，方便复用与管理。</li>
<li><strong>效率：</strong>采用了原有已经制作好的PRD框架+手机组件作为基础素材，方便提升的制作效率，与此同时规范性与模块化也为后续的制作带来了高效率性。</li>
</ol>
<p><strong>4.1.2 项目准备</strong></p>
<ul>
<li><strong>项目名称：</strong>UEDART云办公APP1.0</li>
<li><strong>项目调研：</strong>了解竞品、分析竞品、竞品结构分析（主要针对飞书、钉钉）</li>
<li><strong>项目安排：</strong>周期安排，利用业余晚上和周末的时间完成</li>
<li><strong>制作工具：</strong>Axure9.0版本、xmind8.0</li>
<li><strong>项目启动：</strong>2020年12月1日启动，</li>
<li><strong>预计完成：</strong>2021年1月15日</li>
<li><strong>实际时间：</strong>2021年2月6日</li>
</ul>
<p>Tip：回溯项目整个的制作时间，2021年1月穿插了很多其他事情，比之预期有所滞后，最终还算比较顺利的在春节前完成了整个项目的制作与整理。</p>
<p><strong>4.1.3 最终产出</strong></p>
<ul>
<li><strong>脑图：</strong>云办公APP、交互规则、非功能性需求</li>
<li><strong>大型交互说明框架：</strong>UEDART云办公APP交互案例</li>
<li><strong>中型交互说明框架：</strong>交互说明框架_中型</li>
<li><strong>小型交互说明框架：</strong>交互说明框架_小型</li>
<li><strong>原型元素：</strong>原型元素规范</li>
</ul>
<h3 id="qI9vj">4.2 文档结构</h3>
<p><strong>4.2.1 浏览框架结构</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/pxWnlUJBozGqVyr6SDr0.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<ol>
<li><strong>标记1：</strong>交互文档标题，包含项目名称+版本号</li>
<li><strong>标记2：</strong>主模块频道切换，可根据需要自定义和调整排序</li>
<li><strong>标记3：</strong>模块内，切换菜单，可根据需要自定义增加或减少</li>
<li><strong>标记4：</strong>子菜单内容展示，可根据需要自定义内容页内容</li>
</ol>
<p>Tip：整体框架封装好自适应结构，方便笔记本与pc电脑的阅读感，同时封装好切换点击动效，整体浏览感就和平时浏览网站是一样的效果，方便读者阅读</p>
<p><strong>4.2.2 交互文档结构</strong></p>
<p><strong>大结构分为：</strong>基础信息、交互说明、原型页面、回收站四个模块</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/Fv0fqpqeXnYnOFyd8xjh.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p id="JdfRS">部分内容展示：</p>
<p>更新日志：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/03A4JSvLJV42NqtTF409.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>产品介绍：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/BXkmbsBqNZ3zIaI2W40F.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>设计思路：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/Ko1pHIqMMaaH2nXtP77W.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>通用规则：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/4ps21ZLh8NpDOl7dJhtY.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>非功能性需求说明：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/mHYQEvi3tgOoux8BLAu0.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>交互说明目录：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/UCFLPByfEbtGUAlb4nyj.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>页面流程图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/SBB6NMlIoKfhmwkmxRZ1.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<h3 id="Cooe6">4.3 文档规范与模块化</h3>
<p><strong>4.3.1 原型元素规范</strong></p>
<p>在整体文档制作开始时，先制定好整个原型文档的原型元素是一件很必要的事情，这为后续制作的规范统一性提供了坚实的基础，基于统一的规则，方便保持元素的一致性，提升文档细节美观度和阅读感。</p>
<p>这样能够保证后续组件与页面的元素统一，保持一致性的原则。</p>
<p>主要定义了品牌色、自定义灰度色系、头像尺寸、字号、4px间距</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ftK9oTm23Z57uRUXRa9y.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p><strong>4.3.2 组件规范</strong></p>
<p>我们在工作中经常会用到一些固有的组件库，比如Ant蚂蚁出品的axure组件，很多同学可能就“拿来主义”直接应用到自己的项目中，这确实也是一个比较容易也很省事的做法。</p>
<p>我个人比较习惯于把这些组件素材作为制作的基础素材，在实际应用中根据项目的业务所需，重塑组件。项目中的组件制作是一个循序渐进的过程，不能一蹴而就，在我们制作过程中，拆分出来的通用模块，就可以封装为一个组件样式，方便下一个流程或页面的复用。</p>
<p>本次制作中我应用了UEDART出品的手机端组件作为基地素材，进而优化成本次项目中的组件元素。</p>
<p>这套组件规范也是我参与制作的一个项目。<strong><br>
</strong></p>
<p><strong>预览地址：</strong><a href="https://vip.uedart.com/demo/UEDART_003/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/demo/UEDART_003/index.html</a><strong><br>
</strong></p>
<p><strong>4.3.3 模块化思维</strong></p>
<p>我们不止在制作文档时需要模块化这种思维，在设计产品与流程设计时也需要带着这种思维，可以有效地将流程中公用的子业务流进行串联，避免重复子流程与重复的开发工作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/FxSTqwd2KOzMEKnCSR2d.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<h3 id="sCauW">4.4 调整与修改</h3>
<p><strong>4.4.1 文档联动调整</strong></p>
<p>框架页面名称，采用函数制作，名称自动按照页面名称展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/4dYFa5Q5KnwZvLK5N3nD.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p><strong>交互说明目录名称：</strong>采用引用制作，名称自动识别页面名称展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/F4bOJgN7jI4XmaKLiNvr.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p><strong>页面流程的页面与页面名称：</strong>页面采用引用自动识别对应原型展示，页面名称采用引用自动识别页面名称展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/S0TXWF0ZF7kipcrd3WkY.png" alt width="1280" height="720" referrerpolicy="no-referrer"></p>
<p>通过以上几个小应用可以做到方便后续修改时，不需要做过多的重复命名工作，只需修改左侧树结构的页面名称，所有相关页面都会同步修改名称，而且当我们需要在页面名称上备注此页面（修改）时，在其他环节也会展示，相当方便。</p>
<p>不过在前面的制作时就要按方法执行，避免后续为调整修改名称，工作量大且容易忽略，导致名称不对应。</p>
<p><strong>4.4.2 更新修改</strong></p>
<p>当文档进行修改或更新时要做哪些动作。</p>
<p><strong>更新日志添加：</strong></p>
<p><span style="color: #666666; font-size: 16px;">按照修改时间、属性、描述、修改人进行添加，当同一天更新比较多时（修改了需求），此时可以按照调整模块拆分成多条来添加。</span></p>
<p><strong style="color: #666666; font-size: 16px;">添加目录与页面备注：</strong></p>
<p><span style="color: #666666; font-size: 16px;">在交互说明对应的流程目录上添加更新备注。</span></p>
<p><span style="color: #666666; font-size: 16px;">时间+更新，</span><span style="color: #666666; font-size: 16px;">在页面名称后加上（新增）或（修改）。</span></p>
<p><strong style="color: #666666; font-size: 16px;">添加页面流程标记：</strong></p>
<p>页面流程中的标记，根据所做的修改部分进行标记。</p>
<p>为了方便大家在页面流程中的标记，我将标记修改进行了组件化：多页面修改标记、注释调整标记、单页面局部标记、删除隐藏标记。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/vuHBQJdqJJeke364oL8J.png" alt width="1280" height="860" referrerpolicy="no-referrer"></p>
<p>这边我举个例子，方便大家对标记实操的理解。当我修改了登录页面的一键登录页面和注释描述时。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ccn0jtHHcsDbp7oWB4r8.png" alt width="1280" height="2137" referrerpolicy="no-referrer"></p>
<h2 id="QPYUK">五、浏览阅读</h2>
<p><strong>借助原型托管工具：</strong>这边我采用了阿里云oss上传。主要是考虑浏览速度的因素，蓝湖大文档的原型托管会卡。当然你也可以选择Axhub或蓝湖以及其他托管平台都可以实现将Axure生成的html进行上传。</p>
<p><strong>链接分享：</strong>通过分享的地址链接，其他成员可以通过连接打开进行项目的浏览。</p>
<p><strong>APP交互案例</strong><strong>预览：</strong><a href="https://vip.uedart.com/works/CloudOffice/Complete/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/Complete/index.html</a></p>
<p><strong>交互说明框架(中型)预览：</strong><a href="https://vip.uedart.com/works/CloudOffice/mid/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/mid/index.html</a></p>
<p><strong>交互说明框架</strong><strong>(小型)</strong><strong>预览</strong><strong>：</strong><a href="https://vip.uedart.com/works/CloudOffice/little/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/little/index.html</a></p>
<p><strong>原型元素规范预览：</strong><a href="https://vip.uedart.com/works/CloudOffice/element/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/works/CloudOffice/element/index.html</a></p>
<p><strong>UEDART手机端基础组件预览：</strong><a href="https://vip.uedart.com/demo/UEDART_003/index.html" target="_blank" rel="noopener noreferrer">https://vip.uedart.com/demo/UEDART_003/index.html</a></p>
<h2 id="S21rz">六、结语</h2>
<p>本次关于Axure打造交互文档的分享就到此结束了，希望能够给大家带来一些帮助。完整的案例可以在预览地址里可以查看，欢迎大家与我交流，共同进步。谢谢！</p>
<p><strong>关联文章：</strong></p>
<p><a href="http://www.woshipm.com/pd/1065161.html" target="_blank" rel="noopener noreferrer">《不只是“设计”，产品思维赋予设计新动力！》</a></p>
<p><a href="http://www.woshipm.com/rp/2803969.html" target="_blank" rel="noopener noreferrer">《原型制作四字诀：整、拆、合、移》</a></p>
<p><a href="http://www.woshipm.com/pd/812777.html" target="_blank" rel="noopener noreferrer">《PRD文档构建及使用流程》</a></p>
<p> </p>
<p>本文由 @时光若刻 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4377278" data-author="55654" data-avatar="https://static.woshipm.com/APP_U_201809_20180905123930_7656.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">2人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://image.woshipm.com/wp-files/2015/10/touxiang-6.jpg!/both/80x80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183122_9897.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            