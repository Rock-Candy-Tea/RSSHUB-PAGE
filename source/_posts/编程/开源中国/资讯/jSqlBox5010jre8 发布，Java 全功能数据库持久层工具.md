
---
title: 'jSqlBox5.0.10.jre8 发布，Java 全功能数据库持久层工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9738'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 12:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9738'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>jSqlBox，Java数据库持久层工具，</h2> 
<p>主页：<a href="https://gitee.com/drinkjava2/jsqlbox">https://gitee.com/drinkjava2/jsqlbox</a></p> 
<h2>本次更新内容是5.0.6.jre8到5.0.10.jre8版的更新汇总：</h2> 
<ol> 
 <li>在ImprovedQueryRunner类（是DbContext的基类)中添加了StatementConfiguration初始化参数，以保持与DbUtils的初始化参数一致。 </li> 
 <li>新增一个CamelHandler拦截器，当SQL中出现这个拦截器作为参数时，会将返回Map中的下划线字段名转为驼峰式字段名，如"user_name"将转变为"userName"，使用示例：<br>   listMp = DB.qryMapList("select * from user_table order by id ",  new CamelHander());</li> 
 <li>在DialectFunctionTemplate中添加registerFunction方法，用来登录自定义函数，如下面的语句为MySQL和H2数据库添加一个名为regexlike的自定义函数： <br> DialectFunctionTemplate.registerFunction("regexlike", "2=$P1 regexp $P2", "MySQL", "H2"); <br> String sql=DB.trans("select regexlike(name, 'a') from user_tb"); </li> 
 <li>方言模块添加一个通用qt函数，用于在不同数据库下使用时添加对应数据库的引用符号，如： <br> String sql = DB.trans("select qt(name) from qt(helloWorld) where qt(name) like ?"); </li> 
 <li>更新单元测试junit和HikariCP版本到最新版。 </li> 
 <li>更正IdentityGenerator在PostgreSQL中的DDL生成bug。 </li> 
 <li>jSqlBox除了可以用@Table和@Column注解对每个表和字段进行配置，从5.0.10版起，在jDialect中新增一个setGlobalNamingConversion方法，这样就可以不用每个类或属性上加注解了，目前可以有以下三种设定： <br> Dialect.setGlobalNamingConversion(NamingConversion.LOWER_CASE_UNDERSCORE); //实体表名或属性aaBb映射为aa_bb格式 <br> Dialect.setGlobalNamingConversion(NamingConversion.UPPER_CASE_UNDERSCORE); //实体表名或属性aaBb映射为AA_BB格式 <br> Dialect.setGlobalNamingConversion(NamingConversion.NONE); //实体表名或属性aaBb不作变换，这是缺省设定 <br> 当以上设定不满足使用时，可以在setGlobalNamingConversion方法中给一个自定义的NamingConversion类实例。 </li> 
 <li>添加一个@UUID注解，以方便使用，这个注解等效于@UUID32一样，表示是一个32位字符长的随机字符ID<br>   <h2>附jSqlBox主要特点介绍： <br> 配置简单，没有依赖任何第三方库</h2> <p>在pom.xml中加入以下依赖即可使用。 如果需要查看或修改源码，甚至可以直接将jSqlBox的源码拷到项目目录里就可以直接使用了。</p> 
  <div> 
   <div> 
    <pre><span><span><dependency></span></span>
<span>   <span><groupId></span>com.github.drinkjava2<span></groupId></span></span>
<span>   <span><artifactId></span>jsqlbox<span></artifactId></span>  </span>
<span>   <span><version></span>5.0.10.jre8<span></version></span> <span><!-- 或最新版 --></span></span>
<span><span></dependency></span> </span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>直接在Java里写SQL</h3> <p>jSqlBox的最大特点是直接在Java里SQL，它的整个架构都是围绕在这个基础上，这是它与其它DAO工具最大的区别。在Java里直接写SQL的最大优点是学习成本低，只要会SQL就可以立即上手使用，降低了学习难度。使用jSqlBox并不表示要使用它的全部功能，很多时候使用SQL就能处理业务，没必要引入复杂的ORM。</p> 
  <div> 
   <div> 
    <pre><span>DbContext db= new DbContext(dataSource);</span>
<span>db.exe("insert into users (", //</span>
<span>          " name ,", par("Sam"), //一个参数写一行，方便维护</span>
<span>          notNull("address,", user.getAddress()), //空值判断</span>
<span>  when(age>10, "age,", par(user.getAge())), //根据条件动态添加SQL片段</span>
<span>          " address ", par("Canada"), //</span>
<span>          ") ", valuesQuestions()); //自动根据参数个数补上 values(?,?...?)片段</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>在Java里写SQL谁都会，但是象jSqlBox这样写出花来的工具并不多，个人认为这种混写方式是最能发挥原生SQL的威力，同时也是易学性、灵活性、可护展性最好的SQL写法。</p> <h3>借助字符串常量或Q类，可以写出支持重构的SQL</h3> 
  <div> 
   <div> 
    <pre><span> QTbPriceSetting p=QTbPriceSetting.instance;</span>
<span> DB.exe("insert into ",p," (", //</span>
<span>p.id, ",", par(1200), //</span>
<span>p.price, ",", par(80), //</span>
<span>p.currency, ",", par("USD"), //</span>
<span>p.created_at, par("2019-09-17 04:07:55"), //</span>
<span>")", valuesQuestions());</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>Q类或包含字符串常量的实体类源码，可以使用jSqlBox的源码生成功能，从数据库直接生成，另外jSqlBox也支持从实体类或数据库中导出Excel格式的数据库表结构，详见jDialect的<a href="https://gitee.com/drinkjava2/jdialects/wikis/%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C/5.4%20%E5%AE%9E%E4%BD%93%E6%88%96%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%93%E6%9E%84%E5%AF%BC%E5%87%BAExcel">实体结构或数据库结构导出到Excel</a></p> <h3>架构合理，模块式架构，各个子模块(jBeanBox,jDbPro,jDialects,jTransaction)都可以脱离jSqlBox单独存在。</h3> <p>jSqlBox是源码包含模块式架构，目的是隔离功能点，并分享给其它工具重用。例如只想使用jDialcet数据库方言模块，可以在项目的pom.xml中加入:</p> 
  <div> 
   <div> 
    <pre><span><span><dependency></span></span>
<span>    <span><groupId></span>com.github.drinkjava2<span></groupId></span></span>
<span>    <span><artifactId></span>jdialects<span></artifactId></span></span>
<span>    <span><version></span>5.0.10.jre8<span></version></span></span>
<span><span></dependency></span></span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>基于jDialects模块，支持80多种数据库的分页、DDl脚本生成、从数据库生成实体源码、函数变换、主键生成等功能。</h3> <p>例如下面的SQL语句，就可以在多种数据库上使用而不需要更改源码，jSqlBox的jDialects模块自动处理与方言相关的DDL生成、分页、函数翻译。</p> 
  <div> 
   <div> 
    <pre><span>DB.exe(DB.gctx().toCreateDDL(HelloWorld.class)); //根据实体生成DDL，创建数据库表</span>
<span>String sql=DB.trans("select concat('a','b','c'), current_time() from user_tb where age>0"); //根据方言对SQL函数翻译</span>
<span>DB.qryString(sql, " and price>100", pagin(1, 10));  //任意数据库分页只需要传入一个pagin对象</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>简洁的ActiveRecord模式</h3> <p>继承ActiveRRecord类，或只需要声明实现ActiveEntity接口(Java8以上)，就可以实现ActiveRecord模式了：</p> 
  <div> 
   <div> 
    <pre><span>public class User implements ActiveEntity&#123;</span>
<span> @UUID</span>
<span> private String id;</span>
<span> private String name;</span>
<span> //getter &setter .....</span>
<span>&#125;</span>

<span>//用ActiveRecord模式</span>来存取数据库
<span>new User().loadById("张三").setUserAge(13).update(); </span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>强大的参数式设计。 拦截器、分页、模板、缓存、实体映射器等都可以当作参数拼接到SQL方法里去</h3> <p>例如SQL模板引擎可以当作参数传到SQL里，这样jSqlBox就具备了支持并以扩充各种SQL模板的功能：</p> 
  <div> 
   <div> 
    <pre><span>SqlTemplateEngine TEMPLATE = BasicSqlTemplate.instance()</span>
<span>ctx2.exe(TEMPLATE, "update users set name=#&#123;user.name&#125;, address=:user.address", bind("user", tom));</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>再例如下面的SQL，只会执行一次，因为参数中有一个缓存拦截器，重复的SQL不再执行而是直接从缓存中取结果：</p> 
  <div> 
   <div> 
    <pre><span>SimpleCacheHandler cache = new SimpleCacheHandler();</span>
<span>for (int i = 0; i < 10; i++)</span>
<span>   DB.qry(cache, new EntityListHandler(), DemoUser.class, "select u.* from DemoUser u where u.age>?", par(10));</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>为Java8及以下开发环境提供多行文本支持，方便利用IDE快速定位到多行SQL文本上</h3> 
  <div> 
   <div> 
    <pre><span>public static class InsertDemoSQL extends Text &#123;</span>
<span>/*-  </span>
<span>insert into demo</span>
<span>      (id, name) </span>
<span>values( ?,  ?)</span>
<span>*/</span>
<span>&#125;</span>
<span>//使用：</span>
<span>DB.exe(InsertDemoSQL.class, par("1", "Foo"));</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>灵活的实体关联查询</h3> <p>例如下例，可以一次无递归查询树节点并装配成内存中对象树，其中的EntityNetHandler、alias, give等方法都是与实体关联映射相关的SQL参数：</p> 
  <div> 
   <div> 
    <pre><span>Object[] targets = new Object[] &#123; new EntityNetHandler(), TreeNode.class, TreeNode.class,</span>
<span>alias("t", "p"), give("p", "t", "parent"), give("t", "p", "childs") &#125;;</span>
<span>EntityNet net = ctx.qry(targets, //深度树的海底捞算法</span>
<span>  "select t.**, t.pid as p_id from treenodetb t where t.line>=? and ",</span>
<span>      "t.line< (select min(line) from treenodetb where line>? and lvl<=?) ", par(line, line, lvl));</span>
<span>TreeNode node = net.pickOneEntity("t", d.getId());</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>不同于Hibernate和MyBatis复杂的配置，在jSqlBox中，实体关联查询只不过是一种参数略微复杂的SQL而已，随用随拼，不需要配置。</p> <h3>兼容主要JPA注解，支持在运行期动态更改配置</h3> <p>为了方便学习，jSqlBox兼容JPA实体类的以下主要注解:</p> 
  <div> 
   <div> 
    <pre><span>@Entity, @Transient, @UniqueConstraint, @GenerationType, @Id, @Index, @SequenceGenerator, </span>
<span>@GeneratedValue, @Table, @Column, @TableGenerator, @Version, @Enumerated, @Convert, @Temporal</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>jSql自带一些特殊实体注解如CreatedBy、LastModifiedBy、ShardTable、ShardDatabase、Snowflake等。 jSqlBox在运行期可动态更改实体关联配置，例如下面在运行期给一个pojo类动态配置UUID32主键，并更改它的name字段映射到address字段上:</p> 
  <div> 
   <div> 
    <pre><span>TableModel m = TableModelUtils.entity2Model(PojoDemo.class);</span>
<span>m.column("id").pkey().uuid32();</span>
<span>m.column("name").setColumnName("address");</span>
<span>TableModelUtils.bindGlobalModel(PojoDemo.class, m);</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>jSqlBox自带多租户、主从、分库分表功能</h3> <p>jSqlBox的主从和分库分表功能除了默认的用实体Sharding注解操作外，还支持将分库分表方法作为参数直接传到SQL中使用，精准控制每一条SQL的分库分表:</p> 
  <div> 
   <div> 
    <pre><span>//实体的分库分表</span>
<span>for (i:=0;i<100;i++)</span>
<span>   new TheUser().put("databaseId", i).insert(); </span>
<span>   </span>
<span>//SQL中的分库分表   </span>
<span>db[2].exe(User.class, "insert into ", shardTB(tbID), shardDB(dbID)," (id, name, databaseId) </span>
<span>          values(?,?,?)", par(tbID, "u1", dbID), USE_BOTH);</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>多租户功能可以根据IP地址等进行分库分表，这个和根据实体字段内容分库分表是有区别的，实际多租户要配置TenantGetter实例：</p> 
  <div> 
   <div> 
    <pre><span> public static class CustomTenantGetter implements TenantGetter &#123;</span>
<span>        @Override</span>
<span>        public ImprovedQueryRunner getTenant() &#123;</span>
<span>            return DB.gctx(); //通常是根据IP地址等，从treadlocal中取一个DbContext实例：</span>
<span>        &#125; </span>
<span>    &#125;</span>
<span> //启动阶段</span>
<span> ctx = new DbContext(); </span>
<span> ctx.setTenantGetter(new CustomTenantGetter());</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>自带声明式事务，也支持使用Spring的事务</h3> <p>jSqlBox内置IOC/AOP工具，自带声明式事务功能，详见“事务配置”一节。如果是在Spring环境中，单独或与其它工具比如Hibernate/MyBatis混用，配置也非常简单，如下：</p> 
  <div> 
   <div> 
    <pre><span>DbContext ctx = new DbContext(ds);</span>
<span>ctx.setConnectionManager(SpringTxConnectionManager.instance());</span>
<span>DbContext.setGlobalDbBoxContext(ctx);// 设定静态全局上下文</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <h3>自带分布式事务功能</h3> <p>详见“分布式事务”一节，jSqlBox的分布式事务原理和Seata项目类似，可以自动生成回滚SQL，但jSqlBox的源码远比Seata简洁，因为jSqlBox是基于实体的CRUD生成回滚SQL，所以不需要考虑SQL兼容性这个问题。</p> <h3>不重复发明轮子，避开反模式</h3> <p>jSqlBox不重新发明轮子，使用DbUtils作为内核，以源码内含的方式包含到项目中，DbUtils是一个成熟、简洁、高效的JDBC工具。 jSqlBox尽量避免反模式，反模式就是花很多时间做没有意义的事，比如作者认为实体一对多、多对一的关联配置是个反模式，带来的性能、学习、维护问题往往比它解决的问题还要多，所以在jSqlBox中不支持一对多、多对一的JPA注解支持。 jSqlBox中也不存在用Java方法代替SQL关键字的这种做法，认为它也是一种反模式，比如下面这种写法：</p> 
  <div> 
   <div> 
    <pre><span>List<S1UserPojo> userPojoList = dslContext.select()</span>
<span>            .from(S1_USER)</span>
<span>            .where(S1_USER.ID.eq(1))</span>
<span>            .fetch(r -> r.into(S1UserPojo.class));</span></pre> 
    <div>
      
    </div> 
   </div> 
  </div> <p>只适合简单的CRUD，当逻辑稍微一复杂可读性、可维护性就非常差，还不如直接手写SQL来得方便。<br> <br> 更多功能点介绍和使用，请详见jSqlBox的<a href="https://gitee.com/drinkjava2/jsqlbox/wikis/pages">用户手册</a></p> </li> 
</ol>
                                        </div>
                                      
</div>
            