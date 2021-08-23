
---
title: 'B 类产品设计细节：对话框 vs 抽屉'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dLrBVEvvSwaN0oL0hWtg.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 23 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dLrBVEvvSwaN0oL0hWtg.jpg'
---

<div>   
<blockquote><p>编辑导读：B类产品设计时一定要注意产品细节，即使是对话框这样容易被忽略的产品设计细节也不要放过。本文从“对话框 vs 抽屉”的设计细节出发，给出不同的设计细节及展示，一起来看看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5100804 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dLrBVEvvSwaN0oL0hWtg.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>说在前面：对话框和抽屉都是在当前页面之上覆盖出现的组件，让用户在不离开主路径的情况下，查看信息/提示/反馈，或快速执行某些的操作。两者的交互模式有类似之处，使用场景也有所重叠。本文对两个组件的主要差别进行了对比，并提供方法帮助大家快速判断应该选择哪一个。</p>
<h2 id="toc-1">一、对比：对话框 vs 抽屉</h2>
<h3>1. 信息量与干扰性</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Nok54Kx1lwY2BENKiP8q.jpg" alt width="397" height="200" referrerpolicy="no-referrer"></p>
<h3>2. 模态与非模态</h3>
<ul>
<li>模态化的（Modal）：用户将不能操作页面层上的内容，只能操作页面层之上的内容容器，直到用户明确与内容容器的交互结束。</li>
<li>非模态化的（Non-Modal）：即使出现了内容层之上的内容容器，用户仍然可以与背景页面的内容进行交互（例如，选择某一链接或点击某一按钮）。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KsiQUigfzFUYJztOHR9h.jpg" alt width="407" height="300" referrerpolicy="no-referrer"></p>
<p>对话框和抽屉均可分为模态、非模态，有遮罩、无遮罩；<b>通常有遮罩的为模态，无遮罩的为非模态。</b></p>
<h3>3. 何时使用模态</h3>
<p>1）在重要的警告时使用，避免出现严重问题、或修正已出现的问题。</p>
<p>例如：用户未保存就要关闭时，弹出模态对话框提示用户保存。</p>
<p>2） 在需要用户输入信息或进行某操作，才能继续当前流程的时候使用。</p>
<p>例如：某些资源网站会在用户浏览一段时间后弹出模态化的登录/注册/试用窗口，引导注册。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/OAJN3K8xcM5gO0PrJRGv.jpg" alt width="402" height="219" referrerpolicy="no-referrer"></p>
<p>3）用来将复杂流程拆分成简单步骤。</p>
<p>例如：分步骤的模态对话框式的新手引导。</p>
<p>4）用来获取信息，该信息可大大减轻用户的后续操作/精力。</p>
<p>例如：在房地产网站 Zillow 中，用户可以在没有账号或房产代理的情况下浏览房源列表，当用户图联系某代理以获取房源信息时，站点会通过一个模式对话框询问他们是否已经有代理。</p>
<h3>4. 何时不能使用模态</h3>
<p>1）不要在获取与当前流程不相关、不必要信息的时候使用。</p>
<p>2）不要在会打断高风险流程中使用。</p>
<p>例如：付款为高风险流程，避免在用户付款过程中弹出模态弹窗打断用户，可能会让用户改变主意放弃购买。</p>
<p>3）不要让用户在模态组件上进行需要额外信息（这些信息不在上面）的复杂决策。</p>
<p>例如：Frontier Airlines 使用模态对话框来追加销售机票之外的更多服务，该对话框显示现在购买可以省162 美元，但却找不到为什么会省这个额度的钱：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nHVxb9dt3C8FldBJa3ah.jpg" alt width="401" height="211" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、案例对比</h2>
<h3>1. 对话框的模态 vs 非模态</h3>
<p>文档工具语雀中的模态对话框：登录状态失败提醒。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nUTLDWhy2s5X5kN9HeJD.jpg" alt width="400" height="124" referrerpolicy="no-referrer"></p>
<p>语雀中的进行关联操作的非模态对话框，一个短小的表单：文字链设置（这里也可以使用气泡卡片组件）</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/UWxFtKJtheIMlv3zPhoL.jpg" alt width="401" height="165" referrerpolicy="no-referrer"></p>
<p>Gmail 中点击「写邮件」按钮，在右下角打开非模态小对话框，让用户参考下面的邮件撰写新邮件：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/uAyRVXlgsmx38qyL7OL8.jpg" alt width="407" height="225" referrerpolicy="no-referrer"></p>
<p>点击上图对话框右上角表示「放大」的 icon 后，扩展为模态大对话框，转化为沉浸式的体验：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/tkFbYfPHR0BPPoIauXGO.jpg" alt width="395" height="218" referrerpolicy="no-referrer"></p>
<h3>2. 抽屉的模态 vs 非模态</h3>
<p>项目管理工具 Jira 的帮助文档入口在页面右侧，点开后从右侧划入非模态抽屉展示内容，这样便于用户进行对照查看和操作：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/f1t4PpwtgAF04VCdaN9V.jpg" alt width="407" height="225" referrerpolicy="no-referrer"></p>
<p>搜索功能入口在页面左侧中的导航中，点开后从左侧划入模态抽屉进行交互，用户可以更加专注于当前操作：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8gYLEUrfxzjFnRCdTHYU.jpg" alt width="406" height="224" referrerpolicy="no-referrer"></p>
<h3>3. 模态抽屉 vs 非模态对话框</h3>
<p>上一案例来自之前的 Jira，当前版本的 Jira 对导航和交互模式进行了调整，例如通知模块由模态抽屉改为了非模态对话框，出现的位置均遵循就近原则，体验上非模态对话框更加轻量。</p>
<p>原来由左侧划入的模态抽屉，点击左侧导航后从左侧划入：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Q7dpzUVn8mhN7evsK4j4.jpg" alt width="403" height="223" referrerpolicy="no-referrer"></p>
<p>当前版本使用非模态对话框，点击顶部导航后在 icon 下方出现：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dHKqIel9Y2aEFkQKwDbV.jpg" alt width="392" height="218" referrerpolicy="no-referrer"></p>
<h3>4. 非模态抽屉 vs 模态对话框</h3>
<p>研发效能工具 Aone 中用<b>非模态抽屉来</b>展示项目的需求/任务/bug 的具体内容：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/aQvCt8WHhbtQK29yzqiy.jpg" alt width="411" height="229" referrerpolicy="no-referrer"></p>
<p>与上图 Aone 的类似场景下，同类产品 Teambition 则采用了<b>模态对话框</b>：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yxcIKOdhpAIlnYtbbvlP.jpg" alt width="389" height="212" referrerpolicy="no-referrer"></p>
<p>相比之下，非模态抽屉的优点是，用户可以同时查看下面的父级页面中其他任务的标题，并快速点击切换到其他需求；而模态对话框的优点是用户可以完全沉浸在当前的任务中，同时顶部也增加了「上一条」、「下一条」按钮，支持上下条快速切换。</p>
<p>两者对比可以看出，两种组件自身的优点也是对方的不足，没有百分百的十全十美。选择哪一个，要看具体用户的需求和产品的定位。</p>
<h3>5. 模态抽屉 vs 气泡卡片</h3>
<p>文档工具 Gitbook 中，产品功能和交互都很简洁轻量，没有出现对话框组件，在文档中插入图片或文件、编辑导航、导入文档等稍重的操作使用抽屉，而插入表情、标签等位置指向明确、操作很轻的使用气泡卡片，这些气泡卡片和非模态的对话框类似：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/mSuB7v2Pn4eUwLtHSVRj.jpg" alt width="399" height="203" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oQaCqnZWuoq9wHijqUwz.jpg" alt width="399" height="203" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、选择：用对话框还是抽屉？</h2>
<p>按下图从应用场景、交互需求、信息长度三个维度来判断使用对话框还是抽屉。</p>
<p>例如：为一个表单选择组件，从应用场景来看，对话框和抽屉皆可；从交互维度，该表单的填写需要参考表单的父级页面中的内容，则确定选择非模态抽屉，不需要再从长短考虑。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/FtPuGooxd0DV2NTY2QCy.jpg" alt width="372" height="180" referrerpolicy="no-referrer"></p>
<ul>
<li><b>一致性</b>：除以上列表中的三个判断维度，还有「一致性」原则需要考虑，例如某产品弹出的表单大多较长，采用抽屉组件，为了保持体验的一致性，个别短表单也可以同样采用抽屉。但针对不同产品的具体情况，一致性的优先级有所区别，因此未放入判断列表。</li>
</ul>
<h2 id="toc-4">四、注释和举例</h2>
<ul>
<li><b>操作确认、信息提示、操作反馈场景</b>：在需要用户暂停当前操作、即刻阅读/处理时，使用模态对话框，否则建议使用较轻量的组件如警告提示、全局提示、通知提醒框、气泡确认框。本文讨论对话框和抽屉的区分。</li>
<li>需要<b>和父级页面内容相互参照</b>：使用无遮罩的非模态抽屉，便于查看和操作。</li>
<li>需要<b>在父级页面中快速选择切换</b>：使用无遮罩的非模态抽屉。在下面父页面露出的部分上进行与抽屉内容和位置都无关的操作，且不是点击空白区域时，抽屉不用自动消失。</li>
<li><b>叠放</b>：是指在一个对话框/抽屉上面叠加放置更多对话框/抽屉。不建议对话框上叠放对话框，但抽屉组件支持多层抽屉，即在抽屉内打开新的抽屉，用以解决多分支任务的复杂状况。</li>
</ul>
<p>必要的情况下，在抽屉上叠放对话框也是可以的，例如在抽屉操作过程中有非常重要的信息要即刻告知用户，可以通过对话框展示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DeCCTkTOjAlvdSqaRorA.gif" alt width="399" height="233" referrerpolicy="no-referrer"></p>
<ul>
<li><b>表单长短</b>：表单项超出 5 条时，建议采用抽屉而非弹窗。</li>
<li><b>内容长短</b>：在展示静态信息给用户时，如果内容少、不超出 5 行，建议使用弹窗而非抽屉；如果信息多到超出一屏，功能上弹窗和抽屉都支持滚动条，都可以使用，如何选择请设计师根据设计倾向和一致性决定。</li>
</ul>
<p>参考：</p>
<ul>
<li><span class="invisible">https://www.</span><span class="visible">uisdc.com/pop-up-applic</span><span class="invisible">ation-design</span></li>
<li><span class="invisible">http://www.</span><span class="visible">woshipm.com/ucd/3502268</span><span class="invisible">.html</span></li>
<li><span class="invisible">https://</span><span class="visible">mp.weixin.qq.com/s/xZ5U</span><span class="invisible">uOtlbDb8wEOd8IjYcg</span></li>
<li><span class="invisible">https://</span><span class="visible">yuque.antfin.com/docs/s</span><span class="invisible">hare/7b3c3efd-7766-49dc-9799-09d95b3bf44e?#</span></li>
<li><span class="invisible">https://www.</span><span class="visible">nngroup.com/articles/mo</span><span class="invisible">dal-nonmodal-dialog/</span></li>
</ul>
<p> </p>
<p>作者：林叶，蚂蚁集团设计师</p>
<p>本文由 @Ant Design 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5081980" data-author="1275742" data-avatar="http://image.woshipm.com/wp-files/2021/05/qQzaYS0DiYKZrsomCZyR.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            