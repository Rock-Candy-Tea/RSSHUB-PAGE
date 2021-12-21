
---
title: 'B端设计师必读：B端产品响应式设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/PCJWTVDyfbcWPpcnd1wT.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 21 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/PCJWTVDyfbcWPpcnd1wT.jpg'
---

<div>   
<blockquote><p>导读：B端设计可能是下一个风口，目前内卷也很严重，由于B端设计师中很多都不太了解前端的技术，这次给大家分享一下最近学习和整理的网页布局相关的知识，本文会从B端设计师的视角带大家了解各种布局的知识点，让我们设计小伙伴在和开发的沟通中有一定话语权。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5259035 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/PCJWTVDyfbcWPpcnd1wT.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>一文了解布局的相关知识，在与前端开发对接时掌握设计话语权；深度解析B端产品响应式设计的知识点。</p>
<h2 id="toc-1">一、开发岗位种类和入门知识</h2>
<p>开发岗位分成前端工程师和后端工程师。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/0P4iQPcN2QJ09XC3aqPI.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>后端开发工程师主要职责是平台设计、接口设计和功能实现，在日常工作中与我们设计师的交流不太多。</p>
<p>作为UI设计师的我们，在工作中最常打交道的就是前端工程师。前端开发主要工作是将UI设计师的高保真设计稿通过代码转化成可用的前端页面。前端开发又可细分为web前端开发、原生iOS开发和原生安卓开发。前端开发主要是用JS+CSS完成页面的构建。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/yVOOCug3wPpvWc7YEKQP.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>这里简单介绍一下JS、CSS和HTML。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/kEYJtMS7IY5spCDa4Hxx.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>1. HTML</h3>
<p>HTML（HyperText Markup Language）是超文本标记语言。超文本就是超越文本的意思，表示它不仅仅是简单的文本，它比普通的 .txt 文件要高级。这些记号超越了普通文本的标记，它们对普通文本的修饰，构成了一套规则，这套规则就是 HTML。</p>
<p>以盖房子类比，必须定义这个房子有多长、多宽，每一块面积如何规划，例如哪里是卫生间、哪里是饭厅、哪里是卧室。将这些定义好，网页也就有了最基本的样子。</p>
<h3>2. CSS</h3>
<p>CSS（Cascading Style Sheets）是级联样式表。CSS 中的“样式”就是指外观。还以盖房为例，定义好了各个空间，房子也盖起来了，但还要装修，例如给客厅贴壁纸、给卧室铺地板。CSS 就是起装修作用的，要和 HTML —起配合使用。</p>
<h3>3. JavaScript</h3>
<p>JavaScript是一种脚本语言，主要用于前端页面的 DOM 处理。房子已经装修好，贴上了墙纸，铺上了地板，桌子、板凳、沙发都已经摆好，一切都很完美。可是，一个有生活情趣的住户时常要买些新家具，或者把茶几换个位置，这时，移动、添加、减少物件就只能靠 JavaScript 实现。</p>
<h3>4. 前端开发CSS单位</h3>
<p>前端开发人员所使用的CSS单位包含很多种，我们设计师只需要了解所有单位分成两类，绝对单位和相对单位。网页设计中最常使用的单位px像素，就是一种绝对单位。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/wjeTdChIb4lTFk0TQn2n.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p><strong>绝对单位</strong></p>
<p>绝对长度单位是固定的，用任何一个绝对长度表示的长度都将恰好显示为这个尺寸。设置宽度为2px，不管屏幕变大还是变小都始终显示2px。</p>
<p><strong>相对单位</strong></p>
<p>相对长度单位规定相对于另一个长度属性的长度。相对长度单位在不同渲染介质之间缩放表现得更好。</p>
<h2 id="toc-2">二、布局种类介绍</h2>
<h3>1. 固定&静态布局</h3>
<p><strong>概念</strong></p>
<p>页面保持固定的宽度，不会根据浏览器或显示器的宽度大小而变化。开发使用像素这种绝对单位作为单位，页面按照精确像素展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/msZIlaphEIfZYoOwq9iT.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>固定布局属于前20年的技术产物，由于当时的科技水平有限，使用的纯平显示器尺寸类型都较固定，所以当时很多网页都使用的是固定布局。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/G84c5syeyzfOIKqf5Zfw.gif" referrerpolicy="no-referrer"></p>
<p><strong>优点</strong></p>
<p>设计简单，不需要考虑屏幕尺寸的限制，使用一种固定的尺寸进行设计即可。</p>
<p>开发简单，不需要考虑屏幕尺寸的适应问题。</p>
<p><strong>缺点</strong></p>
<p>小屏幕时需要左右滚动才能看到全部内容，大屏幕时两侧留白较多，空间浪费。</p>
<p><strong>代表案例</strong></p>
<p>目前部分网页依然会使用固定布局设计开发，常见于一些新闻门户类网站，这一类网页以大量的图片和文字资讯为主，如：新浪网、中华网</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Llw6fQe45J0cQVwrK4j6.gif" referrerpolicy="no-referrer"></p>
<p><strong>设计建议</strong></p>
<p>固定布局形式适合一些新闻门户类等文字内容很多的网站，设计师在设计过程中可以定义一种适合浏览的页面内容区宽度，通常设置为1200px，内容区域居中两侧空间留白。</p>
<h3>2. 流式布局</h3>
<p><strong>概念</strong></p>
<p>流式布局（Liquid）的特点（也叫”Fluid”) 是页面元素的宽度按照屏幕分辨率进行适配调整，但整体布局不变。网页中主要的划分区域的尺寸使用百分数。</p>
<p>页面中主要的划分区域的尺寸使用百分数（搭配min-*、max-*属性使用），例如，设置页面主体的宽度为80%，min-width为960px。图片也作类似处理（width:100%, max-width一般设定为图片本身的尺寸，防止被拉伸而失真）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/1MPA6YME3CMXXufRL8jv.gif" referrerpolicy="no-referrer"></p>
<p><strong>优点</strong></p>
<p>布局保持不变，内容跟随页面宽度变化去做变化，内容会在大屏和小屏幕之间的宽度变化而变化，能够适应大屏和小屏之间的显示。</p>
<p><strong>缺点</strong></p>
<p>内部字体无法跟随变化大小</p>
<p>如果屏幕尺度跨度太大，那么在相对其原始设计而言过小或过大的屏幕上不能正常显示。</p>
<p><strong>代表案例</strong></p>
<p>阿里云网页版在低于750px分辨率时采用流式布局方式。</p>
<p><strong>设计建议</strong></p>
<p>流式布局在设计中使用频率较少，在设计中需要注意宽度变化后导致的内容高度变化，设计时可以考虑做一种最大宽度的效果和最小宽度的效果。</p>
<h3>3. 自适应布局</h3>
<p><strong>概念</strong></p>
<p>自适应布局是分别为不同的屏幕分辨率定义布局，即创建多个静态布局，每个静态布局对应一个屏幕分辨率范围。改变屏幕分辨率可以切换不同的静态局部（页面元素位置发生改变），但在每个静态布局中，页面元素不随窗口大小的调整发生变化。可以把自适应布局看作是静态布局的一个系列。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Ts2DSHoyq25mrgj7uEVC.gif" referrerpolicy="no-referrer"></p>
<p><strong>优点</strong></p>
<p>在多个不同尺寸设备终端下查看网页内容，并且在小屏幕下也能保证相对好的阅读体验，对于不同的分辨率能够灵活的进行操作应用</p>
<p>通过单一的URL地址收集所有的社交分享链接。你可以为创建更好、更友好的网站而做出积极贡献。</p>
<p><strong>缺点</strong></p>
<p>设计工作量大，需要根据不用的页面设计不同宽度的设计稿</p>
<p>页面存在多个版本，每个版本都必须单独更新。通常，设计师需要针对6种最常见的屏幕宽度进行设计。320、480、760、960、1200和1600dp。而且，这个数字还在不断增长，这使得设计师在现场维护方面的工作变得更加艰辛和耗时。</p>
<p><strong>代表案例</strong></p>
<p>Amazon在自己的页面中使用了部分宽度自适应的方法，与使用自适应网页设计的其他网站类似，亚马逊更加鼓励用户下载其官方APP。据报道，通过采用自适应设计，亚马逊移动端的访问速度比以往的响应式网页设计提高了40%。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/G5sDGXk7gSvmQCI7bDtv.gif" referrerpolicy="no-referrer"></p>
<p><strong>设计建议</strong></p>
<p>对于UI设计师而言，一旦团队确定使用自适应布局开发产品，就需要做多套设计稿尺寸。对于自适应布局而言，就是根据不同的页面宽度加载不同的页面。</p>
<p>常用的设计尺寸使用600, 840, 960, 1280, 1440, 和1600dp作为断点，这里的断点个数和尺寸可以根据实际情况灵活去变化，主要是根据目前终端所在的宽度进行选择，例如产品目标用户使用笔记本的数量多，可以将1366作为断点。</p>
<h3>4. 响应式布局</h3>
<p><strong>概念</strong></p>
<p>随着CSS3出现了媒体查询技术，又出现了响应式设计的概念。响应式设计的目标是确保一个页面在所有终端上（各种尺寸的PC、手机、手表、冰箱的Web浏览器等等）都能显示出令人满意的效果。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Vo9iK3T4CiXLAEngWPI1.gif" referrerpolicy="no-referrer"></p>
<p>对CSS编写者而言，在实现上不拘泥于具体手法，但通常是糅合了流式布局+弹性布局，再搭配媒体查询技术使用。——分别为不同的屏幕分辨率定义布局，同时，在每个布局中，应用流式布局的理念，即页面元素宽度随着窗口调整而自动适配。即：创建多个流体式布局，分别对应一个屏幕分辨率范围。可以把响应式布局看作是流式布局和自适应布局设计理念的融合。</p>
<p><strong>优点</strong></p>
<p>响应式布局设计产品能够给用户带来无缝的体验感，无论使用哪种设备（台式机，移动设备等），访客都将获得相同的无缝体验。即使当它们从一种设备过渡到另一种设备时，也会给人一种熟悉和信任的感觉。</p>
<p>对于B端产品来说，跨终端办公是今后的趋势。那么响应式设计对于B端产品来说尤为重要，实现同一个页面在pc和pad上都能够流畅查看且操作。</p>
<p><strong>缺点</strong></p>
<p>响应式网页设计最大的担忧之一是加载时间。响应性网站会为所有设备加载信息，而不仅仅是访问者正在查看您网站的设备信息。</p>
<p>要匹配足够多的屏幕大小，工作量很大，设计也需要多个版本。</p>
<p><strong>代表案例</strong></p>
<p>苹果官网</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/fgRZEDBLvWtt6R7y6v6Q.gif" referrerpolicy="no-referrer"></p>
<p><strong>设计建议</strong></p>
<p>与自适应一样，对于UI设计师而言，一旦团队确定使用响应式布局开发产品，就需要做多套设计稿尺寸。每套设计稿在不同尺寸下设计元素以及导航要发生相应变化，比如在宽度缩小到750，考虑设备为移动端，内容在设计侧考虑移动端规范，需要遵循移动端的导航与用户习惯。</p>
<p>在实操过程中，我们需要更多分析竞品以及采用响应式布局的其他产品页面，并且能够熟悉掌握各个终端的设计规范。</p>
<h2 id="toc-3">三、网页响应式设计策略</h2>
<p>不同断点间屏幕上的界面相互切换适应的策略有：展现、转变、分割、重排、扩展和移位。</p>
<p>1、展现，小屏幕上隐藏的UI信息在屏幕增大时可以展现出来，如下图所示本来隐藏在手机侧边导航中的菜单项在平板的左侧直接显示出来了。这一点也和以600为分界的策略相呼应，在更大的屏幕上直接显示出两级信息：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/plYDgmijkqVZhAqw12Ou.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>2、转变，界面元素从一个组件变为另一个组件，这一点也说明组件的使用并不是一成不变的，可以根据屏幕的大小选择合适的组件。如下图所示，侧边导航的菜单项可能在大屏上显示为标签；小屏幕上的文字列表项可以在大屏上显示为图片网格列表：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ZVd0RavKwNmidOjHNvM1.png" alt width="1080" height="905" referrerpolicy="no-referrer"></p>
<p>3、分割，分层的信息在一个大的空间里铺开：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/dlykp2ZDTHhBLOvply95.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>4、重排，界面元素可以重新排布以填满新的空间：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/xPR6dDA3SGWWIDjmFqdF.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>5、拓展，界面元素在大屏幕上展开为更大的尺寸：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/qyAYagG1E4qXw8OcTvaf.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>6、移位，界面元素调整到更合适的位置：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/qkLH9kxt3GELN9lwDQU5.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、B端产品的响应式介绍</h2>
<h3>1. 布局</h3>
<p>目前有很多大厂商都出了自己的B端系统，如Arco、element。解读响应式设计，我在这里选择了 AntDesign 的布局相关规范。</p>
<p>Ant design中，主要应用了两种典型的适配布局形式，左右布局和上下布局，响应式规则主要作用在工作区中的内容区域中。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/JPrVpdh7LkYYh9D7W3Aw.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p>在这个区域中，Ant 采用了 24 列栅格（Coloum）、23 列水槽（Gutter）的栅格系统。其中水槽数值是固定的，内容区域减去 23 列间隔后，剩下的部分等分成 24 个格线。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/facQv0Pm9nE5ZgC8QLiC.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<h3>2. 栅格系统</h3>
<p>栅格系统可以让你依靠秩序与逻辑去完成设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/FqQ4Lp4anbCvMspVzlHj.png" alt width="1080" height="600" referrerpolicy="no-referrer"></p>
<p><strong>栅格系统优势：</strong></p>
<p>减少决策成本提高设计理解力：</p>
<p>栅格系统在页面排版布局、尺寸设定方面给了设计者直观的参考，它让页面设计变得有规律，从而减少了设计决策成本；例如发送消息，预订酒店房间或乘车。用户能够连贯的理解并找到找到下一条信息或下一步要采取的步骤。</p>
<p>响应化：</p>
<p>使用产品时，人们通常会在多个设备之间切换，以完成该产品的单个任务。<strong>所以响应式设计不应该是一种奢侈品，而是一种必需品。</strong>这意味着设计师不能再为单个设备的屏幕构建。多设备环境迫使设计人员根据动态网格系统进行思考，而不是固定宽度。使用网格可以跨不同屏幕尺寸的多个设备创建连贯的体验。</p>
<p>加速团队协作设计：</p>
<p>当多位设计师共同设计产品时，一个统一标准就变得尤为重要。<strong>网格系统有助于将界面设计工作分开，因为多位设计师可以在统一的布局下进行不同部分工作，并且无缝集成并保持连贯。</strong></p>
<p>加速开发并保证视觉还原：</p>
<p>大多数设计项目的落地，涉及到设计者和开发者之间的沟通协作。<strong>栅格化提高了页面布局的一致性；</strong>从而提升了整个设计开发流程的效率、并能帮助开发者实现较为理想的设计还原。2.栅格系统应用</p>
<p><strong>列和槽（Columns and Gutters）</strong></p>
<p>栅格系统的基础应用，就是对内容模块分配指定数值的 “列”，比如一个组件的宽包含 3 列、4列、或者 12列。在同一行中，总共包含 24 列，横向的元素按照设计师设计的大小比例平分这24列。</p>
<p><strong>列的数量越多，页面就会被分割的越“碎”，在页面设计时就会越难把控，适用于业务信息量大、信息分组较多、单个盒子内信息体积较小的页面设计。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/McIQXDUb8utQSIJYK8y6.gif" alt width="640" height="360" referrerpolicy="no-referrer"></p>
<p><strong>页面边距（Side Margins）</strong></p>
<p>在响应式设计中，你选择了一个页面边距之后，缩小页面宽度时页面还是会有你设置的最小页面边距，直到到达下一个响应点（breakpoint）。当你增大页面宽度时，页面就有更多的页面边距，直到页面宽度到达下一个响应点（breakpoint）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/1UVmy4k9wgDoQuIrXsS7.png" alt width="647" height="488" referrerpolicy="no-referrer"></p>
<p><strong>模块</strong></p>
<p>模块就是页面中的设计区域，可以是一段文字，一张图片，或是其他更加丰富的元素。背景元素并不能算作是设计模块，所以并不需要遵循栅格系统。模块的定义是很灵活的，它可以是个小的单位或是元素，也可以是一个元素丰富的区块。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/gJz9P5uMhnSWUdrAToma.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/BRTWhxCsU4nmX3PfjqHo.gif" alt width="640" height="360" referrerpolicy="no-referrer"></p>
<p>创建好画布以后，在需要响应式的区域创建出对应尺寸的24栅格系统，一个24栅格系统可以根据业务需要被2等分、3等分、4等分、6等分、12等分，然后在该栅格体系内定义宽高、间距即可，Ant 的框架会自动帮助我们完成响应的功能，具体采用哪种比例的组合需要我们根据自己业务需求来定。</p>
<h3>3. 响应式设计方法</h3>
<p><strong>第1步：确定列的数量</strong></p>
<p>根据页面内容复杂程度确定列的数量。</p>
<p>根据前端框架确定列的数量，例如ant使用24列栅格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/gft8jsej7pfjPnvdnrke.png" alt width="1324" height="469" referrerpolicy="no-referrer"></p>
<p><strong>第2步：定义水槽和边距</strong></p>
<p>确定页面边距，通过边距算出水槽的宽度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/omQbA55orcsIBjgzWYfQ.gif" alt width="640" height="360" referrerpolicy="no-referrer"></p>
<p><strong>第3步：设计工具布局设置</strong></p>
<p>figma或者sketch都有设置布局的功能，这里以sketch为例展开：</p>
<p>利用 sketch 的布局设置功能，即可快速搭建出网格系统的参考布局，在平时做设计的过程中，可以经常使用 Ctrl+L 快捷键切换布局的显示，提高设计效率。</p>
<p><strong>Total Width：</strong></p>
<p>就是内容区域（Container）的值</p>
<p><strong>Offset：</strong></p>
<p>表示栅格的偏移量，我们只要设定完成以后按Center按钮即可，会自动居中；</p>
<p><strong>Number of Columns：</strong></p>
<p>就是栅格数</p>
<p><strong>Gutter on outside：</strong></p>
<p>是非常重要的设置，勾选以后才能跟前端的栅格算法匹配。</p>
<p><strong>Gutter Width：</strong></p>
<p>就是栅格之间的间距</p>
<p><strong>Columns Width：</strong></p>
<p>就是栅格的宽度</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/RYI8EauUdP9XmEcpn6jr.png" alt width="676" height="552" referrerpolicy="no-referrer"></p>
<p><strong>第4步：设置断点</strong></p>
<p>断点是自定义屏幕的宽度范围，在不同范围下确定不同的布局规则，这是为了适应不同的设备和屏幕尺寸。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/bslS1YrsTovWM7u5LWrc.png" alt width="1080" height="2467" referrerpolicy="no-referrer"></p>
<p>先从 Break Point断点的个数来看，Sales Force 的断点个数最少，只有3个。个人认为的原因是 Sales Force 的用户群体使用的都是PC端，因为大多为后台操作，所以 Break Point 较少，而且从开发成本来看，断点越多，规则越复杂，意味着研发成本越高。而其他三家都有自己的硬件设备，为了设计能更好的服务于全端的设备，所以断点个数较多。</p>
<p>根据设计稿常见尺寸，我们可以得出下面结论：</p>
<ul>
<li>0-599px 大致为手机适配</li>
<li>600-1023 大致为平板适配</li>
<li>1024-1439 大致为笔记本电脑</li>
<li>适配1440+ 大尺寸适配</li>
</ul>
<p>经过多年实践，以这几种尺寸作为断点，是不会有错的。</p>
<p> </p>
<p>本文由 @晨屹 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5238873" data-author="265625" data-avatar="http://image.woshipm.com/wp-files/2021/10/QC7ndE6f9pjapW9Y0aWy.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            