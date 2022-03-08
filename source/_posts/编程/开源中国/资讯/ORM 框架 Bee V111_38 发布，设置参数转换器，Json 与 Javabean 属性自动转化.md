
---
title: 'ORM 框架 Bee V1.11_3.8 发布，设置参数转换器，Json 与 Javabean 属性自动转化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5046d84f1efdd8ac7b0f53db621626a78a4.png'
author: 开源中国
comments: false
date: Mon, 07 Mar 2022 23:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5046d84f1efdd8ac7b0f53db621626a78a4.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#3498db">Bee，互联网新时代的Java ORM工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#c0392b">Bee让程序员/软件工程师，从手工编码中解放出来，Bee更适合智能软件制造时代！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">立志做最懂用户的软件!</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#40485b">V1.11.0.3.8 (</span></strong><span><span><strong><span><span style="color:#ef39a1">Lady First</span></span></strong></span></span><strong><span style="background-color:#ffffff; color:#40485b">)</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>新增PreparedStatement设置参数转换器,</strong><br> Javabean使用<strong>java.util.Date</strong>类型,进行SUID作兼容处理.  <br> <strong>SQLite</strong>获取Timestamp结果作转化处理.   <br> <strong>实体属性是Javabean与DB表Json类型字段在参数设置与查询结果时自动转换(使用Json注解定制开发)</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">例子:</p> 
<p><img height="39" src="https://oscimg.oschina.net/oscnet/up-5046d84f1efdd8ac7b0f53db621626a78a4.png" width="506" referrerpolicy="no-referrer"></p> 
<p><img height="49" src="https://oscimg.oschina.net/oscnet/up-a9e571cb6ce95cc355c301de55479a950d1.png" width="715" referrerpolicy="no-referrer"></p> 
<pre><code class="language-java">public class Dept implements Serializable &#123;

private Integer id;
private String deptName;
@Json
private JsonValue jsonValue;</code></pre> 
<pre><code class="language-java">List<Dept> list=suid.select(new Dept());</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">日志:</p> 
<pre><code class="language-sql">[INFO] [Bee] select SQL: select id,dept_name,json_value from dept   [values]: 
[INFO] [Bee]  | <--  select rows: 1
[INFO] Dept[id=1,dept=部门1,jsonValue=JsonValue[deptId=1,deptName=子部门1,deptLeaderId=11]]</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>准备向复杂的分库分表进军了。。。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">近期已添加功能:</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/177042/bee-1-11-0-1-1-released" target="_blank">ORM 框架 Bee V1.11.0.1.1（2022新年版）发布，更快、更简单、更自动</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/180926/bee-1-11-0-2-1-released" target="_blank">ORM 框架 Bee V1.11.0.2.1（2022 春节版）发布，拦截器、多租户(过年不打烊)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.4 (2022北京冬奥版)发布,二级缓存扩展支持(Redis)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架</a> <a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">Bee<span> </span></a><a href="https://www.oschina.net/news/182304/bee-2022-romantic-released" target="_blank">2022 Romantic 版发布,加 JustFetch,Datetime 等注解和 Jndi 支持</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/183310/bee-1-11-0-2-20-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.20 2022(荣耀)版发布，完善拦截器，增加多种注解简化开发</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/184359" target="_blank">ORM 框架 Bee V1.11.0.2.28 发布，查询结果拦截、ShardingStruct 为分库分表准备</a></p> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">相关框架设计信息也可关注微信公众号：软件设计活跃区</span></p> 
<p><span style="background-color:#ffffff; color:#e74c3c">QQ群(</span><strong style="color:#e74c3c">992650213</strong><span style="background-color:#ffffff; color:#e74c3c">)</span></p>
                                        </div>
                                      
</div>
            