
---
title: 'sqltoy-orm-4.18.22 发版，还在坚持 mybatis(plus) 吗？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-79df40c2507d956c9000ad54e6216704cd8.bmp'
author: 开源中国
comments: false
date: Fri, 28 May 2021 21:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-79df40c2507d956c9000ad54e6216704cd8.bmp'
---

<div>   
<div class="content">
                                                                    
                                                        <ul> 
 <li style="text-align:justify"> <p style="text-align:left"><strong>开源地址：</strong></p> </li> 
 <li>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenrenfei%2Fsagacity-sqltoy" target="_blank">https://github.com/sagframe/sagacity-sqltoy</a></li> 
 <li>gitee: <a href="https://gitee.com/sagacity/sagacity-sqltoy">https://gitee.com/sagacity/sagacity-sqltoy</a></li> 
 <li>idea 插件(可直接在idea中检索安装):  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthreefish%2Fsqltoy-idea-plugins" target="_blank">https://github.com/threefish/sqltoy-idea-plugins</a></li> 
 <li style="text-align:justify"> <p style="text-align:left"><strong>更新内容</strong></p> </li> 
</ul> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">1、在findEntity中EntityQuery可以设置fetchSize，在sqltoyContext中可以全局设置fetchSize，实现查询数据提取的性能</span><br> <span style="background-color:#ffffff; color:#40485b">2、</span><span style="background-color:#ffffff; color:#40485b">针对一些特殊原因导致表名是数据库关键词场景的兼容</span></p> 
<ul> 
 <li style="text-align:left"><strong>ORM的最佳形态：类JPA对象式操作+超强查询</strong></li> 
</ul> 
<ol> 
 <li style="text-align:left"><strong>jpa对象式操作</strong>：dao.save(entity)/saveAll(List<Entity>)/update(entity)/load(new Entity(id)) 模式,简单直接，对此大家基本能形成共识，也是各种ORM差异最小的。<strong>sqltoy在这个方面相信是对等的</strong>，因为是共识理论上来说不必要每次都提及！</li> 
</ol> 
<p style="text-align:left"><img alt height="712" src="https://oscimg.oschina.net/oscnet/up-79df40c2507d956c9000ad54e6216704cd8.bmp" width="721" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">2. <strong>超强查询</strong>：最理想的状态就是：第一在数据库客户端调试好的sql 最直观高效的移入项目工程中；第二、在需求变化时最简单快速的可以从工程中放入数据库客户端中进行调试。也就是说要最大限度的保持sql的原始面貌；</p> 
<p style="text-align:left">  <img alt height="800" src="https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp" width="1689" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt height="755" src="https://oscimg.oschina.net/oscnet/up-968e45d6d4552b9099301c18efa933f8226.png" width="1074" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:left"><strong>用ORM我们真真正正的痛点是什么？</strong></li> 
</ul> 
<p style="text-align:left">1、sql的编写和后期维护，上面的图例已经说明问题。</p> 
<p style="text-align:left"><strong>2、执行效率：当同样功能效率有几倍差距时其实就是天地之别了，带来的直接效果就是：一边是用户的高度夸赞、一边是用户的鄙视，您能理解这是什么差距吗？</strong></p> 
<ul> 
 <li style="text-align:left"><strong>sqltoy的缓存翻译，大幅减少表关联简化sql，让你的查询性能成几何级提升</strong></li> 
</ul> 
<p style="text-align:left"><img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/85287e14aa3e428fbabe297472596455?from=pc" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:left">极致的分页，同样帮助你实现查询的性能大幅提升</li> 
</ul> 
<ol> 
 <li style="text-align:justify">快速分页:@fast() 实现先取单页数据然后再关联查询，极大提升速度</li> 
 <li style="text-align:justify">分页优化器:page-optimize 让分页查询由两次变成1.3~1.5次(用缓存实现相同查询条件的总记录数量在一定周期内无需重复查询</li> 
 <li style="text-align:justify">sqltoy的分页取总记录的过程不是简单的select count(1) from (原始sql)；而是智能判断是否变成:select count(1) from 'from后语句'， 并自动剔除最外层的order by</li> 
 <li style="text-align:justify">sqltoy支持并行查询：parallel="true"，同时查询总记录数和单页数据,大幅提升性能</li> 
 <li style="text-align:justify">在极特殊情况下sqltoy分页考虑是最优化的，如:with t1 as (),t2 as @fast(select * from table1) select * from xxx 这种复杂查询的分页的处理，sqltoy的count查询会是:with t1 as () select count(1) from table1, 如果是:with t1 as @fast(select * from table1) select * from t1 ,count sql 就是：select count(1) from table1</li> 
</ol> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p6-tt.byteimg.com/origin/pgc-image/3d5f7094da154671985dd390f56f6302?from=pc" referrerpolicy="no-referrer">
</div> 
<div style="text-align:start">
  
</div> 
<ul> 
 <li style="text-align:start"><strong>做过统计分析的您，害怕数据旋转吗？害怕同比环比吗？</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/949bc75b5c53441c98284dae2bed11fe?from=pc" referrerpolicy="no-referrer"> 
 <p> </p> 
</div> 
<ul> 
 <li><strong>无限极分组统计(含汇总求平均)，算法配置简单又跨数据库！</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/f5edc52adbbe4a1ca327d9a9b0c5d64c?from=pc" referrerpolicy="no-referrer"> 
 <p> </p> 
</div> 
<ul> 
 <li><strong>同比环比</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/b9d435e2852644c9a4c9e062cc3d46d7?from=pc" referrerpolicy="no-referrer">
</div> 
<ul> 
 <li><strong>sqltoy还有什么？</strong></li> 
</ul> 
<p><strong>     因为篇幅原因，这里不过多展开，我相信您想要的，在sqltoy中基本都可以找到满意的答案！比如：分库分表、树形数据处理、sql跨数据库等等！</strong></p> 
<ul> 
 <li><strong>致谢</strong></li> 
</ul> 
<p><strong>     感谢广大网友的支持，提出宝贵的反馈意见，sqltoy的一步步的成熟是大家直觉式的眼光和敢于试错的精神加入到sqltoy这个还处于发展中的小众框架用户群体中来，让我们一起来让其成熟发展服务于更多的用户！也祝愿sqltoy可以帮助到大家，愿大家可以工作生活平衡！</strong></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"> </p>
                                        </div>
                                      
</div>
            