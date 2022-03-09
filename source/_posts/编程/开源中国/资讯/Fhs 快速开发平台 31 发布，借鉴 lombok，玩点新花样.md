
---
title: 'Fhs 快速开发平台 3.1 发布，借鉴 lombok，玩点新花样'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-821f1095527e02eb32c796a301881ac16e8.jpg'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 10:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-821f1095527e02eb32c796a301881ac16e8.jpg'
---

<div>   
<div class="content">
                                                                                            <h1>1 本次更新</h1> 
<p><strong>1.1 前言</strong></p> 
<p><strong>   </strong>相信Myabtis Plus的wrapper大家已经很熟悉了，尤其是
 <!-- for WeLink copy-->LambdaQueryWrapper比JPA的
 <!-- for WeLink copy-->Specification好用了不知道多少倍，但是LambdaQueryWrapper写起来还不够行云流水，我一直在想能不能更简化它，于是出现了本次fhs版本更新带来的PO Wrapper增强器功能，他类似lombok，不需要写很多代码就可以对PO进行wrapper化增强配合ActiveRecord简直不要太爽。</p> 
<p><strong>1.2 上DEMO</strong></p> 
<p><strong> </strong>首先我们定义一个PO，并且使用
 <!-- for WeLink copy-->@Wrapperable注解标记要增强。</p> 
<pre><code class="language-java">@Data
@Wrapperable
@TableName("user")
public class User &#123;

    @TableId("user_id")
    private Integer userId;

    @TableField("name")
    private String name;

    @TableField("age")
    private Integer age;

    @TableField("sex")
    private String sex;


&#125;
</code></pre> 
<p> 然后使用activeRecord愉快的对User表进行CRUD操作。</p> 
<pre><code class="language-java">@RestController
public class UserController &#123;

    @GetMapping("/one")
    public User one() &#123;
        return User.newOBJ().nameLike("小").one();
    &#125;

    @GetMapping("/oneField")
    public User oneField() &#123;
        return User.newOBJ().nameLike("小").one(new String[]&#123;User.USERID, User.NAME&#125;);
    &#125;

    @GetMapping("/list")
    public List<User> list() &#123;
        return User.newOBJ().ageBetween(10, 25).list();
    &#125;

    @GetMapping("/listField")
    public List<User> listField() &#123;
        return User.newOBJ().ageBetween(10, 20).list(new String[]&#123;User.USERID, User.NAME&#125;);
    &#125;

    @GetMapping("/delete")
    public int delete() &#123;
        return User.newOBJ().ageBetween(50, 80).delete();
    &#125;

    @GetMapping("/count")
    public Long count() &#123;
        return  User.newOBJ().ageBetween(10,26).count();
    &#125;

   
    @GetMapping("/update")
    public int update() &#123;
        User user = User.newOBJ();
        user.setAge(19);
        return user.nameEQ("小明").update();
    &#125;
&#125;</code></pre> 
<p>支持的方法(注意XX代表属性名，如果有多个属性的话，则会生成多个方法)</p> 
<table border="1" cellpadding="1" cellspacing="1" style="width:800px"> 
 <tbody> 
  <tr> 
   <td>方法名称</td> 
   <td>方法用途</td> 
  </tr> 
  <tr> 
   <td>
    <!-- for WeLink copy-->bean2Wrapper</td> 
   <td>把po转换为一个wrapper</td> 
  </tr> 
  <tr> 
   <td>list        </td> 
   <td>返回集合            </td> 
  </tr> 
  <tr> 
   <td>
    <!-- for WeLink copy-->list(String[] fields)</td> 
   <td>返回集合 并且指定查询字段</td> 
  </tr> 
  <tr> 
   <td>one            </td> 
   <td>返回单个，如果条件能查询出多个返回第一个</td> 
  </tr> 
  <tr> 
   <td>one (String[] fields)</td> 
   <td>返回单个，如果条件能查询出多个返回第一个，并且指定查询字段</td> 
  </tr> 
  <tr> 
   <td>count    </td> 
   <td>总数</td> 
  </tr> 
  <tr> 
   <td>delete</td> 
   <td>删除</td> 
  </tr> 
  <tr> 
   <td>update</td> 
   <td>更新</td> 
  </tr> 
  <tr> 
   <td>newOBJ    </td> 
   <td>调用无参构造方法返回一个对象</td> 
  </tr> 
  <tr> 
   <td>xxEQ    </td> 
   <td>=</td> 
  </tr> 
  <tr> 
   <td>xxNE    </td> 
   <td>!=</td> 
  </tr> 
  <tr> 
   <td> <p>xxLike</p> </td> 
   <td>like</td> 
  </tr> 
  <tr> 
   <td>xxLikeRight    </td> 
   <td>like  xx%</td> 
  </tr> 
  <tr> 
   <td>xxLikeLeft</td> 
   <td>like  %xx</td> 
  </tr> 
  <tr> 
   <td>xxNotLike</td> 
   <td>not like</td> 
  </tr> 
  <tr> 
   <td>xxIn    </td> 
   <td>in</td> 
  </tr> 
  <tr> 
   <td>xxNotIn</td> 
   <td>not in</td> 
  </tr> 
  <tr> 
   <td>xxBetween</td> 
   <td>between</td> 
  </tr> 
  <tr> 
   <td>xxNotBetween    </td> 
   <td>not betwen</td> 
  </tr> 
  <tr> 
   <td>xxGE</td> 
   <td>>=</td> 
  </tr> 
  <tr> 
   <td>xxGT</td> 
   <td>></td> 
  </tr> 
  <tr> 
   <td>xxLT</td> 
   <td><</td> 
  </tr> 
  <tr> 
   <td>xxLE    </td> 
   <td><=</td> 
  </tr> 
  <tr> 
   <td>xxIsNull</td> 
   <td>is null</td> 
  </tr> 
  <tr> 
   <td>xxNotNull</td> 
   <td>not null</td> 
  </tr> 
  <tr> 
   <td>xxOrderByAsc    </td> 
   <td>order by xx asc</td> 
  </tr> 
  <tr> 
   <td>xxOrderByDesc    </td> 
   <td>order by xx desc</td> 
  </tr> 
 </tbody> 
</table> 
<p>除了生成方法外还会生成常量，方便引用属性名。</p> 
<p>比如属性中有一个name(小写) 会自动生成一个public static final String NAME="name".</p> 
<p><strong>1.3 所用技术简介</strong></p> 
<ul> 
 <li>Java APT+AST 在编译期对PO的class进行修改，添加我们需要的方法</li> 
 <li>idea plugin  生成的class增加了方法和常量后，idea并不能索引到，所以需要开发插件告诉idea我们其实有这些方法，idea就不会报错并且可以自动提示了。</li> 
 <li>
  <!-- for WeLink copy-->QueryWrapper 当你执行了nameLike后其实框架是自动调用了
  <!-- for WeLink copy-->QueryWrapper.like("name","xx")，所以底层还是
  <!-- for WeLink copy-->QueryWrapper</li> 
</ul> 
<p><strong>1.4 觉得上述特性很好用，但是又不想用我的fhs framework怎么办？</strong></p> 
<p>
 <!-- for WeLink copy--> 我们对此模块进行了单独抽离，https://gitee.com/fhs-opensource/fhs_mp maven中央仓库最新是1.0.2版本，</p> 
<pre><code class="language-xml"> <dependency>
            <groupId>com.fhs-opensource</groupId>
            <artifactId>mp_ext</artifactId>
            <version>1.0.2</version>
 </dependency></code></pre> 
<p> 为了方便大家折腾自己的插件，我们也对idea进行了开源：</p> 
<p>https://gitee.com/fhs-opensource/myabtis_plus_ext_idea_plugin</p> 
<p> 和mp作者聊过，本插件孵化好后可能会合并到mp官方 作为mp4新特性发布。</p> 
<p> </p> 
<h1>2 fhs framework相关</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.1 FHS V3介绍</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>   </strong>优秀的国内快速开发平台非常多，FHS V2发布后我们单位内部也做了一番讨论，要不要坚持用自己的轮子，最终决定还是要做。一番讨论后，我们确定了以下几点目标：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>  全面拥抱vue,但是前端技术栈不求最新，但求最快。</li> 
 <li>  前端简单的页面使用JSON驱动，简单的CRUD功能代码就算是后端也能开发和维护</li> 
 <li>  全面拥抱微服务，但是不能因为SpringCloud的引入带来很大的学习成本(我们的项目有一些新手和实习生在干)</li> 
 <li>  提供AllInOne模式，本地开发实现只启动一个SpringBoot 应用即可完成开发调试，test prod环境又可以支持微服务模式部署(俺们单位还有部分机器是E3 1230V2+8G 内存)</li> 
 <li>  把部分组件提出来作为单独的开源项目发布，因为我们接的很多项目甲方要求使用他们的平台，我们可以引入几个组件但是不能换平台</li> 
 <li>  提供高级查询API，简单的单表查询不要让程序员手动写一行代码。</li> 
 <li>  提供基础的组织，用户，角色，菜单，字典，日志，前后端代码生成器</li> 
 <li>  在不增加学习成本的情况下，尽可能使用国产开源组件</li> 
</ul> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2.2 FHS V3差异化</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>   翻译组件</strong> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">       <img alt height="181" src="https://oscimg.oschina.net/oscnet/up-821f1095527e02eb32c796a301881ac16e8.jpg" width="435" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">        字典码 sex  0 需要翻译成男 给前端，userid 1 需要翻译成张三给前端，使用翻译组件，配合Mybatis Plus，无需自己写SQL加一个注解即可实现。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">        翻译组件支持一个项目多个数据源，以及跨微服务进行翻译，还支持传统的枚举翻译。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">        此组件已经单独开源：https://gitee.com/fhs-opensource/easy_trans</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong> 简化远程调用</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">        Feign 做远程调用需要首先写一个service方法，然后用controller把service方法包一下，接着写一个feign接口，最后使用，而且对SpringCloud依赖性比较强，无法实现我们的All In One目标，我们希望把这个过程简化掉，于是EasyCloud模块出现了，只需要在service层加个注解就可以把普通的service方法暴漏出去给别人调用。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">@CloudApi</span>(serviceName=<span style="color:#032f62">"producer"</span>)<span style="color:#6a737d">//producer 是服务提供者的服务名称</span>
<span style="color:#d73a49">public</span> <span><span style="color:#d73a49">interface</span> <span style="color:#6f42c1">UserService</span> </span>&#123;

    <span style="color:#6a737d">@CloudMethod</span>  <span style="color:#6a737d">//加此注解意思是此方法提供给其他微服务调用</span>
    <span>List<UserDto> <span style="color:#6f42c1">listByIds</span><span>(String[] ids)</span></span>;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">   我要使用的时候只需要依赖User微服务的接口和pojo，然后进行注入即可。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"> <span style="color:#032f62">@Autowired</span>
 private UserService userService;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">     通过EasyCloud，我们的开发者只需要多记2个注解即可，没有额外学习成本，本组件已经单独抽离开源：https://gitee.com/fhs-opensource/easy_cloud</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong> JSON驱动VUE插件集-PAGEX</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">     常年逛开源中国的开发者应该对avue和amis比较熟悉，他们的star数量就能看出越来越多的前端开发者已经接受了JSON驱动，我们对组件的理解是：高度抽象，搭配后台API设计规范，开发者通过JSON告诉组件，我需要一个下拉框/多选框/Other，你的数据绑定到表单对象的哪个属性上，你这个组件的数据源URL是什么，你这个组件数据校验规则是什么于是我们写一个下拉tree是如下代码：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-json">&#123;
    type: <span style="color:#032f62">"treeSelect"</span>,
    name: <span style="color:#032f62">"organizationId"</span>,
    label: <span style="color:#032f62">"部门"</span>,
    rule: <span style="color:#032f62">"required"</span>,
    query: &#123;&#125;,
    api: <span style="color:#032f62">'/basic/ms/sysOrganization/tree'</span>,
    selectOn: <span><span>(node)</span> =></span> &#123;
        <span style="color:#d73a49">this</span>.changeRoleSelect(node.id);
    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    又比如列表的过滤条件，我只需要告诉组件，我需要input，他的title是分组编码，对应字段是code，我需要模糊匹配。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-json"><span style="color:#005cc5">filters</span>: [
    &#123;<span style="color:#005cc5">label</span>: <span style="color:#032f62">'分组名称:'</span>, <span style="color:#005cc5">name</span>: <span style="color:#032f62">'groupName'</span>, <span style="color:#005cc5">placeholder</span>: <span style="color:#032f62">"分组名称"</span>, <span style="color:#005cc5">type</span>: <span style="color:#032f62">'text'</span>, <span style="color:#005cc5">operation</span>: <span style="color:#032f62">'like'</span>&#125;,
    &#123;<span style="color:#005cc5">label</span>: <span style="color:#032f62">'分组编码:'</span>, <span style="color:#005cc5">name</span>: <span style="color:#032f62">'groupCode'</span>, <span style="color:#005cc5">placeholder</span>: <span style="color:#032f62">"分组编码"</span>, <span style="color:#005cc5">type</span>: <span style="color:#032f62">'text'</span>, <span style="color:#005cc5">operation</span>: <span style="color:#032f62">'='</span>&#125;
  ]</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    配合高级查询API规范，需求变动加过滤字段，更改数据过滤操作符前端自己就搞了。当然我们也考虑了很多扩展，这里就不示例了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    一个JSON驱动的CRUD 的代码demo。 https://gitee.com/fhs-opensource/fhs-framework/blob/v3.x/vue_ui/src/views/system/dict/index.vue</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong> AllInOne 模式</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    all in one的好处是省内存，调试方便，在新建微服务的时候需要注意业务代码和springboot启动类分离开，比如我有用户中心，订单2个微服务，那么使用all in one需要user,userApp,order,orderApp,allinoneApp 这么几个子模块，其中spingboot相关依赖和配置放到userApp和orderApp上，业务代码和springcloud 相关类解耦即可。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong> 高级查询API</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      高级查询API很多项目已经有了，配合前端PAGEX的CRUD组件，可以更简单灵活的构造列表查询参数。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-json"> &#123;
<span style="color:#6f42c1">"groupRelation"</span>: <span style="color:#032f62">"AND"</span>,
<span style="color:#6f42c1">"pagerInfo"</span>: &#123;
<span style="color:#6f42c1">"page"</span>: <span>1</span>,  <span style="color:#6a737d">//第几页，从1开始</span>
<span style="color:#6f42c1">"pageSize"</span>:<span>10</span><span style="color:#6a737d">//每页多少条</span>
&#125;,
<span style="color:#6f42c1">"params"</span>: &#123;&#125;,<span style="color:#6a737d">//扩展参数，具体要和后端约定</span>
<span style="color:#6f42c1">"querys"</span>: [
&#123;
<span style="color:#6f42c1">"group"</span>: <span style="color:#032f62">"main"</span>,<span style="color:#6a737d">//分组</span>
<span style="color:#6f42c1">"operation"</span>: <span style="color:#032f62">"="</span>,<span style="color:#6a737d">//操作符</span>
<span style="color:#6f42c1">"property"</span>: <span style="color:#032f62">"userName"</span>,<span style="color:#6a737d">//Java属性名</span>
<span style="color:#6f42c1">"relation"</span>: <span style="color:#032f62">"AND"</span>,<span style="color:#6a737d">//是and 还是or</span>
<span style="color:#6f42c1">"value"</span>: <span style="color:#032f62">"wanglei"</span> <span style="color:#6a737d">// 属性username=wanglei的查询出来</span>
&#125;
],
<span style="color:#6f42c1">"sorter"</span>: [
&#123;
<span style="color:#6f42c1">"direction"</span>: <span style="color:#032f62">"ASC"</span>,<span style="color:#6a737d">//ASC 从小到大排序，DESC 从大到小排序</span>
<span style="color:#6f42c1">"property"</span>: <span style="color:#032f62">"createTime"</span><span style="color:#6a737d">//排序的字段名</span>
&#125;
]
&#125;</code></pre> 
<ul> 
 <li style="text-align:left"><strong> Mybatis Plus+PO增强 简化查询条件构造</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">     为本次主要更新内容，这里不多说了</p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>4 体验地址</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=http%3A%2F%2F82.157.62.164%2Flogin">http://82.157.62.164/login</a><span> </span>admin 123456</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>5 预览图</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="863" src="https://gitee.com/fhs-opensource/fhs-framework/raw/v3.x/img/fhs.jpg" width="1918" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>5 用到的国产组件集</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Mybatis Plus</li> 
 <li>Sa-Token</li> 
 <li><span style="background-color:#ffffff; color:#40485b">Validate-Springboot-Starter</span></li> 
 <li> <p style="margin-left:0; margin-right:0">SpringCloud Alibaba</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">ip2region</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">knife4j</p> </li> 
</ul>
                                        </div>
                                      
</div>
            