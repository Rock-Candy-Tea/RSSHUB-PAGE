
---
title: 'B 端产品用户体验升级之旅'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/06/ZH4NuNq5Zak8wYRRz8u1.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 08 Jun 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/06/ZH4NuNq5Zak8wYRRz8u1.jpg'
---

<div>   
<blockquote><p>编辑导语：产品设计的目标之一便是达成更加完善的用户体验，进而提升用户粘性，推动后续用户的留存和转化。作者深度复盘了他的项目，分享B端产品体验升级背后思考过程，希望可以带给大家更多帮助！</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-819577 aligncenter" src="https://image.yunyingpai.com/wp/2022/06/ZH4NuNq5Zak8wYRRz8u1.jpg" alt referrerpolicy="no-referrer"></p>
<p>BrokerCould是一款为金融券商提供客户关系管理的SaaS产品，至今发展已有4年。市场不断在变化，客户对于产品服务的要求也在不断变化，为了让用户有更好的使用体验，需要对产品进行不断的优化创新。在2020年下半年，产品进行了自上线以来规模最大的一次改版。</p>
<p>在这次改版中，我们对产品主要板块进行了体验上的升级改造，新增了BI和Marketing功能，产品能力大幅提升。本文将为你带来这一过程中我们在产品设计上的思考过程，出于保证产品隐私考量对于页面中的一些字段信息进行了替换处理。</p>
<h2 id="toc-1">一、为什么做体验升级</h2>
<p>做出产品全面体验升级的决策并没有那么容易，团队在经过几轮的会议讨论后，才最终决定对产品进行全面升级改造，产品进行全面体验升级的原始驱动力主要有以下三点：</p>
<ol>
<li> NPS净推荐值：作为一款金融垂直领域SaaS产品，客户介绍是我们获取新客户的主要途径之一，NPS净推荐值也是我们长期关注的指标，我们希望通过这次的体验优化来提升产品的NPS值。</li>
<li>品成熟期：产品经过孵化期、成长期进入到成熟期，在这个阶段产品功能趋于稳定，让我们有更多的时间来优化打磨产品，提升产品的用户体验。</li>
<li>海外战略：产品国内市场发展受限，业务拓展重心向海外市场转移，产品交互和视觉上需要针对海外用户的使用习惯进行调整（关于海外用户对视觉风格倾向的用研结论显示，海外用户更倾向于Chrome及谷歌系产品风格）。</li>
</ol>
<h2 id="toc-2">二、产品现有问题分析</h2>
<p>解决问题的前提是定位出产品中真正的问题。只有清楚的了解产品的现状，才能提出优质的解决方案。因此在项目启动后，我们就开始了对产品现有问题的分析和整理，信息来源于以下三个方向：</p>
<ol>
<li>客户反馈：通过客户成功人员收集客户反馈，深入地了解客户期望与客户体验之间的差距，定位出产品存在的体验问题。</li>
<li>数据分析：分析产品在接入GrowingIO后产生的真实数据，直观地洞察用户行为，分析异常数据背后的原因。</li>
<li>竞品分析：对比分析Salesforce、HubSpot、Zoho等相关竞品，找出与之相比我们产品中存在的不足之处和潜在的机会点。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Td26uhQUsorRk5Nhqjd4.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、明确改版设计目标</h2>
<p>产品没有目标就没有前进方向，如果只是一个接一个的做不同的功能，只会把产品做成一个功能的集合，而不会劲往一个方向使。</p>
<p>经过前期的市场调研和竞品分析，再结合我们自身掌握的资源和产品现状，我们确定了新阶段的产品目标。产品目标是新阶段我们对于产品形态的全新定位，也是我们后续进行改版设计的准则。</p>
<p><strong>新阶段产品目标关键词：</strong></p>
<ul>
<li>高效管理工具：B端产品的核心价值在于降本提效，通过交互流程优化、引入智能助手等方式将用户从繁琐的基础工作中解放出来，提升用户日常工作效率，为客户带来实际的价值。</li>
<li>有温度的产品：关注用户使用产品时的情绪，产品的功能服务于用户需求的同时，更注重情感的交流，让用户在产品使用过程更轻松、顺畅。</li>
<li>差异化的能力：增强产品能力、优化产品体验，与竞争对手形成明显区别，获取竞争优势，让产品突出重围。</li>
</ul>
<h2 id="toc-4">四、改版设计方向</h2>
<p>我们无意于仅做表层视觉的优化，根据产品属性、特征以及现实状况，我们围绕“高效管理工具、有温度的产品、差异化的能力”三个关键点，对目标进行了分解，对应到具体的页面升级改造上，对部分功能进行了重构优化，对视觉表现进行了全面的升级。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/i3TwExBBB8DhTf0OGMGA.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、优化方案展示</h2>
<h3>1. 页面自定义，打造专属工作台</h3>
<p><strong>1）首页优化</strong></p>
<p>在产品最初的阶段，我们并没有一个真正意义上的首页，而是出于用户实际的使用场景，将用户最常访问的客户列表页作为进入产品后的第一个页面。在后续产品运营过程中，有一些客户提出需要一个能统一查看客户跟进情况及业绩排行等信息的页面，方便公司对销售工作进行汇总管理。</p>
<p>获取到用户的实际需求后，我们决定用首页来承载这些功能模块，开始阶段我们打算只在首页放置一些通用性强的功能模块，但后续客户不断提出更为定制化的需求，首页也变得越来越不可控。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/AHILZnziOfseNozx75Uz.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">旧版首页的形成</p>
<p>产品设计一旦进入到这种模式，对于产品研发团队和用户而言都是一种灾难。为了满足客户需求，产品研发团队无法避免会做一些客户的定制功能的开发，这类定制开发十分占用产品研发资源，影响正常的产品迭代节奏，而最终呈出的大杂烩式的首页也谈不上什么用户体验。</p>
<p><strong>2） 转变方向，重回以人为本的体验设计</strong></p>
<p>旧版首页框架是围绕业务架构建立的，在这次改版中，我们希望基于每一个使用者的视角，来建立新的首页框架。在建立框架之前，首先我们需要明确的是，新版首页的定位是什么？</p>
<p>我们对新版首页的定位是提升工作效率方便用户快速开展工作的平台，基于这个定位，新版首页需要考虑到不同角色对首页的不同功能需求。不同角色因其工作职责和内容的差异，对其而言同样一个功能板块的重要程度是不一样的。一个内容统一固定的首页并不能满足所有角色的工作需要，我们需要设计一个更为灵活的首页，自定义的需求顺应而生。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/l1V6rAOLOWAF8yXtRKXF.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版设计框架</p>
<p>为此我们分别找到对应角色的用户，调研他们的日常工作流程（具体到每天、每周、每月的工作流程），以便更加深入了解他们的需求。基于前面对用户工作流程的梳理，基本上可以判断出各个角色关注的核心数据和常用功能。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/d5VUNrafx6B9xY4z9ASE.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">不同角色工作流程</p>
<p>随着产品的持续迭代，产品业务种类增多，业务流程变得复杂，用户处理业务时往往需要在多个页面间进行来回切换，在一定程度上影响着用户的工作效率。其实用户常用的功能并不多，完全可以将他们迫切需要的功能或数据展现到首页，方便用户开展工作。</p>
<p>基于前期对不同角色用户日常工作流程的调研，我们抽象归纳出不同角色的工作路径，整理出他们对功能、数据的不同需求，将其中高价值的部分做成组件，汇总起来搭建首页组件库。用户在首页配置页可以根据自己的工作需要挑选出相应的组件，配置自己的专属首页。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/nshmrKdNwQCamjCtu9Ts.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">布局模式选择</p>
<p>在首页的配置页面，可以进行卡片组件的添加、编辑、拖拽调整位置等操作。每次设置只会应用于个人视图，不会影响团队中其他成员的视图。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/OaHm52nXLuIfYmF6V4MH.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">首页编辑页示意图</p>
<p>最后我们一起来看看不同布局模式下首页的实际效果。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/l6w3Cr1RKyLdnPa54c53.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">首页三列布局实际效果图</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/rvQcRLGfxW1iPONKoTnI.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">首页两列布局(左宽)实际效果图</p>
<h3>2. 体验流程优化，提升用户体验</h3>
<p><strong>1）列表页优化</strong></p>
<p>对于B端用户而言，来后台主要目的之一就是对数据进行查阅和操作。列表页可以查看和处理大量的数据，常有导航至详情的作用。用户可在列表页对数据进行筛选、比对、新增、分析、下钻至数据完整详情页等操作。因此帮助用户更高效的查看、处理、查找数据对于提升B端用户的操作效率有着举足轻重的作用。</p>
<p>B端用户都是产品的重度使用者，一个每天会被使用到几十次的功能，操作步骤是5步还是3步，会带来明显的体验差异。很多看似合理的设计，在高频使用的场景下，就开始暴露出问题。</p>
<p>将自己武装成重度使用产品的用户，进入到打造高效信息管理列表页的实战阶段，从实际使用者的角度出发分析并定义问题，寻找设计突破口。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/hPQ7yi9PmJDg0w0blNZT.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">原有列表页问题分析</p>
<p>在定位出列表页存在的问题后，针对问题点提出相应的改进优化方案。列表页的改版优化主要围绕列表页的三大组成部分筛选器、工具栏、表格来进行。</p>
<p><strong>2）筛选器-高效、便捷的筛选体验</strong></p>
<p>筛选器的存在对列表页来说是非常重要的，它可以帮助用户在列表页茫茫多的数据当中进行快速的定位。对列表数据进行快速的划分，缩短用户对于数据的寻找时间。</p>
<p>旧版筛选器是产品中用户吐槽很多的一个点，旧版筛选器固定展示在列表页的左侧，将所有的筛选字段依次罗列出来。在进行筛选操作时需要先选中筛选字段点击展开，然后再对筛选项进行操作，交互步骤较为繁琐。缺少针对筛选项的排序功能，在筛选时需要花费大量时间来挨个寻找自己要用的筛选项，实际使用体验不佳。为了用户更好的筛选场景体验，我们选择对列表页的筛选功能进行优化。</p>
<p>设计之前我们对市面常见筛选器形式进行了调研，为后续设计提供参考。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/D7bLTNU08nG5aqfwqlnE.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">常见筛选器分析</p>
<p>在我们产品的实际业务场景中，每一个表单字段都有可能成为用户的筛选条件之一，但是大部分情况下用户在筛选时只会使用三到四个筛选项结合进行筛选，这几个筛选项也基本上是如时间、地址、客户级别、客户状态这类的高频筛选字段。</p>
<p>因为筛选功能是用户进入列表页会频繁使用到的一个功能，所以筛选操作的便捷性是我们在设计新版筛选器时着重考虑的一个点。</p>
<p>通过分析不同类型筛选器的优劣再结合到我们实际的业务场景，设计出更为高效与便捷的新版筛选器，新版筛选器改动主要有以下三点：</p>
<ol>
<li>浮层式筛选器：新版筛选器位置由原本的固定在列表页左侧改为通过点击按钮触发的浮层，这样的改动能够扩大表格横向宽度，表格在横向上能展示更多的字段信息，改动对于后续新增的行内快捷编辑功能也更为友好。</li>
<li>选项平铺：在原来筛选器使用中就有客户反应这种勾选筛选项以后才能展开筛选项内容进行筛选的交互方式很不方便，在新的筛选器中我们选择将部分筛选字段平铺展示，这样能简短操作步骤，提升交互效率。</li>
<li>筛选项的增删与排序：新增筛选项的增删与排序功能后，用户可以根据自己的工作需要将自己常用筛选项进行排序后固定展示，不用在寻找筛选项上花费大量时间。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/daO2nVBGvwx0Vr2xRSmO.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版筛选器</p>
<p><strong>3）工具栏-空间与布局的合理安排</strong></p>
<p>旧版设计中列表工具栏空间浪费较多，压缩了表格区域空间，我们希望通过优化顶部操作区域使空间利用更合理。列表工具栏大概有两个模式，一种是单行模式，节约纵向空间，一种是双行模式，适用于内容量较多的情况。</p>
<p>在设计过程中我们分别尝试了两种模式，我们产品的内容量在单行布局下显得十分局促，在双行模式下更满足元素排序逻辑，所以我们还是选择了双行模式。</p>
<p>在双行模式下，我们选着将标题、视图、新增等优先级高的元素放在第一行。</p>
<p>表格工具、筛选、表格信息等优先级相对较低的内容放在第二行，为了节省纵向空间，对第二行的内容进行了弱化处理。为了确保搜索的全局性，选择将搜索放在第一行，不受其他筛选项的影响。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/p8ZRJINETQK4LFA37qkk.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">列表工具栏</p>
<p><strong>4）表格-最优信息密度与快捷编辑</strong></p>
<p>我们为用户提供了“紧凑”、“舒适”和“宽松”这三种表格模式选择，同时满足用户在“效率型”“阅读型”“展示型”等不同页面场景的需求。我们还未表格新增行内快捷编辑功能，编辑信息在列表页即可完成，不用再进入详情页进行修改，简化了步骤，提升用户工作效率提升。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/DTaKOduIEuwDJA2N7Bpo.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">表格阅读模式</p>
<p>除了上述的改动，我们还为列表页新增了看板视图模式，看板试图模式在商机等场景有很好的应用，最后让我们一起看看优化后的列表页。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/OL4fVS7TUooPO5HrSznh.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">列表页(表格视图模式)</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/HbdLZ3pyEns8bSsDboPD.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">列表页(看板视图模式)</p>
<p><strong>5）详情页优化</strong></p>
<p>原版的详情页为在新页全屏展示，优化为详情页在当前页面中展开显示的方式，可以让用户不必经常切换页面，直接通过点击下方列表中的客户名来进行快速切换。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/U3VHowCxYtmvXMQsiE3d.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版详情页查看模式</p>
<p><strong>6）信息降噪，让界面信息更聚焦</strong></p>
<p>详情页需要承载的信息、功能繁多，但是单页面承载能力有限，一旦内容过多，就会出现焦点不突出，内容不清晰的情况。这无疑增加了用户的思考时间，降低了工作效率。那么如何改善用户体验，让其能够高效且舒适地使用我们的产品呢？</p>
<p>加强重点、信息降噪是保持信息干净清晰，更好触达用户的保证。通过强化页面内的有效信息，降低多余元素干扰，从而提升页面内的“信噪比”，以达到功能与信息有效传递，降低用户理解成本，提高产品操作效率。</p>
<p>提升“信噪比”不能以牺牲用户正常的信息获取需求为代价，当页面元素太多放不下，除了增加产品页面数，我们可以尝试运用动效，在同一页面上扩大产品的内容范围。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/1L6LkAMYjQP3wfOzpPJJ.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">动态扩展内容范围</p>
<p>旧版产品中跟进记录模块是将整个发布控件完整的展现出来，在新版设计中我们将详情页由原本的新页全屏展示优化为当前页面展开的抽屉形式，详情页布局空间也因此变小，新版设计中如果再将发布控件完整的展现出来，由于控件本身占据空间较大，其他内容的展示空间会变得很局促。</p>
<p>因此在新版设计中，我们选择只将根据记录的输入框固定展示，将跟进方式选择、发布按钮这些元素都暂时隐藏起来，当用户点击输入框触发发布控件时，再扩展为完整的发布控件形态。这样的改动既保证了跟进记录功能的完整，也保证了页面信息的干净清晰。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/3T1OmdsnhBn2Sntnwc0l.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">动态记录模块优化</p>
<p>出于用户长期使用中形成的使用习惯，我们并没有大幅调整详情页的页面结构，在新版设计中主要优化信息的呈现和细节交互，通过细节优化来提升用户实际体验。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/rNZGVLeFJs8lhDhkcnfx.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">详情页</p>
<h3>3. 组件优化，从底层提升效率</h3>
<p>在2年前，为了提升设计输出的一致性以及提高和下游开发同学的对接效率，我们搭建了UI组件库。旧版组件库相对较为基础，和我们自身的业务贴合度不高。</p>
<p>新版组件库为解决实际问题而生，基于B端产品特性和自身业务特点，确定组件库清晰、灵活、效率、优雅的设计原则，对如地址选择、人员选择、时间选择等20余个组件进行了设计优化。我们希望用户使用新版组件更高效地去解决问题，并且从中获得愉悦的感受。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/d1OnjR6eUVqGweVO56cg.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版组件库设计思路</p>
<p><strong>1）组件优化示例-字段选择组件</strong></p>
<p>产品中如列表页配置表头显示内容、后台配置默认显示字段等很多场景都需要进行字段选择。不同场景之间的功能需求也有所区别，有的需要能对选择后的字段进行排序，有的对已选择的字段有数量限制。</p>
<p>旧版设计中是使用穿梭框来进行字段选择，为了满足这些穿梭框能力之外的功能需求，我们对穿梭框进行了改造，产品中因此产生了几个衍生版本的穿梭框组件，整体性差，不成体系。</p>
<p>在我们产品实际的用户使用环境中，可选字段数量经常能达到七八十个字段。这么多字段的情况下选用穿梭框进行字段选择效率很低。</p>
<p><strong>2）新版设计中</strong></p>
<p>1.侧重的将可选字段区域占比扩大，并将字段平铺展开，这样可以展示更多的可选字段，更从容、高效的进行字段选择。</p>
<p>2.在已选字段区域，将排序、限制已选字段数量等功能统一设计，保持交互的统一性。</p>
<p>3.新增搜索功能，方便用户快速选择目标字段。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/FgINc7qT8CAb0knFAxJB.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版字段选择组件</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/GU7Cby7D3Ri7MAWqY2mx.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">应用实例</p>
<p><strong>3）组件优化示例-地址选择组件</strong></p>
<p>地址选择是新建表单中的常见填写项，旧版地址选择组件缺少搜索功能，级联选择的选择方式效率低，在列表页中进行筛选时旧版地址选择组件不能支持多选。</p>
<p><strong>在新版设计中我们针对这些问题进行了相应的优化：</strong></p>
<ol>
<li>地址信息平铺展开，提高选择效率</li>
<li>地址选择组件新增搜索功能</li>
<li>添加复选框，支持筛选场景下的多选需求</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/zl2FfJRWuf6bsdsEWJxl.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版地址选择组件</p>
<p><strong>4）组件优化示例-下拉选择组件</strong></p>
<p>在类似于审批人选择这类场景，我们除了可以选择具体的“成员”为审批人外，同时可以选择“角色”或“部门”作为审批人，这样可避免因成员离职变动导致审批流失效。</p>
<p>在一个组件中同时选择三种不同类型的数据，旧版下拉选择组件是不支持的。旧版设计中我们的解决方案是用两个选择组件配合使用来达到这样的效果，先选择审批人的类别，再选择具体的审批选项。</p>
<p>这种交互方式的无疑体验不好，新版设计中我们给选择器新增了Tab，通过Tab切换来区分选择不同类型的数据。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/oEHHHbWvPAsQC3yJuuIy.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新版下拉选择组件</p>
<p>新版组件库有一套全新的设计语言，从设计原则到字体排版，从交互到文案，从动效到样式，从组件到设计工具……</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/hYlTBSTDyAauBZlKNXws.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<h3>4. 帮助引导系统化、体系化</h3>
<p>大多数的B端产品，业务逻辑都非常复杂，为了满足复杂业务逻辑的需要，设计的业务流程和产品页面也相对复杂，为了让用户在使用产品时能方便、快捷的完成任务，在客户使用产品前会安排专门的实施人员对用户进行产品知识培训。尽管提供了培训，用户在使用产品过程中或多或少还会遇到问题。</p>
<p>这时候一个好的帮助引导系统存在就很有必要，旧版产品中帮助功能是一个很小的模块，当用户产生疑问时，引导他去帮助中心查阅资料，这种方案显然不太高效，帮助中心是按产品功能逻辑排列说明文档，定位问题答案十分不易。</p>
<p>用户根本诉求是：能快速定位到问题的答案，排解自己的疑惑。因此我们仔细询问过用户疑惑感来源的方方面面，构建了构建了基于场景识别的帮助引导系统。</p>
<p><strong>1）简单问题，就地解决</strong></p>
<p>如名称解释、操作提示等简单问题，提前预判问题点，给出轻量化的快速解答，就地化解疑惑。若疑惑未被消除，提供入口，将用户引导至该问题对应的详细说明文档。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/a01bSgWIrXkSBFj7ROu7.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示例一</p>
<p><strong>2）因地制宜 ，快捷访问</strong></p>
<p>我们对全局帮助面板进行升级，它的形式不再是一成不变，而是根据用户当前访问的页面，给出当前页面用户可能出现问题指引和快速开始教程，帮助用户快速解决问题。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Col263d3F8faP7HE67B3.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示例二</p>
<p><strong>3）复杂功能 ，视频讲解</strong></p>
<p>在如图表配置、数据工场这类流程和逻辑复杂的页面，通过文字来给用户完善的引导往往需要长篇大论。在这类页面我们给用户提供视频讲解来帮助用户快速上手，相对于文字而言视频的讲解更形象易懂。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/a3ynbGo7nh8do37Y6akd.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示例三</p>
<p><strong>4）空页面，无形的引导</strong></p>
<p>最好的引导是无形的，不强制要求用户完成教学任务，将空页面作为用户引导流程的一个起点，将空页面设计为介绍产品功能，引导用户的模块。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/caEY5BTQbsEt2wBn7hBC.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示例四</p>
<p>最后我们还有一个强大的后方——帮助中心，帮助中心是我们整个帮助引导系统中重要的部分之一。在这里我们为用户提供了各种各样的帮助形式和学习资料，如教学视频、帮助文档、问答社区等。用户有了问题进入到帮助中心，可以很便捷的找到自己想要的答案，并且答案足以解决他们的问题。</p>
<h3>5. 全新风格、情感化插画</h3>
<p>在新版设计中我们绘制了全新风格的产品插画，运用于产品中空状态，加载等待、运营活动等场景，插画作为现代设计的一种重要视觉传达，可以进行信息的传达、感情的传递。</p>
<p>具备文字所不具备的温度的插画，能引发共情效应的同时，可以具像化品牌形象、促进转化以及提升用户粘合度。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/hBFc6hYPmSt5Tn5S5mBL.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">列表页搜索为空示例</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/1QCvPLnvjNgLuSlsfg1C.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">空状态插图示例</p>
<h2 id="toc-6"><strong>六、总结</strong></h2>
<p>以上，是本次全面体验升级背后的原因以及思考过程，从前期用户调研、问题分析、目标确定（1.高效管理工具；2.有温度的产品；3.差异化的能力），到通过多维度地将目标落地（1.页面自定义，打造专属工作台；2.体验流程优化，提升用户体验；3.组件优化，从底层提升效率；4.帮助引导系统化、体系化；5.全新风格、情感化插画），优化了体验、提高了使用效率。</p>
<p>新版设计在上线灰度测试后，通过问卷对本次体验升级进行满意度收集，测试租户对于新版产品的满意度平均值高达90%，用户对于新版产品有很多正面反馈，有租户反馈新版首页对员工日常工作帮助很大，新版列表页对于用户日常管理用户更高效。</p>
<p>对于自我认知，设计更像一场修行，知易行难。作为体验设计师，不要纸上谈兵，只在乎视觉层面的感知，应该深入用户群体，升入了解用户使用场景，从用户和业务的角度去研究用户群体，只有站在更全面的的角度去思考问题，才能更好地服务用户。</p>
<p>受限于篇幅，没有将新功能BI和marketing部分的设计思考过程展示出来，以后会单独分享，最后按照惯例上一波设计图。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Sapte3CZdj3mt0YnD5rh.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/1IjInALpCDyDEc6zfhuG.png" width="391" height="183" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：Yone杨 ；公众号：黑马家族</p>
<p>原文链接：https://mp.weixin.qq.com/s/Kejsj3gkdvMW17zrQxhTXg</p>
<p>本文由@黑马家族 授权发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
                      
</div>
            