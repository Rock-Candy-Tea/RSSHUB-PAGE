
---
title: 'Bee 2022 Romantic 版发布,加 JustFetch,Datetime 等注解和 Jndi 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ed6b3ba1140bdcf4dd8d4d66656b05cabae.bmp'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 08:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ed6b3ba1140bdcf4dd8d4d66656b05cabae.bmp'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Bee V1.11.0.<span style="color:#e74c3c"><strong>2.15</strong></span><span> </span>2022浪漫版发布</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#3498db">Bee，互联网新时代的Java ORM工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#c0392b">Bee让程序员/软件工程师，从手工编码中解放出来，Bee更适合智能软件制造时代！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">立志做最懂用户的软件!</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Bee V1.11.0.<span style="color:#e74c3c"><strong>2.15</strong></span><span> </span>2022浪漫版发布</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#e67e22">2.14西方情人节, 2.15 中国情人节, 哪个节日更浪漫!</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>功能列表:</strong></p> 
<p><strong>1.注解增强:</strong><br> @Datetime<br> @Createtime,<br> @Updatetime<br> <strong>@JustFetch</strong></p> 
<p><strong>2.Jndi支持<br> 3.检测MapSqlKey的值</strong></p> 
<p>例子:</p> 
<pre><code class="language-java"> * eg:
 * @JustFetch("CONCAT(fisrt_name,last_name)") //多表查询时,若字段会混淆,需要带表名
 * private String fullname;
 * -->select CONCAT(fisrt_name,last_name) as fullname
 *  
 *  map field name and column name,but can not transform to where part
 *  eg:
 * @JustFetch("name")
 * private String name2;
 * -->select name as name2</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下个版本预告:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">动态设置数据源.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">多数据源同时支持多种DB类型操作, 支持兼容旧系统.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">近期已添加功能:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/177042/bee-1-11-0-1-1-released" target="_blank">ORM 框架 Bee V1.11.0.1.1（2022新年版）发布，更快、更简单、更自动</a></p> 
<p><a href="https://www.oschina.net/news/180926/bee-1-11-0-2-1-released" target="_blank">ORM 框架 Bee V1.11.0.2.1（2022 春节版）发布，拦截器、多租户(过年不打烊)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.4 (2022北京冬奥版)发布,二级缓存扩展支持(Redis)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee#bee%E4%B8%BB%E8%A6%81%E5%8A%9F%E8%83%BD%E7%89%B9%E7%82%B9%E4%BB%8B%E7%BB%8D">https://gitee.com/automvc/bee#bee主要功能特点介绍</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>好消息:</strong><br> 2022年2月15日<strong>元宵节</strong>前登记的企业用户，可获得专业的生产环境使用帮助,为你的系统保驾护航、提高性能；<br> 个人用户登记后入群，可获得个性化的使用咨询!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">登记地址：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee/issues/I3PIUJ">https://gitee.com/automvc/bee/issues/I3PIUJ</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee%2Fissues%2F43" target="_blank">https://github.com/automvc/bee/issues/43</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">完成登记的伙伴,请加QQ群(<strong>992650213</strong>),找群主领资料!</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">------------------------------------------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由Bee框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与DB交互的编码工作量, 是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的Java 框架!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee简单易用：单表操作、多表关联操作，可以不用写sql,极少语句就可以完成SQL操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333">,10分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee功能强大：复杂查询也支持向对象方式，分页查询性能更高，一级缓存即可支持个性化优化；具有分布式特性。高级要求，还可以方便自定义SQL语句。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="398" src="https://oscimg.oschina.net/oscnet/up-ed6b3ba1140bdcf4dd8d4d66656b05cabae.bmp" width="888" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">相关框架设计信息也可关注微信公众号：软件设计活跃区</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            