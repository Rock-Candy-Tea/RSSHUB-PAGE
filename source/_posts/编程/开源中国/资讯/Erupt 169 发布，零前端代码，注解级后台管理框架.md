
---
title: 'Erupt 1.6.9 发布，零前端代码，注解级后台管理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/erupt/erupt/raw/master/readme/login2.png'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 10:40:00 GMT
thumbnail: 'https://gitee.com/erupt/erupt/raw/master/readme/login2.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left"><span style="color:#1abc9c">本次更新内容</span></h2> 
<ul> 
 <li>🐞 修复erupt-monitory依赖缺失的问题</li> 
 <li>🐞 紧急修复初次加载时有几率登陆报错的恶性bug</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <h1 style="text-align:left"><span style="color:#2ecc71">Erupt Framework</span></h1> 
   <p style="text-align:left">Erupt 是一个低代码 <strong>全栈类</strong> 框架，它使用 <strong>Java 注解</strong> 动态生成页面以及增、删、改、查、权限控制等后台功能。</p> 
   <p style="text-align:left">零前端代码、零 CURD、自动建表，仅需 <strong>一个类文件</strong> + <strong>简洁的注解配置</strong>，快速开发企业级 Admin 管理后台。</p> 
   <p style="text-align:left">提供企业级中后台管理系统的全栈解决方案，大幅压缩研发周期，专注核心业务。</p> 
   <h2 style="text-align:left"><strong>项目官网：</strong><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz" target="_blank">www.erupt.xyz</a></strong></h2> 
   <p style="text-align:left"><img src="https://gitee.com/erupt/erupt/raw/master/readme/login2.png" referrerpolicy="no-referrer"></p> 
   <h2 style="text-align:left">特性 | Features</h2> 
   <ul> 
    <li> <p><strong>自动建表</strong>：表结构自动生成，无需手动建表</p> </li> 
    <li> <p><strong>易于上手</strong>：会简单的 <strong>Spring Boot</strong> 基础知识即可</p> </li> 
    <li> <p><strong>使用简单</strong>：仅需了解 <strong>@Erupt</strong> 与 <strong>@EruptField</strong> 两个注解即可上手开发</p> </li> 
    <li> <p><strong>代码简洁</strong>：仅需一个 <code>.java</code> 文件, template、controller、service、dao 都不需要创建</p> </li> 
    <li> <p><strong>功能强大</strong>：动态条件处理，逻辑删除，LDAP，自定义登录逻辑，RedisSession，操作日志等</p> </li> 
    <li> <p><strong>多数据源</strong>：支持：MySQL、Oracle、SQL Server、<strong>PostgreSQL</strong>、H2，甚至支持 <strong>MongoDB</strong></p> </li> 
    <li> <p><strong>高扩展性</strong>：支持自定义数据源实现、自定义登录逻辑、动态权限管理、生命周期函数、<strong>自定义 OSS</strong></p> </li> 
    <li> <p><strong>大量组件</strong>：滑动输入、时间选择、<strong>一对多</strong>、图片上传、代码编辑器、自动完成、树、<strong>多对多</strong>、地图等23类组件</p> </li> 
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
   <h2> </h2> 
   <h2 style="text-align:left">演示截图 | Screenshot</h2> 
   <p><img src="https://gitee.com/erupt/erupt/raw/master/readme/login2.png" referrerpolicy="no-referrer"></p> 
   <p style="text-align:left"><img src="https://gitee.com/erupt/erupt/raw/master/readme/index.png" referrerpolicy="no-referrer"></p> 
   <p style="text-align:left"><img src="https://gitee.com/erupt/erupt/raw/master/readme/seer.png" referrerpolicy="no-referrer"></p> 
   <p style="text-align:left"><img src="https://gitee.com/erupt/erupt/raw/master/readme/goods.png" referrerpolicy="no-referrer"></p> 
   <p style="text-align:left"><img src="https://gitee.com/erupt/erupt/raw/master/readme/complex-edit.png" referrerpolicy="no-referrer"></p> 
   <h2 style="text-align:left">为什么要做 Erupt ?</h2> 
   <p style="text-align:start"><span style="color:#000000">虽然近些年来 <strong>代码生成器</strong> 成了后台开发的新宠，但它真的是后台开发的最优解吗？</span></p> 
   <p style="text-align:start"><span style="color:#000000">代码生成器的本质还是生成繁琐的前端与后台代码，一旦修改后期生成的代码很难合并，想想 Mybatis-Generator，基本上就是一次性的东西，虽然减轻了部分工作，可解决方式并非最佳。</span></p> 
   <p style="text-align:start"><span style="color:#000000">开发后台管理系统大部分情况下只想做个普通的增删改查界面，用于数据管理，类似下面这种：</span></p> 
   <p style="text-align:left"><img alt="result" src="https://gitee.com/erupt/erupt/raw/master/readme/view.png" referrerpolicy="no-referrer"> <img alt="result" src="https://gitee.com/erupt/erupt/raw/master/readme/edit.png" referrerpolicy="no-referrer"></p> 
   <pre style="text-align:left"><code class="language-java"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Erupt</span></span></span></span></span>(
        name = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"简单的例子"</span></span></span></span></span>,
        power = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Power</span></span></span></span></span>(importable = true, export = true)
)
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Table</span></span></span></span></span>(name = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"demo_simple"</span></span></span></span></span>)
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Entity</span></span></span></span></span>
public class Simple extends BaseModel &#123;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"文本"</span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"文本"</span></span></span></span></span>, notNull = true, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span>)
    )
    private String input;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"数值"</span></span></span></span></span>, sortable = true),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"数值"</span></span></span></span></span>, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span>)
    )
    private Float number;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"布尔"</span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"布尔"</span></span></span></span></span>, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span>)
    )
    private Boolean bool;


    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"时间"</span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"时间"</span></span></span></span></span>, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span>(vague = true))
    )
    private Date date;

    <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@EruptField</span></span></span></span></span>(
            views = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@View</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"滑动条"</span></span></span></span></span>),
            edit = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Edit</span></span></span></span></span>(title = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"滑动条"</span></span></span></span></span>, type = EditType.SLIDER, search = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@Search</span></span></span></span></span>,
                    sliderType = <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@SliderType</span></span></span></span></span>(max = 90, markPoints = &#123;0, 30, 60, 90&#125;, dots = true))
    )
    private Integer slide;

&#125;</code></pre> 
   <p style="text-align:left">这个界面虽然用 Vue + Ant Design + SSM 也能做出个大概，但仔细观察会发现它有大量细节功能如：</p> 
   <ul> 
    <li>有按钮可以查询、新增、批量删除、excel 导入导出</li> 
    <li>可以对数据做筛选、隐藏某列、按某列排序</li> 
    <li>表格有分页与汇总，可预览单行数据</li> 
    <li>多种组件、有校验规则</li> 
   </ul> 
   <p style="text-align:left">全部实现这些仅前端就需要大量的代码，后端的接口与业务逻辑更不在少数。</p> 
   <p style="text-align:left">但可以看到，用 erupt 只需要 <strong>30几行</strong> 代码就能完成，</p> 
   <blockquote> 
    <p>完全不需要了解 <strong>Angular / React / Vue / Jquery</strong><br> 而且不需要了解 <strong>JavaScript / HTML / CSS</strong><br> 甚至不需要了解 <strong>Spring MVC / Mybatis / SQL</strong></p> 
   </blockquote> 
   <p style="text-align:left">即便没学过 erupt 也能猜到大部分配置的作用，只需要简单配置就能完成所有后台页面开发。</p> 
   <p style="text-align:left">这正是建立 erupt 的初衷，对于大部分常用页面，应该使用最简单的方法来实现，甚至不需要学习各种框架和工具，专注核心业务，告别 996，省下的时间做自己喜欢做的事，从此不再因为繁琐的后台开发而焦头烂额。</p> 
   <h2 style="text-align:left">在线体验 | Demo</h2> 
   <h4 style="text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erupt.xyz%2Fdemo" target="_blank">https://www.erupt.xyz/demo</a><br> 账号密码：<code>guest / guest</code></h4> 
   <p style="text-align:left"><strong>支持主流 4 款现代浏览器，以及 Internet Explorer 11+，可直接运行在 Electron 等基于 Web 标准的环境上</strong></p> 
   <table cellspacing="0" style="width:834.809px"> 
    <tbody> 
     <tr> 
      <th><img alt="IE / Edge" height="24px" src="https://cdn.jsdelivr.net/gh/alrra/browser-logos/src/edge/edge_48x48.png" width="24px" referrerpolicy="no-referrer"><br> Edge / IE</th> 
      <th><img alt="Firefox" height="24px" src="https://cdn.jsdelivr.net/gh/alrra/browser-logos/src/firefox/firefox_48x48.png" width="24px" referrerpolicy="no-referrer"><br> Firefox</th> 
      <th><img alt="Chrome" height="24px" src="https://cdn.jsdelivr.net/gh/alrra/browser-logos/src/chrome/chrome_48x48.png" width="24px" referrerpolicy="no-referrer"><br> Chrome</th> 
      <th><img alt="Safari" height="24px" src="https://cdn.jsdelivr.net/gh/alrra/browser-logos/src/safari/safari_48x48.png" width="24px" referrerpolicy="no-referrer"><br> Safari</th> 
      <th><img alt="Opera" height="24px" src="https://cdn.jsdelivr.net/gh/alrra/browser-logos/src/opera/opera_48x48.png" width="24px" referrerpolicy="no-referrer"><br> Opera</th> 
      <th><img alt="Electron" height="24px" src="https://cdn.jsdelivr.net/gh/alrra/browser-logos/src/electron/electron_48x48.png" width="24px" referrerpolicy="no-referrer"><br> Electron</th> 
     </tr> 
     <tr> 
      <td style="border-color:#dfe2e5">Edge 16 / IE 11+</td> 
      <td style="border-color:#dfe2e5">522</td> 
      <td style="border-color:#dfe2e5">57</td> 
      <td style="border-color:#dfe2e5">11</td> 
      <td style="border-color:#dfe2e5">44</td> 
      <td style="border-color:#dfe2e5">Chromium 57</td> 
     </tr> 
    </tbody> 
   </table> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            