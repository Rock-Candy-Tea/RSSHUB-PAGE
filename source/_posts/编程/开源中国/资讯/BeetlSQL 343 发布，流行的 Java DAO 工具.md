
---
title: 'BeetlSQL 3.4.3 发布，流行的 Java DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 05:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                                            <ul> 
 <li>SQLManagerBuilder增加了接口配置主键生成器，代替直接使用SQLManagaer指定的方式</li> 
 <li>删除了之前SpringBoot集成版本对Swagger的依赖。</li> 
 <li>轻量级高速Web框架Solon框架集成更新到最新版</li> 
</ul> 
<p style="text-align:left">Maven</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>com.ibeetl<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>beetlsql<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>3.4.3-RELEASE<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
<p style="text-align:left">BeetlSQL 研发自2015年，目标是提供开发高效，维护高效，运行高效的数据库访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑,不亚于MyBatis. 你不想写SQL也好，或者想更好的些SQL也好，BeetlSQL都能满足这要求，目前支持的数据库如下</p> 
<ul> 
 <li>传统数据库：MySQL,MariaDB,Oralce,Postgres,DB2,SQL Server，H2,SQLite,Derby，神通，达梦，华为高斯，人大金仓，PolarDB 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎:Drill,Presto，Druid</li> 
 <li>内存数据库:ignite，CouchBase</li> 
</ul> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"> </span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a></p> 
<p style="text-align:left">BeetlSQL也支持IDEA插件，提供向导和自动提示</p> 
<p style="text-align:left"><img alt height="288" src="https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png" width="600" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">代码示例</h2> 
<h3 style="text-align:left">例子1,内置方法，无需写SQL完成常用操作</h3> 
<pre style="text-align:left"><code class="language-java">UserEntity user  = sqlManager.unique(UserEntity.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>,1);

user.setName(<span style="color:#032f62"><span style="color:#032f62">"ok123"</span></span>);
sqlManager.updateById(user);

UserEntity newUser = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> UserEntity();
newUser.setName(<span style="color:#032f62"><span style="color:#032f62">"newUser"</span></span>);
newUser.setDepartmentId(1);
sqlManager.insert(newUser);

</code></pre> 
<p style="text-align:left">输出日志友好,可反向定位到调用的代码</p> 
<pre style="text-align:left"><code>┏━━━━━ Debug [user.selectUserAndDepartment] ━━━
┣ SQL：     <span style="color:#d73a49"><span style="color:#d73a49">select</span></span> * <span style="color:#d73a49"><span style="color:#d73a49">from</span></span> <span style="color:#d73a49"><span style="color:#d73a49">user</span></span> <span style="color:#d73a49"><span style="color:#d73a49">where</span></span> 1 = 1 <span style="color:#d73a49"><span style="color:#d73a49">and</span></span> <span style="color:#d73a49"><span style="color:#d73a49">id</span></span>=?
┣ 参数：     [1]
┣ 位置：     org.beetl.sql.test.QuickTest.main(QuickTest.java:47)
┣ 时间：     23ms
┣ 结果：     [1]
┗━━━━━ Debug [user.selectUserAndDepartment] ━━━
</code></pre> 
<h3 style="text-align:left">例子2 使用SQL</h3> 
<pre style="text-align:left"><code class="language-java">String sql = <span style="color:#032f62"><span style="color:#032f62">"select * from user where id=?"</span></span>;
Integer id  = 1;
SQLReady sqlReady = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> SQLReady(sql,<span style="color:#d73a49"><span style="color:#d73a49">new</span></span> Object[id]);
List<UserEntity> userEntities = sqlManager.execute(sqlReady,UserEntity.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>);
<span style="color:#6a737d"><span style="color:#6a737d">//Map 也可以作为输入输出参数</span></span>
List<Map> listMap =  sqlManager.execute(sqlReady,Map.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>);
</code></pre> 
<h3 style="text-align:left">例子3 使用模板SQL</h3> 
<pre style="text-align:left"><code class="language-java">String sql = <span style="color:#032f62"><span style="color:#032f62">"select * from user where department_id=#&#123;id&#125; and name=#&#123;name&#125;"</span></span>;
UserEntity paras = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> UserEntity();
paras.setDepartmentId(1);
paras.setName(<span style="color:#032f62"><span style="color:#032f62">"lijz"</span></span>);
List<UserEntity> list = sqlManager.execute(sql,UserEntity.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>,<span style="color:#6f42c1"><span style="color:#6f42c1">paras</span></span>);

String sql = <span style="color:#032f62"><span style="color:#032f62">"select * from user where id in ( #&#123;join(ids)&#125; )"</span></span>;
List list = Arrays.asList(1,2,3,4,5); Map paras = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> HashMap();
paras.put(<span style="color:#032f62"><span style="color:#032f62">"ids"</span></span>, list);
List<UserEntity> users = sqlManager.execute(sql, UserEntity.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>, <span style="color:#6f42c1"><span style="color:#6f42c1">paras</span></span>);
</code></pre> 
<h3 style="text-align:left">例子4 使用Query类</h3> 
<p style="text-align:left">支持重构</p> 
<pre style="text-align:left"><code class="language-java">LambdaQuery<UserEntity> query = sqlManager.lambdaQuery(UserEntity.class);
List<UserEntity> entities = query.andE<span style="color:#032f62"><span style="color:#032f62">q(UserEntity::getDepartmentId,1)</span></span>
                    .andIsNotNull(UserEntity::getName).select();

</code></pre> 
<h3 style="text-align:left">例子5 把数十行SQL放到sql文件里维护</h3> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d">//访问user.md#select</span></span>
SqlId id = SqlId.of(<span style="color:#032f62"><span style="color:#032f62">"user"</span></span>,<span style="color:#032f62"><span style="color:#032f62">"select"</span></span>);
Map <span style="color:#d73a49"><span style="color:#d73a49">map</span></span> = new HashMap();
<span style="color:#d73a49"><span style="color:#d73a49">map</span></span>.put(<span style="color:#032f62"><span style="color:#032f62">"name"</span></span>,<span style="color:#032f62"><span style="color:#032f62">"n"</span></span>);
List<UserEntity> list = sqlManager.<span style="color:#d73a49"><span style="color:#d73a49">select</span></span>(id,UserEntity.class,<span style="color:#d73a49"><span style="color:#d73a49">map</span></span>);
</code></pre> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5f89c4abc4b0b777ff342b109c162b7298c.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">例子6 复杂映射支持</h3> 
<p style="text-align:left">支持像mybatis那样复杂的映射</p> 
<ul> 
 <li>自动映射</li> 
</ul> 
<pre style="text-align:left"><code class="language-java"><span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@ResultProvider</span></span>(AutoJsonMapper.class)
 public static class MyUserView &#123;
        <span style="color:#d73a49"><span style="color:#d73a49">Integer</span></span> <span style="color:#d73a49"><span style="color:#d73a49">id</span></span>;
        <span style="color:#d73a49"><span style="color:#d73a49">String</span></span> <span style="color:#d73a49"><span style="color:#d73a49">name</span></span>;
        <span style="color:#d73a49"><span style="color:#d73a49">DepartmentEntity</span></span> <span style="color:#d73a49"><span style="color:#d73a49">dept</span></span>;
 &#125;

</code></pre> 
<ul> 
 <li>配置映射，比MyBatis更容易理解，报错信息更详细</li> 
</ul> 
<pre style="text-align:left"><code class="language-json">&#123;
<span style="color:#6f42c1"><span style="color:#6f42c1">"id"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"id"</span></span>,
<span style="color:#6f42c1"><span style="color:#6f42c1">"name"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"name"</span></span>,
<span style="color:#6f42c1"><span style="color:#6f42c1">"dept"</span></span>: &#123;
<span style="color:#6f42c1"><span style="color:#6f42c1">"id"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"dept_id"</span></span>,
<span style="color:#6f42c1"><span style="color:#6f42c1">"name"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"dept_name"</span></span>
&#125;,
<span style="color:#6f42c1"><span style="color:#6f42c1">"roles"</span></span>: &#123;
<span style="color:#6f42c1"><span style="color:#6f42c1">"id"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"r_id"</span></span>,
<span style="color:#6f42c1"><span style="color:#6f42c1">"name"</span></span>: <span style="color:#032f62"><span style="color:#032f62">"r_name"</span></span>
&#125;
&#125;
</code></pre> 
<h3 style="text-align:left">例子7 最好使用mapper来作为数据库访问类</h3> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d">@SqlResource</span></span>(<span style="color:#032f62"><span style="color:#032f62">"user"</span></span>) <span style="color:#6a737d"><span style="color:#6a737d">/*sql文件在user.md里*/</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#d73a49"><span style="color:#d73a49">interface</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">UserMapper</span></span> <span style="color:#d73a49"><span style="color:#d73a49">extends</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">BaseMapper</span></span><<span style="color:#6f42c1"><span style="color:#6f42c1">UserEntity</span></span>> &#123;

    <span style="color:#6a737d"><span style="color:#6a737d">@Sql</span></span>(<span style="color:#032f62"><span style="color:#032f62">"select * from user where id = ?"</span></span>)
    UserEntity <span style="color:#6f42c1"><span style="color:#6f42c1">queryUserById</span></span>(Integer id);

    <span style="color:#6a737d"><span style="color:#6a737d">@Sql</span></span>(<span style="color:#032f62"><span style="color:#032f62">"update user set name=? where id = ?"</span></span>)
    <span style="color:#6a737d"><span style="color:#6a737d">@Update</span></span>
    <span style="color:#d73a49"><span style="color:#d73a49">int</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">updateName</span></span>(String name,Integer id);

    <span style="color:#6a737d"><span style="color:#6a737d">@Template</span></span>(<span style="color:#032f62"><span style="color:#032f62">"select * from user where id = #&#123;id&#125;"</span></span>)
    UserEntity <span style="color:#6f42c1"><span style="color:#6f42c1">getUserById</span></span>(Integer id);

    <span style="color:#6a737d"><span style="color:#6a737d">@SpringData</span></span><span style="color:#6a737d"><span style="color:#6a737d">/*Spring Data风格*/</span></span>
    List<UserEntity> <span style="color:#6f42c1"><span style="color:#6f42c1">queryByNameOrderById</span></span>(String name);

    <span style="color:#6a737d"><span style="color:#6a737d">/**
     * 可以定义一个default接口
     * @return
     */</span></span>
     <span style="color:#d73a49"><span style="color:#d73a49">default</span></span>  List<DepartmentEntity> <span style="color:#6f42c1"><span style="color:#6f42c1">findAllDepartment</span></span>()&#123;
        Map paras = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> HashMap();
        paras.put(<span style="color:#032f62"><span style="color:#032f62">"exlcudeId"</span></span>,1);
        List<DepartmentEntity> list = getSQLManager().execute(<span style="color:#032f62"><span style="color:#032f62">"select * from department where id != #&#123;exlcudeId&#125;"</span></span>,DepartmentEntity.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>,<span style="color:#6f42c1"><span style="color:#6f42c1">paras</span></span>);
        <span style="color:#d73a49"><span style="color:#d73a49">return</span></span> list;
    &#125;


    <span style="color:#6a737d"><span style="color:#6a737d">/**
     * 调用sql文件user.md#select,方法名即markdown片段名字
     * @param name
     * @return
     */</span></span>
     List<UserEntity> <span style="color:#6f42c1"><span style="color:#6f42c1">select</span></span>(String name);


    <span style="color:#6a737d"><span style="color:#6a737d">/**
     * 翻页查询,调用user.md#pageQuery
     * @param deptId
     * @param pageRequest
     * @return
     */</span></span>
    PageResult<UserEntity>  <span style="color:#6f42c1"><span style="color:#6f42c1">pageQuery</span></span>(Integer deptId, PageRequest pageRequest);

    <span style="color:#6a737d"><span style="color:#6a737d">@SqlProvider</span></span>(provider= S01MapperSelectSample.SelectUserProvider.<span style="color:#d73a49"><span style="color:#d73a49">class</span></span>)
    <span style="color:#6f42c1"><span style="color:#6f42c1">List</span></span><<span style="color:#6f42c1"><span style="color:#6f42c1">UserEntity</span></span>> <span style="color:#6f42c1"><span style="color:#6f42c1">queryUserByCondition</span></span>(<span style="color:#6f42c1"><span style="color:#6f42c1">String</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">name</span></span>);

    <span style="color:#6a737d"><span style="color:#6a737d">@SqlTemplateProvider</span></span>(provider= S01MapperSelectSample.SelectUs
    List<UserEntity> <span style="color:#6f42c1"><span style="color:#6f42c1">queryUserByTemplateCondition</span></span>(String name);

    <span style="color:#6a737d"><span style="color:#6a737d">@Matcher</span></span> <span style="color:#6a737d"><span style="color:#6a737d">/*自己定义个Matcher注解也很容易*/</span></span>
    List<UserEntity> <span style="color:#6f42c1"><span style="color:#6f42c1">query</span></span>(Condition condition,String name);
&#125;
</code></pre> 
<blockquote> 
 <p>你看到的这些用在Mapper上注解都是可以自定义，自己扩展的</p> 
</blockquote> 
<h3 style="text-align:left">例子8 使用Fetch 注解</h3> 
<p style="text-align:left">可以在查询后根据Fetch注解再次获取相关对象，实际上@FetchOne和 @FetchMany是自定义的，用户可自行扩展</p> 
<pre style="text-align:left"><code class="language-java">    <span style="color:#6a737d"><span style="color:#6a737d">@Data</span></span>
    <span style="color:#6a737d"><span style="color:#6a737d">@Table(name="user")</span></span>
    <span style="color:#6a737d"><span style="color:#6a737d">@Fetch</span></span>
    <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> static <span style="color:#d73a49"><span style="color:#d73a49">class</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">UserData</span></span> &#123;
        <span style="color:#6a737d"><span style="color:#6a737d">@Auto</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> Integer id;
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> String name;
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> Integer departmentId;
        <span style="color:#6a737d"><span style="color:#6a737d">@FetchOne("departmentId")</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> DepartmentData dept;
    &#125;

    <span style="color:#6a737d"><span style="color:#6a737d">/**
     * 部门数据使用"b" sqlmanager
     */</span></span>
    <span style="color:#6a737d"><span style="color:#6a737d">@Data</span></span>
    <span style="color:#6a737d"><span style="color:#6a737d">@Table(name="department")</span></span>
    <span style="color:#6a737d"><span style="color:#6a737d">@Fetch</span></span>
    <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> static <span style="color:#d73a49"><span style="color:#d73a49">class</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">DepartmentData</span></span> &#123;
        <span style="color:#6a737d"><span style="color:#6a737d">@Auto</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> Integer id;
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> String name;
        <span style="color:#6a737d"><span style="color:#6a737d">@FetchMany("departmentId")</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> List<UserData> users;
    &#125;

</code></pre> 
<h3 style="text-align:left">例子9 不同数据库切换</h3> 
<p style="text-align:left">可以自行扩展ConditionalSQLManager的decide方法，来决定使用哪个SQLManager</p> 
<pre style="text-align:left"><code class="language-java">        SQLManager a = SampleHelper.init();
        SQLManager b = SampleHelper.init();
        Map<String, SQLManager> <span style="color:#d73a49"><span style="color:#d73a49">map</span></span> = new HashMap<>();
        <span style="color:#d73a49"><span style="color:#d73a49">map</span></span>.put(<span style="color:#032f62"><span style="color:#032f62">"a"</span></span>, a);
        <span style="color:#d73a49"><span style="color:#d73a49">map</span></span>.put(<span style="color:#032f62"><span style="color:#032f62">"b"</span></span>, b);
        SQLManager sqlManager = new ConditionalSQLManager(a, <span style="color:#d73a49"><span style="color:#d73a49">map</span></span>);

        <span style="color:#6a737d"><span style="color:#6a737d">//不同对象，用不同sqlManager操作，存入不同的数据库</span></span>
        UserData user = new UserData();
        user.setName(<span style="color:#032f62"><span style="color:#032f62">"hello"</span></span>);
        user.setDepartmentId(2);
        sqlManager.insert(user);

        DepartmentData dept = new DepartmentData();
        dept.setName(<span style="color:#032f62"><span style="color:#032f62">"dept"</span></span>);
        sqlManager.insert(dept);

</code></pre> 
<p style="text-align:left">使用注解 @TargetSQLManager来决定使用哪个SQLManger</p> 
<pre style="text-align:left"><code class="language-java">    <span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@Table</span></span>(name = <span style="color:#032f62"><span style="color:#032f62">"department"</span></span>)
    <span style="color:#032f62"><span style="color:#032f62">@TargetSQLManager</span></span>(<span style="color:#032f62"><span style="color:#032f62">"b"</span></span>)
    public static class DepartmentData &#123;
        <span style="color:#032f62"><span style="color:#032f62">@Auto</span></span>
        private Integer id;
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> <span style="color:#d73a49"><span style="color:#d73a49">String</span></span> <span style="color:#d73a49"><span style="color:#d73a49">name</span></span>;
    &#125;
</code></pre> 
<h3 style="text-align:left">例子10 如果想给每个sql语句增加一个sqlId标识</h3> 
<p style="text-align:left">这样好处是方便数据库DBA与程序员沟通</p> 
<pre style="text-align:left"><code class="language-java"> <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#d73a49"><span style="color:#d73a49">static</span></span> <span style="color:#d73a49"><span style="color:#d73a49">class</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">SqlIdAppendInterceptor</span></span> <span style="color:#d73a49"><span style="color:#d73a49">implements</span></span>  <span style="color:#6f42c1"><span style="color:#6f42c1">Interceptor</span></span>&#123;
        <span style="color:#6a737d"><span style="color:#6a737d">@Override</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#d73a49"><span style="color:#d73a49">void</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">before</span></span>(InterceptorContext ctx) &#123;
            ExecuteContext context = ctx.getExecuteContext();
            String jdbcSql = context.sqlResult.jdbcSql;
            String info  = context.sqlId.toString();
            <span style="color:#6a737d"><span style="color:#6a737d">//为发送到数据库的sql增加一个注释说明，方便数据库dba能与开发人员沟通</span></span>
            jdbcSql = <span style="color:#032f62"><span style="color:#032f62">"/*"</span></span>+info+<span style="color:#032f62"><span style="color:#032f62">"*/\n"</span></span>+jdbcSql;
            context.sqlResult.jdbcSql = jdbcSql;
        &#125;
 &#125;
</code></pre> 
<h3 style="text-align:left">例子11 代码生成框架</h3> 
<p style="text-align:left">可以使用内置的代码生成框架生成代码何文档，也可以自定义的，用户可自行扩展SourceBuilder类</p> 
<pre style="text-align:left"><code class="language-java">List<SourceBuilder> sourceBuilder = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> ArrayList<>();
SourceBuilder entityBuilder = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> EntitySourceBuilder();
SourceBuilder mapperBuilder = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> MapperSourceBuilder();
SourceBuilder mdBuilder = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> MDSourceBuilder();
<span style="color:#6a737d"><span style="color:#6a737d">//数据库markdown文档</span></span>
SourceBuilder docBuilder = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> MDDocBuilder();

sourceBuilder.<span style="color:#d73a49"><span style="color:#d73a49">add</span></span>(entityBuilder);
sourceBuilder.<span style="color:#d73a49"><span style="color:#d73a49">add</span></span>(mapperBuilder);
sourceBuilder.<span style="color:#d73a49"><span style="color:#d73a49">add</span></span>(mdBuilder);
sourceBuilder.<span style="color:#d73a49"><span style="color:#d73a49">add</span></span>(docBuilder);
    SourceConfig config = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> SourceConfig(sqlManager,sourceBuilder);
   <span style="color:#6a737d"><span style="color:#6a737d">//只输出到控制台</span></span>
ConsoleOnlyProject project = <span style="color:#d73a49"><span style="color:#d73a49">new</span></span> ConsoleOnlyProject();
String tableName = <span style="color:#032f62"><span style="color:#032f62">"USER"</span></span>;
config.gen(tableName,project);
</code></pre> 
<h3 style="text-align:left">例子13 定义一个Beetl函数</h3> 
<pre style="text-align:left"><code class="language-java">        GroupTemplate groupTemplate = groupTemplate();
        groupTemplate.registerFunction("nextDay",new NextDayFunction());

        Map map = new HashMap();
        map.put("date",new Date());
        String sql = "<span style="color:#d73a49"><span style="color:#d73a49">select</span></span> * <span style="color:#d73a49"><span style="color:#d73a49">from</span></span> <span style="color:#d73a49"><span style="color:#d73a49">user</span></span> <span style="color:#d73a49"><span style="color:#d73a49">where</span></span> create_time <span style="color:#d73a49"><span style="color:#d73a49">is</span></span> <span style="color:#d73a49"><span style="color:#d73a49">not</span></span> <span style="color:#005cc5"><span style="color:#005cc5">null</span></span> <span style="color:#d73a49"><span style="color:#d73a49">and</span></span> create_time<<span style="color:#6a737d"><span style="color:#6a737d">#&#123;nextDay(date)&#125;";</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">List</span></span><UserEntity> <span style="color:#d73a49"><span style="color:#d73a49">count</span></span> = sqlManager.execute(<span style="color:#d73a49"><span style="color:#d73a49">sql</span></span>,UserEntity.class,<span style="color:#d73a49"><span style="color:#d73a49">map</span></span>);
</code></pre> 
<p style="text-align:left">nextDay函数是一个Beetl函数，非常容易定义,非常容易在sql模板语句里使用</p> 
<pre style="text-align:left"><code class="language-java">   <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#d73a49"><span style="color:#d73a49">static</span></span> <span style="color:#d73a49"><span style="color:#d73a49">class</span></span> NextDayFunction <span style="color:#d73a49"><span style="color:#d73a49">implements</span></span> Function &#123;

        <span style="color:#6a737d"><span style="color:#6a737d">@Override</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> Object call(Object[] paras, Context ctx) &#123;
            Date date = (Date) paras[0];
            Calendar c = Calendar.getInstance();
            c.setTime(date);
            c.add(Calendar.DAY_OF_YEAR, 1); <span style="color:#6a737d"><span style="color:#6a737d">// 今天+1天</span></span>
            <span style="color:#d73a49"><span style="color:#d73a49">return</span></span> c.getTime();
        &#125;
    &#125;
</code></pre> 
<h3 style="text-align:left">例子14 更多可扩展的例子</h3> 
<p style="text-align:left">根据ID或者上下文自动分表，toTable是定义的一个Beetl函数，</p> 
<pre style="text-align:left"><code class="language-java">    static <span style="color:#d73a49"><span style="color:#d73a49">final</span></span> String USER_TABLE=<span style="color:#032f62"><span style="color:#032f62">"$&#123;toTable(</span><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">'user'</span></span></span><span style="color:#032f62">,id)&#125;"</span></span>;
    <span style="color:#6a737d"><span style="color:#6a737d">@Data</span></span>
    <span style="color:#6a737d"><span style="color:#6a737d">@Table(name = USER_TABLE)</span></span>
    <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> static <span style="color:#d73a49"><span style="color:#d73a49">class</span></span> <span style="color:#6f42c1"><span style="color:#6f42c1">MyUser</span></span> &#123;
        <span style="color:#6a737d"><span style="color:#6a737d">@AssignID</span></span>
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> Integer id;
        <span style="color:#d73a49"><span style="color:#d73a49">private</span></span> String name;
    &#125;
</code></pre> 
<p style="text-align:left">定义一个Jackson注解，@Builder是注解的注解，表示用Builder指示的类来解释执行，可以看到BeetlSQL的注解可扩展性就是来源于@Build注解</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#032f62"><span style="color:#032f62">@Retention</span></span>(RetentionPolicy.RUNTIME)
<span style="color:#032f62"><span style="color:#032f62">@Target</span></span>(value = &#123;ElementType.METHOD, ElementType.FIELD&#125;)
<span style="color:#032f62"><span style="color:#032f62">@Builder</span></span>(JacksonConvert.class)
public <span style="color:#032f62"><span style="color:#032f62">@interface</span></span> Jackson &#123;

&#125;
</code></pre> 
<p style="text-align:left">定义一个@Tenant 放在POJO上，BeetlSQL执行时候会给SQL添加额外参数，这里同样使用了@Build注解</p> 
<pre style="text-align:left"><code class="language-java">
<span style="color:#6a737d"><span style="color:#6a737d">/**
 * 组合注解，给相关操作添加额外的租户信息，从而实现根据租户分表或者分库
 */</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Retention</span></span>(RetentionPolicy.RUNTIM@
<span style="color:#032f62"><span style="color:#032f62">@Target</span></span>(value = &#123;ElementType.TYPE&#125;)
<span style="color:#032f62"><span style="color:#032f62">@Builder</span></span>(TenantContext.class)
public <span style="color:#032f62"><span style="color:#032f62">@interface</span></span> Tenant &#123;

&#125;
</code></pre> 
<p style="text-align:left">使用XML而不是JSON作为映射</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d">@Retention(RetentionPolicy.RUNTIME)</span></span>
<span style="color:#6a737d"><span style="color:#6a737d">@Target(value = &#123;ElementType.TYPE&#125;)</span></span>
<span style="color:#6a737d"><span style="color:#6a737d">@Builder(ProviderConfig.class)</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span style="color:#6a737d"><span style="color:#6a737d">@interface</span></span> XmlMapping &#123;
    String path() <span style="color:#d73a49"><span style="color:#d73a49">default</span></span> <span style="color:#032f62"><span style="color:#032f62">""</span></span>;
&#125;

</code></pre> 
<blockquote> 
 <p>参考源码例子 PluginAnnotationSample了解如何定义自定的注解，实际上BeetlSQL有一半的注解都是通过核心注解扩展出来的</p> 
</blockquote>
                                        </div>
                                      
</div>
            