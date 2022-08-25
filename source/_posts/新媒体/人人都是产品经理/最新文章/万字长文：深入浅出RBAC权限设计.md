
---
title: '万字长文：深入浅出RBAC权限设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/08/osn7sOCAWa7z5xXpfLVu.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 25 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/08/osn7sOCAWa7z5xXpfLVu.jpg'
---

<div>   
<blockquote><p>权限管理是B端中常见的话题，它规定了用户各自的角色和可使用的职能，也对数据的安全提供了保障。本篇文章中作者结合自身经验，从四部分讲述关于权限管理的设计经验与设计方法。</p>
</blockquote><p><img data-action="zoom" class="size-full wp-image-853879 aligncenter" src="https://image.yunyingpai.com/wp/2022/08/osn7sOCAWa7z5xXpfLVu.jpg" alt referrerpolicy="no-referrer"></p>
<p>权限管理是B端产品绕不开的话题，本文总结了我对权限管理的设计经验与设计方法，共分为4个部分：</p>
<ol>
<li>权限管理的概念梳理</li>
<li>RBAC权限设计的一般步骤</li>
<li>设计功能权限的三板斧：基础版（权限、角色、用户管理）、进阶版（部门、职位、菜单管理）、拓展（版本管理）</li>
<li>如何设计数据权限</li>
</ol>
<p>所有内容均根据自身思考实践及经验借鉴而来，如有错误欢迎指正。</p>
<h2 id="toc-1">第一章：权限管理的概念梳理</h2>
<h3>一、权限是什么</h3>
<p>权限包括了功能权限和数据权限：</p>
<ul>
<li>功能权限是系统执行权限控制的基本单元，包括页面权限、菜单权限、按钮权限等</li>
<li>数据权限包括基础数据、业务数据、资源数据等</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/vL7tNzKkCQngIvDaPoeP.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>针对功能模块划分用户权限是一种粗颗粒度的划分方式，表现在不同用户可以查看相同的数据，但可执行的操作不同，如线上数据库的数据只有超管可以删除，其他人只能查看；针对数据划分用户权限是一种细颗粒度的划分方式，表现在不同用户进入同一页面/菜单时，可见的数据有差异，如运营经理可以看到部门所有数据，运营人员只能看到自己创建的数据。做权限设计时，首先要分清功能权限和数据权限的界限，不要为了图方便将二者揉起来。</p>
<h3>二、为什么需要权限管理</h3>
<ul>
<li>岗位职责的需要</li>
<li>数据安全的需要</li>
</ul>
<h3>三、权限设计的核心思想</h3>
<p>权限管理是用来控制用户可以访问而且只能访问某些资源的系统，根据该定义，我们可以绘制出如下示意图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/Usy0s1KWWOKCDb1ecLQ2.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>可以看出，用户和资源形成了错综复杂的映射关系，很难管理。要解决这一问题，有两种方法：一是减少用户/资源数，显然不切实际，这样就只剩下了一种方法——<strong>减少映射关系</strong>。</p>
<p>在详细介绍该方法前，我们先来看看数据库中是如何解决查询慢的问题的。大家可以思考一个问题，在【35、27、48、12、29、38、55】这组数列中如何快速找到数字55？</p>
<p>大部分人的第一反应就是一个个遍历，这样一共需要查询7次。而对数据库工程师来说，首先会<strong>找到一个媒介来构建这组数列的表示关系</strong>（见下图-平衡二叉树），然后再通过简单的判断只用3次就可以找到55了。这个媒介就是数据库中的<strong>索引</strong>，在数据量巨大的时候，利用索引进行查询的优势十分明显。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/YuNOIQoI6CpfQekDPtG6.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>如果这个例子不好理解，大家还可以联想下字典中的索引、书籍中的目录或是图书馆中的书架标签，核心思想都是<strong>抽象出对象的公共属性，再进行分类管理</strong>。</p>
<p>利用这一思想，我们再来回看如何减少用户和资源的映射关系。</p>
<ol>
<li>判断用户与用户之间是否有公共属性？</li>
<li>找到对权限有影响的公共属性，比如部门、职位等</li>
<li>不断抽象出中间媒介</li>
</ol>
<p>对于资源也是同理。</p>
<p>经过以上步骤，原本杂乱无章的映射关系就变得既简约又有层次（见下图），我们只要把权限赋予到抽象出来的虚拟媒介上，就能够大大降低管理的复杂程度。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/YAHCYozEnioLNqBguyzD.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<h3>四、权限管理模型的演进</h3>
<p>了解了权限设计的核心思想后，我们以CMS系统的更新为例来阐述权限管理模型的演进。</p>
<p><strong>1. ACL：基于用户的权限管理模型</strong></p>
<p>小王是一家创业公司的产品经理，负责一款CMS系统的设计。起初，网站的所有内容都由公司唯一的运营小红负责，所以小王就对小红的账号开启了所有权限。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/bcdBqqs62a7CwhKV7IuU.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>这种直接将权限绑定在用户账号上的方式就叫做基于用户的权限管理（ACL）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/8USiy52FbyPlQUmEmUys.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2. RBAC：基于角色的权限管理模型</strong></p>
<p>随着运营部门不断发展壮大，每次有新员工入职，小王都要为其单独配置权限，而且无法批量修改，十分繁琐。同时小王发现运营部门分工明确，部分人员负责内容审核，需要为他们开启审核管理的权限；部分人员负责产出内容，需要为他们开启内容管理的权限……这就导致小王经常会做一些重复性的工作。于是小王就想在现有的用户层上再抽象出一层——角色层，只要对角色设置权限，属于该角色的人员就自动拥有这些权限。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/mQherhBiQsF4RU2Iehmt.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>这种将权限绑定在角色上，再给用户账号赋予角色的方式就叫做基于角色的权限管理（RBAC），该模型于1992年由美国国家标准与技术研究院组织开发，是目前最通用的权限管理模型，节省了很大的权限维护成本。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/fhYBxA0QpQS9mdnAYtwR.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>GerorgeMason大学的教授Ravi Sandhu于1996年对RBAC模型进行改进，提出了RBAC96模型族，包括RBAC0、RBAC1、RBAC2和RBAC3四个模型。上图代表RBAC0模型，也是其他3个模型的基础。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/Gf7QAqvdAlilW0dsAkbs.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>a. RBAC1：角色继承的RBAC模型</strong></p>
<p>在CMS系统使用了一段时间后，小王发现了一个新问题——系统中存在的角色太多了，因为只要有权限不一样的用户加入系统，就需要新建一个角色，当用户权限分得很细的时候，甚至比ACL还繁琐，于是小王就想着手解决这一问题。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/HUWGuyszlCC1bv136jUA.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>点他发现角色之间存在着类似组织架构一样的上下级关系，比如COO>运营经理>运营主管>运营组长>运营人员>运营实习生，并且上级拥有下级的所有权限，同时可以额外拥有其他权限，于是他在现有的角色基础上又抽象出一层角色等级。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/eKJtgth9qbEbCsly2iMR.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>这种在角色中引入上下级关系的RBAC模型就叫做角色继承的RBAC模型（RBAC1），通过给角色分级，高级别的角色可继承低级别角色的权限，一定程度上简化了权限管理工作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/rSzMYcnWn5QwOWCcYsGu.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>另外角色间的继承关系可分为一般继承关系和受限继承关系。一般继承关系要求角色继承关系是一个绝对偏序关系，允许角色间的多向继承，即下级角色可以拥有多个上级角色，上级角色也可以拥有多个下级角色。而受限继承关系则要求角色继承关系是一个树状结构，角色间只能单向继承，即下级角色只能拥有一个上级角色，但是上级角色可以拥有多个下级角色。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/bpL2tVUTYBAUz9xEr5KL.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>b. RBAC2：角色限制的RBAC模型</strong></p>
<p>过了一段时间，运营经理小红向小王反馈，她的账号竟然可以看到公司的财务账单，经过核查，是小王由于粗心导致给小红的账号多绑了一个财务经理的角色。为了彻底规避这种风险，小王就让开发加了一条判断：当角色是运营经理时不能同时是财务经理。</p>
<p>这种针对角色进行限制的模型就叫做角色限制的RBAC模型（RBAC2），可以把限制具体地分为静态职责分离（SSD）和动态职责分离（DSD）：</p>
<p>SSD：</p>
<ul>
<li>互斥角色：同一用户只能分配到一组互斥角色集合中至多一个角色，比如用户不能同时拥有会计和审计两个角色</li>
<li>基数约束：一个用户可拥有的角色数目受限；一个角色可被分配的用户数量受限；一个角色对应的权限数目受限</li>
<li>先决条件角色：用户想要成为上级角色，必须先成为下一级角色，比如游戏中的转职</li>
</ul>
<p>DSD：允许一个用户具有多个角色，但在运行时只能激活其中某些角色，比如BOSS直聘，一个用户既可以是招聘者也可以是应聘者，但同时只能选择一种身份进行操作</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/VOcdueyzCmCckbzj9TDu.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>c. RBAC3：统一的RBAC模型</strong></p>
<p>RBAC3=RBAC1+RBAC2，既引入了角色间的继承关系，又引入了角色限制关系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/KYBNJy6s9AEXkrJDsg9g.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>d. 组：完善的RBAC模型</strong></p>
<p>现有的权限管理模型虽然已经对“角色”进行了层级优化，但并没有优化“用户”方，这就意味着每入职一个新员工，小王得单独为其设置权限，还是很麻烦，于是他利用抽象的思想将相同属性的用户进行归类。在公司里，最简单的相同属性就是“部门”了，如果给部门赋予了角色和权限，那么这个部门中的所有用户都有了部门权限，而不需要为每一个用户再单独指定角色。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/KtIEnZyvYP6XmYIzkziF.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>用户可以分组，权限同样也可以分组。在权限特别多的情况下，可以把同一层级的权限合并为一个权限组，如二级菜单下面有十几个按钮，如果对按钮的操作没有角色限制，可以把这些按钮权限与二级菜单权限合并为一个权限组，然后再把权限组赋予角色就可以了。</p>
<p>“组”概念的引入完善了RBAC模型，在简化操作的同时更贴近了实际业务，便于理解。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/gQQGtQubpEe6EEXbdlRN.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>3. ABAC：基于属性的权限管理模型</strong></p>
<p>为了内容的安全，运营经理小红向小王提了一个需求：负责内容管理的人员不可以在公司以外的地点发布内容。这可难倒了小王，因为现有的RBAC权限模型仅能对页面/功能/数据赋予权限，没法执行如此精细的权限控制。在查阅相关资料后，小王找到了该问题的解决方法——基于属性的权限管理模型（ABAC）。</p>
<p>ABAC是通过动态计算一个或一组属性是否满足某种条件来进行授权判断的，包括用户属性（如性别年龄）、环境属性（如时间地点）、操作属性（如编辑删除）和对象属性（如一篇文章）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/nMP6pyEoxnb3Ha0Qj6hu.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>跟RBAC相比，ABAC能够实现非常灵活的权限控制，可扩延展性也很高，几乎能满足所有类型的需求。但是设计起来比较复杂，而且对于单一属性可以通过编写简单的判断逻辑代替，所以还没有被广泛应用。</p>
<h3>五、权限管理与权限体系</h3>
<p>权限管理是指为解决某一具体的权限分配问题而采用的方法，比如解决文件的权限分配问题可以采用ACL模型，解决不同年龄段的用户可访问不同类型的电影问题可以采用RBAC+ABAC。</p>
<p>而权限体系是指整个系统内采用的权限管理方法的集合。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/1GPeyQ8Un2DSbS7p6IgO.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>本系列文章聚焦于单系统内的RBAC权限管理。</p>
<h3>六、权限设计的误区</h3>
<p><strong>1. 唯RBAC论</strong></p>
<p>尽管RBAC已经被广泛应用，但还是要避免一上来就这么做。权限的设计需要评估数据量和业务复杂度，如果预估的数据量特别少，业务又很简单，那完全可以用其他方式。</p>
<p><strong>2. 唯自由配置论</strong></p>
<p>不要认为把权限设置得灵活可配用户就满意了，实际上用户没有那么聪明，他会为角色名称而纠结，看到一系列的权限配置也会不知所措。如果你的业务能够抽象出一些固定角色和统一权限，那就把他们内置起来。</p>
<p><strong>3. 权限越多/越细越好</strong></p>
<p>权限不是功能列表，一味地细化而不注重实际业务，只会增加开发工作量，也不利于用户配置。可以仅选择常用的功能点作为权限配置，也可以将多个功能点抽象为一个权限点，如将“增删改”三个功能抽象为一个“管理”权限点。</p>
<h2 id="toc-2">第二章：RBAC权限设计的一般步骤</h2>
<h3>一、梳理角色</h3>
<p><strong>1. 罗列所有角色</strong></p>
<p>角色是一种抽象的身份，RBAC离不开角色，因此第一步就是从业务中找到所有可能涉及到的角色。</p>
<p>如果你做的是企业内部管理系统（如ERP、OA），可以参考组织架构找到所有角色（如产品经理、产品助理、项目负责人）；其他系统可以通过业务流程找到相关角色，如开展一次线上笔试按流程需要出题老师、题目审查老师、考场管理员、助理、监考老师、巡考老师、考生、阅卷老师。</p>
<p><strong>2. 找到各角色之间的关系</strong></p>
<p>找到所有角色后，第二步就是找出各角色之间的联系。常见的有继承、互斥和共享关系，还可根据实际业务找到角色之间的其他关系：</p>
<ul>
<li>等级/继承：产品总监、产品经理、产品助理、产品实习生</li>
<li>互斥：财务和审计不能是一个人</li>
<li>共享：阅卷老师和监考老师可以是同一个人</li>
<li>串行：先由产品经理进行设计再由开发人员开发</li>
<li>并行：前端后端一起开发</li>
<li>……</li>
</ul>
<p><strong>3. 分析角色是否需要内置以及是否需要隐藏</strong></p>
<p>分析哪些角色我们可以事先定好，哪些角色可由用户自定义。内置角色适用于角色通用且固定、使用频率高的情况，目的是为了简化用户的操作步骤。常把“管理员”角色进行内置，也可根据实际业务选择，比如线上考试系统，“考生管理”菜单就属于内置角色，添加到该列表中的账号只能是“考生”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/ll4qS3zVoKMBSf0jW5bX.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>同样还要考虑角色是否需要展示给用户，比如一些系统的“超级管理员”就不需要展示给用户。</p>
<h3>二、梳理权限</h3>
<p><strong>1. 梳理功能权限</strong></p>
<p>权限分为功能权限和数据权限，其中功能权限又可分为菜单权限和按钮权限。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/mqHuifzBMNgJBRqGB5nj.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>梳理功能权限一个最简单最实用的办法就是用“<strong>功能列表</strong>”（下图以“有赞”为例）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/mgTEvdPHyb9ha0XuHhFY.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2. 梳理数据权限</strong></p>
<p>数据权限就是系统中存在的数据、资源能够被谁查看和管理。说到数据权限，就不能不提数据库。</p>
<p><strong>1）表/对象</strong></p>
<p>表是包含数据库中所有数据的数据库对象，不同的业务数据存在于不同的表中，如下图从上到下依次为考生表、考场表和考官表。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/3KE4YSDl0hW9A5nlKCkR.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2）数据</strong></p>
<p>表中存放着二维数据，由行和列组成，如下图的考生表，每一行代表一个考生，每一列代表考生的一个属性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/iRodDrq19b6xhr4nybAJ.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>通过表和数据之间的关系，可以把数据权限分为以下四种情况：</p>
<p><strong>（1）基于系统的数据权限</strong></p>
<p>即系统中的所有表都能被大家看到并管理，也可理解为没有数据权限，比如管理员A、B都能看到并管理所有考生、考官、考场数据。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/FiOO7loJf35jrOvByb6Q.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>（2）基于对象的数据权限</strong></p>
<p>即按表划分数据权限，比如管理员A只负责管理考生，管理员B只负责管理考场。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/OVOHwcKaARmwkATKdOGN.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>（3）基于行的数据权限</strong></p>
<p>即按表中的数据行划分数据权限，比如管理员A只能管理B学校的考生，但不能管理C学校的考生；或者A部门的经理只能看到A部门职员的周报。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/j4kS578aXqT5ggNbJitu.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>（4）基于列的数据权限</strong></p>
<p>即按表中的数据列划分数据权限，比如管理员A只能看到考生的姓名，而管理员B可以看到考生的姓名、手机号和身份证号。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/NHTVACwgFpwxjpGJHEXh.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>在梳理数据权限时，可根据实际业务对对象、行和列的数据权限自由组合，比如针对学校A的管理员只能查看学校A的考生及考官的姓名和电话号码，无法查看身份证号这个需求，就使用到了基于行和列的数据权限。</p>
<h3>三、连接角色与权限</h3>
<p><strong>1. 连接角色和功能权限</strong></p>
<p>得到功能列表后，需要跟角色关联在一起，可直接在表后添加角色列，再根据业务对角色是否拥有该功能权限做判断。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/dU51t131Ei7SkDQ0L98x.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2. 连接角色和数据权限</strong></p>
<p>数据权限一般是一系列的规则，可通过文字描述附在上表后。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/laKJbThepChAqCnosGT3.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>3. 分析与整理</strong></p>
<p><strong>所有的权限都需要进行分配，但不是每个权限都值得让用户来配置。</strong></p>
<p>在上一步完成后，我们就建立起了所有角色和权限的联系，但上表还不能直接使用，在详细设计之前，还要分析出哪些权限需要用户手动分配，哪些不需要？哪些功能权限可以合并，以便减少用户操作次数？什么场景下数据权限需要可配置？等等这些必须得根据具体的业务进行判断。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/PAr8C0u36qfhMsJNJnKA.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>仍以“有赞”为例，上图是配置“线索管理”功能权限的实际页面，可以看到它只为用户提供“查看、编辑、转让、放弃、添加资料项、办理试听”这几个功能，其他的功能权限要么都归属于“查看”（添加、办理报名等），要么合并到一个功能里（“批量转让”合并到“转让”）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/k0TTlymW7sDh7JzOeUI6.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>理论上是可以把所有的功能权限拿出来让用户配置，但是考虑到用户体验，对权限进行分析和整理是非常有必要的。</p>
<h2 id="toc-3">第三章：设计功能权限的三板斧</h2>
<p>通过上述分析，我们得到了最终的角色与权限的关系，接下来就进入到如何设计界面的环节。</p>
<p>设计功能权限离不开最基本的三要素：<strong>用户管理、角色管理、权限管理</strong>；根据业务的不同，可能还会涉及更复杂的三要素：<strong>部门管理、职位管理、菜单管理</strong>，在这些之上还会配置不同的版本满足不同的客户需求，这就需要<strong>版本管理</strong>，下文将会对如何设计这些管理功能进行详细的介绍。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/8gutNYwsKcIvg7X8v9nG.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<h3>一、三板斧-基础版</h3>
<p><strong>1. 权限管理</strong></p>
<p>权限管理是为角色赋予权限，权限可以内置，也支持用户自定义，权限的配置需要跟角色绑在一起，当权限较简单且相对固定时，可由后端人员写死在代码里或者写死在配置文件里。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/Cq87zLSjZV5o8V2oRGF4.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2. 角色管理</strong></p>
<p>在“梳理角色”步骤中，我们列出了系统中涉及到的所有角色，“角色管理”就是对这些角色进行线上化的镜像和管理。</p>
<p>按角色的来源可分为用户自定义角色和系统内置角色：</p>
<p><strong>自定义角色：角色的名称和权限都可由用户自由配置，并可任意修改。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/qjlNP7l7kU0B5FpS9A4j.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>内置角色：角色的名称和权限由系统内置好，用户仅可查看无法修改。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/SCG6y2XRjp1tC8NjzKFk.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>设计“角色管理”主要有三个页面：</p>
<ul>
<li>角色列表页：展示系统中的所有角色，至少应显示角色名称以及查询、删除（自定义角色）、查看（内置角色）、新增、编辑等操作。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/vhG6ncQNQUhZfQmXWSVE.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<ul>
<li>添加角色页：必须输入不可重复的角色名称，可选填状态、备注、排序等信息。交互方式上可根据页面内容的丰富程度选择弹窗或抽屉的形式。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/soDG7Lhnhzyl4MRyJtaG.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<ul>
<li>配置权限页：可在创建角色的同时配置权限（见上图），也可在创建角色后配置权限（见下图），两种方式没有本质区别。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/l1JfOXa1ZKn9gwyPLakt.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>另外在一些系统里，绑定权限的这个载体不叫“角色”，而是其他的名字，比如在钉钉中叫“管理组”，这里我们要清楚它其实就是“角色”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/CDxlsZaEYBzKqAjzGf93.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>3. 用户管理</strong></p>
<p>“用户管理”是用于管理用户信息的，如更改用户角色、创建或删除用户、更改密码和用户信息。</p>
<p>设计“用户管理”主要有两个页面：</p>
<ul>
<li>用户列表页：展示系统中所有的用户。应支持新增、编辑、删除、导出、导入及批量操作。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/y1NNW8i1ZpuqC2CSjbbI.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<ul>
<li>添加用户页：根据业务选择创建时需要的字段。添加用户时，必须为用户设置角色，可选角色为“角色列表”中存在的自定义角色和内置角色。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/pwm5SxEfHO2worlzmvXU.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>同“权限分配”一样，“角色分配”也可以单独放在用户列表中的操作里，这样的交互更专一，但实际没有什么不同。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/IWiVlWijE95vt2lNpf71.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>4. 注意事项</strong></p>
<p><strong>1）用户与角色</strong></p>
<p>需要根据实际业务确定一个用户可以绑定多少个角色。如果可以绑定多个角色，角色之间有没有继承、互斥等关系，功能权限如何划分，这些情况都要提前考虑到。</p>
<p>另外，如果有内置角色，别忘了在内部的“运营管理平台”上设计专门针对“内置角色”的管理功能。</p>
<p><strong>2）角色间的关系</strong></p>
<p>上文中我们列出了角色之间的关系（等级/继承、互斥、共享等），现有的“角色管理”仅能通过一个用户绑定多个角色的方式实现“角色共享”，但没法实现角色间的继承和互斥。</p>
<p>角色间如果有继承关系，可通过下文的“角色组（职位）管理”实现；如果有互斥关系（如会计和审计），对于内置角色可以在代码中写死判断，对于自定义角色，可以让用户另外设置互斥规则。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/nWtKzrSYwG5b31OeYGAv.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>3）权限组</strong></p>
<p>上文说的分析与整理，其实就是建立权限组，将不必要的权限进行合并，可以简化用户操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/4acwVyYoyNAMlQPt7TkT.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>经过以上步骤，一个基本的权限系统就设计完成了，足够应付80%的场景。</p>
<h3>二、三板斧-进阶版</h3>
<p>如果是做OA系统的权限管理，或者对灵活度有较高的要求，那么可以了解下进阶版的权限管理三板斧。</p>
<p><strong>1. 部门管理</strong></p>
<p>“部门管理”有三种使用场景。第一种是为了构建企业的组织架构，在这种情况下，部门管理与功能权限没有关系，仅用于归类用户以及分配数据权限。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/7W2Kdgx97UXNVaTb05kM.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>与功能权限有关系的是下面两种场景：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/IcFWzba8billEvxlOzDz.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>第二种场景是为了承担“用户组”的作用。在上文介绍RBAC中，如果用户量很多时，将每个用户与角色权限匹配会十分麻烦，这时就需要将用户的共有属性做抽象，在企业中，用户的共有属性可以用部门来表示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/7vsYCSaxcCH6D1oWf1DI.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>第三种场景是为了承担“角色”的作用，可以为部门直接赋予功能权限，部门中的用户继承该部门的功能权限。若用户也拥有其他角色的权限（如下图的用户2），则实际的功能权限为二者的并集。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/imE4Kieud9q1cXjoL64L.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>另外在分配部门权限时，还需要考虑子部门与父部门的权限关系：可以选择同父部门的权限保持一致，也可以选择子部门继承父部门的权限，并可在其范围内进行编辑，还可以设置完全区别于父部门的权限，这取决于业务的复杂程度。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/ZNzzOWFmYLUTTmS9lNFc.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2. 职位管理</strong></p>
<p>“职位管理”有两种使用场景。第一种是为了完善员工信息，属于一种属性，与功能权限没有关系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/lhTB7761CGSLLg53KOXe.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>第二种场景与功能权限相关，是为了承担“角色组”的作用。“角色组”是为了满足上下级关系而衍生出的概念，比如“产品经理”应该拥有“产品助理”的所有权限，有了上下级后，再来一个“产品总监”的角色，就不用单独为其设置所有的功能权限，只需将它设为“产品经理”角色的父级，再添加一些特殊的权限即可。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/HF0w0no7zfl83aV9D5Se.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>3. 菜单管理</strong></p>
<p>不管是“部门”还是“职位”，解决的都是“用户”和“角色”怎样配置更灵活的问题。在RBAC中还有一个“权限”，目前对权限的管理只介绍了可以通过后端人员写死在代码里或者写死在配置文件里，如果功能权限经常变动，并且自由配置的需求极高，有没有更灵活的办法来管理权限呢？有！就是“菜单管理”。</p>
<p>“菜单管理”又被称为资源管理，是系统资源对外的表现形式。有了“菜单管理”，不仅可以让权限的管理更简单（不需要后端写死），还能够让系统展示更灵活（能够改菜单信息）。</p>
<p>“菜单”分为三类：</p>
<ol>
<li>目录：在系统内没有实际页面</li>
<li>菜单：存在实际页面</li>
<li>按钮：菜单中的可操作项</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/PevjekwpVUeUWSE1nnyK.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>设计“菜单管理”主要有两个页面：</p>
<p><strong>1）菜单列表页：</strong></p>
<p>导航菜单是分上下级的，因此可以用树状图表示，常见的菜单属性包括菜单名称、菜单类型（目录、菜单、按钮）、图标、排序、路由地址（浏览器访问菜单的地址）、组件路径（项目的组件文件的路径）、权限标识（查看、编辑、添加等）、是否外链、启用状态和创建时间。除了图中展示的字段，根据业务需求还可以增加“编号、是否打开新页面、是否隐藏、是否缓存（切换到其他菜单当前菜单会进行缓存）”等字段。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/tgtIt1fPkEBZGCBzZ8XX.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2）添加菜单页：</strong></p>
<p>添加目录：目录可以是外链，即点击后跳转到外部地址，必须带上https://或者http://，如果不是外链，则需要填入路由地址，由开发人员给出。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/vmlkjGBo9J8sK8WTAMV9.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>添加菜单：当菜单是外链时，规则同目录，若不是外链，则可选填组件名称、权限标识、组件路径（具体应跟开发讨论系统中是否有涉及）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/lehxbfIf8B1V4mYh31jO.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>添加按钮：添加按钮时，输入权限标识即可。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/we6iDsTReS8k8mOFkeAK.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"><br>
<strong>4. 注意事项</strong></p>
<p><strong>1）谁继承谁</strong></p>
<p>关于“权限继承”，细心的读者会发现我在第一章介绍RBAC时写过：“高级别的角色可继承低级别角色的权限”，而在本章中又说：“子部门可以继承父部门的权限”，是不是冲突了。</p>
<p>其实不然，假设现有AB两个部门，要在它们之上设立一个部门C，则C部门的权限为AB两个部门的并集，从这个角度讲，部门C继承了部门AB的权限，且部门C还可单独设置权限；而如果要给部门A下设一个部门C，部门C会继承部门A的权限，并可在此范围内细化权限。两种说法表达的意思是一样的，都是子级属于父级的权限范围内。</p>
<p><strong>2）功能权限最好不要绑在多个实体上</strong></p>
<p>在上面的介绍中，“部门”、“职位”都可以充当“角色组”直接绑定功能权限，但在实际中却很少有系统这么设计，根本的原因就是没有必要——功能权限最好只绑在一个实体上，意思是说，如果系统中已经有了“角色管理”（为角色设置功能权限），就没有必要再对部门或职位设置功能权限了，同样如果系统中已经为了部门/职位设置了权限，也就没有必要再引出“角色”这个概念了。因为在现实工作中，很少有人在部门、职位和角色上有单独的功能权限，即便是有，也可以通过新建一种“角色”来简化复杂度。如今大部分的OA系统上，职位和部门更多被用于用户归类以及管理数据权限。</p>
<p><strong>3）菜单管理如何实现权限组</strong></p>
<p>需要注意的是，“菜单管理”是精细到系统中最小的操作，可以直接用于分配角色的权限，但如果为了提升用户体验，需要给用户展示出合并后的功能权限时（见下图），则不可在“菜单管理”中直接设置“查看与操作”的按钮，而应该在“菜单管理”之上建一层专门用于展示给用户的功能权限，其中“查看与操作”权限绑定了“新建+编辑+删除”的按钮。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/GVVt14bD4AeZVmOWBQDN.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>5. 拓展：版本管理</strong></p>
<p>对于SAAS软件，常常会分多个版本来满足不同层次的客户需求，不同版本之间的功能权限会有差异。面对这种情况，可以通过“版本管理”来实现灵活管理（此“版本”非产品迭代的版本）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/8oZNEJZ0PIDWT8wYdt0f.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>设计“版本管理”主要有两个页面：</p>
<ul>
<li>版本列表页：列表展示版本的信息。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/UeybDDNkSeZTZ2TgWwQ7.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<ul>
<li>版本功能权限配置页：类似于为角色分配权限，这里可以理解为为版本分配权限。不同的是这里的功能权限会比“菜单管理”中的权限更细致。以“题目管理”为例，一般在“菜单管理”中，只会设置到一级页面的“添加、导入、删除、编辑题目”按钮，但在版本管理中会细化到题目类型，如免费版不能添加“听力题”，甚至会对功能的可用次数进行限制。有两种设计方案可以解决这一需求，如果每个版本之间的权限分得又细又多（见本节第一张图，考试星的版本功能对比），那么最好在菜单管理中覆盖掉所有子页面的按钮，可用次数以单独的规则进行限制；如果版本之间只是个别的细小功能有差异，则在现有“菜单管理”的功能基础上添加限制规则即可。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/8oHwWPDaAMWyYmNQZvL9.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>还有一种更复杂的情况，同一版本的不同客户之间也会有不同的功能权限，那么还需要对每一个客户配置功能限制。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/vfCS98y8wZ9s9FpujV3t.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">第四章：如何设计数据权限</h2>
<p>上文讲过数据权限分为四种情况（划分依据详见第二章）：</p>
<ol>
<li>基于系统的数据权限</li>
<li>基于对象的数据权限</li>
<li>基于行的数据权限</li>
<li>基于列的数据权限</li>
</ol>
<p>其中”基于系统的数据权限”可以理解为不分数据权限，因为大家看到的和可操作的内容都是一样的；“基于对象的数据权限”可以通过功能权限来实现，比如为用户A分配了客户表的权限，那么A就能够看到并操作所有客户，也就相当于为用户A分配了“客户管理”的功能权限。因此下文主要讨论后两种情况。</p>
<p>另外，数据权限的分配也可分为内置和用户自定义两种。内置数据权限属于系统中写死的规则，如本校老师只能看到本校的资源，公共库中的资源所有学校的老师均可看到，销售人员创建的线索只有自己能够管理等等，内置数据权限过于简单，也不在本文讨论范围内。</p>
<h3>一、基于行的数据权限</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/f3OcrPRrmH2Q4XmCXTMC.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>基于行的数据权限分为两种情况，一种是为对象（部门/角色）分配数据，如上级部门可以管理下级部门的所有数据；还可以将数据分配给对象，如共享文件。</p>
<p><strong>1. 为对象分配数据</strong></p>
<p><strong>1）无组织架构</strong></p>
<p>对于不涉及组织架构的系统，数据权限的设计比较简单，在为角色配置权限时，一并展示可分配的数据权限即可。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/oZsnYkfrJHaNeYp5Y4Yp.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>分配数据权限的前提是分配了对应的功能权限，比如要让计算机老师只能管理“软件工程”的所有题目，前提是要给老师开启“题库管理”的功能权限，否则老师连“题库管理”都看不到，何来管理其中的题目数据。当然功能权限不一定非要手动分配，也可以内置，比如蓝湖，加入的成员默认开启了“团队文件”的菜单，所以在配置时只需要展示数据权限列表。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/rWVLbE9waJGZXcldgwkB.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2）有组织架构</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/KCXPL8KCJfXZboOcOR5O.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>可以通过设置“管理范围”实现上下级之间的数据权限控制。比如针对上级可以看到下级的题库这一需求，可以设置一个“部门负责人”角色，并设置管理范围为“所在部门和下级部门”，然后将公司领导、各部门负责人都添加成这个角色，即可实现该需求。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/FJtbKRX8OjYzPLycrhZr.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>也可以通过设置“管理范围”实现跨部门之间的数据权限控制。比如针对研发部负责人可以看到IT部门题目的需求，则可以新建一个角色，管理范围选择“特定部门”，并勾选“研发部和IT部”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/54zVQppdjSjdp9VH2nqj.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>还可以通过设置“管理范围”实现同部门之间的数据权限控制。比如都是产品部，产品组长能看到下属创建的题目，但看不到产品总监创建的题目，产品助理只能看到自己创建的题目，这时就需要用到职位的层级关系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/PYMiADBE1yCuejAgCYiz.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p><strong>2. 为数据分配对象</strong></p>
<p>可以理解为把数据直接共享给某个角色/部门，常用于文件/资源的共享，下图是钉钉上对文件的权限管理。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/6GXO3MxKfCAaG3It8DVE.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<h3>二、基于列的数据权限</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/qrOOSxaAEypchO5PkZwO.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>如果说数据权限是对功能权限在纵向的扩展，那么字段权限就是在横向的扩展。因为设置数据列权限可以禁止指定角色对某些敏感字段的访问，如身份证号、交易金额等。</p>
<p>设计“列权限”主要有两个页面：</p>
<ul>
<li>入口：可以在创建角色时一同设置，也可以单独作为角色的一个操作，还可以放在“角色管理”中对所有角色批量设置，更可以在对应的菜单页面中进行设置。</li>
<li>列权限设置页：下图展示的是对所有角色批量设置列权限的设计，列出有各功能权限的角色和该菜单中的字段，由用户勾选即可。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="万字长文：深入浅出RBAC权限设计" src="https://image.yunyingpai.com/wp/2022/08/dWgyz977uDUikhg1eGjP.png" alt="万字长文：深入浅出RBAC权限设计" referrerpolicy="no-referrer"></p>
<p>全文完。</p>
<p>最后做个总结，本文第一章讲了权限管理的基本概念，第二章讲了RBAC权限管理在设计前的分析步骤，第三章和第四章分别讲了如何设计功能权限（权限、角色、用户、部门、职位、菜单、版本）和数据权限（基于行和基于列）。文中部分图片手机看不清，可用电脑端打开，内容如有错误欢迎指正。</p>
<div class="article--copyright"><p>本文由 @产品乱弹 原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自 unsplash，基于 CC0 协议</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5576757" data-author="53146" data-avatar="https://image.woshipm.com/wp-files/2022/04/8y6kwQm5ZKujwmYa80IY.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            