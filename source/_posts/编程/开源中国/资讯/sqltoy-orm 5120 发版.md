
---
title: 'sqltoy-orm 5.1.20 发版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b2fd6e30c83f9e805107db11fdc5d8d9e6b.png'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 13:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b2fd6e30c83f9e805107db11fdc5d8d9e6b.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>开源地址：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenrenfei%2Fsagacity-sqltoy" target="_blank">https://github.com/sagframe/sagacity-sqltoy</a></li> 
 <li>gitee: <a href="https://gitee.com/sagacity/sagacity-sqltoy">https://gitee.com/sagacity/sagacity-sqltoy</a></li> 
 <li>idea 插件(可直接在idea中检索安装):  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthreefish%2Fsqltoy-idea-plugins" target="_blank">https://github.com/threefish/sqltoy-idea-plugins</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新内容</strong></p> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#40485b">1、升级log4j2依赖版本为2.15.0</span><br> <span style="background-color:#ffffff; color:#40485b">2、sql补全优化，如from table where xxx 情况下自动补全select *</span><br> <span style="background-color:#ffffff; color:#40485b">3、增加一些容错校验判断</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff; color:#40485b">周末因个别用户使用偌依(ruoyi)集成sqltoy，修改了一个简单的字典类别查询，真是由衷的感慨，都说java没有好的ORM框架，核心是mybatis代表了大家！</span></p> 
 <p style="margin-left:0; margin-right:0"><img alt height="957" src="https://oscimg.oschina.net/oscnet/up-b2fd6e30c83f9e805107db11fdc5d8d9e6b.png" width="1265" referrerpolicy="no-referrer"></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>sqltoy特点介绍：</strong></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li style="text-align:start"><strong>sqltoy的核心构建思想</strong></li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="868" src="https://oscimg.oschina.net/oscnet/up-a385d72ceb030d705e8e5803ca3cd4c09a1.png" width="1136" referrerpolicy="no-referrer"></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li style="text-align:start"><strong>sqltoy的对比mybatis(plus)和fluent mybatis的核心点：查询语句编写、可阅读性、可维护性</strong></li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong><img alt height="988" src="https://oscimg.oschina.net/oscnet/up-93bc88150c80aed200b6ff7d95c9c7bd7df.png" width="1797" referrerpolicy="no-referrer"></strong></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong><img alt height="945" src="https://oscimg.oschina.net/oscnet/up-abc5180de641a848bcd97939eb2b0f06e5d.png" width="1786" referrerpolicy="no-referrer"></strong></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li style="text-align:start"><strong>对象化crud是基础，但sqltoy有针对性的改进：update、updateSaveFetch、updateFetch等</strong></li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><img alt height="845" src="https://oscimg.oschina.net/oscnet/up-6b8e8204061eec3d2096a50e9899548351e.png" width="1745" referrerpolicy="no-referrer"></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li style="text-align:left"><strong>sqltoy的缓存翻译，大幅减少表关联简化sql，让你的查询性能成几何级提升</strong></li> 
 </ul> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    除xml配置模式外，也支持注解模式</p> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java">@<span style="color:#d73a49">Translate</span>(<span style="color:#d73a49">cacheName</span> = <span style="color:#032f62">"dictKeyName"</span>, cacheType = <span style="color:#032f62">"DEVICE_TYPE"</span>, keyField = <span style="color:#032f62">"deviceType"</span>)
private String deviceTypeName;

@<span style="color:#d73a49">Translate</span>(<span style="color:#d73a49">cacheName</span> = <span style="color:#032f62">"staffIdName"</span>, keyField = <span style="color:#032f62">"staffId"</span>)
private String staffName;</code></pre> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/85287e14aa3e428fbabe297472596455?from=pc" referrerpolicy="no-referrer"></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li style="text-align:left"><strong>极致的分页，同样帮助你实现查询的性能大幅提升</strong></li> 
 </ul> 
 <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
  <li style="text-align:justify">快速分页:@fast() 实现先取单页数据然后再关联查询，极大提升速度</li> 
  <li style="text-align:justify">分页优化器:page-optimize 让分页查询由两次变成1.3~1.5次(用缓存实现相同查询条件的总记录数量在一定周期内无需重复查询</li> 
  <li style="text-align:justify">sqltoy的分页取总记录的过程不是简单的select count(1) from (原始sql)；而是智能判断是否变成:select count(1) from 'from后语句'， 并自动剔除最外层的order by</li> 
  <li style="text-align:justify">sqltoy支持并行查询：parallel="true"，同时查询总记录数和单页数据,大幅提升性能</li> 
 </ol> 
 <div style="text-align:start">
  <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p6-tt.byteimg.com/origin/pgc-image/3d5f7094da154671985dd390f56f6302?from=pc" referrerpolicy="no-referrer">
 </div> 
 <div style="text-align:start">
   
 </div> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li style="text-align:start"><strong>便利的跨数据库统计计算：数据旋转</strong></li> 
 </ul> 
 <div style="text-align:start">
  <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/949bc75b5c53441c98284dae2bed11fe?from=pc" referrerpolicy="no-referrer">
 </div> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><strong>便利的跨数据库统计计算：无限极分组统计(含汇总求平均)</strong></li> 
 </ul> 
 <div style="text-align:start">
  <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/f5edc52adbbe4a1ca327d9a9b0c5d64c?from=pc" referrerpolicy="no-referrer">
 </div> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><strong>便利的跨数据库统计计算：同比环比</strong></li> 
 </ul> 
 <div style="text-align:start">
  <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/b9d435e2852644c9a4c9e062cc3d46d7?from=pc" referrerpolicy="no-referrer">
 </div> 
</div>
                                        </div>
                                      
</div>
            