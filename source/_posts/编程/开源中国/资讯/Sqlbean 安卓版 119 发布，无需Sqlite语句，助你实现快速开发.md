
---
title: 'Sqlbean 安卓版 1.1.9 发布，无需Sqlite语句，助你实现快速开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6188'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 09:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6188'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0em; margin-right:0em; text-align:left">Sqlbean For Android</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p>Sqlbean是一款使用Java面向对象思想来编写并生成Sql语句的工具，在此基础上对Android SQLite实现轻量级插件支持。其中内置大量常用SQL执行的方法，可以非常方便的达到你想要的目的，相对复杂的SQL语句也得以支持，在常规的项目开发几乎做到不写SQL，可以有效的提高项目开发的效率，让开发者更专注于业务代码的编写。</p> 
<p>🚀特点: 零入侵, 自动建表, 连表查询, 乐观锁，分页</p> 
<p>💻环境: Android 4.0+</p> 
<p>Sqlbean-Core与Java-Spring版请移步这里👉<span> </span><a href="https://gitee.com/iJovi/vonce-sqlbean">gitee</a>,<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FJovilam77%2Fvonce-sqlbean">github</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">简单上手</h4> 
<p>1.引入Gradle依赖</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>implementation 'cn.vonce:vonce-sqlbean-android:1.1.9'</span>
<span>annotationProcessor 'cn.vonce:vonce-sqlbean-android:1.1.9'</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>2.标注实体类，实体类与表字段映射</p> 
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
<p>3.获取连接（建议在上一步把所有表字段关系建立好，第一次获取连接时会自动创建表结构）</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">MainActivity</strong> <strong>extends</strong> <strong style="color:#445588">AppCompatActivity</strong> <span>&#123;</span></span>

<span>    <strong>private</strong> <strong style="color:#445588">SqlBeanHelper</strong><span><</span><strong style="color:#445588">Essay</strong><span>,</span> <strong style="color:#445588">String</strong><span>></span> <span>essaySqlBeanHelper</span><span>;</span></span>
<span>    <span style="color:#888888">//private SqlBeanHelper<User, String> userSqlBeanHelper;</span></span>

<span>    <span>@Override</span></span>
<span>    <strong>protected</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">onCreate</strong><span>(</span><strong style="color:#445588">Bundle</strong> <span>savedInstanceState</span><span>)</span> <span>&#123;</span></span>
<span>        <strong>super</strong><span>.</span><span style="color:#008080">onCreate</span><span>(</span><span>savedInstanceState</span><span>);</span></span>
<span>        <span>setContentView</span><span>(</span><span style="color:#008080">R</span><span>.</span><span style="color:#008080">layout</span><span>.</span><span style="color:#008080">activity_main</span><span>);</span></span>

<span>        <span style="color:#888888">//方式一，单库模式</span></span>
<span>        <strong style="color:#445588">SQLiteHelper</strong><span>.</span><span style="color:#008080">init</span><span>(</span><strong style="color:#000000">this</strong><span>,</span> <span style="color:#dd2200">"testdb"</span><span>,</span> <span style="color:#009999">1</span><span>);</span><span style="color:#888888">//建议放在MainActivity或继承的Application</span></span>
<span>        <span>essaySqlBeanHelper</span> <span>=</span> <strong style="color:#445588">SQLiteHelper</strong><span>.</span><span style="color:#008080">db</span><span>().</span><span style="color:#008080">get</span><span>(</span><strong style="color:#445588">Essay</strong><span>.</span><span style="color:#008080">class</span><span>);</span></span>

<span>        <span style="color:#888888">//方式二，多库模式</span></span>
<span>        <span style="color:#888888">//essaySqlBeanHelper = SQLiteHelper.db(this, "testdb1", 1).get(Essay.class);</span></span>
<span>        <span style="color:#888888">//userSqlBeanHelper = SQLiteHelper.db(this, "testdb2", 1).get(User.class);</span></span>

<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>4.CRUD操作</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">MainActivity</strong> <strong>extends</strong> <strong style="color:#445588">AppCompatActivity</strong> <span>&#123;</span></span>

<span>    <strong>private</strong> <strong style="color:#445588">SqlBeanHelper</strong><span><</span><strong style="color:#445588">Essay</strong><span>,</span> <strong style="color:#445588">String</strong><span>></span> <span>sqlBeanHelper</span><span>;</span></span>

<span>    <span>@Override</span></span>
<span>    <strong>protected</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">onCreate</strong><span>(</span><strong style="color:#445588">Bundle</strong> <span>savedInstanceState</span><span>)</span> <span>&#123;</span></span>
<span>        <strong>super</strong><span>.</span><span style="color:#008080">onCreate</span><span>(</span><span>savedInstanceState</span><span>);</span></span>
<span>        <span>setContentView</span><span>(</span><span style="color:#008080">R</span><span>.</span><span style="color:#008080">layout</span><span>.</span><span style="color:#008080">activity_main</span><span>);</span></span>

<span>        <strong style="color:#445588">SQLiteHelper</strong><span>.</span><span style="color:#008080">init</span><span>(</span><strong style="color:#000000">this</strong><span>,</span> <span style="color:#dd2200">"testdb"</span><span>,</span> <span style="color:#009999">1</span><span>);</span></span>
<span>        <span>sqlBeanHelper</span> <span>=</span> <strong style="color:#445588">SQLiteHelper</strong><span>.</span><span style="color:#008080">db</span><span>().</span><span style="color:#008080">get</span><span>(</span><strong style="color:#445588">Essay</strong><span>.</span><span style="color:#008080">class</span><span>);</span></span>

<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//查询</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">select</strong><span>()</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//查询列表</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">User</strong><span>></span> <span>list</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">select</span><span>();</span></span>
<span>        <span>list</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">selectBy</span><span>(</span><strong style="color:#445588">Wrapper</strong><span>.</span><span style="color:#008080">where</span><span>(</span><span>gt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">10</span><span>)).</span><span style="color:#008080">and</span><span>(</span><span>lt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">20</span><span>)));</span></span>
<span>        <span style="color:#888888">//指定查询</span></span>
<span>        <span>list</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">select</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>().</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">name</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">phone</span><span>).</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">eq</span><span>());</span></span>

<span>        <span style="color:#888888">//查询一条</span></span>
<span>        <strong style="color:#445588">User</strong> <span>user</span> <span>=</span> <span>userService</span><span>.</span><span style="color:#008080">selectById</span><span>(</span><span style="color:#009999">1</span><span>);</span></span>
<span>        <span>user</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">selectOneBy</span><span>(</span><strong style="color:#445588">Wrapper</strong><span>.</span><span style="color:#008080">where</span><span>(</span><span>eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">1001</span><span>)));</span></span>

<span>        <span style="color:#888888">//sql语义化查询《20岁且是女性的用户根据创建时间倒序，获取前10条》</span></span>
<span>        <span>list</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">select</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>().</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">name</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">phone</span><span style="background-color:#ffadad; color:#a61717">$</span><span>).</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">age</span><span>,</span> <span style="color:#009999">22</span><span>).</span><span style="color:#008080">and</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">gender</span><span>,</span> <span style="color:#009999">0</span><span>).</span><span style="color:#008080">back</span><span>().</span><span style="color:#008080">orderByDesc</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">createTime</span><span>).</span><span style="color:#008080">page</span><span>(</span><span style="color:#009999">0</span><span>,</span> <span style="color:#009999">10</span><span>));</span></span>

<span>        <span style="color:#888888">//联表查询《20岁且是女性的用户根据创建时间倒序，查询前10条用户的信息和地址》</span></span>
<span>        <strong style="color:#445588">Select</strong> <span>select</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>();</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">name</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">phone</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">province</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">city</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">area</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">details</span><span style="background-color:#ffadad; color:#a61717">$</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">join</span><span>(</span><strong style="color:#445588">JoinType</strong><span>.</span><span style="color:#008080">INNER_JOIN</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">_tableName</span><span>,</span> <strong style="color:#445588">UserAddress</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">user_id</span><span>,</span> <strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">gt</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">age</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <span style="color:#009999">22</span><span>).</span><span style="color:#008080">and</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">gender</span><span style="background-color:#ffadad; color:#a61717">$</span><span>,</span> <span style="color:#009999">0</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">orderByDesc</span><span>(</span><strong style="color:#445588">User</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">createTime</span><span style="background-color:#ffadad; color:#a61717">$</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">page</span><span>(</span><span style="color:#009999">0</span><span>,</span> <span style="color:#009999">10</span><span>);</span></span>

<span>        <span style="color:#888888">//查询Map</span></span>
<span>        <strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>></span> <span>map</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">selectMap</span><span>(</span><span>select</span><span>);</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>>></span> <span>mapList</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">selectMapList</span><span>(</span><span>select</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//分页</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">getPageList</strong><span>()</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">// 查询对象</span></span>
<span>        <strong style="color:#445588">Select</strong> <span>select</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>();</span></span>
<span>        <strong style="color:#445588">PageHelper</strong><span><</span><strong style="color:#445588">User</strong><span>></span> <span>pageHelper</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">PageHelper</strong><span><>(</span><span style="color:#009999">0</span><span>,</span> <span style="color:#009999">10</span><span>);</span></span>
<span>        <span>pageHelper</span><span>.</span><span style="color:#008080">paging</span><span>(</span><span>select</span><span>,</span> <span>sqlBeanHelper</span><span>);</span></span>
<span>        <strong style="color:#445588">ResultData</strong><span><</span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Essay</strong><span>>></span> <span>data</span> <span>=</span> <span>pageHelper</span><span>.</span><span style="color:#008080">getResultData</span><span>();</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//更新</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">update</strong><span>(</span><strong style="color:#445588">Essay</strong> <span>essay</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//根据bean内部id更新</span></span>
<span>        <strong style="color:#445588">long</strong> <span>i</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">updateByBeanId</span><span>(</span><span>essay</span><span>);</span></span>
<span>        <span style="color:#888888">//根据外部id更新</span></span>
<span>        <span style="color:#888888">//i = sqlBeanHelper.updateById(essay, 20);</span></span>
<span>        <span style="color:#888888">//根据条件更新</span></span>
<span>        <span style="color:#888888">//i = sqlBeanHelper.updateBy(Wrapper.where(gt(User$.age, 22)).and(eq(User$.gender, 1)));</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//删除</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">deleteById</strong><span>(</span><strong style="color:#445588">String</strong><span>[]</span> <span>id</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//根据id删除</span></span>
<span>        <strong style="color:#445588">long</strong> <span>i</span> <span>=</span> <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">deleteById</span><span>(</span><span>id</span><span>);</span></span>
<span>        <span style="color:#888888">//根据条件删除</span></span>
<span>        <span style="color:#888888">//i = sqlBeanHelper.deleteBy(Wrapper.where(gt(User$.age, 22)).and(eq(User$.gender, 1)));</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//插入</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">void</strong> <strong style="color:#990000">add</strong><span>()</span> <span>&#123;</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Essay</strong><span>></span> <span>essayList</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">ArrayList</strong><span><>();</span></span>
<span>        <strong style="color:#000000">for</strong> <span>(</span><strong style="color:#445588">int</strong> <span>i</span> <span>=</span> <span style="color:#009999">0</span><span>;</span> <span>i</span> <span><</span> <span style="color:#009999">100</span><span>;</span> <span>i</span><span>++)</span> <span>&#123;</span></span>
<span>            <strong style="color:#445588">Essay</strong> <span>essay</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Essay</strong><span>(</span><span>i</span><span>,</span> <span style="color:#dd2200">"name"</span> <span>+</span> <span>i</span><span>);</span></span>
<span>            <span>essayList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span>essay</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <span>sqlBeanHelper</span><span>.</span><span style="color:#008080">insert</span><span>(</span><span>essayList</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p>本次更新内容：</p> 
<p><span style="background-color:#ffffff; color:#40485b">1：列字段注解名称允许为空；</span><br> <span style="background-color:#ffffff; color:#40485b">2：连接表注解支持ON自定义连接条件；</span><br> <span style="background-color:#ffffff; color:#40485b">3：修复创建表时默认值的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">4：修复排序时如果没有表别名也增加转义的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">5：修复单表查询时指定class映射不生效的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">6：修复分页克隆的count方法在遇到分组时的bug；</span><br> <span style="background-color:#ffffff; color:#40485b">7：优化创建sql语句主键字段加上not null；</span><br> <span style="background-color:#ffffff; color:#40485b">8：优化指定类型返回功能；</span><br> <span style="background-color:#ffffff; color:#40485b">9：优化内部部分代码和重新实现；</span></p>
                                        </div>
                                      
</div>
            