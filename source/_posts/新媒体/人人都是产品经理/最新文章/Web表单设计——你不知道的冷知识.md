
---
title: 'Web表单设计——你不知道的冷知识'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/I1d6F9DkTonlFdgatR1A.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 28 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/I1d6F9DkTonlFdgatR1A.jpg'
---

<div>   
<blockquote><p>编辑导语：在产品设计中，细节之处有时隐含着许多值得思考的地方。Web表单界面设计便是如此，比如标签设计中，哪种标签对齐方式更好？标签末尾又是否需要加冒号……设计师应该如何解决这些细碎的问题？本篇文章里，作者就Web表单设计中的“冷知识”进行了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5193596 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/I1d6F9DkTonlFdgatR1A.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>当我们设计Web表单时，往往用最直觉的设计经验本能驱动我们去解决一些看似在界面设计中最简单的问题，但每每到细微之处，又会有无数疑问从细节中冒出来给我们的设计造成困扰。</p>
<p>例如：在表单界面Label（标签） 和 Input（输入框） 上下还是左右排列合理、Label要不要加冒号、输入框到底多宽合适等等……</p>
<p>以上这类问题看起来并不影响用户完成任务，很久以来也少有人关心这些细微之处会不会对用户有什么影响。</p>
<p>以至于，我表达想写一篇探究这些细节的文章时，同事会偷笑说：你都开始研究标签末尾要不要加冒号了吗……太冷了——真是个冷知识！</p>
<p>确实如此，这些偏门、细碎的内容，鲜少有人会去留意和思考。因此我在写下这些分享内容时期望可以达到目标是：“冷知识虽然冷，但有用”。用我了解的这些表单设计冷知识：启发你的冷思维、引出你的热思考。</p>
<p>话不闲聊，我们开始讨论第一个问题。</p>
<h2 id="toc-1">一、标签末尾要加冒号吗</h2>
<p>有个表单细节不知道你有没有想过，标签末尾是否要加冒号？</p>
<p>这个问题在我前团队发生过激烈争论，有同事说：“不要加，占用间距，而且没人会留意它……”,也有人说：“要加，从含义上讲，冒号的作用就是提示上下文或总结上下文的停顿。加上之后能更好表示标签与输入域的关联…….”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/nOv2EVHKBJAokuaXGvFr.png" alt="Web表单设计——你不知道的冷知识" width="661" height="268" referrerpolicy="no-referrer"></p>
<p>听起来好像都有些道理，那到底谁更对呢！</p>
<p>首先，我们追溯一下 Web 发展史，早期可访问性核对清单中通常坚持要标签带冒号，因为屏幕阅读器一度必须依赖各种技巧才能理解标记不明的表单。</p>
<p>而随着技术发展，Web表单使用“label”标签（tag）可以做正确的标记，那么屏幕阅读器就能通过标记（markup）把标签（label）和相应的字段对应起来则无需再借助冒号。</p>
<p>不过在客户端又有些意外！曾经 Windows Vista 指南中明确要求使用冒号， Mac Aqua 也有此要求但规则会稍灵活一些。</p>
<p>这种情况是因为某些情况下屏幕阅读器在桌面环境与可阅读源代码的网页标记相比会遇到一些困难，桌面环境不会直接显示代码。也是这个历史原因，造成 Vista 和 Aqua 各自都有大量其标签包含冒号的历史表单。因为实在没有必要把它们全部改掉，直到今天客户端的表单依旧延续这一规则。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/lWDvyyIyjGgFugEOLwRp.png" alt="Web表单设计——你不知道的冷知识" width="662" height="422" referrerpolicy="no-referrer"></p>
<p>通过Web发展史我们明白表单标签带冒号的产生是为了解决早期屏幕阅读器的识别，如今的屏幕阅读器技术已转变为识别标签的底层代码，无需借助这种形式了。所以从这点来看要求标签带冒号已经站不住脚了。</p>
<p>那从情感角度分析标签带冒号的是否对用户体验有影响呢？</p>
<p>回到最开始，我和同事们的争论……</p>
<p><strong>先简单说下答案，无任何影响！</strong></p>
<p>在《Web表单设计·创建高可用性的网页表单》中，作者（卡罗琳·贾雷特）曾经做过大量的表单测试，最终证明从未有一名用户谈论冒号是否出现，即使是有些在其他环境中很介意标点符号的人似乎在线上表单中也未曾注意到。</p>
<p>从以上两个角度不难发现，无论是从技术发展还是情感体验，都证明可不必要求表单带冒号；因为可用性访问清单不再有这样的要求，用户研究也证明几乎没有人会留意表单冒号是否出现。</p>
<p>这样的结论，看似表单带冒号是失败了……但这并不妨碍它作为一种习惯或传统延续至今，无论在客户端还是Web设计系统中仍然常见。例如：苹果电脑的Mac系统，国内阿里的Ant Design Web设计系统。</p>
<p><strong>因此，得到以下几点建议：</strong></p>
<ul>
<li><strong>如果你希望自己的网页表单与流行的桌面环境保持一致，请使用冒号。</strong></li>
<li><strong>如果你已有大量使用冒号的表单，请保持继续使用下去。</strong></li>
<li><strong>如果你在建立一个新的系统，你也可以索性抛硬币决定，不过要严格遵循一种方法。</strong></li>
</ul>
<h2 id="toc-2">二、哪种标签对齐方式更好</h2>
<p>在表单中标签与表单域的对齐方式，如果你的团队已有明确的规范和使用场景，你只要拿来主义即可。可如果某天由你主导定义一个新的表单规范时，不知道你会不会重新考虑哪种标签对齐方式更好，怎样区分使用场景！</p>
<p>通过科学实验发现，无论是在眼动仪的热图，还是在许多可用性测试的观察结果中，用户在填写网页表单时视线主要集中在输入框的左侧。他们的视线几乎不会落到输入框的右侧，甚至都不会瞟上一眼。</p>
<p>以此为基础，我们在网页表单设计中有3种最常见的标签对齐方式：顶对齐标签、右对齐标签和左对齐标签。你可能会说还有混合对齐标签、内联标签、图标标签等，这些确实存在但并不是最核心的几种对齐方式，它们基本是在这3种形式上变化，不脱离本质。</p>
<p>下面我们逐个分析一下。</p>
<h3>1. 顶对齐标签</h3>
<p>马泰奥·彭佐从2006年7月进行眼动研究发现，从标签移动到输入框只需50毫秒。比左对齐标签快了10倍，后者需要500毫秒；比右对齐标签方式快2倍，后者高达240秒。能迅速填完顶对齐标签表单的原因之一，是因为眼球只需要在标签和输入框之间进行上下单向运动。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/JwCDoA7uIXmSQT8SIzEK.png" alt="Web表单设计——你不知道的冷知识" width="662" height="631" referrerpolicy="no-referrer"></p>
<p>1）优势</p>
<p>最利于减少表单填写时间（标签和输入框位置最为靠近）；用户视线固定，动线一直向下（清晰的完成路径）；节省大量横向空间（可用于以多种方式组合的相关输入框）。</p>
<p>2）劣势</p>
<p>占用额外的垂直空间（如果可提供使用的垂直屏幕空间较小，应当谨慎使用顶对齐标签）；建议使用输入框50%至75%的高度作为相邻输入框间距。</p>
<p>3）适用场景</p>
<p>希望用户快速填写表单，完成任务；同时，当输入项存在主次之分时，对标签扩展性要求高。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/W786INKcFN8ecCUiIIMD.png" alt="Web表单设计——你不知道的冷知识" width="663" height="450" referrerpolicy="no-referrer"></p>
<h3>2. 右对齐标签</h3>
<p>如果要尽量减少表单占用垂直屏幕空间，右对齐能提供快速完成时间。马泰奥·彭佐的眼动研究发现，专家用户和新手用户扫视（眼睛运动）右对齐标签表单的标签和输入框的平均时间分别在170毫秒和240毫秒，而填写完成时间比左对齐快2倍。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/LuBZ3lueMkKsDZmdXM0Z.png" alt="Web表单设计——你不知道的冷知识" width="662" height="475" referrerpolicy="no-referrer"></p>
<p>1）优势</p>
<p>标签与输入框相邻（方便快速填写）。</p>
<p>2）劣势</p>
<p>右对齐布局造成左侧不齐，影响了快速游览表单的效率问题；若标签文字宽度变宽，右对齐还存在灵活度问题。</p>
<p>3）适用场景</p>
<p>既要减少垂直空间，又要加快填写速度的场景。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ZWpVVFnPT3zXqjkIFqGV.png" alt="Web表单设计——你不知道的冷知识" width="659" height="447" referrerpolicy="no-referrer"></p>
<h3>3. 左对齐标签</h3>
<p>在顶、右、左三种方案中，左对齐表单填写速度最慢。因为左对齐表单解析问题时眼球定位次数最多，用户一般情况下都能将左对齐布局中的标签和输入框联系起来，只是花费时间较长。根据马泰奥·彭佐的研究，典型扫视时间为500毫秒，很长说明用户经历了沉重的认知压力。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/zeFOpRY2XdIMCmmjAlVl.png" alt="Web表单设计——你不知道的冷知识" width="661" height="497" referrerpolicy="no-referrer"></p>
<p>1）优势</p>
<p>容易游览标签；占用垂直空间较少。</p>
<p>2）劣势</p>
<p>标签和输入框的相邻间距增大；适合于用户不熟悉表单要收集的数据或问题无法分成易处理的内容组，左对齐标签游览表单问题会更容易。用户只要上上下下阅读标签左栏，不会被输入框打断。</p>
<p>3）适用场景</p>
<p>表单中存在较多的复杂或敏感信息，希望用户放慢速度、仔细思考（在一些注册类表单中较多使用）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/IuVQIeLwPCDLRkrTy1Yh.png" alt="Web表单设计——你不知道的冷知识" width="660" height="444" referrerpolicy="no-referrer"></p>
<p>单从效率角度看，顶对齐标签>右对齐>左对齐，但是根据应用场景，效率快并不是我们选择标签对齐方式的唯一的指标。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SDoO1ibA9TEGUfm3DCnF.png" alt="Web表单设计——你不知道的冷知识" width="663" height="360" referrerpolicy="no-referrer"></p>
<p>因此，得到以下几点建议。</p>
<p>如果你希望用户放慢速度，仔细思考表单中每个表单项，左对齐标签是个好选择，特别是含有大量可选输入框或高级设置的陌生数据时。</p>
<p>而顶对齐标签在一些国际化产品的表单设计时，会有更好的延展性。</p>
<p>至于，右对齐标签虽然与表单域联系紧密，便于用户填写，但是要考虑好标签的长短不齐如何解决。能否精简标签内容，以及确定好表单与界面的边距。</p>
<h2 id="toc-3">三、标记必填与可选字段的困惑</h2>
<p>许多表单设计中，有个常见问题：是否应该标记必填字段？如果表单中的大多数字段或全部都是必填的，我们是否仍然应该标记它们？</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/EOXjpHVk9I1r06DiX75V.png" alt="Web表单设计——你不知道的冷知识" width="664" height="475" referrerpolicy="no-referrer"></p>
<p>先简单回答：是肯定的，用户有时需要通过必填标记来评估工作量，了解输入信息量的最低限度。我会在下面具体解释原因。</p>
<h3>1. 了解不标记必填字段的诱惑</h3>
<p>通常，设计师会觉得每个必填字段都有一个标记是重复的、丑陋的、占空间，而且干扰界面，甚至可能看起来很扰乱（有认知负担！）。因此通常采取以下一种或两种策略：</p>
<ol>
<li>在表单顶部显示说明，说明中除非另有解释，否则所有字段都是必填；</li>
<li>只标记可选字段，因为它们通常较少；</li>
<li>在某些特殊情况下，也会什么都不做：相信用户会神奇地知道需要填写什么字段；如果不知道，那么只需要点击提交报错即可。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/OHcqiNYY90JxSRQCJANi.png" alt="Web表单设计——你不知道的冷知识" width="662" height="450" referrerpolicy="no-referrer"></p>
<h3>2. 这些方法有什么问题？如果你这样想，我来告诉你</h3>
<p>1）用户一般不喜欢阅读表单顶部说明。不难想象，用户不太可能阅读表单顶部的说明。表单字段需要自给自足，毕竟，每个字段都有特定指令——它的标签，为什么用户需要阅读其他任何东西来填写它呢？</p>
<p>2）即使用户阅读了说明，也可能忘记。你可能会说：用户阅读了顶部的说明，怎么就会忘记——这么简单的事情？</p>
<p>的确容易忘记，特别是当表单很长或填写表单被打断时（这种情况在移动端很常见）。即使用户记得，但这占用了工作记忆，增加了认知负荷。换句话说，你让用户完成任务更难了。填写表单本身对用户来说就相当有挑战性——为什么要让它更具有挑战性？</p>
<p>3）用户必须扫描表单以确定是否为必填字段。不难发现，无论是否在表单顶部包含说明，结果都可能相同，用户会忽略或忘记。他们会扫视表单，找到一个标记为必填或可选的标识。</p>
<p>而且有些用户甚至不会费心去环顾四周，他们只会做出假设。他们会想——“嗯，邮箱——不需要我的邮箱吧？先空着呢”。即使用户没有留空，也不得不暂停来思考一个字段是否需要填写，减慢交互速度并使过程看起来更长、更乏味。</p>
<p>想要解决以上问题很简单：标记所有必填字段。尽量明确和清晰展示每个必填字段，并标记它。当然，就像有些设计师所说：界面出现大量必填标识（红色星号*）确实会增加视觉噪声。甚至重复的星号 * 会带来一些认知恐慌。但相比之下，两害取其轻，这些负面因素是轻微的。</p>
<h3>3. 如何标记必填字段？</h3>
<p>这里包含至少有两种方式：星号*（红色）和“必填”提示。星号*在网页上已经很常见，用户熟悉其含义。优点是它不占用太多空间，也看起来与标签文字足够不同，所以使用它。</p>
<p>可以使用其他标记形式吗？当然可以，但是最好遵循市面上常见的形式（雅各布定律），这样更符合用户认知。</p>
<p>星号应该在字段标签之前还是在字段标签之后？</p>
<p>这不一定有实际影响，但将其放在标签之前的一个原因是，只需扫视标签的最左边字符，就能轻松定位必填哪些字段。</p>
<p>星号*是一种视觉标记，应当仔细考虑表单中的标识位置。标识在标签左边能指引用户迅速浏览界面，并判断出必填项。如果在右侧由于输入框形式、长度各不相同，标识和输入框对齐会导致难以浏览和判断。</p>
<h3>4. 是否也应该标记可选字段？</h3>
<p>虽然这不是强制性的，但标记可选字段确实减轻了用户思考：如果没有这个标识，用户要环顾四周，并根据其他标记字段推断该字段是可选的。如果“非必填”在字段标签旁边，那该任务会变得更容易。不描述可选字段，这没问题，但这样做会是一个很好的额外帮助。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/egNwaobBXqz5XWIVnB8F.png" alt="Web表单设计——你不知道的冷知识" width="661" height="268" referrerpolicy="no-referrer"></p>
<h3>5. 为什么登录表单没有标记必填？</h3>
<p>登录表单很短，一般由两个字段组成：用户名和密码，这两个字段总是必填的。如果使用星号*，标记这些字段的成本很低，并不会出错。但是，绝大多数用户都使用过很多登录表单，他们是知道要登录需要输入邮箱/用户名和密码的。所以，在登录表单中，可以省略这种形式。</p>
<p>而在注册表中不标记必填字段是危险的。注册表单因产品而异——不同公司在创建帐户时需要不同类型的信息。它不仅仅包含用户名和密码，所以请标记所有必填字段（包括用户名和密码）。</p>
<p><strong>因此，提出以下几点建议。</strong></p>
<p><strong>基础前提，尽量去除任何不需要回答的问题，特别是涉及到用户隐私的内容。可以更容易让用户填完表单。</strong></p>
<p><strong>为了增加表单填写的机会，请尽量减少用户需要付出的努力和他们需要记住的信息。有很多方面有助于解决这些问题，但标记必填字段（以及可选字段）是最容易的方法之一。</strong></p>
<h2 id="toc-4">四、表单域提供一些默认值有必要吗</h2>
<p><strong>先给出答案：这是肯定的！</strong></p>
<p>在《选择的悖论》一书中，作者巴里·施瓦茨讨论了生活中选择过多的影响。并提出策略应付无处不在的过多选择。他特别叙述了智能默认的能量——即在满足多数人需要的地方放置选择——来帮助人们做出明智的选择。</p>
<p>而在Web表单中也有很多地方能利用智能默认减少不必要的选择次数或输入，加速表单完成过程。所以，只要合适就在表单域中预先为用户填写你认为他们想要的输入值。</p>
<p>通过提供合理的默认，能有效节省用户时间，就是这么简单。应用分担了用户思考或输入答案的工作。填写表单永远不是一件有趣的事情，如果这个模式能把表单填写的时间减少一半，用户会非常感激。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/i6HZZy9vAfMCjbPhbVAd.png" alt="Web表单设计——你不知道的冷知识" width="662" height="378" referrerpolicy="no-referrer"></p>
<p>你可能会问：默认值不是用户想要的，误导用户怎么办？</p>
<p>在设计有默认值的表单域时，你要思考默认值是否是大多数用户可以接受的答案，如果不确信可以先去做一下用户调研，了解用户的心声。</p>
<p>就算默认值真的不是用户想要的，至少你也为他提供了一个示例来告诉用户答案应该是什么样子的。这一点也可以节省用户几秒的思考时间——或避免一条错误信息。</p>
<p>但并不代表所有的表单域都要给出默认值，我们只是尽可能的让用户节省时间。</p>
<p><strong>如何使用：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/MYzpoPHkwLY2Ur0sqUYx.png" alt="Web表单设计——你不知道的冷知识" width="661" height="268" referrerpolicy="no-referrer"></p>
<p>在第一次向用户显示表单时，用一个合理的默认值预先填写文本框、组合框或者其他控件。也可以使用用户之前提供给应用的信息来动态地给出默认值（例：通过身份证自动识别出生日期；利用邮编，推导出对应省/市）。</p>
<p>如果只是因为你觉得不应该留下空白的输入域，那么不要使用默认模式。只有当你有理由确信绝大部分用户，在绝大多数情况下，不会修改这个取值时才提供默认值——否则，这将会给用户带来额外的工作！</p>
<h2 id="toc-5">五、输入框的宽度如何设定</h2>
<p>有一个容易被忽视但实则举重若轻的问题，表单中输入框宽度如何设定？</p>
<p>在表单设计中，对于 Checkbox、Radio 等控件，很明确必须跟随内容自适应处理。但对于Input、Select等你会不会产生困惑，是定宽处理还是跟随内容更好。</p>
<p>不知道你是否试图这么理解过？输入框作为用户填写信息的主要方式，其表现形式是否可以提供给用户填写表单的有用线索。</p>
<p>唐纳德·诺曼的著作《设计心理学》中详细讲解过心理暗示方面的内容。而宽度的变化就是一种有效暗示。</p>
<p>在真实场景中，大部分输入框是存在理想长度的，那么就应该向用户暗示所需输入内容的长度来减轻判断负担。</p>
<p>下图就是典型案例，一个实际不需要花多少钱的金额输入框在左图中进行等宽处理，反而容易误导用户对输入金额的判断，造成一种不安全感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4SDZalVky5uNvwVToA6J.png" alt="Web表单设计——你不知道的冷知识" width="663" height="173" referrerpolicy="no-referrer"></p>
<p>表现形式要为用户填写提供有用线索，采用不同长度的文本框提供了暗示；这种暗示是一种有用线索，当输入框长度长短不定时，用户会很自然地思考为什么这样；填写输入框时会自然考虑这些线索。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/yTSsZbVgSPkryGOafTKv.png" alt="Web表单设计——你不知道的冷知识" width="663" height="379" referrerpolicy="no-referrer"></p>
<p>请注意！保证暗示效果的同时，不要设定太多的宽度，反而会让表单显得凌乱；太少又会让表单看起来都像四四方方的盒子。最佳方法是找到适合产品的最佳模度值和数量。</p>
<p><strong>什么是模度值和数量呢！</strong></p>
<p>落在具体设计上要先梳理产品中常见的表单类型，然后设置一个默认宽度。以此为基础来有规律的增加长度，并考虑清楚它们的适用场景；从而定义出不同的模度，最终制定出整洁有序的模度规范。这样就可以让一线的设计师们跳过部分繁琐磨人的细节思考，快速搭建出合适的表单宽度并合理有效。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="Web表单设计——你不知道的冷知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SBGXOeiBLNG7DlZxiZny.png" alt="Web表单设计——你不知道的冷知识" width="661" height="257" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、结语</h2>
<p>本篇文章更多是从表单设计中的一些冷门内容，即易忽略的一些设计点在展开讨论，利用问题加案例的形式对表单设计进行剥离拆解，没有系统地、成本成套的来分析表单的构成和交互细节等等。因为这类内容讲的人太多了，我也认为讲的要比我精彩。</p>
<p>所以，我把讲的内容称为“私房菜”，更多是我总结了日常工作中会遇到的表单设计疑问和思考，帮助大家换一个口味来品味表单设计，大家可结合文章中给出的建议作为参考去灵活应用。</p>
<p>同时，我也希望能够通过这篇文章给到大家更多的启发。内容如果有不严谨、错误的地方还望大家给与指正。</p>
<p> </p>
<p>作者：百度MEUX，百度移动生态用户体验设计中心，负责百度移动生态体系的用户/商业产品的全链路体验设计</p>
<p>本文由 @百度MEUX 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5192419" data-author="180796" data-avatar="http://image.woshipm.com/wp-files/2020/05/TtUzNAsIlx3fAtQVqoSV.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            