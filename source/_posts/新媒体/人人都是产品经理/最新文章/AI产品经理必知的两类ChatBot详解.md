
---
title: 'AI产品经理必知的两类ChatBot详解'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZTLji8BL9aVxbdRXkjFM.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 16 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZTLji8BL9aVxbdRXkjFM.jpg'
---

<div>   
<blockquote><p>编辑导语：对话机器人（ChatBot）目前已应用在众多领域，但还有一些AI产品经理对其概念没有一个系统化的认知。作者在文中对两类ChatBot进行了详解，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4882362 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZTLji8BL9aVxbdRXkjFM.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>对话机器人（ChatBot），以自然语言的方式和用户进行交互，从而完成咨询、客服、助理、娱乐等用户诉求，目前已经应用在很多领域。</p>
<p>本文主要介绍两类应用最广的ChatBot：FAQChatBot和多轮对话ChatBot，包括这两类ChatBot的适用场景和构造模块。</p>
<h2 id="toc-1">第一类：FAQChatBot</h2>
<p>FAQ(Frequently Asked Questions) ChatBot，从英文全称可以看出来，是将一些频繁用到的问题和答案对整理好，形成知识库。</p>
<p>当用户提问时，将用户的问题和知识库的众多问题进行匹配，匹配完成后，将匹配到的知识库问题对应的答案，返回给用户，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/d0avfJTUKxQAyT2ejNm6.png" alt width="326" height="96" referrerpolicy="no-referrer"></p>
<p>为了匹配更精准，在构建知识库时，可以多设置几个扩展问题，如下表所示，在疫情期间，为了快速构建一个FAQ ChatBot，提高问题匹配精准度，可以这样构建知识库：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/8s69C6t13YYjYULH1mwb.png" alt width="863" height="371" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">当我们的目标是快速构建一个基于常用知识的咨询时，就可以用FAQ ChatBot，例如打造一个公司内部的入职咨询、报销指南。</span></p>
<p>总结一下，FAQ ChatBot 的目的是：将企业的各种知识有效管理起来，采取一问一答的单轮对话方式，为用户提供咨询服务。</p>
<p>该方法的优点是建设快，质量可控、准确率高，其缺点是泛化能力比较弱。随着不断迭代，知识库的更新很大程度依赖于人工，不能自主提升自己的泛化能力。</p>
<h2 id="toc-2">第二类：多轮对话ChatBot</h2>
<p>当面临更加复杂的问题时，例如用户想要完成订餐、订票等任务，需要进行多轮陈述，才能完成用户的诉求。</p>
<p>一方面，用户在对话过程中可以不断修改或完善自己的需求；另一方面，当用户的陈述的需求不够具体或明确的时候，机器也可以通过询问、澄清或确认来帮助用户找到满意的结果。</p>
<p>对于这样的多轮对话，ChatBot架构如下：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/58sdN4AEHqnaEQyfmT5R.png" alt referrerpolicy="no-referrer"></p>
<p>下面，我们配合下面这个预订会议室的例子，来理解多轮对话ChatBot架构的各个模块：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pvHbYX4TbuOT0qT5DqfB.png" alt width="424" height="389" referrerpolicy="no-referrer"></p>
<h3>1. NLU(Natural Language Understanding)</h3>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/sNQLDrwcDaGff2HUUlZ2.png" alt referrerpolicy="no-referrer"></p>
<p>NLU的目的是，完成对用户指令的理解。</p>
<p>所以NLU模块的输入是用户指令，输出主要采用DIS的表示结构，D代表Domain（领域）, I代表Intent（意图），S代表Slot（槽位）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/WFf6OdAGAH6iCCCL1H8g.png" alt width="376" height="149" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（有些情况下没有Domain，直接输出为Intent）</p>
<p>Domain、Intent和Slot都是产品经理根据需求预先定义好的。不同的业务场景会定义不同的DIS。</p>
<p>对于这个预订会议室的例子，可以定义DIS如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/41k38GphrYkGj0vIBrMr.png" alt width="338" height="172" referrerpolicy="no-referrer"></p>
<h3>2. DM(Dialog Management)</h3>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/CuHbg3D1aoXSL72Aw1Sz.png" alt referrerpolicy="no-referrer"></p>
<p>对话管理DM控制着人机对话的过程，是ChatBot的核心。</p>
<p>在对话过程中，对话机器人系统会不断根据当前的对话状态和用户行为，决定下一步应该采取的最优动作，从而完成整个对话任务。</p>
<p>因此，在这个过程中，DM主要完成以下两个任务：</p>
<p><strong>（1）维护&更新对话状态(dialog state tracking, DST)</strong></p>
<p>根据之前的状态和用户的输入，维护一份最新的对话状态。</p>
<p><strong>（2）产生系统决策(dialog strategy)</strong></p>
<p>根据DST中的对话状态做出系统决策，决定下一步做什么。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AjqYZcyXIalOb1V3YpJ5.jpeg" alt referrerpolicy="no-referrer"></p>
<p>如上图，对于当前的会议室预订实例，当用户表达了想预订906会议室，当前的最新对话状态为：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mYvygnGpa9UOQeye6mdd.png" alt referrerpolicy="no-referrer"></p>
<p>此时，系统做出决策：对话补全。因此，系统继续追问用户：您想预约什么时间段？</p>
<p>用户对此反馈：明天上午9点到11点。</p>
<p>系统根据此时最新的反馈和刚才的对话状态状态，产生新的系统决策，并更新状态。</p>
<p>更新后的状态为：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DdoKKvSVaF1GfFjHtMdY.png" alt referrerpolicy="no-referrer"></p>
<p>在这个案例里，DM的输入输出如下图：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/HU0AJITLORSxXO5CMVTQ.png" alt referrerpolicy="no-referrer"></p>
<p>在产生系统决策时，DM一般会利用以下两种策略：</p>
<p><strong>（1）意图重入：当从当前的用户行为中分析不出意图时，会将上一轮的意图重入。</strong></p>
<p>例如“我还想定一个下午两点到四点的”，单凭这一句话，无法得出用户的意图，则将上一轮查询的“会议室预订”意图进行重入。</p>
<p><strong>（2）领域重入：当意图重入匹配度较低，则会采用领域重入。</strong></p>
<h3>3. NLG（Natural LanguageGeneration）</h3>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/hVmrf2hbeUzLibci4mI3.png" alt referrerpolicy="no-referrer"></p>
<p>当DM做出和用户交互相关的系统决策时，需要NLG模块配合，生成自然语言，和用户完成交互。</p>
<p>当用户预订会议室成功后，DM模块将预订成功的信息传给NLG模块：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/cm1ILu4hPLsVniVYXFoJ.png" alt referrerpolicy="no-referrer"></p>
<p>NLG模块则根据预设的模版或其他生成算法，以自然语言方式反馈给用户结果：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DFTngvsnsRKiRWzfYkWy.png" alt referrerpolicy="no-referrer"></p>
<p>总结一下，多轮对话与单轮对话的不同在于，携带前几轮对话的上下文信息，可以完成更复杂的任务，也使得对话过程更加智能。</p>
<p> </p>
<p>本文由 @躺平看星星 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4869192" data-author="1112312" data-avatar="https://static.qidianla.com/woshipm_def_head_2.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            