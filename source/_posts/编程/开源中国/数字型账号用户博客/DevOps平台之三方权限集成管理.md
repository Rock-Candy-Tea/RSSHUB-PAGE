
---
title: 'DevOps平台之三方权限集成管理'
categories: 
 - 编程
 - 开源中国
 - 数字型账号用户博客
headimg: 'https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJVrFURnren91Jn6HIlj6POicZ6LqSLu3n5F6hZ6X01kpLeMXaRcHqFTZDZAsYGAVJ4asOxJ1WNsQMw/640?wx_fmt=jpeg'
author: 开源中国
comments: false
date: 2021-04-15 04:08:58
thumbnail: 'https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJVrFURnren91Jn6HIlj6POicZ6LqSLu3n5F6hZ6X01kpLeMXaRcHqFTZDZAsYGAVJ4asOxJ1WNsQMw/640?wx_fmt=jpeg'
---

<div>   
<div class="content">
                                                                                                                                                                                        <p style="color:#333333; text-align:center"><img height="325" src="https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJVrFURnren91Jn6HIlj6POicZ6LqSLu3n5F6hZ6X01kpLeMXaRcHqFTZDZAsYGAVJ4asOxJ1WNsQMw/640?wx_fmt=jpeg" width="578" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span><strong><span style="color:#888888">​转载本文需注明出处：微信公众号EAWorld，违者必究。</span></strong></span></p> 
<p> </p> 
<p><span style="color:#000000"><strong>前言：</strong></span></p> 
<p> </p> 
<p><span>本文主要介绍DevOps的第三方服务的权限管理设计过程中的一些思路和理念，包括一些权限模型概念的分享、DevOps本身的权限控制设计、在适配第三方服务时遇到的问题和解决思路以及对DevOps第三方权限管理模块的优化建议。</span></p> 
<p> </p> 
<p><span style="color:#000000"><strong>目录：</strong></span></p> 
<p> </p> 
<p><span>1.总体思路</span></p> 
<p><span>2.权限设计模型讲解</span></p> 
<p><span>3.DevOps-自身的权限管理设计</span></p> 
<p><span><span>4</span><span>.DevOps-第三方服务权限管理设计</span></span></p> 
<p><span><span>5.总结</span></span></p> 
<p><span>在使用之前版本的DevOps过程中，用户很可能在使用任务模块、代码模块和介质模块时遇到没有权限执行操作的问题，这个会带给用户很大的困扰，举个例子，测试人员遇到一个bug，在平台里想要创建一个bug工作项，结果报错没有权限，最终细究才发现尽管在DevOps当前项目中该用户是测试人员，但对应的项目管理工具（如Jira）中该用户并没有被添加测试人员的角色，这时就需要用户去Jira中再进行授权，为避免这种情况，我们提出了第三方权限管理的需求。</span></p> 
<p><span style="color:#4a94e7">1.总体思路</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>1.先明确需要被管理权限的第三方服务主体是什么：</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>目前DevOps涉及到操作权限跟第三方服务账号权限挂钩的有项目管理工具、代码管理工具和介质管理工具，细化一下就是Jira、Zentao、Gitlab、Github、Bitbucket、Nexus、Harbor等服务。</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>2.再要了解每一个第三方服务的权限系统设计模型是什么样的：</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>目前大部分系统所采用的权限设计模型都是基于角色的访问控制（RBAC）模型，Jira、Zentao、Gitlab、Bitbucket等服务全部是按照RBAC模型来设计的权限模块。</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>3.如何适配到DevOps平台也很重要：</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>集成至DevOps平台分两个思路，一个就是将第三方服务的权限模块拿过来，在DevOps的平台界面由配置管理员做一个权限配置管理，另一个思路就是将第三方服务的授权连同DevOps的授权模块结合起来，在进行DevOps成员授权的同时自动去为指定用户分配好第三方服务的权限。</span></p> 
<p><span style="color:#4a94e7">2.权限设计模型讲解</span></p> 
<p style="color:#333333; text-align:justify"><span>在这里简单的讲解一下我所了解的一些市面上常见的权限设计模型。</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>1．访问控制列表（Access Control List, ACL）</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>访问控制列表就是用一个列表的形式来维护对某个资源的访问控制，它是早期的实现访问控制的模型，用户可以通过ACL定义什么人或什么等级的人可以访问什么资源，每一个ACL都包含一个用户和组的列表， 以及它们的访问权限，ACL优点是可以很直接的把人和权限绑在一起， 但也会有诸如无法批量编辑用户权限、不适用于用户量大的场景等问题。</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>2．自主访问控制（Discretionary Access Control, DAC）</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>DAC和上面提到的ACL非常类似，区别在于ACL权限分配是通过配置表来实现的，而DAC模型下用户可以自主将自己拥有的权限分配给其他用户，如NTFS、Linux都是采用的DAC权限模型。</span></p> 
<p style="color:#333333; text-align:justify"><span>DAC也存在一些问题，如超级管理员权力太过于集中化，可以随意变更所有用户的ACL，且拥有超级管理员权限的用户就可以对服务器所有的资源进行任意操作；再有当用户将权限分配出去之后，就很难再对该权限的分配进行约束，被授权人员可以自由的再次分配该权限。</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>3．强制访问控制（Mandatory Access Control, MAC）</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>由于DAC对权限的控制过于的松散，MAC为此应运而生，MAC的设计理念是每个用户和每个对象都有独属于自己的权限标识，用户对对象有无操作权限就是根据双方的权限标识是否匹配来实现的，通常而言，这套匹配机制由系统写死，用户无权更改。</span></p> 
<p style="color:#333333; text-align:justify"><span>MAC适用的目标包含一些涉密机构以及等级制度严格的行业，但对于商业服务系统而言MAC过于死板，所以并不适用。</span></p> 
<p style="color:#333333; text-align:justify"><span>有些安全策略，只有用户知道，系统是无法知道的，那么适合自主访问控制。</span></p> 
<p style="color:#333333; text-align:justify"><span>有些安全策略，系统是已知的，是固定的，不受用户影响的，那么适合强制访问控制。</span></p> 
<p style="color:#333333; text-align:justify"><span><strong><span>4．基于属性的访问控制（Attribute-Based Access Control, ABAC）</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>ABAC是一种为解决行业分布式应用可信关系访问控制模型,它利用相关实体(如主体、客体、环境)的属性作为授权的基础来研究如何进行访问控制。基于这样的目的,可将实体的属性分为主体属性、客体属性和环境属性,这与传统的基于身份的访问控制（IBAC）不同。在基于属性的访问控制中，访问判定是基于请求者和资源具有的属性，请求者和资源在ABAC 中通过特性来标识，而不像IBAC 那样只通过ID 来标识，这使得ABAC 具有足够的灵活性和可扩展性，同时使得安全的匿名访问成为可能，这在大型分布式环境下是十分重要的，ABAC基于任意的属性组合来达到访问控制的目的，是最灵活的访问控制模型，从另外一个角度来看，也是最复杂的模型。</span></p> 
<p style="color:#333333; text-align:justify"><span>不同于常见的将用户通过某种方式关联到权限的方式，ABAC则是通过动态计算一个或一组属性来是否满足某种条件来进行授权判断（可以编写简单的逻辑）。属性通常来说分为四类：用户属性（如用户年龄），环境属性（如当前时间），操作属性（如读取）和对象属性（如一篇文章，又称资源属性），所以理论上能够实现非常灵活的权限控制，几乎能满足所有类型的需求。</span></p> 
<p style="color:#333333; text-align:justify"><span>例如规则：“允许所有班主任在上课时间自由进出校门”这条规则，其中，“班主任”是用户的角色属性，“上课时间”是环境属性，“进出”是操作属性，而“校门”就是对象属性了。</span></p> 
<p style="color:#333333; text-align:justify"><span>总结一下，ABAC有如下特点：</span></p> 
<ul> 
 <li> <p><span>集中化管理</span></p> </li> 
 <li> <p><span>可以按需实现不同颗粒度的权限控制</span></p> </li> 
 <li> <p><span>不需要预定义判断逻辑，减轻了权限系统的维护成本，特别是在需求经常变化的系统中</span></p> </li> 
 <li> <p><span>定义权限时，不能直观看出用户和对象间的关系</span></p> </li> 
 <li> <p><span>规则如果稍微复杂一点，或者设计混乱，会给管理者维护和追查带来麻烦</span></p> </li> 
 <li> <p><span>权限判断需要实时执行，规则过多会导致性能问题</span></p> </li> 
</ul> 
<p style="color:#333333; text-align:justify"><span><strong><span>5．基于角色的访问控制（Role-Based Access Control, RBAC）</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>因为DAC和MAC的诸多限制，于是诞生了RBAC，并且成为了迄今为止最为普及的权限设计模型。</span></p> 
<p style="color:#333333; text-align:justify"><span>RBAC概念最初是在1992年由美国国家标准局（NIST）所提出。该权限模型引入了Role的概念，目的是为了隔离User（即动作主体，Subject）与Privilege（权限，表示对Resource的一个操作，即Operation+Resource）。</span></p> 
<p><span>简单来说，RBAC对权限的控制不是直接将权限授予的用户，而是在用户和权限之间建立一个角色，每一种角色对应一组权限，对用户的授权是通过授予用户角色来实现的。这样做优点是，不必在每次创建用户时都进行分配权限的操作（ACL的授权方式），只要分配给用户对应的角色即可，而且角色的权限变更比用户的权限变更要少得多，这样将简化用户的权限管理，减少系统的开销。</span></p> 
<p><span><span style="color:#4a94e7">3.DevOps-自身的权限管理设计</span></span></p> 
<p style="color:#333333; text-align:justify"><span>DevOps所采用的权限控制模型是RBAC模型，初始超级管理员账号拥有平台所有权限，超级管理员可以将平台配置相关权限授予配置管理员，由配置管理员去承担角色权限分配、用户授予角色的工作，平台的每一个菜单、每一个按钮、每一个环境都配置了独自的权限码，角色的权限配置十分细化，下图是DevOps在项目中对项目成员授权的示例。</span></p> 
<p style="color:#333333; text-align:justify"><span>项目角色授权界面：</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicETKI9Kb916icDKnoFdLOlBBb1mqn2FTEMqhLBb21BZ7rAviaLIeAoI1w/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>项目成员赋予角色界面：</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POic7D9uXS3IzHVSXTqVffOWjdiaSibytEQic16qddnUJzoqicT87ehEibESVibw/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>DevOps配置管理员可以在平台页面的图中所示位置预设一组项目角色模板，用于在新建项目时初始化配置项目的角色信息。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicicia9IqfWTIibsa7PpnbLnZRNhNbXj9ibxmIs7JjNOHoJhDS54mbmDS1CA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>对于平台级权限DevOps平台也有独立的权限模块，平台会初始化系统管理员、项目管理员、产品管理员等关键角色，管理者可根据需求自定义角色。</span></p> 
<p style="color:#333333; text-align:justify"><span>平台角色授权界面：</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicn5zMia796kImmeH7m8icjiaibpuxG6ttLsic6OR2zoPvvfGWnwxianKBXaicQ/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>平台成员授予角色界面：</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicfMGN1diasV315fnx9H2cpKNM8LKxbpqopKIczicUyUh8pz1tUUUt9eMw/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicHhZQUtLqSvvkhlbuqTicX1icTCRSOpjFKf5pOdLEI543EF8xPVGpfsIQ/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span><span style="color:#4a94e7">4.DevOps-第三方服务权限管理设计</span></span></p> 
<p style="color:#333333; text-align:justify"><span><span>目前DevOps的第三方服务权限管理采用的是第一种思路开发设计的，就是将第三方服务的权限模块拿过来，在DevOps平台做一个配置管理，目前集成完毕的由Jira的权限管理模块以及Gitlab的权限管理模块，今天以Jira的权限集成作为讲解。</span></span></p> 
<p style="color:#333333; text-align:justify"><span style="color:#4a94e7"><strong><span style="color:#4a94e7">Jira权限集成：</span></strong></span></p> 
<p style="color:#333333; text-align:justify"><span>Jira的权限管理模块跟DevOps的权限管理模块十分类似，都是初始化配置好角色，然后在项目中为指定角色添加用户。</span></p> 
<p style="color:#333333; text-align:justify"><span>项目角色人员配置页面：</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicFNTnRMZuyUoChNW5LNprbXFLu0Mic01B3NicAMAGlDJCjYLljLABxDuw/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span>下图是给示例人员1授予DevOps示例项目的Developer角色的过程：</span></p> 
<p> </p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POic7vvYr1SLuP8EaQ1HxiaauJY7U0lAH51G6nQgfB9apXIbCJWV5n9rcLA/640?wx_fmt=png" width="538" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><span>项目角色权限配置界面：</span></p> 
<p> </p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POiccH6LbJxciaLV0ZxrGfzzcGV8QicibVZdibicBEQibSjAic1DguHY4yGNlvKQg/640?wx_fmt=png" width="538" referrerpolicy="no-referrer"></p> 
<p><span>下图是将项目中的某一权限配置给指定角色的过程：</span></p> 
<p> </p> 
<p style="text-align:center"><img height="263" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POicYsulZYJqBkOIXCGvWTkGsj6quSzgia1lKIlzN54iadRWvR0BK6P13yPA/640?wx_fmt=png" width="538" referrerpolicy="no-referrer"></p> 
<p><span>对于DevOps平台而言，只需要Jira默认的四种角色已足够使用，故略去了Jira自定义角色权限的功能，我们只需要适配可以在DevOps配置给DevOps项目成员Jira项目中的角色即可.</span></p> 
<p><span>关键维度信息示例：</span></p> 
<p><span>1.人员A在DevOps项目X中</span></p> 
<p><span>2.DevOps项目X关联了Jira项目Y</span></p> 
<p><span>3.人员A在DevOps的用户信息需同步至Jira</span></p> 
<p><span>4.人员A也在Jira项目Y中</span></p> 
<p><span>5.人员A在DevOps项目X的权限和在Jira项目Y的权限匹配</span></p> 
<p><span>关键维度信息确认完毕就可以正式的开发了，首先明确2点，DevOps本身支持项目成员的管理，关键维度信息1解决；DevOps中所有项目都是可以通过项目Code关联Jira中的相应项目的，关键维度信息2解决；</span></p> 
<p><span>Jira权限管理最终效果如下图展示，配置人员可以通过变更项目来管理不同项目中成员的Jira权限，表格横轴展示的当前项目在Jira中拥有的角色种类，纵轴展示的是当前项目在DevOps平台中的项目成员列表，当为某个DevOps项目成员授予Jira项目的角色后，系统先会自动判别该成员是否有对应的Jira用户，若没有则自动同步，这一步解决了关键维度信息3；其次系统会通过Jira的接口将该用户添加至Jira项目的指定角色中去，这一步解决了关键维度信息4；纵轴的人员名称后面的小问号展示了该人员在当前DevOps项目中的角色信息，这一步解决了关键维度信息5；至此，Jira权限管理介绍完毕。</span></p> 
<p><span>图示：</span></p> 
<p style="text-align:center"><img height="263" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJVrFURnren91Jn6HIlj6POic5H8G1RzlcKoIhoaoXCXFViawSuX0LyhnSJrCLblRfB3ISLjYrszyl3A/640?wx_fmt=png" width="538" referrerpolicy="no-referrer"></p> 
<p><span style="color:#4a94e7">5.总结</span></p> 
<p><span>现阶段的DevOps第三方权限管理已满足最基本的需求，实现了我们有这个能力配置第三方服务的权限，但也只局限于各个服务组件分离式的RBAC权限控制，所以说DevOps第三方权限管理仍有进步的空间，比如说在配置DevOps的角色权限时自动映射第三方服务的角色权限，这样当为DevOps用户授予角色时，便同步的配好了该用户在第三方服务中的角色信息，这样操作起来对用户更加友好。</span></p> 
<p><span style="color:#888888">参考资料：</span></p> 
<p><span style="color:#888888">https://baike.baidu.com/item/基于角色的访问控制</span></p> 
<p><span style="color:#888888">https://www.jianshu.com/p/ce0944b4a903?utm_source=oschina-app</span></p> 
<p><span style="color:#888888">https://www.cnblogs.com/seawaving/archive/2011/07/08/2100628.html</span></p> 
<p> </p> 
<p style="color:#333333; text-align:justify"><img align="left" height="171" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJXMGicMVPmm7OYbJc9bZ9jkw2VJXwnqCeBLjO1faVkOZlic7OljBLQgowWapHL3IQpxY6ticZtHkFNyA/640?wx_fmt=jpeg" width="123" referrerpolicy="no-referrer"><strong><span>关于作者</span></strong><span>：</span><span>欣宇，普元Java开发工程师，擅长Java、MySQL、Jenkins等；</span><span>参与DevOps的5.2-5.5版本的研发工作，参与九江银行的DevOps部署实施，参与碧桂园DevOps定制开发等。</span></p> 
<p style="color:#333333; text-align:justify"> </p> 
<p style="color:#333333; text-align:justify"> </p> 
<p style="color:#333333; text-align:justify"><img align="left" height="123" src="https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJXoqDSEoBJfiaUqSiawpnWXuFicqEU053j5nXuhfO18icrmn5PibfibibR8VxqaryqVickjDTyjBbMXrHgoQg/640?wx_fmt=jpeg" width="123" referrerpolicy="no-referrer"><strong><span>关于EAWorld</span></strong><span>：微服务，DevOps，数据治理，移动架构原创技术分享。<strong>长按二维码关注！</strong></span></p>
                                        </div>
                                      
</div>
            