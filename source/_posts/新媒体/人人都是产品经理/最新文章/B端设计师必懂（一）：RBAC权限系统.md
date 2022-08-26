
---
title: 'B端设计师必懂（一）：RBAC权限系统'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/kohrljs9kzYi97fnvFiY.png'
author: 人人都是产品经理
comments: false
date: Fri, 26 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/kohrljs9kzYi97fnvFiY.png'
---

<div>   
<blockquote><p>电商行业中，后台会有客服、采购、财务等不同的角色，对应展示不同权限、界面数据。在设计B端后台权限模块时，简单的用权限勾选即可，然而复杂的需要涉及到多角色、多权限相互匹配的场景中，则需要引入一个概念——RBAC权限模型。本文作者对RBAC权限模型进行了介绍，一起来看一下吧。</p>
</blockquote><p><img data-action="zoom" class="aligncenter size-full wp-image-5578952" src="https://image.woshipm.com/wp-files/2022/08/kohrljs9kzYi97fnvFiY.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>这是一篇<strong>实战经验+概念解释</strong>文章。</p>
<p>想法来自近期在进行一个后台产品中，涉及到权限管理的设计，需要设计多种角色、并需要对应不同级别，需要区分不同权限的设计，说半天，上个图！</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/jfytKbbaitn7IBbpTKWs.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p>大概意思就是在D的角色下会有A、B、C这3人，而C又包含角色A、B的权限，角色A、B下方又有A-1、B-1等人；而D拥有最大权限，对应下分不同角色配对不同权限，而下一级又是不同权限！于是一层层套娃开始了！</p>
<p>做过电商行业的应该都知道，在后台会有客服、采购、财务等不同的角色，对应展示不同权限、界面数据。</p>
<p>这就要求设计师在设计时，就要从业务角度上，去对每个角色进行代入、根据实际业务理解后进行设计。</p>
<p>通常在设计B端后台权限模块时，需要先厘清角色与权限之前的关系，比如对子账号进行角色管理、权限分配等场景进行分类，如果简单一点的模式设计就很好处理，用权限勾选即可，但复杂一点的就需要涉及到<strong>多角色、多权限相互匹配</strong>的场景中，简单权限勾选就不足以支撑起权限模块了。</p>
<p>因此，在B端后台界面设计中，就需要引入一个概念：<strong>RBAC权限模型</strong>，现今权限设置几乎都是在RBAC模型上进行扩展的，本文下面将会对RBAC权限模型进行简略介绍。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/bam4S1mYr99RbosI02Fw.jpeg" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、RBAC模型定义</h2>
<p>那说起RBAC权限模型，那我们来看下它在“维基”上的定义：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/ix4tQGUpPllm9vwtENex.png" alt="B端设计师必懂（一）：RBAC权限系统" width="653.6" referrerpolicy="no-referrer"></p>
<p>可以看到：RBAC是Role-Based Access Control的英文缩写，意思就是以【角色】为基础进行【权限】的【控制】。</p>
<p>换句话说：就是<strong>划定【权限】范围，赋予【角色】，再将【角色】赋予【账户】</strong>，这样【账户】拥有了权限，权限边界会很清晰，而去命定账户权限时只要去管理角色即可。</p>
<p>还是不懂？看图👇</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/JwUszF2quOd5A44CSJBg.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：RBAC简单示例</p>
<p>再用王者荣耀来比喻：</p>
<ul>
<li>角色 == 英雄人物</li>
<li>权限 == 英雄技能</li>
<li>账户 == QQ/微信账号</li>
</ul>
<p>使用【英雄人物】的就是你的账户，账户可以拥有多个英雄人物，管理权限的时候只要去管理【英雄人物】就行了。</p>
<h2 id="toc-2">二、RBAC模型细项说明</h2>
<p>在RBAC模型中，有三个比较重要的概念：</p>
<ol>
<li>权限：原子级别功能，能够访问某个数据或者进行某个操作的资格或权力</li>
<li>角色：分子级别功能，对某一类共同拥有权限集合群体名称</li>
<li>账户：组合功能，对拥有角色集合的群体名称</li>
</ol>
<p>下面对每个概念进行说明。</p>
<h3>1. 权限说明</h3>
<p>在计算机系统中，权限是指某个特定的用户具有特定的系统资源的使用权力，在后台管理中，系统资源指的是系统模块、页面、操作功能等。</p>
<p>大致可以将权限分为：<strong>功能操作权限、数据权限</strong>。</p>
<ul>
<li>功能操作权限：在系统的操作、交互都是功能权限，操作都需要页面承载，所以包浏览页面权限、操作按钮权限都归属功能操作权限</li>
<li>数据权限：对数据进行增删改查</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/O0B1Px0z2QvWc2k7OzgU.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：权限的构成图</p>
<h3>2. 角色说明</h3>
<p>角色是一定数量的权限的集合以及载体，很好理解，就是界定好哪几个角色拥有哪些权限。</p>
<p>比如角色一拥有：查看订单、修改订单价格、确认发货、订单评价 等权限，那角色一其实定义的是客服角色，那就可以给角色一命名为【客服】。</p>
<p>如下图所示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/Q6SJF5cD7kZ7q941PzEl.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：新增角色操作界面</p>
<h3>3. 账户说明</h3>
<p>账户是对角色的囊括，也是角色集合的载体，即界定账户拥有哪些角色，对应拥有哪些角色的权限。</p>
<p>如下图所示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/G6WsvEXYfbin1h7JXupC.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：账户对应的角色</p>
<h3>4. 升级模型：RBAC1模式</h3>
<p>上述所有模型是基础模型，实际业务中仅有基础模式是不够使用的。</p>
<p>比如一个系统中有了角色：管理员、客服、采购、财务等。</p>
<p>但财务下会有多种角色，例如：总账会计、明细帐会计、出纳等角色，故此对RBAC模型进行升级，会把一开始没有上下级关系的称为<strong>RBAC0模型</strong>，在RBAC0基础上引入角色间的上下级关系，升级后称为为<strong>RBAC1模型</strong>。</p>
<p>如下图所示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/8KlU0Wc5pdabRD861VyB.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：RBAC1模型</p>
<p>在RBAC1之后还有RBAC2、RBAC3等关系，较为复杂，不在本次讨论范围之内。</p>
<h2 id="toc-3">三、设计中引用RBAC模型的好处</h2>
<p>RBAC中具有角色的概念，设想一下，如果系统中没有角色，那么需要设置每个账户的权限，如果较复杂系统中，涉及到权限都非常多，每个账户都单独设置一遍，无疑是一件繁琐且工作量巨大的任务，可以说引用RBAC模型可以大大提高生产力。</p>
<p>在还未引入模型时，需要对每个账户都进行权限限定，参考下图，线条代表了需要操作的次数。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/RQ4CIS1fxBdsOruGsIQq.jpeg" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p>如果引入角色后，只需要给<strong>将角色给不同账户</strong>，<strong>给角色赋予权限，这样账户拥有的角色就直接拥有了该角色下的所有权限。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/tigD9JnP88Xy0lVgcSMk.jpeg" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、实战：如何设计RBAC模型</h2>
<h3>1. 梳理权限</h3>
<p>可以对页面当中拥有哪些可操作项收集，通常权限都是由系统、页面操作限定的，可以梳理一下产品整体框架，对所有权限进行分类。</p>
<p>比如千牛商家后台，在【店铺】一级页面下，拥有【店铺管理】【商户中心】【神笔】【营销管理】四大权限，在这四大权限之下又拥有次级页面，在次级页面下拥有各个模块的操作，这样从功能操作+数据上实现了集合。</p>
<p>如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/Xl8TzQmTFd5FwvZE9RVA.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：千牛商家自定义权限</p>
<h3>2. 命定角色</h3>
<p>从拥有【店铺】整体权限来分析，其实更多是关于到整体运营层属性，所以在归属【店铺】权限，可以对应到【运营组长】【运营专员】等角色。</p>
<p>如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/SvVe6Qq8vL8g0r2SzStb.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：千牛商家命定角色</p>
<h3>3. 账号限定</h3>
<p>其实对账号的限定很简单，重点是对账号拥有哪些角色范围圈定，圈定角色之后就隶属于哪个部门使用账号的问题了</p>
<p>如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/nNXtKn9c0KeSOdOM6Axe.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端设计师必懂（一）：RBAC权限系统" src="https://image.woshipm.com/wp-files/2022/08/Jo8VVeo53DFaAdIClxTK.png" alt="B端设计师必懂（一）：RBAC权限系统" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">例：千牛商家命定账号</p>
<p><strong>大功告成！完成这3步就完成整体设定啦！</strong></p>
<h2 id="toc-5">总结一下</h2>
<p>B端后台权限设计引入RBAC权限模型设计，是基于角色进行的权限访问控制，再进行对角色进行账号匹配。在进行产品设计时，尽量使用权限、账号分开模式去设计，而使用角色——权限匹配模式来做解耦。</p>
<p>后台类或者TO B内部产品，不会像C端用户一样权限简单，也不会追求极致用户体验，而是追求明确、结构清晰，不要在交互操作或文字上，让使用者有疑惑，尤其针对权限一块，或涉及业务功能设计上，尽量减少歧义，避免造成返工、错误理解等情况。</p>
<p>另附带RBAC模型升级概念解释，下期见！</p>
<ol>
<li>RBAC0：是RBAC的核心思想</li>
<li>RBAC1：RBAC基础上增加了角色分层模型，即进行了角色上下级区分</li>
<li>RBAC2：RBAC基础上增加了约束模型，什么是约束呢，就是账号想要获得高级权限，必须先拥有低级权限，否则无法命定</li>
<li>RBAC3：其实是RBAC2 + RBAC1，双重限定条件</li>
</ol>
<div class="article--copyright"><p>本文由 @无尘弟弟 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议。</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5578448" data-author="294181" data-avatar="https://image.woshipm.com/wp-files/2020/06/J9Kn0hY5laObRcDUix6g.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            