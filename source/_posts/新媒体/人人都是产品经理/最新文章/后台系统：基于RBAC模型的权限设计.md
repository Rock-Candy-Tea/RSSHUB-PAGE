
---
title: '后台系统：基于RBAC模型的权限设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/RNFiO60NTbnpbC0CP5x0.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 10 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/RNFiO60NTbnpbC0CP5x0.jpg'
---

<div>   
<blockquote><p>编辑导语：RBAC是一套成熟的权限模型，在传统权限模型中，我们直接把权限赋予用户。而在RBAC中，首先把权限赋予角色，再把角色赋予用户。本文作者以后台系统为例，以RBAC模型为基础，为我们展示了权限设计的过程。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4683921" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/RNFiO60NTbnpbC0CP5x0.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>对于业务复杂或数据庞大的系统，为了方便管理，一定要做权限设计。权限设计是后台系统要考虑的一个授权策略问题。直白的说，权限设计就是根据公司的业务规则，对权限管理系统设置的安全策略。</p>
<p>权限一般分为功能权限，数据权限与菜单权限：</p>
<ul>
<li>功能权限控制当前账号可以操作的功能按妞，比如风控只能审核标的登记，但不能发起进件申请。</li>
<li>数据权限控制当前账号可以看到的数据范围，比如客服A只能看到分配到她名下的出借人的投资数据。</li>
<li>菜单权限控制当前账号可以看到的页面内容，比如催收人员只能看到案件逾期后流转到催收页面的内容。</li>
</ul>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/mEWAYdd9Je73iNQiuIa7.png" alt="后台系统：基于RBAC模型的权限设计" width="502" height="258" referrerpolicy="no-referrer"></p>
<p>对于权限设计，关键是理清用户、权限、角色三者的关系。即给谁创建账户，分配什么角色，赋予何种权限。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/sJNgEMItTgJDlF5WX62j.png" alt="后台系统：基于RBAC模型的权限设计" width="602" height="276" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、需求背景</h2>
<p>权限设计的首要问题是明确需求。权限设计牵涉到后台系统底层架构的业务逻辑，在做后台系统之前，一定要对现有的权限控制和业务情况了解清楚，才能避免在权限设计的问题上踩坑。</p>
<p>以某车贷风控系统为例，我们通过相关业务部门的反馈和当前权限系统的调研，发现它存在的问题有以下几点：</p>
<ol>
<li>用户的权限归属不明确，导致进件的申请和审核操作为同一个人；</li>
<li>敏感数据没有做权限控制和脱敏处理，导致用户隐私数据被泄露；</li>
<li>角色的分类不合理，每个用户只能配置一个角色，导致工作组和流程节点比较复杂；</li>
<li>对所属团队的客户经理、团队经理和城市经理做了三级维护关系，但人员调动和离职率较大，导致管理成本高。</li>
</ol>
<p>了解完现有需求背景后，我们借鉴钉钉的那套权限维护方式，改进了管理系统的权限设计。</p>
<p>一方面收集权限需求，根据部门需求列一份权限清单，并做好CheckList。在模块的功能页面要放置哪些权限，完全可以根据《操作权限申请表》的业务需求，进行灵活的权限配置。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/NLcSGH9rBu7U218kRSNS.jpg" alt="后台系统：基于RBAC模型的权限设计" width="602" height="401" referrerpolicy="no-referrer"></p>
<p>另一方面借助UML建模的用例图，将角色按功能Uc级细分到增删改查导，方便确认相关人员的操作权限。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rlaAod34iNTaV6TZTVa9.png" alt="后台系统：基于RBAC模型的权限设计" width="702" height="442" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、设计过程</h2>
<p>明确需求后，就要选择合适的权限设计模型。做后台系统权限设计，我们可以借鉴一些控制模型。</p>
<p>常见的权限设计控制模型有：自主访问控制（DAC）、强制访问控制（MAC）、访问控制列表(ACL)、基于角色的访问控制(RBAC) 、基于任务和工作流的访问控制(TBAC) 、基于任务和角色的访问控制(T-RBAC)、基于对象的访问控制（OBAC）、使用控制模型( UCON)、基于属性的访问控制（ABAC）等。</p>
<p>最常见的权限设计控制模型是RBAC模型。像业务复杂且功能庞大的某车贷风控系统，权限设计选择的就是RBAC模型，主要是方便后续的扩展。</p>
<p>RBAC即基于角色的权限访问控制（Role-Based Access Control），在RBAC模型中，权限与角色相关联，用户通过成为对应角色的成员，从而得到这些角色的权限。即用户关联角色，角色关联权限，可实现系统权限的灵活配置。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/GFjLbl7gL4qGv03Hk1ep.jpg" alt="后台系统：基于RBAC模型的权限设计" width="603" height="411" referrerpolicy="no-referrer"></p>
<p>访问控制的核心是授权策略。在RBAC模型中，Who、What、How构成了权限控制三要素，也就是Who对What(Which)进行How的操作。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ax6NXbfghinTZdTToo4h.png" alt="后台系统：基于RBAC模型的权限设计" width="407" height="288" referrerpolicy="no-referrer"></p>
<p>RBAC的权限授权其实就是Who、What、How的问题。Who：权限的拥用者，What：权限针对的资源，How：具体的权限。在RBAC中，根据权限设计的复杂程度，可分为RBAC0、RBAC1、RBAC2、RBAC3。</p>
<p>RBAC模型包含用户(User)、资源(Resource)、操作(Operation)三个关键要素。通过将资源以及资源操作授权给用户，而使用户获得对资源进行操作的权限，保证了权限分配的实施。</p>
<p>此外，RBAC模型遵循三条安全原则：最小权限原则，责任分离原则和数据抽象原则，从而简化了权限管理。</p>
<h2 id="toc-3">三、实施过程</h2>
<p>选择RBAC模型后，就要从账户、角色、权限三方面考虑实施过程，并满足不同的用户在使用过程中的不同权限需求。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/UPb4NpwfiS72XK9ScgH8.png" alt="后台系统：基于RBAC模型的权限设计" width="599" height="316" referrerpolicy="no-referrer"></p>
<p>其中账户和角色关联、角色和权限关联，且都是多对多的关系，我们可以借助UML建模的类图了解三者之间的关系。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/zmQG4UihQVNp3lf5WBu2.jpg" alt="后台系统：基于RBAC模型的权限设计" width="609" height="356" referrerpolicy="no-referrer"></p>
<p>以某车贷风控系统为案例，我们要为某风控A创建一个管理账户，并分配对应的风控人员角色，且在系统拥有访问标的详情权限和操作标的登记权限。</p>
<h2 id="toc-4">四、账户管理</h2>
<p>账户管理的入口在系统管理模块，包括基本的新增账户，编辑账户，删除账户、查看账户、查询账户，以及给账户分配角色。</p>
<p>账号管理是管理员最常用到的功能，相应字段一般是常用字段和特定字段。常用字段比如用户ID，手机号，姓名，角色，状态和注册时间等，特定字段是公司业务需求，比如分配角色，登录时间，登录次数，访问IP，访问设备等。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/w4FXEbh06pI8rNyXZrO8.png" alt="后台系统：基于RBAC模型的权限设计" width="599" height="288" referrerpolicy="no-referrer"></p>
<p>管理员在新增账户时，通过给该账户分配风控人员的角色，从而拥有该角色的相关权限。RBAC模型就是通过给用户分配角色，而取得角色的权限，这样就简化了用户权限分配流程。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/PJpV4E3CTRyhrRIbmYbv.png" alt="后台系统：基于RBAC模型的权限设计" width="406" height="426" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、角色管理</h2>
<p>角色管理的入口在系统管理模块，包括基本的新增角色，编辑角色，删除角色、查看角色、查询角色，以及给角色分配权限。</p>
<p>角色管理是用来管理公司内部用户的角色信息。一个复杂的后台会被分割成很多角色，比如管理员、运营人员、客服人员、财务人员、催收人员等。我们可把具有共同特征的某一类人群的身份进行归纳，从而为不同的用户赋予对应的角色权限。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/TsYqByQ553pqjg7BLDuu.png" alt="后台系统：基于RBAC模型的权限设计" width="606" height="287" referrerpolicy="no-referrer"></p>
<p>管理员会根据公司业务需要，新增对应的角色，并给该角色赋予对应的页面权限和操作权限。角色是关联用户和权限的纽带，可以为用户赋予该角色所集成的相关权限。我们在权限拦截流程设计时，就会限制菜单要根据给用户分配的角色填充，只显示该角色可展示的菜单。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/kzHALPRf7ENc4bmqbIJq.png" alt="后台系统：基于RBAC模型的权限设计" width="500" height="436" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、权限管理</h2>
<p>权限管理的入口在系统管理模块，包括基本的新增权限，编辑权限，删除权限、查看权限，以及给权限状态进行开关。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZZtlPNU2tyt8R9vcPUSj.png" alt="后台系统：基于RBAC模型的权限设计" width="599" height="287" referrerpolicy="no-referrer"></p>
<p>任何一个B/S系统或C/S系统都会做权限管理。权限管理限制用户可以访问而且只能访问自己被授权的内容或数据。</p>
<p>管理员在新增权限时，会限定权限性质为基本权限或操作权限。比如用户没有操作权限时，点击按钮会提示无权限，或者按钮置灰不可点击，或者隐藏该操作按钮。</p>
<p><img data-action="zoom" class="inline-img aligncenter" title="后台系统：基于RBAC模型的权限设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/slZSRMCEXz6kCmoaFP2n.png" alt="后台系统：基于RBAC模型的权限设计" width="503" height="332" referrerpolicy="no-referrer"></p>
<p>权限设计是后台系统必不可少的一个环节。基于RBAC模型的权限设计，能支持业务复杂的权限控制，也能满足平台运营的安全策略，增加了权限管理的灵活性与简便化。</p>
<h3>#专栏作家#</h3>
<p>朱学敏，微信公众号：朱学敏聊产品，人人都是产品经理专栏作家。畅销书《产品闭环：重新定义产品经理》作者，7年金融产品人，专注于金融行业，从0到1负责产品的全过程开发与设计。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4682161" data-author="657972" data-avatar="https://static.woshipm.com/APP_U_202102_20210222165710_5307.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            