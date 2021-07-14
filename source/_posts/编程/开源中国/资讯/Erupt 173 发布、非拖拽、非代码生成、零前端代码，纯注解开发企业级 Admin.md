
---
title: 'Erupt 1.7.3 发布、非拖拽、非代码生成、零前端代码，纯注解开发企业级 Admin'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 02:27:00 GMT
thumbnail: 'https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc'
---

<div>   
<div class="content">
                                                                    
                                                        <h1><span style="color:#2ecc71">Erupt  通用后台管理框架</span></h1> 
<p style="text-align:left">Erupt 是一个低代码 <strong>全栈类</strong> 框架，它使用 <strong>Java 注解</strong> 动态生成页面以及增、删、改、查、权限控制等功能。</p> 
<p style="text-align:left">零前端代码、零 CURD、自动建表，仅需 <strong>一个类文件</strong> + <strong>简洁的注解配置</strong>，快速开发企业级 Admin 管理后台。</p> 
<p style="text-align:left">提供企业级中后台管理系统的全栈解决方案，大幅压缩研发周期，专注核心业务</p> 
<h1><span style="color:#1abc9c">本次更新内容</span></h1> 
<div style="text-align:left"> 
 <div> 
  <ul> 
   <li>🐞 修复EruptUser对象与EruptRole对象修改时由于存在游离对象所产生的bug</li> 
   <li>🐞 修复树视图下 choice 组件数据不自动清空的 bug </li> 
   <li>🐞 修复oracle数据源 EruptOperateLog 表无法自动创建的bug</li> 
   <li>🐞 修复oracle数据源 EruptJobLog 表无法自动创建的bug  </li> 
   <li>🐞 修复获取当前用户信息后，数据转变为游离状态的bug</li> 
   <li><span style="color:#314659">🌟 </span> 关闭一对多弹出层点击框外就自动关闭能力</li> 
   <li><span style="color:#314659">🌟 </span> 优化 erupt-monitor 手机端布局</li> 
   <li><span style="color:#314659">🌟 </span> 优化 tab_table 组件滑动条出现的最大宽度</li> 
   <li><span style="color:#314659">🌟 </span>限制 table 表格最大宽度</li> 
   <li><span style="color:#314659">🌟 </span>优化审计数据用户关联对象，EruptUser对象替换为数据结构更简单的EruptUserVo对象 </li> 
   <li><span style="color:#314659">🌟</span> magic-api升级至1.3.3</li> 
   <li><span style="color:#314659">🌟 view注解附件与图片</span>支持全路径网络资源的展示</li> 
   <li><span style="color:#314659">🌟 @RowOperation 注解新增后置JS表达式执行，实现</span>OperationHandler接口，<span style="color:#fa8c16">afterJS</span>方法即可</li> 
   <li><span style="color:#314659">🌟 多数据源支持自动建表，支持jpa额外配置项</span><span style="color:#f5222d">（多数据源配置发生破坏性更改，详见：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Ferupts%2Ferupt%2Fbgn4gg%2Fedit" target="_blank">多数据源配置</a><span style="color:#f5222d">）</span></li> 
  </ul> 
 </div> 
</div> 
<h2 style="text-align:left"><strong><span style="color:#2ecc71">项目官网</span>：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz" target="_blank">www.erupt.xyz</a></strong></h2> 
<pre><code class="language-java">@Erupt(
       name = "简单的例子",
       power = @Power(importable = true, export = true)
)
@Table(name = "t_simple")   //数据库表名
@Entity
public class Simple extends BaseModel &#123;

    @EruptField(
            views = @View(title = "文本"),
            edit = @Edit(title = "文本", notNull = true, search = @Search)
    )
    private String input;

    @EruptField(
            views = @View(title = "数值", sortable = true),
            edit = @Edit(title = "数值", search = @Search)
    )
    private Float number;

    @EruptField(
            views = @View(title = "布尔"),
            edit = @Edit(title = "布尔", search = @Search)
    )
    private Boolean bool;


    @EruptField(
            views = @View(title = "时间"),
            edit = @Edit(title = "时间", search = @Search(vague = true))
    )
    private Date date;

    @EruptField(
            views = @View(title = "滑动条"),
            edit = @Edit(title = "滑动条", type = EditType.SLIDER, search = @Search,
                    sliderType = @SliderType(max = 90, markPoints = &#123;0, 30, 60, 90&#125;, dots = true))
    )
    private Integer slide;

    @EruptField(
            views = @View(title = "下拉选择"),
            edit = @Edit(
                    search = @Search,
                    title = "下拉选择", type = EditType.CHOICE,
                    choiceType = @ChoiceType(fetchHandler = SqlChoiceFetchHandler.class,
                            fetchHandlerParams = "select id,name from e_upms_menu"
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
<h2> </h2> 
<h2><span style="color:#2ecc71">在线体验 | Demo</span></h2> 
<h4 style="text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz%2Fdemo" target="_blank">https://www.erupt.xyz/demo</a><br> 账号密码：<code>guest / guest</code></h4> 
<p style="text-align:left"><strong>支持主流 4 款现代浏览器，以及 Internet Explorer 11+，可直接运行在 Electron 等基于 Web 标准的环境上</strong></p> 
<p style="text-align:left"> </p> 
<h1><span style="color:#2ecc71">演示截图 | Screenshot ⛰ </span></h1> 
<div style="text-align:justify">
 <img alt="使用 Erupt 零前端代码，仅需一个类文件，开发 Admin 管理后台" src="https://p3-tt.byteimg.com/origin/pgc-image/b054e9ba1907443da1ac9a45dbb61eaa?from=pc" referrerpolicy="no-referrer"> 
 <p> </p> 
</div> 
<div style="text-align:justify">
 <img alt="使用 Erupt 零前端代码，仅需一个类文件，开发 Admin 管理后台" src="https://p3-tt.byteimg.com/origin/pgc-image/fa801c93ff44429390962958e431d0cb?from=pc" referrerpolicy="no-referrer">
</div>
                                        </div>
                                      
</div>
            