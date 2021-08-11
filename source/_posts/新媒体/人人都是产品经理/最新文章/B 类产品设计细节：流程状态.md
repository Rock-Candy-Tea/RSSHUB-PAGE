
---
title: 'B 类产品设计细节：流程状态'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WzlA1Y8hQWTiMqzEFZJC.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 11 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WzlA1Y8hQWTiMqzEFZJC.jpg'
---

<div>   
<blockquote><p>编辑导语：在B类产品设计中，会涉及到一系列抽象/具象事物的流转和变化。在不同的流程状态中，对应着不同的角色和具体操作。作者分享了在B类产品设计中的细节，我们一起来看看流程状态的具体细节吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5025160 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WzlA1Y8hQWTiMqzEFZJC.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是流程状态</h2>
<p>B 类产品通常涉及一系列抽象/具象事物的流转、变化，如一个任务的执行、一家商家的入驻等等，这些过程均涉及规范的流程，流程的不同阶段涉及不同的状态，不同的状态又对应不同的角色和具体操作（如下图）。</p>
<p>因此流程状态的设计必不可少，且必须清晰易懂、简洁直接。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/L1vKzhxA6KAPBz2EsZ0k.png" alt width="729" height="130" referrerpolicy="no-referrer"></p>
<p>除了流程状态之外，还有一种 B 类产品中常见的状态，就是生命周期状态，例如营销推广的推广组状态可分为「推广中」、「已下线」等等。</p>
<p>在很多产品中，生命周期与关键流程有紧密的联系，两种类型的状态会有一定交叉。本文主要讨论的是流程状态。</p>
<h2 id="toc-2">二、状态的命名</h2>
<p>流程状态的设计原则与人机交互的最根本原则一致，即「以用户为中心」，确保目标用户在相应的使用场景下能够快速理解并正确执行相关操作。</p>
<h3>1. 按行业规则命名</h3>
<p>专业工具或平台的设计中，对于状态的命名如果有行业约定俗成的术语，则遵照行业规则命名，即便在体验设计师自己眼中可能不够简洁美好。</p>
<p>例如：以工程师为主要用户群体的项目管理工具 Aone 中，bug 的状态有 10 种（如下图），且遵循了英文技术术语。对于设计师来说状态种类复杂、语言不统一，但从用户的角度来说这样是必须的、规范的，因此设计师要尊重用户的习惯和需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oSNIl583MxYMmMnUlOMZ.png" alt width="799" height="318" referrerpolicy="no-referrer"></p>
<h3>2. 围绕核心操作命名</h3>
<p>流程的名称通常是描述对应操作的过程或结果，如「待付款」、「退款中」是操作的过程，「完成付款」、「退款失败」是操作的结果。</p>
<h3>3. 单个核心操作</h3>
<p>最简单、最常见的流程是：角色A 发起流程 – 角色B 进行操作 – 流程结束给出结果。</p>
<p>这种两个角色三步走的流程，状态命名通常分为如下两种（框中是状态命名）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/kaeqaamQow2xAtXnnazJ.png" alt width="763" height="561" referrerpolicy="no-referrer"></p>
<p>上图里面的动词可替换成其他动作；结果状态也可用「已通过」、「未通过」等，根据实际情况而定。</p>
<p>围绕一个核心的操作，也可能涉及多个角色。</p>
<p>例如：最常见的审批流程，过程中涉及多个角色的层层审批。如果不同角色审批时，用户可执行的操作不同，或审批的详细过程对用户非常关键，这时审批单的状态命名上需要注明具体角色。</p>
<p>如果通常不需要关注具体到哪个人审批了，则统一称为「审批中」即可，用户可以到详情页面查看具体进度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/2mcb77cRjrGL4lMNRr2R.png" alt width="781" height="393" referrerpolicy="no-referrer"></p>
<h4>4. 多个核心操作</h4>
<p>涉及多个角色、一串核心操作的复杂流程。</p>
<p>在流程完成之前的中间过程中，告知用户下一步待执行的操作，比上一步刚刚完成哪个更重要。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/SwgJkHcg55sqzrJz10w9.png" alt width="758" height="438" referrerpolicy="no-referrer"></p>
<p>在角色多、极易混淆的情况下建议在状态名上增加角色名。</p>
<p>例如：数字仓单的仓单质押流程中涉及三个角色（存货人、仓储方、资金方）多个步骤，过程中关键是引导用户继续后续操作、高效完成申请，所以状态上展示当前要进行的操作。</p>
<p>同时流程中包含连续多个角色的接力审核确认，容易混淆，因此状态标签中显示当前需要哪个角色进行操作；而放款、收款的角色很明显是资金方和申请方来操作，所以对应的状态没有显示角色名称。如图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Q6LBr4QW7xAF9eEqP99N.png" alt width="812" height="191" referrerpolicy="no-referrer"></p>
<p>同一阶段时，不建议区分不同用户角色看到的状态名，可以给他们不同的反馈或提醒。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ETHMOZ8MnP7yBij9Op28.png" alt width="791" height="330" referrerpolicy="no-referrer"></p>
<p>状态组间存在一对多的映射关系时，要注意区分逻辑关系，不建议将上下层状态打平到一起。</p>
<p>接上面数字仓单的案例：系统中，货物的所有者可以用仓单进行质押，这样仓单就会有「未质押」、「质押申请中」和「质押中」状态（不允许重复质押）。而质押申请是个复杂的流程，「质押申请中」这一仓单状态，对应「质押申请单」的一系列流程状态。</p>
<p>同理，在仓单解除质押、注销等其它情况下，又会有「解质流程中」、「注销中」等状态，对应的「解除质押流程」、「注销流程」有会一系列对应的状态。如图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/4WuC2OS3P4Xr7zxWqsY3.png" alt width="742" height="1526" referrerpolicy="no-referrer"></p>
<p>这种情况下要梳理好业务流程，如果将上下层状态打平到一起，短期内可能看起来比较简洁，但随着产品复杂度的提升（B 类产品通常会越来越复杂），逻辑关系会越来越混乱。</p>
<h2 id="toc-3">三、状态的视觉设计</h2>
<h3>1. 状态的颜色</h3>
<p>表示状态的颜色不建议超过 5 种：红色、橙色、绿色、蓝色、灰色。</p>
<p>设计师需要结合色彩的功能特性、品牌色板、产品逻辑、用户需求来选择适合的颜色。常用配色举例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Arl30KsDd4H1WD96DT3t.png" alt width="681" height="365" referrerpolicy="no-referrer"></p>
<p>状态的颜色不止会用在标签上，对应的可视化图表、图标等视觉元素要用色一致。例如进度条：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xRi8UGgLYhvTXbnvPW68.png" alt width="719" height="171" referrerpolicy="no-referrer"></p>
<h3>2. 状态标签的样式</h3>
<p>不同状态对应不同用户的不同操作，因此状态信息通常与普通文本在视觉上有所区分。常用的样式包括彩色标签、彩色圆点等等。例如：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/3ZMKhV4ESC2ROH1sFS6k.png" alt width="855" height="159" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/a8tkf2ILUIDhg1V2eBv9.png" alt width="856" height="226" referrerpolicy="no-referrer"></p>
<p>注意列表、表单中状态标签的样式统一。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/bWWi3OC8x0hSFhx9jsi9.png" alt width="721" height="456" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、总结</h2>
<h3>1. 原则</h3>
<p>流程状态的设计原则与人机交互的最根本原则一致：以用户为中心。</p>
<h3>2. 命名</h3>
<ol>
<li>在流程完成之前的中间过程中，告知用户下一步待执行的操作，比上一步刚刚完成哪个更重要；</li>
<li>在角色多、极易混淆的情况下建议在状态名上增加角色名；</li>
<li>同一阶段时，不建议区分不同用户角色看到的状态名，可以给他们不同的反馈或提醒。</li>
<li>专业工具或平台中，如果有行业约定俗成的术语来命名状态，则遵照行业规则。</li>
</ol>
<h3>3. 关系</h3>
<p>状态组间存在一对多的映射关系时，不要将上下层状态打平到一起。</p>
<h3>4. 颜色</h3>
<p>表示状态的颜色不建议超过「红色、橙色、绿色、蓝色、灰色」这 5 种。</p>
<p> </p>
<p>作者：林叶，蚂蚁集团设计师</p>
<p>本文由 @Ant Design 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5019658" data-author="1275742" data-avatar="http://image.woshipm.com/wp-files/2021/05/qQzaYS0DiYKZrsomCZyR.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            