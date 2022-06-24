
---
title: '浅析CRM系统的用户权限管理'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/wySU6ynl66cMJqngo1H1.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 24 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/wySU6ynl66cMJqngo1H1.jpg'
---

<div>   
<blockquote><p>编辑导语：权限管理可以用来控制什么人可以干什么事，需要根据每个用户的部门、角色来清晰的划分，以此来保障系统的数据安全。本文作者根据自身公司在引进使用CRM客户关系管理系统时的情况，对CRM系统的用户权限管理进行了分析，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5501013" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/wySU6ynl66cMJqngo1H1.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在公司深耕教育行业8年之际，终于决定引入CRM（Customer Relationship Management）客户关系管理系统，以下是一些系统使用心得。</p>
<h2 id="toc-1">一、背景分析</h2>
<p>以往公司所有订单数据均是依赖金数据这种表单收集系统，金数据有一个好处就是灵活，收集的数据最后都集中于一个个的表格里，想要修改什么信息非常方便，也很容易就创建出来复杂多变的表单来收集数据。</p>
<p>但是这也会带来一个很大的问题就是数据容易泄露，不管是暴露在表单里的数据还是表单收集来的数据（真的就发生过，嘘~），再者就是在项目运营期间的数据轮转包括数据统计都非常的不方便，对学生来说，这就是一次性的消费没有账户概念，也不利于公司内部导流和复购。</p>
<p>还有一个问题就是数据权限问题，以我司举例，我们的员工分为销售部、产品部、客服部、技术支持以及其他职能部门。产品部分管公司的不同项目，销售部按东南西北区域划分市场，客服部是负责公司400客服热线的部门。金数据收集来的数据对于所有这些员工是无差别展示的，总监和专员在数据呈现上没有任何区别。</p>
<p>因此随着公司业务发展以及长期战略规划布局，决定抛弃以往方式，引入CRM系统，帮助公司实现更加数据化、标准化的前进发展，解决公司在客户管理、销售行为管理上的痛点、难点。</p>
<h2 id="toc-2">二、主要目标</h2>
<p>公司希望所有的报名数据整合在一个系统，对学生生成账户，形成订单记录，为以后的更多玩法奠定基础。再加上订单会有大量B端产生的数据，所有B\C端的数据在项目后期又会统一运营，所以还会涉及到和自有系统的推送问题。</p>
<p>最重要就是保证数据安全，不管是对内的员工还是对外的竞争对手。以我司举例，我们的销售部要看到自己负责的所有产品的数据，产品部要看到自己负责产品的所有区域的数据，客服部要看到自己支持部门的所有数据，技术支持要看到公司所有的订单数据。所有这些员工谁该看到什么、谁能干什么，这需要一套完善的权限管理办法来实现。</p>
<p>权限管理简单来说就是用来控制什么人可以干什么事，需要根据每个用户的部门、角色来清晰的划分，以此来保障系统的数据安全。</p>
<p>本文也主要讲解CRM系统的权限管理模块内容。</p>
<h2 id="toc-3">三、实施办法</h2>
<p>先了解一下CRM系统的“三位一体”<strong>多维度权限</strong>管理方法，这种人、部门、角色的多维度权限管理办法兼备灵活度和易用性，当人员与部门变动后，只需简单调整即可完成对应的组织权限关系，并且能根据需要处理用户相关联数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/d61k2L07pXZvBGZGRtqA.jpg" alt width="561" height="204" referrerpolicy="no-referrer"></p>
<p>在CRM系统里的每一个用户都有一个部门的划分，作为权限管理里一个重要的层级。每一个用户又可独自分配角色和职能，而权限管理又以此分为角色管理和职能管理。</p>
<p>其中职能管理用来控制你能做什么（比如能否查看订单、能否删除订单能否转移订单），角色管理是决定了你能操作哪些数据（比如只能操作本人的数据、本人及下属的、本部门、本部门及下属部门或者全部数据）。以一张图示来表明这种关系：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/91BqafxEScgTbB4uAgSZ.jpg" alt width="836" height="298" referrerpolicy="no-referrer"></p>
<p>每种职能的功能权限构成“<strong>权</strong>”,每种角色的数据权限构成“<strong>限</strong>”。权+限=一个用户完整的权限。</p>
<p>下面以订单举例，逐个分析每个部门用户的权限管理办法：</p>
<h3>1. 销售部</h3>
<p>销售部员工是按区域划分各自的服务范围，比如一部分员工专门负责华北区域的订单，这些员工又分别负责各自的项目。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/zIuiJ5itLK863PT2nw0Z.png" alt width="625" height="449" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图1</p>
<p>销售部的员工需要的功能有基本的增删改查订单权限，如上图第三级列表，这些功能需要在职能管理中设置，职能管理配置截图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/3ioaCgi8CI1mjuSFmn4d.png" alt width="898" height="421" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2</p>
<p>图1的二级列表标签是代表每个销售员工依据自己职位的高低可视的数据范围，比如专员A不应该看到专员B的数据，主管应该看到自己及下属的数据，这种可视数据权限即需要在角色管理设置。角色管理配置截图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/ASW49FltvzJCSa1yXR2d.png" alt width="900" height="419" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图3</p>
<p>以上是销售部员工基于部门&角色的权限管理办法。但是销售部员工的订单负责人均是自己，也就是说除了自己别人都看不到也无法操作这些订单，那产品部的权限该如何处理呢？</p>
<h3>2. 产品部</h3>
<p>产品部员工需要看到自己负责产品的四大区域的订单，而这些订单的订单负责人已经划分给销售了，所以产品部无法直接看到订单数据。再者一个销售可能同时负责多个不同产品负责人的项目，因为这种相互交叉关联，所以也无法利用系统的助理或者共享规则来实现。产品部和销售部两个部门的数据对应关系如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/LdMg2Brh1pmkNqm8BWUM.jpg" alt width="888" height="652" referrerpolicy="no-referrer"></p>
<p>此时销售部门的按照「<strong>部门</strong>」的数据划分模式不能满足产品部门了，所以产品部门就需要开启数据权限多维度管理，新增「<strong>产品</strong>」管理维度，将业务对象“订单”及其他需要的对象同时开启产品维度管理，系统开启截图如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/aphnSTDXi85ZyjiATWS4.png" alt width="679" height="245" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图5</p>
<p>将需要开启产品维度管理的对象开启之后，给每一个用户的权限设置选择自己负责的产品，这也就构成了产品部门用户的“<strong>限</strong>”，产品部门的“<strong>权</strong>”则和市场部门一样根据自己的职能决定。产品选择截图:</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/9h9IICMB3RscYWCdaESb.png" alt width="796" height="330" referrerpolicy="no-referrer"></p>
<h3>3. 客服部</h3>
<p>客服部是按照对应区域给各销售人员配置的，类似于助理角色。因此可利用系统的“助理设置”，即把某销售人员设置为经理，把其对应客服设置为他的助理即可。</p>
<p>因为系统的助理具有和经理一样的数据查看权限，这样如无特殊要求则无需新增一种新的角色，但是需要根据业务需要新建职能，来特殊控制客服部门的操作权限，例如客服只能查看订单详情但是不可以删除订单。系统配置截图如下:</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/14bFnQGgSzvkE6Y38ZiS.png" alt width="615" height="243" referrerpolicy="no-referrer"></p>
<h3>4. 技术支持</h3>
<p>技术支持这一角色因为其角色的特殊性，所以需要看到公司所有人的订单数据，所以在上图3的角色权限设置为全部即可。但是技术支持又不需要像顾问或者客服一样高的功能权限，这一点也在上图2的职能权限设置即可。</p>
<p>有些时候技术支持不需看到订单的某些特殊字段，此时利用CRM系统的一个特殊功能：每一个对象的每一个字段都可以针对每一个职能来单独设置字段的可见\只读\导出权限。系统配置截图如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/bWmLFDIEam2vkN27b8XF.jpg" alt width="894" height="411" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、思考总结</h2>
<p>以上是以订单举例来盘点crm系统个用户的权限管理办法，总结一下就是有两种权限管理纬度，部门和产品。</p>
<p><strong>1）部门的权限管理办法</strong></p>
<p>用户可拥有多个角色及多个职能，职能负责控制功能权限，角色负责管理数据范围。给每一个用户赋予角色和职能,再把权限赋予这些角色和职能，这样的权限管理办法也就是RBAC（Role-based Access Control）基于角色的权限控制模型。这样的权限管理模式拥有极大程度的灵活、便利以及可拓展性，关于此模型详解本站也有很多文章分析，感兴趣的同学可以去搜索。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/IaMY58k0RP06ItxqiriO.png" alt width="936" height="282" referrerpolicy="no-referrer"></p>
<p><strong>2）产品的权限管理办法</strong></p>
<p>直接给用户勾选数据，这种就是传统的权限管理模型，直接给用户本身赋予权限。而这样的管理模型无疑是不够灵活的，一旦人员发生变动则有可能牵一发而动全身。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/zRmOjVKoNwYldk2ipkpX.png" alt width="423" height="242" referrerpolicy="no-referrer"></p>
<p>不管是什么产品都有可能遇到不同等级的权限问题，了解不同权限管理办法，在产品设计之初就应努力打造一个灵活、可拓展的权限模块，避免用到时需要“伤筋动骨”。</p>
<p> </p>
<p>本文由 @不做代码狗了 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5495372" data-author="1106096" data-avatar="https://static.qidianla.com/woshipm_def_head_4.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            