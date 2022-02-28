
---
title: 'ORM 框架 Bee V1.11_2.28 发布，查询结果拦截、ShardingStruct 为分库分表准备'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ed6b3ba1140bdcf4dd8d4d66656b05cabae.bmp'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 08:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ed6b3ba1140bdcf4dd8d4d66656b05cabae.bmp'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#3498db">Bee，互联网新时代的Java ORM工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#c0392b">Bee让程序员/软件工程师，从手工编码中解放出来，Bee更适合智能软件制造时代！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">立志做最懂用户的软件!</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#40485b">V1.11.0.2.28 (Special Day)</span></strong><br> <strong><span style="background-color:#ffffff; color:#40485b">增加ShardingStruct,简化多租户且为分库分表作准备</span></strong><br> <span style="background-color:#ffffff; color:#40485b">Column列名与属性名映射扩展支持</span><br> <span style="background-color:#ffffff; color:#40485b">支持自定义<strong>TypeHandler</strong>，</span>查询结果拦截，<span style="background-color:#ffffff; color:#40485b">处理查询的ResultSet结果</span><br> <span style="background-color:#ffffff; color:#40485b">PreparedSql自定义sql支持多表查询,<strong>返回多表关联Javabean结构数据</strong></span><br> <span style="background-color:#ffffff; color:#40485b">fixed bug:</span><br> <span style="background-color:#ffffff; color:#40485b">多表查询同一个实体自我关联查询禁止自我多次循环</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>准备向复杂的分库分表进军了。。。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">近期已添加功能:</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/177042/bee-1-11-0-1-1-released" target="_blank">ORM 框架 Bee V1.11.0.1.1（2022新年版）发布，更快、更简单、更自动</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/180926/bee-1-11-0-2-1-released" target="_blank">ORM 框架 Bee V1.11.0.2.1（2022 春节版）发布，拦截器、多租户(过年不打烊)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.4 (2022北京冬奥版)发布,二级缓存扩展支持(Redis)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架</a> <a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">Bee </a><a href="https://www.oschina.net/news/182304/bee-2022-romantic-released" target="_blank">2022 Romantic 版发布,加 JustFetch,Datetime 等注解和 Jndi 支持</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/183310/bee-1-11-0-2-20-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.20 2022(荣耀)版发布，完善拦截器，增加多种注解简化开发</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee#bee%E4%B8%BB%E8%A6%81%E5%8A%9F%E8%83%BD%E7%89%B9%E7%82%B9%E4%BB%8B%E7%BB%8D">https://gitee.com/automvc/bee#bee主要功能特点介绍</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">------------------------------------------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由Bee框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与DB交互的编码工作量, 是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的Java 框架!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee简单易用：单表操作、多表关联操作，可以不用写sql,极少语句就可以完成SQL操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333">,10分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee功能强大：复杂查询也支持向对象方式，分页查询性能更高，一级缓存即可支持个性化优化；具有分布式特性。高级要求，还可以方便自定义SQL语句。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="398" src="https://oscimg.oschina.net/oscnet/up-ed6b3ba1140bdcf4dd8d4d66656b05cabae.bmp" width="888" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p>
                                        </div>
                                      
</div>
            