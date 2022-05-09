
---
title: '关于 B 端表单设计的一些思考！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hpvk2jz8Gajss0MuNsAr.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 09 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hpvk2jz8Gajss0MuNsAr.jpg'
---

<div>   
<blockquote><p>编辑导语：B端的表单设计，对产品的体验起着至关重要的作用。作为收集信息、开展工作任务、形成产品闭环的关键步骤，表单要怎么设计更好呢？一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5430285" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hpvk2jz8Gajss0MuNsAr.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>表单作为收集信息、开展工作任务、形成产品闭环的关键步骤。在一系列 B 端产品中，有较为高频的应用场景。随着 B 端设计的精细化，表单设计对 B 端产品的体验起到愈发关键作用。</p>
<p>本文从<strong>高效和清晰两个表单设计原则</strong>出发，阐述b端产品的表单优化思路。通过制定设计规范，对复杂的业务场景提供设计决策依据。</p>
<h2 id="toc-1"><strong>一、表单定义</strong></h2>
<p>表单页是一种用于信息添加、录入的页面类型。用来确保用户按照要求录入信息提交给系统使用或引导用户进行应用设置。表单的常见类型 基础表单、分组表单、分步表单。</p>
<h3><strong>1. 基础表单</strong></h3>
<p>是一种较为简单的表单类型，通常只需要少量的信息既可以完成的任务。如登陆注册界面页面等。</p>
<h3><strong>2. 分步表单</strong></h3>
<p>将复杂的填写内容按照线性流程进行组织，并拆解成若干步骤。</p>
<p>好处：可以给予用户明确的任务预期，快速了解填写流程和进度；降低用户的填写负担，减少出错率。</p>
<p><strong>1）常规分步表单</strong></p>
<p>用户需要在每个步骤完成之前点击确认才能进入下一步，更加适用于具有明确线性顺序的填写步骤。</p>
<p>在实际应用中用户未通过第一步的填写和校验，不可以进行后面步骤的操作。也可以理解成如果不具备后面步骤的填写条件，可以在第一步时就选择放弃，这样反而不会被用户反感。但是，如果仅仅是因为填写内容过长，而选择常规分布表单，似乎无意地增加了用户的填写步骤，这时就比较推荐灵活分布表单。</p>
<p><strong>2）灵活分步表单</strong></p>
<p>在给予用户分步选择的同时（给予用户充分预期）。将所有输入字段直接展示出来，用户也可以按照操作需求自定义输入的顺序。</p>
<p>此种方式更像是步骤条和锚点定位的组合，好处是用户不必点击下一步，也不必按照既有的线性顺序，更加灵活完成信息录入。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/BJCnPsXNYTgzseG56jUm.png" alt="关于 B 端表单设计的一些思考！" width="855" height="507" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/PhoajWZ2ezAjzqF7mjpR.png" alt="关于 B 端表单设计的一些思考！" width="850" height="543" referrerpolicy="no-referrer"></p>
<h3><strong>3. 分组表单</strong></h3>
<p>将需要填写复杂的内容归类分组，分组内容具有一定的相似性和可归纳性。和分步骤表单类似可以减轻用户的操作负担，提高操作效率。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/6aUEHhqo4kVa9xI1yErQ.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p><strong>小思考：</strong>这里大家可能会纠结，灵活分步表单和分组表单会比较类似。我的观点是，首先要根据业务场景去选择合适的表单样式，其次这里的“灵活分步表单”可以是对分步表单的升级，也可以是对分组表单的升级，叫什么名称其实不重要，重要的是能否帮助用户高效地完成填写任务。</p>
<h2 id="toc-2"><strong>二、背景</strong></h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/idEwweDR3CqBVaL4zcGB.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p><strong>1）用户侧</strong></p>
<p>在过往的工作中，我们通过对用户调研，并对反馈进行整理。发现用户对表单使用问题集中表现为<strong>使用效率低，填写复杂。</strong></p>
<p><strong>2）设计侧</strong></p>
<p>设计师在设计表单时，对一些设计细节点认知不一致，往往凭借已有的设计经验开展设计工作。需要一个表单设计规范，去引导和规范设计工作。</p>
<h2 id="toc-3"><strong>三、设计策略</strong></h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/JiTG0C9CLkmtJDKWgamQ.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p>我们通过对现状的分析，结合用户调研，确定设计目标为高效、清晰、组件化，并将设计目标拆解为具体的可执行动作。</p>
<h3><strong>策略一：高效 – 提升用户决策效率</strong></h3>
<p>目的：通过合理的信息组织，使用户快速完成表单填写。</p>
<ul>
<li>行动 1. 更少的浏览时间，合理的布局</li>
<li>行动 2. 更短的视觉路径，加强视觉引导</li>
<li>行动 3. 更快的决策路径，规范操作行为</li>
</ul>
<h3><strong>策略二：清晰 – 明确填写目标</strong></h3>
<p>目的：帮助用户理解表单填写项的含义，准确的填写表单，降低出错率。</p>
<ul>
<li>行动 1. 暗示输入长度，减少用户的认知负担</li>
<li>行动 2. 视觉降噪，加强用户感知，建立用户心智</li>
<li>行动 3. 有容错机制，有填写错误的校验提醒</li>
</ul>
<h2 id="toc-4"><strong>四、关键行动</strong></h2>
<h3><strong>策略一：高效 – 提升用户决策效率</strong></h3>
<p><strong>1）更少的浏览时间 – Lable 和 Input 的对齐方式</strong></p>
<p>Lable 和 Input 的对齐方式，推荐选择右对齐和顶对齐的方式。</p>
<p>Matteo Penzo 通过眼动追踪实验的方式，对表单中 Lable 的放置位置进行深入研究。研究发现，对于用户来说，需要有一个从 Lable 到 Input 扫视的时间，来感知之间的联系。其中，左对齐需要 500 毫秒，右对齐需要 240 毫秒，顶对齐需要 50 毫秒。填写速度从快到慢依次是顶对齐、左对齐、右对齐。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/coGo9GtcPdNT4nk1ae0I.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p>为了提升表单在业务场景中使用效率，同时考虑到系统的美观、有序，防止设计者仅凭个人经验选择 Lable 的对齐方式，我们推荐选择顶对齐和右对齐两种方式。</p>
<p>那么我们该如何对左对齐和顶对齐进行选择呢？</p>
<p>最直观的区别是占空间大小和视觉美观。顶对齐视觉相对平衡，所占横向空间最小，缺点是需要较长的屏幕纵向空间。右对齐因为受限 Lable 的宽度不固定，视觉效果较为参差，占横向空间较大，但所占纵向空间较少。</p>
<p>考虑到内部 B 端产品会涉及到大量的表单输入项，为了节约纵向空间提升屏效。我们推荐一个系统优先使用左对齐的方式，同时保留两种对齐方式。并给出如下的选择条件供设计师判断。</p>
<p>顶对齐：</p>
<ul>
<li>当页面横向空间较少，比如在内容较少的弹窗、抽屉、页面分屏、页面</li>
<li>更加聚焦填写内容，要求极高的填写效率</li>
<li>不会因为 Lable 的长度不固定，而引起视觉不平衡，视觉上整齐统一</li>
</ul>
<p>左对齐：</p>
<ul>
<li>当纵向空间较少，填写内容多，需要提高屏效时</li>
<li>表单整体长度较长，需要用户填写项较多</li>
<li>相对顶对齐，可以节约大量的纵向空间，较常用的对齐方式</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/QbIdX2q1uJrDHjETlIDh.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p><strong>2）更短的视觉路径 – 单列和多列</strong></p>
<p>多列布局的格式，对相似的选项进行阅读。视觉路径更长，阅读效率相对更低。</p>
<p>在 B 端业务中推荐运用单列布局的形式，更短的视觉路径，更高的阅读效率。</p>
<p>但是在特定的业务诉求下，用户对屏效的要求比较高，也可以采用多列布局的形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/AOrwp4m19d6rvTXpERdK.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p><strong>3）更快的决策路径 – 按钮的位置</strong></p>
<p>参考 Ant Design ，“我们确定了一个清晰的设计策略来决策按钮区位置：<strong>应将按钮放置于用户浏览路径中，便于被用户发现，并且应尽量靠近其所控制的对象。</strong>在未刻意建立信息层级引导视觉路径时，经典 “F” “Z” 网页浏览模式作为了我们按钮位置放置规则的基础指导。”</p>
<p><strong>F形阅读模式：</strong>用户的视线首先是水平移动的浏览内容区域的顶部，这是F的第一横。接下来用户的视线会沿着屏幕的左侧向下移动，如果找到感兴趣的点，视线会继续向右移动，这是F的第二横。最后用户的视线会继续沿着屏幕垂直向下移动。</p>
<p><strong>Z字形阅读（古腾堡法则）：</strong>用户关注流(通常含鼠标移动)遵循一个 Z 字形模式。视线流从左上到右下，左上角为第一视觉区，右下角为视觉终点区。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Lhg6mxtk1WS7iRnQYfmv.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p>为了提升用户的决策效率，我们对表单按钮的摆放位置进行了统一。当单列布局时，按钮的位置选择跟随表单。当多列布局时，按钮的位置在右下角。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/d06GaxDyZe3g22kladxy.png" alt="关于 B 端表单设计的一些思考！" referrerpolicy="no-referrer"></p>
<h3><strong>策略二 ：清晰 – 明确填写目标</strong></h3>
<p><strong>1）暗示输入长度 – Input 定宽</strong></p>
<p>目前对 Input 的宽度常见的处理方式有定款和自适应两种。常见在实际的业务场景中，大部分 Input 都有理想的输入长度。Input 的宽度应该向用户暗示需要输入字符的长短，给用户明确的填写预期。基于此，我们选择定宽的处理方式。</p>
<p>牛顿说：“如果我看的更远，那是因为我站在巨人的肩上。”</p>
<p>我们不妨站在巨人的肩膀上看问题，根据 Ant Design 的研究，得出5种高频的表单宽度区间。宽度值是 XS – 80~160px、S – 160~280、M – 280~360px、L – 360px~480px、XL – 480~560px。</p>
<p>为了呈现出错落有致的排列效果，倡导组合 Input 和单个 Input 的对齐概率最大化，这样Input的宽度差值可以呈现出一个固定规律，且总结出一种不同宽度尺码的排列公式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/gZ2nt4DPWaYT9Zd9qLRt.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p>我们设定 XS 尺寸可以容纳 7 个中文字段的 input 或 99999.00 的 number input。根据设计规范，此时宽度刚好为 100PX。并且根据公式推算出5种 Input的宽度，以及应用场景。分别是XS=108PX、S=208PX、M=316PX、L=424PX、XL=532PX。</p>
<p><strong>XS：</strong>我们设定支持输入 5～7 个中文字符，7～10 个英文字符， 宽度为 108PX。</p>
<p>适用于：较短文本、短数字、选项、价格、数量。如：课程价格、学员性别、选择时间点等。</p>
<p><strong>S：</strong>支持输入 14～16 中文字符，宽度为 208PX。</p>
<p>适用于：短文本和选项，如：学员姓名、学员电话、学员微信、邮箱、身份证、学员 ID 、课程 ID、日期段选择等。</p>
<p><strong>M：</strong>显示23～25个中文字段，宽度为 316PX。</p>
<p>适用于：常规输入框大小，适用于大部分字段长度。如：课程名称、班级名称、模版名称、日期时间段选择等。</p>
<p><strong>L：</strong>宽度为 424PX。</p>
<p>适用于：较长字段录入，适用于长网址、标签组展示、文件路径、集联选择器等。</p>
<p><strong>XL：</strong>宽度为 532PX。</p>
<p>适用于：超长文本的输入，如：正文、描述、备注、简介等。</p>
<p>小结：我们根据此规范，对真实使用场景做优化，有较为显著的提升效果。在满足填写需求的同时，我们也通过设定的 Input 尺寸，给予用户所输入内容长短的心理预期。与表单自适应规则不同，Input 定宽的处理方式可以降低适配过程中的视觉风险。同时，错落有致的布局，更接近真实的使用场景也符合设计美感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/roeNsHDsABO034o10Eql.png" alt="关于 B 端表单设计的一些思考！" width="853" height="516" referrerpolicy="no-referrer"></p>
<p><strong>2）视觉降噪 – 必填和选填的抉择</strong></p>
<p>大量的必填项小红点会增加用户的认知负荷，产生焦躁的情绪，增加填错的风险。表单中的视觉噪声越少可读性越强。</p>
<p>当必填项过多时，推荐选择非必填提示的形式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/oHBZtGdlXF92nGhvmEv5.png" alt="关于 B 端表单设计的一些思考！" width="847" height="390" referrerpolicy="no-referrer"></p>
<p><strong>3）合理的预期-提示反馈</strong></p>
<p>用户在初次使用表单时，对各种定义、用途、使用条件等概念往往理解不清晰。我们希望用户在填写表单时，给予用户清晰的引导和明确的填写预期。这里我们对输入说明、输入线索、错误提示进行规范。</p>
<p><strong>输入说明</strong>：指在空白文本字段的旁边或下方，放置一个短语或示例，解释输入内容或提示输入要求。</p>
<p>作用：</p>
<ul>
<li>保持 Lable 标签字段简洁</li>
<li>补充说明填写要求，降低填写难度，提高填写的成功率</li>
</ul>
<p><strong>输入线索</strong>：指用示例或说明文本，以占位符的形式，引导、提示用户输入内容。</p>
<p>作用：</p>
<ul>
<li>以较少的占位空间，提示用户，视觉负担较轻</li>
<li>在输入框内，容易引起用户的重视</li>
</ul>
<p><strong>错误提示</strong>：是表单出现输入错误时，为用户展示的一条引人注目的解释性消息。</p>
<p>作用：</p>
<ul>
<li>帮助用户修复他们在输入时遇到的问题</li>
<li>让用户尽可能快速，轻松地完成任务</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/M9GU3g914EozVkWMq8KD.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<h2 id="toc-5"><strong>五、总结</strong></h2>
<p>本文根据用户对于表单的使用痛点，挖掘出用户目标。将用户目标转化为设计目标，找到设计抓手。并将表单设计的思考，总结为规范，引导设计工作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 B 端表单设计的一些思考！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/b74EwKP4kmgWBZ6GYEjn.png" alt="关于 B 端表单设计的一些思考！" width="850" referrerpolicy="no-referrer"></p>
<p>这里对表单设计规范作用的理解，不仅是为一些简单的业务场景，提供设计模版供设计师直接使用。更重要的意义是，<strong>面对复杂和未覆盖的场景，设计规范可以为设计者决策提供设计依据和设计边界。</strong></p>
<p>感谢阅读。</p>
<p> </p>
<p>本文由 @😠 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5429436" data-author="288304" data-avatar="https://static.woshipm.com/WX_U_201707_20170703145548_2327.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            