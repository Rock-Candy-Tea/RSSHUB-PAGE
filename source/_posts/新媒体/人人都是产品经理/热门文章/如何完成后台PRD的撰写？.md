
---
title: '如何完成后台PRD的撰写？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/102.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 08 Feb 2018 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/102.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/102.jpg" referrerpolicy="no-referrer"><blockquote><p>本文作者将分享自己在后台需求文档的撰写上的心得和建议，enjoy~</p></blockquote>
<p>
</p><p>近期在工作上独立完成了一份后台的需求规格说明书，因此有了一些心得体会。在这之前，我浏览过许多关于后台设计的文章，大部分文章都是在阐述如何设计后台，给了我们很多设计理念上的建议与帮助。</p>
<p>只是，无论什么样的设计都最终都需要以文档的形式产出，因此，本文我将在后台需求文档的撰写上分享自己的心得和建议。现在，我们先来做做下笔前的思想工作：</p>
<h2 id="toc-1">为什么要进行后台设计？</h2>
<p>我们设计后台的初心，都是为了支撑业务，并进一步提高运营效率和产品竞争力，这是我们在设计后台时需要时刻提醒自己的。由于后台的产品不需要过多的考虑UI和交互设计，所以在明确好业务逻辑和系统架构之后，<strong>将效率的提升作为后台产品的重要指标（KPI），</strong>注意避免用户在使用你的产品时，做太多重复、机械的操作。</p>
<h2 id="toc-2">下笔的前提</h2>
<p>关于后台的设计还是需要老话重提。<strong>产品经理一定要对你所设计的后台业务了如指掌，</strong>亲自深入到业务的实际工作中去，将工作流拆分成多个环节，形成功能的初步构想。期间，你需要记录下业务的整体流程和涉及到的元素，如字段、字段限制、业务要求等。</p>
<p>我个人的习惯是先将这部分内容写于纸上，清楚的梳理好业务之后，再将内容转化成电子档。在纸上，你可以迅速的对内容进行编辑、修改，甚至可以将原型直接画出，让功能先简单的呈现出来，再进行调整改动，这样可以减少很多电脑操作的时间。</p>
<p><strong>同时还需明确目标用户，也就是这个功能是给谁用的。</strong>一般后台的目标用户都是公司内部人员，如运营、市场等等，用户就在身边，那么产品经理千万不能浪费机会，一定要与用户进行沟通，提炼出他们的需求。以下是可以提的一些问题举例：</p>
<ul>
<li>过去是怎么处理这项业务的？</li>
<li>哪一个环节给你带来困扰或者说需要花费你大量的时间去完成？</li>
<li>你最希望实现的功能是什么？</li>
<li>谁可以操作这项业务？操作的范围又是哪些？</li>
<li>是否需要对用户的操作行为进行记录？</li>
<li>……</li>
</ul>
<p>大家可以根据实际情况进行问题的列举和提问，只有充分地融入到用户中，才能设计出走心的后台哦。</p>
<p><strong>总结一下，下笔之前需要明确几个要素：角色、角色的权限（包括功能权限和数据权限）、业务流程、所需字段、操作日志等。</strong></p>
<h2 id="toc-3">下笔的顺序</h2>
<p>无论是功能还在初拟阶段还是已经开始撰写需求文档，<strong>下笔的顺序一定是从核心功能（业务）->分支功能（业务），</strong>因为核心功能是奠定整个后台的基础，其他功能都是围绕着核心功能延伸开来。无论是字段规则还是业务规则，其他功能都必须与核心功能保持一致，才能够保证后台的顺利运行。</p>
<p>当你完成核心功能的设计和文档撰写时，可以先与研发讨论设计是否合理和可行，接着再进行分支功能的设计，这么做避免后期需要推倒重做的窘境。</p>
<p>后台系统的目标用户可能是运营人员、市场人员……，而需求文档的目标用户一定是你的研发同事们，需求文档是你输出的一个产品，因此我们一定要让需求文档变得更清晰更易懂。</p>
<h2 id="toc-4">什么样的需求文档研发爱看？</h2>
<h3><strong>简洁、高效</strong></h3>
<p>设计时要遵循“简洁、高效”的原则。能用一个词说明清楚的事，千万不要用一句话。</p>
<h3><strong>前后描述一致</strong></h3>
<p>设计后台时，模块之间必然会有关联性，不同的模块可能会涉及到相同的字段，因此对于每项字段、字段类型、字段说明等内容必须保持一致，不要有前后矛盾的情况。</p>
<h3><strong>善用表格、图文并茂：</strong></h3>
<p>后台中的功能结构、角色权限的分配等结构性内容采用表格的形式；</p>
<p>数据流向、业务流程用流程图、泳道图等描述清楚；</p>
<p>功能用原型图呈现，原型图中的信息进行归类，不能因为是后台，无需考虑太好的用户体验而忽视了页面的清晰整洁度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/02/reLJ7QZaUpc1T6ZaMdVP.jpg" alt width="809" height="423" referrerpolicy="no-referrer"></p>
<p>原型图的各类按键规格保持一致，让研发或UI更好的设计，降低沟通成本。</p>
<h3><strong>描述方法：</strong></h3>
<p>一般后台功能可分为列表数据、功能操作（增删改查等）两大块。可以从以下方式进行描述：</p>
<p><strong>（1）列表数据</strong></p>
<ul>
<li><strong>字段：</strong>字段名称、字段类型、字段描述、数据来源、字段规则等；</li>
<li><strong>列表：</strong>呈现字段、排序规则、分页规则、状态等。</li>
</ul>
<p><strong>（2）功能操作</strong></p>
<p><strong>方法一：事件流程法</strong></p>
<p>比较复杂的后台功能在同一个功能点中可能包含多个事件，所以复杂后台功能可按照：基本事件流程、子事件流程与特别需求来描述。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/02/VvXiYPSaHFRxoJr0H8RZ.jpg" alt width="614" height="340" referrerpolicy="no-referrer"></p>
<p><strong>方法二：条件描述法</strong></p>
<p>这个方法适用于查询功能，直接对需要查询的条件、规则进行描述。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/02/fb2d9YmqniHTf77fHayi.jpg" alt width="519" height="183" referrerpolicy="no-referrer"></p>
<p><strong>方法三：输入输出法</strong></p>
<p>输入处理输出大部分是由开发来考虑的，但产品经理如果能站在开发的角度，明确输入、处理、输出的内容，那会省去很多开发的理解成本。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/02/0zCqhsNktKQMQm3QJRjB.jpg" alt width="539" height="462" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/02/ze0qoCo6D4piBhjaKdVu.jpg" alt width="536" height="512" referrerpolicy="no-referrer"></p>
<p><strong>方法四：简要测试用例</strong></p>
<p>测试用例可直接用来表述简单、常见的功能，直击功能的目的。前提是这类功能一定是比较常见的，不需要过多的深入描述，开发也能懂。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/02/T8g9HfGbzeOBZVS0O8Bo.jpg" alt width="429" height="204" referrerpolicy="no-referrer"></p>
<p><strong>一些小TIPS：</strong></p>
<ol>
<li><strong>需不需要描述很细节的东西？</strong>这个问题要取决于整个开发团队的默契度，以及在开发之前是否已经形成了标准的规范，如果是，那么产品经理可以适当减少一些细节描述，简要概括，将重点放在业务的流程和逻辑上。</li>
<li>大部分情况下，前台需求决定后台需求，后台产品经理设计前一定要与前台产品经理进行深入沟通，不管是对目前有的功能还是未来的前台需求规划，后台产品经理都要了解，提前做好规划，眼光放长远，思考功能的可持续性。</li>
<li>有些团队的后台文档可能会由若干个产品经理共同完成，建议对每个模块的作者做好标注，方便开发找到负责人沟通。同时，做好各大模块的标题和大纲，供开发查找。</li>
<li>一份需求文档一定会修改好几个版本，一般采用R（Requirement）0、R2.0……来表示版本号。</li>
</ol>
<p> </p>
<p>本文由 @有馅儿的丸子  原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自StockSnap.io，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="935312" data-author="115035" data-avatar="http://image.woshipm.com/wp-files/2017/12/CZduVVf3i8cPziRR4Xdg.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">4人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182956_6960.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182656_8064.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175040_5637.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602174850_7385.png?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            