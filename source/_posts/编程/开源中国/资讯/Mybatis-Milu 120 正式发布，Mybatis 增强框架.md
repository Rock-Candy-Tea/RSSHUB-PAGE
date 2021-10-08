
---
title: 'Mybatis-Milu 1.2.0 正式发布，Mybatis 增强框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3294'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 15:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3294'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mybatis-Milu 1.2.0 现已发布，具体更新内容如下：</p> 
<ul> 
 <li> <p>增加自定义短配置注解功能 。<br> <span style="background-color:#ffffff; color:#40485b">使用@SnowflakeId注解在主键上，将会在insert时自动使用snowflakeId注入值。<br> 使用@CreateTime注解在日期属性上，将会在insert时自动使用当前日期。</span></p> <p>开发者可以自定义自己的注解别名使用。内置的别名注解及自定义方式见文档。</p> </li> 
 <li> <p>typeHandler声明支持。<br> 现在可在@AttributeOptions上声明字段typeHandler以及jdbcType。</p> </li> 
</ul> 
<p>starter引用依赖</p> 
<pre><code class="language-xml"><dependency>
    <groupId>com.yuehuanghun</groupId>
    <artifactId>mybatismilu-spring-boot-starter</artifactId>
    <version>1.2.0</version>
</dependency></code></pre>
                                        </div>
                                      
</div>
            