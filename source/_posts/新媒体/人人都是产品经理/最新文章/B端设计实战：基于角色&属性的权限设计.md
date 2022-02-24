
---
title: 'B端设计实战：基于角色&属性的权限设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/n6XOuVpQQDAfS7Fl7NsD.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 24 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/n6XOuVpQQDAfS7Fl7NsD.jpg'
---

<div>   
<blockquote><p>编辑导读：“权限控制”是中后台的基础能力，用于管控操作人员在平台内可做的事项内容。即通过权限控制，可以决定哪些人在平台内可以做哪些事。本文作者围绕角色&属性的权限设计展开分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5331502 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/n6XOuVpQQDAfS7Fl7NsD.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>Hello，我是一名交互设计师。</p>
<p>随着3月暖春的即将到来，苏州的疫情却似乎没有好转的迹象，于是被迫居家隔离的我，反而有了更多的时间来思考复盘自己参与B端设计后的一些收获。</p>
<p>我现在参与的项目是资源生产中台，说白了，就是当字节内部的业务需要某类资源时（如教育业务需要题目资源、电商业务需要竞品价格资源、房产业务需要房源数据资源等等），它们可以选择联系资源生产中台，我们将根据业务的预算提供合规的资源采集，当然我们都知道，对企业而言，这类预算当然是越少越好。</p>
<p>那么，为了帮助企业降低预算，中台便开拓了众包业务（其实BAT早就开拓了），具备高学历的全职奶妈、在校大学生、兼职老师这批Freelancer群体，可以通过我们的众包平台注册为生产员进行接单，来帮助消化业务部门的资源采集诉求，从而也可以为自己赚取一笔额外的收入。</p>
<p>起初，为了快速搭建平台，我们在权限上做了简单处理，管理员和生产员在平台内的权限仅能通过研发和运营进行手动表格配置（可以参考下文中的ACL模型），然而随着业务的不断增多和平台人员的快速扩张，我们发现了一个严重的问题：</p>
<blockquote><p>因为权限设计的比较简单，随着业务需求的定制化或用户类别的细分化，已经开始大量占用研发时间和运营人力，这种现象严重违背了中台“降本提效“的初衷。</p></blockquote>
<p>那么为了解决这个问题，我们需要对众包平台的权限系统进行重构设计，实现灵活智能的平台权限配置，减少对研发和运营的人力占用，以下是我在进行设计时的一些思考和尝试：</p>
<h2 id="toc-1">一、什么是权限控制</h2>
<p>“权限控制”是中后台的基础能力，用于管控操作人员在平台内可做的事项内容。即通过权限控制，可以决定哪些人在平台内可以做哪些事。</p>
<h3>1.1 权限控制的价值</h3>
<ul>
<li>可以让管理者基于安全规则和策略，配置不同用户合理访问对应资源；</li>
<li>可以让用户能够在有效的限制范围内访问被授权的资源。</li>
</ul>
<p>在B端场景中，通过权限控制可以让工作群组内不同的角色专注于自己的工作范围，可以降低操作风险发生概率，便于进一步管理。</p>
<h3>1.2 权限控制的应用场景</h3>
<p>权限控制的应用主要有两种场景：</p>
<p><b>版本管理场景</b></p>
<p>基于版本进行产品权限的分配和控制，该场景主要应用于有商业化诉求的B端产品。 通过权限控制将产品功能切割为普通权限功能和高级权限功能，从而衍生出普通版和高级版，甚至更多版本的产品。 这些版本功能范围基本处于一个包含关系，如下图的企业版就包含了标准版的功能权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/nKOsdwJhK3KaFEeHRvU8.jpg" alt width="3840" height="2160" referrerpolicy="no-referrer"></p>
<p><b>权限管理场景 </b></p>
<p>基于角色或属性规则进行产品权限的分配和控制，该场景适用于逻辑复杂模块繁多需要提升工作效率的B端产品。 通常一个角色对应一组静态权限，而一个用户可能有多个角色，如下图“分析师”角色便对应了一组数据权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/okJNQwebooW8KuZhBpdh.jpg" alt width="3840" height="2160" referrerpolicy="no-referrer"></p>
<p>通常一组属性规则对应一组动态权限，如下图授权规则便对应了一个主体的动态资源权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/o3FfEMqQN3P9dG2g3LRr.jpg" alt width="3840" height="2160" referrerpolicy="no-referrer"></p>
<p>在B端中后台的设计中，最常见的应用场景为“权限管理”，权限管理涉及的维度也会比版本管理更为复杂。</p>
<h2 id="toc-2">二、怎么设计权限控制？</h2>
<h3>2.1 了解和选择权限技术模型</h3>
<p>权限控制的实现依赖于技术实现，而常见的技术模型主要分成如下3类：</p>
<ul>
<li>【ACL】Access Control Lists 访问控制列表</li>
<li>【RBAC】Role-based Access Control 基于角色的权限访问模型</li>
<li>【ABAC】Attribute-Based Access Control 基于属性的权限访问模型</li>
</ul>
<p>不同体量的权限系统，我们可以参考不同的权限模型进行梳理和设计。 <b>【ACL】访问控制列表 </b>ACL通常用于配置哪些用户可以访问操作哪些资源。当权限系统体量小，用户有直接对应具体功能点即可满足系统诉求时，可以考虑使用ACL模型作为参考。 实现原理：每一项资源，都配有一个列表，这个列表记录的就是哪些用户可以对这项资源操作。当系统试图访问这项资源时，会首先检查这个列表中是否有关于当前用户的访问权限，从而确定当前用户可否执行相应的操作。 ACL权限中，只有用户、资源这两个要素：</p>
<ul>
<li>用户：是发起操作的主体，可以是1个人，也可以是1个用户群组。例如：后台管理系统的用户、OA系统的内部员工、设计部门等。</li>
<li>资源：用户可以访问操作的客体，例如：页面、文档、数据等。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/pV5XjQTKnjHsqjG4Rfhj.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>ACL常用于部门隔离场景，适用资源如人事页面、客户页面。如下图部门成员配置页，通过Excel表格来一次性批量导入部门成员信息，使这批成员在提交后自动获取该部门下的数据权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/gsMpLU4SgpDbM8ji08ZH.jpg" alt width="3840" height="1520" referrerpolicy="no-referrer"></p>
<p><b>拓展：【DAC】自主访问 </b></p>
<p>DAC在ACL基础上，增加了权力下放的能力，允许拥有权限的用户再次将权限授予其他用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BjwoSpxQjwG6Mii61ral.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>DAC常用于文件管理场景，适用资源如培训文档。如下图所示，拥有文档编辑权限的用户可以将编辑权限再次授予其他用户。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/tI3RN1W557zJH8FKUDQg.jpg" alt width="3840" height="710" referrerpolicy="no-referrer"></p>
<p><b>拓展：【MAC】强制访问 </b></p>
<p>MAC在ACL基础上，增加了双重验证的限制，要求用户和要访问的资源必须具备相应的安全等级关系才可获取权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/YdWRTNkqhibzLPnOENNE.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>MAC常用于保密信息场景，适用资源如保密数据。如绝密级的财务数据只能被企业高级用户查看、访客级用户无法查看企业级的文档、机密级的部门架构信息仅能被部门负责人级别的账号查看。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/IiOZzFQztHZ1Clz63Ok1.jpg" alt width="3840" height="1420" referrerpolicy="no-referrer"></p>
<blockquote><p><b>ACL模型优势： </b>研发实现快速简单，不需要耗费较多开发成本。</p>
<p><b>ACL模型劣势： </b>当拥有大量用户和资源时，维护成本变得极高，每次有新用户&新资源加入时都需要重新挨个配置每个用户与每个资源的关系，不适用于频繁变更用户权限的场景。</p></blockquote>
<p><b>【RBAC】基于角色的权限访问模型 </b></p>
<p>RBAC通常用于配置哪些角色拥有哪些权限，而哪些用户可以拥有这些角色。 实现原理：把用户按角色进行归类，通过用户的角色来确定用户能否针对某项资源进行某项操作。 RBAC模型的三要素为：用户、角色、权限。</p>
<ul>
<li>用户：是发起操作的主体，可以是1个人，也可以是1个用户群组。例如：后台管理系统的用户、OA系统的内部员工、设计部门等。</li>
<li>角色：用于连接了用户和权限的桥梁，每个角色可以关联多个权限，同时一个用户也可以关联多个角色，那么这个用户就有了多个角色的多个权限。</li>
<li>权限：用户可以访问的资源权限，包括：页面权限、操作权限、数据权限。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/J53sejq55jsbvMJGwXRN.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>RBAC常用于企业数据和功能管理场景。如下图当某用户被分配分析师角色时，则该用户账号自动获取了分析师角色下的所有权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/PHOGkwOG4ZekSpbjCut6.jpg" alt width="3840" height="2160" referrerpolicy="no-referrer"></p>
<p><b>拓展：【RBAC1】角色分层 </b></p>
<p>RBAC1模型是在RBAC模型基础上，引入了角色分层的概念，即角色具有上下级的关系，每个等级对应不同的权限组，从而实现更细粒度的权限管理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/tsB7WcV1RW9GkF0GaTds.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>RBAC1常用于角色内的多级别分层场景。如下图，通过权限组的形式对管理员角色进行再次权限分层，例如可以将设计师角色分成设计师、设计主管、设计经理和设计总监等多级权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/jPWoBIhjQg9Lm4qvUB1O.jpg" alt width="3840" height="1838" referrerpolicy="no-referrer"></p>
<p><b>拓展：【RBAC2】 角色限制 </b></p>
<p>RBAC2模型是在RBAC模型基础上，增加对角色的限制约束。主要包括以下约束:</p>
<p><b>互斥关系</b>: 同一用户只能分配到一组互斥角色集合中至多一个角色，互斥角色是指各自权限互相制约的两个角色。例如一个用户不能同时具备销售和财务2个角色，否则就可以自己审批自己的报销申请了。</p>
<p><b>基数约束</b>:</p>
<ul>
<li>一个角色被分配的用户数量受限，例如一个部门内能只能存在1个总监角色；</li>
<li>一个用户可拥有的角色数目受限，例如一个供应商生产员可以同时最多拥有组长和员工2个角色；</li>
<li>同一个角色对应的访问权限数目受限，例如一个业务职能员工角色最多只能拥有1个业务的数据权限，而中台职能员工角色可以拥有多个业务的数据权限。</li>
</ul>
<p><b>先决条件</b>: 简单理解即如果某用户想获得上级角色，必须得先获得其下一级的角色。例如一个员工角色必须在系统内先晋升为主管角色，才能继续晋升为经理角色。</p>
<p><b>运行互斥</b>：允许一个用户具有两个角色的资格，但在运行中不可同时激活这两个角色。</p>
<p><b>拓展：【RBAC3】 统一模型 </b></p>
<p>可以单纯的理解为RBAC0 + 1 + 2的集合体，在基本模型的基础上同时具备了分层能力和限制能力。</p>
<blockquote><p><b>RBAC模型优势： </b>当拥有大量用户和资源时，维护成本较低。</p>
<p><b>RBAC模型劣势： </b>无法对单个用户、单个资源进行个体定制。比如，某角色拥有创建、删除的权限，当我们要对针对拥有该角色的某个用户去掉删除的权限。那么，我们就必须创建另一个角色来满足需求。如果这种情况很频繁，就会丧失角色的统一性，降低系统的可维护性。</p></blockquote>
<p><b>【ABAC】基于属性的权限访问模型 </b></p>
<p>ABAC通常用于配置哪些属性的用户在哪些属性的环境下可以对哪些属性的资源进行哪些操作。 实现原理：通过各种属性条件来动态判断一个操作是否可以被允许，也可以理解为我们俗称的“配置规则”。 我们在配置规则时需要定义属性条件和资源的关系。其中属性条件又分成以下3类：</p>
<ul>
<li>用户属性：如年龄、部门、职位、性别等；</li>
<li>环境属性：如时间、地点、场景等；</li>
<li>资源属性：如资源状态、资源创建时间、资源存放位置、资源保密等级等。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/KdCYYDjhMURjPaLfZqHa.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>以1个权限控制策略为例：</p>
<blockquote><p>只有设计部门内职位为视觉设计师的用户，在工作时间内且处于上海办公区时，才可以访问和编辑草稿状态的人物素材库。</p></blockquote>
<p>其中“设计部门”、“视觉设计师”为用户属性，“工作时间”、“上海办公区”为环境属性，“草稿状态”为资源属性，只有命中符合这些属性条件时，该规则才会生效，用户才能具备对相应资源的操作权限。 我们设置的属性条件也可以定义“且/或”的关系，当我们定义“且”关系时，必须所有属性条件命中才会生效规则；当我们定义“或”关系时，只需要命中部分属性条件就可以生效规则。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ePJL93fbAc3Z2lYZr0Te.png" alt width="3840" height="932" referrerpolicy="no-referrer"></p>
<p>ABAC的使用场景较灵活，常用于复杂多变的策略定制场景。如定制架构可见范围、定制会话权限等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Vtk2EX2HhG85DJX2pFMn.jpg" alt width="3840" height="2722" referrerpolicy="no-referrer"></p>
<ul>
<li><b>ABAC模型优势： </b>能够根据上下文动态执行，可以发挥权限控制最大的灵活性，满足更细颗粒度的场景需求。</li>
<li><b>ABAC模型劣势：</b> 学习成本比较高，随着规则（策略）的不断增多，管理和维护成本也会攀升。</li>
</ul>
<p>综合以上3大权限模型的优劣来看：</p>
<ul>
<li>ACL模型基于资源进行配置，适用于用户量少、更新频次低、无明确职能划分的小型组织，开发成本低但后期管理维护成本高，适合作为平台搭建初期时的临时过渡方案；</li>
<li>RBAC模型基于角色进行配置，适用于用户量一般、更新频次一般、有明确职能划分、较少定制权限的中型组织，开发成本高但后期维护成本低，适合作为平台管理少量内外部用户时的方案；</li>
<li>ABAC模型基于属性进行配置，适用于用户量多、更新频次高、职能划分复杂多变、有安全合规诉求、权限定制多样化的大型组织，能够在保障效率的同时降低安全风险，适合作为平台管理大批量复杂用户时的方案。</li>
</ul>
<h3>2.2 基于业务梳理关键信息</h3>
<p><b>第一步：选择权限模型 </b></p>
<p>不同的业务特点指向不同的使用场景，因此我们需要基于业务特点选择合适的权限模型。 以众包平台为例，平台具备B/C双端的特点，因此在进行权限设计时需要考虑两端的使用场景和受众群体。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Cb19spn2dJJIVLoD7tsD.png" alt width="1930" height="820" referrerpolicy="no-referrer"></p>
<p>基于以上业务特点，我们可以发现B端后台管理权限分配更适合基于“角色”进行设计，而C端前台的生产权限更适合基于“属性”进行设计。</p>
<p>完成模型选择后，我们需要基于模型进一步梳理平台内所需的角色、属性和权限信息。</p>
<p><b>第二步：明确关键角色和属性 </b></p>
<p>角色是连接用户和权限的桥梁，因此我们需要对平台内的B端管理角色进行穷举。 角色定义通常取决于岗位职能划分和任务流分工。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bQJsfhKYyGpnSnREEszD.png" alt width="1928" height="736" referrerpolicy="no-referrer"></p>
<p>超级管理员是一种特殊的角色，主要作用是为了添加首批管理人员，通常为隐形状态，且该角色不可通过配置进行分配。 通过盘点，我们在该步骤可以得出一份「角色列表」。 属性是触发规则运行的基本条件，我们需要将平台内所有影响规则运行的属性进行整理归类。 关键属性通常取决于平台用户数据的字段定义、用户操作环境的客观因子和业务资源数据的标签维度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/mDydyTjob76EoStflklC.png" alt width="1932" height="288" referrerpolicy="no-referrer"></p>
<p>通过盘点，我们在该步骤可以得出一份「属性列表」。</p>
<p><b>第三步：梳理权限 </b></p>
<p>权限是用户能够访问的资源，本步骤需要将平台内所有权限点按照类型进行整理归类。权限点主要有以下几种类型需要盘点：</p>
<p><b>页面权限</b>即用户在平台内可见的页面，由导航菜单来控制，包括一级导航菜单、二级导航菜单，甚至三级导航菜单，只要用户有对应导航菜单的权限即可访问页面。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/PP7MlEolZSBDlwimdAaZ.jpg" alt width="3840" height="2160" referrerpolicy="no-referrer"></p>
<p><b>操作权限</b>即页面内的功能按钮，包括我们常规认知的增删改查操作。 如下图众包平台的权限示例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/b8wxhcv5twhTXp3tf9Qb.jpg" alt width="3840" height="2160" referrerpolicy="no-referrer"></p>
<p>在实际操作场景中，部分操作权限会因状态而发生变化，在盘点操作权限时，需要梳理状态关联性来检查是否有缺漏，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/N3W3oC3fDYll3PCIJ0g6.png" alt width="1388" height="256" referrerpolicy="no-referrer"></p>
<p>一期因时间问题，我们统一仅基于页面配置“查看”与“操作”两类权限。</p>
<p><b>数据权限</b>即用户在同一页面看到的数据，不同数据权限的用户在同一页面内将看到截然不同的数据。 如下图示例，切换力家长或GauthMath项目后，在同一页面内看到的数据完全不同：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MHp2AVoGqa7TBkJvQlLa.png" alt width="3840" height="1248" referrerpolicy="no-referrer"></p>
<p>B端后台出于数据安全性考量，各业务会期望数据处于仅自己业务管理员可见的状态，因此我们发现站在业务角度使用“项目组”的形式来分隔数据更加简单有效，通俗来讲就是每个业务对应一个项目，将用户加入项目内即可获取对应业务的数据权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bpMYSiEYFI0Y1Ft9nSS3.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>各业务在面向C端生产角色开放数据权限时，通常需要综合效率、质量和成本等多种目的来进行考量选择，权限也会针对相同类型的用户进行集中配置，因此针对生产角色的会更多基于“用户群组”的形式来进行数据分隔，我们将相同类型的用户进行编组，再对整组用户按照分流规则授予相应的数据权限，群组在命中分流规则后可在任务广场内看到相应的任务数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/oN76PjTOH1z5qoqVJjzz.png" alt width="3624" height="1712" referrerpolicy="no-referrer"></p>
<p>通过盘点，我们在该步骤可以得出一份「权限点列表」。</p>
<p><b>第四步：关联权限</b></p>
<p><b> 关联角色和权限</b>：结合「角色列表」、「属性列表」和「权限点列表」，我们可以整合出一张完整的权限对应表。在梳理角色和权限的关系时，可以通过“角色行为穷举”来进行权限点转化和连接。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/pTNhEzZC0NxGFS6U6iwZ.png" alt width="3840" height="674" referrerpolicy="no-referrer"></p>
<p>以众包B端的几个管理角色为例，进行“角色行为穷举”：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ONeyX6khSpDvNJG1iRaI.png" alt width="1684" height="1004" referrerpolicy="no-referrer"></p>
<p><b>关联属性和权限</b>：属性也可以通过同样的方式来进行权限点转化和连接。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ATyW0VSmHZLHezyOTfrB.png" alt width="3840" height="674" referrerpolicy="no-referrer"></p>
<p>以众包C端的规则为例，进行“属性群组行为穷举”：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/vz2yFzWIjfL5ii3FtZt7.png" alt width="1626" height="1050" referrerpolicy="no-referrer"></p>
<p>通过盘点，我们在该步骤可以得出一份「角色&属性权限对应表」。</p>
<h3>2.3 设计赋权流程</h3>
<p>在明确了角色&属性与权限的关系后，需要去设计赋权的交互方式。</p>
<p><b>B端管理账号赋权</b></p>
<p>众包B端用户以产品和运营为主，用户数量和权限数量一般（100以内），有明确的管理职能划分，主要负责管理和监控平台内的多个子模块进展，因此较适用于RBAC基于角色的权限模型。</p>
<p><b>第一步：明确流程方案 </b></p>
<p>首先，我们需要确认B端数据权限是否需要做分隔处理：</p>
<ul>
<li>通常仅服务于单个业务的后台数据权限，不需要做分隔处理，可以直接通过角色赋权账号；</li>
<li>涉及到多业务的保密数据时，需要做权限分隔处理，数据权限不可以和角色直接关联绑定。</li>
</ul>
<p>如下为数据权限不需要隔离的流程方案：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/aXx1n6e7d5S3kRkRQERf.png" width="1369" referrerpolicy="no-referrer"></p>
<p>如下为数据权限隔离的流程方案：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ApLdN60F7O0WjMQHlmuK.png" width="1650" referrerpolicy="no-referrer"></p>
<p>考虑到众包平台期望未来接入更多业务的愿景，我们选用数据权限隔离的流程方案，之后就可以开始设计角色配置方案了。</p>
<p><b>第二步：创建角色并配置操作权限 </b></p>
<p>首先，我们需要新增一个角色管理页，通过该页面进行角色数据的创建和管理，当业务接入平台时，我们会提供一些默认角色供业务使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/NTcC8ixGYY4feo3YhJYU.png" alt width="2736" height="1604" referrerpolicy="no-referrer"></p>
<p>如果提供的默认角色无法满足业务诉求，那么业务运营可以在该页面内编辑默认角色或新增角色，为角色自定义页面权限和操作权限。 操作项必然依托于页面，因此我们在设计角色配置交互时：</p>
<ul>
<li>通过Table设计将页面权限与操作权限进行关联配置，在用户提交配置时将页面权限赋予角色，这样可以保障拥有该角色的账号能够查看到相应导航页面并对相关页面进行操作；</li>
<li>以嵌套子表格的设计表现一级页面和二级页面的父子关系，当勾选一级页面的操作权限时视为勾选其所有子页面的操作权限；</li>
<li>从系统的运行逻辑角度出发，对查看权限（可以看到该页面导航）和操作权限（可以看到该页面内的操作项）进行交互关联，当用户仅勾选某页面的查看权限时，不会联动选中操作权限；当用户勾选操作权限时，会联动选中查看权限。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/OJKlEbdpjAZYFHUKgoht.png" alt width="3456" height="1600" referrerpolicy="no-referrer"></p>
<p>完成角色配置设计后，就需要考虑如何将角色权限与管理员账号进行关联了。</p>
<p><b>第三步：对账号配置角色和数据权限</b></p>
<p>前文提到，考虑到业务自有数据的私密性诉求和安全性考量，因此不能将数据权限直接赋予多业务通用的角色身份，而选择与私密性更好的账号进行绑定配置，为此我们需要新增一个账号管理页，通过该页面可以对管理账号和用户账号数据进行创建和管理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MOPRISFD77kWeyjxrNuY.png" alt width="2736" height="1828" referrerpolicy="no-referrer"></p>
<p>在设计管理账号配置交互时：</p>
<ul>
<li>遵循RBAC权限模型，通过角色配置项实现对账号页面&操作权限的集中赋予，角色配置项采用映射展示项的Checkboxes+Table设计，便于用户勾选角色后能够直观看到对应的角色所拥有的页面权限和操作权限；</li>
<li>考虑到频繁请求全量数据权限容易造成接口崩溃，因此在配置管理员权限时，将角色配置和数据权限控制拆成了2步，通过增加环节数降低全量数据请求的频次；</li>
<li>众包的数据权限分为项目-车间两级，因此在配置数据权限时会优先引导用户先为账号选择项目数据权限，完成项目选择时会在下方展示项目下的子级权限控制入口，用户可以在项目下继续为账号选择车间数据权限（低频操作）。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/RFvn6TTzzEtMtj1zGzyD.png" alt width="3452" height="3548" referrerpolicy="no-referrer"></p>
<p>完成以上角色配置 + 管理账号配置的2步操作后，我们完成了对管理账号的赋权，之后通过将管理账号分发给业务运营，实现业务接入平台后的管理成员就位。</p>
<p><b>C端生产账号赋权 </b></p>
<p>众包C端的用户分为Freelancer和供应商两类，用户数量大（数千人），权限需要依赖多类复杂的属性组合因素（任务类型 x 职能 x 语言 x 学科 x 年级），且需要根据不同业务要求进行调整（随着业务数量增多，调整次数将持续翻倍），且部分业务仍有跨国合规诉求和权限定制诉求，需要根据变量条件来灵活调整，因此较适用于ABAC基于属性的权限访问模型。</p>
<p><b>第一步：明确流程方案 </b></p>
<p>C端用户的赋权设计可以基于推荐渠道用户和普通用户两个角度进行考量。 我们通常会通过线下招募、熟人转推荐和供应商签约3种渠道来招募定向的高质量用户，这部分用户通常会具备相应的基础生产能力，我们可以直接对这类用户进行批量赋权。</p>
<p>当批量渠道用户无平台账号时，我们可以采用如下邀请赋权的流程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ZCZ2mwP5N8WTAT3paWik.png" alt width="3316" height="520" referrerpolicy="no-referrer"></p>
<p>当批量渠道用户有平台账号时，我们可以继续采用邀请赋权的方式，但考虑到减少对用户的干扰，我们也可以采用如下管理员手动赋权的流程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/IdOFDrHovAtmLX8kEskG.png" alt width="2396" height="520" referrerpolicy="no-referrer"></p>
<p>而针对普通用户，因为我们不了解这类用户是否具备完成任务生产的能力，所以我们需要面向这类用户增加培训考试环节，因此会采用如下考试赋权的流程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/CO7bRYCpRl1cxxzoFogB.png" alt width="2696" height="228" referrerpolicy="no-referrer"></p>
<p><b>第二步：创建用户群组</b></p>
<p>因C端用户数量较多，通常我们会基于某类属性规则对用户进行标签分组（如高质量数学生产组、高效率英语质检组、低成本知识点标注组），也就是我们熟称的“用户群组”。</p>
<blockquote><p>角色和用户群组的概念区分： 角色赋予的是主体，主体可以是用户，也可以是用户群组 ；角色是权限的集合 ；用户群组是用户的集合 。</p></blockquote>
<p>基于“用户群组”进行批量赋权可以极大的提升平台配置效率。 因此，我们需要新增一个群组管理页，通过该页面进行群组数据的创建和管理，当业务接入平台时，业务可以通过该页面将目标用户批量导入对应用户群组内。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/dWTH520SGLNsnu6o1bCT.png" alt width="2752" height="1822" referrerpolicy="no-referrer"></p>
<p><b>第三步：对用户&群组配置操作权限</b></p>
<p>完成群组的创建后，我们需要赋予群组相应的任务操作权限，但C端任务操作权限需要依赖于组合复杂的能力标签（任务类型 x 职能 x 语言 x 学科 x 年级），为此我们需要将相应任务的能力标签具象为易于用户理解的“证书”，而C端用户要获得这些“证书”，则需要进行相应的培训“考试”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/JeGq2ZyxEOuhCBvyFu3U.png" alt width="3840" height="1750" referrerpolicy="no-referrer"></p>
<p>基于“能力证书”的逻辑，我们首先需要新增一个证书管理页，证书管理页用于配置要获得一个任务的操作权限需要用户拥有哪些能力证书。为了满足灵活多变的业务场景，通常一个任务会包含多个属性变量组（如工作职责 x 学科 x 学段 x 人群组），因此证书配置的设计也会以规则组的形式，来提供用户对属性变量条件进行设置的能力。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/HEevC2nJzSbt0RqFnSsv.png" alt width="2736" height="1540" referrerpolicy="no-referrer"></p>
<p>在完成配置后，C端的用户在领取任务时将基于任务的属性条件来确认当前用户是否已具备所需的证书，若已具备则进入任务操作界面，若未具备则弹出如下的考试引导，需要用户通过考试后才能获得相应的证书。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/vK2N6J67xgAIfOwwqrQT.png" alt width="790" height="667" referrerpolicy="no-referrer"></p>
<p>完成能力证书与任务操作权限的关联后，我们需要基于用户类型来展开不同的路径设计，前文提到，C端用户的赋权设计需要基于推荐渠道用户和普通用户两个角度来进行考量：</p>
<p>推荐渠道用户指通过线下招募、熟人转推荐和供应商签约等渠道来招募的高质量用户，这部分用户通常会具备相应的基础任务生产能力，我们可以直接对这类用户进行批量赋权。因此，我们需要新增一个能力管理页，能力管理页用于配置哪些用户可以通过白名单直接拥有哪些能力证书（任务操作权限），当业务接入平台时，业务可以通过该页面将证书（即任务操作权限）分配给对应用户或群组。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MtybzVfnUEgZagt84q5o.png" alt width="2736" height="1604" referrerpolicy="no-referrer"></p>
<p>而针对普通用户，我们并不了解这类用户是否具备完成任务生产的能力，所以我们需要面向这类用户增加考试环节，为此我们需要新增一个考试管理页。考试管理页正是用于配置要获得一个能力证书需要进行哪些考试。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/sCOvggPgkb2U2FymYlKe.png" alt width="2732" height="1536" referrerpolicy="no-referrer"></p>
<p>无论是通过管理员批量授权还是通过考试获得授权，得到授权的用户将得到一份证书，并展示在C端用户的个人中心内。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/6Erh4t37yzjpXcjaLo3D.png" alt width="2418" height="1328" referrerpolicy="no-referrer"></p>
<p><b>第四步：对群组配置数据权限</b></p>
<p>通过能力证书可以赋予用户对某类任务的操作权限，但不会直接赋予用户任务数据权限，因此任务数据仅对群组开放，若用户不在对应群组内，则无法看到任务数据。 这么处理的原因在于业务生产策略的差异化，同类任务在不同业务考量（如成本、效率、质量）下会倾向于采用不同的生产流程和人员配置。</p>
<p>因此将同类用户并入群组，再基于不同的属性变量条件对群组进行数据权限的分流配置，更符合复杂场景下策略自动化的诉求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/nI2j5c4IKG6syRmiMlLt.png" alt width="2764" height="1688" referrerpolicy="no-referrer"></p>
<p><b>第五步：将用户加入群组</b></p>
<p>将用户加入群组的方式分为3种：管理员批量导入、活动邀请加入和自动分群标记加入。</p>
<p><b>1、管理员批量导入</b>：该方式已在“第三步”中有所提及，这里不再赘述。</p>
<p><b>2、活动邀请加入</b>：通过运营线下活动招募或熟人转介绍的渠道用户通常没有平台账号，因此我们倾向于通过活动邀请来将这类用户加入群组。 首先，我们需要新增一个活动管理页，通过该页面进行邀请活动数据的创建和管理，当业务接入平台时，业务可以通过该页面配置群组邀请码、链接或二维码。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/f2q3aRgoqor6kz8gSqBA.png" alt width="2736" height="1722" referrerpolicy="no-referrer"></p>
<p>通过邀请活动完成注册或指定操作的用户将被自动加入该活动关联的群组，如下为活动示例Banner入口，通过该入口完成招募操作的用户将被自动加入框题任务用户群组，从而获得框题任务的生产操作权限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TbvLnezpie5omll98OpR.png" alt width="2616" height="400" referrerpolicy="no-referrer"></p>
<p><b>3、自动分群标记加入</b>：对于已注册的其他用户，我们会基于业务对生产策略的诉求，抽象出关键的属性变量条件，系统将按照特定条件自动将符合条件的用户加入群组，将不符合条件的用户移出群组。</p>
<blockquote><p>注意事项：为了确保安全性，邀请活动可设置失效时间； 完成赋权/授权后，需要对用户进行及时的消息推送。</p></blockquote>
<h3>2.4 提取通用设计点</h3>
<p>通过以上流程设计，我们实现了B/C端的权限控制，但为了提升后续相关权限控制的拓展，我们需要抽象提取可以复用的通用设计点，形成设计规范：</p>
<p><b>页面权限设计 </b></p>
<p>当前用户无页面权限且不可申请时，在导航内隐藏对应菜单项；</p>
<p>当前用户无页面权限但支持申请时，在导航内显示对应菜单项，点击选中该菜单项后在页面内显示“抱歉，你无权访问该页面”空态提示：</p>
<p>若支持用户线上申请，则显示“申请权限”按钮，点击后弹出申请理由表单；</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/RPSkUtKmQEnvjsYkuYwJ.png" alt width="2736" height="1520" referrerpolicy="no-referrer"></p>
<p>若仅支持线下申请，则仅显示“抱歉，你无权访问该页面，请联系XXXX开通权限”文案提示。</p>
<p><b>操作权限设计</b></p>
<p>当前用户无操作权限且不可申请时，隐藏对应操作；</p>
<p>当前用户无操作权限但支持申请时，点击后弹出引导申请Popover提示；</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/pMCsSWWnPjCpqeggGP7p.png" alt width="2736" height="1604" referrerpolicy="no-referrer"></p>
<p>当前用户有操作权限但暂时不可操作时，按钮显示为禁用态，不支持点击。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TS6tlvJz3GURsiaXvu5T.png" alt width="1368" height="802" referrerpolicy="no-referrer"></p>
<p><b>数据权限设计：</b></p>
<p><b>项目权限的切换与展示</b>：当前账号具备的项目权限数=1时，仅显示项目名称，无交互效果，不支持切换。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/2ZEgm5Wq6e2Y83BAzO28.png" alt width="1768" height="160" referrerpolicy="no-referrer"></p>
<p>当前账号具备的项目权限数>1时，显示项目名称和下拉按钮，支持点击切换。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/N6eYRLE8kPjBpYp64za2.png" alt width="1768" height="846" referrerpolicy="no-referrer"></p>
<p><b>无项目权限的处理</b> ：当前用户无项目数据权限且不可申请时，在项目选项列表中隐藏无权限的项目；</p>
<p>当前用户无项目数据权限但支持申请时，在选中对应项目后，在页面内展示“抱歉，你无权访问该项目”空态提示：</p>
<p>若支持用户线上申请，则显示“申请权限”按钮，点击后弹出申请理由表单；</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/IPyHYDrnP9vupG5j7Krq.png" alt width="2736" height="1520" referrerpolicy="no-referrer"></p>
<p>若仅支持线下申请，则仅显示“抱歉，你无权访问该项目，请联系XXXX开通权限”文案提示。</p>
<h2 id="toc-3">三、总结</h2>
<p>权限系统作为中后台的基础能力之一，能够让不同组织下的不同人员专注于自己的工作领域，降低数据风险，实现人员和数据的高效管理。 在选择权限技术模型时：</p>
<ul>
<li>面向用户量和权限量少、更新频次低、无明确职能划分的小型组织进行权限设计时，可以考虑参考开发成本低的ACL权限列表权限设计，基于账号进行授权设计；</li>
<li>面向用户量和权限量多、更新频次多、有明确职能划分的中型组织进行权限设计时，可以考虑维护成本低的RBAC角色权限设计，基于角色进行授权设计；</li>
<li>面向用户量和权限量多、更新频次高、无明确职能划分、有安全合规诉求、权限定制多样化的大型组织，可以考虑够在保障效率的同时降低安全风险的ABAC属性权限设计，基于属性规则进行授权设计。</li>
</ul>
<p>在权限设计时需要基于业务角度考虑页面权限、操作权限和数据权限等多个方面：</p>
<ul>
<li>页面的赋权设计需要注意关联体现页面间的层级关系与对应操作权限；</li>
<li>操作的赋权设计需要注意数据状态变化导致的操作变化；</li>
<li>数据的赋权设计需要注意多业务数据是否需要基于安全性进行分隔处理；</li>
<li>注意提取通用设计点，以保证平台内权限设计的统一性。</li>
</ul>
<p>通过以上基于角色&属性的权限设计，我们实现了权限分配流程的100%线上配置化，将有效的释放原来用于支持权限开发90%以上的研发人力和运营人力，将这部分人力资源更好的应用于中台能力建设。</p>
<h3>#专栏作家#</h3>
<p>愚者秦，微信公众号：feather-wit，人人都是产品经理专栏作家。先后任职于爱奇艺、字节跳动的一枚体验设计师，同时是兼职写小说的斜杠青年，善于总结和抽象设计方法，热衷于探索不同用户场景下的产品策略。</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5330566" data-author="86856" data-avatar="http://image.woshipm.com/wp-files/2018/10/kvMfyGYHdrCviAUcOssl.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            