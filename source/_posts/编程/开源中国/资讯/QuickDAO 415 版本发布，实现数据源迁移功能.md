
---
title: 'QuickDAO 4.1.5 版本发布，实现数据源迁移功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7941'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 14:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7941'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">QuickDAO4.1.5版本已发布,可在maven中央仓库下载(阿里云仓库可能更新不及时),本次更新内容如下:</p> 
<ul> 
 <li>[新增]数据源迁移功能，可将数据记录从一个数据源迁移到另外一个数据源，支持跨数据源迁移（例如从SQLite迁移到MySQL）</li> 
 <li>[新增]添加addColumnExclude方法,用于返回部分字段，但该方法仅可调用一次</li> 
 <li>[修复]子查询生成查询语句时未添加上分页和排序信息</li> 
 <li>[修复]手动新增索引时，using字段前未添加using字符串问题</li> 
 <li>[优化]取消使用MDC保存日志，因框架中使用了MDC.clear()可能会和用户需求代码冲突</li> 
 <li>[优化]fastjson依赖升级至1.2.75</li> 
</ul> 
<p style="text-align:left">QuickDAO是一款简单易用的ORM框架,虽然市面上ORM框架已经非常多,但是有很多痛点这些框架并没有解决.QuickDAO相较于其他ORM框架的特点如下:</p> 
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
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Ftransaction%2Ftransaction" target="_blank">虚拟查询文档</a></p> 
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
            