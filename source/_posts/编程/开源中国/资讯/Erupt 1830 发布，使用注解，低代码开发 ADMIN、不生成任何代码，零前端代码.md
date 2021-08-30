
---
title: 'Erupt 1.8.30 发布，使用注解，低代码开发 ADMIN、不生成任何代码，零前端代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc'
author: 开源中国
comments: false
date: Sun, 29 Aug 2021 23:22:00 GMT
thumbnail: 'https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc'
---

<div>   
<div class="content">
                                                                                            <h1 style="text-align:left"><span style="color:#2ecc71">Erupt  通用后台管理框架</span></h1> 
<p style="text-align:left">Erupt 是一个低代码 <strong>全栈类</strong> 框架，它使用 <strong>Java 注解</strong> 动态生成页面以及增、删、改、查、权限控制等功能。</p> 
<p style="text-align:left">零前端代码、零 CURD、自动建表，仅需 <strong>一个类文件</strong> + <strong>简洁的注解配置</strong>，快速开发企业级 Admin 管理后台。</p> 
<p style="text-align:left">提供企业级中后台管理系统的全栈解决方案，大幅压缩研发周期，专注核心业务</p> 
<h1 style="text-align:left"><span style="color:#1abc9c">本次更新内容</span></h1> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <ul> 
    <li>🐞 修复表格文字显示溢出bug</li> 
    <li>🌟 增加上下文对象获取工具类 EruptContextService </li> 
    <li>🌟 自定义按钮 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Ferupts%2Ferupt%2Fgaing7%23kdCWH" target="_blank">OperationHandler</a> 移除 afterJS 方法，exec方法返回值作为前端执行的 js</li> 
    <li>🌟 数据表格分页支持300、500行数据显示 </li> 
    <li>🌟 增加树展开层级配置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Ferupts%2Ferupt%2Frz3beg" target="_blank">expandLevel</a>，可以支持十万级树节点快速计算与渲染</li> 
    <li>🌟 TAB_TREE 组件支持 filter 配置 </li> 
    <li>🌟 CHECKBOX 组件支持 filter 配置</li> 
    <li>🌟 角色列表支持根据已登录用户身份自动过滤  </li> 
    <li>🌟 角色菜单可根据已登录用户身份自动过滤</li> 
    <li>🌟 管理员用户可删除登录日志与操作日志 </li> 
    <li>🌟 非管理员用户管理角色时可根据已有角色菜单向下分配，无权分配没有权限的菜单</li> 
    <li>🌟 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Ferupts%2Ferupt%2Ffamk6i" target="_blank">AttachmentProxy</a> → upload 方法支持自定义存储路径 </li> 
    <li>🌟 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Ferupts%2Ferupt%2Fnicqg3" target="_blank">DataProxy</a> → before方法移除无实际作用的Class<?>参数，增加List<Condition>参数，用于获取和处理前端查询条件</li> 
   </ul> 
  </div> 
 </div> 
</div> 
<h2 style="text-align:left"><strong><span style="color:#2ecc71">项目官网</span>：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz" target="_blank">www.erupt.xyz</a></strong></h2> 
<pre style="text-align:left"><code class="language-java"><span style="color:#032f62">@Erupt</span>(
       name = <span style="color:#032f62">"简单的例子"</span>,
       power = <span style="color:#032f62">@Power</span>(importable = true, export = true)
)
<span style="color:#032f62">@Table</span>(name = <span style="color:#032f62">"t_simple"</span>)   <span style="color:#6a737d">//数据库表名</span>
<span style="color:#032f62">@Entity</span>
public class Simple extends BaseModel &#123;

    <span style="color:#032f62">@EruptField</span>(
            views = <span style="color:#032f62">@View</span>(title = <span style="color:#032f62">"文本"</span>),
            edit = <span style="color:#032f62">@Edit</span>(title = <span style="color:#032f62">"文本"</span>, notNull = true, search = <span style="color:#032f62">@Search</span>)
    )
    private String input;

    <span style="color:#032f62">@EruptField</span>(
            views = <span style="color:#032f62">@View</span>(title = <span style="color:#032f62">"数值"</span>, sortable = true),
            edit = <span style="color:#032f62">@Edit</span>(title = <span style="color:#032f62">"数值"</span>, search = <span style="color:#032f62">@Search</span>)
    )
    private Float number;

    <span style="color:#032f62">@EruptField</span>(
            views = <span style="color:#032f62">@View</span>(title = <span style="color:#032f62">"布尔"</span>),
            edit = <span style="color:#032f62">@Edit</span>(title = <span style="color:#032f62">"布尔"</span>, search = <span style="color:#032f62">@Search</span>)
    )
    private Boolean bool;


    <span style="color:#032f62">@EruptField</span>(
            views = <span style="color:#032f62">@View</span>(title = <span style="color:#032f62">"时间"</span>),
            edit = <span style="color:#032f62">@Edit</span>(title = <span style="color:#032f62">"时间"</span>, search = <span style="color:#032f62">@Search</span>(vague = true))
    )
    private Date date;

    <span style="color:#032f62">@EruptField</span>(
            views = <span style="color:#032f62">@View</span>(title = <span style="color:#032f62">"滑动条"</span>),
            edit = <span style="color:#032f62">@Edit</span>(title = <span style="color:#032f62">"滑动条"</span>, type = EditType.SLIDER, search = <span style="color:#032f62">@Search</span>,
                    sliderType = <span style="color:#032f62">@SliderType</span>(max = 90, markPoints = &#123;0, 30, 60, 90&#125;, dots = true))
    )
    private Integer slide;

    <span style="color:#032f62">@EruptField</span>(
            views = <span style="color:#032f62">@View</span>(title = <span style="color:#032f62">"下拉选择"</span>),
            edit = <span style="color:#032f62">@Edit</span>(
                    search = <span style="color:#032f62">@Search</span>,
                    title = <span style="color:#032f62">"下拉选择"</span>, type = EditType.CHOICE,
                    choiceType = <span style="color:#032f62">@ChoiceType</span>(fetchHandler = SqlChoiceFetchHandler.class,
                            fetchHandlerParams = <span style="color:#032f62">"select id,name from e_upms_menu"</span>
                    )
            )
    )
    private Long choice;

&#125;</code></pre> 
<h2 style="text-align:left"><span style="color:#2ecc71">特性 | Features</span></h2> 
<ul> 
 <li> <p><strong>自动建表</strong>：表结构自动生成，无需手动建表</p> </li> 
 <li> <p><strong>易于上手</strong>：会简单的 <strong>Spring Boot</strong> 基础知识即可</p> </li> 
 <li> <p><strong>使用简单</strong>：仅需了解 <strong>@Erupt</strong> 与 <strong>@EruptField</strong> 两个注解即可上手开发</p> </li> 
 <li> <p><strong>代码简洁</strong>：仅需一个 <code>.java</code> 文件, template、controller、service、dao 都不需要创建</p> </li> 
 <li> <p><strong>功能强大</strong>：动态条件处理，逻辑删除，LDAP，自定义登录逻辑，RedisSession，操作日志等</p> </li> 
 <li> <p><strong>多数据源</strong>：支持：MySQL、Oracle、SQL Server、<strong>PostgreSQL</strong>、H2，甚至支持 <strong>MongoDB</strong></p> </li> 
 <li> <p><strong>高扩展性</strong>：支持自定义数据源实现、自定义登录逻辑、动态权限管理、生命周期函数、<strong>自定义 OSS</strong></p> </li> 
 <li> <p><strong>大量组件</strong>：滑动输入、时间选择、<strong>一对多</strong>、图片上传、代码编辑、自动完成、树、<strong>多对多</strong>、地图等23类组件</p> </li> 
 <li> <p><strong>丰富展示</strong>：普通文本、<strong>二维码</strong>、链接、图片、HTML、代码段、iframe、swf等</p> </li> 
</ul> 
<hr> 
<ul> 
 <li> <p><strong>低侵入性</strong>：几乎所有功能都围绕注解而展开，不影响Spring Boot其他功能或三方库库的使用</p> </li> 
 <li> <p><strong>前后端分离</strong>：后端与前端可分开部署</p> </li> 
 <li> <p><strong>响应式布局</strong>：支持PC端手机端等各种规格的设备中使用</p> </li> 
 <li> <p><strong>自定义页面</strong>：支持自定义页面，自定义弹出层，且支持：原生H5 / Freemarker / Thymeleaf等方式渲染</p> </li> 
 <li> <p><strong>前端零代码</strong>：前端布局自动构建，一行前端代码都不用写</p> </li> 
 <li> <p><strong>无需二次开发</strong>：仅需引用 jar 包即可 ！</p> </li> 
</ul> 
<blockquote> 
 <p style="text-align:left"><span style="color:#6a737d">完全不需要了解 </span><strong><span style="color:#6a737d">Angular / React / Vue / Jquery</span></strong></p> 
 <p style="text-align:left"><span style="color:#6a737d">而且不需要了解 </span><strong><span style="color:#6a737d">JavaScript / HTML / CSS</span></strong></p> 
 <p style="text-align:left"><span style="color:#6a737d">甚至不需要了解 </span><strong><span style="color:#6a737d">Spring MVC / Mybatis / SQL</span></strong></p> 
</blockquote> 
<h2 style="text-align:left"> </h2> 
<h2 style="text-align:left"><span style="color:#2ecc71">在线体验 | Demo</span></h2> 
<h4 style="text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz%2Fdemo" target="_blank">https://www.erupt.xyz/demo</a><br> 账号密码：<code>guest / guest</code></h4> 
<p style="text-align:left"><strong>支持主流 4 款现代浏览器，以及 Internet Explorer 11+，可直接运行在 Electron 等基于 Web 标准的环境上</strong></p> 
<p style="text-align:left"> </p> 
<h1 style="text-align:left"><span style="color:#2ecc71">演示截图 | Screenshot ⛰</span></h1> 
<div style="text-align:justify">
 <img alt="使用 Erupt 零前端代码，仅需一个类文件，开发 Admin 管理后台" src="https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc" referrerpolicy="no-referrer"> 
 <p> </p> 
</div> 
<div style="text-align:justify">
 <img alt="使用 Erupt 零前端代码，仅需一个类文件，开发 Admin 管理后台" src="https://p3-tt.byteimg.com/origin/pgc-image/fa801c93ff44429390962958e431d0cb?from=pc" referrerpolicy="no-referrer">
</div>
                                        </div>
                                      
</div>
            