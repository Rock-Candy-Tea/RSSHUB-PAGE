
---
title: 'Pear Admin Pro 1.1.1 发布，零侵入式多租户，数据规则权限'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4047'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 10:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4047'
---

<div>   
<div class="content">
                                                                                            <p>项目简介：</p> 
<p>1.基于 Spring 实现的通用权限管理平台（RBAC模式）。整合最新技术高效快速开发，前后端分离模式，开箱即用。</p> 
<p>2.核心模块包括：用户、角色、职位、组织机构、菜单、字典、日志、多应用管理、文件管理、定时任务等功能。</p> 
<p>3.代码量少、学习简单、功能强大、轻量级、易扩展，轻松开发从现在开始！</p> 
<p>项目地址：<a href="https://gitee.com/pear-admin/pear-admin-pro">前往</a></p> 
<p>更新内容：</p> 
<p>[新增] @DataScope 注解 rules 属性，支持 数据权限 规则配置模式</p> 
<p>[新增]  Parameter validation 参数验证</p> 
<p>[新增]  Tenant 拦截器，基于 tenant_id 的逻辑数据隔离</p> 
<p>[新增]  TenantConstant 静态配置</p> 
<p>[新增]  ExcelUtil 读写 Excel 方法，增加</p> 
<p>[修复]  DataScopeInterceptor 拦截 Auto 模式，分页失败</p> 
<p>[优化]  抽象 Invocation 的相关操作到 InvocationHandler </p> 
<p>本次更新，主要解决 数据权限 使用的不足，推出的规则模式，高度自定义的数据过滤方式</p> 
<p>应用场景：</p> 
<p>例如，存在订单列表 与 消息列表，有 两个 角色 admin (管理员) 与 user (用户)，管理员 对 订单列表 的查询范围 为 全部, 对消息列表 的查询范围 为自己，用户 对 订单列表 的查询范围为 仅自己，对 消息列表 的查询范围同样为 仅自己</p> 
<p>简单归纳：<span style="color:#ab1942">不同服务 在 不同角色 访问时 给予不同 的 可见范围</span></p> 
<p>在之前的版本中，此业务只能通过 自定义 mapper 的方式去实现业务，本次更新 解决了 自定义 mapper 繁琐，使用 @DataScopeRule 注解开发该类业务</p> 
<p>核心支持：</p> 
<p>@DataScope 权限注解</p> 
<p>@DataScopeRule 规则注解</p> 
<p>简单示例：</p> 
<p>声明 mapper 实现，查询所有订单</p> 
<pre><code><span style="color:#dd1144"><select id="selectOrder" resultType="SysOrder"></span></code><code>  <span style="color:#0e9ce5">select</span> * from sys_order</code><code><span style="color:#dd1144"></select></span></code>
</pre> 
<p>定义 mapper 接口，查询所有订单</p> 
<pre><code>public List<span style="color:#0e9ce5"><<span style="color:#0e9ce5">SysOrder</span>></span> selectOrder();</code>
</pre> 
<p>可以看到以上代码，为查询所有订单，并未加入过滤条件</p> 
<p>如果我们想要，实现 admin (管理员) 查询所有订单，user (用户) 查询自己的订单，应该怎么做呢？</p> 
<p>修改 mapper 接口如下：</p> 
<pre><code>@DataScope(</code><code>  rules = &#123;</code><code>    @DataScopeRule(role=<span style="color:#dd1144">"admin"</span>, scope=Scope.ALL),</code><code>    @DataScopeRule(role=<span style="color:#dd1144">"user"</span>, scope=Scope.SELF)</code><code>  &#125;</code><code>)</code><code><span style="color:#ca7d37">public</span> List<SysOrder> <span style="color:#dd1144">selectOrder</span>();</code>
</pre> 
<p>详解：</p> 
<p>@DataScope 注解标注的接口，会被 Interceptor 拦截，进行相应的权限处理</p> 
<p>@DataScope 中的 rules 属性，权限规则，即 规定 角色 对应 的查询范围</p> 
<p>@DataScopeRule 为 规则 的载体，用于配置 角色 与 权限的映射，role 属性为 角色 的 code 标识，scope 为 数据权限的枚举</p> 
<p>修改后的 mapper 可以翻译为 ：</p> 
<p>管理员 查询时，返回所有订单信息，用户 查询时，返回自己发起的订单</p> 
<p>解析 ：</p> 
<p>原 SQL 语句</p> 
<pre><code><span style="color:#ca7d37">select</span> * <span style="color:#ca7d37">from</span> sys_order</code>
</pre> 
<p>管理员访问时，执行的 SQL 语句</p> 
<pre><code><span style="color:#ca7d37">select</span> * <span style="color:#ca7d37">from</span> sys_order</code>
</pre> 
<p>用户访问时，执行的 SQL 语句</p> 
<pre><code><span style="color:#ca7d37">select</span> * <span style="color:#ca7d37">from</span> (<span style="color:#ca7d37">select</span> * <span style="color:#ca7d37">from</span> sys_order) data a <span style="color:#ca7d37">where</span> a.create_by = <span style="color:#0e9ce5">1</span></code>
</pre> 
<p>核心实现：DataScopeInterceptor</p> 
<p>回顾：</p> 
<p>指定模式：@DataScope 的 scope 属性，用于指定所有访问都采用该 查询范围</p> 
<p>快速上手：</p> 
<pre><code>@DataScope(scope = Scope.DEPT)</code><code><span style="color:#ca7d37">public</span> List<SysMessage> <span style="color:#dd1144">selectMessage</span>()</code>
</pre> 
<p>解析：所有访问者，都返回自己所在部门的订单信息</p> 
<p>自动模式：scope 配置为 Scope.AUTO 时 , 所有访问的用户，采用该用户拥有的角色所配置的权限范围过滤，当存在多个时，重叠查询范围</p> 
<p>快速上手:</p> 
<pre><code>@DataScope(scope = Scope.AUTO)</code><code><span style="color:#ca7d37">public</span> List<SysMessage> <span style="color:#dd1144">selectMessage</span>()</code>
</pre> 
<p>解析：根据访问者，所拥有的角色对应的数据权限，返回相应范围的消息，当存在多个 角色 时，重叠返回</p> 
<p><span style="background-color:#ffffff; color:#333333">本次除 数据权限 的增强外，还提拱了对多租户的支持</span></p> 
<p>多租户是指软件架构支持一个实例服务多个组织（Customer），每一个用户被称之为租户 （tenant），租户之间的数据是隔离的，并且保证每个用户的数据对其他租户不可见</p> 
<p>由于共享开发和维护成本，对某些用户来说，多租户也是一种经济的解决方案。</p> 
<p>在 Pro 中，我们是如何提供做租户的技术支持</p> 
<p>开始使用：</p> 
<p>TenantConstant 静态配置​​​​​​​</p> 
<pre><code> <em>/**</em></code><code><em>  * 开启多租户</em></code><code><em>  * */</em></code><code>  <span style="color:#ca7d37">public</span> <span style="color:#ca7d37">static</span> <span style="color:#ca7d37">boolean</span> enable = <span style="color:#0e9ce5">true</span>;</code><code>  <em>/**</em></code><code><em>   * 租户字段</em></code><code><em>   * */</em></code><code>  <span style="color:#ca7d37">public</span> <span style="color:#ca7d37">static</span> <span style="color:#ca7d37">String</span> TENANT_COLUMN = <span style="color:#dd1144">"tenant_id"</span>;</code><code>  <em>/**</em></code><code><em>   * 忽略内容</em></code><code><em>   * */</em></code><code>  <span style="color:#ca7d37">public</span> <span style="color:#ca7d37">static</span> <span style="color:#ca7d37">String</span> IGNORE_TABLE[] = &#123;&#125;</code>

</pre> 
<p>1. enable : 启用多租户</p> 
<p>修改 enable 为 true 后，项目全局启用多租户模式，所有的 Select Insert </p> 
<p>Update 操作，将 扩展 对 tenant_id 的字段的关联</p> 
<p>举例：</p> 
<p>Enable 为 false 时：​​​​​​​</p> 
<pre><code><span style="color:#ca7d37">select</span> * from sys_user su</code>
<code>insert into sys_user (name,age) values(<span style="color:#dd1144">"admin"</span>,<span style="color:#0e9ce5">18</span>)</code>
<code>update sys_user set name=<span style="color:#dd1144">"admin"</span> where name = <span style="color:#dd1144">"root"</span></code>
</pre> 
<p>Enable 为 true 时：​​​​​​​</p> 
<pre><code><span style="color:#ca7d37">select</span> * <span style="color:#ca7d37">from</span> sys_user su <span style="color:#ca7d37">where</span> su.tenant_id = <span style="color:#0e9ce5">1</span></code>
<code>insert <span style="color:#ca7d37">into</span> <span style="color:#dd1144">sys_user</span> (name,age,tenant_id) <span style="color:#dd1144">values</span>(<span style="color:#dd1144">"admin"</span>,<span style="color:#0e9ce5">18</span>,<span style="color:#0e9ce5">1</span>)</code>
<code>update sys_user <span style="color:#ca7d37">set</span> name=<span style="color:#dd1144">"admin"</span> <span style="color:#ca7d37">where</span> name = <span style="color:#dd1144">"root"</span> and tenant_id=<span style="color:#0e9ce5">1</span></code>
</pre> 
<p>众所周知，在项目开发中，我们存在 sys_config，sys_tenant 等公共表，是不需要多租户过滤的，我们提供了 <span style="background-color:rgba(0, 0, 0, 0.03)">IGNORE_TABLE</span> 配置​​​​​​​</p> 
<pre><code><span style="color:#ca7d37">public</span> <span style="color:#ca7d37">static</span> <span style="color:#ca7d37">String</span> IGNORE_TABLE[] = &#123;</code><code>       <span style="color:#dd1144">"sys_config"</span>, <span style="color:#dd1144">"sys_tenant"</span>,</code><code>&#125;;</code>
</pre> 
<p>在更复杂的业务中，如 Sys_user 表，需要全局开启多租户的数据隔离，但其中的某一个服务需要查询所有租户的数据，使用 @IgnoreTenant 注解，忽略该接口被多租户处理器处理​​​​​​​</p> 
<pre><code>@IgnoreTenant</code><code>List<span style="color:#0e9ce5"><<span style="color:#0e9ce5">SysUser</span>></span> selectAll();</code></pre>
                                        </div>
                                      
</div>
            