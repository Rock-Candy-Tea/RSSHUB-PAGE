
---
title: '如何搭建B 端系统帮助体系'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/RTwwzrQlrTumi3UZSMRt.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 11 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/RTwwzrQlrTumi3UZSMRt.jpg'
---

<div>   
<blockquote><p>编辑导语：一些复杂的B端系统，在用户用起来时会比较困难，总能听到用户说学不会，不会用，为了减低用户的使用成本，搭建一个全局的帮助系统是很有必要，本文从三大帮助系统类型出发，进行详细拆解。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5562482 aligncenter" src="https://image.woshipm.com/wp-files/2022/08/RTwwzrQlrTumi3UZSMRt.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>一些复杂的B端产品，因为其特殊的业务属性和复杂度操作使用上门槛不低，总是会听到用户反馈不会用、学不会、记不住。为了降低用户使用成本，保证用户在一个大型业务系统的可用性，引入一个在全局系统层面用户帮助体系对于提升用户体验是非常有必要的。</p>
<p>Jakob Nielsen于1994年提出的十大可用性原则中，其最后一条原则Help and documentation（帮助性指导原则）是搭建B端用户帮助体系的核心准则，在理想情况下，没有帮助文档就可以使用系统是最好的，但在某些情况下（尤其是B端系统），提供一些引导性的帮助其实是必要的。本文从三种 B 端帮助体系的三种类型主动式帮助、被动式帮助、自动式帮助进行详细拆解说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/5RlwyEy8QU2516RUFTul.png" alt width="1440" height="691" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、主动式帮助</h2>
<p>什么是主动式帮助呢？回归到生活的场景中，进入地铁站的方向指示牌，马路上的路标，都是让行人们可以根据指示找到想去的地方；刚刚参加工作，一般都会有前辈带着你学习工作流程，进行教学指导；机场和车站的展示大屏，告诉我们目前车次的检票口和车辆状况，这些都是我们生活中主动帮助的例子。</p>
<p><strong>沿用到互联网产品中也是一样的，同样也是主动帮助向用户提供帮助，让用户尽快熟悉系统。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/qeiZS1EZKcQ2hDrh6LPM.png" alt width="1440" height="1076" referrerpolicy="no-referrer"></p>
<h3>1. 在系统中的使用场景</h3>
<p>对于第一次接触系统或者第一次接触系统中某个模块的新用户，刚开始使用产品的时候，需要快速熟悉并尝试系统中的某一功能，这个时候系统提供一些主动的功能介绍或者操作引导可以让用户快速了解。</p>
<p>下面是一款室内装修设计师画图使用的系统，属于操作复杂的工具类型，对于新用户来说在第一次进入系统主动出现一个弹窗介绍完成渲染出图的步骤，可以让用户快速学习到什么使用这款产品做一个设计效果图，也让用户清楚了解每个步骤之间的先后顺序。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/6GpR1XvoLZZp6ewtkNUx.png" alt width="1440" height="890" referrerpolicy="no-referrer"></p>
<p>对于老用户当系统新上线了功能需要告知哪里更新了，更新了什么内容。花瓣更新了点击头像下拉后展示更多信息的功能，在改版后第一次进入系统，出现了提示引导，引导用户快速点击进行体验，当然也可以选择关闭。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/URhbBqTbX3xVJflgkbQU.png" alt width="1440" height="892" referrerpolicy="no-referrer"></p>
<p>使用主动帮助有 2 个核心场景，「对新用户帮助教学」和「新功能上线后对老用户的提示」； 总结 5 种交互形式：引导页、模态弹窗、向导形式、工具提示、文字提示，需要设计师根据不同的场景，去适配不同的引导方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/m9L1R64C9GxRWkP3N2eq.jpg" alt width="1440" height="919" referrerpolicy="no-referrer"></p>
<h3>2. 引导页</h3>
<p>在用户首次进入产品或者产品中某个独立功能的时候，将产品最核心的功能加入一些品牌基调展示给用户，可以加入一些插画或者视频吸引用户，另外需要注意在文字部分不要长篇大论，提炼最核心的内容传达给用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/urONEFVT5PUfsyos5FZ8.png" alt width="1440" height="621" referrerpolicy="no-referrer"></p>
<h3>3. 模态弹窗</h3>
<p>让用户聚焦当前内容，在用户第一次打开某个特定页面时出现，缺点是用户容易忽略或者无视，直接关掉，引导的效果差一点，所以弹窗教程建议保留二次进入的入口，当用户需要的时候可以顺利找到。应用场景有「版本更新提示」「新功能介绍」「常规通告」。</p>
<p>设计形式上可以在文本的基础上加入图片、插画、动画、视频讲解和实例演示等视觉表现形式，不管用什么形式，其目的都是帮助用户快速理解系统的功能特性。也可以使用一些视觉元素烘托氛围，并在文案上注入情绪化的表达，从而提升用户的关注度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/CRGADvUmx5QlMPBFAhNw.png" alt width="1440" height="1027" referrerpolicy="no-referrer"></p>
<p>承载内容上可以师简单业务逻辑的功能说明或单页面功能，采用让用户一次性进行学习。复杂业务逻辑的功能说明或多页面功能联动，通常会进行分步讲解，通过循序渐进的形式将所有知识点逐渐披露出来，让用户有充裕时间进行信息的接收和理解。</p>
<h3>4. 向导引导</h3>
<p>在用户首次进入相关页面，且无操作时出现。有明确的指向性，提前告知用户具体功能的使用场景，因此它会具体指向界面中的某些特定区域，同时会随着具体操作的具体位置发生变化，让用户实际感知到功能的整个运转逻辑和流程。针对局部功能升级的提示说明，一般与元素绑定关系较强，可让用户直观了解关注点，提升功能触达率。</p>
<p>设计组成元素蒙层（可选）+ 文字 + 插图/GIF（可选）。向导主要围绕某个操作的引导说明，与元素绑定关系较强，核心功能和操作在视觉上突出显示。</p>
<p>为了让用户高效获取信息，一次仅显示一条。如果需要用户聚焦了解功能或说明，不被页面中其他元素干扰使用蒙层，注意蒙层的透明度要比弹窗蒙层浅，向导的蒙层需要用户可以看到元素在页面中的位置。具体使用过程中有三种交互方式随着提示强度由强到弱依次是：「分布引导」「气泡提示」「闪点提示」</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/yO4dYFfo5oPzH8lx8ir8.png" alt width="1440" height="569" referrerpolicy="no-referrer"></p>
<p>分步式引导（重）：常用于页面多个功能升级的引导组。当页面有多个升级点，直接平铺会让页面臃肿不聚焦。通过「下一步」操作，逐步唤出剩余引导。为避免步骤过多导致用户疲劳，建议最多不超过5步。</p>
<p>气泡式（轻）：相对轻量的引导，有足够的提示性但不影响其他功能操作。</p>
<p>闪点提示（弱）：微辅助型提示，常与气泡引导配合使用。在需要关注的地方闪烁，点击闪点后唤出关联气泡提示。不对用户造成视觉干扰，又能引起一定的关注。</p>
<h3 id="M4306">5. 文字提示</h3>
<p>文字提示作为最直观的信息展示，一般会采用直接平铺的展示方式，针对一些功能较多逻辑较为复杂的页面，将对用户有帮助的信息直接放在页面上从而指导用户的行为不失为一种简单粗暴的设计方法。对重点或复杂功能提供直观描述或建议。</p>
<p>带有引导性的文案处理，会促进用户优化填写方案，输入更合适的内容。关于文案设计的详细延展查看<a class="ne-link" href="https://www.zcool.com.cn/work/ZNjA3NzU1ODA=.html" target="_blank" rel="noopener">https://www.zcool.com.cn/work/ZNjA3NzU1ODA=.html</a>这篇文章非常详细的拆解了文案设计原则以及使用场景。具体的使用场景有：「页面功能辅助说明」「占位提示」。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/RWkxEUX0b81QEFLA84Fs.png" alt width="1440" height="570" referrerpolicy="no-referrer"></p>
<h3>6. 工具提示</h3>
<p>工具提示比文字直接展示要更简洁降噪，没有直接进行展示，在用户需要的时候通过悬浮或者点击元素以气泡的形式呼出，Material Design在对工具提示（Tooltip）的官方定义是这样的：“When activated, tooltips display a text label identifying an element, such as a description of its function.”工具提示仅仅起到提示的作用，它会出现在当用户激活某一控件的时候，针对某一特定的元素通过简要的文字来阐述其功能特性。</p>
<p>在设计形式上有短暂性、匹配性、简明性的特点：短暂性指工具提示出现和消失的时机需要恰当和短暂；匹配性指工具提示需要出现在与之关联的元素附近；简明性则是对工具提示承载的文本内容提出了要求，要尽可能具备简短性和描述性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/stQ7rIh1cMNf69OznjSC.png" alt width="1440" height="570" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、被动式帮助</h2>
<p>被动引导映射到我们生活中的场景下可以看作是手机地图导航软件，当你不知道该怎么走或者迷路的时候才会主动去打开地图软件进行导航。</p>
<p>另一个生活中的场景是产品说明书，在使用前或者再遇到不会用的功能的时候才会去查阅说明书，无论是导航软件还是说明书它不会自动把全部内容展示在你眼前，都需要你去进行查找。沿用到互联网产品中是指用户遇到问题的时候系统能够提供一些帮助，去指导用户接下来怎么做。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/Sv8DON4HuBkSy2AYoKDq.png" alt width="1440" height="690" referrerpolicy="no-referrer"></p>
<h3>1. 在系统中的使用场景</h3>
<p>被动式帮助一般会依托于主动式帮助，产品发展的初期阶段，主动式帮助是必须的，当产品发展到一定规模具备一定成熟度后，被动式帮助的引入就可以极大的提高整体产品的使用体验。常用的被动引导有：帮助中心/帮助文档、客服支持、全局常驻性功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/pyRq522mpTBgGq56FjNy.png" alt width="1440" height="660" referrerpolicy="no-referrer"></p>
<h3>2. 全局提示</h3>
<p>重点信息的汇总或提示。此类提示完美融合于页面，醒目且对操作无干扰，用户可根据披露内容判断是否处理。常用的交互形式是全局提示、徽标，向用户传达信息的变化并提供快速触达的能力，无形中提升用户响应效率。</p>
<p>全局提示：不同颜色的提示条。常作为前置提示存在于页面或模块顶部，为用户顺利操作提供指引性帮助。既不打断用户当前操作，又足够明显，一般需手动关闭或事件结束后自行消失。不同颜色属性不同：一般蓝色代表消息通知、绿色代表成功、橙色代表警示、红色代表错误或异常等情况。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/4udFf5hJG0oEP0WGA9rC.png" alt width="1440" height="587" referrerpolicy="no-referrer"></p>
<p>徽标：形态各异的小红点。常出现在图标、按钮右上角的红色圆点、数字或文字，简单且醒目。表示内容更新或有待处理的信息，此类提示符合用户心智，无需教育就能向用户精准传达提示意图。使用时注意无数字与有数字的应用场景。有数字的徽标给用户带来的心理压力会更大，也会更吸引用户注意力，同时需注意数字长度控制。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/uQHfYNd8X4cnVPP7ctr9.png" alt width="1440" height="569" referrerpolicy="no-referrer"></p>
<h3>3. 客服中心</h3>
<p>客服中心是B端产品的服务团队和客户建立联系的平台，目前大部分客服采用智能客服+人工客服的组合，通过智能客服先过滤已经在帮助中心的问题，可以解决 80%以上的共性简单的问题，剩下没有办法通过智能客服解决的问题会转接到人工客服。</p>
<p>在设计上通常悬浮在右下角以入口或者悬浮窗口的形式，可以加入品牌形象IP、情感化来提升存在感，吸引用户关注拉近平台与用户的距离。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/JT2QEgEMsvzSPF4SP1gj.png" alt width="1440" height="581" referrerpolicy="no-referrer"></p>
<h3>4. 帮助中心</h3>
<p>帮助中心是全平台信息文档的汇总，提供一个快捷入口，帮助用户了解他想了解的问题，在帮助文档中需要注意方便用户直接进行搜索。文档内容要针对用户的核心任务，描述要尽量步骤化和流程化，另外由于大部分用户实际上都不喜欢阅读大篇幅文字，如何在文档中直接传达重要的信息也很重要。</p>
<p>在设计上为保证用户高效获取信息，需突出内容本身，不要度装饰。框架设计清晰将页面氛围导航区和内容展示区，让用户通过导航快速定位到想要查找的内容。一般帮助中心会由三部分组成：产品介绍，产品入门和使用，常见问题的汇总。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/hWOiYCTiuRqymxhPeXeB.png" alt width="1440" height="569" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、自助式帮助</h2>
<p>自助式帮助就就像我们去吃自助餐，不用自己买菜、处理食材、烹饪，饭店直接把我们可能会喜欢的食物准备好了，直接来选择自己喜欢的食物就可以了。在系统中也是一样提前预判用户的预期，直接为用户提供建议和帮助，或者直接帮用户自动执行一些任务，减少用户的决策压力，不过前提是需要产品设计师考虑非常周全并配合大量数据支撑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/enOZbClltjkzRnm7QlFv.png" alt width="1440" height="640" referrerpolicy="no-referrer"></p>
<h3>1. 在系统中的使用场景</h3>
<p>针对一些用户操作风险较小且系统能力能够支持的场景，可以直接交付系统来自动完成。一些用户操作风险较大且系统能力也能够勉强支持的场景，可以提供部分选项供用户进行选择，同时提供必要的容错能力。常用的自助式帮助引导有智能推荐、错误校验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/bTtmNngKlaDTL4cdbEqd.png" alt width="1440" height="660" referrerpolicy="no-referrer"></p>
<h3>2. 智能推荐</h3>
<p>系统自动提供内容供用户进行选择，帮助用户做出决策，不过这种设计的前提是平台有足够的数据积累，系统通过字段自动为用户预置内容。</p>
<h3>3. 模版设计</h3>
<p>用户新建每一个内容都需要从头到尾重新填写一遍内容，成本极高，可以把高频的类型变为模版进行选择。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/ncRkSY2IrOQBCtEEtT2m.png" alt width="1440" height="570" referrerpolicy="no-referrer"></p>
<h3>4. 错误校验</h3>
<p>当操作出现输入错误时，为用户展示明确的提示性消息，纠正和引导用户的修改内容。设计的时候需要注意反馈的时机做到及时反馈，将发生了什么，接下来怎么调整告知用户。常见的有以下类型：toast、表单错误校验、模态弹窗、根据不同的场景适配不同的交互方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/mcD9lzEyCeLGQiUrqR1A.png" alt width="1440" height="641" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">最后</h2>
<p>任何的引导都要注意任何事情都是过尤不及，适当的给用户提供帮助当然是好的，但是在用户不需的时候过多的进行引导和帮助反而会适得其反，我们在使用引导和帮助的时候一定要合理的进行判断，避免适得其反。</p>
<p> </p>
<p>本文由@郭大毛毛设计笔记 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5562124" data-author="840352" data-avatar="https://image.woshipm.com/wp-files/2022/03/v3zDRP3JAWhsfvHtGgLU.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            