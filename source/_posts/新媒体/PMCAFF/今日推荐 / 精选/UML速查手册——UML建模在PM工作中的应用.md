
---
title: 'UML速查手册——UML建模在PM工作中的应用'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://img.pmcaff.com/Fj-aDA2pMpUZDxU21ymV_KstvyzT-picture'
author: PMCAFF
comments: false
date: Sun, 08 Aug 2021 22:07:58 GMT
thumbnail: 'https://img.pmcaff.com/Fj-aDA2pMpUZDxU21ymV_KstvyzT-picture'
---

<div>   
<pre><style>
#articleCont &#123;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  word-wrap: break-word;
&#125;
#articleCont :first-child &#123;
  margin-top: 0 !important;
&#125;
#articleCont h1,
#articleCont h2,
#articleCont h3,
#articleCont h4,
#articleCont h5,
#articleCont h6 &#123;
  margin: 40px 0 20px;
&#125;
#articleCont h1 &#123;
  font-size: 24px;
&#125;
#articleCont h2 &#123;
  font-size: 22px;
&#125;
#articleCont h3 &#123;
  font-size: 20px;
&#125;
#articleCont h4 &#123;
  font-size: 18px;
&#125;
#articleCont h5 &#123;
  font-size: 16px;
&#125;
#articleCont i &#123;
  font-style: italic;
&#125;
#articleCont p,
#articleCont div &#123;
  word-wrap: break-word;
  margin: 14px 0;
  text-align: justify;
&#125;
#articleCont blockquote &#123;
  border-left: 6px solid #ddd;
  padding: 5px 0 5px 10px;
&#125;
#articleCont blockquote p:last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont .simditor-body blockquote :last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont a &#123;
  color: #82b64a;
&#125;
#articleCont a:visited &#123;
  color: #82b64a;
&#125;
#articleCont a:hover &#123;
  color: #74a342;
&#125;
#articleCont img &#123;
  max-width: 100%;
  height: auto;
&#125;
#articleCont hr &#123;
  margin: 19px 0;
  border: none;
  border-top: solid 1px #ddd;
&#125;
#articleCont ol &#123;
  list-style-type: decimal;
&#125;
#articleCont ol li &#123;
  list-style-type: decimal;
&#125;
#articleCont ul &#123;
  list-style-type: disc;
  padding-left: 40px;
&#125;
#articleCont ul li &#123;
  list-style-type: disc;
&#125;
#articleCont table &#123;
  width: 100%;
  font-size: 12px;
  border-collapse: collapse;
  line-height: 1.7;
&#125;
#articleCont table thead &#123;
  background: #f9f9f9;
&#125;
#articleCont table th,
#articleCont table td &#123;
  border: solid 1px #ccc;
  text-align: left;
  vertical-align: top;
  padding: 2px 4px;
  height: 30px;
  min-width: 40px;
  box-sizing: border-box;
&#125;
#articleCont pre &#123;
  white-space: pre-wrap;
&#125;
</style><p>UML为什么在产品工作中应用？能解决产品经理工作上的哪些痛点？</p><p style="text-align:center;"><img alt="v2-38fd243a16a34ac59ff8002c040f8254_1440w.jpg" src="https://img.pmcaff.com/Fj-aDA2pMpUZDxU21ymV_KstvyzT-picture" width="1134" height="442" coffee-w="1134px" coffee-h="442px" coffee-format="png" referrerpolicy="no-referrer"><br></p><h1>一、先看图例<br></h1><p>是否在工作中见过这些图呢？是否在偏技术型的文档中见过这些图？</p><p>1、这是一张“用户-角色-权限”关联关系图，表达了“表”与“表”之间的关系；属于类图。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/bbc42155fe003287c84555d2b83710b1-picture" alt="bbc42155fe003287c84555d2b83710b1-picture" coffee-w="720px" coffee-h="407px" coffee-format="png" referrerpolicy="no-referrer"></p><p>2、这是一张拼团产品中“用户-团-权益”的对应关系图，以及每个业务概念的属性字段与操作；同样属于类图。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/f996a810eef03fe12e9fe59f3df5fb98-picture" alt="f996a810eef03fe12e9fe59f3df5fb98-picture" coffee-w="720px" coffee-h="433px" coffee-format="png" referrerpolicy="no-referrer"></p><p>3、这是一张表达相对独立的功能间的关系图，表达了一个功能模块的输入与输出，及与另一个功能模块间的供需关系；属于构件图。</p><p><img src="http://img.pmcaff.com/34f72864b6209268ff5ad329480bf9c5-picture" alt="34f72864b6209268ff5ad329480bf9c5-picture" coffee-w="682px" coffee-h="372px" coffee-format="png" referrerpolicy="no-referrer"></p><p>4、这是一张表达服务器、数据库、使用网络地域范围的部署图。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/5907f296c5bae524178a19cac630ccbb-picture" alt="5907f296c5bae524178a19cac630ccbb-picture" coffee-w="560px" coffee-h="304px" coffee-format="png" referrerpolicy="no-referrer"></p><p>5、这是一张以“员工申请立项，三个领导审批”事件为主的流程图。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/a2cbf7e3cab719747b378f9d42a7ed3d-picture" alt="a2cbf7e3cab719747b378f9d42a7ed3d-picture" coffee-w="720px" coffee-h="380px" coffee-format="png" referrerpolicy="no-referrer"></p><p>6、这是上图中“审批单”的状态变化图，学名：状态机图。表达了审批单在不同用户的操作下的触发的状态变化。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/bda94ed018d54f435af473a7f8ac12c8-picture" alt="bda94ed018d54f435af473a7f8ac12c8-picture" coffee-w="720px" coffee-h="420px" coffee-format="png" referrerpolicy="no-referrer"></p><p>7、这是一张用户在注册账户过程中“用户-前端界面-后端系统-数据库”之间的交互及信息传递图，学名顺序图，主要用来表达复杂的交互、系统与系统之间的交互。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/62bcc3d8ecd7274a6d1950d43451f163-picture" alt="62bcc3d8ecd7274a6d1950d43451f163-picture" coffee-w="606px" coffee-h="372px" coffee-format="png" referrerpolicy="no-referrer"></p><p>8、这是一张表达了某系统范围内三种角色各自可操作的用例，以及角色与角色之间的继承关系，属于用例图。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/7aae73217048a7942b37286905003ee1-picture" alt="7aae73217048a7942b37286905003ee1-picture" coffee-w="478px" coffee-h="453px" coffee-format="png" referrerpolicy="no-referrer"></p><p>看完上面7种图，感觉流程图最熟悉了，其他的几种图似曾相识。那么，其他的图有什么作用呢？先看看我们工作中的痛点。</p><h1>二、产品经理工作中的痛点<br></h1><ol><li>业务分析时，范围不清晰，逻辑不严谨，或自己的方案超出技术边界。<br></li><li>刚接手一个产品时，弄不清一个概念与另一个概念的对应关系、关联关系，同事也不能系统地给你讲述全面。<br></li><li>需求文档中，文字描述很清楚，但程序员搞不清楚也不爱看文字。<br></li><li>经常听到程序员说：我们没有这张表、没有这个字段，这里接口对不上。<br></li><li>和程序员讨论最多的也是：如果用户这样操作了该显示什么状态？该怎么提示？<br></li></ol><p>怎么才能在避免这些问题呢？—— 利用UML作为沟通语言、利用UML图作为思考工具。</p><h1>三、UML是什么<br></h1><p><b>1、What：是什么？</b></p><ul><li>UML，Unified Modeling Language，统一建模语言。<br></li><li>建模的输出主要是图的形式，分为两类，一种是结构型图、一种是行为型图。<br></li><li>我们常画的流程图就是一种行为型的UML。<br></li></ul><p><b>2、Who：谁来用？</b></p><ul><li>产品经理（需求分析时可画出简易版的UML图）<br></li><li>程序员（学技术的都能看懂ULM，甚至可以和程序员一起完善UML）<br></li></ul><p><b>3、When：产品经理什么时候用到UML？</b></p><ul><li>业务分析提炼需求、挖掘需求时<br></li><li>与技术人员交流时<br></li></ul><p><b>4、Where：用在什么地方？</b></p><ul><li>业务分析</li><li>需求文档<br></li><li>.......</li></ul><p><b>5、Why：为什么要用？</b></p><ul><li>作为一种工具可以帮助产品经理完整无遗漏地梳理需求。<br></li><li>作为一种语言，可以清晰易懂，与技术人员顺畅沟通。<br></li><li>作为以图形为主的语言，更形象易懂。<br></li></ul><h1>四、产品工作中常用的UML有哪些？<br></h1><p style="text-align:center;"><img src="http://img.pmcaff.com/e2ad56c601a2be151f53a129bb4820e6-picture" alt="e2ad56c601a2be151f53a129bb4820e6-picture" coffee-w="635px" coffee-h="707px" coffee-format="png" referrerpolicy="no-referrer"></p><p>最常用的是：流程图、状态机图、顺序图、用例图、类图</p><h1>五、各类UML图的语法<br></h1><ul><li>学习网站：uml.org.cn/oobject/OObject.asp</li><li>学习书籍：《UML大战需求分析》</li></ul><h2>（一）类图<br></h2><h3>1、什么是类</h3><p>类是面向对象的，里面有属性、有操作。通俗讲一个类就是一个业务概念、就是一张表。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/c25a07af0342502811fa7a7c62409a0d-picture" alt="c25a07af0342502811fa7a7c62409a0d-picture" coffee-w="142px" coffee-h="152px" coffee-format="png" referrerpolicy="no-referrer"></p><p>在表达类与类之间关系时，一般隐藏属性和操作，只用类名代表一个类。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/dc87d107347633d413e4bfd774d06124-picture" alt="dc87d107347633d413e4bfd774d06124-picture" coffee-w="153px" coffee-h="56px" coffee-format="png" referrerpolicy="no-referrer"></p><h3>2、语法</h3><p>在类图的表达中，一定要注意箭头的区别</p><p style="text-align:center;"><img src="http://img.pmcaff.com/3983e0bc923465d1a66c2f2f8497211b-picture" alt="3983e0bc923465d1a66c2f2f8497211b-picture" coffee-w="720px" coffee-h="353px" coffee-format="png" referrerpolicy="no-referrer"></p><h4>（1）关联关系</h4><p>a、用直线相连接，代表两个类之间有关联关系，当不确定具体关系时，均先用直线链接；直线两端的数字代表对应的数量关系，如下：</p><p style="text-align:center;"><img src="http://img.pmcaff.com/6d6219a8a2db0a87d6f0ec5080e4b1df-picture" alt="6d6219a8a2db0a87d6f0ec5080e4b1df-picture" coffee-w="419px" coffee-h="44px" coffee-format="png" referrerpolicy="no-referrer"></p><p>代表1个G可以0～3个M，如一个拼团除了团长可以有0～3个团员。</p><ul><li>b、导航关系<br></li></ul><p style="text-align:center;"><img src="http://img.pmcaff.com/1aa7363ccc024155dd5562022c6f0a8c-picture" alt="1aa7363ccc024155dd5562022c6f0a8c-picture" coffee-w="394px" coffee-h="41px" coffee-format="png" referrerpolicy="no-referrer"></p><p>代表由A可以导航到B，通俗讲是由A可以找到B，如：在拼团名单中可以找到参与用户。</p><h4>（2）聚合关系，即弱包含关系</h4><h4 style="text-align:center;"><img src="http://img.pmcaff.com/17445331f9de2fca722ef6f20d745491-picture" alt="17445331f9de2fca722ef6f20d745491-picture" coffee-w="384px" coffee-h="41px" coffee-format="png" referrerpolicy="no-referrer"></h4><p>代表一个部门可以由多个员工组成，如果部门没了，员工可继续存在。</p><h4>（3）组合关系，即强包含关系</h4><h4 style="text-align:center;"><img src="http://img.pmcaff.com/aac158a9fd8ae22fb3932515607e47b5-picture" alt="aac158a9fd8ae22fb3932515607e47b5-picture" coffee-w="381px" coffee-h="45px" coffee-format="png" referrerpolicy="no-referrer"></h4><p>代表一个部门可以由多个员工组成，如果部门没了，员工也就没了。</p><h4>（4）泛化关系</h4><p style="text-align:center;"><img src="http://img.pmcaff.com/afce1a8b1f4668cc8fd4ec6f196ed6c5-picture" alt="afce1a8b1f4668cc8fd4ec6f196ed6c5-picture" coffee-w="408px" coffee-h="42px" coffee-format="png" referrerpolicy="no-referrer"></p><p>代表A泛化为B，A具备B的特点，也有自己的特有特点，如香蕉泛化为水果。</p><h4>（5）依赖关系</h4><p style="text-align:center;"><img src="http://img.pmcaff.com/f800c21881fd58352361356695fc6e8b-picture" alt="f800c21881fd58352361356695fc6e8b-picture" coffee-w="402px" coffee-h="39px" coffee-format="png" referrerpolicy="no-referrer"></p><p>代表A依赖于B，对于某件事，A需要B的协助才能完成。</p><h3> 3、类图建模的步骤：</h3><ul><li>识别类，先记下类的名称<br></li><li>识别出类的主要属性、操作<br></li><li>描绘出类之间的关系<br></li><li>对各类进行分析、抽象、整理<br></li></ul><p>这个图是网上找的，箭头使用不是很规范。切记要使用类图语法中的箭头。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/4847b50c993f613b9c09f881a7609739-picture" alt="4847b50c993f613b9c09f881a7609739-picture" coffee-w="720px" coffee-h="373px" coffee-format="png" referrerpolicy="no-referrer"></p><h2>（二）构件图<br></h2><h2>1、什么是构件？</h2><p><img src="http://img.pmcaff.com/1e45750dab73f1ea48ad031c984aa5d5-picture" alt="1e45750dab73f1ea48ad031c984aa5d5-picture" coffee-w="720px" coffee-h="201px" coffee-format="png" referrerpolicy="no-referrer"></p><h2>2、语法</h2><p>（1）一个构件符号如下。服务接口像一个手一个拳头，可联系记忆为：伸手要服务，出拳打人服务。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/4d8a2d2fc621e3989fafcbdaaf8ae29b-picture" alt="4d8a2d2fc621e3989fafcbdaaf8ae29b-picture" coffee-w="172px" coffee-h="146px" coffee-format="png" referrerpolicy="no-referrer"></p><p>（2）两个构件之间的对接如下：</p><p style="text-align:center;"><img src="http://img.pmcaff.com/20d1aa9d6a0655663fbba0172ed67dd2-picture" alt="20d1aa9d6a0655663fbba0172ed67dd2-picture" coffee-w="476px" coffee-h="91px" coffee-format="png" referrerpolicy="no-referrer"></p><p>（3）示例如下：</p><p style="text-align:center;"><img src="http://img.pmcaff.com/53f6a4e9a9e786e0d2c6bfc7a631733a-picture" alt="53f6a4e9a9e786e0d2c6bfc7a631733a-picture" coffee-w="673px" coffee-h="355px" coffee-format="png" referrerpolicy="no-referrer"></p><h2>（三）部署图<br></h2><p>产品经理一般需要搞清楚：</p><ul><li>服务器部署在哪里？数据库放在哪里？</li><li>是互联网还是局域网？</li></ul><p style="text-align:center;"><img src="http://img.pmcaff.com/8abc6b2432def805ec0c2067faeaeed8-picture" alt="8abc6b2432def805ec0c2067faeaeed8-picture" coffee-w="556px" coffee-h="280px" coffee-format="png" referrerpolicy="no-referrer"></p><h2>（四）活动图（流程图）<br></h2><p>活动图比较常用，不做太多讲述，但在画图时一定要规范，如每个活动用“主动宾”的表达方式，当采用泳道图，有角色泳道时，可以省略“主语”。</p><h3>1、语法</h3><h2 style="text-align:center;"><img src="http://img.pmcaff.com/bca94cf4a487db53949a2a1f5e17969c-picture" alt="bca94cf4a487db53949a2a1f5e17969c-picture" coffee-w="720px" coffee-h="538px" coffee-format="png" referrerpolicy="no-referrer"></h2><h3>2、绘制步骤</h3><ul><li>明确该流程要表达怎么样的业务目的？<br></li><li>该流程有什么角色？<br></li><li>画出正常情况下的流程，是流程的主干，一般是线性的流程。<br></li><li>明确主干流程中的角色与活动<br></li><li>逐步增加分支流程，将关键的流程分支画出，部分异常流程可简单画出并用文字说明<br></li><li>适当控制活动粒度<br></li><li>优化流程<br></li></ul><h2>（五）状态机图<br></h2><p>状态机图是从某个事物的状态是如何变化的角度来展示流程。在触发行为描述时也要严格采用“主动宾”的表达方式。</p><h3>1、语法</h3><ul><li>开始状态<br></li><li>结束状态<br></li><li>状态框：一个圆角矩形框代表一个状态，框内文字为状态名称。<br></li><li>转换：状态与状态之间的箭头叫做转换，箭头上的文字说明发生了什么事情导致状态发生了变化。<br></li></ul><p style="text-align:center;"><img src="http://img.pmcaff.com/124d2ce074a483649171e7e1589603ec-picture" alt="124d2ce074a483649171e7e1589603ec-picture" coffee-w="720px" coffee-h="419px" coffee-format="png" referrerpolicy="no-referrer"></p><h3>2、步骤</h3><ul><li>状态机图与流程图的目的相似，只不过是以某一事物为主，所以开始时先画流程图，根据流程图画状态机图<br></li><li>明确参与的角色<br></li><li>明确该事物有什么状态<br></li><li>明确状态在什么角色的什么动作下触发变化<br></li></ul><h2>（六）顺序图<br></h2><h3>1、基本语法</h3><p style="text-align:center;"><img src="http://img.pmcaff.com/6fae6daa0a2769d6fa2b8da24c0c7b2b-picture" alt="6fae6daa0a2769d6fa2b8da24c0c7b2b-picture" coffee-w="649px" coffee-h="314px" coffee-format="png" referrerpolicy="no-referrer"></p><p style="text-align:center;"><img src="http://img.pmcaff.com/207b22407e596a0df578beddc01c0a02-picture" alt="207b22407e596a0df578beddc01c0a02-picture" coffee-w="704px" coffee-h="139px" coffee-format="png" referrerpolicy="no-referrer"></p><p>   顺序图的读法是：从上到下，从左到右。如下案列：</p><p style="text-align:center;"><img src="http://img.pmcaff.com/d9ac0b03909632e11f3f228b0f30c8d2-picture" alt="d9ac0b03909632e11f3f228b0f30c8d2-picture" coffee-w="329px" coffee-h="495px" coffee-format="png" referrerpolicy="no-referrer"></p><p>此图为我们在ATM取款机取款时的人机交互。</p><h3>2、复杂语法</h3><p style="text-align:center;"><img src="http://img.pmcaff.com/52528cd8a59f46d2e742c21f28e0f590-picture" alt="52528cd8a59f46d2e742c21f28e0f590-picture" coffee-w="660px" coffee-h="521px" coffee-format="png" referrerpolicy="no-referrer"></p><ul><li>loop：为循环语法，如果满足循环条件，则重复执行本框里的内容。<br></li><li>alt：条件语法，相当于if......else......语法，即满足哪个条件就执行这个条件下的动作。<br></li><li>opt：可选语法，如果满足可选条件，就执行框中的内容，否则跳过不执行。<br></li></ul><p>如下案例：还是我们在ATM取款机取款时的人机交互，只是更为复杂些。表述了只要输入密码就检查密码合法性，当输错超过三次时吞卡。密码正确时直接给与顾客菜单。</p><p style="text-align:center;"><img src="http://img.pmcaff.com/0d0427e1047788b8512dfb579fd3f889-picture" alt="0d0427e1047788b8512dfb579fd3f889-picture" coffee-w="668px" coffee-h="535px" coffee-format="png" referrerpolicy="no-referrer"></p><h3>3、步骤</h3><ul><li>针对某一条流程中分析各角色的交互方式时<br></li><li>先分析有哪些角色参与这个流程<br></li><li>分析各角色在这个流程中的职责，各角色的专业特色<br></li><li>将流程分解为角色与角色之间的交互，想清楚各角色之间的“接口”是怎样的<br></li><li>用顺序图按照时间顺序将“交互”动作组织起来<br></li><li>适当控制好粒度，不断优化和重组。有太复杂分支机构的流程不适用。<br></li></ul><h3>4、备注</h3><p>一般产品经理可以不用画复杂语法的内容，只需要画出关键重点交互即可，如下：</p><p style="text-align:center;"><img src="http://img.pmcaff.com/f7796eaa1128c12cf916d1cad6c57aca-picture" alt="f7796eaa1128c12cf916d1cad6c57aca-picture" coffee-w="606px" coffee-h="377px" coffee-format="png" referrerpolicy="no-referrer"></p><h2>（七）用例图<br></h2><p>用例图主要用来回答两个问题——这个系统的用户角色有哪些？每个角色能干什么？</p><h3>1、基本语法</h3><p>角色、用例、系统范围、关联关系</p><p style="text-align:center;"><img src="http://img.pmcaff.com/eeecb09b32ff88719a088429f204a61a-picture" alt="eeecb09b32ff88719a088429f204a61a-picture" coffee-w="460px" coffee-h="346px" coffee-format="png" referrerpolicy="no-referrer"></p><h3>2、复杂语法</h3><p>角色的继承、用例的继承、用例的include、用例的extend</p><p style="text-align:center;"><img src="http://img.pmcaff.com/64aaf6e6cff6d40fc12612006941a76b-picture" alt="64aaf6e6cff6d40fc12612006941a76b-picture" coffee-w="610px" coffee-h="497px" coffee-format="png" referrerpolicy="no-referrer"></p><h3>3、步骤</h3><ul><li>明确系统范围<br></li><li>有什么角色，角色与角色之间关系<br></li><li>有什么用例，角色与用例之间关系，用例的子用例及扩展。<br></li></ul><p style="text-align:center;"><br></p><p style="text-align:center;">~完~</p></pre>
  
</div>
            