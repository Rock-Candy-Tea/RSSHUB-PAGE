
---
title: 'QuickDAO 4.1.8 版本发布，实现 Oracle 分页操作以及大量细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1104'
author: 开源中国
comments: false
date: Wed, 04 Aug 2021 11:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1104'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">QuickDAO4.1.8版本已发布,可在maven中央仓库下载(阿里云仓库可能更新不及时),本次更新内容如下:</p> 
<p>友情提示:每次更新版本时通常在线文档也会同步更新.请注意查看文档页面时清空缓存,以便获取最新文档</p> 
<ul> 
 <li>[新增]Oracle分页操作支持,由于oracle分页的特殊性,调用分页方法后只能调用execute方法</li> 
 <li>[新增]DAOUtil工具类,支持同步两个数据库的表结构,支持数据库数据迁移</li> 
 <li>[新增]插入时和更新时设置字段值,例如数据库表需要设置插入或者更新记录的用户是谁时,就可以使用此方法</li> 
 <li>[新增]新增事务操作便捷方法startTransaction(Consumer<Transaction>)方法,免去需要编写提交事务和回滚的相关代码</li> 
 <li>[优化]新版本优化了大数据量时批量插入的方法效率,支持batch方式插入</li> 
 <li>[优化]根据数据库表生成java实体类方法,支持设置数据库列类型和java类型转换</li> 
 <li>[优化]简化初始化获取数据库表信息sql语句,解决数据库表较多时初始化速度慢的问题</li> 
 <li>[修复]解决初始化时重复获取数据库表信息问题</li> 
</ul> 
<h2 style="text-align:left"> </h2> 
<p>QuickDAO是一款简单易用的ORM框架,虽然市面上ORM框架已经非常多,但是有很多痛点这些框架并没有解决.QuickDAO相较于其他ORM框架的特点如下:</p> 
<h2 style="text-align:left">支持lambda表达式</h2> 
<p style="text-align:left">从版本4.1.4开始，查询API支持lambda查询</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2Flambda" target="_blank">lambda文档</a></p> 
<h2 style="text-align:left">支持外键关联操作</h2> 
<p style="text-align:left">虽然很多ORM框架宣称支持外键查询,但无一例外最终形式仍然是让开发者手写SQL语句.QuickDAO在API设计层面上支持外键关联查询,真正的无需手写多表关联查询SQL语句.</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2FjoinTable" target="_blank">外键关联查询文档</a></p> 
<h2 style="text-align:left">虚拟查询(无实体类查询)</h2> 
<p style="text-align:left">常规的ORM框架都需要建立实体类，然后再根据实体类来查询。QuickDAO支持无实体类查询，不用事先建立实体类也能够事先对数据库的查询,修改和删除.</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2Fvirtual" target="_blank">虚拟查询文档</a></p> 
<h2 style="text-align:left">事务操作</h2> 
<p style="text-align:left">QuickDAO实现了事务功能,事务相关API提供了QuickDAO其他数据库操作一样便利的API,对于复杂的事务操作需求,QuickDAO也能够满足</p> 
<p style="text-align:left"><a href="http://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Ftransaction%2Ftransaction">事务操作文档</a></p> 
<h2 style="text-align:left">子查询支持</h2> 
<p style="text-align:left">QuickDAO在API层面上支持子查询,您可以通过API直接拼接生成一个子查询SQL语句。这意味着即使是一些相当复杂的SQL语句，QuickDAO也能够轻松面对。</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2Fsubquery" target="_blank">子查询文档</a></p> 
<h2 style="text-align:left">自定义数据库列类型,索引等</h2> 
<p style="text-align:left">QuickDAO提供了实体注解，实体注解的类型丰富。通过实体注解，您可以定义数据库列的列名，列类型，列注释，表索引，非空，check约束等等等等。</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fconfig%2Fannotation" target="_blank">实体注解文档</a></p> 
<p style="text-align:left">最后,写这个框架的初衷是市面上已有的ORM框架不能解决开发中痛点.QuickDAO经过近2年的支持开发,目前已经迭代到4.X版本,也在个人项目,公司项目实际使用过.希望本人开发的QuickDAO框架能够为中国的开源事业贡献一份自己的力量.</p> 
<p style="text-align:left">QuickDAO文档: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn" target="_blank">https://quickdao.schoolwow.cn</a></p> 
<p style="text-align:left">QuickDAO的github地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsunyue1380%2FQuickDAO4" target="_blank">https://github.com/sunyue1380/QuickDAO4</a></p> 
<p style="text-align:left">QuickDAO的gitee地址: <a href="https://gitee.com/648823596/quickdao4" target="_blank">https://gitee.com/648823596/quickdao4</a></p>
                                        </div>
                                      
</div>
            