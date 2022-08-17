
---
title: 'B端产品之权限设计（RBAC权限模型）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/pk2DRL5rVLk4jjCCnvqQ.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 17 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/pk2DRL5rVLk4jjCCnvqQ.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端管理系统中，“权限管理”是必不可少的功能，不同的系统中权限的应用复杂程度不一样，要根据实际产品以及需求而设置合理的权限。本文作者通过介绍RBAC权限模型的概念，结合实际案例，对B端产品的权限设计进行了分析，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5568656" src="https://image.woshipm.com/wp-files/2022/08/pk2DRL5rVLk4jjCCnvqQ.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>随着互联网的快速发展，B端行业也逐渐崛起，很多企业管理中使用的软件我们通常称其为B端管理系统，而在B端系统中“权限管理”是必不可少的功能，不同的系统中权限的应用复杂程度不一样，都是根据实际产品以及需求情况而设置合理的权限。</p>
<p>而我们现在对于权限的设置基本上都是建立在RBAC权限模型上的、扩展的，下面我会通过介绍RBAC权限模型的概念，以及结合实际业务情况列举权限设置的应用。</p>
<h2 id="toc-1"><strong>一、什么是RBAC权限模型？</strong></h2>
<p>RBAC是Role-BasedAccess Control的英文缩写，意思是基于角色的访问控制。RBAC认为权限授权实际上是Who、What、How的问题。在RBAC模型中，who、what、how构成了访问权限三元组，也就是“Who对What进行How的操作，也就是“主体”对“客体”的操作。其中who是权限的拥有者或主体（例如：User、Role），what是资源或对象（Resource、Class)。</p>
<p><strong>简单的理解其理念就是将“角色”这个概念赋予用户，在系统中用户与权限之间通过角色进行关联，以这样的方法来实现灵活配置。</strong></p>
<p>RBAC其实是一种分析模型，主要分为：基本模型RBAC0、角色分层模型RBAC1、角色限制模型RBAC2和统一模型RBAC3。</p>
<p>RBAC权限模型是基于角色的权限控制。模型中有几个关键的术语：</p>
<ul>
<li>用户：系统接口及访问的操作者</li>
<li>权限：能够访问某接口或者做某操作的授权资格</li>
<li>角色：具有一类相同操作权限的用户的总称</li>
</ul>
<h3>1. RBAC0</h3>
<p>RBAC0是RBAC权限模型的核心思想，RBAC1、RBAC2、RBAC3都是在RBAC0上进行扩展的。RBAC0是由四部分构成：用户、角色、会话、许可。</p>
<p>用户和角色的含义很简单，通过字面意思即可明白，会话：指用户被赋予角色的过程，称之为会话或者是说激活角色；许可：就是角色拥有的权限（操作和和被控制的对象），简单的说就是用户可使用的功能或者可查看的数据。</p>
<p>用户与角色是多对多的关系，用户与会话是一对一的关系，会话与角色是一对多的关系，角色与许可是多对多的关系。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/fMM5x1wZkMbKRePlEFPW.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h3>2. RBAC1</h3>
<p>RBAC1是在RBAC0权限模型的基础上，在角色中加入了继承的概念，添加了继承的概念后，角色就有了上下级或者等级关系。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/eUEJmkdN0V6W40dLlzKU.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>举例：集团权责清单下包含的角色有：系统管理员、总部权责管理员、区域权责管理员、普通用户，当管理方式向下兼容时，就可以采用RBAC1的继承关系来实现权限的设置。上层角色拥有下层的所有角色的权限，且上层角色可拥有额外的权限</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/NoS7cpEzAwiO2YxVW9yT.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h3>3. RBAC2</h3>
<p>RBAC2是在RBAC0权限模型的基础上，在用户和角色以及会话和角色之间分别加入了约束的概念（职责分离），职责分离指的是同一个人不能拥有两种特定的权限（例如财务部的纳入和支出，或者运动员和裁判员等等）。</p>
<p>用户和角色的约束有以下几种形式：</p>
<ul>
<li>互斥角色：同一个用户在两个互斥角色中只能选择一个（也会存在一个用户拥有多个角色情况，但是需要通过切换用户角色来实现对不同业务操作）</li>
<li>基数约束：一个用户拥有的角色是有限的，一个角色拥有的许可也是有限的</li>
<li>先决条件约束：用户想要获得高级角色，首先必须拥有低级角色</li>
</ul>
<p>会话和角色之间的约束，可以动态的约束用户拥有的角色，例如一个用户可以拥有两个角色，但是运行时只能激活一个角色。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/u9DD8QLY8XUl2BMOulA6.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>例如：iconfont和蓝湖的用户与角色就采用了约束的概念，超级管理员只允许只有一个</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/yq9y1SXlvoMnBGgkSSjt.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/uFE10MSFhh3CbGYSKHof.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h3>4. RBAC3</h3>
<p>RBAC3是RBAC1与RBAC2的合集，所以RBAC3包含继承和约束。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/ADFXdtOpbu8hDiDa2ezs.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h2 id="toc-2"><strong>二、为什么要引用RBAC权限模型？</strong></h2>
<p>RBAC中具有角色的概念，如果没有角色这个概念，那么在系统中，每个用户都需要单独设置权限，而系统中所涉及到的功能权限和数据权限都非常多，每个用户都单独设置权限对于维护权限的管理员来说无疑是一件繁琐且工作量巨大的任务。</p>
<p>而引入角色这个概念后，我们只需要给系统设置不同的角色，<strong>给角色赋予权限，再将用户与角色关联，这样用户所关联的角色就直接拥有了该角色下的所有权限。</strong></p>
<p>例如：用户1~用户8分别拥有以下权限，不同用户具有相同权限的我用不同的颜色做了区分，如下图：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/yA89CubvEeOz6Arb5nzf.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>在没有引入RBAC权限模型的情况下，用户与权限的关系图可采用下图的杨叔叔展示，每个用户分别设置对应的权限，即便是具有相同权限的用户也需要多次设置权限。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/9J0wCfyatpy3YvWGp5Gt.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>引入RBAC权限模型及引入了角色的概念，根据上面表格的统计，用户1、用户3、用户5、用户8拥有的权限相同，用户2、用户6、用户7拥有相同的权限，用户4是独立的权限，所以我们这里可以根据数据统计，以及实际的需求情况，可以建立三个不同的角色，角色A、角色B、角色C，三个角色分别对应三组用户不同的权限，如下图所示：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/m6tpFuwlwUd0fAYY4RfG.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>对应的上面的案例表格我们就可以调整为含有角色列的数据表，这样便可以清楚的知道每个用户所对应的角色及权限。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/xIII5yIbKsfDg3FiyQsN.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/2AO2LeHx2nPEJofxwyFi.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>通过引用RBAC权限模型后，对于系统中大量的用户的权限设置可以更好的建立管理，角色的引入让具有相同权限的用户可以统一关联到相同的的角色中，这样只需要在系统中设置一次角色的权限，后续的用户便可以直接关联这些角色。</p>
<p>这样就省去了重复设置权限的过程，对于大型平台的应用上，用户的数量成千上万，这样就可避免在设置权限这项工作上浪费大量的时间。</p>
<h2 id="toc-3"><strong>三、引入用户组的概念</strong></h2>
<p>我们依旧拿上面表格案例举例，虽然前面我们应用的RBAC权限模型的概念，但是对于大量用户拥有相同权限的用户，我们同样的也需要对每个用户设置对应的角色，如果一个部门上万人，那么我们就需要给这个部门上万人分别设置角色。</p>
<p>而这上万其实是具有相同的权限的，如果直接采用基础的RBAC权限模型的话，那么面对这样的情况，无疑也是具有一个庞大的重复的工作量，并且也不利于后期用户变更的维护管理，那么针对相同用户具有相同的权限的情况，我们便可以引入用户组的概念。</p>
<p>什么是用户组呢？<strong>用户组：把具有相同角色的用户进行分类。</strong></p>
<p>上面我们的数据表格案例中的用户1、用户3、用户5、用户8具有相同的角色A，用户2、用户6、用户7也拥有相同的角色B，那么我们就可以将这些具有相同角色的用户建立用户组的关系，拿上面的案例，我们分别对相同角色的用户建立组关系，如下：</p>
<ul>
<li>用户1、用户3、用户5、用户8→建立用户组1</li>
<li>用户2、用户6、用户7→建立用户组2</li>
</ul>
<p>因为用户4只有一个用户，所以直接还是单独建立用户与角色的关系，不需要建立用户组，当然尽管只有一个用户也是可以建立用户组的关系，这样有利于后期其他用户与用于4具有相同的角色时，就可以直接将其他用户添加到这个用户组下即可，根据业务的实际情况而选择适合的方案即可。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/dVlGieHqjUXXsuLKDfGZ.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/bcIyFVfQyNGxkRtDq4U2.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>通过案例表格的变化我们就可以直观的看出权限设置变得清晰简洁了，通过对用户组赋予角色，可以减少大量的重复的工作，我们常见的企业组织、部门下经常会出现不同用户具有相同角色的情况，所以采用用户组的方式，便可以很好地解决这个问题。</p>
<p>给具有相同权限的用户建立用户组，将用户组关联到对应的角色下，此用户组就拥有了此角色下的所有权限，而用户是属于用户组的，所以用户组下的所有用户也就同样的拥有了此角色下的所有权限。一个用户可以属于多个用户组，一个用户组也可以包括多个用户，所以用户与用户组是多对多的关系。</p>
<h2 id="toc-4"><strong>四、引入权限组的概念</strong></h2>
<p>权限组与用户组的原理差不多，是将一些相对固定的功能或者权限建立组的关系，然后再给此权限组赋予角色，目前我所接触的B端项目中使用权限组的概念的比较少，可简单地看一下关系图：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/ZNJZ2ufwJsO2LfWQT9lQ.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/m6CRaGAOXJc8ItwTQz82.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h2 id="toc-5"><strong>五、功能权限和数据权限</strong></h2>
<p>B端系统中一般产品的权限由页面、操作和数据构成。页面与操作相互关联，必须拥有页面权限，才能分配该页面下对应的操作权限，数据可被增删改查。所以将权限管理分为<strong>功能权限管理和数据权限管理。</strong></p>
<ul>
<li>功能权限管理：指的是用户可看到那些模块，能操作那些按钮，因为企业中的用户拥有不同的角色，拥有的职责也是不同的。</li>
<li>数据权限管理：指的是用户可看到哪些模块的哪些数据。</li>
</ul>
<p>例如：一个系统中包含多个权责清单（清单1、清单2、清单3），系统管理员能对整个系统操作维护，也就可以对系统中的所有清单都能操作（增、删、改、查）；假如分配给总部权责管理员的是清单1，那么他将只能对清单1进行操作（增、改、查）；普通用户也许只有查看数据的权限，没有数据操作的权限（查）,这里的操作是系统中所有可点击的按钮权限操作，列举的增删改查只是最常见的几种操作而已。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/ksTWaCSyUT3zPr78ksgK.jpeg" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h2 id="toc-6"><strong>六、实战案例总结</strong></h2>
<p>我目前所做的项目是一个关于权责管理平台的B端系统，关于系统中的权限需求我这里简单的介绍一下，并采用上面所总结的RBAC权限模型对实际业务需求进行设计分析：</p>
<ol>
<li>不同的区域管理员的权限各不相同<strong>（说明会存在不同的用户具有不同的权限，那么我们就可以采用角色对其进行规范）</strong></li>
<li>有大量的用户具有相同的权限（例如组织、部门等）<strong>（说明存在相同权限的用户，那么我们就可以采用用户组的概念）</strong></li>
<li>上级管理员拥有下级人员的所有权限<strong>（说明存在继承关系）</strong></li>
<li>不同用户所看到的数据和能编辑的数据不同，一些机密性的数据只允许部分人员看或者编辑<strong>（说明存在约束）</strong></li>
<li>会存在临时性的用户<strong>（说明需要支持新建新角色）</strong></li>
<li>同一用户会存在多个角色<strong>（多角色求合集或者切换用户角色）</strong></li>
</ol>
<p>简单说明一下，我所做这个项目的人员管理是在另外一个系统中管理的，权责平台只是调用另外一个平台的组织结构树即可，所以权限设置模块没有做人员管理的模块。</p>
<p>根据上面对需求的分析，整个权限管理模块中我们需要建立用户组管理模块、功能角色管理模块、业务（数据）管理模块、权限设置模块，下面就对每个模块做更细致的页面展示设计分析。</p>
<h3>1. 用户组管理模块</h3>
<p>用户组管理主要是对具有相同权限的用户分类建组，所以页面中我们需要有新建用户组的功能，每个用户组下我们需要关联对应的组织、部门、岗位、人员，让这些具有相同权限的用户在同一个用户组下，如下图：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/y41XCYVRNxSZwNlP7oMM.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h3>2. 功能角色管理模块</h3>
<p>B端项目中一般会建立几个默认的角色是不支持用户修改、删除的，例如最常见的系统管理员，而也会需要有其它角色的需求，所以此模块需要支持用户新建角色，功能角色是对大模块的页面和操作的权限设置，操作权限的颗粒度可以细分到每个页面的每一个按钮的操作，如下图：</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/wzVF36U8nuUt02wV0DKH.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h3>3. 业务（数据）角色管理模块</h3>
<p>业务角色是对页面中的数据查看的权限设置，而对于系统中的普通用户查看系统的权限是常用不变的，所以我们考虑默认有一个普通用户的角色，其它业务角色用户根据实际需求情况自行建立即可。</p>
<p>由于我们权责系统的特殊性，我们需要满足用户对部分数据可编辑且对部分数据的字段可编辑，按照常理来说，编辑的操作行为是属于功能权限的设置，但是这里的操作行为是建立在数据的基础之上的，所以如果把这里对数据的操作权限在功能角色模块中设置，就会显得混乱。</p>
<p>所以我们直接在业务角色模块中加入对数据的可编辑权限，这里在设置的时候更方便灵活。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/PfdcSiakwiO5I1SYmeHn.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/n3R0OZxWOb77wZbGMFwO.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<h3>4. 权限设置模块</h3>
<p>权限设置模块只需要设置权限分配的对象，选择对应的用户或者用户组，关联对应的功能角色和业务（数据）角色即可，这样就形成了一条完整的闭环的权限设置。</p>
<p><img data-action="zoom" class=" aligncenter" title="B端产品之权限设计（RBAC权限模型）" src="https://image.woshipm.com/wp-files/2022/08/KfRywR2gQE67g1SKxAN1.png" alt="B端产品之权限设计（RBAC权限模型）" referrerpolicy="no-referrer"></p>
<p>对于06同一用户会存在多个角色，我们系统是采用切换角色的模式来实现的，因为不同角色中存在互斥的情况，以及所涉及的领域不同，操作权限差距较大，求合集不利于控制权限，所以只能采用切换的模式实现。</p>
<h2 id="toc-7"><strong>七、总结</strong></h2>
<p>权限设置是B端项目必不可少的模块，也是令设计师头疼的一件事，但是只要理清楚实际的业务需求，合理运用RBAC权限设置的原理，其实也没那么难，关于权限设置的分享就到这来了，希望对处于B端设计的小伙伴有所帮助，也欢迎大家和我一起讨论关于设计的有趣事情哦！</p>
<p> </p>
<p>本文由 @设计小余 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5568368" data-author="1131797" data-avatar="https://image.woshipm.com/wp-files/2021/08/318nVsgz69UPnNMipSIh.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            