
---
title: 'QuickDAO 4.1.10 版本发布，支持自定义适配数据库类型'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3435'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 15:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3435'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO4.1.10 版本已发布,可在maven中央仓库下载(阿里云仓库可能更新不及时),本次更新内容如下:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">友情提示:每次更新版本时通常在线文档也会同步更新.请注意查看文档页面时清空缓存,以便获取最新文档</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[新增]自定义数据提供者功能，可以自主适配例如clickhouse,presto等数据库驱动程序</li> 
 <li>[新增]实现SQLite删除列功能</li> 
 <li>[优化]整合DAOUtil类关于数据库结构同步的方法成一个</li> 
 <li>[优化]解决调用or查询方法失败问题</li> 
 <li>[新增]DAOUtil添加对比数据库字段信息并生成SQL语句的功能</li> 
 <li>[修复]解决批量更新报错时无法打印SQL问题</li> 
</ul> 
<p>自定义适配数据库功能需要用户提供DatabaseProvider接口适配类即可。目前QuickDAO内置实现了MySQL,Oracle等数据库适配器。</p> 
<p>例如若用户需要适配clickhouse数据库，clickhouse数据库的语法同mysql类似，因此我们可以继承MySQLDatabaseProvider，然后修改关于获取表结构的SQL语句。样例代码如下：</p> 
<pre><strong>ClickHouseDDLBuilder.java</strong></pre> 
<pre><code class="language-java">import cn.schoolwow.quickdao.builder.ddl.MySQLDDLBuilder;
import cn.schoolwow.quickdao.domain.Entity;
import cn.schoolwow.quickdao.domain.Property;
import cn.schoolwow.quickdao.domain.QuickDAOConfig;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ClickHouseDDLBuilder extends MySQLDDLBuilder &#123;

    public ClickHouseDDLBuilder(QuickDAOConfig quickDAOConfig) &#123;
        super(quickDAOConfig);
    &#125;

    @Override
    public String hasIndexExists(String tableName, String indexName) &#123;
        throw new UnsupportedOperationException("不支持的的操作");
    &#125;

    @Override
    public String dropIndex(String tableName, String indexName) &#123;
        throw new UnsupportedOperationException("不支持的的操作");
    &#125;

    @Override
    protected void getIndex(List<Entity> entityList) throws SQLException &#123;

    &#125;

    @Override
    protected void getEntityPropertyList(List<Entity> entityList) throws SQLException &#123;
        String getEntityPropertyListSQL = "select name,table from system.columns";
        ResultSet resultSet = connectionExecutor.executeQuery("获取表字段信息",getEntityPropertyListSQL);
        while (resultSet.next()) &#123;
            for(Entity entity : entityList)&#123;
                if(!entity.tableName.equalsIgnoreCase(resultSet.getString("table")))&#123;
                    continue;
                &#125;
                //添加字段信息
                Property property = new Property();
                property.column = resultSet.getString("name");
                entity.properties.add(property);
                break;
            &#125;
        &#125;
        resultSet.close();
    &#125;

    @Override
    protected List<Entity> getEntityList() throws SQLException &#123;
        String getEntityListSQL = "show tables;";
        ResultSet resultSet = connectionExecutor.executeQuery("获取表列表",getEntityListSQL);

        List<Entity> entityList = new ArrayList<>();
        while (resultSet.next()) &#123;
            Entity entity = new Entity();
            entity.tableName = resultSet.getString(1);
            entityList.add(entity);
        &#125;
        resultSet.close();
        return entityList;
    &#125;
&#125;</code></pre> 
<pre><code class="language-java">QuickDAO.addDatabaseProvider(new MySQLDatabaseProvider() &#123;
            @Override
            public AbstractDDLBuilder getDDLBuilderInstance(QuickDAOConfig quickDAOConfig) &#123;
                return new ClickHouseDDLBuilder(quickDAOConfig);
            &#125;

            @Override
            public String name() &#123;
                return "clickhouse";
            &#125;
        &#125;);

        HikariDataSource hikariDataSource = new HikariDataSource();
        hikariDataSource.setDriverClassName("com.clickhouse.jdbc.ClickHouseDriver");
        hikariDataSource.setJdbcUrl("jdbc🇨🇭//127.0.0.1/ck?socket_timeout=120000");

        dao = QuickDAO.newInstance()
                .autoCreateTable(false)
                .autoCreateProperty(false)
                .dataSource(hikariDataSource)
                .build();</code></pre> 
<p>使用QuickDAO.addDatabaseProvider方法添加提供者即可。若有不理解的地方可参考内置的MySQLDatabaseProvider类等等。</p> 
<p> </p> 
<p>QuickDAO是一款简单易用的ORM框架,虽然市面上ORM框架已经非常多,但是有很多痛点这些框架并没有解决.QuickDAO相较于其他ORM框架的特点如下:</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">支持lambda表达式</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从版本4.1.4开始，查询API支持lambda查询</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2Flambda" target="_blank">lambda文档</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">支持外键关联操作</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">虽然很多ORM框架宣称支持外键查询,但无一例外最终形式仍然是让开发者手写SQL语句.QuickDAO在API设计层面上支持外键关联查询,真正的无需手写多表关联查询SQL语句.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2FjoinTable" target="_blank">外键关联查询文档</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">虚拟查询(无实体类查询)</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">常规的ORM框架都需要建立实体类，然后再根据实体类来查询。QuickDAO支持无实体类查询，不用事先建立实体类也能够事先对数据库的查询,修改和删除.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2Fvirtual" target="_blank">虚拟查询文档</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">事务操作</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO实现了事务功能,事务相关API提供了QuickDAO其他数据库操作一样便利的API,对于复杂的事务操作需求,QuickDAO也能够满足</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="http://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Ftransaction%2Ftransaction">事务操作文档</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">子查询支持</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO在API层面上支持子查询,您可以通过API直接拼接生成一个子查询SQL语句。这意味着即使是一些相当复杂的SQL语句，QuickDAO也能够轻松面对。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fselect%2Fsubquery" target="_blank">子查询文档</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">自定义数据库列类型,索引等</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO提供了实体注解，实体注解的类型丰富。通过实体注解，您可以定义数据库列的列名，列类型，列注释，表索引，非空，check约束等等等等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn%2F%23%2Fzh-cn%2Fconfig%2Fannotation" target="_blank">实体注解文档</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">最后,写这个框架的初衷是市面上已有的ORM框架不能解决开发中痛点.QuickDAO经过近2年的支持开发,目前已经迭代到4.X版本,也在个人项目,公司项目实际使用过.希望本人开发的QuickDAO框架能够为中国的开源事业贡献一份自己的力量.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO文档: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquickdao.schoolwow.cn" target="_blank">https://quickdao.schoolwow.cn</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO的github地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsunyue1380%2FQuickDAO4" target="_blank">https://github.com/sunyue1380/QuickDAO4</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickDAO的gitee地址: <a href="https://gitee.com/648823596/quickdao4" target="_blank">https://gitee.com/648823596/quickdao4</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            