
---
title: 'Messenger Group Redesign：缓解群组社交压力设计思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/oLdBL6y0faQTmWWZ9fwA.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 24 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/oLdBL6y0faQTmWWZ9fwA.jpg'
---

<div>   
<blockquote><p>编辑导语：Group（群组）是 Messenger 重要的产品特色，通过这个功能可以创建不同的群组，广受人们喜爱，但它也存在着一些问题。这篇文章分析了用户使用 Messenger Group（群组）的过程，以用户的视角开展设计思考，提出改进建议，感兴趣的小伙伴们快来看看吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5366766" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/oLdBL6y0faQTmWWZ9fwA.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>和大家分享笔者在 NTHU HCI 课程主导的一个 Slide Project。Project涉及的内容很多，节选两个我觉得很有意思的设计洞察分享给大家。</p>
<p>这个 Project 试图通过研究用户使用 Messenger Group（群组）的体验旅程，<strong>找到用户可能存在的社交压力点，并以用户的视角开展设计思考</strong>。</p>
<p>高度信息化的网络世界，让人们连接交流的门槛更低、粘性更高，形成自发自主的线上交流圈子。你应该有类似的经验，在微信或QQ会有各种家庭群、公司群、兴趣群、学习打卡群以及专业交流群等等。</p>
<p>当然，这些在台湾社会同样流行，选择 Messenger Group（群组）作为研究对象，藉由这个题目去了解台湾当地人的网络群组文化。</p>
<h2 id="toc-1">一、Messenger Group</h2>
<p>Messenger 最早在 2008 年，只是集成在 Facebook 的聊天功能“ Facebook Chat ”。Facebook 注意到 Chat 具备成为独特商业生态系统的潜力，经过2年多的改革和升级，于2011年8月正式推出Messenger。</p>
<p>在台湾社会民众日常使用的社交应用中，最受欢迎的基本都是外来品，本地出品的社交软件普遍市场接受程度不高，几乎没有诞生出有影响力的本地公司。</p>
<p>Twnic 2020发布调研报告指出在有使用社交App习惯的群体（n=1852）中，有94.2%的受访者使用 Facebook，排名第一。2019年在台湾，Messenger名列最受欢迎的iOS应用程式第二名，仅次于Facebook。</p>
<p>Group（群组）是 Messenger 重要的产品特色，你可以为你的家人、朋友、工作伙伴和同事创建不同的群组，广受大家的喜爱。</p>
<p>尽管如此，Group (群组)还是有许多不尽如人意的地方，比如，在 Facebook 上的任何人都可以在未经你同意的情况下，将你添加到群组中。当用户被添加到他们不关心的群组时，他们通常会感到沮丧。</p>
<p>下面来看看Messenger Group(群组)设计思考都发现了哪些东西吧。以下， Enjoy~</p>
<h2 id="toc-2">二、用户需求：收集与分析</h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/ra4Do1sivsGYYvqKg6jb.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="852" height="251" referrerpolicy="no-referrer"></p>
<h3>1. 用户访谈</h3>
<p>在开展设计工作之前，需要定好访谈大纲。经过讨论后，访谈以下面5个问题为基本提纲：</p>
<ol>
<li>了解他们是如何使用群组？</li>
<li>在使用过程中遇到过哪些记忆深刻的事情？</li>
<li>当时具体的情形是怎么样的？</li>
<li>最后是怎么解决的？</li>
<li>对用户产生的影响是什么？</li>
</ol>
<p>接着就发动号召，找到目标用户进行深度访谈，以下为本次访谈用户样本描述（n=5）。</p>
<ul>
<li>样本1 → 男性 | Age=25 | 研究生在读</li>
<li>样本2 → 女性 | Age=32 | 职场白领</li>
<li>样本3 → 女性 | Age=24 | 本科大四在读</li>
<li>样本4 → 男性 | Age=45 | 大学教授</li>
<li>样本5 → 男性 | Age=30 | 职场白领</li>
</ul>
<p>然后，与受访者敲定时间后，逐个进行。需要注意的是，在访谈过程中主要以大纲为框架，但遇到用户愿意多聊的内容，可以继续深入，多问几个为什么。最后把用户谈及的内容收集汇总，待下个步骤进行分析。</p>
<h3>2. 旅程梳理</h3>
<p>经过访谈后，收集到来自受访者反馈的各种信息。我们需要开展审查，找出受访者使用群组旅程中场景和使用感受，梳理用户旅程和脚本，并修正预设流程。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/0mXPy6HBCyQlcjhj0889.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="849" height="250" referrerpolicy="no-referrer"></p>
<p>在用户访谈过程中，群组的生命周期基本遵循“<strong>创建群组→使用群组→闲置群组→退出群组</strong>”的流程。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/0e3fbLmAd5cA7oE938Xa.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="851" height="327" referrerpolicy="no-referrer"></p>
<p>对于用户访谈反馈的内容，进行分类后总结以下 4 类典型的问题：</p>
<ol>
<li>用户在使用群组的过程中，<strong>群组信息太多太杂</strong>，不知道哪些需要关注，又害怕<strong>错过重要信息</strong>。</li>
<li>群组信息没办法分类，<strong>只想回复与我相关的消息</strong>。</li>
<li>用户在使用群组的过程中，积累了<strong>大量闲置群组</strong>，想要退出群组，但由于退出群组会自动广播，用户<strong>不想面对尴尬的场面</strong>。</li>
<li>大量闲置群组，想要能依据群组使用情况<strong>快速进行整理</strong>。</li>
</ol>
<h3><strong>3. 设计机会</strong></h3>
<p>拆解用户使用群组过程中的痛点需求，以及在心理层面造成的压力影响，有助于我们快速找到切入设计的机会点。</p>
<p>根据 SCQA 模型可以看出，用户在日常使用群组过程中面临的问题分别是：退出群组的困境和信息过载。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/T4aeWaDjP10RgvfiszUH.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="850" height="211" referrerpolicy="no-referrer"></p>
<p>针对这两个问题，以产品设计的视角可以理解为：</p>
<ul>
<li>如何使得用户可以在没有压力和后续烦恼的情况下，退出群组</li>
<li>如何能让用户在面对信息过载时，能够有效分类</li>
</ul>
<p>Okay，设计机会点找到了，那接下来就可以尝试通过还原场景，提出合适的设计方案。</p>
<h2 id="toc-3">三、用户故事：退出群组的烦恼</h2>
<h3>1. 故事板</h3>
<p>故事板在设计思考中是一个有效而且低代价的捕捉、关联、探索体验的方式。比起单调记录事实的文字，讲故事要让人好记 22 倍（Jerome Bruner）。</p>
<p>根据用户访谈资料，笔者绘制了“用户退出群组的烦恼”故事板：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/zdeVL0k8gJGky1wSB1WA.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="850" height="802" referrerpolicy="no-referrer"></p>
<p>用户A今天去参加一个家庭聚会，在聚会中一群亲戚拉了个群，方便大家在群组中讨论和分享资讯。一段时间后，群组的人不再活跃，群组成为某些成员发小广告的聚集地。<strong>用户A不想接收群组的广告信息，产生了退出群组的想法</strong>。</p>
<p>想到之前用户C退群后，群组自动发布公告经历。用户A不想面对尴尬的场面，无奈之下放弃了退群的想法。</p>
<p>为了让大家更好理解实际用户体验场景，制作了一个短视频（请移步公众号观看）。</p>
<p>视频大意是男主某天发现一个好几年前的家庭群组，亲戚最近一直在推小广告，萌生了想要退出群组的想法。但一想到退群后会被广播，妈妈就会过来念叨，不得已放弃了退出群组的想法。</p>
<h3>2. 设计洞察</h3>
<p>这个在台湾社会是一个典型的现象，社交网络圈子小，同地域、兴趣、专业……更容易产生社会性连结。</p>
<p>有网友甚至调侃说“<strong>不孝有三，退群为大！</strong>”对于各种养生谣言、鸡汤文、关于孝道的文章和营销小广告，以及不同文化差异带来的价值观不认同。在群组感到太尴尬，打算悄悄退出，却被Messenger群组的设计让你无法悄无声息不伤感情华丽地离开。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/pDDXyyJJRVZLIWrb1DqY.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="850" height="513" referrerpolicy="no-referrer"></p>
<p>另外，在故事板和短视频剧情可以看出用户从创建群组，到产生退出群组行为和心理的变化过程。用户通常会在“发生群组冲突”、“长时间闲置群组”或“积累大量闲置群组”后，产生退出群组的想法和行为。</p>
<h2 id="toc-4">四、设计理论：框架效应</h2>
<h3>1. 框架效应Framing Effect（Tverksy and Kahneman. 1981）</h3>
<p>原本群组默认是是要管理员手动操作才可以解散，另外成员退出群里还会自动公告，这造成了成员的极大困扰。</p>
<p>利用框架效应的作用调整群组的预设机制，创建的群组不再需要管理员，群组预设自动解散。<strong>对于特定的群组可以预设为“限时群组”，</strong><strong>到了设定的时限，群组可以自动解散，谁都不会有压力，这样一来有效避免了</strong><strong>社会责任的扩散和社会压力与多元文化的冲突。</strong></p>
<h2 id="toc-5">五、设计方案</h2>
<h3>1. Case 1：限时群组</h3>
<p>回到前面的用户故事，如果采用了“限时群组”的设计方案，会有哪些变化呢？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/8wlWnrZd3nE0u289HxUL.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="850" height="802" referrerpolicy="no-referrer"></p>
<p>用户A今天去参加一个家庭聚会，在聚会中一群亲戚拉了个群，方便大家在群组中讨论和分享资讯。</p>
<p>用户创建的群组默认是有时效的，根据实际情况设置群组的解散日期。大家在群组中讨论和分享资讯，聊得来的可以私下互加好友，到期群组自动解散。</p>
<p>在群组原型设计方案中，用户可以根据需要创建不同的群组，对于限时群组最大的特点，就是群组会在创建时便预先定好该群组的解散时间。<strong>设计上希望让用户对于阶段性的群组，可以免除长期管理的或闲置后变为无效群组的问题。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/f7U7PAO11TC8zbJdoGFT.png" alt width="851" height="329" referrerpolicy="no-referrer"></p>
<p>针对限时群组，会在Chat窗口显示解散倒计时，到设定时间后群组会自动解散。</p>
<p>考虑到群组类型的转变，默认设定为自动解散，但当你希望继续留在该群组的时候，你可以把该群组设置为一般群组，待倒计时结束后，同样设定为“一般群组”的成员，将会继续留在群组内。</p>
<h3>2. Case 2：批量退出群组</h3>
<p>对于有大量闲置群组的用户而言，批量退出会是一个省事省心的设定。在Chat提供新增群组设定入口，继承Messenger的设定。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/tmPnkHwiYhe2JgbkVale.png" alt width="851" height="329" referrerpolicy="no-referrer"></p>
<p>针对所有群组，会提供角色和筛选方式。</p>
<ul>
<li><strong>全部：</strong>展示所有群组</li>
<li><strong>管理员/成员：</strong>展示特定身份的群组</li>
<li><strong>按加入时间：</strong>会根据加入群组时刻进行排序</li>
<li><strong>按使用频率：</strong>则可根据最近使用近况进行统计排序</li>
</ul>
<p>设计目的是希望为使用者在群组管理提供判别群组有效度识别。根据筛选的结果，<strong>用户可以进行多个群组标记，并一次性退出。</strong></p>
<h2 id="toc-6">六、用户故事 2：信息过载</h2>
<h3>1. 故事板</h3>
<p>根据用户访谈资料，绘制关于“用户信息过载”故事版。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/IUe7CNRVzwCQgbhczwMu.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="850" height="1528" referrerpolicy="no-referrer"></p>
<p>临近期末报告时间，用户A提醒组员为下周的会议做准备。在与用户B和C的对话中，用户A在回复C的时候，却忘了还有B的问题没有处理。B多次@A，A向上滚动查看聊天记录，<strong>要反复回去找需要回复的消息，信息太多很难找到原来的问题</strong>。A在面对多人的交流很是烦躁，这让A、B陷入了不愉快的场面。</p>
<p>同样制作了一个短视频，大家看看实际用户体验场景（请移步公众号观看）。</p>
<p>视频是在使用群组的两个典型场景：</p>
<ol>
<li><strong>片段一：</strong>男主在使用群组过程中，被多个朋友@，需要一条一条消息往上翻，费时费力。</li>
<li><strong>片段二：</strong>男主在使用群组过程中，遭遇信息过载，不知道应该关注哪些消息，哪些又和他有关，男主感觉到有些焦虑。</li>
</ol>
<h3>2. 设计洞察</h3>
<p>在工作和生活中，我个人有事会看到群组消息，但手上有别的事情在处理，一时间会误以为已经回复了，然后就没了这件事。虽然不是有意为之，但也给其他人造成了不少的麻烦。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/PhtinamgfyZC3oX4S8w4.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="849" height="514" referrerpolicy="no-referrer"></p>
<p>在使用群组过程中，常见的问题“消息太多，无法及时回复”、“容易落下和我相关且重要的消息”，还有就是“每次回复，需要上滑去找到查找”。</p>
<h2 id="toc-7">七、设计理论：待办事项心理学</h2>
<h3>1. 待办事项心理学（Bluma Zeigarnik 俄罗斯心理学家）</h3>
<p>找出需要完成的任务和顺序，写下它们，然后一个接一个地划掉它们。这可以让我们在面对生活和工作事，减轻对混乱的焦虑。</p>
<p>效能专家大卫-艾伦表示，将待办事项写在索引卡上是迄今为止最理想的自我组织方式。待办事项的机制，可以在群组聊天过程中，将待办事项和提醒事项在群组标记和收集下来，能够赋予大脑内“复述环路”隐性和显性权限，让大脑暂时忽视这些东西。</p>
<p><strong>只标记我关注的和与我有关的，给了用户一个结构、一个计划、一个回应策略，可以更加轻松地面对海量的信息。</strong>这样，用户便可将注意力集中在其他东西上。</p>
<p>除此之外，这些待办也证明了用户在群组对话中某天、某一周或某个月所取得的成就。</p>
<h2 id="toc-8">八、设计方案</h2>
<h3>1. Case 3：群组待办</h3>
<p>对于有大量信息处理能够为用户提供暂存的能力，对于用户来说是非常实用的。为了避免无序和混乱，浮窗功能只会在特定的群组出现。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/hQdRtOOyvS8cpOL7Q9h6.png" alt width="900" height="348" referrerpolicy="no-referrer"></p>
<p>关于待办收集，会提供两种方式对消息进行标记：</p>
<ol>
<li>长按文字，然后点击收集按钮</li>
<li>长按消息，然后右滑收集到待办</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/I6M0oDmxkEl6wCmDfatB.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="897" height="225" referrerpolicy="no-referrer"></p>
<p>浮窗功能只会在特定的群组出现，群组浮窗可以通过点击浮窗控件查看（唤起），或者左滑呼出隐藏在右侧的页面。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/7IbQgHDIdg4YxJccB36A.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="909" height="228" referrerpolicy="no-referrer"></p>
<p>将消息标记到待办事项列表，无论是哪种类型的消息（文本、图片、视频、网址等）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/HXVNuyRBEcIEMYC2CD6d.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="885" height="181" referrerpolicy="no-referrer"></p>
<p>对于群组中被收集到待办的聊天内容，用户可以直接点击某天信息，直接定位到该信息的位置，方便用户结合聊天内容上下文，做出回复。</p>
<p>改善回复体验，快速定位消息位置，用户不必频繁上下滚动。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="Messenger Group Redesign - 缓解群组社交压力设计思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/aESuGtlJfFYy4xgaFWlt.png" alt="Messenger Group Redesign - 缓解群组社交压力设计思考" width="899" height="279" referrerpolicy="no-referrer"></p>
<p>可快速查看全部待办和只看@我的，回复消息自动@发布者，已回复后自动清空待办。</p>
<h2 id="toc-9">九、总结</h2>
<p>本文介绍内容主要围绕用户在使用前、中、后的社交压力进行设计思考，目的是希望通过重新设计Messenger群组，缓解用户在群组社交中的压力感。</p>
<p><strong>设计思考于笔者的理解，是用批判的眼光来进行审视。找寻用户会在哪里犯错？可以在哪些方面减少用户的工作？哪里感觉与现实不符？</strong></p>
<p>只要你深入了解，一定会发现很多现实面的冲突，这些都是设计可以介入，可以改进的部分。</p>
<p>在这个过程中使用到了很多设计方法和工具，比如用户访谈、SCQA、故事板、视频、流程图等等，灵活组合可以让用户体验旅程鲜活起来<strong>，把设计者带到用户的生活中，能够站在用户的立场上去审视自己的设计，帮助设计者理解已知的场景，同时也能验证对潜在场景的假设。</strong></p>
<p>篇幅有限，很多Project的细节无法一一展示，抛砖引玉，如果你也有同样的题目，欢迎一起交流探讨。</p>
<p>最后，与压力共存，快乐生活，快乐工作。</p>
<h3>参考资料</h3>
<p>[1] Messenger 数据大事纪-facebook.com</p>
<p>[2] Saving Product X – A Design Thinking Case Study-toptal.com</p>
<p>[3] 服务应用概况-2020台湾网络报告-twnic.tw</p>
<p>[4] 如何在 Facebook Messenger 中退出群聊-a7la-home.com</p>
<p>[5] 待办事项心理学-zditect.com</p>
<p>[6] 创新不是无中生有，要创造人人都爱的产品/服务，就从设计思考开始-cw.com.tw</p>
<p>[7] Tversky, A., & Kahneman, D. (1981). The Framing of Decisions and the Psychology of Choice. Science, 211(4481), 453-458</p>
<p>[8] David Allen 《尽管去做——无压力工作的艺术》, 2001</p>
<p>[9] 专注在对你重要的事项-slack.com</p>
<p>[10] Make Your Story 22 Times More Memorable-marketingprofs.com</p>
<h3>#专栏作家#</h3>
<p>龙国富，公众号：龙国富，人人都是产品经理专栏作家，人因工程硕士。致力于终身学习和自我提升，分享用户研究、客户体验、服务科学等领域资讯，观点和个人见解。</p>
<p>本文原创发布于人人都是产品经理，未经授权，禁止转载</p>
<p>题图来自Pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5364044" data-author="100850" data-avatar="http://image.woshipm.com/wp-files/2021/05/WBiO9KeJKiEALvtJhClA.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            