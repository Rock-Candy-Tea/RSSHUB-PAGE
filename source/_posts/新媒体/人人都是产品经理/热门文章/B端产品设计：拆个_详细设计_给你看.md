
---
title: 'B端产品设计：拆个_详细设计_给你看'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/C36RbGYxSRhSYWbiC3nv.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 22 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/C36RbGYxSRhSYWbiC3nv.jpg'
---

<div>   
<blockquote><p>编辑导语：产品详细设计，是对产品的具象化呈现，是向研发团队展示产品的实现逻辑、业务规则等内容。本文作者从建立业务模型、确认系统底层结构、系统操作流程三个步骤，拆解了“详细设计”，希望看后对你的B端产品设计会有所帮助。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4482295" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/C36RbGYxSRhSYWbiC3nv.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在整体解决方案中完成了产品定位和规划等工作（整体方案详见上一篇），也明确了产品在不同阶段分别要实现的功能模块，接下来的产品详细设计由此展开。</p>
<p>什么是产品详细设计？是对产品的具象化呈现，是向研发团队展示产品的实现逻辑、业务规则等内容。在呈现内容上需要保持简洁明了，将复杂的逻辑通俗且直观的表达出来，让其他成员更容易理解。</p>
<p>在实际操作中，我们可以通过3个步骤依次分解：</p>
<ol>
<li>通过“建立业务模型”确认系统底层结构；</li>
<li>通过“系统操作流程”描述用户执行任务的路径；</li>
<li>通过“绘制产品原型”呈现产品的界面、交互、规则。</li>
</ol>
<p>接下来开始我的表演。</p>
<h2 id="toc-1">一、建立业务模型</h2>
<p>建系统犹如建房子，先确定房子的框架，然后打地基、搭钢架、添砖加瓦。</p>
<p>在整体方案中确定了系统框架，详细设计将从打地基开始，而不是一上来就添砖加瓦。建立业务模型就是系统的“打地基”，直接影响系统底层结构。后续的详细设计是在业务模型下进行拓展，如果业务模型设计偏差，系统从开始也就歪了。</p>
<p>注意：一旦底层的业务模型涉及大范围调整，则后续设计和开发都将受到严重影响。业务模型的建立也是对底层数据归类的过程，可以从3个步骤来实现，并通过ER图或其他方式进行展示。</p>
<ol>
<li>要素抽离：根据之前梳理的业务流程进行再次抽象，提取流程中出现的关键业务要素；</li>
<li>2找准关系：罗列关键业务要素，结合业务逻辑找到关键要素之间的关联关系；</li>
<li>设计模型：考虑业务诉求、资源限制、系统拓展性等情况，设计出对应模型。同时配备对应文字解读，避免看图出现遗漏信息。</li>
</ol>
<p>举例：Z公司TMS项目中，通过访谈方式对业务流程进行了全面梳理。部分业务流程为：计划员创建运单任务（订单），调度员根据订单的运输量、物料等要素对运单进行拆分或合并，再根据承运资源池中不同车辆任务分配情况指派给对应司机生成车次。</p>
<p>在梳理过程中找到了诸多要素，部分关键要素为：订单、运单、车次。下图以简化版的业务模型为例，看看不同图形表达的呈现效果。</p>
<p><img data-action="zoom" class="aligncenter" style="letter-spacing: 0.16px;" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/eRNeDGfSFtQuaywQ4F2g.png" alt width="803" height="106" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图1</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/UyBh6Rg60XKPqLtYrtLX.png" alt width="802" height="387" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2</p>
<p>上图中，业务模型想要表达以下信息：</p>
<ol>
<li>1个订单可以和1个或多个运单进行关联；</li>
<li>1个或多个运单可以和1个车次进行关联；</li>
<li>来自不同订单产生的运单可以关联到同1个车次。</li>
</ol>
<h2 id="toc-2">二、系统操作流程</h2>
<p>经过业务模型了解了业务关键要素关系，接下来可以着手系统操作流程设计。流程合理、角色任务清晰是系统设计成功的前提。我们应遵循从业务起点至终点、从主流业务到分支业务、从正向流程到逆向流程的设计思路，同时考虑各任务的逻辑先后顺序和依赖关系。</p>
<p>系统操作和业务是存在着对应关系，都是由一个个任务衔接而成，可以从角色和任务2个维度来拆解，并通过跨部门流程图+备注进行展示。单个环节可以从以下4点细化：</p>
<ol>
<li>参与角色：对应任务的参与角色，包含了人员或物体（如设备、单据等）；</li>
<li>任务触发：满足什么样的条件来触发对应任务的执行，如预设的执行时间、上游的输出物等；</li>
<li>任务执行：在当前任务中，参与角色需要完成的事项；</li>
<li>结果输出：事项完成后产生了什么交付物，并通过什么方式向下游进行传递。</li>
</ol>
<p>系统操作流程确定后就可以绘制页面流转图，即用户完成对应任务需要访问的页面及页面跳转的顺序，页面流转图可以更好的帮助团队成员理解用户的操作行为路径。</p>
<p>举例：Z公司TMS项目中，通过对业务模型的完善，接下来对订单、运单、车次的简化版系统操作进行描述。我们通过Visio的多泳道流程图来呈现，并配上关键节点的文字描述。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/KXS8NS1jlKvNdFWZ4Me5.png" alt width="902" height="506" referrerpolicy="no-referrer"></p>
<h3>1. 创建订单</h3>
<ul>
<li>角色：计划员</li>
<li>描述：通过在系统后台手动创建，或者是通过Excel表单导入，把排产计划转变为订单。</li>
</ul>
<h3>2. 订单审核</h3>
<ul>
<li>角色：计划员</li>
<li>描述：订单创建之后，需要管理员进行审核，确认订单内容没有错误审核通过之后，系统会自动生成运单。</li>
</ul>
<h3>3. 运单拆分</h3>
<ul>
<li>角色：调度员</li>
<li>描述：运单生成之后，当运单的物料过多，一辆车装不下的时候，可以进行运单拆分，将运单拆为多单。</li>
</ul>
<h3>4. 运单指派</h3>
<ul>
<li>角色：调度员</li>
<li>描述：运单确认无误后，可以指派对应的车辆和司机去执行这个运单。支持1单1车和多单1车。</li>
</ul>
<h3>5. 调度审核</h3>
<ul>
<li>角色：调度员</li>
<li>描述：审核运单指派的车辆和司机，确认调度无误后即可执行。</li>
</ul>
<h3>6. 生成车次</h3>
<ul>
<li>角色：调度员</li>
<li>描述：运单指派审核通过之后，系统自动生成车次。同时支持打印派车单。</li>
</ul>
<h3>7. 运输执行</h3>
<ul>
<li>角色：司机</li>
<li>描述：司机接到车次任务之后进入运输执行环节。包含到达取货点、已装车、到达送货点、已签收等多个环节。</li>
</ul>
<h2 id="toc-3">三、绘制产品原型</h2>
<p>经过了业务模型、系统操作流程、页面流转图等相关内容的输出，已经做到了对产品从全局到细节的全面了解，最后输出PRD交付研发团队即可。</p>
<p>产品原型是PRD的重要组成部分之一，原型需要将系统页面元素和排版、交互效果、系统规则等信息通过简单明了的方式进行展现，帮助团队成员更好地理解需要实现的效果。</p>
<p>原型工具有很多，如Axure、墨刀、摹客等。</p>
<p>在绘制原型图时将需要的元素和排版表达到位即可，堪比UI稿的高保真原型是没有必要的。比如配色可使用黑、白、灰、蓝、红进行表达，复杂配色对研发和UI团队来说并不一定友好，同时也会消耗自己大量的时间资源。</p>
<p>B端产品系统主要由4类页面组成，通过了解页面类型设计时可以结构化的组织信息，便于向用户提供可预期的操作，降低使用成本。如下：</p>
<ul>
<li>表单页：用户在系统中进行新增、删除、修改等提交信息动作的操作页面。如登录页，提交用户名和密码；</li>
<li>详情页：系统向用户展示对应详细信息的页面。如任务详情页，展示任务编号、时间、状态、内容等信息；</li>
<li>列表页：系统向用户展示对应同类型的数据信息。如任务列表页，展示编号、名称、状态、操作等字段；</li>
<li>图表页：系统向用户展示综合型页面，此类页面多有图形和表单构成，常见如数据分析页面。</li>
</ul>
<p>举例：Z公司TMS项目中，以运单管理为例展示运单列表页、运单详情页、指派司机弹窗的原型及对应规则备注（示例中的原型和规则备注方式还可以进行优化）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/AMOqOork5z2Em0hstPU8.png" alt width="1004" height="436" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图1：运单列表页</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/i7Dgg4CxuaDMsIwZ1rXK.png" alt width="1000" height="729" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2 ：运单详情页</p>
<p><img data-action="zoom" class="aligncenter" style="letter-spacing: 0.16px;" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/u96sPvwhrSx6hSBrm7EU.png" alt width="998" height="341" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><img data-action="zoom" src="https://cors.zfour.workers.dev/?http://www.woshipm.com/pd//Users/Perfect/AppData/Local/YNote/data/qq07B4EA9A6F3F9D6B315B129AED8F1158/82b5b46603744e83abe91d1c3a2afc20/3.png" alt referrerpolicy="no-referrer">图3：指派司机弹窗</p>
<p>交互设计关注点：</p>
<ul>
<li>遵循“尼尔森十大可用性原则”：从多个方面保障交互的合理性、可用性、友好性，甚至可以在设计完成后进行复查；</li>
<li>不建议设计复杂交互：B端产品目的在于帮助企业解决业务问题，交互优先级并不高，复杂交互不利于用户操作同时也过多占用研发资源；</li>
<li>采用标准模板和控件：行业内会很多成熟的商业软件，获得了用户认可，可以借鉴系统布局、交互方式等，帮助提高设计效率。</li>
</ul>
<p>以上。</p>
<p> </p>
<p>本文由 @耳目不染 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4481339" data-author="931453" data-avatar="http://image.woshipm.com/wp-files/2021/02/VLOpbBtxfckKwYuglYt7.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182702_3295.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            