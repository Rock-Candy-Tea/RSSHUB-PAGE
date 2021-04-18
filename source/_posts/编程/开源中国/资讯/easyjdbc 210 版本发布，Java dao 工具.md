
---
title: 'easyjdbc 2.1.0 版本发布，Java dao 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1844'
author: 开源中国
comments: false
date: Sat, 17 Apr 2021 22:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1844'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">easyjdbc 在 spring jdbctemplate 之上进行了一些包装，支持部分常用的 JPA 注解，使得经过注解的实体可以像 Hibernate,jpa 一样进行增、删、改和获取。SQL 构造工具、SQL 注解、链式 API 等让查询操作更为灵活。动态实体映射使得各种查询不再需要写大量的 RowMapper。</p> 
<p style="text-align:left"><strong>功能简介：</strong></p> 
<ol> 
 <li> <p>常用的 JPA 注解支持。</p> </li> 
 <li> <p>简化的批处理操作。</p> </li> 
 <li> <p>简化的分页操作。</p> </li> 
 <li> <p>灵活的链式查询 API 和 SQL 构造器以及 SQL 注解。</p> </li> 
 <li> <p>实体属性动态映射。</p> </li> 
 <li> <p>支持多种数据库（mysql,mariadb,oracle,sqlserver,postgresql,db2,sqlite,hsqldb)</p> </li> 
</ol> 
<p style="text-align:left">maven 坐标</p> 
<pre style="text-align:left"><span style="background-color:#efefef"><span style="color:#333333"><</span></span><strong><span style="color:#333333"><span style="color:#22863a">dependency</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>
    <span style="background-color:#efefef"><span style="color:#333333"><</span></span><strong><span style="color:#333333"><span style="color:#22863a">groupId</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>cn.xphsc<span style="background-color:#efefef"><span style="color:#333333"></</span></span><strong><span style="color:#333333"><span style="color:#22863a">groupId</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>
    <span style="background-color:#efefef"><span style="color:#333333"><</span></span><strong><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>easyjdbc<span style="background-color:#efefef"><span style="color:#333333"></</span></span><strong><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>
    <span style="background-color:#efefef"><span style="color:#333333"><</span></span><strong><span style="color:#333333"><span style="color:#22863a">version</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>2.1.0<span style="background-color:#efefef"><span style="color:#333333"></</span></span><strong><span style="color:#333333"><span style="color:#22863a">version</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span>
<span style="background-color:#efefef"><span style="color:#333333"></</span></span><strong><span style="color:#333333"><span style="color:#22863a">dependency</span></span></strong><span style="background-color:#efefef"><span style="color:#333333">></span></span></pre> 
<p style="text-align:left">spring boot 坐标</p> 
<pre style="text-align:left"><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"><</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"><</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>cn.xphsc.boot<span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"></</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"><</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>easyjdbc-spring-boot-starter<span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"></</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"><</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>2.1.0<span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"></</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span>
<span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333"></</span></span></span><strong><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></strong><span style="background-color:#efefef"><span style="color:#333333"><span style="color:#333333">></span></span></span></pre> 
<h1 style="text-align:left">更新日志</h1> 
<h2 style="text-align:left">Changes in version 2.1.0</h2> 
<ul> 
 <li style="text-align:left">添加支持使用注解@daoscan注册easyjddbc dao接口</li> 
</ul> 
<div style="text-align:left"> 
 <ul> 
  <li>将easyjdbc Daos的默认注解@easydao更改为@Dao接口</li> 
  <li>默认情况下，支持用于easyjdbc dao接口的注解Dao和注解@Repository接口</li> 
  <li>添加支持jdk8的日期类型instant，offsetdatetime，offsettime，year</li> 
  <li>支持数据库，如“Derby”、' Derby ',' Phoenix(phoenix) '达梦数据库 database (dm), 阿里云 PPAS 数据库 database(edb), 神通数据库 database(oscar), herddb(herddb)</li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            