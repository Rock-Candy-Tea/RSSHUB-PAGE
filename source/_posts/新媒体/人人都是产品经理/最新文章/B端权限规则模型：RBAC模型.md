
---
title: 'B端权限规则模型：RBAC模型'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ISlomXpYAdWeSMk2juD6.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 13 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ISlomXpYAdWeSMk2juD6.jpg'
---

<div>   
<blockquote><p>导读：B端项目上，需要设计实现一个权限管理模块，就要知道到一个很重要的RBAC模型，所以整理总结了RBAC的一些知识。目前，使用最普遍的权限管理模型正是RBAC（Role-Based Access Control）模型，这篇文章主要是介绍基于RBAC的权限管理系统，将会从RBAC是什么、如何设计RBAC两部分来介绍。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5174739 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ISlomXpYAdWeSMk2juD6.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、RBAC模型是什么?</h2>
<h3>1. RBAC模型概述</h3>
<p>RBAC模型（Role-Based Access Control：基于角色的访问控制）模型是20世纪90年代研究出来的一种新模型，但其实在20世纪70年代的多用户计算时期，这种思想就已经被提出来，直到20世纪90年代中后期，RBAC才在研究团体中得到一些重视，并先后提出了许多类型的RBAC模型。其中以美国George Mason大学信息安全技术实验室（LIST）提出的RBAC96模型最具有代表，并得到了普遍的公认。</p>
<p>RBAC认为权限授权的过程可以抽象地概括为：Who是否可以对What进行How的访问操作，并对这个逻辑表达式进行判断是否为True的求解过程，也即是将权限问题转换为What、How的问题，Who、What、How构成了访问权限三元组，具体的理论可以去调查RBAC96的研究文件，这里就不做详细的展开介绍，让大家有个了解和即可。</p>
<h3>2. RBAC的组成</h3>
<p>在RBAC模型里面，有3个基础组成部分，分别是：用户、角色和权限。</p>
<p>RBAC通过定义角色的权限，并对用户授予某个角色从而来控制用户的权限，实现了用户和权限的逻辑分离（区别于ACL模型），极大地方便了权限的管理。</p>
<p><strong>下面在讲解之前，先介绍一些名词：</strong></p>
<p>User（用户）：每个用户都有唯一的UID识别，并被授予不同的角色</p>
<p>Role（角色）：不同角色具有不同的权限</p>
<p>Permission（权限）：访问权限</p>
<p>用户-角色映射：用户和角色之间的映射关系</p>
<p>角色-权限映射：角色和权限之间的映射</p>
<p><strong>它们之间的关系如下图所示：</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/u8mrjILAHxSJOcChWIw0.png" referrerpolicy="no-referrer"></p>
<p>例如下图，管理员和普通用户被授予不同的权限，普通用户只能去修改和查看个人信息，而不能创建创建用户和冻结用户，而管理员由于被授 予所有权限，所以可以做所有操作。</p>
<p>例如下图，管理员和普通用户被授予不同的权限，普通用户只能去修改和查看个人信息，而不能创建创建用户和冻结用户，而管理员由于被授予所有权限，所以可以做所有操作。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/x63d1WOxRxha8HbSOyi8.png" referrerpolicy="no-referrer"></p>
<h3>3. RBAC支持的安全原则</h3>
<p>RBAC支持三个著名的安全原则：最小权限原则、责任分离原则和数据抽象原则。</p>
<p>最小权限原则：RBAC可以将角色配置成其完成任务所需的最小权限集合。</p>
<p>责任分离原则：可以通过调用相互独立互斥的角色来共同完成敏感的任务，例如要求一个计账员和财务管理员共同参与统一过账操作。</p>
<p>数据抽象原则：可以通过权限的抽象来体现，例如财务操作用借款、存款等抽象权限，而不是使用典型的读、写、执行权限。</p>
<h3>4. RBAC的优缺点</h3>
<p><strong>优点：</strong>简化了用户和权限的关系易扩展、易维护。</p>
<p><strong>缺点：</strong>RBAC模型没有提供操作顺序的控制机制，这一缺陷使得RBAC模型很难适应哪些对操作次序有严格要求的系统。</p>
<h3>5. RBAC的3种模型</h3>
<p><strong>1）RBAC0</strong></p>
<p>RBAC0，是最简单、最原始的实现方式，也是其他RBAC模型的基础。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/flPCLn9moPI5ez47cNwz.png" referrerpolicy="no-referrer"></p>
<p>在该模型中，用户和角色之间可以是多对多的关系，即一个用户在不同场景下是可以有不同的角色，例如：项目经理也可能是组长也可能是架构师。同时每个角色都至少有一个权限。这种模型下，用户和权限被分离独立开来，使得权限的授权认证更加灵活。</p>
<p><strong>A、权限是用户可以访问的资源，包括<strong>页面权限</strong>、<strong>操作权限</strong>、<strong>数据权限</strong>。</strong></p>
<p>a、页面权限：即用户登录系统可以看到的页面,由菜单来控制,菜单包括一级菜单和二级菜单,只要用户有一级和二级菜单的权限,那么用户就可以访问页面。</p>
<p>b、操作权限： 即页面的功能按钮，包括查看、新增、修改、删除、审核等，用户点击删除按钮时，后台会校验用户角色下的所有权限是否包含该删除权限，如果是，就可以进行下一步操作，反之提示无权限。有的系统要求”可见即可操作”，意思是如果页面上能够看到操作按钮，那么用户就可以操作，要实现此需求，这里就需要前端来配合，前端开发把用户的权限信息缓存，在页面判断用户是否包含此权限，如果有，就显示该按钮，如果没有，就隐藏该按钮。某种程度上提升了用户体验，但是在实际场景可自行选择是否需要这样做。</p>
<p>c、数据权限：数据权限就是用户在同一页面看到的数据是不同的，比如财务部只能看到其部门下的用户数据，采购部只看采购部的数据，在一些大型的公司，全国有很多城市和分公司，比如杭州用户登录系统只能看到杭州的数据，上海用户只能看到上海的数据，解决方案一般是把数据和具体的组织架构关联起来，举个例子，再给用户授权的时候，用户选择某个角色同时绑定组织如财务部或者合肥分公司，那么该用户就有了该角色下财务部或合肥分公司下的的数据权限。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/oflTw3ES3PIrlsw8EOio.jpeg" referrerpolicy="no-referrer"></p>
<p><strong>2）RBAC1</strong></p>
<p>基于RBAC0模型，引入了角色间的继承关系，即角色上有了上下级的区别。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/DFyylr4DRGpN8ZxHJjVn.png" referrerpolicy="no-referrer"></p>
<p>角色间的继承关系可分为一般继承关系和受限继承关系。一般继承关系仅要求角色继承关系是一个绝对偏序关系，允许角色间的多继承。而受限继承关系则进一步要求角色继承关系是一个树结构，实现角色间的单继承。</p>
<p><strong>A、数据范围的继承</strong></p>
<p>我们可以将用户进行分级管理，比如建立多层级的组织架构树，将不同用户放置于组织架构的不同根节点上，来实现多层级用户的建立和管理。</p>
<p>如果用户的层级如果比较简单（不多于三级），可以将层级关系融入到角色之中。</p>
<p>比如用户分为三级：管理员-组长-组员，管理员能看到全部的数据范围和拥有全部的功能权限，而组长能查看组员的数据范围和拥有部分功能权限（比如无法编辑用户），而组员的数据范围仅仅为自己负责的数据和拥有部分功能权限。</p>
<p>我们可以在组长这个角色下，允许其绑定组员，针对不同的角色设置不同的数据范围读取方式，管理员可以读取全部数据范围，组长需要读取其组员的，组员只能读取自己的。这种模型适合于角色之间层次分明，可以给角色分组分层。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/57CQiGTYBBSvpIzha0N2.png" referrerpolicy="no-referrer"></p>
<p><strong>RBAC2：</strong></p>
<p>RBAC2，基于RBAC0模型的基础上，进行了角色的访问控制。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/zGnLAcjjVbhm8WZm0Xsk.png" referrerpolicy="no-referrer"></p>
<p>RBAC2中的一个基本限制是互斥角色的限制，互斥角色是指各自权限可以互相制约的两个角色。对于这类角色一个用户在某一次活动中只能被分配其中的一个角色，不能同时获得两个角色的使用权。</p>
<p><strong>该模型有以下几种约束：</strong></p>
<p>互斥角色 ：同一用户只能分配到一组互斥角色集合中至多一个角色，支持责任分离的原则。互斥角色是指各自权限互相制约的两个角色。对于这类角色一个用户在某一次活动中只能被分配其中的一个角色，不能同时获得两个角色的使用权。常举的例子：在审计活动中，一个角色不能同时被指派给会计角色和审计员角色。</p>
<p>基数约束 ：一个角色被分配的用户数量受限；一个用户可拥有的角色数目受限；同样一个角色对应的访问权限数目也应受限，以控制高级权限在系统中的分配。例如公司的领导人有限的；</p>
<p>先决条件角色 ：可以分配角色给用户仅当该用户已经是另一角色的成员；对应的可以分配访问权限给角色，仅当该角色已经拥有另一种访问权限。指要想获得较高的权限，要首先拥有低一级的权限。就像我们生活中，国家主席是从副主席中选举的一样。</p>
<p>运行时互斥 ：例如，允许一个用户具有两个角色的成员资格，但在运行中不可同时激活这两个角色。</p>
<p><strong>RBAC3：</strong></p>
<p>最全面的权限管理,它是基于RBAC0,将RBAC1和RBAC2进行了整合。</p>
<h2 id="toc-2">二、如何设计RBAC?</h2>
<p>介绍设计基于RBAC模型的权限系统的功能模块组成、流程以及数据库的设计。</p>
<h3>1. RBAC的功能模块</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/yFOQUzzXVoyPVQRL3T0u.png" referrerpolicy="no-referrer"></p>
<h3>2. RBAC执行流程</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/yh6ZJhF6nK0v2ugXvTMa.png" referrerpolicy="no-referrer"></p>
<h3>3. RBAC数据库设计</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/XxB9u0b6qF9SSQ9S6hkt.png" referrerpolicy="no-referrer"></p>
<h3>4. 用户组</h3>
<p>平台用户基数增大，角色类型增多时，而且有一部分人具有相同的属性，比如财务部的所有员工,如果直接给用户分配角色，管理员的工作量就会很大，如果把相同属性的用户归类到某用户组，那么管理员直接给用户组分配角色，用户组里的每个用户即可拥有该角色，以后其他用户加入用户组后，即可自动获取用户组的所有角色，退出用户组，同时也撤销了用户组下的角色，无须管理员手动管理角色。</p>
<p>根据用户组是否有上下级关系,可以分为有上下级的用户组和普通用户组。</p>
<p>具有上下级关系的用户组：最典型的例子就是部门和职位，可能多数人没有把部门职位和用户组关联起来吧。当然用户组是可以拓展的，部门和职位常用于内部的管理系统，如果是面向C端的系统，比如淘宝网的商家，商家自身也有一套组织架构，比如采购部，销售部，客服部，后勤部等，有些人拥有客服权限，有些人拥有上架权限等等，所以用户组是可以拓展的。</p>
<p>普通用户组：即没有上下级关系，和组织架构，职位都没有关系，也就是说可以跨部门，跨职位,举个例子，某电商后台管理系统，有拼团活动管理角色，我们可以设置一个拼团用户组，该组可以包括研发部的后台开发人员，运营部的运营人员，采购部的人员等等。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/8bFPbiCOQJaGcurfWBuG.png" referrerpolicy="no-referrer"></p>
<h3>5. 组织</h3>
<p>常见的组织架构如下图：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/givHilAH1HEBgOZSibms.jpeg" referrerpolicy="no-referrer"></p>
<p>可以把组织与角色进行关联，用户加入组织后，就会自动获得该组织的全部角色，无须管理员手动授予，大大减少工作量，同时用户在调岗时，只需调整组织，角色即可批量调整。</p>
<h3>6. 授权流程</h3>
<p>授权即给用户授予角色，按流程可分为手动授权和审批授权。权限中心可同时配置这两种，可提高授权的灵活性。</p>
<p>手动授权：管理员登录权限中心为用户授权，根据在哪个页面授权分为两种方式：给用户添加角色，给角色添加用户。</p>
<p>给用户添加角色就是在用户管理页面，点击某个用户去授予角色，可以一次为用户添加多个角色；给角色添加用户就是在角色管理页面，点击某个角色，选择多个用户，实现了给批量用户授予角色的目的。</p>
<p>审批授权：即用户申请某个职位角色，那么用户通过OA流程申请该角色，然后由上级审批，该用户即可拥有该角色，不需要系统管理员手动授予。</p>
<h2 id="toc-3">三、整理总结：</h2>
<h3>1. RBACM模型</h3>
<p>RBAC0、RBAC1、RBAC2、RBAC3</p>
<p>RBAC0：是RBAC的核心思想。</p>
<p>RBAC1：RBAC基础上增加了角色分层模型。</p>
<p>RBAC2：RBAC基础上增加了约束模型。</p>
<p>RBAC3：其实是RBAC2 + RBAC1。</p>
<h3>2. 权限</h3>
<p><strong>1) 权限赋予</strong></p>
<p>权限赋予是把当前用户的权限拉出来，然后分配的客服可以小于等于当前用户的权限。</p>
<p><strong>2) 权限加载</strong></p>
<p>正常的加载权限，当用户登录后，并且第一次使用权限判断的时候， Shiro（页面框架） 会去加载权限。</p>
<p><strong>3) 权限判断</strong></p>
<p>走正常用户权限判断，但是数据操作需要判断是不是当前归属的用户的数据，其实这个是属于业务层，就算你不是客服，也是需要判断。</p>
<p><strong>(4) 禁用|启用</strong></p>
<p>禁用启用，也是正常的用户流程，添加到禁用列表里，如果被禁用，就无法操作任何内容。</p>
<p> </p>
<p>本文由 @K 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5173846" data-author="1305427" data-avatar="https://static.woshipm.com/WX_U_202107_20210728160143_6743.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            