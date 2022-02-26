
---
title: '🚀 Erupt 1.10.2 发布，零前端代码，仅需一个类文件，快速开发 Admin 管理后台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 15:40:00 GMT
thumbnail: 'https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#2ecc71">Erupt  通用后台管理框架</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Erupt 是一个低代码 <strong>全栈类</strong> 框架，它使用 <strong>Java 注解</strong> 动态构建页面，及增、删、改、查、权限控制等功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">零前端代码、零 CURD、自动建表，仅需 <strong>一个类文件</strong> + <strong>简洁的注解配置</strong>，快速开发企业级 Admin 管理后台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">提供企业级中后台管理系统的全栈解决方案，大幅压缩研发周期，专注核心业务</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#1abc9c">本次更新内容</span> </h1> 
<div> 
 <h1 style="margin-left:0; margin-right:0"><span>1.10.2 (2022年02月24日)</span></h1> 
 <p style="margin-left:0; margin-right:0"><strong><span>Spring boot版本：2.6.0</span></strong></p> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>🐞 修复erupt-magic-api数据源管理权限不足的 BUG</span></li> 
  <li><span>🐞 修复自定义按钮组件执行顺序错乱的 BUG</span> </li> 
  <li><span>🌟 </span><span>优化使用细节，如用户表为空则会自动删除初始化标识文件（.erupt）重新初始化</span></li> 
  <li><span>🌟 菜单权限校验不区分大小写</span></li> 
  <li><span>🌟 erupt-bi 图表查询依赖必填查询项</span> </li> 
 </ul> 
</div> 
<div style="text-align:left"> 
 <h2 style="margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#2ecc71">项目官网</span>：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz" target="_blank">www.erupt.xyz</a></strong></h2> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Erupt</span></span></span></span></span></span></span></span></span></span>(
       name = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"简单的例子"</span></span></span></span></span></span></span></span></span></span>,
       power = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Power</span></span></span></span></span></span></span></span></span></span>(importable = true, export = true)
)
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Table</span></span></span></span></span></span></span></span></span></span>(name = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"t_simple"</span></span></span></span></span></span></span></span></span></span>)   <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">//数据库表名</span></span></span></span></span></span></span></span></span></span>
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Entity</span></span></span></span></span></span></span></span></span></span>
public class Simple extends BaseModel &#123;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span></span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"文本"</span></span></span></span></span></span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"文本"</span></span></span></span></span></span></span></span></span></span>, notNull = true, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span></span></span></span></span></span>)
    )
    private String input;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span></span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"数值"</span></span></span></span></span></span></span></span></span></span>, sortable = true),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"数值"</span></span></span></span></span></span></span></span></span></span>, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span></span></span></span></span></span>)
    )
    private Float number;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span></span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"布尔"</span></span></span></span></span></span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"布尔"</span></span></span></span></span></span></span></span></span></span>, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span></span></span></span></span></span>)
    )
    private Boolean bool;


    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span></span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"时间"</span></span></span></span></span></span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"时间"</span></span></span></span></span></span></span></span></span></span>, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span></span></span></span></span></span>(vague = true))
    )
    private Date date;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span></span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"滑动条"</span></span></span></span></span></span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"滑动条"</span></span></span></span></span></span></span></span></span></span>, type = EditType.SLIDER, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span></span></span></span></span></span>,
                    sliderType = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@SliderType</span></span></span></span></span></span></span></span></span></span>(max = <span><span><span><span><span><span><span><span>90</span></span></span></span></span></span></span></span>, markPoints = &#123;<span><span><span><span><span><span><span><span>0</span></span></span></span></span></span></span></span>, <span><span><span><span><span><span><span><span>30</span></span></span></span></span></span></span></span>, <span><span><span><span><span><span><span><span>60</span></span></span></span></span></span></span></span>, <span><span><span><span><span><span><span><span>90</span></span></span></span></span></span></span></span>&#125;, dots = true))
    )
    private Integer slide;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span></span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span></span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"下拉选择"</span></span></span></span></span></span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span></span></span></span></span></span>(
                    search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span></span></span></span></span></span>,
                    title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"下拉选择"</span></span></span></span></span></span></span></span></span></span>, type = EditType.CHOICE,
                    choiceType = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@ChoiceType</span></span></span></span></span></span></span></span></span></span>(fetchHandler = SqlChoiceFetchHandler.class,
                            fetchHandlerParams = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"select id,name from e_upms_menu"</span></span></span></span></span></span></span></span></span></span>
                    )
            )
    )
    private Long choice;

&#125;</code></pre> 
 <h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#2ecc71">特性 | Features</span></h2> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li> <p style="margin-left:0; margin-right:0"><strong>自动建表</strong>：表结构自动生成，无需手动建表</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>易于上手</strong>：会简单的 <strong>Spring Boot</strong> 基础知识即可</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>使用简单</strong>：仅需了解 <strong>@Erupt</strong> 与 <strong>@EruptField</strong> 两个注解即可上手开发</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>代码简洁</strong>：仅需一个 <code>.java</code> 文件, template、controller、service、dao 都不需要创建</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>功能强大</strong>：动态条件处理，逻辑删除，LDAP，自定义登录逻辑，RedisSession，操作日志等</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>多数据源</strong>：支持：MySQL、Oracle、SQL Server、<strong>PostgreSQL</strong>、H2，甚至支持 <strong>MongoDB</strong></p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>高扩展性</strong>：支持自定义数据源实现、自定义登录逻辑、动态权限管理、生命周期函数、<strong>自定义 OSS</strong></p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>大量组件</strong>：滑动输入、时间选择、<strong>一对多</strong>、图片上传、代码编辑、自动完成、树、<strong>多对多</strong>、地图等23类组件</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>丰富展示</strong>：普通文本、<strong>二维码</strong>、链接、图片、HTML、代码段、iframe、swf等</p> </li> 
 </ul> 
 <hr> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li> <p style="margin-left:0; margin-right:0"><strong>低侵入性</strong>：几乎所有功能都围绕注解而展开，不影响Spring Boot其他功能或三方库库的使用</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>前后端分离</strong>：后端与前端可分开部署</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>响应式布局</strong>：支持PC端手机端等各种规格的设备中使用</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>自定义页面</strong>：支持自定义页面，自定义弹出层，且支持：原生H5 / Freemarker / Thymeleaf等方式渲染</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>前端零代码</strong>：前端布局自动构建，一行前端代码都不用写</p> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>无需二次开发</strong>：仅需引用 jar 包即可 ！</p> </li> 
 </ul> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#6a737d">完全不需要了解 </span><strong><span style="color:#6a737d">Angular / React / Vue / Jquery</span></strong></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#6a737d">而且不需要了解 </span><strong><span style="color:#6a737d">JavaScript / HTML / CSS</span></strong></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#6a737d">甚至不需要了解 </span><strong><span style="color:#6a737d">Spring MVC / Mybatis / SQL</span></strong></p> 
 </blockquote> 
 <h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#2ecc71">在线体验 | Demo</span></h2> 
 <h4 style="margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz%2Fdemo" target="_blank">https://www.erupt.xyz/demo</a><br> 账号密码：<code>guest / guest</code></h4> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>支持主流 4 款现代浏览器，以及 Internet Explorer 11+，可直接运行在 Electron 等基于 Web 标准的环境上</strong></p> 
 <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#2ecc71">演示截图 | Screenshot ⛰</span></h1> 
 <div style="text-align:justify">
  <img alt="使用 Erupt 零前端代码，仅需一个类文件，开发 Admin 管理后台" src="https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:justify">
  <img alt="使用 Erupt 零前端代码，仅需一个类文件，开发 Admin 管理后台" src="https://p3-tt.byteimg.com/origin/pgc-image/fa801c93ff44429390962958e431d0cb?from=pc" referrerpolicy="no-referrer">
 </div> 
</div>
                                        </div>
                                      
</div>
            