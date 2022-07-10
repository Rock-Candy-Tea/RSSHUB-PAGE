
---
title: 'Bee V1.17.0.8 兼容 JPA 注解，主键兼容更多类型更智能，支持注解方式生成主键值'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0e926ad3919e67e8da5f7459c9b895e3fd8.png'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 10:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0e926ad3919e67e8da5f7459c9b895e3fd8.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#3498db"><strong>ORM Bee为适应互联网时代软件需求量大,需求变更频繁,性能要求高等要求,应运而生!</strong></span><br> <strong>Bee，互联网新时代的Java ORM框架，更快、更简单、更自动，开发速度快，运行快，更智能！<br> 简单易用,文件小,性能好;同时支持JDBC(比如JavaWeb),Android和Harmony。</strong></p> 
<p><strong style="color:#40485b">新增功能:</strong></p> 
<p><strong style="color:#40485b">V1.17.0.8(海纳百川)</strong><br> <span style="background-color:#ffffff; color:#40485b">1)主键支持名称不叫"id",类型除了Long,可以是Integer或String</span><br> <span style="background-color:#ffffff; color:#40485b">2)支持用注解定义主键自动生成,主键值生成注解:GenId,GenUUID</span><br> <span style="background-color:#ffffff; color:#40485b">3)@Column添加默认实现(强烈建议:在新系统中不要使用该注解)</span><br> <span style="background-color:#ffffff; color:#40485b">4)@Table,@Column,@PrimaryKey(@Id)可以兼容JPA相应注解(在AnnoAdapter接口定义)</span><br> <span style="background-color:#ffffff; color:#40485b">5)分布式id生成器,支持设置起始年份:bee.distribution.genid.startYear</span><br> <span style="background-color:#ffffff; color:#40485b">6)链式编程SelectImpl,UpdateImpl调整字段检测.</span></p> 
<p><strong>智能判断:</strong><br> 当主键字段的类型是Integer,使用@GenId会生成Integer类型的数字; <br> 若想主键具有分布式全局唯一ID特性,可使用Long型.<br> 若想使用UUID作为主键, 可以用@GenUUID.<br> <strong>松耦合设计:</strong><br> 配置主键自动生成不覆盖已存在的值，当主键有值时，就不会采用自动生成。<br> 不强依赖框架自动生成，可轻松使用自己的策略生成主键值。</p> 
<p><strong>感谢网友</strong>: <a href="https://gitee.com/xfl12345" target="_blank">xfl12345</a>   <a href="https://gitee.com/crazytrip" target="_blank">小书生</a>  <a href="https://gitee.com/sesame8" target="_blank">zxz</a>  <a href="https://gitee.com/LkyQiuFeng" target="_blank">Fall</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee%2Fissues%3Fq%3Dis%253Aissue%2Bis%253Aopen%2Bauthor%253Aq1349" target="_blank">q1349</a></p> 
<p><strong>Bee架构图:</strong></p> 
<p><img height="792" src="https://oscimg.oschina.net/oscnet/up-0e926ad3919e67e8da5f7459c9b895e3fd8.png" width="637" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由 Bee 框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与 DB 交互的编码工作量，是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的 Java 框架！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">(技术交流 扣群：992650213 ; 更多设计思想，请关注微信公众号：软件设计活跃区)</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee 简单易用：单表操作、多表关联操作，可以不用写 sql, 极少语句就可以完成 SQL 操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333"><span> </span>,10 分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee 功能强大：<strong>复杂查询也支持向对象方式，分页查询性能更高</strong>，一级缓存即可支持个性化优化；具有分布式特性。</span><strong><span style="background-color:#ffffff">高级要求，还可以方便自定义 SQL 语句</span></strong><span style="background-color:#ffffff">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#c0392b"><strong>你还想添加什么功能，请到评论区告诉我们！</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p>
                                        </div>
                                      
</div>
            