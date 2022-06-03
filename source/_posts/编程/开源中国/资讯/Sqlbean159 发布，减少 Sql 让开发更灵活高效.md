
---
title: 'Sqlbean1.5.9 发布，减少 Sql 让开发更灵活高效'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2182'
author: 开源中国
comments: false
date: Thu, 02 Jun 2022 10:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2182'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0em; margin-right:0em; text-align:left">Sqlbean</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p>Sqlbean是一款使用Java面向对象思想来编写并生成Sql语句的工具，在此基础上对<strong>Mybatis</strong>和<strong>Spring Jdbc</strong>实现了类似于JPA的轻量级插件支持。其中内置大量常用SQL执行的方法，可以非常方便的达到你想要的目的，相对复杂的SQL语句也得以支持，在常规的项目开发几乎做到不写DAO层，可以有效的提高项目开发的效率，让开发者更专注于业务代码的编写。</p> 
<p>🚀特点: 零入侵, 多数据源, 动态Schema, 读写分离, 自动建表, 连表查询, 乐观锁, 分页, 支持Mybatis和Spring Jdbc</p> 
<p>💻环境: JDK8+, Mybatis3.2.4+, (Spring MVC 4.1.2+, Spring Boot 1.x, Spring Boot 2.x)</p> 
<p>💿数据库: Mysql, MariaDB, Oracle, Sqlserver2008+, PostgreSQL, DB2, Derby, Sqlite, HSQL, H2</p> 
<p>Sqlbean For Android请移步这里👉<span> </span><a href="https://gitee.com/iJovi/vonce-sqlbean-android">gitee</a>,<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FJovilam77%2Fvonce-sqlbean-android">github</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">简单上手</h4> 
<p>1.引入Maven依赖</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><dependency></span>
<span><groupId>cn.vonce</groupId></span>
<span><artifactId>vonce-sqlbean-spring</artifactId></span>
<span><version>1.5.9</version></span>
<span></dependency></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>2.标注实体类</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@SqlTable</span><span>(</span><span style="color:#dd2200">"d_essay"</span><span>)</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">Essay</strong> <span>&#123;</span></span>
<span>    <span>@SqlId</span><span>(</span><span>type</span> <span>=</span> <strong style="color:#445588">IdType</strong><span>.</span><span style="color:#008080">SNOWFLAKE_ID_16</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Long</strong> <span>id</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>userId</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>content</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Date</strong> <span>creationTime</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Date</strong> <span>updateTime</span><span>;</span></span>
<span>    <span style="color:#888888">/**省略get set方法*/</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>3.无需Dao层，Service层接口只需继承SqlBeanService<实体类, id类型></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>public</strong> <strong>interface</strong> <strong style="color:#445588">EssayService</strong> <strong>extends</strong> <strong style="color:#445588">SqlBeanService</strong><span><</span><strong style="color:#445588">Essay</strong><span>,</span> <strong style="color:#445588">Long</strong><span>></span> <span>&#123;</span></span>
<span>    <span style="color:#888888">//已内置大量常用查询、更新、删除、插入方法，这里可以写自己封装的方法</span></span>

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
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">EssayServiceImpl</strong> <strong>extends</strong> <strong style="color:#445588">MybatisSqlBeanServiceImpl</strong><span><</span><strong style="color:#445588">Essay</strong><span>,</span> <strong style="color:#445588">Long</strong><span>></span> <strong>implements</strong> <strong style="color:#445588">EssayService</strong> <span>&#123;</span></span>

<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>5.Controller层</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@RequestMapping</span><span>(</span><span style="color:#dd2200">"essay"</span><span>)</span></span>
<span><span>@RestController</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">EssayController</strong> <span>&#123;</span></span>

<span>    <span>@Autowired</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">EssayService</strong> <span>essayService</span><span>;</span></span>

<span>    <span style="color:#888888">//查询</span></span>
<span>    <span>@GetMapping</span><span>(</span><span style="color:#dd2200">"select"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">select</strong><span>()</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//查询列表</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Essay</strong><span>></span> <span>list</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">select</span><span>();</span></span>
<span>        <span>list</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">selectBy</span><span>(</span><strong style="color:#445588">Wrapper</strong><span>.</span><span style="color:#008080">where</span><span>(</span><span>gt</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">10</span><span>)).</span><span style="color:#008080">and</span><span>(</span><span>lt</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">20</span><span>)));</span></span>

<span>        <span style="color:#888888">//查询一条</span></span>
<span>        <strong style="color:#445588">Essay</strong> <span>essay</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">selectById</span><span>(</span><span style="color:#009999">1L</span><span>);</span></span>
<span>        <span>essay</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">selectOneBy</span><span>(</span><strong style="color:#445588">Wrapper</strong><span>.</span><span style="color:#008080">where</span><span>(</span><span>eq</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">333</span><span>)));</span></span>

<span>        <span style="color:#888888">//复杂查询</span></span>
<span>        <strong style="color:#445588">Select</strong> <span>select</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>();</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>).</span><span style="color:#008080">column</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">content</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">where</span><span>().</span><span style="color:#008080">gt</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">id</span><span>,</span> <span style="color:#009999">1</span><span>).</span><span style="color:#008080">and</span><span>().</span><span style="color:#008080">eq</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">content</span><span>,</span> <span style="color:#dd2200">"222"</span><span>);</span></span>
<span>        <span>select</span><span>.</span><span style="color:#008080">orderByDesc</span><span>(</span><strong style="color:#445588">Essay</strong><span style="background-color:#ffadad; color:#a61717">$</span><span>.</span><span style="color:#008080">creation_time</span><span>);</span></span>
<span>        <span>list</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">select</span><span>(</span><span>select</span><span>);</span></span>

<span>        <span style="color:#888888">//用于查询Map</span></span>
<span>        <strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>></span> <span>map</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">selectMap</span><span>(</span><span>select</span><span>);</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>>></span> <span>mapList</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">selectMapList</span><span>(</span><span>select</span><span>);</span></span>

<span>        <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">successHint</span><span>(</span><span style="color:#dd2200">"获取成功"</span><span>,</span> <span>list</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//分页</span></span>
<span>    <span>@GetMapping</span><span>(</span><span style="color:#dd2200">"getList"</span><span>)</span></span>
<span>    <strong>public</strong> <strong style="color:#445588">Map</strong> <strong style="color:#990000">getList</strong><span>(</span><strong style="color:#445588">HttpServletRequest</strong> <span>request</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">// 查询对象</span></span>
<span>        <strong style="color:#445588">Select</strong> <span>select</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Select</strong><span>();</span></span>
<span>        <strong style="color:#445588">ReqPageHelper</strong><span><</span><strong style="color:#445588">Essay</strong><span>></span> <span>pageHelper</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">ReqPageHelper</strong><span><>(</span><span>request</span><span>);</span></span>
<span>        <span>pageHelper</span><span>.</span><span style="color:#008080">paging</span><span>(</span><span>select</span><span>,</span> <span>essayService</span><span>);</span></span>
<span>        <strong style="color:#000000">return</strong> <span>pageHelper</span><span>.</span><span style="color:#008080">toResult</span><span>(</span><span style="color:#dd2200">"获取列表成功"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//更新</span></span>
<span>    <span>@PostMapping</span><span>(</span><span style="color:#dd2200">"update"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">update</strong><span>(</span><strong style="color:#445588">Essay</strong> <span>essay</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//根据bean内部id更新</span></span>
<span>        <strong style="color:#445588">long</strong> <span>i</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">updateByBeanId</span><span>(</span><span>essay</span><span>);</span></span>
<span>        <span style="color:#888888">//根据条件更新</span></span>
<span>        <span style="color:#888888">//i = essayService.updateBy(Wrapper.where(gt(Essay$.id, 1)).and(eq(Essay$.content, "222")));</span></span>
<span>        <strong style="color:#000000">if</strong> <span>(</span><span>i</span> <span>></span> <span style="color:#009999">0</span><span>)</span> <span>&#123;</span></span>
<span>            <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">successHint</span><span>(</span><span style="color:#dd2200">"更新成功"</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">othersHint</span><span>(</span><span style="color:#dd2200">"更新失败"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//删除</span></span>
<span>    <span>@PostMapping</span><span>(</span><span style="color:#dd2200">"deleteById"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">deleteById</strong><span>(</span><strong style="color:#445588">Integer</strong><span>[]</span> <span>id</span><span>)</span> <span>&#123;</span></span>
<span>        <span style="color:#888888">//根据id删除</span></span>
<span>        <strong style="color:#445588">long</strong> <span>i</span> <span>=</span> <span>essayService</span><span>.</span><span style="color:#008080">deleteById</span><span>(</span><span>id</span><span>);</span></span>
<span>        <span style="color:#888888">//根据条件删除</span></span>
<span>        <span style="color:#888888">//i = essayService.deleteBy(Wrapper.where(gt(Essay$.id, 1)).and(eq(Essay$.content, "222")));</span></span>
<span>        <strong style="color:#000000">if</strong> <span>(</span><span>i</span> <span>></span> <span style="color:#009999">0</span><span>)</span> <span>&#123;</span></span>
<span>            <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">successHint</span><span>(</span><span style="color:#dd2200">"删除成功"</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <strong style="color:#000000">return</strong> <strong>super</strong><span>.</span><span style="color:#008080">othersHint</span><span>(</span><span style="color:#dd2200">"删除失败"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">//插入</span></span>
<span>    <span>@PostMapping</span><span>(</span><span style="color:#dd2200">"add"</span><span>)</span></span>
<span>    <strong>public</strong> <span style="color:#008080">RS</span> <strong style="color:#990000">add</strong><span>()</span> <span>&#123;</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Essay</strong><span>></span> <span>essayList</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">ArrayList</strong><span><>();</span></span>
<span>        <strong style="color:#000000">for</strong> <span>(</span><strong style="color:#445588">int</strong> <span>i</span> <span>=</span> <span style="color:#009999">0</span><span>;</span> <span>i</span> <span><</span> <span style="color:#009999">100</span><span>;</span> <span>i</span><span>++)</span> <span>&#123;</span></span>
<span>            <strong style="color:#445588">Essay</strong> <span>essay</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Essay</strong><span>(</span><span>i</span><span>,</span> <span style="color:#dd2200">"name"</span> <span>+</span> <span>i</span><span>);</span></span>
<span>            <span>essayList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span>essay</span><span>);</span></span>
<span>        <span>&#125;</span></span>
<span>        <span>essayService</span><span>.</span><span style="color:#008080">insert</span><span>(</span><span>essayList</span><span>);</span></span>
<span>        <strong style="color:#000000">return</strong> <strong style="color:#990000">successHint</strong><span>(</span><span style="color:#dd2200">"成功"</span><span>);</span></span>
<span>    <span>&#125;</span></span>

<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p>本次更新内容</p> 
<p><span style="background-color:#ffffff; color:#40485b">1：优化orderBy方法；</span><br> <span style="background-color:#ffffff; color:#40485b">2：修复创建表没有id时的错误；</span><br> <span style="background-color:#ffffff; color:#40485b">3：重载xxxByCondition方法为xxxBy；</span><br> <span style="background-color:#ffffff; color:#40485b">4：xxxByCondition等方法标记为过时未来删除；</span><br> <span style="background-color:#ffffff; color:#40485b">5：Select新增table方法重载父类并返回Select；</span><br> <span style="background-color:#ffffff; color:#40485b">6：修复简单条件链式条件时没有返回调用者的类型</span></p>
                                        </div>
                                      
</div>
            