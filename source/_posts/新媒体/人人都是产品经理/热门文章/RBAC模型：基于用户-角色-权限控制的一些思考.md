
---
title: 'RBAC模型：基于用户-角色-权限控制的一些思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/08/j6EqsBoCWFJej6ke0yAI.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 07 Aug 2018 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/08/j6EqsBoCWFJej6ke0yAI.jpg'
---

<div>   
<blockquote><p>本文将从什么是RBAC模型、RBAC模型的分类、什么是权限、用户组的使用、实例分析这几个方面来整理说明。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-1220944" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/08/j6EqsBoCWFJej6ke0yAI.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>目前这份工作做的大部分系统都是ToB性质，几乎每个都涉及到了权限管理。经过多个系统的设计，知识的丰富，慢慢的发现主流的权限管理系统都是RBAC模型（Role-Based Access Control 基于角色的访问控制）的变形和运用，只是根据不同的业务和设计方案，呈现不同的显示效果。于是在前人的基础上，加上自己的理解，认真总结一下RBAC模型的相关知识。</p>
<p>在正式讨论RBAC模型之前，我们先思考一个问题，为什么我们要做角色权限系统？</p>
<p>大家先给自己1分钟时间思考（产品经理要学会随时思考哦）。</p>
<p>…思考10s</p>
<p>…思考30s</p>
<p>…思考50s</p>
<p>好的，1分钟到了，下面揭晓答案：</p>
<p>一个很明显的答案就是系统存在不同权限的用户，而根据业务要求的不同，每个用户能使用的功能、查看的内容是不同的。举个最简单的例子：钉钉后台，普通员工和行政能看到的菜单、使用的功能是不同的，行政可以查看所有员工的出勤记录而普通员工则不行。</p>
<p>接下来，本文将从以下几个方面进行整理说明：<b>什么是RBAC模型、RBAC模型的分类、什么是权限、用户组的使用、实例分析</b>。</p>
<h2 id="toc-1">一、什么是RBAC模型</h2>
<p>RBAC（Role-Based Access Control）即：基于角色的权限控制。通过角色关联用户，角色关联权限的方式间接赋予用户权限。</p>
<p>如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/Tv1YwLlngzOs6oQN9UG0.png" alt width="776" height="73" referrerpolicy="no-referrer"></p>
<p>有人会问为什么不直接给用户分配权限，还多此一举的增加角色这一环节呢？</p>
<p>其实是可以直接给用户分配权限，只是直接给用户分配权限，少了一层关系，扩展性弱了许多，适合那些用户数量、角色类型少的平台。</p>
<p>对于通常的系统，比如：存在多个用户拥有相同的权限，在分配的时候就要分别为这几个用户指定相同的权限，修改时也要为这几个用户的权限进行一一修改。有了角色后，我们只需要为该角色制定好权限后，将相同权限的用户都指定为同一个角色即可，便于权限管理。</p>
<p>对于批量的用户权限调整，只需调整用户关联的角色权限，无需对每一个用户都进行权限调整，既大幅提升权限调整的效率，又降低了漏调权限的概率。</p>
<h2 id="toc-2">二、RBAC模型的分类</h2>
<p>RBAC模型可以分为：RBAC0、RBAC1、RBAC2、RBAC3 四种。其中RBAC0是基础，也是最简单的，相当于底层逻辑，RBAC1、RBAC2、RBAC3都是以RBAC0为基础的升级。</p>
<p>一般情况下，使用RBAC0模型就可以满足常规的权限管理系统设计了。</p>
<h3>2.1 RBAC0模型</h3>
<p>最简单的用户、角色、权限模型。这里面又包含了2种：</p>
<ol>
<li>用户和角色是多对一关系，即：一个用户只充当一种角色，一种角色可以有多个用户担当。</li>
<li>用户和角色是多对多关系，即：一个用户可同时充当多种角色，一种角色可以有多个用户担当。</li>
</ol>
<p>那么，什么时候该使用多对一的权限体系，什么时候又该使用多对多的权限体系呢？</p>
<p>如果系统功能比较单一，使用人员较少，岗位权限相对清晰且确保不会出现兼岗的情况，此时可以考虑用多对一的权限体系。其余情况尽量使用多对多的权限体系，保证系统的可扩展性。如：张三既是行政，也负责财务工作，那张三就同时拥有行政和财务两个角色的权限。</p>
<h3>2.2 RBAC1模型</h3>
<p>相对于RBAC0模型，增加了子角色，引入了继承概念，即子角色可以继承父角色的所有权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/CN3L7POv7d8Ku1QMnXGU.png" alt width="746" height="148" referrerpolicy="no-referrer"></p>
<p><strong>使用场景：</strong>如某个业务部门，有经理、主管、专员。主管的权限不能大于经理，专员的权限不能大于主管，如果采用RBAC0模型做权限系统，极可能出现分配权限失误，最终出现主管拥有经理都没有的权限的情况。</p>
<p>而RBAC1模型就很好解决了这个问题，创建完经理角色并配置好权限后，主管角色的权限继承经理角色的权限，并且支持在经理权限上删减主管权限。</p>
<h3>2.3 RBAC2模型</h3>
<p>基于RBAC0模型，增加了对角色的一些限制：角色互斥、基数约束、先决条件角色等。</p>
<ul>
<li><strong>角色互斥：</strong>同一用户不能分配到一组互斥角色集合中的多个角色，互斥角色是指权限互相制约的两个角色。案例：财务系统中一个用户不能同时被指派给会计角色和审计员角色。</li>
<li><strong>基数约束：</strong>一个角色被分配的用户数量受限，它指的是有多少用户能拥有这个角色。例如：一个角色专门为公司CEO创建的，那这个角色的数量是有限的。</li>
<li><strong>先决条件角色：</strong>指要想获得较高的权限，要首先拥有低一级的权限。例如：先有副总经理权限，才能有总经理权限。</li>
<li><strong>运行时互斥：</strong>例如，允许一个用户具有两个角色的成员资格，但在运行中不可同时激活这两个角色。</li>
</ul>
<h3>2.4 RBAC3模型</h3>
<p>称为统一模型，它包含了RBAC1和RBAC2，利用传递性，也把RBAC0包括在内，综合了RBAC0、RBAC1和RBAC2的所有特点，这里就不在多描述了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/7MEIhTRfnGmV0T5MBYoH.png" alt width="385" height="249" referrerpolicy="no-referrer"></p>
<h2 id="toc-3"><strong>三、什么是权限</strong></h2>
<p>说了这么久用户-角色-权限，可能小伙伴们都了解了什么是用户、什么是角色。但是有的小伙伴会好奇，那权限又是个什么玩意呢？</p>
<p>权限是资源的集合，这里的资源指的是软件中所有的内容，包括模块、菜单、页面、字段、操作功能（增删改查）等等。具体的权限配置上，目前形式多种多样，按照我个人的理解，可以将权限分为：<strong>页面权限、操作权限和数据权限</strong>（这种分类法，主要是结合自己在工作中的实际情况理解总结而来，若有不足之处，也请大家指出）。</p>
<p><strong>页面权限：</strong>所有系统都是由一个个的页面组成，页面再组成模块，用户是否能看到这个页面的菜单、是否能进入这个页面就称为页面权限。</p>
<p>如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/zZMuljfwRvu8Be6oEFlV.png" alt width="634" height="225" referrerpolicy="no-referrer"></p>
<p>客户列表、客户黑名单、客户审批页面组成了客户管理这个模块。对于普通用户，不能进行审批操作，即无客户审批页面权限，在他的账号登录后侧边导航栏只显示客户列表、客户黑名单两个菜单。</p>
<p><strong>操作权限：</strong>用户凡是在操作系统中的任何动作、交互都是操作权限，如增删改查等。</p>
<p><strong>数据权限：</strong>一般业务管理系统，都有数据私密性的要求：哪些人可以看到哪些数据，不可以看到哪些数据。</p>
<p>简单举个例子：某系统中有销售部门，销售专员负责推销商品，销售主管负责管理销售专员日常工作，经理负责组织管理销售主管作业。</p>
<p>如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/eQKuv1vmlhA7eNDvlb1t.png" alt width="764" height="229" referrerpolicy="no-referrer"></p>
<p>按照实际理解，‘销售专员张三’登录时，只能看到自己负责的数据；销售主管2登录时，能看到他所领导的所有业务员负责的数据，但看不到其他团队业务员负责的数据。</p>
<p>换另外一句话就是：我的客户只有我和我的直属上级以及直属上级的领导能看到，这就是我理解的数据权限。</p>
<p>要实现数据权限有多种方式：</p>
<ol>
<li>可以利用RBAC1模型，通过角色分级来实现。</li>
<li>在‘用户-角色-权限’的基础上，增加用户与组织的关联关系，用组织决定用户的数据权限。</li>
</ol>
<p>具体如何做呢？</p>
<p><strong>①组织层级划分：</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/7OfSVWkovU90yPLCAYXl.png" alt width="492" height="230" referrerpolicy="no-referrer"></p>
<p><strong>②数据可视权限规则制定：</strong>上级组织只能看到下级组织员工负责的数据，而不能看到其他平级组织及其下级组织的员工数据等。</p>
<p>通过以上两点，系统就可以在用户登录时，自动判断要给用户展示哪些数据了。</p>
<h2 id="toc-4"><strong>四、用户组的使用</strong></h2>
<p>当平台用户基数增大，角色类型增多时，如果直接给用户配角色，管理员的工作量就会很大。这时候我们可以引入一个概念“用户组”，就是将相同属性的用户归类到一起。</p>
<p>例如：加入用户组的概念后，可以将部门看做一个用户组，再给这个部门直接赋予角色（1万员工部门可能就几十个），使部门拥有部门权限，这样这个部门的所有用户都有了部门权限，而不需要为每一个用户再单独指定角色，极大的减少了分配权限的工作量。</p>
<p>同时，也可以为特定的用户指定角色，这样用户除了拥有所属用户组的所有权限外，还拥有自身特定的权限。</p>
<p>用户组的优点，除了减少工作量，还有更便于理解、增加多级管理关系等。如：我们在进行组织机构配置的时候，除了加入部门，还可以加入科室、岗位等层级，来为用户组内部成员的权限进行等级上的区分。</p>
<p>关于用户组的详细疑难解答，请查看<a href="https://wen.woshipm.com/question/detail/88fues.html" target="_blank" rel="noopener">https://wen.woshipm.com/question/detail/88fues.html</a>。在这里也十分感谢为我解答疑惑的朋友们！</p>
<h2 id="toc-5"><strong>五、实例分析</strong></h2>
<h3>5.1 如何设计RBAC权限系统</h3>
<p>首先，我们思考一下一个简单的权限系统应该具备哪些内容？</p>
<p>答案显而易见，RBAC模型：<strong>用户-角色-权限</strong>。所以最基本的我们应该具备用户、角色、权限这三个内容。</p>
<p>接下来，我们思考，究竟如何将三者关联起来。回顾前文，角色作为枢纽，关联用户、权限。所以在RBAC模型下，我们应该：<strong>创建一个角色，并为这个角色赋予相应权限，最后将角色赋予用户</strong>。</p>
<p>将这个问题抽象为流程，如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/UGJGmWviv32mWGgEkYpC.png" alt width="597" height="147" referrerpolicy="no-referrer"></p>
<p>现在，基本的流程逻辑已经抽象出来了，接下来，分析该如何设计呢？</p>
<ul>
<li>第一步，需要角色管理列表，在角色管理列表能快速创建一个角色，且创建角色的同时能为角色配置权限，并且支持创建成功的角色列表能随时进行权限配置的的修改；</li>
<li>第二步，需要用户管理列表，在用户管理列表能快速添加一个用户，且添加用户时有让用户关联角色的功能。</li>
</ul>
<p>简单来说权限系统设计就包含以上两步，接下来为大家进行实例分析。</p>
<h3>5.2 实例分析</h3>
<p><strong>①创建角色列表</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/KHqjDiWnyZrOxgJnvjRX.png" alt width="786" height="261" referrerpolicy="no-referrer"></p>
<p>在角色列表快速创建一个角色：点击创建角色，支持创建角色时配置权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/uPzZ1iOh0bQpKkYbWCAc.png" alt width="688" height="434" referrerpolicy="no-referrer"></p>
<p><strong>②创建用户列表</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/x1pHe9duvadzeUfoeOac.png" alt width="736" height="233" referrerpolicy="no-referrer"></p>
<p>在用户列表快速创建一个用户：支持用户关联角色的功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/VZLXACV2P72RTzJn0Us8.png" alt width="754" height="449" referrerpolicy="no-referrer"></p>
<p>上述案例是基于最简单的RBAC0模型创建，适用于大部分常规的权限管理系统。</p>
<p>下面再分析一下RBAC1中角色分级具体如何设计。</p>
<ol>
<li><strong>在RBAC0的基础上，加上角色等级这个字段。</strong></li>
<li><strong>权限分配规则制定</strong>：低等级角色只能在高等级角色权限基础上进行删减权限。</li>
</ol>
<p>具体界面呈现如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/07/lGcyi0RJKsKmDI6C0bXy.png" alt width="754" height="444" referrerpolicy="no-referrer"></p>
<p>以上就是简单的RBAC系统设计，若需更复杂的，还请读者根据上面的分析自行揣摩思考，尽管样式不同，但万变不离其宗，理解清楚RBAC模型后，结合自己的业务就可以设计出一套符合自己平台需求的角色权限系统，具体的就不再多阐述了。</p>
<h2 id="toc-6"><strong>六、小结</strong></h2>
<p>文章的内容主要是自己工作中实际的使用场景，抱着他山之石可以攻玉的想法，参考了现有的方法论，结合自己系统的实际情况，对RBAC模型做了细致的总结理解。若有不足之处，还请大家多多沟通，共同进步。</p>
<p> </p>
<p>本文由 @ 珣玗琪 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="1150093" data-author="257654" data-avatar="http://image.woshipm.com/wp-files/2018/05/tbL9BkgP8ykdQl3OhT8O.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">6人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://image.woshipm.com/wp-files/2015/10/touxiang-8.jpg!/both/80x80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/woshipm_def_head.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602174758_6190.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182841_6929.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602174833_9311.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183216_6628.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            