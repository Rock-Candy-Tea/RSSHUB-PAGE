
---
title: '智能客服的优化建议 _ AI产品经理需要了解的智能对话知识'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OKzqTN1jKrngwqDjPT5w.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 10 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OKzqTN1jKrngwqDjPT5w.jpg'
---

<div>   
<blockquote><p>编辑导语：如今随着科技的不断发展，人工智能渐渐的深入我们的工作和生活，比如现在很多平台都会使用智能客服进行工作，可以引导用户进行操作以及解决一些固定问题；本文作者分享了关于智能客服优化的建议，我们一起来了解一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4453703" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/OKzqTN1jKrngwqDjPT5w.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>人工智能领域，2020年迎来了NLP落地场景智能客服的崛起。不同场景和业务的应用要求智能对话更拟人、更懂客户。</p>
<p>本文以京东智能客服「开发票业务」从语音和图形两种产品形态，对智能对话的优化提出小小建议。</p>
<h2 id="toc-1">一、智能对话中语音交互和图形交互的区别</h2>
<p>1）对话的引导项不同</p>
<p>语音交互的引导回复话术最多给出2-3个选择。图形交互的引导，在GUI页面内，可以显示多个引导项。</p>
<p>2）对话的上下文处理不同</p>
<p>语音交互的上下文存在对话树中，超过层级的对话内容会从对话树中删除，但用户人脑还存在上文感知，需要更专业和复杂的引导帮助用户进行下一步操作。</p>
<p>图形交互的上文存在对话列表内，用户很容易感知上文内容，哪怕上文失效，也可以回到之前的对话部分进行查看。</p>
<p>3）对话逻辑的处理不同</p>
<p>语音交互中，存在筛选、指代、相似内容搜索、跨场景对话等对话逻辑；一旦触发一个规则，需要增加更多引导回复方便用户完成对话任务。</p>
<p>图形交互的对话逻辑，可以用文本、tab、列表等方式辅助对话任务，便捷的点击操作，让用户更好的按引导完成对话。</p>
<p>4）对话的“拟人化”程度不同</p>
<p>用户要求语音交互比图形交互更“人性化”，希望对话的智能客服更像人；对话不仅包括ASR的声音拟人化，更要求对话的内容像日常说话一样自然，对话交互要秉持友好自然有个性的原则。</p>
<p>5）情绪识别模型的使用场景不同</p>
<p>语音交互中，情绪的感知相对比较强烈，用户一说话就能感知对方是情绪低落还是情绪高涨，情绪模型的对话应用于每一句用户回复的对话中。</p>
<p>图形交互中，只有用户输入的语言文字带有情绪内容，或使用情绪的表情符号，才能识别用户当前的情绪状态。</p>
<p>6）对话的兜底应答策略不同</p>
<p>语音交互中，经常会遇到智能客服回答不了的问题，这时候需要应对技能进入相对无解的状态，对话设计不能让用户的感觉“雪上加霜”，一般回复以「机灵可爱的承认没听懂+引导下一步话术」组合出现。</p>
<p>例如：“小东在自己强大的神经网路内走迷路啦，您如果还要继续开发票请对我说我要开发票”，图形交互的回复主要以展示下一步用户可能操作的TAB选项为主。</p>
<h2 id="toc-2">二、图形交互的智能客服</h2>
<h3>1. 当前智能客服对话存在的问题</h3>
<ul>
<li>回复话术内容过多文字过长堆叠严重，用户很难聚焦。</li>
<li>关联推荐的关联问题相关性不是很好。</li>
<li>没有精细的多轮对话流程引导。</li>
<li>回复的内容没有进行流程步骤的拆解。</li>
</ul>
<h3>2. 产品优化建议</h3>
<p>1）回复话术准确、简洁、有目标性</p>
<p>例如：用户说“我要开发票”，直接引导用户开发票，完成任务。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7Ms7dwVKhsriNhuZmV2L.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p>2）客服提示的问题和用户的下一步操作引导强相关，和用户当前业务无关的提示不再出现。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/He93bRDkOHZE9IMlWt89.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p>3）需要用户输入的选择性问题，以提示tab按键代替手动输入。</p>
<p>下图，蓝色方框为TAB按键：</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/gpjoxEnYbcGDo1tbdxrp.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p>4）智能客服的回复，将用户下一步潜在的需求以流程的形式在界面中展示出来。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/bM2ek3F7UXRL5LMACtSt.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/giuXQwBiXfYHdOayR2Ju.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p>5）以解决问题为导向，细化解决方案，将方案变成用户可操作的路径。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/qDaL7ipTCvTaBrDbsCKY.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<h3>3. 图形交互对话设计样例</h3>
<p>开发票按业务流程分为访问客服、选择订单、确认信息并下单、售后服务几个场景模块。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Zus9xO5bdRC0BDEzIDBq.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/nP8BdS9yzkOuOVQMTFBU.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、语音交互的智能客服</h2>
<h3>1. 拆解业务场景</h3>
<p>开发票从业务场景上主要分为三个部分业务咨询、实施过程、售后服务。</p>
<p>业务咨询解答通用的FAQ问题，实施过程是用户真正开发票的过程，售后服务针对性回复售后相关的内容。</p>
<p>对话的内容分为：问答、闲聊、任务，结合当前场景，不存在闲聊内容，主要是问答FAQ和任务型对话。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/kOtWJW12kDgayKNer5EU.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<h3>2. 关于智能客服的开场白</h3>
<p>开场白要清楚简洁，并带有明确的引导性。基于用户的第一句话，回复意图分两个方向处理：如果是明确意图，开场白要精简明确。如果是非明确意图，开场白的回复要做推荐引导。</p>
<p>举例：</p>
<p>「对话一」</p>
<ul>
<li>“我要开发票” 用户的开场白意图很明确。</li>
<li>进入开发票的对话任务中，回复“好的，您要哪天的订单开发票呢？”</li>
</ul>
<p>「对话二」</p>
<ul>
<li>“你好”“在不”“有客服吗？”用户开场白意图不明确。</li>
<li>由于不清楚用户具体需求，给出更多可能的推荐引导回复“您好，我可以帮你开发票、办理售后，请问您要办理什么业务？”</li>
</ul>
<h3>3. 复合型指令的智能回复</h3>
<p>开发票的业务场景中，经常会用到选择订单，用户回复包括序号和选项内容，例如：“1、2020年8月4日订单”“第二个，婴儿床订单”，对话需要扩展可识别的指令词库，支持用户说订单时间、订单内容、商品信息等指令信息，方便用户在选择订单时能快速完成任务。</p>
<h3>4. 针对FAQ问答出现在任务型对话中的解决方案</h3>
<p>当前对话过程中，FAQ问答可穿插的任务型对话的任意节点，FAQ回复结束后，可自动返回之前的任务型对话节点让对话继续。</p>
<ul>
<li>FAQ问答表示科普类的、名词解释类的通用回复内容。包括：电子发票是什么？都可以开哪种发票？发票什么时候发货？</li>
<li>任务型对话表示基于明确任务目标的前提下，在达到最终节点前全部对话流程和槽位信息（填槽位的对话流程）。</li>
</ul>
<p>例如：</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/k6IAfWv3kZioR5ievkep.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<p>当前列子中“发票多久可以收到”属于FAQ问答，智能客服回复以后，需要再次询问上一个节点对话内容，引导用户继续完成对话，当前市面很多产品并没有FAQ问答结束后再继续对话的产品功能。</p>
<h3>5. 槽位信息的补充采用多轮对话的方式</h3>
<p>任务型对话中，用户在完成开发票业务前，需要的发票信息内容，如纳税人识别号、发票表头等信息，可以通过多次询问补充和完善。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/edfDu5l9Qol7yoA2dgcV.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<h3>6. 在不同场景（对话树）发生跳转时进行干预</h3>
<p>对话任务中会出现跨场景跳转，为避免超出用户预期，需要在跳转前进行二次询问。</p>
<p>举例：当前在业务咨询模块（一个场景的对话任务），用户再次询问售后服务模块（另一个场景对话任务）的时候；在语音交互中，防止失误识别而导致的对话跳转（即对话树的更改）需要再次询问用户“是否要询问售后服务关于发票收货时间的问题？”</p>
<p>如果用户确认，再更改对话任务；如果用户未确认，保持当前对话上下文。</p>
<p><img data-action="zoom" class=" aligncenter" title="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/pHYujAhqZufcxFVfDSpO.png" alt="智能客服的优化建议 | AI产品经理需要了解的智能对话知识" referrerpolicy="no-referrer"></p>
<h3>7. 异常处理</h3>
<ul>
<li>识别正确，但是没有对应的结果，如果回复。</li>
<li>识别到两个或多个域都有结果，提示用户在两个里面做选择。（有歧义的query）</li>
<li>时间过长导致上下文丢失，怎么处理？</li>
<li>对话树层级太长，有部分上文丢失，但是用户还记得上文怎么处理？（基于对话树可以维持几层）</li>
<li>用户无应答时候的处理。</li>
</ul>
<p>很多朋友给我抱怨现在的智能音箱或者机器人很傻，不能理解自己。</p>
<p>我总是安慰说，给产品和技术更多一些时间；而智能对话是真实可提升用户直观感受的重要交互方式，在智能对话领域的探索，才是让智能产品更快应用于场景，更快找到落地方式的唯一手段。</p>
<p> </p>
<p>公众号：小小仙女狮狮随想</p>
<p>本文由 @小小仙女王狮狮 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4452157" data-author="200781" data-avatar="https://static.woshipm.com/APP_U_202009_20200923095243_3638.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            