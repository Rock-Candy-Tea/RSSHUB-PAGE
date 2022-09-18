
---
title: 'Mybatis-Milu 1.8.0 发布，Mybatis 增强框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3550'
author: 开源中国
comments: false
date: Sun, 18 Sep 2022 17:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3550'
---

<div>   
<div class="content">
                                                                                            <p>本次更新内容</p> 
<ol> 
 <li>@Table注解的schema参数支持； <pre><code class="language-java">@Table(schema="db")
public class SomeEntity &#123;
    @LogicDelete(value = "Y", resumeValue="N")
    private String isDeleted;
&#125;
// 查询示例：someEntityMapper.findAll();
// 输出示意：SELECT * FROM db.some_entity</code></pre> <p> </p> </li> 
 <li>增加Criteria查询中对逻辑删除状态查询条件。 <pre><code class="language-java">someEntityMapper.findByCriteria(p -> p.undeleted());
// 输出示意：SELECT * FROM some_entity WHERE is_deleted = 'N';
someMapper.findByCriteria(p -> p.deleted());
// 输出示意：SELECT * FROM some_entity WHERE is_deleted = 'Y';</code></pre> </li> 
</ol> 
<p> </p> 
<p><strong>介绍</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">Mybatis-Milu是基于Mybatis的功能增强框架，遵循JPA规范的ORM，仅允许通过实体映射进行查询操作。</span></p> 
<p>基础接口支持单表查询，基于实体关系的多表关联查询。</p> 
<p>支持Mapper接口方法表达式，快捷定义专用查询。</p> 
<p>基于Lambda的强大且便捷的动态查询功能。</p> 
<p><strong>这是一个轮子，也是一个不容错过的轮子。</strong></p>
                                        </div>
                                      
</div>
            