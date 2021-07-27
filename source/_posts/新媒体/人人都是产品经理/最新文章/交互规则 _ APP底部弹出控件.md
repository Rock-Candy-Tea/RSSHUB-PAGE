
---
title: '交互规则 _ APP底部弹出控件'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qhfpb4hICNiluRkaHhjT.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 27 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qhfpb4hICNiluRkaHhjT.jpg'
---

<div>   
<blockquote><p>编辑导语：在日常生活中，我们经常会使用到手机。每当我们打开一个APP时，总能够发现在APP底部弹出的控件，你是否有注意到它们之间有何区别？怎样的弹出控件设计才是令人喜欢的？作者分享了一些关于APP底部弹出控件的交互规则，我们一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4944213 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qhfpb4hICNiluRkaHhjT.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>APP中从底部弹出的控件，因其自定义用法十分灵活，已经逐渐成为控件库中重要的基础建设。不过，面对市场上各式各样的用法，我们应该编写一套什么样的规则，能够更好的驾驭这些控件，让它们的体验更一致、使用更清晰呢？本文和大家分享我的思考过程。</p>
<h2 id="toc-1">一、常见的“自定义”用法</h2>
<p>现在“底部弹出控件”的自定义用法很丰富，并且一些新用法和其使用场景有着很高的契合度。</p>
<p>基于大体量APP呈现出的“界面元素、功能过饱和”现状，我们的设计并没有一味拘泥于iOS/安卓的使用建议，而是充分发挥了“底部弹出控件”的灵活性。</p>
<p>不过“灵活”的另一面，是给控件用法的统一带来了难度。以下归类主要覆盖了“自定义”用法使用率较高的5种情形。</p>
<h3>1. 收纳</h3>
<p>收纳是最常见的场景，因为涵盖的情况难以用一种归类完全承载，所以我分别按照使用目的、交互形式和生效机制进行了归类。</p>
<p>下面配合一些线上例子，来呈现这些用法（“动作菜单”与“数据项菜单”会在后文中详述，此处略过）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/BK2Bx8hXBEDgdfJl46iF.png" alt width="1504" height="600" referrerpolicy="no-referrer"></p>
<p><strong>（1）收纳信息</strong></p>
<p>这个用法很好理解，但是同时我们也发现，底部面板的退出方式，3家产品已经存在3种不同的规则：点击“完成”、左侧点击“关闭”、右侧点击“关闭”。关于如何保持一致的问题，在后面“模态的退出方式”中会展开详述。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZhOuZnCB7Kdoo6Uz3iz2.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>（2）收纳服务</strong></p>
<p>该用法最早源于对iOS中“Activiy View”的自定义，现在根据各业务不同诉求，运用的越来越成熟。乍看上去样式五花八门，本质上都是对当前场景所提供服务的一种收纳。</p>
<p>用法并不复杂，做好主次层级的划分、保证每个功能的合理去向，以及兼顾全端的一致性即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qPQE27VAFvwT1tSXXMk1.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: left;"><strong>（3）常驻于底部、由界面元素触发</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/oNEUcXYNUTSSW6UG9nmb.png" alt width="776" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: left;"><strong>（4）即时生效、非即时生效</strong></p>
<p style="text-align: left;">关于生效机制，刚好可以在飞书中分别找到对应的案例，这样我们可以更直观理解它们的不同之处。</p>
<p style="text-align: left;"><strong>即时生效：进行操作→面板收起→操作生效</strong></p>
<p style="text-align: left;">有一种情况面板不会自动收起，即面板中的操作选项较多、且每个选项对应不同的界面效果，如果次次点击都收起面板反而效率很低。这种情况下，可以让用户自行决定关闭面板的时机。</p>
<p style="text-align: left;"><strong>非即时生效：所有操作需要点击“确认”/“完成”才可生效</strong></p>
<ul>
<li>操作单一：常用于筛选、提交申请、确认支付等场景。</li>
<li>操作多元：常用于编辑、设置等场景，操作类型除了数据的勾选和输入，一般还会涉及添加、删除、排序等。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/hwbOf89nJuAT81jNydpq.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h3>2. 响应、询问</h3>
<p><strong>（1）即时响应</strong></p>
<p>移动设备中的即时型反馈，一般使用 Toast 和 Snackbar 就够用了。不过有些情况，需要底部面板来帮忙：在图表/工具类场景中，存在这样一种交互形式，即随着手指完成操作、离开屏幕，会触发</p>
<p>某个控件的弹出。比如案例中的k线图场景（下图左一），手指完成2个位置的点击后，底部面板随即弹出。用户可以边对照k线图、边查看面板中的数据，操作完成后点击关闭退出“区间统计”。</p>
<p><strong>（2）主动询问</strong></p>
<p>现在我们都知道，在一个任务完成的节点提供反馈是必要的。不过还可以再进一步，如果该反馈节点存在一些关联性很强的功能，我们可以通过“底部弹出控件”进行自然的衔接和有效的聚合。</p>
<p><strong>衔接：</strong></p>
<p>例①：在“高德地图”完成一个订单的支付后，APP会立即弹出面板，以主动询问的方式，收集某个问题的用户反馈。由于该设计有助于提升乘客的打车体验，通常参与度比较高（下图左二）。</p>
<p>例②：在“豆瓣”收藏内容成功后，底部面板除了提供反馈，以主动询问的方式，提醒用户填写本次收藏的理由、以免遗忘。该设计对于帮助用户管理杂乱的收藏，是很有效的（下图左三）。</p>
<p><strong>聚合：</strong></p>
<p>例如在“天天基金”进行截屏操作时，会触发APP立即弹出面板，询问用户当前是想对截屏内容进行分享、还是意见反馈、或带着截图发帖至社区。这几项功能的关联与聚合，都达到了快捷、有效的目的（下图左四）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/UmXV06iEgctotmKLw0YG.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h3>3. 连续</h3>
<p>使用“底部弹出控件”来承载一系列连续的动作、或者一个流程简单的小任务，已逐渐形成趋势。其最大的好处就是保证了步骤间的连续性。</p>
<p>试想在一个流程中，一会儿弹Alert、一会儿打开新页面、一会儿左/右呼出抽屉，和全部使用“底部弹出控件”的顺滑体验相比，在“连续性”上相差还是比较大的。</p>
<p>连续，意味着开始出现多个层级。我在这里试着给出2个使用判断上的建议，供大家讨论、参考。</p>
<p><strong>判断1：在层级较深的页面，承载多项任务</strong></p>
<p>像微信这样同时兼顾“工具”与“内容”的超级App，用户经常会被带到层级较深的页面、临时跳出当前场景完成一些任务。比如在支付场景去“添加新银行卡”、在阅读场景去“分享到朋友圈”、在发布场景“选择可见范围”等。</p>
<p>微信中大量使用“底部弹出控件”，通过一致、连续的交互，来降低用户“离开当下”的感受，让用户感觉他仍在此处、掌控着一切。信息结构的复杂并没有消失，它只是被设计者巧妙的“分解”了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/zpo9aWPrsInGqF2EIOth.png" alt width="652" height="341" referrerpolicy="no-referrer"></p>
<p>如上图中的“设置备注和标签”功能，微信在“新建标签”的控件上做了独到的改造，帮助用户专注眼前任务，提高效率。相比较常见的Alert/Dialog（上图右一），使用“底部弹出控件”的连续性会好一些。</p>
<p><strong>判断2：在沉浸型场景，承载多个功能</strong></p>
<p>每类产品的沉浸场景不同，但是他们对功能呼出方式的诉求是一致的，即尽量不离开当下、尽量连续。无论是股票产品的行情场景（下图左侧）还是音乐产品的播放场景（下图右侧），除了必要的跳转，都会见到大量“底部弹出控件”的使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/QzJ7eJkviKPrb9DeH6r2.png" alt width="770" height="473" referrerpolicy="no-referrer"></p>
<p>内容社交型产品Instagram也是如此，内容流和个人主页是它的主要分发阵地，使用“底部弹出控件”来安置这些常规功能，满足了“不离开当下、继续浏览”的需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/CK0KIeyWOaR9ab0sQqEF.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h3>4. 并行</h3>
<p>如果我们把移动设备的屏幕比作一个有限的容器、把屏幕上流动的内容比作一张纸的话，那么就会出现：</p>
<p>这张纸的长度有时会很长，而同时浏览纸上内容的人又想边浏览、边参与讨论或者看点其他内容。如果空间允许，采用左右结构当然最为理想。</p>
<p>但是移动设备，我们只能在Y轴上做文章。如果将这张纸的尾部内容裁剪下来，制作出<strong>“第二张纸”</strong>，并把它固定在容器底部、给它加上可以滑动的轨道，是不是问题就迎刃而解了？</p>
<p>在“豆瓣”的案例中（下图左侧），使用从底部拖出的面板来承载互动相关的需求，就好像容器中的“第二张纸”，在y轴上创造出比拟z轴的空间。券商类产品“长桥”（下图右侧）也尝试将自选股的最新动态放入“第二张纸”中，与自选股列表紧密的粘合在一起。</p>
<p>两张纸理论上都可以承载无限的内容，如此便完美的实现了在一个场景中、两个需求的“并行”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/hmVCFmia0UWp0rcIf7wb.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h3>5. 定制</h3>
<p>除了以上几种存在共性的“自定义”，还有一些被各业务定制出来的用法。比如下图中的股票快捷下单、外卖点餐、编辑图片、发送弹幕等，各业务场景下的“自定义”都需要具体问题具体分析。确保交互的合理、体验感受的顺畅即可，本文在此不做展开。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/hTlk26pNNJekDx0oXFAT.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、从“模棱两可”到“使用清晰”</h2>
<p>刚刚我们先解决了“什么时候用底部弹出控件”以及“什么场景使用哪类用法”的问题。不过观察下来发现，再往下落到一些具体细节时，仍然存在很多“模糊”地带。</p>
<h3>1. 动作菜单与数据项菜单</h3>
<p>动作菜单对应到原生控件，就是iOS中的Action Sheet和安卓中的Dropdown Menu。顾名思义，动作菜单，承载的选项应该是一个操作、或者通过点击菜单链至一个新的去向。比如微信iOS中Action Sheet的一些使用案例。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/grSwFUUEoKPjewW63iK0.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<p id="uaae9e2ad" class="ne-p"><span class="ne-text">所以，如果你要收纳的菜单不是一个操作或者一个去向，那么他们大概率是用作筛选的数据项菜单。数据少的时候推荐使用下拉菜单，好处是离触发区近且多端体验一致；数据多的时候可以采用上文提到的自定义底部面板或者右侧弹出抽屉。</span></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/gMQHWcNIjpFqK3fnAkm9.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h3>2.全屏模态视图、模态面板、向右进入新页面</h3>
<p>“全屏模态视图”（Full Screen / Full-screen Dialog）和“向右进入新页面”在层级的叠加上，成本是一样的。不过“全屏模态视图”除了可以向左回退，在微信中也培养出了可以一直向下关闭页面、退出层级的认知。</p>
<p>二者根本的区别在于，“全屏模态视图”可以一键退出该任务流程，而“向右进入新页面”因为属于“层级导航”，想退出只能原路返回、一层层的回到起点。</p>
<p>所以我们会看到，在层级较深的位置，不会使用“向右进入新页面”再展开一个多步骤的任务，它更多用于进一步呈现详细、完整的信息。</p>
<p>苹果在iOS13将“模态面板”（Modal Sheets）调整为卡片形式后，至此没有再更新其用法。除了苹果自己的系统在广泛使用这个控件，只有“印象笔记”等个别产品能看到它的集中使用。我认为原因在于，脱离了苹果系统的使用场景，“模态面板”在其他App中表现出使用不清晰、通用性不好的问题，微信也干脆没用，依靠“全屏模态视图”完成了大部分多层级的场景。</p>
<p>但是全靠“全屏模态视图”去堆叠层级，难免会在一些场景给用户带来迷失感。所以更建议大家将“全屏模态视图”与上文提到的“自定义底部面板”结合使用，先保证全端交互的一致性。后续iOS如有通用性更好的用法，再考虑将其加入控件库。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DzB3onNQzxkXCgcNryrz.png" alt width="984" height="405" referrerpolicy="no-referrer"></p>
<h3>3. 模态的退出方式</h3>
<p>① 点击“遮罩层”退出。除了“全屏模态视图”，剩余底部弹出控件都可支持。</p>
<p>② 点击“关闭”退出。常用于收纳信息。</p>
<p>③ 既可点击“关闭”、又可点击“确定”退出。一般用于“确定”需要被激活的情况，所以同时提供“关闭”的方式。</p>
<p>④ 点击按钮退出模态。一般有以下3种情况：</p>
<ul>
<li>a.“取消”：常用于Action Sheet、Activity View</li>
<li>b.“确定”或“完成”：常用于单一操作 / 收纳信息的底部面板</li>
<li>c.“取消”+“确定/完成/发送/提交/…”：常用于Full Screen、非即时生效的底部面板</li>
</ul>
<p>以上退出方式，无论遵循哪一套规则，只要使用清晰合理即可。最重要的是保证产品全局上的高度一致。</p>
<h3>4. 何时使用拖动手柄</h3>
<p>其实拖动手柄收起“底部弹出控件”，也是一种退出模态的方式。不过大家可以通过上文诸多案例发现，“拖动手柄”的使用不仅在各家产品中规则不一样、在一些产品内部也存在着不一致的地方。</p>
<p>豆瓣、钉钉（见下图）常驻于底部、通过手柄拖入拖出的用法，是现在使用较为明确、清晰的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/WuheJDlTLuBlfK0dDAJe.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<p>豆瓣在最近版本中已经将不必要的“拖动手柄”去掉了，只在上图示意的场景中保留使用。我认为这种变化让一个控件的使用边界，更加清晰了。<strong>在必要场景合理使用、且不滥用，是控件规则存在的价值之一。</strong></p>
<p>不过，有一些跑在前面的产品，正在用“拖动”关闭面板、逐渐代替“点击按钮”关闭面板。</p>
<p>所以我们在Ins和微牛中看到了处处带有“拖动手柄”、而不再使用按钮的设计。这些走在趋势前沿的产品，一般设计团队话语权较高、或者产品刚刚完成从0到1，有着较好的实验土壤。</p>
<p>如果你所在产品不具备这样的条件，建议还是等趋势应用的成熟了，再判断是否跟随。</p>
<h3>5. 自定义底部面板中的多层级回退，关闭还是返回</h3>
<p>当前任务中所承载的操作较多元，且有些操作又需要新的去向，如搜索、新建等，使用层层“关闭”的逻辑完成回退（下图左侧），体验较为一气呵成。</p>
<p>如果当前任务在第一层级即可完成主要操作，第二层级仅承载次要信息，使用“返回”逻辑即可（下图右侧）。我们每天都在用的“支付宝-密码支付-选择银行卡”功能，就是一个比较经典的案例。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/wsEulUOnU0DSR72uzTVp.png" alt width="720" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、使用规则的编写思路</h2>
<p>以上是我在规则草稿阶段，进行观察、思考和抽象的过程。现在我们有了“自定义”的主要用法，一些“模棱两可”的问题也有了清晰的结论。接下来我们关注三件事：</p>
<h3>1. 先平铺再合并</h3>
<p>对于处在稳定迭代周期中的产品，我们先通过走查的方式，将线上的案例一个个收集起来。在有了粗略的归类整理后，还要继续审视当前的控件使用类型，是否还有“瘦身”的空间。</p>
<p>因为文档的使用者通常是产品、UI、研发、测试等协作方，如何帮助他们快速、准确的定位到某个控件的使用，是最重要的。</p>
<p>如果有两种用法，你发现它们的使用边界比较模糊，证明其中一个是可以被合并、或者直接删掉的。分类越集中，越有利于保持一致。</p>
<h3>2. 分类框架因地制宜</h3>
<p>“底部弹出控件”同时包含了原生和自定义的用法，且落到不同产品中，自定义的归类方式会存在较大差异。这里以美港股券商为例，以下是我的分类框架。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/TeKjdv9slmS6WBMdF3BT.png" alt width="806" height="442" referrerpolicy="no-referrer"></p>
<p>“基于原生”，指的是直接调取系统原生控件，在交互上没有进行自定义改造的基础用法。它们可能在视觉上有着区别于原生风格的再设计，但是底层仍可清晰对应至某个原生控件。</p>
<p>“自定义”用法在上文中已详细阐述，以美港股券商为例，目前还没有遇到“并行”的用法，未来如果出现了对应需求，再补充至文档中即可。</p>
<p>“关联功能”相当于这份文档的落地指引。在完成以上全部用法的编写后，以筛选、货币兑换、日期选择为具体案例，来说明这份文档如何使用、以及使用后可以带来哪些收益。</p>
<p>同时还可以为这些功能的体验换新，提前做好方案上的储备。</p>
<h3>3. 保持一致</h3>
<p>保持一致的重要性无需赘述，它是保证一个产品体验质量的基石。尤其在编写控件规则的过程中，每一步都需要反复确认“一致性”的问题，直到没必要的分叉一个个消失，全局的整体性才会逐渐浮现。</p>
<h2 id="toc-4">四、Q&A</h2>
<p><strong>1.“操作确认”类对话框需要从Alert整体调整为底部弹出控件吗？</strong></p>
<p>从体验差别上来说，必要性不大。我目前调研到的产品，应该只有豆瓣、脉脉做了全局上的规划和调整。而这样的改动，落地成本通常较高，投入产出比较低，不建议盲目推进。</p>
<p><strong>2. 如何让这类横向规则文档，被真正的使用起来，而不是束之高阁？</strong></p>
<p>非0-1的产品，想依照文档对老旧设施进行重建、改造，需要等待大改版这样的顺风车时机。除此之外，我们还可以从两个角度入手，小步推进。</p>
<p>一是在文档确认、发布后接到的需求，从设计内部的输出环节开始，使用最新的规则设计需求；</p>
<p>二是在接到已上线功能的需求，发现其涉及到文档中内容，可尝试与研发、产品、测试同学进行沟通，如排期、风险可控，可借此机会解决一个单点问题。</p>
<p> </p>
<p>本文由 @cony的小书包 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4938463" data-author="1125063" data-avatar="https://static.qidianla.com/woshipm_def_head_3.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            