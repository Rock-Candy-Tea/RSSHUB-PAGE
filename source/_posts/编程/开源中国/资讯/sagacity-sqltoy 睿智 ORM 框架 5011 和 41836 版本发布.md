
---
title: 'sagacity-sqltoy 睿智 ORM 框架 5.0.11 和 4.18.36 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a056422b84c198968931a100095e8210048.png'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 11:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a056422b84c198968931a100095e8210048.png'
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
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">1、优化重复sqlId的提示和处理</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">2、升级pom依赖版本</span></p> 
<ul> 
 <li style="text-align:left"><strong><span style="background-color:#ffffff; color:#40485b">sqltoy的关键优势：</span></strong></li> 
</ul> 
<pre><code class="language-java">//------------------了解 sqltoy的关键优势: -------------------------------------------------------------------------------------------*/
//1、最简最直观的sql编写方式(不仅仅是查询语句)，采用条件参数前置处理规整法，让sql语句部分跟客户端保持高度一致
//2、sql中支持注释(规避了对hint特性的影响,知道hint吗?搜oracle hint)，和动态更新加载，便于开发和后期维护整个过程的管理
//3、支持缓存翻译和反向缓存条件检索(通过缓存将名称匹配成精确的key)，实现sql简化和性能大幅提升
//4、支持快速分页和分页优化功能，实现分页最高级别的优化，同时还考虑到了cte多个with as情况下的优化支持
//5、支持并行查询
//6、根本杜绝sql注入问题
//7、支持行列转换、分组汇总求平均、同比环比计算，在于用算法解决复杂sql，同时也解决了sql跨数据库问题
//8、支持保留字自动适配
//9、支持跨数据库函数自适配,从而非常有利于一套代码适应多种数据库便于产品化,比如oracle的nvl，当sql在mysql环境执行时自动替换为ifnull
//10、支持分库分表
//11、提供了取top、取random记录、树形表结构构造和递归查询支持、updateFetch单次交互完成修改和查询等实用的功能
//12、sqltoy的update、save、saveAll、load 等crud操作规避了jpa的缺陷,参见update(entity,String...forceUpdateProps)和updateFetch
//13、提供了极为人性化的条件处理：排它性条件、日期条件加减和提取月末月初处理等
//14、提供了查询结果日期、数字格式化、安全脱敏处理，让复杂的事情变得简单，大幅简化sql或结果的二次处理工作
//-----------------------------------------------------------------------------------*/</code></pre> 
<p style="text-align:start"><strong>sqltoy特点介绍：</strong></p> 
<ul> 
 <li style="text-align:start"><strong>JPA式的crud是基本共识，但sqltoy改进了update，增加了updateFetch</strong></li> 
</ul> 
<p style="text-align:start"><strong><img alt height="673" src="https://oscimg.oschina.net/oscnet/up-a056422b84c198968931a100095e8210048.png" width="771" referrerpolicy="no-referrer"></strong></p> 
<ul> 
 <li style="text-align:start"><strong>sqltoy的update、updateAll，弹性设置强制修改属性，一次性数据库交互，解决并发问题</strong></li> 
</ul> 
<pre><code class="language-java">/**
 * @todo 修改数据并返回数据库记录变更数量(非强制修改属性，当属性值为null不参与修改)
 * @param entity
 * @param forceUpdateProps 强制修改的字段属性
 * @return Long 数据库记录变更量(插入数据量)
 */
public Long update(Serializable entity, String... forceUpdateProps);

/**
 * @TODO 批量修改操作，并可以指定强制修改的属性(非强制修改属性，当属性值为null不参与修改)
 * @param <T>
 * @param entities
 * @param forceUpdateProps
 * @return Long 数据库记录变更量(插入数据量)
 */
public <T extends Serializable> Long updateAll(List<T> entities, String... forceUpdateProps);

//保存或修改数据并返回数据库记录变更数量
public Long saveOrUpdate(Serializable entity, String... forceUpdateProps);</code></pre> 
<ul> 
 <li style="text-align:start"><strong>updateFetch: 一次交互完成锁查询、修改，并返回修改后的结果，尤其适用于库存台账、资金台账场景</strong></li> 
</ul> 
<pre><code class="language-java">// sqltoy的updateFetch是jpa没有的，可以深入了解其原理，一次交互完成查询、锁定、修改并返回修改后结果
/**
 * @todo 获取并锁定数据并进行修改(只支持针对单表查询，查询语句要简单)
 * @param queryExecutor
 * @param updateRowHandler
 * @return
 */
public List updateFetch(final QueryExecutor queryExecutor, final UpdateRowHandler updateRowHandler);</code></pre> 
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
            