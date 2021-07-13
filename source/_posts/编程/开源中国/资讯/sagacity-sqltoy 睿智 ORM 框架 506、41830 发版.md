
---
title: 'sagacity-sqltoy 睿智 ORM 框架 5.0.6、4.18.30 发版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp'
author: 开源中国
comments: false
date: Tue, 13 Jul 2021 11:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><strong>开源地址：</strong></p> 
<ul> 
 <li>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenrenfei%2Fsagacity-sqltoy" target="_blank">https://github.com/sagframe/sagacity-sqltoy</a></li> 
 <li>gitee: <a href="https://gitee.com/sagacity/sagacity-sqltoy">https://gitee.com/sagacity/sagacity-sqltoy</a></li> 
 <li>idea 插件(可直接在idea中检索安装):  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthreefish%2Fsqltoy-idea-plugins" target="_blank">https://github.com/threefish/sqltoy-idea-plugins</a></li> 
</ul> 
<p style="text-align:left"><strong>更新内容</strong></p> 
<p style="text-align:left">1.优化执行带有缓存翻译的查询，在首次执行时因获取缓存影响当前sql执行后台日志输出问题（建议升级，以免单元测试时产生对日志的困惑）！</p> 
<p style="text-align:left">感谢网友的反馈，sqltoy及时发版进行修正</p> 
<h1 style="text-align:left"><span style="color:#c0392b"><strong>sqltoy特点介绍：</strong></span></h1> 
<ul> 
 <li><strong>sqltoy最佳sql编写模式，便于开发和后期维护</strong></li> 
</ul> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-968e45d6d4552b9099301c18efa933f8226.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:left"><strong>sqltoy的缓存翻译，大幅减少表关联简化sql，让你的查询性能成几何级提升</strong></li> 
</ul> 
<p style="text-align:left"><img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/85287e14aa3e428fbabe297472596455?from=pc" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:left"><strong>极致的分页，同样帮助你实现查询的性能大幅提升</strong></li> 
</ul> 
<ol> 
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
<ul> 
 <li style="text-align:start"><strong>便利的跨数据库统计计算：数据旋转</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/949bc75b5c53441c98284dae2bed11fe?from=pc" referrerpolicy="no-referrer">
</div> 
<ul> 
 <li><strong>便利的跨数据库统计计算：无限极分组统计(含汇总求平均)</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/f5edc52adbbe4a1ca327d9a9b0c5d64c?from=pc" referrerpolicy="no-referrer">
</div> 
<ul> 
 <li><strong>便利的跨数据库统计计算：同比环比</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/b9d435e2852644c9a4c9e062cc3d46d7?from=pc" referrerpolicy="no-referrer">
</div>
                                        </div>
                                      
</div>
            