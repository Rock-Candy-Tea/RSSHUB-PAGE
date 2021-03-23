
---
title: 'B端Dashboard设计指南（一）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/V6l0ODz89bQg7zgodBMg.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 23 Mar 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/V6l0ODz89bQg7zgodBMg.jpg'
---

<div>   
<blockquote><p>编辑导语：Dashboard在B端设计中经常可以见到，并且在网页端用的比较多，Dashboard的设计页面不用过于复杂，因为对于To B用户而言，它的核心始终是传递信息；本文作者分享了关于B端Dashboard设计的详细指南，我们一起来了解一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4422440" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/V6l0ODz89bQg7zgodBMg.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、Dashboard的含义</h2>
<h3>1. 前言</h3>
<p>Dashboard在B端设计的工作中是一个绕不开的话题，在此我根据自己工作中实际的一些经验总结给大家归纳出一篇更符合工作场景中Web端的Dashboard设计内容。</p>
<p>什么是Dashboard？</p>
<p>Dashboard的中文直译是仪表盘，最初与dashboard相关在界面出现的是苹果电脑系统Mac OS X v10.4 Tiger操作系统中的应用程序，用作称为“widget”的小型应用程序之运行基础。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/8epq7FQvRtPMZtiTSs2w.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<h3>2. B端常见Dashboard</h3>
<p>2013年Stephen Few写的《Information Dashboard Design》中指出“仪表盘是为了实现某些特定目标而对重要信息进行的视觉传达，对一屏上的内容进行组织呈现使人一瞥便能掌握其所传达的信息。简单点来说就是：<strong>为用户提供全局概览，让用户快速掌握工作进展及进入工作状态并可以访问最重要的数据，功能和控件。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/Pie78jmV6SdCgA7oNYjx.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/VBnVwS3pMBQPpF5Eifle.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<h3>3. Dashboard设计案例</h3>
<p>以下是Dashboard常见4点设计不是很好的案例，现在带大家一个个看下怎么才是更为合理。</p>
<p>案例一：右边Dashboard上的信息做了层级的区分，相对左边更加直观。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/eh1VJfzQDUUKYHwlQnNe.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p>案例二：左边Dashboard颜色偏荧光色，色彩语言相对右边不适合长期工作使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/Ojmh6IIKBPXqqQ9JzVhJ.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p>案例三：设计方案时没有采用格栅格化解决适配对不齐等等问题</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/9CJGhJa2mPHl5ZdhD0Gi.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p>案例四：dashboard模块之间间距没有呼吸感。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/r38KZqtPGbWuIBP5uEKg.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、B端Dashboard的功能分类</h2>
<h3>1. 设计师需要了解的功能分类</h3>
<p>B端设计中，设计师要实时了解哪些是重要内容以及核心数据。Dashboard可以直接传递出：“业务整体状况如何？有哪些关键指标？各指标的运行情况分别如何？哪些指标出现异常？需要用户做些什么？”。</p>
<p>由此可知，B端Dashboard产品中大多数都以看为主，辅以功能控制；主要分为监控操作、分析处理两大场景。当业务较为复杂时，可以用战略概览场景提供快速入口。<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/kzV8Rdf3rOLItBt1WKR6.jpg" alt width="2898" height="1356" referrerpolicy="no-referrer"></p>
<p><strong>1）监控操作</strong></p>
<p>使用户可以一目了然地检查其状态，提供关键指标实时监测并且告知异常状态，更重视实时观看状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/KyRVuTGMsPPKcHx8slMZ.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><strong>2）分析处理</strong></p>
<p>通过数据图表，配合控件进行不同维度的数据分析。以数据为中心，并显示尽可能多的相关数据视图。</p>
<p>2.1 数据性Dashboard。数据概览可视化展示为主。帮助用户提供较为直观数据维度，更好分析决策。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/KY9E9Doio9oa3XfUuiD8.jpg" alt width="2902" height="1742" referrerpolicy="no-referrer"></p>
<p>2.2 综合性Dashboard，既有提供数据全局概览可视化，同时也能快速在页面进行操作完成工作。国内B端产品最常出现的Dashboard功能模式。本篇文章也是着重介绍如何完成这个类型需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/Vcd43qlONwkTqMlB8fme.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><strong>3）战略概览</strong></p>
<p>在复杂的业务中，可以呈现业务分散的重点信息，用户可以通过提供入口快速跳转至相关模块。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/vx3psDllMgT3Wa92XjY5.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、设计前分析</h2>
<h3>1. 了解Dashboard的用户</h3>
<p>B端设计过程中每多了解一个维度分析就更有利于下一步Dashboard框架搭建。因此在对Dashboard有了一些简单了解之后，我们再来了解下用户场景。</p>
<p>例如：用户是财务人员审批商户充值申请。工作人员进入dashboard之后先是进行充值打款申请。</p>
<p>那么设计时可以考虑在Dashboard中加入常用功能：充值。并且需要给到相应充值数据概览：账户余额，每个B端产品都有自己特定工作场景；因此从用户、场景和任务这三方面考虑，可以做到帮助设计师更清晰设计dashboard布局以及设计自查。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/hGJKziU2talH5tWBLoFy.jpg" alt width="2898" height="1356" referrerpolicy="no-referrer"></p>
<p>因此以上这些信息都是需要在设计Dashboard时弄清楚的内容。</p>
<h3>2. 信息处理</h3>
<p>当弄清楚需要呈现信息内容后，需要进一步对信息做处理。</p>
<p>从用户的角度，举个例子在FMS财务系统记账中，财务需要查看季度报表；那么数据的单位以默认季度呈现会更为符合使用用户需求，准确且高效。</p>
<p>具体可以从以下四个维度来做进一步处理：覆盖范围、时间跨度、粒度、个性定制；一般核心指标不超过7个，确定核心指标的联系及优先级。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/N3SMKTH5ARywiDh3mtrg.jpg" alt width="2898" height="1536" referrerpolicy="no-referrer"></p>
<p>合理的信息结构能够帮助用户高效阅读，理解内容。如何将信息碎片有逻辑地组合在一起，合理呈现和布局，选择使用什么结构视内容而定。</p>
<p>举个例子：</p>
<p>对于<strong>管理者</strong><strong>的角色</strong>来说使用Dashboard的诉求是：及时把控业务情况。</p>
<p>信息处理内容：</p>
<ul>
<li>掌握重要业务数据：经营数据，订单数据，客户数据；</li>
<li>了解员工工作进度；</li>
<li>处理急需解决的工作任务。</li>
</ul>
<p>对于<strong>执行者</strong><strong>的角色</strong>来说使用Dashboard的诉求是：高效完成工作任务。</p>
<p>信息处理内容：</p>
<ul>
<li>急需解决的工作任务：待发货订单，待退款，待跟进客户；</li>
<li>了解自己的工作进度；</li>
<li>经常使用的功能：发布商品，添加客户，开单；</li>
<li>查看重要通知公告：公司发布的公告。</li>
</ul>
<h3>3. 了解Dashboard的表现设计类型</h3>
<p><strong>Dashboard表现结构常见两种类型：卡片型、流程型。</strong></p>
<p><strong>卡片型：</strong></p>
<p>最常见就是卡片型。即将有相关联的内容进行分组呈现，让Dashboard内容归类而不杂乱无章。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/cUTk5nH1FzskXFYv27md.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><strong>流程型：</strong></p>
<p>内容相互之间具有一定的逻辑关系，如地理位置关系、数字包含关系、对象父子关系等，这种结构可以让对象之间的逻辑关系十分直观。很直观的呈现了资源对象之间的相互关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/8hrnkfKjtv52vWuJq89u.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、Dashboard的设计</h2>
<h3>1. Dashboard的表现构成</h3>
<p>国内B端产品一般是由以下这几个部分组成的。全局导航、数据概览、待办事项、常用功能、任务进展、平台推送、数据图表。</p>
<p>下面带大家仔细看下具体每个部分具体如何设计：</p>
<p>1）全局导航</p>
<p>在B端Dashboard中，全局导航一般由三个部分组成。平台LOGO、功能入口导航、快捷功能导航。</p>
<p><strong>平台LOGO：</strong></p>
<p>一般这里都会放LOGO，对于一些壁垒标准化B端服务，这里通常是给好标准规则，后台自动配不同客户的LOGO。因此要考虑到区域的色彩是否适用各种不同LOGO。如果是OA或是定制化B端服务，那么就可以直接定制设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/2PMYgluXS0CaunHAXpXL.jpg" alt width="2902" height="1738" referrerpolicy="no-referrer"></p>
<p><strong>功能入口导航：</strong></p>
<p>就是菜单导航，在B端Dashboard一般都是在侧边。建议最多不要超过9个，遵循7±2原则。尽量将同类型归类，好好利用下二级分类。另外入口不要太深，用户容易找不到入口。尽量设计优化合并来减少用户使用负担。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/PVQeDiQAqxOlCTFp3Rzn.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p>在国内B端产品中，最常就是将功能入口导航放在侧边。适用于更专注功能和快速操作的系统</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/H6iKsG9MeW8wwFnjXHWB.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><strong>优点：</strong></p>
<ul>
<li>拓展性，一级导航的数目可以展示更多；</li>
<li>层级清晰，一二三级导航都可以流畅展示；</li>
<li>操作效率高，用户在操作和浏览中可以快速定位和切换当前位置。</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>视觉动线左右折回，比顶部导航更易疲劳；</li>
<li>内容区的排版空间更小，需要考虑适配问题。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/8mXCtqZIpiPuKznnQHfW.jpg" alt width="2902" height="1626" referrerpolicy="no-referrer"></p>
<p>在国内B端结构比较庞大的后台中,通常会将功能入口导航设计为混合模式。混合模式就是将功能入口分为顶部与侧边两边都有。这是因为侧边模式已经无法层级扩展性已经无法很好的满足产品架构了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/DobBCvO4Bl3m54drgJCu.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><strong>优点：</strong></p>
<p>层级拓展性强，可达四、五级导航。</p>
<p><strong>缺点：</strong></p>
<p>操作难度上升、视觉动线更复杂。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/rb3Eeo9kq9ZzvpHeLZbt.jpg" alt width="2902" height="1536" referrerpolicy="no-referrer"></p>
<p>还有一种模式：顶部模式，这种模式在国外产品中较多，在国内的B端产品中较为少应用。原因之一是起初最早的国内B端产品就采用这种排版模式，在国内形成了一种用户操作习惯。国外最常见的B端顶部导航：saleforces、hubspot、zoho。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/CsS7ik2iET9535Lx2gNy.jpg" alt width="2902" height="1740" referrerpolicy="no-referrer"></p>
<p><strong>优点：</strong></p>
<p>沉浸感比侧边以及混合都要强，几乎不会对于用户的阅读行为有干扰，因为Web也有顶部浏览器菜单。</p>
<p><strong>缺点：</strong></p>
<p>一级导航栏的栏数及字段内容受限严重。国内B端产品会有很多快捷功能就更不利用采用这种模式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/4tqtCd2LfvWeH8Ct6Amb.jpg" alt width="2902" height="1488" referrerpolicy="no-referrer"></p>
<p><strong>快捷功能导航：</strong></p>
<p>一般包含：消息通知、账号信息、帮助中心、设置。在国内B端产品中基本上都是在右上角。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/lKcaw4PWHnDgscP4cJj7.jpg" alt width="2902" height="1226" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/dViVN2uUH9Npqw5OkvF2.png" alt width="2914" height="886" referrerpolicy="no-referrer"></p>
<p>2）数据概览</p>
<p>在B端Dashboard中，数据概览通常都是选取最关注的数据指标来展示，而不是全部数据；选取最关注的时间段，而非全部时间段。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/MIG6szXsUyQEEBRQovIK.jpg" alt width="2902" height="1594" referrerpolicy="no-referrer"></p>
<p>构成：数据名称+数字</p>
<p>这个模块在设计表现上最重要就是信息层级的设计处理。如何能够让用户一眼就看到最关注的数据内容指标。设计时注意突出数据才是关键。设计时关键数字上就要字号大一点，甚至可以采用特殊的数字字体，例如DIN系列，来加强对比。</p>
<p>3）待办事项</p>
<p>待办事项模块通常是应用在执行角色的Dashboard中。节省工作人员寻找任务的时间，避免遗漏任务。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/pWKb0lWh55vUPBkvXL8B.jpg" alt width="2902" height="1500" referrerpolicy="no-referrer"></p>
<p>构成：待办事项名称+数字+可点击跳转的链接</p>
<p>待办事项的展示方式可以是数据可视化也可以是数据概览。但是有一点，数据必须是要能够点击的，因为待办事项就是要有入口去操作。同时也可以把待办事项平铺出来，平铺几个可以根据具体情况定。如果待办样式本身很多的情况下，可以采用tap切换的样式全部展示出来。</p>
<p>4）常用功能</p>
<p>用户高频操作快捷入口，点击跳转相应操作页面。这个模块每个b端产品都不一样，需要仔细反复斟酌是否是用户需要的高频功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/pEyvgE5FqmQLVmIFSKHK.jpg" alt width="2902" height="1500" referrerpolicy="no-referrer"></p>
<p>5）任务进展</p>
<p>用户当前最关心的任务，常用进度条或者时间轴的形式表示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/QJkGa5PsSIC4iFOVih1X.jpg" alt width="2902" height="1500" referrerpolicy="no-referrer"></p>
<p>6）平台推送</p>
<p>平台用来触达企业的信息，一般有产品更新动态，学习培训，客服，广告推送，活动消息（这个一般比较常出现在平台类的b端产品中）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/FRBl2c7Xys74n0Eir8m0.jpg" alt width="2902" height="1500" referrerpolicy="no-referrer"></p>
<p>7）卡片式数据图表</p>
<p>卡片式数据图表可以拆分成图表+辅助两种组成部分。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/bQSKox99aYdNDH0iqAnA.jpg" alt width="2902" height="1500" referrerpolicy="no-referrer"></p>
<p><strong>图表：</strong></p>
<p>B端设计师需要准确通过图表来表达出用户需要的维度信息。</p>
<p>折线图：</p>
<p>随时间（连续内容）而变化的连续数据，适合表现趋势。Y 轴刻度值选择要合理，以数据波动要最大化的显示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/uEB0DalQYkvT0CC3kxbW.jpg" alt width="2902" height="1372" referrerpolicy="no-referrer"></p>
<p>面积图：</p>
<p>面积图和折线图比较类似，针对只有单个数据类型有面积区域的表达效果比折线图好。数据类型尽量不要超过2个，有2个数据类型时，注意调整面积区域的透明度以及色系保持统一。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/gaVTYfxwET6u4VRCpQZm.jpg" alt width="2902" height="1370" referrerpolicy="no-referrer"></p>
<p>柱状图：</p>
<p>通常用来统计累积叠加数据，数据之间能够非常清晰直观对比。</p>
<p>柱状图的单位宽度不要是固定值，单位宽度之间间距在不同分辨率屏幕下的对比要合理。不用大圆角元素，不够严谨，太活泼；最多使用两种颜色，一种默认，一种hover或tap，保持界面统一性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/MMEGRJb4AN3qMUCcAOGn.jpg" alt width="2902" height="1374" referrerpolicy="no-referrer"></p>
<p>扇形图：</p>
<p>有共同的上一级层级作为统计总合，数据之间平级且有占比；数据必须是正整数，至少两个以上数据，且用不同颜色表示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/bFfXsqwHzqBKAN4AQJ5M.jpg" alt width="2902" height="1370" referrerpolicy="no-referrer"></p>
<p>环形图：</p>
<p>与扇形图很相似，但是比扇形图更加直观浏览且不被抢视觉；避免过于太细太粗，控制好留白呼吸感。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/qX1sXkGB2Cw63p1RewC2.jpg" alt width="2902" height="1370" referrerpolicy="no-referrer"></p>
<p>以上是常用的图形图表，绝不是全部。</p>
<p>8）辅助元素</p>
<p>卡片型图表的第二部分也就是辅助元素。辅助元素里面还有很多细节元素组成：标题、轴、提示信息、标签、气泡信息、功能（筛选、导出、保存）；当然在实际设计中，会根据场景去修饰删减一些元素，以此来减少冗余信息，帮助用户快速达成目标，在最少的时间内获取更多的信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/nrlysqXkUsxoElFq1aSq.jpg" alt width="2902" height="1856" referrerpolicy="no-referrer"></p>
<p>标题：</p>
<p>标题是区分卡片信息，迅速让用户了解卡片图表的重要元素。通常需要斟酌严谨不重复，简洁概括。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/hROC7T9rcrKW99feVXBE.jpg" alt width="2902" height="1554" referrerpolicy="no-referrer"></p>
<p>轴：</p>
<p>轴上最重要的内容就是单位，将每个数据在同一轴上都是维持同种基准。便于进行数据测量。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/19Q4SNXCUJr1xOiKYAon.jpg" alt width="2902" height="1552" referrerpolicy="no-referrer"></p>
<p><strong>轴的细节：</strong></p>
<p>现在知道了轴由哪几部分构成，那么接着了解细节。</p>
<p>轴线：</p>
<p>轴线细节一般只考虑是否显示，在有网格线的情况下，可以考虑隐藏x/y轴线。通常显示数据的轴作为隐藏，突出视觉重点，减少不必要的线条。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/zRIMPNnQJVdEbAKNcYah.jpg" alt width="2906" height="1414" referrerpolicy="no-referrer"></p>
<p>轴刻度：</p>
<p>轴刻度是轴线上的间距不宜过密，确保信息可读性以及呼吸感，根据 7±2 法则，在可见的卡片内尽量保持这个规则，可以利用抽样显示的手段来优化轴标签重叠的问题，这种一般是在连续性内容上可以使用。</p>
<p>若轴上单位信息确实过多，虽然是连续性内容例如展示30天单位，由于本身卡片信息不是过于最重要层级，设计在相对狭小空间尺寸中，那么建议考虑在轴线上安排滚动条，并将重看单位放置前位。设计特别注意点，将滚动条设计作为辅助元素不宜抢视觉。</p>
<p>网格线：</p>
<p>网格线是用来辅助图表数据直观对比的，增加数据更快速的阅读性。</p>
<p>举个例子：数据展示轴线在左边。那么离左边最近的数据图形可能不需要网格线就能立即对应到相应数字。但是越靠近右边的数据图形就相对比左边的数据图形就比较难一眼识别；因此网格线也担任了刻度尺的功能。</p>
<p>在设计网格线时要注意网格线更多是辅助的角色。表现类型可以选择虚线或是实线，但是要把握好颜色选用不抢视觉重点又能看到。</p>
<p>9）提示信息</p>
<p>以对照的方式来理解可视化对象的项目归类信息，总结图形形状和文本组成内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/uttlixsQYVYqcWKjWfVo.jpg" alt width="2902" height="1414" referrerpolicy="no-referrer"></p>
<p>标签：</p>
<p>在图表中，标签是对当前的一组数据进行的内容标注。根据不同的图表类型选择使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/iu9NqfqotvIbTR0Y93Tu.jpg" alt width="2902" height="1414" referrerpolicy="no-referrer"></p>
<p>气泡信息：</p>
<p>当标签默认不显示，气泡信息一般是鼠标tap或者hover时，显示该位置的数据。在简洁的页面中，也能让用户直观看到信息对应数据结果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/F772I0UcxMc3BeZsf05Q.jpg" alt width="2902" height="1414" referrerpolicy="no-referrer"></p>
<p>功能：</p>
<p>这个模块涉及的内容偏多，在表单页面更常出现，以后有机会可以单独说；一般常用功能如筛选、导出、保存，可以让用户控制和友好的体验。</p>
<h3>2. 确定B端产品的设计风格</h3>
<p>首先tob的产品dashboard说到底还是给使用用户所使用，也就是“人”；所以通常情况下dashboard除了传递出用户想要的数据信息，还要传递服务于人。</p>
<p>此外最重要的是B端设计师需要理解项目背景。例如某个财务应用平台不属于科技未来感，而是突出一种安全，高效，具有客户亲和力的商业产品特性。那么关键词：服务、轻松、高效、亲和、精致。那么一个干净、相对轻量、统一的Dashboard UI界面就提炼出来。</p>
<p>色彩：</p>
<p>常说色彩是一种情绪版，在Dashboard设计中，色彩也是映射关键词的非常重要一个环节。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/03/3cZZdJQSlSOJtDpo5mBz.jpg" alt width="2902" height="1990" referrerpolicy="no-referrer"></p>
<p>字体：</p>
<p>B端产品一般都是以数据为主要信息源，针对一些关键信息指标时，可以采用特殊的数字字体；由于本身数字字体包内存不大，所以也方便调用。例如DIN系列等等</p>
<p>设计稿尺寸：</p>
<p>本篇内容都是针对pc端内容，具体移动端以后有机会会分享。大多数B端设计师都知道以1440×900设计，但是在工作中会以埋点数据了解到事实上真实场景还是以1920×1080的尺寸为多数。</p>
<p>毕竟时代不一样了。以1440做设计主要还是考虑从上下兼容的角度的。B端与C端不同，C端往往照顾大多数的用户群体或是主要消费力群体；但是B端一般不会放弃任何一个用户，哪怕定制化。这个在C端是不太现实的。因此适配对于B端产品来说也是尤为重要。</p>
<h3>3. 设计原则</h3>
<p>上面的内容更多是阐述每个部分的内容，实际工作中设计Dashboard时不一定按照那个顺序进行，因此在此再强调下设计Dashboard的设计顺序以及原则。</p>
<p>要先弄清楚目标用户以及使用场景，确定好关键的大约7个核心指标；将用户整个流程梳理流畅之后，再开始考虑Dashboard设计执行。</p>
<p>同时在设计执行上也要特别注意几个点：</p>
<ul>
<li>突出核心指标（7个左右）</li>
<li>信息层级区分</li>
<li>减少用户选择，尽可能默认给到用户需要的数据维度</li>
<li>界面简洁严谨</li>
<li>避免过多颜色与不统一</li>
<li>数据维度正确图表选择</li>
</ul>
<h3>4. 设计的注意事项以及建议</h3>
<p>1）tob的设计师要了解业务所处的周期在什么样的阶段。在探索期建议dashboard的设计应用于市面上现成的组件进行搭建，以便与研发团队一起为业务助力。更好更快的发展。</p>
<p>2）在tob的dashboard设计中，设计师要特别注意数据表现的落地效果</p>
<p>3）当dashboard只在设计层面改版，并且改版内容过大时，推荐保留旧版入口，提前进行埋点用户以便应对用户对于大版本适应缓解焦虑。如果有新功能或功能调整要及时加入一些引导设计，以便减少用户的学习成本。关于引导设计的内容欢迎参考我的上一篇文章：《B端必看的引导设计（一）》</p>
<p>4）允许用户定制和共享dashboard，虽然不适用于所有的B端产品，如果类似于团队协作中多种角色共用一套的dashboard平台，可以考虑引入这个功能。几组定制模块可以满足于不同角色的用户需求，并且能够增加dashboard的使用率</p>
<p>5）dashboard关键信息数据尽量设计在一屏以内，作为数据可视化，内容快速浏览获知全局，并且完成任务是比较重要的。</p>
<p>6）突出统计数据的变化并对异常情况作出反应</p>
<p>7）数字设置不一定要设置为右对齐，但是单位是金额，那么要将金额设置为右对齐，为了使用用户识别方便，快速比较。</p>
<p>8）设计完Dashboard一定要自查一遍，是否真的符合工作人员的使用场景。有没有理解不准确的地方。</p>
<h2 id="toc-5">五、最后</h2>
<p>为什么b端设计师要懂得Dashboard，在很多b端业务场景中，有个特点，设计师常常会接到大量数据展示要求。</p>
<p>如果设计师对dashboard缺乏认知，就有很大的可能性会造成信息杂乱，并且在Dashboard的界面中充斥着一些无关紧要的指标，这就是失去了Dashboard存在的意义；另一方面在b端产品中，Dashboard往往是以首页的形式出现的,是非常重要的。</p>
<p>因为篇幅关系，如何把这篇文章用到实际需求中，在后续实例操作中还会分享以及很多细节展开。</p>
<p> </p>
<p>本文由 @一九互七 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自pexels，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4421411" data-author="1181444" data-avatar="https://static.woshipm.com/APP_U_202101_20210126141831_9994.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            