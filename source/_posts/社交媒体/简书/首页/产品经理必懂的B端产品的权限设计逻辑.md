
---
title: '产品经理必懂的B端产品的权限设计逻辑'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<p><b>一、B端后台权限的必要性和重要性。</b></p><p>权限控制是管理后台的重要功能，可以有效的提高系统的安全性，减少误操作、数据泄漏等风险的发生。</p><p>由于太过基础，很多人对于权限设置的认识很多是浮于表面或直接拿来主义直接照搬。权限结构设置好坏，直接影响企业生产、经营的效率，可以说，权限的设置企业来说至关重要。</p><p><br></p><p><b>二、ACL(Access control list), 权限访问列表</b></p><p>ACL权限控制模式是一种通过账号直接控制权限的访问模式，这种模式可以抽象下图。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="911" data-height="690"><img data-original-src="//upload-images.jianshu.io/upload_images/5974177-5dfacf774f2b99d3" data-original-width="911" data-original-height="690" data-original-format="image/png" data-original-filesize="34583" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p>这种模式很好理解，新建用户时直接赋予用户相应的权限，。</p><p><br></p><p>优点：</p><p>这种模式的优点在于其设置的灵活性，可为不同的用户赋予不同的权限。</p><p>企业中不同的岗位有不同职责，每个岗位或职级的工作内容有所不同，对应到权限系统就是分别对应不同的功能权限与数据权限。</p><p>适合人数少且系统权限较少的企业，设置灵活且高效。</p><p><br></p><p>缺点：</p><p>这种模式的缺点显而易见，不太适用中大型企业，易用性和扩展性较差。</p><p>中大型企业中由于人数较多，职责划分较为明确：产品、研发、技术、销售、财务...等岗位，各岗位的职责相对明确，采用此种模式设置权限或当人员发生岗位或职级变动去编辑权限时，需要针对用户一个个去设置权限，效率极低且不具备扩展性。</p><p><br></p><p>三、RBAC(Role-Based Access Control)，基于角色的访问控制</p><p>RBAC模式是现在企业中应用最为广泛的权限控制模式。</p><p><br></p><p>说RBAC模式前，先说几个非常重要的概念：</p><p>1、用户（账号）；2、角色、3、岗位；4、职级。</p><p><br></p><p>1、用户：系统中的用户对应着企业中一个个真实的用户，每个用户可拥有1个或多个账号。</p><p><br></p><p>2、角色：提起角色的概念，一般人很容易与岗位进行关联，角色与岗位关联也是可以的，但是当企业中同一个岗位有不同的职级时，角色与岗位关联在控制权限中无法精准控制。</p><p>在企业中，对于「销售」这个岗位，可能会细分为：「销售专员」、「销售经理」等不同的职级，「销售专员」、「销售经理」在实际的工作中的权限会有不同，在角色中「销售专员」、「销售经理」也不能等同于一个角色。</p><p><br></p><p>所以说，角色具体与岗位关联还是与岗位中的具体职级关联，主要取决于现实企业中具体场景。</p><p><br></p><p>3、岗位与职级。同一个岗位可能有不同的职级或者职称。</p><p><br></p><p><b>常见的RBAC模式：</b></p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="724" data-height="364"><img data-original-src="//upload-images.jianshu.io/upload_images/5974177-1308bdc4932d3546" data-original-width="724" data-original-height="364" data-original-format="image/png" data-original-filesize="19597" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p>常见的RBAC模式是先创建一个「角色」，角色中会定义相应的权限，然后在新建「用户」，选择用户所属的权限。</p><p><br></p><p><b>RBAC模式的权限一般会有3种：</b></p><p><b>1、数据权限</b></p><p>数据权限主要跟组织架构相关。比如同是销售部门的员工小A和小B，小A只能看自己维护的客户信息和交易信息，小B只能看自己维护的客户信息和交易信息，数据互不关联；员工小A和小B的领导小C，可查看小A、小B和自己部门手下员工的全部客户信息和交易信息。</p><p><br></p><p>一般有2种方式解决数据权限问题：</p><p>（1）通过菜单权限去控制可查看数据范围。</p><p>这种很好理解，就是将特殊的数据入口做成功能，赋予用户相关的功能权限后才能才看数据。</p><p>（2）通过企业组织的层级关系去限制数据权限。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="475"><img data-original-src="//upload-images.jianshu.io/upload_images/5974177-a1c4f79d78952233" data-original-width="1080" data-original-height="475" data-original-format="image/png" data-original-filesize="59976" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p>这是根据企业的组织架构，根据职员的职位高低来控制数据的访问权限。所以它通常的解决方案是和组织架构相关联的，具体逻辑如下：</p><p>（1）在给职员分配账号的时候，设置好对应的部门和职位</p><p>（2）当用户获取数据时，根据自己当前的部门和职位，获取到所有下属的职员信息</p><p>（3）将属于这些下属职员的所有客户信息显示出来，这个数据控制就完成了。</p><p><br></p><p><b>2、功能权限</b></p><p>功能权限主要是指不同的岗位工作职责不同，映射到系统中就是相关的功能权限不同。</p><p><br></p><p><b>3、特殊权限</b></p><p>在门店业务系统中，在收银时，针对同一个职级的不同员工，需要进行支付方式的限制。就需要在用户中进行特殊业务场景权限的设置。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="640"><img data-original-src="//upload-images.jianshu.io/upload_images/5974177-df1d13259bdf15b4" data-original-width="1080" data-original-height="640" data-original-format="image/png" data-original-filesize="109162" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p><br></p><p><b>优点</b></p><p>1、对比ACL模式，RBAC模式更贴合多数企业的适用场景。</p><p>2、具有很强的可扩展性。随着企业业务的发展，针对特殊的权限设置更具扩展性。</p><p>3、设置权限效率较高。当人员岗位或者职级调动后，直接修改该用户的角色即可。</p><p><br></p><p>在RBAC模式中，<b>用户与角色的关系是多对多的关系。</b></p><p>实际企业内部关系中，一个用户可能会有多个角色。</p><p>比如：集团下属的上海销售负责人，可能负责江苏或者浙江的销售市场，设置权限时，单个用户赋予多个角色即可实现，这时候该用户所拥有的权限则是所有角色权限的并集。（针对用户赋予「针对业务的特殊权限」，也能达到针对一个用户赋予多个角色进行权限管理的目的，具体采用哪种方式，需要根据具体的业务进行衡量采用。）</p><p><br></p><p><b>此外，RBAC还有几个扩展模型：</b></p><p>第一种：在角色上加入了上下级关系，上级可以继承下级的权限。</p><p>这种在适合大多数企业的数据权限。上级默认可查看下级的数据权限。</p><p>第二种：在角色之间加入了多个约束关系，如<b>角色互斥</b>。</p><p>针对一个用户赋予多个角色后，角色直接的只能可能是冲突的，尤其是有审核的场景。如：采购专员发起采购申请后，一般需要采购经理审核后进行采购。这时候如果将采购专员和采购经理角色赋予同一个用户，也就失去了审核的意义，这时候设置多个角色时需要进行必要的提示。</p><p>以上就是常见的权限设置及优缺点，RBAC模式在实际场景中因为极具扩展性、设置高效应用广泛，RBAC模式在设置权限中，有很多种通用的方法需要结合企业组织架构和实际业务场景灵活采用。</p>  
</div>
            