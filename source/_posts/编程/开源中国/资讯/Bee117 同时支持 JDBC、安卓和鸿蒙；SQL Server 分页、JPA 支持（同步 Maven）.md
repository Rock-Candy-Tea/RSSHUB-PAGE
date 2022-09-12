
---
title: 'Bee1.17 同时支持 JDBC、安卓和鸿蒙；SQL Server 分页、JPA 支持（同步 Maven）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0e926ad3919e67e8da5f7459c9b895e3fd8.png'
author: 开源中国
comments: false
date: Sun, 11 Sep 2022 18:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0e926ad3919e67e8da5f7459c9b895e3fd8.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>ORM Bee同时支持JDBC,安卓Android和鸿蒙HarmonyOS;比传统ORM有更好的运行性能;SQL Server分页全面支持;</strong></p> 
<p><strong>在 Harmony 和 Android 两个环境 , 可以用同一套 Bee 代码访问 DB, 提高代码重用，节省人力物。</strong></p> 
<p><strong style="color:#3498db">Bee，互联网新时代的 Java ORM 工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p><strong>更新功能列表:</strong></p> 
<p><strong style="color:#40485b">V1.17 (2022・中秋)</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>新增功能</strong>:<br> <strong>1)SqlServer支持start,size两个参数分页<br> 2)事务注解Tran及提供与AOP协调的默认实现;支持在类级别使用</strong><br> 3)<strong>支持<span style="color:#3498db">Android</span>(安卓)直接使用Bee访问SQLite数据库;Bee增加Android ORM功能.</strong><br> 4)<strong>支持<span style="color:#e74c3c">HarmonyOS</span>(鸿蒙)直接使用Bee访问SQLite数据库;Bee增加HarmonyOS ORM功能.</strong><span> </span>在<strong>Harmony和Android两个环境</strong>,可以用<strong>同一套Bee代码访问DB</strong>,提高代码重用,节省人力物力!<br> 5)支持Android日志:android.util.Log<br> 6)支持HarmonyOS日志:ohos.hiviewdfx.HiLog</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">7)主键支持名称不叫"id",类型除了Long,可以是<strong>Integer或String</strong><br> 8)支持用注解定义主键自动生成,主键值生成注解:GenId,GenUUID<br> 9)@<strong>Column</strong>添加默认实现(强烈<strong>建议</strong>:在新系统中不要使用该注解)<br> 10)@Table,@Column,@PrimaryKey(@Id),@Ignore(@Transient)可以兼容<strong>JPA</strong>相应注解(在AnnoAdapter接口定义)<br> 11)字段名称引用类(默认格式:<strong>实体名_F</strong>(自动生成))增加ALL_NAMES属性,可一次获取实体的所有字段值<br> 12)Ddl.java支持<strong>创建索引</strong>(normal,unique),<strong>联合主键</strong><br> 13)动态获取JdbcToJavaType<br> 14)<strong>命名转换增加种类4(</strong>DbUpperAndJavaLower):数据库使用大写字母，Java使用小写字母;忽略大小写,使用的字符是一样的<br> 15)同时使用多种命名时,缓存添加TranslateType部分<br> 16)分布式id生成器,支持设置起始年份:bee.distribution.genid.startYear</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>优化与增强:</strong><br> 1)增强:<strong>GenBean生成Javabean</strong>,当id是BigDecimal时,重置为Long型</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2)优化GenBean,支持都使用默认配置<br> 3)<strong>Ddl: 优化创建表流程</strong><br> <strong>4)多数据源环境下,增加日志提示当前使用的是哪个数据源名称</strong><br> 5)分页查询,当获取一页的数据量size为0时,直接返回emptyList<br> 6)增强:<strong>SQLite</strong>日期类型 (date) 匹配转换支持<br> 7)优化缓存<br> 8)condition.op(fieldName, Op.in, Value)增加支持List,Set,Number Array,单个Number元素<br> 9)condition.opOn(fieldName, Op.in, Value) Value限定只支持Number和String<br> 10)增强:<strong>like</strong>;Op添加likeLeft,likeRight,likeLeftRight(参数值由框架负责转义);打印SQL日志作相应转义<br> 11)增强:ExcelReader数据列数目动态计算<br> 12)增强:<strong>SQLite</strong>日期类型 (date) 匹配转换支持<br> 13)<strong>链式编程</strong>SelectImpl,UpdateImpl调整字段检测.</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">fixed bug: 1)level 2缓存判断;TypeHandlerRegistry返回值类型转换<br> 2)拦截器对象不使用原型模式产生脏数据,改为原型模式</p> 
<p><strong>参考实例(部分):</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://my.oschina.net/u/4111850/blog/5538992" target="_blank">Android 环境使用 Bee </a></h1> 
<p>https://my.oschina.net/u/4111850/blog/5538992</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://my.oschina.net/u/4111850/blog/5542608" target="_blank">HarmonyOS 鸿蒙使用 ORM Bee 访问数据库实例</a></h1> 
<p>https://my.oschina.net/u/4111850/blog/5542608</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://my.oschina.net/u/4111850/blog/5561350" target="_blank">Bee 事务注解 @Tran 使用实例</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://my.oschina.net/u/4111850/blog/5561350</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://my.oschina.net/u/4111850/blog/5551862" target="_blank">Bee 的约定与自定义</a></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://my.oschina.net/u/4111850/blog/5551862</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://my.oschina.net/u/4111850/blog/5558755" target="_blank">同时使用不同数据源和不同命名转换实例</a></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://my.oschina.net/u/4111850/blog/5558755</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://my.oschina.net/u/4111850/blog/5560414" target="_blank">模糊查询 like 用法实例 (Bee)</a></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://my.oschina.net/u/4111850/blog/5560414</p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更多使用实例：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://gitee.com/automvc/bee-exam</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://github.com/automvc/bee-exam</p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Bee 架构图:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="792" src="https://oscimg.oschina.net/oscnet/up-0e926ad3919e67e8da5f7459c9b895e3fd8.png" width="637" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由 Bee 框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与 DB 交互的编码工作量，是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的 Java 框架！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">(技术交流 扣群：992650213 ; 更多设计思想，请关注微信公众号：软件设计活跃区)</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee 简单易用：单表操作、多表关联操作，可以不用写 sql, 极少语句就可以完成 SQL 操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333"><span> </span>,10 分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee 功能强大：<strong>复杂查询也支持向对象方式，分页查询性能更高</strong>，一级缓存即可支持个性化优化；具有分布式特性。</span><strong><span style="background-color:#ffffff">高级要求，还可以方便自定义 SQL 语句</span></strong><span style="background-color:#ffffff">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">Bee 2.0 Shading 具有分片功能的分库分表 ORM, 即将要与大家见面了!期待大家的踊跃参与!</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p>
                                        </div>
                                      
</div>
            