
---
title: '一条提示信息的N种表现方式'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/06/W7VUbebY3iSMV2vXWq90.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 01 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/06/W7VUbebY3iSMV2vXWq90.jpg'
---

<div>   
<blockquote><p>编辑导语：本篇文章聚焦在校验规则及提示信息，帮助新手B端体验设计师快速了解提示信息的触发规则及注意事项，搭配复杂案例助力融会贯通。欢迎感兴趣的小伙伴们一起阅读分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-831624 aligncenter" src="https://image.yunyingpai.com/wp/2022/06/W7VUbebY3iSMV2vXWq90.jpg" alt referrerpolicy="no-referrer"></p>
<p>业务性强，内容复杂度高是ToB产品的典型特征。<strong>当用户需要在产品流程中录入大量数据信息时，业务本身的复杂性会大大增加录入成本</strong>。</p>
<p>作为体验设计师，通过<strong>系统引导性提示</strong>和<strong>校验性提示信息</strong>帮助用户快速完成工作是我们的职责所在。下面我们一起来看看复杂的校验性提示信息如何去做：</p>
<h2 id="toc-1">一、提示信息存在的必要性</h2>
<p>提示信息是系统与用户之间信息反馈的载体，告知用户当前操作的可行性，减少操作损失，引导用户进行。</p>
<p>提示信息是反馈组件的一部分，属于反馈组件，但不包含所有的反馈组件。<strong>因为只有在录入内容出现报错、阻断时才需要提示信息。</strong></p>
<h3>1. B端产品的校验规则为什么复杂？</h3>
<p>C端产品的提示信息除了提示以外还起到安抚用户的作用，适当进行情感化的设计帮助留住用户。</p>
<p>而<strong>B端提示信息只有在必要时才会展示，能不要提示尽量不要提示，不要给用户额外的“负担”，提升工作效率和使用效率才是我们的目标。</strong>所以提示信息的设计需要谨慎，谨慎的事情必然伴随一定的复杂性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/UqSrdJMboNa5zgDY3ika.png" width="540" height="305" referrerpolicy="no-referrer"></p>
<h3>2. 常见的校验规则</h3>
<p><strong>提示信息分为系统性提示和校验性提示</strong>，我们这次只针对校验性提示进行讲解。</p>
<p>提示信息跟随校验结果出现，本质上也是一种信息反馈。</p>
<h3>3. 基本原则</h3>
<p><strong>信息校验一般分为前端校验和后端校验</strong>。举个例子，前端校验就像我们登录邮箱，输入了密码，主观判断输入正确，但是提交后发现后输入错误。如果这里系统强制要求是12位数密码，你只输入了11位，那么这里提示：“请输入12位数的登录密码”就属于前端校验，而提交后提示的：“账号或密码错误”是属于后端校验。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/I4E3AMpjT0zfa59hK9M7.png" width="525" height="224" referrerpolicy="no-referrer"></p>
<p>前端校验常见的有：<strong>字段校验、必填项校验、完成度校验、产品业务数据校验等等</strong>。比如电话号码少填写一位数、必填内容未完成、一共三个步骤只填写了两步。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/js5WxGhVGJpDrJPOkBYo.png" width="523" height="169" referrerpolicy="no-referrer"></p>
<p><strong>当产品业务数据校验放在前端去做时，多半是因为校验内容过多，想给后端校验跑数据时减轻压力</strong>，将一些简单的业务功能性校验放在前端去做。但是这里要注意，要跟前端工程师沟通好，并不是所有内容都适合放在前端进行校验的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/CtKwZB9RjaIuCldQPtg6.png" width="529" height="270" referrerpolicy="no-referrer"></p>
<p>后端校验涉及到<strong>用户信息确认、业务数据确认等需要跑通数据库的校验内容</strong>。</p>
<p>常见的比如保险理赔中我们报案提交理赔的时间，不能早于事故发生的日期，这方面的数据存储于后端数据库，所以需要后端调取数据进行核实才能出校验结果。</p>
<h3>4. 提示信息的出现顺序</h3>
<p>校验步骤的基本规则是<strong>先前端校验，再后端校验</strong>。基础内容完成后，再进行复杂信息的校验。</p>
<p><strong>校验出现以下3种情况，才会对应展示提示信息：</strong></p>
<p><strong>（1）Error错误类</strong></p>
<p>具有强打断性，如果错误内容未做修改，是不能继续提交进行下一阶段的，所以Error类是最先进行报错并提示的。</p>
<p><strong>（2）提示无需确认</strong></p>
<p>不会被强制打断，但是会作为普通提示告知用户。比如我们在校验用户身份信息时，会根据用户提供的证件类型来判断校验的内容，若用户未填写，需要提示用户必须先录入证件信息才能编辑其他内容。</p>
<p><strong>（3）提示需要确认</strong></p>
<p>具有打断性，这时的提示信息一定要给出用户明确提示，以及提交保存或确认后影响的内容。因为强打断，所以需谨慎。但是也不用畏手畏脚，该提示的必须提示，掌握好这个分寸。</p>
<p><strong>前端校验与后端校验提示信息出现的顺序基本一致</strong>：Error错误类 – 提示需确认&提示无需确认，<strong>只是前端无法调用复杂数据只能做简单的字段校验，而后端校验涉及到的是数据库保存的内容信息。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/iE90Cs9mwaRNFMyGN94s.png" width="518" height="221" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、校验提示的三类情况及表现形式</h2>
<p>校验后的提示信息一般伴随用户录入信息页面时出现（交互三原则之一：操作后有反馈），<strong>录入过程又分为录入中校验和阶段提交校验</strong>；<strong>提示信息也分为需要确认和无需确认两种情况</strong>。下面是综合两者进行的三种形式分类：</p>
<h3>1. 录入过程中，提示无需确认</h3>
<p>当信息录入中，有些小错误给用户简单的提示即可。比如“需要录入身份证信息，才能查看您的用户数据”，这时候给一个全局提示，不需要用弹窗、气泡卡片这种打断性强的内容。</p>
<p><strong>（1）提示无需确认使用的反馈组件</strong></p>
<p><strong>① 警告提示</strong></p>
<p><strong>基本定义和使用规则：</strong>展示需要关注的信息，适用于简短的警告提示。有用户操作触发或系统触发两种情况。警告提示有四种样式，带有底色，颜色更能吸引人的注意力，所以<strong>警告提示的内容优先级一般高于全局提示。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/yvy6re9kKAeIGvPrEGGb.png" width="534" height="179" referrerpolicy="no-referrer"></p>
<p><strong>为什么用：</strong>警告的信息的内容需要被用户确认，它会以非模态的展现形式，始终展现，不会自动消失，用户需要点击才能关闭。（根据业务产品需求，也会出现3s自动消失的情况，根据情节而定）</p>
<p><strong>② 全局提示</strong></p>
<p><strong>基本定义和使用规则：</strong>由用户的操作触发的“轻量级”全局反馈。默认3秒即消失</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/nOU7W5wpiVAo76eo7TDf.png" width="522" height="175" referrerpolicy="no-referrer"></p>
<p><strong>何时使用：</strong>用来提供成功、警告和错误等反馈信息，而且不会打断用户的操作。</p>
<p><strong>显示位置：</strong>页面顶部居中</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/zUZntPeLFumyQ6JPM5kZ.png" width="534" height="204" referrerpolicy="no-referrer"></p>
<h3>2. 录入过程中，提示需确认</h3>
<p>比如列表中的“删除”按钮，用户有可能不小心点击，这时候给一个气泡卡片，二次确认即可。</p>
<p>比如用户即将离开页面，但修改内容未做保存时，给用户二次确认，减少误操作的损失。</p>
<p>需要确认的原因：减少用户误操作、操作联动、影响用户下一流程的内容。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/sMi6ciU6lw7zqAzT2Sze.jpeg" width="531" height="178" referrerpolicy="no-referrer"></p>
<p><strong>（1）提示需确认常用的反馈组件</strong></p>
<p><strong>① 气泡卡片</strong></p>
<p><strong>基本定义和使用规则：</strong>点击后触发，弹出气泡式的确认框</p>
<p><strong>何时使用：</strong>气泡确认框是一种轻量的反馈方式，承载的内容也相对较少。主要用于二次确认操作。对比较为常规的对话框二次确认，气泡确认框从形式上更轻量，干扰更小，控件的打开关闭方式也更为便捷。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Dq2VXy89K6yb2udEWGbY.jpeg" width="530" height="162" referrerpolicy="no-referrer"></p>
<p><strong>显示位置：</strong>跟随内容展示，有12个方向供选择</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/wPeFzgjHGvhRtOl1Vsdy.jpeg" width="533" height="159" referrerpolicy="no-referrer"></p>
<p><strong>② 通知提醒框</strong></p>
<p><strong>基本定义和使用规则：</strong>用于向用户反馈重要的警告提示和通知消息。</p>
<p><strong>何时使用：</strong>一般用于系统级通知，需要吸引用户关注但又不强制用户去处理的场景。当消息出现时，用户可以选择继续当前操作，也可以选择处理当前消息。因为是系统级通知，所以显示位置也不用跟随操作，在指定的位置展示即可。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/RAHopAbKHMf7w10xxrp2.jpeg" width="534" height="198" referrerpolicy="no-referrer"></p>
<p><strong>显示位置：</strong>页面右上角</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/SkfFParapQpcm9iEhAuu.jpeg" width="539" height="206" referrerpolicy="no-referrer"></p>
<p><strong>③ 对话框（弹窗）</strong></p>
<p><strong>基本定义和类型：</strong>对话框是模态形式的浮层，在当前页面打开后承载相关操作。因为会中断用户当前的任务流程，所以需要谨慎使用，一般用于快捷且不需要频繁操作的任务，满足用户执行操作且不离开当前页面。</p>
<p><strong>对话框的类型有三种：功能对话框、确认对话框、消息提示对话框。</strong></p>
<p><strong>功能对话框：</strong>涉及到平台内容的录入，信息较为复杂，还会伴随步骤和反馈等等。</p>
<p>今天我们主要讲的是提示信息相关的反馈，也就是确认对话框、消息提示对话框这两种。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/MGBHBpGhAWjbNx6DDrz0.jpeg" width="536" height="199" referrerpolicy="no-referrer"></p>
<p><strong>何时使用：</strong>要求用户立即响应、通知用户紧急信息、确认用户决定时使用。</p>
<p><strong>显示位置：</strong>页面上下左右居中</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/1Q7csdF9V1jIh6xcfwBR.jpeg" width="539" height="206" referrerpolicy="no-referrer"></p>
<p><strong>④ 抽屉页面</strong></p>
<p>抽屉页还能承载提示信息？</p>
<p>没错！<strong>有时会因为业务的复杂关联性导致一个任务提交，触发多种校验提示</strong>。弹窗已经不能满足我们内容承载，我们需要使用抽屉页面来承载大量的提示信息，而且伴随分类和不同的提示话术。最后的案例会具体讲。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/ggCHy1G6X7mwVjxE3mL3.jpeg" width="534" height="204" referrerpolicy="no-referrer"></p>
<h3>3. 阶段性提交，提示需确认</h3>
<p><strong>提交成功</strong>，给一个弹窗（对话框）明确告知用户已成功提交，必要时配图，培养用户的操作习惯和对品牌的感知。但这仅仅是用于多步骤录入或大量信息录入时使用，简单的录入不需要这样“声势浩大”的提交反馈。</p>
<p><strong>提交失败</strong>，给出明确的错误原因和错误引导。如果错误内容数量多，种类多，可进行分类展示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/DnDutlRcBPHnUoGj1j3x.jpeg" width="524" height="174" referrerpolicy="no-referrer"></p>
<p><strong>（1）阶段性提交，提示需确认常用的反馈形式</strong></p>
<p>当商户入驻虾皮，需要填写关于个人身份、店铺详情等信息，分步骤填写并提交保存时，视为阶段性提交。</p>
<p>当然这只是比较简单的形式，<strong>相信很多B端从业的伙伴们都见过超长表单，当表单过长，系统进行阶段性提交就会触发比较多的提示信息</strong>。</p>
<p>所以下面讲解的是常见的三种阶段性提交，系统反馈的提示信息类型：</p>
<p><strong>① 只触发一项内容需要校验并修改时 – 单条信息 – 对话框</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/VqYJnk6p1xH7vEfRU87k.jpeg" width="530" height="158" referrerpolicy="no-referrer"></p>
<p><strong>② 触发一项以上内容需要校验 – 多条信息对话框聚合</strong></p>
<p>用总结性话术，帮助用户确认所有提示信息，比如【具体修改内容描述，可自定义的一句话】修改影响以下内容，是否确认？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/xmRyAts4oFjnn8EM3wJa.jpeg" width="519" height="233" referrerpolicy="no-referrer"></p>
<p><strong>③ 内容过多需要逐个确认- 用抽屉页面承载 – 同时考虑是否一个折叠入口</strong></p>
<p>根据业务诉求，有2点体验细节需要考虑：</p>
<ol>
<li>内容过多，用户需要一一查看，有时无法一次性确认，可以给一个折叠入口，方便用户再次确认</li>
<li>但是用户每次提交都会给出最新的校验后提示信息，所以“折叠入口”也不是非要有，根据业务需求来决定</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/ehdVNN0QLrM9KzBjpUS5.jpeg" width="521" height="329" referrerpolicy="no-referrer"></p>
<p>以上是提示信息常用的反馈组件，下面这张图是关于反馈的强度和提示时间的对比：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/rEycbz3MN1FAOKFskArq.png" width="537" height="176" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、信息反馈的设计原则</h2>
<h3>1. 轻量化</h3>
<p>关于轻量化，不得不提的是非模态提醒。那么模态与非模态又有什么区别呢？</p>
<p><strong>（1）模态</strong></p>
<p><strong>用户在完成任务的过程中，界面会出现弹窗打断用户的操作行为</strong>，用户必须通过主动点击才可以进行下一步操作，这即是模态弹窗。</p>
<p><strong>① 优点</strong></p>
<p><strong>模态弹窗通常能较好的获取用户的视觉焦点</strong>，并通过承载的内容、按钮主次层级来引导用户完成他们的需求，这也会根据用户、产品侧重点的不同，弹出样式也有所不同。</p>
<p>常见的模态弹窗有对话框、动作栏、抽屉…等。</p>
<p><strong>② 缺点</strong></p>
<p><strong>模态是一种强打断的形式</strong>，直接打断用户录入的过程非常“不礼貌”，会导致用户反感，若非必要情况下不要使用。<strong>非必要不模态。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/ji5gvvmadBDXYJsjvSwC.png" width="536" height="225" referrerpolicy="no-referrer"></p>
<p><strong>（2）非模态</strong></p>
<p><strong>相比模态弹窗，非模态提示较为轻量，触发后以一种非阻碍的的方式呈现，不会打断用户的当前操作，</strong>主要是给予用户即时反馈，让用户清楚应用当前的交互后状态。</p>
<p><strong>优点：</strong>非模态弹窗不强制用户操作，根据反馈信息的重要程度及意愿，可在一定的时间内自动消失，也可等待用户操作后消失。</p>
<p><strong>（3）常见非模态</strong></p>
<p>前面我们讲过的气泡卡片、全局提示、警告提示都是常见的非模态提示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/XKedhbUiMayeuBjuKcGw.png" width="523" height="219" referrerpolicy="no-referrer"></p>
<h3>2. 精准化</h3>
<p><strong>（1）文案清晰</strong></p>
<p>引导文案一定要清晰有效，不要说了半天用户无法理解。</p>
<p><strong>（2）目标清晰</strong></p>
<p>我们需要帮助用户完成目标，直接给出“友好”的目标提示。</p>
<p><strong>（3）引导清晰</strong></p>
<p>对于复杂业务场景，给出“新手引导”式有指向性的提示，帮助用户理解、方便用户操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/XkQLlFCyzfXKHNNYHETX.png" width="520" height="284" referrerpolicy="no-referrer"></p>
<h3>3. 高效化</h3>
<p><strong>（1）节省时间</strong></p>
<p>能在前端校验的内容不要放到后端校验，减少后端校验时的反馈时间。</p>
<p><strong>（2）聚合反馈</strong></p>
<p>能一次提示清楚内容不要分多个反馈组件出现，会让“眼花缭乱”无法识别。</p>
<p><strong>（3）读取效率</strong></p>
<p>能分类的、能明确错误模块的一定要给到，方便用户快速定位错误区域。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/7QMluMVgtbBzL6zghzKp.png" width="536" height="293" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、复杂案例带练</h2>
<p>说了这么多，可能还是有点懵，下面我有一个复杂案例带大家拆解。</p>
<p><strong>案例介绍：</strong></p>
<ul>
<li><strong>业务特点</strong>：流程型业务，涉及多个操作角色，每一环节叠加内容</li>
<li><strong>内容特点</strong>：复杂表单录入，涉及内容联动，“牵一发而动全身”</li>
<li><strong>涉及模块</strong>：页面录入、触发编辑态录入、抽屉录入</li>
</ul>
<h3>1. 模块保存-校验规则/交互规范</h3>
<ol>
<li>点击“修改”，激活模块内容，内容由只能查看，变为可以编辑的状态</li>
<li>当内容有修改时，点击“取消”触发前端校验，给用户一个气泡确认的反馈，告知用户有内容未保存</li>
<li>点击“保存”，触发后端校验，后端校验需要时间（一般不超过5s）</li>
<li>这时“保存”变成“加载状态”，“取消”按钮不可点击</li>
<li>提示需求确认的信息使用“全局提示”给用户反馈</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/hHdpdLPMRRlANv0Ly4qk.png" width="532" height="400" referrerpolicy="no-referrer"></p>
<h3>2. 阻断类：校验提示信息</h3>
<p>阻断：不修改正确无法继续进行下一步流程。这时候我们的提示信息要给出明确指导提示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/r56KdzaI6WSVrHDx3PAN.png" width="529" height="277" referrerpolicy="no-referrer"></p>
<h3>3. 抽屉提交/保存-校验规则/交互规范</h3>
<p>使用抽屉页录入信息并提交或保存时，一般有两种结果，成功或失败。保存成功的反馈比较简单我们就不细讲了。</p>
<p><strong>提交成功/保存成功</strong> ：关闭弹窗并给到全局提示</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/Fu1KTafvsBpOaYhPnUrG.png" width="525" height="268" referrerpolicy="no-referrer"></p>
<p><strong>而提交失败含有两种情况：</strong></p>
<ol>
<li>第一种情况：校验出错误，需要修改后重新提交</li>
<li>第二种情况：无错误信息，但是有些内容修改会出现联动变化，需要用户进行确认才能保存。</li>
</ol>
<p>当提示信息有且只有一条，用一个对话框进行展示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/GwHJRv7MBvCzS1Rev7cM.png" width="555" height="273" referrerpolicy="no-referrer"></p>
<p>若提示需确认信息超过2条，使用抽屉聚合。通过信息分类和专业的话术方案帮助用户决策。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/ZgNXjaCIq97p1lqxO67I.png" width="546" height="269" referrerpolicy="no-referrer"></p>
<h3>4. 页面提交/保存-校验规则/交互规范</h3>
<p>录入信息超过一屏，在进行保存提交时，如果触发超过2条及以上的报错、提示信息，我们会用抽屉页面去展示。依然保持错误类型、内容模块的分类。</p>
<ol>
<li><strong>错误类型</strong>：普通提示、需确认</li>
<li><strong>内容模块：</strong>基本信息、账户信息、支付信息等录入时涉及到的具体模块</li>
<li><strong>提示信息内容</strong>：文案话术尽可能的简洁易懂，做到多一个字少一个字都会影响阅读的程度</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/06/0EIUvzvvEsqUQblA9Avh.png" width="536" height="339" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、文章总结</h2>
<p><strong>B端交互体验的魅力在于“解决问题，提升操作效率，降低工作成本”</strong>，但常常因为业务本身的复杂性而屡屡受挫。</p>
<p>就像我们之前可能认为“很简单”的提示信息和校验规则，在跟产品经理、前后端小伙伴们讨论拆解中竟也能发现如此多需要注意的细节点。</p>
<p><strong>下面我尝试用3句话总结文章重点：</strong></p>
<ol>
<li>校验顺序：先前端再后端。</li>
<li>提示规则：阻断类先行；提示无需确认随时可能出现；提示需确认必须出现。</li>
<li>提示信息在校验后出现，结合业务需求考量，使用操作效率更高的的反馈组件，非必要不出现。</li>
</ol>
<p> </p>
<p>本文由 @EllieOne 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5508119" data-author="880323" data-avatar="http://image.woshipm.com/wp-files/2022/05/gKfqx1lLKJ8sV3OXRewR.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            