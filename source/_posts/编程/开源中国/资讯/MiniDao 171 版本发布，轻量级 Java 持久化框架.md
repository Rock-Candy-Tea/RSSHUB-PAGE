
---
title: 'MiniDao 1.7.1 版本发布，轻量级 Java 持久化框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-38c90069d92c5d417865d852c53fc44d814.png'
author: 开源中国
comments: false
date: Mon, 29 Mar 2021 10:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-38c90069d92c5d417865d852c53fc44d814.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:left">项目介绍</h3> 
<blockquote> 
 <p>MiniDao 是一款轻量级JAVA持久层框架，基于 SpringJdbc + freemarker 实现，具备Mybatis一样的SQL分离和逻辑标签能力。Minidao产生的初衷是为了解决Hibernate项目，在复杂SQL具备Mybatis一样的灵活能力，同时支持事务同步。</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v1.7.1 | 2021-03-29</p> 
<h3 style="text-align:left">源码下载</h3> 
<ul> 
 <li> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FMiniDao" target="_blank">https://github.com/zhangdaiscott/MiniDao</a></li> 
 <li> <a href="https://gitee.com/jeecg/minidao">https://gitee.com/jeecg/minidao</a></li> 
</ul> 
<h3 style="text-align:left">升级日志</h3> 
<ul> 
 <li>升级spring版本到5.2.10.RELEASE</li> 
 <li>升级freemarker版本到2.3.30</li> 
 <li>提供代码生成器工具，快速生成dao和sql</li> 
 <li>增加非持久化字段标记注解</li> 
 <li>增加雪花分布式ID生成工具类</li> 
 <li>提供springboot2快速集成starter</li> 
</ul> 
<h3 style="text-align:left">技术文档</h3> 
<ul> 
 <li>技术官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>技术文档： <a href="https://minidao.mydoc.io/">https://minidao.mydoc.io</a></li> 
 <li><a href="https://minidao.mydoc.io/?t=336070">如何快速集成minidao</a></li> 
</ul> 
<h3 style="text-align:left">MiniDao特征</h3> 
<blockquote> 
 <p>An powerful enhanced toolkit of SpringJdbc for simplify development</p> 
</blockquote> 
<p style="text-align:left">具有以下特征:</p> 
<ul> 
 <li>O/R mapping不用设置xml，零配置便于维护</li> 
 <li>不需要了解JDBC的知识</li> 
 <li>SQL语句和java代码的分离</li> 
 <li>只需接口定义，无需接口实现</li> 
 <li>SQL支持脚本语言（强大脚本语言，freemarker语法）</li> 
 <li>支持与hibernate轻量级无缝集成</li> 
 <li>支持自动事务处理和手动事务处理</li> 
 <li>性能优于Mybatis</li> 
 <li>比Mybatis更简单易用</li> 
 <li>SQL 支持注解方式</li> 
 <li>SQL 支持独立文件方式，SQL文件的命名规则: 类名_方法名; SQL文件更容易定位，方便后期维护，项目越大此优势越明显</li> 
 <li>SQL标签采用<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fblog.csdn.net%2Fzhangdaiscott%2Farticle%2Fdetails%2F77505453" target="_blank">Freemarker的基本语法</a></li> 
</ul> 
<h2 style="text-align:left">代码体验</h2> 
<h4 style="text-align:left">1. 接口定义[EmployeeDao.java]</h4> 
<pre style="text-align:left"><code><span style="color:#6a737d">@MiniDao</span>
<span style="color:#d73a49">public</span> <span style="color:#d73a49">interface</span> <span style="color:#6f42c1">EmployeeDao</span> &#123;

 <span style="color:#6a737d">@Arguments(&#123; "employee"&#125;)</span>
 <span style="color:#6a737d">@Sql("select * from employee")</span>
 List<Map<String,Object>> getAll(Employee employee);

 <span style="color:#6a737d">@Sql("select * from employee where id = :id")</span>
 Employee <span style="color:#d73a49">get</span>(<span style="color:#6a737d">@Param("id")</span> String id);

 <span style="color:#6a737d">@Sql("select * from employee where empno = :empno and  name = :name")</span>
 Map getMap(<span style="color:#6a737d">@Param("empno")</span>String empno,<span style="color:#6a737d">@Param("name")</span>String name);

 <span style="color:#6a737d">@Sql("SELECT count(*) FROM employee")</span>
 Integer getCount();

 int update(<span style="color:#6a737d">@Param("employee")</span> Employee employee);

 void insert(<span style="color:#6a737d">@Param("employee")</span> Employee employee);
 
 <span style="color:#6a737d">@ResultType(Employee.class)</span>
 <span style="color:#d73a49">public</span> MiniDaoPage<Employee> getAll(<span style="color:#6a737d">@Param("employee")</span> Employee employee,<span style="color:#6a737d">@Param("page")</span>  int page,<span style="color:#6a737d">@Param("rows")</span> int rows);
</code></pre> 
<p style="text-align:left">&#125;</p> 
<h4 style="text-align:left">2. SQL文件[EmployeeDao_getAllEmployees.sql]</h4> 
<pre style="text-align:left"><code><span style="color:#d73a49">SELECT</span> * <span style="color:#d73a49">FROM</span> employee <span style="color:#d73a49">where</span> 1=1 
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
<h4 style="text-align:left">3. 接口和SQL文件对应目录</h4> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-38c90069d92c5d417865d852c53fc44d814.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">4. 测试代码</h4> 
<pre style="text-align:left"><code><span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> Client &#123;
<span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> void main(String args[]) &#123;
BeanFactory factory = <span style="color:#d73a49">new</span> ClassPathXmlApplicationContext(<span style="color:#032f62">"applicationContext.xml"</span>);
EmployeeDao employeeDao = (EmployeeDao) factory.getBean(<span style="color:#032f62">"employeeDao"</span>);
Employee employee = <span style="color:#d73a49">new</span> Employee();
String id = UUID.randomUUID().toString().replaceAll(<span style="color:#032f62">"-"</span>, <span style="color:#032f62">""</span>).toUpperCase();
employee.setId(id);
employee.setEmpno(<span style="color:#032f62">"A001"</span>);
employee.setSalary(<span style="color:#d73a49">new</span> BigDecimal(5000));
employee.setBirthday(<span style="color:#d73a49">new</span> Date());
employee.setName(<span style="color:#032f62">"scott"</span>);
employee.setAge(25);
<span style="color:#6a737d">//调用minidao方法插入</span>
employeeDao.insert(employee);
&#125;
&#125;</code></pre>
                                        </div>
                                      
</div>
            