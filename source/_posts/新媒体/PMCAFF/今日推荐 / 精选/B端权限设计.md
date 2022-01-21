
---
title: 'B端权限设计'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/7cf0596cd24027f0b065944a39402ded-picture'
author: PMCAFF
comments: false
date: Sun, 09 Jan 2022 21:30:42 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/7cf0596cd24027f0b065944a39402ded-picture'
---

<div>   
<div><style>
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
</style><blockquote><p>权限设计的最终目标就是定义每个用户可以在系统中做哪些事情。</p></blockquote><h2>什么是权限？</h2><p>当我们谈到权限的时候，一般可以依次分为，菜单权限，功能权限、数据权限；</p><ul><li>菜单权限：按照模块-菜单理解，一个大模块下可能有多个菜单，比如咨询管理模块，可能会有留言资讯，会话列表，资讯管理，资讯配置四个菜单，菜单权限的意思就是我能不能看到这些菜单，比如说文案编辑岗位，那么我就需要看到资讯管理和资讯配置页面，如果是客服岗位，那么我就需要看到留言资讯和会话列表这两个页面，这就是菜单权限。</li><li>功能权限：拿同一个部门的两个岗位来举例子，比如项目部的项目经理和新招的项目助理，他们都需要看到内部OA系统，都可以看到公司中正在运行的项目，而项目经理则可以对公司新拓展的项目进行新增，添加到列表里，但项目助理则不能新增，只能查看，而项目经理则有增删改查的功能权限，这就是功能权限，也可以理解为按钮权限。</li><li>数据权限：数据权限一般位于菜单权限下，也有人把数据权限理解成为菜单权限，理解清楚就可以，在这里的数据权限大家可以理解为页面下的数据情况，在举一个同部门不同岗位的例子，人力资源部的HR经理和新招的HR助理，他们都可以看到公司的在岗人员，但HR经理则可以看到和编辑人员更详细的东西，比如工资，社保，工作年限，但新招的HR助理则在同一页面看不到这些数据，这就是数据权限，也可以理解为字段权限，一般来说，这里的数据权限已经非常细致，开发是不愿意做这么细的，或者也可以通过产品设计去规避这么细致的划分，因为权限分的越细致，改动的成本就越高，对于前期的需求调研也就更严格，但B端前期权限可能他们自己都不清楚，部署后也可能有变化，所以一般就只配置到功能权限就截止了。大概就是下面的意思<img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/7cf0596cd24027f0b065944a39402ded-picture" alt width="620" height="170" coffee-w="620px" coffee-h="170px" coffee-format="png" referrerpolicy="no-referrer"></li></ul><h2>权限设计怎么理解？</h2><p>在一般的组织中，用户的权限是由岗位决定的，由于用户可能面临转岗、离职等工作；所以岗位和权限的关系比用户和岗位的关系要稳定的多。<br>所以为了简化用户权限的分配操作，降低操作风险；同时，也便于把权限管理移交给统一的用户管理部门，一般会引入角色的概念，作为菜单权限和功能权限的抽象；如下图</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/9d14dc435695993459baac02cec4a11a-picture" alt width="805" height="382" coffee-w="805px" coffee-h="382px" coffee-format="png" referrerpolicy="no-referrer"></p><p>这里的超级管理员，应该大家还比较熟悉，就是最高权限者，其他的角色大家可以根据这个去理解，比如什么客服，销售，产品，研发等等的角色</p><h2>权限设计的进一步抽象</h2><p>考虑一种场景，一个集团有50个分支机构，每个分支机构下平均有3个部门，各个部门的组织架构是大体类似，在系统中都分为单据的录入者、复核者、审批者和查询者；这种情况下，如果按照角色来设置，需要设置50*3*4共600个角色；而且一旦面临的部门和团队的增加和撤销，也面临角色的大量设置和调整。</p><p>针对这种情况，我们可以设置一个数据组织，这块可以理解为一个分公司或者一个大的文件夹，由于这个组织结构比较均匀，所以用户权限其实等同于功能权限和菜单权限的交叉组合，功能权限表示横向的录入、复核、审批和查询权限；菜单权限表示具体某个分支机构下的部门。我们这里把这个组织称为数据组织。</p><p>如果使用数据组织那么就根据分公司或者部门来设置大角色，只需要预设置50*3=150个数据组织和4个角色。而且方便于将来的组织拓展，比如某个分支机构下要新增一个团队，按照原来的方案，需要新增4个角色，现在只需要在基础资料里加1个数据组织就可以了。大概下面这样<img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/fe04b2e6ea91e575272a630ba3fa7663-picture" alt width="667" height="381" coffee-w="667px" coffee-h="381px" coffee-format="png" referrerpolicy="no-referrer"></p><p>如上图所示，张三同时具有录入角色和审批角色，用户名本身绑定的数据组织是北京的团队；当张三切换到录入角色时，由于录入角色没有绑定数据组织，所以使用其自身的数据组织，那么张三只能新增北京分支结构团队A的单据；如果切换到审批角色时，由于审批角色绑定了上海的数据权限，所以张三只能查询并审批上海分支机构b提交的单据。</p><p>有的系统数据权限设计的更为复杂，可以分配给角色、数据组织和用户名本身，在此基础上建立优先级关系，从事实现更为复杂和灵活的权限配置。但这样越级处理或者越级分配权限容易造成BUG，一般不会这样分配。</p><h2>权限体系的实现价值</h2><p>跨系统解决了角色问题，从系统的角度把角色定义和分类，让每一个新建（注册、创建）的用户都有一套默认的角色，让系统分类有序、逻辑通顺。<br>比如上图，跨几个子系统时，我们可能有不同身份的用户，我们只要通过几个基础角色的组合即可以实现用户身份分类，从系统角度着眼，不要局限某一个子系统，例如下：</p><p>角色A=基础角色a+基础角色b+基础角色e<br>角色B=基础角色a+基础角色d+基础角色e<br>角色C=基础角色f+基础角色h+基础角色g<br>。。。。<br>。。。。</p><p>解决了身份问题，我们就可以不考虑身份问题，直接关联个性角色给某个用户，让用户可以控制目标功能，访问目标数据。<br>用户（小李）=&#123;身份（基础角色集合）默认不显示在前端操作页面+个性角色&#125;小李是新建服务管理员，只要关联服务管理的角色给小李就可以了。</p><h2>写在最后</h2><p>最近发生了很多事，致敬每一个认真生活的人</p></div>
  
</div>
            