
---
title: 'Fhs 快速开发平台 V3 版本发布，拥抱 vue，拥抱微服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/fhs-opensource/fhs-framework/raw/v3.x/222.jpg'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 09:57:00 GMT
thumbnail: 'https://gitee.com/fhs-opensource/fhs-framework/raw/v3.x/222.jpg'
---

<div>   
<div class="content">
                                                                                            <p><strong>1 FHS V3介绍</strong></p> 
<p><strong>   </strong>优秀的国内快速开发平台非常多，FHS V2发布后我们单位内部也做了一番讨论，要不要坚持用自己的轮子，最终决定还是要做。一番讨论后，我们确定了以下几点目标：</p> 
<ul> 
 <li>  全面拥抱vue,但是前端技术栈不求最新，但求最快。</li> 
 <li>  前端简单的页面使用JSON驱动，简单的CRUD功能代码就算是后端也能开发和维护</li> 
 <li>  全面拥抱微服务，但是不能因为SpringCloud的引入带来很大的学习成本(我们的项目有一些新手和实习生在干)</li> 
 <li>  提供AllInOne模式，本地开发实现只启动一个SpringBoot 应用即可完成开发调试，test prod环境又可以支持微服务模式部署(俺们单位还有部分机器是E3 1230V2+8G 内存)</li> 
 <li>  把部分组件提出来作为单独的开源项目发布，因为我们接的很多项目甲方要求使用他们的平台，我们可以引入几个组件但是不能换平台</li> 
 <li>  提供高级查询API，简单的单表查询不要让程序员手动写一行代码。</li> 
 <li>  提供基础的组织，用户，角色，菜单，字典，日志，前后端代码生成器</li> 
 <li>  在不增加学习成本的情况下，尽可能使用国产开源组件</li> 
</ul> 
<p><strong>   <img alt src="https://gitee.com/fhs-opensource/fhs-framework/raw/v3.x/222.jpg" referrerpolicy="no-referrer"></strong></p> 
<p><strong>2 FHS V3差异化</strong></p> 
<ul> 
 <li><strong>   翻译组件</strong> </li> 
</ul> 
<p>       <img alt height="181" src="https://oscimg.oschina.net/oscnet/up-821f1095527e02eb32c796a301881ac16e8.jpg" width="435" referrerpolicy="no-referrer"></p> 
<p>        字典码 sex  0 需要翻译成男 给前端，userid 1 需要翻译成张三给前端，使用翻译组件，配合Mybatis Plus，无需自己写SQL加一个注解即可实现。</p> 
<p>        翻译组件支持一个项目多个数据源，以及跨微服务进行翻译，还支持传统的枚举翻译。</p> 
<p>        此组件已经单独开源：https://gitee.com/fhs-opensource/easy_trans</p> 
<ul> 
 <li><strong> 简化远程调用</strong></li> 
</ul> 
<p>        Feign 做远程调用需要首先写一个service方法，然后用controller把service方法包一下，接着写一个feign接口，最后使用，而且对SpringCloud依赖性比较强，无法实现我们的All In One目标，我们希望把这个过程简化掉，于是EasyCloud模块出现了，只需要在service层加个注解就可以把普通的service方法暴漏出去给别人调用。</p> 
<pre><code class="language-java">@CloudApi(serviceName="producer")//producer 是服务提供者的服务名称
public interface UserService &#123;

    @CloudMethod  //加此注解意思是此方法提供给其他微服务调用
    List<UserDto> listByIds(String[] ids);
&#125;</code></pre> 
<p>   我要使用的时候只需要依赖User微服务的接口和pojo，然后进行注入即可。</p> 
<pre><code class="language-java"> @Autowired
 private UserService userService;</code></pre> 
<p>     通过EasyCloud，我们的开发者只需要多记2个注解即可，没有额外学习成本，本组件已经单独抽离开源：https://gitee.com/fhs-opensource/easy_cloud</p> 
<ul> 
 <li><strong> JSON驱动VUE插件集-PAGEX</strong></li> 
</ul> 
<p>     常年逛开源中国的开发者应该对avue和amis比较熟悉，他们的star数量就能看出越来越多的前端开发者已经接受了JSON驱动，我们对组件的理解是：高度抽象，搭配后台API设计规范，开发者通过JSON告诉组件，我需要一个下拉框/多选框/Other，你的数据绑定到表单对象的哪个属性上，你这个组件的数据源URL是什么，你这个组件数据校验规则是什么于是我们写一个下拉tree是如下代码：</p> 
<pre><code class="language-json">&#123;
    type: "treeSelect",
    name: "organizationId",
    label: "部门",
    rule: "required",
    query: &#123;&#125;,
    api: '/basic/ms/sysOrganization/tree',
    selectOn: (node) => &#123;
        this.changeRoleSelect(node.id);
    &#125;
&#125;</code></pre> 
<p>    又比如列表的过滤条件，我只需要告诉组件，我需要input，他的title是分组编码，对应字段是code，我需要模糊匹配。</p> 
<pre><code class="language-json">filters: [
    &#123;label: '分组名称:', name: 'groupName', placeholder: "分组名称", type: 'text', operation: 'like'&#125;,
    &#123;label: '分组编码:', name: 'groupCode', placeholder: "分组编码", type: 'text', operation: '='&#125;
  ]</code></pre> 
<p>    配合高级查询API规范，需求变动加过滤字段，更改数据过滤操作符前端自己就搞了。当然我们也考虑了很多扩展，这里就不示例了。</p> 
<p>    一个JSON驱动的CRUD 的代码demo。 https://gitee.com/fhs-opensource/fhs-framework/blob/v3.x/vue_ui/src/views/system/dict/index.vue</p> 
<ul> 
 <li><strong> AllInOne 模式</strong></li> 
</ul> 
<p>    all in one的好处是省内存，调试方便，在新建微服务的时候需要注意业务代码和springboot启动类分离开，比如我有用户中心，订单2个微服务，那么使用all in one需要user,userApp,order,orderApp,allinoneApp 这么几个子模块，其中spingboot相关依赖和配置放到userApp和orderApp上，业务代码和springcloud 相关类解耦即可。</p> 
<ul> 
 <li><strong> 高级查询API</strong></li> 
</ul> 
<p>      高级查询API很多项目已经有了，配合前端PAGEX的CRUD组件，可以更简单灵活的构造列表查询参数。</p> 
<pre><code class="language-json"> &#123;
"groupRelation": "AND",
"pagerInfo": &#123;
"page": 1,  //第几页，从1开始
"pageSize":10//每页多少条
&#125;,
"params": &#123;&#125;,//扩展参数，具体要和后端约定
"querys": [
&#123;
"group": "main",//分组
"operation": "=",//操作符
"property": "userName",//Java属性名
"relation": "AND",//是and 还是or
"value": "wanglei" // 属性username=wanglei的查询出来
&#125;
],
"sorter": [
&#123;
"direction": "ASC",//ASC 从小到大排序，DESC 从大到小排序
"property": "createTime"//排序的字段名
&#125;
]
&#125;</code></pre> 
<p><strong>4 体验地址</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=http%3A%2F%2F82.157.62.164%2Flogin">http://82.157.62.164/login</a><span> </span>admin 123456</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>5 预览图</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://gitee.com/fhs-opensource/fhs-framework/raw/v3.x/fhs.jpg" referrerpolicy="no-referrer"></p> 
<p><strong>5 用到的国产组件集</strong></p> 
<ul> 
 <li>Mybatis Plus</li> 
 <li>Sa-Token</li> 
 <li><span style="background-color:#ffffff; color:#40485b">Validate-Springboot-Starter</span></li> 
 <li> <p>SpringCloud Alibaba</p> </li> 
 <li> <p>ip2region</p> </li> 
 <li> <p>
   <!-- for WeLink copy-->knife4j</p> </li> 
</ul>
                                        </div>
                                      
</div>
            