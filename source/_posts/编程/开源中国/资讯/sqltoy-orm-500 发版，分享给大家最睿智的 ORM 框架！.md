
---
title: 'sqltoy-orm-5.0.0 发版，分享给大家最睿智的 ORM 框架！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp'
author: 开源中国
comments: false
date: Wed, 30 Jun 2021 02:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp'
---

<div>   
<div class="content">
                                                                    
                                                        <ul> 
 <li style="text-align:justify"> <p style="text-align:left"><strong>写在开头</strong></p> </li> 
</ul> 
<p style="text-align:left">    sagacity-sqltoy 是JPA+超强查询有机融合体，是个人长期项目实践的归纳总结，极为注重项目过程实践，尤其是项目痛点,如：sql注入、动态条件sql编写、树形结构查询、sql跨数据库、查询性能极致优化、极致的分页查询、涉及统计分析的行列转换、分组汇总计算等等，都有极为独特的解决策略！</p> 
<p style="text-align:left">    感谢广大网络用户的支持和反馈，sagacity-sqltoy5.0 在拥有良好特性的基础上进一步完善了代码结构，必将更好的为大家的选择提供坚实的支撑！</p> 
<ul> 
 <li style="text-align:justify"> <p style="text-align:left"><strong>开源地址：</strong></p> </li> 
 <li>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenrenfei%2Fsagacity-sqltoy" target="_blank">https://github.com/sagframe/sagacity-sqltoy</a></li> 
 <li>gitee: <a href="https://gitee.com/sagacity/sagacity-sqltoy">https://gitee.com/sagacity/sagacity-sqltoy</a></li> 
 <li>idea 插件(可直接在idea中检索安装):  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fthreefish%2Fsqltoy-idea-plugins" target="_blank">https://github.com/threefish/sqltoy-idea-plugins</a></li> 
 <li style="text-align:justify"> <p style="text-align:left"><strong>更新内容</strong></p> </li> 
</ul> 
<p>1. 规整4.x版本的代码目录，使其更加科学</p> 
<ul> 
 <li>去除executor目录，将QueryExecutor 对外的模型统一移入model目录下面</li> 
 <li>将非对外的内部模型移入到model.inner 包下面，将一些配置化的模型移入到config.model下面</li> 
</ul> 
<p>2. 将PaginationModel 改为Page，并将PageNo 由Long改为long，避免需要写1L，简化书写<br> 3. 优化support下面的LinkSupport，BaseSupport</p> 
<ul> 
 <li>剔除掉LinkSupport和BaseSupport，合并到SqlToyDaoSupport</li> 
</ul> 
<p>4. 去除一些根本用不到的方法，避免产生疑问和混淆，使得SqlToyDao更加清晰</p> 
<ul> 
 <li>去除updateFetchTop、updateFetchRandom</li> 
 <li>去除：public Long executeSql(String sqlOrNamedSql, Serializable entity, ReflectPropsHandler reflectPropertyHandler)带有reflectPropertyHandler 的开放方法</li> 
</ul> 
<p>5. 去除@ListSql  @PageSql @LoadSql 这些注解，尽量让使用方法归一<br> 6. 去除ObtainDataSource，避免跟DataSourceSelector产生功能重叠<br> 7. 将ConnectonFactory移入org.sagacity.sqltoy.plugins.datasource包下<br> 8. 剔除findAll方法，用findEntity(Class voClass,null) 代替findAll方法属于极小众方法<br> 9. 并行查询设置分页模型方法：pageMode(Pagination pageModel)改为page(Page page)<br> 10. 增加loadEntity方法，通过EntityQuery获得单条记录：</p> 
<pre><code class="language-java"> public <T extends Serializable> T loadEntity(Class<T> entityClass, EntityQuery entityQuery);
</code></pre> 
<p>11. 增加numFmt（numberFormat) 对英文金额转大写的支持</p> 
<pre><code class="language-xml">   <number-format columns="total_amt" format="capital-en"/>
</code></pre> 
<p>12. 删除对SybaseIQ数据库的支持<br> 13. 优化部分不使用的代码和注释</p> 
<h1>4.x 升级5.0 修改点</h1> 
<ul> 
 <li>分页查询PaginationModel 类改为Page</li> 
 <li>org.sagacity.sqltoy.executor.QueryExecutor 改为 org.sagacity.sqltoy.model.QueryExecutor</li> 
 <li><strong>拥有JPA模式的对象CRUD</strong></li> 
</ul> 
<p>对象式CRUD是ORM框架的基本共识，这里不做更多介绍。</p> 
<ul> 
 <li style="text-align:left"><strong>超强查询</strong>：最理想的状态就是：第一在数据库客户端调试好的sql 最直观高效的移入项目工程中；第二、在需求变化时最简单快速的可以从工程中放入数据库客户端中进行调试。也就是说要最大限度的保持sql的原始面貌；</li> 
</ul> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-7bf9649420e381d2ae4fe673c2890fe39eb.bmp" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-968e45d6d4552b9099301c18efa933f8226.png" referrerpolicy="no-referrer"></p> 
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
                                        </div>
                                      
</div>
            