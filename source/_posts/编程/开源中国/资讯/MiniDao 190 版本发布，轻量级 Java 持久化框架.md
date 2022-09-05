
---
title: 'MiniDao 1.9.0 版本发布，轻量级 Java 持久化框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-38c90069d92c5d417865d852c53fc44d814.png'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 03:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-38c90069d92c5d417865d852c53fc44d814.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">MiniDao 是一款轻量级 JAVA 持久层框架，基于 SpringJdbc + freemarker 实现，具备 Mybatis 一样的 SQL 分离和逻辑标签能力。Minidao 产生的初衷是为了解决 Hibernate 项目，在复杂 SQL 具备 Mybatis 一样的灵活能力，同时支持事务同步。</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.9.0 | 2022-09-02</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FMiniDao" target="_blank">https://github.com/zhangdaiscott/MiniDao</a></li> 
 <li> <a href="https://gitee.com/jeecg/minidao">https://gitee.com/jeecg/minidao</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>升级依赖版本号与 jeecgboot 版本号一致，重点升级 jsqlparser 重构了不兼容方法</li> 
 <li>升级 springframework 依赖到 5.3.18 ，与 jeecgboot 同步</li> 
 <li>升级 spring-boot-starter 依赖到 2.6.6 ，与 jeecgboot 同步</li> 
 <li>升级 javassist 依赖到 3.25.0-GA</li> 
 <li>升级 jsqlparser 依赖到 4.3</li> 
 <li>升级 ognl 版本号解决报错问题</li> 
 <li>不支持 SqlServer 分页问题</li> 
 <li>支持用户自定义数据源</li> 
 <li>SqlServer2012 (derby 用到)、PostgreSql、神通、Hsql、mysql 分页优化，有分页关键词就用 select 包裹起来</li> 
 <li>反射打破方法没必要写，去掉 fields [j].setAccessible (true)</li> 
 <li>SQL Server 表名关键字查询失败</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术文档</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>技术官网：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>技术文档：<span> </span><a href="https://minidao.mydoc.io/">https://minidao.mydoc.io</a></li> 
 <li><a href="https://minidao.mydoc.io/?t=336070">如何快速集成 minidao</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">MiniDao 特征</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">An powerful enhanced toolkit of SpringJdbc for simplify development</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具有以下特征:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>O/R mapping 不用设置 xml，零配置便于维护</li> 
 <li>不需要了解 JDBC 的知识</li> 
 <li>SQL 语句和 java 代码的分离</li> 
 <li>只需接口定义，无需接口实现</li> 
 <li>SQL 支持脚本语言（强大脚本语言，freemarker 语法）</li> 
 <li>支持与 hibernate 轻量级无缝集成</li> 
 <li>支持自动事务处理和手动事务处理</li> 
 <li>性能优于 Mybatis</li> 
 <li>比 Mybatis 更简单易用</li> 
 <li>SQL 支持注解方式</li> 
 <li>SQL 支持独立文件方式，SQL 文件的命名规则：类名_方法名；SQL 文件更容易定位，方便后期维护，项目越大此优势越明显</li> 
 <li>SQL 标签采用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fblog.csdn.net%2Fzhangdaiscott%2Farticle%2Fdetails%2F77505453" target="_blank">Freemarker 的基本语法</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">代码体验</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left">1. 接口定义 [EmployeeDao.java]</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#6a737d">@MiniDao</span>
<span style="color:#d73a49">public</span> <span><span style="color:#d73a49">interface</span> <span style="color:#6f42c1">EmployeeDao</span> </span>&#123;

 <span style="color:#6a737d">@Arguments(&#123; <span>"employee"</span>&#125;)</span>
 <span style="color:#6a737d">@Sql(<span>"select * from employee"</span>)</span>
 List<Map<String,Object>> getAll(Employee employee);

 <span style="color:#6a737d">@Sql(<span>"select * from employee where id = :id"</span>)</span>
 Employee <span style="color:#d73a49">get</span>(<span style="color:#6a737d">@Param(<span>"id"</span>)</span> String id);

 <span style="color:#6a737d">@Sql(<span>"select * from employee where empno = :empno and  name = :name"</span>)</span>
 Map getMap(<span style="color:#6a737d">@Param(<span>"empno"</span>)</span>String empno,<span style="color:#6a737d">@Param(<span>"name"</span>)</span>String name);

 <span style="color:#6a737d">@Sql(<span>"SELECT count(*) FROM employee"</span>)</span>
 Integer getCount();

 int update(<span style="color:#6a737d">@Param(<span>"employee"</span>)</span> Employee employee);

 void insert(<span style="color:#6a737d">@Param(<span>"employee"</span>)</span> Employee employee);
 
 <span style="color:#6a737d">@ResultType(Employee.class)</span>
 <span style="color:#d73a49">public</span> MiniDaoPage<Employee> getAll(<span style="color:#6a737d">@Param(<span>"employee"</span>)</span> Employee employee,<span style="color:#6a737d">@Param(<span>"page"</span>)</span>  int page,<span style="color:#6a737d">@Param(<span>"rows"</span>)</span> int rows);
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">&#125;</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">2. SQL 文件 [EmployeeDao_getAllEmployees.sql]</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">SELECT</span> * <span style="color:#d73a49">FROM</span> employee <span style="color:#d73a49">where</span> <span>1</span>=<span>1</span> 
<<span style="color:#6a737d">#if employee.age ?exists></span>
<span style="color:#d73a49">and</span> age = :employee.age
</<span style="color:#6a737d">#if></span>
<<span style="color:#6a737d">#if employee.name ?exists></span>
<span style="color:#d73a49">and</span> <span style="color:#d73a49">name</span> = :employee.name
</<span style="color:#6a737d">#if></span>
<<span style="color:#6a737d">#if employee.empno ?exists></span>
<span style="color:#d73a49">and</span> empno = :employee.empno
</<span style="color:#6a737d">#if></span>
</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:left">3. 接口和 SQL 文件对应目录</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-38c90069d92c5d417865d852c53fc44d814.png" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">4. 测试代码</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> Client &#123;
<span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span>void</span> main(<span>String</span> args[]) &#123;
BeanFactory factory = <span style="color:#d73a49">new</span> ClassPathXmlApplicationContext(<span style="color:#032f62">"applicationContext.xml"</span>);
EmployeeDao employeeDao = (EmployeeDao) factory.getBean(<span style="color:#032f62">"employeeDao"</span>);
Employee employee = <span style="color:#d73a49">new</span> Employee();
<span>String</span> id = UUID.randomUUID().toString().replaceAll(<span style="color:#032f62">"-"</span>, <span style="color:#032f62">""</span>).toUpperCase();
employee.setId(id);
employee.setEmpno(<span style="color:#032f62">"A001"</span>);
employee.setSalary(<span style="color:#d73a49">new</span> BigDecimal(<span>5000</span>));
employee.setBirthday(<span style="color:#d73a49">new</span> <span>Date</span>());
employee.setName(<span style="color:#032f62">"scott"</span>);
employee.setAge(<span>25</span>);
<span style="color:#6a737d">//调用minidao方法插入</span>
employeeDao.insert(employee);
&#125;
&#125;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            