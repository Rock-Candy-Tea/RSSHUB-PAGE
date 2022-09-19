
---
title: 'Sqlbean1.5.15 发布，Java 快速开发利器，感受_无 SQL_编程'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7349'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 09:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7349'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0em; margin-right:0em; text-align:left">Sqlbean</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p>Sqlbean是一款通过Java语法编写SQL语句并自动生成的ORM插件，除了支持Mybatis也同时支持Spring Jdbc，内置大量常用方法，无需编写DAO层，能减少90%的SQL语句，帮助你快速进行业务功能开发。</p> 
<p>🚀特点: 无入侵, 多数据源, 动态Schema, 读写分离, 自动建表, 连表查询, 乐观锁, 分页, 支持Spring Jdbc</p> 
<p>💻环境: JDK8+, Mybatis3.2.4+, (Spring MVC 4.1.2+, Spring Boot 1.x, Spring Boot 2.x)</p> 
<p>💿数据库: Mysql, MariaDB, Oracle, Sqlserver2008+, Postgresql, DB2, Derby, Sqlite, HSQL, H2</p> 
<p>Sqlbean For Android请移步这里👉<span> </span><a href="https://gitee.com/iJovi/vonce-sqlbean-android">gitee(推荐)</a>、<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FJovilam77%2Fvonce-sqlbean-android">github(停止更新)</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">简单上手</h4> 
<p>1.引入Maven依赖</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><dependency></span>
<span><groupId>cn.vonce</groupId></span>
<span><artifactId>vonce-sqlbean-spring</artifactId></span>
<span><version>1.5.15</version></span>
<span></dependency></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>2.标注实体类</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@SqlTable</span><span>(</span><span style="color:#dd2200">"d_user"</span><span>)</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">User</strong> <span>&#123;</span></span>
<span>    <span>@SqlId</span><span>(</span><span>type</span> <span>=</span> <strong style="color:#445588">IdType</strong><span>.</span><span style="color:#008080">SNOWFLAKE_ID_16</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Long</strong> <span>id</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>name</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>age</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>stature</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>gender</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>phone</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Date</strong> <span>createTime</span><span>;</span></span>
<span>    <span style="color:#888888">/**省略get set方法*/</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>3.无需Dao层，Service层接口只需继承SqlBeanService<实体类, id类型></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>public</strong> <strong>interface</strong> <strong style="color:#445588">UserService</strong> <strong>extends</strong> <strong style="color:#445588">SqlBeanService</strong><span><</span><strong style="color:#445588">User</strong><span>,</span> <strong style="color:#445588">Long</strong><span>></span> <span>&#123;</span></span>
<span>    <span style="color:#888888">//这里可以写自己封装的方法</span></span>

<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>4.Service实现类只需继承MybatisSqlBeanServiceImpl<实体类, id类型>和实现你的Service接口</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">//使用Spring Jdbc的话将继承的父类改成SpringJdbcSqlBeanServiceImpl即可</span></span>
<span><span>@Service</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">UserServiceImpl</strong> <strong>extends</strong> <strong style="color:#445588">MybatisSqlBeanServiceImpl</strong><span><</span><strong style="color:#445588">User</strong><span>,</span> <strong style="color:#445588">Long</strong><span>></span> <strong>implements</strong> <strong style="color:#445588">UserService</strong> <span>&#123;</span></span>

<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>5.Controller层</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@RequestMapping</span><span>(</span><span style="color:#dd2200">"user"</span><span>)</span></span>
<span><span>@RestController</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">UserController</strong> <span>&#123;</span></span>

<span>    <span>@Autowired</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">UserService</strong> <span>userService</span><span>;</span></span>

<span>    <span style="color:#888888">//查询</span></span>
<span>    <span>@GetMapping</span><span>(</span><span style="color:#dd2200">"select"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">select</strong><span>()</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//查询列表</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">User</strong><span>></span> <span>list</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">select</span><span>();</span></span>
<span>        <span>list</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">selectBy</span><span>(</span><strong style="color:#445588">Wrapper</strong><span>.</span><span style="color:#008080">where</span><span>(</span><span>gt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">10</span><span>)).</span><span style="color:#008080">and</span><span>(</span><span>lt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">20</span><span>)));</span></span>
<span>        <span style="color:#888888">//指定查询</span></span>
<span>        <span>list</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">select</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>().</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">name</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">phone</span><span style="background-color:#ffadad; color:#a61717">$</span><span>).</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">gt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <span style="color:#009999">10</span><span>));</span></span>

<span>        <span style="color:#888888">//查询一条</span></span>
<span>        <strong style="color:#445588">User</strong> <span>user</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">selectById</span><span>(</span><span style="color:#009999">1</span><span>);</span></span>
<span>        <span>user</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">selectOneBy</span><span>(</span><strong style="color:#445588">Wrapper</strong><span>.</span><span style="color:#008080">where</span><span>(</span><span>eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">1001</span><span>)));</span></span>

<span>        <span style="color:#888888">//sql语义化查询《20岁且是女性的用户根据创建时间倒序，获取前10条》</span></span>
<span>        <span>list</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">select</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>().</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">name</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">phone</span><span style="background-color:#ffadad; color:#a61717">$</span><span>).</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">age</span><span>,</span> <span style="color:#009999">22</span><span>).</span><span style="color:#008080">and</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">gender</span><span>,</span> <span style="color:#009999">0</span><span>).</span><span style="color:#008080">back</span><span>().</span><span style="color:#008080">orderByDesc</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">createTime</span><span>).</span><span style="color:#008080">page</span><span>(</span><span style="color:#009999">0</span><span>,</span> <span style="color:#009999">10</span><span>));</span></span>

<span>        <span style="color:#888888">//联表查询《20岁且是女性的用户根据创建时间倒序，查询前10条用户的信息和地址》</span></span>
<span>        <strong style="color:#445588">Select</strong> <span>select</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>();</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">name</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">phone</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">province</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">city</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">area</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">details</span><span style="background-color:#ffadad; color:#a61717">$</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">join</span><span>(</span><strong style="color:#445588">JoinType</strong><span>.</span><span style="color:#008080">INNER_JOIN</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">_tableName</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">user_id</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">gt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">age</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <span style="color:#009999">22</span><span>).</span><span style="color:#008080">and</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">gender</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <span style="color:#009999">0</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">orderByDesc</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">createTime</span><span style="background-color:#ffadad; color:#a61717">$</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">page</span><span>(</span><span style="color:#009999">0</span><span>,</span> <span style="color:#009999">10</span><span>);</span></span>

<span>        <span style="color:#888888">//查询Map</span></span>
<span>        <strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>></span> <span>map</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">selectMap</span><span>(</span><span>select</span><span>);</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>>></span> <span>mapList</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">selectMapList</span><span>(</span><span>select</span><span>);</span></span>

<span>        <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">successHint</span><span>(</span><span style="color:#dd2200">"获取成功"</span><span>,</span> <span>list</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//分页</span></span>
<span>    <span>@GetMapping</span><span>(</span><span style="color:#dd2200">"getList"</span><span>)</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">Map</strong> <strong style="color:#990000">getList</strong><span>(</span><strong style="color:#445588">HttpServletRequest</strong> <span>request</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">// 查询对象</span></span>
<span>        <strong style="color:#445588">Select</strong> <span>select</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>();</span></span>
<span>        <strong style="color:#445588">ReqPageHelper</strong><span><</span><strong style="color:#445588">User</strong><span>></span> <span>pageHelper</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">ReqPageHelper</strong><span><>(</span><span>request</span><span>);</span></span>
<span>        <span>pageHelper</span><span>.</span><span style="color:#008080">paging</span><span>(</span><span>select</span><span>,</span> <span>userService</span><span>);</span></span>
<span>        <strong style="color:#000000">return</strong> <span>pageHelper</span><span>.</span><span style="color:#008080">toResult</span><span>(</span><span style="color:#dd2200">"获取列表成功"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//更新</span></span>
<span>    <span>@PostMapping</span><span>(</span><span style="color:#dd2200">"update"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">update</strong><span>(</span><strong style="color:#445588">User</strong> <span>user</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//根据bean内部id更新</span></span>
<span>        <strong style="color:#445588">long</strong> <span>i</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">updateByBeanId</span><span>(</span><span>user</span><span>);</span></span>
<span>        <span style="color:#888888">//根据条件更新</span></span>
<span>        <span style="color:#888888">//i = userService.updateBy(Wrapper.where(gt(User$.age, 22)).and(eq(User$.gender, 1)));</span></span>
<span>        <strong style="color:#000000">if</strong> <span>(</span><span>i</span> <span>></span> <span style="color:#009999">0</span><span>)</span> <span>&#123;</span></span>
<span>            <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">successHint</span><span>(</span><span style="color:#dd2200">"更新成功"</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">othersHint</span><span>(</span><span style="color:#dd2200">"更新失败"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//删除</span></span>
<span>    <span>@PostMapping</span><span>(</span><span style="color:#dd2200">"deleteById"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">deleteById</strong><span>(</span><strong style="color:#445588">Integer</strong><span>[]</span> <span>id</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//根据id删除</span></span>
<span>        <strong style="color:#445588">long</strong> <span>i</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">deleteById</span><span>(</span><span>id</span><span>);</span></span>
<span>        <span style="color:#888888">//根据条件删除</span></span>
<span>        <span style="color:#888888">//i = userService.deleteBy(Wrapper.where(gt(User$.age, 22)).and(eq(User$.gender, 1)));</span></span>
<span>        <strong style="color:#000000">if</strong> <span>(</span><span>i</span> <span>></span> <span style="color:#009999">0</span><span>)</span> <span>&#123;</span></span>
<span>            <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">successHint</span><span>(</span><span style="color:#dd2200">"删除成功"</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">othersHint</span><span>(</span><span style="color:#dd2200">"删除失败"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//插入</span></span>
<span>    <span>@PostMapping</span><span>(</span><span style="color:#dd2200">"add"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">add</strong><span>()</span> <span>&#123;</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">User</strong><span>></span> <span>userList</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">ArrayList</strong><span><>();</span></span>
<span>        <strong style="color:#000000">for</strong> <span>(</span><strong style="color:#445588">int</strong> <span>i</span> <span>=</span> <span style="color:#009999">0</span><span>;</span> <span>i</span> <span><</span> <span style="color:#009999">100</span><span>;</span> <span>i</span><span>++)</span> <span>&#123;</span></span>
<span>            <strong style="color:#445588">User</strong> <span>user</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">User</strong><span>(</span><span>i</span><span>,</span> <span style="color:#dd2200">"name"</span> <span>+</span> <span>i</span><span>);</span></span>
<span>            <span>userList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span>user</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <span>userService</span><span>.</span><span style="color:#008080">insert</span><span>(</span><span>userList</span><span>);</span></span>
<span>        <strong style="color:#000000">return</strong> <strong style="color:#990000">successHint</strong><span>(</span><span style="color:#dd2200">"成功"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p>本次更新内容：</p> 
<p><span style="background-color:#ffffff; color:#40485b">1：列字段注解名称允许为空；</span><br> <span style="background-color:#ffffff; color:#40485b">2：查询表名称时增加表注释字段查询；</span><br> <span style="background-color:#ffffff; color:#40485b">3：表信息列信息注释字段改为remarks；</span><br> <span style="background-color:#ffffff; color:#40485b">4：连接表注解支持ON自定义连接条件；</span><br> <span style="background-color:#ffffff; color:#40485b">5：Mysql数据库创建表时新增表注释和列注释支持；</span><br> <span style="background-color:#ffffff; color:#40485b">6：修复sqlserver分页问题；</span><br> <span style="background-color:#ffffff; color:#40485b">7：修复oracle查询tableList的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">8：修复创建表时默认值的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">9：修复排序时如果没有表别名也增加转义的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">10：修复单表查询时指定class映射不生效的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">11：修复不同数据库boolean类型和bit类型的兼容；</span><br> <span style="background-color:#ffffff; color:#40485b">12：修复hsql数据库因大小写问题导致的bug；</span><br> <span style="background-color:#ffffff; color:#40485b">13：修复分页克隆的count方法在遇到分组时的bug；</span><br> <span style="background-color:#ffffff; color:#40485b">14：优化创建sql语句主键字段加上not null；</span><br> <span style="background-color:#ffffff; color:#40485b">15：优化指定类型返回功能；</span><br> <span style="background-color:#ffffff; color:#40485b">16：优化内部部分代码和重新实现；</span></p>
                                        </div>
                                      
</div>
            