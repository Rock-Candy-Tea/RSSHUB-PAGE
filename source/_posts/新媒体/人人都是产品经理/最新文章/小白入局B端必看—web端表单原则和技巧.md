
---
title: '小白入局B端必看—web端表单原则和技巧'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/gtM2EovWJXftU8eUkPwB.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 13 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/gtM2EovWJXftU8eUkPwB.jpg'
---

<div>   
<blockquote><p>编辑导语：表单页用于信息的添加和录入，它在企业中台中无处不在。本文作者对B端的基础通用组件表单进行了总结，并对其中一些高频问题作出了解答，感兴趣的小伙伴们一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5436933" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/gtM2EovWJXftU8eUkPwB.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>表单页是B端产品中的典型页面，用于信息的添加和录入，表单页在企业中台中无处不在，如创建直播、新增客户、新建商品、中奖设置、报销申请、职位发布等，有些小伙伴在设计B端表单时，不知道需要注意哪些问题，本文对B端基础通用组件表单进行了总结，带你全面了解在设计表单过程中需要了解的知识和遵循的原则，希望能给到小伙伴一些启发和帮助。</p>
<h2 id="toc-1"><strong>一、表单的作用</strong></h2>
<p>后台产品的本质是针对数据的增、删、改、查，其中增、改、查都可以用表单来完成，系统本身是没有信息的，表单是用户和数据库之间的媒介，在网页中主要负责数据采集的功能。</p>
<p>相对于其他页面而言，当用户进到表单页时使用阻力和操作阻力是很大的，因为用户完成任务时有思考成本和操作成本，很多时候用户会因为填写信息太过繁琐，从而放弃了对该产品的使用。</p>
<p>因此在设计录入表单时，合适的表单才能提高录入任务的完成度和满意度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/9UrAdo3X3bmyPNLeT9To.png" alt width="850" height="2052" referrerpolicy="no-referrer"></p>
<h2 id="toc-2"><strong>二、 表单的构成</strong></h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/T2tKPulg6s2kXPi79Ob6.png" alt width="850" height="2024" referrerpolicy="no-referrer"></p>
<p><strong>1）标签</strong><strong>/</strong>Lable</p>
<p>说明：通常放置在表单字段之外或者字段内，对输入项或设置项的解释说明，可用文字或图标表示。</p>
<p>作用：提示用户要输入什么内容，帮助用户快速理解每一项字段的作用。</p>
<p><strong>2）表单域</strong>/Formfield</p>
<p>说明：包含了输入框、下拉框、日期选择器、时间选择器、开关、上传等等。</p>
<p>作用：用来收集用户输入的信息，每个字段包含着某一类型的信息，是形成表单的核心内容。</p>
<p><strong>3）提示信息</strong>/Promptinformation</p>
<p>说明：包含占位符、帮助信息、校验信息，后面会详细讲到。</p>
<p>作用：帮助用户有效正确填写信息的引导内容或反馈内容。</p>
<p><strong>4）操作按钮</strong>/operatingbutton</p>
<p>说明：当用户完成信息录入时，暗示可点击性，必须让用户一眼看出这个是可点击的交互区域，一般情况占据最高的层次关系，暗示整个界面的唯一目的和操作。</p>
<p>作用：提交内容到服务器，对表单内容进行校验、提交或者进行下一步操作。</p>
<h3><strong>1. 标签</strong></h3>
<p>指明用户需在此表单上要填写什么类型的信息，通常放置在表单文本框之外居左或上方的位置，极少数情况下也会放置于文本输入框内，可用文字或图标展示，标签的对齐方式一般分为左标签、顶标签、行内标签。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/A9ego47RzB7P5ltISFLs.png" alt width="850" height="1580" referrerpolicy="no-referrer"></p>
<p>在Matteo Penzo《Label Placement in Forms》文章中有分享过关于表单标签放置的研究，他分别对标签左对齐、右对齐以及顶部对齐做了用户眼动追踪实验，下图是此测试的眼动数据。</p>
<p>Matteo Penzo-根据表单标签对齐方式研究出来的时间表：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/WoCblICxzhX5NQBGHo4z.png" alt width="850" height="2136" referrerpolicy="no-referrer"></p>
<p>单从效率角度看，顶对齐标签>右对齐>左对齐，但是根据应用场景，效率快并不是我们选择标签对齐方式的唯一的指标，还是要根据用户需求和实际业务场景提供不同的解决方案。</p>
<p><strong>1）左对齐标签</strong></p>
<p>视线从标签移动到输入框的时间为500ms ，花费时间很长说明用户经历了沉重的认知压力，原因是违反了格式塔原理，标签和表单域之前存在负空间（格式塔原理：距离更近的更容易被看成一个整体）离得远用户就要思索一段时间判断是否是一个整体所以左对齐表单填写速度最慢。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/85vKYwrlPyuKclEX1ehy.png" alt width="850" height="1840" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>优点</strong>：视觉动线符合用户的阅读习惯，因此阅读效率高。</li>
<li><strong>缺点</strong>：标签与输入域负空间间距长短不一，操作效率低 。</li>
</ul>
<p><strong>2）右对齐标签（冒号对齐标签）</strong></p>
<p>视线从标签移动到输入框的时间为240ms。</p>
<p>因为右对齐有锯齿状的视觉动线，不利于快速扫视，所以用户阅读效率不高，但是符合亲密性原则,快速填写的速度更快，右对齐表单完成时间比左对齐快2倍。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/oIqr2H3X3BSDJN70x1LA.png" alt width="850" height="1840" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>优点</strong>：标签与输入域有明确的视觉关联，符合亲密性原则，操作效率高。</li>
<li><strong>缺点</strong>：有锯齿状的视觉动线，不利于快速扫视，所以用户阅读效率不高。</li>
</ul>
<p><strong>3）顶对齐标签</strong></p>
<p>视线从标签移动到输入框的时间为50ms。</p>
<p>Matteo Penzo从2006年7月进行眼动研究发现视线从标签移动到输入框的时间为50ms， 比左对齐标签方式快了10倍，比右对齐标签方式快2倍，能迅速填完顶对齐标签表单的原因之一，是因为眼球只需要在标签和输入框之间进行上下单向运动。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/l87uRarpzS109diT76o8.png" alt width="850" height="2200" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>优点</strong>： 节约横向空间，对齐视觉舒适，对齐方式符合视觉动线，阅读、操作效率高。</li>
<li><strong>缺点</strong>：一定程度上占用大量的纵向空间，纵向空间利用率不高。</li>
</ul>
<p><strong>4）行内标签</strong></p>
<p>视线从标签移动到输入框的时间为10ms。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/suC9YyGmb153IXCMkc1m.png" alt width="850" height="1840" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>优点</strong>：最节约空间，多用于登录注册。</li>
<li><strong>缺点</strong>：输入状态标签消失，用户会有迷失感。</li>
</ul>
<p><strong>高频问题一：</strong>表单标签应简洁明了，在哪个位置才是最高效的呢？标签到底是左对齐、右对齐还是顶部对齐呢？</p>
<p>答案是根据用户需求和实际业务场景提供不同的解决方案。</p>
<p>如果是用于<strong>移动端或者国际化的产品</strong>（比如国际化的出海产品设计，可能会适配多种语言，有些单词翻译过来就会很长）顶对齐标签是个不错的选择。</p>
<p>如果是<strong>详情的陈列</strong>（快速扫视的速度更快）或者<strong>涉及比较复杂和敏感需要用户放慢速度</strong>，仔细思考的场景，可以选用左对齐标签。</p>
<p>右对齐标签虽然与表单域视觉关联强，用户录入效率高，不过要考虑好标签长短不一的问题。</p>
<h3><strong>2. 输入域</strong></h3>
<p>输入域是表单的主题与核心，用来收集用户操作的信息，每个输入域字段包含一个类型信息，输入域不仅仅是文本输入框，从交互组件的角度来看，其包括文本输入框、单选框、复选框、开关、选择器、步骤条、上传、Tab切换、滑块、步骤条等等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/wFb3hBIH89zyHzAWIjYC.png" alt width="850" height="1700" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/JJsZezzbYxUUTfl0pSaL.png" alt width="896" height="4113" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/QePWA8TV8DT1zHRcDKZb.png" alt width="850" height="7874" referrerpolicy="no-referrer"></p>
<h3><strong>3. 提示信息</strong></h3>
<p>帮助用户有效正确填写信息的引导内容或反馈内容，以文字或者图标形式展现在要说明的内容旁边，图标形式的情况鼠标hover时显示全部信息，从提示信息所处的位置和提示出现的时机，提示可分为输入框内提示、输入框外提示、激活输入框提示、图标悬停提示及单独区域提示等。</p>
<p><strong>1）占位符</strong><strong>/</strong>Placeholder</p>
<p>说明：通常放置在表单字段之外或者字段内，对输入项或设置项的解释说明。<br>
作用：提示用户要输入什么内容，帮助用户快速理解每一项字段的作用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/MP1bwtDT0TXxLGY3L2u3.png" alt width="850" height="1040" referrerpolicy="no-referrer"></p>
<p><strong>2）帮助信息</strong><strong>/</strong>Help Information</p>
<p>说明：文字形式的表单帮助信息很重要，需要让用户必须知晓的一般放在表单字段右侧，图标形式则常用于信息内容非用户必须知晓的，以图标形式隐藏内容，在需要时鼠标hover显示。</p>
<p>作用：帮助用户解释名词和引导用户完成任务。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/uN07zVsWGLTC01S41wqL.png" alt width="850" height="1498" referrerpolicy="no-referrer"></p>
<p><strong>3）校验信息</strong><strong>/</strong>Check the information</p>
<p>说明：当用户填写表单的信息无法被录入时给予反馈、实时提供建议参考或者对录入内容的提示，在错误信息显示在对应表单项旁边，尽量减少用户记忆和认知负荷。</p>
<p>作用：当用户填写的信息无法被录入时给予反馈。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/5OLbVMG42b3upiyhULru.png" alt width="850" height="1032" referrerpolicy="no-referrer"></p>
<p>提示一般可分为引导提示和反馈提示两类。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/bG6Ufsks6DJSFRq3goCR.png" alt width="850" height="1528" referrerpolicy="no-referrer"></p>
<p><strong>4）引导提示</strong></p>
<p>发生在用户输入前，引导用户正确输入信息或对输入信息规则的注释与说明，输入框内提示、输入框外提示、激活输入框提示都可归为引导提示，引导提示可细分为全局提示和定位提示。</p>
<p><strong>①全局提示：</strong>一般位于表单顶部显示的注释与说明，告知用户填写表单的注意事项、信息采集的用途以及信息安全性保证等，解除用户输入时的顾虑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/aT6aVjTo1VoLSdl5xLbs.png" alt width="850" height="2128" referrerpolicy="no-referrer"></p>
<p><strong>②定位提示：</strong>适用于表单很长，用户注意不到自己错哪儿了，在相应错误位置进行提示，帮助用户快速定位到错误内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/rtxY0Qd5MhSVbBidqe1Q.png" alt width="850" height="2130" referrerpolicy="no-referrer"></p>
<p>单项提示也可以选用不同的布局，分别有输入框内提示、在鼠标haver时气泡提示、输入框下方文字提示、输入框后方文字提示。</p>
<p>错误提示一般停留2-3S后消失。</p>
<p><strong>5）反馈提示</strong></p>
<p>发生在输入中或输入后，页面系统对用户的输入给与校验，并对校验结果予以展示的提示形式，输入中作用：实时反馈， 输入后作用：提醒和纠错。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/3kG72R6AiNCVoJPpjad5.png" alt width="850" height="1764" referrerpolicy="no-referrer"></p>
<ul>
<li>缺点：影响一些性能，但是这个影响比较小，如果在输入一个错误率很高的内容，频繁的给用户错误提示会影响用户体验。</li>
<li>优点：该方式的校验条件多在本地，不需要实时向服务器发命令，以得到反馈，减轻后台数据传送压力。</li>
</ul>
<p><strong>①失去焦点、即时报错</strong></p>
<p>当某项录入项已录入完成并失去焦点时，触发系统校验（校验内容存储在远端，程序需要完整的输入信息到远端进行检验，并给出反馈）并且尽量采用非模态反馈的方式，避免打断当前任务流。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/b8aKaclMFIjE87WC5SIm.png" alt width="850" height="948" referrerpolicy="no-referrer"></p>
<ul>
<li>缺点：如果输入有误，用户需要多一步操作，点击会有错误的输入框进行修改，稍微影响用户体验。</li>
<li>优点：降低用户的问题查找和修改成本，避免出现很多错误需要改正的情况。</li>
</ul>
<p>注意：<strong>要清晰地描述错误并提供相应的解决方案</strong>，报错文案应该尽可能简短，用户看到一大段文字，很可能会失去了去阅读的耐心，文案还应清晰指出错误的原因，对于用户可自己修复的问题，应告知问题如何修正。</p>
<p>如果弹窗空间足够，可以直接展示图片样式，降低折叠度，避免用户二次点击，减少了一步用户操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/L0UtrJyF3cbQIxrQ9tCh.png" alt width="850" height="1416" referrerpolicy="no-referrer"></p>
<p><strong>②操作/保存/提交/下一步 时全部报错</strong></p>
<p>用户全部输入完成以后，点击下一步操作的时候将所有错误提示都展示给用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/FlfKFuqsIXD4r33pO4Hl.png" alt width="850" height="2534" referrerpolicy="no-referrer"></p>
<ul>
<li>缺点：用户不能及时看到反馈，及时进行修改，如果表单过长的话，会增加用户的问题查找和修改成本。</li>
<li>优点：减少后端服务器压力，提高页面性能。</li>
</ul>
<h3><strong>4. 操作按钮</strong></h3>
<p>操作按钮：表单界面操作的最后一步，填写完表单各项内容后，所要进行的操作动作（eg：保存、取消、提交、确定等）来结束当前操作流程或在流程之中或之后开启新的功能操作，在视觉上暗示用户可点击，提示元素可以是文字或者图形，例如保存、取消、下一步等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/8Zko6u5u4dzsQc8rZHkY.png" alt width="850" height="1656" referrerpolicy="no-referrer"></p>
<p>标签一般为每个输入项的名称，按所要填写信息的必要性又可分为必填项和非必填项。</p>
<ul>
<li><strong>必填项：</strong>用户必须要输入有效的文本信息，否则，该表单就不能正常提交、保存等操作。</li>
<li><strong>非必填项</strong>：该项信息用户可填可不填，根据用户的意愿和需求度来自愿选择填或者不填。</li>
</ul>
<p> </p>
<p><strong>高频问题二：</strong>如果大部分都是必填项，还有必要标记必填字段吗？必填项or非必填项到底有无必要标注。</p>
<p>通常设计师们会觉页面上每个必填字段都有一个标记都有星号会让页面视觉噪音太重，让用户产生视觉疲劳，原本清清爽爽的页面看起来low low的。所以一般设计师逃避星号的三种措施是：</p>
<p><strong>1）给全局提示</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/kHcTXZ7s0I2doY9P0INe.png" alt width="850" height="2196" referrerpolicy="no-referrer"></p>
<p><strong>缺点：</strong>用户一般会直接忽视这类说明，当用户填写字段时，用户视线会更聚焦这项字段本身都什么要求，不太可能阅读到表单最顶部的填写说明，用户会讨厌读各种说明，比如我们去到景区里面，不喜欢读景区里面的景区说明，在公共场合也很容易忽视禁止什么禁止什么的标识，用户很有可能不会注意到表单最顶部的说明。</p>
<p>即使读了之后会忘记，特别是当表单很长或者填写表单被打断的时候。让用户记得顶部说明，会占用用户的工作记忆，增加认知负荷，加大用户填写表单的阻力，让本身就具有挑战性的表单更是难上加难。</p>
<p><strong>2）只标记占比较少的可选字段</strong><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/BdjxOWqBWNQladjkp5JW.png" alt width="850" height="2068" referrerpolicy="no-referrer"></p>
<p><strong>缺点：</strong>用户必须扫描表单以确定是否为必填字段或选填字段，用户会扫视表单找到一个标记为可选的标识，即时找到了那些是非必填也会很容易忘记，看到没有标星的字段可能会做出假设。</p>
<p>用户可能会想：“嗯，工作单位——不需要我的工作单位吧？先空着吧”，即使用户不留空，也不得不暂停来思考这个字段是否需要填写，增加了用户的思考和理解负担。</p>
<p><strong>3、什么都不标注</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/uuNg86TPm5ForTXIGquE.png" alt width="850" height="2068" referrerpolicy="no-referrer"></p>
<p><strong>缺点：</strong>什么都不做，让用户去猜哪个是必填项哪个是非必填项，他们相信用户自己可以判断，如果没有填写必填项，提交的时候报错，让用户完善填写信息，当给出用户提示的时候，用户都很有可能不按照规则填写提交的时候出现报错，毋庸置疑，什么都不提示更加会提高用户出错的概率。</p>
<p>用户会通过必填标记来评估工作量，了解输入信息的最低限度，因此标记必填字段是很有必要的，尽量清晰明确的展示每一个必填字段，尽管界面出现大量星标时会让界面看起来不清爽优雅，加重界面的视觉噪音，甚至重复的星号 * 会带来一些认知恐慌和紧张感。但这些负面影响相对于必填项不标星的后果是可以原谅的。</p>
<h2 id="toc-3"><strong>三、交互模式</strong></h2>
<p>表单页面的交互方式分为以下4种：就地编辑、气泡卡片、弹窗、抽屉、页面跳转，根据具体的使用场景选择合适的页面交互。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/WuaVUDHV1sw5oGCTAdcb.png" alt width="850" height="1184" referrerpolicy="no-referrer"></p>
<h3><strong>1. 原位编辑</strong></h3>
<p>原位编辑是比较轻量型信息采集表单形式，适用于表单内容较少，使用频率较低的场景，同时属于主功能分支的场景，表单操作后页面随即发生反馈改变，保证用户对主要功能的高效操作，通过双击或点击特定的操作按钮即变为激活编辑状态。</p>
<p><strong>优点：</strong>操作便捷，不会打断还可单击空白处随时退出。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/VsgLPrggFpcRKjQBbnJx.png" alt width="850" height="1758" referrerpolicy="no-referrer"></p>
<p>hover下给到一个输入框来显示可以原位编辑。</p>
<p>加一个小铅笔的图标，可以是hover的时候高亮，也可以默认放一个小铅笔，主要看业务上编辑的频次高频不高频，编辑和浏览那个需求更重要。</p>
<h3><strong>2. 气泡卡片</strong></h3>
<p>点击或者鼠标移入弹出气泡式的卡片浮层。气泡卡片交互方式也是比较轻量化的形式，气泡提示共有12种箭头方向，其对齐方式根据实际显示内容选择合适的样式，所产生的表单页与当前的页面亲密性紧密相关。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/ryueL5rGD860gpXufyr2.png" alt width="850" height="1290" referrerpolicy="no-referrer"></p>
<h3><strong>3. 弹窗</strong></h3>
<p>弹窗样式的输入表单是主要流程步骤中的分支流程，输入弹窗样式的表单，输入内容的多少处于页面跳转和就地编辑两种样式之间，用户在不离开当前页的情况下继续操作，是流程步骤中的分支行为，可由用户选择是否进行，不不覆盖用户已阅读内容。</p>
<p><strong>注意点：</strong></p>
<p>在直播列表页点击新增直播或者在工作台点击新增直播，弹出的弹窗保持一致， 比如做直播的添加商品弹窗，不管他的入口在任何一个页面，交互出来的容器要保持一致，如果新增一条规则，和新增直播这个无关，规则里面的内容比较多，弹窗容纳不下的情况下，是可以用抽屉来承载内容的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/MMWISbi7XFWmULTcSL81.png" alt width="850" height="2316" referrerpolicy="no-referrer"></p>
<h3><strong>4. </strong><strong>抽屉</strong></h3>
<p>抽屉交互的表单样式是比较常见的交互样式，它的拓展性很强，承载的信息很多，当前页面的分支操作，体现两页面之间的层级关系，信息承载量和页面比肩，又兼具弹窗的优点，同时又有连续操作的优点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/dOoEg7wQ02mNUIVw7ZT7.png" alt width="850" height="2458" referrerpolicy="no-referrer"></p>
<ul>
<li>内容比较多时，可以把弹窗换成抽屉</li>
<li>强调详情可以连续查看</li>
<li>可以快速切换列表，主要操作流程在一个页面中展示，保证主要功能的操作的流畅度</li>
</ul>
<h3><strong>5. 页面跳转</strong></h3>
<p>若输入内容特别多，超出了弹窗/抽屉的承载量时，建议使用页面跳转，页面跳转的信息承载能力强，对反馈的及时性要求不高也没有那么强的关联性，常用于岗位发布、创建直播、初始化入住等复杂信息的发布。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/jRF3L6IjgUrY6rM2Wq4q.png" alt width="850" height="1858" referrerpolicy="no-referrer"></p>
<p>页面跳转包含两种：新页面打开和当前页面跳转。</p>
<ul>
<li><strong>新页面打开</strong>：主要流程步骤中的分支流程，页面功能具有独立性，不影响用户对主流程的继续操作。</li>
<li><strong>当前页面跳转</strong>：流程步骤中的关键步骤，提示用户已进入下一步，关键流程建议在当前页面打开，让产品主流程更加清晰，建立新页面会分散用户注意力增加用户的迷失感，当前页面跳转则让用户更聚焦于当前页面的信息中。</li>
</ul>
<p>尽量避免页面跳转，页面的跳转势必造成重新加载和刷新，这本身就会耗费一定的时间，此外，跳转还会造成用户行为的中断，以及浏览的不顺畅。</p>
<h2 id="toc-4"><strong>四、内容布局</strong></h2>
<p>在web页面中，由于页面的关系，导致跳转页面与弹窗的横向空间较大，纵向空间不足，若出现较多的输入内容时，且不能采用分模块、分步骤、高级等交互布局时，有的小伙伴会采用双列或多列表单，以提高横向空间的利用，这也是可以的，要注意列与列间距的合理性以及遵守用户的视觉流畅，可以参照菲兹定律。</p>
<p>但是作为表单，单列表单的浏览及填写效率是最高的，用户的视觉流较为顺畅，可以提升填写效率，同时能够减少用户的疲劳度，因此建议表单多采用单列布局。</p>
<h3><strong>1. 标题分组</strong></h3>
<p>用户的认知成本会少很多，用户知道自己每填一步在干嘛，而不是密密麻麻一大片，让用户完成表单时会有阶段感，降低用户自主归纳的成本，同时用户可以在填写好一段内容后进行心理上停顿休息，减少视觉疲劳和心理压力。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/bQBTPrVfpJFkiaOVI41T.png" alt width="850" height="2814" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>以必填项划分：</strong>若表单内有必填项和非必填项，且各项之前关联度不高，可采用将必填项划分为一组进行优先呈现，该种方式有助于让用户快速发现自己需要录入的内容。</li>
<li><strong>以相关性划分：</strong>若录入项较多，且各项内容之间存在明显的关联度区分，可考虑以内容相关性进行信息分组，该种方式有助于让用户理解各项内容间的逻辑关系。</li>
</ul>
<h3><strong>2. 标题+卡片分组</strong></h3>
<p>如果表单里面已经完全区分不同性质和类别的时候，可以考虑直接用卡片，输入组件、分类、分模块的排版方式让用户感觉更好，在视觉样式上进一步做归类和区分，上一个是天然的间距区分，该种方式有助于让用户理解各项内容间的逻辑关系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/wTeBcfMfFIELToRh3ADQ.png" alt width="850" height="2814" referrerpolicy="no-referrer"></p>
<h3><strong>3. 标签页</strong></h3>
<p>卡片分组和标题分组都用到了，但是表单太多了，三个相对独立的，那么就用标签页。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/7DMBmcHH5rpSEB3we3M5.png" alt width="850" height="1688" referrerpolicy="no-referrer"></p>
<h3><strong>4. 锚点定位</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/DV46llvqnVrMhsrgQrDX.png" alt width="850" height="2782" referrerpolicy="no-referrer"></p>
<h3><strong>5. 步骤</strong></h3>
<p>对于内容过多的表单输入组件，又有着明确的操作先后关系，可以选用分步骤，一般不超过三步，每屏仅展示该步骤下的表单输入组件有些场景下，系统只需要用户录入简单的信息，分步表单常用于输入项较多，业务本身具有流程化特性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/jACosYpSqAit88WqIqKO.png" alt width="850" height="2782" referrerpolicy="no-referrer"></p>
<p>为了提高用户填写效率，减少用户心理负担，将一个冗长或用户不熟悉的表单任务拆分成多个步骤，一步步指导用户完成，分步表单的流程化明显，后一步填写的内容都是基于前一步来填写、是前一步反馈，分步表单可以缓解用户需要填写较多内容时候的抵触情绪，并且通过拆分步骤，聚焦于每次填写的内容，提升用户在不同模块间的浏览效率。</p>
<p><strong>高频问题三：</strong>这么多不同的组合，那么不同内容布局之间的区别？如何排列组合更合理呢？</p>
<p><strong>1）标签页和锚点定位的区别</strong></p>
<ol>
<li>标签页是切换不在一个页面，锚点定位在当前页面</li>
<li>标签页可以独立提交数据，各提交各的，互不影响</li>
</ol>
<p><strong>2）标签页和步骤条的区别</strong></p>
<p>步骤条更强调顺序，先填什么后填写什么。</p>
<p><strong>3）锚点定位和步骤条的区别</strong></p>
<p>锚点定位可以先填第4个再填第2个，锚点定位本质上是一个快速的目标传送门，只是告诉你这个表单很长，有一个传送门可以让你看到后面的表单节点，有点像鼠标的快速滚轮，让页面滚动的的快一点，而步骤条流程化明显，后一步填写的内容都是基于前一步来填写、是前一步反馈。</p>
<h2 id="toc-5"><strong>五、结语</strong></h2>
<p>春卷对B端表单设计的归纳与总结，把自己学到的经验分享出来，让大家有一个更清晰的认知，希望对从事B端工作或者对B端知识感兴趣的同学有些帮助。感谢阅读，欢迎交流～</p>
<p>本文由郝小七指导<a class="ne-link" href="http://www.woshipm.com/u/917803" target="_blank" rel="noopener">http://www.woshipm.com/u/917803</a></p>
<p>参考文献：</p>
<p>美芳Mia《体验设计手册》：<a class="ne-link" href="https://www.yuque.com/meifangmia" target="_blank" rel="noopener">https://www.yuque.com/meifangmia</a></p>
<p>https://www.yuque.com/weiweiyixiaohennaikan/lmzzoy/ggb9p7</p>
<p>https://mp.weixin.qq.com/s/eKLrUCsm2W12RORNdjqwUA</p>
<p> </p>
<p>本文由 @春卷设计笔记 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5419174" data-author="1063732" data-avatar="http://image.woshipm.com/wp-files/2022/04/lYyRaRP0h5aBDDQHgbtn.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            