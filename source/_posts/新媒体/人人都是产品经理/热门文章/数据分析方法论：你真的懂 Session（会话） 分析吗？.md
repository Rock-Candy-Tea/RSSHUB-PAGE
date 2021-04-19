
---
title: '数据分析方法论：你真的懂 Session（会话） 分析吗？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/107.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 26 Jun 2017 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/107.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/107.jpg" referrerpolicy="no-referrer"><blockquote><p>Session 分析并不“包治百病”，但却是用户行为分析的重要方法。</p></blockquote>
<p>
</p><p>在数据分析领域，Session是一种专业的数据分析。对于有数据驱动意识的互联网人来说，这并不陌生——Session 即会话，是指在指定的时间段内在网站上发生的一系列互动。例如，一次会话可以包含多个网页或屏幕浏览、事件、社交互动和电子商务交易。</p>
<h2 id="toc-1">Session：解决用户分析中的“线”型难题</h2>
<h3><strong>Session 分析有何意义？</strong></h3>
<p>人们往往最熟悉事件分析模型，且用户行为事件往往以“点”的方式呈现，即某人在什么时间什么地点干了一件什么样的事，也就是我们熟知的 4W1H 模型：Who、When、Where、How、What。</p>
<p>王小明昨天下午在 i 百联通过个性化推送买了一双 NIKE 球鞋，张小花今天十点在融 360 上注册后领取了新人基金，某白领晚上六点在五道口区域扫码一辆 ofo 小黄车并报修了它……</p>
<p>基于这样用户角度的行为记录，产品方可以知道他们的用户都具体干了什么事情。并对自己的产品做出精细化运营，但是，还有一些需求，是不能通过“点”来描述的，比如：</p>
<ul>
<li>用户平均会来几次？</li>
<li>每次平均逛了几个页面？</li>
<li>每次来平均待多久？</li>
<li>某个具体页面用户平均停留多长时间？</li>
</ul>
<p>这些需要把用户单点行为串联起来形成一个整体，并在此基础上进行计算后才能得到的数据分析需求，更像是一条“线”。<strong>而 Session 分析的最大意义，就是解决用户分析中的“线”型难题，从不同角度指导精细化运营与商业决策。</strong></p>
<h2 id="toc-2">如何用 Session 分析支持工作？</h2>
<p>如果根据定义，Session 的关键点显然是：多长时间内用户做了什么事。</p>
<h3><strong>Session 切割时间</strong></h3>
<p>假如王小明打开某企业官网了解信息，点击了 DEMO 按钮，并进行了注册试用行为，然后就被领导叫去开会，四十分钟后又跑回来继续浏览页面，这是几个 Session？</p>
<p>这要看数据分析工具的 Session 切割规则，通常来讲，Web 产品建议切割时间为 30 分钟，APP 产品建议切割时间为 1 分钟。比较符合用户的使用习惯，当然规则是活的人也是活的~可以根据产品的业务形态变更。所以王小明两次浏览页面的时间超过了 Web 端的 30 分钟，被记录为两个 Session。</p>
<h3><strong>Session 事件</strong></h3>
<p>Session 记录什么事件，取决于需要关注的用户行为。如果 Session 事件只包含了注册行为（核心事件），那王小明的行为将会被记录为一个 Session。如果包含浏览页面，则会被记录为两个 Session。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/06/T4IKlAAG415UXL2S54gf.png" alt width="649" height="438" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><strong>图1 不同切割时长的 Session   </strong>图片来源：神策数据</p>
<h2 id="toc-3">那么，Session 分析究竟可以分析什么？</h2>
<h3><strong>平均使用时长</strong></h3>
<p>平均访问时长是指在一定统计时间内，浏览网站的一个页面或整个网站时用户所逗留的总时间与该页面或整个网站的访问次数的比。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/06/YbzOa9T4qwFt7mnMhcsI.png" alt width="424" height="111" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><strong>图2 平均访问时长</strong></p>
<p>平均访问时长越久，证明 Web/APP 越有吸引力，如果用户停留的平均时间非常低，那么可能内容不够有趣，或界面优化较差，真正有价值的内容无法吸引用户，影响用户体验。</p>
<h3><strong>平均交互深度</strong></h3>
<p>平均交互深度和平均访问深度定义虽有差别，意义却很相似，都是衡量 Web/APP 质量的重要指标，可以帮助企业了解页面内容的价值，功能是否满足用户需求，指标的具体意义需要依照业务判断。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2017/06/Fjw6r8pTxKvosBVLYkm4.png" alt width="476" height="130" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><strong>图4 平均交互深度</strong></p>
<h3><strong>跳出率</strong></h3>
<p>这部分我在后面的文章会详细的介绍，有兴趣的朋友可以关注下。</p>
<h3><strong>Session 转化分析</strong></h3>
<p>营销推广中一个非常典型的需求是需要知道不同渠道带来的注册、购买等转化情况，该需求本质上，就是需要界定 Session，然后按渠道属性查看注册、购买等事件的转化数量。</p>
<h3><strong>用户路径</strong></h3>
<p>在业务流程中，了解用户的行为路径，有助于运营同学找到用户大量流失环节，衡量网站营销推广效果，产品同学验证用户行为流与初步设想进行对比，完善功能，优化用户体验。</p>
<p>使用用户路径分析，设定起始事件与 Session 切割时间，可以观察一个 Session 内用户的行为流。</p>
<h2 id="toc-4">总结</h2>
<p>Session 分析并不“包治百病”，但却是用户行为分析的重要方法；既可以看透如王小明一样的“常跑路”用户，也可以帮你了解真正的用户使用习惯，避免产品设计“不按套路出牌”的辛酸往事。</p>
<p> </p>
<p>作者：张乔，神策数据内容营销高级经理，用户行为洞察研究院负责人。公众号：用户行为洞察研究院</p>
<p>本文由 @张乔-神策 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="700390" data-author="236250" data-avatar="http://image.woshipm.com/wp-files/2017/04/1QUcR6wiuxeW6RnbG0gD.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">5人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.qidianla.com/woshipm_def_head_2.jpg" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182928_2896.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175248_6880.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175151_3685.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175121_6450.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            