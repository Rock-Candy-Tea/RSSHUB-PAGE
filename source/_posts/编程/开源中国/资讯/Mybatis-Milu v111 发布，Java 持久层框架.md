
---
title: 'Mybatis-Milu v1.1.1 发布，Java 持久层框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=605'
author: 开源中国
comments: false
date: Sun, 29 Aug 2021 22:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=605'
---

<div>   
<div class="content">
                                                                                            <p>Mybatis-Milu v1.1.1 已经发布，Java 持久层框架。</p> 
<p>此版本<a href="https://gitee.com/yuehh/mybatis-milu/releases/v1.1.1" target="_blank">增加各部分功能的分页查询便捷性</a>：</p> 
<ul> 
 <li>Example查询现可以直接使用Pageable参数进行分页。</li> 
 <li>查询创建器（命名式查询）现可以直接在任意参数位置加入Pageable参数进行分页。</li> 
 <li>Criteria查询现可以.limit(Pageable page)进行分页。</li> 
</ul> 
<p>mybatis-milu是基于mybatis的功能增强框架，遵循JPA规范的ORM，提供通用Mapper接口，提供类似Spring Data JPA的查询创建器，通过方法名解析查询语句，极大提高开发效率。 本框架仅做功能增强，拓展statement的创建方式，不覆盖mybatis中的任何实现。</p> 
<p>支持JPA的注解规范，但没有根据实体类注解声明生成表、索引等的功能，所以部分注解或注解属性用来生成表及索引的，使用后并无效果。</p> 
<h4>目标</h4> 
<ol> 
 <li>通过ORM使9成以上查询不需要写SQL就能完成，减少SQL测试调试时间。</li> 
 <li>通过ORM解决多表关联查询问题，避免一涉及多表查询就要写SQL的问题。</li> 
 <li>通过命名查询创建器更方便创建一对一的专用查询接口，更容易审计。</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/yuehh/mybatis-milu/releases/v1.1.1">https://gitee.com/yuehh/mybatis-milu/releases/v1.1.1</a></p>
                                        </div>
                                      
</div>
            