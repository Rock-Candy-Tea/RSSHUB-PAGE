
---
title: 'sqltoy-orm 4.18.13 发版，您还在坚持 mybatis(plus) 吗？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p1-tt.byteimg.com/origin/pgc-image/54e0050264174aa7b84b12780194a2ac?from=pc'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 09:41:00 GMT
thumbnail: 'https://p1-tt.byteimg.com/origin/pgc-image/54e0050264174aa7b84b12780194a2ac?from=pc'
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
<p style="text-align:left">1、 <span style="background-color:#ffffff; color:#40485b">增加DataSourceSelector，为多数据源场景下使用其他开源插件如dynamic-datasource等提供扩展</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">2、升级依赖包版本</span></p> 
<ul> 
 <li style="text-align:justify"><strong><span style="color:#ff5e5e">心中理想的ORM框架应该是什么？</span></strong></li> 
</ul> 
<p style="text-align:start">个人的观念是：<strong>JPA<span style="color:#ff5e5e">+</span>更加灵活高效的sql组织和执行机制</strong>，任何单独强调jpa和mybatis都是有失偏颇的。</p> 
<p style="text-align:start">1、互联网项目很多人认为JPA就足够了(常问jpa够好了为什么有人还在鼓吹mybatis)，忽视了面向管理端和数据统计分析时场景的复杂性，有人说jpa有qsl也可以写原生sql，但真的还不够强!</p> 
<p style="text-align:start">2、ToB的项目很多人认为mybatis灵活便于sql优化，但希望普通的单表操作能跟jpa一样，因此产生了mybatis的各种plus，甚至plus plus！</p> 
<p style="text-align:start">3、更有甚者：强调jooq模式用对象实现sql，<strong>简单查询的对象式并无过错</strong>，但复杂的其实就矫枉过正了，sql本身就是一个普世的语言，在客户端调试完再转成java对象模式，修改的时候再转成sql再调试，这种过程本质而言就是自虐，开发懂sql、产品懂sql、测试懂sql，变成对象模式就只有开发自己懂！</p> 
<p style="text-align:start"><span style="color:#e74c3c"><strong>总之：我们希望有JPA那种对象式的简单直接，也想要有sql的灵活高效</strong></span>。</p> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy-orm 正是为解决上述问题而产生的</strong></li> 
</ul> 
<p style="text-align:start">1、sqltoy有jpa式的对象操作，且针对jpa的一些不足进行了加强</p> 
<p style="text-align:start">2、sqltoy的sql 充分考虑了开发、调试、变更、后期维护的全过程，让sql更加接近于客户端调试完的结果</p> 
<p style="text-align:start">3、sqltoy不是简单地重复jpa和优化mybatis，而是针对性能优化和统计分析提供了独特新颖的解决思路，你会第一次了解到缓存翻译、分页优化、快速分页、并行查询、行列转换等极为有帮助的特性(当然分库分表等人人皆知的功能自然也是支持的)。</p> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy的对象操作介绍，通过框架中的SqlToyLazyDao完成交互</strong></li> 
</ul> 
<pre style="text-align:left"><code>   StaffInfoVO staffInfo = <span style="color:#114ba6"><span style="color:#d73a49">new</span></span> StaffInfoVO(); 
   <span style="color:#999999"><span style="color:#6a737d">//保存</span></span>
   sqlToyLazyDao.save(staffInfo);
   <span style="color:#999999"><span style="color:#6a737d">//删除</span></span>
   sqlToyLazyDao.<span style="color:#114ba6"><span style="color:#d73a49">delete</span></span>(<span style="color:#114ba6"><span style="color:#d73a49">new</span></span> StaffInfoVO(<span style="color:#00753b"><span style="color:#032f62">"S2007"</span></span>));

<span style="color:#999999"><span style="color:#6a737d">//update 针对jpa的缺陷进行了改进</span></span>
   <span style="color:#999999"><span style="color:#6a737d">//public Long update(Serializable entity, String... forceUpdateProps);</span></span>
   <span style="color:#999999"><span style="color:#6a737d">// 这里对photo 属性进行强制修改，其他为null自动会跳过</span></span>
   sqlToyLazyDao.update(staffInfo, <span style="color:#00753b"><span style="color:#032f62">"photo"</span></span>);

   <span style="color:#999999"><span style="color:#6a737d">//深度修改,不管是否null全部字段修改</span></span>
   sqlToyLazyDao.updateDeeply(staffInfo);

   List<StaffInfoVO> staffList = <span style="color:#114ba6"><span style="color:#d73a49">new</span></span> ArrayList<StaffInfoVO>();
   StaffInfoVO staffInfo = <span style="color:#114ba6"><span style="color:#d73a49">new</span></span> StaffInfoVO();
   StaffInfoVO staffInfo1 = <span style="color:#114ba6"><span style="color:#d73a49">new</span></span> StaffInfoVO();
   staffList.add(staffInfo);
   staffList.add(staffInfo1);
   <span style="color:#999999"><span style="color:#6a737d">//批量保存或修改</span></span>
   sqlToyLazyDao.saveOrUpdateAll(staffList);
   <span style="color:#999999"><span style="color:#6a737d">//批量保存</span></span>
   sqlToyLazyDao.saveAll(staffList);
   ...............
   sqlToyLazyDao.loadByIds(StaffInfoVO.class,<span style="color:#00753b"><span style="color:#032f62">"S2007"</span></span>)
   <span style="color:#999999"><span style="color:#6a737d">//唯一性验证</span></span>
   sqlToyLazyDao.isUnique(staffInfo, <span style="color:#00753b"><span style="color:#032f62">"staffCode"</span></span>);
   
   <span style="color:#999999"><span style="color:#6a737d">//提供了独特的updateFetch功能，查询、锁定、修改并返回修改后的结果</span></span>
   <span style="color:#999999"><span style="color:#6a737d">// 适用于高并发、高度一致性场景，如:库存台账、财务资金帐实时扣减、叠加等</span></span>
   <span style="color:#8a7304"><span style="color:#114ba6"><span style="color:#d73a49">public</span></span> List <span style="color:#a82e2e"><span style="color:#6f42c1">updateFetch</span></span>(<span style="color:#114ba6">final</span> QueryExecutor queryExecutor, <span style="color:#114ba6">final</span> UpdateRowHandler updateRowHandler)</span>;</code></pre> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy支持代码中对象查询和直接写sql</strong></li> 
</ul> 
<pre style="text-align:left"><code> <span style="color:#999999"><span style="color:#6a737d">// sqltoy中统一的规则是xml中的sqlId 或者直接传具体的sql语句，而不是only xml</span></span>
 <span style="color:#114ba6"><span style="color:#d73a49">public</span></span> <T extends Serializable> <span style="color:#8a7304">List<T> <span style="color:#a82e2e"><span style="color:#6f42c1">findBySql</span></span>(<span style="color:#114ba6"><span style="color:#d73a49">final</span></span> String sqlOrNamedSql, <span style="color:#114ba6"><span style="color:#d73a49">final</span></span> T entity)</span>;</code></pre> 
<pre style="text-align:left"><code><span style="color:#999999"><span style="color:#6a737d">//带缓存翻译的代码中动态条件查询，xml中的功能用代码基本都可以实现，xml一般用于复杂查询</span></span>
<span style="color:#114ba6"><span style="color:#d73a49">public</span></span> PaginationModel<StaffInfoVO> findStaff(PaginationModel<StaffInfoVO> pageModel, StaffInfoVO staffInfoVO) &#123;
     <span style="color:#114ba6"><span style="color:#d73a49">return</span></span> sqlToyLazyDao.findEntity(StaffInfoVO.<span style="color:#114ba6"><span style="color:#d73a49">class</span></span>, <span style="color:#a82e2e"><span style="color:#d73a49">pageModel</span></span>, <span style="color:#a82e2e"><span style="color:#d73a49">EntityQuery.create</span></span>()
                          .<span style="color:#114ba6"><span style="color:#d73a49">where</span></span>(<span style="color:#00753b"><span style="color:#032f62">"#[staffName like :staffName]#[and createTime>=:beginDate]#[and createTime<=:endDate]"</span></span>)
                          .values(staffInfoVO)
                           <span style="color:#999999"><span style="color:#6a737d">// 将性别代码通过缓存转变成中文名称                    </span></span>
                          .translates(new Translate(<span style="color:#00753b"><span style="color:#032f62">"dictKeyName"</span></span>).setColumn(<span style="color:#00753b"><span style="color:#032f62">"sexTypeName"</span></span>)
                                      .setCacheType(<span style="color:#00753b"><span style="color:#032f62">"SEX_TYPE"</span></span>).setKeyColumn(<span style="color:#00753b"><span style="color:#032f62">"sexType"</span></span>))
                            <span style="color:#999999"><span style="color:#6a737d">//通过缓存显示员工所在机构的名称</span></span>
                          .translates(new Translate(<span style="color:#00753b"><span style="color:#032f62">"organIdName"</span></span>).setColumn(<span style="color:#00753b"><span style="color:#032f62">"organName"</span></span>)
                                      .setKeyColumn(<span style="color:#00753b"><span style="color:#032f62">"organId"</span></span>)));
&#125;

<span style="color:#999999"><span style="color:#6a737d">//演示代码中非直接sql模式设置条件模式进行记录修改</span></span>
<span style="color:#114ba6"><span style="color:#d73a49">public</span></span> <span style="color:#114ba6">Long</span> updateByQuery() &#123;
     <span style="color:#114ba6"><span style="color:#d73a49">return</span></span> sqlToyLazyDao.updateByQuery(StaffInfoVO.<span style="color:#114ba6"><span style="color:#d73a49">class</span></span>,
<span style="color:#a82e2e"><span style="color:#d73a49">EntityUpdate.create</span></span>().<span style="color:#114ba6"><span style="color:#d73a49">set</span></span>(<span style="color:#00753b"><span style="color:#032f62">"createBy"</span></span>, <span style="color:#00753b"><span style="color:#032f62">"S0001"</span></span>)
                     .<span style="color:#114ba6"><span style="color:#d73a49">where</span></span>(<span style="color:#00753b"><span style="color:#032f62">"staffName like ?"</span></span>).values(<span style="color:#00753b"><span style="color:#032f62">"张"</span></span>));
&#125;

<span style="color:#999999"><span style="color:#6a737d">//代码中非直接sql模式设置条件模式进行记录删除</span></span>
sqlToyLazyDao.deleteByQuery(StaffInfoVO.<span style="color:#114ba6"><span style="color:#d73a49">class</span></span>, <span style="color:#a82e2e"><span style="color:#d73a49">EntityQuery.create</span></span>()
                            .<span style="color:#114ba6"><span style="color:#d73a49">where</span></span>(<span style="color:#00753b"><span style="color:#032f62">"status=?"</span></span>).values(<span style="color:#a82e2e">0</span>));</code></pre> 
<ul> 
 <li style="text-align:justify">通过上面的介绍说明sqltoy在常规的crud领域是跟jpa、mybatis(plus)对等的,一些细节因篇幅不做详细介绍，而不是only sql、only xml！因为下面的篇幅更多会以xml和sql形式表达,上面不铺垫一下容易误解sqltoy就必须是sql必须是xml。</li> 
 <li style="text-align:justify">sqltoy在sql编写方式上跟客户端(dbeaver) 上极为一致，让sql极为简洁、直观、便于后期维护</li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p1-tt.byteimg.com/origin/pgc-image/54e0050264174aa7b84b12780194a2ac?from=pc" referrerpolicy="no-referrer"> 
 <p style="text-align:center">sql编写模式上秒杀mybatis</p> 
</div> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy的缓存翻译极大的提升性能同时简化sql，性能还需要对比吗？</strong></li> 
</ul> 
<div style="text-align:start">
 <img alt="阐述sqltoy为什么秒杀mybatis(plus)" src="https://p3-tt.byteimg.com/origin/pgc-image/85287e14aa3e428fbabe297472596455?from=pc" referrerpolicy="no-referrer"> 
 <p style="text-align:center">将多表查询变成了单表查询，性能不秒杀mybatis？</p> 
</div> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy拥有极致的分页优化</strong></li> 
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
 <p> </p> 
</div> 
<ul> 
 <li style="text-align:justify"><strong>并行查询:同时执行多个查询，提升性能</strong></li> 
</ul> 
<pre style="text-align:left"><code>String[] paramNames = new String[] &#123; <span style="color:#00753b"><span style="color:#032f62">"userId"</span></span>, <span style="color:#00753b"><span style="color:#032f62">"defaultRoles"</span></span>, <span style="color:#00753b"><span style="color:#032f62">"deployId"</span></span>, <span style="color:#00753b"><span style="color:#032f62">"authObjType"</span></span> &#125;;
Object[] paramValues = new Object[] &#123; userId, defaultRoles, DEPLOY_ID,GROUP &#125;;

List<QueryResult<TreeModel>> list = <span style="color:#114ba6"><span style="color:#d73a49">super</span></span>.parallQuery(
Arrays.asList(
            ParallQuery.create().sql(<span style="color:#00753b"><span style="color:#032f62">"webframe_searchAllModuleMenus"</span></span>).resultType(TreeModel.<span style="color:#114ba6"><span style="color:#d73a49">class</span></span>),
    <span style="color:#a82e2e"><span style="color:#d73a49">ParallQuery.create</span></span>().sql(<span style="color:#00753b"><span style="color:#032f62">"webframe_searchAllUserReports"</span></span>).resultType(TreeModel.<span style="color:#114ba6"><span style="color:#d73a49">class</span></span>)),
<span style="color:#a82e2e"><span style="color:#d73a49">paramNames</span></span>, <span style="color:#a82e2e"><span style="color:#d73a49">paramValues);</span></span></code></pre> 
<ul> 
 <li><strong>数据旋转</strong></li> 
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
 <p> </p> 
</div> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy支持哪些数据库？</strong></li> 
</ul> 
<p style="text-align:start"><span style="color:#40485b">1、oracle 11g+</span></p> 
<p style="text-align:start"><span style="color:#40485b">2、db2 9.5+,建议从10.5 开始</span></p> 
<p style="text-align:start"><span style="color:#40485b">3、mysql(mariadb/innosql)支持5.6、5.7、8.0 版本</span></p> 
<p style="text-align:start"><span style="color:#40485b">4、postgresql(greenplum) 支持9.5 以及以上版本</span></p> 
<p style="text-align:start"><span style="color:#40485b">5、sqlserver 2012+</span></p> 
<p style="text-align:start"><span style="color:#40485b">6、sqlite</span></p> 
<p style="text-align:start"><span style="color:#40485b">7、DM达梦数据库</span></p> 
<p style="text-align:start"><span style="color:#40485b">8、elasticsearch 只支持查询,版本支持5.7+版本，建议使用7.3以上版本</span></p> 
<p style="text-align:start"><span style="color:#40485b">9、clickhouse、dorisdb</span></p> 
<p style="text-align:start"><span style="color:#40485b">10、oceanBase</span></p> 
<p style="text-align:start"><span style="color:#40485b">11、guassdb</span></p> 
<p style="text-align:start"><span style="color:#40485b">12、tidb</span></p> 
<p style="text-align:start"><span style="color:#40485b">13、kingbase</span></p> 
<p style="text-align:start"><span style="color:#40485b">14、mongodb (只支持查询)</span></p> 
<p style="text-align:start"><span style="color:#40485b">15、sybase_iq 支持15.4以上版本，建议使用16版本</span></p> 
<ul> 
 <li style="text-align:justify"><strong>sqltoy 还有什么特点？</strong></li> 
</ul> 
<p style="text-align:start">因为篇幅原因，关于其他的例如分库分表、跨数据库sql自适应、json类型支持等可通过sqltoy的文档深入了解。</p>
                                        </div>
                                      
</div>
            