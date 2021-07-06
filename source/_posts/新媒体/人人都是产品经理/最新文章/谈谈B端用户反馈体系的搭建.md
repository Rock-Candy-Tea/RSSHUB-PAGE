
---
title: '谈谈B端用户反馈体系的搭建'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5CLkTT6KkP5TNQPiCLcR.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 06 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5CLkTT6KkP5TNQPiCLcR.jpg'
---

<div>   
<blockquote><p>导读：在实际的产品使用体验中，用户和系统时刻通过界面的交互操作和视觉呈现在保持交流。而作为系统背后的产品设计者，如何和用户保持有效的双向反馈，以及如何对用户的反馈做一个体系化的回应。本文将从六个方面，对此进行深入分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4825066 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5CLkTT6KkP5TNQPiCLcR.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>这是关于B端产品设计体系化设计的第二篇文章</p>
<p>全文同样约9000字，阅读大约需要20分钟</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pH6JGWbmytzmAeRDEcOw.png" referrerpolicy="no-referrer"></p>
<p><strong>阅读前须知：</strong></p>
<p>1. 文章有点偏学术性的设计课题研究范畴，所以可能读起来可能会有一点晦涩。</p>
<p>2. 关于这个设计课题（B端产品的用户反馈体系搭建），文章内容主要源于企业内部一次项目级别的用户调研相关设计课题研究，尝试将相关分散的设计点进行体系化和结构化。</p>
<p>3. 宏观意义上反馈体系也是一个很大的设计命题，毕竟<strong>当用户在产品中进行一些业务性操作时，时刻在和系统进行双向的反馈以此形成一个沟通闭环</strong>，同样此文的核心论点“B端用户反馈体系”进行了必要的约束和取舍，侧重在双方明确产生反馈的机制上。</p>
<p>4. 文章中涉及的一些点单拎出来可能就可以写独立的文章，所以有一些点可能涉及并不深，看后期有没有机会再补充深入。</p>
<p>5. <strong>B端用户反馈体系的用户研究部分，本身关于专业的用户研究技术，水很深，作为设计师其实并不用追求极致的专业性，能够将广义上的用户研究思维整合到产品设计过程中即可</strong>，当然有些点单拎出来还是能写独立的文章。</p>
<p>6. 不同于上一篇文章，B端用户帮助体系的搭建，对于B端用户反馈体系而言，其采用的设计手段会和C端差异性较大，以及最终反馈的信息维度相比C端会少一些，但背后的设计模式大致形似。</p>
<p>7. 文章肯定存在不足和没有考虑到的地方，很欢迎指正出来，同时有兴趣的小伙伴可以一起讨论这个设计课题。</p>
<p>8. 最后希望对有缘看到这篇文章的盆友了解这方面的产品设计知识有一定启发和帮助意义。</p>
<p>9.如果你有兴趣进行转载，请直接添加作者WeChat</p>
<p>对于B端产品，闭门造车是比较可怕的事情，直接拍脑袋和屁股决定脑袋的做法在竞品都大同小异的B端市场中都会让产品难以生存下来。</p>
<p>在实际的产品使用体验中，用户和系统时刻通过界面的交互操作和视觉呈现在保持交流，<strong>而作为系统背后的产品设计者，如何和用户保持有效的双向反馈，以及如何对用户的反馈做一个体系化的回应</strong>，是这篇文章想要讨论的重点。</p>
<h2 id="toc-1">01 文章结构</h2>
<p>文章结构按照以下结构【<strong>收集用户反馈的方式 -B端用户&平台反馈体系 -平台内用户反馈机制 -反馈用户的设计形式 -平台外用户反馈机制</strong>】详细说明。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DOlfdpVC9zV6QoDMBwah.png" referrerpolicy="no-referrer"></p>
<p>先明确一下：</p>
<p><strong>反馈的前提是沟通，而沟通是一个双向的过程，为了通过沟通拿到有效的反馈，产品设计者的核心发力点需要在两个方面，如何收集用户反馈，以及如何对用户的反馈做出及时回应，如何通过有效的设计手段让使用者-设计者形成一个机制闭环，并且有动力让这个机制持续运行下去</strong>，文章立足这几点，从产品设计的角度出发，探讨如何体系化搭建出一个B端产品的用户（和设计者的）互相反馈的机制，间接解决如何有效衡量设计改动带来的产品和用户影响这一问题。</p>
<p><strong>如果你作为设计师，自诩要对用户在产品使用上的体验负责，收集用户对于产品体验的反馈且主动去优化体验是设计师有责任去做的事情。</strong></p>
<p>面向用户的产品并不是一个自嗨的系统，只有用户投入参与到其中并将使用体验反馈给产品设计者，同时产品设计者依靠用户的反馈不断完善产品，才能体现出产品设计的价值。</p>
<p><strong>用户反馈体系的搭建可以理解为运用利益相关者共同参与的共建模式，寻求用户以及一切和产品相关人员的参与度，让产品在批评声和表扬声中健康成长。</strong></p>
<p>现在越来越讲究设计的量化标准，不管是过程导向还是结果导向，设计方案的复盘落在商业层面其实就是一些可具体量化的用户行为数据指标的跟踪，B端用户反馈体系搭建的目的也是尝试通过较为完整的闭环来衡量整个产品的可用性和易用性。</p>
<p>按照分类的第一个维度，B端产品的用户反馈体系可以分成实时反馈和非实时反馈两种。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/y856zk6L7YIapaIAMGAY.png" referrerpolicy="no-referrer"></p>
<p>实时反馈一般涉及到用户帮助体系中的客服支持系统，采用一问一答的形式（对话式）来获取和帮助解决用户遇到的问题，通常此类沟通形式大部分时间会花在处理用户的琐碎性需求层面，难以沉淀出可落地到产品功能层的用户需求。</p>
<p>非实时反馈一般会存在明显的时间差，通常在产品层面体现出来的设计形式是作为桥梁连接的作用，以接收用户侧的反馈为主，产品设计者侧的反馈通常会在信息过滤和优先级排序后给到用户侧，此类反馈模式对于系统性收集用户侧需求并提炼出更优解决方案的参考意义更大，非实时反馈的设计模式也是此篇文章讨论的重点。</p>
<h2 id="toc-2">02 收集用户反馈的方式</h2>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/yhpIsN5w2tDHNsiuW4HZ.png" referrerpolicy="no-referrer"></p>
<p>对于B端产品而言，收集用户反馈的方式一般分成两种：</p>
<ul>
<li><strong>平台内用户反馈机制</strong>，包括用户主动和平台主动</li>
<li><strong>平台外用户反馈机制</strong>，包括社交平台反馈收集（如知乎、微博、公众号、贴吧、论坛等收集用户评论和用户吐槽类信息）、第三方数据监测（现在比较主流的比如友盟、神策等，或者是内部自研的数据监测工具）、用户调研手段（常规也是最有效的如用户访谈、可用性测试、用户观察等）</li>
</ul>
<p><strong>这两种形式是B端用户沟通体系的核心组成部分，前者广泛收集现象，后者针对性寻找原因，从现象（How）到原因（Why）相辅相成。</strong></p>
<h2 id="toc-3">03 B端用户&平台反馈体系</h2>
<p>用户通过平台内的用户反馈机制将感受和建议传递给平台，同时平台及时做好伪反馈机制，经由平台收集后经过产品设计者的处理，再通过平台将处理结果传递给用户（真反馈机制），为进行深度用户反馈的收集，产品设计者通过平台外的用户反馈机制进行用户研究，经过整理分析后，将处理结果通过平台或第三方工具传达给用户。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/GKRbmHdq6dXMWtViFx4D.png" referrerpolicy="no-referrer"></p>
<p>对于设计师而言，针对用户反馈体系的搭建，<strong>经过验证比较理想的设计研究过程如下</strong>：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/KUP1LOgUEZZA3xlpJC7J.png" referrerpolicy="no-referrer"></p>
<p>第一步，<strong>首先需要确定想要收集的反馈，即研究目标是什么</strong>，是需要通过用户反馈验证设计方案的合理性、定期的用户满意度调查、弥补性的问题解决调研，还是前瞻性的问题挖掘等。</p>
<p>第二步，<strong>搭建一个合适的用户反馈机制，即研究手段是什么</strong>，是采用平台内用户反馈机制，平台外用户反馈机制，还是两者结合使用。需要注意的是，在整个设计研究过程中，用户反馈机制并不是一成不变的，可以随着整个研究的进行做适应化调整。</p>
<p>第三步，进行反馈收集阶段，即研究执行。</p>
<p>第四步，有了用户反馈的数据后，对数据进行整理分类和过滤分析，筛选出对产品功能的体验改进有参考意义的信息。</p>
<p>第五步，<strong>将已有的反馈范围和最初研究目标所定的范围做对比，考虑是否补充新的沟通形式来对已有用户的反馈进行深入</strong>，直到拿到自己想要甚至超出原定预期的调查结果。</p>
<h2 id="toc-4">04 平台内用户反馈机制</h2>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pYeLRfTZLIgjKJVIqrFi.png" referrerpolicy="no-referrer"></p>
<p><strong>平台内用户主动触发的反馈机制：</strong></p>
<p>用户主动触发的反馈机制会在用户使用产品的整体过程中持续存在，通常表现为一个不会干扰用户当前业务流程的常驻性小入口。通常此类机制需要搭配一套比较成熟的用户激励机制去实现，不然很难驱动用户进行自发的反馈。</p>
<p><strong>平台内系统主动启动的反馈机制：</strong></p>
<p><strong>平台主动启动的反馈机制通常会带着产品设计者的目标去主动接近用户</strong>，在用户功能生命周期的各个阶段去获取用户的及时反馈，一般背后会有一个比较完善的前期设计研究策略（细分用户群体及用户行为）作为支持，这类反馈机制由平台依据已设定的后台判断来启动，一旦启动后，用户的行为流程会有被打断的风险，因此反应在前端的设计形式应该包括忽略、删除的可选项。</p>
<p><strong>用户对产品的瞬时态度是转瞬即逝的，平台主动启动的反馈机制的适度应用（包括合适的场景、合适的时机、合适的设计形式）能够很好的表达出平台想要解决用户问题的态度，同时通过用户反馈 – 发现问题 – 排查问题 – 解决问题 – 平台反馈的良性闭环来达成用户和产品设计者之间的有效沟通。</strong></p>
<p>当然这两者有效运行的核心也需要产品设计者提供引导和鼓励用户进行反馈的设计模式。</p>
<p><strong>平台内系统主动启动的反馈机制：</strong></p>
<p><strong>和C端产品有差异，B端产品引入平台内的系统自发启动的用户反馈机制是可以直接获取到终端用户实时态度和情感的唯一途径。</strong></p>
<p>大部分B端产品都是管理性质的平台型系统，而管理恰恰就是反自然和反人性的，如何直接获取到用户使用产品时的“情绪快照”就是B端设计师需要始终关注的了，通过常规用研手段中的如用户访谈、用户调查的手段实际上并不能很好奏效。</p>
<p>平台内反馈收集的场景实际上伴随着整个用户功能生命周期，也就是说大概率都是当用户处在一些有着明确用户目标的工作流程中时，平台会要求用户提供一些反馈，过程被打断或多或少产生负面情绪是不可避免的，如何让用户保持相对积极的产品体验并且提供一些符合事实的反馈也是产品体验设计师需要思考的事情。</p>
<p><strong>平台内反馈机制的使用场景可以针对特定功能、特定流程、特定用户或整体产品评价</strong>，如针对新功能的初次体验反馈、已有功能的整体使用体验反馈等，又如针对首次使用此功能的用户，针对已经使用此产品三个月的用户等，具体场景的应用可以结合前期的研究目标，具体想要获取的用户数据范围是如何的。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/RIAhCvgyr2hgfcZRgJ16.png" referrerpolicy="no-referrer"></p>
<p><strong>平台内反馈机制的具体设计形式：</strong></p>
<p>针对平台内反馈机制的搭建，设计形式具体表现为UI层面各种用户反馈类组件的单独或者组合使用。</p>
<p><strong>常见的形式有：选择型：二元选择式、等级量表式（评分），多选问题式，输入型：富文本式、多信息载体式，授权型：同意说明式。</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Kb7gyZwRrOeVXdgV6Pom.png" referrerpolicy="no-referrer"></p>
<p><strong>选择型反馈：</strong></p>
<p><strong>说明：选择型反馈形式由系统实现安排若干选项供用户选择，通常出现在一个功能使用或操作流程的最后节点或者使用结束之后</strong></p>
<p><strong>二元选择式：</strong></p>
<p>是最简单的定性用户评价形式，提供二元化的选择（通常为积极情绪和消极情绪两种对立的选项），就像投票一样，赞同或反对可以直接表达出用户在当时场景中的体验情绪。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/iv37WFhIHqAiOWvhaC9K.png" referrerpolicy="no-referrer"></p>
<p><strong>等级量表式：</strong></p>
<p>一般采用星级评分的展示形式，或者为了突出产品和用户之间的情感化联系，可以采用更加图形化的展示形式，比如emoji的引入或者结合IP形象的展示形式。或者采用简单粗暴且更具数字灵活性的纯数字评级形式。</p>
<p>这里需要注意的一点是，反馈机制中的等级量表评分形式和NPS（净推荐值）有差别，前者一般从非零的数字开始，而NPS则会包括0这个选项。</p>
<p>当你需要获知用户在产品使用体验上关于满意度、易用性、好感度、流畅性、帮助性等可以衡量产品性能的指标，可以采用等级量表这种设计形式。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xV1dNoEAafqqUtwydYSB.png" referrerpolicy="no-referrer"></p>
<p><strong>多选问题式：</strong></p>
<p>系统预先提供了一套可供用户自由选择的问题列表，用户根据实际遇到的问题来进行选择，问题需要立足用户的当前用户流程和功能操作，同时不要提供太多的选项。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7w445RsDAyPVC74E4cEN.png" referrerpolicy="no-referrer"></p>
<p><strong>输入型反馈：</strong></p>
<p><strong>说明：输入型反馈形式需要由用户主动去输入信息，通常出现一个功能流程明确结束之后</strong></p>
<p><strong>富文本式：</strong></p>
<p>因为需要用户主动去输入一些当前情境下遇到问题的详细信息，所以这种反馈形式对于用户来说会具有一定挑战性，当然可以尝试结合一些视觉层面用户激励的形式。（如引导性的视觉化表现型形式）</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/nBifz3AyoQW1iPncDW0d.png" referrerpolicy="no-referrer"></p>
<p><strong>多信息载体式：</strong></p>
<p>也可以成为视觉化的反馈形式，通过截图、视频等更直观的多媒体形式来反映用户在产品使用体验中遇到的问题，通常此类反馈对于bug类、系统类错误的改进以及界面布局的优化有很大帮助。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/0tUZl2WtVfhd8hLlvqLL.png" referrerpolicy="no-referrer"></p>
<p><strong>授权型反馈：</strong></p>
<p><strong>说明：授权型反馈形式通常会涉及到用户数据和用户隐私相关的信息展示，通常会出现在用户首次进入特定的功能界面或者常驻在系统配置中。</strong></p>
<p><strong>同意说明式：</strong></p>
<p>授权同意说明式需要将涉及到系统和用户之间的数据交互及权责说明进行详细的解释，让用户自己选择是否参与到系统体验改进计划中，让用户清楚自己的反馈（自己主动反馈的以及系统主动收集的）会被用来做什么。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/kNwDMytJVvXUNbtSJWY3.png" referrerpolicy="no-referrer"></p>
<p><strong>平台内反馈机制的通用设计模式：</strong></p>
<p><strong>结合具体使用场景，从组件拓展到设计模式，下面讲讲几种具体设计模式的应用。</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/eLSjukOToWGUpHYZkgeE.png" referrerpolicy="no-referrer"></p>
<p><strong>针对性反馈：</strong></p>
<p>希望针对性的对特定功能或特定流程收集用户反馈，通常可以采用模块内嵌形式。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/UnTFSyOVf6rEYDdwAM0D.png" referrerpolicy="no-referrer"></p>
<p>其主要目的是为了获取用户和某一特定功能发生交互后的瞬时态度，此类用户反馈的设计模式需要出现此功能模块的相临近区域（同时布局通常采用卡片式模块布局形式），比较常见的是调查目前页面提供的信息是否对用户在此区域的行为目标有帮助，一旦用户已经完成了平台希望采集到的用户反馈，可以立马关闭当前反馈机制，平台也应该及时传递出感谢用户的消息。</p>
<p><strong>整体性反馈：</strong></p>
<p>希望对产品某一整体功能或流程的体验收集用户反馈，通常可以采用三种形式：侧边面板形式、全局弹窗形式、新建页面形式。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lDkFVFbhGou6iJYEp6RO.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/7GiiuURrVxqs7bh10YQh.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/li0ir7xW7J1ihvtwABxF.png" referrerpolicy="no-referrer"></p>
<p>其主要目的是为了获取用户关于已完结功能流程的整体态度和感受，提供一个可供用户自由表达意见的入口，此类用户反馈的设计模式会出现在流程完结后的当前页面中，一般会提供比较详细的关于用户体验的问题列表，同时一旦用户完成了反馈，可以立即关闭此反馈机制，平台也及时传达出感谢用户或激励用户的消息。</p>
<p><strong>综合性反馈：</strong></p>
<p>希望从用户侧收集到关于他们对产品的综合性评价（如NPS），其设计模式同样可以采用：侧边面板形式、全局弹窗形式、新建页面形式</p>
<p>其目的是为了获取用户对平台提供服务的综合性态度，通常会是一个综合的问题评分表，同时会通过视觉化的设计形式将用户的注意力吸引过来，所以需要注意的是，此类设计模式通常需要出现在明确完结的流程之后，确保用户已经离开了上一个任务流程。需要用户反馈的内容详细程度决定于设计者想要获取的信息颗粒度。</p>
<p><strong>当然以上三种模式由于都是平台端启动的用户反馈机制，对用户的正常使用流程必定会存在一定的干扰性，所以要针对一些具有高设计研究价值（高重要性和高影响性）的功能/模块/流程进行安置，同时要选择合适的时机，通常为用户完成一项任务后或最后的任务节点，或预测再次开启此流程的起点。</strong></p>
<p><strong>如何搭建一个有效的平台内用户反馈机制？</strong></p>
<p><strong>从设计目标出发，选择合适的用户反馈组件，用合适的设计模式进行展示，同时具体的反馈内容需要背后需要有一套考虑周全的设计策略作为支撑。比如用户群体的划分策略、内容撰写的策略、收集周期的策略等</strong>。（因此处定义的设计策略实际上已经涉及到具体的细节设计方面，先按下不表）</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/jyq36BuAPvR26Lrmodmq.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">05 反馈用户的设计形式</h2>
<p><strong>平台内收集到用户反馈后，通过整理、归类、过滤等一系列操作，通常得到的是一些偏评价式的现象描述，这个时候就需要通过平台外的用户反馈机制来挖掘现象背后的原因了。</strong></p>
<p>同时对于部分可以直接定性的结论，通过一些沟通途径向用户侧反向反馈，平台内反馈用户或者平台外反馈用户，其目的就是为了增加用户的产品参与感，同时鼓励用户再次反馈，打造一个健康可持续的用户 – 平台沟通闭环。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/tInwMWcGyj6b9Lj7G95M.png" referrerpolicy="no-referrer"></p>
<p><strong>平台内反馈用户：</strong></p>
<p>平台内反馈用户，在用户使用产品的时候告知感谢用户的参与和反馈。</p>
<p>通常的形式，可以采用比如内置的邮件系统、消息通知系统等，作为用户沟通体系的分支系统 – 平台内消息通知系统的搭建为达到较好的体验效果，通常需要配备一个比较完善的设计策略，即反馈强度和提醒分级的合理设置。（具体会在另外的系列文章说明）。</p>
<p>同时涉及到伪反馈机制和真反馈机制的设置，前者会通过通用性的设计模式及时通知到用户，感谢用户的反馈，后者一般存在时间差，会结合具体的反馈对用户表示反馈及传递给用户其产品后续行为。</p>
<p><strong>平台外反馈用户：</strong></p>
<p>平台外反馈用户，通过沟通渠道对用户表示感谢，比如通过邮件形式、短信通知形式、电话访问形式等</p>
<p>当然如果产品是对外的SaaS化平台，为了表示产品设计团队对用户反馈的重视，甚至可以在产品内或官网上开辟一个专门的用户反馈板块，让用户更强烈的感知到自己在共建产品层面的参与感。</p>
<p><strong>通过平台内的用户反馈，可以收集到用户对当前产品现象的态度和情感类反馈，但这些数据会是比较粗颗粒度的，如果需要更深层次的挖掘这些现象背后的原因，B端用户沟通体系中的大头，搭建出一个平台外的用户调研机制并确保有效运行就起到非常关键的作用了。</strong></p>
<h2 id="toc-6">06 平台外用户反馈机制</h2>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/fds4glVLcnLWMJkClM1Z.png" referrerpolicy="no-referrer"></p>
<p>下面重点讲讲平台外的用户反馈，即常规意义上B端的用户调研手段，这些用户调研手段就像是深度的用户反馈机制，对于B端产品而言，调研通常是带着明确的目的，产品体验存在问题想改进，产品体验还可以想挖掘新的机会点，诸如此类。尤其是对于中大型的B端复杂业务系统，分功能模块和分支流程的调研很常见。</p>
<p><strong>和C端丰富的调研手段相比，在实际企业环境中，最适合B端产品的设计调研手段实际上重点在几种定性研究手段上：用户访谈和可用性测试，情境调查（情境式观察和交流），当然不局限，你也可以通过一些辅助的定量用户研究手段来进行一些结果验证性的调查。</strong></p>
<p><strong>设计师发起的用户调研：</strong></p>
<p>由设计师发起的用户调研和产品发起的用户调研虽然存在一定的差异，但核心点都是为了指导产品设计的过程，设计师和用户的直接交流，可以得到更丰富的一手数据，而不是一些被加工过的二手甚至三手数据。</p>
<p>对于B端设计师来说，用户研究的流程和传统非敏捷向的设计流程是比较类似的：</p>
<p>B端用户研究的流程可以概括成如下：</p>
<p><strong>研究目的 → 选择合适的用研手段 → 执行研究 → 信息汇总寻找解决方案 → 报告输出 → 陈述结果 → 选择方案并落地</strong></p>
<p>B端产品设计（设计师侧）的流程同样可以概括成如下：</p>
<p><strong>设计目标 → 选择合适的设计手段 → 设计表现执行 → 多方案比较寻找最优解 → 设计输出 → 方案展示及评审 → 优化方案并落地</strong></p>
<p><strong>如何做B端用户调研：</strong></p>
<p>总结成四点：<strong>听TA说了什么，TA是怎么想的，看TA做了什么，TA的感受如何。</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rNyIuZGm5dbm9uVpsvJd.png" referrerpolicy="no-referrer"></p>
<p>TA是怎么想和TA的感受如何，这两点可以通过平台内用户反馈机制来重点收集，用户对产品的转瞬即逝的情绪和情感是最有价值的，直接感受比事后回忆更具参考价值。</p>
<p>以之前一次比较完整的B端用户调研的实践（企业项目级别）为例说明整个流程：</p>
<p><strong>提纲设计 – 访谈规划 -预访谈 – 提纲确定 – 访谈执行 – 补充访谈 – 问卷补充验证 – 输出报告 – 信息同步 – 落地执行 – 跟踪反馈。</strong></p>
<p><strong>反馈收集：</strong></p>
<p>通过前面这么一套用户调研流程的推动，依据实际执行的经验，一般可以发现两类问题：第一类为老问题（VoC），另一类为新问题。</p>
<p>补充说明一下VoC的概念（Voice of Customer即客户之声），VoC在推动B端产品的小步快速迭代优化方面起着非常重要的作用，有些SaaS产品会配置专门的客服服务部门来跟踪用户对产品的实时体验反馈以及解决客户问题。</p>
<p><strong>对于B端用户来说，其行动动机通常会由两部分组成：</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/1yS12DYzFGHHB02aTgVD.png" referrerpolicy="no-referrer"></p>
<p>第一部分为所在组织的运作目标，关系到整个组织的构架、业务部门的具体运作形式（通俗的讲所处业务部门是如何获取商业利益的）、组织中各个角色和个体是如何进行和配合协同办公的、以及组织的业务目标和拆分到个人上的目标等。第二部分为角色的工作心理模型（指在被管理环境下角色的心理模型），关系到角色的工作目标、具体工作流程、日常工作模块，以及背负的KPI等。</p>
<p><strong>而从产品设计者的角度出发，需要将多角色的业务流程抽象化再组织，考虑角色在系统中的信息流转是怎样的，业务反映在产品界面上的关键决策点应该在哪里，为了达成用户目标，系统应该给用户提供哪些有效且关键的信息？</strong></p>
<p>以上都可以作为B端用户交流体系中确定想要收集的用户反馈阶段的基础内容框架。</p>
<p>ps：关于用户调研的详细介绍会是一个比较的设计命题，由于此篇文章的重点还是关于B端用户沟通体系的搭建，先不涉及更详细的用户调研技术的说明，当然由于用研落地实践的方法论其实大同小异，有兴趣的小伙伴可以自行查阅相关资料。对于平台外用户反馈机制的运行，实操比理论重要的多，甚至并不具备一些用户的专业知识去直接进行调研得到的结果也不会太差，迈开腿去行动是第一步也是最重要的。</p>
<p><strong>反馈分析：</strong></p>
<p>通过各种用研技术拿到了用户的一手反馈数据后，通过各种数据整理归类、过滤处理之后，通常数据处理的标准是依据反馈的合理性进行优先级排序，合理性可以由以下几个方面来评估：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/durqoEnbLiImgi76TU7T.png" referrerpolicy="no-referrer"></p>
<p><strong>实际场景中问题出现的范围</strong>，即同问题反馈的用户数量以及问题的复现概率。</p>
<p><strong>业务使用中用户情绪的范围</strong>，即在实际产品使用中，用户的感受和情绪是怎样的，这里可以结合平台内的用户反馈机制收集的一些有效用户数据。</p>
<p><strong>产品功能组织上出现的范围</strong>，即问题出现对平台的影响，是仅针对功能、模块、还是流程，是针对视觉展示层面、交互流程方面、系统性能层面、还是业务逻辑层面。</p>
<p><strong>团队成员中涉及的范围</strong>，即问题解决的实现难度和实现价值如何。</p>
<p>通过以上三个方面对用户的反馈进行全方位的评估，同时后续依照优先级推动问题的解决。</p>
<p>PS：这个环节的重点是对用户反馈的管理，其实不仅仅针对产品本身，设计师自身设计流程中的用户反馈管理同样可以包含在其中，比如在设计原型评审阶段，团队内外成员以及各种利益相关者的参考意见管理方面。</p>
<p><strong>面向用户的反馈形式：</strong></p>
<p>到这一步，基本上产品设计者针对平台的用户反馈收集和整理完成了，对于整个用户反馈体系而言，用户侧面向产品设计者的反馈完成了，为了确保这个体系能够持续的运行，产品设计者面向用户的反馈同样不可忽视。</p>
<p><strong>记住此文定义的反馈是是用户和平台双向的互动，通过各种手段（平台内反馈机制 + 平台外反馈机制）收集到用户反馈后，如何对后续任务的流转过程和问题解决排期的透明化公布、沟通渠道的维护和开放，以及产品设计者的后续持续跟踪，是打造整个B端产品用户反馈体系闭环化的关键。</strong></p>
<p>及时将关键节点的信息通过各种途径透露并传达给用户，保证用户在产品共建过程中的参与感。一般而言，流转到用户调研的需反馈用户的信息通过平台外反馈用户的设计模式会比较常见，通过比较正式的沟通途径，比如邮件沟通、短信通知、电话沟通等，其目的都是为了让用户有持续进行反馈的动力。</p>
<h2 id="toc-7">07 总结一下下</h2>
<p>B端产品的用户反馈体系可以通过搭建平台内反馈机制和平台外反馈机制结合的方式进行串联和整合。通过平台自发启动的反馈机制收集粗颗粒度的用户反馈，然后补充用户调研的手段来挖掘细颗粒度反馈，将反馈转化为有效的真实需求，同时通过及时反馈用户的方式确保整个机制能够形成闭环，并可持续性的运行。</p>
<p><strong>反馈的前提是沟通，沟通始终是双向的，搭建一个具备及时性和完整性的反馈互动环境，确保用户 – 平台 – 设计者这三方能够顺畅的交流并进行及时反馈。</strong></p>
<p><strong>记住，去调查用户的真实产品使用体验，收集用户的反馈并对用户的反馈做出及时回应是确保产品体验能够正向升级的唯一途径。</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xUHrx9gS5db2gGFLacWy.png" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>本文由 @稻草小八 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4819946" data-author="749450" data-avatar="http://image.woshipm.com/wp-files/2021/06/04QSQwxsfrXXHrakqLbL.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            