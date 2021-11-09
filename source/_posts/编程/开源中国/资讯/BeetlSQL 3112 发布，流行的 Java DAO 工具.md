
---
title: 'BeetlSQL 3.11.2 发布，流行的 Java DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5f89c4abc4b0b777ff342b109c162b7298c.png'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 09:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5f89c4abc4b0b777ff342b109c162b7298c.png'
---

<div>   
<div class="content">
                                                                                            <ul> 
 <li>修复内置的insertTemplate方法，keywordHandler没有启用的Bug</li> 
 <li>Beetl版本更新到3.8.1.RELEASE</li> 
 <li> <p>solon 集成最新版本1.5.50</p> </li> 
</ul> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>修复 3.9 版本以来 ID 生成器没有自动注册的 Bug</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>beetlsql<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>3.11.2-RELEASE<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></code></pre> 
<p>BeetlSQL 自主研发自 2015 年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑，不亚于 MyBatis。你不想写 SQL 也好，或者想更好地写 SQL 也好，BeetlSQL 都能满足这要求，目前支持的数据库如下</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>传统数据库：MySQL (包括支持MySQL协议的各种数据库), MariaDB ,Oralce ,Postgres (包括支持 Postgres 协议的各种数据库), DB2 , SQL Server ，H2 , SQLite , Derby ，神通，达梦，华为高斯，人大金仓，PolarDB，GBase8s，GreatSQL 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive,GreenPlum</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎：Drill,Presto，Druid</li> 
 <li>内存数据库：ignite，CouchBase</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"> </span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a> <a href="https://gitee.com/xiandafu/dao-benchmark">性能测试</a></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子1,内置方法，无需写SQL完成常用操作</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#445588">UserEntity</strong> <span>user</span>  <span>=</span> <span>sqlManager</span><span>.</span><span style="color:#008080">unique</span><span>(</span><strong style="color:#445588">UserEntity</strong><span>.</span><span style="color:#008080">class</span><span>,</span><span style="color:#009999">1</span><span>);</span></span>

<span><span>user</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"ok123"</span><span>);</span></span>
<span><span>sqlManager</span><span>.</span><span style="color:#008080">updateById</span><span>(</span><span>user</span><span>);</span></span>

<span><strong style="color:#445588">UserEntity</strong> <span>newUser</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">UserEntity</strong><span>();</span></span>
<span><span>newUser</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"newUser"</span><span>);</span></span>
<span><span>newUser</span><span>.</span><span style="color:#008080">setDepartmentId</span><span>(</span><span style="color:#009999">1</span><span>);</span></span>
<span><span>sqlManager</span><span>.</span><span style="color:#008080">insert</span><span>(</span><span>newUser</span><span>);</span></span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">输出日志友好,可反向定位到调用的代码</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>┏━━━━━ Debug [user.selectUserAndDepartment] ━━━</span>
<span>┣ SQL：     select * from user where 1 = 1 and id=?</span>
<span>┣ 参数：     [1]</span>
<span>┣ 位置：     org.beetl.sql.test.QuickTest.main(QuickTest.java:47)</span>
<span>┣ 时间：     23ms</span>
<span>┣ 结果：     [1]</span>
<span>┗━━━━━ Debug [user.selectUserAndDepartment] ━━━</span></pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子2 使用SQL</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#445588">String</strong> <span>sql</span> <span>=</span> <span style="color:#dd2200">"select * from user where id=?"</span><span>;</span></span>
<span><strong style="color:#445588">Integer</strong> <span>id</span>  <span>=</span> <span style="color:#009999">1</span><span>;</span></span>
<span><strong style="color:#445588">SQLReady</strong> <span>sqlReady</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">SQLReady</strong><span>(</span><span>sql</span><span>,</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Object</strong><span>[</span><span>id</span><span>]);</span></span>
<span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>userEntities</span> <span>=</span> <span>sqlManager</span><span>.</span><span style="color:#008080">execute</span><span>(</span><span>sqlReady</span><span>,</span><strong style="color:#445588">UserEntity</strong><span>.</span><span style="color:#008080">class</span><span>);</span></span>
<span><span style="color:#888888">//Map 也可以作为输入输出参数</span></span>
<span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">Map</strong><span>></span> <span>listMap</span> <span>=</span>  <span>sqlManager</span><span>.</span><span style="color:#008080">execute</span><span>(</span><span>sqlReady</span><span>,</span><strong style="color:#445588">Map</strong><span>.</span><span style="color:#008080">class</span><span>);</span></span></pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子3 使用模板SQL</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#445588">String</strong> <span>sql</span> <span>=</span> <span style="color:#dd2200">"select * from user where department_id=#&#123;id&#125; and name=#&#123;name&#125;"</span><span>;</span></span>
<span><strong style="color:#445588">UserEntity</strong> <span>paras</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">UserEntity</strong><span>();</span></span>
<span><span>paras</span><span>.</span><span style="color:#008080">setDepartmentId</span><span>(</span><span style="color:#009999">1</span><span>);</span></span>
<span><span>paras</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"lijz"</span><span>);</span></span>
<span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>list</span> <span>=</span> <span>sqlManager</span><span>.</span><span style="color:#008080">execute</span><span>(</span><span>sql</span><span>,</span><strong style="color:#445588">UserEntity</strong><span>.</span><span style="color:#008080">class</span><span>,</span><span>paras</span><span>);</span></span>

<span><strong style="color:#445588">String</strong> <span>sql</span> <span>=</span> <span style="color:#dd2200">"select * from user where id in ( #&#123;join(ids)&#125; )"</span><span>;</span></span>
<span><strong style="color:#445588">List</strong> <span>list</span> <span>=</span> <strong style="color:#445588">Arrays</strong><span>.</span><span style="color:#008080">asList</span><span>(</span><span style="color:#009999">1</span><span>,</span><span style="color:#009999">2</span><span>,</span><span style="color:#009999">3</span><span>,</span><span style="color:#009999">4</span><span>,</span><span style="color:#009999">5</span><span>);</span> <strong style="color:#445588">Map</strong> <span>paras</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">HashMap</strong><span>();</span></span>
<span><span>paras</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"ids"</span><span>,</span> <span>list</span><span>);</span></span>
<span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>users</span> <span>=</span> <span>sqlManager</span><span>.</span><span style="color:#008080">execute</span><span>(</span><span>sql</span><span>,</span> <strong style="color:#445588">UserEntity</strong><span>.</span><span style="color:#008080">class</span><span>,</span> <span>paras</span><span>);</span></span></pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子4 使用Query类</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持重构</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#445588">LambdaQuery</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>query</span> <span>=</span> <span>sqlManager</span><span>.</span><span style="color:#008080">lambdaQuery</span><span>(</span><strong style="color:#445588">UserEntity</strong><span>.</span><span style="color:#008080">class</span><span>);</span></span>
<span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>entities</span> <span>=</span> <span>query</span><span>.</span><span style="color:#008080">andEq</span><span>(</span><span>UserEntity:</span><span>:</span><span>getDepartmentId</span><span>,</span><span style="color:#009999">1</span><span>)</span></span>
<span>                    <span>.</span><span style="color:#008080">andIsNotNull</span><span>(</span><span>UserEntity:</span><span>:</span><span>getName</span><span>).</span><span style="color:#008080">select</span><span>();</span></span>
</pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子5 把数十行SQL放到sql文件里维护</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">//访问user.md#select</span></span>
<span><strong style="color:#445588">SqlId</strong> <span>id</span> <span>=</span> <strong style="color:#445588">SqlId</strong><span>.</span><span style="color:#008080">of</span><span>(</span><span style="color:#dd2200">"user"</span><span>,</span><span style="color:#dd2200">"select"</span><span>);</span></span>
<span><strong style="color:#445588">Map</strong> <span>map</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">HashMap</strong><span>();</span></span>
<span><span>map</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"name"</span><span>,</span><span style="color:#dd2200">"n"</span><span>);</span></span>
<span><strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>list</span> <span>=</span> <span>sqlManager</span><span>.</span><span style="color:#008080">select</span><span>(</span><span>id</span><span>,</span><strong style="color:#445588">UserEntity</strong><span>.</span><span style="color:#008080">class</span><span>,</span><span>map</span><span>);</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5f89c4abc4b0b777ff342b109c162b7298c.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子6 复杂映射支持</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持像mybatis那样复杂的映射</p> 
<ul> 
 <li>自动映射</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@Data</span></span>
<span><span>@ResultProvider</span><span>(</span><strong style="color:#445588">AutoJsonMapper</strong><span>.</span><span style="color:#008080">class</span><span>)</span></span>
<span> <strong>public</strong> <strong>static</strong> <strong>class</strong> <strong style="color:#445588">MyUserView</strong> <span>&#123;</span></span>
<span>        <strong style="color:#445588">Integer</strong> <span>id</span><span>;</span></span>
<span>        <strong style="color:#445588">String</strong> <span>name</span><span>;</span></span>
<span>        <strong style="color:#445588">DepartmentEntity</strong> <span>dept</span><span>;</span></span>
<span> <span>&#125;</span></span>
</pre> 
 </div> 
</div> 
<ul> 
 <li>配置映射，比MyBatis更容易理解，报错信息更详细</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>&#123;</span></span>
<span><span style="color:#bbbbbb"></span><span>"id"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"id"</span><span>,</span></span>
<span><span style="color:#bbbbbb"></span><span>"name"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"name"</span><span>,</span></span>
<span><span style="color:#bbbbbb"></span><span>"dept"</span><span>:</span><span style="color:#bbbbbb"> </span><span>&#123;</span></span>
<span><span style="color:#bbbbbb"></span><span>"id"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"dept_id"</span><span>,</span></span>
<span><span style="color:#bbbbbb"></span><span>"name"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"dept_name"</span></span>
<span><span style="color:#bbbbbb"></span><span>&#125;,</span></span>
<span><span style="color:#bbbbbb"></span><span>"roles"</span><span>:</span><span style="color:#bbbbbb"> </span><span>&#123;</span></span>
<span><span style="color:#bbbbbb"></span><span>"id"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"r_id"</span><span>,</span></span>
<span><span style="color:#bbbbbb"></span><span>"name"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"r_name"</span></span>
<span><span style="color:#bbbbbb"></span><span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子7 最好使用mapper来作为数据库访问类</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@SqlResource</span><span>(</span><span style="color:#dd2200">"user"</span><span>)</span> <span style="color:#888888">/*sql文件在user.md里*/</span></span>
<span><strong>public</strong> <strong>interface</strong> <strong style="color:#445588">UserMapper</strong> <strong>extends</strong> <strong style="color:#445588">BaseMapper</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <span>&#123;</span></span>

<span>    <span>@Sql</span><span>(</span><span style="color:#dd2200">"select * from user where id = ?"</span><span>)</span></span>
<span>    <strong style="color:#445588">UserEntity</strong> <strong style="color:#990000">queryUserById</strong><span>(</span><strong style="color:#445588">Integer</strong> <span>id</span><span>);</span></span>

<span>    <span>@Sql</span><span>(</span><span style="color:#dd2200">"update user set name=? where id = ?"</span><span>)</span></span>
<span>    <span>@Update</span></span>
<span>    <strong style="color:#445588">int</strong> <strong style="color:#990000">updateName</strong><span>(</span><strong style="color:#445588">String</strong> <span>name</span><span>,</span><strong style="color:#445588">Integer</strong> <span>id</span><span>);</span></span>

<span>    <span>@Template</span><span>(</span><span style="color:#dd2200">"select * from user where id = #&#123;id&#125;"</span><span>)</span></span>
<span>    <strong style="color:#445588">UserEntity</strong> <strong style="color:#990000">getUserById</strong><span>(</span><strong style="color:#445588">Integer</strong> <span>id</span><span>);</span></span>

<span>    <span>@SpringData</span><span style="color:#888888">/*Spring Data风格*/</span></span>
<span>    <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <strong style="color:#990000">queryByNameOrderById</strong><span>(</span><strong style="color:#445588">String</strong> <span>name</span><span>);</span></span>

<span>    <span style="color:#888888">/**</span></span>
<span><span style="color:#888888">     * 可以定义一个default接口</span></span>
<span><span style="color:#888888">     * @return</span></span>
<span><span style="color:#888888">     */</span></span>
<span>     <strong style="color:#000000">default</strong>  <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">DepartmentEntity</strong><span>></span> <strong style="color:#990000">findAllDepartment</strong><span>()&#123;</span></span>
<span>        <strong style="color:#445588">Map</strong> <span>paras</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">HashMap</strong><span>();</span></span>
<span>        <span>paras</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"exlcudeId"</span><span>,</span><span style="color:#009999">1</span><span>);</span></span>
<span>        <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">DepartmentEntity</strong><span>></span> <span>list</span> <span>=</span> <span>getSQLManager</span><span>().</span><span style="color:#008080">execute</span><span>(</span><span style="color:#dd2200">"select * from department where id != #&#123;exlcudeId&#125;"</span><span>,</span><strong style="color:#445588">DepartmentEntity</strong><span>.</span><span style="color:#008080">class</span><span>,</span><span>paras</span><span>);</span></span>
<span>        <strong style="color:#000000">return</strong> <span>list</span><span>;</span></span>
<span>    <span>&#125;</span></span>


<span>    <span style="color:#888888">/**</span></span>
<span><span style="color:#888888">     * 调用sql文件user.md#select,方法名即markdown片段名字</span></span>
<span><span style="color:#888888">     * @param name</span></span>
<span><span style="color:#888888">     * @return</span></span>
<span><span style="color:#888888">     */</span></span>
<span>     <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <strong style="color:#990000">select</strong><span>(</span><strong style="color:#445588">String</strong> <span>name</span><span>);</span></span>


<span>    <span style="color:#888888">/**</span></span>
<span><span style="color:#888888">     * 翻页查询,调用user.md#pageQuery</span></span>
<span><span style="color:#888888">     * @param deptId</span></span>
<span><span style="color:#888888">     * @param pageRequest</span></span>
<span><span style="color:#888888">     * @return</span></span>
<span><span style="color:#888888">     */</span></span>
<span>    <strong style="color:#445588">PageResult</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span>  <strong style="color:#990000">pageQuery</strong><span>(</span><strong style="color:#445588">Integer</strong> <span>deptId</span><span>,</span> <strong style="color:#445588">PageRequest</strong> <span>pageRequest</span><span>);</span></span>
<span></span>
<span>    <span>@SqlProvider</span><span>(</span><span>provider</span><span>=</span> <strong style="color:#445588">S01MapperSelectSample</strong><span>.</span><span style="color:#008080">SelectUserProvider</span><span>.</span><span style="color:#008080">class</span><span>)</span></span>
<span>    <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <strong style="color:#990000">queryUserByCondition</strong><span>(</span><strong style="color:#445588">String</strong> <span>name</span><span>);</span></span>

<span>    <span>@SqlTemplateProvider</span><span>(</span><span>provider</span><span>=</span> <strong style="color:#445588">S01MapperSelectSample</strong><span>.</span><span style="color:#008080">SelectUs</span></span>
<span>    <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <strong style="color:#990000">queryUserByTemplateCondition</strong><span>(</span><strong style="color:#445588">String</strong> <span>name</span><span>);</span></span>

<span>    <span>@Matcher</span> <span style="color:#888888">/*自己定义个Matcher注解也很容易*/</span></span>
<span>    <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserEntity</strong><span>></span> <strong style="color:#990000">query</strong><span>(</span><strong style="color:#445588">Condition</strong> <span>condition</span><span>,</span><strong style="color:#445588">String</strong> <span>name</span><span>);</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">你看到的这些用在Mapper上注解都是可以自定义，自己扩展的</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">例子8 使用Fetch 注解</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">可以在查询后根据Fetch注解再次获取相关对象，实际上@FetchOne和 @FetchMany是自定义的，用户可自行扩展</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>    <span>@Data</span></span>
<span>    <span>@Table</span><span>(</span><span>name</span><span>=</span><span style="color:#dd2200">"user"</span><span>)</span></span>
<span>    <span>@Fetch</span></span>
<span>    <strong>public</strong> <strong>static</strong> <strong>class</strong> <strong style="color:#445588">UserData</strong> <span>&#123;</span></span>
<span>        <span>@Auto</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>id</span><span>;</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">String</strong> <span>name</span><span>;</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>departmentId</span><span>;</span></span>
<span>        <span>@FetchOne</span><span>(</span><span style="color:#dd2200">"departmentId"</span><span>)</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">DepartmentData</strong> <span>dept</span><span>;</span></span>
<span>    <span>&#125;</span></span>

<span>    <span style="color:#888888">/**</span></span>
<span><span style="color:#888888">     * 部门数据使用"b" sqlmanager</span></span>
<span><span style="color:#888888">     */</span></span>
<span>    <span>@Data</span></span>
<span>    <span>@Table</span><span>(</span><span>name</span><span>=</span><span style="color:#dd2200">"department"</span><span>)</span></span>
<span>    <span>@Fetch</span></span>
<span>    <strong>public</strong> <strong>static</strong> <strong>class</strong> <strong style="color:#445588">DepartmentData</strong> <span>&#123;</span></span>
<span>        <span>@Auto</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>id</span><span>;</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">String</strong> <span>name</span><span>;</span></span>
<span>        <span>@FetchMany</span><span>(</span><span style="color:#dd2200">"departmentId"</span><span>)</span></span>
<span>        <strong>private</strong> <strong style="color:#445588">List</strong><span><</span><strong style="color:#445588">UserData</strong><span>></span> <span>users</span><span>;</span></span>
<span>    <span>&#125;</span></span>

</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            