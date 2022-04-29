
---
title: 'BeeV1.11 拦截器，多租户、Redis 缓存、注册器、类型转换器和结果处理器（上传 Maven）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6549'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 09:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6549'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#3498db">Bee，互联网新时代的Java ORM工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#c0392b">Bee让程序员/软件工程师，从手工编码中解放出来，Bee更适合智能软件制造时代！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">立志做最懂用户的软件!</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>V1.11 (International Labour Day)</strong></p> 
<p><strong>实例简要展示</strong>:</p> 
<p><strong>1.同时使用多种数据源</strong></p> 
<pre><code class="language-java">//数据源需要提前配置好
        PreparedSql preparedSqlOracle = BeeFactory.getHoneyFactory().getPreparedSql();
preparedSqlOracle.setDataSourceName("ds2");

PreparedSql preparedSqlMysql = BeeFactory.getHoneyFactory().getPreparedSql();
preparedSqlMysql.setDataSourceName("ds1");

String sql="select id,biz_tag,max_id,step,description,update_time,version from leaf_alloc";

Object preValues[]=null;
preparedSqlOracle.select(sql, new LeafAlloc(), preValues, 0, 2); //分页语句部分由Bee负责
</code></pre> 
<p><strong><span style="background-color:#ffffff; color:#40485b">Suid,PreparedSql,MapSuid,MoreTable都增加有方法:setDataSourceName,getDataSourceName,getInterceptorChain</span></strong></p> 
<p><strong>2.拦截器</strong></p> 
<p><strong>CommInterceptorChain</strong></p> 
<p><strong>3.注册器</strong></p> 
<pre><code class="language-java">CalculateRegistry,计算分版算法注册器
DbFeatureRegistry,DB方言特性注册器
InterceptorChainRegistry,拦截器链注册器
NameRegistry,命名转换注册器
SetParaTypeConverterRegistry, PreparedStatement参数类型转换注册器
TypeHandlerRegistry 查询结果转换注册器</code></pre> 
<p><strong>4.类型转换器,.结果处理器</strong></p> 
<p>详细实例:</p> 
<p><a href="https://my.oschina.net/u/4111850/blog/5494806">https://my.oschina.net/u/4111850/blog/5494806</a></p> 
<p><strong>5.实体名_F  就可以引用字段名</strong></p> 
<pre><code class="language-java">      //方式1
        objSQLRichService.update(download, "genProject");
        //方式2, 本次新增.
        objSQLRichService.update(download, Download_F.genProject);</code></pre> 
<p><a href="https://www.oschina.net/news/192843/bee-1-11-4-22-released">https://www.oschina.net/news/192843/bee-1-11-4-22-released</a><br> 7.<strong>自定义动态SQL标签</strong></p> 
<p>select * from orders where userid in #&#123;userid @in&#125;<br> <a href="https://my.oschina.net/u/4111850/blog/5493477">https://my.oschina.net/u/4111850/blog/5493477</a><br>         </p> 
<p>V1.11主要功能更新<br> 1)拦截器、多租户<br> 2)增加<strong>Sharding</strong>Struct为分库分表作准备<br> 3)二级缓存扩展支持<br> <strong>Redis缓存</strong>支持<br> 3)<strong>支持自定义TypeHandler,处理查询的ResultSet结果</strong><br> 4)add SetParaTypeConvert for convert PreparedStatement parameter<br> 5)支持在Suid等对象设置<strong>命名转换器</strong>.<br> 增加DbFeature方言注册器,自定义实现不同DB方言更加易用.<br> 6)支持<strong>Cassandra</strong>.<br> 7)添加<strong>Jndi</strong>数据源支持<br> 8)Ddl.java使用Javabean创建表,支持追加java与db字段类型映射,支持设置某个DB的java_dbtype类型映射.<br> 9)PreparedSql<strong>自定义sql支持批量插入</strong>.<br> PreparedSql自定义sql支持多表查询,返回多表关联Javabean结构数据<br> 10)<strong>自定义动态SQL标签,@in,</strong>@toIsNULL1,@toIsNULL2,<if isNotNull>,<if isNotBlank>.<br> 动态sql,将list转为像in (1,2,3)的语句,不需要foreach,批量插入也<strong>不需要foreach</strong>.</p> 
<p>添加注解:<br> PrimaryKey,Datetime,Createtime,Updatetime;JustFetch<br> AnnotationHandler,AutoSetString自动设置字符值<br> Desensitize,敏感信息模糊处理<br> ReplaceInto,MySQL replace into转换<br> MultiTenancy多租户<br> BeforeReturnAnnotationHandler,AbstractDictI18nDefaultHandler<br> Dict字典转化<br> DictI18n多语言国际化字典转化<br> Column列名与属性名映射<strong>扩展</strong>支持</p> 
<p>增强:<br> multi-DS<strong>同时使用不同类型DB</strong>优化<br>  (比如,同时使用<strong>Mysql,Oracle</strong>,SQL Server)<br> 可用<strong>BF</strong>代替BeeFactoryHelper加快输入<br> Javabean使用<strong>java.util.Date</strong>类型,进行SUID作兼容处理.<br> Ddl.java兼容原生char类型,兼容java.util.Date.<br> <strong>SQLite</strong>获取Timestamp结果作转化处理.<br> 实体属性是Javabean与DB表Json类型字段在参数设置与查询结果时自动转换(使用Json注解自定义实现).<br> 读写模式配置信息去除空格<br> 检测MapSqlKey的值<br> 增加Registry空接口；增加NameRegistry.<br> 更改Serializer接口抛出异常方式.<br> MapSuid,MapSql支持解析字符串的<strong>Boolean</strong>类型.<br> GenBean，还不支持的jdbc类型，<strong>提醒</strong>在哪个文件设置.<br> GenBean增加支持<strong>是否覆盖原有文件</strong>设置.<br> GenBean增加获取字段支持，使用字段名可以不直接使用字符串.<br> SuidRich的selectString方法支持<strong>可变参数</strong>:<br> public List<String[]> selectString(T entity,String... selectFields);<br> CommInterceptorChain增加检测是否添加了相同类型拦截器.<br> 提高缓存安全.<br> 添加<strong>SPI</strong>预加载接口PreLoad.<br> 添加用于<strong>全局的拦截器注册器</strong>InterceptorChainRegistry.</p> 
<p>fixed bug:<br> naming transfer<br> 多表查询同一个实体自我关联查询禁止自我多次循环</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">   </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>准备向复杂的分库分表进军了。。。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>好消息:</strong><br> 2022年<strong><span style="color:#c0392b">5月1日</span>劳动节</strong>前登记的企业用户，可获得专业的生产环境使用帮助,为你的系统保驾护航、提高性能；<br> 个人用户登记后入群(扣群:<strong>992650213</strong>)，可获得个性化的使用咨询!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">登记地址：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee/issues/I3PIUJ">https://gitee.com/automvc/bee/issues/I3PIUJ</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee%2Fissues%2F43" target="_blank">https://github.com/automvc/bee/issues/43</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">功能列表详情:</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/192843/bee-1-11-4-22-released" target="_blank">ORM 框架 Bee V1.11_4.22 发布</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">------------------------------------------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由Bee框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与DB交互的编码工作量, 是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的Java 框架!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee简单易用：单表操作、多表关联操作，可以不用写sql,极少语句就可以完成SQL操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333">,10分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee功能强大：复杂查询也支持向对象方式，分页查询性能更高，一级缓存即可支持个性化优化；具有分布式特性。</span><strong><span style="color:#e74c3c"><span style="background-color:#ffffff">高级要求，还可以方便自定义SQL语句</span></span></strong><span style="background-color:#ffffff; color:#333333">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p>
                                        </div>
                                      
</div>
            