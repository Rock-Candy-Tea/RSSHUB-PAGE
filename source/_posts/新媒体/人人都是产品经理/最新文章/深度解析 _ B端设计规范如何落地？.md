
---
title: '深度解析 _ B端设计规范如何落地？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MfgSHVPMCF8LR3jnUkj2.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 27 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MfgSHVPMCF8LR3jnUkj2.jpg'
---

<div>   
<blockquote><p>编辑导语：设计师往往不止参与产品设计步骤，其工作也需要与其他部门组织协同。那么，B端设计师又该如何制定出一份合适的设计规范并使其落地？本篇文章里，作者就结合他的设计经验为我们详细介绍了B端设计规范落地的关键要点，让我们一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4498317 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MfgSHVPMCF8LR3jnUkj2.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在B端设计中，设计规范怎么建立才能落实下去之前一直困扰着包括我在内的广大设计师老铁们。</p>
<p>设计师期望参与产品的每一个角色（产品、设计、前端开发、测试）都能遵循设计规范，结合设计规范内的内容，保证前端开发页面的还原度。因此从目标来说，其实设计师小伙伴与研发小伙伴的目标是一致的，但是实现起来其实并没有想象中的简单。</p>
<p>在业务初始阶段对业务不熟悉、就盲目着手建立规范其实并不是一个明智的选择。很多B端的萌新小朋友会在业务尚未明确情况下就从第一个版本就开始制定设计规范，这会蕴含巨大的风险，也不易推动落地。</p>
<p>在初期有限的研发资源里只有了解了业务的实际场景，针对场景进行深度思考与分析，与规范涉及人员进行深度沟通统筹各方面资源，才能最后形成一套可以落地执行满足设计标准和业务需求的设计规范。</p>
<h2 id="toc-1">一、B端设计为什么要制定设计规范？</h2>
<h3>1. 对产品来说</h3>
<p>搭建原型可直接调用组件库，能搭建出高保真的原型。与设计师沟通更加顺畅，小的修改可以直接和开发沟通，不需要通过设计师出图，极大加快了前期的节奏。</p>
<h3>2. 对设计师来说</h3>
<p>当同一个项目由多个设计师共同协作时，由于设计理解不一致等各种原因都会出现设计控件使用混乱等问题。此时，为了保证设计各方面统一性，需要一份设计规范做引导。</p>
<h3>3. 对开发来说</h3>
<p>按照设计规范建立好公共组件库，开发效率有了明显的提升。可复用的东西确定下来后不会频繁改动，设计走查的问题也会逐渐减少。</p>
<h3>4. 对测试来说</h3>
<p>模凌两可的交互可以有地方看交互样式了，不需要再询问设计师。有更多时间专注于测试功能上的问题了。</p>
<p><img data-action="zoom" class=" wp-image-4497564 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/fmilTITrqCh4okW7ANuJ.png" alt width="632" height="421" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、什么阶段适合建立设计规范？</h2>
<p>过往，设计师一般默认在启动一个项目的初始阶段进行设计规范的制作，具体时间点跟着版本节奏走。</p>
<p>在1.0版本之前就着手规范的制作，其实这是很欠缺考虑的做法，其中蕴含着极多风险因素在里面。此处分享个人工作中两个比较建议的规范建立时间点供大家参考。</p>
<h3>1. 业务处于探索期</h3>
<p>在初始版本开发并未制定相应的业务组件。规范主要涉及到色彩、字体、间距、布局、栅格等通用设计原则以及常用业务组件的定制。</p>
<p>此阶段搭建的规范具备高效性以及灵活性的特点。由于尚未搭建特殊的业务组件（当领导想要突然调转方向也不会很慌，改动较小就可以完成整体的规范转向），此时搭建规范组件库需要考虑到预留后续更改的空间。</p>
<ul>
<li>优点：灵活，满足业务随时更换的需求；</li>
<li>缺点：体量小，仅能支持初步业务场景。</li>
</ul>
<h3>2. 业务处于成长期</h3>
<p>当业务已经迭代几个版本后，整个团队对业务的理解都不可同日而语，产品也到了较为稳定的版本。</p>
<p>此时若提出搭建组件库，可以结合业务设计出符业务场景的样式。每个符合当前业务的组件逻辑和样式都不是初始阶段凭空想象出来的，当产品有一定的发展、有足够的业务逻辑、积累足够的业务场景，才能设计出有着自身业务的完善组件库。</p>
<ul>
<li>优点：可以依据反馈沉淀组件库，发展到一定阶段整体变数不会太大；</li>
<li>缺点：0-1阶段需要设计师对整体业务设计有比较足的把控力。</li>
</ul>
<p><img data-action="zoom" class=" wp-image-4497568 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/w0KHp9zUTK1d9C8DEqcW.png" alt width="637" height="332" referrerpolicy="no-referrer"></p>
<p>我们公司在2020年初开启的项目，目前已经过了探索阶段处于向成长阶段过度，当时正值疫情高发，整个项目都由我个人负责。</p>
<p>现阶段整个公司在今年第四季度把系统性的产品和服务竞争优势提上了日程，毕竟没有设计规范、对整个业务底层设计架构进行指引，是很难做好产品差异化和规范化的。也是趁此机会，设计可以针对性对现有的业务组件库以及规范进行一次全面的复盘，迭代出一个新的版本，在团队内推动落地以便更好适应产品的发展。</p>
<h2 id="toc-3">三、推动规范需要像需求一样去迭代</h2>
<h3>1. 做好产品定位</h3>
<p>在B端的项目评审时，设计师就需要做好B端的用户画像，弄明白产品的目标用户以及使用用户的区别，他们通常并非同一类人。</p>
<p>除了目标用户的差异外，不同用户的使用场景也是不一样的。只有弄清楚了各个角色的关系以及功能设计的逻辑、具体用户年龄、解决什么问题，才可以产出符合用户需求的设计。</p>
<h3>2. 整理规范的内容和分类</h3>
<p>在制定规范前，需要明确产品中主要有哪几种分类，将最基础的分类定义好方便后续针对分类内容进行整理。B端产品与C端产品既有共同性、也有很大的差异化，可以借鉴但是切忌生搬硬套C端的设计规范。</p>
<p><img data-action="zoom" class="wp-image-4497576 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MR0Frrodq05vjzu1ZSXw.png" alt width="638" height="424" referrerpolicy="no-referrer"></p>
<h3>3. 排优先级嵌入版本迭代内</h3>
<p>一套完整的规范蕴含内容是非常丰富的，将程序小哥的头发全部薅完也难以在一个版本迭代里面改完的。</p>
<p>因此我们需要将自己作为设计规范这个项目的产品经理，针对现有的需求进行拆分，并排出优先级、分版本迭代进产品里面。我们可以依据从大到小的原则进行优先级排序。对产品设计风格影响大的先排，影响小的后排。</p>
<p>那么针对我们业务优先级排序是：设计准则＞框架布局＞组件＞控件＞场景。</p>
<p>当然设计规范的制定不单单局限于设计团队内部，在嵌入版本里面时可与产品和开发多沟通，以便达到更好的落地效果。</p>
<p><img data-action="zoom" class=" wp-image-4497584 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZW63WiITRvDKvtyFr4VQ.png" alt width="636" height="424" referrerpolicy="no-referrer"></p>
<p>上面的场景是否很熟悉，开发小哥每天都得忙很多的事情，如果不用线上文档进行同步的话，他们可能转头就会忘记哦。</p>
<p><img data-action="zoom" class="wp-image-4497593 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/TjfcnUGZrpL40JLDp78M.png" alt width="633" height="360" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、B端的设计规范需要整理哪些东西？</h2>
<h3>1. 页面布局</h3>
<p><strong>1）统一设计尺寸</strong></p>
<p>据统计，目前 PC 端用户屏幕分辨率占比排名前三的是 1920*1080、1366*768、1440*900。</p>
<p>以 1440 来设计的话是一个比较合适的尺寸，向上适配或者向下适配误差会比较小。</p>
<p><img data-action="zoom" class=" wp-image-4497598 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/dLhfFtUHZvRa6oC4KU5x.png" alt width="637" height="425" referrerpolicy="no-referrer"></p>
<p><strong>2）页面框架</strong></p>
<p>主流页面框架主要分为左右栏布局和上下栏布局。</p>
<ul>
<li><strong>左右布局：</strong>顶部菜单栏、左侧菜单栏为固定结构，右侧主体内容根据分辨率进行动态缩放。</li>
<li><strong>上下布局：</strong>顶部菜单栏为固定结构，主体内容进行动态缩放，需定义两边空白区域宽度。</li>
</ul>
<p><img data-action="zoom" class="wp-image-4497606 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/tSX3DSFTSuJ9geAyjeag.png" alt width="640" height="364" referrerpolicy="no-referrer"></p>
<p><strong>3）栅格布局</strong></p>
<p>栅格系统的使用是为了解决自适应和响应式问题，从而更好地进行产品设计和产品开发。</p>
<p>响应式栅格常采用12和24列栅格系统实现，以满足 2、3、4、5、6 分比布局等多种情况。固定宽度 Column，将间隔 Gutter 进行动态缩放。</p>
<ul class=" list-paddingleft-2">
<li>网格（Grid）</li>
<li>栅格总宽度（Container）</li>
<li>列和槽（Column&Gutter）</li>
<li>边距（Margin）</li>
<li>区块（Col-n）</li>
</ul>
<p><img data-action="zoom" class="wp-image-4497614 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/5MWkSpq6eAXBs30JFWy2.png" alt width="635" height="361" referrerpolicy="no-referrer"></p>
<p>我们的产品是在1440px的框架下进行设计的，采用左右布局的形式，将左侧菜单栏（100px）以及间距（24px）减去以后，就是自适应的内容区域（1292px）。</p>
<p><img data-action="zoom" class=" wp-image-4497620 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/q7COK6WgZNbi6QbkyTeA.png" alt width="638" height="299" referrerpolicy="no-referrer"></p>
<h3>2. 颜色/字体</h3>
<p><strong>1）颜色</strong></p>
<p>主色的选择，需要依据使用人群、目标用户、使用场景、产品属性等因素综合进行考虑。</p>
<p>在颜色使用上B端与C端的目的并不相同。C端颜色使用更大胆自由一些，以抓人眼球为主；而B端端使用则是以辅助产品功能为主，需要遵循对比原则，提升产品易读性。</p>
<p>小例子：以我们产品举例，在定义主色之前，我向产品要来了关于用户人群的调研报告以辅助我去推测目标人群以及使用场景，并通过相关平台（七麦网、艾瑞网）去找到竞品的行业报告。这些资料不仅可以帮你定义产品使用的颜色，还可以辅助你进行风格的定义，将这些报告放入评审的会议里面可以极大增强设计说服力和专业性。</p>
<p><img data-action="zoom" class=" wp-image-4497622 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/3wIeZGOuVpkvkQI1dAGq.png" alt width="640" height="360" referrerpolicy="no-referrer"></p>
<p>通过鲸准与艾瑞网等数据相关网站可以轻松获取行业内的一些基本数据，这些数据足以让我们进行用户画像的初步建立了。</p>
<p><img data-action="zoom" class=" wp-image-4497626 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/otdCBql0T7kylaiyrU3H.png" alt width="632" height="341" referrerpolicy="no-referrer"></p>
<p>在规范好颜色以后，需要与前端进行同步，将颜色赋予单独的编号，方便双方就颜色上达成统一。如下图所示，一个编号对应一个RGB色值。</p>
<p><img data-action="zoom" class=" wp-image-4497630 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/s4Re82F9DXzonuz0LGDp.png" alt width="639" height="738" referrerpolicy="no-referrer"></p>
<p><strong>2）字体</strong></p>
<p>B端页面可读性很大程度是由排版所决定端，而在排版中文字更是重点中的重点。</p>
<p><strong>① 字体选择</strong></p>
<p>在参考相关线上的成熟产品后，发现字体的渲染是一个很复杂的过程，首先我们需要知道在Web世界中存在着五大字体家族，江湖人称font-family：serif、sans-serif、monospace、cursive和fantasy。</p>
<p>font-family规定元素的字体系列，可以把多个字体名称作为一个“回退”系统来保存。如果浏览器不支持第一个字体，则会尝试下一个。</p>
<p><img data-action="zoom" class=" wp-image-4497632 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OC8BgRPbvuVPVhrf6YDH.png" alt width="635" height="166" referrerpolicy="no-referrer"></p>
<p>在实际使用场景中，用户的电脑一般是PC和Mac。但是这两个平台的屏幕材质、渲染方式都不一样，所以使用的默认字体也是不一样的。PC默认使用微软雅黑，而Mac默认使用苹方。</p>
<p>当我们打开一个网站，浏览器会读取font-family中的字体名称，并去检索用户电脑系统中的字体，如果有的话就显示，没有的话检索下一个。</p>
<p><img data-action="zoom" class=" wp-image-4497635 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/vQeHb7G91Q9T7SjzluOk.png" alt width="631" height="217" referrerpolicy="no-referrer"></p>
<p><strong>② 字号与字重</strong></p>
<p>字号的选择有多种方式进行参考，比如等差递增和等比递增的方式。我们自身在字体选择上选择由4为基数进行等差递增方式，在定义字号大小时默认采用偶数。</p>
<p><img data-action="zoom" class="wp-image-4497638 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/1xWOJCplreBPEG0nZZ09.png" alt width="639" height="253" referrerpolicy="no-referrer"></p>
<p>字重的功能是为了在文本种突出重点强调内容，在文本中常采用3种规格的自重（regular，Medium，Smlbold）。设定标题一律采用Medium，正文一律采用Regular，强调内容采用颜色区分大于字重去区分。</p>
<p>在使用字体时，我们需要判断其与背景色的对比度是否符合WCAG2.0的最低标准，即3:1。此处我们可以在创建文字样式时将标准标注进去，当我们使用文字样式的时候就可以随时提醒我们不要滥用。</p>
<h3>3. 分隔与间距</h3>
<p>在日常工作中，会常常出现多个小伙伴协同工作时采用的间距不一致的情况。虽然之前有进行口头上的统一（采用8px为基数）进行设计，但是还是会出现同一情况间距不一致的问题。</p>
<p>在参照现有的成熟系统以后，依据亲密性原则与格式塔原理整理出符合现有业务的间距规范。</p>
<p><img data-action="zoom" class=" wp-image-4497647 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/oT6bTpTq4VyiSdfBiPTv.png" alt width="636" height="347" referrerpolicy="no-referrer"></p>
<p>我会将间距分为竖向间距与横向间距。为了方便管理与沟通我会将他们进行尺寸上的区分（XS、S、M、L、XL）。</p>
<ul>
<li>竖向间距：常用于模块与模块之间，一般采用24px，32px，48px。</li>
<li>横向间距：日常设计中使用频率最高的间距，一般出现在组件与组件之间。</li>
</ul>
<p><strong><img data-action="zoom" class=" wp-image-4497650 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/WOZz426SCu63kqZnOXek.png" alt width="639" height="558" referrerpolicy="no-referrer"></strong></p>
<p><img data-action="zoom" class=" wp-image-4497651 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/J6jzgMkR14Cop3OfZjN7.png" alt width="637" height="340" referrerpolicy="no-referrer"></p>
<h3>4. 图标规范</h3>
<p>B端设计和C端设计里的图标无论是从功能、应用场景、图标的状态等方面都有非常大的差异，如果按照C端的方法去绘制B端的图标那简直是费力不讨好。在之前做C端的图标时常常需要考虑精致感与氛围营造，而B端图标功能则是降低用户认知为优先。</p>
<p>为了方便图标端管理我将图标分为两大类型，分别为基础图标和业务拓展图标。</p>
<p>且图标规定在3种尺寸分别为：XS=12px / S=16px / M=20px / L=24px以方便业务随时调用，且遵循偶数原则。</p>
<ul>
<li>基础图标：常规图标，复用性高且出现地方多。</li>
<li>业务拓展图标：依据不同业务场景进行定制化的图标，常常跟着业务走。</li>
</ul>
<p><strong>1）图标尺寸规范</strong></p>
<p>与间距类似，将图标同等进行划分等级。12号字体搭配外框为12px 图标；14号字体请搭配 16px 的图标；16号以上的字体搭配 20px 图标，以达到更好的视觉效果。</p>
<p><img data-action="zoom" class=" wp-image-4497668 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/CzGoYwks71vPBuylFaG6.png" alt width="637" height="333" referrerpolicy="no-referrer"></p>
<p><strong>2）keyline</strong></p>
<p>通过keyline我们可以保证绘制不同形状的图标的一致性，在keyline的基础上画图标时，基线可以给予我们一定的参考避免图标的比例失衡。可以说keyline是图标的栅格也不为过。</p>
<p><img data-action="zoom" class="wp-image-4497673 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/zb431Duza3Dbc5NhXYyj.png" alt width="635" height="196" referrerpolicy="no-referrer"></p>
<p><strong>3）业务图标制作规范</strong></p>
<p>除了常规基础图标外，针对业务场景制作的定制化图标如果不加以限制就会显得五花八门非常杂乱。当图标数量增加到一定程度时就会出现同一表意图标有不同的样式结果。因此有必要在保持图标美观易读的前提下对业务图标进行规整。</p>
<p><img data-action="zoom" class="wp-image-4497675 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/rqeT2teGgYtZEw377Ik9.png" alt width="637" height="333" referrerpolicy="no-referrer"></p>
<p><strong>4）图标命名规范</strong></p>
<p>随着业务增多，团队内之前的随意命名的习惯也开始凸显出弊端。在图标规范中，业务图标需要将每个业务区分开，每个业务都有着单独的后缀，这样可以让公用图标与业务图标更方便的溯源。</p>
<p><img data-action="zoom" class=" wp-image-4497701 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/iwcIpXoaqUNWEzE53gQ3.png" alt width="636" height="183" referrerpolicy="no-referrer"></p>
<p><strong>5）图标的图层整理</strong></p>
<p>随着业务线拉长，涉及的团队人员也越来越多。简洁整齐的图层不但能提升团队效率还可以让会影响接手工作小伙伴的心态。所以图层整理还是得纳入规范内的，此处不进行具体规范仅做提醒和警示作用。</p>
<p><img data-action="zoom" class=" wp-image-4497702 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/PgDJP27r1qpK5ywBEpEP.png" alt width="631" height="296" referrerpolicy="no-referrer"></p>
<p><strong>6）图标交付/iconfont</strong></p>
<p>在与前端开发沟通达成共识、图标制作完成确认后，将图标上传到阿里巴巴图标库中，更方便前端调用图标大小和调整颜色。</p>
<p>如果开发需要自己去找到相关图标，也可以给予权限让开发从蓝湖上传图标（前提是得整理好图标到蓝湖上）。</p>
<p><img data-action="zoom" class=" wp-image-4497703 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/kCzrMPMaTEZ5bkoH0xNa.png" alt width="637" height="284" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、搭建组件库你需要知道的几件事</h2>
<h3>1. 组件库到底是什么？</h3>
<p>组件库常可以类比于常玩的乐高玩具，每个组件都是积木，而产品相当于我们拼好的模型。我们可以根据业务需求，以“搭积木”的方式，让“模型”快速拼起来。</p>
<p>但是并不是说我们可以随心所欲搭建积木，至少需要看一看“说明书”，而这“说明书”就是设计规范。产品、组件和规范差不多就是这样的关系。</p>
<h3>2. 搭建组件库前需要知道的小知识</h3>
<p><strong>1）原子设计/拆分</strong></p>
<p>在业务已经发展到一定体量情况下，需要将项目中具备服用行以及拓展性的模块进行拆解。</p>
<p>对于B端产品来说，筛选的时候会依据之前迭代的版本内容，把页面一一罗列出来，将可替换与相似的模块提取，并利用思维导图的方式统一归纳，并做成可以被替换的组件。</p>
<p>组件的替换建议合成一个大的排期进行替换，避免了线上组件不一致导致体验问题。</p>
<p>以我们产品为例，依据产品类型将组件拆分为：基础组件 、业务组件、数据可视化组件、常用模块。</p>
<p><img data-action="zoom" class=" wp-image-4497705 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/qxJrVMpWsyDNrcft2Kjc.png" alt width="636" height="358" referrerpolicy="no-referrer"></p>
<p><strong>2）原子设计</strong></p>
<p>将产品拆分后，此时得到很多可复用组件。我们再依据原子设计理论针对性进行拆解直至拆分出5个层面：</p>
<ul class=" list-paddingleft-2">
<li>原子（元素、要素）</li>
<li>分子（组件）</li>
<li>组织（模块）</li>
<li>模板（原型）</li>
<li>页面（填充内容）</li>
</ul>
<p>从原子开始重新依据定好的视觉规范进行更改，再由原子组成新的分子。</p>
<p><img data-action="zoom" class=" wp-image-4497707 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/P8Zz0gyZjlf2MBqd3jnX.png" alt width="648" height="546" referrerpolicy="no-referrer"></p>
<p><strong>3）盒子box</strong></p>
<p>在与开发小哥沟通设计规范制定的过程中，常提到他们写CSS样式的时候是采用盒子（box）去写的。通过一个个盒子填充来将我们的组件元素放入其中，最终形成前端展示的页面。</p>
<p><img data-action="zoom" class=" wp-image-4497710 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/kMITrDmQM0Gl7OBPi0cY.png" alt width="636" height="358" referrerpolicy="no-referrer"></p>
<p>走查时使用浏览器我们也可以看到开发写的盒子，了解盒子也可以方便我们走查时知道问题在哪。</p>
<p><img data-action="zoom" class=" wp-image-4497714 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/gDyAE9x3kvyUPDS0cJdB.png" alt width="637" height="358" referrerpolicy="no-referrer"></p>
<h3>3. 按钮</h3>
<p>按钮设定有五种类型：主按钮、次按钮、虚线按钮、文本按钮和链接按钮。</p>
<p>主按钮在同一个操作区域最多出现一次。设计师可以依据自身业务属性，针对性修改按钮的圆角大小与描边，圆角曲率越大越柔越小越硬朗。</p>
<p>除了按钮状态，在制定规范时还需要考虑到按钮的其他情况。比如按钮在放大使用时圆角曲率的变化。</p>
<p><img data-action="zoom" class=" wp-image-4497715 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZSUkTJjO5Ei8v4RpLX7m.png" alt width="637" height="358" referrerpolicy="no-referrer"></p>
<p><strong>1）按钮的尺寸规定</strong></p>
<p>常用的按高度可设定为：24px、32px、40px、48px，超出48px的按钮都属于特殊按钮。需要进行单独设置的，宽度随着内容区域自适应。</p>
<p>常规的按钮可分为：主要按钮（Primary Button ）， 次要按钮（Secondary Button），虚框按钮（Dashed Button），失效按钮（Disable Button ），危险按钮（Danger Button），文字按钮（Text Button）等，对照着不同使用场景灵活运用即可。</p>
<p><img data-action="zoom" class=" wp-image-4497723 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/PBIsk7455HNbynILzDv4.png" alt width="636" height="358" referrerpolicy="no-referrer"></p>
<p><strong>2）按钮的自适应</strong></p>
<p>按钮与按钮间的间距随着网页尺寸变化而变化，常设定几种断点规格进行选择。</p>
<p><img data-action="zoom" class=" wp-image-4497725 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/qAlGvuOGDoK56He6Tk9Y.png" alt width="638" height="359" referrerpolicy="no-referrer"></p>
<h3>4. 表单</h3>
<p>表单承载着采集数据信息的功能，是用户在数据输入的核心模块之一。表单基础单位是由标签，输入框，填写提示，操作按钮构成。一行行列表单位组成表单界面。</p>
<p><img data-action="zoom" class=" wp-image-4497728 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/2R5UPU5S7JMIGFyDKPe7.png" alt width="643" height="362" referrerpolicy="no-referrer"></p>
<p><strong>1）常见的组合样式</strong></p>
<p>据统计，表单内常见的组件样式有：文本框、文本域、选择器、开关、checkbox、radio、步骤条，上传/下载、标签页等。组件类别繁多，在选用组件时需要考虑其排布形式，在多列表情况下会着重描述这一点。</p>
<p><strong>2）单列表单与多列表单如何选择？</strong></p>
<p>在web页面内，在左侧导航条较小情况下会导致右侧输入区域空间较大、纵向空间不足的情况。</p>
<p>若此时业务需求输入内容较多且难以采取分模块、分步骤交互时，采用双列或多列表单的形式提高空间利用率也是可以接受的（ps：可以参照菲兹定律，采用多列的形式需要着重考虑文本框内容长度以及表单间间距的合理性）。</p>
<p>下面以自身业务为例子，列举在工作中多列表单出现的一些状态。</p>
<p><img data-action="zoom" class="wp-image-4497731 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/mfp3B15Fl8nJUBychXel.png" alt width="625" height="473" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="wp-image-4497733 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/vhMuFnW9mpWqp15BPaXB.png" alt width="637" height="361" referrerpolicy="no-referrer"></p>
<p><strong>3）多列表单极端情况</strong></p>
<p>采用多列表单后，随着复杂程度提升会出现各种各样的情况，此时设计师还需考虑到极端情况下表单显示问题。如标签过长规则（标签最好在最初阶段进行限制）、带按钮如何进行换行、屏幕分辨率改变如何进行处理等。建议由设计师制定规则时与前端小哥进行深入沟通，以保证最终的落地效果。</p>
<p><img data-action="zoom" class=" wp-image-4497738 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/k7H4Da2e9aYXp0uEO3Xo.png" alt width="636" height="481" referrerpolicy="no-referrer"></p>
<p><strong>4）让表单具有节奏感</strong></p>
<p>之前我在表单宽度没有进行有意识的规范，导致整个表单呈现一种无序状态，通过有意识控制表单的宽度可以使我们对整体页面有着更好对把控，整体对品质感得到提升。可以对现有业务的表单进行梳理，整理出适合自身业务的表单长度单位。此处推荐阅读Ant_Design《整齐划一？不如错落有致》相信你会有更深的理解。</p>
<p><img data-action="zoom" class="wp-image-4497742 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/CMfqDRI7cqEfn1a1QPvJ.png" alt width="638" height="359" referrerpolicy="no-referrer"></p>
<h3>5. 表格</h3>
<p>表格，常用语展示数据，用户既可以在表格里面获取信息，也可以在表格内进行数据输入。相对于表单，表格可以进行多维度的数据整理与分析。其难点在于表格的组件交互联动多，以及数据展示的形式多。表格的信息密度很高是我们在B端页面设计中涉及最多的一个组件。</p>
<p><strong>1）表格的构成</strong></p>
<p>为了方便记忆，个人将表格分解为2大区域分别是：操作区域以及信息展示区域。</p>
<ul>
<li>操作区域：标题、工具栏、操作单元格；</li>
<li>信息展示区域：表头、信息展示单元格、分页控件。</li>
</ul>
<p><img data-action="zoom" class=" wp-image-4497746 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/87qGBe3jl8g8YPuJjDNG.png" alt width="676" height="317" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/SDVPPuM8sme13hHCZRG7.png" width="675" height="317" referrerpolicy="no-referrer"></p>
<p><strong>2）表头与单元格</strong></p>
<p><strong>① 表头</strong></p>
<p>表头分为带选框与不带选框/带icon与不带icon，需要注意的是表头上文字表意要清晰，简洁的表头能让用户更快明白此列的内容。此时需要与业务方沟通限制字数，若字数过长无法删减，则可以考虑使用tooltips。</p>
<p><img data-action="zoom" class=" wp-image-4497759 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZmwLEYdGU4hkZjSfV2Ae.png" alt width="675" height="269" referrerpolicy="no-referrer"></p>
<p><strong>② 单元格</strong></p>
<p>在与开发沟通后发现，开发在写表格时并不与我们设计师的逻辑相仿，设计师在设计表格时是依据行与列的思维进行表格的设计，而前端则是通过许多的</tr>标签与</td>标签进行堆砌而成。因此在设计时将单元格规范好，前端将更容易还原好表格。</p>
<p><img data-action="zoom" class=" wp-image-4497760 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/eQwRnVIkHB7b9RU8C5Va.png" alt width="667" height="266" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" wp-image-4497764 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Is17zG1OutNxysCq0ohg.png" alt width="682" height="283" referrerpolicy="no-referrer"></p>
<p><strong>3）表格在页面中的样式规范</strong></p>
<p>一般来说，表格内组件功能复杂，为了提升整体表格统一性与设计效率，我整理了业务上几乎所有的表格样式。整理需求后发现几乎所有的表格蕴含序列号与复选操作，故整理了一套通用表格规范以供小伙伴们参考。</p>
<p>常规页面通过栅格，由列的数量决定列宽，与现在的主流框架组件一致；特殊页面可以与前端沟通后，在设计稿里面标注某单元格进行固定宽度，其他百分比缩放进行处理。</p>
<p><img data-action="zoom" class="wp-image-4497768 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/R1FsLCTorCNwo9o35oQo.png" alt width="676" height="344" referrerpolicy="no-referrer"></p>
<p><strong>4）业务中表格的常见问题</strong></p>
<p>此处仅提出几个个人业务中常见情况，更多的表格问题解决方案推荐查看CE青年《B端设计指南06 – 表格（下） 》。</p>
<p><strong>① 有些特殊字段采取左对齐不美观该怎么规范对齐方式？</strong></p>
<ul>
<li>常规文本字段：可点击的字段、普通文本类、数字字母等，此类长短参差不齐的，建议采用左对齐的方式；</li>
<li>特殊字段：日期、时间、字符数一致且比较短可控的，建议与表头居中对齐；</li>
<li>业务字段：金额、状态标签、类型标识等业务性较强的，可根据相关特性与阅读习惯确定对齐方式。</li>
</ul>
<p><strong>② 文本内容过长怎么解决？</strong></p>
<p>当表格列数过多或者横向数据过长时，难免出现单个单元格内数据展示不下的问题，此时常采取换行的方式处理（ps换行处理后的结果需要与后端沟通好，避免出现换行不分字段的情况）。</p>
<p><img data-action="zoom" class=" wp-image-4497771 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/af4cuneAvQ8mn0h85zVF.png" alt width="674" height="343" referrerpolicy="no-referrer"></p>
<p><strong>③ 单元格内操作项数量不一致时，该怎么处理？</strong></p>
<p>此处建议采用平铺式进行处理，此方式适用方式比较广，稳定性较高（亲测）。</p>
<p>将所有操作按照一定的预设排列顺序进行平铺，这种方式能够适应B端的大多数场景。将操作都简单平铺出来虽然看上去简单粗暴，但是在实际工作中，也是一种不错的处理方式。</p>
<p><img data-action="zoom" class=" wp-image-4497772 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/N0sQRCJEFAbQBxg7M0xg.png" alt width="670" height="341" referrerpolicy="no-referrer"></p>
<p><strong>④ 每一页表单展示多少行合适？</strong></p>
<p>如果你经常与开发打交道你就会发现，开发对表格信息的处理逻辑是通过逐行从上到下进行渲染处理的。如果不对行数进行特定的规范，那么开发可能会采取渐进式加载（用户通过滚轮下滑的方式滚动到末尾再进行下一批量的数据加载）来解决表格内容过多的问题，这就会导致体验上的不统一。</p>
<p>可以梳理当前业务，遵循尽量不让用户过多滑动为原则定制每页的行数。</p>
<h3>6. 弹窗</h3>
<p>B端业务中使用的弹窗主要分为模态弹窗和非模态弹窗，其最大区别在于对师傅会打断用户的操作流程，模态弹窗会要求用户必须给予操作。而非模态弹窗不会打断用户当前操作流程，仅仅起提醒用户的作用，非模态弹窗常常过一段时间会自动消失。</p>
<p><img data-action="zoom" class=" wp-image-4497775 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZhJYPNJWCOZ5cq09zgeZ.png" alt width="675" height="220" referrerpolicy="no-referrer"></p>
<ul>
<li>常见的模态弹窗有：对话弹窗、表单弹窗分、分步弹窗等；</li>
<li>常见非模态弹窗有：通知、全局提示、警告提示、气泡提示、文字提示等。</li>
</ul>
<p><img data-action="zoom" class=" wp-image-4497777 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/jOuOBLLRrxqh0435rKYU.png" alt width="674" height="343" referrerpolicy="no-referrer"></p>
<p><strong>1）弹窗依据栅格自适应</strong></p>
<p>为了方便规范系统内等弹窗位置和大小，将弹窗作为一个单独模块进行处理是一个不错的选择，业务中弹窗的性质一般都是横向居中展示。</p>
<p>将弹窗纳入栅格体系中。前端小哥可以让弹窗的宽度随着列宽的大小变化而变化。</p>
<p><img data-action="zoom" class=" wp-image-4497779 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/vp51z4u95vDWSfiYp7Qu.png" alt width="674" height="343" referrerpolicy="no-referrer"></p>
<h3>7. 组件库如何进行迭代</h3>
<p>当我们把第一个版本组件库搭建完成后，对于它当更新和迭代需要依据业务当发展不断去维护。建议设计团队内有规划有目地去维护组件库当多样性，以保证组件库能随着业务的发展一起成长起来。</p>
<p>因篇幅原因，此处遍不细讲此部分内容，如果大家感兴趣后期可以再单开一篇讲讲组件库的迭代流程，此处附上有赞的组件库迭代流程供大家参考。</p>
<p><img data-action="zoom" class=" wp-image-4497780 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/scclhQL50MWJtFABCXQK.png" alt width="688" height="190" referrerpolicy="no-referrer"></p>
<p><strong>小总结：</strong>组件库需要保持简洁和清晰，不能为了做组件而做组件。最好的状态是适合业务当前需求的状态，组件在于精细而不在于数量。臃肿对组件库不但不能提升整体团队效率，反而会拖垮整个工作的节奏。</p>
<h2 id="toc-6">六、如何输出规范？</h2>
<p>搭建设计规范和我们日常处理工作需求类似，并非输出一份文档就结束了。我们还需要将做好的设计规范推广给包括设计小伙伴、PM和开发小伙伴的团队内外，并且需要得到团队内的一致认可才算是初步完成。</p>
<h3>1. 如何推广给PM</h3>
<p><strong>利益点：提升协作效率，减少工作成本。</strong></p>
<p>在启动设计规范的整理之前，内部宣讲让PM对于设计规范的搭建已经有了一个基础的概念，否则也不会分配资源给予时间去搭建整体的设计规范。</p>
<p>可以通过提升PM与设计的效率和降低原型搭建成本去切入，通过组件库以及通用模版的搭建PM只需要极低的成本学习一下组件库怎么使用（我们的PM是使用sketch搭建原型），即可搭建高保真的原型界面。甚至完善好组件库后直接不需要设计的参与，开发通过原型组件库搭建页面。</p>
<p><img data-action="zoom" class=" wp-image-4497781 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/M2hB5uHYPC5Dpn0oBNxz.png" alt width="676" height="380" referrerpolicy="no-referrer"></p>
<h3>2. 设计团队内部如何推广</h3>
<p><strong>利益点：提升设计效率，减少人力损耗。</strong></p>
<p>设计规范一般由团队内小伙伴共同制定，基本上已经对规范的优势达成共识。因此主要讲讲如何更好在团队内部使用规范。</p>
<p><strong>Library共享+更新日志</strong></p>
<p>通过Sketch Library 共享组件库，并建立更新日志规范项目流程提升效率。</p>
<p><img data-action="zoom" class=" wp-image-4497782 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/mrs943IDf1jRglvN9kBX.png" alt width="674" height="379" referrerpolicy="no-referrer"></p>
<h3>3. 研发团队内容如何推广</h3>
<p><strong>利益点：封装组件，更少的更改，缩短研发流程。</strong></p>
<p>需要研发团队认可设计规范，前期前端的参与是必不可少的。在制作规范时设计师了解了前端开发的一些简单原理，前端开发也能及时了解设计师的想法，大家不再是各司其职而是串联起来共同协作，当规范确认下来前端就不会频繁改动组件，而且在有限的项目时间中。设计规范的统一极大缩短了设计和前端开发所需的时间，为后面的项目争取了空间。</p>
<p><strong>小总结：</strong>本人时常听到一些小伙伴的反馈在公司内部设计师的话语权不够，公司不太重视设计。其实总结下来就是专业性得不到团队内的认可。</p>
<p>设计师在工作中如何体现自己的优势是通过一次次的需求业务来体现的，许多小伙伴在做业务时既没有前期调研，也没有进行资料收集，仅仅只是闷头开始动手做，往往结果不会太好。</p>
<p>在处理需求时团队内部的同事也是可利用的资源之一，多与他们协作获取业务相关的信息，不仅能帮你站在全局的角度去思考这个业务，而且能让团队内部成员具有参与感，输出的结果当然更容易让他人认可。</p>
<h2 id="toc-7">七、整理设计规范对个人的影响！</h2>
<h3>1. 收集信息能力</h3>
<p>通过整理规范，需要收集目标用户、使用场景以及前期调研等众多资料，此时我们需要去发现信息以及整理信息。这一点在日常工作中也常常被使用到，日常中我们在做需要时也需要不断去挖掘相关对信息才能从容解决问题。</p>
<h3>2. 归纳总结能力</h3>
<p>将收集好的信息进行分类整理，这要求需要一定的逻辑性。</p>
<p>在设计基础框架时，合理分类可以协助我们处理好每个控件对层级，这项能力无论是在工作还是日常中都有着巨大对好处，可以帮助我们从一堆繁杂的事物中“提纲挈领”，换言之就是“化整为零”，做减法，提取出最关键对因素。</p>
<h3>3. 全面复盘能力</h3>
<p>将信息归纳整理好后，需要对全局进行思考，全局的交互都需要考虑到位，比如什么情况下适合跳转页面、什么情况下适合给与用户弹窗、大体符合什么交互原则。</p>
<p>除了对大体交互需要考虑到位，细节上也不可以忽视，比如异常情况、极端情况该如何去处理，组件之间该怎么去配合等。在日常工作中我们也可以逐渐有意识去培养此类技能，对项目全局思考的越多，那么对整体项目对把控能力也就越强，与他人合作也会越显得专业。</p>
<h3>4. 表达能力</h3>
<p>在整理设计规范时，难免会遇到模凌两可举棋不定的时候。</p>
<p>此时可以寻求向上或者向下的资源寻求帮助，具备良好的表达能力能迅速帮助我们将问题阐述清楚，我认为表达能力是设计师需要具备的重要技能之一。每次在求助它人或向他人汇报，都需要在全面复盘问题过后做到心里有数，将问题自己复述一次是否有漏洞或者没考虑清楚的地方。</p>
<p>长此以往你表达的事情会更清晰，别人也更容易听懂你说的事情、快速理解内在逻辑，那么说服别人推动工作的难度也会越小。</p>
<h3>5. 沟通能力</h3>
<p>在多次与他人沟通，个人认为是对我本人帮助最大的能力了。我总结了几个和上下游沟通的小技巧希望能帮助到小伙伴们，在开始与他人沟通之前我们需要搞清楚我们沟通的原因与对象。</p>
<p><strong>原因里面包含：</strong></p>
<ul>
<li>包含为什么要进行沟通？（推进项目还是告知）</li>
<li>想要达到什么结果？（自己能做多少妥协，底线在哪）</li>
<li>预判对方对这件事持什么态度？（支持/反对/无所谓）</li>
<li>希望对方做？自己的目的是啥？（求助还是说服）</li>
</ul>
<p><strong>对象里面包含：</strong></p>
<ul>
<li>和谁沟通？（上游还是下游）</li>
<li>他们对这件事了解多少？（比我多还是比我要少，需不需要简单讲解一些）</li>
</ul>
<p>当然在沟通时还需要考虑方式和语气，这些都需要好好斟酌。也遇到过情绪不太好的开发小哥，这个时候我们更不能将情绪激化。一般这些情绪化的态度过一会都会消散，可以采取冷处理，等情绪过后换一种方式沟通看看。</p>
<p>关于B端的设计规范想要落地其实并不是靠设计师这一环节努力就可以的，设计规范的建立本身就考验设计团队的设计能力以及推动落地的能力；一个设计规范能够成为团队内的共识是多方共同协作的结果。</p>
<p>拥有一颗积极学习的心做事，就算最后结果不尽人意，从中也能获取很多东西。终于在放假前整理完毕，最后如果我的分享对你有一丝丝帮助那就是对我最大的肯定，感谢看到最后。</p>
<p>参考文献</p>
<p>1.Antdesign 的官网</p>
<p>2.美芳Mia/体验设计手册</p>
<p>3.CE青年——B端设计导航（强烈推荐）</p>
<p>4.罗耀——《概念——原子设计理论 》</p>
<p> </p>
<p>作者：Weiyehe</p>
<p>原文链接：https://www.zcool.com.cn/article/ZMTIyMTgxMg==.html</p>
<p>本文由 @Weiyehe 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
                      
</div>
            