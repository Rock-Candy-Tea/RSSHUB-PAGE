
---
title: 'spring-data-mybatis-mini 2.3.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/vonchange/spring-data-mybatis-mini/raw/master/mini.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 11:36:00 GMT
thumbnail: 'https://gitee.com/vonchange/spring-data-mybatis-mini/raw/master/mini.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">更新日志：</p> 
<p style="text-align:left">新增批量修改接口</p> 
<p style="text-align:left">优化实体类解析和加载</p> 
<pre style="text-align:left"><strong>[</strong><span style="color:#032f62">github地址</span><strong>](</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVonChange%2Fspring-data-mybatis-mini" target="_blank"><strong><u>https://github.com/VonChange/spring-data-mybatis-mini</u></strong></a><strong>)
</strong><strong>[</strong><span style="color:#032f62">gitee地址</span><strong>](</strong><a href="https://gitee.com/vonchange/spring-data-mybatis-mini"><strong><u>https://gitee.com/vonchange/spring-data-mybatis-mini</u></strong></a><strong>)</strong>
<strong>[</strong><span style="color:#032f62">blog</span><strong>](</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.vonchange.com%2Fdoc%2Fmini.html" target="_blank"><u>http://www.vonchange.com/doc/mini.html</u></a><strong>)</strong></pre> 
<p style="text-align:left"><strong>等同于spring data jdbc + mybatis 动态sql能力</strong></p> 
<p style="text-align:left"><strong>大道至简 极致效率 麻雀虽小 五脏俱全</strong></p> 
<ol> 
 <li> <p>抛弃繁琐的xml 只使用mybatis模版引擎即动态sql能力 sql写在markdown文件里 更容易书写和阅读 sql能统一管理查看</p> </li> 
 <li> <p>底层基于springJdbc 而不是mybatis,相当于底层直接使用jdbc 更高效</p> </li> 
 <li> <p>提供单表增删改 批量更新插入等基础方法 支持分页 多数据源 读写分离</p> </li> 
 <li> <p>mybatis最大优点就是sql模版引擎 我也有且仅有使用这部分功能(对于使用过mybatis的无学习成本) 但底层使用springJDBC 更简单直接</p> </li> 
 <li> <p>简化mybatis动态sql写法(可混用-写法还是mybatis那套) 比如</p> </li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre>[@and id in idList] 等于
<if test="null!=idList and idList.size>0"> and id in <foreach
collection="idList" index="index" item="item" open="(" separator=","
close=")">#&#123;item&#125;</foreach></if></pre> 
 </div> 
</div> 
<p style="text-align:left"><img alt="例子" src="https://gitee.com/vonchange/spring-data-mybatis-mini/raw/master/mini.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">== Getting Started</p> 
<ol> 
 <li>提供单表增删改(没有物理删除) 批量更新插入等基础方法</li> 
 <li>抛弃繁琐的xml 所有sql 写在markdown文件里 便于书写和阅读 默认位置sql包下repository接口名.md @ConfigLocation 可自定义位置</li> 
 <li>自定义更新 @Update/@Insert或者update/save/insert/delete 开头方法是更新操作</li> 
 <li>支持分页</li> 
 <li>对于 " > "," < "," >= "," <= "," <> "无需转义(两边需有空格 我会自动替换转义)</li> 
 <li>提供if判断和in查询简写方式(偷懒 >-<)</li> 
 <li>注解属于spring data jpa 体系的</li> 
 <li>支持sql片段 [@sql XX] XX markdown文件XX名的sql片段</li> 
 <li>查询返回实体 不需要必须是DO 如果没特殊规范 也可直接返回VO层实体(抛弃繁琐的DO->DTO->VO 偷懒轻喷)</li> 
 <li>支持批量更新插入（jdbc链接参数需加入rewriteBatchedStatements=true&allowMultiQueries=true）</li> 
 <li>分页某些特性支持mysql,oracle 主支持mysql 可自定义方言实现其他数据库</li> 
 <li>使用简单 约定大于配置 默认配置基本都满足</li> 
 <li>支持LocalDateTime LocalTime jdk8更方便的时间类型</li> 
</ol> 
<p style="text-align:left">== 其他特性 无特殊需要可不用关心</p> 
<ol> 
 <li>分页 可自定义同名+Count的sql 优化分页</li> 
 <li>支持读写分离 根据业务逻辑添加@ReadDataSource在方法名上 默认配置多数据源随机取 可自定义</li> 
 <li>多数源支持但在微服务化潮流里尽量保证同一数据源</li> 
</ol> 
<p style="text-align:left">== 使用步骤基本同jpa,spring data jdbc</p> 
<ol> 
 <li>添加依赖</li> 
 <li>@EnableMybatisMini</li> 
 <li>extends BaseRepository<UserBaseDO, Long> 或 extends BaseQueryRepository(只查询)</li> 
 <li>使用例子demo项目<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVonChange%2Fspring-data-mybatis-mini-demo%2Fblob%2Fmaster%2Fsrc%2Ftest%2Fjava%2Fcom%2Fvonchange%2Fnine%2Fdemo%2Fdao%2FUserBaseRepositoryTest.java" target="_blank">spring-data-mybatis-mini-demo</a></li> 
</ol> 
<p style="text-align:left">Here is a quick teaser of an application using Spring Data mybatis mini in Java:</p> 
<p style="text-align:left">=== Maven configuration</p> 
<p style="text-align:left">Add the Maven dependency:</p> 
<div style="text-align:left"> 
 <div> 
  <pre>  <!-- spring boot 2.x 是使用版本2.3.6 -->
<dependency>
  <groupId>com.vonchange.common</groupId>
  <artifactId>spring-data-mybatis-mini</artifactId>
  <version>2.3.8</version>
</dependency>

<dependency>
       <groupId>org.springframework.data</groupId>
       <artifactId>spring-data-commons</artifactId>
 </dependency>
 <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-jdbc</artifactId>
 </dependency>
<dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.15</version>
</dependency>
</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre><!-- 低版本比如1.5.x 使用版本low-1.9.6-->
<dependency>
  <groupId>com.vonchange.common</groupId>
  <artifactId>spring-data-mybatis-mini-low</artifactId>
  <version>1.9.6</version>
</dependency>
</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>//添加 EnableMybatisMini 注解 
@EnableMybatisMini
@SpringBootApplication 
public class DemoApplication &#123;
    public static void main(String[] args) &#123;
        SpringApplication.run(DemoApplication.class, args);
    &#125;
&#125; </pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>import org.springframework.data.mybatis.mini.jdbc.repository.query.ConfigLocation;
import org.springframework.data.mybatis.mini.jdbc.repository.support.BaseRepository;
import org.springframework.data.repository.query.Param;

public interface UserBaseRepository extends BaseRepository<UserBaseDO, Long> &#123;
  @ReadDataSource
  List<UserBaseDO> findList(@Param("userName") String userName,
                          @Param("createTime") Date createTime);
  Page<UserBaseDO> findList(Pageable pageable, @Param("userName") String userName,@Param("createTime") Date createTime);
  String findUserName(@Param("userName") String userName);

  List<UserBaseVO> findListByIds(@Param("userName") String userName,
                           @Param("createTime") Date createTime,@Param("idList")List<Long> idList);

  int updateIsDelete(@Param("isDelete") Integer isDelete,@Param("id") Long id);
  
&#125;</pre> 
 </div> 
</div> 
<blockquote> 
 <p>默认sql 包下同名吧UserBaseRepository.md 识别```开头结尾的 -- 定义的同名方法 参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVonChange%2Fspring-data-mybatis-mini%2Fblob%2Fmaster%2FUserBaseRepository.md" target="_blank">UserBaseRepository.md</a></p> 
</blockquote> 
<blockquote> 
 <p>实体类 定义ID 和TABLE 名</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>import javax.persistence.Id;
import javax.persistence.Table;

@Data
@Table(name = "user_base")
public class UserBaseDO &#123;
    @Id
    private Long id;
    private String userName;
    private String  firstPhone;

&#125;</pre> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <pre>@Service
public class MyService &#123;
  @Resource
  private final UserBaseRepository userBaseRepository;

  public void doWork() &#123;
     List<UserBaseDO> userBaseDOList = userBaseRepository.findList("test",new Date());
 &#125;
&#125;
</pre> 
 </div> 
</div> 
<blockquote> 
 <p>偷懒简化 if test 和in查询 识别 [@开头判空 [@@开头不会判空</p> 
</blockquote> 
<blockquote> 
 <p>[@and id in idList] 等于</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><if test="null!=idList and idList.size>0"> and id in <foreach
collection="idList" index="index" item="item" open="(" separator=","
close=")">#&#123;item&#125;</foreach></if>
  </pre> 
 </div> 
</div> 
<blockquote> 
 <p>[@@and id in idList] 等于</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>and id in <foreach
collection="idList" index="index" item="item" open="(" separator=","
close=")">#&#123;item&#125;</foreach>
  </pre> 
 </div> 
</div> 
<blockquote> 
 <p>[@and user_name <> userName] 等于</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><if test="null!=userName and ''!=userName"> and user_name <>
#&#123;userName&#125; </if></pre> 
 </div> 
</div> 
<ol> 
 <li> <p>in 查询List实体下的属性 [@and id in userList:id]</p> </li> 
 <li> <p>like</p> </li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre>[@and user_name like userName] 等于 and user_name like CONCAT('%',?,'%')  
[@and user_name like userName%] 等于 and user_name like  CONCAT(?,'%') 
[@and user_name like userName%] 等于 and user_name like CONCAT('%','test')   
</pre> 
 </div> 
</div> 
<ol> 
 <li>其他非4个分隔</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre>[@and id in #&#123;idList:in&#125; and user_name like #&#123;userName:like&#125;]
等于
<if test="@com.vonchange.mybatis.tpl.MyOgnl@isNotEmpty(idList) and @com.vonchange.mybatis.tpl.MyOgnl@isNotEmpty(userName) "> and id in <foreach collection="idList" index="index" item="item" open="(" separator="," close=")">#&#123;item&#125;</foreach> and user_name like  CONCAT('%',#&#123;userName&#125;,'%')  </if>

 [@AND content -> '$.account' = #&#123;bean.account&#125;]
 等于
 <if test="null!=bean.account and ''!=bean.account">
 AND content -> '$.account' = #&#123;bean.account&#125;
 </if>
</pre> 
 </div> 
</div> 
<ol> 
 <li>[@sql XX] XX markdown文件XX名的sql片段</li> 
</ol> 
<blockquote> 
 <p>相关注解</p> 
</blockquote> 
<ol> 
 <li> <p>@ColumnNot 非字段注解</p> </li> 
 <li> <p>InsertIfNull UpdateIfNull 插入或者更新为空时默认值 可使用函数</p> </li> 
 <li> <p>UpdateNotNull updateAllField方法NULL值忽略</p> </li> 
 <li> <p>ReadDataSource 指定某个方法读数据源 默认配置多数据源随机取</p> </li> 
 <li> <p>Update 更新语句 Insert 插入语句返回ID</p> </li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre> //自定义 读库数据源 不自定义默认所有你设置的数据源
    @Bean
    public ReadDataSources initReadDataSources()&#123;
        return new ReadDataSources() &#123;
            @Override
            public DataSource[] allReadDataSources() &#123;
                return new DataSource[]&#123;mainDataSource(),mainDataSource(),readDataSource()&#125;;
            &#125;
        &#125;;
    &#125;</pre> 
 </div> 
</div> 
<blockquote> 
 <p>批量更新插入</p> 
</blockquote> 
<ol> 
 <li> <p>jdbc链接参数需加入rewriteBatchedStatements=true&allowMultiQueries=true</p> </li> 
 <li> <p>提供insertBatch(默认第一行不为NULL的字段) 可在markdown里自定义sql 无需关心List对象大小</p> </li> 
 <li> <p>经测试简单数据插入1万耗时1s以内</p> </li> 
 <li> <p>自定义实现(建议使用 更透明)</p> </li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre>  
  @BatchUpdate(size = 5000)
  int batchInsert(List<UserBaseDO> list);</pre> 
 </div> 
</div> 
<p style="text-align:left">只需定义单条insert 语句</p> 
<div style="text-align:left"> 
 <div> 
  <pre>-- batchInsert
insert into user_base(`user_name`,`mobile_phone`,create_time) values
(#&#123;userName&#125;,#&#123;mobilePhone&#125;,#&#123;createTime&#125;) 
</pre> 
 </div> 
</div> 
<blockquote> 
 <p>大数据量流式读取</p> 
</blockquote> 
<ol> 
 <li> <p>使用场景: 不用编写复杂分包逻辑,表数据大小,可关联表查 可直接 select * from 整个表 不用关心内存爆调 流的方式读取</p> </li> 
 <li> <p>使用例子</p> </li> 
</ol> 
<blockquote> 
 <p>定义方法</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>void findBigData(@Param("")AbstractPageWork<UserBaseDO> abstractPageWork,@Param("userName") String userName);</pre> 
 </div> 
</div> 
<blockquote> 
 <p>定义sql</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre>-- findBigData
select * from user_base
<where> 
[@and user_name like userName]
</where></pre> 
 </div> 
</div> 
<blockquote> 
 <p>使用demo</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre> AbstractPageWork<UserBaseDO> abstractPageWork = new AbstractPageWork<UserBaseDO>() &#123;
            @Override
            protected void doPage(List<UserBaseDO> pageContentList, int pageNum, Map<String, Object> extData) &#123;
                pageContentList.forEach(userBaseDO -> &#123;
                    log.info("&#123;&#125;",userBaseDO.toString());
                &#125;);

            &#125;

            @Override
            protected int getPageSize() &#123;
                return 500;
            &#125;
        &#125;;
       userBaseRepository.findBigData(abstractPageWork,"三");
       log.info("&#123;&#125; &#123;&#125; &#123;&#125;",abstractPageWork.getSize(),abstractPageWork.getTotalPages(),abstractPageWork.getTotalElements());</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            