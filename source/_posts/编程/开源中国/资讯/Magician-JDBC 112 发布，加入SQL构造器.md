
---
title: 'Magician-JDBC 1.1.2 发布，加入SQL构造器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=986'
author: 开源中国
comments: false
date: Sat, 08 May 2021 14:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=986'
---

<div>   
<div class="content">
                                                                    
                                                        <p>此次更新 主要是加入了一个新特性：SQL构造器。方便在单表操作的时候无需写sql</p> 
<h2>一、具体应用如下</h2> 
<h3 style="text-align:start">查询数据</h3> 
<pre><code class="language-java">// 根据主键查询，可以这样构建sql
String sql = SqlBuilder.select("表名").byPrimaryKey("主键名").builder();

// 自定义查询条件，可以这样构建
String sql = SqlBuilder.select("表名").where("表字段名 = #&#123;参数字段名&#125;").builder();

// 自定义查询字段，可以这样构建(column传入的类里面的属性就是要查询的字段)
String sql = SqlBuilder.select("表名").column(DemoDTO.class).where("表字段名 = #&#123;参数字段名&#125;").builder();

DemoDTO param = new DemoDTO();
param.setId(102);

DemoDTO demoDTO = JdbcTemplate.create().selectOne(sql, param, DemoDTO.class);</code></pre> 
<ul> 
 <li>column里面的实体类，如果想排除某个字段 可以在要排除的字段上加上JsonIgnore注解</li> 
 <li>sql构造器，delete，update，select 均可选择byPrimaryKey与where之一</li> 
 <li>以上两条，下面的单表操作相同</li> 
</ul> 
<h3 style="text-align:start">修改数据</h3> 
<pre><code class="language-java">// 构建sql(column传入的类里面的属性就是要修改的字段)
String sql = SqlBuilder.update("表名").column(DemoDTO.class).where("表字段名 = #&#123;参数字段名&#125;").builder();

DemoDTO param = new DemoDTO();
param.setCreateTime(new Date());
param.setName("testName");
param.setId(105);

JdbcTemplate.create().update(sql, param);</code></pre> 
<h3 style="text-align:start">插入数据</h3> 
<pre><code class="language-java">// 构建sql(column传入的类里面的属性就是要插入的字段)
String sql = SqlBuilder.insert("表名").column(DemoDTO.class).builder();

DemoDTO param = new DemoDTO();
param.setCreateTime(new Date());
param.setName("testName");

JdbcTemplate.create().update(sql, param);</code></pre> 
<h3 style="text-align:start">删除数据</h3> 
<pre><code class="language-java">String sql = SqlBuilder.delete("表名").where("表字段名 = #&#123;参数字段名&#125;").builder();

DemoDTO param = new DemoDTO();
param.setId(107);
JdbcTemplate.create().update(sql, param);</code></pre> 
<h2>二、更多特性可以访问官网查看</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmagician-io.com%2F" target="_blank">http://magician-io.com</a></p>
                                        </div>
                                      
</div>
            